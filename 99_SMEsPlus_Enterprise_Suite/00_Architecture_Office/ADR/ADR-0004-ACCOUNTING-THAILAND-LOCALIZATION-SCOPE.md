# ADR-0004: Accounting Module Scope — Thailand Localization Only
Status: APPROVED
Approved By: Boss, 2026-07-05 (recorded via Claude, Engineering Execution AI, in AIOS session)

## Context
The source Odoo codebase bundles Odoo's full multi-country localization pack: 523 `l10n_*` modules
are present in the evidenced module inventory, spanning `Accounting/Localizations/Account Charts`
(120 modules), `Accounting/Localizations/Reporting` (112 modules), and `Accounting/Localizations/EDI`
(72 modules) — 304 modules total under the Accounting/Localizations category tree.
Evidence: `V2.0/THAI/.../Evidence_CSV/Module_Inventory.csv`.

Of these 523 country-localization modules, exactly **two** are Thailand-specific:
- `l10n_th` — "Thailand - Accounting" (depends on `account_qr_code_emv`, `account`; 5 model records, 3 matched)
- `l10n_th_reports` — "Thailand - Accounting Reports" (depends on `l10n_th`, `account_reports`)
Evidence: `Module_Inventory.csv` (grep-confirmed, no other Thailand-tagged module found in this evidence pass).

SMEsPlus Enterprise Suite is a Thailand-only SME market product (per `AI_PROJECT_CONSTITUTION.md` and
prior scope confirmation). Carrying all 523 country localizations forward would add unused scope,
unnecessary maintenance surface, and unclear FDS/SDS coverage for markets SMEsPlus does not serve.

## Problem Statement
Should the Accounting module's Functional Design retain Odoo's full multi-country localization surface,
or should it be scoped exclusively to Thailand, while still keeping all of Odoo's standard
(country-agnostic) accounting functionality intact?

## Decision
1. **Standard Odoo Accounting functionality is retained in full** — Chart of Accounts, General Ledger,
   Journal Entries, Accounts Receivable, Accounts Payable, Vendor Bill 2-way/3-way matching, and Payment
   reconciliation remain in scope exactly as evidenced in `iTEST02_ERD_Accounting_Finance.md` and
   confirmed MATCHED per `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` (FR-ACC-001).
2. **Localization scope is restricted to Thailand only.** In scope: `l10n_th`, `l10n_th_reports`, and any
   Thailand-specific compliance requirement not yet evidenced in the current module inventory (e.g.
   e-Tax Invoice / e-Receipt per the Thai Revenue Department, withholding-tax certificate generation,
   VAT reporting) — these are recorded as **GAP** pending a dedicated Accounting Functional
   Specification Factory pass, not assumed to exist.
3. **All other 521 country-localization modules are OUT OF SCOPE** for SMEsPlus and must not be carried
   into the Accounting FDS, SDS, or build backlog.
4. Standard accounting functions must be verified for Thai-market alignment where Thai regulation
   differs from generic Odoo defaults (e.g. VAT rate, WHT certificate format, Buddhist-era date display,
   Thai Baht as functional currency) — this alignment work is functional-design work, not new
   architecture, and follows the existing Evidence-Driven (ADR-0002) and As-Is-Before-To-Be (ADR-0003)
   standards.

## Alternatives Considered
- **Keep all 523 localizations "just in case":** rejected — adds unbounded scope with no evidenced
  business need; conflicts with the project's Thailand-only market definition.
- **Build Thai compliance features as a wholly custom layer instead of reusing `l10n_th`:** rejected —
  `l10n_th`/`l10n_th_reports` are confirmed present in the evidenced source; Evidence Matching should
  verify and reuse them before any custom build is considered (per ADR-0002).

## Consequences
- Accounting module's Functional Specification Factory pass (not yet started) should scope its
  Evidence Matching exclusively against `l10n_th`/`l10n_th_reports` plus standard Odoo accounting
  objects — not against the other 521 country localizations.
- `BUSINESS_CAPABILITY_MAP.md`, `SOURCE_TO_BUSINESS_MAPPING.md`, `MODULE_DEPENDENCY_MATRIX.md`, and
  `OPEN_SOURCE_TO_SMESPLUS_GAP.md` (Phase 2.5 Knowledge Base package, `07_Output_From_AI/
  Phase_2.5_Knowledge_Consolidation/`) are updated to reflect this scope decision.
- Thai-specific compliance gaps (e-Tax Invoice/e-Receipt, WHT certificate) are logged as GAP, not
  silently assumed covered by `l10n_th`.

## Review Date
Next review at Accounting module's own Functional Specification Factory kickoff (Priority-1, not yet
started as of 2026-07-05).

