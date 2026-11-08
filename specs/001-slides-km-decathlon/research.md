# Phase 0 — Research: Contenu des slides KM (Decathlon / Quechua)

**Date**: 2026-11-08 | **Spec**: [spec.md](./spec.md)

## R1 — Méthode de production du fichier Google Slides

- **Decision**: générer un `.pptx` 16:9 avec **python-pptx 1.0.2** (déjà installé, Python 3.14),
  puis l'importer dans Google Slides (Fichier › Importer des diapositives, ou ouverture depuis
  Drive).
- **Rationale**: décision de l'équipe (constitution) ; python-pptx écrit des formes natives,
  des zones de texte et des **notes orateur**, qui sont conservées à l'import dans Google Slides.
- **Alternatives considered**: Google Apps Script (nécessite un compte et une exécution côté
  Google, moins reproductible localement) ; mise en forme manuelle (trop lente avant le
  2026-11-09).

## R2 — Compatibilité de l'import dans Google Slides

- **Decision**: n'utiliser que des formes automatiques simples (rectangles, rectangles arrondis,
  chevrons, triangles, ellipses, flèches, connecteurs droits), des zones de texte et des
  aplats de couleur. Pas de SmartArt, d'animations, de transitions, d'effets 3D, d'ombres
  complexes ni de polices embarquées.
- **Rationale**: ces éléments sont convertis fidèlement par Google Slides ; SmartArt et
  animations sont perdus ou rasterisés.
- **Alternatives considered**: images PNG générées pour les schémas (non éditables par l'équipe
  dans Google Slides, donc rejetées).

## R3 — Polices

- **Decision**: **Montserrat** (titres, gras) et **Open Sans** (corps), toutes deux des Google
  Fonts disponibles nativement dans Google Slides.
- **Rationale**: rendu identique après import, sans substitution ; lisibilité à distance.
- **Alternatives considered**: police propriétaire Decathlon (non disponible) ; Arial
  (disponible mais plus neutre).

## R4 — Charte visuelle inspirée de Decathlon

