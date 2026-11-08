---

description: "Tâches d'implémentation — deck KM Decathlon / Quechua (MIAGE Conseil)"
---

# Tasks: Contenu des slides KM et choix de l'entreprise (Decathlon / Quechua)

**Input**: documents de conception dans `specs/001-slides-km-decathlon/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md,
contracts/slide-content-contract.md, quickstart.md

**Tests**: pas de TDD demandé. La validation repose sur le script de contrôle
`deck/check_deck.py` (règles C1 à C10 du contrat), qui fait partie du plan. Chaque user story
active les règles qui la concernent.

**Organization**: les tâches sont regroupées par user story (US1 : cadrage, US2 : argumentaire
KM, US3 : oral à trois).

## Format: `[ID] [P?] [Story] Description`

- **[P]** : tâche parallélisable (fichier différent, sans dépendance sur une tâche inachevée).
- **[Story]** : US1, US2 ou US3.
- Chemins relatifs à la racine `C:\Projet\ecole\KM`.

## Références obligatoires pour l'implémenteur

- Trame et titres-phrases des slides 1 à 13 : tableau sous FR-005 dans `spec.md`, à recopier
  **mot pour mot** pour les titres.
- Faits réels autorisés : `research.md` R5 (lignes « Vérifié » uniquement). Concepts et
  références : R6. Calendrier : R8. Volume oral : R9.
- Charte : `research.md` R3 et R4.
  - Polices : Montserrat (titres), Open Sans (corps).
  - Couleurs : `#3643BA`, `#101F47`, `#FFFFFF`, `#F2F3F7`, accent `#FF6A13`, texte `#1B1B1F`.
- Entités et règles : `data-model.md`. Règles de contrôle : `contracts/slide-content-contract.md`.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: initialiser la structure du générateur.

- [X] T001 Créer les dossiers `deck/` et `output/`, ainsi qu'un fichier vide `deck/__init__.py`.
- [X] T002 [P] Vérifier que python-pptx 1.0.2 est disponible
  (`python -c "import pptx;print(pptx.__version__)"`). En cas d'absence, lancer
  `pip install python-pptx==1.0.2`. Consigner le résultat dans la tâche, aucun fichier n'est
  créé.
- [X] T003 [P] Créer `deck/theme.py` avec la charte de `research.md` R3 et R4 :
  - Les constantes de couleur `BLUE=#3643BA`, `NAVY=#101F47`, `WHITE=#FFFFFF`,
    `LIGHT=#F2F3F7`, `ORANGE=#FF6A13` et `TEXT=#1B1B1F`, en `RGBColor`.
  - Les polices `TITLE_FONT="Montserrat"` et `BODY_FONT="Open Sans"`.
  - Les tailles : titre 28 pt, corps 18 pt, légende de schéma 14 pt, pied de page 10 pt.
  - Les dimensions du format 16:9 (`SLIDE_W=Inches(13.333)`, `SLIDE_H=Inches(7.5)`), les marges
    (0,6 in) et la hauteur de la zone de titre (1,2 in).

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: modèle de contenu, moteur de rendu de base et contrôleur. Ce sont les prérequis de
toutes les stories.

**⚠️ CRITICAL**: aucune slide ne peut être rédigée ni générée avant la fin de cette phase.

- [X] T004 Créer `deck/content.py` avec les dataclasses du `data-model.md`.
  - `Speaker` :
    - `code` dans `"A"|"B"|"C"` ;
    - `name` ;
    - `slides`.
  - `Concept` : `key`, `label`, `reference`, `application`.
  - `Hypothesis` : `id`, `statement`, `rationale`, `used_on`.
  - `Phase` :
    - `index` de 1 à 4 ;
    - `name`, `months` ;
    - `actions` (« ≥ 2 ») ;
    - `actors` (« ≥ 1 ») ;
    - `deliverable_or_kpi` (« ≥ 1 ») ;
    - `slide`, `grundstein`.
  - `Slide` :
    - `number` de 1 à 14 ;
    - `title` (« ≤ 110 caractères ») ;
    - `layout` dans `title|bullets|two_columns|cards|diagram|closing` ;
    - `bullets` (« ≤ 6 éléments ») ;
    - `visual` dans `iceberg|timeline|seci|ba|risk_benefit|trust|kpi|None` ;
    - `visual_data: dict` ;
    - `concepts: list[str]` ;
    - `hypothesis_flag: bool` ;
    - `speaker` dans `A|B|C|ALL` ;
    - `notes: str` ;
    - `transition: str|None`.
  - Les constantes :
    - `SPEAKERS` : A = Raphaël [1, 2, 3, 4, 5, 13], B = Caupcine [6, 7, 8],
      C = Fares [9, 10, 11, 12].
    - `CONCEPTS`, `HYPOTHESES`, `PHASES`, `SOURCES` : listes vides à remplir.
    - `SLIDES` : 14 entrées squelettes. Les numéros, titres exacts de la spec, orateurs et
      layouts sont renseignés ; les puces, les visuels et les notes sont laissés vides.
