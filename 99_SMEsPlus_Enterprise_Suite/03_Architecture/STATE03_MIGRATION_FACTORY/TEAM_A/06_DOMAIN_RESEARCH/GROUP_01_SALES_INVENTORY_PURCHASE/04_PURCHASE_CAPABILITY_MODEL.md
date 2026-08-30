> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Phase 4 of 10 — Purchase Deep Research
> All source paths relative to `ACCOUNT/01 ACCOUNT/SOURCE CODE/` unless stated otherwise. DB evidence from the same
> schema-only extraction used in Phases 1-3 (`schema_only.sql`).
> Prior evidence reused by ID, not re-derived: Phase 1 — PRC-22..25 (no Purchase pricelist), TAX-16..19, PAY-15..17,
> CUR-16..20, SEQ-14..16, WH-25..26, CO-28..29, AN-17..19. Phase 2 — GRPA-01/02 (Purchase creates `stock.move`
> directly/synchronously), REPL-10/11 (`purchase_stock` supplies `'buy'` + `_run_buy`), BO/RET sections (backorder/
> return as self-referential `stock.picking`). Phase 3 — SO-43 and the orphaned two-level approval schema first
> found on `sale_order` (§08 item 1 of `03_SALES_CAPABILITY_MODEL.md`) — this phase confirms it is cross-model.

# 04 — PURCHASE CAPABILITY MODEL

## 00 — Scope & Method

Covers `purchase.order`/`purchase.order.line` lifecycle, the real (and the suspected-but-unconfirmed) approval
mechanisms, the demand-signal layer upstream of a PO (`purchase.request`, `purchase.requisition`), and receipt/
quantity/exception mechanics (return-to-vendor, backorder-equivalent, dropship). A major cross-cutting finding —
an orphaned two-level manager-approval DB schema spanning three models — is investigated in depth in §03 and is
the single most significant open governance item in GROUP A research so far.

## 01 — Rollup Index

| # | Concept | Key mechanism | Confidence |
|---|---|---|---|
| 1 | PO lifecycle | 5 states (`draft/sent/to approve/purchase/cancel`) — one more than Sale's 4 | VERIFIED FACT |
| 2 | Confirmation | `button_confirm()` dispatches to `state='purchase'` **or** `'to approve'` depending on `_approval_allowed()` | VERIFIED FACT |
| 3 | Real approval gate | Amount-threshold + manager-group (`po_double_validation`) — genuine, test-confirmed hard gate | VERIFIED FACT |
| 4 | Orphaned two-level approval schema | Identical (minus 1 column) `level1_*`/`level2_*`/`reject_reason` sets on `sale_order`, `purchase_order`, `purchase_request` — **zero source anywhere on any of the three models** | EVIDENCE_MISSING — critical, cross-model |
| 5 | `multi_level_approval_configuration` | Generic, data-driven approval engine; **exactly one real wiring point**: `purchase.request` (not `purchase.order`, not `purchase.requisition`); its own storage tables don't exist in the DB — never installed | EVIDENCE_MISSING — critical |
| 6 | Purchase Request (demand signal) | `purchase.request` upstream of PO; converts via a wizard hard-gated on `state=='approved'` | VERIFIED FACT |
| 7 | Purchase Requisition | Native "Purchase Agreements" — blanket order / template only, **not** a tender type despite the manifest's claim | VERIFIED FACT |
| 8 | Multi-vendor tendering | Lives on `purchase.order` itself (`alternative_po_ids`/`purchase.order.group`), independent of `purchase.requisition` | VERIFIED FACT |
| 9 | Received quantity | Dispatched by `qty_received_method`: `'manual'` (typed) or `'stock_moves'` (sum of done moves, return/dropship-netted) | VERIFIED FACT |
| 10 | Billing gate | `product.purchase_method` (`'purchase'`=on ordered, `'receive'`=on received) — the AP-side equivalent of Sale's `invoice_policy` | VERIFIED FACT |
| 11 | Return-to-vendor | **No dedicated Purchase feature** — a pure location-usage predicate on an ordinary `stock.move` | VERIFIED FACT |
| 12 | Backorder (Purchase side) | **Never referenced by name or field** — remaining supply tracked implicitly via not-done moves | VERIFIED FACT |
| 13 | Dropship | One-line destination substitution on the same move-creation call, gated on `picking_type_id.code=='dropship'` | VERIFIED FACT |

