# U186 — stock_picking_wave: Technical Evidence (L0–L3)

**Unit:** U186 | **Module:** stock_picking_wave (implemented in stock_picking_batch)
**Group:** G06 | **Priority:** P2 | **Status:** NOT_STUDIED → STUDIED
**Source base:** Odoo 19.0.post20260921 Community
**Evidence date:** 2026-10-02

---

## 1. Module Architecture Finding

There is **no standalone `stock_picking_wave` module** in Odoo 19.0 Community. Wave transfer functionality is fully embedded inside the `stock_picking_batch` module (`odoo/addons/stock_picking_batch/`). Waves are `stock.picking.batch` records with `is_wave = True`.

**Key source files:**
- `models/stock_picking_batch.py` — core batch/wave model
- `models/stock_picking.py` — `StockPickingType` wave grouping fields; `StockPicking._find_auto_batch()`
- `models/stock_move.py` — `_action_assign()` triggers `_auto_wave()`
- `models/stock_move_line.py` — `_add_to_wave()`, `_auto_wave()`, `_auto_wave_lines_into_existing_waves()`, `_auto_wave_lines_into_new_waves()`
- `wizard/stock_add_to_wave.py` — `stock.add.to.wave` transient model

---

## 2. Model Definition: `stock.picking.batch`

```python
_name = 'stock.picking.batch'
_inherit = ['mail.thread', 'mail.activity.mixin']
```

### Core Fields

| Field | Type | Notes |
|---|---|---|
| `name` | Char | Auto-assigned from sequence (`WAVE/…` for waves, `BATCH/…` for batches) |
| `is_wave` | Boolean | Distinguishes wave (`True`) from batch (`False`) |
| `state` | Selection | `draft`, `in_progress`, `done`, `cancel` — stored, computed |
| `picking_ids` | One2many → `stock.picking` (via `batch_id`) | All pickings linked to this wave/batch |
| `picking_type_id` | Many2one → `stock.picking.type` | Operation type; required for naming sequence |
| `company_id` | Many2one → `res.company` | Set on create; drives multi-company isolation |
| `user_id` | Many2one → `res.users` | Responsible user; propagated to `picking_ids` |
| `move_ids` | One2many (computed) | Aggregated stock moves from all member pickings |
| `move_line_ids` | One2many (computed, inversed) | Aggregated move lines from all member pickings |

---

## 3. State Machine: `_compute_state()`

File: `stock_picking_batch.py`, lines 144–155.

```python
@api.depends('picking_ids', 'picking_ids.state')
def _compute_state(self):
    batchs = self.filtered(lambda batch: batch.state not in ['cancel', 'done'])
    for batch in batchs:
        if not batch.picking_ids:
            continue
        if all(picking.state == 'cancel' for picking in batch.picking_ids):
            batch.state = 'cancel'
        elif all(picking.state in ['cancel', 'done'] for picking in batch.picking_ids):
            batch.state = 'done'
```

**Rules:**
- All member pickings cancelled → wave state = `cancel`
- All member pickings are `done` or `cancel` (at least one done) → wave state = `done`
- Records already `cancel` or `done` are excluded from recomputation (no reversion)
- `draft` → `in_progress` transition is triggered by `action_confirm()`

---

## 4. Wave Creation: `StockMoveLine._add_to_wave()`

File: `stock_move_line.py`, lines 31–119.

**Two paths:**
1. **New wave** — when `wave=False`: creates `stock.picking.batch` with `is_wave=True`, `picking_type_id` from first line's picking type, optionally `user_id` from context `active_owner_id`.
2. **Existing wave** — when `wave` is provided: links/splits pickings into the specified wave.

**Picking split logic:**
- If **all** move lines of a picking are selected → picking is linked directly to wave via `Command.link`.
- If **partial** move lines selected → picking is split: a new picking is created from `picking.copy_data(...)` carrying only the selected lines/moves; partial moves are split via `move._split(qty)`.

**Auto-confirm:** After adding lines, if `picking_type_id.batch_auto_confirm` is True, `wave.action_confirm()` is called.

---

## 5. Manual Wave Addition Wizard: `stock.add.to.wave`

File: `wizard/stock_add_to_wave.py`.

Fields:
- `wave_id` — Many2one to `stock.picking.batch` filtered by `is_wave=True, state in (draft, in_progress)`
- `mode` — `existing` or `new` wave
- `line_ids` — Many2many `stock.move.line`
- `picking_ids` — Many2many `stock.picking`
- `user_id` — Responsible

`attach_pickings()` → calls `line_ids._add_to_wave(wave_id)` (single-company validation applied first).

---

## 6. Auto-Wave Assignment: `_auto_wave()` Chain

### Trigger

`StockMove._action_assign()` (line 39–41):
```python
def _action_assign(self, force_qty=False):
    super()._action_assign(force_qty=force_qty)
    self.move_line_ids._auto_wave()
```

