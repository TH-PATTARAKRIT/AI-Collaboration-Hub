# Source Map (candidate) — `account_test`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `account_test` |
| Display name | Accounting Consistency Tests |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `a100bf95d7647538` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/account_test/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / —
- Inventory of user-facing artifacts (counts): menu items 1, views 3, window actions 1, server actions 0, reports 1, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `accounting.assert.test` (Accounting Assert Test); `report.account_test.report_accounttest` (Account Test Report)
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: —

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 19 of 19 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: account_test
Source revision: 19.0.post20260921 | Path root: odoo/addons | Method: read-only source reading, neutral wording

## A. Capabilities
- Lets an administrator define "accounting consistency tests" (name, description, ordering, on/off) and print them as a PDF "Accounting Tests" report that lists either a success message or the offending records (account_test/models/accounting_assert_test.py:15-24; account_test/report/report_account_test.py:50-62; account_test/report/accounting_assert_test_reports.xml:3-11).
- Optional module; depends only on `account` (account_test/__manifest__.py:`depends`).
- Menu entry "Accounting Tests" under Accounting > Reporting is visible only in developer mode (technical-features group) (account_test/views/accounting_assert_test_views.xml:90).
- Ships seeded example tests: general balance (Test 1), movement lines (Test 3), payable/receivable lines of reconciled invoices (5.1, 5.2), invoice status (Test 6), bank-statement closing balance (Test 7); tests 4 and 8 are commented out and not active (account_test/data/accounting_assert_test_data.xml:4, 21, 67, 83, 98, 115; commented 49-65, 127-139).

## B. Business objects / lifecycle
- One object: accounting.assert.test (Accounting Assert Test) with name (translatable), description, "Python code" (required), active flag, sequence (account_test/models/accounting_assert_test.py:15-24). Lifecycle is only active/archived (archived filter: account_test/views/accounting_assert_test_views.xml:73).
- Result semantics: code sets a result; empty result = pass and prints "The test was passed successfully"; non-empty result is printed row by row; dictionary rows are printed as ordered "column: value" pairs (account_test/report/report_account_test.py:47-62; help text account_test/views/accounting_assert_test_views.xml:42-54).
- Code runs with a database cursor, the user id, a helper listing reconciled invoices, and an ordering helper (account_test/report/report_account_test.py:38-46). Definition is executable code stored as data; the code text is not analysed here (outside scope).

## C. Validations / security
- Access: base system group may read and delete (no create/write via ACL); Accounting Manager group may read only (account_test/security/ir.model.access.csv:2-3). No record rule, no company field on the object; tests are global, not company-scoped (account_test/models/accounting_assert_test.py:15-24).
- Report executes stored code against the raw database cursor without company filtering in the framework layer; visible result scope depends on the SQL text in each test. UNKNOWN — EVIDENCE INSUFFICIENT for multi-company behaviour of seeded tests beyond their own SQL (account_test/data/accounting_assert_test_data.xml).
- No constraints, no automation (no cron, no onchange) in this module.

## D. Handoffs
- Reads accounting data owned by `account` (journals, moves, lines, bank statements) via SQL/ORM; writes nothing to accounting (account_test/report/report_account_test.py:22; data XML SQL blocks).
- Printing uses the shared report engine and internal layout owned by `web` (account_test/report/report_account_test_templates.xml:4-5).

## E. Configuration that changes outcomes
- Per-test: active flag and sequence (ordering) (account_test/models/accounting_assert_test.py:18, 23-24).
- Developer mode toggles menu visibility (account_test/views/accounting_assert_test_views.xml:90).

## F. Extension path
- No other Community module was found extending accounting.assert.test (grep `_inherit` over addons root, excluding tests).
- No Community module lists account_test in its manifest dependencies (grep of __manifest__.py returned none).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: whether seeded tests were designed for the current data model (some seeded tests are commented out as legacy at account_test/data/accounting_assert_test_data.xml:49, 127).
- UNKNOWN — EVIDENCE INSUFFICIENT: sandbox limits of the code evaluator (owned by base tools; not read).

