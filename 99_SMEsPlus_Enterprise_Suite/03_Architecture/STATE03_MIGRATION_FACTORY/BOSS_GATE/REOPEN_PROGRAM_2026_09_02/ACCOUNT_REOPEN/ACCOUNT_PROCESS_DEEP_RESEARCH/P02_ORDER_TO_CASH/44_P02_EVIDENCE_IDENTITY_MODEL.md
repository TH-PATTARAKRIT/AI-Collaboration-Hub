# 44 — P02 EVIDENCE IDENTITY MODEL

*(mandated semantic name: `30_P02_EVIDENCE_IDENTITY_MODEL.md`; **30 was already taken** by
`30_G02_P02_FINAL_LINEAGE_RECONCILIATION.md` and by this round's own prompt file, so per §15 the
existing files are preserved and the next free number is used.)*

`LAYER 2 — AUDIT QUARANTINE.` Prompt `[SMEPLUS-26-09-05-G02-P02-O2C-FINAL-UNCERTAINTY-CLOSURE-003]`,
**CP-01**. Baseline `aca211e`. **OLD SESSION CONTINUATION.**

**The invariant this model exists to enforce:**

> `Artifact` ≠ `Snapshot` ≠ `Database UUID` ≠ `Database Lineage` ≠ `Deployment Instance` ≠ `Business Entity`

Every counterexample below was **re-derived in this round**, not quoted from an earlier one.

---

## 1. The Six Levels

### 1.1 `ARTIFACT` — a physical file or directory on a storage path

| | |
|---|---|
| **Permitted keys** | absolute path **+** size **+** format **+** content hash. Path alone is **not** an identity — the same bytes appear at many paths. |
| **Forbidden shortcuts** | filename; extension; "two instruments found the same set" **when both share a pattern** (`C-48`). |
| **Evidence required** | a format classification that **validates**, not merely matches a magic string, plus a failure control proving an invalid shape is rejected. |
| **Counterexample (`CE-A1`)** | A file beginning `PGDMPX…` was classified `PGDMP` by magic-prefix matching in this round's own first draft. The failure control caught it; the classifier now requires the archive TOC to parse. |
| **Counterexample (`CE-A2`)** | `iEVING_2026-03-31_06-48-41/dump.sql` — a real 62 MB artefact **missed by three instruments that shared one pattern** (`C-48`). |
| **Classification** | `FACT VERIFIED` where a controlled classifier ran; **`UNRESOLVED` for any format the pattern set does not cover.** |

### 1.2 `SNAPSHOT` — a point-in-time export of a database lineage

| | |
|---|---|
| **Permitted keys** | lineage key **+** the internal state timestamp (`ir_config_parameter.write_date`, max `write_date` of a volume table), **not** the filename's date. |
| **Forbidden shortcuts** | the date in the filename; the file's mtime. |
| **Evidence required** | two artefacts claiming one snapshot must agree on internal counts. |
| **Counterexample (`CE-S1`)** | uuid `551ab874` has two artefacts giving **47,242** and **47,801** valuation layers — **two snapshots, not one** (`C-45`). Both show 0 layers carrying an entry, so the *finding* survives while the *figure* is snapshot-specific. |
| **Classification** | `FACT VERIFIED` per artefact; **any figure must name its artefact** (`P02-F-30a`). |

### 1.3 `DATABASE UUID` — an observed attribute, **not** an identity

