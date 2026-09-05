# P01 — PMO TARGETED EXIT REVIEW

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.** PMO issues a recommendation only. **Boss is Sole Final Approver.**

---

## 1. THE DIRECTIVE'S OWN CHECKLIST

| # | PMO must verify | Verdict |
|---|---|---|
| 1 | Module population denominator corrected | **YES** — 12→35 and 17→45 by transitive closure |
| 2 | Transitive dependency closure used | **YES**, with its five false-negative modes declared |
| 3 | Landed cost included | **YES** — traced; installed in all four, exercised in none |
| 4 | Subcontract purchase included | **YES** — ten modules, nine installed in `D4`, zero transactions |
| 5 | Deployment differences separated from source capability | **YES**, and this was the round's main methodological gain |
| 6 | Receipt-to-Bill bridge sufficiently investigated | **YES** — classified `VERSION-DEPENDENT`, after two corrections |
| 7 | Period Lock sufficiently investigated | **YES** — `MIXED — PATH-DEPENDENT` |
| 8 | Bill correction sufficiently investigated | **YES** — `MIXED`, strong form contradicted |
| 9 | Scope-aware ownership proved or held | **HELD** — `UNPROVEN — INFERRED ONLY`, tolerance-zero |
| 10 | WHT / PND findings routed correctly | **YES** — all statutory questions held and routed to P07 |
| 11 | `DEP-P01-06` resolved or formally held | **`PARTIALLY RESOLVED`** |
| 12 | Peer evidence consumed | **YES** — ten packages; two peer findings re-derived |
| 13 | Source Link Register reproducible | **YES** |
| 14 | Evidence Manifest complete | **YES** |
| 15 | Revision lineage preserves all author errors | **YES** — fifteen error records, none deleted |
| 16 | P11 handoff decision-usable | **YES — materially stronger than the previous round** |

**PMO must not declare readiness merely because the artifact count is high.** It does not, and
§2 is why.

---

## 2. THE EIGHT EXIT CRITERIA

| Criterion | Verdict | Reason |
|---|---|---|
| `EC-01` Scope Bounded | **NOT SATISFIED** | Improved substantially — but the evidence base was **wrong about itself** for a whole round: one database excluded, one mislabelled by three major versions. The function population remains `UNBOUNDED`, so **no coverage percentage is published** |
| `EC-02` Enumeration Converged | **NOT SATISFIED** | The opposite of converged. Eight corrections, all external; contradictions 11→16 |
| `EC-03` Unknown Exhausted | **NOT SATISFIED** | Gating unknowns remain, and `D4`'s transaction data is newly-known-reachable and unread |
| `EC-04` Tolerance-Zero Closed | **NOT SATISFIED** | **Worse than the previous round.** Cross-tenant reachability is now demonstrated as live, and its one guard is proven inert |
| `EC-05` Contradiction Resolution | **NOT SATISFIED** | Sixteen, **zero closed** |
| `EC-06` Negative Claim Controlled | **NOT SATISFIED** — *changed from the previous round* | Three published claims were **false**, each a class-A-shaped statement bounded to a scope that wrongly excluded the decisive database. The classes were declared honestly; **the boundary itself was the defect** |
| `EC-07` Two Clean Independent Passes | **NOT SATISFIED** | One pass, and emphatically not clean: it produced a new material population, a new evidence source, a new finding class and a new gating unknown |
| `EC-08` Final Knowledge Package | **SUBSTANTIALLY SATISFIED** | All required artifacts present; runtime and statutory evidence declared absent rather than concealed |

**Seven of eight not satisfied — one worse than the previous round.**

---

## 3. RECOMMENDATION

> ### `RECOMMEND HOLD`

Unchanged from the previous round, for **stronger and partly different** reasons.

`RECOMMEND CONDITIONAL PASS` is unavailable: `EC-04` forbids passing over a tolerance-zero risk,
and that risk is now demonstrated live rather than suspected.

`RECOMMEND FAIL` is wrong: the research is sound, reproducible and materially advanced. What is
incomplete is the **evidence base**, and this round proved that by repairing part of it.

**Boss is Sole Final Approver. This is a recommendation only.**

---

## 4. WHAT THIS ROUND ACHIEVED, DESPITE THE HOLD

1. The receipt-to-bill bridge **classified**, after the vendor's own design intent was found.
2. **No inventory value reaches the ledger by any route** in the v19 deployments — cause and
   effect both evidenced.
3. The module denominator corrected, and **landed cost and subcontract purchase brought in**.
4. Installed-status evidence introduced, separating source capability from deployed reality for
   all 65 population members.
5. A **live cross-tenant reachability** finding, with its guard proven inert.
6. Two prior findings **disproved** and replaced with better ones.
7. Ten peer packages consumed; the P05 question answered; the P05 contradiction resolved without
   overruling a peer.
8. **Fifteen research-error records**, all preserved with their originals.

---

## 5. THE METHOD FINDING OF THIS ROUND

The previous round's ratio was **five self-caught defects to one externally caught**. This round
it is **two to eight** — and the difference is not that this round was sloppier. It is what the
two sets are *about*:

- The **self-caught** defects were errors in my reasoning over evidence I had.
- **All eight external** defects were errors about **the evidence base itself** — a database
  wrongly declared unreadable, a database mislabelled by three major versions, code assumed to be
  running that runs nowhere, a design change read as a misconfiguration.

> **An author can check their reasoning. An author cannot easily check the frame the reasoning
> sits in, because the frame is what they are reasoning with.**

Three disproof assignments were issued, and **three of three landed**. Ordinary independent
review in the previous round found one denominator defect. Adversarial disproof in this round
overturned two headline findings and repaired the evidence base. **The format did that, not the
effort.**

**Recommendation to the programme:** make the disproof assignment standard for every headline
finding, and require one expert per round whose only task is to **audit the evidence base rather
than the findings**.
