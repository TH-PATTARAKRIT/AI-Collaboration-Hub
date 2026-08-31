# A9 — Inventory → Accounting / Valuation Interface Evidence

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Deeply research source-side valuation/costing evidence and the Inventory↔Accounting handoff, while preserving the authority boundary (Inventory knows the stock/valuation-handoff fact; Accounting owns final financial truth) | Claude (Team A, DR-002) | This artifact; `stock_account/models/`, `stock_landed_costs/models/` | 2026-08-31 | Independent Evidence Review (pending) | VERIFIED (direct source citation) | **This is the deliverable the Boss Amendment specifically mandated deepening beyond GROUP A's "interface observation only" scope** — directly gates A16 Cross-Proof pack |

## 0. Governing authority boundary (restated, per DR-002 §7/A9 and Roadmap Rule AB-03)

`Inventory may know the stock fact and valuation handoff evidence. Accounting owns final financial truth and posting semantics.` Every finding below states explicitly: **WHAT INVENTORY KNOWS / WHAT SOURCE EMITS / WHAT ACCOUNTING MUST OWN / WHAT REMAINS UNKNOWN.** No GL account structure, posting rule, or Thailand tax treatment is designed or invented here.

## 1. Material structural finding: no `stock.valuation.layer` model in this codebase

Standard Odoo 14–18 ships a `stock.valuation.layer` model (a persistent, per-movement valuation ledger row: `quantity`, `unit_cost`, `value`, `remaining_qty`, `remaining_value`, `account_move_id`, `stock_move_id`). **This file/model does not exist anywhere in this checkout** — confirmed by exhaustive grep across the entire `stock_account` module tree for `_name = 'stock.valuation.layer'` (zero hits, both quoting styles), and `stock_account/models/__init__.py` imports no such module.

Instead, valuation data lives **directly on `stock.move` itself** (fields below), plus a `product.value` model that stores only manual-override audit records, not the full valuation ledger.

- **WHAT INVENTORY KNOWS**: which move happened, its quantity, and (via the fields below) its computed monetary value.
- **WHAT SOURCE EMITS**: a `value` on the move record itself, not a separate valuation-layer document.
- **WHAT ACCOUNTING MUST OWN**: whether "value lives on the move" vs. "value lives on a dedicated valuation-layer ledger" is an acceptable target pattern is an Accounting/Team-B design decision, not something this research recommends either way.
- **WHAT REMAINS UNKNOWN**: whether this is a customer-specific fork/older-version artifact or reflects the actual reference codebase's true current architecture (version could not be confirmed — no `release.py` found under the given source root; see A14 N-A9-01).

## 2. Valuation fields on `stock.move` (module: `stock_account`)

| Field | Type | Mechanism |
|---|---|---|
| `value` | Monetary, **stored** | Set by `_set_value()`, not a declarative `@api.depends` compute — "the current value of the move; zero if the move is not valued" |
| `value_manual` | computed/inverse | Manual override; inverse writes a `product.value` audit record |
| `remaining_qty` | computed, `@api.depends('quantity','product_id.stock_move_ids.value')` | FIFO-style "how much of this incoming lot/layer is still unconsumed" |
| `remaining_value` | computed, `@api.depends('value','remaining_qty')` | Prorates `value` by `remaining_qty/quantity` (FIFO) or `remaining_qty * standard_price` (otherwise) |
| `account_move_id` | Many2one to `account.move` | **The explicit Inventory→Accounting link field** — Accounting-owned on the far side |
| `is_in` / `is_out` / `is_dropship` / `is_valued` | computed+stored booleans | Classify the move for valuation purposes; `is_valued = is_in or is_out` |

**WHAT INVENTORY KNOWS**: the move's physical direction (`is_in`/`is_out`), its computed cost/value, and whether it is even eligible for valuation (`is_valued`, gated on `is_storable` and `valuation=='real_time'`, per A5 §4's storable-gating chain). **WHAT SOURCE EMITS**: `value` and `account_move_id` — a single number and a link, not the accounting entry's own construction logic. **WHAT ACCOUNTING MUST OWN**: the journal entry itself (`account.move`/`account.move.line` records), account selection, and posting semantics — see §4.

## 3. Costing method — the source-side inputs (not a target ruling)

| Field | Location | Values | Notes |
|---|---|---|---|
| `product.category.property_cost_method` | `stock_account`, `company_dependent=True` | `standard` / `fifo` / `average` (AVCO) | Category-level default |
| `product.template.cost_method` | `stock_account`, computed | falls back to `product_template.categ_id.property_cost_method`, then `company.cost_method` | Product-level resolved value |
| `product.category.property_valuation` | `stock_account`, `company_dependent=True` | `periodic` ("at closing") / `real_time` ("at invoicing", perpetual) | Gates whether journal entries are created automatically at all (§1's `is_valued` gate) |
| `product.template.valuation` | `stock_account`, computed | falls back to `company.inventory_valuation` | Product-level resolved value |
| `product.template.lot_valuated` | `stock_account`, computed+stored | boolean, forced `False` when `tracking=='none'` (A5 §7) | Enables per-lot/serial valuation |
| `stock.quant.cost_method` | `stock_account` | mirrors product's, display/grouping only | Not an independent source of truth |

**WHAT INVENTORY KNOWS**: which costing method applies to a given product/category and whether valuation is real-time or periodic. **WHAT ACCOUNTING MUST OWN**: whether `standard`/`fifo`/`average` are the correct methods for SMEsPlus's target Thailand accounting treatment, and how each interacts with Thai tax/CIT costing rules — **not evidenced or claimed by this research** (out of scope, deferred to COA-G06 per the Accounting Gate's own established boundary).

