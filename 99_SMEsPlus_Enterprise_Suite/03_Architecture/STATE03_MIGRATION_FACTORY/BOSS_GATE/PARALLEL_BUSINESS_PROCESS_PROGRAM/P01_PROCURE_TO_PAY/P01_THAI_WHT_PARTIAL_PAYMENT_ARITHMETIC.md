# P01 — THAI WHT PARTIAL-PAYMENT ARITHMETIC

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.**
**Statutory position: no claim about Thai law is made anywhere in this file.** Every statement
is about source behaviour or deployed data. Statutory determination belongs to **P07**.

---

## 1. FINAL CLASSIFICATION

> ### `CONTRADICTED` (as previously stated) — and `DEPLOYMENT-DEPENDENT`
>
> The previous round's finding — *"withholding **compounds** across partial vendor payments"* —
> **does not survive independent disproof.** The mechanism it described cannot fire.
>
> **A different, real defect was found in its place: withholding is applied at the FULL bill
> amount on every partial payment, because it is never prorated.**

---

## 2. WHY THE COMPOUNDING CLAIM FAILS

The previous finding rested on the offset term
`amount_wt -= sum(debit) − sum(credit)` over prior payments' withholding lines, reasoning that
on a vendor payment the withholding line is a credit, so the term is negative and the
subtraction *increases* the amount.

**The sign premise is correct.** On a vendor payment the withholding write-off is a credit —
4,944 of 4,951 such lines in live data.

**The selection premise is not.** Verified directly:

| Step | Evidence |
|---|---|
| The payment-line link is `related='move_id.origin_payment_id'` — so **every line of the payment's journal entry** carries it, not only the withholding line | core source, verified |
| The withholding-tax compute has an `elif <payment link>:` branch that stamps the tax on **every** such line | custom source, verified |
| The wizard's filter therefore selects **all** lines of the payment entry | follows from the two above |
| A journal entry balances, so `sum(debit) − sum(credit)` over all its lines is **0.00** | arithmetic |

**The offset is inert.** It neither nets nor compounds. Confirmed against deployed data by the
independent expert: exactly **0.00 in 4,943 of 4,945** deployed payments.

Classification: **FACT VERIFIED**. The previous finding is **withdrawn** — `ERR-P01-12`.

---

## 3. THE DEFECT THAT IS ACTUALLY THERE

The withheld amount is computed as the **whole bill's** withholding and is **never prorated to
the amount being paid**.

### Worked arithmetic — 100,000 bill at 3%, expected total withholding 3,000

| Case | Payment | Expected | Actual | Cumulative actual | Error |
|---|---|---|---|---|---|
| **Control — single full payment** | 100,000 | 3,000 | 3,000 | 3,000 | **none** — the control behaves correctly, exactly as the disproof predicted |
| Two equal halves | 50,000 | 1,500 | **3,000** | 3,000 | +1,500 |
| | 50,000 | 1,500 | **3,000** | **6,000** | **+3,000 total — 200% of the liability** |
| Three unequal parts | 50,000 | 1,500 | 3,000 | 3,000 | |
| | 30,000 | 900 | 3,000 | 6,000 | |
| | 20,000 | 600 | 3,000 | **9,000** | **+6,000 — 300%** |

The error is **linear in the number of partial payments**, not geometric.

> **For comparison, under the shape the previous round assumed, three partials would have given
> 3,000 / 6,000 / 12,000 = 21,000 — worse than what actually happens.** The withdrawn claim
> over-stated the magnitude as well as mis-describing the mechanism. That shape occurs in
> **1 of 4,945** deployed payments.

Classification: **FACT VERIFIED** for the source arithmetic. Whether an operator overrides the
figure before confirming is **`HOLD — RUNTIME EVIDENCE REQUIRED`**.

---

## 4. THE SCOPE CORRECTION THAT MATTERS MOST

> **No readable deployed database runs the code this finding was derived from.**

| Fact | Evidence |
|---|---|
| The v16 deployment runs withholding module version `16.0.1.0.1`, which matches **no copy in P01's declared path set** | module registry |
| That deployed v16 wizard, read in full, **has no offset loop at all** — the disputed mechanism does not exist where the money actually moved | source, 69 lines |
| The v19-line copy **has never executed**: 0 of 7 payments in the two v19 databases carry a withholding tax | deployed data |

So the arithmetic in §3 is a statement about **source code in the declared path set**, and that
code is **not demonstrably running anywhere in this estate**. Class **B** for any deployment
claim. `ERR-P01-13`.

---

## 5. WHAT THIS MEANS FOR THE TARGET DESIGN

Stated as learning; P01 makes no target-architecture decision.

1. **A withholding amount must be prorated to the payment it accompanies**, or explicitly
   declared as withheld-in-full-on-first-payment with the remainder suppressed.
2. **A control that computes an offset must be tested against the case where it evaluates to
   zero.** Here an offset loop exists, looks correct, and is inert — because its filter selects
   a balanced set. It would pass any review that read it without asking what the filter returns.
3. The single-full-payment control case works. **A defect that only appears on partial payments
   will not be found by testing the normal path.**

---

## 6. OPEN

| ID | Item | Status |
|---|---|---|
| `WHT-01` | Whether an operator overrides the amount in practice | `HOLD — RUNTIME EVIDENCE REQUIRED` |
| `WHT-02` | Which withholding code each deployment actually runs — none matches the declared path set | `HOLD — SOURCE EVIDENCE REQUIRED`; a root outside the declared path set must be located |
| `WHT-03` | Whether any of this is lawful or compliant | **`HOLD — STATUTORY EVIDENCE REQUIRED` — routed to P07. P01 does not decide it** |
| `WHT-04` | A **third** withholding engine exists and is latent in v19 | intake from the expert; not re-derived |
