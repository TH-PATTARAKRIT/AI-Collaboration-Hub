# GMVQ / LANE A Multi-Source Evidence Bridge

Status: ACTIVE
Authority: Boss
Purpose: Prevent false project-wide absence conclusions caused by reading only one branch, PR, folder, or working tree.

## Mandatory source registry

Before any LANE A / GMVQ intake concludes that evidence, a module, or a Question Bank is absent, read:

`LANE_A_CONTROL/GMVQ_EVIDENCE_SOURCE_REGISTRY.tsv`

The registry is authoritative for which evidence surfaces must be checked.

## Core rule

`NOT FOUND ON THIS BRANCH` is not equivalent to `NOT FOUND IN THE PROJECT`.

Every absence-based conclusion must search all applicable registered evidence surfaces.

## Required search order

1. Canonical/control branch: `SMEsPlus`
2. Merged governed history relevant to the target
3. Candidate PRs/branches containing the target G/module
4. Active working PRs/branches
5. Reconciliation PRs/artifacts
6. A1 / RED TEAM / checkpoint evidence
7. LANE A task/result/control artifacts
8. Any additional evidence surface referenced by an evidence pointer or active task

## Evidence-state separation

For every module/group record separately:
- canonical_tree_presence
- merged_governed_evidence_presence
- candidate_artifact_presence
- candidate_question_bank_presence
- working_branch_presence
- reconciliation_evidence_presence
- roster_membership_state
- canonical_admission_state
- lane_a_disposition
- evidence_pointer

## Prohibited shortcut

Do not conclude `NOT_FOUND`, `NO BANK`, `0 MODULE`, or issue an absence-based HOLD after checking only one source surface.

## Governance interpretation

- Candidate evidence can prove that an artifact exists.
- Candidate evidence does not automatically prove canonical membership.
- Unmerged evidence can still be valid evidence-of-existence when its lineage is preserved.
- A working PR does not become canonical merely because it is newer.
- Reconciliation evidence does not become Boss approval.
- File location does not itself prove Gate admission.

## Dynamic rule

This bridge is not hard-coded to PR #71.

If a new PR, branch, task result, reconciliation package, or evidence pointer appears, it must be treated as an additional evidence surface when relevant. Add it to the registry or record it in the task-specific evidence inventory before final disposition.

No Evidence = No Progress.
No single-source absence may be promoted to project-wide absence.
