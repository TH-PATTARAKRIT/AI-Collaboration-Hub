# STATE02_GATE_DEPENDENCY_MATRIX_v1.0.md

Session: SMEPLUS-26-07-13-GATE01
State: 02 — Governance
Step: 06 — Gate Crosswalk
Prepared By: Claude AI (Responsible role only)
Prepared At: 2026-07-13T17:03:12Z (UTC)
Document Status: DRAFT — NOT CANONICAL
Gate Status: HOLD — REVIEW AND VERIFICATION PENDING

## 1. Scope and Honesty Statement

Only 12 of the 37 Gate IDs in `STATE02_GATE_INVENTORY_REGISTER_v1.0.md` are
classified FOUND (i.e., have stated criteria/owner). Of those 12, only the
core lifecycle sequence (GATE-001 through GATE-013, minus the
standalone/bundled duplicates) has an explicitly stated *order*. The
remaining FOUND gates (GATE-020 Code Review Gate, GATE-029 State Gate,
GATE-030/031/032 Architecture sub-models) each have internal sequencing but
are not stated anywhere to depend on, or block, the core lifecycle sequence.
PARTIAL and NOT FOUND gates have no stated dependency at all — inventing one
would not be honest, so none is recorded for them.

## 2. Dependency Set A — Core Lifecycle Sequence

Source: identical ordering independently confirmed in
`00_Project_Governance/QUALITY_GATE_STANDARD.md` (table order) and
`07_Output_From_AI/Repository_Audit_2026-07-05/BUILD_READINESS_GATE_REPORT.md`
("Gate 1" through "Gate 7", consolidated table).

| Upstream Gate | Downstream Gate | Stated Basis |
|---|---|---|
| GATE-001 Governance Gate | GATE-002 Repository Gate | Table order in `QUALITY_GATE_STANDARD.md`; both listed PASS WITH CONTROL/AMBER before Architecture in the same document |
| GATE-002 Repository Gate | GATE-003 Architecture Gate | `BUILD_READINESS_GATE_REPORT.md`: "Gate 1 — Repository Structure" precedes "Gate 2 — Architecture Foundation" |
| GATE-003 Architecture Gate | GATE-004 FDS Gate | `BUILD_READINESS_GATE_REPORT.md`: "Gate 2" precedes "Gate 3 — Functional Design (FDS)" |
| GATE-004 FDS Gate | GATE-005 SDS Gate | `QUALITY_GATE_STANDARD.md` Gate Principles: "Build is not allowed until FDS, SDS, API, DB, UX, QA and Traceability gates pass" (FDS named before SDS) |
| GATE-005 SDS Gate | GATE-006 API/DB/UX Gate | `QUALITY_GATE_STANDARD.md` table order: SDS Gate row precedes API/DB/UX Gate row |
| GATE-006 API/DB/UX Gate | GATE-010 QA/UAT Gate | `BUILD_READINESS_GATE_REPORT.md`: "Gate 4 — SDS/API/DB Content" precedes "Gate 5 — QA/UAT" |
| GATE-010 QA/UAT Gate | GATE-011 Build Gate | `AI_ROLE_AND_RESPONSIBILITY.md` line 159: "QA / UAT Gate ... Must pass before Build Gate" |
| GATE-011 Build Gate | GATE-012 Release Gate | `QUALITY_GATE_STANDARD.md` table order: Build Gate row precedes Release Gate row |
| GATE-012 Release Gate | GATE-013 Production Gate | `QUALITY_GATE_STANDARD.md` table order: Release Gate row precedes Production Gate row; also `BUILD_READINESS_GATE_REPORT.md`: "Gate 6 — Build Gate" precedes "Gate 7 — Production Gate" (Release Gate is not separately numbered in the audit report — see Section 4) |

This is a **single linear chain of 9 edges over 9 nodes**, GATE-001 through
GATE-004, then GATE-005/006 (API/DB/UX as one bundled step), then GATE-010,
GATE-011, GATE-012, GATE-013. No branching and no stated re-entry to an
earlier gate is present in either source document.

## 3. Dependency Set B — Independent Sub-Models (not linked to Set A)

Each of these has an internally stated sequence but is never stated to feed
into, or depend on, Dependency Set A or any other sub-model.

**GATE-030 (Architecture Gate Model A–D):**
Gate A (Scope Baseline) → Gate B (Architecture Baseline) → Gate C (Build
Ready) → Gate D (Release Ready). Explicit statement: "Gate A does not
authorize feature build." (3 edges, 4 nodes, linear.)

**GATE-032 (Architecture Governance §10, Gate A–E):**
Gate A (Business Approval) → Gate B (Architecture Approval) → Gate C (Design
Approval) → Gate D (Development Ready) → Gate E (Production Ready). Order is
implied by document sequence (§10 lists them A through E in that order,
outputs building on each other) but the document does not use explicit
"must pass before" language for this list, unlike GATE-030. (4 edges, 5
nodes, linear, weaker evidentiary basis than GATE-030.)

**GATE-031 (Architecture Review Gate 5-phase process):**
Proposal → Initial Review → Technical Review → Architecture Review →
Executive Approval → Implementation (post-approval: Implementation Gate →
Code Review Gate → Quality Gate, per §8). Explicit "Outcomes" fields per
phase ("PASS: Proceed to Technical Review", etc.) (5 main edges + 2
post-approval edges = 7 edges, 8 nodes, linear.)

**GATE-029 (State Gate, States 01–12):**
State 01 → State 02 → ... → State 12, per row order in
`STATE_GATE_MATRIX.md`. The document does not state explicit inter-state
"must pass before" language (unlike the Set A chain), but row order and the
State numbering itself is the only basis available. (11 edges, 12 nodes,
linear, weakest evidentiary basis of the four sub-models — recorded as
inferred-from-order, not asserted-in-text.)

## 4. Known Gap: GATE-012 (Release Gate) Absent From the Audit-Report Numbering

`BUILD_READINESS_GATE_REPORT.md` numbers exactly 7 gates (Repository,
Architecture, Functional Design, SDS/API/DB Content, QA/UAT, Build,
Production) and does not include a numbered "Release Gate" step, even though
`QUALITY_GATE_STANDARD.md` lists Release Gate as a distinct row between Build
Gate and Production Gate. This crosswalk does not resolve the discrepancy; it
is recorded here and in `STATE02_GATE_CORRECTION_PLAN_v0.1.md` as an open
item.

## 5. Total Edge Count for Circularity Check

Set A: 9 edges. Set B: GATE-030 (3) + GATE-032 (4) + GATE-031 (7) + GATE-029
(11, inferred) = 25 edges. Combined total: **34 directed edges across 5
independent, non-intersecting graphs** — Set A, GATE-030, GATE-032,
GATE-031, and GATE-029 (Set A and the four Set B sub-models share no
common nodes, since no document states an edge between them). The prior
version of this section undercounted the graph total as 4 by omitting Set
A itself from the graph count while still including its 9 edges in the
total; corrected 2026-07-14 (Step 06 P1 correction). This edge set is the
input to `STATE02_GATE_CIRCULAR_DEPENDENCY_REPORT_v1.0.md`.
