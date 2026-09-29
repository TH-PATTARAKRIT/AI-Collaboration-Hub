# Source Map (candidate) — `purchase`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `purchase` |
| Display name | Purchase |
| Manifest version | 1.2 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G03 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `a34441e3d1ebff54` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/purchase/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `account`
- Direct dependents in 300-module list (6): `project_purchase`, `purchase_edi_ubl_bis3`, `purchase_product_matrix`, `purchase_requisition`, `purchase_stock`, `sale_purchase`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `l10n_din5008_purchase`
- Custom / third-party modules that declare a dependency (name — license only) (18): `scgl_product_image` — no-license, `scgl_jasper_api` — LGPL-3, `19_bhpro_purchase_ext` — OPL-1, `cr_effective_date_entries` — AGPL-3, `purchase_discount_catalog` — OPL-1, `scgl_purchase_advance_payment` — LGPL-3, `purchase_request_level_approve_po` — LGPL-3, `purchase_hide_line_buttons` — OPL-1, `scgl_advance_expense_request` — LGPL-3, `purchase_order_lines_discount` — AGPL-3, `bh_purchase_receipt_all` — LGPL-3, `import_bridge_axis` — OPL-1

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Purchase / Purchase orders, tenders and agreements
- Inventory of user-facing artifacts (counts): menu items 17, views 40, window actions 12, server actions 4, reports 2, mail templates 3, scheduled jobs 1, wizards 2, web routes 5
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (6): `bill.to.po.wizard` (Bill to Purchase Order); `purchase.order.line` (Purchase Order Line); `purchase.order` (Purchase Order); `purchase.bill.line.match` (Purchase Line and Vendor Bill line matching view); `purchase.report` (Purchase Report); `purchase.bill.union` (Purchases & Bills Union)
- Objects extended from other modules (18): `account.tax`, `ir.actions.report`, `analytic.mixin`, `portal.mixin`, `product.catalog.mixin`, `mail.thread`, `mail.activity.mixin`, `account.document.import.mixin`, `account.move`, `account.move.line`, `res.company`, `product.template`, `product.product`, `product.supplierinfo`, `res.config.settings`, `account.analytic.applicability`, `account.analytic.account`, `res.partner`
- Company-dependent settings introduced: 3 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `purchase.order.line` ← Community: `project_purchase`, `purchase_mrp`, `purchase_product_matrix`, `purchase_requisition`, `purchase_requisition_stock`, `purchase_stock`, `sale_purchase`, `sale_purchase_stock`, `stock_dropshipping`, `stock_landed_costs`; open-license custom/third-party scanned: `order_line_sequence`, `purchase_order_lines_discount`, `purchase_request`, `scgl_purchase_advance_payment`, `smesplus_purchase_advance_payment`
- `purchase.order` ← Community: `mrp_subcontracting_dropshipping`, `mrp_subcontracting_purchase`, `project_purchase`, `project_purchase_stock`, `purchase_edi_ubl_bis3`, `purchase_mrp`, `purchase_product_matrix`, `purchase_repair`, `purchase_requisition`, `purchase_requisition_stock` … (+4); open-license custom/third-party scanned: `bh_purchase_receipt_all`, `courier_type`, `purchase_request`, `purchase_request_level_approve_po`, `scgl_jasper_api`
- `purchase.report` ← Community: `purchase_stock`; open-license custom/third-party scanned: `courier_type`
- This module's own extension of other modules' objects: `account.tax`, `ir.actions.report`, `analytic.mixin`, `portal.mixin`, `product.catalog.mixin`, `mail.thread`, `mail.activity.mixin`, `account.document.import.mixin`, `account.move`, `account.move.line`, `res.company`, `product.template`, `product.product`, `product.supplierinfo`, `res.config.settings`, `account.analytic.applicability`, `account.analytic.account`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: `purchase.order` → ['draft', 'sent', 'to approve', 'purchase', 'cancel']; `purchase.report` → ['draft', 'sent', 'to approve', 'purchase', 'cancel']
- Validation: 1 declarative constraint method(s), 2 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Purchase reminder every 1 days
- Security: groups declared 5 (`group_purchase_user`, `group_purchase_manager`, `group_warning_purchase`, `group_send_reminder`, `base.default_user_group`); record rules 8 (of which company-scoped by text 4); access rows 35

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 106 of 107 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map Trace Note: `purchase`

