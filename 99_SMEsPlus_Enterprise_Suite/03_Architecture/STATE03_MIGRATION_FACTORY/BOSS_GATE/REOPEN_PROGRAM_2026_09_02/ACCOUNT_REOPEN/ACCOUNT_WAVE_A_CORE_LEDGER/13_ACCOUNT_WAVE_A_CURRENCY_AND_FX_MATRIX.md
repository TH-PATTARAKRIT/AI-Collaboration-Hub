> **CORR1 CORRECTION NOTICE.** Amended by session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`.
> Corrections landing here: `COR-10, COR-11, COR-14`. Governing text where they conflict with the body below: CORR1/C06 governs the missing-rate row.
> Prior findings are retained unedited for lineage; see `CORR1/C02_..._ACCEPTED_CORRECTIONS_REGISTER.md`.

# 13 — ACCOUNT_WAVE_A_CURRENCY_AND_FX_MATRIX

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

## 1. The required chain, established

> `Transaction Fact → Currency Fact → Valuation Fact → Settlement Fact → Reporting Fact`

| Link | What it asserts | Carrier in the reference | Evidence | Status |
|---|---|---|---|---|
| **Transaction fact** | the amount agreed, in the currency agreed | the item's transaction-currency amount; the currency is **required on every item**, always | `EV-013` | carried |
| **Currency fact** | the measurement applied, on a date | one scalar rate per currency per day per company root, with genuine database constraints | `EV-018` | carried |
| **Valuation fact** | the company-currency amount recorded | the item's balance — **the canonical stored amount**, from which debit and credit derive | `EV-013` | carried |
| **Settlement fact** | what was actually discharged, and the difference that arose | the matching record's three amounts, and the exchange-difference entry it emits | `EV-014` | carried |
| **Reporting fact** | the amount as presented, on a chosen basis | closing, historical, average and current rates **synthesised at query time** from the daily series | `COR-10` | carried |

**All five links exist.** This is the cleanest chain in Wave A — and the correction that established
the fifth link (`COR-10`) also revealed the right principle: **measurement is stored once per date;
valuation bases are derived per reporting purpose.**

## 2. Currency and FX matrix

| Aspect | Reference behaviour | Evidence | SMEsPlus position |
|---|---|---|---|
| Company currency | one per company | `EV-013` | `ADAPT` |
| Transaction currency on the item | **required, always**, even when identical to the company currency | `EV-013` | `ADAPT` — removes an entire class of ambiguity |
| Journal currency | must agree with the journal's default account currency | `EV-019` | `ADAPT` |
| Account currency | optional; forcing it is refused once items exist in another currency | `EV-019` | `ADAPT` |
| Two amounts per item | company-currency balance and transaction-currency amount | `EV-013` | `ADAPT` |
| Sign agreement | **database-enforced** — the two amounts must share a sign | `COR-06` | `ADAPT` — one of only four storage-level guarantees found |
| Magnitude protection | **none** — the transaction-currency magnitude is neither write-guarded nor hash-detected | `CONTRA-01b` | `EXTEND` |
| Hash precision | company-currency amounts are serialised at the **transaction** currency's decimal places, creating a collision vector | `COR-11` / `CONTRA-06` | `EXTEND` |
| Rate storage | one per currency per day per company root; unique constraint; positive-value check | `EV-018` | `ADAPT` |
| Rate resolution | latest rate on or before the date; else the earliest rate ever; else **1.0** | `COR-14` | **`REJECT` the fallback** |
| **Missing rate** | **silently converts at par, producing a valid-looking entry** | `CONTRA-08` | **`REJECT` — must halt the posting** |
| Rate types | `current`, `closing`, `historical`, `average` — **derived at query time**, not stored | `COR-10` | `ADAPT` the derivation model |
| Rate correction | one rate per day is replaceable; effect on already-posted entries not traced | `GAP-H02` | `UNKNOWN` |
| Realised FX | recognised on settlement, emitted automatically by matching | `EV-014` | `ADAPT` |
| Unrealised FX / revaluation | **no posting mechanism found** in the scope read; a closing rate for presentation is user-typable and not stored | `GAP-H01`, Expert 3 | `EXTEND` — SMEsPlus must design this |
| Historical rate on non-monetary items | derivable for reporting; **no mechanism to pin a rate to a fact** | `COR-10` | `EXTEND` |
| Rounding | currency decimal places are a stored precision; cash rounding is separate configuration | `EV-018` | `PC` |
| Reversal | mirrors the original's currency and amounts | `EV-012` | `ADAPT` |
| Multi-company | rates are held per company **group**, not per company | `EV-018` | see file 16 |
| Financial statement presentation | consolidation translation uses the derived rate table | `COR-10` | `WAVE-G REPORTING` |

## 3. Realisation and revaluation — distinguished

Answering Boss question 18 explicitly:

| | Realised | Unrealised |
|---|---|---|
| Trigger | **settlement** — a matching record between items measured differently | **the passage of a reporting date** with the obligation still open |
| Nature | an **accounting event** — a posted entry | a **valuation restatement** — not a settlement |
| Reference mechanism | emitted automatically by reconciliation | **none found for posting**; a derived rate exists for presentation |
| Reversibility | reversed automatically when the match is undone | must be reversed at the start of the next period, or restated |
| Wave A position | `ADAPT` | `EXTEND` — design required |

**The distinction the reference model makes, and SMEsPlus should keep:** realisation is caused by an
*event* (settlement); revaluation is caused by a *date*. Only the first belongs to the settlement
mechanism. Conflating them is the classic error, and the reference model avoids it — by not
implementing the second at all.

## 4. Currency risks carried forward

| # | Risk | Class | Severity |
|---|---|---|---|
| `FX-01` | Missing rate converts at 1:1, silently, producing an internally consistent wrong entry | `CONTRA-08` | **highest in Wave A** — `Tolerance = 0` candidate |
| `FX-02` | Transaction-currency magnitude is unprotected on a secured entry | `CONTRA-01b` | high |
| `FX-03` | Hash rounds company-currency amounts at the wrong currency's precision | `CONTRA-06` | high, compounds `FX-02` |
| `FX-04` | No posting mechanism for unrealised FX or revaluation | `GAP-H01` | design gap |
| `FX-05` | No way to pin a historical rate to a specific non-monetary fact | `COR-10` | design gap |
| `FX-06` | Effect of correcting a past rate on already-posted entries is unestablished | `GAP-H02` | `UNKNOWN` |
