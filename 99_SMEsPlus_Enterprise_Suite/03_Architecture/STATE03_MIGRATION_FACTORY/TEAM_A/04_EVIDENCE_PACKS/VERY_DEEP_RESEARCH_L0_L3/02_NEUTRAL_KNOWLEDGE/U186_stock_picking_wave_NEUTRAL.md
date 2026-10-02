# U186 — Wave Transfer: Neutral Knowledge Summary

**Unit:** U186 | **Module:** stock_picking_wave (part of Batch Transfer)
**Group:** G06 | **Priority:** P2
**Knowledge date:** 2026-10-02

---

## What Is a Wave Transfer?

A wave transfer is a warehouse operation grouping technique that clusters individual stock operations (move lines) from multiple transfers into a single coordinated unit — the "wave" — so that pickers can process many product lines in one physical trip through the warehouse. Unlike a batch transfer (which groups whole deliveries), a wave can span partial lines from multiple transfers and is typically organised by product, product category, or source location zone.

In Odoo 19.0, wave transfers are not a separate object type. They are batch transfer records carrying a flag (`is_wave = True`) and are stored in the same table as ordinary batch transfers. The distinction affects naming, UI actions, creation logic, and how grouping criteria are applied.

---

## Lifecycle

A wave transfer passes through four states:

1. **Draft** — created but not yet confirmed; member pickings may still be in any compatible state.
2. **In Progress** — confirmed; all member pickings are confirmed; picking and packing operations can begin.
3. **Done** — all non-cancelled member pickings have been validated.
4. **Cancelled** — all member pickings were cancelled; the wave is automatically cancelled.

State is derived automatically from the state of member transfers. Once a wave reaches Done or Cancelled, the state cannot revert.

---

## How Waves Are Created

### Manual creation

A user selects move lines from the stock operation list view and invokes the "Add to Wave" action. A wizard appears allowing the user to attach lines to an existing open wave or create a new one. If a new wave is created, it is named automatically using the wave sequence (prefix `WAVE/`).

When lines are added, the system checks whether the source picking's entire set of move lines is being taken:
- If yes, the whole picking is linked to the wave without modification.
- If no, the picking is split: a new picking is created carrying only the selected lines and moves; the original picking retains the remainder.

### Automatic wave creation (auto-wave)

If the operation type has automatic batching enabled with at least one wave grouping criterion active (product, product category, or location), then whenever stock is assigned to move lines (via the availability reservation process), the system attempts to assign those lines to an existing compatible wave or create a new one.

Eligibility for auto-wave assignment requires the line's transfer to be fully available (state `assigned`), the line to have a non-zero demanded quantity, and the line not already to be part of a wave.

---

## How Lines Are Grouped into Waves

The operation type configuration controls wave grouping criteria:

- **By product** — only lines for the same product are placed in the same wave.
- **By product category** — only lines whose product belongs to one of the configured wave categories are placed in the same wave.
- **By location** — lines are grouped by their nearest ancestor in a configured list of wave locations; only lines falling under the same ancestor location are grouped together.

Multiple criteria can be combined. When searching for an existing wave to extend, the system matches all active criteria simultaneously.

---

## Picking and Move Structure Inside a Wave

A wave holds multiple transfers (`picking_ids`). Each transfer may carry one or more stock moves, and each move may carry one or more move lines. The wave provides aggregate views of all moves and move lines across its member transfers. When batch size limits are configured (maximum moves or maximum transfers per batch), these are checked before adding lines to an existing wave or before filling a new wave.

---

## Validation

Validating a wave validates all non-done, non-cancelled member transfers in a single operation. Transfers that are in a waiting state with no processed quantities are detached from the wave (rather than cancelled) before validation proceeds. The wave itself reaches the Done state automatically once all member transfers complete.

---

## Automatic Availability Check

The "Check Availability" button on a wave calls the stock availability reservation method on all member transfers. This also re-triggers the auto-wave logic for any backorder transfers created as a result of partial processing.

---

## Relationship to Batch Transfers

Batch transfers and wave transfers share the same underlying data model. The practical differences are:

- Batch transfers group whole transfers for a responsible user (e.g., a driver consolidating deliveries); creation is triggered when a transfer is confirmed.
- Wave transfers group individual pick lines within a warehouse zone; creation is triggered when stock is assigned to lines.
- The two types cannot be merged with each other.
- Batch auto-grouping criteria and wave auto-grouping criteria are configured separately on the operation type.

---

## Multi-Company Behaviour

Each wave is tied to a single company and is only visible to users operating within that company. The operation type, member transfers, and responsible user must all belong to the same company.

