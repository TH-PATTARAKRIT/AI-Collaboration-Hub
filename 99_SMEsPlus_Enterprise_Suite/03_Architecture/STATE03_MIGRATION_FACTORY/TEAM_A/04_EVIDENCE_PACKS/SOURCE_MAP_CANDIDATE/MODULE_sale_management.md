# Source Map (candidate) — `sale_management`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_management` |
| Display name | Sales |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `49b8dd9441dfa53a` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_management/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `sale`, `digest`
- Direct dependents in 300-module list (7): `event_sale`, `repair`, `sale_expense`, `sale_margin`, `sale_pdf_quote_builder`, `sale_project`, `sale_service`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `pos_sale`, `test_sale_product_configurators`
- Custom / third-party modules that declare a dependency (name — license only) (8): `delivery_split` — AGPL-3, `order_line_sequence` — AGPL-3, `product_brand_sale` — AGPL-3, `bh_parent_company` — LGPL-3, `sale_job_type` — LGPL-3, `sale_order_level_approve` — LGPL-3, `import_bridge_axis` — OPL-1, `auto_gen_job_type` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / From quotations to invoices
- Inventory of user-facing artifacts (counts): menu items 1, views 6, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `sale.order.template` (Quotation Template); `sale.order.template.line` (Quotation Template Line)
- Objects extended from other modules (5): `digest.digest`, `sale.order`, `sale.order.line`, `res.company`, `res.config.settings`
- Company-dependent settings introduced: 1 field(s); company-consistency auto-check declared on 1 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `sale.order.template` ← Community: `sale_pdf_quote_builder`; open-license custom/third-party scanned: —
- `sale.order.template.line` ← Community: `sale_project`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `digest.digest`, `sale.order`, `sale.order.line`, `res.company`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 2 declarative constraint method(s), 2 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 2 (`group_sale_order_template`, `base.group_user`); record rules 1 (of which company-scoped by text 1); access rows 5

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 48 of 48 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: sale_management (revision 19.0.post20260921)
Scope: Odoo Community read-only study. Pointers are `module/path:LINE`; (TEST) = test-derived.

## A. Capabilities and activation
- Adds reusable quotation templates and "optional" sections (customer-selectable extras on the portal) on top of the Sales app; depends only on sale and digest (sale_management/__manifest__.py:38). Flagged as an application (sale_management/__manifest__.py:72). No auto_install flag in the manifest (sale_management/__manifest__.py:3-78).
- Template feature is conditional: menu "Quotation Templates" and the template field on the order form show only for the group "Quotation Templates" (sale_management/views/sale_management_menus.xml:8-13; sale_management/views/sale_order_views.xml:10-14; group defined sale_management/security/sale_management_security.xml:4-6). Group is switched via a Sales setting (sale_management/models/res_config_settings.py:9-10; sale_management/views/res_config_settings_views.xml:14).
- Optional-section handling on portal is not group-gated; it depends on line flags (sale_management/models/sale_order_line.py:11-15).
- Install/uninstall re-activates or deactivates the standard Sales menus owned by sale (sale_management/__init__.py:14-27); install does not back-fill templates onto existing orders (sale_management/__init__.py:9-12).
- Also contributes an "All Sales" digest KPI, restricted to users in the all-leads salesman group (sale_management/models/digest.py:10-23; sale_management/data/digest_data.xml:4-6) and two digest tips (sale_management/data/digest_data.xml:9-32).

## B. Business objects, relationships, lifecycle
- Quotation Template: name, terms text, validity days, confirmation mail, online-signature flag, online-payment flag plus prepayment percentage, invoicing journal, optional company, active flag, ordered lines (sale_management/models/sale_order_template.py:13-55).
- Template Line: either a product line (product, unit, quantity) or a display line (section, subsection, note); sections can be flagged optional; parent section is derived from position (sale_management/models/sale_order_template_line.py:57-105).
- A sales order optionally points to one template; the field is stored, user-editable, company-checked (sale_management/models/sale_order.py:14-19). Company may define a default template (sale_management/models/res_company.py:10-14).
- Selecting a template replaces the order's lines with copies of the template lines (sale_management/models/sale_order.py:84-102). On a new unsaved order, changing customer reloads the template only if lines still equal the template (sale_management/models/sale_order.py:104-120).
- Template values feed order defaults: terms note, signature requirement, payment requirement, prepayment %, validity date (today + days when days > 0), journal (sale_management/models/sale_order.py:34-72).
- Order states are owned by sale: Quotation, Quotation Sent, Sales Order, Cancelled (sale/models/sale_order.py:26-31). Portal edits of optional lines only while state is Quotation or Quotation Sent (sale/models/sale_order.py:2301-2303) and only for lines under an optional section or an optional-section subsection (sale_management/models/sale_order_line.py:43-59).
- Confirmation: after standard confirm, if confirmed from backend and the template names a confirmation mail, that mail is sent (sale_management/models/sale_order.py:128-140); the template mail also overrides the default confirmation mail (sale_management/models/sale_order.py:124-126). Signature/payment gating of confirmation is evaluated by sale, not by this module (sale/models/sale_order.py:1896-1930).
- Website exception: orders that carry a website reference do not get the company default template applied (sale_management/models/sale_order.py:29-31).

