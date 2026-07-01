# iTEST02 Restore Validation Plan

**Generated date:** 2026-07-02

## Objective

Validate that the iTEST02 PostgreSQL custom dump can be restored safely and consistently in an isolated environment without exposing sensitive production-like data.

## Environment Requirements

- Isolated network segment
- No public internet exposure
- Dedicated PostgreSQL instance
- Restricted administrator access
- Audit logging enabled
- No external AI, vendor, or developer access before masking

## Restore Validation Steps

1. Record dump checksum.
2. Confirm PostgreSQL major version and extension availability.
3. Create empty restore database.
4. Restore dump using a controlled service account.
5. Capture complete restore log.
6. Validate schema object counts.
7. Validate extension installation.
8. Capture row counts for critical tables.
9. Run foreign-key integrity checks.
10. Execute masking or redaction jobs.
11. Re-run sensitive-data checks after masking.
12. Obtain owner sign-off.

## Evidence to Store

| Evidence | File example |
|---|---|
| Dump checksum | `evidence_dump_checksum.txt` |
| Restore command | `evidence_restore_command.txt` |
| Restore log | `evidence_restore_log.txt` |
| Extension validation | `evidence_extensions.txt` |
| Object count report | `evidence_object_counts.csv` |
| Row count report | `evidence_row_counts.csv` |
| Masking job result | `evidence_masking_result.md` |
| Owner approval | `evidence_owner_signoff.md` |

## Validation SQL Examples

```sql
SELECT extname FROM pg_extension ORDER BY extname;

SELECT schemaname, tablename
FROM pg_tables
WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY schemaname, tablename;

SELECT conname, conrelid::regclass AS source_table, confrelid::regclass AS target_table
FROM pg_constraint
WHERE contype = 'f'
ORDER BY source_table, conname;
```

## Decision Rule

No migration rehearsal or external sharing should proceed unless all evidence items are attached and reviewed.