## Addendum — Re-Verification (2026-07-05, same day, deeper evidence pass)

Boss requested a second, deeper confidence check on the Thailand-localization evidence before Functional
Design begins. Re-verification against `Business_Rule_Method_Inventory.csv`, `ORM_Field_Inventory_and_
DB_Mapping.csv`, `Dump_Column_Inventory.csv`, `Foreign_Key_Relationship_Edges.csv`, and
`XML_View_Action_Menu_Inventory.csv` (not all consulted in the original pass) produced the following
refinements — none of which change the core decision above, but two of which add material precision:

1. **VAT — confirmed REUSE, clarified mechanism.** `l10n_th` has no separate VAT sub-module; Thai VAT is
   handled through Odoo's standard `account.tax` engine, with Thai rate/configuration data supplied by
   `l10n_th`'s own data files. No new VAT engine is needed.
2. **PromptPay / EMV QR on invoices — confirmed REUSE.** `account_qr_code_emv` (a dependency of `l10n_th`)
   is present with real business methods (`_compute_country_proxy_keys`, `_compute_display_qr_setting`,
   `_check_for_qr_code_errors`) in `01_ACCOUNT.zip`. This is the Thai PromptPay EMV QR payment-code
   mechanism referenced on invoices/payments.
3. **🆕 Thai Withholding Tax Certificate structure — found LIVE, but SOURCE NOT PROVIDED.** The dump
   contains a clearly Thailand-shaped WHT certificate schema: `withholding_tax_cert`,
   `withholding_tax_cert_line`, `create_withholding_tax_cert`, `account_withholding_tax` — with fields
   `income_tax_form`, `wt_cert_income_type`, `tax_payer`, `amount_pension_fund`,
   `amount_socialsecurity_fund`, `amount_provident_fund` (Thai PND-certificate-style categories).
   **No matching module exists in `Business_Rule_Method_Inventory.csv` or `Security_Access_Inventory.csv`
   for any of these four tables** — i.e. this feature is live in the database with zero source code in
   either provided zip. This is the same "found live, no source" pattern already recorded for the
   `efaplus` two-level PO approval extension (RETIRED/OUT OF SCOPE, per `FUNCTIONAL-DESIGN-MATRIX-
   SUMMARY-v0.2.md`). **Recorded as GAP-TH-01** — requires a Boss decision: request the missing source,
   treat as out-of-scope/retire (as was done for `efaplus`), or rebuild the Thai WHT certificate output
   using the generic engine in point 4 below plus Thai-specific form/category mapping.
4. **Generic Withholding-Tax-on-Payment engine — confirmed present, but NOT wired to Thailand.** Odoo's
   own generic module `l10n_account_withholding_tax` ("Withholding Tax on Payment") is present in source
   with real business methods, and is used as the base for Argentina, Cambodia, Sri Lanka, Philippines,
   Saudi Arabia, and others. **`l10n_th` does not depend on or extend this module** in the evidenced
   source. This means a working, reusable withholding-on-payment mechanism exists (ADAPT candidate: wire
   Thailand's PND income-type categories into this generic engine, rather than building a WHT payment
   engine from zero) — but it does not by itself produce a Thai-format WHT certificate; that output layer
   is the unsourced structure in point 3.
5. **Thai e-Tax Invoice / e-Receipt — GAP confirmed with a broader search.** Searched module names,
   categories, XML views, and business methods for e-invoicing/EDI keywords across the full evidence set.
   Indonesia, India, Turkey, and Colombia all have e-invoicing modules in this source; **Thailand does
   not**. This is a firm, well-searched GAP, not merely an earlier unconfirmed guess.

**Net effect on classification (see `OPEN_SOURCE_TO_SMESPLUS_GAP.md` for the authoritative register):**
Thai WHT moves from a single vague "GAP, needs Evidence Matching" to two precise items — GAP-TH-01
(Thai-specific WHT certificate output, found live/unsourced) and an ADAPT opportunity (generic
withholding-on-payment engine, present but unwired to Thailand). VAT and PromptPay QR move from
implicit/assumed REUSE to explicitly confirmed REUSE. Thai e-Tax Invoice/e-Receipt remains GAP, now with
a broader negative search backing it rather than an absence of search.

## Addendum 2 — GAP-TH-01 RESOLVED (2026-07-05, same day, source provided by Boss)

