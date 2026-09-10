# 00A_EVIDENCE_BASE_AND_PATH_SET.md
# Inventory Pilot — Evidence Base, PATH SET and Generation Basis (Execution Step 0)

Session: `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]`
**LAYER 2 — AUDIT QUARANTINE. Boss / PMO / AI-Audit only. Not for Team B or any downstream design surface.**

---

## 1. Why this file exists

The evidence base is itself a claim. Every prior programme defect of the class "X does not exist on
this host" was caused by a search boundary that was **described** instead of **declared**. This file
declares the boundary as a set.

---

## 2. Host sweep — declared PATH SET

Mounts enumerated (`ls /Volumes/`): `ChatGPT Installer`, `iMac`, `iMacSys`.
Home roots enumerated (`ls ~`). Cloud storage enumerated (`ls ~/Library/CloudStorage/`):
`GoogleDrive-jabsung.s@gmail.com`, `GoogleDrive-scgl.thailand@gmail.com`.

**Discovery pattern (content-based, not location-based):** a directory `P` is a reference addons root
iff `P/stock/__manifest__.py` exists **and** `P/account/` exists. This finds distributions wherever
they live, including cloud-storage trees.

`~/Library` was **NOT pruned** in this session. A prior programme prune of `~/Library` (adopted for a
TCC prompt-storm) concealed full reference distributions from three sweeps and two independent
experts; it is treated here as an evidence-affecting exclusion and was not repeated.

**Result: 36 reference addons roots located.** Full list with generation basis in §3.

---

## 3. Generation basis — content discriminator

A directory name is not a generation discriminator. A module manifest `'version'` string is not a
generation discriminator (**measured: every inventory module in every located root declares
`'version': '1.1'`**).

**Discriminator used:** presence of the framework's declarative-constraint construct in the inventory
module's model directory. It is present in series-19 code and absent in series-18 and earlier.
Corroborated by file-count identity of the inventory module and by localisation-module counts.

### Census result (36 roots)

| Idiom | Roots | Localisation modules (range) | Modules (range) |
|-------|------:|------------------------------|-----------------|
| series-19 | 20 | 1 – 523 | 182 – 1,433 |
| series-18 or earlier | 15 | 2 – 433 | 447 – 1,273 |
| (1 root duplicated by symlink/copy path) | 1 | — | — |

### Finding EB-01 — path name contradicts content (CRITICAL for method)

A root whose path segment names series 18 contains **series-19 code**: it carries the series-19
constraint construct, 514 localisation modules and an inventory module whose file count matches the
series-19 roots exactly (313) and not the series-18 roots (289–295).

**Consequence:** any prior or future analysis that selected this root by its path name analysed the
wrong generation. Recorded as a live hazard, not a historical note.

### Finding EB-02 — the obvious series-18 comparator is localisation-stripped

The root most likely to be chosen as "the series-18 tree" by name carries **2** localisation modules
against 523 in the series-19 primary. A cross-generation delta computed over that pair is dominated by
**root scope**, not by generation. Measured contamination: with the wrong comparator the scheduled-job
count appeared to move 10 → 26; with the scope-matched comparator it moves **20 → 26**.

---

## 4. Adopted roots for the Pilot

| Ref | Role | Generation basis | Modules with manifests | Localisation modules |
|-----|------|------------------|-----------------------:|---------------------:|
| **R1** | **PRIMARY** | series-19 idiom present; inventory module 313 files | 1,433 | 523 |
| **R2** | **DELTA COMPARATOR** | series-19 idiom absent; inventory module 290 files | 1,273 | 433 |

R1 is the newest located series-19 enterprise distribution on the host. R2 is the widest located
series-18 distribution, selected because its module scope is closest to R1's (1,273 vs 1,433) — the
scope-matching criterion, not the name-matching criterion.

**Every source finding in this package is bounded to R1 unless it explicitly carries an R2 delta.**

---

## 5. Runtime / database evidence

A database census was attempted. **No PostgreSQL server is running on this host** (socket absent) and
no cluster is started under either installed server version. Archive artefacts exist on the host
(dump and archive files above 5 MB were enumerated across all mounts and `$HOME`).

**Disposition: `HOLD — RUNTIME EVIDENCE NOT ESTABLISHED`.**

This is a bounded negative and it is recorded with its scope:

- **What is proved:** no live database was queryable from this session without starting a service.
- **What is NOT proved:** that no deployment evidence exists. Archive artefacts were located but
  **not opened**; an artefact that has been located and sized has not been read.

**Consequence for coverage (declared, not asserted):** every Pilot finding is a **source** finding.
No Pilot finding establishes **reachability** — whether a behaviour is latent or live on any real
deployment. Source analysis alone cannot rank severity by reachability. This bound is carried into
`INVENTORY_PILOT_COVERAGE_REPORT.md` as a coverage ceiling, not as a footnote.

---

## 6. Declared exclusions

| Excluded | Reason | Evidence-affecting? |
|----------|--------|---------------------|
| `static/`, `__pycache__/`, `i18n/` sub-trees | no functional declarations; translation and asset payloads | No — verified: no menu/action/view/model declaration file has these ancestors |
| `tests/` sub-trees | excluded from the **menu** enumerator only; the surface enumerator records them with a `test` flag rather than dropping them | No — flag preserved, count recoverable |
| 7 XML files that fail to parse | 4 zero-byte, 1 malformed test fixture, 2 zero-byte template stubs; **all 7 lie outside the Inventory module set** and none is a menu/action/view definition file | No — enumerated and named |
| Archive artefacts not opened | time-bounded; recorded as `HOLD`, see §5 | **YES — declared** |
| Live database | not available, see §5 | **YES — declared** |

**No prune in this session was taken for speed.** Every exclusion above is either proved
non-evidence-affecting or declared as affecting.
