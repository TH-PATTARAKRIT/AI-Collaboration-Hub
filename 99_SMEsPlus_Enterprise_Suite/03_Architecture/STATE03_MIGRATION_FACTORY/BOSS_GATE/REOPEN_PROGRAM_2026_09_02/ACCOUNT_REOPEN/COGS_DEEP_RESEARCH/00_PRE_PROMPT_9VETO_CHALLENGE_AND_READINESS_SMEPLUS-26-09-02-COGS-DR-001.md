# [SMEPLUS-26-09-02-COGS-DR-001]
# PRE-PROMPT 9 VETO CHALLENGE & READINESS — COGS / Inventory Valuation Deep Research / L9999.9999

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Domain: `ACCOUNTING CORE / COGS / COSTING / INVENTORY VALUATION / ACCOUNTING × INVENTORY INTERFACE`  
Jira: `ERPPLUS-142`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Boss: `Sole Final Approver`  
Control Level: `/L9999.9999`  
Risk: `CRITICAL / CROSS-BACKBONE / FINANCIAL-TRUTH × STOCK-TRUTH`

## 1. Delta Trigger

Boss identified a material prerequisite gap before Accounting × Inventory Final Cross-Proof:

`COGS / Costing / Inventory Valuation Accounting Semantics are not yet deep-researched at menu-by-menu and Periodic-vs-Perpetual depth.`

Inventory Final Solution v1.0 already exposes this as open Joint decisions, including:
- ownership of valuation policy;
- permitted costing methods and change rules;
- Continuous / Periodic valuation timing;
- COGS recognition timing;
- customer-return cost basis;
- late supplier-bill treatment;
- landed-cost eligibility/accounting treatment;
- manufacturing WIP recognition timing.

Therefore this is a material Delta Trigger, not duplicate research.

## 2. Current Evidence Signals

Controlled Inventory evidence states:
- `Inventory emits facts; Accounting decides postings.`
- Inventory Valuation is an Inventory-side Stock/Cost fact, but Accounting owns the financial recognition and classification.
- Inventory Final Solution v1.0 explicitly leaves `JT-01 / JT-02 / JT-03 / JT-04 / JT-05 / JT-06 / JT-08 / JT-09` open.
- Boss-approved Accounting × Inventory 22-Scenario Cross-Proof and 16-field Minimum Handoff Data Contract are now mandatory controls.

External OpenSource reference documentation shows material version-sensitive behavior around:
- Product Category accounting configuration;
- Product-level Income/Expense overrides;
- Periodic vs Perpetual inventory accounting;
- Stock/Valuation/Variation/Expense/COGS accounts;
- Costing methods;
- inventory closing and recognition timing.

Because reference behavior has changed materially across versions, `version drift / false carry-forward` is a first-class research risk.

## 3. 9 Veto Council Challenge

| Track | Mandatory Challenge | Pre-Prompt Verdict |
|---|---|---|
| 01 Audit VETO | Is this new research materially distinct and evidence-required? | `CONTINUE` — Yes; COGS is a documented Joint dependency and prerequisite to interface closure. |
| 02 TBRAC | Will the research distinguish Thai SME reality, periodic closing practice, stock count, accountant workflow and management needs? | `CONTINUE WITH MANDATORY THAI REALITY TRACK` |
| 03 IBPV | Will it prove the full cost lifecycle rather than only list accounts? | `CONTINUE WITH END-TO-END COST FLOW REQUIREMENT` |
| 04 IDTM | Will quantity, cost layer, valuation, original event, reversal and reconciliation identities be traceable? | `CONTINUE WITH IDENTITY / RECONCILIATION REGISTER` |
| 05 IESA | Will Product Category/Product inheritance and SaaS company/tenant boundaries be studied without cloning source architecture? | `CONTINUE WITH CLEAN-ROOM BOUNDARY` |
| 06 Financial/Tax VETO | Will COGS recognition, Inventory Asset, write-down/loss, landed cost, WIP and Periodic/Perpetual be separated correctly? | `CONTINUE — CRITICAL PRIMARY TRACK` |
| 07 Security/Resilience VETO | Will configuration changes, period close, backdating, reversal and override authority be controlled? | `CONTINUE WITH SOD / CHANGE-CONTROL PROOF` |
| 08 Clean-Room/IP VETO | Will menu/source evidence remain Layer-2 benchmark evidence and not become target schema/workflow? | `CONTINUE WITH QUARANTINE + NEUTRAL BUSINESS LEARNING` |
| 09 AI Control VETO | Will AI be prevented from inventing journal logic, cost facts, reconciliation values or unseen source behavior? | `CONTINUE WITH DETERMINISTIC VALIDATION` |

