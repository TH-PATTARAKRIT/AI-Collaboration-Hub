# 02 — BOSS DECISION COMPONENT REGISTER (`DC-01`..`DC-10B`, 13 rows)

`No Evidence = No Progress.` `Never Skip Gate.` `Boss is the sole Final Approver.` This register converts `SC-01`..`SC-10` / `ACC-DEC-004`..`ACC-DEC-013` into 13 decision components per governing-prompt §7, splitting `SC-05`, `SC-06` and `SC-08` per §CP-02. It recommends. It does not approve. No row below is pre-filled as approved.

## Summary table

| Component | Source SC | Decision ID | Topic | Evidence pointer status | Owner status | AAS+ recommendation | PMO recommendation | Gate impact | Next prompt pack |
|---|---|---|---|---|---|---|---|---|---|
| `DC-01` | `SC-01` | `ACC-DEC-004` | Fixed assets, depreciation, disposal | Verified | Boss | `RECOMMEND IN — BOSS RULING REQUIRED` | `RECOMMEND IN — BOSS RULING REQUIRED` | No gate defined (COA-G04/G05/G06 side effects) | `PP-06` if ruled IN |
| `DC-02` | `SC-02` | `ACC-DEC-005` | Deferred revenues/expenses, recognition schedules | Verified | Boss | `RECOMMEND IN — BOSS RULING REQUIRED` | `RECOMMEND IN — BOSS RULING REQUIRED` | No gate defined (COA-G04/G05/G06 side effects) | `PP-06` if ruled IN |
| `DC-03` | `SC-03` | `ACC-DEC-006` | Budgets / budgetary positions / budget analysis | Verified | Boss (research owner unassigned regardless) | `RECOMMEND HOLD — EVIDENCE REQUIRED` | `RECOMMEND HOLD — EVIDENCE REQUIRED` | No gate defined | None until Boss ruling |
| `DC-04` | `SC-04` | `ACC-DEC-007` | Treasury / Cash & Bank owner | Partial | Unassigned | `OWNER ASSIGNMENT REQUIRED` | `OWNER ASSIGNMENT REQUIRED` | No gate defined | `PP-07` once owner named |
| `DC-05A` | `SC-05` | `ACC-DEC-008` | Employee expenses, Tax Returns menu, Cash Roundings, WT Certificates | Verified | Boss | `RECOMMEND IN — BOSS RULING REQUIRED` (conditional — see detail) | `RECOMMEND IN — BOSS RULING REQUIRED` (conditional) | No gate defined | None named in `12`; new pack recommended if ruled IN |
| `DC-05B` | `SC-05` | `ACC-DEC-008` | Manufacturing valuation, price difference, inventory write-down | Verified | Joint | `JOINT_SESSION_REQUIRED` | `JOINT_SESSION_REQUIRED` | Account + Inventory Backbone baseline HOLD | `PP-04` |
| `DC-06A` | `SC-06` | `ACC-DEC-009` | VAT/CIT ownership model | Partial | Boss / Legal-Tax | `LEGAL_TAX_REVIEW_REQUIRED` | `LEGAL_TAX_REVIEW_REQUIRED` | `COA-G06` | `PP-03` (prerequisite) |
| `DC-06B` | `SC-06` | `ACC-DEC-009` | `PND1` / `PND54` / `PP36` scope | Partial | Legal-Tax | `LEGAL_TAX_REVIEW_REQUIRED` | `LEGAL_TAX_REVIEW_REQUIRED` | `COA-G06` | `PP-03` |
| `DC-07` | `SC-07` | `ACC-DEC-010` | Approval-before-posting workflow | Verified | Boss | `RECOMMEND HOLD — EVIDENCE REQUIRED` | `RECOMMEND HOLD — EVIDENCE REQUIRED` | `CO-02` | None named in `12`; Team B design at CO-02 once unblocked |
| `DC-08A` | `SC-08` | `ACC-DEC-011` | Analytic / dimension model ownership | Verified | Unassigned | `OWNER ASSIGNMENT REQUIRED` | `OWNER ASSIGNMENT REQUIRED` | `COA-G07` | None named in `12`; new pack recommended once owner named |
| `DC-08B` | `SC-08` | `ACC-DEC-011` | Branch (สาขา) statutory status | Verified | Legal-Tax | `LEGAL_TAX_REVIEW_REQUIRED` | `LEGAL_TAX_REVIEW_REQUIRED` | `COA-G06` / `COA-G07` | `PP-03` |
| `DC-09` | `SC-09` | `ACC-DEC-012` | Financial Reporting design owner | Verified | Unassigned (Team B, sequenced) | `OWNER ASSIGNMENT REQUIRED` | `OWNER ASSIGNMENT REQUIRED` | `COA-G05` | `PP-08`, sequenced behind `PP-02` + `PP-03` |
| `DC-10` | `SC-10` | `ACC-DEC-013` | Standard COA template mechanics (`B13 DT-03`) | Verified | Boss | `RECOMMEND HOLD — EVIDENCE REQUIRED` | `RECOMMEND HOLD — EVIDENCE REQUIRED` | `COA-G04S` | None until Boss ruling — carries forward |

