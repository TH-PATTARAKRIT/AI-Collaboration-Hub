# Database Forensic Research Report

Session: `[SMEPLUS-26-08-28-DEEP-CD-001]`  
Status: `REVIEWED WITH LIMITATION / CURRENT DATABASE BASELINE HOLD`  
Prepared Role: Enterprise Functional Architect & Clean-Room Systems Analyst  
Final Approver: Boss

## 1. Objective

Identify persisted business facts and relationships from the database evidence without treating the legacy schema as a target design.

The database answers:

```text
What business fact was stored?
What identity, amount, quantity, status, relationship, or audit fact existed?
```

It does not answer:

```text
What tables should SMEsPlus copy?
```

## 2. Verified Historical Database Evidence

The inspectable historical package records:

| Evidence Area | Count | Primary Artifact |
|---|---:|---|
| Tables | 1,395 | `Dump_Table_Inventory.csv` |
| Columns | 13,940 | `Dump_Column_Inventory.csv` |
| Constraints | 6,682 | `Dump_Constraint_Inventory.csv` |
| Foreign-key edges | 5,141 | `Foreign_Key_Relationship_Edges.csv` |
| Indexes | 1,714 | `Dump_Index_Inventory.csv` |
| Field-level source mappings | 27,682 | `Field_Level_Source_to_Dump_Mapping.csv` |

The table and column inventories were extracted from a PostgreSQL custom dump. The evidence gate records the table and column discoveries as PASS.

## 3. Extraction Limitation

The constraint, foreign-key, and index inventory was produced using dump-string fallback. Historical reviewers explicitly stated that `schema.sql`, `pg_restore` output, live metadata, or a restored database would provide stronger evidence.

Therefore:

- presence of the inventory is verified;
- the count is usable as a historical evidence baseline;
- schema-level completeness and exact DDL semantics are not certified;
- no target schema may be derived directly from these artifacts.

## 4. Current Database Baseline Reconciliation

The current Session states approximately 13,942 columns, compared with the historical verified count of 13,940.

```text
13,942 current working observations
- 13,940 historical verified columns
= 2 columns requiring explicit lineage
```

The two-column delta has not been tied to an inspectable current dump identity, timestamp, schema export, migration record, or SHA-256 manifest. It remains `WORKING CLAIM / NOT VERIFIED`.

The current Session repeats the historical counts for tables, constraints, foreign keys, and indexes. Matching counts alone do not prove that the database version or contents are the same.

## 5. Business-Fact Classification

The database inventory is to be interpreted through vendor-neutral fact classes:

| Fact Class | Examples of Meaning | Clean-Room Treatment |
|---|---|---|
| Identity | tenant, company, party, product, document, account, warehouse | Preserve business identity and migration key semantics, not legacy IDs as architecture |
| Master Data | account, tax, unit, category, route, bill of material | Extract controlled business attributes and effective dates |
| Transaction | journal, invoice, payment, order, movement, production | Preserve legally and operationally relevant facts and lifecycle history |
| Relationship | source document, settlement, allocation, ownership, hierarchy | Reconstruct semantic links independently |
| Quantity | ordered, reserved, moved, consumed, produced, scrapped | Preserve units, precision, direction, and effective timestamps |
| Monetary | debit, credit, tax, cost, valuation, currency amount | Preserve currency, rate basis, rounding, and accounting date |
| Configuration | sequence, policy, account mapping, approval setup | Treat as migration facts only when authorized and still valid |
| Audit | created, changed, approved, posted, reversed | Preserve actor, time, reason, and immutable evidence where required |
| Attachment | document evidence and references | Preserve ownership, hash, type, retention, and access policy |

## 6. Conceptual Persistence Rules

Independent target design should enforce these persistence principles:

1. Every transactional aggregate carries `tenant_id`, `company_id`, and an immutable aggregate identifier.
2. Posted accounting facts are append-only; correction occurs through reversal or adjustment.
3. Inventory quantity events are immutable after completion; corrections create counter-events.
4. Monetary facts store transaction currency, functional currency, rate, rate date, and rounding basis.
5. State transitions write audit and domain-event records atomically.
6. Cross-domain references use stable business identifiers and explicit source-document links.
7. Attachments are content-addressed by cryptographic hash and linked through evidence metadata.
8. Soft deletion is not permitted for statutory or posted records.
9. Optimistic concurrency is required for mutable drafts.
10. Tenant isolation must be enforceable at query and authorization layers.

## 7. Data Anomaly and Integrity Review Position

The available evidence proves structural inventories, but does not provide inspectable results for all of the following:

- orphan row counts by foreign-key relationship
- invalid company/tenant ownership
- duplicate business keys
- cross-company reference violations
- currency-rate completeness
- quantity/value imbalance
- unbalanced journal entries
- invalid posted-document mutation
- attachment integrity
- sequence gaps and duplicate numbering
- inactive master data referenced by active transactions

These are required future validation queries, not assumed defects.

## 8. Database Research Verdict

| Control | Result |
|---|---|
| Historical table inventory | PASS |
| Historical column inventory | PASS |
| Constraint/FK/index inventory existence | PASS WITH LIMITATION |
| Current dump identity and SHA-256 | HOLD |
| Current 13,942-column baseline | HOLD |
| Two-column delta lineage | HOLD |
| Orphan/anomaly validation | HOLD |
| Vendor-neutral business-fact model | PASS WITH CONTROL |

## 9. Gate Impact

`DR3 DATABASE DEEP RESEARCH = HOLD FOR CURRENT BASELINE CERTIFICATION`

The historical database package is sufficient for controlled structural learning and migration-fact planning. It is not sufficient to certify current schema identity, current data integrity, or a production target schema.