---

## Barcode Scanning

Barcode scanning support for wave transfers is available in the Enterprise edition only and is not present in the Community source code.

---

## Naming and Sequences

Wave transfer names follow the pattern `WAVE/{operation-type-code}/{sequence-number}`. The sequence is independent from the batch sequence, so wave numbers and batch numbers do not collide.

---

## Claims Table (Neutral — 9 columns)

| # | Neutral Claim | Concept Described | Source File | Line/Section | Evidence Level | Confidence | Scope | Notes |
|---|---|---|---|---|---|---|---|---|
| C1 | Wave transfers are a variant of batch transfers identified by a dedicated flag; there is no separate wave model | Architecture | `models/stock_picking_batch.py` | 9, 60 | L3 | HIGH | Community | `is_wave = True` Boolean flag |
| C2 | The wave lifecycle uses four states: initial planning, active processing, fully completed, and cancelled | Lifecycle | `models/stock_picking_batch.py` | 40–46 | L3 | HIGH | Community | draft / in_progress / done / cancel |
| C3 | Wave state is derived automatically from the collective state of all member transfers | State derivation | `models/stock_picking_batch.py` | 144–155 | L3 | HIGH | Community | Computed field |
| C4 | A wave holds an ordered set of transfers linked through a foreign key on each transfer | Data structure | `models/stock_picking_batch.py` | 24–27 | L3 | HIGH | Community | `picking_ids` One2many |
| C5 | The operation type associated with a wave controls naming and grouping behaviour | Configuration | `models/stock_picking_batch.py` | 47–49; `models/stock_picking.py` 21–25 | L3 | HIGH | Community | `picking_type_id` |
| C6 | Adding lines to a wave may split the source transfer when only a subset of its lines is selected | Picking split | `models/stock_move_line.py` | 31–119 | L3 | HIGH | Community | `_add_to_wave()` |
| C7 | The automatic wave assignment process is initiated each time stock is reserved for move lines | Auto-trigger | `models/stock_move.py` | 39–41 | L3 | HIGH | Community | `_action_assign()` hook |
| C8 | A move line qualifies for automatic wave placement only when its transfer is fully available and it is not already part of a wave | Eligibility | `models/stock_move_line.py` | 121–129 | L3 | HIGH | Community | `_is_auto_waveable()` |
| C9 | Confirming a wave validates all eligible member transfers in a single step | Validation | `models/stock_picking_batch.py` | 239–281 | L3 | HIGH | Community | `action_done()` |
| C10 | The availability reservation button on a wave triggers reservation on all member transfers | Assign | `models/stock_picking_batch.py` | 283–285 | L3 | HIGH | Community | `action_assign()` |
| C11 | Wave grouping can be configured by product identity, product category, or warehouse zone location | Grouping | `models/stock_picking.py` | 21–25, 72–73 | L3 | HIGH | Community | Three grouping fields |
| C12 | Wave transfer names follow a separate sequence from batch transfers, using a distinct prefix | Naming | `data/stock_picking_batch_data.xml` | seq_picking_wave | L3 | HIGH | Community | `WAVE/` prefix |
| C13 | Each wave belongs to one company and is not accessible to users of other companies | Multi-company | `security/stock_picking_batch_security.xml` | domain_force | L3 | HIGH | Community | Record rule |
| C14 | The stock availability search deliberately excludes transfers already associated with a wave | Isolation | `models/stock_move.py` | 10–13 | L3 | HIGH | Community | Prevents batch/wave mixing |
| C15 | A user-facing wizard allows manual addition of selected operations to an existing or new wave transfer | Manual UX | `wizard/stock_add_to_wave.py` | 36–69 | L3 | HIGH | Community | `stock.add.to.wave` |
| C16 | Batch transfers and wave transfers cannot be merged with each other | Constraint | `models/stock_picking_batch.py` | 333–334 | L3 | HIGH | Community | `action_merge()` guard |
| C17 | Barcode scanning integration for wave transfers is absent from the Community edition | Barcode | filesystem | — | L3 | HIGH | Community | Enterprise-only |
| C18 | New wave creation respects configured limits on maximum moves and maximum transfers per wave | Size limits | `models/stock_move_line.py` | 275–387 | L3 | HIGH | Community | `_is_line_auto_mergeable()` |
| C19 | Confirming a newly created wave also confirms all its member transfers | Confirm cascade | `models/stock_picking_batch.py` | 220–228 | L3 | HIGH | Community | `action_confirm()` calls `picking_ids.action_confirm()` |
