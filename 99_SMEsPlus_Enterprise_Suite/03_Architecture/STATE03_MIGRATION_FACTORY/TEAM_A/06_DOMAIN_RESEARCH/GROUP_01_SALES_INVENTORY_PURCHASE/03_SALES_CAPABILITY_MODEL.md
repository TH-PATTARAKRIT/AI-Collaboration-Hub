> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Phase 3 of 10 — Sales Deep Research
> All source paths relative to `ACCOUNT/01 ACCOUNT/SOURCE CODE/02 OTHER/` unless stated otherwise. DB evidence from
> the same schema-only extraction used in Phases 1-2 (`schema_only.sql`).
> Prior evidence reused by ID, not re-derived: Phase 1 (`01_SHARED_MASTER_DEPENDENCY_MAP.md`) — PTY-13/14, PRC-16..21,
> TAX-13..15, PAY-11..14, CUR-13..15, SEQ-11..13, WH-20/22-24, CO-25..27, AN-13..16. Phase 2
> (`02_INVENTORY_CAPABILITY_MODEL.md`) — GRPA-01/04/05 (Sale creates stock.move indirectly via `stock.rule.run()`,
> advisory-only availability check), BO/RET sections (backorder/return as self-referential `stock.picking`).

# 03 — SALES CAPABILITY MODEL

## 00 — Scope & Method

Covers `sale.order`/`sale.order.line` lifecycle and header logic, the ordered/delivered/invoiced/to-invoice
quantity quadruple, and Sale-side exceptions (cancellation, return, stock-vs-service branching, partial delivery).
Deliberately does not re-derive shared-master or movement-layer facts already established in Phases 1-2 — those
are cited by ID.

## 01 — Rollup Index

| # | Concept | Key mechanism | Confidence |
|---|---|---|---|
| 1 | Order lifecycle | 4 states only (`draft/sent/sale/cancel`); confirmation is a near-empty gate (state + product presence only) | VERIFIED FACT |
| 2 | Locking | Independent boolean; freezes 8 named line fields, not a blanket write-block | VERIFIED FACT |
| 3 | Credit limit | Advisory warning only, never a confirmation gate (test-confirmed) | VERIFIED FACT |
| 4 | Two-level approval (`level1_user_id` etc.) | Real DB columns, **zero source code found anywhere** | EVIDENCE_MISSING — critical |
| 5 | Quantity quadruple | Ordered (input) / Delivered (dispatched compute) / Invoiced (backward-derived) / To-invoice (the one field that branches on `invoice_policy`) | VERIFIED FACT |
| 6 | Cancellation | Cancels not-yet-done pickings; done pickings explicitly spared | VERIFIED FACT |
| 7 | Return | **No Sale-side return feature exists** — closes Phase 2's open question | VERIFIED FACT |
| 8 | Stock vs. Service | Single literal `product_id.type == 'consu'`, repeated 5-7 times, never centralized | VERIFIED FACT |
| 9 | Partial delivery | Header-only persisted (`delivery_status`); line-level `qty_to_deliver` never stored | VERIFIED FACT |

---

# 02 — SALE ORDER LIFECYCLE / HEADER

Read in full: `sale/models/sale_order.py` (2299 lines). Targeted: `account_move.py`, `account_move_line.py`,
`res_partner.py` (credit-warning plumbing), `sale_stock/models/sale_order.py`, `sale/tests/test_credit_limit.py`.

