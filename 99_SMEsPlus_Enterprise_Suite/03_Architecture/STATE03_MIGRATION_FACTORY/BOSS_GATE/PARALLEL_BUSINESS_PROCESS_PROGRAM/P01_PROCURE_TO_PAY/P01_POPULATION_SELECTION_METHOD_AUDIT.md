# P01 — POPULATION-SELECTION METHOD AUDIT

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S18-10`
Trigger: `ERR-P01-23` — the evidence population was scoped by **directory** rather than by
**pattern**, which concealed a whole deployed database that this session's own notes already named.

**The finding of this audit: `ERR-P01-23` was not a single mistake. It is a recurring method
defect, and this run found two further live instances of it — one of them in the source path set
that every P01 code citation depends on.**

---

## 1. THE FAILURE MODES BEING AUDITED FOR

| Mode | Description |
|---|---|
| **M1** | Population scoped by **directory** where it should be scoped by **pattern** |
| **M2** | Enumeration by **filename or extension** rather than by content or format |
| **M3** | **First artefact found** selected, with no declared ranking unit |
| **M4** | A **labelled version** accepted without content proof |
| **M5** | Identity keyed on something other than a **stable identifier** |
| **M6** | A **declared set never intersected with the deployed set** |
| **M7** | An enumeration run at **one pattern width only**, never reconciled against a second |

---

## 2. INSTANCE 1 — `ERR-P01-23` (previously recorded, restated for lineage)

| Field | Value |
|---|---|
| Original population method | Database artefacts enumerated within `~/Downloads` |
| Failure mode | **M1**, compounded by **M2** |
| Corrected method | Enumerate by pattern across the home directory; key identity on `database.uuid` |
| Affected finding | *"No readable deployed series-18 database exists"* — and the two statements built on it |
| Materiality | **Governing.** The round's central conclusion was false |
| Status | **CORRECTED** in the previous round; lineage preserved |

---

## 3. INSTANCE 2 — THE ESTATE CENSUS IS STILL INCOMPLETE (NEW)

| Field | Value |
|---|---|
| Original population method | The round-4 census, re-keyed on `database.uuid` after peer P04's report, returned **five** identities across ten artefacts |
| Failure mode | **M1 again** — the corrected census still did not sweep `~/OCC_BACKUP` |
| Evidence | `idemo18_uat` carries `database.uuid = 551ab874-9acb-11f1-b150-6ec7a480be3d`, which is **not** among the five (`45a8e08e`, `1f6338ae`, `f4a44cce`, `66d1b52a`, `a1430edc`). Peer P04 subsequently identified **two further series-18 identities** — `4b766580` and `96548e18` — which this run also did not hold |
| Corrected method | The estate is **at least six identities across at least eleven artefacts** |
| Affected finding | Every count of the form "the estate has N deployments" |
| Materiality | **High.** The correction to `ERR-P01-23` repaired the *conclusion* without repairing the *method* that produced it |
| Status | **OPEN — floor raised to eight by peer delta.** Peer **P04** (`9e377e30`, §6A.27) has since completed a full-host census: **39 artefacts** under a declared path set (`/Volumes` + `$HOME`), size bound ≥ 1 MB, **two** content signatures (`PGDMP` magic **and** a zip central directory containing `dump.sql`), yielding **8 keyed identities** — and P04 explicitly **declines to state a total**. P01 adopts eight as the floor and likewise states no total. P04 also records that its own two sweeps each missed `96548e18`: a `.zip` defeats a `PGDMP` signature scan, and a 2025 date defeats a `*_2026-*` name pattern — **two independent bounds inside the sweep written to reconcile the first**. See `P01_S18_PEER_DELTA_HANDOFF.md §2.4` |

**This is the uncomfortable part of the audit.** After `ERR-P01-23` was diagnosed *precisely* as a
directory-scoped population, the very next census was still directory-scoped. Diagnosing a method
defect and repairing the finding it caused are not the same act.

---

## 4. INSTANCE 3 — THE SOURCE PATH SET DOES NOT CONTAIN THE DEPLOYED CODE (NEW)

The declared source path set (`E00_P01_PRIMARY_EVIDENCE_BASE.md §1`) names five roots. `R4` —
`/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/smeplus-custom/addons` — is declared as
"the project's own addon set" for the v18 line.

**POPULATION:** the 16 custom modules installed in the series-18 deployment.
**PATTERN:** `find /Volumes/iMacSys -type d -name "<module>"`, full depth, per module.
**UNIT:** one module directory. **MEASURE:** `version` in `__manifest__.py`, compared to the
deployed `ir_module_module.latest_version`.

| Deployed module | Version | Copies on volume | Version match | Where the matching copy is |
|---|---|---|---|---|
| `purchase_request` | 18.0.1.10.0 | 16 | **no** | — |
| `scgl_account_coa_control` | 18.0.1.0.1 | 1 | **no** | (only copy is under `97_OCC_PROJECT`) |
| `scgl_chatter_compact` | 18.0.1.1.0 | **0** | no | — |
| `scgl_custom_title_and_favicon` | 18.0.0.0.2 | 10 | **yes** | `CLAUDE AI/SMEsPlus/SMEsPlus18/02_base_Extramodule/…` |
| `scgl_dashboard_core` | 18.0.1.3.3 | 3 | **no** | — |
| `scgl_date_range_auto_period` | 18.0.1.0.0 | 1 | **yes** | `ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/` |
| `scgl_delivery_cost` | 18.0.1.0.0 | **0** | no | — |
| `scgl_document_terms_conditions` | 18.0.1.0.0 | **0** | no | — |
| `scgl_multi_approve_core` | 18.0.0.3.1 | 3 | **yes** | `ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/` |
| `scgl_multi_approve_purchase_request` | 18.0.1.0.0 | **0** | no | — |
| `scgl_occ_transportation_costs` | 18.0.1.0.0 | 1 | **yes** | `ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/smeplus-custom/` |
| `scgl_product_category_company` | 18.0.1.5.0 | 2 | **yes** | `ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/` |
| `scgl_signature` | 18.0.1.0.0 | **0** | no | — |
| `scgl_signature_hr_expense` | 18.0.1.0.0 | **0** | no | — |
| `scgl_stock_fleet` | 18.0.1.0.0 | **0** | no | — |
| `scgl_uom_archive` | 18.0.1.0.0 | 1 | **yes** | `ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/` |

### 4.1 What this says

- **A version match is necessary, not sufficient.** Peer P04 (`P04-F-97`, relaying P07) records
  that two code bodies can share one version string — 17–179 changed lines across seven files in
  P07's case — and that a display name and version can span two technical identities. **Neither
  name nor version identifies deployed code.** The counts below are therefore an **upper bound** on
  how much of the deployed custom code is available here, never a statement that it *is* available.
  Where this package reads a custom module's *behaviour* it corroborates at schema level instead —
  see `P01_S18_PEER_DELTA_HANDOFF.md §2.3`.
- **6 of 16** deployed custom modules have a version-matching source copy. **10 do not** — of
  which **7 have zero copies by name anywhere on the volume**, and 3 exist only at other versions.
- **None of the 6 matching copies is inside `R4`.** Five are one directory level *above* it, at
  `ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/`; one is under `CLAUDE AI/SMEsPlus/SMEsPlus18/…`.
  `scgl_occ_transportation_costs` is under `smeplus-custom/` but **not** under `smeplus-custom/addons`.
- `scgl_account_coa_control` exists in exactly one place: **`/Volumes/iMacSys/97_OCC_PROJECT`** — a
  root P01 explicitly declared **CLASS C — NOT YET SEARCHED**. And the deployment under study
  **is** the OCC deployment: `web.base.url = https://occ.smeplus.cloud`, and the archive is
  `…_pre_scgl_occ_website_….dump`.

