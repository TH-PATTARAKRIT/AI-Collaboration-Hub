# EC-01 — Source Identity & Integrity Verification

Session: `[SMEPLUS-26-08-28-DEEP-CD-001]`  
Decision Authority: Boss — Sole Final Approver  
Authorization: `DEC-DEEP-CD-003`  
Independent Review Date: 2026-08-29 Asia/Bangkok  
Status: `PASS WITH CONTROL — CANONICAL PROJECT SOURCE IDENTIFIED`

## Objective

Cryptographically and structurally identify the authoritative project source archives before source-baseline reconciliation.

## Important Reconciliation of Intake Names

The three ChatGPT conversation attachments were recorded as:

- `01_ACCOUNT(1).zip`
- `02_OTHER(1).zip`
- `addons_extra(1).zip`

Those attachment aliases were not byte-compared in this runtime to the canonical project copies. Therefore exact attachment-alias equality is **not asserted**.

The authoritative project source path was independently located through the Team A A0/A1 evidence pack:

`/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE`

The canonical archives at that source root are the evidence used for EC-01.

## Canonical Archive Evidence

| Source | Canonical Artifact | Bytes | Modified | SHA-256 | Evidence |
|---|---|---:|---|---|---|
| SRC-CAN-001 | `01_ACCOUNT.zip` | 34,371,329 | 2026-07-14 | `3a40f2499f2db5688c53e437ba1f51c967d4e158aae72010eed740647c1b9ba1` | Team A `SOURCE_MANIFEST.md` + `SOURCE_MANIFEST.sha256` |
| SRC-CAN-002 | `02_OTHER.zip` | 504,676,674 | 2026-07-14 | `f263c81e9908673bb0a83212f880996c87e6aa5e1b1cf2d89410c2aaa24d1d5b` | Team A `SOURCE_MANIFEST.md` + `SOURCE_MANIFEST.sha256` |
| SRC-CAN-003 | `addons_extra.zip` | 77,391,974 | 2026-07-14 | `f66767aff965ce74f1e37e57c28bb69abf85932db0bb2b9d41307654037d0f52` | Team A `SOURCE_MANIFEST.md` + `SOURCE_MANIFEST.sha256` |

## Structural Evidence

Team A read-only source inventory reports:

- `01 ACCOUNT`: 62 modules / 5,553 files
- `02 OTHER`: 1,371 modules / 85,444 files
- `addons_extra`: 69 modules / 2,393 files
- `ks_dashboard_ninja`: 1 module / 273 files
- `ks_dn_advance`: 1 module / 196 files
- total observed source: 1,504 modules / 93,859 files
- 1,504 `__manifest__.py` records parsed with 0 parse errors
- archive/extracted-family integrity was checked in Team A read-only inventory procedure

Evidence paths:

- `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/01_SOURCE_REGISTRY/SOURCE_MANIFEST.md`
- `.../SOURCE_MANIFEST.sha256`
- `.../SOURCE_TREE_INVENTORY.md`
- `.../A1_SOURCE_LANDSCAPE.md`
- commit lineage reviewed at `c44144387061f3cd48665d499641ce0da540a731`

## Independent Review Position

| Control | Result |
|---|---|
| Canonical source location | VERIFIED |
| Canonical archive names | VERIFIED |
| SHA-256 evidence | VERIFIED FROM INSPECTABLE TEAM A HASH REGISTER |
| Byte sizes | VERIFIED FROM INSPECTABLE TEAM A REGISTER |
| Source-tree inventory | VERIFIED FROM INSPECTABLE TEAM A REGISTER |
| Manifest parse coverage | VERIFIED FROM INSPECTABLE TEAM A REGISTER |
| Conversation attachment `(1)` aliases byte-identical to canonical archives | NOT VERIFIED / NOT ASSERTED |
| Raw source copied into this research branch | NO |

## Gate Result

`EC-01 = PASS WITH CONTROL`

`DR-GAP-001 = CLOSED FOR CANONICAL PROJECT SOURCE IDENTITY`

Control retained: exact byte equality between the three ChatGPT attachment aliases and the canonical source archives is not needed for the canonical project source gate and is not claimed.

## Next Step

Proceed to EC-02 — Source Manifest & Baseline Lineage Reconciliation.

## Governance

- No Evidence = No Progress.
- Never Skip Gate.
- CLASS-D remains quarantined.
- No source implementation is transferred into target architecture.
- PR #62 remains Draft/Open/Not Merged.
