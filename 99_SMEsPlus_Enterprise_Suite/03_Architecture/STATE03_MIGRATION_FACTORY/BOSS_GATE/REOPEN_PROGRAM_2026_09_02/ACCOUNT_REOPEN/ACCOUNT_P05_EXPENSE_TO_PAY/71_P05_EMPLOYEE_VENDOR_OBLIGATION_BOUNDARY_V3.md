# 71 — P05 EMPLOYEE vs VENDOR OBLIGATION BOUNDARY V3

`LAYER 2 — AUDIT QUARANTINE` · `CQ-P05-04` · **PHASE S CANDIDATE**

## 1. The Distinction P05 Must Carry

| | Employee obligation | Vendor obligation |
|---|---|---|
| Why it exists | a person spent their own money on the business's behalf | a supplier delivered goods/services |
| Character | **reimbursement** | **trade payable** |
| Origin | an internal actor's out-of-pocket cost | a commercial agreement |
| Evidence | receipt for a cost *already paid by the person* | supplier document for a cost *not yet paid* |
| Ageing meaning | how long a person has been out of pocket | commercial credit consumed |
| Settlement route | payment **or** payroll (`CH-05`) | payment |

## 2. What the Reference Actually Does

| Fact | Class |
|---|---|
| Both resolve to the **same payable account** — the counterparty's payable property | FACT VERIFIED |
| The distinction is carried **only by which counterparty is named** | FACT VERIFIED |
| On the reimbursement route, three different partner-derived values are drawn from **three different fields** of the employee record | FACT VERIFIED |
| On the business-funded route, the counterparty is an **optional, unconstrained field** while the settlement asserts a supplier relationship | FACT VERIFIED |
| Company-consistency of the counterparty is enforced **late** — at accounting-artefact creation, not at capture | FACT VERIFIED |

> **AAS-03 Expert 1 challenged whether a shared payable control account is a defect at all**, and the
> challenge is **accepted in part**: a shared control account distinguished by counterparty is a
> legitimate and common accounting pattern. **The defect is not the shared account.** It is that
> **character is inferred rather than typed** — nothing in the obligation states *"this is a
> reimbursement"* as opposed to *"this is a trade payable"*. Consumers must infer it from partner
> identity, and on one route the partner may be absent entirely.

## 3. Advance / Settlement Relationships

| Relationship | P05 position | Deployment |
|---|---|---|
| Funds advanced against a future cost | should create an **employee receivable**; the reference recognises an **expense** | installed in **none** of eight registries |
| Advance liquidated against actual cost | should clear the receivable | installed nowhere |
| Unused advance returned | should clear the receivable | installed nowhere |
| Float replenishment | creates an obligation to the float holder | **installed and used** on the v18 target |
| Float drawdown | reduces the float | **installed**; no live-posted instance observed |

> The advance semantics are **source-and-design evidence only**. `DUP-03` (an advance-funded cost also
> claimed as an expense) is therefore **vacuous in every evidenced deployment** — there is no advance
> system deployed to double-count against. The design lesson stands; the operational risk does not.

## 4. Candidate Requirements

| ID | Requirement |
|---|---|
| `EVR-01` | **Obligation character is a typed attribute** — reimbursement, trade payable, float replenishment, advance recovery — never inferred from counterparty identity. |
| `EVR-02` | An obligation **cannot exist without an identified counterparty**, on any funding route. |
| `EVR-03` | **An advance creates an asset**, never an expense. |
| `EVR-04` | Employee and supplier balances are **separable without a counterparty-level report**. |
| `EVR-05` | Counterparty company-consistency is enforced **at capture**, not at posting. |

## 5. Boundary

Employee master data, contracts and payroll internals are **not P05's** and were not researched
(`DP-02`). P05 owns the obligation and its character; **who the employee is** is HR's.
