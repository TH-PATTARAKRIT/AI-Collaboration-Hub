# Source Map (candidate) — `mrp_subcontracting_landed_costs`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `mrp_subcontracting_landed_costs` |
| Display name | Landed Costs With Subcontracting order |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `030b819375a59a03` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mrp_subcontracting_landed_costs/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `stock_landed_costs`, `mrp_subcontracting`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Manufacturing / Advanced views to manage landed cost for subcontracting orders
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `stock.landed.cost`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `stock.landed.cost`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 21 of 21 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: mrp_subcontracting_landed_costs
Source revision: 19.0.post20260921 (Odoo 19 Community). Read-only trace; neutral business language; no code copied.

## A. Capabilities / activation
- Bridge that lets landed costs (extra freight/duty-type costs added to already-received goods) be applied to receipts of subcontracted goods, and makes such receipts easier to find in the landed-cost form. mrp_subcontracting_landed_costs/__manifest__.py:5-11
- Conditional: installs automatically when both the landed-cost module and the subcontracting module are present (auto_install). mrp_subcontracting_landed_costs/__manifest__.py:12,17
- No settings, groups, menus, security records or data of its own; only one model extension and one view extension. mrp_subcontracting_landed_costs/__manifest__.py:14-16
- The landed-cost feature itself is switched on by a setting owned by stock_account (module_stock_landed_costs). stock_account/models/res_config_settings.py:7

## B. Business objects and relationships
- Extends the landed-cost document (stock.landed.cost, owned by stock_landed_costs). mrp_subcontracting_landed_costs/models/stock_landed_cost.py:7-8
- Change in behaviour: when selecting which stock movements a landed cost applies to, any movement flagged as a subcontract receipt is replaced by the movements that fed it (its origin movements, i.e. the manufacturing-side movement of the finished good); ordinary movements stay as they are. mrp_subcontracting_landed_costs/models/stock_landed_cost.py:10-18
- Effect (TEST): cost is valued on the linked subcontracting manufacturing movement, not on the receipt movement itself; the receipt movement shows zero value while its origin movement carries the value including the added cost. mrp_subcontracting_landed_costs/tests/test_subcontracting_landed_costs.py:75-78 (TEST)
- Lifecycle (draft -> posted -> cancelled; posting requires target records and matching adjustment totals) is owned by stock_landed_costs, not here. stock_landed_costs/models/stock_landed_cost.py:54-58,103-118,248-254
- View: the "manufacturing orders" selector on the landed-cost form is switched to the subcontracting search/list views, and the transfers selector is restricted to same-company transfers that are incoming, outgoing, or completed subcontract movements. mrp_subcontracting_landed_costs/views/stock_landed_cost_views.xml:8-13

## C. Validations / security / multi-company
- No constraints of its own. Inherited: only FIFO or average-cost products with a non-cancelled, non-zero-quantity movement are eligible; otherwise the user is blocked with an error. stock_landed_costs/models/stock_landed_cost.py:159-177
- Access inherited: landed-cost objects are readable/writable only by inventory managers (group stock.group_stock_manager). stock_landed_costs/security/ir.model.access.csv:2-4
- Company scoping inherited: record rule limits landed costs to the user's allowed companies; the transfers selector also filters on the cost's company. stock_landed_costs/security/stock_landed_cost_security.xml:4-8; mrp_subcontracting_landed_costs/views/stock_landed_cost_views.xml:12

## D. Handoffs (owner module in brackets)
- Valuation/journal entry on validation: posted by stock_landed_costs [stock_landed_costs]; only for products whose valuation is real-time; manual-valuation products create no entry. stock_landed_costs/models/stock_landed_cost.py:112-137,150-153
- Test evidence of split of cost between a subcontracted product and a normal product on the same receipt (equal split, 99 spread across 2 lines -> 49.5 each). (TEST) mrp_subcontracting_landed_costs/tests/test_subcontracting_landed_costs.py:91-139
- Test evidence that with average costing and partial stock left, the journal entry is proportional to quantity still in stock (7 of 10), and the product cost rises from 10 to 11. (TEST) mrp_subcontracting_landed_costs/tests/test_subcontracting_landed_costs.py:141-211
- Subcontract flag itself is owned by [mrp_subcontracting]. mrp_subcontracting/models/stock_move.py:14

## E. Configuration that changes outcomes
- Product cost method (FIFO/average) and valuation type (real-time) per product category gate whether cost can be applied and journalised. stock_landed_costs/models/stock_landed_cost.py:161,133-134
- Company landed-cost journal default (lc_journal_id) supplies the journal default. stock_landed_costs/models/res_company.py:10; stock_landed_costs/models/stock_landed_cost.py:27-29

## F. Effective extension path (other Community modules extending stock.landed.cost)
- mrp_landed_costs (adds manufacturing-order target), mrp_subcontracting_landed_costs (this module). Others: none found across the addons root.

## G. Not verified
- Behaviour when a subcontract receipt has several origin movements or a partially received/backordered subcontract: UNKNOWN — EVIDENCE INSUFFICIENT
- Behaviour of Community-edition subcontracting with landed costs applied via a manufacturing-order target rather than the receipt: UNKNOWN — EVIDENCE INSUFFICIENT
- Reversal of a posted landed cost on subcontract moves beyond the note that negative landed costs are the reversal route (stock_landed_costs/models/stock_landed_cost.py:97-101): UNKNOWN — EVIDENCE INSUFFICIENT

