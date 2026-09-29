# Source Map (candidate) — `mrp_subcontracting_account`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `mrp_subcontracting_account` |
| Display name | Subcontracting Management with Stock Valuation |
| Manifest version | 0.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `53ff8db8ad5b995b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mrp_subcontracting_account/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `mrp_subcontracting`, `mrp_account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Manufacturing / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `product.product`, `stock.move`, `mrp.production`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `product.product`, `stock.move`, `mrp.production`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 2 (of which company-scoped by text 0); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 28 of 28 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map Trace Note: mrp_subcontracting_account

Source revision: 19.0.post20260921 (Odoo 19 Community). Pointers relative to the addons root. `(TEST)` = test-derived. Neutral business language; no code copied.

## 1. Capabilities
- Bridge module: "manage subcontracting with valuation" (`mrp_subcontracting_account/__manifest__.py:8-10`). Depends on `mrp_subcontracting` and `mrp_account` (`:11`); auto-installs when both are present (`:13`) - conditional/optional, never a stand-alone feature.
- Three behaviours only: (a) sets the subcontracting fee component of the finished product's cost from the receipt, (b) adds vendor price to BoM cost computation, (c) keeps the fee out of the production-side journal value for non-standard costing.
- No settings, no new business objects, no data files besides security (`__manifest__.py:16-19`).

## 2. Business objects and lifecycle touched
- Uses the production order's "Extra Unit Cost" field owned by mrp_account (`mrp_account/models/mrp_production.py:13`). That field is copied to backorders (`mrp_account/models/mrp_production.py:96-98`).
- Lifecycle position: the subcontract receipt is validated, which closes the production (`mrp_subcontracting/models/stock_picking.py:45-58`); while the production is valued, this module fills Extra Unit Cost from the receipt, then the standard manufacturing cost routine sums components + extra cost (`mrp_subcontracting_account/models/mrp_production.py:10-22`, `mrp_account/models/mrp_production.py:73-74`).

## 3. Actions, gating, constraints, security
- No user-triggered actions; automatic on production closing.
- Security: portal-only read access to analytic accounts and read/write to analytic lines (`mrp_subcontracting_account/security/ir.model.access.csv:2-3`). Two record rules (Portal group):
  1. Analytic accounts (`security/mrp_subcontracting_account_security.xml:4-9`): a subcontractor sees only accounts linked to BoMs that list them as subcontractor.
  2. Analytic lines (`security/mrp_subcontracting_account_security.xml:11-16`): only lines whose account belongs to those BoMs.
  Purpose: subcontractor portal users recording work on productions must not see other partners' analytics.
- Company scoping: no dedicated rules; rules key on the user's commercial partner only. Multi-company behaviour: UNKNOWN - EVIDENCE INSUFFICIENT.

## 4. Accounting / inventory handoffs and cost determination
Ownership by module:
- Fee = "subcontracting cost per unit" - owned here: taken from the last validated receipt line of the production. Priority as coded: (1) vendor-bill value for the received quantity, plus (2) purchase-order (unbilled) value for the remainder; if both are zero, fall back to the receipt line's own unit price (`mrp_subcontracting_account/models/mrp_production.py:11-21`). Bill/PO lookup routines are defined generically in `stock_account/models/stock_move.py:480-486` and implemented for purchases in `purchase_stock/models/stock_move.py:157,229`; the valuation order (bill first, then quotation/PO, then returns) is in `stock_account/models/stock_move.py:401-424`.
- Finished product unit cost = (consumed component values + workcenter cost + fee x quantity) / quantity, less by-product share - owned by `mrp_account` (`mrp_account/models/mrp_production.py:57-94`, sum at `:73-74`).
- Costing-method split: for standard-cost products the finished move is priced at the product's standard price (`mrp_account/models/mrp_production.py:92-93`); for FIFO/average it is the computed total (`:93`). The difference is posted as a variance on the receipt (TEST `mrp_subcontracting_account/tests/test_subcontracting_account.py:224-250` - standard cost 40 vs components 30 + fee 15: production-account entries use component values and the finished value at standard).
- Journal value of the production-side finished move excludes the fee (non-standard products) so that the fee is booked through the receipt/vendor side: `mrp_subcontracting_account/models/stock_move.py:9-17`.
- Components: valued/consumed from the subcontracting location stock as ordinary production consumption; the component value enters the finished cost through `consumed_moves` (`mrp_account/models/mrp_production.py:74`) (TEST `tests/test_subcontracting_account.py:27-79` flow with components placed in the subcontracting location).
- BoM cost estimate: for a subcontract BoM, adds the vendor price for the BoM quantity and subcontractors, converted to company currency at today's date and to the product unit (`mrp_subcontracting_account/models/product_product.py:10-19`) (TEST `tests/test_subcontracting_account.py:280-345`: 150 fee + components = 700; foreign-currency fee converted).
- Bill vs PO price vs component cost: fee comes from bill, else PO, else receipt price; components from consumed component values; combined by mrp_account. Landed costs and dropship: not handled here (see `mrp_subcontracting_landed_costs`, `mrp_subcontracting_dropshipping`).
- Backorders and tracked components keep the cost logic (TEST `tests/test_subcontracting_account.py:81,165`). Missing production-account case is tested (TEST `:252`).

## 5. Configuration that changes outcomes
- Product category costing method (standard vs FIFO/average) and valuation mode (automated/real-time) decide whether fee is on the production side (`mrp_subcontracting_account/models/stock_move.py:14`, `mrp_account/models/mrp_production.py:88-93`).
- Vendor price list entry for the product and subcontractor drives BoM cost and PO price defaults (`models/product_product.py:15`).
- Production/valuation accounts on the product category and its production location (TEST `tests/test_subcontracting_account.py:252`).

## 6. Effective extension path
Models extended here: `mrp.production`, `product.product`, `stock.move`. Downstream community modules that alter the same valuation chain: `mrp_subcontracting_purchase` (bill/PO-driven revaluation of the finished move), `mrp_subcontracting_dropshipping`, `purchase_stock`, `stock_account`, `mrp_account`. Landed costs: `mrp_subcontracting_landed_costs`.

## 7. By-products
Subcontract BoMs cannot have by-product lines (`mrp_subcontracting/models/mrp_bom.py:24-27`). The general by-product cost-share routine in the shared cost function (`mrp_account/models/mrp_production.py:76-93`) would apply only if by-product moves existed on the production; this module adds nothing for them. Manual by-products on a subcontract production: UNKNOWN - EVIDENCE INSUFFICIENT.

## 8. UNKNOWN items
- Behaviour when the receipt is only partially billed across several bills beyond the two-step bill-then-PO split: UNKNOWN - EVIDENCE INSUFFICIENT.
- Rounding/currency treatment of the fee when PO currency differs from company currency inside the production cost step: UNKNOWN - EVIDENCE INSUFFICIENT (revaluation on bill is handled in `mrp_subcontracting_purchase`; see that note).
- Treatment of the fee for standard-cost products beyond the tested variance case: UNKNOWN - EVIDENCE INSUFFICIENT.