## 4. The valuation-computation priority chain and journal-entry creation

- `_set_value()` (called from `stock.move._action_done()` override, **before** `super()._action_done()` for outgoing moves): for incoming (`is_in`) moves, `value = _get_value()`; for outgoing moves, computes COGS via `_run_fifo()` (if `cost_method=='fifo'`) or `standard_price * qty` (average/standard), with a lot-level override when `lot_valuated`.
- `_get_value_data()` priority order (per its own docstring): accounting documents (invoices/bills) → quotations/landed costs → production → standard-price fallback, implemented across `_get_value_from_account_move`, `_get_value_from_production`, `_get_value_from_quotation`, `_get_value_from_returns`, `_get_value_from_std_price`, `_get_value_from_extra`.
- `_create_account_move()`: creates **one `account.move` per batch**, `journal_id = company.account_stock_journal_id`, with a debit/credit `account.move.line` pair from `_get_account_move_line_vals()` (stock valuation account vs. the location's `valuation_account_id`); links back via `stock.move.account_move_id`; posts it (`account_move._post()`).
- `account.move._post()` override (in `stock_account`) additionally creates **COGS lines** for customer invoices via `_stock_account_prepare_realtime_out_lines_vals()` — the anglo-saxon-accounting mechanism: debit COGS/stock-variation account, credit Stock Account, gated on `product.valuation=='real_time'`.
- `account.move.line.cogs_origin_id` (self-referencing) — "technical field used to keep track in the originating line of the anglo-saxon lines."

**WHAT INVENTORY KNOWS**: the computed cost/value figure and which accounts a category is configured to use. **WHAT SOURCE EMITS**: a complete, already-posted `account.move` — in this codebase, Inventory's own code path constructs and posts the journal entry, not a separate Accounting-domain service. **WHAT ACCOUNTING MUST OWN**: whether SMEsPlus's target architecture should replicate "Inventory directly writes journal entries" or instead require Inventory to emit a neutral valuation event that an Accounting-owned posting service consumes — **this is a genuine, material target-design fork this research surfaces but does not resolve**, registered in A13/A16 as a Cross-Proof-relevant open question, not a recommendation.

## 5. Landed costs (`stock_landed_costs`) — post-receipt cost allocation

- `stock.landed.cost` (`state`: `draft`/`done`/`cancel`; `account_move_id` → `account.move`; `vendor_bill_id` → `account.move` with `move_type='in_invoice'`; `valuation_adjustment_lines` One2many).
- `stock.valuation.adjustment.lines` — per-move allocation: `move_id` → `stock.move`, `former_cost` (Monetary, "Original Value"), `additional_landed_cost`, `final_cost` (computed = sum).
- Mechanism: `stock_landed_costs` overrides `stock.move._get_value_from_extra()` to add `lc.additional_landed_cost` into the move's `value` through the **same** priority chain used for ordinary valuation (§4) — landed costs are additive to `stock.move.value`, not a parallel ledger.
- `StockLandedCost.button_validate()` posts the landed-cost journal entry, then calls `valuation_adjustment_lines.move_id._set_value()` to force recomputation of the affected moves.
- Split methods: `equal`, `by_quantity`, `by_current_cost_price`, `by_weight`, `by_volume`.
- `_create_account_move_line` on `stock.valuation.adjustment.lines` debits the stock valuation account and credits the landed-cost product's expense account (or a configured `account_id`), pro-rated by `remaining_qty` — the Accounting-owned journal-entry side of a landed cost.

**WHAT INVENTORY KNOWS**: which moves a landed cost applies to and by what allocation method. **WHAT SOURCE EMITS**: an additive adjustment to the same `stock.move.value` field. **WHAT ACCOUNTING MUST OWN**: the vendor-bill-to-landed-cost linkage's tax/accounting treatment.

## 6. Explicit Inventory-owned vs. Accounting-owned field split (summary table)

| Inventory-owned (physical/cost reality) | Accounting-owned (explicit `account.move`/`account.move.line` reference) |
|---|---|
| `stock.move.value`, `value_manual`, `remaining_qty`, `remaining_value`, `standard_price` | `stock.move.account_move_id` → `account.move` |
| `stock.quant.value` (derived, display-only) | `account.move.stock_move_ids` (inverse) |
| `product.template.cost_method`, `valuation`, `lot_valuated` | `account.move.line.cogs_origin_id`, `is_landed_costs_line` |
| `stock.valuation.adjustment.lines.former_cost`/`additional_landed_cost`/`final_cost` | `stock.landed.cost.account_move_id`, `vendor_bill_id` |
| `product.category.property_cost_method` | `product.category.property_stock_valuation_account_id`, `property_stock_journal`, `account_stock_variation_id` (all `account.account`/`account.journal` references) |

## 7. Date/cutoff interaction

Not directly evidenced this pass at the field level (see A7 §4 — the same open gap applies here: no `date`/period-lock field was read during this specific research pass). **Registered as the single most material open item feeding Lane C Cross-Proof scenario 6**, in A14 (N-A9-02).

## 8. Source dependencies on journals/accounts/COA

Confirmed present as configuration references only (`account_stock_journal_id`, `property_stock_valuation_account_id`, `property_stock_journal`, `account_stock_variation_id`, `property_price_difference_account_id`) — these are foreign keys into Accounting's own COA/journal setup, not values this research defines or validates. Per Roadmap §"Accounting-dependent Inventory boundary," this remains classified `ACCOUNTING INTERFACE DEPENDENCY` / `COA DEPENDENCY`, not fabricated.

No Evidence = No Progress. DELTA-FIRST. Inventory does not invent GL/COA/posting rules.
