# Source Map (candidate) — `purchase_requisition`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `purchase_requisition` |
| Display name | Purchase Agreements |
| Manifest version | 0.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G03 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `d8628384f1d6fb59` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/purchase_requisition/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `purchase`
- Direct dependents in 300-module list (2): `purchase_requisition_sale`, `purchase_requisition_stock`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Purchase / —
- Inventory of user-facing artifacts (counts): menu items 1, views 12, window actions 3, server actions 0, reports 1, mail templates 0, scheduled jobs 0, wizards 3, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (5): `purchase.requisition.alternative.warning` (Wizard in case PO still has open alternative requests for quotation); `purchase.requisition.create.alternative` (Wizard to preset values for alternative PO); `purchase.order.group` (Technical model to group PO for call to tenders); `purchase.requisition` (Purchase Requisition); `purchase.requisition.line` (Purchase Requisition Line)
- Objects extended from other modules (8): `purchase.order`, `purchase.order.line`, `product.supplierinfo`, `product.product`, `res.config.settings`, `mail.thread`, `mail.activity.mixin`, `analytic.mixin`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `purchase.requisition.create.alternative` ← Community: `purchase_requisition_sale`, `purchase_requisition_stock`; open-license custom/third-party scanned: —
- `purchase.requisition` ← Community: `purchase_requisition_stock`; open-license custom/third-party scanned: —
- `purchase.requisition.line` ← Community: `purchase_requisition_stock`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `purchase.order`, `purchase.order.line`, `product.supplierinfo`, `product.product`, `res.config.settings`, `mail.thread`, `mail.activity.mixin`, `analytic.mixin`

## 6. Actions / states / validation / automation / security
- State fields found: `purchase.requisition` → ['draft', 'confirmed', 'done', 'cancel']
- Validation: 1 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 1 (`group_purchase_alternatives`); record rules 2 (of which company-scoped by text 2); access rows 7

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

