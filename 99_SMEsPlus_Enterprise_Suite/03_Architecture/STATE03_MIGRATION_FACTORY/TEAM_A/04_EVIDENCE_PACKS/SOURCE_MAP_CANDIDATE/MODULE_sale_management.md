# Source Map (candidate) — `sale_management`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

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
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

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
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