- [X] T005 Créer `deck/build_deck.py`, le moteur de base.
  - Il crée la `Presentation()` en 16:9 avec `theme.SLIDE_W/H` et utilise le layout vierge (6).
  - Fonctions à écrire :
    - `add_title(slide, text)` : Montserrat gras 28 pt, couleur NAVY, avec un liseré orange
      sous le titre ;
    - `add_bullets(slide, items, box)` : Open Sans 18 pt, puce « • », couleur TEXT ;
    - `add_footer(slide, n)` : « MIAGE Conseil — KM Quechua » et le numéro, 10 pt, gris ;
    - `add_hypothesis_tag(slide)` : un rectangle arrondi orange « Hypothèse », en haut à
      droite ;
    - `set_notes(slide, text)` : écrit dans `slide.notes_slide.notes_text_frame`.
  - La boucle principale lit `content.SLIDES` dans l'ordre.
  - Le visuel est délégué à `visuals.draw(slide, s.visual, s.visual_data)` s'il est non nul.
  - Le fichier est écrit dans `output/KM_Decathlon_MIAGE_Conseil.pptx`.
  - Contraintes : aucune animation, aucune image, formes natives uniquement (R2).
- [X] T006 [P] Créer `deck/visuals.py` avec un dispatcher `draw(slide, kind, data)` et des
  helpers de formes natives :
  - `box(slide, x, y, w, h, text, fill, font_color, size, shape=MSO_SHAPE.ROUNDED_RECTANGLE)` ;
  - `arrow(slide, x1, y1, x2, y2)` (connecteur droit avec flèche) ;
  - `chevron(...)`.
  Chaque fonction de schéma lève `NotImplementedError` jusqu'à son implémentation dans les
  stories.
- [X] T007 [P] Créer `deck/check_deck.py`.
  - Il ouvre `output/KM_Decathlon_MIAGE_Conseil.pptx` avec python-pptx et importe
    `deck/content.py` pour les métadonnées (concepts, flags, orateurs).
  - Il calcule, pour chaque slide :
    - le titre (première zone de texte en haut) ;
    - les mots affichés, hors titre, pied de page et numéro ;
    - le nombre de puces ;
    - le nombre de formes non textuelles ;
    - le texte des notes.
  - Il implémente un registre de règles C1 à C10, conformément à
    `contracts/slide-content-contract.md`.
  - Il affiche « Cx OK/ÉCHEC + détail », puis un tableau par slide (n°, mots, puces, formes,
    mots de notes, orateur).
  - Il exécute `sys.exit(1)` si une règle échoue.
  - Il force l'encodage de sortie en UTF-8 avec `sys.stdout.reconfigure(encoding="utf-8")`.
- [X] T008 Lancer `python deck/build_deck.py`, puis `python deck/check_deck.py`.
  - Attendu : le `.pptx` de 14 slides est créé et C1 et C2 sont OK.
  - Les autres règles peuvent échouer à ce stade.

**Checkpoint**: le squelette du deck se génère et se contrôle.

---

## Phase 3: User Story 1 — Cadrer l'intervention et l'entreprise cliente (Priority: P1) 🎯 MVP

**Goal**: les slides 1 à 3 posent qui, à qui, pourquoi, le périmètre Quechua et les hypothèses
étiquetées.

**Independent Test**: générer le deck et ne montrer que les slides 1 à 3 à une personne
extérieure. Elle doit restituer le cabinet, le public, le motif « délocalisation partielle au
Vietnam sans impact » et au moins 3 hypothèses. `check_deck.py` doit montrer C3 et C7 OK pour
les slides 1 à 3.

