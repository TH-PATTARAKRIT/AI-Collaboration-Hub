# P10 — CURRENCY AND AMOUNT SEMANTICS  (`CQ-P10-06`)

**Terminal disposition: `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** for what the mechanisms can express · **`CROSS-PROCESS OWNER — HANDOFF PUBLISHED`** for general FX policy, which is P08's.

---

## 1. What Each Mechanism Can Express

| Mechanism | Foreign currency? | Why |
|---|---|---|
| Deferral, both paths | **NO** | The generated line values carry `account`, `product`, `product category`, `balance`, `name`, `attribution` — and **no currency and no foreign amount**. Spreading is performed on the **company-currency balance** |
| Asset depreciation | **NO** | The asset's currency is a *related* field of the company's, so the "conversion" in its entry preparation is an identity and the currency fields it does set merely restate the company amount |
| Loan amortisation | **NO** | Both the loan header and its schedule line take their currency from the company |
| Accrual | **PARTIALLY** | Foreign amount and currency are set **only** when exactly one order is selected and its currency differs from the company's |

**Three of four cannot express a foreign-currency recognition at all.** For the asset the FX machinery is present and **vestigial** — a reader grepping for the currency fields would answer "yes" and be wrong; the settling evidence is the field definition one level up.

## 2. The Rate and Its Date

For a deferral, the input is the source line's company-currency balance, which was already translated at **the source document's own rate on its own date**. Every monthly slice is a pro-rata slice of that one frozen number.

> **A foreign-currency service contract is recognised across its whole window at the rate in force on the invoice date.** No period-end retranslation, no monetary-item treatment. The behaviour is *internally consistent* — a deliberate freeze — and it removes the ability to express the alternative at all.

## 3. The Accrual's Counterpart Line — two distinct defects

The currency branch tests `exactly one order` **and** `order currency differs from company currency`.

| Case | Result |
|---|---|
| **One** foreign-currency order | The test **passes** for the counterpart, which is stamped with the foreign currency and a **zero foreign amount** against a non-zero company-currency balance |
| **Two or more** orders | The test **fails** for the counterpart, which carries **no currency**, while the product lines carry theirs |

**These are different defects and an earlier P10 evidence item stated them as one. Corrected.**

Either way the foreign amounts do not sum to zero on a move whose currency is the foreign one — **and nothing catches it**: balance validation sums company-currency amounts only. **There is no foreign-currency integrity backstop anywhere in P10's surface.**

## 4. Rounding

| Mechanism | Rounding currency |
|---|---|
| Deferral, validation path | the **source line's** currency |
| Deferral, grouped path | the **active company's** currency |

Two paths for one fact round in two different currencies. Minor in amount, and it is a third instance of the one-fact-two-shapes pattern.

## 5. What Is P08's, Not P10's

General FX policy — which rate, at what date, retranslation of monetary items, the treatment of realised and unrealised differences — is **P08's**. P10 supplies:

- the **fact** that its recognition lines carry no currency dimension;
- the **requirement** that a recognition event record the measurement rate and date alongside its base, so that a later design *can* retranslate even if the reference cannot;
- the **question**: what is the currency model for a programmatic entry that carries no currency of its own?

Handoff published. **P10 does not decide FX policy.**

## 6. Disposition

- Expressive capability of each mechanism: **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`**
- The two accrual counterpart defects: **`CONTRADICTED — CORRECTED AND CLOSED`** (an earlier P10 item conflated them)
- General FX policy: **`CROSS-PROCESS OWNER — HANDOFF PUBLISHED`** (P08)
