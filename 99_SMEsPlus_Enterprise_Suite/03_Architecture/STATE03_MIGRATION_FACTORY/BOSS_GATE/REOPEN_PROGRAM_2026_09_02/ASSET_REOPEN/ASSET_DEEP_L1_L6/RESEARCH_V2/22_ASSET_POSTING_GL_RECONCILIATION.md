# 22 — ASSET POSTING AND GL RECONCILIATION
**LAYER 2 — AUDIT QUARANTINE**

Answers §26.

## 1. The trace

```
board line  ──is──►  journal entry  ──contains──►  2 journal items  ──►  general ledger
```

The word "board" describes a **presentation**. There is no board table. Each line of
the depreciation schedule **is** a journal entry, linked to the asset, carrying a
period-start date in a technical field and posting on the period-end date.

`FACT VERIFIED`. This is the strongest single property of the design: the sub-ledger
and the ledger cannot drift apart for posted lines, because they are the same rows.

## 2. The canonical entry

```
Dr   Depreciation Expense           amount
Cr   Accumulated Depreciation       amount
```

Both lines carry: the asset's analytic distribution (if any), the source bill's
partner (if exactly one), the asset's currency, the asset link, the period-start
technical date, and a move type of *depreciation*.

`FACT VERIFIED`

## 3. Variations

| Event | Move type | Shape |
|---|---|---|
| Ordinary depreciation | *depreciation* | The canonical two lines |
| Deferred-revenue-style record | *depreciation* | Same two accounts, **signs inverted** |
| Value decrease (downward re-evaluation) | *negative revaluation* | Canonical shape, flagged as a **value change** so the board excludes it from cumulative depreciation |
| Value increase | *positive revaluation* | Dr the gross-increase asset account / Cr a counterpart account |
| Asset creation from a bill | *purchase* | The bill's own entry, typed retrospectively |
| Disposal | *disposal* | Multi-line — `25` |
| Sale | *sale* | Multi-line — `25` |

`FACT VERIFIED` — seven move types.

## 4. Dates, periods and currency

| Aspect | Behaviour |
|---|---|
| Accounting date | **Period end** |
| Period start | A separate technical field on the entry |
| Period boundary | End of month (monthly) or end of fiscal year, capped by fiscal year end |
| Journal | The asset's journal; general type only |
| Company | The asset's |
| Currency | **The asset's, which is the company's.** Amounts are converted at the depreciation date, but since the two currencies are always identical the conversion is an identity |
| Future entries | **Created and posted at confirm**, dated forward |

The currency row is worth stating plainly: the code contains a full currency
conversion path that, given the field definitions, can never do anything. **There is
no foreign-currency asset capability**, despite the code appearing to support one.

`FACT VERIFIED` · `VERIFIED GAP` for foreign-currency assets

## 5. Reversal, re-posting and draft states

- A depreciation entry that is **reversed** causes a **replacement entry** to be
  generated at the following period, carrying the reversed amount, so the board
  stays closed.
- The reversal carries a **negative day count** and inherits the reversal date as
  its period start.
- Where the engine needs to cancel future entries, it **resets drafts and deletes
  them**, and **reverses** anything already posted. Never deletes a posted row.
- An entry cannot be posted against a `draft` asset.
- A move cannot be reset to draft if its asset is not `draft`; drafting it deletes
  any draft assets it created.

`FACT VERIFIED`

## 6. Lock dates

| Path | Lock-date check in this module |
|---|---|
| Disposal / sale | **Present** |
| Re-evaluate / modify | **Present** |
| Pause | **Absent** |
| Confirm (posts the whole life) | **Absent** |

`UNR-09`. Expert 3 rates this High if confirmed; Expert 4 declines to rate an
untested path. The test is specified in `41`.

## 7. Reconciliation — the gap

**There is no sub-ledger to general-ledger reconciliation function.** No report, no
wizard, no scheduled check compares the asset register to the account balances.

`VERIFIED GAP`

Normally this would matter little, because §1 makes them the same rows. Three
mechanisms break that, and all three are live on a migrated population:

| # | Mechanism | Effect |
|---|---|---|
| 1 | **Already depreciated on import** | Reduces the board **with no journal entry**. Sub-ledger and GL disagree **by design** |
| 2 | **Account changed after posting** | The asset's account triple no longer describes its own history; a balance-based reconciliation splits across accounts |
| 3 | **Direct data load bypassing the ORM** | The board invariant is not evaluated | 

Mechanism 1 is the one a migration actually uses. `FAIL-G02`, `CTR-06`.

## 8. Reporting

One dedicated report — the Depreciation Schedule — built as a proper accounting
report with its own hierarchy, plus the standard journal-entry views filtered to
asset entries.

`FACT VERIFIED`

## 9. For SMEsPlus

1. **Inherit "the board is the entries".** It removes an entire class of
   reconciliation problem at the cost of nothing.
2. **Then build the reconciliation anyway**, because the import mechanism and
   account changes will reintroduce divergence and the reference product detects
   neither.
3. Decide deliberately about **posting the whole life at confirm**. It is convenient
   and it means the ledger permanently contains future-dated posted entries.
4. Do not inherit the dormant currency-conversion path. Either support
   foreign-currency assets properly or leave the capability out.
