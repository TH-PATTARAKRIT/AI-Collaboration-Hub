# P10 — AASP-VETO-01 REVISION 3 RECHECK

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D13`. **Revision 2's conclusions are not inherited.**

---

## 1. Revision History

| Rev | Wording | Grounds |
|-----|---------|---------|
| **1** | No implementation of any P10 mechanism until the Boss rules whether a posting constraint may alter a recognition period | Building first would either reproduce the defect or build a separation the ledger contradicts |
| **2** | Narrowed and re-sequenced; grounds limited to generation; claimed a peer veto bound first | (a) the boundary is adopted so the decision is smaller; (b) a peer veto is broader; (c) the trace option is blocked on a ledger change |
| **3** | Restored; grounds widened to correction and reversal; the evidence-immunity clause struck | All three of revision 2's grounds shown not to hold |

## 2. Re-Evaluation After This Round's Repairs

The directive requires revision 3 be re-evaluated **after** the six repairs. Each is applied.

| Repair | Effect on the veto |
|--------|--------------------|
| **`T0-13` authority restored** | **Strengthens.** Revision 2's ground (a) is not merely unproven — the boundary is an open blocker, so the decision the veto waits on is **larger** than revision 2 assumed, not smaller. And the boundary's close condition has since been **refined** so that refusal alone is insufficient |
| **`R-08` repaired** | **Neutral to the veto; fatal to one of its clauses.** The struck clause — *"no further evidence bears on it"* — is now disproved four times over. Its removal stands |
| **Lock-date exposure corrected** | **Changes what the veto protects, and does not weaken it.** There is no live exposure on the lock path: 1 of 90 companies has a lock, and that database holds ten journal entries. The veto is not holding back remediation — it is **holding a design choice open before the first company closes a period**. That is the cheapest moment to decide and the most expensive to get wrong |
| **`EC-02` work** | **Neutral.** Enumeration still open; nothing bears on the veto |
| **`EC-04` work** | **Slightly strengthens.** Two components closed, but `TZ-4`, `TZ-5` and `TZ-6` remain unreproduced, and `TZ-7` sits with the ledger owner at 0 of 8 |
| **`EC-07` work** | **Strengthens.** Zero clean passes of two required; the package's own reliability is unestablished |

## 3. The One Ground That Could Have Lifted It

If the estate were **exposed**, the veto would be holding back urgent remediation and there would be a case for narrowing it to let a fix proceed.

**The estate is not exposed on the lock path.** So the argument for narrowing on urgency does not arise, and the argument for holding — decide before exposure exists — is stronger than it was.

## 4. The Ground That Now Widens It

The peer's refined close condition establishes a **second mutation path that fires with no lock configured**, reachable by construction in all four deployed databases, with **unknown** exposure.

Revision 3's grounds cover generation, correction and reversal on the **lock** path. They do not mention the lock-free path, which is the more reachable of the two.

> **Revision 3 grounds are extended to include the lock-free mutation path.** The subject is unchanged; the grounds are widened again. This is the fourth time this boundary has been found too narrow — three times by peers, once now by P10 against its own instrument.

## 5. Final Status

> **`AASP-VETO-01` — VETO REMAINS, AND IS STRENGTHENED.**
>
> **Wording, revision 3 as re-checked:** no implementation of any P10 recognition mechanism may start until **both** (a) Boss decision `D-5` — the accounting-event identity — is taken, and (b) Boss decision `P10-D-02` is taken **jointly with `T0-13` / `P11-B-16`**, selecting among the options **as classified in `39` and `40`**.
>
> **CORRECTED, `34` `W-38`:** the lift condition first named `28` revision 2, which carries the **pre-refinement** option logic — it states that refusal alone satisfies the condition and that five options remain admissible if the boundary is adopted. Under the refined condition **`OPT-B` alone and `OPT-E` alone do not suffice**. `39` §4 and `40` §5 are the current classification; `28` revision 2 is retained as lineage and must not be used as the lift condition.
>
> **Grounds:** generation · correction and reversal · the reopen path · **and the lock-free mutation path**.
>
> **Scope:** implementation only. Design work, option analysis and specification are not blocked.
>
> **Not immune to evidence.** The clause asserting that no further evidence bears on it is withdrawn and will not be restored.
>
> **This is the only veto binding P10's implementation.** No peer veto covers it.

## 6. What Would Close It

Both Boss decisions taken. **No amount of further research closes this veto** — but that statement is now made with the evidence search behind it that revision 2 asserted without: the deployed population is enumerated, the exposure is measured, and the outstanding items at `49` §4 are named. Research can still change the veto's *grounds*; it cannot discharge it.
