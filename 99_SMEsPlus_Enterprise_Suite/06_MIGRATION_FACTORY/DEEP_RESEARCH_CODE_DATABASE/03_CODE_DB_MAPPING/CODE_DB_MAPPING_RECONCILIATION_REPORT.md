# Code ↔ Database Mapping Reconciliation Report

Session: `[SMEPLUS-26-08-28-DEEP-CD-001]`  
Status: `HOLD / CURRENT RECONCILIATION INCOMPLETE`  
Prepared Role: Enterprise Functional Architect & Clean-Room Systems Analyst

## 1. Mapping Purpose

The mapping links a source observation to a persisted business fact. It is not a target-schema design.

```text
Source artifact
-> source model/field observation
-> persistence expectation
-> observed table/column or relation
-> business meaning
-> evidence status
```

## 2. Historical Verified Mapping Baseline

The historical package contains 27,682 field-level mapping records. The historical evidence gate confirms 7,703 direct source-field to dump-column matches and classifies the rest for further review.

The historical v1.4 report explicitly rated:

- Model-to-table mapping: `PASS_WITH_GAPS`
- Field-to-column mapping: `PASS_WITH_GAPS`
- Full 100% certification: `HOLD`

The subsequent v1.5 closure report closed the package as a usable Phase B baseline for the artifacts then available. It did not prove that every unresolved field represented a defect-free, fully reconciled current system.

## 3. Current Working Mapping Distribution

The current Session provides this working distribution:

| Working Status | Count | Current Treatment |
|---|---:|---|
| MATCHED_COLUMN | 7,703 | Candidate `VERIFIED_MATCH`, subject to current artifact identity |
| TABLE_NOT_FOUND_IN_DUMP | 8,924 | Do not classify as defect; inspect transient models, uninstalled modules, version drift, and absent tables |
| NOT_FOUND_IN_DUMP | 8,576 | Inspect computed/non-stored/version/custom behavior before deciding |
| NON_STORED_OR_RELATION_TABLE_REVIEW | 2,452 | Candidate `EXPECTED_NON_STORED` or `RELATION_TABLE` |
| NO_MODEL_TABLE_INFERRED | 27 | Candidate `AMBIGUOUS` or `NEEDS_BUSINESS_REVIEW` |
| **Total** | **27,682** | Arithmetic reconciles |

The total is internally consistent. The distribution remains a Boss-provided current working claim until the current register file, timestamp, lineage, and SHA-256 are inspectable.

## 4. Normalized Clean-Room Mapping Statuses

| Normalized Status | Definition | Legacy Status Candidates |
|---|---|---|
| VERIFIED_MATCH | Current source expectation and current persisted column/relationship are directly evidenced | MATCHED_COLUMN |
| EXPECTED_NON_STORED | Business value is computed, contextual, transient, or intentionally not persisted | NON_STORED_OR_RELATION_TABLE_REVIEW, NOT_FOUND_IN_DUMP |
| RELATION_TABLE | N:M or association persistence exists outside the inferred model table | NON_STORED_OR_RELATION_TABLE_REVIEW |
| GENERATED_DERIVED | Value is generated from other facts or an external process | NOT_FOUND_IN_DUMP |
| SOURCE_ONLY | Source capability exists but is absent from the examined database version or installation | TABLE_NOT_FOUND_IN_DUMP, NOT_FOUND_IN_DUMP |
| DB_ONLY | Persisted business fact exists without a current source-field observation | Requires reverse inventory from dump |
| TABLE_NOT_FOUND | Expected persistent entity table is absent | TABLE_NOT_FOUND_IN_DUMP after verification |
| COLUMN_NOT_FOUND | Expected stored field column is absent from an evidenced current table | NOT_FOUND_IN_DUMP after verification |
| AMBIGUOUS | Evidence permits multiple interpretations | NO_MODEL_TABLE_INFERRED |
| NEEDS_BUSINESS_REVIEW | Technical mapping exists but migration/business meaning is unresolved | Any status |
| QUARANTINED | Source or evidence is restricted by CLASS-D, license, security, or legal control | Any status |

## 5. Why Unmatched Records Are Not Automatically Defects

An unmatched source observation may represent:

- a computed or derived field
- a relation stored in an association table
- a transient/wizard entity
- an inherited field stored in another table
- an uninstalled module
- a module version newer than the dump
- a database customization not present in the source archive
- a property/configuration value stored through a generic mechanism
- a binary/attachment reference stored indirectly
- a field removed or renamed between versions
- an extraction limitation

Therefore, `TABLE_NOT_FOUND` and `COLUMN_NOT_FOUND` require evidence-based classification before defect, migration, or target-design decisions.

## 6. Mapping Reconciliation Rules

Every current mapping row must include:

- research item ID
- source archive and source path
- source version/timestamp/hash
- source model and field
- persistence expectation
- current dump identity/hash
- observed table/column/relation
- normalized mapping status
- business interpretation
- confidence
- reviewer and verification status
- clean-room classification
- gate impact

No bulk status conversion is authorized without row-level or rule-based evidence.

## 7. Mapping Findings from Available Samples

Available samples demonstrate all major ambiguity classes:

- directly matched scalar and foreign-key columns
- one-to-many and many-to-many fields requiring relation/non-stored review
- transient/wizard tables absent from the dump
- computed/display/example fields absent from the dump
- configuration fields present in source but absent from the examined database
- intercompany controls with some company-level fields matched and settings-layer fields absent

This supports the normalized status model above. It does not certify the current 27,682 rows.

## 8. Reconciliation Verdict

| Control | Result |
|---|---|
| Historical mapping register accessible | PASS |
| Historical total 27,682 | PASS |
| Historical direct matches 7,703 | PASS |
| Working distribution arithmetic | PASS |
| Current register identity and SHA-256 | HOLD |
| Historical-to-current row lineage | HOLD |
| Current source/dump version binding | HOLD |
| Unmatched-row semantic classification | HOLD |
| CLASS-D mapping quarantine | PASS |

## 9. Gate Impact

`DR4 CODE ↔ DATABASE MAPPING = HOLD`

The mapping evidence is adequate to design a controlled reconciliation method and to identify candidate migration facts. It is not adequate to certify current all-row mapping, current version alignment, or a production migration mapping.