---

# 02 — PO LIFECYCLE, CONFIRMATION, REAL APPROVAL GATE

Read in full: `purchase/models/purchase_order.py` (1416 lines). Targeted full reads: `res_company.py`,
`res_config_settings.py`, `purchase/tests/test_access_rights.py`, `purchase_request/models/purchase_order.py`.

## Evidence table

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| PO-01 | purchase_order.py | L105–111 | `state`: `draft`("RFQ") / `sent`("RFQ Sent") / `to approve` / `purchase`("Purchase Order") / `cancel` — **5 values**. RFQ and PO are the same model/table, distinguished only by `state`, same pattern as Sale |
| PO-02 | purchase_order.py | L112–117 | `locked` — independent Boolean, same shape as Sale's |
| PO-04 | purchase_order.py | L625–639 | `button_confirm()` — the whole dispatcher: gate via `_confirmation_error_message()`; validates analytic distribution; `_add_supplier_to_product()` (writes the vendor into `product.supplierinfo` if new — the write path populating the table Purchase uses instead of a pricelist); **then branches**: `_approval_allowed()` True → `button_approve()` (`state='purchase'`); False → `state='to approve'` |
| PO-05 | purchase_order.py | L657–668 | `_confirmation_error_message()` — the **only** structural gate: every real line needs a `product_id`. No credit/budget/vendor-status check — structurally identical in spirit to Sale's finding |
| PO-06 | purchase_order.py | L1249–1258 | `_approval_allowed()` — **the real, sourced gate**: True if `po_double_validation=='one_step'`, OR (`'two_step'` AND `amount_total < po_double_validation_amount`, currency-converted), OR user has `purchase.group_purchase_manager` |
| PO-07 | purchase_order.py | L615–619 | `button_approve()` — silently **drops** (no error) any order failing the gate; survivors get `state='purchase'`, `date_approve=now()`, conditional lock |
| PO-08 | purchase/tests/test_access_rights.py | L102–127 | `test_double_validation` — **test-confirmed**: non-manager confirms into `'to approve'`; that same non-manager's `button_approve()` is a **silent no-op**; after granting the manager group, it succeeds |
| PO-09 | purchase_order.py | L621–623 | `button_draft()` — **no precondition at all**; any state can be forced back to draft by direct call (contrast Sale's `action_draft()`, which restricts source states) |
| PO-10 | purchase_order.py | L641–649 | `button_cancel()` — two hard gates: `locked` blocks the whole batch; any non-cancel/non-draft vendor bill also blocks the whole batch |
| PO-12 | purchase_order.py | L408–412 | Deletion requires `state=='cancel'` **exactly** — stricter than Sale (which also allows `draft`) |
| PO-13 | purchase_order.py | L1378–1386 | `_is_readonly()` = `state=='cancel'` only — **does not check `locked`**, a real divergence from Sale's `_is_readonly()` |
| PO-14/15 | res_company.py, res_config_settings.py | L10–23, 10–44 | `po_lock` (edit/lock), `po_double_validation` (one_step/two_step, default one_step), `po_double_validation_amount` (default 5000) — genuinely user-configurable |
| PO-17 | purchase_order.py | L479–483, 611–613 | `sent` reached only as a side effect of emailing or printing the RFQ — mirrors Sale's "SENT is an email-tracking flag" finding |
| PO-18 | purchase_order.py | L835–917 | `action_merge()` — RFQ-only; merges into the oldest, cancels the losers through the same `button_cancel()` gate; `_merge_alternative_po()` is a **no-op stub** in base `purchase` (actual grouping supplied by `purchase_requisition`, §06) |
| PO-20 | purchase_request/models/purchase_order.py | L80–84 | `button_confirm()` override posts a traceability message back onto the originating `purchase.request` — **adds no gating logic**, pure cross-document notification |

## Synthesis — Lifecycle, Confirmation, Real Approval Gate

- **Business purpose**: same one-model-two-phases pattern as `sale.order`, but Purchase adds a genuine **third**
  phase, `'to approve'`, that Sale's 4-state machine has no equivalent of.
- **What exactly becomes true on confirmation**: gate = product presence only; analytic validated; vendor
  opportunistically registered into `product.supplierinfo`; **then branches** on the amount-threshold gate into
  either a fully committed PO or a pending-approval state.
- **Is there a real, sourced approval gate for Purchase, unlike Sale? Yes — for the amount-threshold case.**
  `_approval_allowed()` is a genuine, test-confirmed hard gate — structurally the polar opposite of Sale's
  advisory-only credit check. **But it is a single binary threshold check, not a two-level approval chain** — no
  concept of "level 1 approver"/"level 2 approver" as distinct assigned people, no sequencing, no per-order
  approver assignment. The orphaned `level1_user_id`/`level2_user_id` columns (§03) describe a categorically
  different, more elaborate mechanism than the one actually implemented here.
- **Company/warehouse/branch context**: gate evaluated per `company_id` with currency conversion — multi-company/
  multi-currency-aware, consistent with Phase 1's CUR-16..20.
- **Confidence**: High throughout; PO-08 additionally test-confirmed.

---

# 03 — THE ORPHANED TWO-LEVEL APPROVAL SCHEMA (cross-model investigation)

This is the single most significant open governance question surfaced across GROUP A research so far. It spans
three models and two research phases.

## What's confirmed

| ID | Evidence | What it evidences |
|---|---|---|
| PO-21/DBX-02 | `purchase_order` DDL | Carries `x_review_result`, `x_has_request_approval`, `level1_user_id`, `level2_user_id`, `level1_approved_by`, `level2_approved_by`, `reject_reason`, `level1_approved_date`, `level2_approved_date` — same set found on `sale_order` (Phase 3), plus two `x_`-prefixed fields |
| DBX-01 | `purchase_request` DDL | Same set **minus `level2_user_id`** |
| DBX-03 | `purchase_requisition` DDL | **None** of these columns — the schema touches only `purchase.request` and `purchase.order`, not `purchase.requisition` |
| PO-22/DBX-05 | Full-tree grep, all of `01 ACCOUNT`/`02 OTHER`/`addons_extra` | **Zero files** declare any of `level1_user_id`/`level2_user_id`/`level1_approved_by`/`level2_approved_by`/`reject_reason` on any of the three models |
| PO-23/DBX-04 | `purchase_order_level_reject` and `purchase_request_level_reject` tables | Two parallel orphaned reject-audit-log tables (`order_id`/`request_id`, `current_state`, `mode`, `reason`) — zero source anywhere |
| PO-27 | `multi_level_approval_configuration/__manifest__.py` | Named "SMEsPlus Approval All in One"; description names "Sale Order, Purchase Order, MRP Order" explicitly; **`'active': False`** in the manifest itself |
| PO-28/APPR-05/06 | Exhaustive grep, all 3 `multi_level_approval*` module trees | **Zero code or data hits** referencing `purchase.order`, `purchase.requisition`, or `sale.order` anywhere |
| APPR-07/08/09 | `multi_level_approval_configuration` | The **one real wiring point**: hard manifest dependency on `purchase_request`; Python override of `purchase.request.button_rejected()`/`button_draft()`; a view change **removing** the native approve/reject buttons |
| APPR-10/11 | `models/base_model.py`, `models/multi_approval_type.py` | The engine is architecturally generic: `write()` on **every model** routes through a configurable check; an admin can point a `multi.approval.type` at *any* `ir.model` at runtime via `action_configure()`, which dynamically creates exactly `x_review_result`/`x_has_request_approval`/`x_need_approval` on the target model |
| APPR-12 | `multi_approval_type.py` L669–697 | `check_rule()`'s actual block-the-write branch is **commented out** — as shipped, even where wired, this "hard lock" never actually raises |
| PO-31/APPR (DB check) | `schema_only.sql`, full grep for `multi_approval*` tables | **Neither `multi_approval` nor `multi_approval_type` exists in the live database at all** — the entire engine has never been installed in the DB that produced this dump |
| PO-32 | `multi_level_approval_configuration/models/purchase_request.py` | Its one functional code path references `x_need_approval`, a field that **does not exist** in the live `purchase_request` schema — independent confirmation the code is not currently executable |
| DBX-06 | `02 OTHER/web_studio*` | Odoo Studio (no-code customization) is present in this stack — a plausible, unconfirmed origin for schema-only changes with no `.py`/`.xml` trace |

## Synthesis

- **The schema is confirmed cross-model**: `sale_order` (Phase 3), `purchase_order`, and `purchase_request` all
  carry a near-identical "level 1 / level 2 approver, approved-by, approved-date, single shared reject reason"
  column set, and in **all three cases zero Python source anywhere declares them.** This is far more consistent
  with a single external schema-migration or Odoo-Studio-customization pass applied uniformly across multiple
  business documents than with three independent coincidental accidents — but this remains **not provable from
  source alone.**
- **The module whose name and manifest most directly promise this feature cannot be its origin.** Its own
  supporting tables don't exist in the DB — meaning it has never been installed by ordinary Odoo mechanics, and
  could not have retroactively added unrelated columns to three other models even if it had been.
- **A partial, more defensible clue exists and should not be conflated with the fuller mystery**: `x_review_result`
  and `x_has_request_approval` are the *exact* field names `action_configure()` would create on any model an admin
  points the generic engine at — circumstantial evidence that `purchase.order` (and `purchase.request`) may have
  been configured as target models for that engine at the data level (not visible in source, since configuration
  is admin/data-driven, not code). But the `level1_*`/`level2_*`/`reject_reason` fields and the `*_level_reject`
  tables **do not match this module's naming pattern or its dynamic-field set at all** (`action_configure` never
  creates `level1_*`/`level2_*`) and have **no explanation anywhere in the read source**. These may be two
  genuinely separate customization efforts layered on the same models, not one.
