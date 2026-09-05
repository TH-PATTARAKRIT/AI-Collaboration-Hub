# AI04 — P09_DEPRECIATION_ANALYTIC_ECONOMIC_TRACE

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · continuation `…ANALYTIC-ECONOMIC-INTEGRITY-001`
**Layer:** 1 — clean-room.

---

## 1. THE FULL FORENSIC TRACE

Worked with a 100 % allocation to one cost centre `CC` and a monthly depreciation charge of `X = 1,000`.

```
ASSET
  carries an allocation D = { CC : 100 }
  D is itself a weighted average of the allocations on the asset's originating rows
      ↓
DEPRECIATION EVENT  (a schedule line, not a user act)
      ↓
JOURNAL ENTRY  — exactly two rows, built in one function
      ↓
   ┌─ ROW 1 ─ accumulated depreciation  (BALANCE SHEET)   credit 1,000   balance −1,000   D applied ✔
   └─ ROW 2 ─ depreciation expense      (PROFIT & LOSS)   debit  1,000   balance +1,000   D applied ✔
      ↓
POSTING  → analytic-line creation over the WHOLE row set, no account-type filter
      ↓
   ┌─ MANAGEMENT RECORD 1   from row 1   amount = −(−1,000)×100/100 = +1,000   general account = accumulated depreciation
   └─ MANAGEMENT RECORD 2   from row 2   amount = −(+1,000)×100/100 = −1,000   general account = depreciation expense
      ↓
ANALYTIC ACCOUNT  CC
      gross movement 2,000        net balance 0
      ↓
MANAGEMENT REPORTS  → the surfaces disagree; see §3 and AI08
```

## 2. THE FIVE QUESTIONS THE DIRECTIVE ASKS

| # | Question | Answer | Class |
|---|---|---|---|
| 1 | Does the depreciation **expense** reach the intended cost centre? | **Yes** — one management record of `−1,000`, correctly signed for a cost, correctly attributed. | FACT VERIFIED |
| 2 | Does the **accumulated depreciation** side also reach it? | **Yes** — one management record of `+1,000`, on a balance-sheet general account, attributed to the same cost centre. | FACT VERIFIED |
| 3 | What is the **net** analytic effect? | **Zero.** Unconditionally, by the algebra of `AI02` §3 Corollary 1. | FACT VERIFIED |
| 4 | What is the **gross** analytic effect? | **2,000** — twice the economic cost, as two records of opposite sign. | FACT VERIFIED |
| 5 | What does the report show? | **It depends entirely on the surface.** See §3. | FACT VERIFIED |

## 3. WHAT EACH SURFACE SHOWS FOR THE SAME EVENT

> **This section was corrected during the continuation.** A first draft stated that the financial-report analytic column "contributes 0". That was **wrong**, and an independently tasked reviewer disproved it. The corrected analysis is below; the error is logged in `AI14` §2 and in the revision log.

The decisive mechanism is **bucketing**. Each management record carries **its own** general account — the record from the balance-sheet row carries the accumulated-depreciation account, the record from the profit-and-loss row carries the expense account. Any surface that groups by general account therefore places the two records in **different buckets, where they cannot cancel**. Only a surface that sums a cost centre's records **regardless of general account** can cancel them.

| Surface | Does it group or filter by the general account? | What it shows for the 1,000 depreciation | Class |
|---|---|---|---|
| **the analytic account's own `balance`** | **no** — it splits purely on the sign of the amount | **balance 0** | FACT VERIFIED |
| **the same account's `debit` and `credit`** | no | **debit 1,000, credit 1,000** — the gross footprint survives | FACT VERIFIED |
| **analytic item list, pivot, graph, grid** | no | nets to **0** in any cell that contains both records; shows **+1,000 and −1,000 individually** when the rows are not aggregated together | FACT VERIFIED |
| **budget consumption ("achieved")** | **yes** — the query admits only income and expense general accounts | **1,000 consumed** — the correct figure. The balance-sheet record is dropped before summation, so there is nothing to cancel against | FACT VERIFIED |
| **financial-report analytic column** | **yes, indirectly but decisively** — the shadow view keys its account column to each record's own general account, and each report line then filters to its own accounts | a profit-and-loss analytic column shows the **full 1,000**; a balance-sheet analytic column shows the counterpart. **They never meet, so they never cancel** | FACT VERIFIED |
| **project profitability — every section** | filters on provenance markers instead: journal-item link, category, or document type | **neither record appears at all.** Both legs carry a journal-item link, category "other", and a miscellaneous document type, and every section's filter excludes one or more of those. The pair is **invisible**, not netted | FACT VERIFIED |
| **timesheet analysis** | requires a project on the record | excluded | FACT VERIFIED |

