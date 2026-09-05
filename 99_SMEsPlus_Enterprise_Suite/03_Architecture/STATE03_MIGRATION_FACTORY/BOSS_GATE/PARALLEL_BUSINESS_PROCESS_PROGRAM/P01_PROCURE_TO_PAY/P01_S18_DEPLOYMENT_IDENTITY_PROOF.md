# P01 — SERIES-18 DEPLOYMENT IDENTITY PROOF

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Execution: **SUPPLEMENTAL TARGETED CONTINUATION — NO RESET**
Baseline: `2620c832b278e45d1d5f81fe95ad6ec52e12ee39`
Checkpoint: `CP-P01S18-01`
Classification: Layer 1. Identifiers below are **deployment evidence**, not canonical design identity.


> ### PEER DELTA APPLIED — BOUND TO ONE IDENTITY
>
> Peer **P04** (`9e377e30`, `P04-F-101`) records **three** series-18 database identities on this
> host, not one: `551ab874` (361 modules — the one analysed here), `4b766580` (478 modules), and
> `96548e18` (`T805efaplus`, 123 modules, never transacted). **Everything in this document is
> bounded to `551ab874` @ 2026-08-30** and is not a claim about the series-18 generation as
> deployed elsewhere. See `P01_S18_PEER_DELTA_HANDOFF.md §2.2`.

---

## 1. WHY THIS DOCUMENT EXISTS

`ERR-P01-23` established that a deployed series-18 database exists, contradicting three published
statements. That correction was itself made under time pressure at the end of the previous round.
This document re-establishes the identity **from primary evidence, independently**, so that
everything built on it in this run rests on a proof rather than on a correction.

---

## 2. ARCHIVE IDENTITY

| Property | Value | How obtained |
|---|---|---|
| Archive path | `~/OCC_BACKUP/idemo18_uat_pre_scgl_occ_website_20260830_085432.dump` | filesystem |
| Size | 45,633,645 bytes | `ls -la` |
| Archive format | CUSTOM, dump version **1.16-0**, gzip | `pg_restore -l` header |
| Archive created | **2026-08-30 08:52:24 +07** | `pg_restore -l` header |
| Declared dbname | **`idemo18_uat`** | `pg_restore -l` header |
| Dumped from engine | **PostgreSQL 17.9 (Debian 17.9-0+deb13u1)** | `pg_restore -l` header |
| Dumped by | pg_dump 17.9 | `pg_restore -l` header |
| TOC entries | 23,232 | `pg_restore -l` header |
| TABLE definitions | **1,122** | `grep -c " TABLE public " TOC.txt` |
| TABLE DATA entries | **1,122** | `grep -c "TABLE DATA" TOC.txt` |

**Tool capability declared.** `/opt/homebrew/opt/postgresql@18/bin/pg_restore` reports
`pg_restore (PostgreSQL) 18.6 (Homebrew)`; `/opt/homebrew/opt/postgresql@16/bin/pg_restore`
reports 16.15. Archive format 1.16 requires the 18-series binary. The 16-series binary is
recorded here so that no future round repeats `ERR-P01-15` — *enumerate the instruments present,
not the one that failed.*

**Extraction method.** `pg_restore -t <table> --data-only -f <outfile> <dump>`, then parse the
`COPY public.<table> (cols) FROM stdin;` block. Piping the restore output yields zero bytes.
This dump was produced by **pg_dump 17.9**, which quotes only reserved column names — the
`"json_value"` quoting that caused a near-miss in the previous round appears here on
`ir_default` and is handled by the parser (`s18/pgc.py`), which strips quotes from every column name.

**Do not read the filename as evidence.** The name contains `idemo18` and `occ_website`.
Neither is used as proof of anything below. Every fact in §3–§7 is read from table content.

---

## 3. DATABASE IDENTITY

Source: `ir_config_parameter`, 56 rows.

