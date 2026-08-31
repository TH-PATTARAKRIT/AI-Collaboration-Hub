> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Phase 2 of 10 — Inventory Core Deep Research
> All source paths relative to `ACCOUNT/01 ACCOUNT/SOURCE CODE/02 OTHER/` unless stated otherwise. DB evidence from
> the same schema-only extraction used in Phase 1 (`schema_only.sql`, from `iTEST02_2026-06-14_14-41-19.dump`).
> Prior evidence reused by ID, not re-derived: WH-01..26 (warehouse/location master data), UOM-01..22, PRD-01..18
> — see `01_SHARED_MASTER_DEPENDENCY_MAP.md`. This phase covers the movement/transaction layer on top of that data.

# 02 — INVENTORY CAPABILITY MODEL

## 00 — Scope & Method

Physical stock reality only — `stock.move`, `stock.move.line`, `stock.quant` (the on-hand ledger), the operational
documents wrapping them (`stock.picking`/`stock.picking.type`), backorder, return, lot/serial, package,
replenishment, and put-away. Inventory valuation/accounting consequence is explicitly out of scope here (interface
observation only, per governance Section 19) — the `account_move_id` FK on `stock.move` is noted where found but
not traced into Accounting Core.

**Structural note carried from source research:** several Odoo-19 filenames differ from older/expected
conventions and would return false negatives on a naive grep: `stock.picking.type` lives inside `stock_picking.py`
(no separate file); Lot/Serial is `stock_lot.py` (not `stock_production_lot.py`); Package is `stock.package` (not
`stock.quant.package`) split across `stock_package.py`/`stock_package_type.py`/`stock_package_history.py`;
Put-away lives in `product_strategy.py` (not a `stock_putaway.py`).

## 01 — Rollup Index

| # | Concept | Model(s) | Independent lifecycle? | GROUP A coupling | Confidence |
|---|---|---|---|---|---|
| 1 | Movement | `stock.move`, `stock.move.line` | Yes — the only real state machine in this phase | Purchase: direct sync `create()`. Sale: indirect via `stock.rule.run()` | VERIFIED FACT |
| 2 | Reservation/Quantities | `stock.quant` | No — a ledger, mutated only by move/move-line methods | Sale reads compute fields (advisory only, no confirmation gate). Purchase re-derives `qty_received` from done moves | VERIFIED FACT |
| 3 | Picking/Transfer | `stock.picking`, `stock.picking.type` | No — state fully derived from child moves | Purchase carries `picking_type_id` directly; Sale reads `picking_type_id.code` | VERIFIED FACT |
| 4 | Backorder | same `stock.picking` (self-referential) | n/a — not a separate model | Not directly referenced by Sale/Purchase; reached only via `stock.picking`/`stock.move` | VERIFIED FACT |
| 5 | Return | same `stock.picking` (self-referential) + wizard | n/a — wizard is transient | Not directly referenced in files read; EVIDENCE_MISSING on Sale-side return button wiring | VERIFIED FACT for mechanism |
| 6 | Lot/Serial | `stock.lot` | No — gated by `product.template.tracking` (Phase 1 scope) | Not directly grepped against Sale/Purchase this pass | VERIFIED FACT |
| 7 | Package | `stock.package(.type/.history)` | No — derived from contained quants | Not directly grepped against Sale/Purchase this pass | VERIFIED FACT |
| 8 | Replenishment | `stock.warehouse.orderpoint`, `stock.rule` | n/a | Purchase (`purchase_stock`) supplies the `'buy'` action + `_run_buy`; core `stock` has no compile-time dependency on Purchase | VERIFIED FACT |
| 9 | Put-away | `stock.putaway.rule` | n/a | Not directly referenced by Sale/Purchase — pure Inventory-internal placement | VERIFIED FACT |

---

# 02 — MOVEMENT CORE (`stock.move` / `stock.move.line`)

Read in full: `stock_move.py` (2675 lines), `stock_move_line.py` (1236 lines).

