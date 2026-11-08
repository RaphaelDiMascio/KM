# Feature Specification: Contenu des slides KM et choix de l'entreprise (Decathlon)

**Feature Branch**: `001-slides-km-decathlon`

**Created**: 2026-11-08

**Status**: Draft

**Input**: User description: "on fait le contenu des slides et le choix de l'entreprise"

## Contexte et décision

- **Sujet** : consultants (5 ans) d'un petit cabinet de conseil, nous promouvons le Knowledge
  Management (KM) auprès des cadres opérationnels d'une grande entreprise récemment auditée par
  notre employeur. Complément n°06 : certains cadres envisagent de délocaliser une partie de leur
  activité au Vietnam ; cela ne doit pas impacter l'activité. Focus : **pérennisation et partage
  des connaissances**, et **comment nous nous y prendrions**.
- **Entreprise retenue (décision de l'équipe, 2026-11-08)** : **Decathlon**, grande entreprise
  française de conception et distribution d'articles de sport, avec ses marques propres
  (ex. Quechua, Kipsta, Btwin).
- **Activité envisagée pour la délocalisation (hypothèse)** : une partie de la **conception
  produit** (développement   technique, prototypage) et de l'**ingénierie qualité** de la marque
  **Quechua** (randonnée / camping), transférée vers une équipe basée au Vietnam, au plus près des sites de production
  partenaires. La création et la vision produit restent en France.
- **Pourquoi Decathlon** : entreprise connue du jury ; présence industrielle crédible au Vietnam ;
  savoir-faire fortement tacite (tests terrain, compréhension des usages sportifs, arbitrages
  qualité, relation fournisseurs) ; risque de perte de connaissances cruciales clairement
  illustrable ; application naturelle de SECI, Grundstein, du « Ba » et des critères de confiance.
- **Alternatives écartées** : Clairefontaine (contexte initial du docx), Groupe SEB, BNP Paribas,
  Orange, Sanofi, ainsi que des ETI 100 % françaises (Ligne Roset, Gautier, J.M. Weston,
  Saint James), écartées car l'énoncé impose une grande entreprise.

## Clarifications

### Session 2026-11-08

- Q: Quelle marque Decathlon sert d'exemple pour le périmètre délocalisé ? → A: Quechua
  (randonnée / camping).
- Q: Quel jeu d'hypothèses chiffrées afficher sur la slide 3 ? → A: 40 ingénieurs conception /
  qualité en France, future équipe de 15 à Hô Chi Minh-Ville, transfert progressif sur 18 mois.
- Q: Qui sont les orateurs A, B et C ? → A: A = Raphaël, B = Caupcine, C = Fares.
- Q: Quel nom donner au cabinet de conseil fictif ? → A: MIAGE Conseil.
- Q: Quelle identité visuelle donner aux slides ? → A: Couleurs inspirées de Decathlon (bleu,
  blanc, accent orange), client cité sobrement.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Cadrer l'intervention et l'entreprise cliente (Priority: P1)

Le jury (et, dans la fiction, les cadres opérationnels de Decathlon) comprend en moins de
3 minutes qui nous sommes, à qui nous nous adressons, pourquoi nous intervenons, quelle activité
serait délocalisée et quelles hypothèses nous posons.

**Why this priority**: l'énoncé exige explicitement ce cadrage et la déclinaison des hypothèses ;
sans lui, le reste de l'argumentaire n'a pas de point d'ancrage.

**Independent Test**: présenter uniquement les slides de cadrage à une personne extérieure ; elle
peut restituer « qui / à qui / pourquoi », le périmètre délocalisé et au moins 3 hypothèses.

**Acceptance Scenarios**:

1. **Given** les slides de cadrage, **When** un lecteur les parcourt, **Then** il identifie le
   cabinet, le public (cadres conception produit et qualité de Decathlon), le motif (projet de
   délocalisation partielle au Vietnam) et l'objectif « zéro impact sur l'activité ».
2. **Given** une information non fournie par le sujet (effectifs, calendrier, localisation),
   **When** elle apparaît, **Then** elle est explicitement étiquetée comme hypothèse.

---

### User Story 2 - Convaincre avec un argumentaire KM complet (Priority: P1)

Les cadres opérationnels voient, slide après slide, ce qu'est le KM, pourquoi il est indispensable
dans leur projet de délocalisation, et comment notre prestation sécurise concrètement la
pérennisation et le partage des connaissances entre la France et le Vietnam.

**Why this priority**: c'est le cœur de l'évaluation (3 questions de l'énoncé et complément n°06).

**Independent Test**: pour chacune des 3 questions (Quoi / Pourquoi / Comment), au moins une
slide y répond explicitement ; chaque slide de démarche cite au moins un concept du cours appliqué
au cas Decathlon.

**Acceptance Scenarios**:

1. **Given** la présentation complète, **When** on cherche la réponse à « Qu'est-ce que le KM ? »,
   **Then** on trouve les 3 postulats et la distinction tacite/explicite appliqués à Decathlon.
2. **Given** la partie « Comment », **When** on la lit, **Then** on y trouve une démarche phasée
   (phases, actions, rôles, calendrier, indicateurs) reliée à Grundstein, SECI, au « Ba » et aux
   4 critères de confiance.
3. **Given** la conclusion, **When** elle est présentée, **Then** elle formule un appel à l'action
   concret (prochaine étape proposée aux cadres).

---

### User Story 3 - Présenter à trois de façon équilibrée (Priority: P2)

Les trois membres du groupe disposent chacun d'environ 5 minutes de parole, avec des notes
orateur pour chaque slide et des transitions claires entre orateurs.

**Why this priority**: la soutenance est collective et chronométrée (~15 min), mais ce volet
dépend du contenu des slides (US1, US2).

**Independent Test**: lire les notes orateur à voix haute chronomètre en main : chaque orateur
parle entre 4 et 6 minutes et le total ne dépasse pas 15 minutes.

**Acceptance Scenarios**:

1. **Given** chaque slide, **When** on consulte ses notes, **Then** l'orateur (Raphaël, Caupcine ou Fares) et
   le texte à dire y figurent.
2. **Given** un changement d'orateur, **When** il survient, **Then** une phrase de transition
   l'annonce.

---

### Edge Cases

- Le jury conteste la crédibilité d'un chiffre sur Decathlon : tout chiffre non vérifié est
  présenté comme hypothèse ou ordre de grandeur sourcé.
- Le jury demande « pourquoi ne pas tout simplement documenter ? » : l'argumentaire distingue
  explicitement tacite et explicite (Polanyi) et montre les limites d'une approche purement
  technologique.
- Le jury demande comment éviter la rétention de connaissances par les experts français qui
  craignent pour leur poste : la slide confiance traite ce risque (critères de bonne
  intelligence, transparence des décisions, absence de stress lié aux moyens, à l'isolement social
  et au temps).
- La présentation dépasse 15 min en répétition : des slides ou passages « coupables » sont
  identifiés dans les notes.
- Différences culturelles et linguistiques France–Vietnam (schémas d'interprétation) : traitées
  explicitement, sans stéréotypes.

## Requirements *(mandatory)*

### Functional Requirements

**Choix de l'entreprise**

- **FR-001**: La présentation MUST retenir Decathlon comme entreprise cliente, avec pour périmètre
  hypothétique la délocalisation au Vietnam d'une partie de la conception produit (développement
  technique, prototypage) et de l'ingénierie qualité de la marque Quechua (randonnée / camping).
- **FR-002**: La présentation MUST justifier ce choix en une phrase (savoir-faire tacite critique,
  crédibilité d'une implantation au Vietnam).
- **FR-003**: Tout fait présenté comme réel sur Decathlon MUST être exact et vérifié avant
  l'envoi ; toute donnée non vérifiée MUST être présentée comme hypothèse.

**Structure et contenu des slides**

- **FR-004**: La présentation MUST compter entre 10 et 15 slides (hors slide de questions et de
  sources), au format 16:9.
- **FR-005**: La présentation MUST suivre la trame ci-dessous ; chaque slide MUST avoir un
  titre-phrase porteur du message clé et au plus ~6 puces / ~40 mots affichés.

| # | Slide (titre-phrase indicatif) | Contenu attendu | Concepts du cours | Orateur |
|---|--------------------------------|-----------------|-------------------|---------|
| 1 | « Délocaliser sans oublier : pérenniser le savoir-faire Decathlon entre la France et le Vietnam » | Titre, nom du cabinet (MIAGE Conseil), membres (Raphaël, Caupcine, Fares), cours, date | — | A |
| 2 | « Qui sommes-nous, à qui parlons-nous, pourquoi ? » | Cabinet de conseil MIAGE Conseil (5 ans, a audité Decathlon) ; public : cadres opérationnels conception produit et qualité ; motif : projet de délocalisation partielle au Vietnam ; objectif : zéro impact sur l'activité | Contexte d'intervention (énoncé) | A |
| 3 | « Nos hypothèses de travail » | Marque Quechua ; 40 ingénieurs conception / qualité en France, future équipe de 15 à Hô Chi Minh-Ville ; transfert progressif sur 18 mois ; contraintes (qualité, délais, sécurité produit) — tous étiquetés hypothèses | Exigence de l'énoncé | A |
| 4 | « Ce qui part au Vietnam, ce ne sont pas des tâches, ce sont des connaissances » | Iceberg : explicite (cahiers des charges, normes, protocoles de test) vs tacite (gestes et ressentis des tests terrain, compréhension des usages sportifs, arbitrages qualité, relation fournisseurs) | Postulat 3, Polanyi « We know more than we can tell » | A |
| 5 | « Le KM : manager les activités qui créent et utilisent des connaissances » | Définition du KM ; 3 postulats appliqués : connaissance = interprétation (sense-giving / sense-reading, schémas d'interprétation FR/VN différents), connaissance liée à l'action, tacite/explicite ; approche socio-technique vs technologique | 3 postulats, définition KM, approches | A |
| 6 | « Sans KM, la délocalisation met en danger qualité, délais et innovation » | Risques : défauts qualité, retards de mise en marché, perte de connaissances cruciales (départ ou démotivation des experts), rupture du lien usage–conception ; bénéfices : continuité, montée en compétence, capitalisation pour innover | Connaissances cruciales | B |
| 7 | « Notre démarche en 4 phases » | Vue d'ensemble : Repérer → Préserver → Transférer et partager → Actualiser et piloter, avec calendrier indicatif | 5 facettes de Grundstein | B |
| 8 | « Phase 1 — Repérer et préserver les connaissances cruciales » | Cartographie des connaissances cruciales (critères : rareté, difficulté d'acquisition, impact sur l'activité) ; entretiens et récits d'experts ; vidéos de tests terrain ; référentiel de conception et de qualité | Grundstein (repérer, préserver) ; SECI – Externalisation | B |
| 9 | « Phase 2 — Transférer en faisant tourner la spirale SECI » | Socialisation (binômes FR–VN, immersions croisées, tests terrain partagés) ; Externalisation (retours d'expérience formalisés) ; Combinaison (base de connaissances bilingue, revues de conception communes) ; Internalisation (pratique encadrée, transfert progressif par gamme de produits) | Modèle SECI | C |
| 10 | « Phase 3 — Créer un "Ba" France–Vietnam pour partager durablement » | Espace physique et virtuel : communauté de pratique, rituels (revue de cas qualité), plateforme collaborative, fonctionnement semi-ouvert, référents passeurs biculturels | Concept de « Ba », fonctionnement semi-ouvert | C |
| 11 | « Pas de partage sans confiance » | 4 critères de bonne intelligence appliqués (respect, complémentarité, réciprocité, transparence des décisions) ; éviter les facteurs de stress (manque de moyens, isolement social, pression du temps) ; sécuriser les experts français pour éviter la rétention | Approche socio-technique, confiance | C |
| 12 | « Phase 4 — Actualiser et piloter dans la durée » | Gouvernance (sponsor, responsable KM, référents) ; indicateurs (part des connaissances cruciales formalisées, autonomie de l'équipe Vietnam, taux de défauts, délais) ; mise à jour continue | Grundstein (actualiser, valoriser, manager) | C |
| 13 | « Délocaliser, c'est transférer des connaissances : lançons un pilote » | Synthèse Quoi / Pourquoi / Comment ; appel à l'action : pilote sur une gamme de produits, prochaine étape datée | Synthèse | A |
| — | « Questions » + sources | Remerciements, références (supports de cours, sources sur Decathlon) | — | Tous |

- **FR-006**: La présentation MUST répondre explicitement aux 3 questions de l'énoncé :
  « Qu'est-ce que le KM ? » (slides 4–5), « Pourquoi le promouvoir ? » (slide 6),
  « Comment le mettre en œuvre ? » (slides 7–12).
- **FR-007**: Chaque slide de démarche (7–12) MUST relier au moins un concept du cours à une
  action concrète du cas Decathlon.
- **FR-008**: La démarche MUST préciser, pour chaque phase, les actions, les acteurs, la durée
  indicative et au moins un livrable ou un indicateur.
- **FR-009**: La présentation MUST traiter les différences de schémas d'interprétation entre
  équipes française et vietnamienne (risque de mauvais sense-reading) et proposer au moins un
  dispositif pour les réduire.
- **FR-010**: Au moins 4 slides MUST être construites autour d'un schéma (ex. iceberg, frise des
  4 phases, spirale SECI, schéma du Ba) plutôt que du texte seul.
- **FR-010a**: Toutes les slides MUST suivre une même charte inspirée de Decathlon : fond clair,
  bleu dominant, blanc, une seule couleur d'accent orange ; le nom ou logo du client apparaît
  au plus sur la slide de titre et de manière sobre.

**Notes orateur et répartition**

- **FR-011**: Chaque slide MUST avoir un texte orateur, fourni dans un document Markdown séparé
  (`output/notes_orateur.md`, pas de notes dans les slides), indiquant l'orateur (A = Raphaël,
  B = Caupcine, C = Fares) et
  le texte ou les points clés à dire.
- **FR-012**: La répartition MUST donner environ 5 minutes à chaque orateur (A : slides 1–5 et 13,
  B : slides 6–8, C : slides 9–12), pour un total d'environ 15 minutes.
- **FR-013**: Les notes MUST contenir une phrase de transition à chaque changement d'orateur.

### Key Entities

- **Slide** : numéro, titre-phrase, contenu affiché, visuel éventuel, concept(s) du cours,
  orateur, notes orateur.
- **Hypothèse** : énoncé, justification ; affichée sur la slide 3 ou signalée là où elle sert.
- **Concept du cours** : nom (SECI, Grundstein, Ba, postulats, confiance…), définition courte,
  application au cas.
- **Phase de la démarche** : nom, objectifs, actions, acteurs, durée, livrables / indicateurs.
- **Orateur** : A = Raphaël, B = Caupcine, C = Fares ; slides attribuées, durée cible.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100 % des éléments exigés par l'énoncé sont couverts : cadrage qui / à qui /
  pourquoi, 3 questions, focus pérennisation et partage, hypothèses explicites.
- **SC-002**: Au moins 6 concepts distincts du cours sont mobilisés et chacun est appliqué au cas
  Decathlon sur au moins une slide.
- **SC-003**: La présentation compte entre 10 et 15 slides de contenu, et aucune ne dépasse
  ~40 mots affichés.
- **SC-004**: En répétition chronométrée, le total est ≤ 15 minutes et chaque orateur parle entre
  4 et 6 minutes.
- **SC-005**: Une personne extérieure au groupe, après une lecture unique, peut résumer en une
  phrase la proposition de valeur et citer les 4 phases de la démarche.
- **SC-006**: 0 fait inexact présenté comme réel ; toutes les données non vérifiées sont
  étiquetées « hypothèse ».

## Assumptions

- Le cabinet de conseil est fictif et s'appelle « MIAGE Conseil ».
- Les hypothèses chiffrées (40 ingénieurs en France, 15 à Hô Chi Minh-Ville, 18 mois) sont
  affichées comme telles ; la répartition des 18 mois entre les 4 phases est fixée lors de la
  rédaction.
- La présentation est en français et sera produite sous forme de fichier importable dans
  Google Slides (contraintes de format portées par la constitution).
- Les supports de cours (`KM1app.pdf`, `KM3app.pdf`, notes manuscrites) sont la référence
  théorique ; les rappels théoriques du docx peuvent être réutilisés, mais pas son contexte
  Clairefontaine.
- Hors périmètre : préparation de questions-réponses pour le jury, document écrit
  complémentaire, envoi du mail au professeur.
- Dépendance : rendu au plus tard le 2026-11-09 (veille de la soutenance du 2026-11-10).
