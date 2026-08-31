# A12 — Migration / Provenance / Historical Continuity Evidence

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Research Inventory facts needed for migration: opening quantity, location ownership, lot/serial/package provenance, in-flight transfers, reservation state, cost/valuation history interface, adjustments, manufacturing stock state, cross-year continuity, record identity/provenance, duplicate/orphan/invalid states | Claude (Team A, DR-002) | This artifact | 2026-08-31 | Independent Evidence Review (pending) | VERIFIED (source-based) | Evidence semantics only — does not design the Migration Factory implementation |

## 1. Opening / on-hand quantity

Migration-relevant fact: `stock.quant.quantity` is the atomic on-hand fact, keyed on `(product, location, lot, package, owner)` (A3 §1). A migration must reproduce this exact five-key granularity per bin, not merely a per-product total — collapsing lot/package/owner distinctions during migration would lose information the source model itself treats as load-bearing (e.g., `stock.quant.value` is prorated per-bin when `lot_valuated`).

## 2. Location/warehouse ownership

Warehouse configuration is a **generator**, not static data (A5 §1, A10 SAAS-04) — a migration must either regenerate the `reception_steps`/`delivery_steps`-derived location/route graph in the target system's own terms, or explicitly map each source location's `usage` (7 values, A5 §2) to an equivalent target concept. Simply copying `stock.location` rows without their generative configuration would produce an inert, non-functional route graph.

## 3. Lot/serial/package provenance

- Lot/serial: `product.template.tracking` (serial/lot/none) determines whether provenance exists at all for a given product (A5 §7); a non-tracked product has no lot/serial history to migrate by construction.
- Package: GROUP A's own §08 finding (reused DELTA-FIRST, not independently re-tested this pass) — `stock.package.history` is a **separate, append-only, frozen snapshot** created once a picking is Done, not an FK back to a possibly-reused live `stock.package` row. This is the single most migration-relevant package fact GROUP A identified: a live package row can be reused/repurposed over time, but its history snapshots are immutable point-in-time records. A migration must decide whether to migrate live package state, historical snapshots, or both, and must not conflate the two.

## 4. Open/in-flight transfers

Any `stock.move`/`stock.picking` not yet `done`/`cancel` at migration cutover represents an in-flight physical transfer. Because `stock.move.quantity`'s meaning is state-dependent (A3 §2 — "picked so far" before done, "what actually moved" at done), a migration snapshot taken mid-transfer must preserve which state each move was in, not just its quantity fields, to avoid misinterpreting a partially-picked move as either fully done or not started.

## 5. Reservation state

`stock.quant.reserved_quantity` and the `stock.move.line` records created during `_action_assign()` represent live reservation state (A3 §2, §6). A migration cutover must decide whether to migrate reservations as-is (preserving exact bin-level allocation) or to re-derive them fresh in the target system post-migration — carrying stale reservations across a system boundary risks reserving stock against orders/documents whose own migration mapping may not yet exist.

## 6. Cost/valuation history interface

Per A9: valuation lives directly on `stock.move.value`/`remaining_qty`/`remaining_value`, not a separate ledger. A migration wanting to preserve FIFO cost-layer history must therefore migrate the relevant `stock.move` records themselves (with their `value`/`remaining_qty` fields), not merely current on-hand quantities — the FIFO remaining-quantity mechanism is intrinsically tied to move-level history, confirmed by `remaining_qty`'s own dependency on `product_id.stock_move_ids.value` (a product-wide, multi-move computation).

## 7. Inventory adjustments

Per A7: the only path to directly overwrite on-hand quantity outside normal move flow is the `inventory_quantity`/`inventory_diff_quantity` count-and-apply mechanism, which itself generates a `stock.move` once applied. A migration does not need a separate "adjustment record" concept distinct from ordinary moves — an adjustment is, by the time it is `done`, an ordinary `stock.move` to/from the `inventory` (Inventory Loss) usage location.

## 8. Manufacturing-related stock state

Per A8 §3: raw-material consumption and FG receipt are both ordinary `stock.move` records tagged with `raw_material_production_id`/`bom_line_id` or `production_id`. A migration of an in-flight `mrp.production` (state `confirmed`/`progress`/`to_close`) must migrate its linked component/FG moves consistently with the MO's own state, since `_post_inventory()` computes FG quantity as `qty_producing - qty_produced` — a mid-production snapshot that doesn't preserve both figures would misstate remaining production.

## 9. Cross-year inventory continuity

Not directly evidenced this pass — no fiscal-year-boundary or year-end-closing-specific Inventory field or method was read in the modules examined (this sits closer to the Accounting-owned period/cutoff question flagged as open in A7 §4/A9 §7). Registered `EVIDENCE_MISSING` in A14 (N-A12-01).

## 10. Source record identity / provenance

Every `stock.move`/`stock.quant`/`stock.picking` is a standard Odoo integer-ID record with no separate external-reference/provenance field observed in the core models read this pass (beyond the cross-domain link fields like `sale_line_id`/`purchase_line_id`/`account_move_id`, which are themselves internal FKs, not external-system identifiers). A migration will need to introduce its own provenance/external-ID mapping layer — the source does not provide one natively for Inventory records.

## 11. Duplicate/orphan/invalid states — migration-invalid states possible via direct SQL

Per A2/A13: no DB CHECK constraints prevent negative quantities, over-fulfillment, or bin-key duplication; the `stock_move_line.move_id` FK is `ON DELETE SET NULL` rather than a cascading/restricting constraint (GROUP A DB-forensics finding, reused DELTA-FIRST). This means a migration extracting data via **direct SQL** (rather than through the ORM) could encounter: orphaned `stock.move.line` rows (move deleted, line's `move_id` nulled rather than the line being removed), duplicate quant bins pending `_merge_quants()` cleanup, or negative on-hand quantities that the application layer would normally have prevented from being created through its own UI/API. A migration extraction process must defensively handle all three, not assume ORM-level invariants held at extraction time.

No target Migration Factory implementation is designed here — this document prepares evidence semantics only, per DR-002 §7/A12's explicit instruction.

No Evidence = No Progress. DELTA-FIRST.