## `stock.move` — evidence table

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| MOV-01 | stock_move.py | L18–22 | `_name='stock.move'`, `_order='sequence, id'`, `_rec_name='reference'` |
| MOV-02 | stock_move.py | L54–57 | `product_qty` — **compute-only**, "Real Quantity" in product's default UoM |
| MOV-03 | stock_move.py | L58–65 | `product_uom_qty` — "Demand", the **planned** quantity; lowering it does not generate a backorder |
| MOV-04 | stock_move.py | L75–90 | `location_id`(Source), `location_dest_id`(intermediate/actual dest), `location_final_id`(true end target of a chain) — three distinct location concepts |
| MOV-05 | stock_move.py | L98–105 | `move_dest_ids`/`move_orig_ids` — chaining via `stock_move_move_rel` (e.g. pick→pack→ship) |
| MOV-06 | stock_move.py | L106 | `picking_id` — a move optionally belongs to one transfer document |
| MOV-07 | stock_move.py | L107–120 | `state`: `draft`→`waiting`/`confirmed`→`partially_available`/`assigned`→`done`; plus `cancel` |
| MOV-08 | stock_move.py | L121–124 | `picked` — stored compute, "just indicative", a pre-done marker distinct from `state` |
| MOV-09 | stock_move.py | L130 | `origin` — free-text traceability to originating document, not a relational FK |
| MOV-10 | stock_move.py | L131–138 | `procure_method`: `make_to_stock` vs `make_to_order` (creates a procurement on confirm) |
| MOV-11 | stock_move.py | L153 | `move_line_ids` — planned/parent ↔ actual/detail relationship |
| MOV-12 | stock_move.py | L166–168 | `warehouse_id` is only "for route selection on next procurement" — **not** the authoritative operational location |
| MOV-13 | stock_move.py | L171–172 | `quantity` — compute+inverse+store, sum of move-line `quantity` — the **actual/reserved-or-done** amount, distinct from both `product_uom_qty` and `product_qty` |
| MOV-15 | stock_move.py | L376–380 | `_compute_product_qty`: `product_qty` is always derived from `product_uom_qty`, never the reverse |
| MOV-16 | stock_move.py | L400–437 | `_quantity_sml`/`_compute_quantity` docstring: `quantity` drives `_action_done`'s backorder-vs-extra-move decision |
| MOV-18 | stock_move.py | L481–486 | `_set_product_qty` **unconditionally raises UserError** — `product_qty` is read-only by design, guarded even against accidental writes |
| MOV-19 | stock_move.py | L488–499 | `_compute_product_availability`: if `done`, availability=`product_qty` (what was moved); else `min(product_qty, quant free qty)` (what could still be reserved) — **same field, state-dependent meaning** |
| MOV-22 | stock_move.py | L927–953 | `_do_unreserve()`: cannot unreserve a `done` move (except scrap exception) |
| MOV-23 | stock_move.py | L1541–1596 | `_action_confirm()`: `draft`→`waiting` if chained/make-to-order, else `confirmed`; builds a `stock.rule.Procurement` and calls `stock.rule.run()` for make-to-order |
| MOV-24 | stock_move.py | L1596–1624 | Negative-demand handling: source/dest **swapped**, treated as a return |
| MOV-27 | stock_move.py | L1756–1813 | `_update_reserved_quantity`: calls `stock.quant._get_reserve_quantity`, creates/updates move lines; `taken_quantity` may be **less than** requested (partial reservation) |
| MOV-28 | stock_move.py | L1818–1821 | `_should_bypass_reservation()` = bypass location OR non-storable product |
| MOV-30 | stock_move.py | L1894–2035 | `_action_assign()`: "considered reserved once Σ(reserved_qty for move lines) = `product_qty`" |
| MOV-31 | stock_move.py | L2037–2077 | `_action_cancel()`: cannot cancel a `done` move (except scrap) — raises UserError instructing a return instead. **CORRECTIVE PRECISION UPDATE (session CORR-003, POCANC-13)**: re-read at L2038-2039 for a Purchase-cancellation follow-up — the exact guard is `any(move.state=='done' and move.location_dest_usage!='inventory' for move in self)`, i.e. an **all-or-nothing check over the whole recordset** passed to the call (one done move anywhere in a batch blocks the entire batch, not just itself), and the exception is keyed on the **destination location's `usage=='inventory'`** (Inventory Loss/scrap-adjustment), not a separate "scrap move" concept. See `04_PURCHASE_CAPABILITY_MODEL.md` §04 for the full cascade this feeds into. |
| MOV-32 | stock_move.py | L2094–2162 | `_action_done()`: `_create_backorder()` called **before** `move_line_ids._action_done()` executes the physical transfer |
| MOV-34 | stock_move.py | L2167–2183 | `_create_backorder()`: if `quantity < product_uom_qty`, remainder split via `_split()` into a new move — the literal backorder mechanism |
| MOV-37 | stock_move.py | L2261–2281 | `_recompute_state()`: `quantity>=product_uom_qty`→assigned; `0<quantity<product_uom_qty`→partially_available; make_to_order-unfinished→waiting; else confirmed |
| MOV-40 | stock_move.py | L1232–1329 | `_merge_moves()`: identical-characteristic moves silently merged into one record — **move cardinality is not stable** relative to source document lines |
| MOV-44 | stock_move.py | whole file | **No `models.Constraint`/`_sql_constraints` declared anywhere** — every quantity/state rule is Python-level, not a DB CHECK |
| MOV-45 | stock_move.py | L822–836 | `_update_orderpoints()` — moves touch `stock.warehouse.orderpoint` recomputation directly |
| MOV-46 | stock_move.py | grepped | **No branch-level field or logic** anywhere in this file — `company_id` is the only organizational scope |

