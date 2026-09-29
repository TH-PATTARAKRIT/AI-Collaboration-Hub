# Source Map (candidate) — `mrp_repair`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `mrp_repair` |
| Display name | Mrp Repairs |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `73dcbf7c594b5191` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mrp_repair/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `repair`, `mrp`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Inventory / —
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `repair.order`, `stock.move`, `mrp.production`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `repair.order`, `stock.move`, `mrp.production`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 25 of 27 source pointers resolve to an existing file and in-range line (2 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: mrp_repair
Source revision: 19.0.post20260921 (Odoo 19 Community). Read-only trace; neutral business language; no code copied.

## A. Capabilities / activation
- Two capabilities: (1) parts that are kits (phantom bills of materials) added to a repair are automatically replaced by their components; (2) manufacturing orders and repair orders are cross-linked and each shows a counter/button to the other. mrp_repair/models/repair.py:31-47,49-65; mrp_repair/models/production.py:9-34
- Conditional: auto-installs when repair and mrp are both installed. mrp_repair/__manifest__.py:9,15
- Also narrows the "add from catalog" list on a repair to the components of the repaired product's bill of materials, with a default filter on it when a BoM exists. mrp_repair/models/repair.py:67-74

## B. Business objects and relationships
- Kit expansion: for each repair part, the module looks for a phantom BoM for that product in the part's company; if found, the kit line is deleted and replaced by one part line per non-service component, quantities scaled to the kit quantity, keeping the repair, the line type (add/remove/recycle), price, and locations, and reset to draft. mrp_repair/models/repair.py:31-47,77-92
- Expansion triggers after every create and every write of a repair order (so parts added later, including to a confirmed repair, are expanded). mrp_repair/models/repair.py:20-29
- (TEST) Adding a kit to a confirmed repair yields component lines only, linked to the repair. mrp_repair/tests/test_mrp_repair_flow.py:56-85 (TEST)
- (TEST) A consumable-type kit product can itself be repaired through to Repaired state. mrp_repair/tests/test_tracability.py:327-345 (TEST)
- Repair -> manufacturing: count of manufacturing orders = those attached to the repair's stock references. mrp_repair/models/repair.py:9-18,49-65
- Manufacturing -> repair: count of source repairs = repairs reached through the order's downstream moves. mrp_repair/models/production.py:9-34
- (TEST) With a make-to-order rule on the repair operation and a product with MTO + Manufacture routes, confirming the repair creates a manufacturing order for the requested quantity linked back to the repair (counts 1/1). mrp_repair/tests/test_mrp_repair_flow.py:16-54 (TEST)
- Kit explosion on stock movements in general (not only repair): the repair link is carried onto exploded component movements. mrp_repair/models/stock_move.py:7-11 (base explosion owned by mrp: mrp/models/stock_move.py:478,506)
- Lifecycle is that of repair (draft -> confirmed -> under repair -> repaired / cancelled); this module adds no states. repair/models/repair.py:42-53
- UI: manufacturing button on repair form hidden in draft; repair button on manufacturing form hidden at zero. mrp_repair/views/repair_views.xml:13; mrp_repair/views/production_views.xml:13

## C. Validations / security / multi-company
- No constraints of its own. Kit lookup is restricted to the part's company; it runs with elevated rights for BoM lookup/unlink of the replaced line. mrp_repair/models/repair.py:35,39,45
- Service-type components are skipped (not turned into part lines). mrp_repair/models/repair.py:41
- Groups: manufacturing counter on repair needs manufacturing user (mrp.group_mrp_user); repair counter on manufacturing needs inventory user. mrp_repair/models/repair.py:12; mrp_repair/models/production.py:12
- Company scoping is inherited from parent record rules (repair: repair/security/repair_security.xml:5-9).

## D. Handoffs (owner in brackets)
- Manufacturing orders come from procurement (make-to-order rule + Manufacture route) [stock rules, mrp]. mrp_repair/tests/test_mrp_repair_flow.py:23-38 (TEST)
- BoM/kit definition and explosion [mrp]. mrp_repair/models/repair.py:35-39
- Traceability of lots/serials across repair and production [stock traceability, repair, mrp]; TEST coverage for tracked components removed by a repair then reused in another BoM. mrp_repair/tests/test_tracability.py:15-80,83-179 (TEST)
- No accounting handoff in this module.

## E. Configuration that changes outcomes
- A phantom BoM on the part product (and its company/type/picking type) decides whether explosion happens. mrp_repair/models/repair.py:35
- BoM of the repaired product drives catalog filtering. mrp_repair/models/repair.py:68-73
- MTO/Manufacture routes on product and the repair operation's MTO rule. mrp_repair/tests/test_mrp_repair_flow.py:23-38 (TEST)

## F. Effective extension path
- repair.order extended by mrp_repair, purchase_repair, l10n_din5008_repair; mrp.production extended by many modules (mrp_repair among them); stock.move extended by many (mrp_repair among them). Module names only, from _inherit search.

## G. Not verified
- Price behaviour on exploded lines (price copied per component from the kit line without splitting; commercial effect on quotation): UNKNOWN — EVIDENCE INSUFFICIENT
- Exploding kits already reserved/picked (state reset to draft in vals): UNKNOWN — EVIDENCE INSUFFICIENT
- Behaviour with nested phantom BoMs beyond what the explode call returns: UNKNOWN — EVIDENCE INSUFFICIENT
- Performance/recursion considerations of running expansion on every write: UNKNOWN — EVIDENCE INSUFFICIENT

