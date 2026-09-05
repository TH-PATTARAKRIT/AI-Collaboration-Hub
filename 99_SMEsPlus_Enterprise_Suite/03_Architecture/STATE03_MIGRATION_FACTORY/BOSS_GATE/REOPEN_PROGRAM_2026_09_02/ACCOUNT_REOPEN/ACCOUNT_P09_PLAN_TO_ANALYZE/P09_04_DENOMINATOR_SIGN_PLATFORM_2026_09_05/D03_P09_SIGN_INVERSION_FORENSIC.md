# D03 — P09_SIGN_INVERSION_FORENSIC

**Checkpoint:** `CP-P09D03` · **Layer:** 1 — clean-room.

---

## 1. THE QUESTION

Why did the published net move from **−2,961,221.81** to **+3,595,851.11**, and what does the sign mean?

## 2. THE ANSWER — NEITHER FIGURE MEASURED THE MECHANISM

| Figure | What it actually was |
|---|---|
| −2,961,221.81 | the difference between two **asset-derived account subsets** |
| +3,595,851.11 | the difference between two **complete account-type populations** |
| **the mechanism's true contribution** | **exactly 0.00**, across 17,404 of 17,405 paired entries |

**The sign did not invert because anything about depreciation changed.** It inverted because the second population included **opening-balance and carry-forward entries** that the first happened to exclude, and those entries carry ±78 M on the balance-sheet side with no depreciation-expense counterpart.

**Both signs were artifacts of population choice. Neither was a property of the accounting.**

## 3. THE CHAIN, TRACED

| Step | Value for one depreciation entry |
|---|---|
| journal row — depreciation expense | debit `X`, balance `+X` |
| journal row — accumulated depreciation | credit `X`, balance `−X` |
| allocation | the asset's own, written to **both** rows |
| management amount = **negated** balance × share | expense leg `−X`; balance-sheet leg `+X` |
| **entry net** | **0.00** |
| ledger effect | correct and undisturbed |

**Verified against 17,404 entries producing exactly 0.00.** The negation is the product's cost/revenue convention; applied to both legs of a balanced pair it cancels, by arithmetic.

## 4. WHICH ASSUMPTION INVERTED THE RESULT

Not an arithmetic error, not a sign-convention error, not an extraction error.

> **The inverting assumption was that a sum over accounts is a sum over events.**

Once the aggregation is done per entry, there is no inversion to explain: the mechanism contributes zero on every entry it touches, and the residue belongs to five entries that are not depreciation postings.

## 5. SIGN-INTEGRITY STATEMENT

| Element | Convention, verified |
|---|---|
| management amount | **negated** journal balance |
| a cost | **negative** in the management ledger |
| a revenue or contra-credit | **positive** |
| the balance surface | credit-minus-debit over signed amounts — a **margin**, not a trial balance |
| a balance-sheet credit leg admitted to that surface | appears as **margin-positive**, and is economically meaningless there |

**Numeric magnitude ≠ economic direction.** The +3.6 M is magnitude with no economic direction attached, because its constituents are not economic events of one kind.

## CHECKPOINT
**`CP-P09D03` — COMPLETE — EVIDENCE VERIFIED.** Auto-continue.