## `stock.move.line` — evidence table

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| MOVL-02 | stock_move_line.py | L21–30 | `picking_id`, `move_id` — **neither `required=True`**; `company_id` required |
| MOVL-03 | stock_move_line.py | L37–42 | `quantity` (line UoM) vs `quantity_product_uom` (product's own UoM) — two parallel representations |
| MOVL-06 | stock_move_line.py | L83 | `state = related='move_id.state'` — **the line has no independent lifecycle** |
| MOVL-09 | stock_move_line.py | L172–180 | `_check_lot_product`: lot's product must match line's product |
| MOVL-10 | stock_move_line.py | L182–185 | `_check_positive_quantity` — ORM-level only, no DB CHECK exists |
| MOVL-11 | stock_move_line.py | L338–378 | `create()`: a line without `move_id` auto-creates its own parent move — lines can precede and spawn a move (barcode/immediate-transfer path) |
| MOVL-13 | stock_move_line.py | L400–419 | A line created already `state=='done'` moves the quant immediately — can be born already executed |
| MOVL-14 | stock_move_line.py | L422–553 | Editing a reserved line unreserves-old/reserves-new; editing a **done** line undoes/redoes the actual quant transfer — history is physically re-applied, not just recorded |
| MOVL-15 | stock_move_line.py | L555–563 | A `done`/`cancel` line can **never** be deleted — immutability of executed history at ORM level |
| MOVL-17 | stock_move_line.py | L588–707 | `_action_done()`: per line, `_synchronize_quant(-qty, source, "reserved")` → `_synchronize_quant(-qty, source)` → `_synchronize_quant(+qty, dest)` |
| MOVL-18 | stock_move_line.py | L709–729 | `_synchronize_quant()` — the single low-level primitive every quantity/location change funnels through |
| MOVL-20 | stock_move_line.py | L995–1011 | Auto-created parent move gets `product_uom_qty=0` if picking not done, else `=quantity` — **proves planned demand can be zero while actual quantity is non-zero** |

## Database evidence

`stock_move` (schema): `company_id, product_id, product_uom, location_id, location_dest_id, product_uom_qty, date,
procure_method` NOT NULL; `state, quantity, product_qty, picked` nullable at DB level. Also carries
`account_move_id, sale_line_id, purchase_line_id, weight, production_id, workorder_id, bom_line_id, repair_id`, etc.
— **none declared in `stock/models/stock_move.py`**; injected by `sale_stock`/`purchase_stock`/`stock_account`/
`mrp`/`repair` extending the same table. `stock_move_sale_line_id_fkey`→`sale_order_line`, `..._purchase_line_id_fkey`
→`purchase_order_line`, `..._account_move_id_fkey`→`account_move` (all `ON DELETE SET NULL`) are the literal FKs
from movement to the commercial/accounting documents. `stock_move_line.move_id` FK is `ON DELETE SET NULL` —
**more permissive than the ORM**, which normally prevents an orphaned line from being created through the app; a
bulk/direct-SQL migration step could produce states the live application never creates. No CHECK constraint exists
on either table.

## GROUP A consumers — asymmetry (flagged for later phases)

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| GRPA-01 | purchase_stock/models/purchase_order_line.py | L364–370 | `_create_stock_moves()` calls `self.env['stock.move'].create(values)` **directly and synchronously** |
| GRPA-04/05 | sale_stock/models/sale_order_line.py | L369–405 | `_create_procurements()`/`_action_launch_stock_rule()` builds a `stock.rule.Procurement` tuple and calls `stock.rule.run()` — Sale creates moves **indirectly**, through the procurement/rule engine |

**Purchase creates `stock.move` rows synchronously and directly; Sale creates them asynchronously and indirectly
via `stock.rule.run()`.** A migration mapping that assumes symmetric "SO line → move" / "PO line → move" creation
would be wrong for the Sale side. `stock.rule.py` itself is covered under Replenishment (§09) below.

## Synthesis — Movement Core

- **Business purpose**: `stock.move` is the planned/authorized unit of movement ("move X, qty Y, A→B, by document
  Z"); `stock.move.line` is the executed/detailed record (which lot, package, exact location, how much). The split
  exists because one planned move can be fulfilled by many quant-level reservations, and demand vs. actual are
  allowed to diverge (resolved via backorder or extra move).
- **Actor/maintainer/consumer**: `stock` owns both models outright. `sale_stock`/`purchase_stock` are the two
  immediate consumers turning commercial documents into moves — asymmetrically. `mrp`/`repair`/
  `purchase_requisition`/`stock_account` all extend the **same tables** rather than creating separate movement
  ledgers — this is the single physical-movement ledger for the whole suite.
- **Source owner observation**: the crux of the Quantity Semantics Register: `product_uom_qty` (Demand/planned),
  `product_qty` (Demand, product's own UoM, compute-only, write-guarded), and `quantity` (actual/reserved, driven
  bottom-up from move lines) — `quantity` means "reserved so far" pre-done and "actually moved" once `done`; no
  field name changes, only the state context changes its meaning.
- **Company/warehouse/branch context**: `company_id` NOT NULL on both tables, enforced via `check_company=True`
  throughout (ORM-level, not DB). `warehouse_id` on the move is route-selection-only and can be **stale** relative
  to the location's own derived warehouse — do not use it as authoritative for reporting/migration. **No branch
  concept** anywhere in this layer (MOV-46).
- **Source-specific coupling (do not copy)**: silent move-merging (MOV-40) breaks 1:1 SO/PO-line↔move assumptions;
  every quantity change funnels through one primitive (`_synchronize_quant`) that defers to `stock.quant` (§03);
  no DB CHECK constraints anywhere — a migration moving data via direct SQL bypasses every business rule.
- **Confidence**: High — both files read in full, every quantity/state claim traces to an exact anchor.
- **Unknown/Conflict**: `stock.rule` pull/push engine internals (`Procurement` class body, `_get_rule()`) — see §09.
  `stock.picking`-level `_create_backorder` vs the move-level one (MOV-34) may differ in trigger timing — see §04/05.
  MRP/Repair/Purchase-Requisition extension columns (production_id, workorder_id, bom_line_id, repair_id, etc.) —
  existence confirmed, semantics out of scope.

---

# 03 — RESERVATION & QUANTITY SEMANTICS (`stock.quant`)

Read in full: `stock_quant.py` (1564 lines). Targeted: `product.py` (quantity compute methods), reservation call
sites in `stock_move.py`/`stock_move_line.py` (method names confirmed via grep before citing).

## The ledger — evidence table

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| QNT-01 | stock_quant.py | L19–23 | One row = one (product, location, lot, package, owner) **bin**, not a transaction log |
| QNT-02 | stock_quant.py | L56 | `company_id` = related from `location_id` — **derived, not independently set** |
| QNT-04 | stock_quant.py | L78–81 | `quantity` — on-hand, per bin |
| QNT-05 | stock_quant.py | L82–86 | `reserved_quantity` — required, default 0.0 — already claimed by a move line |
| QNT-06 | stock_quant.py | L87–90, L119–122 | `available_quantity` = `quantity - reserved_quantity` — **per-bin** free-to-reserve |
| QNT-08 | stock_quant.py | L96–114 | Physical-count fields (`inventory_quantity`, `inventory_diff_quantity`) live on the **same row** as the ledger — count workflow is fused in, not a separate document |
| QNT-11 | stock_quant.py | L617–628 | `_get_removal_strategy`: category wins, else walks location parent chain, else defaults `'fifo'` |
| QNT-13 | stock_quant.py | L1224–1228 | `_quant_tasks()` = merge + clean-reservations + unlink-zero-quants — periodic housekeeping, **not per-transaction** |

## Available/Reserved computation

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| AVL-QNT-01 | stock_quant.py | L793–819 | `_get_available_quantity(...)`: untracked = `SUM(quantity)-SUM(reserved_quantity)`, clamped to 0 unless `allow_negative=True` |
| AVL-QNT-03 | stock_quant.py | L834–914 | `_get_reserve_quantity()`: returns `[(quant, qty)]`; nets against quants already carrying negative "available" before handing out new reservation |
| AVL-QNT-04 | stock_quant.py | L1038–1105 | `_update_available_quantity()` — the **single low-level mutator**; locks the matching row or creates a new one |
| AVL-QNT-08 | stock_quant.py | L1177–1222 | `_merge_quants()` — raw-SQL dedup; exists because **concurrent transactions can each insert a new row instead of updating the same one** — duplicate-key races are expected, cleaned up after the fact |

## Reservation mechanics (on move/move-line)

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| RES-01 | stock_move.py | L107–120 | `assigned` = "reserved"; help text is the authoritative state-meaning source |
| RES-04 | stock_location.py | L411–413 | `should_bypass_reservation()` = usage in (supplier/customer/inventory/production) — virtual/external locations always "available" |
| RES-07 | stock_move.py | L1894 | `_action_assign(force_qty=False)` — confirmed real name via grep, not assumed |
| RES-15 | stock_move_line.py | L588–596 | `_action_done()` — confirmed real name; "actually moves a quant from source to destination, unreserving as needed" |
| RES-17 | stock_move_line.py | L689–699 | Per line: release reservation → decrement source → increment dest |

## Negative stock / oversell

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| NEG-01 | stock_quant.py | L793, L814–819 | Default getter **clamps reported available to 0**; the underlying row's `quantity` column is not itself clamped |
| NEG-05 | schema grep, 0 hits | — | **No DB CHECK constraint** prevents `stock_quant.quantity`/`reserved_quantity` from going negative — entirely an application-layer convention |
| NEG-06 | stock_orderpoint.py | L420, 469, 522 | Reordering-rule logic explicitly reasons about **negative `virtual_available`** as a normal trigger condition — forecast is allowed negative; on-hand is only negative in an oversell edge case |

## Consumer-facing quantity fields (`product.product`/`product.template`)

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| AVL-01 | product.py | L52–64 | `qty_available` — **On-Hand** |
| AVL-02 | product.py | L65–76 | `virtual_available` — **Forecasted** = On-Hand − Outgoing + Incoming |
| AVL-03 | product.py | L77–88 | `free_qty` — **Available-to-Promise** = On-Hand − Reserved |
| AVL-04 | product.py | L89–99 | `incoming_qty` — planned incoming |
| AVL-05 | product.py | L100–110 | `outgoing_qty` — planned outgoing |
| AVL-07 | product.py | L164–213 | Incoming/outgoing domains **explicitly exclude `done` moves** — always "still in flight", never historical |
| AVL-09 | product.py | L253, 256 | On-hand = raw `SUM(stock.quant.quantity)`, **no reservation adjustment** |
| AVL-12 | product.py | L260–262 | Forecast = On-Hand + Incoming − Outgoing exactly as help text states |
| AVL-14 | product.py | L337–388 | With no context, defaults to **all warehouses of `self.env.companies`** — company-scoped by default, not global |

## The six quantity concepts (do not conflate — critical for the later Quantity Semantics Register)

- **On-Hand** (`stock.quant.quantity` / `product.qty_available`) — physically present, raw sum, no reservation
  adjustment. What a warehouse count would show.
- **Reserved** (`stock.quant.reserved_quantity`) — claimed by confirmed-but-not-done move lines; only exists at
  bin level — **no `product.reserved_qty` field exists** (EVIDENCE_MISSING at product level; only the complement
  `free_qty` surfaces).
- **Available/Free-to-Promise** (`stock.quant.available_quantity` per bin; `product.free_qty` at product level) —
  On-Hand − Reserved. The number safe to hand out as a **new** reservation.
- **Incoming** (`product.incoming_qty`) — sum of not-yet-done moves whose destination crosses into scope.
- **Outgoing** (`product.outgoing_qty`) — mirror, not-yet-done moves whose source is in scope, dest leaves it.
- **Forecasted** (`product.virtual_available`) — On-Hand + Incoming − Outgoing; can legitimately go negative
  (used by reordering rules), unlike raw on-hand.

## GROUP A consumers

- **Sale → availability check is advisory only.** `sale_order_line._compute_qty_at_date` reads `qty_available`/
  `free_qty`/`virtual_available` (draft/sent) or the line's own reserved moves (confirmed) purely to drive a UI
  forecast widget. **No `UserError`/block on insufficient stock found anywhere** in the methods read — Sale order
  confirmation is **not gated** by `stock.quant` availability in this codebase.
- **Purchase → receipt increases on-hand, confirmed end-to-end.** `purchase_order_line._prepare_qty_received` sums
  `stock.move.quantity` only over moves that reached `state=='done'` — reaching `done` is exactly the event that
  calls `_action_done`→`_synchronize_quant`→`stock.quant._update_available_quantity`, incrementing the destination
  quant, which `product.qty_available` subsequently sums.
- Both bridge modules reuse the **exact same product-level compute fields** rather than re-deriving their own
  quantity math — these fields are the intended shared quantity-semantics contract across the group.

## Company/warehouse/branch context

A quant's `company_id`/`warehouse_id` are both *related* fields derived from `location_id` — a quant does not carry
independent org identity. Aggregate on-hand/available/forecast figures default to **all warehouses of the active
company set** when no location context is given — the same product can report different `qty_available` under
different company contexts on identical underlying quant rows. No branch concept found layered on top.

## Database evidence / source-specific coupling

No unique/composite index enforces "one row per (product, location, lot, package, owner)" — the uniqueness the
whole reservation algorithm depends on is an **application convention only**, reconciled after the fact by
`_merge_quants`. No CHECK constraint anywhere on `stock_quant` — negative-stock prevention is 100% application-layer
and bypassable by direct SQL or `allow_negative=True`/superuser paths. `quantity` is nullable at DB level while
`reserved_quantity` is `NOT NULL` — an asymmetry a migration must decide how to normalize.

## Confidence / Unknown

High for all mechanics (full read, method names grep-confirmed, not assumed from prior-Odoo-version memory).
**Unknown/deferred**: `stock_move.is_in`/`is_out` DB columns — compute source not opened. Whether NULL
`stock_quant.quantity` rows occur in live data — would require a data query, out of read-only-source scope. The
full procurement/`stock.rule` chain that *creates* delivery/receipt moves (only the consumption side was traced
here) — see §09.

---

# 04 — PICKING / TRANSFER (`stock.picking`, `stock.picking.type`)

Read in full: `stock_picking.py` (2145 lines — both `StockPickingType` L20–535 and `StockPicking` L538–2145 live in
this one file).

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| PICK-02 | stock_picking.py | L42 | `stock.picking.type.code`: `incoming`(Receipt)/`outgoing`(Delivery)/`internal`(Internal Transfer) — the categorization lives on the **type**, not the picking |
| PICK-04 | stock_picking.py | L317–337 | `incoming`→source defaults to Suppliers location; `outgoing`→dest defaults to Customers location; else both default to `warehouse_id.lot_stock_id` — the concrete rule defining Receipt vs Delivery vs Internal |
| PICK-05 | stock_picking.py | L133–139 | `create_backorder`: `ask`/`always`/`never` — lives on **picking type**, a per-operation-type policy |
| PICK-06 | stock_picking.py | L43–46 | `return_picking_type_id` — the type used when returning goods created by this type |
| PICK-09 | stock_picking.py | L575–589 | `state`: `draft, waiting, confirmed, assigned, done, cancel` |
| PICK-10 | stock_picking.py | L815–862 | `_compute_state`: picking state is **entirely derived** from child move states — no independent state machine |
| PICK-13 | stock_picking.py | L560–568 | `backorder_id`/`backorder_ids` and `return_id`/`return_ids` — **Backorder and Return are the same `stock.picking` record type linked to itself**, not separate documents |
| PICK-14 | stock_picking.py | L1396–1456 | `button_validate()` — confirmed real name; runs sanity checks, the backorder-wizard gate, then `_action_done()` |
| PICK-19 | stock_picking.py | L710–713 | `unique(name, company_id)` — real DB constraint, reference uniqueness per company |

## Synthesis — Picking/Transfer

- **Business purpose**: the operational transfer document a warehouse worker executes — one Receipt, Delivery, or
  Internal Transfer, wrapping one or more moves. The type object both classifies and drives defaults.
- **GROUP A consumers (confirmed by grep)**: `sale_stock/models/sale_order.py:287,294` reads `picking_type_id.code`
  directly. `purchase_stock/models/purchase_order.py:24` — PO carries its own FK to `stock.picking.type` (label
  "Deliver To"). Base `purchase` module (no `_stock` suffix) has **zero** `picking_type_id` hits — coupling to
  Inventory is entirely inside the bridge module.
- **Company/warehouse/branch context**: `stock.picking.company_id` is related from `picking_type_id.company_id` —
  inherited, not independently set. No native branch model anywhere in `stock/models/`.
- **Database evidence**: `stock_picking` also carries `sale_id, carrier_id, project_id, ticket_id, batch_id,
  website_id, job_type_id` — **none declared in this module's class** — DB proof that shipping/project/helpdesk/
  batch-picking/website_sale all extend the same table. Same "wide shared table" pattern as Warehouse/Location
  and Movement.
- **Source-specific coupling**: `picking_type.code` is read via **string literal comparison** throughout — any
  migration mapping must preserve the exact values `'incoming'`/`'outgoing'`/`'internal'`.
- **Confidence**: High. **Unknown/Conflict**: none found in scope.

---

# 05 — BACKORDER

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| BO-01 | stock_picking.py | L560–564 | `backorder_id` — self-referential M2O, "links to the shipment which contains the already processed part" |
| BO-03 | stock_picking.py | L133–139 | `create_backorder`: `ask`/`always`/`never` policy switch |
| BO-04 | stock_picking.py | L1531–1544 | `_check_backorder()`: fires only for `ask` type, flags under-picked moves |
| BO-05 | stock_picking.py | L1471–1490 | `_pre_action_done_hook()`: intercepts `button_validate()` before `_action_done()`, opens the wizard if backorder-eligible |
| BO-08 | stock_picking.py | L1561–1599 | `_create_backorder_picking()` → copies the original (`name='/'`, empty moves, `backorder_id=self.id`); unfinished moves/lines re-pointed onto it |
| BO-10 | stock_picking.py | L1496–1499 | `_should_ignore_backorders()` = `bool(self.return_id)` — **a Return picking never triggers its own backorder** |
| BO-11 | wizard/stock_backorder_confirmation.py | L16–37 | `stock.backorder.confirmation` (TransientModel) — per-picking checkbox to backorder or not |

## Synthesis — Backorder

- **Business purpose**: handles partial fulfillment — unfinished lines split into a new `stock.picking` linked via
  `backorder_id`, rather than blocking or losing the original document.
- **Source owner observation**: Backorder is **not a separate model** — it is `stock.picking` self-referencing
  itself. There is no `stock.backorder` business-object model; only the transient confirmation wizard.
- **GROUP A consumers**: not directly referenced by Sale/Purchase by name in files read — reached only indirectly
  via `stock.picking`/`stock.move` fields (§04). EVIDENCE_MISSING for a definitive "Sale never touches
  `backorder_id`" claim.
- **Database evidence**: `stock_backorder_confirmation` table is minimal — confirms it's UI-only; real state lives
  on `stock_picking.backorder_id`/`backorder_ids`.
- **Confidence**: High for the wizard/picking mechanism. **Unknown**: `stock.move._get_picked_quantity()`'s exact
  formula (referenced, not opened in this pass — see §02).

---

# 06 — RETURN

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| RET-01 | stock_picking.py | L566–568 | `return_id`/`return_ids` — same self-referential pattern as Backorder |
| RET-02 | stock_picking.py | L2109–2111 | `_can_return()` = `state=='done'` — **only a fully Done picking is returnable** |
| RET-05 | wizard/stock_picking_return.py | L139–159 | New return picking's `picking_type_id` = original's `return_picking_type_id` if set; source/dest locations **swapped** |
| RET-06 | wizard/stock_picking_return.py | L161–187 | `_create_return()`: unreserves downstream moves, then creates the return picking via `.copy()` of the original |
| RET-07 | wizard/stock_picking_return.py | L25–45 | New return move's locations swapped from `self.move_id`; sets **`origin_returned_move_id = self.move_id.id`** — the exact traceability linkage field |
| RET-08 | wizard/stock_picking_return.py | L47–79 | Return move is spliced into the same `move_orig_ids`/`move_dest_ids` procurement chain as the original — not a free-floating document |
| RET-10 | wizard/stock_picking_return.py | L239–264 | `action_create_exchanges()`: for non-incoming types, builds `Procurement` tuples and calls `stock.rule.run()` — re-enters the same replenishment engine as orderpoints |

## Synthesis — Return

- **Business purpose**: reverses a completed (`done`) transfer, remaining traceably linked to the original document
  and to the specific move lines it reverses.
- **Source owner observation**: like Backorder, Return has **no dedicated persistent business-object model** —
  `stock.return.picking(.line)` are wizard-only (TransientModel); the durable record is an ordinary `stock.picking`
  distinguished by `return_id`. The true traceability primitive is **`stock.move.origin_returned_move_id`**, a
  field on the move, not the picking — must be preserved in any migration mapping.
- **GROUP A consumers**: not found directly referencing the return wizard or `origin_returned_move_id` in the
  grep passes performed — EVIDENCE_MISSING on whether Sale's "Return" button is a thin wrapper over this wizard.
- **Database evidence**: `stock_return_picking` carries a `ticket_id` column **not present** in the wizard class —
  DB proof `helpdesk` extends the return wizard. `stock_return_picking_line` carries `to_refund` **not declared**
  in the base line model — proof `stock_account`/`sale` layer on refund-accounting behavior.
- **Confidence**: High for the wizard mechanics. **Unknown/Conflict**: `returned_move_ids` (referenced from the
  wizard at L61/L68) was **not located as a field definition** in the portions of `stock_move.py` read — flagged
  as **UNKNOWN — verify before relying on this reverse-lookup relation**, not invented.

---

# 07 — LOT / SERIAL (`stock.lot`)

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| LOT-01 | stock_lot.py | L24–29 | `stock.lot` (Odoo 19 renamed away from "Production Lot"/`stock_production_lot.py`) |
| LOT-02 | product.py | L838–845 | `product.template.tracking`: `serial`/`lot`/`none`, required, default `none` — **the field that makes a product lot/serial/untracked**, confirming the hypothesis |
| LOT-03 | stock_lot.py | L44–48 | A lot can only attach to a product with `tracking != 'none'` AND `is_storable=True` |
| LOT-06 | stock_picking.py | L293–300 | `incoming`→`use_create_lots=True` (Receipts create new lots); `outgoing`→`use_existing_lots=True` (Deliveries consume existing) |
| LOT-07 | stock_lot.py | L103–126 | `_check_unique_lot`: name+product uniqueness per company, including cross-company dedup |
| LOT-10 | stock_lot.py | L52–53, 210–235 | On-hand quantity for a lot is **derived** by summing quants filtered by `lot_id`, not stored directly |
| LOT-12 | stock_lot.py | L61–63, 173–179 | Setting a lot's `location_id` on the form **actually executes a stock move**, not a pure data edit |

## Synthesis — Lot/Serial

- **Business purpose**: traceability unit for lot/serial-tracked products — anchor for recalls, expiry, and
  forward/backward genealogy.
- **Source owner observation**: tracking mode lives on `product.template` (Phase 1 scope), not on `stock.lot` — a
  lot's existence rules are downstream of a product-master setting, a genuine cross-cluster dependency.
- **GROUP A consumers**: not directly grepped against Sale/Purchase this pass — EVIDENCE_MISSING.
- **Database evidence**: `stock_lot` carries `standard_price`, `avg_cost`, `expiration_date`, `use_date`,
  `removal_date`, `alert_date` — **none declared** in the class read — proof `product_expiry`/landed-cost modules
  extend it.
- **Confidence**: High. **Unknown**: `produce_line_ids` (referenced, likely an MRP field) not defined in any file
  read this pass.

---

# 08 — PACKAGE (`stock.package`, `.type`, `.history`)

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| PKG-01 | stock_package.py | L16–23 | `stock.package` (Odoo 19 renamed from `stock.quant.package`) — packages nest recursively |
| PKG-03 | stock_package.py | L44–49 | `parent_package_id`/`child_package_ids` (current) vs `package_dest_id`/`child_package_dest_ids` (**destination**) — two parallel hierarchies |
| PKG-09 | stock_package_history.py | L6–23 | A **separate, append-style snapshot** created once a picking is Done, with frozen text fields — Done pickings count packages via history, not live search |

## Synthesis — Package

- **Business purpose**: groups quants (and other packages) as one handling unit — "what travels together" (source)
  vs "what it'll be packed into" (destination) — freezing into history once Done.
- **Source owner observation**: the **live-vs-historical split is the single most migration-relevant fact** in
  this cluster — a naive "just migrate `stock_package` rows" approach loses the Done-picking snapshot semantics,
  since history is a genuinely distinct, denormalized table, not an FK back to a (possibly since-reused) live row.
- **Database evidence**: `stock_package_type` carries `shipper_package_code`/`package_carrier_type` **not
  declared** in the class read — proof a shipping/carrier module extends it.
- **Confidence**: High for the model/hierarchy. **Unknown**: `action_put_in_pack`'s exact packing algorithm
  (delegated to `stock_move_line.py`, not opened this pass).

---

# 09 — REPLENISHMENT (`stock.warehouse.orderpoint`, `stock.rule`)

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| REPL-01 | stock_orderpoint.py | L21–26 | `stock.warehouse.orderpoint` — "Minimum Inventory Rule", the reordering rule |
| REPL-04 | stock_orderpoint.py | L101–104 | `unique(product_id, location_id, company_id)` — one orderpoint per product/location/company |
| REPL-05 | stock_orderpoint.py | L417–431 | `_get_qty_to_order()`: fires when `qty_forecast < product_min_qty`; order qty = `max(min,max) - forecast` |
| REPL-06 | stock_orderpoint.py | L707–745 | `_procure_orderpoint_confirm()`: builds a `Procurement` tuple, calls `stock.rule.run()` — **an orderpoint never creates a PO/move itself**, only emits an abstract need |
| REPL-07 | stock_rule.py | L63–65 | Core `stock.rule.action`: `pull`/`push`/`pull_push` **only** — `'buy'`/`'manufacture'` are **not** in core |
| REPL-08 | stock_rule.py | L450–500 | `run()` dispatches by **reflective lookup** `_run_%s % action` — logs, doesn't crash, if the method doesn't exist |
| REPL-09 | stock_rule.py | L161–165 | First-party comment: overridden "in mrp and purchase_stock" — confirms this is intentional architecture |
| REPL-10/11 | [XMOD] purchase_stock/models/stock_rule.py | L18, 59 | `purchase_stock` adds `'buy'` to the selection AND supplies `_run_buy` — this is where a PO actually gets created from a procurement need |
| REPL-13 | data/stock_sequence_data.xml | L46–57 | Daily cron `ir_cron_scheduler_action` — the concrete scheduled trigger for the whole engine |
| REPL-15 | stock_orderpoint.py | L76–79 | `route_id` domain references string values `'buy'/'manufacture'` **inside core `stock`** even though the Selection doesn't define them — a real (if minor) crack in the otherwise clean isolation |

## Synthesis — Replenishment

- **Business purpose**: "keep at least min, top up to max" per product/location; when forecast falls below min, a
  procurement need is raised (daily cron or manual button) and handed to the generic rule engine.
- **Source owner observation**: the cleanest evidence of core-module isolation discipline in this whole domain —
  `stock` defines the abstract need and a reflective dispatch contract, genuinely not knowing how to fulfill
  `'buy'`. The dependency direction is one-way: `purchase_stock` depends on `stock`'s contract; `stock` has no
  compile-time dependency on `purchase_stock`.
- **GROUP A consumers**: confirmed directly (REPL-10/11) — this fully answers "does replenishment connect to
  Purchase": yes, via reflective dispatch, not a direct call.
- **Database evidence**: `stock_warehouse_orderpoint` carries `supplier_id`/`bom_id` **not declared** in the core
  class — DB-level proof `purchase`/`mrp` extend the orderpoint row exactly as the source predicts.
- **Confidence**: High for the trigger chain and core/extension boundary. **Unknown**: `stock.rule.Procurement`
  helper class's own field definition (constructor usage seen at 7 positional args; class body not opened).

## CORRECTIVE UPDATE (Session SMEPLUS-26-08-31-MIG-A-GRPA-SIP-CORR-003)

The `stock.rule.Procurement` "Unknown" above and REPL-10/11's `_run_buy`/selection-registration citations are now
**CLOSED** by a targeted corrective follow-up. Full findings live in the corrective closure report
(`19_TEAM_A_CORRECTIVE_CLOSURE_REPORT.md`); key facts folded in here per DELTA-FIRST (original REPL-01..15 rows
above are preserved unedited — this is additive):

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| BUY-01 | purchase_stock/models/stock_rule.py | L58–59 | `_run_buy(self, procurements)` confirmed as the real (only) method name — `Procurement` itself is a `typing.NamedTuple` with 8 positional fields: `product_id, product_qty, product_uom, location_id, name, origin, company_id, values` (closes the "class body not opened" unknown) |
| BUY-08/22 | stock_rule.py | L99, L358–390 | `_run_buy` searches for and **reuses an existing draft PO** matching a vendor/company/picking-type/currency domain (`_make_po_get_domain`) before creating a new one — consolidation aggressiveness is a **per-vendor setting** (`partner.group_rfq`), not hardcoded |
| BUY-09/21 | stock_rule.py | L104–115, L326–356 | New PO created `with_user(SUPERUSER_ID)`; field map includes `partner_id`, `user_id=partner.buyer_id.id` (buyer comes from the **vendor's** record, not the acting user), `picking_type_id`, `currency_id`, `date_order` (computed from lead time) |
| SEL-01 | purchase_stock/models/stock_rule.py | L18–20 | `action = fields.Selection(selection_add=[('buy', 'Buy')], ondelete={'buy': 'cascade'})` — confirmed verbatim, additive to the base 3-value Selection |
| MTO-03/08 | stock/models/stock_move.py | L1541, **L1580** | The exact MTO re-trigger call site, previously unresolved: `_action_confirm()` detects `procure_method=='make_to_order'` and calls `self.env['stock.rule'].run(procurement_requests, ...)` at line 1580, batched per-confirm-call. `_action_assign()` was checked and confirmed to NOT re-trigger (it only skips reservation on MTO moves) |
| MTO-10 | stock_move.py | L1700–1701 | `_prepare_procurement_values()` sets `move_dest_ids = self` for MTO moves — the exact linkage field connecting a chained replenishment move to the new PO line, backed at the DB level by `stock_move_created_purchase_line_rel` (junction table, `ON DELETE CASCADE`) |

**Net effect**: the full chain "Sales delivery → chained MTO move → `_action_confirm()` L1580 →
`stock.rule.run()` → `'buy'` rule matched → `_run_buy()` → draft-PO reuse-or-create → PO line with
`move_dest_ids` linking back to the original move" is now evidenced end-to-end with no remaining gap. Cross-ref:
this closes E2E Scenario 2's `_run_buy()` unknown in `05_INTEGRATED_E2E_LIFECYCLE_MAP.md` and Gap Register items
Critical #3, High #6, High #7 in `14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md`.

---

# 10 — PUT-AWAY (`stock.putaway.rule`)

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| PA-01 | product_strategy.py | L16–20 | `stock.putaway.rule` — lives in `product_strategy.py`, not a `stock_putaway.py` |
| PA-02 | product_strategy.py | L43–58 | Rule matches on `product_id` OR `category_id` OR `package_type_ids`, plus `storage_category_id` |
| PA-04 | stock_location.py | L297–376 | `_get_putaway_strategy()`: sorts candidate rules by specificity — package-type > product > exact-category > any-category |
| PA-06 | product_strategy.py | L69–79 | `sublocation`: `no`/`last_used`/`closest_location` — three distinct sub-strategies |

## Synthesis — Put-away

- **Business purpose**: determines the exact physical sub-location goods are stored in on arrival — decoupling
  "which zone" (picking-type default) from "which bin within that zone."
- **Source owner observation**: the specificity-ordering rule is a genuinely non-obvious priority scheme expressed
  only in a sort-lambda, not a named constant — any re-implementation must replicate it exactly.
- **GROUP A consumers**: not directly referenced from Sale/Purchase — purely Inventory-internal, triggered by any
  incoming move regardless of origin.
- **Database evidence**: `stock_putaway_rule` is the **one sub-concept in this whole domain with no unexplained
  extension columns** in the DDL.
- **Confidence**: High for the rule/priority algorithm. **Unknown**: `_check_access_putaway()`/`_check_can_be_used()`
  bodies (delegated, not opened).

---

# 11 — CROSS-CLUSTER DEPENDENCY NOTES (observations only)

1. A Return picking never generates its own backorder (`_should_ignore_backorders`) — it's either fully done or
   not validated.
2. The Return/Exchange wizard is a **second, independent caller** of the same procurement engine used by
   orderpoints — a Replenishment-layer change has a blast radius into the Return wizard too.
3. Put-away resolution cannot be evaluated without the Package cluster's `stock.package.type` already present
   (package-type is part of the specificity sort).
4. Every lot-tracking rule in this cluster is gated by a Phase-1-scope product-master field (`tracking`,
   `is_storable`) — not re-litigated here.

# 12 — CRITICAL FINDINGS CARRIED FORWARD TO LATER PHASES

1. **No DB CHECK constraints exist anywhere in this domain** (move, move-line, quant, picking beyond one unique
   constraint) — every business rule (non-negative quantity, lot/product match, done-immutability, one-orderpoint-
   per-product-location) is enforced in Python only. Direct-SQL migration paths bypass all of it.
2. **"Wide shared table" pattern recurs across every model in this phase**: `stock_move`, `stock_move_line`,
   `stock_picking`, `stock_lot`, `stock_package_type`, `stock_warehouse_orderpoint` all carry DB columns from
   other modules (`sale_stock`, `purchase_stock`, `mrp`, `repair`, `stock_account`, `helpdesk`, shipping
   connectors, `website_sale`) not declared in the `stock` module itself. A migration reading only `stock/models/`
   will systematically miss the columns carrying cross-module business linkage.
3. **Sale/Purchase asymmetry in move creation is confirmed at the mechanism level**: Purchase → `stock.move.create()`
   direct and synchronous; Sale → `stock.rule.run()` indirect, inside the pull/push procurement engine (not yet
   opened — required reading before Phase 3/4 finalize Sales/Purchase capability models).
4. **Backorder and Return are not separate models** — both are the same `stock.picking` self-referencing itself,
   distinguished only by which FK (`backorder_id` vs `return_id`) is set. Any target design must decide whether to
   preserve this collapsed representation or split them.
5. **Quantity semantics are state-dependent, not field-dependent**: `stock.move.quantity` means "reserved so far"
   pre-done and "actually moved" once done — this single fact must anchor the eventual Quantity Semantics Register
   (deliverable #9) rather than treating field names as fixed-meaning labels.
6. **Sale order confirmation is not gated by inventory availability** — availability display is advisory-only
   (compute fields, no blocking validation found). This is a material Fit-Gap candidate question: does SMEsPlus
   need a hard stock check at confirmation, or is advisory-only (as observed) the intended behavior?
7. **Replenishment→Purchase is a one-way reflective dependency**: core `stock` never references `purchase_stock`
   at compile time; `purchase_stock` registers itself into `stock`'s dispatch contract. This is the cleanest
   module-boundary evidence found in the whole GROUP A research so far and is worth preserving as a target
   architecture pattern candidate (not a decision made here — Team A does not design).
8. **Live vs. historical Package representation** (`stock.package` vs `stock.package.history`) — a naive migration
   of only the live table loses Done-picking snapshot semantics permanently.
9. **Return traceability primitive is `stock.move.origin_returned_move_id`**, a field on the move — not on the
   picking. Must be preserved for return-chain traceability in any target design.
10. **Unresolved from this phase, needed before the Quantity Semantics Register can be finalized**: `stock.rule`'s
    `Procurement` class body and `_get_rule()`; `stock_move.is_in`/`is_out` column semantics; `returned_move_ids`
    field definition; `produce_line_ids` (likely MRP). All EVIDENCE_MISSING, not guessed.
    **CORRECTIVE UPDATE (session CORR-003)**: the `Procurement` class body is now CLOSED (a `typing.NamedTuple`
    with 8 positional fields — see §09's corrective addendum, BUY-01) and the MTO re-trigger call site that
    depends on `_get_rule()`'s resolution is also CLOSED (`stock_move.py` L1580, see §09). `is_in`/`is_out`,
    `returned_move_ids`, and `produce_line_ids` remain open — out of scope for this corrective session's four
    clusters.
