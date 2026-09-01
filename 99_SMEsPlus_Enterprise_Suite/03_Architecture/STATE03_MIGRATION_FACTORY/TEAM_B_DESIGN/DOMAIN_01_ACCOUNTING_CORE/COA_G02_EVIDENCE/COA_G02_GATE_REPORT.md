# COA-G02 — Gate Report

Date: 2026-09-01
Gate: `COA-G02 — Base COA Kernel Discovery`
Boss authorization: `29eafce5bd9923d577167ecb8f9f1f63e88286df`

## 1. Execution Result

The Boss-authorized G02 discovery pass is complete at Team B evidence-production scope.

Evidence-backed result:

`BASE COA KERNEL CANDIDATE = 36 SEMANTIC ACCOUNTS`

The result is derived from:

`39 explicit ODOO18 default/control anchors - 9 net consolidation/extension adjustments + 6 mandatory non-anchor semantic additions = 36`.

This is **not** a forced `32` and is not the final Standard Thai COA.

## 2. Primary Evidence Verification

The Boss-approved workbook was independently re-downloaded/read during this execution.

- File: `Account_Odoo18_19 sent 270369.xlsx`
- Size: `307308` bytes
- SHA-256: `0b886e38cc8225e90e4534f04ed2bb6f2300e9f012e4ecc51edc1022e3e471f2`
- Exact match to G01 CORR4 recovery evidence
- ODOO18: 389 non-empty rows, 14 Account Types, reconcile True=33 / False=356
- Explicit `account.1_*` default/control anchors: 39

The `ODOO19` workbook tab is intentionally not used to derive G02 count; G02 remains on the G01-authorized source baseline of ODOO18 + separately verified `l10n_th` evidence.

## 3. Evidence Artifacts

1. `COA_G02_BASE_KERNEL_DISCOVERY_REGISTER.md`
2. `COA_G02_SOURCE_ANCHOR_DISPOSITION_REGISTER.md`
3. `COA_G02_SAAS_INVARIANT_COMPLIANCE.md`
4. `COA_G02_GATE_REPORT.md` (this file)

## 4. Key Controls Preserved

- `~32` remains a historical working expectation, not a target mandate.
- `389 source rows != 389 target accounts`.
- Account Code / Name / source technical ID are not canonical identity.
- Channel, POS, custodian and company-specific distinctions do not automatically multiply GL accounts.
- Tax-treatment differences are not silently merged.
- WHT form-level statutory granularity is explicitly reserved for G06.
- Accumulated-depreciation source classification conflict is not silently overwritten; K14's final type rule is deferred to G04.
- 19 ACTIVE Account Types remain unchanged; G02 does not require one default account per type.
- SI-01..SI-10 = 10/10 PASS at G02 classification/discovery scope.

## 5. Open Items That Are NOT G02 Blockers

| Item | Disposition | Owner Gate |
|---|---|---|
| Final Account Type/contra rule for accumulated depreciation | Controlled downstream dependency | G04 |
| Standard Template vs tenant/company provisioning/versioning | Controlled downstream dependency | G04S |
| Financial-statement line taxonomy | Controlled downstream dependency | G05 |
| WHT PND form-specific GL-vs-tax-subledger granularity | Controlled downstream dependency | G06 |
| Runtime multi-company/isolation proof | Controlled downstream dependency | G07 |

These are not converted into G02 evidence and receive no completion credit here.

## 6. Current Gate Status

`COA-G02 TEAM B DISCOVERY = COMPLETE`

`COA-G02 EVIDENCE PACKAGE = READY FOR CHATGPT INDEPENDENT AUDIT`

`COA-G02 FINAL GATE STATUS = PENDING INDEPENDENT AUDIT -> PMO -> BOSS DECISION`

COA-G03 is **NOT STARTED / NOT AUTHORIZED by this execution**.

## 7. Progress Governance

`% Board = TBD / NO APPROVED EVIDENCE-WEIGHTED DENOMINATOR`

`% STATE = TBD / NO APPROVED EVIDENCE-WEIGHTED DENOMINATOR`

`% STEP = TBD / NO APPROVED EVIDENCE-WEIGHTED DENOMINATOR`

No percentage is guessed.

No Evidence = No Progress. Never Skip Gate.
