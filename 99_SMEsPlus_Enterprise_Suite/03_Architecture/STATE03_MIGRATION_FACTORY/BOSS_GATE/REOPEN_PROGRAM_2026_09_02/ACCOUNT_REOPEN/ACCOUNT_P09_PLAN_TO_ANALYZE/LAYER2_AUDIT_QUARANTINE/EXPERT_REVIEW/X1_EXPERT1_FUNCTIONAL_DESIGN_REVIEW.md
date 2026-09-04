# X1 — AAS-03 EXPERT 1 · FUNCTIONAL DESIGN · ADVERSARIAL REVIEW
**LAYER 2 — AUDIT QUARANTINE.** Session SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001.
Independent reviewer, disjoint assignment, instructed to disprove rather than agree, and instructed to report any wrong path in its own brief as a finding.

## A. CORRECTIONS RETURNED AGAINST THE RESEARCH TEAM

**COR-REV-01 — narrows EV-P09-025.** The "no ledger link at module level" claim is correct but must not be read as "analytic lines are a homogeneous population that can be summed". The reviewer independently established that the record asserts at least **five** structurally different business facts across its real producers. E00 documented the base model correctly but nowhere stated that the meaning of the amount and the quantity is producer-specific and non-comparable.

**COR-REV-02 — closes a class-C residue in EV-P09-019 by transcription.** The reporting grouping map is exactly four entries: `account_move_line`, `purchase_order_line`, `account_asset`, `hr_expense` (`analytic/models/analytic_mixin.py:141-144`). E00 cited the map without transcribing it; the "exactly four, no more" sub-claim is now class **A**.

**COR-REV-03 — generalises COR-P09-05.** The discarded ledger link is not an isolated inventory-valuation fact; it is one instance of a broader pattern in which one business event produces independently-created management records through several code paths, at least one of which structurally cannot carry the link.

**COR-REV-04 — new fact E00/E01 did not surface.** `project_account/models/project_project.py:128-131` carries a source comment admitting its own domain is incomplete and depends on a downstream module patching it (`sale_timesheet/models/project_project.py:512-517`). **In a deployment with timesheets and project accounting but without the sales-timesheet bridge, timesheet-produced management records fall into a generic "other costs" bucket, unlabelled as labour.** Class A.

**Path finding returned against the brief.** The reviewer could not locate the tenant custom roots (its brief named only the two reference roots) and correctly declared class **C — not searched, because not found** rather than asserting absence. It also flagged that its own `ls` of the reference root returned 797 entries against E00's 790 manifests, and declined to call E00 wrong without running E00's method. **Both figures are correct measurements of different units** — 790 module manifests, 797 directory entries including non-module files. Recorded in `P09_REVISION_LOG` §R3.

## B. NEW FINDINGS

**X1-01 — one management record asserts at least five non-equivalent facts.**
1. ledger-attested share — `account/models/account_move_line.py:3174-3206`; amount = −balance × share, link set, category invoice/vendor_bill/other.
2. labour-time fact with no ledger correlate — `hr_timesheet/models/hr_timesheet.py` `_timesheet_postprocess_values`; amount = −quantity × employee hourly cost, converted at the record's own date; the class never sets the link, the general account, or a distinguishing category.
3. recomputed shadow of a posted valuation, deliberately unlinked — `stock_account/models/stock_move.py:557-606`; amount derived from the posted entry's own rows, builder at `:594-606` has no link key.
4. machine-hour estimate computed twice per event from two rate bases — see X1-04.
5. the budget's achieved figure re-derives a sixth meaning by re-filtering (2)+(3)+(4) through account-type and category heuristics that do not match how project profitability filters the identical rows — see X1-06.
**There is no invariant beyond "a signed amount attached to a set of axis columns."**

**X1-02 — the category field is a non-discriminator except in one place.** Full enumeration of every contribution: `other` (`analytic/models/analytic_line.py:202-205`), `invoice`/`vendor_bill` (`account/models/account_analytic_line.py:45`), `manufacturing_order` (`mrp_account/models/analytic_account.py:79`), `picking_entry` (`project_stock_account/models/account_analytic_line.py:9`). `NOT FOUND IN SCOPE: hr_timesheet/**/*.py, pattern "category"` — class **A**, whole module read. A manually posted ledger-linked entry with an allocation and a ledger-less timesheet record both carry `other`. The field's only load-bearing use is at `project_account/models/project_project.py:133-139`, excluding two categories from a generic bucket to prevent one specific double-count.

**X1-03 — the project↔axis binding is optional, many-to-one capable, and orphans history on reassignment.** `project/models/project_project.py:93` — the axis field is **not required**, and the mixin constraint that would require at least one axis is explicitly overridden to do nothing at `:1005-1008`. `_inverse_company_id` at `:249-264` branches on a count greater than one, so **the model expects several projects to share one axis value**. `write()` (`:539-609`, read in full) has no guard preventing the axis being changed once management records exist — contrast `:261`, which does check for existing records, but only for the company field. On deletion (`:611-619`) an axis value with no records is auto-deleted; one with records survives detached. Class A.

**X1-04 — one work-order duration change produces two independently created management records at potentially different axis values, both tagged with the same category.** Work-centre path: `mrp_account/models/mrp_workorder.py:13-21` → `:49-54`, value = −hours × work-centre rate, against the **work centre's own** allocation. Employee path: `project_mrp_workorder_account/models/mrp_workcenter_productivity.py:9-14` → `:34-40`, amount = −duration × employee cost, against the **project's** allocation. The profitability section at `project_mrp_account/models/project_project.py:30-37` aggregates by axis value and category with **no filter distinguishing the two buckets**. If a work centre's allocation is configured to include the project's axis value — which nothing prevents — the same hour is counted twice at two different rates. Mechanism class A; whether it fires is configuration-dependent — **NOT DECIDABLE FROM SOURCE**.