Also triggered from `StockPicking.button_validate()` for backorder move lines:
```python
assignable_pickings.move_line_ids.with_context(skip_auto_waveable=True)._auto_wave()
```

### Line eligibility: `_is_auto_waveable()` (lines 121–129)

A move line is auto-waveable if ALL of:
- Has a picking
- Picking state is `assigned` OR context flag `skip_auto_waveable` set
- Quantity is non-zero
- Not already in a wave (`batch_id.is_wave == False`)
- Operation type has `auto_batch=True` AND at least one wave grouping key enabled
- If `wave_group_by_category`, product category must be in `wave_category_ids`

### Wave Grouping Keys on `stock.picking.type`

| Field | Meaning |
|---|---|
| `wave_group_by_product` | Group lines sharing the same product |
| `wave_group_by_category` | Group lines sharing product category (from `wave_category_ids`) |
| `wave_group_by_location` | Group lines sharing nearest ancestor wave location (from `wave_location_ids`) |

### `_auto_wave()` flow (lines 131–163)

1. Resolve location hierarchy for `wave_group_by_location` lines.
2. Filter batchable lines via `_is_auto_waveable()`.
3. Call `_auto_wave_lines_into_existing_waves()` → returns remaining unmatched line IDs.
4. Call `_auto_wave_lines_into_new_waves()` on remaining lines.

### Existing wave matching (`_auto_wave_lines_into_existing_waves`)

Searches `stock.picking.batch` where `is_wave=True` and state not done/cancel, same picking type and company. Per-line matching checks: company, partner, location, product/category/location grouping keys, and batch size limits via `_is_line_auto_mergeable()`. Matched lines are added via `_add_to_wave(wave)`.

### New wave creation (`_auto_wave_lines_into_new_waves`)

Creates new `stock.picking.batch(is_wave=True, ...)` records. Lines sorted by `(picking_id, move_id)` to minimise picking splits. Batch size limits respected via `_is_line_auto_mergeable()`. Description set from `_get_auto_wave_description()`.

---

## 7. Wave Validation: `action_done()`

File: `stock_picking_batch.py`, lines 239–281.

- Filters all non-done, non-cancelled pickings from the wave.
- Removes empty/waiting pickings from wave (detaches, does not cancel).
- Runs `_sanity_check(separate_pickings=False)` across all pickings.
- Calls `pickings.button_validate()` with context `skip_sanity_check=True`.
- Context `batches_to_validate=self.ids` prevents the current wave from being re-targeted by auto-wave during backorder processing.

---

## 8. Auto-Assign on Wave: `action_assign()`

File: `stock_picking_batch.py`, lines 283–285.

```python
def action_assign(self):
    self.ensure_one()
    self.picking_ids.action_assign()
```

Calls `action_assign()` on ALL member pickings — which triggers `_action_assign()` on their moves — which in turn calls `_auto_wave()`. There is no direct `_action_assign()` call at wave level; it propagates through the picking/move chain.

---

## 9. Wave Sequence Naming

File: `data/stock_picking_batch_data.xml`.

```xml
<record id="seq_picking_wave" model="ir.sequence">
    <field name="code">picking.wave</field>
    <field name="prefix">WAVE/</field>
</record>
```

On create/write, if `is_wave=True` → sequence code `picking.wave`; otherwise `picking.batch`. Name format: `{sequence_prefix}/{picking_type.sequence_code}/{sequence_number}`.

---

## 10. Multi-Company Scope

Security rule (`stock_picking_batch_security.xml`):
```python
domain_force="[('company_id', 'in', company_ids)]"
```

The `company_id` field is `required=True`, `readonly=True`, defaulting to `self.env.company`. Both batch and wave records are filtered by the active company context. `check_company=True` on `picking_ids` and `user_id` fields enforces same-company pickings/users.

---

## 11. Batch vs Wave: Key Distinctions

| Aspect | Batch (`is_wave=False`) | Wave (`is_wave=True`) |
|---|---|---|
| Name prefix | `BATCH/` | `WAVE/` |
| Creation | Via `stock.picking.to.batch` wizard or auto-batch | Via `_add_to_wave()` or `_auto_wave()` |
| Grouping trigger | On picking confirm | On stock move `_action_assign()` (i.e., after availability check) |
| Picking granularity | Whole pickings | Can be partial (move-line level split) |
| Auto-create | `_find_auto_batch()` (on picking state → assigned) | `_auto_wave()` (on move line assignment) |
| Merge guard | Batch ↔ Wave merging blocked (`action_merge()`) | Same |
| View action | `stock_picking_batch_action` | `action_picking_tree_wave` |

---

## 12. Barcode Integration

No `stock_barcode_picking_wave` module present in Odoo 19.0 Community source. Barcode-wave integration is an Enterprise feature only.

---

## 13. `_search_picking_for_assignation_domain()` Override

File: `stock_move.py`, lines 10–13.

