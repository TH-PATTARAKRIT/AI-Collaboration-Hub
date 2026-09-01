# 02 — CORR-005 SHA-256 Reproduction (Independent)

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Independently recompute CORR-005's claimed 27-file manifest directly from git blob content, not by re-reading the manifest's own claims | Claude (IDR-007) | This artifact | 2026-09-01 | Self (mechanical `git show \| shasum -a 256`) | 27/27 reproduced, byte-for-byte | Confirms package integrity is real, not asserted |

## Method

Unlike IER-003 (which reproduced the DR-002→A19 manifest) and CORR-005 (which authored the 07 manifest), this review computed hashes **independently and directly from git blob content**, without pre-reading the CORR-005 manifest's claimed values, then diffed the two lists. Command pattern used for every file, run at commit `d69da7900941bdae209eb33af20ac24e4893d536`:

```
git show <commit>:"<path>" | shasum -a 256
```

This bypasses any risk that a manifest could describe file content that no longer matches what is actually stored in the commit — a failure mode a self-reported manifest cannot rule out on its own.

## Scope claimed by `07_CORR005_FINAL_SHA256_MANIFEST.txt`

Header, quoted: `"Physical files covered: 21 (Section A) + 6 (Section B) = 27. Operational SHA-256 entries: 27."` Section A = the full current-state `DEEP_RESEARCH_DR002/EXECUTION/` package (21 files, A0-A20); Section B = the six CORR-005 content deliverables (01-06); file 07 (the manifest itself) is excluded from self-hash, matching this project's established convention (same as A19's own header rule).

## Result — Section A (21/21 files, DR-002 EXECUTION package)

