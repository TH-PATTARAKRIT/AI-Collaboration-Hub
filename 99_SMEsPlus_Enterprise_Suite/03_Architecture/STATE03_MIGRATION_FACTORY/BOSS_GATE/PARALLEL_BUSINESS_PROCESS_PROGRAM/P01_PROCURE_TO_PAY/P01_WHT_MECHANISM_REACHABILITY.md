# P01 — WHT MECHANISM REACHABILITY

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Layer: **1.**
**Kept deliberately separate from `P01_WHT_PARTIAL_PAYMENT_V2.md`.** These are two different
findings about two different things, and the directive is explicit that they must not be
conflated.

---

## 1. WHICH MECHANISM THIS DOCUMENT IS ABOUT

| | |
|---|---|
| **Finding ID** | `CONTRA-P01-09`, raised in round 2 and withdrawn in round 3 |
| **The asserted mechanism** | An offset term intended to net previously-withheld amounts, computed as `debit − credit` over prior payments' withholding lines. Asserted to be sign-inverted, so each partial payment **increased** the amount withheld — geometric compounding |
| **This is NOT** | the separate, surviving finding that withholding is computed on the full bill base and repeated per partial payment. That is `REPEATED FULL-BASE WITHHOLDING`, and it is verified |

---

## 2. CLASSIFICATION

> ### `VERSION-INAPPLICABLE` — for the deployment that matters
>
> and **`CONTRADICTED`** as a live defect anywhere in this estate.

---

## 3. WHY IT CANNOT FIRE — THREE INDEPENDENT REASONS

| # | Reason | Evidence class |
|---|---|---|
| 1 | **The term does not exist in the deployed series-16 code.** The payment-register extension there is 69 lines, read in full: no loop over prior payments, no debit-minus-credit expression | **DEPLOYED-SOURCE VERIFIED** — the source root was located this round and its version matches the deployment exactly |
| 2 | **Where the term does exist (later-series copies), it is inert.** Its filter selects every line of the payment's journal entry, and a journal entry balances, so the expression evaluates to **0.00 in 4,943 of 4,945 deployed payments** | **DEPLOYMENT VERIFIED** (expert, prior round) |
| 3 | **The later-series copy has never executed.** Zero of seven payments in the series-19 estate carry a withholding tax | **DEPLOYMENT VERIFIED** (expert, prior round) |

---

## 4. THE REQUIRED FACETS

| Facet | Value |
|---|---|
| **Required module** | the Thai withholding-tax custom module |
| **Required version** | the later-series copies — the term is absent from the series-16 copy |
| **Required configuration** | withholding tax on bill lines, and prior partial payments carrying a withholding line |
| **Actual deployment — series 16** | module installed, **term absent from the code** |
| **Actual deployment — series 19 estate** | module installed, term present, **inert**, and **never exercised** |
| **Why it cannot fire** | absent where the accounting happened; inert and unexercised where present |

---

## 5. WHAT REMAINS TRUE AND WHAT DOES NOT

| Statement | Status |
|---|---|
| *"Withholding compounds geometrically across partial payments"* | **CONTRADICTED — withdrawn.** Preserved in the revision log with its original evidence |
| *"An offset term exists whose sign is wrong"* | **True of the later-series copies only, and the term is inert there** |
| *"Withholding is over-applied on partial payments"* | **TRUE — but by a different mechanism**: full-base repetition, linear. See the v2 arithmetic document |
| *"The defect is live"* | **The compounding defect is not live anywhere.** The full-base defect **is** present in the deployed series-16 code |

---

## 6. THE METHOD POINT

This is the clearest instance in P01 of a distinction the programme now enforces:

> **A defect claim has two separable parts — that the code is wrong, and that the wrong code
> runs. Each needs its own evidence.**

Round 2 established neither properly: it read one line, inferred a sign, and did not evaluate
what the filter selected or check which copy was deployed. Round 3 disproved the mechanism.
**This round located the deployed source and found the term is not there at all** — which is a
stronger disproof than the inertness argument, because it does not depend on runtime data.

Meanwhile the **real** defect survived all three rounds and is now verified in deployed source.
The withdrawn claim and the surviving one were never the same finding; conflating them would
have retired a live defect along with a dead one.

---

## 7. STATUS

| Item | Status |
|---|---|
| Compounding mechanism | **`VERSION-INAPPLICABLE` / `CONTRADICTED`** |
| Live anywhere in this estate | **No** |
| Retained as | source-level learning about a sign convention, and a method lesson |
| Confused with the surviving defect? | **No — kept separate by instruction, and the separation is load-bearing** |
