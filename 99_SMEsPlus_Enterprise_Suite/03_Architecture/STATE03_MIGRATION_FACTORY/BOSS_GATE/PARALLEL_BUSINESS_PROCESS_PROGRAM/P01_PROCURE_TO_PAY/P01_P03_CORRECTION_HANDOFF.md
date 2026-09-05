# P01 → P03 — DELTA CORRECTION HANDOFF

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Layer: **1.**
**This is a DELTA. It does not replace or overwrite any prior P01 handoff.**

---

## 1. WHAT P03 ASKED

P03's `OWN-03` records a contested boundary and — correctly and carefully — **asserts nothing
about it**:

> The manufacturing order's extra cost is set from *the receipt's price, not the vendor bill's*.
> For a standard-costed product a later bill difference routes to the price-difference account.
> For a FIFO or average-costed product the cost was already capitalised at the receipt price,
> and **what happens to a later bill difference is a P2P question, not visible from the P03
> side.** P03 asks P01 to state the answer. Recorded as P03's `DEP-06`.

P03 explicitly declined to supply itself an answer key. **P01 respects that boundary and answers
only the part that is P01 evidence.**

---

## 2. THE CORRECTION

> **P03's premise is correct for application series 18 and does not hold for series 19.**

| Series | How the subcontract extra cost is derived |
|---|---|
| **18** | from the **receipt's** price unit — exactly as P03 states |
| **19** | from the **vendor bill first**: the value is taken from the bill for the billed quantity, then from the purchase order for the unbilled remainder, and the receipt price is used **only as a fallback when both yield nothing** |

Classification: **FACT VERIFIED**, symmetric source comparison of the same file in both series,
re-derived by this session after an independent expert raised it.

---

## 3. WHAT THIS MEANS FOR P03's QUESTION

P03 asked what happens to a **later bill difference** for a FIFO or average-costed subcontracted
product.

> **In series 19 the question largely dissolves, because there is no "later" difference: the
> bill is the primary source of the cost, not a correction to it.** The receipt price is a
> fallback, not the basis.
>
> **In series 18 the question stands exactly as P03 framed it.**

**P01 states this as source behaviour. P01 does not define P03's cost architecture**, and does
not answer whether the series-19 model is the one SMEsPlus should adopt — that is a design
decision and belongs to P03, P11 and Boss.

---

## 4. THE DEPLOYMENT QUALIFICATION P03 MUST CARRY

This correction is **source-only**, and P03 should not treat it as observed behaviour:

| Fact | Status |
|---|---|
| Subcontracting installed | in **one** of three deployments in the estate — the one with 453 modules and **10 journal entries in total** |
| Subcontract transactions observed | **zero** — under independent disproof challenge in this round |
| Deployment with real accounting history | is application series **16**, where subcontracting is **not** installed |
| Series-16 source | **never read by P01** — no series-16 root is in P01's declared path set |

So neither the series-18 nor the series-19 behaviour above has been observed running anywhere.

---

## 5. A SECOND ITEM P03 SHOULD KNOW

P01 previously reported a subcontract **receipt credit-split** construct — the credit divided
into a component-cost line and a subcontracting-service-cost line, with the source's own comment
warning the service figure may not be the real cost. Status: **FACT VERIFIED for series 18**,
**CONTRADICTED for series 19** — the construct is gone there.

If P03's cost model assumes that split, it assumes a series-18 behaviour.

---

## 6. WHAT P01 IS NOT DOING

- Not answering P03's `DEP-06` for series 18 — the FIFO/average bill-difference path in that
  series remains **UNRESOLVED — EVIDENCE REQUIRED**, and P01 has no deployment to test it in.
- Not defining P03 architecture, ownership or cost model.
- Not closing P03's `DEP-06`. Only P03 can close it, and P11 reconciles.

## 7. STATUS

| Item | Status |
|---|---|
| Correction issued | **YES — delta only** |
| P03's `OWN-03` premise | **corrected for series 19; stands for series 18** |
| P03's `DEP-06` | **remains open**; P01 has answered the series-19 half from source |
| P01 authority boundary | **respected — P03 not overruled, P03 architecture not defined** |