| Field | Value |
|---|---|
| Failure mode | **M1** (directory-scoped, and one level too deep), **M6** (declared set never intersected with the deployed set) |
| Affected finding | Every P01 statement about custom-module behaviour in the v18 line |
| Materiality | **High.** The path set that carries P01's code citations does not contain the code this deployment runs |
| Status | **OPEN — method corrected, path set not yet re-declared.** Re-declaring the P01 source path set is a change to the evidence base of four published rounds and is **not** done unilaterally at the end of a run; it is raised as a decision item |

### 4.2 The exclusion reason was stated, and stating it stopped the audit

`97_OCC_PROJECT*` was excluded as CLASS C with a stated reason. A stated exclusion reason reads as
authority and ends the enquiry. It was not authority: it was a scoping convenience, and the
excluded root turned out to hold the only copy of a deployed module for the deployment now under
study. **A negative about the evidence base needs the same authority as a negative about the
subject.**

---

## 4A. INSTANCE 4 — THE CUSTOM-MODULE POPULATION WAS NAME-SCOPED, AND THE CORE PATH SET IS INCOMPLETE (NEW)

> **`ERR-P01-32`.** Found by AAS-03 Expert C under the assignment *"find another
> population-selection defect"*. Verified here before adoption.

**Two defects, one enumeration.**