| | |
|---|---|
| **Permitted use** | as **one** discriminator among several; as evidence of a **restore event** when it changes while birth metadata does not. |
| **Forbidden shortcuts** | **treating it as lineage identity.** It fails in **both** directions, demonstrated in this estate. |
| **Counterexample (`CE-U1`) — under-count** | **Seven** separately named, concurrently existing, differently configured live databases share `a6664233`. Re-derived this round: `occ_anglo_test` has `stock_account` **installed**, `occ_sim` has it **uninstalled** — they are not the same database (`C-44`). |
| **Counterexample (`CE-U2`) — over-count** | The `iEVING` lineage carries **two** uuids across **four** artefacts. Re-derived: all share `ir_config_parameter` **row id 2** with `create_date` `2026-03-18 04:58:50.421471` **to the microsecond**, and `res_company` id 1 `create_date` identical. The uuid **value** was rewritten at `2026-03-30 02:35:31` — **five minutes after the `02:30:18` backup** (`C-49`). |
| **Classification** | **`OBSERVED ATTRIBUTE`. Never `IDENTITY`.** `P02-F-28a`, which argued the opposite, is **WITHDRAWN**. |

### 1.4 `DATABASE LINEAGE` — continuous ancestry across backup / restore / copy / upgrade

**This is the level P02 had no key for, and it is the one that matters.**

> ## ⚠ SECOND AMENDMENT — THE KEY IS DISPROVED IN BOTH DIRECTIONS (`C-63`, `C-64`)
>
> The first amendment (below) added **founding-company identity** as clause (b). **Clause (b) is itself
> wrong and has been demoted.** `res_partner` id 1 `name` carries `write_date > create_date` in **36 of
> 36** artefacts — it is a **current-state field on a birth-time record**, the same class of attribute
> as `database.uuid`, which §1.3 already demotes. It collides in **both** directions in this estate:
> `"My Company"` appears in 9 of 36 artefacts across 3 birth groups, and two genuinely distinct lineages
> share a founding-company **name and VAT number** while sharing **0 of 5,732** ancestry rows. Applied
> as a key it produced a **false split** on `pfp-main`/`pfp-staging`, which content ancestry, the
> `database.secret` value and the uuid **version** all show to be **one lineage**.
>
> **`DATABASE LINEAGES = 14`, not 15.** Both amendments were made to fix an over-count and each
> introduced a new error in the opposite direction.
>
> **CANONICAL KEY (third form) — CONTENT ANCESTRY.** Two artefacts belong to one lineage iff **≥N rows
> share `(table, id, create_date)`** *and* the **latest** such shared `create_date` is **≥1 day after
> database birth**, corroborated across **≥2 tables from different modules**, and validated against a
> **declared negative-control pair that must return ≈0**. Birth metadata, founding-company name and
> `database.uuid` are all **`OBSERVED ATTRIBUTE`** — useful as corroboration or as evidence of a rename
> or restore **event**, never as identity.
>
> **Free discriminators that outperform clause (b) and were not used:** uuid **version** (v1 = written by
> this codebase, v4 = platform replacement) and uuid1's **embedded node and timestamp**, which
> independently confirmed both the `iEVING` rotations and the `pfp` copy.
>
> **Also corrected here:** §2's *"instances ≥26"* contradicts `45` §4's *"≥9 live"* — same round — and
> §1.5 of this file classifies archived instances `UNRESOLVED`, which forbids the ≥26 figure its own §2
> asserts. **Use `≥9 live`; archived instances remain `UNRESOLVED`.** §1.1's required **content hash was
> never computed**, so `ARTEFACTS = 40` is a path count (**28 distinct contents** accessible).
> **`CE-S1` is withdrawn** (`C-69`): only **one** `551ab874` artefact exists, yielding **47,801**; the
> 47,242 figure's level of origin is unresolved.

> ## ⚠ AMENDMENT — THE KEY BELOW WAS TESTED AND IS INSUFFICIENT (`P02-F-45a`)
>
> The composite proposed in this section was put to a falsification test in `45` §5 and **produced FALSE
> MERGES in 2 of 3 multi-uuid groups**. Birth metadata identical **to the microsecond** does **not**
> establish one lineage — databases provisioned from a common template or base image share it:
>
> | birth group | founding company | verdict |
> |---|---|---|
> | `2026-03-18…421471` | **same** (วีอิ้ง อินเตอร์เทรด) across 3 uuids | merge **confirmed** |
> | `2023-06-20…517597` | **ข้าวสุวรรณภูมิ** vs **เอสซีจี เลกาซี** | **false merge** |
> | `2025-04-24…91748` | **My Company** vs **Premium Flexible Packaging** | **false merge** |
>
> **AMENDED RULE — birth metadata AND founding-company identity must BOTH agree.** Where they disagree,
> the merge must not be made and the pair is `UNRESOLVED` until a further discriminator settles it.
> **A key adopted to fix an over-count produced a different over-merge, and only its own falsification
> test caught it.** That test is now part of the key, not an optional check.

