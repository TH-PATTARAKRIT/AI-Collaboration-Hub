# Source Map (candidate) — `sale_timesheet_margin`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_timesheet_margin` |
| Display name | Service Margins in Sales Orders |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `e71e48cd353b8b34` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_timesheet_margin/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_margin`, `sale_timesheet`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / Bridge module between Sales Margin and Sales Timesheet
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 13 of 13 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: sale_timesheet_margin (Odoo 19 Community, revision 19.0.post20260921)
## A. Capabilities; core / optional / conditional
- Bridge that makes sale order line cost (and so margin) reflect real timesheet cost for service lines. sale_timesheet_margin/__manifest__.py:6-11
- Conditional: auto-installs when sale_margin and sale_timesheet are both installed. sale_timesheet_margin/__manifest__.py:12-13
## B. Business objects and lifecycle
- Object: sale order line cost (purchase price). Base cost = product standard cost converted to line unit and currency. sale_margin/models/sale_order_line.py:21-35; margin = subtotal minus cost x quantity. sale_margin/models/sale_order_line.py:37-46
- Override applies to lines delivered by timesheet whose product has no standard cost: cost becomes actual timesheet cost per hour (analytic amount over hours on project timesheets), converted to line unit and currency; falls back to product cost if no timesheets. sale_timesheet_margin/models/sale_order_line.py:19-43
- Recalculated when analytic line amounts or the delivery method change. sale_timesheet_margin/models/sale_order_line.py:9
- Excluded from recomputation: confirmed, non-expense service lines with prepaid / manual / milestone policy and non-zero cost. sale_timesheet_margin/models/sale_order_line.py:14-18; (TEST) sale_timesheet_margin/tests/test_sale_timesheet_margin.py:90-197
- (TEST) Cost equals employee hourly cost converted to the order-line unit (day) after a timesheet is logged and cost recomputed. sale_timesheet_margin/tests/test_sale_timesheet_margin.py:54-88
## C. Validations, automation, security, multi-company
- No constraints or access entries; margin/cost fields are visible only to internal users (group on parent field). sale_margin/models/sale_order_line.py:12-18
- Cost computed in each line's own company context and currency. sale_timesheet_margin/models/sale_order_line.py:33,42-43
## D. Accounting / inventory / analytic handoffs
- Timesheet cost amounts: hr_timesheet analytic lines (hourly cost may be overridden by sale_timesheet employee mapping, sale_timesheet/models/hr_timesheet.py:194-199). Margin fields: sale_margin. No journal entries or stock effect here.
## E. Configuration
- Product standard cost (zero triggers timesheet-based cost); product service policy; company project time unit. sale_timesheet_margin/models/sale_order_line.py:20,34-37
## F. Extension path
- _inherit: sale.order.line only. Dependents: none in tree.
## G. Not verified
- Sign handling when timesheet amounts are positive (revenue-type lines): UNKNOWN — EVIDENCE INSUFFICIENT
- Effect on lines whose cost is manually edited (field editable in parent): UNKNOWN — EVIDENCE INSUFFICIENT

