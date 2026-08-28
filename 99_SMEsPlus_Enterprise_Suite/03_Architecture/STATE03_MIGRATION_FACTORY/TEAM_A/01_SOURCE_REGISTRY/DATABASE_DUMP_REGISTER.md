# DATABASE_DUMP_REGISTER

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-28-MIG-A-EXPERT-DR-001 |
| Date | 2026-08-28 |
| Phase | A1 — Source Forensic Inventory |
| Provenance | P6 — Customer-approved database evidence |
| Restore performed this session | **NO** (file-level forensics only; `pg_restore`/`psql` not on PATH, Docker daemon down) |

## 1. Primary Dump — `iTEST02_2026-06-14_14-41-19.dump`

| Attribute | Value | Fact Status |
|---|---|---|
| Logical database | `iTEST02` (from filename; snapshot taken 2026-06-14 14:41:19) | SUPPORTED INFERENCE (filename convention) |
| Copies | 2 — `…/01 ACCOUNT/SOURCE CODE/` (mtime 2026-07-14) and `…/01 ACCOUNT/` (mtime 2026-06-29) | VERIFIED |
| Copy identity | **Byte-identical** — SHA-256 `d67fff6dbd3a957a5089e3bd7f982b1f8a98b954e8be2e40e6c227a70339d8c0` both; `cmp` clean | VERIFIED |
| Size | 65,444,053 bytes | VERIFIED |
| Format | PostgreSQL custom-format archive, format version v1.16-0 (`PGDMP` magic present) | VERIFIED (`file` + header probe) |
| Creator | pg_dump **18.4** (Debian 18.4-1.pgdg12+1); server version **PostgreSQL 18.4** | VERIFIED (internal version markers via read-only header probe) |
| Table-name probe (strings sample) | Odoo schema visible: `account_account`, `account_account_tag`, `account_accrued_orders_wizard`, many `*_rel` tables; Thai customization visible: `account_account_create_withholding_tax_cert_rel`; **non-Odoo-named table `Products` (capitalized)** — origin UNKNOWN, likely import/staging artifact → gap G-07 | VERIFIED (names observed); interpretation SUPPORTED INFERENCE |

## 2. Prior Database Evidence Chain (referenced, not re-derived)

| Evidence | Location | Content |
|---|---|---|
| R3A DB Evidence Inventory | `ACCOUNT/01 ACCOUNT/STEP040304R3A_DB_EVIDENCE_INVENTORY/` | Prior DB evidence gate-closed (G01–G14 all PASS); ruling: do not restart inventory |
| R3B Source↔Dump Reconciliation | `ACCOUNT/01 ACCOUNT/STEP040304R3B_DB_RECONCILIATION/` | Boss-extra source-to-dump mapping, drift analysis, restore decision evidence |
| R3C Controlled Restore | `ACCOUNT/01 ACCOUNT/STEP040304R3C_CONTROLLED_RESTORE/` (2026-08-23) | Method: NO database server created; per-table `pg_restore --data-only --table=<t>` inside ephemeral Docker (`--rm`, `--network none`); scope: THAILAND-SCOPE ONLY / NO PERSONAL DATA EXPORT / CLEAN-ROOM EVIDENCE ONLY |
| Dump column register | `06 MIGRATION FACTORY/TEAM A_SOURCE_EXTRACTION_OBSERVATION/04_MAPPING_EVIDENCE/` | Current V1.2 column rows **13,942** vs historical Phase B v1.5 closure **13,940** — delta reconciled row-level, status RECONCILED / PASS (session MIG-A-001) |
| Dump table inventory | `ACCOUNT/03 DATABASE/V1.1/Dump_Table_Inventory.csv` (196,089 B) + `Source_to_Dump_Mapping_Validation.csv` (1,306,018 B) | Customer-era table inventory & source↔dump mapping validation (V1.1 pack, 2026-06-29) |

## 3. `ACCOUNT/03 DATABASE/` — What It Actually Is

**Documentation/mapping-pack version dirs (V1.1, V1.2, V1.3, V1.4, V.1.4, V1.5, V2.0), NOT raw
dumps.** No `.dump`/`.sql`/`.backup` exists under `03 DATABASE` (confirmed by R3A inventory and
this session's listing). Packs contain Module_Inventory.csv, Dump_Table_Inventory.csv,
Source_to_Dump_Mapping_Validation.csv, Accounting_Table_Details.csv, charter/PM/architecture/
functional/technical documents (14-section structure). The only raw dump in the project is
`iTEST02_2026-06-14_14-41-19.dump` (§1).

## 4. Open Items for Database Deep Observation (Phase A5/L9)

1. This session performed **file-level observation only**. Full object inventory
   (`DATABASE_OBJECT_INVENTORY.md`), relationship register, data profile, and exception register
   remain to be produced in the domain/database phase, using the same controlled method as R3C
   (ephemeral container, no network, Thailand scope, no personal-data export) — **requires
   Docker daemon (colima) started; Boss/PMO awareness noted** since prior authorization was
   step-scoped to R3C.
2. Dump is dated **2026-06-14** — 75 days older than today's source snapshot state; freshness /
   representativeness for final migration profiling is a business decision → gap G-08.
3. `Products` capitalized table origin → gap G-07.