- **Definitive answer to "does any approval module wire into any Purchase-side model?": yes, exactly one point** —
  `multi_level_approval_configuration` → `purchase.request` only (button overrides + view change), never
  `purchase.order` or `purchase.requisition` in source. Whether it was ever additionally *data-configured* against
  `purchase.order` is a runtime/data-level fact this schema-only dump (0 `COPY` statements) cannot answer.
- **Do not conflate this with Purchase's real approval gate** (§02) — `_approval_allowed()` is a single amount-
  threshold check with no per-order approver assignment; the orphaned schema describes a materially different,
  more elaborate two-person sequential mechanism that is not what's actually implemented anywhere in source.
- **Confidence**: High for all existence/absence claims (direct DDL reads, exhaustive greps). The *origin and
  operational status* of the orphaned columns is UNKNOWN/EVIDENCE_MISSING and requires row-level data
  (`ir_model_fields`/`ir_model_data` filtered to these three models) to resolve — recommended as a follow-up data
  pull before any target design decision assumes either approval path is safe to ignore or safe to carry forward.

---

# 04 — CANCELLATION

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| PO-35 | purchase_order.py | L641–649 | `button_cancel()` — dual gate: `locked` OR any non-cancel/non-draft vendor bill blocks the whole batch |
| PO-36 | purchase_order.py | L408–412 | Deletion requires `state=='cancel'` exactly (Sale allows `draft` too) |
| PO-37 | purchase_order.py | L621–623 | `button_draft()` has no state precondition — whether reachable by an end user depends on view-level button visibility, not verified this pass |