No Blocking Veto exists **before research**. The research itself may later return HOLD/FAIL.

## 4. 9 Special Teams — ACTIVATED

All 9 Special Teams are activated because this work is a critical Accounting × Inventory backbone dependency:

1. `S1 COGS / Financial Accounting` — recognition, classification, gross profit, close.
2. `S2 Inventory Costing` — Standard / Average / FIFO / specific-identification evidence where applicable.
3. `S3 Product Category & Product Accounting Configuration` — field behavior, inheritance, override, precedence, company context.
4. `S4 Periodic Accounting` — purchase expense flow, stock closing, variation, cut-off, reconciliation.
5. `S5 Perpetual Accounting` — inventory asset flow, COGS recognition, interim/variation controls, reconciliation.
6. `S6 Returns / Adjustment / Scrap / Landed Cost` — reversal and non-COGS classifications.
7. `S7 Manufacturing Cost` — RM → WIP → FG → COGS and variance boundaries.
8. `S8 Thai Accounting / Tax / Audit Reality` — authoritative Thai evidence only; unsupported claims remain HOLD.
9. `S9 Migration / Replay / AI Controls` — opening inventory, historical cost, deterministic replay, idempotency and evidence chain.

## 5. Required Research Separation

The New Session must maintain three evidence layers:

`Layer A — OpenSource Reference ERP Observed Behavior`  
`Layer B — Thai Accounting / Tax / Statutory / Audit Evidence`  
`Layer C — SMEsPlus Clean-Room Candidate Semantics`

No Layer A behavior may become Layer C design automatically.
No Layer B rule may be asserted without authoritative evidence.
No vendor-specific implementation structure may become SMEsPlus Core architecture.

## 6. Mandatory Questions Before Any Final Solution Claim

The research must resolve or explicitly HOLD at least:

1. Where the inventory valuation/accounting policy is configured in the reference UI and what the inheritance/override precedence is.
2. Exact observed meaning of Product Category accounting fields.
3. Exact observed meaning of Product → Accounting tab Income Account / Expense Account and when each is used.
4. Periodic vs Perpetual lifecycle from Purchase → Receipt → Vendor Bill → Sale → Delivery → Customer Invoice → Closing.
5. What event recognizes COGS under each observed accounting pattern/version.
6. How Inventory Value reaches Balance Sheet inventory accounts.
7. How Cost is released from Inventory Value to COGS / Cost of Revenue / other approved expense classifications.
8. Which stock decreases are **not** COGS: scrap, loss, write-down, adjustment, production consumption, inter-company, etc.
9. Costing method interaction with recognition timing.
10. Product Category default vs Product override and historical/configuration change impact.
11. Return/reversal cost basis and link to original cost fact.
12. Late supplier bills / landed cost / price difference after goods are partly or fully sold.
13. Period close / stock closing / cut-off / backdating behavior.
14. Manufacturing RM/WIP/FG/COGS boundary.
15. Multi-company/tenant isolation and account-policy ownership.
16. Migration/opening inventory and historical COGS continuity.
17. Reconciliation identities between physical quantity, Inventory valuation, Accounting inventory balance and COGS.
18. Version-delta behavior across relevant OpenSource reference versions; no silent carry-forward.

## 7. Readiness Decision

`READY — ISSUE COGS MENU-BY-MENU DEEP RESEARCH NEW SESSION PROMPT / L9999.9999`

Readiness means only that the research prompt may be issued.
It does **not** mean:
- COGS Final Solution PASS;
- Accounting Final Solution PASS;
- Inventory Final Solution PASS;
- Joint Cross-Proof PASS;
- Team C / Team D / Development / Release / Production authorization.

## 8. Hard Rules

`Understand deeply -> Transfer accurately -> Preserve verifiably.`  
`Do not hand off documents. Hand off verified understanding.`  
`No Evidence = No Progress.`  
`No Evidence Preservation = No Lifecycle Promotion.`  
`No repeated question without a material delta.`  
`No Answer Key Before Research.`  
`Never Skip Gate.`  
`Boss = Sole Final Approver.`
