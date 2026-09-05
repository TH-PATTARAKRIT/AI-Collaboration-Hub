# 45 — P02 FORMAT-COMPLETE POPULATION REBUILD

*(mandated semantic name `31_P02_FORMAT_COMPLETE_POPULATION_REBUILD.md`; 31 taken, next free number used per §15.)*

`LAYER 2 — AUDIT QUARANTINE.` **CP-02 / CP-03.** Baseline `aca211e`.

**Status: `FILE PATH SET REBUILT AND RECONCILED — POPULATION BOUNDED, NOT CLOSED`.**

> ## ⚠ CORRECTION BANNER — `C-63` … `C-70`. TWO INDEPENDENT EXPERTS, BOTH CONFIRMED BY P02.
> **The lineage count, the snapshot count, the artefact count AND the coverage assertion all move.**
>
> **`C-63` — the amended lineage key is DISPROVED, and clause (b) made it WORSE.** `45` §5 split
> `pfp-main` / `pfp-staging` as a "false merge" on founding-company name. **They are one lineage.**
> Two experts proved it by disjoint instruments:
>
> | instrument | evidence |
> |---|---|
> | **content ancestry** | **72 of 72** `res_partner` ids and **21 of 21** `res_users` shared with `create_date` identical **to the microsecond**, including **66 business records created 2025-05-27 → 2025-11-06 — six months after provisioning.** A template cannot share those. |
> | `ir_config_parameter` | `database.secret` **identical**, row id 1, same `create_date`; staging carries `database.expiration_date` with `create_date = \N` and no `enterprise_code` — the Odoo staging-neutralisation signature. |
> | **uuid version** | `57d32e15` is uuid **v4**; **35 of 36** artefacts carry uuid **v1**. Odoo writes `uuid.uuid1()`, so a v4 **cannot** be a birth value from this codebase — it is a platform-level replacement. |
> | negative controls | `iErpOCC` vs `idemo18`: 5,732 common ids, **0** identical `create_date`. `iTEST02` vs `BK12MAY26`: 3,072 common, **0**. The instrument does not fire promiscuously. |
>
> **`DATABASE LINEAGES = 14`, not 15.** Clause (a) had this pair right and clause (b) overrode it.
>
> **`C-64` — clause (b) is a category error and is demoted.** `res_partner` id 1 `name` has
> `write_date > create_date` in **36 of 36** artefacts: it is a **current-state field on a birth-time
> record**. It collides both ways in-estate — `"My Company"` appears in **9 of 36 artefacts across 3
> distinct birth groups**, and `iErpOCC` / `idemo18_uat` share founding-company name **and VAT** while
> sharing **0 of 5,732** ancestry rows. **Founding-company identity is hereby demoted to
> `OBSERVED ATTRIBUTE`, alongside `database.uuid` — evidence of a rename event, never identity.**
> **Replacement key: content ancestry** — two artefacts are one lineage iff ≥N rows share
> `(table, id, create_date)` **and** the latest shared `create_date` is ≥1 day after database birth,
> corroborated in ≥2 tables from different modules, against a declared negative-control pair.
>
> **`C-65` — `SNAPSHOTS ≥ 24` was ASSERTED, NOT DERIVED. Withdrawn.** Nothing in the evidence supports
> it. Derivable today: distinct `(icp create_date, icp write_date, company count)` tuples = **17**.
> The only arithmetic reaching 24 is `15 lineages + 9 instances` — **a sum of two different units, which
> §4 of this very file exists to forbid.** **`SNAPSHOTS = 17` (≤21 if the four blocked artefacts prove
> distinct).**
>
> **`C-66` — `ARTEFACTS = 40` is a PATH count wearing a content key's label.**
> `iTEST02_2026-06-14_14-41-19.dump` occupies **9 paths at one identical size (65,444,053 bytes)** —
> **verified**. Distinct artefact *contents* among the 36 accessible = **28**; ≤32 including the four
> blocked. `44` §1.1 makes content hash a **required** key member and **no hash was ever computed** —
> the shortcut its own text forbids.
>
> **`C-67` — THE COVERAGE ASSERTION IS WRONG, AND THE ERROR LABELS ARE SWAPPED.** Measured from
> `A_errors.txt`:
>
> | | published | **measured** |
> |---|---|---|
> | content-tested | 141,235 | **116,977** |
> | NOT content-tested | 51,987 (26.9%) | **76,245 (39.5%)** |
> | read failures | "186 read errors" | **24,258 distinct paths in the candidate list** |
> | enumeration errors | "165" | **186 `find:` lines** (the 165 came from a different file) |
>
> **And 807 of the 6,062 cloud files ≥1 MB — the slice explicitly claimed as tested — returned
> UNREADABLE.** They sit **above** the floor, so the *"<1 MB, 3.4× conservative"* justification **does
> not cover them**. Among the unreadable: 185 `.zip` and 28 files larger than the smallest known artefact.
>
> **`C-68` — `RE-40`'s defect class is STILL LIVE in the replacement instrument.** `classify` returns
> `UNREADABLE` only if the **first 512 bytes** fail. A file that opens and then fails deeper
> (`ZipFile.namelist()`, `gzip.read`, `tarfile`, `pg_restore -l` timing out) falls to
> `except Exception: pass` → **`NOTDB`** — an I/O failure indistinguishable from "not a database".
> **No count exists for it.** Required: publish `enumerated / attempted / classified / failed` as four
> numbers.
>
> **`C-69` — `CE-S1`, the sole evidence for the SNAPSHOT level, conflates Artifact with Instance.**
> The population contains **exactly one** `551ab874` artefact and it yields **47,801**; no predicate on
> it yields 47,242 (`company_id` splits 25,978/21,823; `stock_move_id` non-null 44,935;
> `account_move_id` non-null **0**). **The 47,242 figure's level of origin is `UNRESOLVED`.** The
> valuation finding itself is unaffected and was independently reproduced: **47,801 layers,
> `account_move_id` NULL on all 47,801.**
>
> **`C-70` — two further method gaps.** (i) **Gzipped tar is not covered and was not in the declared-open
> list**: the gzip branch tests only for `PGDMP` magic or the SQL header in the first 512 decompressed
> bytes, so **every `.tar.gz`/`.tgz` carrying a dump is silently `NOTDB`** — 38 candidates, of which 3
> unreadable and 2 scanned only to 4,000 members. Also undeclared: a zip whose SQL member is not named
> `dump.sql`, and archive-in-archive. (ii) **93 lines of `A_candidates.txt` are corrupted** by
> interleaved concurrent writes (`/Voln/Library/…`, `umes/iMacSys/…`), so the 193,222 denominator
> contains unopenable fragments and an unquantified loss of real paths.
>
> **What survived attack.** The path-split arithmetic reproduces exactly (24,500 + 109,673 + 1,000 +
> 6,062 = 141,235; 193,222 total). The `<1 MB` floor's minimum is exactly 3,374,773 bytes. The four
> `Group Containers` artefacts are genuinely blocked (`os.stat` under `signal.alarm` times out — even
> their size is unknown). **Raw PostgreSQL data directories were searched for and none exist.** And the
> substantive zero-COGS / zero-linkage finding on `551ab874` was independently re-derived from the
> artefact.
>
> **Corrected headline for this file: 40 artefact PATHS / 28 distinct contents accessible · 17 snapshots
> · 14 lineages · ≥9 live instances (not re-derivable now — the container runtime is down).**

