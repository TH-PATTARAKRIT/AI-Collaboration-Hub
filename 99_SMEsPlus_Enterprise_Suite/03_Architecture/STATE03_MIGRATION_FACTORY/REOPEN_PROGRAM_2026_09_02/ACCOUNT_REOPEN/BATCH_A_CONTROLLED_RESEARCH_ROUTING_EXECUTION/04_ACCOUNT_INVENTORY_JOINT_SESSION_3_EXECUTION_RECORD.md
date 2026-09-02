# 04 — ACCOUNT x INVENTORY JOINT SESSION 3 EXECUTION RECORD

| Field | Value |
|---|---|
| Decision ID | `ACC-DEC-019` (convening) |
| Jira | `ERPPLUS-140` |
| Batch A Approved Direction | Proceed with Account x Inventory Joint Session 3 routing |
| Batch A Control Status | `PENDING JOINT SESSION 3` |
| Boss Approval Record | branch `boss/account-batch-a-research-routing-approval-2026-09-02`, commit `fa75eb0ebfd8c3eee41b0e78c7afb39cbac7e751`, §2 row 4 |
| Source Routing Pack | `07_ACCOUNT_INVENTORY_JOINT_SESSION_3_ROUTING_BRIEF.md`, branch `audit/account-boss-decision-legal-tax-routing-2026-09-02-001`, commit `1fbc64c20d2d2003f1ee0dbeb591bef9a4cd4ff6` |
| Owner | Boss (convene) / Joint (Account + Inventory) |
| Gate Impact | Account + Inventory Backbone baseline HOLD |

`No prompt from the Account side may close an Inventory-owned or Joint item.` This record executes routing only: it confirms the agenda, assigns Owner/Evidence Location/Status/Gate Impact/Next Action to the convening pre-conditions, and does not convene, adjudicate, or close any agenda item.

## Agenda execution table (11 mandatory topics, unchanged from source brief)

| # | Topic | Owner | Evidence Location | Status | Next Action |
|---|---|---|---|---|---|
| 1 | Receipt posting | Joint | source brief §"Mandatory agenda coverage" #1 | `PENDING JOINT SESSION 3` | Confirm Inventory-side counterpart at session |
| 2 | Delivery / COGS posting | Joint | #2 | `PENDING JOINT SESSION 3` | Same |
| 3 | Return basis conflict | Inventory (internal, first) then Joint | #3 — flagged `CONFLICTING` inside Inventory before Joint adjudication | `PENDING — INVENTORY INTERNAL RESOLUTION FIRST` | Inventory resolves internally; Account side must not pre-empt |
| 4 | Adjustment | Joint | #4 | `PENDING JOINT SESSION 3` | — |
| 5 | Landed cost | Joint | #5 | `PENDING JOINT SESSION 3` | — |
| 6 | Manufacturing | Joint; cross-references `ACC-DEC-008`/SC-05 | #6 | `PENDING JOINT SESSION 3` | Do not resolve from Account side alone (see `05_ACCOUNT_SCOPE_RESEARCH_REGISTER_SC01_SC10.md`) |
| 7 | Price difference | Joint; cross-references `ACC-DEC-008`/SC-05 | #7 | `PENDING JOINT SESSION 3` | Same |
| 8 | Opening balance cross-proof | Joint | #8 (`G-5`); ties to `MG-C11` subledger tie-out | `PENDING JOINT SESSION 3` | — |
| 9 | Monthly close sequence | Joint | #9 (`G-1`, `G-2`) | `PENDING JOINT SESSION 3` | — |
| 10 | Year-end retained earnings design | Joint; Account half at `COA-G03` | #10 (`G-6`); ties to `OB-04` (`999999` placeholder vs `321200`) | `PENDING JOINT SESSION 3 — ACCOUNT HALF NOT YET JOINT-READY` | Account-side `COA-G03` Boss decision must land before this topic is Joint-ready |
| 11 | Product category dual ownership | Joint | #11 | `PENDING JOINT SESSION 3` | — |

## Additional carried-in items (unchanged from source brief)

`G-3` posting-architecture fork (gate scope mismatch — `TH-INV-03` deferred to `COA-G06`, which does not cover costing methods; Boss must resolve, `ACC-DEC-013`-adjacent), inventory write-down, dimension assignment on inventory-originated lines (also `ACC-DEC-011`), multi-company transfer, company/tenant cross-domain enforcement, capitalised spare parts vs stock.

## Pre-convening checklist execution

| Item | Owner | Status | Next Action |
|---|---|---|---|
| Confirm Inventory-side attendee(s) and package reference (branch/commit) | Boss | `NOT CONFIRMED IN THIS RESEARCH PASS` — this Account-side session did not verify or select an Inventory-side branch; the source brief's own note that Inventory "has already handed over its side" is carried forward as a citation only, not independently re-verified here, consistent with the rule that no Account-side prompt may close an Inventory-owned item | Boss/PMO to confirm the specific Inventory package reference at convening time |
| Confirm Account-side attendee(s) and package reference | Boss | `THIS PACKAGE`: branch `audit/account-batch-a-research-routing-2026-09-02-001` (this record), predecessor branch `audit/account-boss-decision-legal-tax-routing-2026-09-02-001` commit `1fbc64c20d2d2003f1ee0dbeb591bef9a4cd4ff6`, and `audit/account-menu-process-deep-study-2026-09-02-001` commit `5183e9f6ef4272e68c65d831580886e341118d53` | `READY` |
| Confirm a neutral clean-room reviewer is present for the OB-13 VETO checkpoint | Boss | Source brief §"Pre-conditions before convening" — Inventory's own "G-2" proposes an "Accounting lock-exception model as template" for the Joint seam; must be treated as a clean-room VETO checkpoint, not assumed | `NOT CONFIRMED` | Boss to name a neutral reviewer before convening |
| Set agenda order (items 1–3 before 9–10) | Boss | This record, agenda table above | `ROUTED, NOT SCHEDULED` | Boss to schedule |
| Record outputs back into both sides' gap registers | Joint | N/A — no session has yet occurred | `PENDING` | After Joint Session 3 occurs |

## Explicit non-claim

No agenda item is resolved, no attendee list is finalized, and no session date is set by this record. `ACC-DEC-019` remains `PENDING JOINT SESSION 3`.
