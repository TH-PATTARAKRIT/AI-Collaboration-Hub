# Source Map (candidate) — `sale_project_stock_account`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_project_stock_account` |
| Display name | Sale Project Stock Account |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G06 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `f488a303cc738a02` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_project_stock_account/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_project`, `project_stock_account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Services/Project / Technical Bridge
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `stock.move`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `stock.move`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 10 of 10 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: sale_project_stock_account (Odoo 19 Community, revision 19.0.post20260921)
## A. Capabilities; core / optional / conditional
- Technical bridge between sale_project and project_stock_account; auto-installs when both present. sale_project_stock_account/__manifest__.py:5-9
- Single behaviour: under anglo-saxon accounting, stock moves of products with a re-invoice policy (sales price or cost) do not generate project analytic lines. sale_project_stock_account/models/stock_move.py:10-15
## B. Business objects and lifecycle
- Object: stock move. Base rule (project_stock_account): analytic lines are made only for moves whose transfer has a project and whose operation type has analytic costs enabled. project_stock_account/models/stock_move.py:24-25
- Effect (TEST): a delivery on a project with a cost-policy product, operation type analytic costs on and anglo-saxon on, validated by a stock user, produces no analytic lines. sale_project_stock_account/tests/test_analytics_reinvoice.py:8-36
## C. Validations, automation, security, multi-company
- Gate uses the current user's company setting for anglo-saxon accounting, not the move's company. sale_project_stock_account/models/stock_move.py:13. Consequence in multi-company use: UNKNOWN — EVIDENCE INSUFFICIENT
- No access entries, rules or constraints in this module (file inventory).
## D. Accounting / inventory / analytic handoffs
- Analytic line creation for stock moves: project_stock_account (project_stock_account/models/stock_move.py:27-29); valuation and anglo-saxon: account/stock_account; re-invoice revenue: sale via product policy. Purpose inferred: avoid double cost when the re-invoice flow already records it (comment) sale_project_stock_account/models/stock_move.py:12
- Without anglo-saxon accounting the filter is not applied, so analytic lines are still created. sale_project_stock_account/models/stock_move.py:12-14
## E. Configuration
- Company anglo-saxon accounting flag; product re-invoice policy; operation type "analytic costs"; project on transfer. sale_project_stock_account/models/stock_move.py:13-14; project_stock_account/models/stock_move.py:24
## F. Extension path
- _inherit: stock.move only. Overrides project_stock_account valid-moves domain. Dependents: none in tree.
## G. Not verified
- Where the re-invoiced cost is recorded instead: UNKNOWN — EVIDENCE INSUFFICIENT
- Interaction with manufacturing consumption moves: UNKNOWN — EVIDENCE INSUFFICIENT

