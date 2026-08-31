# A2 — Database / Dump Forensic Register

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Reconcile schema/data/dump evidence for Inventory facts that source reading alone cannot settle | Claude (Team A, DR-002) | This artifact | 2026-08-31 | Independent Evidence Review (pending) | **PARTIAL — DELTA-FIRST REUSE OF GROUP A FORENSICS; THIS SESSION'S OWN RE-RESTORE ATTEMPT BLOCKED BY SANDBOX CONTROL** | Does not block the overall package — see disposition below |

## 1. This session's own restore attempt — honest record

- Dump: `iTEST02_2026-06-14_14-41-19.dump`, 65,444,053 bytes, PostgreSQL custom-format archive, `pg_dump` archive version 1.16.
- Local `pg_restore`/`psql`/`pg_dump` available: version 16.15 (Homebrew). `pg_restore --list` against the raw dump failed: `unsupported version (1.16) in file header` — the archive format requires PostgreSQL 18-class client tooling.
- A `postgres:17` Docker image was pulled successfully (network access confirmed), and `pg_restore --list` was re-attempted via that image against the dump through a bind-mounted volume — the bind mount did not expose the host file inside the container in this sandbox (confirmed with a trivial known-good `/tmp` bind-mount test, which also failed to expose files), ruling out a path-specific issue.
- A `docker cp`-based approach (start a disposable named Postgres container, copy the dump in via the Docker API rather than a bind mount, then run `pg_restore` inside the container) was attempted next. This command was **blocked by this session's own auto-mode permission classifier** before execution (reason given: a compound action starting a background service + loading data + executing commands inside it). No container was created; `docker ps -a` confirms a clean state. Per this session's own safety instructions, this was not circumvented — the attempt was stopped and is recorded honestly here rather than forced through or faked.
- Temporary copies of the dump made during the bind-mount troubleshooting (`/tmp/iTEST02.dump`, a scratchpad copy) were deleted immediately after the attempt was abandoned. No dump content was committed, transmitted, or retained outside the authorized local source path.

**Disposition for this session's own attempt:** `EVIDENCE_MISSING — DB RESTORE BLOCKED BY SANDBOX CONTROL, NOT BY SOURCE INACCESSIBILITY`. This is explicitly distinct from the dump being inaccessible or corrupt — the dump is present, correctly sized, and its archive format was successfully identified (`pg_restore` produced a clear version-mismatch diagnostic, not a read error). A session with container-provisioning permission enabled could complete this restore.

## 2. DELTA-FIRST reuse — GROUP A's own frozen DB forensics (commit `8b0993d824cf726fa52edd687272ff54b0977c42`, independently re-verified at `626873c3b924a0350dfd75cf52d276eff6414dd2`)

Per DR-002 §5.2 ("Use as verification evidence, not as a replacement for primary re-performance") and the Amendment's DELTA-FIRST principle, this pass reuses GROUP A's already-independently-verified restoration rather than re-deriving it, since this session's own re-performance was blocked for an environmental reason unrelated to evidence quality:

- GROUP A's corrective session (CORR-003) restored the **full** dump (schema + data) into a scratch local PostgreSQL instance (not persisted) and ran row-level SQL queries directly against it.
- GROUP A's own methodology note claimed PostgreSQL 16 tooling; the **Independent Evidence Review independently attempted its own fresh restore** and found PG16 fails with a hard archive-version-incompatibility error identical in kind to what this session observed — confirming this is a real, reproducible property of the dump file itself, not an error specific to any one session's environment. The Independent Review resolved this using PG18-class tooling, and **independently reproduced every one of GROUP A's quantitative row-count/percentage claims exactly**. Verdict: `IR-1 — PostgreSQL tooling-version documentation inaccuracy — CONTROLLED CARRY-FORWARD, NOT GATE BLOCKING`; GROUP A's underlying DB findings are corroborated, not merely self-reported.
- This independently-corroborated chain (GROUP A restore → Independent Review re-restore on correct tooling → exact reproduction) is treated by this DR-002 pass as **VERIFIED WITH CONDITIONS** primary evidence, per DR-002 §10's Fact Status vocabulary — "conditions" being: (a) it reflects one specific customer's `iTEST02` dataset, not Thailand-wide practice (see A11); (b) it was captured 2026-06-14, a single point in time, not a longitudinal sample.