- Source revision: `19.0.post20260921` (Odoo 19 Community, addons root `odoo/addons`)
- Method: read-only static reading of source + bundled tests. No code copied. No runtime executed.
- Pointer convention: `path:LINE` relative to the addons root. `(TEST)` = derived from a bundled test, not from production code.
- Skeleton used for orientation only: `sourcemap/purchase.json`.

## 1. Capabilities and classification

| Capability | Class | Pointer |
|---|---|---|
| Module is an application; depends only on `account` (no `auto_install`) | CORE | purchase/__manifest__.py:5-14,52-53 |
| RFQ / Purchase Order document with lines, taxes, currency, payment terms, incoterm, buyer, priority | CORE | purchase/models/purchase_order.py:21-26,88-160 |
| Vendor bill creation from PO lines; bill-to-PO linking by line | CORE | purchase/models/purchase_order.py:760; purchase/models/account_invoice.py:523-535 |
| Manual received-quantity entry (only receiving mechanism in this module alone) | CORE | purchase/models/purchase_order_line.py:225-238,251-258 |
| Bill control policy per product (bill on ordered vs received qty) | CORE | purchase/models/product.py:14-30; purchase/models/purchase_order_line.py:171-184 |
| Send RFQ/PO by email, print, portal view, vendor acknowledgement, vendor date update | CORE | purchase/models/purchase_order.py:545,601; purchase/controllers/portal.py:144-196 |
| Merge multiple RFQs of same vendor | CORE | purchase/models/purchase_order.py:835 |
| Down payment lines (PO line flagged as down payment) | CORE | purchase/models/purchase_order.py:724-758; purchase/wizard/bill_to_po_wizard.py:43 |
| Bill-line matching workbench (PO lines vs unlinked vendor bill lines) | CORE (read-only SQL view + actions) | purchase/models/purchase_bill_line_match.py:83-135,163,202 |
| Purchase analysis report; bill-union picker view | CORE (report views) | purchase/report/purchase_report.py:13-16; purchase/report/purchase_bill.py:8-46 |
| Dashboard (draft / sent / late / not acknowledged counters, days to order) | CORE | purchase/models/purchase_order.py:977 |
| Double approval (two levels) | OPTIONAL: company setting `po_double_validation` default one step | purchase/models/res_company.py:15-19; purchase/models/res_config_settings.py:12-13 |
| Lock confirmed orders | OPTIONAL: company setting `po_lock` default `edit` | purchase/models/res_company.py:9-13 |
| Daily vendor receipt-reminder email | CONDITIONAL: group `group_send_reminder` (implied for all internal users, setting default True) + per-vendor flag + PO not acknowledged | purchase/security/purchase_security.xml:30-38; purchase/models/res_config_settings.py:19; purchase/models/purchase_order.py:1064,1134 |
| Purchase warnings on vendor/product | OPTIONAL: group `group_warning_purchase` | purchase/security/purchase_security.xml:26; purchase/models/res_config_settings.py:16 |
| Purchase agreements | OPTIONAL: installs `purchase_requisition` | purchase/models/res_config_settings.py:17 |
| Grid entry | OPTIONAL: installs `purchase_product_matrix` | purchase/models/res_config_settings.py:18 |
| 3-way matching switch (`module_account_3way_match`) | OPTIONAL toggle; target module absent from Community tree (`account_3way_match` not found), UI widget is an upgrade prompt | purchase/models/res_config_settings.py:16; purchase/views/res_config_settings_views.xml:43 |

## 2. Business objects, relationships, lifecycle

- `purchase.order` (PO): header; one-to-many `purchase.order.line`; many bills linked indirectly through bill lines (purchase/models/purchase_order.py:71-76,111-113).
- `purchase.order.line`: carries ordered qty, received qty, invoiced qty, qty-to-invoice, tax, price, date planned; links to bill lines via `invoice_lines` (purchase/models/purchase_order_line.py:171-217).
- `account.move.line.purchase_line_id`: the single link from a vendor bill line to a PO line, nullified if PO line is removed (purchase/models/account_invoice.py:528).
- Read-only projections: `purchase.bill.line.match`, `purchase.bill.union`, `purchase.report` (SQL views, not business documents).
- Transient: `bill.to.po.wizard` (purchase/wizard/bill_to_po_wizard.py:6-11).

PO states (purchase/models/purchase_order.py:105-111): `draft`(RFQ) -> `sent`(RFQ Sent) -> `to approve` -> `purchase`(PO) -> `cancel`.