- [X] T009 [US1] Remplir `HYPOTHESES` dans `deck/content.py` avec H1 à H6 (`data-model.md`).
  Pour chacune, renseigner une `rationale` d'une phrase et `used_on`.
  - H1 : périmètre conception produit et ingénierie qualité Quechua, la vision produit restant
    en France.
  - H2 : 40 ingénieurs conception et qualité en France.
  - H3 : une équipe de 15 personnes à Hô Chi Minh-Ville.
  - H4 : un transfert progressif sur 18 mois, en 3 vagues (sacs à dos, tentes, chaussures).
  - H5 : des contraintes de qualité, de délais et de sécurité produit.
  - H6 : MIAGE Conseil a audité Decathlon.
- [X] T010 [US1] Rédiger la slide 1 dans `deck/content.py`, avec le layout `title`.
  - Le titre-phrase est celui de la spec.
  - Le sous-titre contient « MIAGE Conseil — Proposition aux cadres conception & qualité
    Quechua (Decathlon) ».
  - On y ajoute les membres (Raphaël, Caupcine, Fares), « Master 2 MIAGE — Introduction au
    Knowledge Management — P.-E. Arduin » et la date 10/11/2026.
  - Le nom « Decathlon » n'apparaît en grand que sur cette slide, sans logo.
- [X] T011 [US1] Rédiger la slide 2 dans `deck/content.py`.
  - Layout `cards`, `visual="cards"` (rendu par T013), `hypothesis_flag=True`, au plus
    40 mots.
  - Elle comporte 4 cartes :
    - « Qui » : MIAGE Conseil, consultants depuis 5 ans, a audité Decathlon (H6) ;
    - « À qui » : cadres conception produit et qualité Quechua ;
    - « Pourquoi » : projet de délocalisation partielle au Vietnam ;
    - « Objectif » : zéro impact sur l'activité.
  - N'utiliser que des faits de `research.md` R5 marqués « Vérifié » ; toute autre donnée porte
    le tag « Hypothèse ».
- [X] T012 [US1] Rédiger la slide 3 dans `deck/content.py`.
  - Layout `bullets`, `hypothesis_flag=True`.
  - Elle liste H1 à H6 en au plus 6 puces et au plus 40 mots.
  - Elle comporte un bandeau « Hypothèses de travail — à valider avec vous ».
  - La note de bas de slide rappelle un fait vérifié : « Decathlon : conception française,
    production majoritairement en Asie depuis 1988 » (R5).
- [X] T013 [US1] Implémenter le rendu des layouts `title` (fond NAVY, titre blanc, liseré
  orange) et `cards` (2×2 ou 1×4 rectangles arrondis LIGHT avec un en-tête BLUE).
  - Dans `deck/build_deck.py` : les deux layouts.
  - Dans `deck/visuals.py` : la fonction `draw_cards(slide, data)`.
- [X] T014 [US1] Lancer le build puis le check.
  - Attendu pour les slides 1 à 3 : C3 OK (au plus 6 puces, au plus 40 mots) et C7 OK (tag
    « Hypothèse » sur les slides 2 et 3, H1 à H6 listées sur la slide 3).
  - Corriger `deck/content.py` en cas d'échec.

**Checkpoint**: le cadrage est complet et présentable seul.

---

## Phase 4: User Story 2 — Convaincre avec un argumentaire KM complet (Priority: P1)

**Goal**: les slides 4 à 13 et la slide 14 répondent à Quoi (4–5), Pourquoi (6) et Comment
(7–12), puis concluent sur un appel à l'action (13) et listent les sources (14). Chaque slide de
démarche relie un concept du cours à une action Quechua.

**Independent Test**: `check_deck.py` doit montrer C3, C4, C5, C6 et C7 OK. Une personne
extérieure doit pouvoir citer les 4 phases et résumer la proposition de valeur en une phrase
(SC-005).

### Données transverses

