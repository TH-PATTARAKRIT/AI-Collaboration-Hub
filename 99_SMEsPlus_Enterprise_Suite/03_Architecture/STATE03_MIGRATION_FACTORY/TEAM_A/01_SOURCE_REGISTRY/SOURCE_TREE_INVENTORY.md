# SOURCE_TREE_INVENTORY

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-28-MIG-A-EXPERT-DR-001 |
| Date | 2026-08-28 |
| Phase | A1 — Source Forensic Inventory |
| Provenance | P7 — Vendor Source Observation (customer-authorized copy) |
| Method | Read-only `os.walk` + AST manifest parse (`scan_source.py`), zero writes in source tree |
| Fact Status | VERIFIED FACT (counts measured, not estimated) |

## 1. Authorized Primary Source Root

`/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE`

Top-level contents (14 entries):

| Entry | Type | Bytes | Modified | Role |
|---|---|---:|---|---|
| `01 ACCOUNT/` | dir (62 modules) | 164,761,994 | content ≤ 2026-06-29 | Odoo Enterprise accounting module set |
| `01_ACCOUNT.zip` | archive | 34,371,329 | 2026-07-14 | archive of the above |
| `02 OTHER/` | dir (1,371 modules) | 1,693,861,873 | content ≤ 2026-06-29 | full Odoo addons corpus (community LGPL-3 + Enterprise OEEL-1) |
| `02_OTHER.zip` | archive | 504,676,674 | 2026-07-14 | archive of the above |
| `addons_extra/` | dir (69 modules) | 93,243,719 | extracted 2026-08-23 | customer custom + third-party addons |
| `addons_extra.zip` | archive | 77,391,974 | 2026-07-14 | archive of the above |
| `ks_dashboard_ninja/` | dir (1 module) | 82,703,503 | content ≤ 2024-02-19 | Ksolves Dashboard Ninja |
| `ks_dashboard_ninja-…zip` | archive | 79,354,049 | 2026-08-23 | archive of the above |
| `ks_dn_advance/` | dir (1 module) | 57,078,308 | content ≤ 2024-02-19 | Ksolves Dashboard Ninja Advance |
| `ks_dn_advance-…zip` | archive | 55,605,496 | 2026-08-23 | archive of the above |
| `iTEST02_2026-06-14_14-41-19.dump` | PostgreSQL custom dump v1.16 | 65,444,053 | 2026-07-14 (copy) | customer database dump |
| `.DS_Store` | macOS metadata | — | — | non-evidence |

## 2. Measured File Statistics (extracted areas)

| Area | Modules | Files | Bytes | Newest content file (excl. `.DS_Store`) |
|---|---:|---:|---:|---|
| `01 ACCOUNT` | 62 | 5,553 | 164,761,994 | ≤ 2026-06-29 |
| `02 OTHER` | 1,371 | 85,444 | 1,693,861,873 | 2026-06-29 |
| `addons_extra` | 69 | 2,393 | 93,243,719 | 2026-08-23 (extraction) |
| `ks_dashboard_ninja` | 1 | 273 | 82,703,503 | 2024-02-19 |
| `ks_dn_advance` | 1 | 196 | 57,078,308 | 2024-02-19 |
| **TOTAL** | **1,504** | **93,859** | **2,091,649,397 (~1.95 GiB)** | — |

## 3. File-Type Profile (top extensions per area)

| Area | Profile |
|---|---|
| `01 ACCOUNT` | .po 3,290 · .py 961 · .xml 680 · .js 283 · (none) 84 · .pot 62 · .scss 57 · .csv 44 · .svg 28 · .png 20 · .pdf 10 · .xlsx 10 |
| `02 OTHER` | .po 38,884 · .py 15,247 · .xml 11,194 · .js 8,389 · .webp 1,733 · .png 1,707 · .scss 1,618 · .svg 1,288 · .pot 1,229 · .csv 1,177 · (none) 855 · .jpg 537 |
| `addons_extra` | .png 584 · .py 547 · .po 435 · .xml 276 · .rst 94 · .csv 86 · **.pyc 86** · .xls 52 · .html 42 · .svg 41 |
| `ks_dashboard_ninja` | .png 150 · .js 23 · .py 19 · **.pyc 18** · .xml 17 · .css 14 |
| `ks_dn_advance` | .png 128 · .svg 24 · .gif 10 · .js 9 · .xml 7 · .py 5 · **.pyc 4** |

Observation: `.pyc` compiled files in `addons_extra` and both `ks_*` modules are evidence these
copies were taken from a **running deployment environment**, not from clean distribution
packages. (Fact Status: VERIFIED — files observed; interpretation: SUPPORTED INFERENCE.)

## 4. Manifest Parse Result

- 1,504 module manifests parsed (`__manifest__.py`), **0 parse errors**, 0 legacy `__openerp__.py`.
- License distribution (all areas): OEEL-1 744 · LGPL-3 706 · AGPL-3 22 · OPL-1 17 ·
  **UNDECLARED 12** · Other proprietary 2 · GPL-3 1.
- 90 modules flagged `application: True`.
- Full row-level register: `MODULE_MASTER_REGISTER_FULL.csv` (1,504 rows + header,
  SHA-256 `f11b1d74731dabd1cbe5e5d0c671c4daee1dc0c3d960cfabd1440f93d5e5faac`) —
  machine companion to `MODULE_MASTER_REGISTER.md`.

## 5. Integrity Notes

- Zero writes performed inside the source tree by this session (scanner is read-only; outputs
  land in session scratchpad and this factory only).
- Recent `.DS_Store` mtimes are Finder browsing artifacts, not content changes.
- Duplicate raw-source copying into the factory: **NOT performed** (per directive §7);
  the factory stores metadata, hashes, and registers only.
