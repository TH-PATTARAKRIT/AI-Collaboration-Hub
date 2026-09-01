# CORR-007B — Team I3: N-A12-01 Fiscal-Year / Cross-Year Continuity Proof

Session: `SMEPLUS-26-09-02-CORR007B-3HIGH-CLOSURE-001`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `audit/inventory-core-corr007b-3high-closure-010`
Base commit: `deceb7339b39eba309236782f159f8393224f5fd`
Timestamp: 2026-09-02
Mode: Evidence-first / clean-room / no development authorization / read-only

## 1. Prior status

CORR-006 §5.8 found that lock-date and inventory-adjustment accounting-date mechanisms exist, but held
the item `HIGH REMAINS — cross-proof required` because full migration/cutover continuity was not
proven. This session re-verifies the cited mechanisms against primary source and, following the same
domain-boundary method CORR-007A used to resolve `GRPA-M18`'s WHT sub-item, determines whether the
unresolved part of this item is genuinely a pure-Inventory blocker or an Accounting-contract dependency
that should be carried forward rather than left as an open Inventory High item.

## 2. Source evidence (independently re-read this session)

All paths under `ACCOUNT/01 ACCOUNT/SOURCE CODE/`.

### 2.1 Inventory-side: accounting date propagation (`02 OTHER/stock_account/`)

- `models/stock_quant.py:12-16` — `accounting_date` (Date) field on `stock.quant`: *"Date at which the
  accounting entries will be created in case of automated inventory valuation. If empty, the inventory
  date will be used."*
- `models/stock_quant.py:80-101` — `_apply_inventory()` override: when `accounting_date` is set, calls
  `super()._apply_inventory(date)` with context `force_period_date=accounting_date`, and appends
  `" [Accounted on %s]"` to the inventory move name.
- `wizard/stock_inventory_adjustment_name.py:1-21` (full file) — `stock.inventory.adjustment.name`
  wizard extension adds `accounting_date` and computed `should_show_accounting_date` (shown only when
  any counted product uses `real_time` valuation); `_get_quants_context()` injects
  `force_period_date = self.accounting_date`.
- `models/stock_move.py:203` — `'date': self.env.context.get('force_period_date') or
  fields.Date.context_today(self)` — the posted accounting move's date uses `force_period_date` when
  supplied, else today. This confirms the full propagation chain: wizard → quant context → stock move
  → account move date.

### 2.2 Inventory-side: lock-date enforcement on physical movement (`02 OTHER/stock_account/models/stock_picking.py`, full file, 34 lines)

- `_check_backdate_allowed()` (`@api.constrains("scheduled_date", "date_done")`): raises
  `ValidationError` if `picking._is_date_in_lock_period()`, unless the
  `stock_account.skip_lock_date_check` config parameter is set.
- `_is_date_in_lock_period()`: for a `done` picking, calls
  `self.company_id._get_lock_date_violations(self.scheduled_date.date(), fiscalyear=True, sale=False,
  purchase=False, tax=False, hard=True)` against `scheduled_date`, and again against `date_done` when
  present.
- This is a real, active, hard enforcement point: a completed stock picking's dates are checked against
  the company's fiscal-year and hard lock dates, and backdating into a locked period is blocked at the
  ORM constraint level — not merely detected.

### 2.3 Accounting-side: where the lock dates actually live (`01 ACCOUNT/account/models/company.py:70-119`)

- `fiscalyear_lock_date`, `tax_lock_date`, `sale_lock_date`, `purchase_lock_date`, `hard_lock_date` are
  all declared here, on `res.company`, inside the **`account`** module — not inside `stock` or
  `stock_account`.
- `def _get_lock_date_violations(...)` (the method `stock_picking.py` calls into) is also defined in
  this same file — confirmed by `grep -rln "def _get_lock_date_violations" $SRC` returning only this
  path.
- Conclusion: Inventory's picking-date enforcement is a **consumer** of an Accounting-owned contract.
  Inventory does not define, and cannot unilaterally change, what a "locked period" is; it correctly
  calls into Accounting's own lock-date logic.

### 2.4 Cross-year valuation math (`02 OTHER/stock_account/models/res_company.py:255-315`)

