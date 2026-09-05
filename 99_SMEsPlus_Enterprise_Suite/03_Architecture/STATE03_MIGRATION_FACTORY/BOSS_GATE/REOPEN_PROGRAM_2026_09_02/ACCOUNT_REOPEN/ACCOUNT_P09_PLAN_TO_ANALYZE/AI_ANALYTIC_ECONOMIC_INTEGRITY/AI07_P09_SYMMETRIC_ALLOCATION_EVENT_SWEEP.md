# AI07 — P09_SYMMETRIC_ALLOCATION_EVENT_SWEEP

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · continuation `…ANALYTIC-ECONOMIC-INTEGRITY-001`
**Layer:** 1 — clean-room.

This closes the item the base package explicitly declared **unsearched** (`NS-12`, `DEP-P09-12`): *whether any event type other than depreciation allocates both legs of a balanced pair.*

**It does not.** Corrected after adversarial challenge: **three mechanism families reproduce the exact zeroing** — depreciation, deferred recognition, the cut-off/change-period accrual, and the two cash-basis pairs — and the cash-basis one is **worse than depreciation** because no surface can see past it. **Two further mechanisms fail differently**, by leaving a meaningless residue rather than a zero. Predominantly core accounting, not the asset module.

---

## 1. DENOMINATOR — DECLARED AND EXECUTED

- **POPULATION:** every site that writes an allocation key into journal-row values.
- **PATTERN:** the two literal spellings of that key in a values dictionary, non-test files. **Declared false-negative mode:** a site that sets the field by assignment on a record rather than in a values dictionary, or through a variable-held key name, is **not** selected — class **C** for that residue.
- **PATH SET:** the reference enterprise root.
- **UNIT:** one write site.

**Executed result: 45 write sites across 11 modules — AND THIS DENOMINATOR IS INADEQUATE. See §1A.** The module set: core accounting, accounting (enterprise), asset, reports, cash-basis reports, analytic, expense, payroll accounting, purchase requisition, purchase/stock, stock accounting.

## 1A. THE DENOMINATOR DOES NOT CONTAIN ITS OWN SUBJECT — **FOUND BY CHALLENGE**

An independent reviewer measured the blind spot this sweep declared and left unmeasured. The result:

| Pattern form | Sites |
|---|---|
| the declared pattern — key followed by a colon in a values dictionary | **45** (11 modules) |
| record-attribute assignment | 19 |
| **subscript assignment** | 18 |
| **union** | **82 sites across 23 modules** |

**Delta: +37 sites (+82 %), +12 modules (+109 %).**

> **And the single write site on which this entire finding rests — the both-legs assignment in the asset module — is a *subscript* assignment, and is therefore NOT a member of the declared 45.**

The team found it by **reading the function**, which the Layer 2 record states plainly. The sweep, run over the whole root, **would not have found it**. Declaring a residue as class C is not the same as bounding it: here the residue contained the headline mechanism itself.

**Consequence for every count in this document: `45/11` must be read as a lower bound, and the sweep re-derived over `82/23` before any count here is relied upon.** Twelve project-, sale- and purchase-side modules have not been reasoned about at all. Recorded as `DEP-P09-27`.

## 2. THE SWEEP