Boss provided `Archive.zip` containing 7 OCA "l10n-thailand" (https://github.com/OCA/l10n-thailand)
modules, authored by Ecosoft, with author-field credit already showing prior SMEsPlus/SCG adaptation
("SMEsPlus Clean Room, SMEsPlus Ai Team", "SCG LEGACY"):

| Module | Version | Purpose |
|---|---|---|
| `l10n_th_withholding_tax` | 19.0.1.6 | Core WHT engine — `account.withholding.tax` model, tax/product/move/payment integration |
| `l10n_th_withholding_tax_cert` | 19.0.1.5 | WHT certificate — `withholding.tax.cert`, `withholding.tax.cert.line`, `create.withholding.tax.cert` wizard |
| `l10n_th_withholding_tax_cert_form` | 19.0.1.0.3 | PND certificate print layout — adds `amount_pension_fund`, `amount_socialsecurity_fund`, `amount_provident_fund` |
| `l10n_th_withholding_tax_multi` | 19.0.1.0.3 | Multi-tax-line withholding on a single payment |
| `l10n_th_withholding_tax_report` | 19.0.1.0.2 | XLSX/QWeb WHT report export |
| `l10n_th_amount_to_text` | 19.0.1.0.1 | Thai Baht amount-to-text (used on the certificate form) |
| `l10n_th_partner`, `l10n_th_base_location` | 19.0.1.0.1 / 19.0.0.0.3 | Thai partner/address data extensions |

**Field-level verification performed:** every table and field previously found live in the DB dump with
"no source" (`withholding_tax_cert`, `withholding_tax_cert_line`, `create_withholding_tax_cert`,
`account_withholding_tax`, `income_tax_form`, `wt_cert_income_type`, `tax_payer`, `amount_pension_fund`,
`amount_socialsecurity_fund`, `amount_provident_fund`) is now traced to an exact `_name`/`fields.X`
definition in this archive — 100% match, no unexplained remainder.

**Notable clean-room decisions already made in this code** (per its own manifest comments, in Thai):
the module explicitly removes the Enterprise-only `l10n_th_reports` dependency to run on pure Community
edition, and routes PND report generation through an external gateway rather than an in-app Enterprise
report handler — both are licensing-driven adaptations, already done, not something SMEsPlus needs to
re-decide.

**Decision:** GAP-TH-01 is RESOLVED. Reclassified from "found live, source not provided" to **REUSE**
(with the SMEsPlus/SCG clean-room adaptation already applied upstream of this ADR). See
`OPEN_SOURCE_TO_SMESPLUS_GAP.md` §1 and `BUSINESS_RULE_CATALOG.md` for the extracted business rules
(certificate state lifecycle, WHT line base/percent/amount validation, PND-3/PND-53 form-type
auto-detection from tax tags).

**Open registry question (not resolved in this pass):** this archive is real Python module source code,
licensed AGPL-3, not a governance/evidence document. `AI-Collaboration-Hub`'s registered document types
(constitution, ADR, FDS, templates, evidence) do not include a "source code module" category, and the
project's own data-handling guidance for the DB dump ("store only metadata reports and diagrams in
GitHub... never commit raw exports") suggests raw module trees may belong in a separate code repository
rather than this governance repo. Flagging for Boss: confirm where `l10n_th_withholding_tax*` modules
should physically live (a new code repo, an existing one, or a `10_Modules/Accounting/vendor/` style path
in this repo) before Phase 5 (SDS/build).

## Addendum 3 — Reclassified Under ADR-0006 (2026-07-06, Clean Room Policy A)

Per **ADR-0006**, every "REUSE" verdict in this ADR is reclassified as **Concept Match**, and the
"physical storage" question in Addendum 2 is superseded, not merely reframed:

- **`l10n_th`, `l10n_th_reports`, the generic `account.tax` VAT engine, and `account_qr_code_emv`
  (PromptPay QR)** — these remain valid evidence that Thailand-specific VAT and QR-payment concepts
  are well-understood, proven patterns. They are **not** being installed into SMEsPlus. SMEsPlus's
  own VAT and PromptPay QR handling will be independently designed and implemented in the
  FastAPI/SQLAlchemy stack defined in `TECHNOLOGY_STACK_STANDARD.md`, informed by — but not
  derived from — these Odoo modules.
- **The OCA `l10n_th_withholding_tax*` suite (`Archive.zip`)** — reclassified from REUSE to Concept
  Match. These modules cannot run inside SMEsPlus's actual backend (FastAPI/Python, not the Odoo
  runtime) regardless of any licensing question, so "where should this code live in our repo" is
  moot as originally asked. It may be retained as **labeled reference material only** (e.g. a
  `99_Reference_Material/` path, never a code dependency path) for the Architecture Team to consult
  while independently designing SMEsPlus's own withholding-tax certificate feature.
- **Net effect on scope:** the Thailand-only localization *scope* decision in this ADR's main body
  (§Decision) is unchanged — SMEsPlus still targets only Thailand, not the other 521 country
  localizations. What changes is *how* that scope gets built: entirely original implementation,
  informed by Concept Match evidence, never installed reference-system code.