- **Decision**: bleu principal `#3643BA`, bleu nuit `#101F47` pour les titres et fonds de
  séparateurs, blanc `#FFFFFF`, gris clair `#F2F3F7` pour les cartes, accent orange `#FF6A13`
  (une seule couleur d'accent), texte `#1B1B1F`. Fond des slides de contenu clair.
- **Rationale**: identification immédiate du client sans reproduire son identité de marque ;
  contraste suffisant pour un vidéoprojecteur.
- **Alternatives considered**: charte Dauphine, charte neutre du cabinet (écartées en
  clarification).
- **Note**: le logo Decathlon n'est pas inséré (droits) ; le nom du client figure en texte sur
  la slide de titre.

## R5 — Faits vérifiés sur Decathlon et Quechua (sources : Wikipédia FR/EN, consultées le 2026-11-08)

| Fait | Statut |
|------|--------|
| Entreprise française de conception et distribution d'articles de sport, créée en 1976 par Michel Leclercq | Vérifié |
| Siège à Villeneuve-d'Ascq (Métropole européenne de Lille) | Vérifié |
| ~103 000 salariés (102 913, données 2025) ; présence dans ~82 pays | Vérifié |
| Production internationalisée dès 1988 (premier bureau de production en Asie) ; >1 000 sous-traitants, essentiellement en Asie | Vérifié |
| Decathlon a récemment ouvert des magasins au Vietnam | Vérifié |
| Quechua : marque montagne / randonnée créée en 1997, basée à Passy (Haute-Savoie), au pied du Mont-Blanc ; le site montagne regroupe ~400 personnes | Vérifié |
| Conception Quechua partiellement transférée au Vietnam | **Hypothèse** (fiction du sujet) |
| 40 ingénieurs conception / qualité, 15 à Hô Chi Minh-Ville, 18 mois | **Hypothèse** (clarification) |

- **Decision**: n'afficher comme faits réels que les lignes « Vérifié » ; tout le reste porte la
  mention « Hypothèse ».
- **Rationale**: constitution, principe III et SC-006.

## R6 — Concepts du cours à mobiliser (supports `KM1app.pdf`, `KM3app.pdf`, notes manuscrites)

| Concept | Source cours | Usage dans le deck |
|---------|--------------|--------------------|
| Approche technologique vs managériale et socio-technique | KM1 p.6–7, 32–36 | Slide 5 |
| Système à base de connaissances (Benchimol et al., 1986) | KM1 p.14 | Slide 10 (outil de la plateforme, en appui) |
| 3 postulats ; sense-giving / sense-reading ; Polanyi 1958 ; schémas d'interprétation ; commensurabilité forte/faible | KM1 p.18–24 | Slides 4–5, 9 |
| Savoirs (explicités) vs savoir-faire (tacites) ; Nelson et Winter 1982 | KM1 p.27–30 | Slide 4 |
| Finalité patrimoniale vs finalité d'innovation durable | KM1 p.35–36 | Slides 6 et 13 |
| Modèle SECI (Nonaka et Takeuchi, 1995) | KM1 p.38 ; KM3 p.7, 29 | Slide 9 |
| « Ba » (Nonaka et Konno, 1998) ; fonctionnement semi-ouvert SopIM (Grundstein, 1988) | KM1 p.39–40 | Slide 10 |
| KM = « Manager des activités qui créent et qui utilisent des connaissances » | KM1 p.42 | Slide 5 |
| Entreprise étendue (Grundstein et Rosenthal-Sabroux, 2009) | KM3 p.4 | Slide 6 (fournisseurs et partenaires asiatiques) |
| Axe de progrès connaissances privées/disséminées, formalisées/non formalisées (Grundstein, 1998) | KM3 p.7 | Slide 8 |
| 5 facettes de la capitalisation sur les connaissances cruciales (Grundstein, 1996) | KM3 p.8–9 | Slides 7, 8, 12 |
| Relations de « bonne intelligence » (4 critères) | KM3 p.11 ; notes cours 3 | Slide 11 |
| Phases d'un projet de KM (IIIA-GTM, 2000) : orientations stratégiques, pilotage opérationnel, déploiement | KM3 p.12–14 | Slide 12 (gouvernance) |
| Cas AXA : du fichier des incidents isolé à un espace collaboratif de pérennisation, réunions incidents, vocabulaire commun | KM3 p.16–32 | Slides 10 et 9 (analogie) |
| À ne pas reproduire : facteurs de stress (manque de moyens, isolement social, temps) | Notes cours 3 | Slide 11 |

- **Decision**: chaque slide 4–12 cite au moins un concept de ce tableau, avec sa référence
  (auteur, année) dans les notes orateur ou la slide de sources.

## R7 — Exigences de rendu issues du cours

- **Finding**: KM1 p.4 précise « Rendu : diapositives + commentaires », avec notation
  individuelle.
- **Decision**: les **notes orateur** constituent les « commentaires » rendus ; elles sont
  rédigées en texte complet (et non en simples mots-clés), et chaque membre porte une partie
  identifiable du discours.

## R8 — Calendrier des 18 mois (point ouvert de la clarification)

- **Decision** (hypothèse affichée) :
  - Phase 1 « Repérer et préserver » : M0–M3 ;
  - Phase 2 « Transférer (SECI) » : M3–M15, en 3 vagues successives par gamme Quechua :
    vague 1 = sacs à dos (pilote, M3–M7), vague 2 = tentes et bivouac (M7–M11),
    vague 3 = chaussures de randonnée (M11–M15) ;
  - Phase 3 « Ba France–Vietnam » : ouverte dès M3, permanente ;
  - Phase 4 « Actualiser et piloter » : transverse M0–M18, puis en continu.
- **Rationale**: transfert modulaire et progressif (on commence par la gamme la moins critique
  pour la sécurité), qui laisse le temps à la socialisation ; c'est cohérent avec l'objectif
  « zéro impact ».
- **Alternatives considered**: transfert en bloc (risque de rupture maximal) ; vagues par
  métier plutôt que par gamme (moins lisibles pour des cadres produit).

## R9 — Durée orale et volume des notes

- **Decision**: débit de référence ≈ 130 mots/min, soit **550 à 700 mots de notes par orateur**
  (≈ 4 min 15 à 5 min 20), total ≤ 1 950 mots (≈ 15 min).
- **Rationale**: permet un contrôle automatique du SC-004 avant la répétition chronométrée.
