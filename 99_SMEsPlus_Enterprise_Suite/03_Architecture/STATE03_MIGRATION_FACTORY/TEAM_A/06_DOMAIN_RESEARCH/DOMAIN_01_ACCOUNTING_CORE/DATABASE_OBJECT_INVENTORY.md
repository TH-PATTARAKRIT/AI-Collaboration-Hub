# DATABASE OBJECT INVENTORY — DOMAIN_01 (CORRECTED, CORR-01)

Evidence level: **DIRECTLY RE-VERIFIED** by `pg_restore -l` on `iTEST02_2026-06-14_14-41-19.dump`,
executed offline in a controlled ephemeral container. Metadata only.

## ARCHIVE HEADER — DIRECTLY VERIFIED
| Field | Value |
|---|---|
| Archive created | 2026-06-14 14:41:20 UTC |
| Database name | `iTEST02` |
| **TOC entries** | **28,648** |
| Compression | gzip |
| Dump version | 1.16-0 |
| Format | CUSTOM |
| Dumped from | PostgreSQL **18.4** (Debian 18.4-1.pgdg12+1) |
| Dumped by | pg_dump 18.4 |
| Owner role observed | `efaplus` |
| Extensions | pg_stat_statements, pg_trgm, vector (+3) |

## OBJECT-TYPE CENSUS — DIRECTLY VERIFIED (whole database)
| Object type | Count |
|---|---:|
| FK CONSTRAINT | 5,141 |
| SEQUENCE | 2,871 |
| TABLE | 2,763 |
| CONSTRAINT (PK/UNIQUE/**CHECK**) | 1,860 |
| INDEX | 1,808 |
| TABLE DATA | 1,395 |
| DEFAULT | 888 |
| VIEW | 36 |
| RULE | 9 |
| EXTENSION | 6 |
| **TRIGGER** | **0** |

Two numbers matter for this domain: **TRIGGER = 0** and the presence of CHECK constraints
inside the 1,860 CONSTRAINT entries.

## RECONCILIATION AGAINST PRIOR EVIDENCE
| Metric | Prior (Evidence_CSV, P5) | Direct observation (P2) | Assessment |
|---|---:|---:|---|
| Tables | 1,395 | 1,395 TABLE DATA entries | **CONFIRMED** |
| FK constraints | 5,141 | 5,141 | **CONFIRMED** |
| PK constraints | 1,392 | within 1,860 CONSTRAINT | consistent |
| UNIQUE | 149 | within 1,860 CONSTRAINT | consistent |
| CHECK constraints | 0 | **present — 4 on account_move_line alone** | **PRIOR EVIDENCE INCOMPLETE — corrected** |
| Triggers | not captured | **0** | **NEWLY ESTABLISHED** |
| Rules | not captured | 9, all view `_RETURN` | **NEWLY ESTABLISHED** |

The `TABLE` count (2,763) exceeds `TABLE DATA` (1,395) because relation/join tables and tables
without data sections still appear as TABLE entries.

## ACCOUNTING CORE OBJECTS — DIRECTLY VERIFIED PRESENT
Accounting objects exist · journal objects exist · journal-entry structures exist ·
journal-line structures exist · configuration objects exist · lock objects exist ·
company-boundary objects exist.

| Object | Present | Data section |
|---|---|---|
| account_account | YES (PK `account_account_pkey`) | YES |
| account_account_tag | YES (+ UNIQUE `account_account_tag_name_uniq`) | YES |
| account_journal | YES (+ UNIQUE `account_journal_code_company_uniq`) | YES |
| account_move | YES (PK `account_move_pkey` + FKs) | YES |
| account_move_line | YES (PK + FKs + **4 CHECK constraints**) | YES |
| account_full_reconcile | YES | YES |
| account_partial_reconcile | YES | YES |
| account_lock_exception | YES | YES |
| account_fiscal_position_account | YES (UNIQUE src/dest) | — |
| account_journal_group | YES (UNIQUE name) | — |

Currency and company boundary objects are present via `account_move.account_move_currency_id_fkey`
and `account_move_company_id_fkey` (directly observed FK entries).