### Reused DB forensic findings material to Inventory (from GROUP A §04 / §08 / §14, cited by their original IDs)

| Finding | Evidence Character | Fact Status | Inventory relevance |
|---|---|---|---|
| `stock_move` carries `account_move_id, sale_line_id, purchase_line_id, weight, production_id, workorder_id, bom_line_id, repair_id` — none declared in `stock/models/stock_move.py` itself | Database direct (schema) | VERIFIED | Confirms the "wide shared table" pattern this pass's own source reading also observed (A3–A4): cross-domain link fields are injected by extending modules, not owned by core `stock` |
| `stock_move_line.move_id` FK is `ON DELETE SET NULL` (more permissive than the ORM's own cascade expectations) | Database direct (schema) | VERIFIED | Migration-invalid-state risk: a DB-level operation could orphan a move line without the ORM's `ondelete` semantics ever running — relevant to A12 |
| No unique/composite DB index enforces one-row-per-`(product, location, lot, package, owner)`-bin uniqueness on `stock_quant` | Database direct (schema) | VERIFIED | Confirms NEG-05/QNT findings from source reading (A3): reconciliation is application-layer (`_merge_quants()`), not DB-enforced — a genuine invariant gap, see A13 |
| Three approval modules' live usage: `sale_order_level_approve` (n=2, too small to characterize), `purchase_request_level_approve_po` (98.5% of 27,874 rows have `level1_user_id` set; undocumented `to_check_level` state on 131 rows), `purchase_request_level_approve` (1,945 approved / 96 rejected / 104 approved_level1 of 2,199 rows) | Database direct (row-level) + runtime historical data | VERIFIED (usage pattern); internal logic EVIDENCE_MISSING (source absent) | Not Inventory-owned directly, but gates whether a Purchase commitment becomes a physical receipt expectation in this customer's build — registered in A10/A14 |
| Reject-table pair (`purchase_order_level_reject`/`purchase_request_level_reject`) exists in schema but has **zero rows** | Database direct | VERIFIED (negative finding) | Schema presence without usage — a real-world signal that a designed control path may be dormant; relevant to A13 invariant candidates (do not assume schema presence implies active enforcement) |
| No DB CHECK constraint anywhere in the Inventory/Movement layer preventing negative `stock_quant.quantity`/`reserved_quantity`, or preventing delivered/received qty from exceeding ordered/demanded qty | Database direct (schema, negative finding) | VERIFIED | Directly material to A13 cross-domain invariants — over/under-fulfillment and negative-stock guards are 100% application-layer |

### Not re-derived by this pass

Full per-table Clean/Wide/Orphaned/Conflict classification (GROUP A §08 `08_SOURCE_DATABASE_SEMANTIC_TRACEABILITY_MATRIX.md`) is reused by reference, not reproduced here — see A14 for the carried-forward Unknown/Conflict items still open (`res.partner` brand/HQ orphan columns; `account.fiscal.position` base model unlocated).

## 3. Residual gap this pass leaves genuinely open

This session did **not** independently re-run new SQL queries of its own against the raw dump (blocked, §1). Any Inventory-specific question that GROUP A's combined Sales+Inventory+Purchase forensics pass did not already ask (e.g., an Inventory-only row-level query this DR-002's deeper scope might otherwise have wanted — such as historical `stock_move.state` distribution, or `stock.quant` negative-quantity incidence in this dataset) remains **`EVIDENCE_MISSING — REQUIRES SESSION WITH CONTAINER/DB PROVISIONING PERMISSION`**. This is registered as N-DB-01 in `A14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md` and does not silently disappear.

No Evidence = No Progress. DELTA-FIRST.
