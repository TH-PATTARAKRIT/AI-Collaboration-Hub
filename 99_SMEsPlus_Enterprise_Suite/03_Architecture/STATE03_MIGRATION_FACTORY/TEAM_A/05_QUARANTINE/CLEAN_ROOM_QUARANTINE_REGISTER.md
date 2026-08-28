# CLEAN_ROOM_QUARANTINE_REGISTER

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-28-MIG-A-EXPERT-DR-001 |
| Date | 2026-08-28 |
| Rule | Class E (vendor-specific observation) and Class F (source-system technical detail) findings are Team A knowledge only — NEVER Team B input. CLASS-D items additionally carry license/IP uncertainty. |

## 1. CLASS-D License Quarantine — 12 modules (CARRY-FORWARD, still controlled)

Carried forward from STEP040301 classification + MIG-A-001 gate (re-verified independently this
session from fresh manifest parsing; sets match exactly). No reuse cleared. Boss ruling on
CLASS-D remains pending (prior gate HOLD item).

| Module | Author (manifest) | Version | Note |
|---|---|---|---|
| `bi_print_journal_entries` | BrowseInfo | 1.0.0 | third-party, no license key |
| `dev_print_cheque` | DevIntelle | 19.0.1.3 | third-party, no license key |
| `equipment_sequence` | SMEsPlus Co.,Ltd | 19.0.1.4 | customer-authored |
| `full_summarize_bills` | SMEsPlus Co.,Ltd | 19.0.0.1 | customer-authored |
| `invoice_promptpay` | SMEsPlus | 19.0.1.0 | customer-authored |
| `print_payment_remittance_adviec` | SMEsPlus Co.,Ltd | 19.0.1.1 | customer-authored |
| `print_voucher_request` | SMEsPlus Co.,Ltd | 19.0.1.0 | customer-authored |
| `product_stock_equipment` | Scg-Legacy | 19.0.1.0 | customer-authored |
| `sale_productinfo_ext` | (none) | 19.0.1 | author undeclared |
| `smesplus_product_image` | SMEsPlus | 19.0.1.0 | customer-authored |
| `smesplus_special_access_rights` | SMEsPlus Co.,Ltd | 19.0.1.0 | customer-authored; security-critical |
| `smesplus_uom_ext` | (none) | 19.0.1.0 | author undeclared |

Observation for Boss decision support (not a ruling): 10 of 12 appear customer-authored
(SMEsPlus/Scg-Legacy manifests) — customer ownership confirmation could clear them; the 2
third-party ones (BrowseInfo, DevIntelle) need vendor license verification.

## 2. Class E/F Restricted Observations Created This Session

| ID | Restricted content | Where held | Class |
|---|---|---|---|
| Q-E01 | Odoo module technical inventory (model counts, `_name`/`_inherit` structures, per-module dependency graphs) in MODULE_MASTER_REGISTER §5–§6 and the workflow evidence JSONs | Factory registers + session scratchpad archive | E/F |
| Q-E02 | Dump internal table-name samples and PostgreSQL version markers | DATABASE_DUMP_REGISTER.md | F |
| Q-E03 | Vendor state/technical detail from prior 591-model extraction (referenced, not copied) | prior STEP040304R4 evidence | E/F |
| Q-E04 | Security-relevant implementation facts (TLS verify=False, plaintext tokens, `_check_access` override, runtime pip install) | MODULE_MASTER_REGISTER.md §6 | F |

Handling rule: these artifacts live in Team A registries only. Any Team B candidate derived from
them must first pass Neutralization (Phase A7) → Classification (A8) → ChatGPT audit → PMO →
Boss gate. Nothing in this register is cleared for Team B.

## 3. Proprietary-License Exposure Map (context for quarantine discipline)

- OEEL-1: 744 modules (Odoo Enterprise) — code readable for source understanding under
  customer's deployment rights; **implementation reuse prohibited** (clean-room rule +
  license). 31-module metadata-only + 19 permanently-black-box constraints from STEP040303/R4
  remain binding for deep research.
- OPL-1: 17 modules (Ksolves ×2, Domiup multi_level_approval ×3, Openinside oi_* ×3,
  bm_thai_rd_vat_company_search, contact_reference_sequence, import_bridge_axis, + 4 in 02 OTHER, …).
- Other proprietary: 2. GPL-3: 1 (`deepseek_r1` — copyleft, flag for license review).
