# 03 — ACC-WHT-06 RESEARCH EXECUTION RECORD

| Field | Value |
|---|---|
| Decision ID | `ACC-DEC-003` |
| Batch A Approved Direction | Treat WHT multi-rate baseline as mandatory research topic |
| Batch A Control Status | `RESEARCH REQUIRED` |
| Boss Approval Record | branch `boss/account-batch-a-research-routing-approval-2026-09-02`, commit `fa75eb0ebfd8c3eee41b0e78c7afb39cbac7e751`, §2 row 3 |
| Source Routing Pack | `04_ACC_WHT_06_MODULE_BASELINE_DECISION_PACK.md`, branch `audit/account-boss-decision-legal-tax-routing-2026-09-02-001`, commit `1fbc64c20d2d2003f1ee0dbeb591bef9a4cd4ff6` |
| Owner | UNASSIGNED (Accounting-Tax reviewer, once named) |
| Gate Impact | `COA-G06`; `ACC-WHT-06` (severity: **HIGH**) |

## Reading of the Boss decision

Batch A approves `ACC-DEC-003` to proceed **as a research topic**, not as an option selection. This is distinct from and must not be conflated with choosing Option A, B, or C from the source decision pack. The source pack's own "Boss decision record" block (Option ☐A ☐B ☐C, decided by, date) remains **unfilled** — Boss's Batch A approval routes the item into research, it does not check a box.

## The fact this decision turns on (carried forward unchanged)

Source `A2` §B.1 recorded that the benchmark instance had the `l10n_th_withholding_tax_multi` module's dependency present but the module itself not installed — meaning the benchmark's observed WHT behaviour reflects single-rate handling, not the multi-rate handling that module would add. `ACC-WHT-06` was originally scoped before this fact was known.

## Research execution table

| Item | Owner | Evidence Location | Status | Gate Impact | Next Action |
|---|---|---|---|---|---|
| Option A — baseline on benchmark-as-observed (single-rate, module absent) | UNASSIGNED (Accounting-Tax) | `04_ACC_WHT_06_MODULE_BASELINE_DECISION_PACK.md` §"Decision options" | `RESEARCH REQUIRED — NOT SELECTED` | `COA-G06`, `ACC-WHT-06` (HIGH) | No further evidence needed for this option specifically, but it remains unselected pending Boss ruling |
| Option B — baseline on multi-rate WHT as in-scope, using module documentation | UNASSIGNED | Same | `RESEARCH REQUIRED — NOT SELECTED` | Same | Requires module re-observation or documentation citation, flagged as such if used |
| Option C — defer `ACC-WHT-06` entirely until legal-tax review returns authoritative WHT rate/category citations | UNASSIGNED | Same; cross-reference `02_LEGAL_TAX_REVIEW_ROUTING_EXECUTION_RECORD.md` §A item `WHT-1` | `RESEARCH REQUIRED — NOT SELECTED` | Same | Depends on `WHT-1` legal-tax review output (see `02`) |
| Cross-reference: WHT multi-rate categories and percentages | UNASSIGNED | `02_LEGAL_TAX_REVIEW_ROUTING_EXECUTION_RECORD.md` §A, item `WHT-1` — status `LEGAL_TAX_REVIEW_REQUIRED` | `LEGAL_TAX_REVIEW_REQUIRED` (unchanged) | `COA-G06` | Boss commissions Legal-Tax reviewer per `02`; `WHT-1` output is a direct input to this research item |

## Why Option A is not a default despite requiring no further evidence

The source pack states as fact that Option A is "the only option not requiring any further evidence-gathering, because it is what was actually observed." Batch A's classification of this item as `RESEARCH REQUIRED` (rather than closing it via Option A by default) means Boss has not accepted that convenience as sufficient — this record preserves that reading and does not select Option A on Boss's behalf.

## Explicit non-claim

No option (A, B, or C) is selected by this record. `ACC-WHT-06` remains `HIGH` severity, `COA-G06` cannot proceed on the WHT sub-item, and the module baseline decision record in the source pack remains blank pending a named Accounting-Tax owner and a Boss ruling — informed by, but not required to wait indefinitely for, the Legal-Tax Review output tracked in `02`.
