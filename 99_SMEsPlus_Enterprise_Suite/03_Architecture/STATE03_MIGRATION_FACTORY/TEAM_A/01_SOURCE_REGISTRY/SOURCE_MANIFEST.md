# SOURCE_MANIFEST

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-28-MIG-A-EXPERT-DR-001 |
| Date | 2026-08-28 |
| Phase | A1 — Source Forensic Inventory |
| Machine companion | `SOURCE_MANIFEST.sha256` (verify with `shasum -a 256 -c`) |
| Hash tool | macOS `shasum -a 256` |
| Rule honored | §7 — raw source NOT duplicated into the factory; registered by path + hash instead |

## Registered Primary Assets

| # | Asset (absolute path) | Bytes | Modified | SHA-256 (short) | Classification |
|---|---|---:|---|---|---|
| 1 | `…/01 ACCOUNT/SOURCE CODE/iTEST02_2026-06-14_14-41-19.dump` | 65,444,053 | 2026-07-14 | `d67fff6d…39d8c0` | CUSTOMER DATABASE DUMP (restricted — never commit) |
| 2 | `…/01 ACCOUNT/iTEST02_2026-06-14_14-41-19.dump` | 65,444,053 | 2026-06-29 | `d67fff6d…39d8c0` | duplicate copy — **byte-identical to #1 (verified)** |
| 3 | `…/SOURCE CODE/01_ACCOUNT.zip` | 34,371,329 | 2026-07-14 | `3a40f249…c1b9ba1` | VENDOR SOURCE ARCHIVE (restricted) |
| 4 | `…/SOURCE CODE/02_OTHER.zip` | 504,676,674 | 2026-07-14 | `f263c81e…24d1d5b` | VENDOR SOURCE ARCHIVE (restricted) |
| 5 | `…/SOURCE CODE/addons_extra.zip` | 77,391,974 | 2026-07-14 | `f66767af…37d0f52` | CUSTOMER CUSTOMIZATION ARCHIVE (restricted) |
| 6 | `…/SOURCE CODE/ks_dashboard_ninja-20260823T085058Z-1-001.zip` | 79,354,049 | 2026-08-23 | `aac737c8…c6ff9e9` | THIRD-PARTY MODULE ARCHIVE (restricted) |
| 7 | `…/SOURCE CODE/ks_dn_advance-20260823T085058Z-1-001.zip` | 55,605,496 | 2026-08-23 | `a079d386…8296a79` | THIRD-PARTY MODULE ARCHIVE (restricted) |
| 8 | `…/01 ACCOUNT/SOURCE CODE-20260823T131112Z-1-001.zip` | 804,282,956 | 2026-08-23 | `76091aa2…b5f95bf0` | UMBRELLA SOURCE ARCHIVE (Google Takeout-style export of SOURCE CODE) |
| 9 | `…/ACCOUNT/03 DATABASE.zip` | 5,313,706 | 2026-06-29 | `8059ffc2…db9918f` | DB WORKING-AREA ARCHIVE (restricted) |
| 10 | `…/ACCOUNT/03 DATABASE/V1.5.zip` | 5,882,964 | 2026-06-29 | `de1f550b…4cf6a29` | DB WORKING-AREA ARCHIVE (restricted) |
| 11 | `TEAM_A/01_SOURCE_REGISTRY/MODULE_MASTER_REGISTER_FULL.csv` | 1,505 lines | 2026-08-28 | `f11b1d74…5e5faac` | TEAM A EVIDENCE ARTIFACT (committable) |

`…` = `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT` prefix; full paths are in the
`.sha256` machine file.

## Facts Established

1. **Dump deduplication (VERIFIED FACT):** the two `iTEST02_2026-06-14_14-41-19.dump` copies are
   byte-identical (identical SHA-256). One logical customer database snapshot exists, dated
   2026-06-14 14:41:19, of database `iTEST02`.
2. **Chain of custody:** archives #3–#5 dated 2026-07-14; #6–#8 exported 2026-08-23
   (timestamped export names `…20260823T…Z`); extracted trees match the archive family
   (extraction-status detail in `A1_SOURCE_LANDSCAPE.md`).
3. **GitHub rule:** assets #1–#10 are raw source / dumps / proprietary archives —
   **prohibited from GitHub** per directive §9. Only registers, hashes, and `.md` research
   artifacts are committed.
