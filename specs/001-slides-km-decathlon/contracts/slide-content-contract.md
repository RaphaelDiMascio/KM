# Contrat : contenu du deck et contrôle automatique

**Consommateurs** :
- `deck/build_deck.py` lit `deck/content.py`.
- `deck/check_deck.py` lit `output/KM_Decathlon_MIAGE_Conseil.pptx`.

**Interface CLI** :

```text
python deck/build_deck.py   → écrit output/KM_Decathlon_MIAGE_Conseil.pptx et output/notes_orateur.md, code 0
python deck/check_deck.py   → affiche un rapport C1..C10 (OK/ÉCHEC) et un tableau par slide ; code 0 si tout est OK, 1 sinon
```

## Règles vérifiées

| ID | Règle | Source |
|----|-------|--------|
| C1 | Exactement 14 slides : 13 de contenu et 1 « Questions et sources » ; format 16:9 (13,333 × 7,5 in) | FR-004 |
| C2 | Chaque slide a un titre non vide ; les titres des slides 1 à 13 correspondent à la trame FR-005 | FR-005 |
| C3 | ≤ 6 puces et ≤ 40 mots affichés hors titre, pied de page et numéro (slide 14 : sources exclues du compte) | FR-005, principe V |
| C4 | ≥ 4 slides contiennent un schéma en formes natives (≥ 4 formes hors zones de texte), dont l'iceberg, la frise, SECI et Ba | FR-010 |
| C5 | Les slides 4 à 12 citent ≥ 1 concept du cours (champ `concepts`) et toutes les références figurent sur la slide 14 | FR-007, principe II |
| C6 | Les mentions « Socialisation », « Externalisation », « Combinaison », « Internalisation » apparaissent sur la slide 9 ; « Ba » sur la slide 10 | FR-007 |
| C7 | Toute slide portant `hypothesis_flag` affiche le mot « Hypothèse » ; la slide 3 liste H1 à H6 | FR-003, SC-006 |
| C8 | Chaque slide a un texte orateur (dans `output/notes_orateur.md`, pas dans le `.pptx`) commençant par `[Orateur X – Prénom]`, conforme à la répartition A/B/C | FR-011 |
| C9 | Volume de notes par orateur entre 550 et 700 mots ; total ≤ 1 950 mots | FR-012, R9 |
| C10 | Les notes des slides 4, 8, 12 et 13 contiennent une phrase de transition nommant l'orateur suivant (ou annonçant les questions) | FR-013 |

## Contrat de mise en forme (non automatisé, vérifié dans le quickstart)

- Polices : Montserrat (titres) et Open Sans (texte).
- Couleurs : `#3643BA`, `#101F47`, `#FFFFFF`, `#F2F3F7`, accent `#FF6A13` uniquement.
- Le nom « Decathlon » n'apparaît en grand que sur la slide 1. Aucun logo.
- Pied de page discret : « MIAGE Conseil — KM Quechua » et numéro de slide.
- Aucune animation ni transition ; aucun SmartArt ; aucune image raster obligatoire.
