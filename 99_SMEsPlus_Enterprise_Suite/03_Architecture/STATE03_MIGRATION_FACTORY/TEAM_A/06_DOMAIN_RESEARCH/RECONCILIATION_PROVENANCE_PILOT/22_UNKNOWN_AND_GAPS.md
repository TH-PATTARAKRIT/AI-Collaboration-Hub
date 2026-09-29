> Domain: RECONCILIATION_PROVENANCE_PILOT (Gx10) | Evidence Gap Register

# 22 — UNKNOWN AND GAPS (Gx10)

| ID | Gap | Impact | Status | Route to close |
|---|---|---|---|---|
| GAP-RCN-01 | Whether the stock-move-to-journal-entry cross-link (RCN-F02) exists and is inspectable for *ordinary* (non-backdated) transactions, or is a backdating-specific enhancement | Materially affects how strong a "provenance" claim can be made for the general case, not just the backdating edge case | **`SOURCE/DUMP FINDING — CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION` (2026-09-30, Handoff round 2 `R9`), `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET` — source-static lead.** A stock move carries a reference to the journal entry it creates, set every time the system creates a move-level accounting entry — not conditioned specifically on backdating; `force_period_date` only sets the posting date, it is not a separate reference mechanism. **Important scope limit** (`INFER`): this reference exists only for entries created at the **move level** (the mechanism this whole Deep Study's Gx6/Gx8 chain describes); entries created from a vendor-bill or customer-invoice **line** (referencing their own originating order line, not the stock move directly) are a *different* link, not confirmed to be the same reference. So the answer is "yes, a real reference exists for ordinary move-level entries" but **not a confirmation that every stock-to-financial link in the system uses this same mechanism**. **Not a closure** | Manifest/dependency review (no override found in license-open modules, except `cr_effective_date_entries`'s non-Odoo-19 date-handling wizard), then runtime confirmation of the audit-trail text a user actually sees |
| GAP-RCN-02 | Whether per-lot cost-origin tracking (RCN-F03) applies under AVCO, not just FIFO | `CQS-RCN-03` | **`SOURCE/DUMP FINDING — CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION` (2026-09-30, Handoff round 2 `R9`), `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET`** — per-lot valuation (when enabled on a product) supports Standard, Average (AVCO), and FIFO alike in the lot-cost computation itself; lot cost updates per the product's own costing method; outgoing moves of a lot-valuated product use that lot's own cost. This directly answers the gap in the affirmative for Community core: AVCO is not excluded. **Not a closure** — the specific quality of AVCO-per-lot numbers against a late-arriving vendor bill was not traced | Manifest/dependency review, then documentation or runtime pass |
| GAP-RCN-03 | Same network/egress constraint as all prior Gx | Search-synthesis, not verbatim reads | **Non-blocking** | Same as prior Gx |

## Status summary

```
GAPS OPEN              : 3 (GAP-RCN-01..03 — none closed; GAP-RCN-01/02 now carry a SOURCE/DUMP FINDING, not a closure)
SOURCE/DUMP FINDING RECEIVED, PENDING RECONCILIATION : 2 (GAP-RCN-01, GAP-RCN-02, both CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET)
NON-BLOCKING           : 1 (GAP-RCN-03)
```

**No V-level or gap is treated as closed on the strength of a source/schema finding alone.** Both findings above came from a separate Source/Dump Deep Research Worker session (Boss's local Claude Code session), relayed via `STATE03_SOURCE_DUMP_EVIDENCE_DELTA_HANDOFF.md` round 2 `R9` — this session (STATE03 Integration/Architecture Knowledge Owner) has reconciled the wording into this canonical register but has not declared either gap closed, and has not created a competing register or denominator. This closes the Gap Register *research* activity for the full 10-scenario Lane C set (2026-09-28 documentation round) — it does not close either gap itself.

## Cross-reference

Source-code research performed 2026-09-30 (round 2) by a separate Source/Dump Deep Research Worker (Boss's local Claude Code session, read-only, `odoo-19.0.post20260921` Community source), pushed to branch `claude/local-odoo-source-research`. Full detail: `TEAM_A/04_EVIDENCE_PACKS/STATE03_SOURCE_DUMP_EVIDENCE_DELTA_HANDOFF.md` §`R9`. **Mandatory caveat**: the actual test/pilot database (`iTEST02`) has ~696 tables beyond vanilla Community — every finding above is `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET`.
