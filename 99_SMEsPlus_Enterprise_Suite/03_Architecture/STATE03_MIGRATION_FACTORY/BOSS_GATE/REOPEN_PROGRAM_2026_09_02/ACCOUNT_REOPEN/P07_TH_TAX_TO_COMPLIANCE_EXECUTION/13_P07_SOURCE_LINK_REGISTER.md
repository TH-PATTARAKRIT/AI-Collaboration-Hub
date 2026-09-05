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

Two truncations in that command are disclosed here because they were undeclared in the
first issue of this register:

- Removing `-maxdepth 2` returns **1374** for `02 OTHER`, not 1371. The three extra are
  install-test fixtures nested at depth 13 inside `base/tests/`. The depth limit is doing
  exclusion work and is now stated as such.
- `addons_extra` contains **71** entries, not 69: the 69 module directories plus two
  archives, `l10n_th_withholding_tax_cert_form.zip` and `l10n_th_withholding_tax_multi.zip`
  — archived copies of population members, inside the PATH SET, never opened or
  version-compared in this session. Carried as `P07-U-22`.

Generation evidence: the extra set declares `"version": "19.0.x"` throughout and the
base set contains modules introduced in the 19 line. The declared source set is
therefore the **v19 reference generation**. This is stated as an attribute of the
declared set, not as a claim about what is deployed in production (see `U-01`).

### 2.0 A Caveat On This Register Itself — It Orders as Well as Bounds

Added after this register was shown to have **selected** a piece of evidence, not merely
bounded it. Sharpened by P11 from P07's own account of the failure, and recorded as a
standing caveat on §2:

> A declared scope register bounds the evidence and, in doing so, also **orders** it. If the
> register is consulted before the ranking, **the register is the ranking** — and its ordering
> was chosen for *containment*, not for *relevance*.

The concrete instance is `22 §8.3`. A database sits inside the PATH SET declared above, so it
was the one opened first, and an entire runtime section was built on it. It is the **broadest
module install** available and therefore a defensible choice for configuration claims — but it
holds 23 accounting lines against another database's 447,384, and it was used to support
**population negatives** as well. That cost a published finding (`P07-F-60`, withdrawn).

**Declaring a scope does not exempt selection within it from also being declared.** The
practical consequence for anyone reading or extending this register:

1. This §2 answers *what may be used as evidence*. It does **not** answer *which item to
   reach for first*, and it must not be read as answering it.
2. Any claim resting on one member of the PATH SET must state **why that member** — and, if
   the members differ in scale or shape, **rank them with the unit declared** (`22 §8.3`).
3. The right member depends on the **kind of claim**: configuration and schema questions want
   the broadest artefact; population and operational questions want the deepest. Both kinds
   appeared in this package and were not distinguished until after publication.

### 2.1 Path sets deliberately EXCLUDED, and why

Excluded sets exist on the same volume and were located, so their exclusion is a
decision, not an omission:

All excluded roots below are absolute paths on the `/Volumes/iMacSys` volume, **not**
relative to the execution folder in §1. The base was undeclared in the first issue of this
register and is stated here.

| Excluded root | Reason |
|---|---|
| `CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons` (790 manifests) | Prior-generation (v18) base. Retained as a comparison surface only. |
| `ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/smeplus-custom/{addons,WHT}` (65 + 5) | v18 project custom set. Comparison surface only. |
| `ODOO/ODOO-COMMUNITY/Odoo14/addons` (127) | v14 legacy line. Used **only** to establish that four Thai tax modules exist there and not in the declared set (`P07-N-03`). |
| `CLAUDE AI/MIGRATION/ODOO18/18.0.5_account/*` | Account-line build; near-duplicate of the declared extra set at a different version string. |
| `95_BHPRO_PROJECT/*`, `ODOO/ODOO-COMMUNITY/ODOO19/efaplus-custom/*` | Different products. Out of scope. |
| `ODOO/ODOO-COMMUNITY/ODOO19/SMEsPlus-SMEsPlus_Extra19` (83 manifests) | **Same generation as the declared set and a strict superset of it for the P07 modules** — it contains all nine Thai withholding modules *and* `account_payment_multi_deduction`. Added after independent challenge. |
| `CLAUDE AI/MIGRATION/SMEsPlus19/01_extra_module/SMEsPlus_19.0.2` (75 manifests) | Same generation; also contains `account_payment_multi_deduction`. Added after independent challenge. |
| `CLAUDE AI/SMEsPlus/SMEsPlus_19.0.20260418/.../01_extra/addons_extra` (69 manifests) | Same generation and the same module count as the declared set; does **not** contain `account_payment_multi_deduction`. Added after independent challenge. |

**Consequence for `P07-D-01`.** Two of the three roots above are the same generation as the
declared set and do contain the dependency that `P07-D-01` reports as unsatisfiable. That
finding is therefore an artefact of **set composition**, not of a missing artefact, and it
cannot be closed until the Boss fixes which extra-addon set is canonical (`U-01`). Stated
here rather than left implied.

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

`POPULATION = 15` **as first enumerated. That enumeration was refuted during independent
challenge and is corrected in §5.1.**

### 5.1 Population Correction — the First Enumeration Was Incomplete

The population of 15 above was produced by the four name-based patterns of §4. Independent
challenge established that it is **not closed under this register's own PATTERN 5**
(manifest `depends`-graph closure), which was declared with "none known" false-negative
modes and then not run to closure. Running it adds ten members that are in the PATH SET and
were outside the population:

