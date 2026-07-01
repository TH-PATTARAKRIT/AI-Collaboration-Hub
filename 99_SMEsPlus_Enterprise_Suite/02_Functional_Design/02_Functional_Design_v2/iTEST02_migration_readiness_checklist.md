# iTEST02 Migration Readiness Checklist

**Generated date:** 2026-07-02

## Readiness Status

Overall migration readiness is **not ready for execution** until restore validation, data masking, owner sign-off, and reconciliation criteria are completed.

## Checklist

| Area | Item | Status | Evidence required |
|---|---|---:|---|
| Source control | Dump stored in approved secure location | HOLD | Storage path and access log |
| Restore | Restore completed in isolated PostgreSQL environment | HOLD | Restore command and log |
| Restore | PostgreSQL version compatibility confirmed | HOLD | Version evidence |
| Restore | Extension compatibility confirmed | HOLD | `pg_trgm`, `vector`, `pg_stat_statements` validation |
| Data quality | Key table row counts captured | HOLD | Row count report |
| Data quality | Foreign key validation completed | HOLD | FK validation report |
| Privacy | Sensitive fields classified | PASS | `iTEST02_sensitive_columns_inventory.csv` |
| Privacy | Masking rules approved | HOLD | Approved masking specification |
| Privacy | Masked copy generated | HOLD | Masking job evidence |
| Functional design | Module inventory created | PASS | `iTEST02_module_inventory.csv` |
| Functional design | Module owners validate scope | HOLD | Owner sign-off |
| Reconciliation | Accounting reconciliation criteria defined | HOLD | Finance acceptance criteria |
| Reconciliation | Inventory reconciliation criteria defined | HOLD | Stock acceptance criteria |
| Reconciliation | HR data retention criteria defined | HOLD | HR acceptance criteria |
| Cutover | Rollback plan drafted | HOLD | Cutover and rollback document |
| Security | Tokens and credentials purged | HOLD | Security scan evidence |

## Minimum Go Criteria

The dump can move from HOLD to PASS only after restore evidence, masking evidence, row-count evidence, and owner sign-off are attached.
