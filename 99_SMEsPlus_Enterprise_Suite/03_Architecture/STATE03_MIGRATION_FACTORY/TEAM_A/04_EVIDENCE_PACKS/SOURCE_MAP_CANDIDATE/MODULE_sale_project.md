# Source Map (candidate) — `sale_project`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_project` |
| Display name | Sales - Project |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `83109f074e7ff57e` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_project/` |
| auto_install / application | ['sale_management', 'project_account'] / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_management`, `sale_service`, `project_account`
- Direct dependents in 300-module list (6): `project_mrp_sale`, `project_sale_expense`, `sale_project_stock`, `sale_project_stock_account`, `sale_purchase_project`, `sale_timesheet`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / Task Generation from Sales Orders
- Inventory of user-facing artifacts (counts): menu items 0, views 28, window actions 9, server actions 1, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (16): `project.template.create.wizard`, `account.move`, `sale.order`, `project.update`, `account.move.line`, `sale.order.line`, `product.template`, `product.product`, `project.task.recurrence`, `project.task.type`, `sale.order.template.line`, `project.task`, `project.project`, `project.milestone`, `report.project.task.user`, `sale.report`
- Company-dependent settings introduced: 3 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `project.template.create.wizard`, `account.move`, `sale.order`, `project.update`, `account.move.line`, `sale.order.line`, `product.template`, `product.product`, `project.task.recurrence`, `project.task.type`, `sale.order.template.line`, `project.task`, `project.project`, `project.milestone`, `report.project.task.user`, `sale.report`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 2 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 0); access rows 4

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 67 of 67 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — sale_project
Source revision: 19.0.post20260921 | Module: "Sales - Project" — task generation from sales orders (sale_project/__manifest__.py:4-5) | depends: sale_management, sale_service, project_account (:12) | auto_install when sale_management AND project_account are present (:13) | LGPL-3 (:48)
Basis: static reading of manifest, init hooks, security, and models sale_order(_line), product_template/product, project_project (key parts), project_task, project_milestone, account_move(_line), wizard; test names listed (about 2,000-line main test + milestone/reinvoice/multicompany tests), a few tests read.

## A. Capabilities and optionality
- A1. A service product sold on an order can create, on confirmation: a task in a chosen existing project ("Task"), a new project with a task per line ("Project & Task"), or an empty new project ("Project"); optionally from a project template and a task template. sale_project/models/product_template.py:22-43; sale_project/models/sale_order_line.py:336-436
- A2. Billable projects/tasks: a project can be flagged billable, linked to a sales order item; tasks and timesheets then point to a sales line for invoicing. sale_project/models/project_project.py:27-35; sale_project/models/project_task.py:25-38
- A3. Milestone-based invoicing: service policy "Based on Milestones" makes delivered quantity follow reached milestones; option offered only when the milestones feature is enabled. sale_project/models/product_template.py:11-20; sale_project/models/sale_order_line.py:71-101
- A4. Manual creation of a project from a confirmed order ("Create a Project" wizard), project/task smart buttons, milestone view on the order. sale_project/models/sale_order.py:165-201,203-268; sale_project/wizard/project_template_create_wizard.py:45-67
- A5. Project profitability panel: revenue items from confirmed service sale lines, invoice items, and links to the sales order items. sale_project/models/project_project.py:541-660
- A6. Portal: task lists group/search by sales order item, order and invoice; project sharing knows the billable flag. sale_project/controllers/portal.py:9-45
- A7. On first installation an init step flags existing projects that carry sales-related data (or have tasks needing it) as billable; on uninstall two embedded project actions are disabled. sale_project/__init__.py:9-27

## B. Objects, relationships, lifecycle
- B1. Service policies map to invoicing settings: prepaid/fixed price = invoice on ordered quantity; delivered manual = on delivered quantity (manual); delivered milestones = on delivered quantity with milestone type. sale_project/models/product_template.py:91-107
- B2. Product links (project, project template, task template) are per company. Task template must belong to the chosen global project. sale_project/models/product_template.py:33-43,56-60
- B3. Confirmation flow: for each service line with a tracking type, generate project/task; done in the order's company context; orders of several companies confirmed together are handled one by one. sale_project/models/sale_order.py:138-149
- B4. Rules of generation: skips optional lines with zero quantity; one project per order for lines without template and one per (order, template) otherwise; later lines attach to the existing project; the first generated project becomes the order's project if none. Re-confirming a cancelled/reset order reuses existing project/task. sale_project/models/sale_order_line.py:336-414
- B5. Global-project tasks: use the product's project else the order's project; error "A project must be defined..." if neither; no task for zero-quantity lines; task template used at most once per template per pass. sale_project/models/sale_order_line.py:416-436
- B6. Project created from a line: name from customer reference/order name (plus product/template name), analytic account = the order project's account or a new one, billable, company of the line, default stages (To Do, In Progress, Done, Cancelled) created if none, order recorded as re-invoiced order. sale_project/models/sale_order_line.py:182-245
- B7. Task created from a line: name (prefixed by order name unless project has a sale item), allocated hours = ordered quantity (0 for milestone type), customer, order and line links, unassigned. sale_project/models/sale_order_line.py:252-279. Quantity change on a service line updates the task's allocated hours; adding quantity to a zero-quantity line triggers generation. sale_project/models/sale_order_line.py:151-166. (TEST) sale_project/tests/test_sale_project.py:1555-1660,1916
- B8. Chatter: order gets "Task Created" note for lines created on a confirmed order; task gets "created from order" note. sale_project/models/sale_order_line.py:136-139,323-327
- B9. Milestones: for milestone-type lines the project's milestone feature is switched on; unassigned milestones are linked and share the quantity equally, else a 100% milestone named after the line is created (and set on the task for Project & Task). Delivered quantity = sum of reached-milestone percentages x ordered quantity. sale_project/models/sale_order_line.py:85-101,438-457; sale_project/models/project_milestone.py:30-50. (TEST) sale_project/tests/test_so_line_milestones.py:84-118
- B10. Task billing link (sale item): defaults from parent task (same customer), milestone, or project; cleared when the project is not billable; sale order follows the item; if the customer no longer matches the order's partner set, order and item are cleared. sale_project/models/project_task.py:72-131
- B11. Setting a sales item on a project or task auto-confirms a draft quotation containing it (orders created from project/task are confirmed on save). sale_project/models/project_project.py:166-197; sale_project/models/project_task.py:155-186; sale_project/models/sale_order.py:270-284
- B12. Cancelling an order clears the sale item on projects pointing to its lines. sale_project/models/sale_order.py:286-291. (TEST) sale_project/tests/test_sale_project.py:267-289
- B13. Project non-billable -> project customer cleared; customer changed and no longer matching the sale item -> sale item cleared. sale_project/models/project_project.py:69-83
- B14. Duplicating an order does not duplicate its project (fields not copied); duplicated projects drop task sale items. sale_project/models/sale_order_line.py:11-16; sale_project/models/project_project.py:64-67. (TEST) sale_project/tests/test_sale_project.py:1129
- B15. Analytic: default analytic distribution of a line adds the project's account(s) missing from its plans, using the product project, order project or context project. sale_project/models/sale_order_line.py:103-124. Invoice line falls back to the task/project account, or to the single project account found for the line. sale_project/models/sale_order_line.py:459-480
- B16. Vendor-bill/other analytic lines whose analytic accounts match a project's are mapped to the order of that project (oldest confirmed first) for re-invoicing. sale_project/models/account_move_line.py:35-81. (TEST) sale_project/tests/test_reinvoice.py:50-484