### 4A.1 The custom-module population was selected by NAME, not by membership

§4 above enumerates **16** installed custom modules. That 16 is the output of a **name pattern** —
`scgl_*` plus `purchase_request`. It is not the set of installed modules that are not core.

The membership test — intersect the 361 installed modules against the declared source roots —
gives a different answer:

| Test | Result |
|---|---|
| Installed modules | **361** |
| Not present in `R1` (`.../odoo/addons`, 798 directories) | **66** |
| Not present in `R1 ∪ R2` (`… ∪ .../odoo/addons_archive`, 962 directories) | **55** |
| The population §4 actually enumerated | **16** |

**39 installed non-core modules were never enumerated.** Among them:

- **the entire Thai withholding-tax stack** — `l10n_th_withholding_tax` 18.0.1.4,
  `l10n_th_withholding_tax_cert` 18.0.1.3, `l10n_th_withholding_tax_cert_form` 18.0.1.0.2,
  `l10n_th_withholding_tax_report` 18.0.1.0.1 (all Ecosoft / OCA). See §4A.3 — this changes a
  published P01 attribution.
- **`om_data_remove` 18.0.1.0.0 — installed.** Peer process **P06** recorded this module as
  deleting ledger data without authorisation. **It is live in this deployment too.** Not analysed
  here; P06 owns it, and it is flagged to P06 and P11 rather than re-derived.
- `account_payment_multi_deduction`, `hr_expense_petty_cash` (both Ecosoft/OCA),
  `account_invoice_fixed_discount`, `bi_print_journal_entries`, `journal_entries_report`,
  `full_summarize_bills`, `print_voucher_request`, `date_range`, `report_xlsx`,
  `stock_card_report`, `construction`, `equipment_sequence`, `product_stock_equipment`,
  `inherit_inventory`, `inherit_sales`, `delivery_cement_truck`, `hr_payroll_other_input`,
  `invoice_promptpay`, `l10n_th_partner`, `l10n_th_amount_to_text`, `base_location` and others.

**Every negative source claim in this package inherits that gap.** `P01_S18_PERIODIC_PERPETUAL_POLICY_PROOF.md §12`
already scopes its negatives to *"method-level override unverified"*; the correct denominator for
that scope is **55 modules, not 16**.

### 4A.2 `R1` is not the deployed core — a second root was never declared

**66 installed modules are absent from `R1`; only 55 are absent from `R1 ∪ R2`.** The eleven in the
gap — including `fleet`, `account_fleet`, `hr_fleet`, `documents_fleet`, `snailmail`,
`construction`, `journal_entries_report` — live in `.../odoo/addons_archive` (**962 directories**).

`R2` **is** in P01's declared path set, described as *"modules present in the build but outside the
active addons root"*. But every core citation in five rounds of P01 has been made against `R1`
alone, on the working assumption that `R1` is the core. **For this deployment it is not.** The
deployed core is `R1 ∪ R2`, and any absence proved against `R1` alone is a narrower claim than it
appears.

