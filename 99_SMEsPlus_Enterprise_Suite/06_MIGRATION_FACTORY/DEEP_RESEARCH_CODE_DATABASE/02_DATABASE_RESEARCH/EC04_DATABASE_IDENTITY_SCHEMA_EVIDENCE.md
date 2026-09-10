# EC-04 — Database Identity + Schema Evidence Review

Session: `[SMEPLUS-26-08-28-DEEP-CD-001]`  
Date: 2026-08-29 Asia/Bangkok  
Reviewer: ChatGPT L99 / Evidence Gate Review  
Technical Evidence Status: `PASS WITH CONTROL`  
Workflow Gate Status: `PARKED — EC-03 REMAINS HOLD`

## Objective

Verify the identity, integrity, format, version, and available schema lineage of the database dump used for code↔database and migration-fact research.

## Primary Dump Identity

Artifact: `iTEST02_2026-06-14_14-41-19.dump`

| Attribute | Evidence Result |
|---|---|
| Logical database | `iTEST02` — supported inference from filename convention |
| Snapshot timestamp | 2026-06-14 14:41:19 — filename evidence |
| Copies observed | 2 |
| Copy identity | VERIFIED BYTE-IDENTICAL |
| SHA-256 | `d67fff6dbd3a957a5089e3bd7f982b1f8a98b954e8be2e40e6c227a70339d8c0` |
| Size | 65,444,053 bytes |
| Archive format | PostgreSQL custom-format archive, v1.16-0 (`PGDMP`) |
| Creator | pg_dump 18.4 (Debian 18.4-1.pgdg12+1) |
| Server version marker | PostgreSQL 18.4 |
| Read-only header probe | Odoo accounting schema names observed; Thai WHT customization relation observed |

## Prior Schema / Restore Evidence Chain

Team A database register references:

- R3A — DB Evidence Inventory
- R3B — Source↔Dump Reconciliation
- R3C — Controlled Restore (2026-08-23)

R3C method is recorded as per-table `pg_restore --data-only --table=<t>` inside an ephemeral Docker container using `--rm` and `--network none`, Thailand-scope only, with no personal-data export.

The current Team A session itself performed file-level forensics only; it did not restore the dump.

## Column Lineage

The database evidence chain records:

- Historical Phase B: 13,940 column rows
- Current V1.2 register: 13,942 column rows
- Delta: +2 rows
- Team A database register records this delta as row-level reconciled / PASS in prior MIG-A-001 evidence.

This review accepts the existence of the reconciliation evidence chain, but does not re-execute the underlying database extraction in this runtime.

## Evidence Reviewed

- `03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/01_SOURCE_REGISTRY/DATABASE_DUMP_REGISTER.md`
- `.../SOURCE_MANIFEST.md`
- `.../SOURCE_MANIFEST.sha256`
- `.../A1_SOURCE_LANDSCAPE.md`
- `.../10_SESSION_ARCHIVE/SESSION_SMEPLUS-26-08-28-MIG-A-EXPERT-DR-001_CLOSURE.md`
- evidence commit reviewed: `c44144387061f3cd48665d499641ce0da540a731`

## Gate Test

| Test | Result |
|---|---|
| Dump identity | PASS |
| Dump SHA-256 | PASS |
| Dump size | PASS |
| Dump format/version | PASS |
| Duplicate-copy integrity | PASS |
| Prior controlled restore evidence exists | PASS WITH CONTROL — referenced prior evidence, not re-executed here |
| 13,940 → 13,942 column delta lineage | PASS WITH CONTROL — prior row-level reconciliation referenced |
| Freshness vs 2026-08-28 source snapshot | HOLD CONTROL — dump is dated 2026-06-14 |
| Full current data-quality/anomaly validation | NOT YET — EC-07 |

## Technical Evidence Result

`DR-GAP-005 = CLOSED WITH CONTROL — DATABASE DUMP IDENTITY IS CRYPTOGRAPHICALLY IDENTIFIED`

`DR-GAP-006 = EVIDENCE FOUND / PASS WITH CONTROL — TWO-COLUMN DELTA REPORTED RECONCILED IN PRIOR REGISTER`

The following controls remain open and are not waived:

- dump freshness/representativeness for final migration profiling;
- stronger current schema/metadata validation where required;
- DB-only inventory;
- anomaly/orphan/duplicate/cross-company/ledger/inventory validation;
- current mapping lineage.

## Workflow Gate Position

Because EC-03 remains HOLD, this EC-04 evidence review is **not represented as sequential gate advancement**. The technical evidence is prepared and reviewed so work does not stall, but the controlled closure sequence remains parked at EC-03.

No coding, schema freeze, migration-engine build, release, deployment, or production migration is authorized.