| File | Manifest-claimed SHA-256 | Independently computed SHA-256 | Match |
|---|---|---|---|
| A0_GOVERNANCE_AND_BASELINE_VERIFICATION.md | `ced0834773b2240597318c965be7c380c70080c46878201555c695ca522a6b38` | `ced0834773b2240597318c965be7c380c70080c46878201555c695ca522a6b38` | ✅ |
| A1_INVENTORY_SOURCE_LANDSCAPE_AND_MODULE_SCOPE.md | `548301a91f1595c8e6ccfe587733ba04bc15316715ca3d65ed26f40501c0e781` | `548301a91f1595c8e6ccfe587733ba04bc15316715ca3d65ed26f40501c0e781` | ✅ |
| A2_DATABASE_DUMP_FORENSIC_REGISTER.md | `c6f6222c24fea94ad9533cba306af92867d0b5a7d5c1ba85225ecd56af55a2a7` | `c6f6222c24fea94ad9533cba306af92867d0b5a7d5c1ba85225ecd56af55a2a7` | ✅ |
| A3_STOCK_TRUTH_AND_QUANTITY_SEMANTICS.md | `abf734dbf793f5f02951c658a219906d63f79d2f139b83bd25e8e871654618c7` | `abf734dbf793f5f02951c658a219906d63f79d2f139b83bd25e8e871654618c7` | ✅ |
| A4_STATE_EVENT_LIFECYCLE_EVIDENCE.md | `94ecc404cbed0e6470b761502e3524cc9f867eafd1258f099a2f22a74c5c6b30` | `94ecc404cbed0e6470b761502e3524cc9f867eafd1258f099a2f22a74c5c6b30` | ✅ |
| A5_WAREHOUSE_LOCATION_PRODUCT_UOM_TRACEABILITY.md [CORR-005 edited] | `c9a0135fd65872aa9b6010beb308ce3d399773f31819ce89a3cab5ffb9886ca5` | `c9a0135fd65872aa9b6010beb308ce3d399773f31819ce89a3cab5ffb9886ca5` | ✅ |
| A6_ROUTE_PROCUREMENT_REPLENISHMENT_EVIDENCE.md | `d785da9f5c2a9150e097421b38ae6af481990ff30361c852c8f57249fcf59b2e` | `d785da9f5c2a9150e097421b38ae6af481990ff30361c852c8f57249fcf59b2e` | ✅ |
| A7_ADJUSTMENT_COUNT_CUTOFF_EVIDENCE.md [CORR-005 edited] | `56dc679f9a2511d8a96f48f53626a51875d19d48951e0f4955605402927cd83d` | `56dc679f9a2511d8a96f48f53626a51875d19d48951e0f4955605402927cd83d` | ✅ |
| A8_CROSS_DOMAIN_PHYSICAL_HANDOFF_MATRIX.md | `b0a8f07fb9f61e7541c8862b9c400738e54251917728c53f81e95a3ead4a42fb` | `b0a8f07fb9f61e7541c8862b9c400738e54251917728c53f81e95a3ead4a42fb` | ✅ |
| A9_INVENTORY_ACCOUNTING_VALUATION_INTERFACE_EVIDENCE.md [CORR-005 edited] | `d64cab0f60aa490ce1ddda9b16e4cb9ab165796cb342be4f78866255098d0fc8` | `d64cab0f60aa490ce1ddda9b16e4cb9ab165796cb342be4f78866255098d0fc8` | ✅ |
| A10_SAAS_TENANT_COMPANY_WAREHOUSE_RISK_REGISTER.md [CORR-005 edited] | `682b51ce9c6734b365504b4a4cabb90554164db506474ec56cb7a4bc3c331ab1` | `682b51ce9c6734b365504b4a4cabb90554164db506474ec56cb7a4bc3c331ab1` | ✅ |
| A11_THAILAND_BUSINESS_REALITY_AND_REGULATORY_REGISTER.md | `600d447b3392de38fc6e829425d79a35118c7203bdd73c1ce04763ad1f7d5a1c` | `600d447b3392de38fc6e829425d79a35118c7203bdd73c1ce04763ad1f7d5a1c` | ✅ |
| A12_MIGRATION_PROVENANCE_AND_CONTINUITY_EVIDENCE.md [CORR-005 edited] | `052ddcb6bfb43c3e19d95949c2163228583cc9ed07d8fbd40c59c827a9b0cfd7` | `052ddcb6bfb43c3e19d95949c2163228583cc9ed07d8fbd40c59c827a9b0cfd7` | ✅ |
| A13_CROSS_DOMAIN_INVARIANT_CANDIDATE_REGISTER.md [CORR-005 edited] | `0d72f3425b83da5e2fc6296c087ecddd17a73d00ad318a2b709f40c829763eac` | `0d72f3425b83da5e2fc6296c087ecddd17a73d00ad318a2b709f40c829763eac` | ✅ |
| A14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md [CORR-005 edited] | `40eb675ce3077b8edfa50e27d81e16614dc7c84a1e936588920f9311c9b90e77` | `40eb675ce3077b8edfa50e27d81e16614dc7c84a1e936588920f9311c9b90e77` | ✅ |
| A15_MATERIAL_UNKNOWN_EXHAUSTION_REPORT.md [CORR-005 edited] | `7769c0845d954fa1e09335c58cd643ba786e59b539f9e7dabdbaaec61be49d60` | `7769c0845d954fa1e09335c58cd643ba786e59b539f9e7dabdbaaec61be49d60` | ✅ |
| A16_ACCOUNTING_X_INVENTORY_CROSS_PROOF_INPUT_PACK.md [CORR-005 edited] | `66872abba2fb1fe972ec9b4b12a879cf56330b6e4238a255b95a0da29110b0fb` | `66872abba2fb1fe972ec9b4b12a879cf56330b6e4238a255b95a0da29110b0fb` | ✅ |
| A17_CLEAN_ROOM_CLASSIFICATION_AND_QUARANTINE_REGISTER.md [CORR-005 edited] | `a2cc2c193439957ac4448cbc64f4a27f7dc9d4de021be3cca26f421da31a48cd` | `a2cc2c193439957ac4448cbc64f4a27f7dc9d4de021be3cca26f421da31a48cd` | ✅ |
| A18_TEAM_A_INVENTORY_DEEP_RESEARCH_FINAL_REPORT.md [CORR-005 edited] | `2becb2f69d79fb59de840a45bc3b3bb0de6e9b396de1df50e8f5c484cc3072d0` | `2becb2f69d79fb59de840a45bc3b3bb0de6e9b396de1df50e8f5c484cc3072d0` | ✅ |
| A19_INVENTORY_DEEP_RESEARCH_SHA256_MANIFEST.txt [CORR-005 addendum] | `80da943ca298d4da468e6bbb7daa8500c654c74efba3857bf0f1a94dcca5d000` | `80da943ca298d4da468e6bbb7daa8500c654c74efba3857bf0f1a94dcca5d000` | ✅ |
| A20_SESSION_CLOSURE_SMEPLUS-26-08-31-MIG-A-INV-BB-DR-002.md [CORR-005 addendum] | `b7957c853883b433b7f206777bdfe694444b9a6ed37f3de0583d584a4bc45026` | `b7957c853883b433b7f206777bdfe694444b9a6ed37f3de0583d584a4bc45026` | ✅ |