## C. Validations, automation, security, multi-company
- Line constraints: a non-display line needs product and unit; a display line must have no product, zero quantity, no unit (sale_management/models/sale_order_template_line.py:12-19); line type cannot be changed after creation (sale_management/models/sale_order_template_line.py:116-119). Products offered must be saleable and not combo type (sale_management/models/sale_order_template_line.py:123-126).
- Prepayment percentage must be within (0,1] when online payment is required (sale_management/models/sale_order_template.py:126-130).
- Company rule: a shared template (no company) cannot hold company-restricted products; a company template cannot hold products inaccessible to that company (sale_management/models/sale_order_template.py:86-124) (TEST: sale_management/tests/test_sale_order_template.py:43-113, including parent/branch cases).
- Archiving a template clears it as default from any company (sale_management/models/sale_order_template.py:140-143). Disabling the setting clears the default template on all companies (sale_management/models/res_config_settings.py:15-24).
- Portal quantity update: token/portal access check, order and line must be editable, quantity floored at zero, combo items follow the combo line, price recompute only if pricelist active and sale.disable_sale_update not set (sale_management/controllers/portal.py:12-59).
- Access: salesmen read-only on templates and lines; sales managers full; system group read template (sale_management/security/ir.model.access.csv:2-6). Multi-company record rule: templates visible when company in allowed companies or empty (sale_management/security/sale_management_security.xml:9-13).

## D. Handoffs
- Invoicing/journal: template journal is a company-dependent value copied onto the order; invoice creation is owned by sale/account (sale_management/models/sale_order_template.py:51-55; sale_management/models/sale_order.py:68-72).
- Delivery, purchase, analytic: no handoff in this module. Project/service and PDF quote-builder extend templates in separate modules (see F).
- Online payment/signature execution: owned by sale and payment stack; this module only stores the requirement (sale_management/models/sale_order.py:41-58).

## E. Configuration that changes outcomes
- Setting "Quotation Templates" (group) and per-company default template (sale_management/models/res_config_settings.py:9-13).
- Template validity days, signature, payment/prepayment %, journal, confirmation mail (sale_management/models/sale_order_template.py:22-55). Template default signature/payment/prepayment come from company portal settings at creation (sale_management/models/sale_order_template.py:59-74; company defaults sale/models/res_company.py:16-17).
- Configured default via defaults table on the order field does not raise onchange warnings (TEST: sale_management/tests/test_sale_order.py:492-526).
- Portal editing rules for optional lines and discounts/price recompute (TEST: sale_management/tests/test_sale_order.py:528-600).

## F. Extension path (module names, from grep of _inherit)
- sale.order.template: sale_pdf_quote_builder. sale.order.template.line: sale_project. Line-description override hook `_use_template_name`: event_sale, event_booth_sale. Optional-line helper used by: sale_project. Portal-edit hook overridden by: sale_loyalty. Confirmation-mail hook overridden by: website_sale.
- Modules that depend on sale_management: sale_expense, sale_margin, event_sale, sale_project, sale_pdf_quote_builder, sale_service, repair, pos_sale, test_sale_product_configurators (grep of __manifest__.py).

## G. Not verified
- Exact effect of sale-owned portal payment/signature flows on template values: UNKNOWN — EVIDENCE INSUFFICIENT
- Behaviour of client-side widgets (static/src/fields, interactions): UNKNOWN — EVIDENCE INSUFFICIENT
- Report layout of optional sections in printed quotation: UNKNOWN — EVIDENCE INSUFFICIENT

