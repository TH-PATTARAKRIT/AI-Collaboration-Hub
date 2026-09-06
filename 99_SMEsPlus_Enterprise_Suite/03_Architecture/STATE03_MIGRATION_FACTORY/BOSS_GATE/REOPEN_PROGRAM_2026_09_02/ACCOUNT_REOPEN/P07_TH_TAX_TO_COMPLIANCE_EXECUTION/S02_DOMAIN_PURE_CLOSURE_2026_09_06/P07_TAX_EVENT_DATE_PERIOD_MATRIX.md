# P07 — TAX EVENT / DATE / PERIOD MATRIX

Round `SMEPLUS-26-09-06-…-002`. `LAYER 2 — AUDIT QUARANTINE`.
Answers `CQ-P07-01`, `CQ-P07-02`, `CQ-P07-06`. Deepens `04_P07_TAX_POINT_MATRIX.md`; **replaces
nothing in it.**

> `CQ-P07-02` says: *do not collapse different dates into one field merely because the reference
> implementation does.* This file keeps five dates apart and states, for each, whether the estate
> carries it, whether anything reads it, and what the statute needs.

## 1. The Five Dates, Kept Separate

| # | Date | What it is | Statutory relevance | Carrier in the estate | Read for tax-period selection? |
|---|---|---|---|---|---|
| `D-1` | **Business / economic event** | delivery, ownership transfer, service performance or utilisation | the tax point itself for goods (`S-01`) and for services used before payment (`S-02`) | **none on the tax fact.** Delivery lives in P02/Inventory, service utilisation in P02/P05 — `X-04`, `X-05`, both `BLOCKING for P07` | **no — no carrier exists to read** |
| `D-2` | **Document / tax-invoice date** | the date printed on the statutory document | fixes the tax month for notes (`S-13`, `S-14`, `S-23`, `S-24`) and bounds the input-tax claim (`S-09`) | `account.move.invoice_date` | **no.** One display column only (`l10n_th_reports_ext/models/tax_report_vat.py:175`, header "Bill Date") |
| `D-3` | **Recognition / posting date** | the date the ledger entry belongs to | **none.** It is an accounting attribute | `account.move.date` | **yes — it is the sole selector, for every tax report in the declared set** |
| `D-4` | **Payment / settlement date** | when consideration moves | **the** withholding tax point (`S-30`); remittance runs 7 days from it (`S-32`); the cash-basis VAT tax point (`S-02`) | P06's; **user-settable and mutable**, and P06 states that changing it silently drops the whole withholding (`PI-02`, citing P05 `TX-03`) | **no.** The PND branch dates the fact by the **invoice** (`P07-F-11`, `W-C-01`) |
| `D-5` | **Filing / statutory period** | the month whose return the fact belongs to | the unit of every return | **derived from `D-3` at query time.** No stored period, no period state | derived, never stored |

**The inversion, restated in one line:** the only date the system selects on is the **one date
with no statutory relevance**.

## 2. The Carriers That Exist For `D-2`/`D-5` — Measured, Not Asserted

New this round. Full evidence at `P07_SOURCE_LINK_AND_EVIDENCE_SUPPLEMENT.md §5`.

| carrier | level | defined by | present in | read for selection |
|---|---|---|---|---|
| `account.move.tax_period` | **entry** | `scgl_tax_period_date` | **3 of 7 identities** | **no** — display column only |
| `account.move.line.tax_period_date` | **item** | `scgl_tax_period_date` | **3 of 7 identities** — the same three | **no** — one readonly, `optional="hide"` list column |

Three consequences, and each is a separate statement:

1. **A tax-period carrier exists at item granularity.** P10's `FACT VERIFIED` that it is *absent
   from the item* is **CONTRADICTED** (`P07-F-107`). The two carriers are co-present and
   co-absent because one module defines both; "entry yes, item no" is not a reachable state.
2. **Both are inert.** Present at two levels, read for selection at neither. The predecessor
   file carried `COALESCE(tax_period, date)` and the current file does not (`04 §4`): **the tax
   point was demoted from a selector to a decoration, and a column was added showing the reader
   a date the report did not use.**
3. **Four of seven identities have no tax-period carrier at all.** Any design that assumes one
   is designing for 3 of 7 deployments on this host.

## 3. What the Thai Localisation Contributes to Dates — Nothing

