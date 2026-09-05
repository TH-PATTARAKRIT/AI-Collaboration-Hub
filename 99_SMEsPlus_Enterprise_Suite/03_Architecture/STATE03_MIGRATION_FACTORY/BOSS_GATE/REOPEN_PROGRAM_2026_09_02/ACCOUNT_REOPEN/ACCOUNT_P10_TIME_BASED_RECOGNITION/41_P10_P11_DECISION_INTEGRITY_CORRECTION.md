# P10 → P11 — DECISION INTEGRITY CORRECTION

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D04`.

> **THIS IS A SUPPLEMENT AND CORRECTION. IT IS NOT A REPLACEMENT.**
>
> The prior P10 decision package — `16` §5 as revised, and `35` §5 — is **preserved unchanged as audit lineage**. Nothing in it is deleted. This document states what was wrong in it, what is restored, and what P11 must carry forward instead.

---

## 1. Original Decision Package

Delivered at `f9b40b3`: seven decisions, one with an attached acceptance condition, terminal state *maximum available evidence reached — hold for specific peer / Boss decision*. Preserved in full.

## 2. The Original Assumption

That the peer tolerance-zero boundary `T0-13` was an **adopted programme boundary**, and that its close condition therefore operated on P10's option set as a constraint already in force.

## 3. The Unauthorized Adoption

`T0-13` is blocker `P11-B-16`, status **`HOLD — BOSS DECISION REQUIRED`**. It has never been adopted. P10 recorded it as adopted in three documents while its own intake register classed it correctly as a position. **P10 converted an unresolved peer decision into a programme boundary and reasoned from it.**

The directive's rule, which P10 breached: `UNRESOLVED PEER DECISION ≠ ADOPTED PROGRAMME BOUNDARY.`

## 4. Affected Options

| Option | Effect |
|--------|--------|
| **`OPT-A` — permit the silent re-date (status quo)** | **Eliminated**, on the sole ground that it did not satisfy an "adopted" boundary |
| `OPT-B`, `OPT-C`, `OPT-D` | Carried; unaffected |
| `OPT-E`, `OPT-F` | Not discovered at the time — a completeness defect, not an elimination |

## 5. Restored Options

**`OPT-A` is restored, unconditionally, to the decision space.** Its correct standing: *conditionally excluded if and only if the Boss adopts `T0-13`.* See `39`.

Two further options — a shipped lock-exception mechanism and a chatter trace — are in the set. **Correction, `34` `W-44`: they were found in the PRIOR round's fresh challenge, not during this repair.** This document mis-dated its own discovery. The option set is **six**, not three.

## 6. `T0-13` True Status, and a Refinement P10 Did Not Have

Status: **`HOLD — BOSS DECISION REQUIRED`** · tolerance-zero · present defect · *"found narrow three times"*.

**Close condition refined by P11 at its Delta 08, after P10 last read it:**

> A second mutation path fires with **no lock configured**, so there is nothing to refuse. **Where a mutation path has no violation to detect, an attributable trace is MANDATORY, not alternative.**

**Consequence P11 must carry:** a design satisfying `T0-13` by implementing **refusal alone** would leave that path live and the boundary would read as met. P10's earlier framing — that the condition offered two interchangeable alternatives — is superseded.

## 7. Corrected Conditional Logic

| If the Boss… | Then P10's option set is… |
|--------------|---------------------------|
| adopts `T0-13` as refined | `OPT-C`, `OPT-D`, `OPT-F`, or `OPT-B`+`OPT-F`, or `OPT-E`+`OPT-F` |
| adopts `T0-13` unrefined | as above **plus** `OPT-B` alone and `OPT-E` alone — and the lock-free path remains live |
| rejects `T0-13` | all six, decided on domain grounds |
| defers `T0-13` | all six; **P10 cannot close `P10-D-02`** |

## 8. Decisions the Boss Must Consider Together

**`P10-D-02`** and **`T0-13` / `P11-B-16`** — one decision in two parts, `T0-13` first. Truth table at `40` §5.

**`D-5`** (accounting-event identity) is adjacent, not coupled: it gates `OPT-D` and P10's kernel question, and nothing else in this decision.

## 9. Remaining Evidence

| Item | Status |
|------|--------|
| Has any recognition entry actually been re-dated in the deployed estate? | **ANSWERED — no.** See `43`. Closed across the whole readable population |
| Is the lock-exception route available on the older estate line? | Open — the object is absent from that line's schema |
| The lock-free mutation path's population in P10's own mechanisms | **Open** — P10 has not enumerated it; it is P11's `UAE-05` and belongs jointly to P10 and the ledger owner |
| Peer scope-matrix comparison | Class `C` — not compared; routed to P11 |

## 10. What P11 Should Do With This

1. Carry `OPT-A` in the option set, marked conditionally excluded.
2. Present the two decisions coupled, `T0-13` first.
3. Note that P10's prior package reasoned from an unadopted boundary. **The claim that no P10 finding of fact depends on that error is class `B`, not established** — it was asserted without an enumeration, and the enumeration since performed at `47` §3 records a second decision-authority error that *is* a finding of fact (`34` `W-36`). The safe statement: the breach affected the decision space; whether it touched any finding of fact has not been exhaustively checked.
4. Treat the prior package as lineage, not as superseded content.