| # | Event | Rows given an allocation | Symmetric? | Net analytic effect | Class |
|---|---|---|---|---|---|
| 1 | **customer invoice** | product rows only; the receivable counterpart is not given one | no | correct | A |
| 2 | **vendor bill** | product rows only; the payable counterpart is not given one | no | correct | A |
| 3 | **employee expense** | expense rows only | no | correct | A |
| 4 | **asset depreciation** | **both** rows — expense **and** accumulated depreciation | **YES** | **zero** | **A** |
| 5 | **deferred expense / deferred revenue recognition** | **CORRECTED by challenge: it is NOT the asset module's builder** — it lives in the reporting module and builds its two legs from **different denominators** (a per-key ratio for the profit-and-loss legs, an aggregate ratio for the balance-sheet leg) | **NO — a residue case, not a clean zero** | **not zero** with more than one grouping key; and the move is immediately reversed, producing a **second, cross-move** pair the sweep's unit cannot see | **A — reclassified** |
| 6 | **cut-off / change-period accrual** | **both** rows — the original account and the accrual account, built as an explicit debit/credit **swap** of each other, same allocation on both | **YES** | **zero** | **A** |
| 7 | **change-account transfer** | source rows keep their own allocation; the counterpart receives a **re-derived** allocation computed from money amounts | **NO — reclassified after challenge** | **not zero**: unallocated source rows dilute the counterpart's shares below 100, and rounding shortens them further | **A** — a *different* failure mode, see §3A |
| 8 | **accrued orders (accrued expense / accrued revenue)** | N order rows keep their own; **one** globalised counterpart receives a re-derived weighted aggregate. **Not a two-row pair at all** | **NO — reclassified after challenge** | **not zero**: order lines with no allocation are skipped in the numerator but counted in the denominator, so the counterpart sums below 100 | **A** — see §3A |
| 9 | **cash-basis tax entry — base rows** | the base row **and its counterpart**, built by swapping debit and credit **on the same account**, same allocation | **YES — the worst case** | **zero, and undetectable** — see §4 | **A** |
| 10 | **cash-basis tax entry — tax rows** | tax row and its counterpart, swapped, same allocation | **YES** | **zero** | **A** |
| 11 | **early-payment discount / discount allocation rows** | a proportionally derived allocation on an opposite-signed row | **reasoning CONTRADICTED by challenge** — see §5 | conclusion survives, evidence does not | A |
| 12 | **exchange difference** | one of the two generated rows | no | one-sided | A (base package) |
| 13 | **bank write-off / reconciliation model rows** | the write-off row | no | one-sided | A (base package) |
| 14 | **inventory valuation posting** | passes the source row's allocation through | not a balanced pair in the relevant sense | — | A |
| 15 | **payroll** | rows derived from salary rules carrying an analytic account | no | one-sided | A |
| 16 | **purchase/stock price-difference rows** | price-difference rows | no | one-sided | A |
| 17 | **manufacturing work-in-progress ledger entry** | **no row carries an allocation** | n/a | no attribution at all | A (base package) |
| 18 | **manual journal entry** | whatever the user types | user-determined — a user **can** create the symmetric case by hand and nothing warns them | **A** for the absence of a warning |

## 3A. RECLASSIFICATION AFTER ADVERSARIAL CHALLENGE

> An independent reviewer tasked to **disprove** this sweep contradicted its first draft. Rows 7 and 8 were listed as symmetric. **They are not.** Their counterpart's allocation is **re-derived from money amounts**, not copied, so the antecedent of the zeroing theorem is not satisfied and the terms do not cancel.
>
> **The corrected reading is not milder.** These two mechanisms attribute **neither correctly nor to zero**: they leave a residue on the cost centre that corresponds to no economic fact. Two independent causes, both verified:
> 1. source rows carrying **no** allocation contribute to the counterpart's **denominator** but nothing to its numerator, so its shares sum to **less than 100** while the source side sums to 100;
> 2. every share is rounded to two digits on write, so a three-way split re-derived as 33.33 × 3 = 99.99 never reaches the exact-100 remainder branch.
>
> **Revised count: three mechanism families satisfy the zeroing antecedent** — depreciation (and its deferred-recognition variants), the cut-off/change-period accrual, and the two cash-basis pairs. **Two further mechanisms fail by residue.** The base package's unsearched item is closed either way, and closed more thoroughly than the first draft claimed.

## 3. THE RESIDUE MECHANISMS — WORSE THAN A CLEAN ZERO

Rows 7 and 8 leave a residue rather than a zero. **Three** independent causes, the first found by this sweep and the other two by the challenge that reclassified it:

1. **Weighting-base mismatch** (accrued orders): the counterpart's blend is weighted by **tax-inclusive** line totals, while the balances it offsets are **tax-exclusive** subtotals. The two weightings do not match.
2. **Unallocated rows dilute the denominator**: source rows carrying no allocation contribute to the counterpart's total balance but nothing to its numerator, so its shares sum to **less than 100** while the source side sums to 100.
3. **Percentage rounding**: shares are rounded to two digits on write, so a re-derived three-way split of 33.33 × 3 = 99.99 never reaches the exact-100 remainder branch and that side is short by 0.01 % of balance.

**A clean zero is at least recognisable as wrong. A small residue looks like a real cost.** Classification: **FACT VERIFIED** for all three mechanisms; the magnitude in any deployment is **UNRESOLVED — DATA REQUIRED** (`SW-U-03`).

## 4. THE CASH-BASIS CASE — THE ONLY ONE NO SURFACE CAN SEE

Every other symmetric case is partly rescued by **bucketing**: the two legs sit on different general accounts, so account-filtered surfaces (budget consumption, financial-report analytic columns) see only one of them and report the correct figure (`AI04` §3).