- [X] T015 [P] [US2] Remplir `CONCEPTS` dans `deck/content.py` avec au moins 10 entrées issues de
  `research.md` R6 (au moins 6 exigés par SC-002). Chaque entrée a un `label`, une `reference`
  (auteur, année) et une `application` Quechua en une phrase. Clés et références :
  - `postulats` ;
  - `polanyi` (Polanyi 1958) ;
  - `tacite_explicite` (Nonaka et Takeuchi 1995 ; Nelson et Winter 1982) ;
  - `sense_giving` (Tsuchiya 1993) ;
  - `socio_technique` ;
  - `definition_km` ;
  - `patrimoniale_innovation` ;
  - `entreprise_etendue` (Grundstein et Rosenthal-Sabroux 2009) ;
  - `grundstein_facettes` (Grundstein 1996) ;
  - `axe_progres` (Grundstein 1998) ;
  - `seci` (Nonaka et Takeuchi 1995) ;
  - `ba` (Nonaka et Konno 1998) ;
  - `semi_ouvert` (Grundstein 1988) ;
  - `bonne_intelligence` ;
  - `iiia_phases` (IIIA-GTM 2000) ;
  - `cas_axa`.
- [X] T016 [P] [US2] Remplir `PHASES` dans `deck/content.py` avec les 4 phases de
  `research.md` R8. Pour chaque phase : au moins 2 actions, au moins 1 acteur, au moins 1
  livrable ou KPI (FR-008), et les facettes Grundstein.
  - Phase 1 « Repérer et préserver », M0–M3, slide 8 : repérer, préserver.
  - Phase 2 « Transférer (SECI) », M3–M15 en 3 vagues, slide 9 : valoriser.
  - Phase 3 « Partager (Ba) », dès M3 et en permanence, slide 10 : valoriser.
  - Phase 4 « Actualiser et piloter », M0–M18 et au-delà, slide 12 : actualiser, manager.
- [X] T017 [P] [US2] Remplir `SOURCES` dans `deck/content.py`.
  - Supports du cours KM1 et KM3 (P.-E. Arduin, Université Paris Dauphine-PSL).
  - Toutes les `reference` de `CONCEPTS`.
  - « Decathlon », « Quechua » (Wikipédia, consultés le 08/11/2026).

### Schémas natifs (fichier `deck/visuals.py`, à faire dans l'ordre car un seul fichier)

- [X] T018 [US2] Implémenter `draw_iceberg(slide, data)` pour la slide 4.
  - Une ligne de flottaison horizontale BLUE.
  - Au-dessus : un triangle LIGHT « Explicite (savoirs) » avec 3 à 4 libellés courts.
  - En dessous : un trapèze NAVY « Tacite (savoir-faire) » avec 4 libellés en blanc.
  - La citation de Polanyi « Nous savons plus que nous ne pouvons dire » est en accent orange.
  - Au moins 4 formes natives.
- [X] T019 [US2] Implémenter `draw_timeline(slide, data)` pour la slide 7.
  - Une frise M0→M18 avec 4 chevrons ou barres BLUE positionnés selon les mois de `PHASES`.
  - Les 3 vagues de la phase 2 sont matérialisées par des pastilles orange.
  - La barre « Confiance » est transverse, en LIGHT.
  - Le tag « Hypothèse » indique le calendrier.
- [X] T020 [US2] Implémenter `draw_seci(slide, data)` pour la slide 9.
  - Une matrice 2×2 de rectangles arrondis :
    - S en haut à gauche, « tacite→tacite » ;
    - E en haut à droite ;
    - C en bas à droite ;
    - I en bas à gauche.
  - Des flèches courbes ou des connecteurs forment la spirale S→E→C→I.
  - Chaque case porte le libellé exact (« Socialisation », « Externalisation »,
    « Combinaison », « Internalisation ») et une action Quechua de 3 à 6 mots.
- [X] T021 [US2] Implémenter `draw_ba(slide, data)` pour la slide 10.
  - 2 ellipses qui se chevauchent : « France — Passy » et « Vietnam — Hô Chi Minh-Ville ».
  - L'intersection, en orange, est libellée « Ba ».
  - Elles sont entourées de 4 étiquettes : communauté de pratique, rituels (revue de cas
    qualité), plateforme collaborative bilingue, référents passeurs.
  - Une mention « semi-ouvert » est ajoutée.
