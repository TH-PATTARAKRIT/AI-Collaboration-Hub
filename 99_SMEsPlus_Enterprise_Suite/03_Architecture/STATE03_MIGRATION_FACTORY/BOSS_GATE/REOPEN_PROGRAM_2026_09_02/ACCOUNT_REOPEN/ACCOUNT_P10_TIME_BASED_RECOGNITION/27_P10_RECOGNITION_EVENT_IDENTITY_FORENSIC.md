# P10 — RECOGNITION EVENT IDENTITY FORENSIC

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-CROSS-PROCESS-RECON-001` · Layer 1

The parent package's root-cause finding was that the recognition event is collapsed into the posting act. This forensic asks the next question: **what would an identity have to be, for it to work across every mechanism — and whose object is it?**

---

## 1. The Invariant Being Served

> `ONE ECONOMIC FACT → ONE CANONICAL RECOGNITION EVENT → ONE ACCOUNTING EFFECT PATH.`

The invariant is unenforceable without an addressable event. If the event has no identity, "one" cannot be counted, "canonical" cannot be designated, and "one path" cannot be checked. Every duplicate and lost-recognition path the parent package constructed is a consequence of a missing subject, not of a missing rule.

## 2. What Each Mechanism Anchors To

Eight mechanisms are in the declared floor. Their anchors differ, and this is the crux:

| Mechanism | The economic fact | What the event would anchor to | Anchor exists today? |
|-----------|-------------------|-------------------------------|----------------------|
| Deferral, on validation | An already-invoiced amount earned over a window | A slice of a source document line | **Partly** — a live move-level anchor is set on every generated entry. Absent: line-level anchoring and the period **start** |
| Deferral, grouped | The same fact, aggregated | A set of source documents | **Partly** — the anchor **set** is accumulated, stored on the entry, and written as the full cross-product against both generated entries |
| Accrual | An estimate of what is not yet invoiced | The wizard invocation | No — the object is transient and the back-link is dead code |
| Asset depreciation | Consumption of a carrying amount | A period of an asset's life | **Yes — asset *and* period.** The entry carries a populated, consumed period-beginning date alongside the asset link |
| Loan amortisation | A contractual instalment | A schedule line | **Yes — the only one** |
| Recurring entries | Repetition of a whole entry | The origin entry | Partly |
| Periodic transfer | A balance moved on a frequency | The transfer model | Partly |
| Automatic period reallocation | A posted amount reallocated | Counterpart lines | No |

> **CORRECTED — `34` `W-06`, `W-07`, `W-08`, `W-09`.** As first written this table said three of eight had no anchor (its own cells said four), reduced the asset anchor to the object alone, and denied the deferral anchors outright. Three of the four cells P10 re-verified against source came back different. Anchoring is **graduated, not binary**.

**Corrected reading.** Anchor grades present today: **line-level** (loan) · **object-plus-period** (depreciation) · **move-set level** (both deferral paths) · **none** (accrual). Of the four mechanisms re-verified, **only the accrual has no anchor at all**.

This materially weakens P10's own urgency argument: retrofitting an identity by reference looks **more** available than P10 claimed, not less. The remaining rows — recurring entries, periodic transfer, automatic period reallocation — are **class `C`, not searched**, and their cells must not be read as confirmed.

## 3. The Candidate Identity, Tested

The identity proposed under adversarial challenge in the parent round was:

`(anchor reference, period start, period end, policy)`

Tested against the eight anchors above:

| Test | Result |
|------|--------|
| Does it accommodate a contractual instalment? | Yes — anchor is the schedule line |
| A period of an asset's life? | Yes — anchor is the asset, period is the board period |
| A slice of an invoice line? | Yes — anchor is the line |
| A point-in-time estimate with no period? | **Only degenerately**, as a period of length zero or one. This is the over-generalisation the Boss's second ruling warns against, and it should be rejected rather than accommodated |
| An aggregation of many source documents into one entry? | **YES — P10's claim here was CONTRADICTED, `34` `W-09`.** The grouped path already carries the anchor set. The disjunction P10 posed as a design requirement — *the aggregation must carry the set of anchors* — is **already satisfied by the code P10 cited as destroying it**. What aggregation actually loses is **per-line amount attribution within the aggregate**, which is a weaker and different claim |
| Does it survive inter-company recharge? | **Unknown.** Not tested. Class `D` |

Result: the candidate identity is **sound for the four schedule-shaped mechanisms and unsound for the two aggregate or point-in-time ones**. That is a real finding: it says a recognition-event identity should not be forced to cover the accrual, and it says the grouped aggregation is not merely a different journal shape — it is **identity-destroying**.

## 4. Whose Object Is It — the reconciliation result

`P08` reports that no accounting-event object exists anywhere in the 22 declared roots. **P10 did not re-derive that claim, and P10's own intake rule (`23` `IN-14`, `RF-01`) says a peer class-`A` claim outside the three the peer re-ran must be read as class `C`. P10 stated that rule and then failed to apply it to the one claim that moves this design** (`34` `W-16`).

**Partial repair, executed by P10:** a search of the **declared reference root** for any accounting-event model returns **none**, against a positive control of 216 hits for the sibling pattern. Class `A` within one root.

> **CORRECTED AGAIN — `34` `W-36`. P10's downgrade of the peer's claim was itself wrong.**
>
> P10 wrote that the peer's 22-root claim *"remains class `C`"*. The peer's own root-set declaration records `RS-A-01` — *no accounting-event model exists* — as **`A VERIFIED ABSENCE, scope = the declared 22-root set`**, and lists it as **one of the three claims legitimately promoted after re-running across all 22 roots**, two of the three independently reproduced by a reviewer.
>
> **P10 applied its own intake rule and got the membership wrong**, downgrading a peer's properly-earned class `A`. The peer's claim stands at class `A` over 22 roots. P10's root-scoped search corroborates it; it does not bound it.
>
> **This error occurred inside the decision-authority step added to prevent exactly this class of error, in that step's first application.** A protocol executed by its author is still self-review. `P09` holds an AAS+ veto blocking implementation while the accounting-event identity is undefined. `P11` has already named it as Boss decision `D-5`.

Three processes and P10 are blocked on **one undefined object**.

**P10's position, changed by this reconciliation:**

> P10 **withdraws** its proposal to author a recognition-event identity as element 1 of a P10 kernel. The accounting-event object belongs to `P08`. P10 specialises it into a recognition event by adding a period and an allocation policy, and contributes the anchor taxonomy in §2 and the tests in §3 to Boss decision `D-5`.

If P10 authored its own, the programme would hold **two event identities for one economic fact** — the exact failure the invariant forbids, committed by the process enforcing it. This is the single most important correction the cross-process round produced to P10's own design.

## 5. What P10 Contributes to `D-5`

1. The anchor taxonomy (§2), which any accounting-event identity must satisfy.
2. The corrected finding that anchoring is **graduated** — line-level, object-plus-period, move-set, or absent — and that of the four mechanisms verified, **only the accrual has none**. Retrofitting by reference is therefore partly available.
3. ~~That aggregation destroys identity~~ — **WITHDRAWN, `34` `W-09`.** The corrected contribution is narrower: aggregation preserves the anchor set and loses **per-line amount attribution**.
4. The requirement that the event carry its **period** independently of the posting date — see `28`.
5. The warning that a point-in-time estimate should be **excluded** from the recognition-event abstraction rather than modelled as a degenerate schedule.

## 6. Classification

| Statement | Class |
|-----------|-------|
| The eight anchors and their presence or absence | `VERIFIED FACT`, bounded to the declared reference root |
| ~~That aggregation destroys the per-fact anchor~~ | **`E — CONTRADICTED`.** It was self-certified `VERIFIED FACT` and the cited construction refutes it. This is the negative-claim standard's own failure mode, committed in a contribution to a Boss decision |
| That the candidate identity is unsound for point-in-time estimates | `INFERENCE` |
| Behaviour under inter-company recharge | `D — UNKNOWN`, not searched |
| That the object belongs to `P08` | `RECOMMENDATION`, routed to `D-5`. **P10 does not decide it** |