---


> ## ✅ MAJOR REVERSAL — `C-86`. THE REFERENCE DISTRIBUTIONS EXIST. `C-55` IS WITHDRAWN.
>
> Every sweep in this programme pruned `~/Library` (adopted from the TCC prompt-storm lesson). **Full
> Odoo reference distributions for 14, 15, 16, 17, 18 and 19 sit inside it**, at
> `~/Library/CloudStorage/GoogleDrive-…/00 SW_SOURCE CODE/`:
>
> | distribution | module directories |
> |---|---|
> | **14 ODOO 14 ENTERPRISE** | **796** |
> | **16 ODOO 16 ENTERPRISE** | **950** |
> | 15 / 17 / 18 / 19 | present |
>
> Verified to contain `account`, `stock_account`, `sale_stock` — the exact modules P02 needs.
>
> **What this withdraws:**
> - **`C-55` — WITHDRAWN.** *"90.7% of the headline evidence comes from a generation whose standard
>   source cannot be read at all"* is **false**. A **950-module 16.0 Enterprise distribution** is on this
>   host. The "59 module directories" figure came from `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/addons`,
>   a **custom** directory mistaken for the distribution.
> - **`46` §2 / `C-43` side-note — "no 14.0 root exists on this host": false** (796 dirs).
> - **`31` §1's "the standard union is a floor"** — the floor was drawn far too low.
> - **Expert 4's `CH-4`** ("0 for all ten module names; no 16.0 or 14.0 core distribution anywhere") —
>   **refuted**; its sweep pruned `Library` too.
>
> **Quantified effect — the custom-module counts across the package were OVERSTATED.** Standard union
> rebuilt: **1,634 → 1,932 names**. Non-standard installed modules re-derived:
>
> | lineage | gen | published | **corrected** |
> |---|---|---|---|
> | `45a8e08e` **iSMEs** | 16.0 | 13 | **1** |
> | `a1cdeab8` | 16.0 | 25 | **3** |
> | `25e88cd4` iErpOCC | 14.0 | 36 | **23** |
> | `5d5164c4` odoo_cff | 14.0 | 409 | **380** |
> | **total rows** | | **620** | **540** |
>
> **The deployment carrying 90.7% of the marker-capable evidence runs ONE non-standard module, and its
> standard source is readable.** That is a materially **stronger** position than the package claimed.
>
> **How it was missed.** A blanket prune, adopted for a good reason (a TCC prompt storm), was never
> declared as an evidence-affecting exclusion and was inherited by **three P02 sweeps and two independent
> experts**. *Shared blind-spot agreement*, recurring — and this time the shared blind spot was one the
> package had itself written into its method.