### 3.1 The corrected statement of the defect

**The zeroing is real, and it is confined to surfaces that ask "what is this cost centre's net analytic balance".** It does **not** propagate to surfaces that bucket by general account.

This is narrower than the first reading and **more dangerous**, for three reasons:

1. **The surfaces disagree with one another.** The same asset, the same month, the same cost centre: the analytic account reports a balance of **0**, budget consumption reports **1,000**, and the profit-and-loss analytic column of a financial report reports **1,000**. All three are reading the same two records correctly under their own rules.
2. **The correct figures are correct by accident.** The budget query filters to income and expense accounts for its own unrelated reasons; the report column buckets by account because that is how reports work. Neither is a control against symmetric allocation. Remove either filter — or add a surface that sums a cost centre without bucketing — and the figure silently becomes zero.
3. **Project profitability shows nothing at all.** A project that bears an asset's depreciation sees **no** depreciation in its profitability panel — not a zero, an absence. That is a separate defect from the zeroing and is not fixed by fixing the zeroing.

### 3.2 What this means for the central hypothesis

The hypothesis "analytic records exist but economic cost zeroes out" is **verified** — with its scope now precisely bounded: it zeroes out **in the net analytic balance of the cost centre**, which is the figure a cost-centre report is most likely to present, and it does **not** zero out in account-bucketed consumption figures.

## 4. THE INTENT QUESTION

The directive asks (Q6, Q7, Q11) what the analytic ledger is *for*, and whether the cancellation is intended.

**Finding:** the source carries **no statement of intent** anywhere on this path. Specifically:
- the function that builds the two rows carries a comment explaining **why the key is conditional**, and **no comment about why both rows receive it**;
- there is no "balanced analytic subledger" concept expressed anywhere — no analytic counterpart account, no analytic balancing rule, no analytic trial balance, and no constraint that an entry's analytic amounts sum to zero;
- the analytic account's own presentation exposes **debit, credit and balance**, which is consistent with a *balanced subledger* reading; but every consumer that answers a management question (budget consumption, profitability) filters to profit-and-loss accounts, which is consistent with a *cost attribution* reading.

**The two readings are both present in the product and are not reconciled by it.** P09 therefore does **not** assert that the cancellation is a bug in the reference product — that is a statement about another party's design intent and the evidence does not support it. P09 asserts the operational fact and the requirement it generates for SMEsPlus.

**Classification: `DESIGN DECISION REQUIRED AT FINAL GATE`** for the question "what is the analytic ledger for". SMEsPlus must choose one reading; the reference pattern demonstrates the cost of choosing neither.

## 5. THE SMEsPlus REQUIREMENT THIS TRACE GENERATES

**AI-R-01.** The management model shall declare, once and at model level, whether the analytic ledger is a **cost attribution ledger** (only rows carrying the economic effect are attributed; it does not balance) or a **balanced analytic subledger** (every row is attributed; it balances by construction and net balance is meaningless as a cost figure). **These are different products and cannot both be true of one record set.**

**AI-R-02.** Whichever is chosen, **every consumer shall apply the same filter**, and the filter shall be a property of the model, not re-implemented per report. The reference pattern's surfaces disagree precisely because each re-implements its own.

**AI-R-03.** Where the cost-attribution reading is chosen — P09's recommendation — the eligibility rule shall be enforced at **creation**, not at consumption: a balance-sheet row shall not produce a cost attribution at all, rather than producing one that each report must remember to exclude.

**AI-R-04.** A cost attribution shall be derived from the **accounting event**, not from its rows independently. The event knows which of its rows carries the economic effect; a row does not.

## 6. CHECKPOINT

**CP-AI04 — DEPRECIATION TRACE COMPLETED.** Net effect zero (FACT VERIFIED); gross effect double; surfaces disagree; intent undeclared in source and routed as a design decision. Auto-continue.
