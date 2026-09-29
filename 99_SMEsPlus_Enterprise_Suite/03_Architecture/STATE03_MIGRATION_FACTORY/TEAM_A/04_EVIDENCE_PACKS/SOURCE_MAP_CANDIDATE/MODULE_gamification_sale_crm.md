# Source Map (candidate) — `gamification_sale_crm`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `gamification_sale_crm` |
| Display name | CRM Gamification |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `68ea1ca2a7e8ca8e` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/gamification_sale_crm/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `gamification`, `sale_crm`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/CRM / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: —

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 9 of 9 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: gamification_sale_crm (revision 19.0.post20260921)
Scope: Odoo Community read-only study. Pointers `module/path:LINE`. Data-only module (no Python, no tests).

## A. Capabilities and activation
- Ships example goal definitions and two challenges tied to sales/CRM usage (gamification_sale_crm/__manifest__.py:8). Depends on gamification and sale_crm (gamification_sale_crm/__manifest__.py:7); auto_install (gamification_sale_crm/__manifest__.py:11). sale_crm is itself auto_install over sale and crm (sale_crm/__manifest__.py:19,28).
- All records are loaded as "no update": local edits are kept on upgrade (gamification_sale_crm/data/gamification_sale_crm_data.xml:2).

## B. Business objects and lifecycle
- Goal definitions (10): total invoiced (sum of invoice-report subtotals, customer invoices not cancelled) (data:5-17); new leads (leads plus opportunities, by creation date) (data:19-31); time to qualify a lead (lower is better) (data:33-46); days to close a deal (lower is better) (data:48-62); new opportunities (data:64-75); new sales orders (order states other than draft/sent/cancel) (data:77-88); paid sales orders count (invoices paid or in payment) (data:90-100); total paid sales orders (data:102-115); customer credit notes count (data:117-128); total credit notes value (data:130-143). Paths are gamification_sale_crm/data/gamification_sale_crm_data.xml.
- Batch evaluation per user: goals evaluate per salesperson through the user field of the source record (data:15-16,29-30,44-45).
- Challenges: "Monthly Sales Targets" (one line: total invoiced, target 20000) and "Lead Acquisition" (three lines: new leads target 7, time-to-qualify target 15, new opportunities target 5). Monthly period, ranking visibility, weekly report, participants = users in the salesman group (data:148-190).
- Challenge lifecycle is owned by gamification: draft, in progress, done (gamification/models/gamification_challenge.py:78-81). Data file sets no state; only the demo file sets the sales challenge to in progress (gamification_sale_crm/data/gamification_sale_crm_demo.xml:4-6). Default state is draft (gamification/models/gamification_challenge.py:82), so in a non-demo database the two challenges are expected to start in draft until someone starts them.
- Observation: the goal named "Time to Qualify a Lead" reads the day-to-close field and "Days to Close a Deal" reads the day-to-open field (data:34,40,49,55); intent of the naming: UNKNOWN — EVIDENCE INSUFFICIENT

## C. Validations, security, multi-company
- No constraints or access rules defined here; challenge participants are selected by group membership, not by company (data:152,160). Company scoping of the invoice report and lead data is inherited from account and crm: UNKNOWN — EVIDENCE INSUFFICIENT

## D. Handoffs (owner)
- Invoice metrics read the accounting invoice report (account) (data:10-13). Order metrics read sales orders (sale) (data:82-84). Lead metrics read CRM leads (crm) (data:24-27). This module only reads; it posts nothing to accounting, inventory, purchase or analytic.

## E. Configuration that changes outcomes
- Target values on challenge lines, period, participant domain, report frequency are all editable data (data:148-190). Only two of the ten goal definitions are used by the shipped challenges (data:165-189).

## F. Extension path
- No module lists gamification_sale_crm as a dependency (grep of manifests). It extends gamification through data only.

## G. Not verified
- Goal computation mechanics and rewards (belongs to gamification): UNKNOWN — EVIDENCE INSUFFICIENT

