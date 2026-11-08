# Quickstart — Générer, vérifier et importer le deck

## Prérequis

- Python 3.14 et python-pptx 1.0.2. Pour vérifier : `python -c "import pptx;print(pptx.__version__)"`.
- Un compte Google (Drive / Slides) pour l'import.
- Dans PowerShell : `$env:PYTHONIOENCODING='utf-8'`, pour afficher correctement les accents.

## 1. Générer

```powershell
cd C:\Projet\ecole\KM
python deck\build_deck.py
```

**Attendu** : les fichiers `output\KM_Decathlon_MIAGE_Conseil.pptx` et
`output\notes_orateur.md` sont créés.

## 2. Vérifier automatiquement

```powershell
python deck\check_deck.py
```

**Attendu** : C1 à C10 sont tous OK et le code retour vaut 0. Les règles sont décrites dans
[contracts/slide-content-contract.md](./contracts/slide-content-contract.md).

En cas d'échec, corriger `deck\content.py`, puis relancer les étapes 1 et 2.

## 3. Importer dans Google Slides

Deux méthodes possibles :
- Déposer le `.pptx` dans Drive, puis faire Ouvrir avec › Google Slides › Fichier ›
  Enregistrer au format Google Slides.
- Ou, dans une présentation vide : Fichier › Importer des diapositives › Importer tout.

**Contrôle visuel attendu** :
- 14 slides en 16:9.
- Polices Montserrat et Open Sans, sans substitution.
- Schémas (iceberg, frise, SECI, Ba) intacts et éditables.
- Aucun texte qui déborde.
- Aucune note dans le `.pptx` : le texte orateur est dans `output/notes_orateur.md`.

## 4. Relecture croisée (principes I et IV)

Chaque membre relit les slides d'un autre membre et vérifie que :
- les 3 questions de l'énoncé et le contexte du complément n°06 (Vietnam, pérenniser et
  partager) sont traités ;
- les titres-phrases parlent aux cadres opérationnels ;
- tous les faits réels sur Decathlon correspondent à la liste « Vérifié » de
  [research.md](./research.md) (R5).

## 5. Répétition chronométrée

- Lire les notes de `output\notes_orateur.md` en mode présentateur.
- **Attendu** : 15 min ± 1 min au total ; environ 5 min par orateur (A : Raphaël, B : Caupcine,
  C : Fares) ; transitions fluides.
- En cas de dépassement, couper en priorité les passages marqués « (coupable) » dans les notes.

## 6. Envoyer

Avant le **2026-11-09**, envoyer le lien Google Slides (droits de lecture) ou le `.pptx`
exporté à pierre-emmanuel.arduin@dauphine.psl.eu.
