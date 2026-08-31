> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design) | Boss sole Final Approver
> Session: SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CD-005 | Phase 0 — Governance / Baseline / Evidence Intake

# 01 — TEAM B SCOPE BASELINE AND INPUT REGISTER

## 00 — Purpose

Records what TEAM B verified before design work began: repository/branch/commit state, the exact approved evidence
package consumed, the Boss Gate authorization, and every controlled carry-forward inherited from Team A / the
Independent Evidence Review / the Boss Gate record. This file is the anchor every later TEAM B deliverable in this
folder cites back to.

## 01 — Repository / Branch / Baseline Verification

| Item | Value | Verification method |
|---|---|---|
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` | `git remote -v` — confirmed matches |
| Canonical branch | `SMEsPlus` | `git branch -a` — confirmed exists, tracked |
| Canonical baseline SHA (at prompt creation) | `8f5fa522a3f1a3553584eb5d5063238eec6a88a2` | `git cat-file -t` — confirmed exists as a commit; `git log -1 --oneline` on the checked-out TEAM B branch resolves to this exact commit as HEAD |
| TEAM B working branch | `claude/team-b-group-a-sip-design-005` | Already existed on `origin` before this session (pre-created); checked out locally via `git checkout -B ... origin/...`; contains prior, unrelated TEAM B work for `DOMAIN_01_ACCOUNTING_CORE` — left untouched by this session |
| Working tree state at session start | Clean | `git status --short` — no output |
| Team A evidence branch | `claude/group-a-sales-inventory-purchase-dr002` | `git branch -a` — confirmed exists on `origin` |
| Team A frozen reviewed commit | `8b0993d824cf726fa52edd687272ff54b0977c42` | `git cat-file -t` — confirmed `commit`; evidence files 01–19 + `20_GROUP_A_FINAL_SHA256_MANIFEST.txt` read directly from this commit via `git show <sha>:<path>`, not from a possibly-moved branch tip |
| Independent Evidence Review branch | `audit/group-a-sip-evidence-review-004` | `git branch -a` — confirmed exists |
| Independent Evidence Review commit | `626873c3b924a0350dfd75cf52d276eff6414dd2` | `git cat-file -t` — confirmed `commit`; `08_GROUP_A_EVIDENCE_GATE_RECOMMENDATION_TO_BOSS.md` read from this exact commit |
| Boss Gate commit | `bd9b87f959711d502d0108d6ef4dce098a3bec1a` | `git cat-file -t` — confirmed `commit`, author "TH.PATTARAKRIT SOLUTION SERVICE CO., LTD.", message `boss gate(group-a): approve Sales Inventory Purchase Evidence Gate`; file `GROUP_A_BOSS_EVIDENCE_GATE_APPROVAL_2026-08-31.md` read in full |
| Governance standard | `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/STATE03_PLUS_PRE_PROMPT_INDEPENDENT_CHALLENGE_RULE.md` | Present on `SMEsPlus` HEAD, `Status: BOSS APPROVED / EFFECTIVE`, read in full |

**Finding**: every SHA, branch, and file path named in the governing prompt resolves to a real, readable object in
this repository. Nothing in this baseline required invention or substitution. The TEAM B branch tip (`8f5fa52...`)
is identical to the canonical-baseline SHA the prompt names — the branch has not drifted from the prompt's stated
baseline.

## 02 — Boss Gate Authorization Confirmed

- Decision: `EVIDENCE GATE — PASS / BOSS APPROVED` (Document `SMEPLUS-26-08-31-GRPA-SIP-EG-BOSS-001`, decided
  2026-08-31T11:43+07:00).
- Effect confirmed as read: authorizes entry into `TEAM B — Independent Canonical Domain Design` only. Team C,
  Development, Team D, Formal IBPV, Formal IDTM, Formal IESA, Release, and Production are all explicitly marked
  `NOT AUTHORIZED` / `NOT ACTIVE` in the same record. This TEAM B session does not claim any of those.
- Boss Gate §4 "Mandatory Carry-Forward Controls" (4 items) and §5 "Clean-room / Independence Boundary" — both
  reproduced and honored throughout this design package; see §04 below for the carry-forward register and
  [18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md](18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md) for the
  full disposition of each.

## 03 — Approved Evidence Package Inventoried (Team A Frozen Commit)

All 19 content/report files plus the SHA-256 manifest were read in full from commit `8b0993d824cf726fa52edd687272ff54b0977c42`. None were substituted from a later branch tip.

| # | File | Role |
|---|---|---|
| 01 | `01_SHARED_MASTER_DEPENDENCY_MAP.md` | Party, Product, Category, UOM, Pricing, Tax, Payment Term, Currency, Sequence, Warehouse/Location, Company/Branch, Analytic — shared-master evidence |
| 02 | `02_INVENTORY_CAPABILITY_MODEL.md` | Movement, Reservation/Quant, Picking/Transfer, Backorder, Return, Lot/Serial, Package, Replenishment, Put-away |
| 03 | `03_SALES_CAPABILITY_MODEL.md` | Order lifecycle, quantity quadruple, cancellation, return (absence), stock-vs-service, partial delivery |
| 04 | `04_PURCHASE_CAPABILITY_MODEL.md` | PO lifecycle, real approval gate, orphaned/resolved approval schema, Purchase Request, Requisition/Tendering, receipt quantities |
| 05 | `05_INTEGRATED_E2E_LIFECYCLE_MAP.md` | 12 cross-module scenarios |
| 06 | `06_CROSS_MODULE_EVENT_AND_DEPENDENCY_MAP.md` | Event catalogue by originating module + cross-cutting reads |
| 07 | `07_BUSINESS_FACT_OWNERSHIP_AND_HANDOFF_MATRIX.md` | Fact/owner/event/consumer index |
| 08 | `08_SOURCE_DATABASE_SEMANTIC_TRACEABILITY_MATRIX.md` | Clean/Wide/Orphaned/Conflict DB reconciliation |
| 09 | `09_QUANTITY_SEMANTICS_REGISTER.md` | Canonical quantity register, Sales/Purchase/Inventory |
| 10 | `10_EXCEPTION_PARTIAL_RETURN_CANCELLATION_MATRIX.md` | 20-item exception catalogue |
| 11 | `11_THAILAND_BUSINESS_REALITY_AND_VARIATION_REGISTER.md` | TBRAC-classified Thailand observations |
| 12 | `12_PERSONA_USER_FITNESS_OBSERVATION_MATRIX.md` | Persona/role observations, all Unknown/Requires-Validation |
| 13 | `13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md` | Enforced / not-enforced / symmetric / asymmetric invariant candidates |
| 14 | `14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md` | Master Unknown/Conflict register (post-CORR-003: 0 Critical, 3 High, 10 Medium, 4 Low open) |
| 15 | `15_EXTERNAL_DEPENDENCY_AND_SYSTEM_RISK_OBSERVATION_REGISTER.md` | Accounting/CRM/MRP/Logistics/E-commerce/Payment/Government dependency register |
| 16 | `16_FIT_GAP_CANDIDATE_PACK.md` | Team A's non-binding ADAPT/EXTEND/REJECT/UNKNOWN candidate proposals |
| 17 | `17_GROUP_A_EVIDENCE_MANIFEST.md` | SHA-256 for files 01–16 + two session prompts |
| 18 | `18_TEAM_A_EVIDENCE_GATE_CANDIDATE_REPORT.md` | Team A's own terminal status and gate checklist |
| 19 | `19_TEAM_A_CORRECTIVE_CLOSURE_REPORT.md` | CORR-003 corrective session — closed all 3 original Critical gaps |
| 20 | `20_GROUP_A_FINAL_SHA256_MANIFEST.txt` | External hash covering files 01–19 |
| — | `GROUP_A_BOSS_EVIDENCE_GATE_APPROVAL_2026-08-31.md` (Boss Gate commit) | Boss decision record, §4 carry-forwards, §5 clean-room boundary |
| — | `08_GROUP_A_EVIDENCE_GATE_RECOMMENDATION_TO_BOSS.md` (Independent Review commit) | Independent reviewer's PASS recommendation + 2 corrective notes |

**Local extraction note**: to read this evidence without disturbing the working tree (the files live on a
different branch/commit than the one TEAM B has checked out), each file was extracted read-only via
`git show <frozen-sha>:<path>` into this session's private scratch directory, then read in full. No file under
`TEAM_A/` was modified, moved, or re-committed by this session — confirmed by `git status --short` showing no
changes under that path at any point in this session.

## 04 — Mandatory Carry-Forward Register (§16 of the governing prompt) — Initial Classification

Full disposition detail lives in
[18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md](18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md). Initial
classification recorded here per the governing prompt's explicit instruction that Phase 0 register carry-forwards:

| # | Carry-forward | Initial classification |
|---|---|---|
| 1 | Internal workflow/permission semantics of `sale_order_level_approve`, `purchase_request_level_approve_po`, `purchase_request_level_approve` | `CONTROLLED CARRY-FORWARD` — Boss Gate §4.1 explicitly forbids inventing this; source code confirmed absent from every location on the research machine (Independent Review's own finding, not just Team A's) |
| 2 | `account.fiscal.position` base logic | `CONTROLLED CARRY-FORWARD` — Accounting Core interface dependency only, per §10 of the governing prompt |
| 3 | Orphaned `res.partner` multi-brand/multi-HQ columns | `CONTROLLED CARRY-FORWARD` — real DB columns, zero declaring source found anywhere in Team A's exhaustive grep |
| 4 | Two uncoordinated Thai branch implementations | `CONTROLLED CARRY-FORWARD` — TBRAC-classified, requires real data-profiling/user validation before either is treated as a target requirement |
| 5 | Remaining Medium/Low gaps from `14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md` | Mixed — see full item-by-item disposition in file 18 of this package; none dropped |
| 6 | Real-user validation items from TBRAC evidence (file 11) | `CONTROLLED CARRY-FORWARD` — consolidated into [16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md](16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md) |

Additionally, per Boss Gate §4.2–4.3 (not part of the governing prompt's numbered six, but Boss-mandated and
therefore binding on this session):

| Boss Gate item | Disposition |
|---|---|
| §4.2 — CORR-003 PostgreSQL tooling-version wording discrepancy | Documentation-only; does not affect any TEAM B design decision; no action required from TEAM B |
| §4.3 — Fit-Gap candidate #15's "many SME businesses expect a salesperson-initiated RMA" generalization | Carried forward as `HYPOTHESIS / REQUIRES REAL USER VALIDATION`, never treated as a verified Thai/SME-wide fact anywhere in this design package — see [16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md](16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md) and [17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md](17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md) |

## 05 — Non-Binding Input Confirmation

`16_FIT_GAP_CANDIDATE_PACK.md` (Team A) is read and treated strictly as **non-binding input / challenge material**
per §5 of the governing prompt. TEAM B's own, independently-reasoned classification of every item in that pack is
recorded in
[17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md](17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md),
including every case where TEAM B agrees, disagrees, splits, defers, or reclassifies a Team A candidate.

## 06 — Clean-Room Boundary Statement

TEAM B confirms it will extract only generic business semantics (capability, lifecycle, state, event, ownership,
dependency, exception behavior, control requirement) from the Team A evidence, and will not carry forward any
Odoo/vendor model name, table name, method name, or schema shape as a SMEsPlus target-design name. Where a
source-observed mechanism is judged worth preserving as a *pattern* (e.g., the planned-vs-executed movement split,
the reflective/pluggable replenishment-to-purchase dispatch), the deliverables below name it independently and
state explicitly that only the generic shape, not the vendor implementation, is being adopted.

## 07 — Scope Confirmation

In scope for this session: Business Capability Model, Canonical Business Concept/Fact Model, Domain Boundary
Model, Lifecycle Model, Business State Model, Business Event Model, Fact Ownership Model, Cross-Domain
Handoff/Dependency Model, Quantity/Commitment/Fulfillment Semantics, Exception/Partial/Cancel/Return/Correction
Semantics, Approval/Control/SoD Requirement Model (business-semantic level only), Multi-company/tenant/branch/
warehouse boundary semantics, Accounting/financial interface dependency semantics (handoff only), Thailand/
user-reality validation requirements, Independent Fit-Gap/Design Decision Register, Traceability and Unknown
Register.

Explicitly out of scope and not attempted anywhere in this package: Node.js/production source code, physical DB
DDL, ORM implementation, API/controller/service implementation, deployment/infrastructure design, Accounting Core
internal architecture (COA, GL posting, WHT engine, tax engine, fiscal-position internals, valuation accounting,
AR/AP posting logic), Team C/Team D/Formal IBPV/Formal IDTM/Formal IESA execution, merge to `SMEsPlus`, release,
or any claim of Boss approval or Development readiness for this package.

## 08 — Session Phase Progress Denominator

Per the governing prompt §23: no approved Board/STATE/STEP denominator or STEP binding is evidenced for this
session (`STEP Binding: TBD / BASELINE LINKAGE REQUIRED — DO NOT INVENT` per the prompt header). This package
therefore reports only local session-phase progress (`completed / 13 planned phases`, Phases 0–12 as defined in
the governing prompt) — never an official Board/STATE/STEP percentage. See
[20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md](20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md) for the final count.
