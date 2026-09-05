# P10 ↔ P08 — LEDGER / RECOGNITION-PERIOD RECONCILIATION

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-CROSS-PROCESS-RECON-001` · Layer 1
Peer: `P08` Record-to-Report, head `4bdf8a2`, terminal `RECOMMEND HOLD`, exit criteria **0 of 8**, eight tolerance-zero boundaries open and none closed.

`P08` owns the ledger contract every other Account process must satisfy. P10 supplies it a recognition event; P08 decides what a posting is. This is the reconciliation on which P10's central design element depends.

---

## 1. The Finding That Relocates P10's Design

> **`P08`: no accounting-event object exists in any of the 22 declared roots, so `ONE FACT → ONE ACCOUNTING EFFECT` is unenforceable.**

The parent P10 package's single most important structural finding was that the reference product **collapses the recognition event into the posting act**, and that every other P10 defect follows from that collapse. It proposed a recognition-event object with identity as the kernel's first element.

`P08` has now established that the absence is **not a deferral property and not a recognition property**. It is a property of the accounting core: there is no event object for *anything*. Two processes found the same hole at two layers, independently.

**Consequence for P10's design position — this is a change, not a confirmation:**

| Parent position | Reconciled position |
|-----------------|---------------------|
| P10 defines a recognition-event object with identity, as element 1 of a shared recognition kernel | **P08 defines the accounting-event object. P10 specialises it into a recognition event.** P10 must not define a competing identity |

If P10 authored its own event identity while P08 authored the accounting-event identity, the programme would acquire **two event objects for one economic fact** — which is the precise failure the invariant forbids, committed by the processes enforcing it. Recorded as `P10-D-01` restated in `35`, and fed to Boss decision `D-5`, which `P11` has already named.

## 2. Recognition Period versus Posting Date — the ledger's answer

| P10's requirement | P08's evidence | Verdict |
|-------------------|----------------|---------|
| A recognition event must carry the period it belongs to, separately from the date its posting carries | **"Closing a period is moving a date."** The ledger has no period object; a period is a date range and a lock is a date | **The separation P10 requires cannot be expressed in the ledger as it stands** |
| A posting constraint must not silently alter a recognition period | The irrevocable lock **relocates rather than refuses** on the posting path, and the product's own test asserts a full annual charge crossing a fiscal year | **Confirmed, with the same executed positive control P04 supplied** |

So P10's requirement is not a preference the ledger merely fails to honour — **there is no field in which a recognition period could be recorded.** The requirement is a new ledger obligation, and `28` classifies the options without choosing between them.

## 3. Obligations P10 Places on P08

| # | Obligation | Driven by |
|---|-----------|-----------|
| `OB-01` | Define the accounting-event object and its identity. P10 will specialise, not duplicate | `IN-05`, Boss `D-5` |
| `OB-02` | Provide a place to record **the period an amount belongs to**, distinct from the date the entry carries | §2 |
| `OB-03` | When a posting constraint moves an entry's date: **refuse, or record an attributable trace of the original period — and where the mutation path has no violation to detect, the trace is MANDATORY, not alternative.** **CORRECTED, `38` §6 and `58`:** the earlier wording gave the unrefined condition and said P10 *adopts* it. `T0-13` is an **open blocker**; P10 does not adopt it, and its refined form is the one that binds if the Boss adopts it | `PD-16` |
| `OB-04` | ~~The nets-to-zero attribution is a posting-layer property~~ — **WITHDRAWN, `34` `W-19`.** The attribution shape is built by each mechanism, not by the posting layer. Only the **untracked post-lock editability** of allocations belongs to `P08`. The attribution shape returns to the recognition domain, where it is the strongest argument for a shared allocation layer | `OUT-03` |
| `OB-05` | State the currency model for a programmatic entry that carries no currency of its own — P10's recognition lines carry none | `D-13` |

## 4. Constraints P08 Places on P10

| # | Constraint | P10's response |
|---|-----------|----------------|
| `CN-01` | A posted journal item is editable in place | P10 cannot rely on immutability of a posted recognition entry. Every P10 control must assume the entry can change after the fact |
| `CN-02` | The double-entry balance invariant is a caller-supplied parameter with no database-level enforcement | P10's recognition pairs are balanced by construction and by construction only. No backstop exists |
| `CN-03` | P08's root-set defect is closed for only 3 of ~23 class-`A` claims | P10 carries P08's other claims as class `B` and never as sole support for a gate movement. See `23` `IN-14` |
| `CN-04` | P08's own gate is 0 of 8 with 8 tolerance-zero boundaries open | **P10 cannot close `EC-04` while the ledger it posts into has not closed one tolerance-zero boundary.** See `31` |

## 5. The Reconciliation's Hardest Consequence

`CN-04` is the one that decides P10's gate.

P10's two company-boundary findings, its silent-re-date finding, and its nets-to-zero finding all resolve into the posting layer. P08 has that layer open at 0 of 8 with 8 tolerance-zero boundaries unclosed. **No amount of further P10 research can close `EC-04` for P10**, because the boundary P10 would have to close is not in P10's scope.

This is not a reason to route P10's blocker to a later wave — the 8-Criteria Constitution forbids using a later route to hide a blocker belonging to the current scope. It is a statement that the blocker **belongs to P08's scope and is correctly held there**, and that P10's own gate is consequently dependent rather than independent. Stated plainly in `31` and `36`.

## 6. Where P08 and P10 Disagree

**None found.** Every P08 finding P10 tested against its own evidence either agreed or addressed a layer P10 had not examined. This is recorded as an agreement, not as a confirmation of correctness: two processes reading the same source with the same method can share a blind spot, and neither has runtime evidence of the posting layer's behaviour under the specific conditions P10 cares about.