| Key | Value |
|---|---|
| `database.uuid` | **`551ab874-9acb-11f1-b150-6ec7a480be3d`** |
| `database.create_date` | **2026-08-18 06:09:12** |
| `web.base.url` | `https://occ.smeplus.cloud` |

### 3.1 This is a SIXTH database identity

The previous round, after peer P04's report (`ERR-P01-22`), recorded **five** distinct
`database.uuid` values across ten artefacts: `45a8e08e`, `1f6338ae`, `f4a44cce`, `66d1b52a`,
`a1430edc`. **`551ab874` is not among them.**

**The estate is therefore at least six database identities across at least eleven artefacts.**
The round-4 census was itself incomplete — for the same reason `ERR-P01-23` recorded: it did not
sweep `~/OCC_BACKUP`. This is registered as a materiality item in
`P01_POPULATION_SELECTION_METHOD_AUDIT.md` and is **not** presented as a final count; the count
is a **floor**, not a total.

### 3.2 What the create date means, and what it does not

The database was created **2026-08-18**, twelve days before the archive was taken. It does not
follow that the *business data* is twelve days old — §6 shows the majority of it was migrated in
from a predecessor system. **Database age and data age are different claims.** Only the first is
proved here.

---

## 4. APPLICATION SERIES — READ FROM THE REGISTRY, NOT INFERRED

Source: `ir_module_module`, 1,369 rows.

| State | Count |
|---|---|
| `installed` | **361** |
| `uninstalled` | 1,005 |
| `uninstallable` | 3 |

Histogram of `latest_version` across the 361 installed modules, keyed on the first two
version segments: **`{'18.0': 361}`**. There is no second series present.

Named modules material to P01:

| Module | State | `latest_version` |
|---|---|---|
| `base` | installed | 18.0.1.3 |
| `account` | installed | 18.0.1.3 |
| `stock` | installed | 18.0.1.1 |
| `stock_account` | installed | 18.0.1.1 |
| `purchase` | installed | 18.0.1.2 |
| `purchase_stock` | installed | 18.0.1.2 |
| `purchase_request` | installed | **18.0.1.10.0** |
| `account_accountant` | installed | 18.0.1.1 |
| `l10n_th` | installed | 18.0.2.0 |

`ir_module_module.latest_version` is the only stored version instrument in an Odoo-lineage
database. Its limits are stated in `P01_FALSE_ZERO_CONTROL_REGISTER.md §5` and it is the subject
of a standing disproof assignment in `P01_S18_AAS03_FRESH_CHALLENGE.md`.

**CLASSIFICATION: FACT VERIFIED — the deployed application series is 18.**

---

## 5. COMPANY POPULATION

Source: `res_company`, **4 rows**.

| id | Name | Currency | Parent |
|---|---|---|---|
| 1 | บจก.โอเชี่ยน คอนกรีต (สำนักงานใหญ่) | 133 (THB) | none |
| 2 | บจก. โอ.ซี.ซี. คอนกรีต (สำนักงานใหญ่) | 133 | none |
| 3 | หจก. พรนำพา (สำนักงานใหญ่) | 133 | none |
| 4 | หจก. โอเชี่ยน คอนกรีต คอนสตรัคชั่น (สำนักงานใหญ่) | 133 | none |

Four independent companies, no parent/child hierarchy, single currency.

### 5.1 The company denominator is 4. The *transacting* denominator is 2.

| Population | Companies 1 and 2 | Companies 3 and 4 |
|---|---|---|
| `account_move` | 9,733 + 5,789 = **15,522** | **0** |
| `stock_valuation_layer` | 25,978 + 21,823 = **47,801** | **0** |

Every accounting statement in this package about "the series-18 deployment" is a statement about
**two** companies unless it explicitly says otherwise. Companies 3 and 4 are configured but have
never transacted. Under the rule *never-transacted rows are the informative ones*, they are
retained as the negative control for configuration-versus-execution questions, not discarded.

---