Every row's "Do not proceed to" value is identical: **Final Solution / Functional Design / Development.** No component in this register is ready for any of those three.

## Detail per component

### `DC-01` — Fixed assets, depreciation, disposal
**Boss decision required:** Rule IN / OUT / DEFERRED on fixed-asset, depreciation and disposal accounting as SMEsPlus v1 scope. If IN, assign the asset sub-domain owner inside Accounting Core (currently `UNASSIGNED`) and authorize Pack `PP-06`.
**Evidence link:** `12_ASSET_DEFERRED_RECOGNITION_MAP.md` (deep-study package) — full 12-row Thai asset-model template (`account.asset-th.csv`), 22 `asset_fixed` + 6 `asset_non_current` template accounts already instantiated (§3, `FT-02`); `UK-02` records the scope question itself as still open.

### `DC-02` — Deferred revenues/expenses, recognition schedules
**Boss decision required:** Rule IN / OUT / DEFERRED on deferred-revenue/expense recognition-schedule design as v1 scope. If IN, sequence behind `DC-01`'s owner assignment — both feed the same `PP-06` research pass (`10` §A), and the deferral sub-scope should specifically wait for this ruling per `10` §A's own sequencing note.
**Evidence link:** `12_ASSET_DEFERRED_RECOGNITION_MAP.md` §4 (deferral lifecycle `DF-01`..`DF-07`); `FT-03`/`FT-04` record that the Thai template has zero Prepayments-type accounts and no general deferred-revenue account — a real design gap, not a benchmark-absence-only question.

### `DC-03` — Budgets / budgetary positions / budget analysis
**Boss decision required:** Confirm whether Section 6.8 budget scope reflects an actually-felt Thai SME need before ruling IN, given three evidentiary weaknesses not present for `DC-01`/`DC-02`: (a) `account_budget` is **not installed** in the benchmark instance at all — zero benchmark behavior evidence exists, vs. Assets/Deferred's fully-populated 144-row template; (b) the deep-study package classifies budget menus `Conditional`, not `Mandatory`; (c) no research owner exists even provisionally (`UNASSIGNED`, not merely unnamed-pending-ruling). This is why the AAS+/PMO recommendation differs from `DC-01`/`DC-02` despite an identical "Boss lists it, no gate covers it" starting posture in the source register.
**Evidence link:** `13_ANALYTIC_BUDGET_MANAGEMENT_REPORT_MAP.md` §4 and `UK-03` ("Budget scope: Boss Section 6.8 lists budgets; file 02 says Conditional; benchmark instance lacks `account_budget`").

