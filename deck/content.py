"""Contenu du deck — source unique, modifiable sans toucher au code.

Règles (contracts/slide-content-contract.md) : ≤ 6 puces et ≤ 40 mots affichés par slide,
titres 1–13 identiques à la spec, notes commençant par « [Orateur X – Prénom] ».
"""
from dataclasses import dataclass, field
from typing import Optional

import theme as T


# --------------------------------------------------------------------------- entités

@dataclass
class Speaker:
    code: str          # "A" | "B" | "C"
    name: str
    slides: list


@dataclass
class Concept:
    key: str
    label: str
    reference: str
    application: str


@dataclass
class Hypothesis:
    id: str
    statement: str
    rationale: str
    used_on: list


@dataclass
class Phase:
    index: int
    name: str
    months: str
    start: int
    end: int
    actions: list           # ≥ 2
    actors: list            # ≥ 1
    deliverable_or_kpi: list  # ≥ 1
    slide: int
    grundstein: list


@dataclass
class Slide:
    number: int
    title: str              # ≤ 110 caractères
    layout: str             # title | bullets | two_columns | cards | diagram | closing
    speaker: str            # A | B | C | ALL
    bullets: list = field(default_factory=list)   # ≤ 6
    visual: Optional[str] = None
    visual_data: dict = field(default_factory=dict)
    concepts: list = field(default_factory=list)
    hypothesis_flag: bool = False
    notes: str = ""
    transition: Optional[str] = None


# --------------------------------------------------------------------------- orateurs

SPEAKERS = {
    "A": Speaker("A", "Raphaël", [1, 2, 3, 4, 5, 13]),
    "B": Speaker("B", "Caupcine", [6, 7, 8]),
    "C": Speaker("C", "Fares", [9, 10, 11, 12]),
}

# --------------------------------------------------------------------------- hypothèses

HYPOTHESES = [
    Hypothesis("H1", "Périmètre : une partie de la conception produit (développement technique, "
               "prototypage) et de l'ingénierie qualité Quechua ; la vision produit reste en France",
               "Le savoir-faire de conception est très tacite, donc fragile lors d'un transfert.",
               [3, 4]),
    Hypothesis("H2", "40 ingénieurs conception et qualité concernés en France",
               "Ordre de grandeur plausible pour une partie du site montagne de Passy (~400 personnes).",
               [3]),
    Hypothesis("H3", "Une équipe de 15 personnes à Hô Chi Minh-Ville",
               "Proximité des fournisseurs asiatiques ; Decathlon est déjà présent au Vietnam (magasins).",
               [3, 9]),
    Hypothesis("H4", "Transfert progressif sur 18 mois, en 3 vagues : sacs à dos, tentes, chaussures",
               "Commencer par la gamme la moins critique pour la sécurité limite le risque.",
               [3, 7, 9, 13]),
    Hypothesis("H5", "Contraintes non négociables : qualité, délais, sécurité produit",
               "Traduction opérationnelle de l'objectif « zéro impact » du complément n°06.",
               [3, 6, 12]),
    Hypothesis("H6", "MIAGE Conseil a récemment audité Decathlon",
               "Prémisse de l'énoncé : notre employeur a audité l'entreprise cliente.",
               [2, 3]),
]

# --------------------------------------------------------------------------- concepts du cours

COURSE = "Arduin, supports de cours KM"

