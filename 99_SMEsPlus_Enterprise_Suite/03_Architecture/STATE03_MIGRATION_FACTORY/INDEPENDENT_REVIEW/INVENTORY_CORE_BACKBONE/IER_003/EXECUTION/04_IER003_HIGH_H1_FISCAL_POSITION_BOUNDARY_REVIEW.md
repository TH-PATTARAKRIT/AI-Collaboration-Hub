# 04 — High H1 (GRPA-H4): Fiscal Position Base Model — Independent Verdict

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Independently test GRPA-H4's classification, evidence, and Gate impact | Independent Evidence Reviewer | `01 ACCOUNT/account/models/partner.py:27` | 2026-09-01 | Boss | **VERIFIED CLOSED — CORRECTS TEAM A** | Removed as an Inventory Gate item; reclassified as a routine Accounting-domain fact |

## TEAM A's claim (A14 Part 1, GRPA-H4)

> "`account.fiscal.position` base model file never located... Evidence Found: Not found in GROUP A's extraction; not independently re-searched this pass (out of this pass's assigned module scope)... Status: `EVIDENCE_MISSING`."

## What this review found

A full-tree search of the entire authorized source root (`01 ACCOUNT/` + `02 OTHER/` + `addons_extra/`) for the model's `_name` declaration:

```
grep -rn "_name = 'account.fiscal.position'" "SOURCE CODE"
→ 01 ACCOUNT/account/models/partner.py:27:    _name = 'account.fiscal.position'
```

The model **is defined** — inline within `partner.py` (not a dedicated `account_fiscal_position.py` file, which is almost certainly why a search for a same-named file would fail to find it), inside the core `account` module folder at `01 ACCOUNT/account/`. Confirmed as a genuine model declaration, not a stray string: the same file also declares the companion model `account.fiscal.position.account` (`partner.py:304`) and is referenced consistently throughout `01 ACCOUNT/account/models/company.py` (`fiscal_position_ids`, `account_purchase_receipt_fiscal_position_id`) and `partner.py` (`property_account_position_id`, `_get_fiscal_position()`).

## Why TEAM A missed it

A0 §2 states: "`01 ACCOUNT/` subfolder contains **only** `account_*`-prefixed Accounting Core modules (62 folders) — no Inventory-relevant modules live here." This description is imprecise in a way that plausibly caused the miss: the base module folder is literally named `account` (no underscore-suffix), not `account_something`. A0's own module-landscape scan (A1) was scoped to Inventory-relevant modules, and GRPA-H4 was inherited from GROUP A's earlier extraction rather than independently re-searched this pass ("not independently re-searched this pass (out of this pass's assigned module scope)" — A14's own words). No party in the DR-002 chain appears to have run a full-tree grep for this specific model declaration before this review.

## Inventory-side dependency — checked directly

```
grep -rn "fiscal_position" 02\ OTHER/stock 02\ OTHER/stock_account
→ stock_account/models/account_move.py:114
→ stock_account/models/account_move_line.py:20-21
```

Both hits are inside `stock_account`'s **Accounting-interface** code (`_stock_account_prepare_realtime_out_lines_vals`-adjacent logic that resolves which G/L accounts a product uses, via `get_product_accounts(fiscal_pos=...)`), not inside core Inventory models (`stock.move`, `stock.quant`, `stock.picking` themselves never reference fiscal position). This confirms TEAM A's own instinct (A14: "Stock Truth Impact: None (Accounting concept)") was directionally correct even while the underlying "file never located" premise was wrong.

## Independent verdict

**`VERIFIED CLOSED`**

- Evidence read: `01 ACCOUNT/account/models/partner.py` (full model declaration and its usage across `company.py`).
- What remains unknown: nothing material to Inventory. (Whether SMEsPlus's own target design should model fiscal positions the same way is an Accounting/Team-B design question, explicitly out of scope for both TEAM A's and this review's authority.)
- **Inventory Gate Blocking: NO** (was already assessed as low by TEAM A; now the underlying evidence gap is fully closed rather than merely assumed low-risk).
- Stock Truth impact: None — confirmed directly, not inferred.
- Accounting interface impact: Direct — `stock_account`'s valuation-posting code depends on `account.fiscal.position` to resolve product accounts; this is now traceable to an exact, existing model rather than an unlocated dependency.
- Dependent-domain impact: Tax/Accounting only.
- Migration impact: Low, unchanged from TEAM A's assessment.
- Next owner / next action: **None required to close this item.** Recommended: TEAM A's next evidence pass should incorporate this citation into A14/A15's canonical record (a documentation correction, not a re-research task) — see [14](14_IER003_TARGETED_TEAM_A_CORRECTIVE_RECOMMENDATION.md).

No Unknown was converted to a Fact by inference here — the model file was read directly, cited exactly, and its Inventory-side non-dependency was confirmed by grep of the actual Inventory modules, not assumed.