## C. Validations, security, multi-company
- C1. Product constraints: no project/template when tracking is "none"; no template for "task in global project"; no global project for the project-creating options; switching a product away from service resets tracking and project. sale_project/models/product_template.py:115-145
- C2. Task sale item must be a service line and not a re-invoiced expense. sale_project/models/project_task.py:144-153
- C3. Expense lines never generate project/task. sale_project/models/sale_order_line.py:129-131
- C4. Product of a confirmed service line can't be changed. sale_project/models/sale_order_line.py:64-69
- C5. Order project selectable only if billable and not a template. sale_project/models/sale_order.py:35-36
- C6. ACLs: project users and managers read sales orders; project managers also read order lines. sale_project/security/ir.model.access.csv:2-5. Rule: project managers see only confirmed service lines that have a project or task (read-only). sale_project/security/sale_project_security.xml:4-13
- C7. Generation and project/task creation run with elevated rights because salespeople may lack project access; the visible project list is filtered by read access. sale_project/models/sale_order.py:145,153; sale_project/models/sale_order_line.py:134,317-320; sale_project/models/sale_order.py:134
- C8. Group-gated fields: tasks/projects on the order need project user (milestone option: milestone group); "To invoice" on task needs the sales group with all leads; the re-invoiced order needs salesman. sale_project/models/sale_order.py:23-34; sale_project/models/project_task.py:37; sale_project/models/project_project.py:37-40,45
- C9. Multi-company: the project takes the company of the line; when the only project comes from a template, the project takes the template's company; the wizard passes the order's company; portal/access tested for a project in another company. sale_project/models/sale_order_line.py:191; sale_project/models/sale_order.py:151-159. (TEST) sale_project/tests/test_sale_project_multicompany_access.py:1-71; sale_project/tests/test_sale_project.py:858-945
- C10. Task partner must match the order's customer set (customer, invoice or delivery, commercial partner). sale_project/models/project_task.py:82-91,101-112

## D. Handoffs
- D1. Owners: project/task/milestone/timesheet = project (and sale_timesheet for hours); order/line/invoicing = sale/account; analytic accounts and distribution = analytic/account; project cost & profitability items (bills, purchases) = project_account, project_purchase; stock re-invoice = sale_project_stock.
- D2. Invoicing: revenue only when the sale line has quantity to invoice or invoiced; expenses excluded; all service policies classified as service revenues. sale_project/models/project_project.py:541-555
- D3. Invoice creation from a project opens the order invoice wizard (default percentage down payment when nothing invoiceable). sale_project/models/project_project.py:320-329
- D4. Invoice list links open account invoices; bills through vendor bill action. sale_project/models/account_move.py:9-11; sale_project/models/project_project.py:882
- D5. Inventory: procurement values carry the project for stock. sale_project/models/sale_order_line.py:489-493

## E. Configuration that changes outcomes
- E1. Product: service tracking, service policy, project / project template / task template. sale_project/models/product_template.py:22-44
- E2. Project: billable flag, sale item, re-invoiced order, milestones feature, stages. sale_project/models/project_project.py:27-47
- E3. Order: order project (drives analytic default and global-project tasks). sale_project/models/sale_order.py:35-36
- E4. Context switch to disable generation. sale_project/models/sale_order.py:140. Export templates provided for services. sale_project/data/sale_project_data.xml:10-62

## F. Effective extension path (modules)
- Depended on by: project_mrp_sale, project_sale_expense, sale_project_stock, sale_project_stock_account, sale_purchase_project, sale_timesheet (manifest grep). Same hooks overridden in sale_timesheet (generation, hours conversion, delivered quantity).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: project_project.py profitability item building beyond the domain (lines 557-840 skimmed), views and JS panel, sale_project_portal_templates, and the demo data.

