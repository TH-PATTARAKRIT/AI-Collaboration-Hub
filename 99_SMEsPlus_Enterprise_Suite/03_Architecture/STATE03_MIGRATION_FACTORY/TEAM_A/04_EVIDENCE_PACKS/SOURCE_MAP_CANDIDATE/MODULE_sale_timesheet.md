# Source Map (candidate) — `sale_timesheet`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_timesheet` |
| Display name | Sales Timesheet |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `ebf995fac3ccb15e` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_timesheet/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_project`, `hr_timesheet`
- Direct dependents in 300-module list (2): `sale_timesheet_margin`, `spreadsheet_dashboard_sale_timesheet`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_main_flows`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / Sell based on timesheets
- Inventory of user-facing artifacts (counts): menu items 1, views 37, window actions 7, server actions 0, reports 2, mail templates 0, scheduled jobs 0, wizards 3, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `project.sale.line.employee.map` (Project Sales line, employee mapping)
- Objects extended from other modules (15): `sale.advance.payment.inv`, `account.move`, `account.analytic.line`, `sale.order`, `account.move.line`, `sale.order.line`, `product.template`, `product.product`, `account.move.reversal`, `hr.employee`, `project.task`, `res.config.settings`, `project.project`, `report.project.task.user`, `timesheets.analysis.report`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `sale.advance.payment.inv`, `account.move`, `account.analytic.line`, `sale.order`, `account.move.line`, `sale.order.line`, `product.template`, `product.product`, `account.move.reversal`, `hr.employee`, `project.task`, `res.config.settings`, `project.project`, `report.project.task.user`, `timesheets.analysis.report`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 70 of 70 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: sale_timesheet (Odoo 19 Community, revision 19.0.post20260921)
Pointers are module-relative. (TEST) = derived from module tests only.

## A. Capabilities; core / optional / conditional
- Purpose: sell service time and bill it from recorded timesheets; sets the sales order item on each timesheet so delivered quantity is real. sale_timesheet/__manifest__.py:8-15
- Depends on sale_project and hr_timesheet; installs automatically when both are present (bridge, not a stand-alone app). sale_timesheet/__manifest__.py:16,38
- Adds a new service invoicing policy "Based on Timesheets" (delivered quantity from time) next to prepaid/manual/milestone policies. sale_timesheet/models/product_template.py:12-19; maps to (invoice on delivery, service type timesheet); prepaid maps to (order, timesheet). sale_timesheet/models/product_template.py:71-76
- Ships one protected master product "Service on Timesheets" (hourly, timesheet policy, list price 40). sale_timesheet/data/sale_service_data.xml:4-12; cannot be deleted, archived or company-restricted. sale_timesheet/models/product_template.py:98-110
- Three project pricing modes: task rate, project rate (fixed rate), employee rate; only for billable projects. sale_timesheet/models/project_project.py:29-36,81-91
- Optional billing period on the invoice wizard (start/end date) to bill only timesheets in a period. sale_timesheet/wizard/sale_make_invoice_advance.py:10-16,33-50
- Upsell activity for prepaid services once delivered time passes a threshold (default 100%). sale_timesheet/models/product_template.py:23; sale_timesheet/models/sale_order.py:50-67,94-113
- Portal: customers see timesheets on invoices and sales orders; search/group by order item and invoice. sale_timesheet/controllers/portal.py:19-31,60-81,126-137
- Reports: timesheet analysis extended with revenue, margin, billable/non-billable time; task report shows remaining hours on order. sale_timesheet/report/timesheets_analysis_report.py:12-19,34-47; sale_timesheet/report/project_report.py:9-24
- Conditional: "Time Billing" and "Invoice Policy" settings block appears in Timesheet settings; the Invoice Policy switch is an upgrade-style toggle (backing feature not in this tree). sale_timesheet/views/res_config_settings_views.xml:10-18; sale_timesheet/models/res_config_settings.py:10. Its effect: UNKNOWN — EVIDENCE INSUFFICIENT.
- Milestone policy only offered when the milestone feature group is enabled (parent module). sale_project/models/product_template.py:18-19
- Sales-order-item fields on timesheet views are shown only to sales salesman group. sale_timesheet/views/hr_timesheet_views.xml:45,60-61
- Installing implies the unit-of-measure feature for all internal users. sale_timesheet/data/sale_service_data.xml:15-17
- Post-install step: existing manual-type, order-invoiced service products (with project/task tracking or none) are converted to the timesheet type. sale_timesheet/__init__.py:13-23

