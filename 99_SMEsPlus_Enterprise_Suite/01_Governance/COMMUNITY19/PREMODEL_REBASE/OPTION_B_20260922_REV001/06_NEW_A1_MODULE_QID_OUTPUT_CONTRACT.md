# Corrected A1 Contract — MODULE + QID

## Input identity

For module `base`, A1 must use exactly:

- W1-STD freeze and Standard 55 bank pinned in `05_FROZEN_QUESTION_MODEL_BINDINGS.json`;
- W1-B01 freeze and the 50-question base bank pinned in the same file;
- isolated V1.00-admitted LGPL-3 source only;
- a fresh context and new output lineage;
- no old S1/S2 answer carry-forward.

## Exact answer universe

A1 must produce exactly one row for each frozen `MODULE + QID` pair:

- `base + STD-Q01..STD-Q55` = 55 rows;
- `base + G01-BASE-Q001..G01-BASE-Q050` = 50 rows;
- exact total = 105 Research Evidence rows.

This is not a Canonical Function-ID denominator and is not Formal Coverage.

## Mandatory answer fields

`MODULE`, `QID`, `QUESTION_TYPE`, `QUESTION_BANK_FILE`, `QUESTION_BANK_SHA256`, `FREEZE_ID`, `FREEZE_HASH`, `LAYER`, `ANSWER_STATUS`, `ANSWER_TEXT`, `DISCONFIRMING_RESULT`, `EVIDENCE_IDS`, `SOURCE_UNIT_IDS`, `SOURCE_PROOF`, `CONFIGURATION_PROOF`, `RUNTIME_PROOF`, `CROSS_MODULE_PROOF`, `E2E_PROOF`, `APPLICABILITY_REASON`, `FUNCTION_CANDIDATE_IDS`, `RULE_IDS`, `SCENARIO_IDS`, `GAP_IDS`, `CRQ_IDS`, `WORKER_CONTEXT_ID`, `ATTEMPT`, `ANSWERED_AT`.

Allowed `ANSWER_STATUS`: `ANSWERED`, `NOT_APPLICABLE`, `NOT_OBSERVED`, `NOT_FOUND_IN_SOURCE`.

## Required package

- `00_README.md`
- `01_ANSWER_REGISTER.tsv` — exactly 105 unique MODULE+QID rows
- `02_EVIDENCE_INDEX.tsv`
- `03_GAP_REGISTER.tsv`
- `04_CRQ_REGISTER.tsv`
- `05_FUNCTION_CANDIDATE_REGISTER.tsv`
- `06_RULE_REGISTER.tsv`
- `07_SCENARIO_REGISTER.tsv`
- `08_SELF_CHECK.json`
- `MANIFEST_SHA256.txt` written last

Every QID must be answered from fresh study. Prior pre-model findings may not be used as answer evidence.