## Synthesis — Cancellation

- **Business purpose**: same as Sale — stop a commitment without destroying already-completed work — but
  Purchase's gate is **stricter and dual**: both `locked` and an outstanding vendor bill independently block
  cancellation (Sale only checks `locked`).
- **Source owner observation**: base `purchase`'s `button_cancel()` is a pure `write()` with zero direct
  `stock.picking`/`stock.move` interaction — consistent with Purchase's synchronous/direct move-creation pattern
  (Phase 2 GRPA-01/02) not implying a symmetric cancellation cascade.
- **Confidence**: High. **Unknown**: whether `purchase_stock` overrides `button_cancel()` to cascade into receipts
  — not opened this pass.

---

# 05 — PURCHASE REQUEST (demand signal, upstream of PO)

Read: `addons_extra/purchase_request/` (ForgeFlow/OCA, LGPL-3) — models, wizard, security — in full.

## Evidence table

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| PREQ-01 | `__manifest__.py` | L1–31 | ForgeFlow/OCA "Purchase Request", `depends: [purchase, product, purchase_stock, hr, smesplus_uom_ext, project]` — a customized OCA import, not from-scratch SMEsPlus |
| PREQ-02 | models/purchase_request.py | L8–14 | State: `draft → to_approve → approved / rejected` |
| PREQ-04 | models/purchase_request.py | L94 | `assigned_to` (Approver) = `related="requested_by.employee_ids.pr_approver"` — approver derived from a per-employee field |
| PREQ-07/08 | models/purchase_request.py | L312–345 | `button_approved` requires `assigned_to==env.uid`; `button_rejected` opens a reason wizard. **Both carry the code comment**: "No need this code if we use multi_level_approval related modules" |
| PREQ-13 | wizard/purchase_request_line_make_purchase_order.py | L44–73 | **Hard gate**: conversion to PO blocked (`UserError`) unless `request_id.state=='approved'` |
| PREQ-14/15 | same file | L231–314, 151–158 | **The exact conversion mechanism**: reuses an existing draft PO/line or creates new `purchase.order`+`purchase.order.line`; writes a `purchase.request.allocation` bridge row carrying the allocated quantity |
| PREQ-19/20/21 | models/stock_rule.py, product_template.py, orderpoint.py | multiple | Reordering-rule "buy" action routes into a `purchase.request` (not a plain RFQ) when the product's `purchase_request` boolean is set; open PR-line quantities feed the orderpoint's "already incoming" calculation |
| PREQ-23/24/25 | security/purchase_request.xml | L7–64 | Two groups (`user`/`manager`); multi-company `ir.rule`; plain users see only their own requests |