## B. Business objects, relationships, lifecycle
- Timesheet line (analytic line with project) gains: order item (so_line), billable type, invoice link, "order item manually edited" flag, order (stored for portal grouping). sale_timesheet/models/hr_timesheet.py:35-46
- Order item resolution (when not manually edited and not yet billed): no task -> employee mapping (employee-rate projects) then project's item; task with billing allowed -> task's item for task-rate/fixed-rate; employee-rate -> mapping entry matching employee and customer, else task's item; otherwise none. sale_timesheet/models/hr_timesheet.py:79-82,117-144
- Billable type classification: none item -> non-billable (or manual if project billed manually); delivery+timesheet policy -> billed on timesheets (revenue type when amount and hours positive); delivery other -> milestones/manual/fixed; order policy -> fixed price. sale_timesheet/models/hr_timesheet.py:53-69
- Project-mapping object employee -> order item with hourly cost override; one entry per employee per project. sale_timesheet/models/project_sale_line_employee_map.py:22-44,77-82
- Project pricing type is derived: mapping present -> employee rate; project item present -> project rate; else task rate; non-billable -> none. sale_timesheet/models/project_project.py:81-91
- Task: default customer item = latest service item of that customer with remaining hours; remaining hours on order shown per task. sale_timesheet/models/project_task.py:37-56,79-84,96-112
- Delivered quantity of a timesheet-method order line = sum of its timesheets (project-bound). sale_timesheet/models/sale_order_line.py:62-88
- Billing lifecycle: creating invoices from a sale order links eligible timesheets to the draft invoice. sale_timesheet/models/sale_order.py:156-163; sale_timesheet/models/account_move.py:69-92
  - Deleting a draft invoice line releases the timesheets without re-allocating their item. sale_timesheet/models/account_move_line.py:28-58
  - Posting a credit note on a reversed invoice releases that invoice's timesheets for that item. sale_timesheet/models/account_move.py:99-108
  - "Reverse and modify" re-links timesheets to the new invoice per order item. sale_timesheet/models/account_move_reversal.py:7-26
  - Timesheet counts as unbilled if no invoice, or invoice cancelled (unless imported from legacy invoicing state). sale_timesheet/models/hr_timesheet.py:95-97
- Period invoicing: quantity to invoice recomputed for the period from unbilled or credited timesheets, capped at delivered minus invoiced when credit notes exist. sale_timesheet/models/sale_order_line.py:150-196 ; (TEST) sale_timesheet/tests/test_sale_timesheet.py:1586-1614

