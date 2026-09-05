# 41 — P05 EVIDENCE BASE RECONSTRUCTION

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E01`
Prompt `SMEPLUS-26-09-05-ACC-P05-E2P-EVIDENCE-BASE-LIVE-RISK-REPAIR-001`
Baseline verified: `96748109c1d56e7084a5d22ea3a1241d7e45336d` (short `9674810`), remote in sync.

## 1. Why This Was Needed

Round 2 (`P05#03`) recorded `RE-07`: the package had asserted no database evidence existed while five
readable dumps sat on the host. **Round 2 then made the same class of error again** — it enumerated
the dumps it happened to encounter rather than searching exhaustively, and reported "six registries"
as though that were a population.

**This reconstruction ran the exhaustive search that neither prior round ran.**

## 2. Declared Search — POPULATION, PATTERN, PATH SET, UNIT

```
find /Users/admin /Volumes/iMacSys \
  \( -name "*.dump" -o -name "*.backup" -o -name "*.sql" -o -name "*.sql.gz" \
     -o -name "*.pgdump" -o -name "*.custom" \) -type f -size +100k
```

- **PATH SET:** the entire user home **and** the entire project volume — not a folder.
- **PATTERN:** six archive extensions, ≥100 KB.
- **UNIT:** one file.
- **POPULATION:** **34 files**, reduced to **25 database candidates** after excluding IDE/browser/
  messaging artefacts (`state.vscdb.backup`, WhatsApp media, `Secure Preferences.backup`, etc.).

## 3. Result — the population Round 2 missed

| Archive identity (`dbname`) | Copies | Size | Readable | Known to Round 2? |
|---|---|---|---|---|
| `iTEST02` | **9 file copies**, 2 snapshot dates | 62 MB | yes | partly (2 of 9) |
| `iSMEs` | 1 | 148 MB | yes | yes |
| `iEVING` | 1 custom + **1 plain-SQL 60 MB** | 24 MB | yes | custom only |
| `BK12MAY26` | 1 | 34 MB | yes | yes |
| **`idemo18_uat`** | **1** | **44 MB** | **yes** | **NO — MISSED** |
| **`pankhamhom`** | **1** | **28 MB** | **yes** | **NO — MISSED** |
| `occ_sim` | **7 snapshots** | 3.2–3.6 MB | yes | 1 of 7 |
| `iErpOCC` | 1 | **0 B** | **no — cloud placeholder** | no |
| `iSCErP` | 1 | **0 B** | **no — cloud placeholder** | no |

**Distinct database identities: 9.** Readable in substance: **7**. Unreadable: **2** (zero-byte Google
Drive placeholders; `pg_restore -l` returns a header but there is no content — recorded as
`UNREADABLE — CLOUD PLACEHOLDER`, **not** as absence of a database).

> ### The decisive miss
>
> **`idemo18_uat` is an Odoo 18.0 database** — the exact target platform whose absence Round 2
> recorded as its principal gating unknown (`U-01` residue) and named as the cheapest unblocker.
> It was on this machine at `/Users/admin/OCC_BACKUP/` throughout, 44 MB, fully readable offline.
>
> Round 2 wrote: *"No Odoo 18 database carrying the P05 surface exists in the available evidence."*
> **That claim is class `E — CONTRADICTED`.** It was a class-B statement ("not found in the folders I
> looked in") published with class-A force, which is the exact defect `RE-07` was logged for one round
> earlier. Recorded as **`RE-20`**.

## 4. Reading Method — read-only, unchanged

`pg_restore --data-only --table=<t> -f <out> <dump>` — file-to-file. **No `-d` was ever passed. No
database was created, connected to, or restored. No dump was modified.** `pg_restore` refuses to run
without `-f` or `-d`, so the read path cannot silently touch an environment. v1.16 archives require
the PostgreSQL 18 client (`/opt/homebrew/Cellar/postgresql@18/18.6/bin/pg_restore`); v1.14/v1.15 are
readable by either.

## 5. Evidence Boundary

| Statement | Class |
|---|---|
| These 25 candidate files are every archive ≥100 KB with those six extensions under the two declared roots | **A** within the declared path set and pattern |
| Nine distinct database identities exist in that population | **A** |
| `idemo18_uat` is Odoo 18.0 and carries the P05 surface | **A** |
| No further Odoo 18 database exists anywhere | **B** — not searched outside the two roots; no network, cloud or server-side location was enumerated |
| The two zero-byte archives contain no P05 evidence | **D — UNKNOWN.** They are placeholders; their content was never downloaded. **Not** upgraded to absence. |

## 6. Consequence

The P05 evidence base is now materially different from the one every prior conclusion rested on.
`U-01`'s gating residue is **closed** (`42`, `43`); the petty-cash and employee-advance
reclassifications from Round 2 are **re-derived from scratch** (`45`, `46`); and one Round 2 headline
finding is **contradicted by production data** (`45`).
