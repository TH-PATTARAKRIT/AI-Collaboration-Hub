> Domain: PERIOD_CUTOFF_VALIDATION_PILOT (Gx6) | Evidence Gap Register

# 22 — UNKNOWN AND GAPS (Gx6)

| ID | Gap | Impact | Status | Route to close |
|---|---|---|---|---|
| GAP-PCO-01 | No documented correction mechanism for a post-Hard-Lock error | Cannot state how a design should handle this case | **`SOURCE/DUMP FINDING — CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION` (2026-09-30, Handoff `D-07`), `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET`** — 5 lock types (Global, Tax, Sales, Purchase = soft; Hard = irreversible, no exception path in source); an entry dated at/before Hard Lock is blocked (`UserError`), at/before Global Lock is blocked unless a Lock Exception is granted; a *new* entry whose date falls inside the locked window is instead silently rolled forward to the first open day at create/post time (two distinct code paths, not yet reconciled against each other by this finding). Correction path = a new entry/reversal dated after the lock, not an in-place edit. **Schema-only confirms no database-level CHECK/trigger enforces any lock — enforcement is application-layer only**, so a direct-SQL import bypasses it. **Not a closure** — a third-party OCA module (`account_lock_date_update`) and a Cybrosys module (`base_accounting_kit`) both touch lock-date handling in the actual installed set and have not been fully override-audited; Enterprise-only lock-date-change tooling exists in schema with no source to review | **Manifest/dependency review of `account_lock_date_update`/`base_accounting_kit` overlay, then documentation or runtime pass** |
| GAP-PCO-02 | Whether Stock Closing is a required manual action or can be scheduled/automated | Affects operational-design assumptions about period-close reliability | **`SOURCE/DUMP FINDING — CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION` (2026-09-30, Handoff `D-06`), `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET`** — Stock Closing defaults to a Manual action but source supports scheduled/automatic (daily or monthly cron) generation as a configuration choice; it is **not itself a self-reversing entry** — the reversal-dated mechanism belongs to the separate Accrued Orders/WIP wizards, a distinction the prior "self-reversing" framing conflated. **Not a closure** — not runtime-confirmed | Manifest/dependency review, then documentation or runtime pass |
| GAP-PCO-03 | Whether a bill created before receipt (Gx5 `GAP-PDT-01`, if confirmed as a real gap) interacts with the accrual mechanism or bypasses it entirely | Compound question across two open findings | **Non-blocking, flagged as a good combined AWT target** | AWT, combined with the Gx5 `PDT-F03` test |
| GAP-PCO-04 | Same network/egress constraint as all prior Gx | Search-synthesis, not verbatim reads | **Non-blocking** | Same as prior Gx |

## Cross-Gx resolution action taken

The valuation-timing question previously logged as an Evidence Conflict in `GRV-F04` (Gx1), `GAP-SDV-01` (Gx2), and `GAP-IAV-01` (Gx4) is **downgraded from "Evidence Conflict" to "Resolved — documentation-tier, high confidence, AWT still recommended for final confirmation"** in each of those files via addendum (originals not deleted). See each file's own update note.

## Status summary

```
GAPS OPEN                 : 4 (GAP-PCO-01..04 — none closed; GAP-PCO-01/02 now carry a SOURCE/DUMP FINDING, not a closure)
SOURCE/DUMP FINDING RECEIVED, PENDING RECONCILIATION : 2 (GAP-PCO-01, GAP-PCO-02, both CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET)
NON-BLOCKING              : 2 (GAP-PCO-03, 04)
CROSS-Gx ITEMS RESOLVED THIS ROUND (2026-09-28) : 3 (GRV-F04 conflict, GAP-SDV-01, GAP-IAV-01) — unaffected by this round's source finding
```

**No V-level or gap is treated as closed on the strength of a source/schema finding alone.** `GAP-PCO-01`/`GAP-PCO-02` findings above came from a separate Source/Dump Deep Research Worker session (Boss's local Claude Code session), relayed via the consolidated `STATE03_SOURCE_DUMP_EVIDENCE_DELTA_HANDOFF.md` (`D-06`, `D-07`) — this session (STATE03 Integration/Architecture Knowledge Owner) has reconciled the wording into this canonical register but has not declared either gap closed, and has not created a competing register or denominator.

## Cross-reference

Source-code research performed 2026-09-30 by a separate Source/Dump Deep Research Worker (Boss's local Claude Code session, read-only, `odoo-19.0.post20260921` Community source + schema-only `iTEST02` dump cross-check), pushed to branch `claude/local-odoo-source-research` and reconciled here per the same Carry-forward-citation discipline used for `GROUP_01_SALES_INVENTORY_PURCHASE`. Full detail: `TEAM_A/04_EVIDENCE_PACKS/STATE03_SOURCE_DUMP_EVIDENCE_DELTA_HANDOFF.md` §3 `D-06`/`D-07`. **Mandatory caveat**: the actual test/pilot database (`iTEST02`) has ~696 tables beyond vanilla Community, and at least two license-open third-party modules (`account_lock_date_update`, `base_accounting_kit`) actively touch lock-date logic in the confirmed-installed set — every finding above is `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET` until those modules' override behavior is fully reviewed (partial review done; see Handoff §2.1).
