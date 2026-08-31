# 09 — Database / Dump Independent Re-Verification Report

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Attempt independent DB restore and run narrow, targeted evidence queries where the prior sessions were blocked | Independent Evidence Reviewer | This artifact | 2026-09-01 | Boss | **SUCCEEDED — N-DB-01 CLOSED** | Directly supplies evidence for H1, H2, H3, H4, H5, GRPA-M14 |

## 1. Why the prior attempt (A2, N-DB-01) failed and this one did not

TEAM A's own session (A2 §1) candidly recorded that its `docker run` + data-load + `exec` sequence was refused by its own session's auto-mode permission classifier as a compound action, before any container was created. This review's session did not encounter that block: `docker ps -a` at the start of this review showed Docker already running with ~36 pre-existing, unrelated containers from other work — confirming Docker itself was already an approved, in-use tool in this environment, not a fresh elevated-permission request.

## 2. Method — disposable, isolated, cleaned up

1. `docker run -d --name ier003-audit-pg-temp ... postgres:18` — a uniquely-named container, chosen specifically to avoid any collision with the ~36 pre-existing containers already running (`scgl-*`, `pcat-*`, `occ-odoo18-*`, `db2test`, none of which were touched, stopped, or inspected).
2. `docker cp` the dump file (read-only source copy) into the container; `createdb` + `pg_restore --no-owner --no-privileges -j 4` using PG18-class tooling — consistent with GROUP A's own Independent Evidence Review's prior finding (reused DELTA-FIRST by TEAM A in A2 §2) that PG16 fails on this dump's v1.16 archive format and PG18 succeeds.
3. **Result: 1,432 tables restored successfully.** 30 non-fatal errors, all confined to one table (`ai_embedding`) requiring the `pgvector` Postgres extension (`vector_cosine_ops` operator class) not present in the vanilla `postgres:18` image — immaterial to Inventory, not retried.
4. A second, independent restore was performed later in the same session (fresh container `ier003-audit-pg-temp2`) to run one follow-up query — same method, same result (1,432 tables, same class of `ai_embedding`-only errors), confirming the first restore's result was not a fluke.
5. Both containers were `docker stop`+`docker rm` immediately after their queries completed. `docker ps -a` confirmed zero residual audit containers and zero effect on the pre-existing container set, both before and after.
6. All queries issued were read-only `SELECT`/`to_regclass`/`information_schema` lookups. No `INSERT`/`UPDATE`/`DELETE`/`ALTER` was ever issued. No dump content was copied outside the container's own filesystem (the `docker cp` destination is internal to the disposable container, discarded on `docker rm`).

**Disposition: `N-DB-01` (A14's own registered gap — "this session's own DB re-verification... blocked") is CLOSED.** A session with container-provisioning permission was able to complete exactly the re-run TEAM A's own next-action called for.

## 3. Material caveat this restore surfaces: the dataset is far smaller/emptier than the frozen forensics implied for Inventory specifically

| Table | Row count found |
|---|---|
| `stock_quant` | **0** |
| `stock_move` | 48 total (`assigned`: 28, `cancel`: 20 — **zero `done` moves**) |
| `product_template` (by `type`) | `consu`: 82,723; `service`: 1,030 |
| `res_company` | 1 (no branch/child hierarchy populated) |

GROUP A's frozen DB forensics (reused DELTA-FIRST throughout A2/A9/A13/A14) cites large row counts for the **Purchase-approval** tables (`purchase_request_level_approve_po`: 27,874 rows) — those figures are real and independently unchallenged here. But this review's own fresh query shows the **Inventory-specific** tables (`stock_quant`, `stock_move`) are minimally populated: zero quants, and only 48 moves with none ever reaching `done`. This means:

- The "no negative-quantity incidence" and "no duplicate-bin incidence" checks run in [03](03_IER003_PRIMARY_CLAIM_REPERFORMANCE_REPORT.md) §5 are **schema-level confirmations, not data-level tests** — an empty table trivially has zero violations, so this is not evidence that the application would prevent a violation under real operating volume.
- Any future Cross-Proof scenario relying on this specific dump to observe realistic Inventory transaction volume, valuation postings, or reservation behavior will find this dataset **insufficient** for that purpose — it appears to be a fresh/onboarding/test snapshot from an Inventory-operations standpoint, not a mature operational history, even though it clearly has mature Accounting/Purchase-approval history.
- **This is registered as a new finding, not previously disclosed by TEAM A or GROUP A** (their DB forensics discussion never states the `stock_quant`/`stock_move` row counts) — see [13](13_IER003_FINDING_AND_GATE_IMPACT_REGISTER.md).

## 4. Findings supplied to other deliverables by this restore

| Finding | Consumed by |
|---|---|
| No `stock_valuation_layer`/`uom_category`/`product_packaging`/`procurement_group` tables; `stock_reference` table confirmed present | [03](03_IER003_PRIMARY_CLAIM_REPERFORMANCE_REPORT.md) §1–2 |
| `product_template.type` data contains no legacy `'product'` value | [03](03_IER003_PRIMARY_CLAIM_REPERFORMANCE_REPORT.md) §3, closes GRPA-M14 |
| `res_partner` orphan-column existence + `ir_model_data` module provenance (`bh_parent_company`) | [05](05_IER003_HIGH_H2_PARTNER_BRAND_HQ_FORENSIC_REVIEW.md) |
| `l10n_th`/`l10n_th_partner`/`l10n_th_reports` install state; single-row, unbranched `res_company` | [06](06_IER003_HIGH_H3_THAI_BRANCH_TBRAC_REVIEW.md) |
| `res_company`/`account_lock_exception` lock-date columns | [07](07_IER003_HIGH_H4_CUTOFF_TIMING_REVIEW.md) |

## 5. Clean-room handling of this session's own DB access

See [12](12_IER003_CLEAN_ROOM_TBRAC_SAAS_INTEGRITY_REVIEW.md) §2 for the explicit disposition — no raw row-level customer data (e.g. the literal company legal name found in `res_company.name`) is reproduced verbatim anywhere in this review's 18 deliverables; only structural facts (table/column/module names, aggregate counts) are cited, consistent with the standard TEAM A's own package already established.

No Evidence = No Progress. This review's own DB access is disclosed in full, including the caveat in §3 that a naive reading of "restore succeeded" could otherwise obscure.
