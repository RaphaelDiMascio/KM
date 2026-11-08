# Implementation Plan: Contenu des slides KM et choix de l'entreprise (Decathlon / Quechua)

**Branch**: `001-slides-km-decathlon` | **Date**: 2026-11-08 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `specs/001-slides-km-decathlon/spec.md`

## Summary

Produire une présentation orale d'environ 15 minutes (13 slides de contenu et une slide
« Questions et sources »), au format 16:9, importable dans Google Slides. Le cabinet fictif
« MIAGE Conseil » y convainc les cadres opérationnels de la conception produit et de la qualité
Quechua (Decathlon) de mettre en place une démarche de KM. L'objectif est de pérenniser et de
partager les connaissances lors du transfert progressif, sur 18 mois, d'une partie de l'activité
vers Hô Chi Minh-Ville.

Approche technique :

- Le contenu (titres, puces, schémas, notes orateur) est rédigé dans un **module Python de
  données** (`deck/content.py`).
- Un générateur **python-pptx** (`deck/build_deck.py`) en produit un `.pptx` qui n'utilise que
  des formes natives éditables.
- Un script de contrôle (`deck/check_deck.py`) vérifie automatiquement les règles de la spec :
  nombre de slides, mots par slide, notes et orateurs, mention des hypothèses, volume oral.
- Le fichier est ensuite importé dans Google Slides et validé à la main.

## Technical Context

**Language/Version**: Python 3.14.8 (Windows)

**Primary Dependencies**: python-pptx 1.0.2 (déjà installé). Aucune dépendance supplémentaire :
PyYAML est absent, donc le contenu est stocké en Python.

**Storage**: fichiers locaux.
- `deck/content.py` (source du contenu).
- `output/KM_Decathlon_MIAGE_Conseil.pptx` (livrable).

**Testing**:
- `deck/check_deck.py` relit le `.pptx` généré et applique le contrat
  [contracts/slide-content-contract.md](./contracts/slide-content-contract.md).
- Contrôle visuel après import dans Google Slides.
- Répétition chronométrée.

**Target Platform**: Google Slides (navigateur), via l'import d'un `.pptx` 16:9.

**Project Type**: générateur de document (script unique) et livrable de présentation.

**Performance Goals**: oral de 15 min ± 1 min ; ≈ 5 min par orateur ; 550 à 700 mots de notes par
orateur (≈ 130 mots/min).

**Constraints**:
- Langue française.
- ≤ 6 puces et ≤ 40 mots affichés par slide (hors titre).
- ≥ 4 slides schématiques.
- Polices Google Fonts (Montserrat, Open Sans).
- Formes natives uniquement : pas de SmartArt, d'animations ni d'images de marque.
- Charte bleu / blanc / accent orange.
- Envoi par e-mail au plus tard le 2026-11-09, soutenance le 2026-11-10.

**Scale/Scope**: 14 slides (13 + Questions/sources), 3 orateurs, 1 fichier livrable.

Aucun point « NEEDS CLARIFICATION » : tous les points ouverts sont tranchés dans
[research.md](./research.md) (R1–R9).

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principe | Exigence | Comment le plan la respecte | Statut |
|----------|----------|-----------------------------|--------|
| I. Fidélité à l'énoncé et au complément | Répondre aux 3 questions ; contexte « délocalisation au Vietnam, pérenniser/partager » | Trame FR-005 : Quoi (4–5), Pourquoi (6), Comment (7–12). Le contrôle vérifie la présence des 3 questions dans la slide 13. | PASS |
| II. Ancrage dans la théorie du cours | Concepts du cours nommés et appliqués | Tableau R6 : chaque slide 4–12 porte un champ `concepts` non vide (contrat C5). Références en slide de sources. | PASS |
| III. Entreprise réaliste et hypothèses explicites | Faits vérifiés, hypothèses étiquetées | R5 sépare les faits vérifiés des hypothèses. La slide 3 est 100 % hypothèses ; le contrôle C7 exige le mot « Hypothèse » sur les slides 3, 7 et 8–12 qui citent des chiffres. | PASS |
| IV. Pitch persuasif pour managers opérationnels | Titres-phrases, bénéfices concrets, appel à l'action | Titres-phrases issus de la spec ; slide 6 sur les risques et bénéfices ; slide 13 propose un pilote daté. | PASS |
| V. Clarté visuelle et compatibilité Google Slides | ≤ 6 puces / 40 mots, schémas, rendu fidèle | R2–R4 ; contrat C2–C4 ; 4 schémas natifs (iceberg, frise, spirale SECI, Ba). | PASS |
| VI. Équilibre de l'équipe | ≈ 5 min chacun, transitions | Répartition A/B/C de la spec ; contrat C8–C9 (volume de notes par orateur, transitions). | PASS |

**Résultat** : aucune violation, la section Complexity Tracking est donc vide.

**Re-check post-design (Phase 1)**: PASS.
- Le data model et le contrat imposent mécaniquement les principes II, III, V et VI.
- Le quickstart couvre la vérification manuelle des principes I et IV (relecture croisée et
  répétition).

## Project Structure

### Documentation (this feature)

```text
specs/001-slides-km-decathlon/
├── spec.md
├── plan.md              # Ce fichier
├── research.md          # Phase 0
├── data-model.md        # Phase 1
├── quickstart.md        # Phase 1
├── contracts/
│   └── slide-content-contract.md
├── checklists/
│   └── requirements.md
└── tasks.md             # Phase 2 (/speckit-tasks)
```

### Source Code (repository root)

```text
deck/
├── content.py           # Données : SLIDES (14 entrées), HYPOTHESES, CONCEPTS, PHASES, SPEAKERS, SOURCES
├── theme.py             # Couleurs, polices, tailles, positions (charte R3–R4)
├── visuals.py           # Schémas en formes natives : iceberg, frise 4 phases, spirale SECI, Ba, cartes
├── build_deck.py        # Génère output/KM_Decathlon_MIAGE_Conseil.pptx
└── check_deck.py        # Vérifie le .pptx selon le contrat (C1–C10), code retour ≠ 0 en cas d'échec

output/
├── KM_Decathlon_MIAGE_Conseil.pptx   # Livrable importé dans Google Slides
└── notes_orateur.md                  # Export lisible des notes, pour la répétition
```

**Structure Decision**: un seul dossier `deck/` sépare le **contenu** (`content.py`, modifiable
par les 3 membres sans toucher au code) de la **mise en forme** (`theme.py`, `visuals.py`) et de
la **validation** (`check_deck.py`). Les sources du cours (`*.pdf`, `*.jpg`, `.docx`) restent à
la racine, en lecture seule.

**Phases de la démarche**: les noms utilisés dans la slide 7 sont alignés sur les slides 8–12 :
1. Repérer et préserver.
2. Transférer (SECI).
3. Partager (Ba).
4. Actualiser et piloter.

La confiance (slide 11) est traitée comme une condition transverse. Calendrier : voir R8.

## Complexity Tracking

Aucune violation de la constitution à justifier.
