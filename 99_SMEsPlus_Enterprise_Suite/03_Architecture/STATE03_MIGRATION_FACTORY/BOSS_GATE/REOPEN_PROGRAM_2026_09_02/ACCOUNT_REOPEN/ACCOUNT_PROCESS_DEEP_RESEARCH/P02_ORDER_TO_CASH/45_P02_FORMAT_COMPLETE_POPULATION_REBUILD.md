# 45 — P02 FORMAT-COMPLETE POPULATION REBUILD

*(mandated semantic name `31_P02_FORMAT_COMPLETE_POPULATION_REBUILD.md`; 31 taken, next free number used per §15.)*

`LAYER 2 — AUDIT QUARANTINE.` **CP-02 / CP-03.** Baseline `aca211e`.

**Status: `FILE PATH SET REBUILT AND RECONCILED — POPULATION BOUNDED, NOT CLOSED`.**

---

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
