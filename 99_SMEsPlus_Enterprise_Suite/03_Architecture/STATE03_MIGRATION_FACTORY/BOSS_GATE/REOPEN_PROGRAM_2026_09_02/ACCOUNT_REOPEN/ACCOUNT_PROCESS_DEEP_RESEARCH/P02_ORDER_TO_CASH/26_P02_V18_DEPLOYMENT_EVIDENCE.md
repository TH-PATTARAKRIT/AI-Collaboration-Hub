# 26 — P02: THE v18 DEPLOYMENT — PEER-SOURCED DENOMINATOR CORRECTION

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-TARGETED-FORENSIC-CLOSURE-001`

## 1. Origin — A Peer Corrected P02's Population

**P04 (Acquire-to-Retire) reported a deployed database that P02's search never reached:**
`~/OCC_BACKUP/idemo18_uat_pre_scgl_occ_website_20260830_085432.dump`.

P02's declared path set was `~/Downloads` and `/Volumes/iMacSys`. **`~/OCC_BACKUP` is under the home
directory and was never searched.**

**This is the fourth evidence-base failure in this package, and the third of the same class:**

| # | Failure | Class |
|---|---|---|
| `RE-13` | "no database access" — no search performed at all | untested negative |
| — | default restore client refuses two archives — tooling not exhausted | narrow instrument |
| `RE-16` | search pattern never looked inside archives | narrow pattern |
| **`RE-20`** | **search path set excluded a home-directory folder** | **narrow path** |

P04's own diagnosis of the cause is adopted here because it is more useful than the artefact: its census had
**POPULATION, PATTERN and UNIT declared and executed, and the PATH SET author-chosen and never written
down.** P02's has now failed on the same axis three times. **The path set is the component of a denominator
that fails silently and is the one this package has never got right.**

## 2. Identity — Verified Independently By P02

| Field | Value |
|---|---|
| Database | `idemo18_uat` |
| UUID | `551ab874-9acb-11f1-b150-6ec7a480be3d` — **distinct from all five previously counted** |
| **Generation** | **Odoo 18.0** — `base 18.0.1.3`, `account 18.0.1.3`, `stock 18.0.1.1`, `stock_account 18.0.1.1`, `sale_stock 18.0.1.0`, `l10n_th 18.0.2.0` |
| Modules installed | **361** |
| Snapshot date | **2026-08-30** — later than every archive previously examined |
| Companies | **4**, all Thai fiscal country |
| Journal lines | **40,353** |
| Valuation layers | **47,801** |
| Requires | PostgreSQL 18 client; the host default 16.15 rejects it |

## 3. Two P02 Claims Refuted

### C-29 — TC-35 REFUTED: a v18 deployment **does** exist

`22` §8 / TC-35 stated: *"The estate contains **no deployment of the generation this package analysed**…
Generation distribution: one database on 16.0, four on 19.0, and **NONE on 18.0**."*

**Refuted.** `idemo18_uat` is 18.0, with 361 modules installed and real transaction volume.

**Corrected generation distribution — 6 distinct databases:**

| Generation | Databases | Journal lines | Source on this host |
|---|---|---|---|
| **16.0** | 1 | 447,384 | **none** |
| **18.0** | **1** | **40,353** | **full tree — the package's primary root** |
| 19.0 | 4 | 610 | full tree |

**The consequence is the opposite of the one C-21 forced.** C-21 established that the package's v18 source
analysis had zero deployed instances. **It now has one — with 40,353 journal lines, on the exact generation
the analysis was written against, and with its source readable.** The v18 analysis is **re-attached to
deployed reality**, which is a materially better position than the closure reported.

### C-30 — TC-03 REFUTED AGAIN: split recognition is ON in one deployed company

TC-03 as published: *"false in all 93 company records"*. Corrected by C-24 to *"false in 91, unset in 2"*.

**Refuted a second time.** In `idemo18_uat`, **company 1 carries `anglo_saxon_accounting = TRUE`** — the
only company anywhere in the estate with split cost recognition enabled.

**Corrected: across 6 databases and 95 company records — 91 false, 2 unset, and 1 TRUE.**

## 4. The Decisive Test — And TC-02 Survives On The Generation That Matters Most

`idemo18_uat` is the single most likely database in the estate to contain cost-of-sales lines: it is on the
generation whose invoice-side mechanism this package analysed, **and** it is the only one with that
mechanism's gate switched on.

**`FACT VERIFIED` — TC-36. It contains zero.**

| Measure | Result |
|---|---|
| `display_type = 'cogs'` lines | **0** of 40,353 |
| `cogs_origin_id` populated | **0** |
| Journal-line types present | product 29,586 · payment_term 5,494 · tax 5,202 · line_note 70 · line_section 1 |
| Valuation layers | **47,801** |
| **Valuation layers carrying a journal entry** | **0** |

**`FACT VERIFIED` — TC-02 SURVIVES, AND IS NOW STRONGER THAN WHEN PUBLISHED.** Across **6 distinct
deployed databases, 95 company records and 488,347 journal lines — zero cost-of-sales entries** — including
a v18 database with split recognition ON, stock accounts configured, and 47,801 valuation layers.

## 5. Why It Is Zero — And It Confirms The Package's Central Mechanism Claim Exactly

**`FACT VERIFIED` — TC-37.** In `idemo18_uat`, across **126 product categories**, `property_valuation` is
**unset (`NULL`) on every single one**. It therefore falls back to the field default, which v18 data sets to
manual/periodic (`EV-P02-100`).

Meanwhile:

- `anglo_saxon_accounting` = **TRUE** on company 1 — the gate the package identified;
- `property_stock_account_output_categ_id` and `property_stock_valuation_account_id` are **configured**,
  per company, on 15–16 categories;
- `property_cost_method` is set to average on 18 categories.

**So: the boolean is ON, the accounts are configured, the costing method is chosen — and a third setting,
left unset on all 126 categories, silently defeats all of it.** No valuation entries. No cost lines.

> **This is `P02-F-05` observed in production, on the right generation, with the gate open.**
> The package's central claim was that cost recognition is decided by **settings held on different objects
> that are never validated against one another**. Here an implementer switched on split recognition and
> configured the accounts — everything a person would do to enable it — and got **nothing**, because a
> fourth setting on a fourth object was left at a default that recognises no cost at all.

**`FACT VERIFIED` — TC-38.** This is the **outcome-3 case** of `01` S5 — *cost of sales recognised nowhere*
— observed live, on v18, with 47,801 valuation layers and 89.7 million in inventory value moving through
them and **not one accounting entry behind any of it**.

## 6. What This Changes For The Boss Decision

**It strengthens `B-01` and it weakens the case for treating recognition as configuration.**

The closure previously argued that the reference cannot hold the recognition policy still *across
versions*. This database shows it cannot hold it still **within one version, on one deployment, with a
competent implementer**: three of the four settings were configured correctly and the outcome was still
"no cost of sales anywhere".

**`DESIGN CANDIDATE` — reaffirming `DC-02-01` with deployed evidence.** A recognition profile must be a
**single named, validated object**. A configuration surface where switching on the feature, choosing the
costing method and setting the accounts still produces nothing — because a fourth field on a fourth model
is unset — is not a configuration surface a tenant can be asked to operate.

## 7. Peer Handling

| Item | Disposition |
|---|---|
| P04's report | **Verified independently by P02 before adoption** — identity, generation, module count and every figure above were re-derived from the archive, not accepted from the message. |
| P04's claim about P02's finding | P04 explicitly did **not** claim P02's finding was wrong, only that it was untested against this database. **That was the correct framing, and the test confirmed the finding.** |
| P04's candidate list | P04 named further name-matched candidates and **counted none of them**, flagging them as candidates only. **P02 adopts the same discipline** — a name-matched sweep is not a census. P02 has run a content-test sweep over the host; results in §8. |
| Return to P04 | P02 confirms the database, confirms it is v18, and reports that it contains **zero** cost-of-sales lines — so P04's hypothesis that this was the most likely database to move the finding was well-founded, and the finding held. |

## 8. Population Status

The content-test sweep P04 recommended — signature-based, not extension-based, over the whole host — was
executed by P02. **Results and the final denominator are recorded in §9 when that sweep completes.** Until
then the honest statement is:

**6 distinct deployed databases confirmed and tested. The population is NOT declared closed**, because it
has now been reopened four times, three of them by an outside party. **P02 does not assert completeness of
this population again without a published, reproducible discovery command and its output.**