- [X] T022 [US2] Implémenter `draw_risk_benefit` (slide 6), `draw_trust` (slide 11) et
  `draw_kpi` (slide 12).
  - `draw_risk_benefit` : 2 colonnes, « Sans KM » (risques, en-tête NAVY) et « Avec KM »
    (bénéfices, en-tête orange).
  - `draw_trust` : 4 cartes, une par critère de bonne intelligence, avec une bande « À éviter :
    manque de moyens · isolement · pression du temps ».
  - `draw_kpi` : 4 tuiles d'indicateurs et un mini-organigramme de gouvernance (sponsor →
    responsable KM → référents).

### Contenu des slides 4 à 14 (`deck/content.py`, séquentiel car un seul fichier)

Pour chaque slide :
- le titre est recopié de la spec ;
- au plus 6 puces et au plus 40 mots affichés, schéma compris ;
- `concepts` n'est pas vide pour les slides 4 à 12 ;
- `hypothesis_flag` vaut True si un chiffre hypothétique apparaît.

- [X] T023 [US2] Slide 4 (A) : layout `diagram`, `visual="iceberg"`,
  `concepts=["postulats","polanyi","tacite_explicite"]`.
  - Explicite : cahiers des charges, normes, protocoles de test.
  - Tacite : ressenti des tests terrain, compréhension des usages, arbitrages qualité,
    relation fournisseurs.
- [X] T024 [US2] Slide 5 (B) : layout `two_columns`,
  `concepts=["definition_km","postulats","sense_giving","socio_technique"]`.
  - Colonne gauche : la définition du KM (citation du cours) et les 3 postulats appliqués.
  - Colonne droite : « approche technologique seule » opposée à « approche socio-technique »,
    avec un point sur les schémas d'interprétation France/Vietnam (FR-009).
- [X] T025 [US2] Slide 6 (B) : `visual="risk_benefit"`,
  `concepts=["grundstein_facettes","patrimoniale_innovation","entreprise_etendue"]`.
  - Risques : défauts qualité, retards de mise en marché, perte de connaissances cruciales,
    rupture du lien usage–conception.
  - Bénéfices : continuité, montée en compétence de l'équipe Vietnam, capitalisation pour
    innover.
- [X] T026 [US2] Slide 7 (B) : `visual="timeline"`, `hypothesis_flag=True`,
  `concepts=["grundstein_facettes","iiia_phases"]`.
  - Les 4 phases et leurs mois, issus de `PHASES`.
- [X] T027 [US2] Slide 8 (B) : layout `bullets`,
  `concepts=["grundstein_facettes","axe_progres","seci"]` (externalisation).
  - Cartographie des connaissances cruciales selon les critères rareté, difficulté
    d'acquisition et impact.
  - Entretiens et récits d'experts, vidéos des tests terrain, référentiel conception et qualité.
  - Livrable : la carte des connaissances cruciales.
- [X] T028 [US2] Slide 9 (C) : `visual="seci"`, `hypothesis_flag=True` (vagues),
  `concepts=["seci","cas_axa"]`.
  - S : binômes France–Vietnam, immersions croisées à Passy, tests terrain partagés.
  - E : retours d'expérience formalisés.
  - C : base de connaissances bilingue et revues de conception communes.
  - I : pratique encadrée et transfert par gamme.
- [X] T029 [US2] Slide 10 (C) : `visual="ba"`, `concepts=["ba","semi_ouvert","cas_axa"]`.
  - Espace physique et virtuel, communauté de pratique, revue de cas qualité mensuelle.
  - Plateforme collaborative, référents passeurs biculturels, glossaire commun France/Vietnam
    (FR-009, analogie avec le vocabulaire AXA).
- [X] T030 [US2] Slide 11 (C) : `visual="trust"`,
  `concepts=["bonne_intelligence","socio_technique"]`.
  - Les critères : respect, complémentarité, réciprocité, transparence des décisions.
  - Facteurs à éviter : manque de moyens, isolement social, pression du temps.
  - Sécuriser les experts français (reconnaissance du rôle de mentor) pour éviter la rétention.
- [X] T031 [US2] Slide 12 (C) : `visual="kpi"`, `hypothesis_flag=True`,
  `concepts=["grundstein_facettes","iiia_phases"]`.
  - Gouvernance : sponsor, responsable KM, référents.
  - Indicateurs : % de connaissances cruciales formalisées, autonomie de l'équipe Vietnam,
    taux de défauts, délais de mise en marché.
  - Mise à jour continue.
