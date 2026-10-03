# STATE02_GATE_ALIAS_AND_MODEL_CROSSWALK_v1.0.md

Session: SMEPLUS-26-07-13-GATE01
State: 02 — Governance
Step: 06 — Gate Crosswalk
Prepared By: Claude AI (Responsible role only)
Prepared At: 2026-07-13T17:03:12Z (UTC)
Document Status: DRAFT — NOT CANONICAL
Gate Status: HOLD — REVIEW AND VERIFICATION PENDING

## 1. Purpose

Map every Gate-name variant and every competing Gate model found in the
repository (see `STATE02_GATE_INVENTORY_REGISTER_v1.0.md`) against each
other, so the aliasing and overlap is visible in one place instead of
scattered across six documents.

## 2. Architecture Office Model Check (required by task brief)

The task brief asked whether an `00_Architecture_Office/Governance/` or
`00_Architecture_Office/Review_Checklists/` path exists. Both exist and are
real, populated directories:

- `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/Governance/` contains
  `ARCHITECTURE_REVIEW_GATE.md`, `README.md`, `GITHUB_JIRA_SYNC_CONTROL.md`.
- `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/Review_Checklists/`
  contains `ARG_CHECKLIST.md`, `README.md`, `SMEPLUS-ARCHITECTURE-REVIEW-GATE-v0.1.md`,
  and a PDF (`SMEPLUS Architecture Review Gate v0.1.pdf`).

This is therefore **not** a "not found" case for the Architecture Office
model — it is real and is one of the six models catalogued below. However,
two files it references do not exist and are recorded as gaps:
`Security_Review_Checklist.md` and `Integration_Review_Checklist.md`, both
named in `Review_Checklists/README.md` under "Checklists" but absent from the
directory listing (confirmed by `ls`, see Search Execution Log).

## 3. The Letter "Gate A" Problem

The token "Gate A" is used for at least three unrelated things in this
repository:

| Usage | Meaning | Source |
|---|---|---|
| Gate A (Model 2) | Scope Baseline — product boundary, capability map, domain list, AI Owner/reviewer per domain, deliverable list, risk register, principles | `03_Architecture/00_Architecture_Governance/ARCHITECTURE_GATE_MODEL.md` |
| Gate A (Model 3) | Business Approval — Output: Business Scope, Requirement | `01_SaaS_Foundation/ARCHITECTURE_GOVERNANCE.md` §10 |
| (no letter, first item) | Business Gate | `00_Architecture_Office/Review_Checklists/SMEPLUS-ARCHITECTURE-REVIEW-GATE-v0.1.md` |

Model 2's Gate A and Model 3's Gate A are plausibly the same real-world
milestone (both precede an "Architecture" gate and both gate the transition
out of pure business/scope framing) but the two documents were never
reconciled: Model 2 lists 7 required artifacts, Model 3 lists 2 output
artifacts, and neither cross-references the other. This crosswalk does not
merge them — that is a Boss-level decision, logged as an open item in
`STATE02_GATE_CORRECTION_PLAN_v0.1.md`.

## 4. "Architecture Gate" — Three Different Objects, Same Name

| Object | Scope | Source |
|---|---|---|
| GATE-003 | A single named checkpoint in the 10-gate lifecycle list | `QUALITY_GATE_STANDARD.md`, `AI_ROLE_AND_RESPONSIBILITY.md` |
| GATE-030 (Model 2, Gate A–D) | A 4-stage sub-model specific to Architecture work | `ARCHITECTURE_GATE_MODEL.md` |
| GATE-032 (Model 3, Gate A–E) | A 5-stage sub-model specific to Architecture Governance | `ARCHITECTURE_GOVERNANCE.md` §10 |
| GATE-031 | The 5-phase review *process* used to move a design through review | `ARCHITECTURE_REVIEW_GATE.md` |

None of these four documents references any of the other three. A reader
following only `QUALITY_GATE_STANDARD.md` would not learn that "Architecture
Gate" has three separate, more detailed sub-models elsewhere in the
repository.

## 5. "FDS Gate" vs. "Functional Gate" vs. "Functional Design gate" (lower case)

- `QUALITY_GATE_STANDARD.md`, `AI_ROLE_AND_RESPONSIBILITY.md`,
  `ACC-001_L99_REVIEW_GATE_REPORT.md` all use **"FDS Gate"**.
- `SMEPLUS-ARCHITECTURE-REVIEW-GATE-v0.1.md` uses **"Functional Gate"** as a
  distinct list item, never using the string "FDS Gate" anywhere in that
  file.
- Several documents use the lower-case, unhyphenated phrase **"Functional
  Design gate"** as a narrative reference rather than a table entry:
  `12_Traceability/Requirement_Matrix/ACC-001_TRACEABILITY_MATRIX.md`,
  `07_Output_From_AI/ACC-001_EVIDENCE_REGISTER.md`,
  `07_Output_From_AI/ACC-001_GAP_ANALYSIS.md`,
  `17_Functional_Specification_Factory/docs/MODULE_TIERING_STRATEGY.md`.

These three phrasings are very likely the same real gate referred to three
ways, but no document states that equivalence explicitly, so this crosswalk
records it as a probable-alias, not a confirmed one.

## 6. "Release Gate" vs. "Release Readiness Gate" vs. "Production Gate"

Three names cluster around the go-live decision:

