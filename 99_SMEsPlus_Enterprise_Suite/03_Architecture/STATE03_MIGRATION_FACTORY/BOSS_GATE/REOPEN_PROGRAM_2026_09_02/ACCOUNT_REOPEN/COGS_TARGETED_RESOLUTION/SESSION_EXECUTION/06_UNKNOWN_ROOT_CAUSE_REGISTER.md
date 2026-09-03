# 06 — Unknown Root Cause Register

Codes `RC-01`–`RC-12` are available; only codes actually evidenced by findings in files `03`/`05` are populated below. Unused codes are listed at the end and left empty rather than force-filled.

| Code | Root Cause | Evidenced By | Item Count |
|---|---|---|---:|
| `RC-01` | Reference-benchmark behavior changed across major versions, so "match the reference" has no single target | `CGS-U01`, `CGS-U02`, `CGS-U05` | 3 |
| `RC-02` | Primary-source fetch failure / reconstruction from secondary sources | `CGS-U04`, `CGS-U12` | 2 |
| `RC-03` | Same UI label carries different underlying meaning depending on mode/version | `CGS-U06` | 1 |
| `RC-04` | Reference vendor's own documentation is internally contradictory across sources | `CGS-U03`, `CGS-U34` | 2 |
| `RC-05` | Behavior never directly observed on a live instance; inferred only by analogy or community corroboration | `CGS-U05`, `CGS-U07`, `CGS-U30`, `CGS-U32` (FIFO sub-case), `CGS-U42` | 5 |
| `RC-06` | Vendor's own documentation admits an unresolved internal control gap (not a documentation gap — a genuine product gap) | `CGS-U32` (AVCO sub-case), `CGS-U36` | 2 |
| `RC-07` | No reference precedent exists at all — this is original design territory, not an evidence gap | `CGS-U37`, `CGS-U39` | 2 |
| `RC-08` | Requires a SMEsPlus-specific business-policy or accounting-policy ruling that no external evidence can supply | `CGS-U16`, `CGS-U22`, `CGS-U40`, `CGS-U45`, `CGS-U48`, `CGS-U50` | 6 |
| `RC-09` | Thai statutory primary source not yet extracted or not yet cross-tested against a specific SMEsPlus question | `TH-HOLD-COGS-01`–`04`, `TH-HOLD-05-residual`, `TH-NEW-01`, `TH-NEW-02` | 7 |
| `RC-10` | Structural mismatch between two independently-designed subsystems (e.g. Inventory-side vs. Accounting-side idempotency) | `CGS-U45` (secondary), `CGS-U40` (secondary) | (counted under `RC-08` primary; noted here as secondary influence only, not double-counted in the item count column) |

**Codes not populated — no evidence found to support them this session:** `RC-11`, `RC-12`. Stated explicitly per the instruction not to force all twelve codes to have entries.

## Note on Double-Counting

`CGS-U40` and `CGS-U45` each have both a primary root cause (`RC-08`, business-policy ruling required) and a secondary structural-mismatch character (`RC-10`-like). To avoid inflating the item count, each item is counted once under its primary root cause only, consistent with the same single-primary-category discipline used in the Fact Verification session's own classification matrix (file `04` of that package).