## 1. Why A Rebuild Was Required

`C-48` established that the prior sweep was blind to plain-SQL dumps, and that **three instruments
agreed on 39 because all three carried the same pattern.** This round rebuilds discovery with a declared
pattern set, per-format positive controls, failure controls, and a **materially different** second
implementation.

## 2. Method A — Content-Led

Classifies **file bytes**. Shapes recognised: `PGDMP` · `ODOOZIP` · `PLAINSQL` · `GZSQL` · `GZPGDMP` ·
`PGTAR`.

**Validation, not matching.** `PGDMP` requires the archive **TOC to parse** (`pg_restore -l`), not merely
the magic string. `ODOOZIP` requires `dump.sql` **at the archive root**, or `<root>/dump.sql` **together
with `<root>/manifest.json`**.

### 2.1 Controls

| Control | Result |
|---|---|
| Positive — `PGDMP` (`iSMEs…dump`) | **PASS** |
| Positive — `ODOOZIP` (`BK12MAY26…zip`) | **PASS** |
| Positive — `PLAINSQL` (`iEVING…/dump.sql`) | **PASS** |
| Failure — file beginning `PGDMPX…` | **PASS** (rejected; **it was accepted by the first draft** — see `RE-37`) |
| Failure — `-- Some other database dump` | PASS |
| Failure — zip with no `dump.sql` | PASS |
| Failure — random bytes / gzip of a text file | PASS |
| **Failure — PLAUSIBLE negative: a zip whose `dump.sql` is a nested library sample** | **PASS after correction — it was accepted first** (`RE-38`) |

### 2.2 Path set — declared, with exclusions recorded rather than hidden

| Root | Status |
|---|---|
| `/Volumes/iMacSys` | fully enumerated |
| `~/Downloads`, `~/Desktop`, `~/Documents`, `~/OCC_BACKUP`, `~/OCC_Odoo18_Simulation_Lab`, `~/SMEsPlus`, `~/Library/CloudStorage`, `~/Library/Mobile Documents`, `~/Movies`, `~/Music`, `~/Pictures`, `~/Public` | fully enumerated |
| **`~/Library/Group Containers`** | **BLOCKED — traversal hangs (TCC).** Holds **4 known artefacts** |
| `~/Library/Application Support`, `~/Library/Containers` | **EXCLUDED — declared**, traversal hangs |
| Pruned by rule | `node_modules`, `.git`, `Library/Caches`, `*.app` |

**Coverage assertion.** 193,222 unique candidates >100 KB enumerated; **141,235 content-tested**;
**51,987 not content-tested** — all cloud-backed and **< 1,000,000 bytes**, where reads cost ≈1 s each.
The **smallest artefact in the entire known population is 3,374,773 bytes**, so that floor is **3.4×
conservative**; it is a bound, and it is declared rather than assumed away. 165 enumeration errors and
186 read errors captured.

## 3. Method B — Structure-Led, Materially Independent

**It never classifies file bytes.** It locates Odoo-backup *structure* — `dump.sql`, `manifest.json`,
`filestore/`, `toc.dat` — and infers an artefact from the **relationship** between them. This catches
**unpacked backup directories**, which no byte classifier can see.

**Result: 160 markers → 1 distinct unpacked backup directory —
`/Volumes/iMacSys/95_BHPRO_PROJECT/DOCUMENT/iEVING_2026-03-31_06-48-41`**, the artefact three
pattern-sharing instruments missed. **The independent method found it on its first run.**

## 4. Result By Unit — Four Numbers, Never One

| Unit | Count | Basis |
|---|---|---|
| **ARTEFACTS** | **40** | 36 verified by Method A this round + 4 known, read-blocked this session |
| **SNAPSHOTS** | **≥ 24** | distinct (lineage, internal state) pairs; multi-artefact copies collapse, differing measurements do not |
| **DATABASE LINEAGES** | **15** | composite key **with corroboration** (§5) |
| **DEPLOYMENT INSTANCES** | **≥ 9 live** | `occ-odoo18-db` (7) + `bhpro92-db` (2), all transaction-empty. Archived instances **UNRESOLVED** |