## C. Validations, automation, security, multi-company
- Billable project must point to a service item that is not from expense/vendor bill. sale_timesheet/models/project_project.py:161-167
- Invoiced timesheets (non-cancelled invoice) cannot change hours, employee, project, task, item, date when item is delivery-based. sale_timesheet/models/hr_timesheet.py:102-107
- Timesheet with a posted invoice cannot be deleted. sale_timesheet/models/hr_timesheet.py:176-179
- Turning off "billable" on a project clears items on its unbilled timesheets; moving a timesheet to a non-billable project clears item and edited flag. sale_timesheet/models/project_project.py:169-175; sale_timesheet/models/hr_timesheet.py:109-115; (TEST) sale_timesheet/tests/test_sale_timesheet.py:1883-1911
- Manually edited item is preserved when the task's item changes. (TEST) sale_timesheet/tests/test_edit_so_line_timesheet.py:19-60
- Employee mapping uniqueness per project. sale_timesheet/models/project_sale_line_employee_map.py:41-44
- Order created with employee-mapping context must contain a service line; it is auto-confirmed without task generation. sale_timesheet/models/sale_order.py:74-81
- Required analytic plans: if the order item's distribution lacks a mandatory plan, timesheet creation is blocked; otherwise accounts come from the item's distribution, with project account as fallback. sale_timesheet/models/hr_timesheet.py:230-264
- Upsell: activity created when order confirmed, has salesperson (order or customer), a prepaid service item is over threshold and not yet warned; one warning per item until fully delivered again. sale_timesheet/models/sale_order.py:54-67,94-113,150-154; (TEST) sale_timesheet/tests/test_upsell_warning.py:11-333
- Security: employee-mapping object readable by all internal users, full edit for project managers. sale_timesheet/security/ir.model.access.csv:2-3
- Two accounting record rules on analytic lines are narrowed to non-project lines so timesheet-specific rules govern timesheets; uninstall restores them to open. sale_timesheet/security/sale_timesheet_security.xml:11-16; sale_timesheet/__init__.py:9-11
- Timesheet visibility rules (own lines for user group, all for approver/manager) belong to hr_timesheet. hr_timesheet/security/hr_timesheet_security.xml:50-80
- Multi-company: employee-mapping lookup picks the entry of the active company's employee, else another allowed company; employee company can be defaulted from the project. sale_timesheet/models/hr_timesheet.py:181-192; sale_timesheet/models/hr_employee.py:9-15; (TEST) sale_timesheet/tests/test_so_line_determined_in_timesheet.py:240-325
- Product/project pickers restricted to same or no company. sale_timesheet/models/product_template.py:21-22. Analytic account company follows customer's company. sale_timesheet/models/project_project.py:520-529
- Portal reads timesheets in elevated mode for invoice/order pages; task portal fields extended with remaining hours. sale_timesheet/controllers/portal.py:29,136; sale_timesheet/models/project_task.py:30-35

## D. Accounting / inventory / analytic handoffs
- Invoice creation, posting, payment: account (invoice) and sale (order); this module only links timesheets and computes quantities. sale_timesheet/models/sale_order.py:156-163
- Analytic cost of a timesheet: hr_timesheet (analytic line amount); hourly cost may be overridden by the employee-mapping cost on employee-rate projects. sale_timesheet/models/hr_timesheet.py:194-199
- Accrued revenue: quantity delivered respects an accrual cut-off date supplied by the accrual wizard (account). sale_timesheet/models/sale_order_line.py:83-88; (TEST) sale_timesheet/tests/test_sale_timesheet_accrued_entries.py:43-134
- Project profitability: timesheet amounts merged into revenue (invoiced) and cost sections by billable type; vendor-bill analytic lines excluded to avoid double count; costs are negative amounts. sale_timesheet/models/project_project.py:381-483
- No inventory handoff in this module.

## E. Configuration that changes outcomes
- Product service policy and unit of measure (timesheet products default to hour unit). sale_timesheet/models/product_template.py:52-69
- Project: billable flag, pricing mode, project item, employee mapping, timesheet product default, billing type "billed manually", allocated hours. sale_timesheet/models/project_project.py:37-71,114-121,157-159
- Company timesheet encoding unit (hour/day) affects displayed remaining time, totals, and cost display. sale_timesheet/models/sale_order_line.py:20-43; sale_timesheet/models/sale_order.py:35-48
- Upsell threshold on product (default 1). sale_timesheet/models/product_template.py:23
- Invoice wizard period dates. sale_timesheet/wizard/sale_make_invoice_advance.py:10-16

## F. Effective extension path (grep of _inherit)
- Dependents in this tree: sale_timesheet_margin (inherits sale.order.line), spreadsheet_dashboard_sale_timesheet, test_main_flows (manifest depends only).
- Extension hooks other modules may use: validated-timesheet domain, period date range, profitability sections. sale_timesheet/models/sale_order_line.py:83-85; sale_timesheet/models/account_move.py:94-97

## G. Not verified
- Effect of the Invoice Policy setting: UNKNOWN — EVIDENCE INSUFFICIENT
- Timesheet validation (approval) feeding delivered quantity: UNKNOWN — EVIDENCE INSUFFICIENT (hook exists, no implementation in Community)
- Demo data (sale_service_demo.xml) not analysed; report SQL joins not verified beyond selects.

