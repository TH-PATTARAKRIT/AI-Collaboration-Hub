# Source Map (candidate) — `mrp_landed_costs`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `mrp_landed_costs` |
| Display name | Landed Costs On MO |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `949c738d868f8f3e` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mrp_landed_costs/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `stock_landed_costs`, `mrp`
- Direct dependents in 300-module list (1): `project_mrp_stock_landed_costs`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Manufacturing / Landed Costs on Manufacturing Order
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 52 of 52 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map Trace Note: mrp_landed_costs

- Source revision: `19.0.post20260921` (Odoo 19.0 Community, addons root). Pointers are `module/path:LINE` relative to the addons root. `(TEST)` = derived from a test.
- Manifest: "Landed Costs On MO", category Supply Chain/Manufacturing, depends on stock_landed_costs and mrp, auto_install true (mrp_landed_costs/__manifest__.py:5,13,18). Total source is tiny: one model file (28 lines) and one view file (22 lines).

## 1. Capabilities
| Capability | Class | Pointer |
|---|---|---|
| Add "Manufacturing Orders" as a landed-cost target type | Conditional: module installs automatically when both stock_landed_costs and mrp are installed | mrp_landed_costs/__manifest__.py:13,18; mrp_landed_costs/models/stock_landed_cost.py:10-12 |
| Select manufacturing orders on a landed cost | Same | mrp_landed_costs/models/stock_landed_cost.py:13-15 |
| Eligible move set includes finished (and cost-sharing by-product) moves of chosen orders | Same | mrp_landed_costs/models/stock_landed_cost.py:23-28 |
| Form shows target selector and MO picker | Same | mrp_landed_costs/views/stock_landed_cost_views.xml:8-19 |
Everything else (documents, splitting, posting, valuation) is inherited unchanged from stock_landed_costs; see stock_landed_costs trace note.

## 2. Business objects and lifecycle
- No new model. Extends the landed cost document (stock.landed.cost) with target type value "Manufacturing Orders" and a many-to-many list of manufacturing orders (mrp_landed_costs/models/stock_landed_cost.py:7-15). Removing the module resets the target type to its default (ondelete "set default") (:12).
- States and transitions (Draft, Posted, Cancelled; validate/cancel) are unchanged, owned by stock_landed_costs (stock_landed_costs/models/stock_landed_cost.py:54-58, 97-153).
- Target document: manufacturing order. Moves considered = all moves of selected transfers (inherited) plus the finished-product moves of the selected orders, minus by-product moves whose cost share is empty/zero (mrp_landed_costs/models/stock_landed_cost.py:23-28). Note the transfers part is always included regardless of the selected target type (:25); the target type only controls which picker is shown and clears the other list on change (:17-21; stock_landed_costs/models/stock_landed_cost.py:76-79).
- Main finished product moves and by-products with a cost share are eligible; by-products without cost share are excluded. (TEST) (mrp_landed_costs/tests/test_stock_landed_costs_mrp.py:180-220).
- Component (raw material) moves are not in the target set (only finished and by-product moves are referenced) (mrp_landed_costs/models/stock_landed_cost.py:26-27).
- Further eligibility (inherited): product cost method FIFO or average, move not cancelled, non-zero quantity (stock_landed_costs/models/stock_landed_cost.py:161-162). If none qualifies, user error (:175-177).
- UI restricts the order picker to orders of the same company having a finished move flagged as valued incoming (mrp_landed_costs/views/stock_landed_cost_views.xml:14-18). That flag is only true for done moves (stock_account/models/stock_move.py:72-77). Server-side check that the order is done: UNKNOWN — EVIDENCE INSUFFICIENT.
- Split methods and apportionment: inherited (Equal, By Quantity, By Current Cost, By Weight, By Volume; rounding, equal fallback) (stock_landed_costs/models/stock_landed_cost.py:180-243). Weight/volume come from the finished product times produced quantity (stock_landed_costs/models/stock_landed_cost.py:170-171).
- (TEST) Order of 2 refrigerators, one Equal cost line of 5.0: one adjustment line for the finished product with 5.0; finished move value becomes 15.0 (component value 10 + 5) and a journal entry exists (mrp_landed_costs/tests/test_stock_landed_costs_mrp.py:78-134).

## 3. Validation, security, company scoping
- No constraints or validations are added by this module (mrp_landed_costs/models/stock_landed_cost.py has only field additions, one onchange and one target override).
- The MO list field is visible/readable only for `stock.group_stock_manager` (mrp_landed_costs/models/stock_landed_cost.py:13-15); the target selector is shown to that group too (mrp_landed_costs/views/stock_landed_cost_views.xml:8-11). (TEST) a user with only Inventory Administrator rights (no manufacturing rights) can pick the order and validate (mrp_landed_costs/tests/test_stock_landed_costs_mrp.py:136-178).
- Access rights and the multi-company rule are those of stock_landed_costs (stock_landed_costs/security/ir.model.access.csv:2-4; stock_landed_costs/security/stock_landed_cost_security.xml:4-8). This module adds no security files (mrp_landed_costs/__manifest__.py:15-17).
- Company scoping of order choice is by picker domain only (same company as the landed cost) (mrp_landed_costs/views/stock_landed_cost_views.xml:18); server enforcement UNKNOWN — EVIDENCE INSUFFICIENT.
- Form field is read-only once Posted (mrp_landed_costs/views/stock_landed_cost_views.xml:13-17).
- Automation: none.

