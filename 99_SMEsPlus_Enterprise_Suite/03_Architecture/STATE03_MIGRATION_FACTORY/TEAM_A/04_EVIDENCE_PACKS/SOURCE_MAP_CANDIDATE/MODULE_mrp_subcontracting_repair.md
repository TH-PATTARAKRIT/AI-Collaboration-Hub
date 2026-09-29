# Source Map (candidate) — `mrp_subcontracting_repair`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `mrp_subcontracting_repair` |
| Display name | MRP Subcontracting Repair |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `3b86042479be7b0b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mrp_subcontracting_repair/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `mrp_subcontracting`, `repair`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Repair / —
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 6 of 8 source pointers resolve to an existing file and in-range line (2 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: mrp_subcontracting_repair
Source revision: 19.0.post20260921 (Odoo 19 Community). Read-only trace; neutral business language; no code copied.

## A. Capabilities / activation
- Declared purpose: a bridge between subcontracting and repair. mrp_subcontracting_repair/__manifest__.py:8-10
- Conditional: auto-installs when both mrp_subcontracting and repair are installed. mrp_subcontracting_repair/__manifest__.py:11-15
- Functional content: NONE found. The package initialiser is an empty file, and the module has no models, views, data, security records or tests (directory contains only the manifest and the empty initialiser). mrp_subcontracting_repair/__init__.py:1 (empty, 0 bytes); mrp_subcontracting_repair/__manifest__.py:4-18
- The source-map skeleton agrees: zero models, zero data files, zero rules/groups. (skeleton /Users/admin/STATE03_RESTRICTED_LOCAL/sourcemap/mrp_subcontracting_repair.json)

## B. Business objects, lifecycle
- None introduced or extended by this module. Its effect is limited to being present as an installed (auto-installed) module in the dependency graph, which may serve as a hook point for other modules' auto-install or data-loading order. (inference from manifest only) mrp_subcontracting_repair/__manifest__.py:11-15
- No cross-reference to repair was found inside mrp_subcontracting (no file mentions repair in its Python or XML). mrp_subcontracting/ (search result, no match)

## C. Validations / security / multi-company
- None. No access rules, no record rules, no constraints. mrp_subcontracting_repair/__manifest__.py:4-18

## D. Handoffs
- None implemented here. The repair object model is owned by [repair]; subcontracting is owned by [mrp_subcontracting].
- Practical consequence for the study: repair orders operate on the repair operation type and location mapping described in repair/models/stock_picking.py:65-114; nothing in this bridge changes them.

## E. Configuration that changes outcomes
- None.

## F. Effective extension path
- This module extends nothing; no other Community module was found that depends on it (module names only: none). Repair itself is extended by mrp_repair, purchase_repair, l10n_din5008_repair (from _inherit search); those are documented in their own notes.

## G. Not verified
- Why the bridge exists (intended behaviour when a subcontracted receipt is repaired, or when a repair operation is performed at a subcontractor): UNKNOWN — EVIDENCE INSUFFICIENT
- Whether any upstream test or data elsewhere relies on this module being installed: UNKNOWN — EVIDENCE INSUFFICIENT
- Whether Enterprise or other editions add content to it: UNKNOWN — EVIDENCE INSUFFICIENT (out of scope; only Community source read)