**New artefacts found by the rebuilt method: ZERO.** Two candidates surfaced and **both were false
positives** (§2.1). Within its declared path set, the format-complete sweep reproduces the known
population exactly — **36 found, 4 unreachable, 0 new.**

## 5. `P02-F-45a` — The Composite Lineage Key Produces FALSE MERGES, And Its Own Test Caught Them

Grouping the 36 accessible artefacts by `ir_config_parameter` birth `create_date` + `res_company` id-1
`create_date` yields **13 groups**. Three were multi-uuid and were put to a **falsification test** —
*do they name the same founding company?* (`res_company` id 1 → `res_partner.name`):

| birth group | uuids | founding company | verdict |
|---|---|---|---|
| `2026-03-18 04:58:50.421471` | `f4a44cce`, `1f6338ae` ×2, **`66d1b52a` ×2** | **บริษัท วีอิ้ง อินเตอร์เทรด จำกัด — all three uuids** | **MERGE CONFIRMED — one lineage, three uuids** |
| `2023-06-20 03:55:19.517597` | `45a8e08e` (iSMEs) / `a1cdeab8` (iMSCG) | **ข้าวสุวรรณภูมิ** vs **เอสซีจี เลกาซี** | **FALSE MERGE — split into 2** |
| `2025-04-24 15:55:31.91748` | `9138b764` / `57d32e15` (pfp main/staging) | **My Company** vs **Premium Flexible Packaging** | **FALSE MERGE — split; `UNRESOLVED` whether staging is a restore-then-rename of main** |

**Two false merges in three tested groups.** A birth timestamp identical **to the microsecond** does
**not** establish one lineage — databases provisioned from a common template or base image share it.
**The key proposed in `44` is insufficient alone and is hereby amended: birth metadata must agree AND the
founding-company identity must agree; where they disagree the merge must not be made.**

**And the merge that *did* hold is larger than previously known.** `BK12MAY26` was counted as a separate
database by the uuid key; it is the **same lineage as `iEVING`**, under a **third** uuid.

## 6. What The uuid Key Gets Wrong, Measured Both Ways

| | |
|---|---|
| uuid-based count published earlier | **17** |
| **Over-counts** | `iEVING` + `BK12MAY26` = **3 uuids, 1 lineage** |
| **Under-counts** | `a6664233` = **1 uuid, 7 concurrently-existing live databases** with differing module state |
| Corrected lineage count (accessible artefacts) | **15** |

## 7. Bounds — What This Does Not Claim

- **Not customer-estate completeness.** This is the evidence estate on this host.
- **51,987 cloud files < 1 MB were not content-tested** (I/O cost). Bound declared, floor justified.
- **`~/Library/Group Containers` could not be traversed**; 4 known artefacts live there and were
  **readable in an earlier session** — a session-scoped access condition, not an absence.
- **Format width remains open** for shapes not in the pattern set: split/multi-volume archives, 7z / rar
  / xz / zstd, encrypted archives, sparse bundles and DMGs, database files inside VM images, and Time
  Machine. **No zero is claimed for any of them.**
- **Docker volumes are outside a filesystem sweep by construction.** 9 live databases were enumerated
  through `docker` instead, and 9 stopped `postgres:16*` containers retain volumes **not** enumerated.

## 8. Instrument Defects Found In This Round's Own Method

| ID | Defect | Caught by |
|---|---|---|
| `RE-37` | `PGDMP` accepted on **magic prefix alone**; a file beginning `PGDMPX` was counted. | **failure control** |
| `RE-38` | `ODOOZIP` accepted any member ending `/dump.sql`, matching a **Gantt library sample** and a **57-byte Magento test fixture**. **Looser than the rule it replaced.** | inspecting the hits, not the count |
| `RE-39` | Path set omitted `~/Library/Group Containers`, which holds **4 known artefacts**. | **regression check against the prior population** |
| `RE-40` | **`timeout` does not exist on this host.** Every wrapped call returned "command not found" → empty output → recorded as `BLOCKED_IO`. **38 artefacts and 4 others were briefly declared unreadable on the strength of a missing utility.** | direct re-test without the wrapper |

**`RE-40` is the most serious.** It would have published *"all 38 artefacts blocked"* — a total
inversion — and it passed silently because an absent command and an unreadable file produce the same
empty string. The replacement instrument is an **in-process bounded read** (`signal.alarm`), which
distinguishes them; under it, the four `Group Containers` artefacts are **genuinely blocked**, and
everything else reads.
