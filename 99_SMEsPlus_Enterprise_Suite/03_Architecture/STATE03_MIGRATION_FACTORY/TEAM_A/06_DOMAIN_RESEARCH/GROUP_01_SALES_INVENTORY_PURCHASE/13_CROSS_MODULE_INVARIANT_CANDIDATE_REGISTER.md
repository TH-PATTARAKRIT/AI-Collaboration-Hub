> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Phase 9 of 10 — Cross-Module Invariant Candidate Register
> These are OBSERVED regularities in the source system, offered as candidates for Team B's independent
> consideration — Team A does not decide which, if any, should become enforced target-system invariants.

# 13 — CROSS-MODULE INVARIANT CANDIDATE REGISTER

## 00 — Method

An "invariant candidate" is a rule that appears to hold consistently across the source system's behavior (even if
not enforced by a database constraint). Each is tagged with its actual enforcement level, since governance §16
draws a hard line between "the database enforces this" and "the application merely usually does this."

## 01 — Invariants that ARE enforced (application-layer, confirmed by source)

| # | Candidate invariant | Enforcement level | Evidence |
|---|---|---|---|
| 1 | A `done` or `cancel` stock.move.line can never be deleted | ORM `@api.ondelete` guard | Phase 2 MOVL-15 |
| 2 | A `done` stock.move cannot be cancelled (must be returned instead) | ORM method guard, raises UserError | Phase 2 MOV-31 |
| 3 | Only a fully `done` stock.picking can be the source of a return | ORM method guard (`_can_return()`) | Phase 2 RET-02 |
| 4 | A confirmed Sale/Purchase order line with existing invoice/bill lines cannot be deleted — must be zeroed instead | ORM `@api.ondelete` guard, symmetric on both models | Sales SOL-19; Purchase POL-16 |
| 5 | A locked Sale order cannot have 8 named commercial fields edited on its lines | ORM `write()` override | Sales SO-26/27 |
| 6 | A branch (child `res.company`) cannot have a different operating currency than its root company | ORM `@api.constrains` | Phase 1 CO-12 |
| 7 | A UoM's conversion ratio (`relative_factor`/`relative_uom_id`) becomes immutable once any non-cancel/non-done stock.move or nonzero stock.quant references it | ORM `write()` override | Phase 1 UOM-11 |
| 8 | A confirmed order's `pricelist_id` cannot change (Sale only) | ORM `write()` override | Sales SO-28 |
| 9 | A Purchase order cannot be cancelled while `locked`, or while it has a non-cancel/non-draft vendor bill | ORM method guard | Purchase PO-10 |
| 10 | Purchase's amount-threshold approval gate: a non-manager cannot self-approve above the configured amount | ORM method guard, test-confirmed | Purchase PO-06/08 |

## 02 — Invariants that are NOT enforced anywhere (source-confirmed absence — a genuine finding, not a gap)

| # | Candidate invariant that does NOT hold | Confirmed absence | Evidence | Risk if assumed |
|---|---|---|---|---|
| 1 | "Delivered/received quantity never exceeds ordered quantity" | Over-delivery/over-receipt are never specially detected or blocked on either Sale or Purchase lines | Purchase POL-24 synthesis (Purchase side); no equivalent Sale-side guard found either | A migration assuming this invariant holds would mishandle real over-fulfillment data |
| 2 | "Stock quantities never go negative" | No DB CHECK constraint anywhere on `stock_quant`; negative-stock prevention is 100% application-layer, bypassable via `allow_negative=True` or direct SQL | Phase 2 NEG-05 | A direct-SQL migration path could silently introduce negative stock with zero system objection |
| 3 | "One row per (product, location, lot, package, owner) in stock.quant" | No unique/composite DB index enforces this — it's an application convention reconciled AFTER THE FACT by `_merge_quants()`, which exists specifically because concurrent writers can violate it | Phase 2 AVL-QNT-08, DB-03 | Any bulk-load migration approach must independently dedupe, since the source database itself does not guarantee uniqueness |
| 4 | "A sale/purchase order's state field only holds one of its declared Selection values" | No DB CHECK/ENUM on `state` on either `sale_order`, `purchase_order`, `stock_move`, or `stock_picking` — pure `character varying` | Sales/Purchase/Phase 2, recurring finding | A direct-SQL write could introduce an invalid state string with zero database-level rejection |
| 5 | "A confirmed order is gated by available stock/credit" | Both Sale's credit warning and inventory-availability display are advisory-only; confirmed by test evidence for credit (Sales SO-36) and by absence-of-guard for stock (Phase 2 GRPA finding) | Sales SO-32/33/36 | A target design assuming a hard stock/credit gate exists in the source would be designing against a feature that isn't actually there |
| 6 | "qty_invoiced never exceeds product_uom_qty/product_qty" | No DB constraint ties any of the quantity fields together on either `sale_order_line` or `purchase_order_line` | Sales/Purchase DB evidence sections | Same risk pattern as #1 |

