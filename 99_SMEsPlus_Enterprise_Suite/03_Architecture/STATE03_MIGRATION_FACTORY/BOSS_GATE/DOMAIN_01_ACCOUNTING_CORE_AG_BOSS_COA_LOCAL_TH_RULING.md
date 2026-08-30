# DOMAIN_01 Accounting Core — Boss Ruling: SMEsPlus Thailand COA Standard & Odoo-like Account Type UX

Date: 2026-08-30

## Authority

Boss = Sole Final Approver.

This ruling resolves and refines `D01-GATE-A3 — Chart of Accounts Template / Instance Structure` for the SMEsPlus Thailand localization baseline.

## Boss Decision

**APPROVED WITH CONTROL — SMEsPlus Thailand COA STANDARD BASELINE.**

### 1. Product Localization Scope

SMEsPlus Accounting Core is to be designed for **Thailand localization as the active product target**.

For COA learning / standardization, the authorized learning scope is narrowed to **Thai chart-of-accounts material only**. Non-Thai localization COA sources are excluded from this COA-standardization work unless Boss separately reopens scope.

This narrowing applies to the COA learning/design workstream. It does not silently redefine unrelated project domains.

### 2. Standard COA Source Basis

The user-supplied workbook:

`Account_Odoo18_19 sent 270369.xlsx`

Sheet / Tab:

`Odoo18`

is approved as the **primary business-facing seed/reference dataset** for constructing the SMEsPlus Standard Thai COA Candidate.

The controlled transformation is:

`Odoo18 Tab COA → Business Meaning → SMEsPlus Canonical Accounting Classification → SMEsPlus Standard Thai COA Template → Company/Tenant COA Instance`

The Odoo18 tab is a reference/business dataset source. It is not authorization to clone Odoo ORM, database schema, source code, technical IDs, field architecture, module architecture, or vendor implementation.

### 3. Account Type Direction

Boss requires the **Account Type user experience and classification vocabulary to remain familiar to Odoo users**, because this reduces operating friction and matches the Boss/user working familiarity.

Therefore:

- Account Type labels/grouping may use an **Odoo-like business-facing mental model** where the terms are generic accounting/business concepts.
- SMEsPlus must own its own canonical internal identifiers and rules.
- Odoo technical enum keys, ORM fields, IDs, model names, schema relationships, or implementation mechanics are not target-design authority.
- Account Type must remain independent from Account Code so renumbering an account does not change its accounting meaning.

Target principle:

`Odoo-like familiarity at UX/business-semantics layer; SMEsPlus-owned canonical model underneath.`

### 4. COA Template / Instance Architecture

SMEsPlus shall separate:

1. `SMEsPlus Standard Thai COA Template`
2. `Company/Tenant COA Instance`
3. `Source Mapping Layer`

A Company/Tenant may extend its COA instance under governance, but extension must not break canonical classification, financial-statement mapping, multi-company consolidation, migration traceability, or reporting semantics.

### 5. Source Mapping Rule

Migration / conversion shall use:

`Source Account → Business Meaning → SMEsPlus Canonical Classification → SMEsPlus Company Account`

Not:

`Vendor Account ID/Code → copied target identity`

Source IDs/codes may be retained as provenance/mapping metadata but must not become SMEsPlus canonical identity.

### 6. Express Benchmark Position

The previously discussed Express-like familiarity remains a **usability/reference benchmark only**.

For the initial SMEsPlus Thailand standard COA, the approved primary seed is now the **Odoo18 tab in the Boss-provided workbook**.

Therefore the hierarchy is:

1. Thai accounting/business truth and regulatory requirements
2. Boss-approved `Odoo18` tab as Standard Thai COA seed/reference
3. Odoo-like Account Type familiarity
4. Express-like usability familiarity where useful
5. SMEsPlus independent clean-room canonical design

### 7. Clean-Room Boundary

Absolute prohibitions remain:

- No Odoo source-code reuse
- No ORM cloning
- No database-schema cloning
- No vendor technical-ID cloning
- No workflow/state-machine cloning
- No module-architecture cloning

Allowed:

- Learn from business-facing account names/codes/classifications in the authorized COA dataset
- Preserve Thai accounting semantics
- Use familiar generic accounting terminology
- Build independent SMEsPlus canonical classifications, rules, controls, and migration mappings

### 8. Thailand-Only COA Learning Scope

For the COA standardization workstream:

- Thai COA sources: IN SCOPE
- `l10n_th` / Thailand-specific accounting semantics: IN SCOPE where authorized and clean-room-safe
- Non-Thai localization COA: OUT OF CURRENT COA LEARNING SCOPE
- Vendor technical implementation: RESTRICTED / NOT TARGET INPUT

### 9. Remaining Controlled Work Before COA Blueprint Freeze

The following must still be evidenced before the exact COA table is frozen:

1. Extract and inventory the actual `Odoo18` tab rows/columns from the Boss-provided workbook.
2. Identify account code, account name, Account Type, grouping/classification, active/inactive or other business-facing attributes actually present.
3. Detect duplicates, gaps, ambiguous classifications, and Thai-specific accounts.
4. Produce `Reference → Canonical Classification → SMEsPlus Standard Thai COA Candidate` mapping.
5. Produce Account Type mapping with Odoo-like user-facing labels and SMEsPlus-owned canonical IDs.
6. Verify Balance Sheet / P&L classification and Thai VAT/WHT/accounting dependencies.
7. Preserve multi-company/consolidation compatibility.
8. Submit the exact COA Candidate for evidence review before Blueprint Freeze.

No uninspected spreadsheet row or field may be represented as verified content.

## Gate Effect

`D01-GATE-A3 — COA Template / Instance Structure = BOSS APPROVED WITH CONTROL`

Approved direction:

- Thailand-only product/localization target for COA standardization
- Odoo18 tab = primary Standard Thai COA seed/reference
- Account Type = Odoo-like business-facing familiarity
- Canonical model = SMEsPlus-owned
- Template → Company/Tenant Instance → Source Mapping separation

Still pending before exact COA content freeze:

`Controlled workbook extraction + canonical mapping + evidence verification.`

This decision does not authorize Development or Production.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