## Synthesis — Purchase Request

- **Business purpose**: internal demand signal — "someone inside the company needs N of X by date Y" — captured
  *before* any vendor is chosen; explicitly upstream of RFQ/PO.
- **Actor/maintainer/consumer**: requesting employee + their designated approver (HR-derived); Purchasing team
  converts approved lines to RFQ via the wizard; consumed downstream by `purchase.order` and upstream by
  `stock.warehouse.orderpoint`.
- **Source owner observation**: unmodified-in-spirit OCA code with SMEsPlus extensions layered on (Thai-language
  urgency levels, project linkage). The module's own author left explicit comments signaling its native
  approve/reject buttons are meant to be **superseded** by an external approval engine — this is the module-level
  intent that `multi_level_approval_configuration` (§03) partially, but not fully, fulfills.
- **GROUP A consumers — exact conversion to `purchase.order`**: only through the wizard, hard-gated on
  `state=='approved'`. No automatic conversion. The PR line's `purchase_state` afterward is a **read model**
  mirroring the PO line's lifecycle — not a separate state machine driving the PO.
- **Source-specific coupling / anomaly**: `purchase_request` carries the same orphaned approval-column family as
  `purchase_order` (§03) — flagged there, not duplicated here.
- **Confidence**: High for the module's own mechanics. Low/Unknown for the orphaned columns (§03).

