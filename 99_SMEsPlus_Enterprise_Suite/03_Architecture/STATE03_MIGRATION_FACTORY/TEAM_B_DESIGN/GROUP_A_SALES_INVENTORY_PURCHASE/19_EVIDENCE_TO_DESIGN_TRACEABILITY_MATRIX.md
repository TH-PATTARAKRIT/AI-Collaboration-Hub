> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 12 — Traceability / Completeness

# 19 — EVIDENCE TO DESIGN TRACEABILITY MATRIX

## 00 — Method

Two views: (1) a deliverable-level index mapping each TEAM B file to the Team A evidence files it draws from,
and (2) worked examples in the governance-required chain format
(`Evidence → Business Semantic → TEAM B Decision → Confidence`) for the design package's most consequential
decisions.

## 01 — Deliverable-to-Evidence Index

| TEAM B deliverable | Primary Team A evidence sources | Boss Gate / Independent Review inputs |
|---|---|---|
| 01 Scope Baseline / Input Register | All 19 files + `20_...MANIFEST.txt` (inventoried) | Boss Gate approval record; Independent Review recommendation |
| 02 Capability / Domain Boundary Model | `01`, `06`, `07` | Boss Gate §5 clean-room boundary |
| 03 Business Fact / Concept Catalog | `01`, `07`, `09` | — |
| 04 Shared Master Boundary Model | `01` (all sections) | Boss Gate §4.1/§4.3 |
| 05 Inventory Core Canonical Design | `02`, `09` (Inventory rows), `13` §01 | — |
| 06 Sales Canonical Design | `03`, `09` (Sales rows), `13` §04 | Boss Gate §4.3 |
| 07 Purchase Canonical Design | `04`, `09` (Purchase rows), `13` §04 | Boss Gate §4.1 |
| 08 Integrated E2E Lifecycle / State Model | `05`, `06`, `07` §06 | — |
| 09 Canonical Business Event Catalog | `06` | — |
| 10 Fact Ownership / Handoff Matrix | `07` | — |
| 11 Quantity/Commitment/Fulfillment Semantics | `09` | — |
| 12 Exception/Partial/Cancel/Return/Correction Model | `10`, `13` §02 | — |
| 13 Approval / Control / SoD Model | `04` §03, `07` §04, `14` (Critical #1 lineage) | Boss Gate §4.1 (governing) |
| 14 SaaS / Multi-Company / Tenant Boundary | `01` §12, `05` Scenario 11 | — |
| 15 Accounting / External Interface Model | `07` §03, `15` §01/§06/§07 | — |
| 16 Thailand / User-Reality Register | `11`, `12` | Boss Gate §4.3 (governing) |
| 17 Fit-Gap / Design Decision Register | `16` (all items) | — |
| 18 Unknown / Conflict / Carry-Forward Register | `14` (all tiers) | Governing prompt §16 (governing) |
| 19 (this file) | All of the above | — |
| 20 IBPV Readiness Report | All of the above | Boss Gate; Independent Review |
| 21 SHA-256 Manifest | This folder's own files | — |

## 02 — Worked Examples (Governance-Required Chain Format)

```
Evidence: `02` §04 MOV-31, precision-corrected by CORR-003 to an all-or-nothing whole-recordset guard
→ Business Semantic: "cannot cancel already-executed physical work" is a real invariant; "an entire batch
  blocked by one executed member" is an implementation defect, not a business rule
→ TEAM B Decision: adopt the invariant, correct the defect — require per-instruction evaluation
→ Confidence: VERIFIED FACT (evidence) + SUPPORTED INFERENCE (that per-instruction evaluation is the correct
  target behavior — no counter-evidence found, and the correction directly serves the audit-integrity goal
  every other TEAM B decision in this package protects)
→ Recorded in: 12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md §07
```

```
Evidence: `04` §03 (full cross-model approval-schema investigation, CORR-003 resolution)
→ Business Semantic: a real, historically-used, sequential multi-level approval control exists on at least one
  document type, with unverifiable internal logic
→ TEAM B Decision: design the vendor-neutral shape (EXTEND); explicitly HOLD the internal logic per governing
  prompt §11's mandatory Unknown control
→ Confidence: RESOLVED — ACTIVE HISTORICAL CONTROL WITH OWNERSHIP EVIDENCE (evidence) / HOLD (internal logic)
→ Recorded in: 13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md §03 (APR-002)
```

```
Evidence: `03` §05 SRET-01..08, `04` §07 POL-29/30 (both full-file-grep negative)
→ Business Semantic: Return/Reversal belongs to Inventory regardless of commercial origin — the single most
  exhaustively-confirmed finding in the whole evidence package
→ TEAM B Decision: ADAPT in full as a hard domain-boundary rule; Sales/Purchase RMA-initiation affordance left
  explicitly open, not resolved by an unsourced generalization (Boss Gate §4.3)
→ Confidence: VERIFIED FACT (both structural mechanism and its commercial-side absence)
→ Recorded in: 05_INVENTORY_CORE_CANONICAL_DESIGN.md §05; 17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md item 15
```

```
Evidence: `01` §02 PTY-17..21, `01` §12 CO-15..24 (two uncoordinated Thai branch modules; orphaned multi-brand
  columns)
→ Business Semantic: real customization exists but is internally uncoordinated and partially unexplained
→ TEAM B Decision: canonical Party model treats Tax-Branch as one attribute (REJECT the duplication pattern);
  multi-brand/HQ capability NOT designed (CONTROLLED CARRY-FORWARD, not invented)
→ Confidence: VERIFIED FACT (columns exist) / EVIDENCE_MISSING (origin/purpose of several columns)
→ Recorded in: 04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md §01; 18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md §01/§02
```

## 03 — Vendor-Contamination Check

TEAM B independently re-scanned this folder's own 21 files for any Odoo/vendor model name, table name, or method
name used as a SMEsPlus target-design term (a clean-room compliance self-check, per Boss Gate §5). Result: no
deliverable in this folder names a target concept using a source model/table/method name — every canonical
concept (Movement Instruction/Execution, Stock Position, Transfer Operation, Fulfillment Continuation, Reversal,
Commercial Commitment, Supply Commitment, Financial Handoff, Approval Control, etc.) is independently named.
Vendor terminology appears only inside evidence citations (quoted, attributed to the Team A file/section it came
from) and inside explicit "the reference system does X" observation sentences — never as a target-design noun.

## 04 — Carry-Forward Completeness Check

Cross-checked against [18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md](18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md):
every item in Team A's Unknown/Conflict/Evidence Gap Register (post-CORR-003: 0 Critical, 3 High, 10 Medium, 4
Low) and every item in the governing prompt's mandatory six-item carry-forward list has a recorded disposition.
No item was silently dropped between the evidence package and this design package.

## 05 — Internal Coherence Check

Cross-references between files 02–18 were verified to resolve to real section anchors within this folder (not to
non-existent sections) as each file was authored sequentially, building on the prior files' established
vocabulary (Movement Instruction/Execution, Stock Position, Commercial/Supply Commitment, Financial Handoff,
Approval Control, Tenant/Company/Branch) rather than introducing competing terms for the same concept in
different files.