- **Release Gate** (GATE-012): `QUALITY_GATE_STANDARD.md`,
  `Governance/README.md`, `Review_Checklists/README.md`.
- **Release Readiness Gate** (GATE-026): only in
  `SMEPLUS-ARCHITECTURE-REVIEW-GATE-v0.1.md`, never elsewhere.
- **Production Gate** (GATE-013): `QUALITY_GATE_STANDARD.md`,
  `APPROVAL_AUTHORITY_MATRIX.md`, `BUILD_READINESS_GATE_REPORT.md`.

`QUALITY_GATE_STANDARD.md` treats Release Gate and Production Gate as two
separate, sequential gates ("Release Gate | Release approval | HOLD" then
"Production Gate | Go-live approval | HOLD"). Since "Release Readiness Gate"
never appears alongside either of these in the same document, this crosswalk
cannot determine whether it is a synonym for Release Gate, a synonym for
Production Gate, or a third, distinct gate that exists in name only. Recorded
as **unresolved alias** in `STATE02_GATE_CORRECTION_PLAN_v0.1.md`.

## 7. "Data Gate" vs. "Data/Migration Gate"

- **Data Gate** (GATE-024) appears once, as an unordered list item, in
  `SMEPLUS-ARCHITECTURE-REVIEW-GATE-v0.1.md`, with no criteria.
- **Data/Migration Gate** (GATE-028) appears three times, always inside the
  identical table row `"Generate migration script | HOLD | Requires
  Data/Migration Gate PASS"`, in
  `00_Master_Templates/SMEPLUS_AI_EXECUTION_TEMPLATE_L99.md`,
  `00_Master_Templates/SMEsPlus L99 Enterprise Master Template Standard v2.0.md`,
  and patch file `0001-fix-l99-split-combined-Master-Template-Standard-v2.0.patch`.

These read as different objects (one a bare list entry, one a specific
build-time precondition), not confirmed as the same gate. No merge is
performed.

## 8. Quality Gate — Document Title vs. Named Checkpoint vs. Closed Instance

The string "Quality Gate" is used three distinct ways:

1. As the **title of the whole governance standard document**:
   `QUALITY_GATE_STANDARD.md` ("Define the quality gate model for SMEsPlus
   Enterprise Suite").
2. As **one named checkpoint inside a 10-gate list**: `Governance/README.md`
   ("6. Quality Gate: Pass code review & testing");
   `Review_Checklists/SMEPLUS-ARCHITECTURE-REVIEW-GATE-v0.1.md` ("6. Quality
   Gate"); `ARCHITECTURE_REVIEW_GATE.md` §8.3 ("Quality Gate — Unit tests
   passing / Integration tests passing / ...").
3. As a **real, closed, dated instance**: `01_SaaS_Foundation/FDS/FDS Phase 2
   Quality Gate.md`, `Status: Approved`, `Decision: Phase 2 is approved as
   Foundation Requirement Baseline v1.0.0.` This is the only document in the
   entire search where a Gate of any kind is recorded as having actually
   reached an approved/closed outcome rather than HOLD/PENDING/PARTIAL.

## 9. GII-003 / GitHub Issue #6 — The Governance Backlog Item This Package Responds To

`STATE02_GITHUB_ISSUE_AUTHORITY_SCAN_ADDENDUM_v0.1.md` lists: `"Issue #6 —
Create State Gate and Domain Gate Crosswalk"`. This is tracked as `GII-003`
in `Step_03_Canonical_RACI/STATE02_RACI_CONFLICT_TO_CORRECTION_MATRIX_v1.0.md`:
`"GII-003 | Issue #6 requires State/Domain Gate crosswalk | GitHub Issue #6 |
Gate ownership crosswalk absent | Gate rows in Canonical RACI Section 3
provide the authority source | Derive gate crosswalk from Canonical RACI
after Boss approval | ... | OPEN"`. It is repeated, still `PENDING`, in
`STATE02_STEP03_STEP04_CROSSWALK_v1.0.md` row `GII-003 (Issue #6 gate
crosswalk)`.

This Step 06 package is a direct attempt to satisfy GII-003, but it is
produced **before** the Canonical RACI has Boss approval, which the GII-003
row explicitly says should happen first ("Derive gate crosswalk from
Canonical RACI **after** Boss approval"). This package therefore cannot close
GII-003; it can only prepare material for GII-003 to be closed once the
Canonical RACI itself clears review, verification, and Boss approval. This
sequencing gap is logged in `STATE02_GATE_CORRECTION_PLAN_v0.1.md`.

## 10. Summary of Unresolved Aliases

| Alias Cluster | Members | Status |
|---|---|---|
| Gate A (business/scope milestone) | Model 2 Gate A; Model 3 Gate A; Business Gate | Probable overlap, not merged |
| Architecture Gate | GATE-003; GATE-030; GATE-032; GATE-031 | Four distinct documents, no cross-reference |
| FDS / Functional | GATE-004; GATE-023; narrative "Functional Design gate" | Probable alias, not confirmed |
| Release / Release Readiness / Production | GATE-012; GATE-026; GATE-013 | Unresolved — could be 2 or 3 distinct gates |
| Data / Data-Migration | GATE-024; GATE-028 | Likely distinct, not merged |
| Quality Gate | Document title; checklist item; closed instance | Three uses, not conflated in this package |
