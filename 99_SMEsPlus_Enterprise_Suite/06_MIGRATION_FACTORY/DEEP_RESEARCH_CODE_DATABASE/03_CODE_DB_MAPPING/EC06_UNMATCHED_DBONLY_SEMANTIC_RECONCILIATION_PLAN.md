# EC-06 — Unmatched + DB-Only Semantic Reconciliation Plan

Session: `[SMEPLUS-26-08-28-DEEP-CD-001]`  
Date: 2026-08-29 Asia/Bangkok  
Status: `PREPARED ONLY / NOT SEQUENTIALLY ACTIVE — EC-03 AND EC-05 HOLD`

## Purpose

Prepare the deterministic classification method for unmatched source↔database records and DB-only facts so execution can begin immediately once the current mapping register is located and verified.

This document does not classify any current row without row-level evidence.

## Normalized Mapping Status Taxonomy

Every current mapping row must resolve to exactly one controlled status:

1. `VERIFIED_MATCH`
2. `EXPECTED_NON_STORED`
3. `RELATION_TABLE`
4. `GENERATED_DERIVED`
5. `SOURCE_ONLY`
6. `DB_ONLY`
7. `TABLE_NOT_FOUND`
8. `COLUMN_NOT_FOUND`
9. `AMBIGUOUS`
10. `NEEDS_BUSINESS_REVIEW`
11. `QUARANTINED`

## Deterministic Classification Rules

### VERIFIED_MATCH
Use only when the expected persistence fact is directly evidenced in the identified dump/schema and the source record is bound to the same source baseline used by the mapping artifact.

Required evidence:
- source item identity;
- table/column evidence;
- dump identity/hash;
- mapping row ID;
- verifier.

### EXPECTED_NON_STORED
Use when the field is demonstrably computed/transient/non-persistent by neutral evidence and no stored column is required for the business fact.

Do not classify from source-framework implementation details alone. The output must be expressed as vendor-neutral persistence semantics.

### RELATION_TABLE
Use where persistence is represented through a separately evidenced relationship structure rather than a scalar column on the expected entity.

### GENERATED_DERIVED
Use for values deterministically generated or derived from other stored business facts and not requiring independent migration as a primary fact.

### SOURCE_ONLY
Use where source metadata/capability exists but the identified database snapshot contains no corresponding persisted fact and the absence is explained by version/install/configuration evidence.

### DB_ONLY
Use where the identified dump contains a business-relevant table/column/fact with no mapped source-field counterpart in the current mapping set.

DB_ONLY records require reverse inventory and business-owner review before migration exclusion.

### TABLE_NOT_FOUND
Use only when the expected table is absent from the identified dump and the absence cannot yet be normalized to non-stored/relation/generated/version behavior.

### COLUMN_NOT_FOUND
Use only when the expected table exists but the expected column is absent and no stronger semantic explanation is evidenced.

### AMBIGUOUS
Use when two or more evidence-backed interpretations remain plausible.

### NEEDS_BUSINESS_REVIEW
Use when a technical mapping can be described but migration meaning, retention, transformation, or target canonical treatment requires a business/domain decision.

### QUARANTINED
Use when license/IP/security/classification controls prohibit semantic promotion or when CLASS-D/other restricted-source controls apply.

## Required Row-Level Evidence Fields

The EC-06 execution register must include at minimum:

- mapping_row_id
- source_module
- source_item/model/field neutral identifier
- source_evidence_id
- source_manifest_version/hash
- dump_hash
- table
- column
- original_mapping_status
- normalized_status
- business_fact_interpretation
- confidence
- evidence_location
- owner
- reviewer/verifier
- verification_timestamp
- exception_id
- migration_gate_impact

## Batch Strategy

When current mapping evidence becomes available, classify in controlled batches:

1. direct matches and deterministic non-stored/relation/generated records;
2. table-not-found and column-not-found records grouped by module/domain;
3. reverse DB-only inventory;
4. ambiguous/business-review records;
5. quarantine records;
6. sample verification per status/domain;
7. exception register reconciliation.

No percentage may be reported until the exact row denominator of the current mapping artifact is verified.

## Quality Controls

- no unmatched row is automatically a defect;
- no not-found row is automatically migration-excluded;
- no framework-specific table/class structure is adopted into target design;
- DB-only facts are never silently dropped;
- business semantics must be expressed independently of vendor implementation;
- CLASS-D/restricted source remains quarantined;
- every normalized row must retain its original evidence trace.

## Current Gate Position

`EC-06 = PREPARED ONLY`

Execution is blocked by:

- EC-03 current classification HOLD;
- EC-05 current mapping lineage HOLD.

The plan is ready for immediate controlled use once the current mapping register and classification gate evidence become inspectable.
