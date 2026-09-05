# S08 — P09_EVENT_TYPE_SWEEP_V2

**Checkpoint:** `CP-P09S08` · **Layer:** 1 — clean-room.
**Only materially affected event types are revalidated.** Unaffected rows from the prior sweep are preserved, not re-run.

---

| Event | Financial source | Analytic eligibility | Sign | Gross | Net | Management effect | Zeroing | Double-count |
|---|---|---|---|---|---|---|---|---|
| **asset depreciation** | 2-row entry | both rows | mirrored | 2X | **0** | destroyed | **CONFIRMED, measured** | no |
| **deferred recognition** | reporting-module entry, then reversed | both legs, **different denominators** | near-mirrored | ≈2X | **residue** | distorted | residue, not clean zero | no |
| **cut-off / change period** | mirrored pair, ×2 entries | both rows | exact swap | 2X | **0** | **period misattribution** — the analytic cut-off does not happen | CONFIRMED | no |
| **change-account transfer** | source rows + re-derived counterpart | both sides | re-derived | ≈2X | **residue** | meaningless residue | residue | no |
| **accrued orders** | N rows + 1 blended counterpart | both sides | re-derived, tax-weighted against untaxed balances | ≈2X | **residue** | meaningless residue | residue | no |
| **cash-basis pairs** | swapped pair on **one account** | both rows | exact swap | 2X | **0** | **arguably required** — the cost was already attributed by the original document | CONFIRMED, but **not a defect** | no |
| **vendor expense / employee expense / revenue** | product rows only | one-sided | correct | X | X | correct | no | no |
| **COGS / inventory** | valuation path | value copied, **ledger link discarded** | one-sided | X | X | correct value, **broken provenance** | no | no |
| **manufacturing duration** | no journal entry at all | work-centre + project bridge | same sign | 2Y | **−2Y** | **duplicated** | no | **CONFIRMED, source-only** |
| **bank fee / write-off** | write-off row | one-sided | correct | X | X | correct | no | no |
| **manual journal** | whatever the user types | user-determined | — | — | — | **a user can create the symmetric case by hand and nothing warns them** | reachable | no |
| **budget transfer** | — | **no budget model exists in any deployment measured** | — | — | — | **NOT DECIDABLE** | — | — |

## Material deltas this round

1. **deferred recognition reclassified** — it is a **residue** case, not a clean zero, and it lives in the reporting module, not the asset module.
2. **cash-basis reclassified** — its cancellation is **arguably required**; the prior "most severe in the programme" ranking is withdrawn.
3. **manufacturing duration** — the corrected bridge path replaces the previously-named pair; **source-only, unexercised in every deployment**.
4. **budget transfer** — cannot be swept: **no deployment holds a budget model this source recognises**.

## CHECKPOINT
**`CP-P09S08` — COMPLETE — EVIDENCE VERIFIED.** Auto-continue.
