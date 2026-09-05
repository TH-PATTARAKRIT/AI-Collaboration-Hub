# P01 — SERIES-16 MODULE SOURCE ↔ DEPLOYMENT MATRIX

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Baseline: `f76e443df3b3e7c9545ca731f0d963a96d636ca0`
Checkpoints: `CP-P01S16-01`, `CP-P01S16-02`

**No external acquisition occurred in this run.** Every source artefact cited is on the
Boss-controlled host and was located through the local estate or the completed local manifest index.

---

## 1. DEPLOYMENT IDENTITY

| Property | Value | Instrument |
|---|---|---|
| Archive | `~/Downloads/iSMEs_2026-07-11_05-03-27.dump` | filesystem |
| Size / format | 155,443,710 bytes, CUSTOM, dump version 1.14-0 | `pg_restore -l` |
| Archive created | 2026-07-11 05:03:27 +07 | `pg_restore -l` |
| Declared dbname | `iSMEs` | `pg_restore -l` |
| Engine | PostgreSQL **15.7** (Debian) | `pg_restore -l` |
| TABLE DATA entries | **651** | TOC |
| **`database.uuid`** | **`45a8e08e-5dcd-11ee-90f5-5242ea102159`** | `ir_config_parameter` |
| `database.create_date` | 2023-09-28 07:04:31 | `ir_config_parameter` |
| `web.base.url` | **`https://swr.smeplus.asia`** | `ir_config_parameter` |
| Companies | **1** — บริษัท ข้าวสุวรรณภูมิ จำกัด (a rice miller) | `res_company` |

### 1.1 This is a different project from the series-18 estate

The series-18 deployment verified in the previous round is `551ab874`, `occ.smeplus.cloud`, **4 companies**,
a concrete business. This is `45a8e08e`, `swr.smeplus.asia`, **1 company**, a rice miller.

**They are different businesses on different generations.** Nothing in this document is a claim about the
series-18 deployment, and nothing in the previous round's documents is a claim about this one. Where the two
are compared it is stated explicitly and the comparison is drawn only after each was classified alone.

---

## 2. SOURCE ROOTS — RANKED BEFORE CHOOSING

Three complete series-16 cores exist on this host (`ERR-P01-41`). **Convenience of location was not allowed to
select the evidence base**; they were ranked against the deployment.

### 2.1 A correction to `ERR-P01-41`'s own reading, made in this run

The first ranking counted `odoo/addons` and found 955 / 31 / 32, which suggested two of the three were not
true cores. **That reading was wrong.** Two of the trees use the **split layout**: `odoo/addons/` holds only
`base` and the `test_*` modules, and the business modules live in `<root>/addons/` — **461** and **464** of them,
including `purchase`, `stock_account` and `l10n_th`.

**All three are complete series-16 cores. The `ERR-P01-41` count of 3 stands.** A correction that was itself
about reading the wrong location was nearly published from reading the wrong location.

### 2.2 The ranking

**POPULATION:** the 190 modules installed in the deployment. **UNIT:** one module directory.
**MEASURE:** `version` in `__manifest__.py`, normalised by the series-16 rule, compared to
`ir_module_module.latest_version`.

**The normalisation rule, read from source rather than assumed** —
`odoo/modules/module.py:56` sets `'version': '1.0'` in the manifest defaults and `:393` applies
`adapt_version`. A core manifest that omits `version` therefore resolves to **`16.0.1.0`**, not to "no version".

| Tag | Root | Modules present | **Version-match** | Absent |
|---|---|---|---|---|
| **E-ENT** | `…/16 ODOO 16 ENTERPRISE/odoo-16.0+e.20230401/odoo/addons` | **144 / 190** | **144** | 46 |
| E-SOM | `…/94 ODOO MODULE/ODOO 16/odoo-16.0/addons` (+`odoo/addons`) | 91 / 190 | 91 | 99 |
| E-KIT | `…/02 KITTIPHUT/odoov16/addons` (+`odoo/addons`, `enterprise`, `custom`) | 92 / 190 | 92 | 98 |