```python
domain = Domain.AND([domain, ['|', ('batch_id', '=', False), ('batch_id.is_wave', '=', False)]])
```

Ensures that when assigning moves to pickings, pickings already in a **wave** are excluded from the search pool. This prevents wave pickings from being auto-merged with batch pickings.

---

## 14. Batch Size Limits

`_is_line_auto_mergeable(num_of_moves, num_of_pickings, weight)` (lines 459–468):
- Checks `picking_type_id.batch_max_lines` (max moves)
- Checks `picking_type_id.batch_max_pickings` (max pickings)
- No weight-based limit enforced (weight parameter tracked but not capped)

---

## Claims Summary Table (9-column)

| # | Claim | Source File | Line(s) | Evidence Level | Confidence | Scope | Risk | Notes |
|---|---|---|---|---|---|---|---|---|
| C1 | Wave transfers are `stock.picking.batch` records with `is_wave=True`; no separate model | `models/stock_picking_batch.py` | 9, 60 | L3 | HIGH | Community | LOW | Confirmed in Odoo 19.0 CE |
| C2 | State values: `draft`, `in_progress`, `done`, `cancel` | `models/stock_picking_batch.py` | 40–46 | L3 | HIGH | Community | LOW | Same enum as batch |
| C3 | `_compute_state()` derives wave state from member picking states | `models/stock_picking_batch.py` | 144–155 | L3 | HIGH | Community | LOW | Done if all pickings done/cancel with ≥1 done |
| C4 | `picking_ids` is `One2many('stock.picking', 'batch_id')` | `models/stock_picking_batch.py` | 24–27 | L3 | HIGH | Community | LOW | Shared field for batch and wave |
| C5 | `picking_type_id` determines naming sequence and grouping | `models/stock_picking_batch.py` | 47–49, 186 | L3 | HIGH | Community | LOW | Sequence code `picking.wave` for waves |
| C6 | `_add_to_wave()` creates wave and links/splits pickings at move-line granularity | `models/stock_move_line.py` | 31–119 | L3 | HIGH | Community | MEDIUM | Picking split via `copy_data` + `_split` |
| C7 | Auto-wave is triggered by `StockMove._action_assign()` calling `move_line_ids._auto_wave()` | `models/stock_move.py` | 39–41 | L3 | HIGH | Community | LOW | Fires after stock availability assignment |
| C8 | `_is_auto_waveable()` requires state=assigned, non-zero qty, not already in wave, wave grouping active | `models/stock_move_line.py` | 121–129 | L3 | HIGH | Community | LOW | Category filter via `wave_category_ids` |
| C9 | `action_done()` validates all member pickings by calling `button_validate()` | `models/stock_picking_batch.py` | 239–281 | L3 | HIGH | Community | LOW | Empty/waiting pickings are detached, not cancelled |
| C10 | `action_assign()` propagates to all member pickings via `picking_ids.action_assign()` | `models/stock_picking_batch.py` | 283–285 | L3 | HIGH | Community | LOW | Indirect L3 auto-assign through picking chain |
| C11 | Wave grouping criteria: product, product category, location (on `stock.picking.type`) | `models/stock_picking.py` | 21–25, 72–73 | L3 | HIGH | Community | LOW | `wave_group_by_product`, `_category`, `_location` |
| C12 | Wave sequence uses `picking.wave` code with prefix `WAVE/` | `data/stock_picking_batch_data.xml` | seq_picking_wave | L3 | HIGH | Community | LOW | Distinct from batch `BATCH/` prefix |
| C13 | Multi-company rule restricts wave records to `company_id in company_ids` | `security/stock_picking_batch_security.xml` | domain_force | L3 | HIGH | Community | LOW | Same rule covers batch and wave |
| C14 | Wave picking assignment search excludes pickings already in waves | `models/stock_move.py` | 10–13 | L3 | HIGH | Community | LOW | Prevents batch↔wave mixing |
| C15 | `stock.add.to.wave` wizard enables manual addition of move lines to existing or new wave | `wizard/stock_add_to_wave.py` | 36–69 | L3 | HIGH | Community | LOW | Validates single-company constraint |
| C16 | `action_merge()` blocks merging batch with wave (`is_wave` mismatch check) | `models/stock_picking_batch.py` | 333–334 | L3 | HIGH | Community | LOW | UserError raised |
| C17 | No `stock_barcode_picking_wave` module present in Community edition | filesystem search | — | L3 | HIGH | Community | LOW | Enterprise-only barcode integration |
| C18 | `_auto_wave_lines_into_new_waves()` creates new waves respecting batch size limits | `models/stock_move_line.py` | 275–387 | L3 | HIGH | Community | LOW | Uses `_is_line_auto_mergeable()` |
| C19 | `action_confirm()` transitions wave from `draft` to `in_progress` and confirms pickings | `models/stock_picking_batch.py` | 220–228 | L3 | HIGH | Community | LOW | Also called by `batch_auto_confirm` in `_add_to_wave` |