**Permitted keys — a composite, no member sufficient alone:**

| Discriminator | Why it survives a restore |
|---|---|
| `ir_config_parameter` row **id** of `database.uuid` | the row is copied, not recreated |
| that row's **`create_date`** | set at database birth; **microsecond-resolution** |
| `res_company` **id 1** `create_date` | the founding company's birth |
| monotone growth of a volume dimension (company count, max id) | orders snapshots **within** a lineage |
| **uuid `write_date` ≫ `create_date`** | positive evidence of a **restore-with-rotation** event |

**Worked example, re-derived this round — the `iEVING` lineage:**

| artefact | format | uuid | icp row | icp `create_date` | icp `write_date` | companies |
|---|---|---|---|---|---|---|
| `iEVING_2026-03-30_02-30-18.zip` | ODOOZIP | `f4a44cce` | **2** | `2026-03-18 04:58:50.421471` | `2026-03-18 12:06:54` | **1** |
| `iEVING_2026-03-31…/dump.sql` **(the artefact three sweeps missed)** | PLAINSQL | `1f6338ae` | **2** | `2026-03-18 04:58:50.421471` | `2026-03-30 02:35:31` | **2** |
| `iEVING_2026-07-23_10-31-06.dump` | PGDMP | `1f6338ae` | **2** | `2026-03-18 04:58:50.421471` | `2026-03-30 02:35:31` | **44** |
| `5010f6cd-…zip` | ODOOZIP | `1f6338ae` | — | — | — | — |

**`P02-F-44a` — CORRECTED AND ENLARGED BY `45` §5: one lineage, **six** artefacts, **three** uuids
(`f4a44cce`, `1f6338ae`, **`66d1b52a`**), 1 → 2 → 44 companies, all naming the same founding company
**บริษัท วีอิ้ง อินเตอร์เทรด จำกัด**. `BK12MAY26` was counted as a separate database by the uuid key and
belongs to this lineage.**
A name-keyed sweep would have been **right** here. The uuid key **split one lineage in two**.

**Forbidden shortcuts:** name; uuid; filename date; "different uuid ⇒ different database".
**Classification:** `FACT VERIFIED` for `iEVING` — the composite is unanimous across four artefacts.
**`LINEAGE HYPOTHESIS` (not fact)** for every other multi-artefact uuid until the composite is run on it.

### 1.5 `DEPLOYMENT INSTANCE` — a lineage actually running, with code and configuration

**Must bind:** lineage · environment/host/container · installed module set · code identity · configuration
scope · effective version.

| | |
|---|---|
| **Counterexample (`CE-D1`)** | The seven `a6664233` databases are **seven deployment instances of one lineage**, differing in installed modules. An artefact-level or uuid-level count sees **one**. |
| **Counterexample (`CE-D2`)** | `bhpro92_test` and `bhpro_tracking_test_20260901` are 19.0 deployment instances **inside a Docker volume** — invisible to any filesystem sweep, and absent from every deliverable before `C-41`. |
| **Classification** | **`UNRESOLVED` for the archived estate** — an artefact records a lineage's *state*, not the instance that was running it. `DEPLOYED CODE IDENTITY UNRESOLVED` is the correct status wherever source is missing. |

### 1.5b `COMPANY SCOPE` — THE LEVEL THIS MODEL OMITTED (`C-71`, AAS-03 Expert 3)

