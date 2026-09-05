# 34 — P05 CROSS-PROCESS OWNERSHIP REGISTER (CONSOLIDATED)

`LAYER 2 — AUDIT QUARANTINE`
Consolidates `09` (ownership boundaries and duplicate attacks) with the deployment reach from `24`
and the routing in `30`. `09` is retained as audit lineage.

## 1. Ownership Boundaries

| Business fact | P05 owns? | Contending process | Reach | Duplicate risk | Routed |
|---|---|---|---|---|---|
| Employee reimbursement liability | **Yes** | P01, if the same cost is also entered as a vendor bill | LIVE | **HIGH** — both produce `in_invoice`; the only discriminator is a link field that four paths sever | P01, P08 |
| Vendor service purchase | **No — P01 owns** | P05 reaches vendor AP through an unconstrained `vendor_id` on a company-paid line | LIVE | MEDIUM | P01 |
| **Vendor advance / down payment** | **No — P01 owns** | `scgl_purchase_advance_payment` | **LIVE, 4 of 4 distinct DBs** | **HIGH — never deducted from the final bill** | **P01, priority** |
| Employee advance | **Yes** | — | LATENT | — | — |
| Petty cash float | **Yes** | P08 cash management | LATENT | MEDIUM | P08 |
| Payment execution | **No — treasury owns** | P05 nevertheless creates **and posts** payments at approval, one per expense line | LIVE | **HIGH** | P06, P08 |
| WHT withholding | **Shared** | P01 and P02 use the same payment-register extension; a **second** subsystem exists in parallel | **LIVE, 4 of 4 distinct DBs** | **HIGH — two systems of record** | **P07, P11** |
| WHT certificate issue | **Shared** | P07 owns statutory form and lifecycle | **LIVE, 4 of 4 distinct DBs** | **MEDIUM — one exact duplicate in 5,201, and no constraint or index prevents more** (corrected, `39 RE-11`) | **P07** |
| Analytic allocation | **Consumes** | P09 owns | LIVE | — | P09 |
| Fiscal lock / period control | **Consumes** | P08 owns | LIVE | — | P08 |
| Journal immutability | **Consumes** | P08 owns | LIVE (core gap) | — | **P08** |
| Chart of accounts, employee master | **Consumes** | core / HR | LIVE | — | — |

## 2. Duplicate Attack Results — reach-adjusted

Mandatory attacks per the directive: double posting, double expense, double AP, double payment,
double tax, double WHT, double reconciliation, double settlement, double analytic cost.

| ID | Duplicate class | Verdict | Reach |
|---|---|---|---|
| `DUP-01` | Same cost claimed twice as two expense lines | **Detected, advisory only.** The approval wizard calls the approve action unconditionally. Duplicates merely *submitted* raise no warning at all. | LIVE |
| `DUP-02` | Same receipt attached to two expenses | **Detected by attachment checksum only.** A re-scanned receipt has a different checksum. | LIVE |
| `DUP-03` | Cost paid by advance **and** claimed as an expense | **NOT DETECTED — structurally.** Class **A**: the advance module and the claim module share no code path at all (`E3-02`). | LATENT |
| `DUP-04` | Same cost as an expense claim **and** a vendor bill | **NOT DETECTED.** Class **A** within the two module scopes. | **LIVE** |
| `DUP-05` | Petty-cash claim **and** an employee reimbursement for the same cost | **NOT DETECTED**, and compounded: the float is never reduced by a claim at all. | LATENT |
| `DUP-06` | One claim producing multiple payments (company branch) | **By design**, one per line — but it breaks the employee branch's own assumption that "only one move is created". | LIVE |
| **`DUP-07`** | **Vendor down payment billed, then the full order billed again** | **NOT DETECTED — the deduction flag has no live consumer.** Class **A** over the custom tree. | **LIVE, 4 of 4 distinct DBs** |
| **`DUP-08`** | **Two WHT subsystems reporting the same withholding** | **NOT RECONCILED.** One derives from `tax_line_id`, the other produces a write-off line with none. | **LIVE, 4 of 5** |
| **`DUP-09`** | **Duplicate withholding certificate for one payment+payee** | **NOT PREVENTED** — the control is a client-side domain the wizard bypasses via context, and the table carries **no UNIQUE constraint and no index** at v16 or v19. **Empirically: one exact duplicate in 5,201** (corrected from an overstated 32 — `39 RE-11`). Multi-certificate payments otherwise follow a one-certificate-per-payee structure. **Whether that structure is permitted is P07's to determine, not P05's** — an earlier draft called it "legitimate" here, which pre-answered a question this package routes to P07. Withdrawn (Challenge D `V-6`, `RE-26`); see `51 §2` item 6. | **LIVE, measured** |

> **`OW-01` (restated).** Every duplicate control found operates **inside one document family**.
> All four undetected classes are **cross-document**. Duplicate control must key on the **cost event**,
> which no single process owns — routed to P11 as `H-P11-1`.
>
> **`OW-02` (new).** The reach data inverts which duplicates matter operationally: `DUP-03` and
> `DUP-05`, which the original package led with, are latent; `DUP-07`, `DUP-08` and `DUP-09` are live
> in the evidenced estate and **all three sit outside P05's ownership** (P01, P07, P07).
>
> **`OW-03`.** `DUP-09`'s magnitude was itself overstated and corrected by review (`39 RE-11`).
> After correction, the ranking of live duplicate exposures is: **`DUP-07`** (vendor down payment
> never deducted — a whole second bill, 4 of 4 distinct databases) > **`DUP-08`** (two WHT systems of record,
> 4 of 5) > **`DUP-04`** (claim vs vendor bill, undetected) > **`DUP-09`** (one instance in 5,201).
> The single most consequential live duplicate exposure in this package is **P01's**.

## 3. Convergence With Peer Processes

Offered as convergence, **not** as adjudication of any peer's canonical architecture.

| P05 finding | Peer counterpart | Convergence |
|---|---|---|
| `SR-07` — the claim↔entry relation cannot be a reconciliation key | Account Wave A: "no event identity" | same root cause, reached from a different surface; a platform primitive is required — `H-P11-2` |
| Accounting date derived from the clock | Account Wave A: "system-derived accounting date" | recurs in a second process and in a custom module |
| FX / currency absent from the custom clearing paths | Boss ruling `GB-08` on FX rate ownership | `GB-08` is **binding** on P05; P05 conforms and does not re-decide |
| Analytic attribution reaches one leg only | P09: "analytic dimension is schema, not data" | consistent from a different surface |

## 4. What P05 Explicitly Does Not Decide

- Whether P01 owns vendor advances (`H-P01-5`).
- P01's authorisation model for advance billing (`SC-02`).
- Any Thai statutory determination (`30 §3`, eight items, all `HOLD — STATUTORY EVIDENCE REQUIRED`).
- Which WHT subsystem is the system of record (P07 statute, P11 reconciliation).
- Core journal immutability policy (`H-P08-1`).
- Cross-process sequencing of remediation (`H-P11-5`).