| Transition | Trigger | Gate | Pointer |
|---|---|---|---|
| draft -> sent | Any chatter post/send with the RFQ-sent context flag, or Print quotation | none besides state = draft | purchase/models/purchase_order.py:479-483,611-613 |
| draft/sent -> purchase | Confirm | Every non-note line must have a product (unless down payment); analytic-distribution rules validated; vendor added to product vendor list; then approval test | purchase/models/purchase_order.py:625-639,657-668 |
| draft/sent -> to approve | Confirm when approval test fails | see approval rule below | purchase/models/purchase_order.py:637-638 |
| to approve -> purchase | Approve | approval test; UI button visible only to `group_purchase_manager` | purchase/models/purchase_order.py:615-619; purchase/views/purchase_views.xml:136 |
| any (draft, sent, to approve, purchase) -> cancel | Cancel | Blocked if order is locked; blocked if any linked bill is not cancelled/draft | purchase/models/purchase_order.py:641-649 |
| cancel -> draft | Set to draft | none | purchase/models/purchase_order.py:621-623 |
| delete | Delete | Only when state = cancel | purchase/models/purchase_order.py:408-411 |

- Approval rule (`_approval_allowed`): allowed if company is one-step; OR two-step AND order total is below the configured threshold (threshold converted from company currency to order currency at order date); OR current user is in `group_purchase_manager` (purchase/models/purchase_order.py:1251-1259).
- `button_approve` silently skips orders that fail the approval test (no error raised); a non-manager calling it leaves the order in `to approve` (purchase/models/purchase_order.py:615-617; (TEST) purchase/tests/test_access_rights.py:102-124).
- Default threshold 5000 (company currency) (purchase/models/res_company.py:19).
- Lock: `locked` is a separate flag, not a state. Approval sets it only if company `po_lock = lock`; Lock button is offered only in that mode; Unlock is offered to managers in UI (purchase/models/purchase_order.py:618,651-655; purchase/views/purchase_views.xml:146-147). A user-triggered lock/unlock also works with setting off (TEST purchase/tests/test_purchase.py:1075-1100). Server-side enforcement of manager-only unlock and of line read-only: UNKNOWN — EVIDENCE INSUFFICIENT (only view-level `groups`/`readonly` traced: purchase/views/purchase_views.xml:147,246).
- Billing status (computed, stored): `no` unless state = purchase; `to invoice` if any line has qty-to-invoice != 0; `invoiced` if all zero and at least one bill exists (purchase/models/purchase_order.py:47-68,127-131).
- Qty to invoice per line: only when PO is in `purchase`; product policy `purchase` -> ordered minus invoiced; otherwise received minus invoiced (purchase/models/purchase_order_line.py:176-182).
- Invoiced qty counts non-cancelled bills; vendor bills add, vendor refunds subtract, with UoM conversion (purchase/models/purchase_order_line.py:197-207).

## 3. Actions, constraints, automation, security

Actions and gates
- Create bill(s) from PO: builds draft vendor bill(s) with lines = qty-to-invoice; keeps only sections that have following lines; merges POs of same company+vendor+currency into one bill; converts to refund if total is negative; optionally attaches uploaded documents (single vendor only) (purchase/models/purchase_order.py:760-833).
- Bill header defaults from PO: partner, currency, fiscal position, payment term, bank account, narration, origin (purchase/models/purchase_order.py:925-945).
- Merge RFQs: only `draft`/`sent`; needs 2+ RFQs with same grouping key (vendor, currency, etc.) (purchase/models/purchase_order.py:835-857).
- Line edits: cannot delete a PO line of a confirmed PO (except section/note); type of a line cannot be changed; qty changes and received-qty changes on confirmed POs are logged to chatter (purchase/models/purchase_order_line.py:319-347,732-742).
- Add bill lines to a PO (wizard): creates/extends a PO from unlinked bill lines and immediately confirms it (subject to approval); or converts bill lines to down-payment lines (purchase/wizard/bill_to_po_wizard.py:13-77).
- Match workbench: with PO lines selected only -> creates draft vendor bill; with both PO and bill lines -> links by product, deletes unmatched selected bill lines, appends residual PO lines to the bill when exactly one bill is involved (purchase/models/purchase_bill_line_match.py:147-200). Rule that only same-vendor lines may be added to a PO: purchase/models/purchase_bill_line_match.py:202-222.
- Matching workbench population: confirmed PO lines with outstanding qty, plus draft/posted vendor bill lines without PO link (purchase/models/purchase_bill_line_match.py:83-132).
- Auto-fill bill from PO / previous bill (onchange) and OCR/EDI matching of PO references to bill lines (purchase/models/account_invoice.py:34-100,331-470).

