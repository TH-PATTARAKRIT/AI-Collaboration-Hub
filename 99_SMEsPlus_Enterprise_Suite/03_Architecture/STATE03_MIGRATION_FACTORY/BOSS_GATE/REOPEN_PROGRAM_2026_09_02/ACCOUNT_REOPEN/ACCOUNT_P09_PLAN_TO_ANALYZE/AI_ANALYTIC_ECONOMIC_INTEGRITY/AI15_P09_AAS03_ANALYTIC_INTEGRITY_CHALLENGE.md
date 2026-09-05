# AI15 — P09_AAS03_ANALYTIC_INTEGRITY_CHALLENGE

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · continuation `…ANALYTIC-ECONOMIC-INTEGRITY-001`
**Layer:** 1 — clean-room. Full challenge records with citations are in the Layer 2 quarantine.

Four AAS-03 experts challenged the continuation with disjoint assignments. **One was tasked to DISPROVE the central hypothesis outright**, as the directive requires.

---

## 1. THE HEADLINE — THE DISPROVER SUCCEEDED, PARTLY

**Verdict returned: `CONTRADICTED` — as stated, with its "unconditionally" quantifier and its mechanism list.**

The **conditional core survives**: when one allocation is applied to every row of a balanced set, the records mirror and the net is zero. That is `CONFIRMED WITH CAVEAT`.

**What failed was the author's move from the conditional to the mechanism list.** Two of the named mechanisms **do not satisfy the antecedent at all**, and a third satisfies it only when a precondition holds. The package asserted the consequent for all of them.

**This is the most valuable single result of the continuation**, and it was produced by a reviewer instructed to attack, not by the author. `AI02` §3.1 and `AI07` §3A are corrected accordingly.

## 2. WHAT THE DISPROVER CONFIRMED

| Attack vector | Result |
|---|---|
| is the row balance stale or unsettled when records are created? | **CONFIRMED the premise** — the balance is the *written* value on every one of the five construction paths, not a derived one. No staleness window |
| can zero-suppression drop one record of a pair but not the other? | **CONFIRMED no asymmetry** — both rows carry the same currency at every construction site examined |
| is there any account-type, journal-type or move-type filter on the creation path? | **CONFIRMED none at row level** |
| for the cash-basis pair, do both legs really share one account? | **CONFIRMED**, and it survived a deliberate attempt to break it: the merge that aggregates base rows includes the allocation in its grouping key, so rows with different allocations are never merged |
| does the analytic balance include both records? | **CONFIRMED** — the pair nets to zero |

## 3. WHAT THE DISPROVER OVERTURNED

| ID | The overturned claim | The correction |
|---|---|---|
| **CH-D1** | the change-account transfer is a symmetric both-legs case | **it is not.** The counterpart's allocation is **re-derived from money amounts**, not copied. It fails by **residue**, not by cancellation |
| **CH-D2** | accrued orders is a symmetric both-legs case | **it is not** — and it is not a two-row pair at all: N source rows against **one** re-derived counterpart |
| **CH-D3** | depreciation zeroing is unconditional | **it is conditional on the asset carrying an allocation.** Without one, each row derives its own by **account prefix**, and the shipped rule mechanism selects on prefixes that match the expense account and not the balance-sheet account — giving a **one-sided, non-zero** attribution |

## 4. NEW DEFECTS THE DISPROVER FOUND THAT THE AUTHOR DID NOT

Six, all class **A** unless stated. Each is a finding in its own right.

| ID | Finding | Why it matters |
|---|---|---|
| **CH-N1** | **A pair can be broken asymmetrically.** Writing the allocation on **one** row of a posted pair destroys and re-creates **that row's** records only; the other row keeps its originals. The result is a one-sided attribution left behind by an ordinary edit | the defect is not only "creates a zero"; it can also **stop** being a zero, silently |
| **CH-N2** | **The stored allocation can silently diverge from the records already created.** The allocation field is a stored compute depending on account, partner and product. A recompute writes the field **without** firing the inverse that maintains the records — and posting writes the partner onto invoice rows **after** the records have been created | the ledger's stated allocation and its actual attribution can disagree with nothing to detect it |
| **CH-N3** | **The zero-suppression test is in the wrong unit.** The amount is derived in **company** currency; the "is this zero" test uses the **row's** currency, which may be foreign | a small foreign-currency allocation can be suppressed or kept on the wrong threshold |
| **CH-N4** | **The posting call does not cover every row set it appears to.** Future-dated moves are removed before the call under soft posting — a **move-level** filter the author's stated fact elided | corrects a stated fact |
| **CH-N5** | **Sub-plan accounting mismatch.** The 100 %-completion counter accumulates against the **root** plan while the value is written to the **specific** plan's column, and the balance computation groups by the specific plan. Two accounts in different sub-plans of one root share a completion accumulator but land in different columns | structural; can misapply the remainder branch |
| **CH-N6** | **The author's sweep denominator missed an override.** The record-preparation method is **overridden** in the sales module — a site the author's pattern could not select, because it does not write the allocation key into a values dictionary | **this is exactly the declared false-negative mode `SW-U-01`, and it materialised** |

## 5. THE DENOMINATOR LESSON, AGAIN

`CH-N6` is the fourth time in this programme that a declared false-negative mode has turned out to be **populated rather than theoretical**. The author declared the blind spot correctly in `AI07` §1 and did not search it; a reviewer did, and found an override in it.

**Declaring a blind spot is not the same as bounding it.** The declaration earns the right to say "class C"; it does not earn the right to assume the class is empty.

## 6. WHAT THE DISPROVER SAYS WOULD STILL SETTLE IT

Four database questions, all read-only, all answerable without a write:

1. does any allocation-rule row carry an account prefix that matches the depreciation-**expense** account code but not the accumulated-depreciation code? If none, `CH-D3` is unreachable in that install.
2. is any analytic plan marked **mandatory**? If none, the obligation check never fires anywhere.
3. does any stored allocation have values summing to ≠ 100 at two decimals? — direct evidence of the residue mode.
4. **group the management records by (entry, plan column) over two-row entries and look for non-zero sums** — the direct observable the hypothesis predicts is always zero.

**Item 4 is the single cheapest decisive test in this whole continuation.** It is recorded as `DEP-P09-18`.

`AI05` establishes that no located deployment contains the rows any of these four would need. They remain **`HOLD — DATABASE EVIDENCE REQUIRED`**.

## 7. CONTROL DEGRADATION — RECORDED, NOT GLOSSED

One evidence strand (the event sweep) failed on a model rate limit and was **author-executed**. Two of the four challenges were tasked to attack it in compensation. **The disprover found two mis-classifications and one populated blind spot in exactly that strand** — which is precisely what the independence control exists to catch, and confirms that the compensation was necessary rather than ceremonial.

## 8. STATUS OF THE REMAINING THREE CHALLENGES

Three further AAS-03 challenges — functional design, code & UI with integration, and cross-process integration — were commissioned with disjoint assignments and were still running when this record was first written. **Their results are appended in §9 as they return; any finding of theirs that corrects the package is applied at the point of correction, not summarised here.**

## CHECKPOINT

**CP-AI15(a) — DISPROVAL CHALLENGE COMPLETE.** Central hypothesis `CONTRADICTED as stated`, conditional core `CONFIRMED WITH CAVEAT`, three claims overturned, six new defects, one declared blind spot found populated. Auto-continue.
