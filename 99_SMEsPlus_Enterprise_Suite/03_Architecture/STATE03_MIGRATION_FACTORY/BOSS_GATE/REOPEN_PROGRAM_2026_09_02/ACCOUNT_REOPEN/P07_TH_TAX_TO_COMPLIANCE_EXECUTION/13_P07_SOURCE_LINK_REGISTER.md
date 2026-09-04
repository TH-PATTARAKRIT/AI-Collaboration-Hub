# P07 — SOURCE LINK REGISTER (SCOPE BOUNDING / EC-01)

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

This file discharges `EC-01 — Scope Bounded` of `SMEPLUS-DR-EXIT-8C-001`. Under the
project Denominator Completeness Rule a denominator is `POPULATION + PATTERN + PATH SET
+ UNIT`, and none of the four may be chosen silently by the author of the claim it
bounds. All four are declared here, before any finding is stated.

## 1. Repository and Branch Lineage

| Item | Value |
|---|---|
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Canonical branch | `SMEsPlus` |
| Working branch | `research/account-p07-th-tax-compliance-2026-09-04-001` |
| Branch point | `88f52cd7ba6dc40b8951c4bfc4e0016af7cbb7ad` (`governance: approve canonical evidence acquisition flow`) |
| Execution folder | `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT_P07_TAX_TH_2026_09_04_EXECUTION` (fresh clone) |
| Merge action | **NONE.** No merge to `SMEsPlus`. Boss decides. |
| Governance read before execution | `bootstrap/AI_BOOTSTRAP_PACKAGE.md` (`SMEPLUS-AIOS-BOOTSTRAP-001`), `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/SMEPLUS_VERY_DEEP_RESEARCH_8_CRITERIA_UNIVERSAL_EXIT_CONSTITUTION.md` (`SMEPLUS-DR-EXIT-8C-001`, effective 2026-09-04) |

## 2. PATH SET — Declared and Proven

The material research universe for P07 is the **Account module's own declared source
index**, not a habitually-searched directory. It is proven by enumeration, not asserted.

Root: `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE`

| Path-set member | Content | Manifest count |
|---|---|---|
| `01 ACCOUNT/` | Accounting application modules of the reference generation | 62 module directories |
| `02 OTHER/` | Base + enterprise addon set of the reference generation | 1371 manifests |
| `addons_extra/` | Project extra / third-party / SMEsPlus-authored modules | 69 manifests |

Enumeration command (proves the path set rather than repeating a habit):

    find "<root>/<member>" -maxdepth 2 -name "__manifest__.py" | wc -l

Generation evidence: the extra set declares `"version": "19.0.x"` throughout and the
base set contains modules introduced in the 19 line. The declared source set is
therefore the **v19 reference generation**. This is stated as an attribute of the
declared set, not as a claim about what is deployed in production (see `U-01`).

### 2.1 Path sets deliberately EXCLUDED, and why

Excluded sets exist on the same volume and were located, so their exclusion is a
decision, not an omission:

| Excluded root | Reason |
|---|---|
| `CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons` (790 manifests) | Prior-generation (v18) base. Retained as a comparison surface only. |
| `ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/smeplus-custom/{addons,WHT}` (65 + 5) | v18 project custom set. Comparison surface only. |
| `ODOO/ODOO-COMMUNITY/Odoo14/addons` (127) | v14 legacy line. Used **only** to establish that four Thai tax modules exist there and not in the declared set (`P07-N-03`). |
| `CLAUDE AI/MIGRATION/ODOO18/18.0.5_account/*` | Account-line build; near-duplicate of the declared extra set at a different version string. |
| `95_BHPRO_PROJECT/*`, `ODOO/ODOO-COMMUNITY/ODOO19/efaplus-custom/*` | Different products. Out of scope. |

## 3. POPULATION — What one member is

| Register | POPULATION | UNIT |
|---|---|---|
| Tax-relevant module population | Every module in the PATH SET whose directory name or manifest category matches the tax selector in §4 | one module directory containing `__manifest__.py` |
| Tax report population | Every `account.report` record and every report handler abstract model in the tax-relevant modules | one report definition record, or one handler model |
| Tax event population | Every code site that creates, computes or classifies a tax amount or tax tag | one call site (**not** one expression, **not** one file) |
| Statutory document population | Every document class the system can emit that a Thai statute names | one document class |
| Negative claim population | Every sentence in this package containing a system-wide negative | one sentence |

The UNIT for the tax event population is fixed as **call site** because the project has
twice recorded that counting expressions and counting sites yield different totals for
one bounded surface.

## 4. PATTERN — The selecting expressions and their false-negative modes