**X1-05 — the budget match join has no exclusivity guard: one management record can be counted as achieved against several budget lines at once.** `account_budget/reports/budget_report.py:49-93`, join condition at `:67-70` and `:88-92`, per axis column: `(bl.<col> IS NULL OR aal.<col> = bl.<col>)`, ANDed. A plain outer join, no distinct-on, no window limit. `budget_line.py` and `budget_analytic.py` read in full: **no uniqueness or non-overlap constraint across budget lines**, only a single line's own date-order check at `budget_line.py:49-53`. Two budget lines with overlapping windows and complementary blank axis columns both match the same record, and the view emits two rows carrying the **same record id** with **two different budget line ids**, each carrying the full unscaled amount; the consumption computation at `budget_line.py:60-74` groups by budget line and sums. **Both lines independently show the full amount as achieved.** Mechanism class A; whether any live configuration triggers it is a data question.

**X1-06 — a blank axis column on a budget line is a wildcard, not "not applicable", and this differs from how project profitability scopes the same records.** Budget: `budget_report.py:88-92` and `:152-156`, `IS NULL OR equal` per column. Profitability: `project_account/models/project_project.py:128-131`, a single strict equality. **The two reporting surfaces resolve "which records belong to this cost object" by structurally different rules**, so a project's own profitability total and that project's budget achieved total are not computed over the same row set even before any double-count. Class A.

**X1-07 — the achieved filter is engineered to sweep in ledger-less records.** `budget_report.py:73-84`: when the account type does not resolve — true for every ledger-less producer — an expense budget captures the record if its category is not in (invoice, other) **or** it is category `other` with a negative amount. Timesheets are category `other` with negative amounts; manufacturing and picking categories are not in that pair. **All three ledger-less producer families are captured as budget consumption by construction.** Class A.

**X1-08 — internal inconsistency between two models inheriting the identical mixin.** The budget line does **not** override the at-least-one-axis constraint, so a budget line cannot exist without an axis; a project **can** exist with none (X1-03). Class A.

**X1-09 — the residual and zero-drop rules are not specific to inventory valuation.** `stock_account/models/analytic_account.py:9-30` is a single shared routine called from `stock_move.py:588-589`, `mrp_account/models/mrp_workorder.py:52`, and `project_mrp_workorder_account/models/mrp_workcenter_productivity.py:37-38`. EV-P09-105/106 therefore govern every producer routed through it. Class A — **widens the stated scope of two E01 findings**.

## C. ADVERSARIAL VERDICTS

### CH-CAND-03 — **CONFIRMED** (upgraded from PLAUSIBLE)
Traced end to end in `account_auto_transfer/models/transfer_model.py` (532 lines, read in full): start date derived from the last **posted** generated entry plus one day (`:224-230`); the forward walk only goes forward (`:139-161`); the regeneration lookup can only find a **draft** entry (`:208-222`); source rows are filtered by transaction date, not by posting timestamp (`:163-177`). A row dated inside an already-posted period but posted afterwards is never picked up, and no mechanism re-opens a posted period. The remaining three module files (10/14/11 lines) were read in full and contain no compensating logic. **Adversarial attempt to disprove:** the only escape is a manual reset of the generated entry to draft, which is a human act outside the mechanism and does not disprove the claim as stated. Class A for the code path; the operational consequence was not executed.

### CH-CAND-04 — **CONFIRMED** (upgraded from PLAUSIBLE) and sharpened
Every step read in full:
1. filter domain — `transfer_model.py:394-398`, containment on the allocation field;
2. what that operator compiles to — `analytic/models/analytic_mixin.py:63-91`, an array-overlap test between **all** the allocation's key ids and the requested ids; `_query_analytic_accounts` at `:44-48` extracts only the keys and **discards the values entirely**, so the percentage never enters the query;
3. the aggregation — `transfer_model.py:400-411`, full summed balance, passed whole to the destination row builder.
**No step multiplies by the matched share.** A row allocated 10 % to an axis value, with a balance of 1000, transfers 1000.
`NOT FOUND IN SCOPE: account_auto_transfer/**/*.py, pattern "analytic_distribution"` beyond the two cited sites — class **A**, whole module.
**Sharpening the research team's language:** the complementary unfiltered bucket excludes the same rows in full (`:275-279`, negated containment), so this is **not a duplication — it is a misallocation**, and the un-allocated fraction is not picked up anywhere either. This phrasing supersedes E00's looser "transferred as if it were total".

## D. QUESTIONS THE EVIDENCE BASE CANNOT ANSWER
1. Whether X1-04's dual manufacturing record double-count fires in a live configuration — data question.
2. Whether X1-05's cross-budget double-count fires in a live configuration — data question.
3. COR-P09-06 could not be independently checked (roots not in this reviewer's brief) — class C, flagged, not disproved.
4. The 790-vs-797 count — not decidable with the commands this reviewer ran; flagged as a residual, not asserted as an error. **Resolved separately by the research team — see `P09_REVISION_LOG` §R3.**
5. Whether real budget configurations rely on the wildcard behaviour of X1-06.

## E. SEARCH BOUNDARY
Declared in full by the reviewer: 40+ enumerated commands covering full reads of the analytic line model, the analytic mixin, the transfer module (all 5 non-test files), the budget report and both budget models, the project and project-accounting models, five producer modules, and a whole-tree category enumeration across both reference roots. No database executed; every operational consequence explicitly hedged. **No prohibited verdict vocabulary used.**