## 03 — Structural symmetries observed (candidates worth preserving as design patterns, not business rules)

| # | Symmetry | Evidence |
|---|---|---|
| 1 | Sale and Purchase both dispatch their "delivered"/"received" quantity computation through a per-line method-selector field that is itself a stored compute — never a single formula | Sales SOL-03/04; Purchase POL-03/11 |
| 2 | Sale and Purchase both branch billing eligibility on a single product-level policy field (`invoice_policy` / `purchase_method`) with the identical two-value shape (order-based vs. fulfillment-based) | Sales SOL-12/34; Purchase POL-07/08 |
| 3 | Sale and Purchase both have NO dedicated Return feature — both defer 100% to the same generic Inventory wizard | Sales §05; Purchase §07 (POL-29/30) |
| 4 | Sale and Purchase both call the identical `res.company._accessible_branches()` API in an identically-named/-shaped `_check_order_line_company_id()` constraint | Phase 1 CO-27/29 |
| 5 | Sale and Purchase both use the `analytic.mixin` inheritance pattern identically on their order lines | Phase 1 AN-13/17 |

## 04 — Structural asymmetries observed (candidates a target design must deliberately choose, not silently normalize)

| # | Asymmetry | Evidence |
|---|---|---|
| 1 | Purchase has a real, working, test-confirmed hard approval gate; Sale's equivalent (credit limit) is advisory-only | Purchase PO-06/08; Sales SO-32/33/36 |
| 2 | Purchase creates `stock.move` directly/synchronously; Sale creates it indirectly via the `stock.rule` procurement engine | Phase 2 GRPA-01/02 vs GRPA-04/05 |
| 3 | Sale has no pricelist-equivalent gap — Purchase has NO pricelist at all, using `product.supplierinfo` instead | Phase 1 PRC-22..25 |
| 4 | Sale's sequence fallback (no matching `ir.sequence`) is the literal string `"New"`; Purchase's is `"/"` — an inconsistency, not a business rule | Phase 1 SEQ-12/15 |
| 5 | Sale's `_is_readonly()` includes `locked`; Purchase's does not | Purchase PO-13 vs Sales SO-23 |
| 6 | Sale's `action_draft()` restricts which prior states can return to draft; Purchase's `button_draft()` has no precondition at all | Purchase PO-09 vs Sales SO-18 |
| 7 | Sale's deletion allows `draft` OR `cancel`; Purchase's requires `cancel` exactly | Purchase PO-12/36 vs Sales SO-29 |
| 8 | ~~Purchase's post-confirmation cancellation cascade into `stock.picking` was never confirmed to exist~~ **CLOSED (CORR-003)**: it exists, is state-partitioned by receipt scenario, and is provably symmetric-in-effect with Sale's (both spare `done` pickings, both fully cancel not-done ones) even though derived independently and not merely assumed | Purchase §04 corrective update |

## CORRECTIVE UPDATE (Session SMEPLUS-26-08-31-MIG-A-GRPA-SIP-CORR-003)

Two new invariant candidates, confirmed by row-level dump forensics (not source code) — added here as a distinct
category since their evidence type differs from everything else in this register:

| # | Candidate invariant | Enforcement level | Evidence |
|---|---|---|---|
| 1 | A `stock.move` cancellation guard is evaluated over the **whole recordset** passed to `_action_cancel()`, not per-move — one `done` move anywhere in a batch blocks the entire batch | ORM method guard, precision-corrected from the original MOV-31 summary | `02_INVENTORY_CAPABILITY_MODEL.md` MOV-31 corrective note, POCANC-13 |
| 2 | A `stock.picking` can never hold a mix of `done` and still-pending moves at the moment of cancellation — Odoo's own backorder mechanics guarantee any partial-completion state is always already split across two picking records before cancellation logic ever runs | Structural (a consequence of `_create_backorder`/`_action_done`'s own design), not an explicit constraint | `04_PURCHASE_CAPABILITY_MODEL.md` §04 corrective update, POCANC-18..20 |

## 05 — Governing note for Team B

None of the above is a recommendation. Section 01 items are candidates for "this rule already works and could be
preserved." Section 02 items are candidates for "this rule does NOT exist today — decide deliberately whether the
target system should add it, rather than assuming the source enforces something it doesn't." Section 03/04 are
observations about consistency (or its absence) between the two commercial modules that a target design should
resolve explicitly rather than inherit by accident.
