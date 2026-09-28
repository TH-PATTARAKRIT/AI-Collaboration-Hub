# EC-05 — Controlled Current Mapping Rebind Procedure

Session: `[SMEPLUS-26-08-28-DEEP-CD-001]`  
Date: 2026-08-29 Asia/Bangkok  
Jira: `ERPPLUS-101`  
Owner Role: Mapping Lead / Evidence Reconciliation Executor  
Reviewer: ChatGPT Evidence Gate Review  
Status: `PROCEDURE AUTHORIZED / EC-05 REMAINS HOLD`

## 1. Purpose

Create an inspectable current-lineage mapping artifact only if an already-existing qualifying current mapping register cannot be recovered.

This procedure does not authorize changing source code, restoring or mutating the database, designing the target physical schema, or implementing migration code.

## 2. Fixed Evidence Anchors

### Source anchors

```text
Historical Phase B inventory: 1,436 rows / 1,433 unique technical names
Approved STEP040301 baseline: 1,502 modules
Current observed source: 1,504 modules
```

The two additional current modules are:

- `ks_dashboard_ninja`
- `ks_dn_advance`

They are not silently promoted into any historical mapping result.

### Database anchor

```text
Artifact: iTEST02_2026-06-14_14-41-19.dump
SHA-256: d67fff6dbd3a957a5089e3bd7f982b1f8a98b954e8be2e40e6c227a70339d8c0
Size: 65,444,053 bytes
Format: PostgreSQL custom-format archive
```

### Historical mapping anchor

```text
Historical rows: 27,682
Historical direct matches: 7,703
```

Historical row count and status are inputs to revalidation, not current proof.

## 3. Required Output Package

The rebind path must create a new immutable package containing at minimum:

1. `CURRENT_CODE_DB_MAPPING_REGISTER.csv`
2. `CURRENT_CODE_DB_MAPPING_LINEAGE.md`
3. `CURRENT_MAPPING_STATUS_RECONCILIATION.csv`
4. `CURRENT_MAPPING_EXCEPTION_REGISTER.csv`
5. `CURRENT_MAPPING_SHA256_MANIFEST.txt`
6. `CURRENT_MAPPING_INDEPENDENT_REVIEW.md`

No existing historical artifact is overwritten.

## 4. Mandatory Register Fields

Every row in `CURRENT_CODE_DB_MAPPING_REGISTER.csv` must contain at least:

```text
mapping_row_id
historical_row_id
source_module
source_artifact
source_path
source_manifest_version
source_manifest_sha256_or_evidence_id
source_model_or_neutral_fact
database_artifact
database_sha256
database_table
database_column
historical_status
current_status
revalidation_method
revalidation_evidence
confidence
review_required
owner
artifact_timestamp
reviewer
verification_status
gate_impact
notes
```

If a field cannot be evidenced, populate an explicit controlled state such as `UNKNOWN`, `NOT_EVIDENCED`, or `NEEDS_REVIEW`; do not invent values.

## 5. Current Status Taxonomy

Allowed normalized outcomes:

- `VERIFIED_MATCH`
- `EXPECTED_NON_STORED`
- `RELATION_TABLE`
- `GENERATED_DERIVED`
- `SOURCE_ONLY`
- `DB_ONLY`
- `TABLE_NOT_FOUND`
- `COLUMN_NOT_FOUND`
- `AMBIGUOUS`
- `NEEDS_BUSINESS_REVIEW`
- `QUARANTINED`

Historical labels may be retained in a separate `historical_status` field but may not be treated as current labels without revalidation.

## 6. Revalidation Rules

### R1 — Direct historical match

A historical `MATCHED_COLUMN` can become `VERIFIED_MATCH` only when the current source fact and selected dump object are both still evidenced under the fixed anchors.

If current source identity changed or cannot be tied to the historical row, use `AMBIGUOUS` or `NEEDS_BUSINESS_REVIEW`.

### R2 — Non-stored/computed/relation behavior

Do not classify from naming alone. The row may become `EXPECTED_NON_STORED`, `RELATION_TABLE`, or `GENERATED_DERIVED` only when inspectable metadata/authorized neutral evidence supports that interpretation.

### R3 — Table / column not found

A historical not-found status remains a current not-found status only after checking the selected dump inventory under the fixed dump hash. Otherwise it remains `AMBIGUOUS`.

### R4 — New current modules

Rows/facts for `ks_dashboard_ninja` and `ks_dn_advance` must be separately identified. Their OPL-1 treatment remains metadata/black-box only until global classification governance permits more. No source-body translation is allowed.

### R5 — CLASS-D

Any CLASS-D-linked source fact remains `QUARANTINED` unless explicit Boss/legal governance changes the treatment. No source-body revalidation is authorized.

### R6 — DB-only objects

Database objects with no safely evidenced source mapping must be registered as `DB_ONLY` or `NEEDS_BUSINESS_REVIEW`; they may not be forced into a source module to make totals reconcile.

## 7. Arithmetic Reconciliation

The procedure must publish:

```text
historical_row_count
current_row_count
carried_forward_rows
revalidated_rows
new_rows
retired_or_superseded_rows
ambiguous_rows
quarantined_rows
```

If current row count is not exactly 27,682, the delta must be explicitly explained with row IDs and evidence. A mismatch is not automatically a failure; an unexplained mismatch is HOLD.

## 8. Integrity Requirements

Before independent review, produce SHA-256 for every output artifact and an overall manifest. The lineage document must state:

- exact source evidence anchor;
- exact dump SHA-256;
- generation timestamp;
- tool/method used;
- row count;
- taxonomy version;
- owner;
- reviewer;
- known limitations.

## 9. Independent Gate Tests

EC-05 may move from HOLD only if all are true:

1. package exists and is accessible;
2. package SHA-256 manifest verifies;
3. source anchor is explicit;
4. dump anchor is explicit;
5. every row has a current controlled status;
6. unknown/ambiguous/quarantined rows are not hidden;
7. arithmetic reconciles;
8. independent reviewer verifies lineage;
9. evidence timestamp, owner and gate impact are present.

## 10. Sequential Boundary

A successful EC-05 technical review still does not bypass global EC-03. EC-06 may use only independently verified EC-05 outputs and remains globally non-sequential until EC-03 is resolved.

`No Evidence = No Progress.`  
`Never Skip Gate.`