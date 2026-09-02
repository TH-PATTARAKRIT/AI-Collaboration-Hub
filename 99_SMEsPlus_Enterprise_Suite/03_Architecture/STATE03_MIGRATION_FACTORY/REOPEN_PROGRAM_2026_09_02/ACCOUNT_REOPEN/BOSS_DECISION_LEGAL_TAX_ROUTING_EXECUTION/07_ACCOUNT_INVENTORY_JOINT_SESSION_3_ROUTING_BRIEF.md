# 07 — ACCOUNT x INVENTORY JOINT SESSION 3 ROUTING BRIEF

| Field | Value |
|---|---|
| Decision ID | `ACC-DEC-019` (convening) |
| Jira | `ERPPLUS-140` |
| Source | `20_GAP_OWNER_GATE_IMPACT_REGISTER.md` §D; `22_NEXT_PROMPT_RECOMMENDATION.md` §2 item 4 |
| Owner | Boss (convene) / Joint (Account + Inventory) |
| Status | `PENDING JOINT SESSION 3` |
| Gate Impact | Account + Inventory Backbone baseline HOLD |

`No prompt from the Account side may close an Inventory-owned or Joint item.` This brief only assembles the agenda; it resolves nothing.

## Why now

The Account menu-by-menu process study (source package, this reopen) has produced its side of the process map. Source `20` records that the Inventory reopen package has already "handed over its side" (its own file 20). Both sides now have enough to convene, per governing-prompt §7 and source `22` item 4.

## Mandatory agenda coverage (per governing prompt §7)

| # | Topic | Source reference | Notes |
|---|---|---|---|
| 1 | Receipt posting | 20 §D (`N-A12-01`); source 08 (Stock/COGS boundary, referenced) | Account-side posting boundary already mapped in source 08; Inventory-side counterpart to confirm |
| 2 | Delivery / COGS posting | 20 §D; source 08 (referenced) | Same as above |
| 3 | Return basis conflict | 20 §D — flagged `CONFLICTING` **inside Inventory first**, i.e. Inventory has an internal disagreement to resolve before the Joint session can adjudicate the Account-facing question | 08 §4 (referenced) | Do not let Account-side assumptions pre-empt Inventory's internal resolution |
| 4 | Adjustment | 20 §D | — |
| 5 | Landed cost | 20 §D | — |
| 6 | Manufacturing | 20 §D; also surfaced in `05` (`ACC-DEC-008` / SC-05) and source 18 (new scope hole: manufacturing valuation) | Cross-referenced — do not resolve from Account side alone |
| 7 | Price difference | 20 §D; also surfaced in `05` (`ACC-DEC-008` / SC-05) | Cross-referenced |
| 8 | Opening balance cross-proof | 20 §D (`G-5`) | Ties to migration `MG-C11` subledger tie-out (see `10`) |
| 9 | Monthly close sequence | 20 §D (`G-1`, `G-2`) | Also referenced in source 18 as a CARRY FORWARD item (close/RE model) |
| 10 | Year-end retained earnings design | 20 §D (`G-6`) | Ties to Account-side OB-04 (`999999` placeholder vs designated RE account, `321200`) — Account's half is Boss-decision-pending at `COA-G03`, not yet Joint-ready |
| 11 | Product category dual ownership | 20 §D | — |

## Additional items carried into the Joint agenda from source `20` §D

`G-3` (posting-architecture fork — also independently flagged in source `20` OB-11: `TH-INV-03` was deferred to `COA-G06`, but `COA-G06` does not cover costing methods — a **gate scope mismatch** that Boss must resolve, `ACC-DEC-013`-adjacent, before or alongside this Joint session), inventory write-down (source 08 SC-20; also `05` `ACC-DEC-008`), dimension assignment on inventory-originated lines (source 13 UK-06; also `05` `ACC-DEC-011`), multi-company transfer, company/tenant cross-domain enforcement, capitalised spare parts vs stock (source 12 UK-05).

## Pre-conditions before convening (per source `20` OB-13)

Source `20` OB-13 flags a **back-door inheritance risk**: Inventory's own "G-2" proposes an "Accounting lock-exception model as template" for the Joint seam. This must be treated as a clean-room VETO checkpoint at the start of the Joint session, not assumed. The Joint session's own charter must confirm no benchmark (Odoo) lock-exception behaviour is inherited without independent Thai-SME-process justification.

## What this brief does not do

- It does not rule on `G-1`..`G-6` or any item above.
- It does not assign a winner between Account's and Inventory's competing readings where they differ (e.g., OB-12: two parallel tracks — Inventory reopen vs. the prior Account Ai Audit package — carry different readings of `COA-G01`/`G02` status; this is itself a `BOSS DECISION REQUIRED` item, tracked as `ACC-DEC-018`-adjacent, not a Joint-session item).
- It does not close SC-05 sub-items (manufacturing, price difference, write-down) from the Account side — those remain routed to both `05` (Boss scope ruling) and this Joint agenda simultaneously, since ownership itself is one of the Joint questions.

## Convening checklist for Boss

- [ ] Confirm Inventory-side attendee(s) and their package reference (branch/commit)
- [ ] Confirm Account-side attendee(s) and this package's reference (branch `audit/account-menu-process-deep-study-2026-09-02-001`, commit `5183e9f6ef4272e68c65d831580886e341118d53`)
- [ ] Confirm a neutral clean-room reviewer is present for the OB-13 VETO checkpoint
- [ ] Set agenda order: items 1–3 (posting mechanics) before items 9–10 (close/RE, which depend on posting mechanics being settled)
- [ ] Record outputs back into both sides' `20` gap registers, not just one
