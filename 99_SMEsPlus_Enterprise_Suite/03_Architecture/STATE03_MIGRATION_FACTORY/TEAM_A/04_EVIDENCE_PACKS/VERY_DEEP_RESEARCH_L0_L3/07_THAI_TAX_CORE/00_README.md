# Thai Tax Core — lane index and completion checklist

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Priority lane per Boss/verifier order (2026-10-02). Source/dump evidence is not runtime proof and not statutory proof. No formal percentage; nothing is Complete until Claude semantic verification is accepted. Extra/Custom/OEEL-1/OPL-1/proprietary logic was not inspected; no SMEsPlus Functional Design was started. Restricted Technical Evidence (files 01–11 and the unit files) is kept separate from the Neutral Clean-Room Knowledge Pack (file 12).

| # | Required completion output | File | Built from | State |
|---|---|---|---|---|
| 1 | Thai Tax Core Function Catalog | `01_THAI_TAX_CORE_FUNCTION_CATALOG.md` | TXA1 (85 rows) + TXA2 (40 rows) | assembled; 125 candidate catalogue entries (not Function-IDs) |
| 2 | Business Rule Register | `02_BUSINESS_RULE_REGISTER.md` | TXA1 (71) + TXA2 (50) | assembled |
| 3 | Source/Override Map | `03_SOURCE_OVERRIDE_MAP.md` | TXA1 (25) + TXA2 (21) | assembled |
| 4 | Field-to-Schema Mapping | `04_FIELD_TO_SCHEMA_MAPPING.md` | TXC (1,285 rows; 44 models; constraint/index/relation reconciliations remain in the TXC unit file) | assembled |
| 5 | State and Reversal Matrix | `05_STATE_AND_REVERSAL_MATRIX.md` | TXA2 (20 rows) | assembled (TXA1 has none) |
| 6 | Accounting Impact Matrix | `06_ACCOUNTING_IMPACT_MATRIX.md` | TXA2 (17 rows) | assembled |
| 7 | Thai Statutory Source Register | `07_THAI_STATUTORY_SOURCE_REGISTER.md` (copy of `TXS_…register.md`) | TXS (120 statements; 5 CONFLICT, 8 UNVERIFIED) | **supplement TXS-R1 in progress** (raw re-read of conflicts and summarised high-risk statements) |
| 8 | Native Capability vs Gap Matrix | `08_NATIVE_CAPABILITY_VS_GAP_MATRIX.md` | TXA1+TXA2 catalogues: NATIVE 86 · PARTIAL 28 · NATIVE GAP / EXTENSION REQUIRED 9 · UNKNOWN 2 | assembled; **every gap's statutory need is pending TXS validation** — absence in Community is not proof the requirement does not exist |
| 9 | Contradiction Register | `09_CONTRADICTION_REGISTER.md` | CONTRA-flagged tax-relevant claims (keyword filter) | assembled; the cross-unit corrections are in `../05_CORRECTION_LOOP/` |
| 10 | Unknown Register | `10_UNKNOWN_REGISTER.md` | UNKNOWN-class tax-relevant claims | assembled |
| 11 | Runtime-Required Register | `11_RUNTIME_REQUIRED_REGISTER.md` | RT-flagged tax-relevant claims (no runtime inference) | assembled; full AWT index in `../06_AWT_BACKLOG/` |
| 12 | Neutral Clean-Room Knowledge Pack | `12_NEUTRAL_CLEAN_ROOM_KNOWLEDGE_PACK.md` | neutral files of TXA1, TXA2, TXC, U13, U23, U24, U25, TXS | assembled (concatenation; each statement keeps its id and claim links) |

## Native gap candidates (statutory need pending TXS validation)
Tax-closing routine · tax period / tax-return object · automatic tax-lock maintenance · non-claimable (prohibited) input VAT treatment · payee-driven withholding selection and payment-level withholding certificates/reports · replacement/re-issued tax document linkage · automatic exchange-rate feed · taxable-supply (tax-point) date computation. Details and claim ids: file 08 and units TXA1/TXA2/TXC/U24.

## Known statutory conflicts carried (see TXS and TXS-R1)
Taxpayer-ID length (10 vs 13 digits across RD pages), VAT FX-rate basis, superseded FX order, WHT minimum amount, Sec. 70 rate; and seed-register conflicts (WHT e-filing mandate date, ETDA standard number).

## Limits
Tax-relevant register extracts are keyword-filtered from unit claims; summary counts in files 08–11 are not coverage figures. Thai legal requirements appear only in the statutory register, each with its own verification status; Odoo behaviour is never used to prove a requirement.