**The model shipped with six levels and none of them was COMPANY**, under a constitution whose axes are
PLATFORM / TENANT / COMPANY. Company count entered only as a *growth* signal for ordering snapshots.
**There is no continuity rule, and the omission was not noticed by the model itself.**

**Measured for the first time in the package** (read-only extraction from `BK12MAY26_2026-08-03`):

| | |
|---|---|
| `res_company` rows | **44 = 4 roots + 40 branch children** (43 active, 1 archived) |
| Roots | `1` วีอิ้ง อินเตอร์เทรด · `14` สรรพสินค้าเซ็นทรัล · `16` โรบินสัน · `28` ซีอาร์ (archived) |
| Tenancy | **one database = one tenant** in this stack — scoping is `company_id`, there is no tenant column |

**`P02-F-44b`. One tenant, four root companies, forty branches — and three commercially unrelated
business groups in one database.** Consequences: (a) any P02 figure aggregated over "the deployment"
spans **four unrelated sets of books**; (b) `SF-06`'s cross-company reconciliation guard is
`company_id.root_id` equality, so exposure is **intra-root** — under a flat 44-company reading it would
appear not to fire at all. **The topology is exactly what makes `SF-06` live, and it had never been
measured.**

**`P02-F-44c` — company-scope discontinuity is aggregated away in the package's own headline table.**
The confirmed `iEVING` lineage runs **1 → 2 → 44** companies. `22` §2 builds `TC-03`…`TC-07` on *"93
company records"*, of which **88 are the two 44-company snapshots of that one lineage** — and those two
snapshots **disagree with each other** on valuation mode. **P02 does transfer figures across a
company-scope change, in its own configuration table.**

**`P02-F-44d` — the unit is wrong for root-delegated fields.** `tax_exigibility` is copied from root to
branches and constrained equal, so `TC-05`'s *"true in every company record that has a value"* counts
**40 copies of 4 root decisions**. `anglo_saxon_accounting` is **not** delegated, so `TC-03`'s
per-company count is sound. **The two sit in one table under one unit with no distinction drawn.**

**RULE ADDED:** no figure may cross a company-count change within a lineage without restatement, and
every per-company count must declare whether its field is **root-delegated**.

### 1.6 `BUSINESS ENTITY` — kept strictly separate

One business name may map to many lineages; one lineage may move across labels and grow from 1 to 44
companies (`P02-F-44a`). **`iSMEs` vs `iSMEs182` share a name stem and are different lineages; `iEVING`
is one lineage under two uuids.** Neither direction may be inferred from the name.

---

## 2. What This Model Withdraws, Narrows, Or Confirms

| Prior statement | Level confused | Disposition |
|---|---|---|
| `P02-F-28a` — *uuid-keying beats name-keying, per `iEVING`* | uuid ⇄ lineage | **WITHDRAWN** (`C-49`). Its own example demonstrates the opposite. |
| *"39 artefacts resolve to 17 distinct databases"* | artifact ⇄ lineage ⇄ instance | **NARROWED.** ≥40 artefacts; **uuid count is not a database count**; instances ≥26. |
| *"47,242 layers, 0 with an entry"* | snapshot ⇄ lineage | **CONFIRMED as a finding, narrowed as a figure** — snapshot-specific; both snapshots give 0. |
| `EV-P02-126` — module state attached to uuid `a6664233` | uuid ⇄ instance | **NARROWED** to the artefact `occ_sim_pre_perpetual.dump`; two live siblings under that uuid have `stock_account` **installed**. |
| Zero-`cogs` invariant | *(no identity confusion)* | **Unaffected by this model.** Its correction (`C-43`) is a selection-membership issue, not an identity one. |

## 3. Required Reporting Shape

Any P02 population statement must publish **four numbers, never one**:

`ARTIFACTS` · `SNAPSHOTS` · `LINEAGES` · `DEPLOYMENT INSTANCES (where determinable)`

and must state, for each, the method, the path set, the pattern set, the positive controls, the failure
controls, and what remains `UNRESOLVED`.
