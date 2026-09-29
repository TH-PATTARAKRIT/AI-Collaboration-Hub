# Source Map (candidate) — `project_stock`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project_stock` |
| Display name | Project Stock |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G06 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `e9f99cdeb51d1066` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project_stock/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `stock`, `project`
- Direct dependents in 300-module list (2): `project_purchase_stock`, `project_stock_account`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Services/Project / Link Stock pickings to Project
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `stock.picking`, `project.project`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `stock.picking`, `project.project`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 25 of 25 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — project_stock (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities; core / optional / conditional
- Links stock transfers (pickings) to a project and gives project users shortcut views of the project's outbound ("From WH"), inbound ("To WH") and all transfers (project_stock/__manifest__.py:6; project_stock/models/project_project.py:10-20).
- Depends on stock and project; auto_install True, installed automatically when both are present (project_stock/__manifest__.py:8, :13).
- Shortcut entries on the project are shown only to inventory users (stock user group), on both the project task action and the project dashboard action (project_stock/views/project_project_views.xml:3-55). The project field on the transfer form is shown only to project users (project_stock/views/stock_picking_views.xml:9).
- Cost/analytic and re-invoicing behaviour is NOT here; it is added by separate bridge modules that also auto-install (see D).

## B. Business objects, relationships, lifecycle
- Transfer (stock.picking) gains an optional link to one project; templates (is_template) are excluded from the choice (project_stock/models/stock_picking.py:9).
- Project shortcuts filter transfers by the project; outbound = operation type code "outgoing", inbound = "incoming"; outbound view defaults the partner to the project customer; new transfers default to the project (project_stock/models/project_project.py:22-45).
- Non-outbound views also offer activity view (project_stock/models/project_project.py:30-32).
- No state machine of its own; transfer states (draft/confirmed/done etc.) are owned by stock. Project link may be set manually or propagated from purchase (see D).

## C. Validations, automation, security, multi-company
- No constraints, access CSV, record rules or cron in this module (file listing: only models and views).
- Access to transfers is governed entirely by stock; the project-link field is a plain link with no domain by company (project_stock/models/stock_picking.py:9). Multi-company consistency between project and transfer: UNKNOWN — EVIDENCE INSUFFICIENT.
- Downstream validations (owned by bridge modules): when an operation type has "analytic costs" enabled and the transfer has a project, validation creates analytic entries on the project; required analytic plans missing on the project raise an error (project_stock_account/models/stock_move.py:11-44; project_stock_account/models/stock_picking_type.py:9).
- Downstream: validating a transfer with re-invoicable products on a project whose linked sales order is draft/sent, cancelled or locked is refused (sale_project_stock/models/stock_picking.py:10-45).

## D. Handoffs (module ownership)
- Inventory documents and operation types: stock. Project record: project.
- Analytic accounting of stock moves to project: project_stock_account (depends stock_account, project_stock — project_stock_account/__manifest__.py:8). Adds analytic-costs flag on operation type, analytic line category "Inventory Transfer", "stock picking" analytic plan applicability (project_stock_account/models/stock_picking_type.py:9; project_stock_account/models/account_analytic_line.py:9; project_stock_account/models/analytic_applicability.py:10-15). Analytic entries only for moves with a project and an operation type that has analytic costs on (project_stock_account/models/stock_move.py:24-29).
- Landed costs analytic distribution from the project: project_stock_landed_costs (project_stock_landed_costs/models/stock_landed_costs.py:9-13).
- Sales re-invoicing of material to the project's sales order (creates order lines at validation for products with expense policy "sales price"/"cost"): sale_project_stock (depends sale_project, sale_stock, project_stock_account — sale_project_stock/__manifest__.py:12; sale_project_stock/models/stock_picking.py:10-61). Also sale_project_stock_account (bridge).
- Purchase: project on a purchase order is copied to receipts, and procurement-generated purchase orders are grouped per project: project_purchase_stock (project_purchase_stock/models/purchase_order.py:9-16; project_purchase_stock/models/stock_rule.py:9-18).

## E. Configuration/defaults that change outcomes
- Operation-type flag "analytic costs" (added by project_stock_account) decides whether validating a project-linked transfer produces project analytic entries and re-invoicing (project_stock_account/models/stock_picking_type.py:9).
- Product expense policy (from sale/account setup) decides which moves are re-invoiced (sale_project_stock/models/stock_picking.py:20).
- Project's analytic account/distribution supplies the cost allocation (project_stock_account/models/stock_move.py:14).

## F. Extension path (grep of _inherit)
- project_stock extends project.project and stock.picking (project_stock/models/*.py). Modules depending on it: project_purchase_stock, project_stock_account, project_stock_landed_costs (via project_stock_account), sale_project_stock, sale_project_stock_account (via project_stock_account) (grep of manifests).

## G. Not verified
- Whether the picking project link is copied to stock moves and their valuation entries beyond analytic distribution: UNKNOWN — EVIDENCE INSUFFICIENT.
- Amounts and accounts posted by analytic entries and effect on project profitability report: UNKNOWN — EVIDENCE INSUFFICIENT (bridge modules only sampled).
- No tests exist in project_stock (no tests directory).

