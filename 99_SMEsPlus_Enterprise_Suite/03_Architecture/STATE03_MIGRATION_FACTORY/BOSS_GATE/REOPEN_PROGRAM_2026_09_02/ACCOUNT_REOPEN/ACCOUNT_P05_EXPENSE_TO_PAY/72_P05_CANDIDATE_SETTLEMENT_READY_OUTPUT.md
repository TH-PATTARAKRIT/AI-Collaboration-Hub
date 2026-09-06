# 72 — P05 CANDIDATE SETTLEMENT-READY OUTPUT

`LAYER 2 — AUDIT QUARANTINE` · `CQ-P05-07` · **PHASE S CANDIDATE — NOT A FINAL CONTRACT**

## 1. Definition

> **Settlement-ready** = P05 has completed everything it owns, such that a settlement process can pay
> the obligation **without re-deriving any P05 truth**.

P05 stops here. **Payment execution, clearing and bank matching are P06's and were not researched.**

## 2. Candidate Output Contract — `CO-01`

| # | Element | Meaning | P05 owns it? | Evidence |
|---|---|---|---|---|
| 1 | **Payable identity** | a stable reference that survives correction | **NO — DEFECT** | four paths sever the claim↔obligation link; line-level reference is null throughout the examined population |
| 2 | **Amount** | what is owed | yes | FACT VERIFIED |
| 3 | **Currency** | denomination, and the rate basis if converted | yes, **weakly** | the effective rate may be one implied by two user-entered numbers rather than a rate table |
| 4 | **Counterparty identity** | who is owed | yes | FACT VERIFIED |
| 5 | **Counterparty character** | employee vs supplier — a *semantic* distinction | **NO — DEFECT** | both resolve to the same payable account; carried only by which partner is named. On the business-funded route the counterparty is **optional** while the settlement asserts a supplier relationship |
| 6 | **Company** | which legal entity owes it | yes | FACT VERIFIED |
| 7 | **Authorisation state** | that it may be paid | yes, **weakly** | the marker is writable without passing the control |
| 8 | **Due / payment metadata** | when, and by what instrument | partial | on the business-funded route the maturity date falls to *today* while the entry date is the cost date |
| 9 | **Correction lineage** | what this supersedes | **NO — DEFECT** | no correction event is published |
| 10 | **Tax withholding attributes** | what must be withheld at settlement | yes | FACT VERIFIED; reachable only on the reimbursement route |

**Four of ten elements are defective or absent in the reference.**

## 3. Preconditions

| Precondition | Present? |
|---|---|
| Obligation authorised | yes, but the marker is unguarded |
| Amount non-zero | yes |
| Counterparty identified | **only on the reimbursement route** |
| Company consistent across claim lines | yes |
| Period open for the recording date | enforced at posting, not at derivation |
| Evidence attached | **not required** |
| Not already settled | derived from the artefacts; on the business-funded route settlement is **asserted** as soon as any artefact is non-draft, before any bank movement |

> **`SRO-01` FACT VERIFIED — P05.** On the business-funded route P05 declares an obligation settled
> **before any money moves**. A settlement consumer that trusts P05's settled flag on that route is
> trusting an assumption, not an observation.

## 4. Candidate Requirements for SMEsPlus

| ID | Requirement |
|---|---|
| `SRR-01` | A payable carries an **immutable identity** that no later action can sever. |
| `SRR-02` | **Counterparty character is a typed attribute**, not an inference from which partner is named. |
| `SRR-03` | A payable **cannot exist without an identified counterparty.** |
| `SRR-04` | *Settled* is an **observation of a settlement event**, never an assumption from a document state. |
| `SRR-05` | Authorisation is a **transition guarded server-side**, not a writable marker. |
| `SRR-06` | Every settlement-ready payable carries its **correction lineage**. |
| `SRR-07` | The **rate basis** for a converted amount is explicit and auditable. |

## 5. Boundary

P05 does not define: payment instruments, batching, bank file formats, clearing, matching,
partial-payment allocation policy, or reconciliation. **Those are P06's and were not researched.**
