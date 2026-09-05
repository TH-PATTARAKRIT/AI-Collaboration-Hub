# AI07 — P09_SYMMETRIC_ALLOCATION_EVENT_SWEEP

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · continuation `…ANALYTIC-ECONOMIC-INTEGRITY-001`
**Layer:** 1 — clean-room.

This closes the item the base package explicitly declared **unsearched** (`NS-12`, `DEP-P09-12`): *whether any event type other than depreciation allocates both legs of a balanced pair.*

**It does not. Four further mechanisms do, three of them in core accounting, and one of them is worse than depreciation.**

---

## 1. DENOMINATOR — DECLARED AND EXECUTED

- **POPULATION:** every site that writes an allocation key into journal-row values.
- **PATTERN:** the two literal spellings of that key in a values dictionary, non-test files. **Declared false-negative mode:** a site that sets the field by assignment on a record rather than in a values dictionary, or through a variable-held key name, is **not** selected — class **C** for that residue.
- **PATH SET:** the reference enterprise root.
- **UNIT:** one write site.

**Executed result: 45 write sites across 11 modules.** The module set: core accounting, accounting (enterprise), asset, reports, cash-basis reports, analytic, expense, payroll accounting, purchase requisition, purchase/stock, stock accounting.

## 2. THE SWEEP

| # | Event | Rows given an allocation | Symmetric? | Net analytic effect | Class |
|---|---|---|---|---|---|
| 1 | **customer invoice** | product rows only; the receivable counterpart is not given one | no | correct | A |
| 2 | **vendor bill** | product rows only; the payable counterpart is not given one | no | correct | A |
| 3 | **employee expense** | expense rows only | no | correct | A |
| 4 | **asset depreciation** | **both** rows — expense **and** accumulated depreciation | **YES** | **zero** | **A** |
| 5 | **deferred expense / deferred revenue recognition** | same two-row builder as depreciation | **YES** | **zero** | **A** |
| 6 | **cut-off / change-period accrual** | **both** rows — the original account and the accrual account, built as an explicit debit/credit **swap** of each other, same allocation on both | **YES** | **zero** | **A** |
| 7 | **change-account transfer** | source rows keep their own allocation; the counterpart row on the destination account receives a **proportionally recomputed** allocation with the exact opposite balance | **YES** | **≈ zero**, with a rounding residue | **A** |
| 8 | **accrued orders (accrued expense / accrued revenue)** | expense or income rows keep their own; the "globalised counterpart" on the accrual account receives a **price-weighted blend** of them all, with balance exactly the negation of their sum | **YES** | **≈ zero, with a tax-driven residue** — see §3 | **A** |
| 9 | **cash-basis tax entry — base rows** | the base row **and its counterpart**, built by swapping debit and credit **on the same account**, same allocation | **YES — the worst case** | **zero, and undetectable** — see §4 | **A** |
| 10 | **cash-basis tax entry — tax rows** | tax row and its counterpart, swapped, same allocation | **YES** | **zero** | **A** |
| 11 | **early-payment discount / discount allocation rows** | a proportionally derived allocation on an opposite-signed row | **opposite-signed but CORRECT** — see §5 | correct | A |
| 12 | **exchange difference** | one of the two generated rows | no | one-sided | A (base package) |
| 13 | **bank write-off / reconciliation model rows** | the write-off row | no | one-sided | A (base package) |
| 14 | **inventory valuation posting** | passes the source row's allocation through | not a balanced pair in the relevant sense | — | A |
| 15 | **payroll** | rows derived from salary rules carrying an analytic account | no | one-sided | A |
| 16 | **purchase/stock price-difference rows** | price-difference rows | no | one-sided | A |
| 17 | **manufacturing work-in-progress ledger entry** | **no row carries an allocation** | n/a | no attribution at all | A (base package) |
| 18 | **manual journal entry** | whatever the user types | user-determined — a user **can** create the symmetric case by hand and nothing warns them | **A** for the absence of a warning |

## 3. THE ACCRUED-ORDERS RESIDUE — WORSE THAN A CLEAN ZERO

The accrual counterpart's allocation is built as a blend weighted by each order line's **tax-inclusive** total, divided by the sum of the orders' **tax-inclusive** totals. The balances it is cancelling are **tax-exclusive** subtotals.

The two weightings therefore do not match, and the cancellation is **approximate**. The cost centre is left with a residue driven by the differing tax ratios across lines — a non-zero number that corresponds to no economic fact at all.

**A clean zero is at least recognisable as wrong. A small non-zero residue looks like a real cost.** Classification: **FACT VERIFIED** for the mechanism; the residue's magnitude in any deployment is **UNRESOLVED — DATA REQUIRED**.

## 4. THE CASH-BASIS CASE — THE ONLY ONE NO SURFACE CAN SEE

Every other symmetric case is partly rescued by **bucketing**: the two legs sit on different general accounts, so account-filtered surfaces (budget consumption, financial-report analytic columns) see only one of them and report the correct figure (`AI04` §3).

The cash-basis base-line counterpart is built on **the same account** as the row it offsets. Both legs therefore land in the **same bucket on every surface**.

> **For the cash-basis base pair, the attribution is zero on *every* management surface, including the ones that report depreciation correctly.**

This is the most severe instance found in the entire P09 programme, and it sits in core accounting, on a path used by every organisation on cash-basis tax.

**Classification: `VERIFIED DEFECT — ANALYTIC RECORDS EXIST BUT ECONOMIC COST ZEROES OUT`, unconditional and surface-independent.**

## 5. NOT EVERY OPPOSITE-SIGNED PAIR IS A DEFECT

The discount-allocation and early-payment-discount rows carry a proportionally derived allocation on an opposite-signed row, on the same account as the cost they reduce. **This is correct.** A discount genuinely reduces the cost attributed to the cost centre, and the two rows are two economically distinct facts.

Recording this matters for three reasons: it shows the sweep discriminated rather than pattern-matched; it proves the defect is not "opposite signs are bad"; and it identifies the missing concept — the system cannot distinguish a **reducing** allocation from a **counterpart** allocation (`AI-E-02`).

## 6. REVISED SCOPE OF THE CENTRAL FINDING

| Base package said | This sweep establishes |
|---|---|
| depreciation allocates both legs; whether any other event does was **not searched** | **five** mechanisms do — depreciation, deferred recognition, cut-off/change-period, change-account transfer, accrued orders — **plus two cash-basis pairs** |
| the finding sat in the asset module | **three of the five sit in core accounting**, and the most severe is the cash-basis one |
| consequence bounded to net-balance surfaces | true for four of them; **false for the cash-basis pair, which is invisible on every surface** |

**The defect is a property of the allocation carrier's granularity, not of the asset module.** Anywhere the platform builds a counterpart row by copying a source row's allocation and inverting its balance, the attribution annihilates.

## 7. OPEN

| ID | Item | Class |
|---|---|---|
| SW-U-01 | write sites that set the field by record assignment rather than in a values dictionary | **C — declared false-negative mode of the pattern** |
| SW-U-02 | off-balance-sheet account rows | **C — not searched** |
| SW-U-03 | the residue magnitude in the accrued-orders case for any real deployment | **UNRESOLVED — DATA REQUIRED** |
| SW-U-04 | tenant custom modules — the sweep covered the reference root only | **C — not searched** |

## 8. CHECKPOINT

**CP-AI07 — EVENT-TYPE SWEEP COMPLETED.** The base package's unsearched item is closed: depreciation is **not** unique. `NS-12` and `DEP-P09-12` are discharged and replaced by the four open items above. Auto-continue.
