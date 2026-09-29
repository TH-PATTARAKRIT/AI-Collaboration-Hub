# Source Map (candidate) — `repair`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `repair` |
| Display name | Repairs |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `d3dc6292965a1ea5` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/repair/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `sale_stock`, `sale_management`
- Direct dependents in 300-module list (3): `mrp_repair`, `mrp_subcontracting_repair`, `purchase_repair`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `l10n_din5008_repair`, `pos_repair`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Inventory / Repair damaged products
- Inventory of user-facing artifacts (counts): menu items 8, views 18, window actions 7, server actions 1, reports 1, mail templates 0, scheduled jobs 0, wizards 2, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `stock.warn.insufficient.qty.repair` (Warn Insufficient Repair Quantity); `repair.order` (Repair Order); `repair.tags` (Repair Tags)
- Objects extended from other modules (17): `stock.warn.insufficient.qty`, `mail.thread`, `mail.activity.mixin`, `product.catalog.mixin`, `stock.warehouse`, `sale.order`, `sale.order.line`, `stock.move.line`, `account.move.line`, `stock.move`, `stock.picking.type`, `stock.picking`, `stock.traceability.report`, `product.product`, `product.template`, `stock.lot`, `stock.forecasted_product_product`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 1 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `repair.order` ← Community: `l10n_din5008_repair`, `mrp_repair`, `purchase_repair`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `stock.warn.insufficient.qty`, `mail.thread`, `mail.activity.mixin`, `product.catalog.mixin`, `stock.warehouse`, `sale.order`, `sale.order.line`, `stock.move.line`, `account.move.line`, `stock.move`, `stock.picking.type`, `stock.picking`, `stock.traceability.report`, `product.product`, `product.template`, `stock.lot`, `stock.forecasted_product_product`

## 6. Actions / states / validation / automation / security
- State fields found: `repair.order` → ['draft', 'confirmed', 'under_repair', 'done', 'cancel']
- Validation: 0 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 1); access rows 3

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