Constraints
- Company consistency: product company must be accessible from PO company (purchase/models/purchase_order.py:184-198).
- Delete only when cancelled (purchase/models/purchase_order.py:408-411).
- Analytic distribution validated at confirmation via business domain `purchase_order` (purchase/models/purchase_order_line.py:745-752; purchase/models/analytic_applicability.py:6-15).
- SQL constraints: none found in the purchase models by skeleton (`sql_constraints: 0` for the PO models); other DB constraints: UNKNOWN — EVIDENCE INSUFFICIENT.

Automation and messaging
- Cron `Purchase reminder`: daily, runs as root, calls the reminder routine; per order sends the reminder template `reminder_date_before_receipt` days before expected arrival. Selection: state = purchase, vendor set, not acknowledged, order reminder flag on, not all-service (purchase/data/ir_cron_data.xml:2-11; purchase/models/purchase_order.py:1064-1082,1134-1142). Default lead is 1 day (purchase/data/purchase_data.xml:41). Reminder flags default from the vendor, per company (purchase/models/purchase_order.py:247-252; purchase/models/res_partner.py:41-44).
- Vendor changing planned dates on the portal creates/updates an activity for the buyer (purchase/models/purchase_order.py:1280-1294,1351-1378).
- Chatter subtypes RFQ Confirmed / Approved / Sent (purchase/data/purchase_data.xml:5-20; purchase/models/purchase_order.py:529-541). Bill creation/modification from a PO posts a chatter note on the bill (purchase/models/account_invoice.py:171-198).
- Order number from sequence `purchase.order`, prefix `P`, padding 5, company-independent (purchase/data/purchase_data.xml:22-28).
- Server action `Share` bound to the PO form (purchase/data/purchase_data.xml:31-39).
- Vendor is auto-added to the product's vendor list on confirmation when not present and list has <= 10 vendors (purchase/models/purchase_order.py:682-708).

Security
- Groups: `group_purchase_user` (implies internal user), `group_purchase_manager` (implies user); technical groups `group_warning_purchase`, `group_send_reminder` (purchase/security/purchase_security.xml:11-33).
- ACL: user and manager get full CRUD on PO and lines; accounting invoice group can read/write (no create); read-only accounting can read; portal read-only (purchase/security/ir.model.access.csv:2-14). Purchase users additionally receive read/write/create (and delete on moves) on vendor bills through ACL, restricted by rule to vendor bill/refund/receipt types (purchase/security/ir.model.access.csv:24-29; purchase/security/purchase_security.xml:63-74).
- Record rules: PO, PO line, report, bill-union scoped to `company_ids` (union also allows no-company rows); portal users see only POs of their commercial partner tree (purchase/security/purchase_security.xml:40-91).
- Multi-company: each PO belongs to one company; line company follows the PO; picking/valuation per company handled in `purchase_stock`. Cross-company product use is rejected (see constraint). Bill grouping keys include company (purchase/models/purchase_order.py:792-805).

## 4. Handoffs to other modules

| Handoff | Owner | Pointer |
|---|---|---|
| Vendor bill creation (draft) from confirmed PO lines | `purchase` writes; `account` owns the bill and posting | purchase/models/purchase_order.py:760-833 |
| Bill line -> PO line link (`purchase_line_id`) | field defined in `purchase` on `account.move.line`; used for invoiced-qty and analytic inheritance | purchase/models/account_invoice.py:528-556 |
| Invoiced qty / bill control policy feeding "Waiting Bills" status | `purchase` | purchase/models/purchase_order_line.py:171-207 |
| Receipt creation, received-qty from stock moves | NOT in `purchase`; owned by `purchase_stock` (in `purchase` alone received qty is manual, services and goods alike) | purchase/models/purchase_order_line.py:225-258; see purchase_stock note |
| Valuation / price-difference / GRNI accounting | NOT in `purchase`; owned by `purchase_stock` + `stock_account` | see purchase_stock note |
| 3-way match (PO/receipt/bill blocking) | Enterprise-only; `account_3way_match` not in Community tree | purchase/views/res_config_settings_views.xml:43 |
| Accrued expense at a past date (qty received/invoiced "at date") | `purchase` supplies figures; `account` accrual wizard consumes them | purchase/models/purchase_order_line.py:186-196,240-249,287-300 |
| Down payments | `purchase` creates negative/zero-qty PO lines flagged down payment linked to bill lines | purchase/models/purchase_order.py:724-758 |
| Vendor tax / fiscal position / payment terms | `account` data used at PO and bill creation | purchase/models/purchase_order.py:925-945 |
| E-invoicing/EDI import of bills into PO | `account.document.import.mixin` on PO; UBL builder in `purchase_edi_ubl_bis3` | purchase/models/purchase_order.py:23,1401-1417 |
| Portal (vendor view, acknowledge, update dates) | `purchase` controllers; token or portal-user access | purchase/controllers/portal.py:144-196 |

