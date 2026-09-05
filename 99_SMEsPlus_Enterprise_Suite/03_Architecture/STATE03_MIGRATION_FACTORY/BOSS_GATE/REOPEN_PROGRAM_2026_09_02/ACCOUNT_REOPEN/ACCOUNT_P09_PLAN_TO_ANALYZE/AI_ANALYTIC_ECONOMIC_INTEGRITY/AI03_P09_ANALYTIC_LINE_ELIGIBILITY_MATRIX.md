# AI03 — P09_ANALYTIC_LINE_ELIGIBILITY_MATRIX

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · continuation `…ANALYTIC-ECONOMIC-INTEGRITY-001`
**Layer:** 1 — clean-room.

Answers directive questions 1, 2, 13, 14, 15, 16, 17.

---

## 1. THE ELIGIBILITY RULE, STATED ONCE

> **A journal row produces management records if, and only if, it carries a non-empty allocation.**

That is the entire rule. There is no second condition on the creation path.

| Candidate eligibility criterion | Does it apply? | Evidence |
|---|---|---|
| **account type** (profit-and-loss vs balance sheet) | **NO** | no account-type test exists anywhere on the creation path — class **A**, the three functions read in full |
| **row / display type** | **NO on the creation path.** A row-type restriction exists, but only inside the *obligation validation* that runs before creation, and it gates whether a **complaint** is raised, never whether a **record** is created | class **A**, both functions read in full |
| **configured allocation rule set** | **INDIRECTLY** — the rule set decides what a row's allocation *becomes* when nothing else set it, so it decides eligibility by populating the field | class **A** |
| **execution context** | **NO for creation.** The context flag gates only the obligation check | class **A** |
| **company ownership** | **NO** — company participates nowhere in the eligibility test | class **A** |
| **whether the row was given an allocation** | **YES — this is the whole rule** | class **A** |

**Consequence.** Eligibility is delegated entirely to whichever code built the row values. It is not a property of accounting; it is a property of the caller. Every defect in `AI07` is a caller that put an allocation somewhere an accountant would not.

## 2. ACCOUNT-TYPE MATRIX

For each account type: can a row on it produce a management record, and does it in practice?

| Account type on the row | Can produce a record? | Does it in practice? | How it happens |
|---|---|---|---|
| **expense** | yes | **yes** — the intended case | product rows on bills, expenses, depreciation expense |
| **income** | yes | **yes** — the intended case | product rows on invoices |
| **fixed asset / non-current asset** | yes | **yes — and this is the defect** | the accumulated-depreciation leg of a depreciation entry |
| **prepaid / deferred expense (asset)** | yes | **yes** | the balance-sheet leg of a deferred-expense recognition |
| **deferred revenue (liability)** | yes | **yes** | the balance-sheet leg of a deferred-revenue recognition |
| **accrual accounts (asset or liability)** | yes | **yes** | the counterpart leg of every cut-off, accrual and change-period entry |
| **payable** | yes | **not normally** — bill counterpart rows are not given an allocation | — |
| **receivable** | yes | **not normally** — invoice counterpart rows are not given an allocation | — |
| **inventory / stock valuation** | yes | **conditionally** — the valuation posting path passes an allocation through | see `AI07` |
| **work in progress** | yes | the ledger-side work-in-progress entry carries **no** allocation on any row | base package finding, unchanged |
| **bank / cash** | yes | **conditionally** — bank write-off and reconciliation-model rows carry allocations | see `AI07` |
| **off balance** | yes | **not searched** — class **C** | — |
| **tax accounts** | yes | **conditionally** — inherited only when the tax record carries the analytic flag, or the repartition row is not used in tax closing | base package finding, unchanged |

**Nothing in this matrix is enforced.** Every "not normally" is a convention of the calling code, not a rule the system holds.

## 3. THE DISCRIMINATOR THE SYSTEM LACKS

Two rows of an entry can legitimately carry **opposite-signed** allocations, and can also do so illegitimately. The system cannot tell them apart, because it has no concept of what the rows mean to each other.

| Pattern | Example | Correct? | Why |
|---|---|---|---|
| **two rows, economically opposite facts** | a cost row and its discount row on the same account | **CORRECT** — the discount genuinely reduces the cost attributed to the cost centre | the two rows are two facts |
| **two rows, two sides of one fact** | depreciation expense and accumulated depreciation | **WRONG** — the attribution cancels | the two rows are one fact |
| **two rows, one fact, same account** | a cash-basis base row and its counterpart | **WRONG, and undetectable** — even account-bucketed surfaces cannot separate them | one fact, one account, opposite signs |

**AI-E-01.** Eligibility shall be decided by the **accounting event**, which knows which of its rows carry the economic effect, not by each row independently. This is the same requirement as `AI-S-01` reached from a different direction: a row-level carrier cannot express a rule whose subject is the event.

**AI-E-02.** The model shall distinguish a **reducing** allocation (a genuine negative attribution, such as a discount or a credit note) from a **counterpart** allocation (the other side of the same fact). The reference pattern represents both as an opposite-signed amount and can therefore never distinguish them after the fact.

**AI-E-03.** Where an allocation would land on a balance-sheet row, the system shall refuse it or mark it as a non-cost attribution. Under the cost-attribution reading recommended in `AI04` §5, a balance-sheet row has no cost to attribute.

## 4. CHECKPOINT

**CP-AI03 — LINE ELIGIBILITY PROVED.** Eligibility is by assignment alone; no account-type, row-type, context or company test applies to creation. Auto-continue.