*This is how `ERR-P01-30` happened.* The bill-line override was declared absent from series 18 on
the strength of a **file name** missing from one directory listing. Two scoping errors of the same
family — one about which root, one about which unit — produced a published falsehood.

### 4A.3 A published attribution that this correction overturns

P01 has recorded the deployment's withholding mechanism as belonging to `l10n_th 18.0.2.0`.
**`l10n_th` contains no withholding-tax code at all.** Across the 798 modules of `R1`, a search for
`withholding.tax.cert` and `account.withholding.tax` returns **zero** hits; `l10n_th` is a
chart-of-accounts, EMV QR and report-layout module (17 files, author *Almacom*). The mechanism
belongs to the **four OCA/Ecosoft modules named in §4A.1**, resolved from `ir_model_data`
ownership of `ir.model` records — and all four have **version-matching source inside `R4`**, which
§4 could not see because §4's population was the 16-module name pattern.

| Field | Value |
|---|---|
| Failure mode | **M6** (declared set never intersected with the deployed set), plus a name-scoped population — the same family as `ERR-P01-23` and `ERR-P01-25` |
| Affected | every P01 statement about the deployment's custom-module surface, and the withholding-mechanism attribution |
| Materiality | **High.** The unenumerated 39 include the WHT stack and a module a peer records as deleting ledger data |
| Status | **CORRECTED as to the denominator (55) and the WHT attribution.** The 39 are **not** analysed in this run; recorded as an open action |

### 4A.4 And a customization surface no module list can show

`web_studio` 18.0.1.0 is **installed**, with 341 `web_studio` xmlids, and `res_company` carries
Studio fields `x_scgl_wip_control_enabled` (true on companies 3 and 4) and
`x_scgl_project_wip_account_id` (accounts 705 / 706). **Studio customisations are data, not
modules**, so no module census — at any pattern width — can enumerate them. They are inert today
because companies 3 and 4 hold zero journal entries. **This is a fifth surface, and this package
has not swept it.**

---

## 5. WHAT THIS AUDIT DID *NOT* FIND

Stated so the audit is not read as wider than it is.

| Checked | Result |
|---|---|
| **M4** — version accepted from a label | Not found in this run. Every version here is read from `ir_module_module.latest_version` or from a `__manifest__.py`, never from a directory or file name. The archive name `idemo18_uat` is explicitly excluded as evidence |
| **M5** — identity on an unstable key | Not found in this run. Database identity is keyed on `database.uuid`; module identity on name **and** version |
| **M3** — first-found selection | Not found in this run; but see §3 — an incomplete census cannot rule out a better artefact existing elsewhere |
| **M7** — single pattern width | **FOUND — §4A.** The 16-module sweep was run at one width and one *kind* of predicate (a name pattern). Re-run as a **membership** test against the declared roots it returns **55**, not 16 |

---

## 6. THE DURABLE LESSON

**Five** instances now, all the same shape:

> The reasoning over what was read was sound. **What was read was the wrong set.**

And the compounding lesson from §3, which is new and worse:

> **Correcting the finding is not correcting the method.** `ERR-P01-23` was diagnosed exactly right
> and the next census repeated the same scoping error. A method defect is closed by re-running the
> enumeration, not by describing it.

Operationally, before any population-dependent claim:

1. Scope by **pattern**, never by directory.
2. Run the enumeration at **two widths** and reconcile — agreement is evidence, disagreement is a finding.
3. **Intersect the declared set with the deployed set**, in both directions — and intersect by
   **membership**, not by a name pattern. A name pattern is a guess about how things are called;
   membership is a measurement.
4. Resolve every artefact the session's own notes already name.
5. Treat a stated exclusion reason as a **claim requiring authority**, not as authority.
6. **Make the unit of the search the unit of the claim.** A directory is not a population
   (`ERR-P01-23`); a file name is not a behaviour (`ERR-P01-30`); a day is not a period
   (`ERR-P01-28`); a name pattern is not a membership (`ERR-P01-32`). **Four of this programme's
   errors are one error.**

Carried to memory as the standing method rule; cross-referenced to the programme's
denominator-completeness and evidence-location standards.