## Evidence table

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| SO-01 | sale_order.py | L26–31 | `SALE_ORDER_STATE = [draft("Quotation"), sent("Quotation Sent"), sale("Sales Order"), cancel]` — exactly **4** states. No `'done'` state (superseded by the independent `locked` boolean) |
| SO-04 | sale_order.py | L77–81 | `locked` — Boolean, independent of `state`, not a state value |
| SO-05 | sale_order.py | L41–44 | `models.Constraint("CHECK((state='sale' AND date_order IS NOT NULL) OR state!='sale')")` — a **real DB CHECK**, confirmed in DDL |
| SO-08 | sale_order.py | L756–763 | `is_expired` = `state in (draft,sent)` and `validity_date` passed — **informational only**, does not block confirmation |
| SO-12 | sale_order.py | L245–249, 616–662 | Header `invoice_status`, `store=True`; non-`sale`-state orders forced to `'no'` |
| SO-13/14 | sale_order.py | L1164–1194, 1201–1214 | `action_confirm()` / `_confirmation_error_message()` — the **only** gate: state must be draft/sent; every non-display/non-downpayment line needs a `product_id`. **No credit check, no approval check, no expiration check.** |
| SO-15 | sale_order.py | L1216–1227 | `_prepare_confirmation_values()` returns exactly `{state:'sale', date_order:now()}` — the entire base-module mutation |
| SO-16 | sale_order.py | L1229–1233 | `_action_confirm()` base body is **empty** — the extension point `sale_stock` overrides for delivery creation |
| SO-17 | sale_order.py | L1196–1199 | `_should_be_locked()` — auto-locks on confirm **only if** `sale.group_auto_done_setting` is enabled; off by default |
| SO-18/19 | sale_order.py | L1056–1063, 1154–1162 | `action_draft()`: only from `cancel`/`sent` — a **confirmed** order cannot be reverted directly. `action_quotation_sent()`: only from `draft`, writes `state='sent'` and nothing else |
| SO-21/22 | sale_order.py | L1316–1331 | `action_lock/unlock()` — no side effects beyond the flag. `action_cancel()`: blocked entirely if `locked`; else cancels only **draft** invoices and sets `state='cancel'` |
| SO-23 | sale_order.py | L2257–2267 | `_is_readonly()` = `state=='cancel' or locked` — a helper predicate, not itself an enforcement point |
| SO-26/27 | sale_order_line.py | L1382–1410 | **What `locked` actually blocks**: line `write()` raises if a locked order's line changes any of exactly 8 fields: `product_id, name, price_unit, product_uom_id, product_uom_qty, tax_ids, analytic_distribution, discount` — a **field-level freeze**, not a blanket block |
| SO-28 | sale_order.py | L1038–1041 | `write()`: changing `pricelist_id` on a `state=='sale'` order raises `UserError` — the **only** header write-restriction tied to `state`; does not check `locked` |
| SO-29 | sale_order.py | L1030–1036 | Deletion blocked unless `state in (draft, cancel)` |
| SO-32/33 | sale_order.py L306–307, 783–794; account/models/account_move.py L1999–2029 | `partner_credit_warning` (non-stored Text) via shared `_build_credit_warning_message()` — computes `total_credit` vs `credit_limit`; **returns an empty string (no warning) or a plain banner — never raises, never gates** |
| SO-36 | sale/tests/test_credit_limit.py L74–99 | `test_warning_on_invoice_with_downpayment` — **direct proof**: an order at exactly the partner's credit limit confirms with **no exception** |
| SO-40/41/42 | addons_extra/product_brand_sale, addons_extra/smesplus_so_section_bydivision | whole files | Custom "Division" (brand) layer: `_create_invoices()` overridden to **split one confirmed order into multiple invoices grouped by `product.brand_id`** when `company.split_invoice` (default `True`); delivery `warehouse_id` can be redirected to a brand-specific warehouse when `company.split_delivery` (default `False`) |
| SO-43 | addons_extra/multi_level_approval/*.py | whole module | Generic "SMEsPlus Approval" framework exists — **verified by exhaustive grep to have ZERO references to `sale.order`** and zero occurrences of `level1_`/`level2_`. Not wired to Sale at all. |

## Database evidence — unaccounted `sale_order` columns

Full-tree search found **zero** Python source anywhere (including `addons_extra/`) for: `level1_user_id`,
`level2_user_id`, `level1_approved_by`, `level2_approved_by`, `level1_approved_date`, `level2_approved_date`,
`reject_reason`, `is_delivery_split`, `is_consolidate`, `store_type_id` (a differently-shaped, unrelated field of
the same name exists on `stock.warehouse`), `job_type_id`, `auto_gen_version`, `auto_gen_code`,
`parent_company_id`, and header-level `brand_id` (a *line-level* `brand_id` does exist and is sourced, SO-41 below
— the header column does not).

## Synthesis — Order Lifecycle

- **Business purpose**: one model/table serves both pre-sale quotation and confirmed commitment, distinguished
  only by `state`. The central question: at what instant does a quotation become binding, and what exactly
  changes.
- **What exactly becomes true on confirmation** (traced precisely, in call order): (1) gate = state + product
  presence only; (2) analytic-distribution validation runs (cross-ref AN-13..16); (3) **exactly two fields
  change**: `state→'sale'`, `date_order→now()`; (4) `_action_confirm()` — **empty in base `sale`**, all
  invoice/delivery creation is 100% delegated to extension modules (`sale_stock`, per Phase 2 GRPA-04/05); (5)
  auto-lock only if a feature flag is enabled (off by default); (6) optional confirmation email. **Confirmation by
  itself does nothing more than flip state, stamp a date, and conditionally lock — no invoice, no delivery.**
- **SENT is functionally an email-tracking flag** — no behavioral difference from `draft` found anywhere beyond
  enabling the "quotation was emailed" signal; `_confirmation_error_message()` treats draft/sent identically.
- **LOCKED, precisely**: independent of `state` (an order can be `state='sale', locked=False` — the default
  out-of-the-box result of confirming). Enforced in exactly 3 places: blocks `action_cancel()`; blocks 8 named
  line fields (SO-26/27); blocks expense re-invoicing (`account_move_line.py`). Generic header `write()` does
  **not** check `locked` at all — only `pricelist_id` is state-gated.
- **Credit/approval gate before confirmation: there is none in vanilla `sale`/`account` source.** Advisory banner
  only, test-confirmed (SO-36). This matches the same "soft warning, hard gate minimal" design philosophy Phase 2
  found for stock availability.
- **The one real unresolved gap, flagged prominently for governance**: a complete two-level manager-approval
  schema exists in the live DB (`level1_user_id`/`level2_user_id`/`level1_approved_by`/`level2_approved_by`/
  approval dates/`reject_reason`) with **zero corresponding source anywhere**, including the one module whose name
  suggests it should own this (`multi_level_approval`, confirmed unrelated by exhaustive grep). Two equally
  consistent explanations: a custom approval module wasn't included in this source export, or these are
  orphaned/legacy columns populated only via direct SQL/ETL outside the ORM. **This is the actual approval-gate
  candidate for this domain and cannot be verified, refuted, or characterized from source alone.**
- **Company/warehouse/branch context**: `company_id` required; `_check_order_line_company_id` (CO-27, re-confirmed
  here) prevents cross-inaccessible-branch product usage. The custom Division/brand layer (SO-40/41/42) means "one
  confirmed order" does **not** guarantee "one invoice" or "one delivery warehouse" — a genuine, sourced
  customization on top of the stock Odoo picture.
- **Confidence**: High throughout (full-file reads, test cross-checked). Low/UNKNOWN — explicitly, not guessed —
  for the 12 orphaned DB columns.

---

# 03 — SALE ORDER LINE: QUANTITY QUADRUPLE & BILLING ELIGIBILITY

Read in full: `sale/models/sale_order_line.py` (1819 lines), `sale_stock/models/sale_order_line.py` (458 lines).
Targeted: `sale_order.py` (`_create_invoices` chain), `product_template.py` (`invoice_policy`, cross-ref only).

## Evidence table

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| SOL-01 | sale_order_line.py | L127–131 | `product_uom_qty` ("ordered") — precomputed default, **plain user input**, never derived from anything else |
| SOL-03/04 | sale_order_line.py | L217–229, 871–885 | Base `qty_delivered_method`: `manual`/`analytic` only. Docstring: "sale_stock redefine the behavior for 'consu' type" |
| SOL-05/06 | sale_order_line.py | L230–235, 887–902 | `qty_delivered` — computed but **directly user-editable** (manual override supported); explicit method-chaining contract for overriding modules |
| SOL-07 | sale_order_line.py | L916–970 | `'analytic'` method: delivered qty = `SUM(account.analytic.line.unit_amount)` grouped by `so_line` (expense-driven) |
| SOL-08/09 | sale_order_line.py | L238–242, 972–1006 | `qty_invoiced` — **pure computed, not manually overridable**; derived backward from `account.move.line` via `invoice_lines`: `out_invoice`→add, `out_refund`→subtract, excludes cancelled moves |
| SOL-10 | sale_order_line.py | L243–246, 1008–1023 | `qty_invoiced_posted` (**not stored**) — same aggregation restricted to `state=='posted'` only; deliberately a **separate, non-interchangeable** computation from `qty_invoiced` |
| SOL-11/12 | sale_order_line.py | L247–251, 1035–1064 | `qty_to_invoice` — **the triad resolves here**: `invoice_policy=='order'` → `ordered − invoiced`; else (`'delivery'`) → `delivered − invoiced`. Comment: `invoice_policy` deliberately excluded from `@api.depends` "to avoid retroactively changing SO" |
| SOL-14/15 | sale_order_line.py | L262–271, 1066–1095 | `invoice_status` (line) — 4 values, evaluated in fixed priority: not-confirmed → `no`; downpayment settled → `invoiced`; `qty_to_invoice≠0` → `to invoice`; over-delivered on order-policy → `upselling`; caught up → `invoiced`; else `no` |
| SOL-17 | sale_order_line.py | L1488–1536 | `_prepare_invoice_line()`: the invoice line's `quantity` = **`qty_to_invoice` verbatim** — not `product_uom_qty`, not `qty_delivered` |
| SOL-19 | sale_order_line.py | L1433–1454 | Confirmed line with `invoice_lines` cannot be deleted — "Set the quantity to 0 instead" — preserves audit history |
| SOL-23/25/26 | sale_stock/sale_order_line.py | L15, 183–214 | `sale_stock` adds `'stock_move'` method: for non-expense `type=='consu'` lines, `qty_delivered = SUM(done outgoing) − SUM(done incoming/returns)` — **only `done` moves count** |
| SOL-27 | sale_stock/sale_order_line.py | L216–240 | Weight-tolerance override: forces `invoice_status='invoiced'` **even if `qty_delivered != product_uom_qty`** for consu/delivery-policy lines once all moves are done/cancel — "products sold by weight" |
| SOL-31 | sale_stock/sale_order_line.py | L416–421 | Hard guard (sale_stock only, absent from sale base): reducing `product_uom_qty` below `max(qty_delivered)` for `consu` lines raises `UserError` — "create a return in your inventory instead" |
| SOL-34/35 | sale/product_template.py | L35–47, 163–164 | `invoice_policy`: `order`/`delivery`, forced to `'order'` whenever `type=='consu'` — `'delivery'` is reachable by default logic only for non-consu (service) products |
| SOL-37/38/39 | sale_order.py | L616–662, 1497–1613 | Order-level `_compute_invoice_status` rolls up line statuses (with a discount-line carve-out); `_create_invoices()` → `_get_invoiceable_lines()` (filters `qty_to_invoice>0`) → `_prepare_invoice_line()` (SOL-17) |

## Database evidence

`sale_order_line`: `product_uom_qty`, `qty_delivered`, `qty_invoiced`, `qty_to_invoice`, `qty_delivered_method`,
`invoice_status` all **stored**. Confirmed **non-stored** (compute-only): `qty_invoiced_posted`, `qty_to_deliver`,
availability-forecast fields. Only 2 CHECK constraints exist, both about `display_type` shape — **no DB constraint
enforces `invoice_status` or `qty_delivered_method` domain values**; the entire billing state machine is
application-layer only. Additional unexplained columns (`is_service`, `project_id`, `task_id`, `fsm_lot_id`,
`planning_hours_*`, etc.) — EVIDENCE_MISSING on owning module (likely `sale_project`/`industry_fsm`/`sale_timesheet`,
not opened this pass).

## Synthesis — Quantity Quadruple

- **The four quantities, precisely (feeds the eventual Quantity Semantics Register directly)**:
  - **Ordered** (`product_uom_qty`) — pure user input.
  - **Delivered** (`qty_delivered`) — a *dispatched* computation: `'analytic'` (expense-driven), `'manual'`
    (services — stays whatever was last written), or `'stock_move'` (sums done moves, once `sale_stock` installed
    and product is `'consu'`). Not one formula — a per-line dispatch table, and the dispatch value itself is a
    stored, computed field.
  - **Invoiced** (`qty_invoiced`) — always derived **backward** from actual invoice lines, never a forward
    counter. Two non-interchangeable variants (`qty_invoiced` vs `qty_invoiced_posted`) answer different
    questions (any non-cancelled vs. posted-only) — a migration must pick one deliberately.
  - **To-invoice** (`qty_to_invoice`) — the **only** one of the four that branches on `invoice_policy`. This single
    `if/else` is the entire mechanism separating "bill on order" from "bill on delivery" businesses.
  - `invoice_status` is a classification over the other four plus `state`, not a fifth quantity; `sale_stock`
    layers one more exception (weight tolerance) on top.
- **Actor/maintainer/consumer**: Sales owns `product_uom_qty` and the compute chain. Accounting is a downstream
  consumer (`qty_to_invoice` feeds the invoice line's quantity verbatim, then is read back for `qty_invoiced`) — a
  round-trip dependency. Inventory (`sale_stock`) is a *conditional second owner*: it redefines how delivered
  quantity itself is computed for stock-tracked lines and adds a hard guard sale-base lacks.
- **Source-specific coupling (do not copy blindly)**: `qty_to_invoice`'s dependency list deliberately excludes
  `invoice_policy` (a documented staleness window, not a business rule); combo-line billability is gated by its
  children (non-local dependency); line-level and order-level `invoice_status` are two independently-maintained
  lists with identical values (a DRY gap, not a requirement).
- **Confidence**: High throughout (both files read in full).

---

# 04 — CANCELLATION

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| CANC-04 | sale_order.py | L1322–1326 | `action_cancel()` raises if `locked` — **locking blocks cancellation outright** |
| CANC-05 | sale_order.py | L1328–1331 | Base `_action_cancel()`: cancels only draft invoices + sets state — **zero stock interaction** in base `sale` |
| CANC-08 | sale_order.py | L1056–1063 | `action_draft()` — cancellation is **not a dead end**; can return to draft from `cancel`/`sent` |
| CANC-13/14 | sale_stock/sale_order.py | L252–267, 258 | Full override: cancels `picking_ids.filtered(state != 'done')` — **done pickings explicitly spared** |
| CANC-17 | sale_stock/tests/test_sale_stock.py | L396–423 | Test-confirmed: cancel→draft→re-confirm creates a **brand-new** picking; the original cancelled one is **retained**, never deleted or revived |

## Synthesis — Cancellation

- **Business purpose**: stop future fulfillment without destroying or reversing physically-completed work.
- **Source owner observation**: cancellation and locking are two independent gates sharing one readonly predicate
  (`_is_readonly`) but otherwise orthogonal — `locked` must be explicitly unlocked before `action_cancel()`
  proceeds; a locked-but-not-cancelled order and a cancelled order have different valid next actions.
- **GROUP A consumers**: `sale_stock._action_cancel()` is a genuine cross-module write path from Sale into
  Inventory (calls `stock.picking.action_cancel()` directly) — contradicts a naive assumption that cancellation
  never touches Inventory.
- **Confidence**: High, CANC-17 additionally test-confirmed. **Unknown**: `stock.picking.action_cancel()`'s own
  body (does it cascade to moves the same way Phase 2's MOV-31 "cannot cancel a done move" rule does?) — not
  opened this pass.

---

# 05 — RETURN (Sale-side — closes Phase 2 §06's open question)

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| SRET-02 | sale_stock/sale_order.py | L249–250 | `action_view_delivery()` — the **only** picking-related button on `sale.order`; generic "Delivery"/"Transfers" label, not "Return" |
| SRET-04/05/06 | sale_stock/wizard/*.py | whole files (14 + 24 lines) | Three surgical overrides that only **re-stamp `sale_id`/`sale_line_id`** onto whatever new picking/move Inventory's own return wizard creates — never change return logic itself |
| SRET-07 | sale_stock/sale_order_line.py | L416–420 | The **only** literal "return" mention reachable from a Sale write path: an error message redirecting the user to Inventory when trying to shrink an already-delivered line |
| SRET-08 (negative) | 4 files, full-file greps | — | No `action_return`, no reference to `stock.return.picking` as a target, no distinct button anywhere in Sale |

## Synthesis — Return

- **Direct answer, closing Phase 2's flag**: **there is no Sale-side "Return" button or feature at all.** A user
  initiates a return from **Inventory's** UI on a done delivery, not from the Sales order form. Sale's only
  participation is keeping the FK trail intact and one redirect error message.
- **GROUP A consumers**: any migration mapping that assumes a "Sales Return" object or a dedicated Sale→Return
  button is inventing UI/process that does not exist in this source tree — confirmed by full reads/greps, not
  sampling.
- **Confidence**: High — both wizard files read in full; negative claim backed by full-file greps across all four
  candidate files.

---

# 06 — STOCK-VS-SERVICE LINE BEHAVIOR

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| SVS-03 | sale_order_line.py | L871–885 | In base `sale` alone, service and non-expensed `consu` are treated **identically** (both `'manual'`) |
| SVS-06 | sale_stock/sale_order_line.py | L375–388 | **The master gate**: `product_id.type != 'consu'` → line never triggers `stock.rule.run()`, never gets a `stock.move`, period |
| SVS-07 | sale_stock/sale_order_line.py | L416–420 | The quantity-floor guard (SRET-07) applies **only** to `consu` lines — service lines can be freely reduced regardless of `qty_delivered` |
| SVS-08/09 | sale_stock/sale_order_line.py | L27, 54–65 | `is_storable` (a **second, distinct** product flag, not `type`) gates only the delivery-forecast UI widget |
| SVS-12 (negative) | 2 files, full-file greps | — | **Zero** literal `== 'service'` comparisons anywhere — every branch targets `'consu'` positively, service is always the implicit complement |

## Synthesis — Stock vs. Service

- **One master switch controls three independent behaviors**: delivered-qty method, whether a stock move is ever
  created, and whether the quantity-floor guard applies — all gated by `product_id.type == 'consu'`. A **second,
  separate** switch (`is_storable`) controls only UI widget visibility. These two are related but not proven to
  always agree (a `'consu'` product with `is_storable` off is not tested) — flagged EVIDENCE_MISSING.
- **Source-specific coupling**: the literal `'consu'` string recurs 5-7 separate times across two files rather
  than being centralized — any migration mapping must replicate every occurrence individually.
- **Confidence**: High for every positive claim; negative claim backed by full-file greps.

---

# 07 — PARTIAL DELIVERY

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| PDEL-01/02 | sale_stock/sale_order.py | L33–41, 90–103 | `delivery_status` (stored, header, 4-value: `pending/started/partial/full`) — algorithm based purely on picking states + whether any line has `qty_delivered` |
| PDEL-03/04 | sale_stock/sale_order_line.py | L24, 54–65 | `qty_to_deliver` (line, **compute-only, never stored**) = `product_uom_qty − qty_delivered` |
| PDEL-05 | sale_stock/sale_order.py | L83–88 | `effective_date` — earliest done-picking date to a customer location; a second, date-based, stored partial/first-delivery marker |

## Synthesis — Partial Delivery

- **Partial delivery is a header-only persisted concept.** `delivery_status` and `effective_date` are the only
  durable signals; nothing equivalent is stored on `sale_order_line` — `qty_to_deliver` is always a live
  recomputation, never a persisted status.
- **Source owner observation**: base `sale` has no equivalent concept at all — entirely a `sale_stock` construct,
  derived from `stock.picking`/`stock.move` state, never inventing its own progress tracking.
- **Confidence**: High. **Unknown**: over-delivery behavior on `qty_to_deliver`'s sign/clamping — not traced.

---

# 08 — CRITICAL FINDINGS CARRIED FORWARD TO LATER PHASES

1. **A complete two-level manager-approval DB schema exists for `sale.order` with zero corresponding source
   anywhere** — the single most significant open governance question in this domain. Cannot be verified, refuted,
   or characterized as live, dead, or externally-integrated from source alone. Carry to the Unknown/Conflict
   register and the Fit-Gap pack as a priority item.
2. **Credit-limit and inventory-availability checks share one design philosophy**: both are advisory-only warnings,
   never confirmation gates, confirmed by direct test evidence in both cases (Sale/Phase-3 for credit,
   Sale/Phase-2 for stock).
3. **Sale has no Return feature of its own** — returns are entirely an Inventory-initiated, Inventory-UI action;
   Sale only preserves FK linkage. Any target design assuming a "Sales Return" object must be told this is not
   how the source system works.
4. **Cancellation spares completed deliveries.** A cancelled SO can coexist indefinitely with a `done` picking —
   the source makes no attempt to reconcile or flag this beyond a quantity-decrease activity log.
5. **Re-confirming a cancelled-then-drafted order always creates a new picking**, never reuses or revives the old
   one — test-confirmed, a concrete target-parity decision point.
6. **The ordered/delivered/invoiced/to-invoice quadruple is the backbone of the eventual Quantity Semantics
   Register** — `qty_to_invoice`'s branch on `invoice_policy` is the *entire* mechanism distinguishing bill-on-
   order from bill-on-delivery business models; there is no other fork.
7. **`qty_invoiced` and `qty_invoiced_posted` are not interchangeable** — a migration must pick one deliberately
   as "the" invoiced quantity; the source treats them as answering different questions (draft-inclusive vs.
   posted-only).
8. **A custom "Division" (brand) layer can split one confirmed order into multiple invoices and redirect delivery
   warehouses** — a sourced customization meaning "one order → one invoice/delivery" is not a safe assumption even
   before line-level invoice_status logic is considered.
9. **The stock-vs-service gate (`product_id.type == 'consu'`) is never centralized** — repeated 5-7 times
   independently; some occurrences also require `is_expense`, `locked`, or `state` conditions, not `type` alone.
10. **Unresolved, needed before this cluster is closed for Fit-Gap purposes**: `stock.picking.action_cancel()`'s
    exact cascade behavior; owning module of `sale_order_line.is_service`; whether `product.type` can literally
    equal `'product'` (seen in one override, unexplained); `qty_to_deliver`'s over-delivery behavior. All
    EVIDENCE_MISSING, not guessed.