## 6. ACCOUNTING AND VALUATION POPULATION

### 6.1 Journal entries — `account_move`, 15,522 rows

| By state | | By type | |
|---|---|---|---|
| posted | 13,773 | `entry` | 10,028 |
| draft | 1,746 | `out_invoice` | 3,559 |
| cancel | 3 | `in_invoice` | **1,904** |
| | | `out_refund` | 30 |
| | | `in_refund` | 1 |

Date range **2026-01-01 → 2038-11-30**. The forward tail is a scheduled/future-dated population
(asset depreciation journals `ASST` are among the largest), not a data error; it is not relied on
by any conclusion in this run.

### 6.2 Valuation layers — `stock_valuation_layer`, 47,801 rows

**This is not one population, and treating it as one would misstate every ratio built on it.**
Decomposed by `description`:

| Class | Rows | Share |
|---|---|---|
| Migrated predecessor history (`v14 2026: …`, `Opening rebalance 2026-01-01`) | **45,978** | 96.2% |
| `Migration correction: align layers to on-hand x cost (2026-08-26)` | 11 | 0.02% |
| Other, including inventory adjustments and business documents | **1,812** | 3.8% |

> **CORRECTED — `ERR-P01-27`.** The first version of this section called that 1,812 "native
> series-18 runtime output" and bounded it by `create_date` after `database.create_date`.
> **`create_date` on this table is loader-supplied, not insertion time**: 44,947 rows carry a
> `create_date` *earlier than the database itself was created*, while **`write_date` has a minimum
> of 2026-08-25 12:19:13 and 47,218 of the 47,801 rows were written on that single day.** The
> whole table was physically written in one five-day window. There is **no sub-population
> separable by insertion time**, and 1,254 of the 1,812 are `Product Quantity Updated` inventory
> adjustments authored by `__system__` inside that same window.

**The defensible runtime set is 558**, reached by two independent classifiers that converge:
a human `create_uid` gives 559, a non-inventory-adjustment underlying move gives 558, and they
overlap on 558. The over-determination-free core — layers that additionally have a stock move, a
non-zero value, a storable product and a fully-configured category — is **541**. Only **61** of
the 558 are purchase-linked. Full derivation in
`P01_S18_PERIODIC_PERPETUAL_POLICY_PROOF.md §8`.

**Consequence for this package.** Where a claim concerns what the *series-18 runtime does*, the
denominator is **558** (or **541** for the strongest form, **61** for purchase-linked events) —
**not 1,812 and not 47,801**. Where a claim concerns what is *in the ledger*, the denominator is
47,801. The two are stated separately everywhere in this run.

**And the layer table is not internally consistent with the product master**: 1,480 done
purchase receipts on storable products with quantity > 0 carry **no** valuation layer, while 220
receipts on non-storable products **do**, and 1,089 layers across the table sit on non-storable
products. The loader did not build layers move-by-move on valuation semantics, which bounds every
behavioural inference drawn across the full 47,801.

### 6.3 The predecessor was a different generation

The `ref` field of 15,434 of the 15,522 journal entries is non-empty, and its content carries
markers of the form `[v14 STJ/UB/00087 - …] STJ/2026/04/0505`. Journal 45 is named
**`MIG26 / "COA Migration 2026"`**. The predecessor system was a **series-14** installation whose
ledger was migrated into this database. This is recorded because it bears directly on §6.2 and on
the valuation-policy question in `P01_S18_PERIODIC_PERPETUAL_POLICY_PROOF.md`: the predecessor's
journal prefix was `STJ`, the stock journal, which indicates the **predecessor posted stock
journal entries**. The series-18 system does not. That is a change between generations, not a
static state.

---

## 7. LOCALIZATION AND CUSTOM MODULE POPULATION

`l10n_th 18.0.2.0` installed — **which supplies no withholding-tax code**; see `ERR-P01-33`.

