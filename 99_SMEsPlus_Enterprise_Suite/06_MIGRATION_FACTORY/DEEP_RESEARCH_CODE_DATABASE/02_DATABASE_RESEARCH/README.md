# 02 — Database Research

Purpose: study the database/dump independently from source-code assumptions and identify business facts that exist in persisted data.

## Required Research Coverage

- Schemas, tables, columns, data types, nullability
- Primary keys, foreign keys, unique constraints, and indexes
- Relation tables and reference/master tables
- Transaction, configuration, audit/history, and attachment-reference structures
- Company, tenant, branch, currency, localization, and sequence-related fields
- Accounting, inventory, manufacturing, sales, purchasing, partner, tax, and integration structures
- Orphan relationships, unusual/custom tables, custom fields, and anomalies

## Governing Question

```text
WHAT BUSINESS FACT EXISTS?
```

The following question is out of scope for this workstream:

```text
HOW SHOULD SMEsPlus COPY THIS DATABASE?
```

No table or column is automatically accepted as a canonical SMEsPlus entity or field. Every finding must be interpreted independently and classified before entering target design.

All detailed observations must be registered in `99_EVIDENCE_REGISTER/DATABASE_DEEP_RESEARCH_REGISTER.csv`.