| Pattern | Applied to | Known false-negative modes |
|---|---|---|
| directory name `l10n_th*` | whole volume, `-maxdepth 9` | misses Thai tax logic in modules not prefixed `l10n_th` — **materialised**: `smesplus_tax_period_date`, `smesplus_account_reports`, `bm_thai_rd_vat_company_search` all carry Thai tax behaviour and do not match. Compensated by the second and third patterns. |
| literal `tax_period` | PATH SET, all file types, excluding `__pycache__`, `.po`, `.pot` | misses a differently-named tax-point field. Mitigated by reading every tax report handler in full. |
| literal `withholding` / `wt_tax` / `wht` | PATH SET | misses Thai-language identifiers. No Thai-language identifier was observed in code; labels only. |
| `account.report` / `report.handler` record and model scan | tax-relevant modules | misses reports defined outside the tax-relevant module set. |
| manifest `depends` graph closure | tax-relevant modules | none known; used to detect the missing dependency in `P07-F-20`. |

**Declared limitation of patterns 2–4:** they are name-based. A Thai tax rule
implemented with no Thai, tax, or withholding token in its identifiers would not be
selected. No compensating control for that residue was available in this session; it is
carried as `U-11`.

## 5. Tax-Relevant Module Population — Enumerated Result

| # | Module | Set | Author band | Role in P07 |
|---|---|---|---|---|
| 1 | `l10n_th` | `02 OTHER` | REF-ERP (vendor) | Thai chart, tax templates, tax groups, PP30-shaped tax report, "Tax Invoice" print title, branch-name compute |
| 2 | `l10n_th_reports` | `02 OTHER` | REF-ERP (vendor, licence `OEEL-1`) | Sales/Purchase tax report XLSX handler; PND3 and PND53 CSV handlers; single `account.return.type` |
| 3 | `l10n_account_withholding_tax` | `02 OTHER` | REF-ERP (vendor) | Generic "Withholding Tax on Payment" framework |
| 4 | `l10n_th_reports_ext` | `addons_extra` | SMEPLUS | Override of the vendor Sales/Purchase tax report XLSX generator |
| 5 | `smesplus_tax_period_date` | `addons_extra` | SMEPLUS | Introduces a tax period date on the document header and on move lines |
| 6 | `smesplus_account_reports` | `addons_extra` | SMEPLUS | Sale/Purchase VAT reports and zero-rate variants; consumes the tax period date |
| 7 | `l10n_th_withholding_tax` | `addons_extra` | Third-party (OCA/Ecosoft), SMEsPlus-refactored | WHT master data, WHT on payment register, PND report override |
| 8 | `l10n_th_withholding_tax_cert` | `addons_extra` | Third-party, co-authored SMEsPlus | s.50 bis certificate model and creation wizard |
| 9 | `l10n_th_withholding_tax_cert_form` | `addons_extra` | Third-party, co-authored SMEsPlus | Certificate print form |
| 10 | `l10n_th_withholding_tax_report` | `addons_extra` | Third-party | WHT report wizard, XLSX/PDF/HTML WHT report |
| 11 | `l10n_th_withholding_tax_multi` | `addons_extra` | Third-party | Multiple WHT taxes on one payment |
| 12 | `l10n_th_partner` | `addons_extra` | Third-party | Thai partner naming, company type (title), **`branch` = Tax Branch** |
| 13 | `l10n_th_amount_to_text` | `addons_extra` | Third-party | Thai amount in words (certificate form) |
| 14 | `bm_thai_rd_vat_company_search` | `addons_extra` | Third-party (proprietary `OPL-1`) | Partner master data from the Revenue Department VAT service API |
| 15 | `l10n_th_base_location` | `addons_extra` | Third-party | Thai address hierarchy |

`POPULATION = 15`. Modules 1–3 are vendor; 4–6 are SMEsPlus-authored; 7–15 are
third-party, three of them carrying SMEsPlus co-authorship in the manifest.

## 6. Evidence Citation Convention

Layer-2 citations in this package take the form
`<module>/<relative path>:<line>` and, where a behaviour is named,
`— <method>`. These citations are **audit quarantine** and must not be transcribed into
any Layer-1 reference package, per the Clean Room Learning Directive. The mechanical
scrub result for the Layer-1 file is recorded in `14_P07_EVIDENCE_MANIFEST.md` §4.

## 7. Not Performed in This Session

Declared so that no reader mistakes silence for coverage.

| Not performed | Consequence |
|---|---|
| Any query against a live or dump database | No finding in this package is a runtime observation. All are source-derived. Recorded as `U-02`. |
| Any determination of which addon copy is deployed | Findings bind to the declared source set only. Recorded as `U-01`. |
| Any execution of the reference ERP | No behavioural confirmation of the ORM-decorator observations (`P07-F-27`). |
| Any Jira transition or issue creation | Jira lineage is stated as required-and-not-yet-created in `18_P07_PMO.md` §6. |
| Any merge, implementation, or design authorisation | Prohibited by the session directive and by `SMEPLUS-DR-EXIT-8C-001` §9. |
