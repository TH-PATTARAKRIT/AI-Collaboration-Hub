# 60 — P05 DUMP READ-ONLY EVIDENCE BOUNDARY

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E22`

## 1. The Question

Round 2 recorded `HOLD — READ-ONLY RESTORE AUTHORIZATION REQUIRED` and named a restore as a cheap
unblocker. The directive is explicit that **restoring a dump is an environment/write action** and must
not be performed without existing authority, and that Boss must not be interrupted to request it.

## 2. Alternatives Exhausted — and the HOLD is no longer needed

| Route | Attempted | Result |
|---|---|---|
| Archive TOC inspection (`pg_restore -l`) | yes | database identity, table inventory, object list |
| Schema extraction (`pg_restore -s`, **unfiltered**) | yes | full constraints, indexes, FK delete actions |
| Data extraction (`pg_restore --data-only --table=X -f`) | yes | **complete table contents, file-to-file** |
| Newer client for v1.16 archives | yes | PG 18 client reads them |
| Plain-SQL archive | located (`dump.sql`, 60 MB) | readable directly |
| Existing extracted evidence from prior rounds | yes | reused, not re-extracted |
| Peer evidence | checked | no peer package consumed |
| **Database restore** | **NOT PERFORMED** | **not required** |

> **`pg_restore` requires `-f` (file) or `-d` (database).** Every extraction in this round used `-f`.
> `-d` was never passed. No database was created, connected to, restored, upgraded or modified; no
> dump file was altered.

## 3. Disposition

**The `HOLD — READ-ONLY RESTORE AUTHORIZATION REQUIRED` is WITHDRAWN as unnecessary for everything
achieved this round.** File-level extraction answered every database question posed, including the
ones Round 2 believed needed a restore — the v18 module registry, petty-cash GL tracing, the TX-01
denominator, and certificate population analysis.

**What a restore would still add**, and therefore what remains held:

| Still requires a live instance | Held as |
|---|---|
| Observing code **execute** (`U-02b`) — e.g. whether `_compute_wt_cert_data` clears `income_tax_form` on recompute (`TX-14`, class D) | `HOLD — RUNTIME EVIDENCE REQUIRED` |
| Rendering the screen report and the CSV export to compare artefacts (`50 §5`) | `HOLD — RUNTIME EVIDENCE REQUIRED` |
| Exact `payment_state` after a force-cancel (`U-03`, class D) | `HOLD — RUNTIME EVIDENCE REQUIRED` |

These are **execution** questions, not **data** questions. A restore alone would not answer them
either — they need the application running. Recorded honestly rather than folded into a restore ask.