**Zero version mismatches in any tree.** Every module that is present matches the deployment exactly. The trees
differ only in coverage. **E-ENT is the ranked winner and is the only tree used for core citations in this package.**

### 2.3 A false-match hazard in the ranking instrument, recorded

The first version comparison reported 23 "mismatches" in E-ENT. **They were an artefact of my own predicate** —
it treated a missing `version` key as unmatched instead of applying the `1.0` default proved in §2.2.
Corrected, the figure is 144/144.

Separately, when the same normaliser was pointed at the **whole-host** index it prefixed `16.0.` to every
version string regardless of the containing tree, so a series-18 tree's `stock_landed_costs 1.1` false-matched
as `16.0.1.1`. **Exact-version matching across the host index is valid only where the containing tree's series
is separately confirmed.** Core reads in this package come from E-ENT, whose series is read from
`odoo/release.py` → `version_info = (16, 0, 0, FINAL, 0, '')`.

---

## 3. THE 190 DEPLOYED MODULES AGAINST THE WHOLE-HOST INDEX

The completed local manifest index — **58,263 manifests parsed of 58,263 enumerated**, 3,174 distinct module
names — resolves what the core trees alone cannot.

| Outcome | Count |
|---|---|
| Version-matching copy exists on this host | **165 of 190** |
| Copy exists at a different version | 24 |
| **No copy anywhere on this host** | **1** |

The single module with no source anywhere is **`studio_customization`** (deployed `latest_version` is NULL).
That is the Odoo Studio–generated module; it has no source distribution by construction. **It is not an
evidence gap.**

The 24 present-at-another-version are almost entirely core modules where the deployment records `16.0.1.0`
(the default) and the host copy declares an explicit `1.1` — `auth_totp`, `contacts`, `portal`, `web_editor`,
`http_routing` and similar. **None is P2P-material.**

### 3.1 The core trees alone were not sufficient — and that matters

Against the three **core** trees, 45 deployed modules appeared absent, including
`purchase_request`, `scgl_purchase_advance_payment`, the entire `l10n_th_withholding_tax*` stack,
`om_data_remove`, `full_summarize_bills` and the `scgl_*` set. Resolved against the **host index**, a sample of
19 of those 45 returned **19 of 19 with a version-matching copy on this host**.

**The bounded probe was the core trees; the population was the host.** This is the fourth occurrence of that
shape in P01 and it is recorded again in `P01_POPULATION_SELECTION_METHOD_AUDIT.md`.

It is also the vindication of an instrument this session had classified `OVERBROAD_SCAN`: the whole-host index
was overbroad **and** decisive. Breadth that is wasteful for one question can be the only thing that answers another.

---

## 4. P01-MATERIAL MODULES — SOURCE / INSTALLED / CONFIGURED / EXERCISED

The four states are established separately. **Source present ≠ installed ≠ configured ≠ exercised.**