CONCEPTS = {c.key: c for c in [
    Concept("postulats", "Les 3 postulats sur la connaissance", COURSE,
            "La connaissance Quechua s'interprète, vit dans l'action et est en grande partie tacite."),
    Concept("polanyi", "« Nous savons plus que nous ne pouvons dire »", "Polanyi, 1958",
            "Le ressenti d'un test terrain ne tient pas dans un cahier des charges."),
    Concept("tacite_explicite", "Savoirs explicites vs savoir-faire tacites", "Nelson et Winter, 1982",
            "Normes et protocoles (explicite) vs arbitrages qualité et usages (tacite)."),
    Concept("sense_giving", "Sense-giving / sense-reading", "Tsuchiya, 1993",
            "Un même cahier des charges est lu différemment à Passy et à Hô Chi Minh-Ville."),
    Concept("socio_technique", "Approche managériale et socio-technique", COURSE,
            "Personnes, rituels et outils plutôt qu'une simple base documentaire."),
    Concept("definition_km", "Manager des activités qui créent et utilisent des connaissances", COURSE,
            "Piloter le transfert comme un projet de connaissances, pas de postes."),
    Concept("patrimoniale_innovation", "Finalité patrimoniale et innovation durable", COURSE,
            "Pérenniser le savoir-faire Quechua et continuer à innover."),
    Concept("entreprise_etendue", "Entreprise étendue", "Grundstein et Rosenthal-Sabroux, 2009",
            "Fournisseurs et partenaires asiatiques associés au partage."),
    Concept("grundstein_facettes", "5 facettes de la capitalisation sur les connaissances cruciales",
            "Grundstein, 1996", "Repérer, préserver, valoriser, actualiser, manager structurent la démarche."),
    Concept("axe_progres", "Axe de progrès privé/disséminé, non formalisé/formalisé", "Grundstein, 1998",
            "Faire passer le savoir des experts de Passy vers un référentiel partagé."),
    Concept("seci", "Modèle SECI", "Nonaka et Takeuchi, 1995",
            "Spirale socialisation → externalisation → combinaison → internalisation, gamme par gamme."),
    Concept("ba", "Ba", "Nonaka et Konno, 1998",
            "Espace partagé physique et virtuel entre Passy et Hô Chi Minh-Ville."),
    Concept("semi_ouvert", "Fonctionnement semi-ouvert (SopIM)", "Grundstein, 1988",
            "Chacun contribue au Ba sans que tout soit imposé d'en haut."),
    Concept("bonne_intelligence", "Relations de bonne intelligence (4 critères)", COURSE,
            "Respect, complémentarité, réciprocité, transparence entre équipes FR et VN."),
    Concept("iiia_phases", "Phases d'un projet de KM", "IIIA-GTM, 2000",
            "Orientations stratégiques, pilotage opérationnel, déploiement des solutions."),
    Concept("cas_axa", "Cas AXA : espace collaboratif de pérennisation", COURSE,
            "Réunions partagées et vocabulaire commun avec la nouvelle équipe."),
]}

# --------------------------------------------------------------------------- phases (research.md R8)

PHASES = [
    Phase(1, "Repérer et préserver", "M0–M3", 0, 3,
          ["Cartographier les connaissances cruciales", "Entretiens, récits et vidéos d'experts",
           "Référentiel conception et qualité"],
          ["Experts conception/qualité de Passy", "Responsable KM"],
          ["Carte des connaissances cruciales (M3)"], 8, ["repérer", "préserver"]),
    Phase(2, "Transférer (SECI)", "M3–M15, 3 vagues", 3, 15,
          ["Binômes FR–VN et immersions croisées", "Retours d'expérience formalisés",
           "Base bilingue et revues communes", "Pratique encadrée puis autonome"],
          ["Ingénieurs FR (mentors)", "Équipe de Hô Chi Minh-Ville"],
          ["Autonomie de l'équipe VN par gamme"], 9, ["valoriser"]),
    Phase(3, "Partager (Ba)", "dès M3, permanent", 3, 18,
          ["Communauté de pratique", "Revue de cas qualité mensuelle", "Plateforme bilingue et glossaire"],
          ["Référents passeurs biculturels"],
          ["Participation aux revues de cas"], 10, ["valoriser"]),
    Phase(4, "Actualiser et piloter", "M0–M18 et au-delà", 0, 18,
          ["Gouvernance sponsor / responsable KM / référents", "Revue trimestrielle et mise à jour"],
          ["Sponsor direction Quechua", "Responsable KM", "Référents FR et VN"],
          ["% connaissances cruciales formalisées", "Taux de défauts", "Délais de mise en marché"],
          12, ["actualiser", "manager"]),
]

WAVES = [("Sacs à dos", 3, 7), ("Tentes", 7, 11), ("Chaussures", 11, 15)]

# --------------------------------------------------------------------------- slides

