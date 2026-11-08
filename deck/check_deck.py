"""Vérifie le deck généré contre contracts/slide-content-contract.md (C1–C10).

Usage (depuis la racine du projet) : python deck\\check_deck.py
Code retour 1 si une règle échoue. Les débordements de texte sont signalés en avertissement.
"""
import re
import sys
from pathlib import Path

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

import content as C

ROOT = Path(__file__).resolve().parent.parent
PPTX = ROOT / "output" / "KM_Decathlon_MIAGE_Conseil.pptx"
SPEC = ROOT / "specs" / "001-slides-km-decathlon" / "spec.md"
EXCLUDED = ("TITLE", "FOOTER", "HYPO_TAG", "DECOR", "SOURCES")
EMU_IN = 914400

failures, warnings = [], []


def words(s):
    return [w for w in s.split() if re.search(r"\w", w)]


def check(rule, ok, msg):
    if not ok:
        failures.append(f"{rule} : {msg}")


def shape_texts(slide):
    for shp in slide.shapes:
        if shp.has_text_frame and shp.text_frame.text.strip():
            yield shp


def displayed_text(slide):
    return "\n".join(s.text_frame.text for s in shape_texts(slide) if not s.name.startswith(EXCLUDED))


def all_text(slide):
    return "\n".join(s.text_frame.text for s in shape_texts(slide))


def notes_text(slide):
    """Texte orateur de la slide (porté par le .md, plus par le .pptx)."""
    s = C.SLIDES[slide - 1]
    return s.notes + (" " + s.transition if s.transition else "")


def spec_titles():
    rx = re.compile(r"^\|\s*(\d+)\s*\|\s*«\s*(.+?)\s*»\s*\|", re.M)
    return {int(n): t for n, t in rx.findall(SPEC.read_text(encoding="utf-8"))}


def overflow(slide, num):
    """Heuristique : lignes estimées × interligne vs hauteur de la zone."""
    for shp in shape_texts(slide):
        tf = shp.text_frame
        w = shp.width / EMU_IN - 0.2
        need = 0.1
        for p in tf.paragraphs:
            size = next((r.font.size.pt for r in p.runs if r.font.size), 18)
            cpl = max(1, int(w * 72 / (size * 0.52)))
            lines = max(1, -(-len(p.text) // cpl))
            need += lines * size * 1.25 / 72 + (p.space_after.pt / 72 if p.space_after else 0)
        h = shp.height / EMU_IN
        if need > h + 0.05:
            warnings.append(f"slide {num} « {shp.name} » : ~{need:.2f} in nécessaires pour {h:.2f} in")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    prs = Presentation(PPTX)
    slides = list(prs.slides)
    by_num = {s.number: s for s in C.SLIDES}

    # C1 — nombre de slides et format 16:9
    check("C1", len(slides) == 14, f"{len(slides)} slides au lieu de 14")
    check("C1", abs(prs.slide_width / prs.slide_height - 16 / 9) < 0.01, "format non 16:9")

    # C2 — titres conformes à la spec
    titles = spec_titles()
    check("C2", len(titles) == 13, f"{len(titles)} titres trouvés dans spec.md")
    for n, t in titles.items():
        shp = next((s for s in slides[n - 1].shapes if s.name == "TITLE"), None)
        got = shp.text_frame.text if shp else ""
        check("C2", got == t, f"slide {n} titre « {got} » ≠ spec « {t} »")

    for i, sl in enumerate(slides, 1):
        disp = displayed_text(sl)
        # C3 — lisibilité
        bullets = [p for s in shape_texts(sl) if not s.name.startswith(EXCLUDED)
                   for p in s.text_frame.paragraphs if p.text.lstrip().startswith("•")]
        check("C3", len(bullets) <= 6, f"slide {i} : {len(bullets)} puces (> 6)")
        nw = len(words(disp))
        check("C3", nw <= 40, f"slide {i} : {nw} mots affichés (> 40)")
        overflow(sl, i)

    # C4 — visuels
    kinds = {}
    for i, sl in enumerate(slides, 1):
        vis = [s for s in sl.shapes if s.name.startswith("VIS_") and s.shape_type != MSO_SHAPE_TYPE.TEXT_BOX]
        if len(vis) >= 4:
            kinds[i] = {s.name[4:].rsplit("_", 1)[0] for s in vis}
    check("C4", len(kinds) >= 4, f"{len(kinds)} slides avec schéma (≥ 4 attendues)")
    found = set().union(*kinds.values()) if kinds else set()
    for k in ("iceberg", "timeline", "seci", "ba"):
        check("C4", k in found, f"schéma « {k} » absent")

    # C5 — ancrage théorique
    sources_txt = all_text(slides[13])
    used = set()
    for n in range(4, 13):
        cs = by_num[n].concepts
        check("C5", bool(cs), f"slide {n} sans concept du cours")
        for k in cs:
            check("C5", k in C.CONCEPTS, f"slide {n} : concept inconnu « {k} »")
            used.add(k)
    for k in used:
        ref = C.CONCEPTS[k].reference if k in C.CONCEPTS else ""
        check("C5", ref in sources_txt, f"référence « {ref} » absente de la slide 14")
    check("C5", len(used) >= 6, f"{len(used)} concepts distincts (≥ 6 attendus)")

    # C6 — SECI et Ba nommés
    s9 = all_text(slides[8])
    for m in ("Socialisation", "Externalisation", "Combinaison", "Internalisation"):
        check("C6", m in s9, f"slide 9 : « {m} » absent")
    check("C6", "Ba" in all_text(slides[9]), "slide 10 : « Ba » absent")

    # C7 — hypothèses étiquetées
    for s in C.SLIDES:
        if s.hypothesis_flag:
            check("C7", "hypothèse" in all_text(slides[s.number - 1]).lower(),
                  f"slide {s.number} : étiquette hypothèse absente")
    s3 = all_text(slides[2])
    for h in C.HYPOTHESES:
        check("C7", h.id in s3, f"slide 3 : {h.id} absent")

    # C8 — en-têtes des notes
    for s in C.SLIDES:
        nt = notes_text(s.number)
        if s.speaker == "ALL":
            exp = "[Tous]"
        else:
            exp = f"[Orateur {s.speaker} – {C.SPEAKERS[s.speaker].name}]"
        check("C8", nt.startswith(exp), f"slide {s.number} : notes ne commencent pas par {exp}")

    # C9 — volume oral par orateur
    total = 0
    per = {}
    for code, sp in C.SPEAKERS.items():
        n = sum(len(words(notes_text(k).split("\n", 1)[-1])) for k in sp.slides)
        per[f"{code} {sp.name}"] = n
        total += n
        check("C9", 550 <= n <= 700, f"orateur {code} : {n} mots (attendu 550–700)")
    check("C9", total <= 1950, f"total {total} mots (> 1950)")

    # C10 — transitions
    for n, kw in ((5, "Caupcine"), (8, "Fares"), (12, "Raphaël"), (13, "questions")):
        check("C10", kw in notes_text(n), f"slide {n} : transition sans « {kw} »")

    print("Mots oraux par orateur :", ", ".join(f"{k} = {v}" for k, v in per.items()), f"| total = {total}")
    for i, sl in enumerate(slides, 1):
        print(f"  slide {i:>2} : {len(words(displayed_text(sl))):>2} mots affichés")
    for w in warnings:
        print("AVERTISSEMENT", w)
    if failures:
        for f in failures:
            print("ÉCHEC", f)
        print(f"\n{len(failures)} échec(s).")
        return 1
    print("\nC1–C10 : tout est conforme.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
