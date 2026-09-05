# P01 — THAI WHT PARTIAL-PAYMENT ARITHMETIC v2

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Layer: **1.**
**No statutory claim is made anywhere in this file. Every statement is source or deployment
behaviour. Statutory determination belongs to P07.**

---

## 1. CLASSIFICATION

> ### `REPEATED FULL-BASE WITHHOLDING`
>
> and, of the permitted values, **also `LINEAR DUPLICATION`** — the two describe the same
> behaviour, the first naming its cause and the second its effect.
>
> **Not** `CORRECT NETTING`. **Not** `PAYMENT-PROPORTIONAL`. **Not** `CONFIGURATION-DEPENDENT`.
> **Not** `CONTRADICTED`.

**And, new in this round: it is now verified in the code that the only deployment with real
accounting history actually runs.**

---

## 2. THE EVIDENCE-BASE ADVANCE THAT MAKES THIS POSSIBLE

The prior round could only say this: *"the deployed withholding module version matches no copy
in the declared path set — no deployment demonstrably runs this code."*

**That gap is now closed.** A custom source root for application series 16 exists on the volume,
was never in P01's declared path set, and has now been searched. Its module versions match the
series-16 deployment's registry:

| Module | Source manifest | Deployed registry | Match |
|---|---|---|---|
| withholding tax | `16.0.1.0.1` | `16.0.1.0.1` | **exact** |
| withholding certificate form | `16.0.1.0.1` | `16.0.1.0.1` | **exact** |
| withholding certificate | `14.0.1.0.0` | `16.0.14.0.1.0.0` | match — the framework prefixes the series |
| withholding report | `1.0.0` | `16.0.1.0.0` | match — same prefixing |
| purchase request | `1.0` | `16.0.1.0` | match |
| data-removal module | `16.0.1.0.1` | `16.0.1.0.1` | **exact** |

> **Six of six match. This root is the source of the deployed series-16 custom layer.**

Classification: **FACT VERIFIED.** This closes the prior round's `WHT-02` / `W2-01`.

---

## 3. THE MECHANISM, READ IN THE DEPLOYED CODE

The payment-register extension in the deployed series-16 module is **69 lines and was read in
full**. The withholding amount is computed as:

> **the sum, over the bill's withholding-bearing lines, of `(rate ÷ 100) × line subtotal`** —
> and then subtracted from whatever payment amount is being registered.

**The computation refers to the bill line's own subtotal. It contains no reference to the
payment amount at all.**

Classification: **FACT VERIFIED**, deployed source, read in full.

---

## 4. THE RECALCULATION REQUIRED BY THE DIRECTIVE

Bill 100,000 · withholding rate 3% · correct total withholding 3,000.

| Step | Value |
|---|---|
| Invoice base | 100,000 |
| WHT base | 100,000 — **the full line subtotal, in every calculation** |
| **Payment 1** | 50,000 |
| Withholding 1 | **3,000** (3% × 100,000) — *correct amount would be 1,500* |
| Remaining base | **unchanged at 100,000** — nothing reduces it |
| **Payment 2** | 50,000 |
| Withholding 2 | **3,000** again |
| **Cumulative WHT** | **6,000 against a 3,000 liability — 200%** |
| Certificate amount | per certificate, the amount recorded at that payment — so **two certificates of 3,000 each** |

Three unequal partials of 50,000 / 30,000 / 20,000 → **3,000 + 3,000 + 3,000 = 9,000, 300%.**

**Control case — a single full payment of 100,000 → 3,000. Correct.**

> The error is **linear in the number of partial payments**: `n × full-bill withholding`.

---

## 5. WHAT THE PRIOR, WITHDRAWN CLAIM SAID — PRESERVED

The round-2 claim was **compounding**: an offset term of `debit − credit` over prior withholding
lines, negative on a vendor payment, so each payment *increased* the amount — 3,000 then 6,000
then 12,000.

That claim was **contradicted** in round 3: the term selects a balanced journal entry and
evaluates to 0.00 in 4,943 of 4,945 deployed payments.

**This round adds the decisive fact:** the deployed series-16 wizard **has no such offset term at
all** — no loop over prior payments, no debit-minus-credit expression, nothing. The disputed
mechanism does not merely fail to fire; **it is not present in the code that processed the
accounting.**

Both the original claim and its withdrawal are preserved in the revision log
(`ERR-P01-12`, `ERR-P01-13`).

---

## 6. A CONTROL AND A HAZARD FOUND WHILE READING

| Item | Finding |
|---|---|
| **A real control** | Registering one payment against **multiple bills** is refused when any line carries withholding. A genuine, executing guard |
| **A hazard** | The subtraction that mutates the payment amount runs **inside a computed field with declared dependencies**, so it re-executes whenever those dependencies change. A side-effecting compute is a poor place for a monetary adjustment; whether it can double-apply within one registration is **`HOLD — RUNTIME EVIDENCE REQUIRED`** |

---

## 7. SCOPE AND LIMITS

| Item | Status |
|---|---|
| Series-16 deployed source | **located and read in full** |
| Behaviour | **FACT VERIFIED in source** |
| Whether an operator overrides the figure before confirming | **`HOLD — RUNTIME EVIDENCE REQUIRED`** — the amount is editable in the wizard |
| Observed over-withholding in the data | **not measured by this session** — class C |
| Lawfulness or compliance of any of it | **`HOLD — STATUTORY EVIDENCE REQUIRED` — P07 owns it** |
| Later-series copies | the same full-base computation, plus the inert offset term; behaviour classified `DEPLOYMENT-DEPENDENT` |
