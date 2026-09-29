# Source Map (candidate) — `project_purchase`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project_purchase` |
| Display name | Project Purchase |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G06 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `54538558d094103b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project_purchase/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `purchase`, `project_account`
- Direct dependents in 300-module list (2): `project_purchase_stock`, `sale_purchase_project`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Services/Project / Monitor purchase in project
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `purchase.order.line`, `purchase.order`, `project.project`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `purchase.order.line`, `purchase.order`, `project.project`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 33 of 33 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — project_purchase
Source revision: 19.0.post20260921 | Module: "Project Purchase" (project_purchase/__manifest__.py:5) | depends: purchase, project_account (:9) | License LGPL-3 (:24)
Basis: static reading of 3 models, 1 controller, 2 views; 2 test files scanned (test names and assertions).

## A. Capabilities and optionality
- A1. Lets a purchase order (PO) be linked to a project; the project then lists its purchase orders, shows a count, and includes purchase spending in its profitability panel. project_purchase/models/purchase_order.py:9; project_purchase/models/project_project.py:12,48-75,139-217
- A2. Conditional: bridge module, installed automatically when purchase and project_account are present. project_purchase/__manifest__.py:22
- A3. Count/button/tabs on the project are shown only to purchase users; the project field on the PO form only to project users. project_purchase/models/project_project.py:12,108; project_purchase/views/project_project.xml:10,20; project_purchase/views/purchase_order.xml:10
- A4. Product catalog on the PO passes the project through so lines added from the catalog receive the project's analytics. project_purchase/controllers/catalog.py:9-22
- A5. Two embedded project tabs "Purchase Orders" (task action and updates action). project_purchase/views/project_project.xml:3-21

## B. Business objects, relationships, lifecycle
- B1. PO (purchase.order, owner purchase) gets optional project link (templates excluded). project_purchase/models/purchase_order.py:9
- B2. PO line analytic distribution: when the order has a project (or a project is passed from the catalog), the project's analytic accounts are added to each line's existing distribution for any plan not yet used; if a line has no distribution, the project's own distribution is applied. project_purchase/models/purchase_order_line.py:9-29 (TEST: tests/test_project_purchase.py:35-74 - accounts from distribution models and the project account coexist; lines added later receive the same result)
- B3. After creation of lines the distribution is recomputed so the project is reflected immediately. project_purchase/models/purchase_order_line.py:31-35
- B4. Project purchase count = orders linked via the project field that have lines, plus orders (not already counted) whose lines carry the project's analytic account; projects with no analytic account count only linked orders. project_purchase/models/project_project.py:14-42 (TEST: tests/test_project_purchase.py:76-121, counts 3 and 2)
- B5. Opening the list gives every PO with a line on the project's account or linked directly; if exactly one, opens the form (unless from the embedded tab). project_purchase/models/project_project.py:48-75
- B6. Profitability, PO lines on confirmed orders whose distribution includes the project account: cost = line subtotal (converted to the project currency) x the account's share; "billed" = posted vendor bill lines, "to bill" = draft bill lines plus remainder not yet billed; refunds subtract; cancelled bills ignored. project_purchase/models/project_project.py:141-199 (TEST: tests/test_project_profitability.py:206-300 to-bill then billed figures follow invoice draft/posted state)
- B7. Vendor bill lines with the project account that are not tied to a PO line are shown in a second section; the drop-out of already-counted invoice lines prevents double counting. project_purchase/models/project_project.py:146,210-216 (TEST: tests/test_project_profitability.py:31-90, 382-573 sections "purchase_order" and "other_purchase_costs")
- B8. Analytic lines coming from purchase invoice lines are excluded from the generic analytic-line cost section so PO-related spend is not counted twice. project_purchase/models/project_project.py:120-124
- B9. No state machine of its own; PO states/invoice status come from purchase (TEST: invoice_status "to invoice" then "invoiced" in tests/test_project_profitability.py:201,365).

## C. Validations, security, multi-company
- C1. No constraints raised by this module. (none found in module)
- C2. Profitability searches run with elevated rights; the drill-down link is offered only to purchase users, invoicing users or accounting read-only users. project_purchase/models/project_project.py:142,147-151
- C3. Drill-down action opens list/form with create and edit disabled. project_purchase/models/project_project.py:85-88
- C4. No new access files or rules. project_purchase/__manifest__.py:12-15
- C5. Multi-company: amounts converted at the project company's rate; test with foreign-currency POs confirms conversion. project_purchase/models/project_project.py:156,176 (TEST: tests/test_project_profitability.py:382-573). Cross-company guard on PO-project link: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs
- D1. Purchasing (RFQ, confirmation, receiving, bills): purchase / account. Analytic account per project, cost items skeleton, non-PO bill section helper: project / project_account (project_account/models/project_project.py:31).
- D2. Stock receipt valuation to project: project_stock_account (separate module). Not here.
- D3. Sales-side re-billing of purchase: sale_purchase_project (see F2), not read.

## E. Configuration/defaults that change outcomes
- E1. Project must have an analytic account for PO spend to appear in profitability (guarded by "if account"). project_purchase/models/project_project.py:141
- E2. Analytic distribution models (product/partner rules) merge with the project account (B2); order of plan roots decides whether the project account is added. project_purchase/models/purchase_order_line.py:18-27
- E3. Only PO lines in state "purchase" feed profitability; the state filter is written as a plain value not a list. project_purchase/models/project_project.py:144 (effect on locked/done orders: see G2)

## F. Effective extension path (grep of _inherit)
- F1. This module extends: project.project, purchase.order.line, purchase.order, and the product catalog controller. project_purchase/models/*.py; project_purchase/controllers/catalog.py:7
- F2. Modules depending on project_purchase: project_purchase_stock, sale_purchase_project.

## G. Not verified
- G1. UNKNOWN — EVIDENCE INSUFFICIENT: helper `_add_purchase_items` deliberately returns nothing (compatibility stub); reason not stated. project_purchase/models/project_project.py:126-127
- G2. UNKNOWN — EVIDENCE INSUFFICIENT: whether locked ("done") POs are included given the filter form at :144.
- G3. UNKNOWN — EVIDENCE INSUFFICIENT: multi-company record rules governing PO/project visibility (not in this module).