`EP-2`, `EP-2b`, `EP-4b`: the installed Thai localisation set adds **18 fields across 8 shared
accounting models**, and **not one is a date, a period or a tax point**. Every one is a
withholding attribute or a branch string.

**`P07-F-105`. The statutory tax point has no carrier in the Thai localisation.** The only
carriers that exist anywhere in the estate come from `scgl_tax_period_date`, a **non-localisation
custom module installed in 3 of 7 identities** — so the tax point is not merely mis-selected, it
is **not a localisation concept in this estate at all.**

This is the sharpest available statement of `O-03`: *P07 owns tax-period membership, and the
implementation delegates it to P08's accounting date.* It is now measured rather than argued.

## 4. Period Crossing — `CQ-P07-06`

Each row is a boundary crossing and what the estate does at it. `TPF-01`…`TPF-05` (`04 §5`) are
the worked cases; this is the general statement.

| # | Crossing | Statutory expectation | Estate behaviour | Class |
|---|---|---|---|---|
| `PX-01` | `D-1` and `D-3` fall in different months (goods delivered Sept, posted Oct) | tax point is `D-1` (`S-01`) | reported in `D-3`'s month; `D-1` has no carrier | `CONTRADICTED` — `P07-F-02`, `P07-F-03` |
| `PX-02` | `D-2` and `D-3` differ (vendor invoice dated Sept, received and claimed Oct) | the deferred-claim rule governs, and is **held** at `P07-U-03` | selected by `D-3`; the user's `tax_period` entry is displayed and ignored — `TPF-02` | `CONTRADICTED` on mechanism; **statutory half `UNRESOLVED`** |
| `PX-03` | `D-4` and `D-2` differ (bill Sept, paid Oct) | withholding tax point is `D-4` (`S-30`); remittance due 7 days from it (`S-32`) | the PND reports it in **September**, the month before the tax existed; October contains nothing — `TPF-04` | `CONTRADICTED` — `P07-F-11`, `W-C-01` |
| `PX-04` | Note issued in a month later than the document it corrects | note's own month (`S-13`, `S-14`, `S-23`, `S-24`) | accounting date of the reversal entry, which an accountant will commonly back-date to match — `TPF-03` | `CONTRADICTED` — `P07-F-07` |
| `PX-05` | Fiscal-year boundary | same rules; no special treatment | not separately modelled; the same single selector | `UNRESOLVED — EVIDENCE REQUIRED` — no statutory source held on year-boundary treatment beyond the monthly rule |
| `PX-06` | A fact moves period **after** the period was filed | whether a filed period may change at all is statute | nothing prevents it: no tax-period state exists, the only control is P08's accounting lock (`A-14`), and un-reconciling is not lock-gated (`PI-02`, corroborated by P08 `REC-11` and P02 `P02-F-46`) | **`BOSS DECISION REQUIRED`** — mechanism named, statute held |

**`PX-06` is the one that cannot be closed by evidence.** P06, P07 and P05 independently hold
the same statutory question in the same state (`MD-06`). That is a correct outcome, not a gap,
and it is **not converted into a research round.**

## 5. Requirement Restatement — `TPR-01`…`TPR-05` Re-tested

`04 §6` stated five requirements. This round tested whether any is now closable.

| # | Requirement | Change this round | Still blocked by |
|---|---|---|---|
| `TPR-01` | a tax point attribute on the **tax fact**, mandatory, sole selector | **strengthened, not closed.** The carrier exists at both levels in 3 of 7 (`P07-F-107`) — so "mandatory" and "sole selector" are the two missing properties, not "exists" | `P07-F-02`, `P07-F-03` — a design act, not evidence |
| `TPR-02` | tax point derivable per transaction class | unchanged | `TP-01`…`TP-07`; `D-1` has no carrier at all |
| `TPR-03` | withholding tax point = the payment; reported fact = the posted withholding line | **counterparty half committed.** P06's `P07-R-01` supplies an immutable settlement date | the **reporting key** is P07's — `P07-F-11` |
| `TPR-04` | notes carry their own date and the original reference | unchanged | `P07-F-07` |
| `TPR-05` | legal basis for a deferred input-tax claim | unchanged | `P07-U-03` — `HOLD — STATUTORY EVIDENCE REQUIRED`; `AASR-P07-VETO-01` rests on it |

**Not one of the five closed.** Two moved from *no counterparty position* to *counterparty half
committed*. That is progress in the dependency, not in the finding.