- [X] T032 [US2] Slide 13 (A) : layout `closing`.
  - Une synthèse en 3 blocs :
    - Quoi : transférer des connaissances, pas des tâches ;
    - Pourquoi : zéro impact ;
    - Comment : 4 phases.
  - Un appel à l'action en accent orange : « Pilote sur la gamme sacs à dos — lancement en
    janvier 2027 (hypothèse) ».
- [X] T033 [US2] Slide 14 (ALL) : layout `closing`.
  - « Merci — Questions ? » et la liste `SOURCES` en 12 pt, exclue du compte de mots par C3.
- [X] T034 [US2] Implémenter les layouts `two_columns` et `closing` dans `deck/build_deck.py`.
  - `closing` : 3 cartes de synthèse et un bandeau orange d'appel à l'action ; pour la slide
    14, un titre centré et les sources en petit.
- [X] T035 [US2] Lancer le build puis le check.
  - Attendu : C3, C4 (au moins 4 schémas, dont iceberg, timeline, seci et ba), C5, C6 et C7
    OK.
  - Corriger `deck/content.py` ou `deck/visuals.py` jusqu'à ce que tout passe.

**Checkpoint**: l'argumentaire est complet, les 14 slides sont lisibles et sans notes
rédigées.

---

## Phase 5: User Story 3 — Présenter à trois de façon équilibrée (Priority: P2)

**Goal**: des notes orateur complètes sur les 14 slides, environ 5 min par orateur et des
transitions entre orateurs.

**Independent Test**: `check_deck.py` doit montrer C8, C9 et C10 OK, entre 550 et 700 mots par
orateur. Lecture chronométrée de `output/notes_orateur.md` : chaque orateur entre 4 et 6 min,
total au plus 15 min.

- [X] T036 [P] [US3] Rédiger les `notes` des slides 1, 2, 3, 4 et 13 (Raphaël) dans
  `deck/content.py`, en environ 600 mots au total.
  - Chaque note commence par `[Orateur A – Raphaël]`.
  - Le texte est rédigé (phrases complètes, ton de consultant face à des cadres) et justifie le
    choix de Decathlon et de Quechua (FR-002).
  - La slide 4 se termine par une transition vers Caupcine (« Caupcine va vous montrer ce
    qu'est le KM… »).
  - La slide 13 se termine par l'annonce des questions.
  - Au moins un passage est marqué « (coupable) ».
- [X] T037 [P] [US3] Rédiger les `notes` des slides 5 à 8 (Caupcine) dans `deck/content.py`, en
  environ 600 mots.
  - Chaque note commence par `[Orateur B – Caupcine]`.
  - Les concepts sont cités avec auteur et année.
  - La slide 8 se termine par une transition vers Fares.
  - Au moins un passage est marqué « (coupable) ».
- [X] T038 [P] [US3] Rédiger les `notes` des slides 9 à 12 (Fares) dans `deck/content.py`, en
  environ 600 mots.
  - Chaque note commence par `[Orateur C – Fares]`.
  - La slide 12 se termine par une transition vers Raphaël pour la conclusion.
  - Au moins un passage est marqué « (coupable) ».
- [X] T039 [US3] Rédiger les `notes` de la slide 14 (`[Tous]`) dans `deck/content.py` : la
  répartition des questions probables par orateur.
- [X] T040 [US3] Ajouter dans `deck/build_deck.py` l'export de `output/notes_orateur.md`.
  - Il est organisé par orateur, puis par slide, avec le titre et les notes.
  - Il affiche le nombre de mots et la durée estimée à 130 mots/min par slide et par orateur.
- [X] T041 [US3] Lancer le build puis le check.
  - Attendu : C8 (en-têtes `[Orateur X – Prénom]` conformes à la répartition), C9 (550 à 700
    mots par orateur, au plus 1 950 au total) et C10 (transitions sur les slides 4, 8, 12 et
    13) OK.
  - Ajuster les notes en cas d'échec.

**Checkpoint**: le deck est complet, avec des notes prêtes pour la répétition.

---

## Phase 6: Polish & Cross-Cutting Concerns

- [X] T042 Lancer `python deck/build_deck.py` puis `python deck/check_deck.py`. Attendu : C1 à
  C10 tous OK et un code retour de 0.
- [X] T043 [P] Produire un aperçu visuel pour repérer les débordements de texte.
  - Si LibreOffice est disponible :
    `soffice --headless --convert-to pdf output/KM_Decathlon_MIAGE_Conseil.pptx --outdir output`.
  - Sinon, inspecter les dimensions des zones de texte avec un contrôle heuristique dans
    `deck/check_deck.py` (avertissement si le nombre de caractères par zone est trop élevé pour
    la taille de police).
  - Corriger les débordements.
- [X] T044 [P] Relire chaque fait réel cité dans `deck/content.py` en le comparant à
  `research.md` R5 (SC-006).
  - Aucune mention de production Decathlon au Vietnam présentée comme un fait.
  - Aucun sujet polémique sur les fournisseurs.
- [X] T045 Mettre à jour `specs/001-slides-km-decathlon/checklists/requirements.md` ou y ajouter
  une note de vérification finale (SC-001 à SC-006, avec le statut de chacun).
- [ ] T046 Exécuter le parcours manuel de `quickstart.md` (étapes 3 à 5), avec l'équipe.
  - Importer dans Google Slides.
  - Faire la relecture croisée.
  - Faire la répétition chronométrée.
  - Rappel : envoi avant le 2026-11-09.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)** : aucune dépendance.
