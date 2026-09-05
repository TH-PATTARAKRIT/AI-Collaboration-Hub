# P10 — TQ-13 AUTHORITY BREACH FORENSIC

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D01`.

---

## 1. Identifier Reconciliation — read this first

The directive names the boundary **`TQ-13`**. **No identifier `TQ-13` exists in the peer package.** An exhaustive search of the P11 package at its current head returns **zero occurrences**.

The authoritative identifier is:

> **`T0-13`**, carried as blocker **`P11-B-16`** in `P11_FINAL_BLOCKER_REGISTER.md`.

`T0` is the peer's prefix for a tolerance-zero boundary. `TQ-13` is treated throughout this document as the Boss's rendering of `T0-13` / `P11-B-16`, and every finding below is stated against the authoritative identifier. Recorded as a naming reconciliation, not as a discrepancy in substance.

## 2. The Authoritative Status — quoted from the peer's own register

| Field | Peer's own words |
|-------|------------------|
| Blocker | `P11-B-16` |
| Boundary | `T0-13` — *"an accounting fact may be SILENTLY MUTATED, at any scope"* |
| **Status** | **`HOLD — BOSS DECISION REQUIRED`** |
| Class | tolerance-zero · **present defect** · *"found narrow three times"* |
| Reachability | *"Reachable today, so it stands whatever the Boss rules on `D-12`"* |

**`T0-13` is an OPEN BLOCKER awaiting a Boss decision. It is not an adopted programme boundary, and it never was.**

## 3. Where P10 Converted a Position Into a Boundary

| Location | What P10 wrote | Authority status of the claim |
|----------|----------------|-------------------------------|
| `28` revision 1 §4 | *"the tolerance-zero condition **already adopted** by two peer processes"* | **BREACH** — the condition is proposed, not adopted |
| `28` revision 1 §4 | *"P10 records that `A` alone is **not** among the options that satisfy `T0-13`, and that this is a **consequence of a boundary two peers have already adopted**, not a P10 preference"* | **BREACH — this is the operative sentence.** An architecture option on a Boss-reserved decision was eliminated, and the elimination was attributed to an adopted boundary that is not adopted |
| `32` revision 2 §2 | *"`T0-13` … is adopted programme-wide"* | **BREACH** |
| `32` revision 2 §3 | The veto was **narrowed** partly on the ground that "two of the four options already satisfy an adopted boundary" | **BREACH with downstream effect** — a governance instrument was weakened on the strength of it |
| `23` §1 `IN-03` | Classed as *"ADOPTED"*, verification recorded as *"the widening applies to P10"* | **MISCLASSIFICATION** — an applicability argument recorded in a verification column |
| `23` §4 | Classed as one of *"4 **adopted positions** rather than facts"* | **CORRECT** — and it contradicts the three entries above |

## 4. The Anatomy of the Breach

P10 did **not** decide the Boss-reserved question — *may a posting constraint alter an original recognition period?* Every document carried it as `BOSS DECISION REQUIRED`.

**P10 decided the question one level up: whether the thing that forecloses the reserved question binds.**

That is the subtler failure, and it is more dangerous, because it does not look like a decision. It reads as a consequence. The chain was:

1. take a peer's **proposed close condition** for an open blocker;
2. record it as **adopted**;
3. observe that the status quo does not satisfy it;
4. conclude the status quo is **excluded** — *"as a consequence, not a preference"*;
5. narrow a **veto** on the strength of the smaller decision that remained.

Steps 3, 4 and 5 are all sound **given step 2**. Step 2 is the breach, and it is a single word.

## 5. Why the Package Did Not Catch It

P10's own intake register had it right at `23` §4 — classed as a position, not a fact — and wrong in three other places. **The package contradicted itself and no internal control fired**, because:

- the four fresh challenges of the previous round were scoped at findings, evidence base and method; **none was scoped at decision authority**;
- the correct classification lived in a summary table, and the incorrect ones lived in the documents that used it;
- P10 read the peer's *position* from its own earlier notes rather than from the peer's **status field**, which was one file away and says `HOLD — BOSS DECISION REQUIRED` in bold.

## 6. Material Delta Discovered While Repairing the Breach

Reading the peer's register properly did not only correct the status. It surfaced a **refinement P10 did not have**, made by the peer at its Delta 08:

> `T0-13`'s close condition was *"refuse **OR** record an attributable trace"*. A second mutation path — `UAE-05` — **fires with no lock configured**, so **there is nothing to refuse**.
>
> **Refined close condition: where a mutation path has no violation to detect, an attributable trace is MANDATORY, not alternative.** A design satisfying `T0-13` by implementing refusal alone would leave that path live and the boundary would read as met.

**Consequence for P10's option set:** under the refined condition, **Option B — refuse — is by itself insufficient**, because it addresses only the lock-triggered path. P10's own `P10-U-23` had identified the lock-free path as a gap; the peer has now folded it into the boundary's close condition.

So the breach cost P10 twice: it eliminated an option it had no authority to eliminate, **and** it left P10 working from a superseded version of the condition it was eliminating against.

## 7. Classification

| Item | Class |
|------|-------|
| `T0-13` is an open blocker, `HOLD — BOSS DECISION REQUIRED` | **FACT VERIFIED** — quoted from the peer's register at the peer's current head |
| `TQ-13` does not exist as an identifier in the peer package | **FACT VERIFIED** — exhaustive search, zero occurrences |
| P10 treated it as adopted in three documents | **FACT VERIFIED** — P10's own text |
| The refined close condition makes refusal alone insufficient | **FACT VERIFIED** — quoted from the peer's Delta 08 |
| That the breach was undetectable by the challenge scopes then in use | **SUPPORTED INTERPRETATION** |

## 8. Remedy

1. Every assertion that `T0-13` is adopted is withdrawn — see `39`, `40`, `41`.
2. Every option eliminated on that basis is **restored** — `39`.
3. The veto is re-evaluated without that ground — **`51`** *(cross-reference corrected; it read `47`)*.
4. P10 **adds a fifth challenge class, decision authority, to its own challenge protocol** — **`47`** *(cross-reference corrected; it read `45`)*. **P10 proposes, and does not impose, that the programme adopt it: that is a PMO and Boss matter.**
5. P10 **proposes for programme adoption**, and applies to itself immediately: *an unresolved peer decision is not an adopted programme boundary, and a peer's status field is the only authority for its status.* **Stated as a proposal, not as a programme rule — P10 has no authority to issue one.** `34` `W-43`.
