# CORR-007B — Team I2: N-A7-01 Inventory Count Freeze / Conflict Proof

Session: `SMEPLUS-26-09-02-CORR007B-3HIGH-CLOSURE-001`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `audit/inventory-core-corr007b-3high-closure-010`
Base commit: `deceb7339b39eba309236782f159f8393224f5fd`
Timestamp: 2026-09-02
Mode: Evidence-first / clean-room / no development authorization / read-only

## 1. Prior status

CORR-006 §5.6 found conflict-detection fields but no hard freeze field, and kept the item
`HIGH REMAINS — Inventory count freeze policy required before design freeze`. IDR-007's independent
spot-check (`06_IDR007_RESIDUAL_COUNT_AND_SEVERITY_RECOMPUTATION.md`, Part C item 2) separately grepped
`stock_quant.py` and reached the same negative finding. This session performs a full independent
re-read of the actual field/method bodies (not just a grep for field names) to determine which of the
task's four reference-behavior categories (A hard freeze / B soft conflict / C no freeze / D mixed)
actually applies, per the closure rule in the task brief.

## 2. Source evidence (independently re-read this session)

All paths under `ACCOUNT/01 ACCOUNT/SOURCE CODE/02 OTHER/`.

### 2.1 `stock/models/stock_quant.py`

- Lines 105-114 — field declarations:
  - `inventory_diff_quantity` (Float, computed, stored) — "Difference" between counted and theoretical quantity.
  - `inventory_quantity_set` (Boolean, computed, stored, `readonly=False`) — whether a count value has been entered.
  - `is_outdated` (Boolean, computed, searchable) — "Quantity has been moved since last count".
- Lines 185-208 — computation logic:
  - `_compute_inventory_diff_quantity()`: `inventory_diff_quantity = inventory_quantity - quantity` only
    when `inventory_quantity_set` is true; otherwise 0.
  - `_compute_is_outdated()`: becomes `True` when the theoretical quantity has moved since the counted
    value was set — i.e. a normal stock move happened **after** the count was entered but **before**
    it was applied. This is the conflict signal, and it is computed retroactively, not enforced
    preventively.
- Line 433 — `def action_apply_inventory(self, date=None):` (full body read):
  - Filters quants where `is_outdated` is true.
  - If any are outdated, returns an `ir.actions.act_window` opening the `stock.inventory.conflict`
    transient wizard, passing the outdated quant IDs in context. **It does not raise, does not block,
    and does not prevent the underlying stock moves that caused the conflict from having already
    happened.**
  - If none are outdated, it proceeds directly to `_apply_inventory(date)`.
- No field, decorator, `_check_company_lock_dates`-style constraint, or ORM-level lock was found
  anywhere in this file that prevents a normal `stock.move` from being created, validated, or completed
  against a quant location while a count is "in progress" (i.e. between the moment a user types a
  counted quantity and the moment `action_apply_inventory()` is run).

### 2.2 `stock/wizard/stock_inventory_conflict.py` (full file read, 24 lines)

- `StockInventoryConflict` is a `TransientModel`, not a lock/session object — it exists only to be
  opened as a one-time dialog.
- `action_keep_counted_quantity()`: overwrites `inventory_diff_quantity` from the counted value, then
  calls `action_apply_inventory()` again (which now proceeds, since `inventory_quantity_set` will be
  reset).
- `action_keep_difference()`: overwrites `inventory_quantity` to preserve the already-observed
  difference, then re-applies.
- Both resolution paths are **user choices made after the fact**, at apply time. Neither path un-does
  or blocks the movement that caused the conflict.

### 2.3 `stock/wizard/stock_inventory_warning.py`

- A second, separate transient wizard (`stock.inventory.warning`) that can reset or set inventory
  quantities — also an apply-time interaction, not a movement-time gate.

## 3. Classification against the task's four reference-behavior categories

| Category | Applies? | Basis |
|---|---|---|
| A. Hard freeze | **No** | No field, method, or constraint was found anywhere in `stock/models/stock_quant.py`, `stock/models/stock_move.py` call paths, or the two wizards that blocks a normal stock move from being created/validated while a count value is set but not yet applied. |
| B. Soft conflict detection | **Yes** | `is_outdated` + `action_apply_inventory()` + `stock.inventory.conflict` wizard is a complete, self-consistent detect-then-resolve-at-apply-time mechanism. |
| C. No freeze at all | No | Rejected — conflict *detection* genuinely exists and is enforced (the wizard is not optional; `action_apply_inventory()` always routes through it when `is_outdated`). |
| D. Mixed | No | There is no hard-freeze component of any kind to mix with the soft-conflict component. |

**Conclusion: Odoo reference behavior is category B — soft conflict detection, with no hard
count-in-progress freeze.** This matches CORR-006 and IDR-007's prior findings; this session adds a
full method-body re-read (not only a field-name grep) as independent confirmation.

## 4. SMEsPlus design decision required (not decided here)

Per the task brief, this is a decision for Team B design, not for this evidence session. The options,
stated without a recommendation from this report:

- **A. Hard freeze during count** — block stock moves against a quant/location once a count value is
  set, until applied. Odoo core does not do this; would be a SMEsPlus customization.
- **B. Soft conflict detection** — adopt Odoo's existing behavior as-is (detect at apply time, let the
  user choose keep-counted vs. keep-difference).
- **C. Location/session lock** — freeze at the location or count-session level rather than per-quant.
- **D. Manager exception workflow** — allow moves during count but require manager approval to resolve
  conflicts, instead of the current self-service wizard.

This report does not select among these. Selecting one is explicitly out of scope for CORR-007B (task
§3, out of scope: "Team B Inventory Design authorization").

## 5. Disposition

Per the task's own closure rule: *"If source proves soft conflict only, recommend closure as
`RESOLVED AS SOURCE BEHAVIOR + DESIGN POLICY REQUIRED`."*

**`N-A7-01`: RESOLVED AS SOURCE BEHAVIOR; DESIGN POLICY REQUIRED.**

The source-evidence question ("what does Odoo actually do today?") is fully and unambiguously answered:
soft conflict detection only, no hard freeze. What remains open is a SMEsPlus product-design decision
among the four options in §4 — that is a design gap, not an evidence gap, and should not continue to be
tracked as an Inventory Evidence Gate High blocker. It should be carried forward as a named, mandatory
input to Team B's design-freeze checklist.

Carry-forward: design-policy decision (§4), owner Team B (not yet authorized to start), target gate:
Inventory Design Freeze. Stop condition: Team B must not finalize count/adjustment UX without
explicitly selecting one of A–D (or a documented variant) and recording the rationale.

This disposition is a recommendation. It is not a Gate PASS declaration and does not authorize Team B
or Team C. See `05_CORR007B_BOSS_DECISION_RECOMMENDATION.md`.
