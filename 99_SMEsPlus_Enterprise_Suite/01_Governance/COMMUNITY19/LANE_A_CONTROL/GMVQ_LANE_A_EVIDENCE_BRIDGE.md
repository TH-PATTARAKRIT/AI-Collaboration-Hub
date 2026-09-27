# GMVQ / LANE A Evidence Bridge

Status: ACTIVE
Authority: Boss
Purpose: Prevent false "NOT_FOUND" conclusions caused by reading only one branch/tree.

## Mandatory evidence surfaces

Every LANE A / GMVQ intake must inspect BOTH:

1. Canonical / control surface
   - Branch: SMEsPlus
   - Current governed files and control artifacts

2. Candidate evidence surface
   - PR #71
   - Head branch: feature/ERPPLUS-170-gmvq-g01-g16-authoring-20260927
   - Head commit: 843e61713939461205c404514555b2bf57c6ed39
   - Candidate path:
     99_SMEsPlus_Enterprise_Suite/01_Governance/COMMUNITY19/GMVQ_CANDIDATE_ROSTER_NOT_VERIFIED/

## Interpretation rules

- "Not present on SMEsPlus" MUST NOT be reported as "does not exist" until PR #71 and other governed evidence surfaces have been checked.
- Candidate Question Bank existence is a separate state from canonical admission.
- Candidate module-name evidence is a separate state from canonical roster membership.
- Closed/unmerged candidate PR evidence may be used as evidence-of-existence, but NOT as canonical membership, downstream authorization, or Formal Coverage proof.

## Mandatory evidence-state fields

For every module/group, record separately:
- canonical_tree_presence
- candidate_artifact_presence
- candidate_question_bank_presence
- roster_membership_state
- canonical_admission_state
- lane_a_disposition
- evidence_pointer

## Known candidate-bank inventory from PR #71

- G02: 11 candidate module banks
- G03: 11 candidate module banks
- G04: 9 candidate module banks
- G05: 14 candidate module banks
- G06: 12 candidate module banks
- G07: 9 candidate module banks
- G08: 31 unique candidate module banks
- G09: 8 candidate module banks
- G11: 8 candidate module banks
- G12: 20 candidate module banks
- G15: 11 candidate module banks

No candidate-bank set in PR #71 for G10, G13, G14, G16.

This inventory is evidence-of-artifact presence only. It does not establish canonical roster membership.

## Required execution rule

Before any `NOT_FOUND`, `NO BANK`, `0 MODULE`, or HOLD rationale based on absence:
1. check SMEsPlus;
2. check PR #71 candidate branch/path;
3. check relevant A1/RED TEAM/reconciliation artifacts;
4. only then classify the evidence state.

No Evidence = No Progress.
No branch-local absence may be promoted to project-wide absence without this bridge check.