| Added member | Set | Why it is tax-relevant |
|---|---|---|
| `partner_company_type` | `addons_extra` | Defines `partner_company_type_id`, the field behind the statutory `Title` column of PND3 and PND53, and behind the partner's stored legal name. **It is cited as evidence in `20 §6` and registered as a broken dependency in `12 §1` while sitting outside the population** — evidence base and population were different sets. |
| `partner_firstname` | `addons_extra` | Imported by `l10n_th_partner/models/res_partner.py:7`; supplies the name composition that produces the payee name on statutory output. |
| `convert_amount_text_to_thai` | `addons_extra` | **Byte-identical duplicate of population member 13** (`l10n_th_amount_to_text`) except for one description asset; same version string, same override of the Thai amount-in-words used on the s.50 bis certificate. Matches none of the four declared patterns — this is the `U-11` residue **materialised**, and it was findable by a `*thai*` glob that was never run. `P07-F-48`. |
| `account_update_tax_tags` | `01 ACCOUNT` | Manifest: *"Allow updating tax grids on existing entries."* A module in the declared set whose entire purpose is mutating tax tags on already-posted moves — i.e. mutating the inputs to the statutory registers after filing. Directly material to `08 §4` `A-15` and to `19` `POS-9`, and absent from the first issue of this package. `P07-F-49`. |
| `report_xlsx`, `report_xlsx_helper`, `date_range`, `base_location`, `base_location_geonames_import` | `addons_extra` | Declared dependencies of the WHT report module; carry the date-range and export machinery of a statutory report. |
| `account`, `account_reports`, `account_qr_code_emv` | `01 ACCOUNT` | The frameworks every finding in this package resolves into. |

**Corrected `POPULATION = 25`** (15 + 10). Three of the ten are materially tax-bearing in
their own right (`partner_company_type`, `convert_amount_text_to_thai`,
`account_update_tax_tags`); the remainder are framework and utility members whose inclusion
matters for dependency closure rather than for tax semantics.

**Method finding, recorded against this register itself.** The defect is not that a pattern
was missing — PATTERN 5 was declared, with its false-negative modes acknowledged as "none
known" — but that a **declared pattern was not run to closure**. Under the project's
Denominator Completeness Rule this is a PATTERN failure, not a PATH SET failure, and the
PATH SET is the half this register spends its length proving. Carried as `REV-E-11` in
`15 §4`.

### 5.2 PND Token Census — Corrected

`03 §4.1` cited a token census as the proof of its denominator. Re-run with this register's
declared exclusions (text files only, `__pycache__`, `.po` and `.pot` excluded), the counts
are:

| Token | First issue | Corrected |
|---|---|---|
| `pnd3` | 105 | **99** |
| `pnd53` | 92 | **77** |
| `pnd3a` | 12 | **9** |
| `pnd1` | 10 | **12** |
| `pnd 54` | 1 | **2** |
| `pnd2` | 0 | **1**, and that one hit is base64 noise inside an unrelated theme asset |

The first issue's counts were taken without the declared exclusions and included
translation catalogues; `pnd1` moved in the opposite direction, which is the signature of an
undeclared filter rather than a simple over-count. **The qualitative conclusions of
`03 §4.1` are unchanged** — PND 54 is provisioned in the chart and nowhere else, and no
genuine PND 2 artefact exists — but a denominator that does not reproduce is a defect in
its own right. `REV-E-12`.

## 6. Evidence Citation Convention

Layer-2 citations in this package take the form
`<module>/<relative path>:<line>` and, where a behaviour is named,
`— <method>`. These citations are **audit quarantine** and must not be transcribed into
any Layer-1 reference package, per the Clean Room Learning Directive. The mechanical
scrub result for the Layer-1 file is recorded in `14_P07_EVIDENCE_MANIFEST.md` §4.

## 7. Not Performed in This Session

Declared so that no reader mistakes silence for coverage.

**Each entry is marked `TESTED` or `ASSUMED`**, per the proposed clause 2.4 of
`SMEPLUS-DR-EVSUB-001-PROPOSED` §2.1b: *a statement that something is unavailable to a
session is a capability claim, and a capability claim is evidence — it must be tested before
it is relied on.* The distinction was added after a peer registered having asserted four
times in writing that it could not open its peers' registers, having never tested it, when
they were one fetch away. This session made the same class of claim about Jira and did test
it; it made no claim at all about peer branches and, when the question arose, fetched them.

| Not performed | Consequence |
|---|---|
| ~~Any query against a live or dump database~~ — **TESTED, AND THE CLAIM WAS FALSE.** A 65 MB PostgreSQL dump of the declared generation sits inside this register's own PATH SET, at `01 ACCOUNT/SOURCE CODE/iTEST02_2026-06-14_14-41-19.dump`, and was printed by a directory listing this session ran in its first minutes. | **Superseded by `22_P07_RUNTIME_EVIDENCE.md`.** Five findings are now runtime-verified and one refined. `U-02` no longer bounds them. Struck rather than deleted, per obligation 5c. `REV-E-24`. |
| Any determination of which addon copy is deployed | Findings bind to the declared source set only. Recorded as `U-01`. |
| Any execution of the reference ERP | No behavioural confirmation of the ORM-decorator observations (`P07-F-27`). |
| Any Jira transition or issue creation — `TESTED`. The connectors are present and unauthorised, and cannot be authorised from a non-interactive session. | Jira lineage is stated as required-and-not-yet-created in `18_P07_PMO.md` §6. |
| Any merge, implementation, or design authorisation | Prohibited by the session directive and by `SMEPLUS-DR-EXIT-8C-001` §9. |