## Result — Section B (6/6 files, CORR-005 deliverables 01-06)

| File | Manifest-claimed SHA-256 | Independently computed SHA-256 | Match |
|---|---|---|---|
| 01_CORR005_PREFLIGHT_AND_BASELINE_VERIFICATION.md | `4c343ed0a979a3543cca521d3807aecf6d6089d74e4721ff53d1a26d74568cde` | `4c343ed0a979a3543cca521d3807aecf6d6089d74e4721ff53d1a26d74568cde` | ✅ |
| 02_CORR005_FIVE_HIGH_RECONCILIATION_MATRIX.md | `d585851d7f3968878f1c1af0c14a863a7ed5ef392eba82793006905a5990a0c9` | `d585851d7f3968878f1c1af0c14a863a7ed5ef392eba82793006905a5990a0c9` | ✅ |
| 03_CORR005_RESIDUAL_BLOCKER_AND_CARRY_FORWARD_REGISTER.md | `a50bf958cb0690fb303861e2509b6ca204367ca20ee62b3df9c19b5b570d6989` | `a50bf958cb0690fb303861e2509b6ca204367ca20ee62b3df9c19b5b570d6989` | ✅ |
| 04_CORR005_DR002_CROSS_FILE_CONSISTENCY_REPORT.md | `2041e3f2f95775d3243512054a346a8f7bc245895be4893e371510d8ac4cb436` | `2041e3f2f95775d3243512054a346a8f7bc245895be4893e371510d8ac4cb436` | ✅ |
| 05_CORR005_INDEPENDENT_DELTA_REVIEW_READINESS_REPORT.md | `4d2a119c22576b4fedde3d4eb4eb5f157aaabcc12d6f0f179d392cd8ff0ca1d1` | `4d2a119c22576b4fedde3d4eb4eb5f157aaabcc12d6f0f179d392cd8ff0ca1d1` | ✅ |
| 06_CORR005_SESSION_CLOSURE.md | `71805d6f533b0ce1a6b65666485232cc793be4d9ab8513807ab38f2aecf19ee7` | `71805d6f533b0ce1a6b65666485232cc793be4d9ab8513807ab38f2aecf19ee7` | ✅ |

## Missing / unexpected / duplicate paths

- **Missing:** 0 — every path listed in the manifest was found in the commit tree.
- **Unexpected:** 0 — `git ls-tree` of both target directories at this commit returned exactly 21 + 7 entries (the 7th being the manifest itself, correctly self-excluded from hashing).
- **Duplicate paths:** 0.
- **Hash mismatches: 0 of 27.**

## Verdict

**PACKAGE INTEGRITY INDEPENDENTLY REPRODUCED — VERIFIED, 27/27, ZERO DISCREPANCY.** This is a first-principles reproduction (hashes computed from blob content before any comparison was made), not a re-statement of IER-003's or CORR-005's own claim. The frozen CORR-005 evidence package has not been altered, truncated, or substituted since its commit.