SLIDES = [
    # ------------------------------------------------------------------ 1
    Slide(1, "Délocaliser sans oublier : pérenniser le savoir-faire Decathlon entre la France et le Vietnam",
          "title", "A",
          visual_data={
              "subtitle": "MIAGE Conseil — Proposition aux cadres conception & qualité Quechua (Decathlon)",
              "members": "Raphaël · Caupcine · Fares",
              "course": "Master 2 MIAGE — Introduction au Knowledge Management — P.-E. Arduin — 10 novembre 2026",
          },
          notes=(
              "[Orateur A – Raphaël]\n"
              "Bonjour à toutes et à tous. Nous sommes Raphaël, Caupcine et Fares, consultants chez "
              "MIAGE Conseil. Vous faites vivre la conception et la qualité des produits Quechua, et "
              "vous étudiez un projet important : transférer une partie de cette activité au Vietnam. "
              "Notre message "
              "tient en une phrase : délocaliser, ce n'est pas seulement déplacer des postes, c'est "
              "déplacer des connaissances. En quinze minutes, nous allons vous montrer comment éviter "
              "que ce savoir-faire se perde en route."
          )),
    # ------------------------------------------------------------------ 2
    Slide(2, "Qui sommes-nous, à qui parlons-nous, pourquoi ?", "cards", "A",
          visual="cards", hypothesis_flag=True,
          visual_data={"cols": 4, "head_h": 0.9, "head_size": 24, "body_size": 22, "items": [
              {"head": "Qui ?", "body": "MIAGE Conseil : 5 ans de conseil, audit Decathlon récent"},
              {"head": "À qui ?", "body": "Cadres conception produit & qualité Quechua"},
              {"head": "Pourquoi ?", "body": "Projet de délocalisation partielle au Vietnam"},
              {"head": "Objectif", "body": "Zéro impact sur l'activité", "accent": True},
          ]},
          notes=(
              "[Orateur A – Raphaël]\n"
              "MIAGE Conseil est un petit cabinet ; nous y sommes consultants depuis cinq ans, et notre "
              "cabinet a récemment audité Decathlon : nous connaissons donc votre organisation. Nous "
              "nous adressons à vous, cadres opérationnels de la conception produit et de l'ingénierie "
              "qualité Quechua, parce que c'est vous qui vivrez ce transfert au quotidien. Pourquoi "
              "maintenant ? Parce que vous envisagez de rapprocher une partie de la conception et de la "
              "qualité des fournisseurs, en Asie. Votre exigence est aussi la nôtre : zéro impact sur "
              "l'activité."
          )),
    # ------------------------------------------------------------------ 3
    Slide(3, "Nos hypothèses de travail", "cards", "A",
          visual="cards", hypothesis_flag=True,
          visual_data={"cols": 3, "head_h": 0.6, "head_size": 22, "items": [
              {"head": "H1", "body": "Conception & qualité Quechua"},
              {"head": "H2", "body": "40 ingénieurs en France"},
              {"head": "H3", "body": "15 personnes à Hô Chi Minh-Ville"},
              {"head": "H4", "body": "18 mois, 3 vagues"},
              {"head": "H5", "body": "Qualité, délais, sécurité produit"},
              {"head": "H6", "body": "Audit Decathlon déjà réalisé"},
          ], "footnote": "Fait : bureau de production en Asie dès 1988"},
          notes=(
              "[Orateur A – Raphaël]\n"
              "Le sujet ne donne pas tous les chiffres : nous avons donc posé six hypothèses, à valider "
              "avec vous. Un : le périmètre est une partie de la conception produit et de l'ingénierie "
              "qualité Quechua ; la vision produit reste en France. Deux : environ "
              "quarante ingénieurs sont concernés. Trois : une équipe de quinze personnes serait créée à "
              "Hô Chi Minh-Ville, près des fournisseurs. Quatre : un transfert progressif sur "
              "dix-huit mois, en trois vagues. Cinq : qualité, délais et sécurité produit sont "
              "non négociables. Six : nous connaissons déjà votre organisation grâce à l'audit. "
              "(coupable) Le seul fait réel affiché est public : Decathlon a ouvert son premier bureau "
              "de production en Asie dès 1988."
          )),
    # ------------------------------------------------------------------ 4
    Slide(4, "Ce qui part au Vietnam, ce ne sont pas des tâches, ce sont des connaissances",
          "diagram", "A", visual="iceberg",
          concepts=["postulats", "polanyi", "tacite_explicite"],
          visual_data={
              "explicit_head": "Explicite — savoirs",
              "explicit": "Cahiers des charges · normes · protocoles de test",
              "tacit_head": "Tacite — savoir-faire",
              "tacit": ["Ressenti des tests terrain", "Compréhension des usages sportifs",
                        "Arbitrages qualité", "Relation fournisseurs"],
              "quote": "« Nous savons plus que nous ne pouvons dire »",
              "author": "Polanyi, 1958",
          },
          notes=(
              "[Orateur A – Raphaël]\n"
              "Voici l'idée centrale de notre proposition : ce qui partira au Vietnam, ce ne sont pas "
              "des tâches, ce sont des connaissances. Une partie est visible, au-dessus de la ligne de "
              "flottaison : les cahiers des charges, les normes, les protocoles de test. Ce sont des "
              "savoirs explicites, déjà écrits, faciles à transmettre. Mais l'essentiel est sous la "
              "surface : le ressenti d'un ingénieur qui teste une tente sous la pluie en montagne, la "
              "compréhension fine des usages des randonneurs, les arbitrages entre coût et qualité, la "
              "relation de confiance construite avec chaque fournisseur. C'est le savoir-faire tacite, "
              "que Nelson et Winter distinguent des savoirs. Michael Polanyi le résumait en 1958 : "
              "« nous savons plus que nous ne pouvons dire ». Transférer des documents, c'est donc "
              "transférer seulement la pointe de l'iceberg."
          )),
    # ------------------------------------------------------------------ 5
    Slide(5, "Le KM : manager les activités qui créent et utilisent des connaissances",
          "two_columns", "A", visual="two_columns",
          concepts=["definition_km", "postulats", "sense_giving", "socio_technique"],
          visual_data={
              "quote": "« Manager des activités qui créent et qui utilisent des connaissances »",
              "left": ["Pas un objet : sense-giving / sense-reading", "Liée à l'action",
                       "Tacite et explicite"],
              "right_head": "Approche retenue",
              "right": ["Technologique seule : insuffisante",
                        "Socio-technique : personnes, rituels, outils",
                        "Schémas d'interprétation FR ≠ VN à aligner"],
          },
          notes=(
              "[Orateur A – Raphaël]\n"
              "Alors, qu'est-ce que le Knowledge Management ? C'est « manager des "
              "activités qui créent et qui utilisent des connaissances ». Il repose sur trois postulats. "
              "Premier postulat : une connaissance n'est pas un objet. Celui qui explique donne du sens, "
              "c'est le sense-giving ; celui qui reçoit interprète, c'est le sense-reading, selon "
              "Tsuchiya. Chacun interprète avec ses propres schémas d'interprétation : un ingénieur de "
              "Passy et un ingénieur de Hô Chi Minh-Ville ne liront pas forcément un cahier des charges "
              "de la même façon, à cause de la langue, du contexte et des usages. Deuxième postulat : la "
              "connaissance est liée à l'action ; elle vit dans vos processus de conception et de test. "
              "Troisième postulat : il existe des connaissances explicites et tacites. Conséquence : une "
              "approche purement technologique, une grande base documentaire, ne suffira pas. Il faut "
              "une approche socio-technique, qui combine les personnes, des rituels et des outils. "
              "C'est ce principe qui guide toute notre démarche."
          ),
          transition="Caupcine va maintenant vous montrer pourquoi le KM est indispensable dans "
                     "votre projet, et comment nous le mettrons en œuvre."),
    # ------------------------------------------------------------------ 6
    Slide(6, "Sans KM, la délocalisation met en danger qualité, délais et innovation",
          "diagram", "B", visual="risk_benefit",
          concepts=["grundstein_facettes", "patrimoniale_innovation", "entreprise_etendue"],
          visual_data={
              "risks_head": "Sans KM — risques",
              "risks": ["Défauts qualité", "Retards de mise en marché",
                        "Perte de connaissances cruciales", "Rupture usage–conception"],
              "benefits_head": "Avec KM — bénéfices",
              "benefits": ["Continuité de l'activité", "Montée en compétence au Vietnam",
                           "Capitalisation pour innover"],
              "band": "Deux finalités : patrimoniale (pérenniser) et innovation durable (créer)",
          },
          notes=(
              "[Orateur B – Caupcine]\n"
              "Merci Raphaël. Maintenant que nous savons ce qu'est le KM, pourquoi le promouvoir dans "
              "votre projet ? À gauche, sans démarche de KM, la "
              "délocalisation fait courir quatre risques. Des défauts qualité, parce que les arbitrages "
              "tacites ne sont pas transmis. Des retards de mise en marché, le temps que la nouvelle "
              "équipe réapprenne seule. La perte de connaissances cruciales, si des experts partent ou "
              "se démotivent ; une connaissance cruciale, c'est une connaissance que l'entreprise ne "
              "peut pas perdre sans risquer de figer son activité. Et une rupture entre l'usage terrain et la conception. À droite, ce que "
              "le KM apporte : la continuité de l'activité, une montée en compétence rapide de l'équipe "
              "vietnamienne, et une capitalisation qui nourrit l'innovation. On retrouve les deux "
              "finalités du KM : une finalité patrimoniale, pérenniser ce que vous savez, et une "
              "finalité d'innovation durable, créer de nouvelles connaissances. Autrement dit, le KM "
              "n'est pas un coût de plus : c'est l'assurance de votre projet. Selon Grundstein, "
              "capitaliser sur ces connaissances cruciales, c'est les repérer, les préserver, les "
              "valoriser, les actualiser et manager l'ensemble : ce sera le fil de notre démarche. "
              "(coupable) Vos "
              "fournisseurs asiatiques font aussi partie de l'entreprise étendue, au sens de Grundstein "
              "et Rosenthal-Sabroux : ils peuvent contribuer à ce partage."
          )),
    # ------------------------------------------------------------------ 7
    Slide(7, "Notre démarche en 4 phases", "diagram", "B", visual="timeline",
          hypothesis_flag=True, concepts=["grundstein_facettes", "iiia_phases"],
          visual_data={
              "phases": [
                  {"label": "1 · Repérer & préserver", "start": 0, "end": 3, "color": T.BLUE},
                  {"label": "2 · Transférer — spirale SECI", "start": 3, "end": 15, "color": T.BLUE},
                  {"label": "3 · Partager — Ba France–Vietnam", "start": 3, "end": 18, "color": T.NAVY},
                  {"label": "4 · Actualiser & piloter (en continu)", "start": 0, "end": 18, "color": T.NAVY},
              ],
              "waves": [{"label": w, "start": s, "end": e} for w, s, e in WAVES],
              "trust": "Confiance : condition transverse à toutes les phases",
              "ticks": [0, 3, 6, 9, 12, 15, 18],
          },
          notes=(
              "[Orateur B – Caupcine]\n"
              "Comment faire ? Nous proposons une démarche en quatre phases, inspirée des facettes de la "
              "capitalisation sur les connaissances cruciales de Grundstein : repérer, préserver, "
              "valoriser, actualiser et manager. Phase un, les trois premiers mois : repérer et "
              "préserver. Phase deux, du mois trois au mois quinze : transférer en faisant tourner la "
              "spirale SECI, en trois vagues, d'abord les sacs à dos, puis les tentes, enfin les "
              "chaussures. Nous commençons par la gamme la moins critique pour la sécurité, afin "
              "d'apprendre sans risque. Phase trois, dès le mois trois et en permanence : créer un Ba, "
              "un espace de partage entre la France et le Vietnam. Phase quatre, du début à la fin : "
              "actualiser et piloter. La confiance, en bas de la frise, conditionne toutes les phases. "
              "Comme le recommande l'IIIA pour un projet de KM, nous articulons trois niveaux : des "
              "orientations stratégiques fixées avec votre direction, un pilotage opérationnel confié à "
              "un responsable KM, puis le déploiement concret des solutions dans vos équipes. "
              "(coupable) Ce calendrier est une hypothèse que nous ajusterons avec vous."
          )),
    # ------------------------------------------------------------------ 8
    Slide(8, "Phase 1 — Repérer et préserver les connaissances cruciales", "bullets", "B",
          visual="side_card", hypothesis_flag=True,
          concepts=["grundstein_facettes", "axe_progres", "seci"],
          bullets=["Cartographier les connaissances cruciales : rareté, difficulté, impact",
                   "Entretiens et récits d'experts Quechua",
                   "Vidéos commentées des tests terrain",
                   "Référentiel conception & qualité partagé",
                   "Grundstein : repérer, préserver · SECI : externaliser"],
          visual_data={"head": "Livrable — M3",
                       "body": "Carte des connaissances cruciales validée avec vous"},
          notes=(
              "[Orateur B – Caupcine]\n"
              "Phase un : repérer et préserver. On ne peut pas tout transférer : il faut d'abord savoir "
              "ce qui compte, et le faire tant que les experts de Passy sont là, avant une mobilité ou "
              "un départ en retraite. Avec vos équipes, nous cartographions les connaissances cruciales selon "
              "trois critères : leur rareté, leur difficulté d'acquisition et leur impact sur "
              "l'activité. Pour chacune, nous posons quatre questions simples : où est-elle, qui la "
              "détient, sous quelle forme, et que se passerait-il si elle disparaissait demain ? "
              "Ensuite, nous les préservons : entretiens et récits d'experts sur des cas "
              "réels, comme un défaut qualité résolu ou un arbitrage difficile, vidéos "
              "commentées des tests terrain, et un référentiel de conception et de qualité partagé. "
              "C'est l'externalisation du modèle SECI : rendre explicite une partie du tacite. Dans "
              "l'axe de progrès de Grundstein, des connaissances privées et non formalisées deviennent "
              "formalisées et disséminées. Le livrable, au mois trois, est une carte des connaissances "
              "cruciales validée par vous. (coupable) Elle désigne aussi les experts à associer en "
              "priorité."
          ),
          transition="Mais documenter ne suffit pas : Fares va vous montrer comment transférer "
                     "réellement le savoir-faire tacite."),
    # ------------------------------------------------------------------ 9
    Slide(9, "Phase 2 — Transférer en faisant tourner la spirale SECI", "diagram", "C",
          visual="seci", hypothesis_flag=True, concepts=["seci", "cas_axa"],
          visual_data={
              "cells": [("Socialisation", "Binômes FR–VN, immersions à Passy"),
                        ("Externalisation", "Retours d'expérience formalisés"),
                        ("Combinaison", "Base bilingue, revues de conception communes"),
                        ("Internalisation", "Pratique encadrée, autonomie par gamme")],
              "waves": ["Vague 1 · Sacs à dos", "Vague 2 · Tentes", "Vague 3 · Chaussures"],
          },
          notes=(
              "[Orateur C – Fares]\n"
              "Merci Caupcine. La phase deux est le cœur du transfert : nous faisons tourner la spirale "
              "SECI de Nonaka et Takeuchi, gamme après gamme. D'abord la socialisation, de tacite à "
              "tacite : chaque ingénieur vietnamien travaille en binôme avec un ingénieur français, avec "
              "des immersions croisées à Passy et au Vietnam, et des tests terrain réalisés ensemble. "
              "Ensuite l'externalisation : les binômes formalisent leurs retours d'expérience, ce qui "
              "enrichit le référentiel de la phase un. Puis la combinaison : ces éléments rejoignent une "
              "base de connaissances bilingue, et les revues de conception se font en commun. Enfin "
              "l'internalisation : l'équipe vietnamienne pratique, d'abord encadrée, puis en autonomie, "
              "et la spirale recommence avec la gamme suivante. Chaque vague dure environ quatre mois : "
              "les sacs à dos d'abord, puis les tentes, puis les chaussures. L'équipe française reste "
              "en appui jusqu'à ce que l'équipe vietnamienne valide seule un produit complet. "
              "(coupable) C'est ce qui a fonctionné "
              "dans le cas AXA vu en cours : on est passé d'un fichier d'incidents isolé à des réunions "
              "partagées où le nouveau prestataire participait activement."
          )),
    # ------------------------------------------------------------------ 10
    Slide(10, 'Phase 3 — Créer un "Ba" France–Vietnam pour partager durablement', "diagram", "C",
          visual="ba", concepts=["ba", "semi_ouvert", "cas_axa"],
          visual_data={
              "left": ("France", "Passy"),
              "right": ("Vietnam", "Hô Chi Minh-Ville"),
              "center": "Ba",
              "center_sub": "Espace physique + virtuel",
              "items": ["Communauté de pratique", "Revue de cas qualité mensuelle",
                        "Plateforme bilingue + glossaire commun", "Référents passeurs biculturels"],
              "caption": "Fonctionnement semi-ouvert : chacun contribue, rien n'est imposé",
          },
          notes=(
              "[Orateur C – Fares]\n"
              "Pour que le partage dure au-delà du transfert, il faut un lieu. C'est le concept de Ba, "
              "proposé par Nonaka et Konno en 1998 : un espace partagé, physique et virtuel, où les "
              "connaissances se créent. Concrètement, quatre dispositifs. Une communauté de pratique "
              "conception et qualité qui réunit Passy et Hô Chi Minh-Ville. Une revue de cas qualité "
              "mensuelle, où l'on analyse ensemble un défaut ou un retour client. Une plateforme "
              "collaborative bilingue, avec un glossaire commun, pour réduire les écarts de schémas "
              "d'interprétation entre les deux équipes ; c'est l'équivalent du vocabulaire commun du "
              "cas AXA. Et des référents passeurs biculturels, qui font le lien. Ce Ba fonctionne en "
              "mode semi-ouvert, au sens de Grundstein : chacun peut contribuer, sans que tout soit "
              "imposé d'en haut."
          )),
    # ------------------------------------------------------------------ 11
    Slide(11, "Pas de partage sans confiance", "diagram", "C", visual="trust",
          concepts=["bonne_intelligence", "socio_technique"],
          visual_data={
              "criteria": [("Respect", "Experts reconnus comme mentors"),
                           ("Complémentarité", "Savoir-faire FR + terrain VN"),
                           ("Réciprocité", "Chacun apprend de l'autre"),
                           ("Transparence des décisions", "Calendrier et postes annoncés")],
              "avoid": "À éviter : manque de moyens · isolement social · pression du temps",
          },
          notes=(
              "[Orateur C – Fares]\n"
              "Tout cela ne fonctionnera pas sans confiance. Un expert français qui craint pour son "
              "poste peut être tenté de garder son savoir-faire pour lui. Nous nous appuyons donc sur "
              "les quatre critères des relations de bonne intelligence. Le respect : les experts sont "
              "reconnus comme mentors, et ce rôle est valorisé. La complémentarité : le savoir-faire "
              "français s'associe à la proximité des fournisseurs côté Vietnam. La réciprocité : chacun "
              "apprend de l'autre, l'échange va dans les deux sens. La transparence des décisions : le "
              "calendrier et l'évolution des postes sont annoncés clairement. À l'inverse, il faut "
              "éviter les facteurs de stress : le manque de moyens, l'isolement social et la pression "
              "du temps. Concrètement, la direction doit annoncer tôt ce que deviennent les postes en "
                            "France, par exemple de nouveaux rôles d'experts référents ou d'innovation, pour que "
                            "partager son savoir ne soit pas vécu comme une menace. (coupable) C'est pourquoi nous "
                            "prévoyons du temps dédié au mentorat dans les plannings."
          )),
    # ------------------------------------------------------------------ 12
    Slide(12, "Phase 4 — Actualiser et piloter dans la durée", "diagram", "C", visual="kpi",
          hypothesis_flag=True, concepts=["grundstein_facettes", "iiia_phases"],
          visual_data={
              "gov_head": "Gouvernance",
              "gov": ["Sponsor · direction Quechua", "Responsable KM", "Référents FR / VN"],
              "kpi_head": "Indicateurs suivis",
              "kpis": ["% connaissances cruciales formalisées", "Autonomie de l'équipe Vietnam",
                       "Taux de défauts", "Délais de mise en marché"],
              "band": "Revue trimestrielle : actualiser, standardiser, enrichir",
          },
          notes=(
              "[Orateur C – Fares]\n"
              "Dernière phase : actualiser et piloter, dès le départ et dans la durée. Côté gouvernance, "
              "nous proposons un sponsor issu de la direction Quechua, un responsable KM qui coordonne "
              "la démarche, et des référents en France et au Vietnam. On retrouve les phases d'un projet "
              "de KM : orientations stratégiques, pilotage opérationnel, puis déploiement des solutions. "
              "Côté indicateurs, nous en suivons quatre : la part des connaissances cruciales "
              "formalisées, l'autonomie de l'équipe vietnamienne, le taux de défauts et les délais de "
              "mise en marché. Une revue trimestrielle permet d'actualiser le référentiel, de corriger "
              "le tir et de standardiser ce qui marche. Et le KM ne s'arrête pas au mois dix-huit : "
                            "les connaissances évoluent avec chaque nouveau produit, et le référentiel doit vivre "
                            "avec elles, sinon il devient vite obsolète. (coupable) Les cibles chiffrées seront "
                            "fixées avec vous pendant le pilote."
          ),
          transition="Raphaël va maintenant conclure et vous présenter notre proposition concrète."),
    # ------------------------------------------------------------------ 13
    Slide(13, "Délocaliser, c'est transférer des connaissances : lançons un pilote", "closing", "A",
          visual="cards", hypothesis_flag=True,
          visual_data={"cols": 3, "head_h": 0.9, "head_size": 24, "body_size": 22, "items": [
              {"head": "Quoi ?", "body": "Transférer des connaissances, pas des tâches"},
              {"head": "Pourquoi ?", "body": "Zéro impact qualité, délais, innovation"},
              {"head": "Comment ?", "body": "4 phases : repérer, transférer, partager, piloter"},
          ], "cta": "Lançons un pilote sur les sacs à dos — janvier 2027"},
          notes=(
              "[Orateur A – Raphaël]\n"
              "Pour conclure, trois idées. Quoi : délocaliser, c'est d'abord transférer des "
              "connaissances, en particulier le savoir-faire tacite de vos équipes. Pourquoi : c'est la "
              "seule façon de tenir l'objectif de zéro impact sur la qualité, les délais et "
              "l'innovation. Comment : une démarche en quatre phases, appuyée sur la confiance. "
              "Notre proposition concrète : un pilote sur la gamme sacs à dos, avec un démarrage "
              "possible en janvier 2027, puis une décision commune sur la base des indicateurs. "
              "(coupable) Ce pilote limite le risque et donne des résultats mesurables en quelques mois."
          ),
          transition="Merci de votre attention ; nous sommes à votre disposition pour vos questions."),
    # ------------------------------------------------------------------ 14
    Slide(14, "Merci ! Des questions ?", "closing", "ALL", visual="sources",
          notes=(
              "[Tous]\n"
              "Répartition des questions probables : choix de Decathlon, hypothèses et pilote : "
              "Raphaël ; définition du KM, tacite et explicite, postulats : Raphaël ; risques, "
              "connaissances cruciales, démarche et calendrier : Caupcine ; SECI, "
              "Ba, confiance et indicateurs : Fares. Si une question porte sur un chiffre, rappeler "
              "qu'il s'agit d'une hypothèse à valider avec le client."
          )),
]

# --------------------------------------------------------------------------- sources (slide 14)

_refs = []
for c in CONCEPTS.values():
    if c.reference != COURSE and c.reference not in _refs:
        _refs.append(c.reference)

SOURCES = (
    [COURSE + " — Introduction au Knowledge Management (KM1, KM3), Université Paris Dauphine-PSL"]
    + [r + " (cité dans les supports de cours)" for r in sorted(_refs)]
    + ["Wikipédia, articles « Decathlon » et « Quechua », consultés le 08/11/2026"]
)

SLIDES[13].visual_data = {"sources": SOURCES,
                          "line": "Raphaël · Caupcine · Fares — MIAGE Conseil"}
