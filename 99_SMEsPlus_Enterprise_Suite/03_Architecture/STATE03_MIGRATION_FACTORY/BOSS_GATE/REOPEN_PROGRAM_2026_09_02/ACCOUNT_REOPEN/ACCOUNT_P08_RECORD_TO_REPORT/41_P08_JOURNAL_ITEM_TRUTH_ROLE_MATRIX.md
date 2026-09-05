# P08_JOURNAL_ITEM_TRUTH_ROLE_MATRIX

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001` · `CP-T08`

Measured on `DB-SM` — **447,384 journal items, product line 16.0** (see `40_P08_VERSION_PREMISE_CORRECTION.md`). Source references are 18.0 and are labelled as such.

## 1. Correction to a published P08 position

> **"The journal item is both original and derived truth, and nothing marks which."**
>
> **First half: `FACT VERIFIED`, and understated.**
> **Second half: `CONTRADICTED AS AN ABSOLUTE`. Corrected below.**

A forensic pass commissioned to disprove this partially succeeded, and the author accepts it. **69.07% of items do carry a stored origin pointer.** Stating that *nothing* marks origin is stronger than the data supports and is withdrawn.

**Corrected statement:**

> The journal item is both original and derived truth. **Origin is marked on the *entry* rather than the *item* for 47.17% of the population; no stored field partitions it; and for 17.00% — rising to 96.29% of the unclassifiable residual — no structural mark exists at all.**

## 2. What actually marks origin

| Tier | Meaning | Items | Share |
|---|---|---|---|
| **1** | a stored pointer to an originating record | 309,015 | **69.07%** |
| **2** | a configuration pointer only (tax, product, model, withholding) | 62,307 | 13.93% |
| **3** | **no provenance pointer of any kind** | **76,062** | **17.00%** |

**But the tier that matters is where the pointer sits.**

| Location of the only Tier-1 pointer | Items | Share |
|---|---|---|
| On the **journal item** itself | 98,000 | 21.91% |
| **On the entry header only** | **211,015** | **47.17%** |

The general ledger, trial balance, balance sheet and profit-and-loss statement all aggregate the **item**. Nearly half the population therefore carries, at the level the statements read, **no origin at all** — its provenance lives one level up.

`FACT VERIFIED`: the item-level mirrors of the entry's pointers are stored copies — **0 of 447,384 items disagree with their entry** — so they add no independent information.

## 3. No field partitions the population

Independent origin predicates matched per item:

| Predicates matched | Items | Share |
|---|---|---|
| 0 | 18,950 | 4.24% |
| 1 | 345,714 | 77.28% |
| **2 or more** | **82,720** | **18.49%** |

**18.49% of items satisfy two or more origin predicates at once.** Largest overlaps: payable-invoice with tax (24,893), payment with withholding (15,213), payable-invoice with purchase-order line (13,465), exchange difference with reversal (6,616).

`FACT VERIFIED`. A discriminator that overlaps on nearly a fifth of the population is not a discriminator.

## 4. The measured semantic population

| Class | Items | Share | Rule |
|---|---|---|---|
| Inventory valuation | 113,231 | 25.31% | reliable — entry pointer |
| Payable invoice | 112,489 | 25.14% | reliable — entry type |
| Asset depreciation | 60,079 | 13.43% | reliable — entry pointer |
| Payment | 53,321 | 11.92% | reliable — entry pointer |
| Cash-basis tax | 30,804 | 6.89% | reliable — entry pointer |
| Bank statement | 30,344 | 6.78% | reliable — entry pointer |
| **Unattributed** | **19,364** | **4.33%** | **no rule fires** |
| Exchange difference | 18,411 | 4.12% | **heuristic — a renameable journal label only** |
| Receivable invoice | 9,288 | 2.08% | reliable — entry type |
| Reversal, other | 53 | 0.01% | reliable |

**Classes the data cannot yield at all:** *manual*, *revaluation*, *closing*, *adjustment*. **No field records human authorship** — the creating user is an author, not a mode.

**The unattributed 19,364 carry 12.19 billion baht of posted debits**, 96.29% of them with no pointer of any kind.

## 5. Two items, identical in accounting content, different in origin — measured

**`FACT VERIFIED`, with real examples.**

- Grouping on exactly what the statements read — company, account, partner, currency, date, debit, credit, transaction amount — **129 groups span different origin classes, covering 355 items**.
- Restricting to items where **every** provenance pointer is null on both item and entry (73,984 items, 16.54%): **6,494 groups covering 23,419 items are indistinguishable on every stored accounting attribute.**

One verified example: three items on one payable-tax account, same partner, same date, same 140.00 debit — one a cash-basis reversal, one a vendor bill, one a cash-basis realisation. **Only free text separates them.**

Another: five items, one account, one partner, one date, 665.00 credit each, in five separate entries, **label empty on every one**. Nothing structural says whether these are five vendor documents or one posted five times.

## 6. Why the derived lines are the unmarked ones — 18.0 source

Independently verified in source, and this is the mechanism behind the whole matrix:

| Derived line | What the creating code writes |
|---|---|
| Tax line | the computed values plus a display marker and the entry id — **no pointer to the base line it was computed from**. The base-to-tax relationship is **reconstructed at query time**, by a routine whose own signature offers an *approximate* mapping when reconstruction fails |
| Inventory valuation line | the creating routine **receives the valuation-layer identifier as a parameter and does not write it into the line values**. The pointer exists only on the entry header |
| Depreciation line | seven accounting attributes and nothing else. The asset reference, the depreciation amount and the period all sit on the **entry**, not the line |

`FACT VERIFIED` for 18.0.

## 7. What the statements read

**The general ledger, trial balance, balance sheet and profit-and-loss statement read essentially no provenance field.** They read account, date, amounts, currency, company, partner, journal, entry, display type and posting state. One report selects a payment pointer solely to choose which drill-down menu to attach — it never touches an amount.

A scoped search across the whole reporting module for the purchase-order line, sales-order line, expense, asset and matching-rule pointers returns **zero hits anywhere**. `B NOT FOUND IN SEARCHED SCOPE`, bounded to 18.0 core reporting — **the deployed database adds a custom reporting module that this claim does not cover.**

## 8. Consequence for the kernel

This is the measured form of `KRN-INV-03` (every posted fact carries its provenance). The benchmark carries provenance for **69%** of items, of which **more than two-thirds carry it on the wrong object**, and the statements that produce the financial position read **none of it**.

The design requirement is therefore sharper than "add provenance": **provenance must be carried on the financial fact itself, because the financial fact is what the statements aggregate.**