- **Foundational (Phase 2)** : dépend de la phase 1 et bloque toutes les stories.
- **US1 (Phase 3)** : dépend de la phase 2. C'est le MVP.
- **US2 (Phase 4)** : dépend de la phase 2.
  - Elle est indépendante de US1 côté contenu.
  - Elle partage `deck/content.py`, donc l'édition est séquentielle avec US1 si une seule
    personne s'en charge.
- **US3 (Phase 5)** : dépend du contenu des slides (US1 et US2), car les notes commentent les
  slides affichées.
- **Polish (Phase 6)** : dépend de US1, US2 et US3.

### Within Each Story

- Données (hypothèses, concepts, phases) → schémas (`visuals.py`) → contenu des slides
  (`content.py`) → layouts (`build_deck.py`) → build et check.

### Parallel Opportunities

- T002 ∥ T003 (phase 1) ; T006 ∥ T007 (phase 2).
- T015 ∥ T016 ∥ T017 : blocs de données distincts. Ils sont dans le même fichier mais dans des
  sections indépendantes ; les fusionner avec soin.
- Les schémas T018 à T022 (`visuals.py`) peuvent avancer en parallèle de la rédaction T023 à
  T033 (`content.py`).
- T036 ∥ T037 ∥ T038 : chaque orateur rédige ses propres notes. C'est la répartition naturelle
  du groupe.

---

## Parallel Example: User Story 3

```text
Raphaël  : T036 — notes des slides 1–5 et 13 dans deck/content.py
Caupcine : T037 — notes des slides 6–8 dans deck/content.py
Fares    : T038 — notes des slides 9–12 dans deck/content.py
→ puis T040–T041 (export et contrôle C8–C10)
```

## Parallel Example: User Story 2

```text
Flux A (mise en forme) : T018 → T019 → T020 → T021 → T022 dans deck/visuals.py
Flux B (contenu)       : T015 ∥ T016 ∥ T017, puis T023 → … → T033 dans deck/content.py
→ jonction : T034 puis T035
```

---

## Implementation Strategy

### MVP First (User Story 1)

1. Phases 1 et 2 : squelette générable et contrôlable.
2. Phase 3 (US1) : slides de cadrage 1 à 3 complètes.
3. **STOP & VALIDATE** : check C3 et C7 sur les slides 1 à 3, puis montrer le cadrage à une
   personne extérieure.

### Incremental Delivery

1. Ajouter US2 : l'argumentaire et les schémas forment un deck lisible sans notes.
2. Ajouter US3 : les notes et l'équilibre de l'oral rendent le deck prêt pour la répétition.
3. Polish : validations finales, import dans Google Slides, envoi le 2026-11-09.

---

## Notes

- Ne jamais présenter comme un fait une donnée absente de `research.md` R5.
- Les titres des slides 1 à 13 viennent de la spec ; toute modification impose de mettre à jour
  `spec.md`.
- Le dossier n'est pas un dépôt git : sauvegarder `deck/content.py` avant les grosses
  modifications.
