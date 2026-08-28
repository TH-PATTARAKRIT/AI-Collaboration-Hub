# EC-05 — Current Code ↔ Database Mapping Lineage Review

Session: `[SMEPLUS-26-08-28-DEEP-CD-001]`  
Date: 2026-08-29 Asia/Bangkok  
Reviewer: ChatGPT L99 / Evidence Gate Review  
Status: `HOLD — CURRENT ROW-LEVEL MAPPING LINEAGE NOT YET INSPECTABLE`

## Objective

Determine whether the 27,682-row code↔database mapping can be certified as current against the canonical source identity and identified database dump.

## Evidence Available

Historical artifacts remain accessible:

- `Field_Level_Source_to_Dump_Mapping.csv`
- `Source_to_Dump_Mapping_Validation.csv`
- historical Phase B mapping total: 27,682 rows
- direct historical matches: 7,703

The historical field-level mapping schema contains:

`index, evidence, module, path, class, model, table, field, field_type, inherited_model, expected_db_column, mapping_status`

Observed historical statuses include:

- `MATCHED_COLUMN`
- `TABLE_NOT_FOUND_IN_DUMP`
- `NOT_FOUND_IN_DUMP`
- relation / non-stored review outcomes

## Current Working Distribution

The current research working baseline retains the following arithmetic:

| Working status | Count |
|---|---:|
| MATCHED_COLUMN | 7,703 |
| TABLE_NOT_FOUND_IN_DUMP | 8,924 |
| NOT_FOUND_IN_DUMP | 8,576 |
| NON_STORED_OR_RELATION_TABLE_REVIEW | 2,452 |
| NO_MODEL_TABLE_INFERRED | 27 |
| **Total** | **27,682** |

The arithmetic reconciles to 27,682, but arithmetic alone does not establish current lineage.

## Current-Lineage Problem

EC-01/EC-02 established that the current observed source is 1,504 modules, while 1,502 remains the last approved baseline and historical Phase B had 1,436 rows / 1,433 unique technical names.

EC-04 established the dump identity as:

- `iTEST02_2026-06-14_14-41-19.dump`
- SHA-256 `d67fff6dbd3a957a5089e3bd7f982b1f8a98b954e8be2e40e6c227a70339d8c0`

A current mapping gate requires a row-level mapping artifact whose provenance explicitly binds to:

1. the source manifest/version used;
2. the database dump hash/version used;
3. generation timestamp;
4. row-level status;
5. SHA-256 of the mapping artifact;
6. reviewer/verifier.

No such current mapping artifact has yet been located in the inspectable GitHub/File Library evidence reviewed in this closure sequence.

## Gate Test

| Test | Result |
|---|---|
| Historical 27,682-row mapping exists | PASS |
| Historical mapping rows inspectable | PASS |
| Current distribution arithmetic reconciles | PASS |
| Current mapping file SHA-256 | HOLD / NOT FOUND |
| Current mapping generation timestamp | HOLD / NOT FOUND |
| Explicit binding to current 1,504 observed source or approved 1,502 source manifest | HOLD |
| Explicit binding to dump SHA-256 `d67fff6d…39d8c0` | HOLD |
| Row-level normalized current status register | HOLD |

## Gate Result

`EC-05 = HOLD`

`DR-GAP-008 = OPEN`

Historical mapping evidence remains valid as historical forensic evidence, but it cannot be promoted to current certification solely because the row count remains 27,682.

## Next Control

Do not represent EC-06 as sequentially active until EC-05 current mapping lineage is inspectable.

Permitted preparation while HOLD:

- retain normalized status taxonomy;
- identify exact missing mapping evidence fields;
- locate the current mapping register from existing Team A / Mapping evidence stores;
- prepare a rebind/reconciliation procedure without changing source or database.

No source code reuse, target schema freeze, migration implementation, merge, release, or deployment is authorized.