### `DC-04` — Treasury / Cash & Bank owner
**Boss decision required:** Name a Treasury owner (Team B / Treasury-specific role). The scope itself — bank journals, Thai bank statement-import formats, reconciliation, cheques, PromptPay, bank feeds, and a PDPA review of bank-data handling — is not in dispute; only the owner is missing.
**Evidence link:** `10_RESEARCH_ROUTING_AR_AP_ASSET_TREASURY_REPORTING.md` §B; independently corroborated by this session's own reading of `17_AI_AUDIT_SMEPLUS_9_VETO_CHALLENGE.md` VC-03 ("Ownerless handoffs exist: `HO-11`/`HO-12` (Treasury, 'not yet designed')") — this closes the `ST-03` citation-depth gap the cross-check package flagged as `UNKNOWN / RESEARCH REQUIRED`.

### `DC-05A` — Employee expenses, Tax Returns menu, Cash Roundings, WT Certificates
**Boss decision required:** Rule IN / OUT / DEFERRED for these four Boss-track sub-items as Accounting-owned scope. The recommendation is conditional (not an unqualified IN) because evidence quality differs across the four: the HR-expense handoff is concretely mapped (`HO-31`, "Employee expense report -> expense + employee payable (HR -> Accounting)"), but Tax Returns/Cash Roundings/WT Certificates menus are evidenced only at the menu-label level, with WT Certificates specifically flagged as having no Thai translation installed in the benchmark at all (a UX-fitness finding, not a scope finding).
**Evidence link:** `A1` §C.4 (deep-study); `08` objections 5–6; `04` `HO-31` (deep-study `04_ACCOUNT_PROCESS_HANDOFF_MAP.md`, cited by the boss-decision package's `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` row `ACC-DEC-008`).

### `DC-05B` — Manufacturing valuation, price difference, inventory write-down
**Boss decision required:** Convene Account x Inventory Joint Session 3 (`ACC-DEC-019`). These three sub-items are Joint agenda items 6 (manufacturing) and 7 (price difference), cross-referenced to inventory write-down (`08` `SC-20`). The Boss ruling needed here is to *convene*, not to scope-rule directly — closure from the Account side alone is explicitly disallowed (`07_ACCOUNT_INVENTORY_JOINT_SESSION_3_ROUTING_BRIEF.md`, "What this brief does not do").
**Evidence link:** `07_ACCOUNT_INVENTORY_JOINT_SESSION_3_ROUTING_BRIEF.md` §Mandatory agenda coverage items 6–7; `20_GAP_OWNER_GATE_IMPACT_REGISTER.md` §D.

### `DC-06A` — VAT/CIT ownership model
**Boss decision required:** Commission the Legal-Tax review (`ACC-DEC-014`) before ruling whether Accounting Core or a separate Tax domain owns VAT/CIT. `17_AI_AUDIT_SMEPLUS_9_VETO_CHALLENGE.md` `VC-06` finds VAT and CIT research "remain zero" and that the benchmark's own exempt-input-VAT template "contradicts its own Thai description" — an ownership ruling made now would rest on unreviewed, internally-inconsistent source material.
**Evidence link:** `06_LEGAL_TAX_REVIEW_BRIEF.md` §B (VAT-1..VAT-6), §C (CIT-1..CIT-5); `17` `VC-06`.

### `DC-06B` — `PND1`/`PND54`/`PP36` scope
**Boss decision required:** Same commissioning decision as `DC-06A`. `PND1` (`WHT-7`), `PND54` (`WHT-8`) and `PP36` (`WHT-9`) scope status is explicitly `LEGAL_TAX_REVIEW_REQUIRED` in `06_LEGAL_TAX_REVIEW_BRIEF.md` §A — these forms sit in the Thai chart template but are not in any approved scope list.
**Evidence link:** `06_LEGAL_TAX_REVIEW_BRIEF.md` §A rows `WHT-7`/`WHT-8`/`WHT-9`.

### `DC-07` — Approval-before-posting workflow
**Boss decision required:** Rule IN / OUT on the `ACC-004` draft approval-before-posting workflow. `17_AI_AUDIT_SMEPLUS_9_VETO_CHALLENGE.md` `VC-07` records this is "assumed in the close checklist but scoped by nobody" (`OBJN-07`). Recommend Boss tie the ruling explicitly to `CO-02` (segregation of duties) before Team B designs at `CO-02` — an IN ruling issued without that linkage risks the same control being designed twice.
**Evidence link:** `14 OBJN-07` (deep-study, cited via `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` row `ACC-DEC-010`); `17` `VC-07`.

### `DC-08A` — Analytic / dimension model ownership
**Boss decision required:** Name an owner for the analytic/dimension model inside Accounting Core (Team B DOMAIN_01). `13_ANALYTIC_BUDGET_MANAGEMENT_REPORT_MAP.md` §8 finding 4 records this area is "currently owned by nobody in the design chain" — Team A calls it "partially in scope" while Team B's own boundary model does not name it as a neighbour at all.
**Evidence link:** `13_ANALYTIC_BUDGET_MANAGEMENT_REPORT_MAP.md` §1 `M-ANA-01`..`04`, §8 finding 4.

### `DC-08B` — Branch (สาขา) statutory status
**Boss decision required:** Commission Legal-Tax review of whether branch (สาขา) is a per-branch VAT-filing unit (a statutory attribute, `06` `DBD-6`) or a management dimension under `COA-G07`'s "prefer dimensions" default. Until answered, `13_ANALYTIC_BUDGET_MANAGEMENT_REPORT_MAP.md` §2 `DIM-02` stays explicitly `HOLD / EVIDENCE REQUIRED`, and this is the same undecided fact flagged as `UK-01` in that file.
**Evidence link:** `13_ANALYTIC_BUDGET_MANAGEMENT_REPORT_MAP.md` §2 `DIM-02`, `UK-01`; `06_LEGAL_TAX_REVIEW_BRIEF.md` §D `DBD-6`.

### `DC-09` — Financial Reporting design owner
**Boss decision required:** Name a Team B Financial Reporting owner. Per `10_RESEARCH_ROUTING_AR_AP_ASSET_TREASURY_REPORTING.md` §C, the design *work* must not start before `COA-G01` clears and the Legal-Tax review returns DBD statement-format evidence (`06` §D `DBD-1`/`DBD-2`) — but naming the owner now still removes the "who" blocker while the "when" blocker (`COA-G01`, Legal-Tax) is worked in parallel via `PP-02`/`PP-03`.
**Evidence link:** `09 RU-08` (deep-study, cited via `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` row `ACC-DEC-012`); `10` §C.

### `DC-10` — Standard COA template mechanics (`B13 DT-03`)
**Boss decision required:** Rule APPROVE / REJECT / MODIFY on `B13 DT-03` standard COA template mechanics. `17_AI_AUDIT_SMEPLUS_9_VETO_CHALLENGE.md` `VC-05` records this "remains explicitly unapproved... unchanged," carrying forward from a prior round. Recommend Boss review this alongside the Legal-Tax findings on statutory depreciation rates/lives (`12` §6 `LT-01`..`LT-03`) and TFRS-for-NPAEs alignment — every one of the 12 asset-class template rows underlying the mechanics question is individually tagged `COA-G06 LEGAL_TAX_REVIEW_REQUIRED` (`12` §2). An APPROVE issued now would fix mechanics before the underlying Thai statutory basis is reviewed.
**Evidence link:** `17 VC-05` (deep-study, cited via `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` row `ACC-DEC-013`); `12_ASSET_DEFERRED_RECOGNITION_MAP.md` §2, §6.

## Explicit non-claim

No component above is ruled IN, OUT, DEFERRED, APPROVED, REJECTED, or MODIFIED by this register. No owner is assigned. No gate is opened, closed, or moved. This register only converts the existing 10-row `SC` scope register into 13 tracked decision components with a recommendation for Boss to rule on, per governing-prompt §5's authority boundary.