**The non-core installed population is 55, not 16.** Sixteen modules match the name pattern
`scgl_*` + `purchase_request`; **66 of the 361 installed modules are absent from `R1` and 55 are
absent from `R1 ∪ R2`**. The 39 not listed below include the four OCA/Ecosoft withholding modules
and `om_data_remove` 18.0.1.0.0. See `P01_POPULATION_SELECTION_METHOD_AUDIT.md §4A`
(`ERR-P01-32`). The sixteen name-matched modules are:

`purchase_request 18.0.1.10.0`, `scgl_account_coa_control 18.0.1.0.1`,
`scgl_chatter_compact 18.0.1.1.0`, `scgl_custom_title_and_favicon 18.0.0.0.2`,
`scgl_dashboard_core 18.0.1.3.3`, `scgl_date_range_auto_period 18.0.1.0.0`,
`scgl_delivery_cost 18.0.1.0.0`, `scgl_document_terms_conditions 18.0.1.0.0`,
`scgl_multi_approve_core 18.0.0.3.1`, `scgl_multi_approve_purchase_request 18.0.1.0.0`,
`scgl_occ_transportation_costs 18.0.1.0.0`, `scgl_product_category_company 18.0.1.5.0`,
`scgl_signature 18.0.1.0.0`, `scgl_signature_hr_expense 18.0.1.0.0`,
`scgl_stock_fleet 18.0.1.0.0`, `scgl_uom_archive 18.0.1.0.0`.

Source-copy reconciliation for these sixteen is in
`P01_POPULATION_SELECTION_METHOD_AUDIT.md §4` and is **not favourable** to the declared source
path set.

---

## 8. BOUNDED ABSENCES

**POPULATION:** the 1,122 TABLE definitions enumerated from this archive's TOC.
**PATTERN:** exact and prefix match on the table name within that TOC listing.
**UNIT:** one table definition.

| Absent | Consequence |
|---|---|
| `ir_property` (no table definition at all) | Series 17+ removed it. The **only** two places a company-dependent value can live in this deployment are the per-record jsonb column and `ir_default`. Both are read in the policy proof. |
| `stock_landed_cost*` (no table definitions) | Landed costs are **not installed**. P01's landed-cost analysis is `NOT REACHABLE` in this deployment. It is not withdrawn — it remains bound to the population in which it was measured. |

Class per the negative-claim standard: **A — VERIFIED ABSENCE**, within the stated population.
The population is the archive, not the estate; nothing here is a claim about any other database.

---

## 9. CLASSIFICATION

| Item | Classification |
|---|---|
| Series-18 deployed database exists and is readable | **FACT VERIFIED** |
| Application series is 18 across 361/361 installed modules | **FACT VERIFIED** |
| Database identity `551ab874-…` is distinct from all five previously catalogued | **FACT VERIFIED** |
| The estate census is incomplete; six identities is a **floor** | **FACT VERIFIED** |
| 4 companies configured, 2 transacting | **FACT VERIFIED** |
| 15,522 journal entries / 47,801 valuation layers | **FACT VERIFIED** |
| 96.2% of valuation layers are migrated predecessor history | **FACT VERIFIED** |
| Predecessor was series 14 and posted stock-journal entries | **SUPPORTED INTERPRETATION** — read from `ref` text, not from a version registry of the predecessor |
| Data age vs database age | **UNRESOLVED — EVIDENCE REQUIRED** for any claim beyond §6.2 |

---

## 10. WHAT THIS DOCUMENT DOES NOT ESTABLISH

- It does not establish that this deployment is production. `web.base.url` and the archive name
  both suggest a UAT instance; neither is proof, and no operational status is claimed.
- It does not establish that the *code running* this database is any copy present on this host.
  That question is answered — negatively, for most modules — in
  `P01_POPULATION_SELECTION_METHOD_AUDIT.md §4`.
- It does not supersede any finding measured in `D1`, `D2`, `D3` or `D4`. Every finding remains
  bound to the population in which it was measured.