## 4. Accounting handoffs (all owned by stock_landed_costs and stock_account; this module contributes only the target moves)
- Journal entry at Validate: per real-time-valued adjustment line, debit the finished product's stock valuation account, credit the cost line's account (else the cost product's expense account), amount scaled by the share of move quantity still in stock; skipped entirely for non-real-time products; no entry if no line results (stock_landed_costs/models/stock_landed_cost.py:121-130, 146-151, 345-388). (TEST) an entry exists for the MO case (mrp_landed_costs/tests/test_stock_landed_costs_mrp.py:129).
- Value of the already-completed finished-goods move increases by the landed amount through the extra-value hook and recomputation of the move value (stock_landed_costs/models/stock_move.py:14-40; stock_landed_costs/models/stock_landed_cost.py:152; stock_account/models/stock_move.py:292-358). (TEST) value 15.0 (mrp_landed_costs/tests/test_stock_landed_costs_mrp.py:134).
- Product cost by method (owner stock_account): Standard excluded from apportionment (stock_landed_costs/models/stock_landed_cost.py:161; stock_account/models/product.py:651-652); FIFO cost = total value / quantity on hand (stock_account/models/product.py:677-684); Average recomputed by stock_account routine (:686-690), formula UNKNOWN — EVIDENCE INSUFFICIENT.
- Whether the added cost is also reflected in already-issued sales of the finished product (cost of goods sold), beyond the remaining-stock share: UNKNOWN — EVIDENCE INSUFFICIENT.
- No price-difference/variation account is used by this module.
- Analytic distribution on the entry lines for orders linked to a project: added by project_mrp_stock_landed_costs, applied when target type is Manufacturing Orders, taken from the order's project (project_mrp_stock_landed_costs/models/stock_landed_costs.py:9-13). Picking-target equivalent lives in project_stock_landed_costs/models/stock_landed_costs.py:9-13.

## 5. Configuration that changes outcomes
- Target type on the document decides which picker is shown (mrp_landed_costs/views/stock_landed_cost_views.xml:13-18); moves of already selected transfers still count (mrp_landed_costs/models/stock_landed_cost.py:25).
- By-product cost share on the bill of materials/order decides whether a by-product receives landed cost (mrp_landed_costs/models/stock_landed_cost.py:26-27). (TEST) share 100 included, share 0 excluded (mrp_landed_costs/tests/test_stock_landed_costs_mrp.py:195-220).
- Product cost method and valuation type of the finished product (stock_account) decide eligibility and whether an entry is posted (stock_landed_costs/models/stock_landed_cost.py:124, 161).
- Split method default per landed-cost product, company default journal: see stock_landed_costs (stock_landed_costs/models/product.py:12-15; stock_landed_costs/models/res_company.py:10).
- Note: a landed cost created from a vendor bill (stock_landed_costs/models/account_move.py:21-40) starts with transfers as target; MO selection requires switching target type in the form. Bill-to-MO automation: UNKNOWN — EVIDENCE INSUFFICIENT.

## 6. Effective extension path
- stock.landed.cost is further extended by mrp_subcontracting_landed_costs (maps subcontract receipt moves to their originating production moves; its view inherits this module's form and adjusts picker domains/context) (mrp_subcontracting_landed_costs/models/stock_landed_cost.py:10-18; mrp_subcontracting_landed_costs/views/stock_landed_cost_views.xml:4-15). (TEST) subcontracting receipt: value moves to the source production move (mrp_subcontracting_landed_costs/tests/test_subcontracting_landed_costs.py:11-68).
- Analytic bridge: project_mrp_stock_landed_costs, auto-installed when project_mrp_account and mrp_landed_costs are present (project_mrp_stock_landed_costs/__manifest__.py:8-9).
- Manifest dependencies: only project_mrp_stock_landed_costs lists this module as a dependency. mrp_subcontracting_landed_costs lists stock_landed_costs and mrp_subcontracting, yet its view inherits this module's form by reference (mrp_subcontracting_landed_costs/__manifest__.py:12; mrp_subcontracting_landed_costs/views/stock_landed_cost_views.xml:4). Guaranteed load order of this module before it: UNKNOWN — EVIDENCE INSUFFICIENT.

## 7. UNKNOWN items
- Server-side check that selected orders are done / same company: UNKNOWN — EVIDENCE INSUFFICIENT.
- Average-cost formula and treatment of already-sold finished goods: UNKNOWN — EVIDENCE INSUFFICIENT.
- Creating an MO-targeted landed cost from a vendor bill: UNKNOWN — EVIDENCE INSUFFICIENT.
- Reopen of a Cancelled landed cost: UNKNOWN — EVIDENCE INSUFFICIENT.

