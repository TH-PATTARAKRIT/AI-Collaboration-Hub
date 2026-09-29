# Source Map (candidate) — `account_update_tax_tags`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `account_update_tax_tags` |
| Display name | Account - Allow updating tax grids |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `5b7673367874486f` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/account_update_tax_tags/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / Allow updating tax grids on existing entries
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `account.update.tax.tags.wizard` (Update Tax Tags Wizard)
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: —

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 19 of 19 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: account_update_tax_tags
Source revision: 19.0.post20260921 | Path root: odoo/addons | Method: read-only source reading, neutral wording

## A. Capabilities
- One capability: a wizard that re-applies the CURRENT tax-grid tag configuration of taxes onto already-existing journal items, from a chosen start date, for the active company (account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:6-18, 35-48, 172-182). Purpose stated: after legal changes to a tax report (account_update_tax_tags/__manifest__.py:`description`).
- Optional module, depends only on `account`; not auto-install (account_update_tax_tags/__manifest__.py:`depends`).
- Entry point: a button in Accounting settings inside the default-taxes block, visible only in developer mode (account_update_tax_tags/views/res_config_settings_views.xml:16-21).

## B. Business objects / lifecycle
- Single transient (temporary) wizard object with company (fixed to current company, read-only) and start date (account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:10-18). No persistent object and no states.
- Start date default: the day after the company tax lock date if one exists, otherwise today (account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:22-26).
- Effect: for base lines, tags come from the "base" distribution line of the tax that matches the document type (invoice vs refund; for manual entries the sign of the balance and tax use decide; zero balance defaults to invoice); child taxes of group taxes are followed; cash-basis entries take document type from the origin move (account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:51-119). For tax lines, tags come from the line's own distribution line (same file:122-129).
- Old tag links of affected lines are deleted and replaced by the new set; lines whose configuration has no tag end up with no tag (same file:137-152). Counterpart lines are not touched (TEST: account_update_tax_tags/tests/test_account_update_tax_tags_wizard.py:300-312).
- Applies to entries in any state - posted, cancelled and draft (TEST: same file:300-312), so posted history is altered.

## C. Validations / security / multi-company
- Only guard that blocks: a child tax used by more than one parent group tax raises an error (account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:172-181; TEST :434).
- Tax lock date is NOT enforced: the wizard only shows a warning when start date is before the lock date ("do this at your own risk") (account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:28-32; account_update_tax_tags/wizard/account_update_tax_tags_wizard.xml:16-18).
- Form warns the action is irreversible and recommends a backup (account_update_tax_tags/wizard/account_update_tax_tags_wizard.xml:9-15).
- Access: Accounting Manager group has read/write/create (no delete) on the wizard (account_update_tax_tags/security/ir.model.access.csv:2). The update runs as direct database statements, bypassing ORM access rules and audit tracking on the move lines (account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:49-50, 169). No chatter/audit message is written by this module.
- Multi-company: only the wizard's own company is updated (query filters by company) (account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:56, 128; TEST :202-224).
- Date filter: only lines dated on/after the start date change (TEST: account_update_tax_tags/tests/test_account_update_tax_tags_wizard.py:164-174).

## D. Handoffs
- Tax definitions, distribution lines, tags, journal items, lock dates: owned by `account` (tables/fields referenced in account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:52-118).
- Downstream: tax reports/tax return grids owned by `account` (and localisation report modules) read the tags; effect is on report figures (stated in wizard warning text, account_update_tax_tags/wizard/account_update_tax_tags_wizard.xml:10-11).
- Method return value (impacted line ids) is not used or logged by the caller (account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:182).

## E. Configuration that changes outcomes
- Current tax repartition/tag configuration on taxes (edited beforehand by user in `account`).
- Start date (default rule above); company tax lock date (only affects default and warning).
- Developer mode to reach the button.

## F. Extension path
- No other Community module extends the wizard (grep `_inherit` account.update.tax.tags.wizard: none); no module depends on this module (manifest grep: none).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: interaction with hash/inalterability locks on posted moves (direct database writes; not tested here).
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour for tax lines on non-tax-distribution manual entries beyond tested scenarios.

