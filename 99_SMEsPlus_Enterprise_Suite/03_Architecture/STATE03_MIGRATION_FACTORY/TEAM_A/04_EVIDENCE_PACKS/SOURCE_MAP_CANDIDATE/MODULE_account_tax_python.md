# Source Map (candidate) — `account_tax_python`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `account_tax_python` |
| Display name | Define Taxes as Python Code |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `92869509ee49ea0a` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/account_tax_python/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (3): `l10n_in`, `l10n_my`, `pos_account_tax_python`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / Use python code to define taxes
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `account.tax`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `account.tax`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 24 of 24 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: account_tax_python
Source revision: 19.0.post20260921 | Path root: odoo/addons | Method: read-only source reading, neutral wording

## A. Capabilities
- Adds a new tax computation type "Custom Formula" to the standard tax object; the tax amount is then produced by a user-written arithmetic formula instead of percent/fixed/etc. (account_tax_python/models/account_tax.py:15-18). Optional module (installed on demand; depends only on `account`) (account_tax_python/__manifest__.py:`depends`).
- The formula text field carries a default (unit price x 10%) and a help text listing the values a formula may use: base amount, unit price, quantity, product (account_tax_python/models/account_tax.py:19-27).
- Formula field is shown and required on the tax form only when the type is Custom Formula (account_tax_python/views/account_tax_views.xml:9).
- The same formula must give the same result in the server and in browser/point-of-sale code; the model explicitly notes a mirrored client-side helper that must stay consistent (account_tax_python/models/account_tax.py:87-89; client helpers loaded in backend and frontend bundles: account_tax_python/__manifest__.py:`assets`).
- Manifest description mentions an "Applicable Code" snippet, but no such field exists in the module's model; only the amount formula is implemented (account_tax_python/__manifest__.py:`description` vs models/account_tax.py:19). Treat manifest wording as outdated.

## B. Business objects / lifecycle
- Only one object is extended: the tax (account.tax). No new business object, no state machine (account_tax_python/models/account_tax.py:13).
- Formula language is a restricted arithmetic subset: numbers, + - * /, comparisons, and/or, unary sign, min/max, and read-only access to named inputs (price_unit, quantity, base, product, uom) (account_tax_python/tools/formula_utils.py:8-20, 66-118).
- Product and unit-of-measure values may be read by field name; only non-relational (simple-valued) fields are accepted; the module records which product/UoM fields a formula reads so the caller can pre-load them (account_tax_python/models/account_tax.py:36-48, 66-83).
- At computation time inputs are flattened to primitive values; non-primitive context raises an error; division by zero yields a zero tax amount (account_tax_python/models/account_tax.py:95-114).
- The formula result is used as the tax amount via the base tax engine's "fixed amount" extension point (account_tax_python/models/account_tax.py:116-120). Tax-included/excluded handling is owned by `account` (TEST: account_tax_python/tests/test_taxes_computation.py:11-40 shows same formula under included and excluded pricing).

## C. Validations / security / multi-company
- On save, a Custom Formula tax must pass syntax and whitelist checks; invalid syntax, unknown names, non-numeric literals, keyword arguments, unknown function calls, and subscripts other than product['x']/uom['x'] are rejected (account_tax_python/models/account_tax.py:30-34; account_tax_python/tools/formula_utils.py:66-118).
- Empty formula is treated as zero for checking (account_tax_python/models/account_tax.py:78).
- (TEST) Rejected examples include relational fields, method calls, string literals, lists/sets/dicts, comprehensions, private attributes (account_tax_python/tests/test_taxes_computation.py:141-168).
- Formula editing rights follow the tax object's access rules from `account`; this module adds no ACL file, record rule or group (account_tax_python/__manifest__.py:`data` lists only a view). Company scoping is inherited from the tax's own company field in `account`; UNKNOWN — EVIDENCE INSUFFICIENT for how (in `account`) that scoping is enforced.
- Disabling the module path: if the Custom Formula type is removed on uninstall, affected taxes are set to Percent and archived (account_tax_python/models/account_tax.py:17).

## D. Handoffs
- Tax computation engine, product field pre-loading, and tax-included handling: owned by `account` (extension hooks named "EXTENDS 'account'": account_tax_python/models/account_tax.py:37, 44, 117).
- Point of sale reuses the client helper: owned by `pos_account_tax_python` (pos_account_tax_python/__manifest__.py:8).
- No accounting entry, inventory, approval or audit event is created by this module itself.

## E. Configuration that changes outcomes
- Choice of amount type = Custom Formula per tax; the formula text (default "unit price x 0.10") (account_tax_python/models/account_tax.py:15-22).
- Price-include override behaviour of the tax (owned by `account`) changes the result (TEST) (account_tax_python/tests/test_taxes_computation.py:20-31).

## F. Extension path (other Community modules)
- Modules that depend on this module: l10n_in, l10n_my, pos_account_tax_python (grep of __manifest__ `depends`).
- Modules extending the tax object (account.tax) overall (any feature): account_edi_ubl_cii, account_tax_python, hr_expense, l10n_account_withholding_tax, l10n_account_withholding_tax_pos, l10n_ar_withholding, l10n_be, l10n_br, l10n_cl, l10n_de, l10n_ec, l10n_ee, l10n_eg, l10n_es, l10n_es_edi_facturae, l10n_es_edi_verifactu, l10n_fr_pdp, l10n_gr_edi, l10n_hr_edi, l10n_hu_edi, l10n_in, l10n_in_pos, l10n_it, l10n_it_edi, l10n_it_edi_doi, l10n_jo_edi, l10n_ke, l10n_lt, l10n_mx, l10n_my_edi, l10n_no, l10n_pe, l10n_ph, l10n_pt, l10n_sa_edi, l10n_sg_ubl_pint, l10n_tr_nilvera_einvoice_extended, l10n_tw_edi_ecpay, l10n_tw_edi_ecpay_pos, l10n_uy, point_of_sale, pos_account_tax_python, purchase (grep `_inherit` account.tax; excludes `account` itself and tests).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: exact client-side (JS) mirror behaviour; the JS helper files were not read.
- UNKNOWN — EVIDENCE INSUFFICIENT: how localisation modules l10n_in / l10n_my use Custom Formula taxes in their data.
- UNKNOWN — EVIDENCE INSUFFICIENT: rounding behaviour of formula results (handled in `account` engine).

