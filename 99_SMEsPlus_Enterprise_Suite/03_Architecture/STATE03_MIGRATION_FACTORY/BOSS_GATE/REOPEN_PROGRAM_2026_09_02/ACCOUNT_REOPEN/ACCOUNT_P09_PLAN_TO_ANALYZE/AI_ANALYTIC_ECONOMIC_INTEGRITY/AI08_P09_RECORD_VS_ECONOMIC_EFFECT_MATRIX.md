# AI08 — P09_RECORD_VS_ECONOMIC_EFFECT_MATRIX

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · continuation `…ANALYTIC-ECONOMIC-INTEGRITY-001`
**Layer:** 1 — clean-room.

Answers directive questions 6, 7, 8, 9, 10, 11, 18, 19, 20.

---

## 1. THE EIGHT DISTINCT THINGS THE DIRECTIVE REQUIRES BE SEPARATED

Applied to one depreciation of 1,000 at a 100 % allocation to one cost centre:

| Concept | Value | Is it what a manager wants? |
|---|---|---|
| **record creation** | 2 records created | not a management fact at all |
| **gross analytic movement** | 2,000 | **twice** the economic cost |
| **net analytic balance** | **0** | **wrong** — the cost was 1,000 |
| **economic cost** | 1,000 | the truth |
| **economic revenue** | 0 | — |
| **cost-centre attribution** | **0 on net-balance surfaces, 1,000 on account-bucketed surfaces** | **inconsistent** |
| **project attribution** | **nothing at all** — every profitability section filters the pair out | **absent** |
| **financial dimension attribution** | correct — the ledger is untouched | the ledger is right |

**Six different numbers describe one event.** Only one of them is the economic cost, and it is not the one a cost-centre report presents.

## 2. THE CENTRAL QUESTION

> Does the current mechanism answer *"which cost centre owns the expense?"* — or merely *"which analytic dimension appears on both journal legs?"*

**It answers the second.** The allocation records which dimension was *named*; the amount records the *arithmetic of the row it was named on*. Nothing in the mechanism asks which row carries the economic effect.

That is why the same allocation, faithfully applied, produces the right answer for a vendor bill (where only the expense row is named) and zero for a depreciation (where both rows are named). **The mechanism is not attributing cost. It is annotating rows, and cost attribution is an emergent property of which rows happen to get annotated.**

## 3. THE MATRIX BY EVENT TYPE

| Event | Record created? | Gross | Net | Economic cost | Attribution correct? |
|---|---|---|---|---|---|
| vendor bill / expense | yes | X | **X** | X | **yes** |
| customer invoice | yes | X | **X** | X (revenue) | **yes** |
| asset depreciation | yes, ×2 | 2X | **0** | X | **no — net-balance surfaces show nothing** |
| deferred recognition | yes, ×2 | 2X | **0** | X | **no** |
| cut-off / change period | yes, ×2 | 2X | **0** | X | **no** |
| change-account transfer | yes, ×2 | ≈2X | **≈0** | 0 (it is a transfer) | **arguably intended** — see §4 |
| accrued orders | yes, ×2 | ≈2X | **small residue** | X | **no — and the residue looks real** |
| **cash-basis base pair** | yes, ×2 | 2X | **0 on every surface** | X | **no — and undetectable** |
| discount / early-payment discount | yes | X | **X reduced by the discount** | X − d | **yes** |
| timesheet, work-order time | yes | X | **X** | X | yes as management truth; **no financial counterpart exists** |
| manufacturing work-in-progress ledger entry | **no record** | 0 | 0 | X | **no — absent entirely** |

## 4. WHERE THE ZERO MIGHT BE CORRECT

Intellectual honesty requires stating the case against the finding.

For the **change-account transfer**, a net-zero analytic effect is arguably **correct**: the entry moves a balance between two general accounts and creates no new economic cost. Attributing nothing is the right answer.

This matters because it shows that **net-zero is not automatically a defect** — it is a defect exactly when the entry *does* carry an economic effect and the attribution cancels it. Depreciation, deferred recognition, cut-off and the cash-basis pair all carry real economic effects. The transfer does not.

**AI-M-01.** The model shall be able to state, per accounting event, whether the event carries an economic effect to attribute. Without that, zero is ambiguous between "correctly nothing" and "wrongly nothing" — which is precisely the state the reference pattern is in.

## 5. ARE HISTORICAL RECORDS ECONOMICALLY CORRECT?

> Directive question 19.

**For the observed deployments: the question does not arise, and that is itself the answer.** No asset in any located deployment carries an allocation (`AI05` §3), so no symmetric depreciation pair exists to be incorrect. Class **A within the searched scope**.

**For any deployment that does allocate:** every historical symmetric pair is economically incorrect on net-balance surfaces from the moment it was posted, and no remediation path exists in the reference pattern — the records are correct individually, so nothing can identify them except by re-deriving the pairing from the entry.

**AI-M-02.** SMEsPlus shall be able to identify, retrospectively, every management record whose net contribution to its dimension was annihilated by a counterpart in the same event. The reference pattern cannot, because the records carry no reference to the event, only to their row.

## 6. CAN A REPORT SHOW NON-ZERO COST WHEN THE PAIR NETS TO ZERO?

> Directive question 20. **Yes — and it is the normal case, not the exception.**

The mechanism is **bucketing, not netting**: the two records carry different general accounts, so any surface that groups or filters by general account places them in different buckets where they cannot cancel, and each shows its full gross amount.

| Surface | Shows |
|---|---|
| budget consumption | **1,000** — correct, by an account-type filter written for another purpose |
| financial-report analytic column, profit-and-loss line | **1,000** — correct, by account bucketing |
| the analytic account's own balance | **0** |
| the analytic account's debit and credit columns | **1,000 and 1,000** |
| project profitability | **nothing** |

**Five surfaces, four different answers, one event.** The exception is the cash-basis pair, where both legs share an account and every surface reports zero.

## 7. CHECKPOINT

**CP-AI08 — RECORD-VS-ECONOMIC-EFFECT SEMANTICS COMPLETED.** The mechanism annotates rows; it does not attribute cost. Auto-continue.