| Module | Version | Source on host | Installed | Configured | **Exercised** | Evidence |
|---|---|---|---|---|---|---|
| `purchase` | 16.0.1.2 | yes (E-ENT) | yes | — | **yes** | 5,881 orders, 5,756 confirmed |
| `purchase_stock` | 16.0.1.2 | yes (E-ENT) | yes | — | **yes** | 10,490 lines carry received/invoiced quantities |
| `stock` | 16.0.1.1 | yes (E-ENT) | yes | — | **yes** | 20,098 pickings, 18,218 done |
| `stock_account` | 16.0.1.1 | yes (E-ENT) | yes | **yes** — journal + accounts | **yes** | 74,982 layers, 57,863 posting |
| `account` | 16.0.1.2 | yes (E-ENT) | yes | yes | **yes** | 183,590 moves, 447,384 items |
| `account_accountant` | 16.0.1.1 | yes (E-ENT) | yes | — | not measured | — |
| **`stock_landed_costs`** | 16.0.1.1 | yes | **yes** | not established | **NO — 0 rows** | `stock_landed_cost` table empty |
| `purchase_request` | 16.0.1.0 | **yes, via host index** (4 exact-version copies; **none in a core tree**) | yes | — | see `P01_S16_BUSINESS_PROCESS_ACCOUNTING_MAP.md` | — |
| `l10n_th` | 16.0.2.0 | yes (E-ENT) | yes | — | — | — |
| `l10n_th_withholding_tax` | 16.0.1.0.1 | yes, via index (6 exact-version copies) | yes | yes | **yes** | 5,201 certificates |
| `l10n_th_withholding_tax_cert` | **16.0.14.0.1.0.0** | yes, via index (15 copies) | yes | yes | **yes** | certificates carry `income_tax_form` |
| `l10n_th_withholding_tax_cert_form` | 16.0.1.0.1 | yes, via index | yes | — | — | — |
| `l10n_th_withholding_tax_report` | 16.0.1.0.0 | yes, via index | yes | — | — | — |
| `scgl_purchase_advance_payment` | 16.0.1.0.0 | yes, via index (18 copies) | yes | — | see `P01_S16_VENDOR_ADVANCE_PAYMENT_SETTLEMENT.md` | — |
| **`om_data_remove`** | 16.0.1.0.1 | yes, via index (4 copies) | **yes** | — | **under challenge** | peer P06 reports this module deletes ledger data |
| `studio_customization` | NULL | **no copy anywhere** | yes | — | — | Studio-generated; not an evidence gap |

### 4.1 `16.0.14.0.1.0.0` — a series-14 body on a series-16 engine

`l10n_th_withholding_tax_cert` is deployed at **`16.0.14.0.1.0.0`**. Under the series-16
`adapt_version` — an unconditional prefix with no part-count guard and no validating regex
(`odoo/modules/module.py:488-492`, read in the series-16 core itself under `ERR-P01-41`) — a manifest declaring
`14.0.1.0.0` installed on a 16.0 engine is stored exactly so.

Several other deployed modules carry the same signature: `l10n_th_amount_to_text`, `l10n_th_partner`,
`partner_company_type`, `partner_firstname` at `16.0.14.*`, and `l10n_th_base_location` at **`16.0.15.*`**.

**FACT VERIFIED: this deployment runs a mixture of series-14, series-15 and series-16 module bodies on a
series-16 engine.** Any claim that "the deployment is series 16" is true of the *engine* and false of parts of
the *code*.

---

## 4.2 A BETTER INSTRUMENT FOR CODE IDENTITY, ADOPTED FROM AAS-03 EXPERT 3

Version matching is not merely insufficient in principle — **it is insufficient in fact for this deployment**.
Expert 3 found **4 distinct `.py` variants of `l10n_th_withholding_tax_cert` sharing `16.0.14.0.1.0.0`**, and
**6 variants of `..._report` sharing `16.0.1.0.0`**. One on-disk copy is **uncommitted and 246 lines ahead of
a 2023 commit with an unchanged version string**.

> **The instrument that worked: discriminate against the deployment's own `ir_model_fields` registry.**
> Only one `_cert` variant declares a `signature` field; the deployed registry has it. **That identifies the
> running code by the shape it declares, not by a string its author controls.**

**Adopted as the P01 standard for custom-module identity**, superseding version matching wherever a model's
field set can discriminate. It is strictly stronger than the schema-level corroboration used in the previous
round, because it reads the **registry the deployment itself built at install time**.

Applied to the deployed `_cert` variant, it establishes by **content** — not by a version prefix — that the
module is the **2021 Odoo-14.0 body differing by exactly one line**, running on a series-16 engine.

---

## 5. WHAT THIS MATRIX DOES NOT ESTABLISH

- **A version match is not code identity — now demonstrated, not merely warned about.** Four `_cert` variants
  share one version string here; six `_report` variants share another. Peer P04 (relaying P07) warned of this;
  **this deployment proves it.** Use the `ir_model_fields` route in §4.2 wherever a field set discriminates.
- **Installed is not exercised**, and the table above marks the difference in every row it could measure.
  `stock_landed_costs` is the clearest case: installed, and **zero** rows.
- It does not establish that any code path **executed** — only that records consistent with it exist.
