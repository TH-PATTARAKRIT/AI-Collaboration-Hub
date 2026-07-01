# iTEST02 Restore Rehearsal Runbook

## Objective
Validate that the iTEST02 PostgreSQL custom dump can be restored repeatably in an isolated environment.

## Pre-Checks
1. Confirm restore environment is isolated.
2. Confirm no production credentials are reused.
3. Confirm required PostgreSQL extensions are available.
4. Confirm dump checksum is recorded.
5. Confirm DBA and Security owner are assigned.

## Execution
1. Create target database.
2. Install required extensions.
3. Restore custom dump.
4. Capture restore log.
5. Reconcile object counts.
6. Validate application-level smoke checks if Odoo runtime is available.
7. Record evidence.

## Exit Criteria
- Restore completes without critical errors.
- Object counts reconcile or differences are explained.
- Extensions are confirmed.
- No unmasked dataset is shared outside approved environment.
