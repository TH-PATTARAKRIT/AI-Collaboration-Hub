# Source Map (candidate) — `sale_gelato_stock`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_gelato_stock` |
| Display name | Gelato/Stock bridge |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `2e782c67c34e51f5` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_gelato_stock/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_gelato`, `sale_stock`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `sale.order.line`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `sale.order.line`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 8 of 8 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — sale_gelato_stock
Source revision: 19.0.post20260921 | Module: "Gelato/Stock bridge" (sale_gelato_stock/__manifest__.py:4) | depends: sale_gelato, sale_stock (:6) | auto_install true (:7) | LGPL-3 (:9)
Basis: static reading of manifest and the single override; no tests, views, data or security exist.

## A. Capabilities and optionality
- A1. When Gelato print-on-demand is used together with inventory, lines for Gelato products do not generate warehouse transfers (Gelato fulfils and ships them directly). sale_gelato_stock/models/sale_order_line.py:11-14
- A2. Automatic bridge whenever both parents are installed. sale_gelato_stock/__manifest__.py:6-7

## B. Objects, relationships, lifecycle
- B1. On confirmation, the stock procurement launch skips lines whose product has a Gelato product identifier; other lines are processed normally. sale_gelato_stock/models/sale_order_line.py:13-14
- B2. Consequence (inferred from the skip only): no delivery orders and no delivered-quantity updates come from stock for Gelato lines. UNKNOWN — EVIDENCE INSUFFICIENT on how delivered quantity or invoicing status is set for those lines (not in this module).
- B3. Mixing Gelato and non-Gelato goods on one order is blocked by sale_gelato, so an order is either all Gelato goods (plus services) or none. sale_gelato/models/sale_order.py:33-50

## C. Validations, security, multi-company
- C1. No constraints, groups, ACLs, or rules here. sale_gelato_stock/ (file list)
- C2. Multi-company: none. UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs
- D1. Fulfilment is handed to the external service (owner sale_gelato); inventory (owner stock/sale_stock) is bypassed for these lines. sale_gelato_stock/models/sale_order_line.py:11-14
- D2. No accounting, purchase or analytic logic in this module.

## E. Configuration that changes outcomes
- E1. A product is treated as Gelato when it has a Gelato product UID (set by synchronisation, see sale_gelato). sale_gelato_stock/models/sale_order_line.py:13; sale_gelato/models/product_product.py:9

## F. Effective extension path (modules)
- Depended on by: none (grep of manifests). Overrides the stock launch hook of sale_stock's sale order line.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: whether a shipment/tracking record ever appears in inventory for Gelato orders; interaction with website_sale_gelato.

