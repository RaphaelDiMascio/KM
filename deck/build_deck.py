"""Génère output/KM_Decathlon_MIAGE_Conseil.pptx (sans notes) et le texte orateur
output/notes_orateur.md.

Usage (depuis la racine du projet) : python deck\\build_deck.py
"""
import re
import sys
from pathlib import Path

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches

import content as C
import theme as T
import visuals as V

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "output"
PPTX = OUT / "KM_Decathlon_MIAGE_Conseil.pptx"
NOTES_MD = OUT / "notes_orateur.md"
WPM = 130
FOOTER_TXT = "MIAGE Conseil — KM Quechua"


def words(s):
    return [w for w in s.split() if re.search(r"\w", w)]


def add_title(slide, title):
    V.text(slide, 0.6, 0.45, 12.1, 1.05, [title], name="TITLE", anchor=MSO_ANCHOR.MIDDLE,
           size=T.TITLE_SIZE, color=T.NAVY, font=T.TITLE_FONT, bold=True)
    V.box(slide, 0.6, 1.5, 1.2, 0.06, fill=T.ORANGE, shape=MSO_SHAPE.RECTANGLE, name="DECOR_title")


def add_footer(slide, number, total):
    V.text(slide, 0.6, 7.0, 8, 0.35, [FOOTER_TXT], name="FOOTER", size=T.FOOTER_SIZE, color=T.NAVY)
    V.text(slide, 11.9, 7.0, 0.8, 0.35, [f"{number} / {total}"], name="FOOTER_NUM",
           size=T.FOOTER_SIZE, color=T.NAVY, align=PP_ALIGN.RIGHT)


def add_hypo_tag(slide):
    V.box(slide, 11.15, 0.12, 1.55, 0.34, [V.head("Hypothèse", size=11)], fill=T.ORANGE,
          shape=MSO_SHAPE.RECTANGLE, name="HYPO_TAG")


def build_title_slide(slide, s):
    V.box(slide, 0, 0, T.SLIDE_W, T.SLIDE_H, fill=T.NAVY, shape=MSO_SHAPE.RECTANGLE, name="DECOR_bg")
    V.box(slide, 0.8, 2.0, 0.15, 2.2, fill=T.ORANGE, shape=MSO_SHAPE.RECTANGLE, name="DECOR_bar")
    V.text(slide, 1.2, 1.8, 11, 2.0, [s.title], name="TITLE", anchor=MSO_ANCHOR.MIDDLE,
           size=36, color=T.WHITE, font=T.TITLE_FONT, bold=True)
    d = s.visual_data
    V.text(slide, 1.2, 4.0, 11, 0.95, [d["subtitle"]], name="SUBTITLE", size=20, color=T.ORANGE,
           font=T.TITLE_FONT, bold=True)
    V.text(slide, 1.2, 5.1, 11, 0.5, [d["members"]], name="MEMBERS", size=18, color=T.WHITE)
    V.text(slide, 1.2, 6.4, 11, 0.5, [d["course"]], name="COURSE", size=14, color=T.WHITE)


def build_bullets(slide, s):
    w = 7.4 if s.visual == "side_card" else 11.7
    V.text(slide, T.CONTENT_LEFT, T.CONTENT_TOP + 0.05, w, T.CONTENT_BOTTOM - T.CONTENT_TOP,
           ["• " + b for b in s.bullets], name="BULLETS", size=20, color=T.TEXT, space_after=10)


def build(path=PPTX):
    prs = Presentation()
    prs.slide_width = Inches(T.SLIDE_W)
    prs.slide_height = Inches(T.SLIDE_H)
    blank = prs.slide_layouts[6]
    total = len(C.SLIDES)

    for s in C.SLIDES:
        slide = prs.slides.add_slide(blank)
        if s.layout == "title":
            build_title_slide(slide, s)
        else:
            add_title(slide, s.title)
            if s.bullets:
                build_bullets(slide, s)
            if s.visual:
                V.draw(slide, s.visual, s.visual_data)
            if s.hypothesis_flag:
                add_hypo_tag(slide)
            add_footer(slide, s.number, total)

    OUT.mkdir(exist_ok=True)
    prs.save(path)
    return path


def export_notes(path=NOTES_MD):
    lines = ["# Notes orateur — KM Quechua (MIAGE Conseil)", "",
             f"Débit de référence : {WPM} mots/min. « (coupable) » = phrase à sauter si retard.", ""]
    total = 0
    for code, sp in C.SPEAKERS.items():
        slides = [s for s in C.SLIDES if s.number in sp.slides]
        n = sum(len(words(s.notes + " " + (s.transition or ""))) for s in slides)
        total += n
        lines += [f"## Orateur {code} – {sp.name} — slides {', '.join(map(str, sp.slides))} "
                  f"— {n} mots ≈ {n / WPM:.1f} min", ""]
        for s in slides:
            lines += [f"### Slide {s.number} — {s.title}", "", s.notes.split("\n", 1)[1], ""]
            if s.transition:
                lines += [f"**→ Transition :** {s.transition}", ""]
    last = C.SLIDES[-1]
    lines += ["## Tous — slide 14 (questions)", "", last.notes.split("\n", 1)[1], "",
              f"**Total oral : {total} mots ≈ {total / WPM:.1f} min**", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path, total


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    p = build()
    md, total = export_notes()
    print(f"OK  {p}\nOK  {md}  ({total} mots ≈ {total / WPM:.1f} min)")