The cash-basis base-line counterpart is built on **the same account** as the row it offsets. Both legs therefore land in the **same bucket on every surface**.

> **For the cash-basis base pair, the attribution is zero on *every* management surface, including the ones that report depreciation correctly.**

**Severity CHALLENGED, and the challenge is accepted.** Applying this package's own test — does the entry carry a **new** economic effect to attribute? — the answer is **no**. The cost was already attributed when the invoice or bill posted, and the pair **copies that same allocation**. **If this pair did not cancel it would double-count.** The cancellation is not merely tolerable; it is **required**.

A reviewer confirmed this empirically in a deployed database: **16,332 management records** sit on the cash-basis base account and sum to **exactly 0.00**.

**Revised classification: a data-hygiene defect, not the programme's most severe economic one.** 16,332 guaranteed-noise records doubling gross movement and polluting every item list, on an account that is not a cost account. **The first draft's ranking of this as "the most severe instance in the entire P09 programme" is withdrawn** — it carried the highest reversal risk in the package.

## 5. NOT EVERY OPPOSITE-SIGNED PAIR IS A DEFECT — **CONCLUSION SURVIVES, REASONING WITHDRAWN**

> **The first draft claimed the discount rows carry an opposite-signed allocation "on the same account as the cost they reduce" and called that a correct *reducing* allocation. A reviewer CONTRADICTED it: the mechanism fires only when the two accounts **differ** — there is an explicit guard — and the discount pair's two allocations **cancel**, exactly like the cases this document calls defects. The correct net comes from the *product* row, not from the discount pair, which is a presentation device that is analytically inert.**
>
> **Consequence:** there is **no reducing-allocation witness anywhere in this sweep**, and `AI-E-02` — the requirement to distinguish a reducing allocation from a counterpart allocation — was derived from a misread. The requirement may still be right; **its stated evidence is withdrawn and it must be re-derived or dropped.** Recorded as `DEP-P09-28`.
>
> The first draft also cited this row as proof that "the sweep discriminated rather than pattern-matched". **That claim is withdrawn with the evidence behind it.**

### 5.1 The original argument (superseded, retained for lineage)

The discount-allocation and early-payment-discount rows carry a proportionally derived allocation on an opposite-signed row, on the same account as the cost they reduce. **This is correct.** A discount genuinely reduces the cost attributed to the cost centre, and the two rows are two economically distinct facts.

Recording this matters for three reasons: it shows the sweep discriminated rather than pattern-matched; it proves the defect is not "opposite signs are bad"; and it identifies the missing concept — the system cannot distinguish a **reducing** allocation from a **counterpart** allocation (`AI-E-02`).

## 6. REVISED SCOPE OF THE CENTRAL FINDING

| Base package said | This sweep establishes (as corrected) |
|---|---|
| depreciation allocates both legs; whether any other event does was **not searched** | **three families** reproduce the exact zeroing — depreciation, deferred recognition, cut-off/change-period accrual, and the two cash-basis pairs — **and two further mechanisms fail by residue instead** |
| the finding sat in the asset module | **the zeroing families are predominantly core accounting**, and the most severe is the cash-basis one |
| consequence bounded to net-balance surfaces | true for the depreciation and accrual families; **false for the cash-basis pair, which is invisible on every surface**; and the residue mechanisms are visible everywhere but meaningless |

**The defect is a property of the allocation carrier's granularity, not of the asset module.** Anywhere the platform builds a counterpart row by copying a source row's allocation and inverting its balance, the attribution annihilates.

## 7. OPEN

| ID | Item | Class |
|---|---|---|
| SW-U-01 | write sites that set the field by record assignment rather than in a values dictionary | **C — declared false-negative mode of the pattern** |
| SW-U-02 | off-balance-sheet account rows | **C — not searched** |
| SW-U-03 | the residue magnitude in the accrued-orders case for any real deployment | **UNRESOLVED — DATA REQUIRED** |
| SW-U-04 | tenant custom modules — the sweep covered the reference root only | **C — not searched** |

## 8. CHECKPOINT

**CP-AI07 — EVENT-TYPE SWEEP COMPLETED AND RECLASSIFIED BY CHALLENGE.** The base package's unsearched item is closed: depreciation is **not** unique, and two of the sweep's own first-draft classifications were wrong. `NS-12` and `DEP-P09-12` are discharged and replaced by the four open items above. Auto-continue.