- `_get_continental_realtime_variation_vals()` (full body read): computes stock valuation variation
  *"for a period"* by comparing `stock_accounting_value()` evaluated at today vs. at
  `self.compute_fiscalyear_dates(fields.Date.today())['date_from']` — i.e. the start of the **current
  fiscal year**, a value Inventory obtains by calling into Accounting's own `compute_fiscalyear_dates()`
  method, not by computing it independently.
- This proves Inventory's real-time valuation posting logic is explicitly fiscal-year-boundary-aware
  and is written to reconcile a period's variation against the company's accounting fiscal calendar —
  but it depends entirely on Accounting's fiscal-year definition being correct and available.

### 2.5 Tests confirming the mechanisms are exercised, not merely declared

- `stock_account/tests/test_account_move.py:258-322` — test confirms fiscal-year/hard lock dates
  prevent backdating a completed picking into a locked period (matches §2.2 behavior).
- `stock_account/tests/test_stockvaluation.py:3057-3082` — test confirms an inventory-adjustment
  journal entry can be created with a specified `accounting_date` (matches §2.1 behavior).

## 3. What is proven vs. what is not

**Proven from Inventory-side source (this session, independently):**
- Inventory adjustments carry an explicit accounting date, propagated correctly through to the posted
  journal entry (§2.1).
- Completed stock pickings are hard-blocked from being backdated into an Accounting-locked fiscal
  period (§2.2).
- Inventory's real-time valuation-over-period math is fiscal-year-boundary-aware (§2.4).
- All of the above are exercised by source-level automated tests, not only declared (§2.5).

**Not proven, and not provable from Inventory source alone:**
- Whether a real SMEsPlus legacy-to-target cutover will correctly carry forward *opening* quantities
  and *opening* valuation amounts across the fiscal-year boundary used for go-live.
- Whether Accounting's own opening-balance / chart-of-accounts migration produces figures that
  reconcile against Inventory's valuation-over-period output for the same boundary.
- These require Accounting's own migration-continuity evidence (opening trial balance handling,
  fiscal-year close procedure for the cutover year), which is out of this session's authorized scope
  (task §3: "Full Accounting COA redesign" is explicitly out of scope) and was not produced by this
  session.

## 4. Domain-boundary determination

Following the same method CORR-007A applied to `GRPA-M18-D` (PND3/PND53 filing was recognized as an
Accounting/Tax-owned concern bundled under an Inventory-labeled item, and formally separated rather than
left as an open Inventory blocker): the unresolved part of `N-A12-01` is not a gap in Inventory's own
source behavior — Inventory's mechanisms are fully proven and independently re-verified (§2, §3). The
unresolved part is a **joint cross-proof deliverable** that by definition requires Accounting's evidence
alongside Inventory's, and cannot be closed by an Inventory-only session regardless of how thoroughly
Inventory's own side is re-examined.

## 5. Disposition

Per the task's decision logic: *"If Accounting contract is required, classify as `CONTROLLED
ACCOUNTING X INVENTORY CROSS-PROOF CARRY-FORWARD`, not an unresolved pure Inventory source blocker."*

**`N-A12-01`: CONTROLLED ACCOUNTING X INVENTORY CROSS-PROOF CARRY-FORWARD.**

This is not a closure and is not a claim that cross-year continuity risk is resolved — the migration
continuity question in §3 ("not proven, and not provable from Inventory source alone") remains
genuinely open. What changes is the classification: it should no longer be counted as a pure Inventory
Evidence Gate High blocker, because Inventory's own contribution to the mechanism is now fully proven.
It must be carried forward with an explicit owner and target gate, not silently dropped.

Carry-forward: joint Accounting x Inventory cross-proof of migration/cutover continuity (opening
quantity and opening valuation reconciliation across the fiscal-year boundary). Owner: Team A
(Inventory) jointly with Accounting/Tax domain (same cross-domain pattern as `GRPA-M18-D`). Target
gate: a future joint cross-proof session, analogous to CORR-007A's `GRPA-M18` domain transfer. Required
evidence: Accounting's opening-balance/COA migration continuity evidence, reconciled line-by-line
against `stock_account`'s valuation-over-period output for the same fiscal-year boundary. Stop
condition: no migration cutover should be executed across a fiscal-year boundary until this joint
cross-proof exists.

This disposition is a recommendation. It is not a Gate PASS declaration and does not authorize Team B
or Team C. See `05_CORR007B_BOSS_DECISION_RECOMMENDATION.md`.