---

# 06 — PURCHASE REQUISITION & MULTI-VENDOR TENDERING

Read: `02 OTHER/purchase_requisition/` and `purchase_requisition_stock/` (native Odoo 19 "Purchase Agreements",
unmodified core) — in full/near-full.

## Evidence table

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| PREQS-02 | models/purchase_requisition.py | L21–23 | `requisition_type`: **only** `blanket_order` / `purchase_template` — **no explicit tender type**, despite the manifest's "calls for tenders" description |
| PREQS-05 | models/purchase_requisition.py | L128–139 | Confirming a blanket order writes a `product.supplierinfo` record — it does **not** itself create a PO |
| PREQS-08/09 | models/purchase.py | L26–34, 36–93 | `purchase.order` inherited: `requisition_id`, `purchase_group_id`, `alternative_po_ids`. `_onchange_requisition_id` is the **actual** agreement→PO mechanism — auto-copies partner/currency/terms and (for template type) lines onto a draft PO |
| PREQS-10 | models/purchase.py | L95–110 | **The actual tendering gate**: confirming a PO with open `alternative_po_ids` intercepts confirmation with a warning wizard asking whether to keep or cancel the losing alternative RFQs |
| PREQS-12 | models/purchase.py | L162–234 | `action_create_alternative()` spins a sibling PO to a different vendor; `get_tender_best_lines()` computes best-price/date **across the whole alternative-PO group** — the actual vendor-comparison logic. A human clicks "Choose," not an automated rule |
| PREQS-16/17 | purchase_requisition_stock | L7–30 | Adds `warehouse_id`/`picking_type_id` onto `purchase.requisition` — without this auto-installing module, requisitions have no warehouse scoping at all |

## Synthesis — Requisition & Tendering

- **Manifest-vs-code conflict, confirmed**: `purchase.requisition` in this Odoo 19 source is a **standing
  agreement** (blanket order or reusable template), **not** a live multi-vendor tender document. The actual
  multi-vendor RFQ/tendering concept — competing offers, pick a winner — is implemented as a **separate,
  requisition-independent** mechanism living directly on `purchase.order` (`alternative_po_ids`/
  `purchase.order.group`). A set of competing RFQs to different vendors does not require a `purchase.requisition`
  record to exist at all. **Anyone scoping "purchase.requisition = the RFQ/tendering table" for a target design
  should be corrected.**
- **Two distinct, non-wizard conversion mechanisms**, both onchange-driven: (1) Agreement→PO: set `requisition_id`
  on a draft PO, `_onchange_requisition_id` populates it — no dedicated convert button. (2) Tender→PO:
  `action_create_alternative()` creates sibling POs; confirming the winner cancels the losers via a warning wizard.
- **Source owner observation**: straight, unmodified Odoo 19 core (no SMEsPlus customization found) — a genuine
  contrast with the demand-signal layer (§05), which is a customized OCA import.
- **Confidence**: High throughout, all read directly and DDL cross-checked.

---

# 07 — PO LINE QUANTITIES & RECEIPT

Read in full: `purchase/models/purchase_order_line.py` (751 lines), `purchase_stock/models/purchase_order_line.py`
(429 lines), `purchase_stock/models/stock_move.py` (249 lines).