## 5. Configuration and computed behavior that changes outcomes

- Company: `po_double_validation` (one_step default / two_step), `po_double_validation_amount` (default 5000), `po_lock` (edit default / lock) (purchase/models/res_company.py:9-19). Settings wizard maps checkboxes to these values (purchase/models/res_config_settings.py:37-44).
- Product: `purchase_method` (bill on ordered vs received). Computed default: services -> ordered; other types -> the template default value (stored, editable) (purchase/models/product.py:14-30). Determines when "Waiting Bills" appears.
- Line received-qty method: `manual` for goods/services in this module alone (purchase/models/purchase_order_line.py:225-231). Whether a Community install with goods uses `manual` or stock moves depends on `purchase_stock` (auto-installed with stock); see companion note.
- Vendor (per company): currency, receipt-reminder flag, days-before-receipt (fallback default 1), buyer, purchase warning (purchase/models/res_partner.py:31-45; purchase/data/purchase_data.xml:41).
- Price/date defaults on a line come from vendor price list (min qty, date, UoM, discount, delay), else product cost converted to PO currency; a manually changed price is preserved unless the vendor list changes it (`technical_price_unit`) (purchase/models/purchase_order_line.py:419-490,302-310).
- Tax totals rounding follows the company's tax calculation rounding method (purchase/models/purchase_order.py:29-45,155-158).
- Currency rate stored per PO; `amount_total_cc` gives total in company currency (purchase/models/purchase_order.py:164-170,212-226).
- Partner `buyer_id` and `property_purchase_currency_id` influence defaults (purchase/models/res_partner.py:31-45).

## 6. Effective extension path (module names only)

- `purchase.order` extended by: purchase_stock, purchase_requisition, purchase_requisition_stock, purchase_product_matrix, purchase_edi_ubl_bis3, project_purchase, project_purchase_stock, sale_purchase, sale_purchase_stock, purchase_mrp, purchase_repair, stock_dropshipping, mrp_subcontracting_purchase, mrp_subcontracting_dropshipping.
- `purchase.order.line` extended by: purchase_stock, purchase_requisition, purchase_requisition_stock, purchase_product_matrix, project_purchase, sale_purchase, sale_purchase_stock, purchase_mrp, stock_dropshipping, stock_landed_costs.
- `purchase.report` extended by: purchase_stock. `purchase.bill.union` / `purchase.bill.line.match`: no extenders found.
- Modules that list `purchase` (or `purchase_stock`) in their manifest: l10n_din5008_purchase, l10n_in_purchase_stock, project_purchase, purchase_edi_ubl_bis3, purchase_mrp, purchase_product_matrix, purchase_repair, purchase_requisition, purchase_requisition_stock, purchase_stock, sale_purchase, sale_purchase_stock, stock_landed_costs, test_main_flows. Auto-install modules: purchase_stock, sale_purchase, project_purchase (check `auto_install` in each manifest).

## 7. UNKNOWN items

- UNKNOWN — EVIDENCE INSUFFICIENT: server-side (non-UI) enforcement that only managers may unlock or that a locked PO rejects line edits.
- UNKNOWN — EVIDENCE INSUFFICIENT: behavior of the Enterprise-only 3-way match module (not in source tree).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether `purchase_ok` product flag or vendor-category restrictions gate product choice on a PO line (not traced).
- UNKNOWN — EVIDENCE INSUFFICIENT: exact effect of `env.company` vs order company in the approval-threshold conversion when a user works in a company other than the order's (code uses the current environment company's currency; purchase/models/purchase_order.py:1256-1258). Observation only; not verified at runtime.
- Observation: the portal report selection tests state values `rfq`/`sent` while the real draft state key is `draft` (purchase/controllers/portal.py:152 vs purchase/models/purchase_order.py:106). Effect on a draft PO viewed by token: UNKNOWN — EVIDENCE INSUFFICIENT.

