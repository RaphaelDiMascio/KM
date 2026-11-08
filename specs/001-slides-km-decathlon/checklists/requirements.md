# Specification Quality Checklist: Contenu des slides KM et choix de l'entreprise (Decathlon)

**Purpose**: Validate specification completeness and quality before proceeding to planning
**Created**: 2026-11-08
**Feature**: [spec.md](../spec.md)

## Content Quality

- [x] No implementation details (languages, frameworks, APIs)
- [x] Focused on user value and business needs
- [x] Written for non-technical stakeholders
- [x] All mandatory sections completed

## Requirement Completeness

- [x] No [NEEDS CLARIFICATION] markers remain
- [x] Requirements are testable and unambiguous
- [x] Success criteria are measurable
- [x] Success criteria are technology-agnostic (no implementation details)
- [x] All acceptance scenarios are defined
- [x] Edge cases are identified
- [x] Scope is clearly bounded
- [x] Dependencies and assumptions identified

## Feature Readiness

- [x] All functional requirements have clear acceptance criteria
- [x] User scenarios cover primary flows
- [x] Feature meets measurable outcomes defined in Success Criteria
- [x] No implementation details leak into specification

## Notes

- Validation passed on the first iteration.
- The only mention of a tool (Google Slides) is a deliverable constraint inherited from the
  constitution, placed under Assumptions; no generation method is specified.
- Points still open, to settle during drafting (not blocking): consulting firm name, real
  speaker names, example brand and numerical hypotheses.

## Vérification finale de l'implémentation (2026-11-08)

Livrable : `output/KM_Decathlon_MIAGE_Conseil.pptx` (14 slides) + `output/notes_orateur.md`.
Contrôle automatique : `python deck/check_deck.py` → C1 à C10 conformes (code retour 0).

| Critère | Statut | Preuve |
|---------|--------|--------|
| SC-001 | ✓ | Cadrage qui / à qui / pourquoi (slide 2), hypothèses (3), KM défini (5), pourquoi promouvoir (6), démarche (7–12), synthèse et pilote (13) |
| SC-002 | ✓ | 16 concepts distincts du cours mobilisés sur les slides 4–12, références en slide 14 (C5) |
| SC-003 | ✓ | 13 slides de contenu + 1 slide questions ; max 39 mots affichés et ≤ 6 puces par slide (C3) |
| SC-004 | ◐ | Estimation à 130 mots/min : A 591 / B 577 / C 599 mots, ≈ 13,6 min (C9). Répétition chronométrée à faire par l'équipe |
| SC-005 | ◐ | Message unique « délocaliser = transférer des connaissances » (slides 1, 4, 13). Test de lecture externe à faire |
| SC-006 | ✓ | Faits relus contre research.md R5 ; aucune production au Vietnam affirmée ; données non vérifiées étiquetées « Hypothèse » (C7) |