## Evidence table

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| POL-01/04/05 | purchase_order_line.py | L23, 65–66 | `product_qty` (ordered, required input) vs `qty_received` (stored compute + manual escape hatch `qty_received_manual`) |
| POL-03/18/20 | purchase_order_line.py + purchase_stock override | L61–64; L25–26, 37–41 | Base declares only `qty_received_method='manual'`; `purchase_stock` bolts on `'stock_moves'`, auto-selected for `type=='consu'` lines once installed |
| POL-06/07 | purchase_order_line.py | L59, 67–68, 164–177 | `qty_invoiced`/`qty_to_invoice` computed together; `qty_to_invoice` **branches on `product.purchase_method`**: `'purchase'` → `product_qty − qty_invoiced` (bill on ordered); else → `qty_received − qty_invoiced` (bill on received) |
| POL-08 | purchase/models/product.py | L14–29 | `purchase_method`: `'purchase'`("On ordered quantities") / `'receive'`("On received quantities") — services forced to `'purchase'` (2-way match only); the **AP-side equivalent of Sale's `invoice_policy`** |
| POL-13/22/23 | purchase_order_line.py / purchase_stock override | L244–251; L55–80, 63–77 | Base handles only `'manual'` → `0.0` otherwise; `purchase_stock` overrides for `'stock_moves'`: sums only `done` moves, with explicit return/dropship netting rules (a purchase-return move subtracts; a dropship-origin move already counted elsewhere is deliberately ignored to avoid double-counting) |
| POL-17 | purchase_order_line.py | L98–105 | Two real DB `models.Constraint` CHECKs — accountable-field-shape rules, matching the Accounting-Core pattern |
| POL-24 | purchase_stock override | L169–199 | Once `qty_received >= product_qty`, **no new picking/move is auto-created** — the closest thing to an over/under-receipt gate. Over-receipt itself is **not blocked anywhere** |
| POL-29 | purchase_stock/stock_move.py | L129–131 | `stock.move._is_purchase_return()` = `location_dest_id.usage=='supplier'` (or inter-company transit with an origin) — **the entire return-to-vendor detection mechanism**, a pure location predicate, not a dedicated model/button |
| POL-30/31 (negative) | purchase/, purchase_stock/ full-file greps | — | **Zero** functional hits for a dedicated return-to-vendor feature or for "backorder" anywhere in Purchase source |
| POL-32/33/34/35 | purchase_stock/purchase_order.py; res_config_settings.py; stock_account; stock_dropshipping | multiple | Dropship = one-line destination substitution (`property_stock_customer` instead of warehouse stock), gated on `picking_type_id.code=='dropship'`; the actual `_is_dropshipped()` bodies live in `stock_account`, while a **same-named, independently-defined** pair also exists in the optional `stock_dropshipping` module — a real method-name-collision hazard for grep-based migration tooling |
| POL-37/38 | schema_only.sql | FK block | `purchase_order_line.sale_line_id → sale_order_line` and `purchase_request_id → purchase_request` — both DB-confirmed, **neither declared in any file read this phase** — a direct PO-line-to-SO-line traceability FK (likely dropship/MTO chain) for a future cross-module phase to open |

## Synthesis — PO Line Quantities & Receipt

- **Three quantity concepts, precisely**: **Ordered** (`product_qty`, plain input, chatter-logged not blocked on
  post-confirmation edit); **Received** (`qty_received`, architecturally dispatched by `qty_received_method` —
  exactly the same "same field, different meaning by mode" pattern Phase 2 found for `stock.move.quantity`);
  **Invoiced/to-invoice** (gated by the product-level `purchase_method`, structurally analogous in role to what a
  Sale-side `invoice_policy` does for AR, though no Sale file was reopened to confirm the exact parallel — flagged
  as structural inference, not asserted fact about Sale).
- **Over/under receipt has no dedicated field or flag anywhere.** The only reaction to a mismatch is procedural:
  auto-picking-creation stops once received catches up to ordered; over-receipt is never specially detected or
  blocked.
- **Backorder is never referenced by name or field on the Purchase side** — remaining supply is tracked implicitly
  through not-done moves and demand-vs-covered arithmetic, never through `stock.picking.backorder_id`.
- **Return-to-vendor has no dedicated Purchase feature** — the exact structural mirror of the Sales-side finding
  (Phase 3 §05: no Sale Return button either). Purchase is, if anything, more Inventory-owned: it doesn't even
  carry a "view return" smart button the way dropship gets one.
- **Dropship is real Purchase-side routing but minimal**: a one-line destination swap on the same move-creation
  call, not a separate code path.
- **Source-specific coupling**: the AP invoicing gate lives on the **product**, not the order — two lines on the
  same PO for different products can be on different billing bases simultaneously. `qty_received`'s meaning is
  100% dependent on a same-record selection field that is itself product-type-derived and can differ line-to-line
  on the same order.
- **Confidence**: High for all direct citations (both line files read in full); High for the return/backorder
  absence claims (full-file greps, not sampling).

---

# 08 — CRITICAL FINDINGS CARRIED FORWARD TO LATER PHASES

1. **The orphaned two-level manager-approval schema now spans three models** (`sale_order`, `purchase_order`,
   `purchase_request`) with two parallel orphaned reject-log tables (`purchase_order_level_reject`,
   `purchase_request_level_reject`) — zero Python source declares any of it anywhere. This is the single most
   significant open governance question across GROUP A research to date. Carry to the Unknown/Conflict register
   and Fit-Gap pack as the top priority item, and flag for whoever researches MRP next (the responsible-looking
   module's manifest also names MRP Order).
2. **The module most plausibly responsible cannot be the origin** — its own storage tables don't exist in the live
   DB (never installed), and its one functional Purchase-adjacent code path references a non-existent field,
   confirming that code path is dead. A **separate, partial clue** (`x_review_result`/`x_has_request_approval`
   exactly matching that module's dynamic-field-creation pattern) suggests a possible *data-level* configuration
   against `purchase.order`/`purchase.request` that source code cannot reveal — genuinely undecidable without a
   row-level data pull (`ir_model_fields`/`ir_model_data`).
3. **Purchase's real approval gate is a single amount-threshold check, not the orphaned two-level chain.** Do not
   conflate `_approval_allowed()`/`po_double_validation` with the orphaned schema — they are two entirely
   different, coexisting mechanisms.
4. **`purchase.requisition` is not the tendering table** — it's a standing agreement (blanket order/template). The
   real multi-vendor comparison mechanism lives on `purchase.order` itself, independent of any requisition. Any
   target design must not conflate the two.
5. **Purchase Request's own author intended its native approval buttons to be replaced by an external engine**
   (explicit code comments) — but the one module that could do that never got as far as touching `purchase.order`,
   and its core tables were never installed. The demand-signal layer's *actual* live approval mechanism (native
   buttons vs. some other system) cannot be determined from source alone.
6. **Return-to-vendor and Sale-side return are structurally identical findings**: neither module has a dedicated
   return feature; both defer entirely to Inventory's generic location-usage-based return mechanism. This
   symmetry is itself a finding worth preserving — the "Return" concept in this codebase is Inventory-owned,
   full stop, regardless of which side (Sale or Purchase) originated the transaction.
7. **A previously-unknown PO-line-to-SO-line FK (`purchase_order_line.sale_line_id`) exists in the DB with no
   declaring module identified in either Sales (Phase 3) or Purchase (this phase) research** — likely a
   dropship/MTO-chain bridge module. Flag for Phase 5 (Cross-Module E2E), since it is direct schema evidence of a
   Sales↔Purchase link that neither domain's research alone surfaced.
8. **Method-name collisions are a real migration-tooling hazard in this codebase**: `_is_dropshipped()` exists
   independently in both `stock_account` (called by `purchase_stock`) and `stock_dropshipping` (on
   `purchase.order`/`purchase.order.line`, unrelated), with different scopes. A migration tool resolving calls by
   name alone will attribute logic to the wrong site.
9. **Unresolved, needed before this cluster is closed for Fit-Gap purposes**: whether `purchase_stock` cascades
   `button_cancel()` into receipts; the declaring module for `sale_line_id`/`purchase_request_id` on
   `purchase_order_line`; full contents of `stock_dropshipping/models/stock.py`. All EVIDENCE_MISSING, not guessed.
