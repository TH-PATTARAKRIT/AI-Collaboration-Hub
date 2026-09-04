# P10 — EVENT TO GENERAL LEDGER MATRIX

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1

Maps each business event to the ledger effect it produces, the identity that effect carries, and the control that governs it.

---

## 1. Deferred Revenue

| # | Business event | Ledger effect | Date used | Identity carried | Governing control |
|---|----------------|---------------|-----------|------------------|-------------------|
| `DR-1` | Customer invoice posted with a service window | Income account debited, deferred revenue credited, full amount | The invoice's accounting date | Link to the source document only | Account-type eligibility, form-level |
| `DR-2` | A month of the window elapses | Deferred revenue debited, income credited, that month's share | That month's end, **unless a lock moves it** | Link to the source document only | None specific |
| `DR-3` | Source document reset to draft | Every generated effect unlinked, cancelled or reversed — decided per entry | Re-derived for reversals; original for unlinks | Per-entry | Refused if the deferral groups several sources |
| `DR-4` | Grouped generation run at a period end | Deferred revenue and income adjusted to the cumulative correct position | The period end | Many-to-many to all contributing sources | Lock-date guard; month-end guard; a date-and-state duplicate proxy |
| `DR-5` | The next day after `DR-4` | The whole of `DR-4` reversed | Period end + 1 day | Link to `DR-4` | Structural, unconditional |

**Deferred expense is `DR-1`..`DR-5` with the direction reversed and an asset-side control account. No separate row set exists.**

## 2. Accrual

| # | Business event | Ledger effect | Date used | Identity carried | Governing control |
|---|----------------|---------------|-----------|------------------|-------------------|
| `AC-1` | Operator accrues a set of open orders at a cut-off | Expense or revenue recognised against a current liability or current asset | The chosen cut-off | **None** — the link to the orders is dead code | Single company and single currency, both enforced by refusal |
| `AC-2` | Immediately, at the same instant | `AC-1` reversed | Cut-off + 1 day, operator-editable | Link to `AC-1` | Reversal date must be after the accrual date |
| `AC-3` | The real invoice later arrives | An ordinary purchase or sales entry | Its own date | No link to `AC-1` | **None** — nothing reconciles the estimate to the actual |

## 3. Depreciation and Loan (comparators)

| # | Business event | Ledger effect | Identity carried |
|---|----------------|---------------|------------------|
| `AS-1` | Asset confirmed | Board created; past periods posted, future periods held | Entry carries the asset link and a period beginning date |
| `AS-2` | Asset modified | A catch-up stub is cut at the modification date, then the remainder re-derived | As above |
| `AS-3` | Asset disposed | Disposal entry with gain or loss | As above |
| `LN-1` | Loan confirmed | The entire schedule materialised: principal and interest per period, plus long-term/short-term reclassification and its next-day reversal | **Entry carries the individual schedule-line link and an entry-type flag** |

## 4. The Control Column, Consolidated

| Control | Deferral (validation) | Deferral (grouped) | Accrual | Depreciation | Loan |
|---------|----------------------|--------------------|---------|--------------|------|
| Duplicate generation | source-document state | date-and-state proxy — **defeated twice under challenge** | **none** | posted entries never rewritten | **none in the confirm path** |
| Company boundary | **policy read from the wrong scope** | **no company guard at all** | **enforced by refusal** | enforced | enforced |
| Currency integrity | cannot represent a currency | cannot represent a currency | partial, and its counterpart line is defective | cannot represent a currency | cannot represent a currency |
| Period-close | **silent re-date** | refusal | silent re-date | explicit guards, refusal | none of its own |
| Lineage to source | many-to-many, no company check | many-to-many, written by raw SQL | **dead code** | object link | **schedule-line link** |
| Teardown integrity | per-entry, mixed outcomes | as validation | n/a | future entries removed, posted retained | three paths correct, **one orphans posted entries** |

Reading down the columns: the accrual mechanism is the strongest on scope and the weakest on lineage; the loan mechanism is the strongest on lineage and among the weakest on duplication; the deferral mechanism is the weakest overall and is the one the Accounting module depends on most.

## 5. The Two Ledger Effects That Have No Business Event

1. **A recognition entry re-dated by a lock.** The ledger records an effect in a period no business event corresponds to. Nothing in the entry states which period the amount belongs to.
2. **A grouped deferral generated with a multi-company selection.** The ledger of the active company records an effect arising from another company's business events. Whether this posts or is refused depends on whether the chart of accounts is shared — see `11_P10_CONTRADICTION_REGISTER.md` `P10-C-02`.

Both are cases of `TR-6` existing without a corresponding, correctly-scoped `TR-5`. Both disappear under a kernel that makes `TR-5` a first-class object.

## 6. Requirements Falling Out of This Matrix

| # | Requirement for SMEsPlus | Driven by |
|---|--------------------------|-----------|
| `R-01` | Every ledger effect produced by a schedule must carry the identity of the recognition event that justified it, in one hop. | §4 lineage row |
| `R-02` | Every recognition event must carry the period it belongs to, independently of the date its posting carries. | §5 case 1 |
| `R-03` | Structural reversals must be typed distinctly from corrective reversals. | `DR-5`, `AC-2`, `LN-1` |
| `R-04` | An estimate (`AC-1`) must carry a link to the actual that settles it (`AC-3`), and the settlement must be reportable. | `AC-3` |
| `R-05` | Generation must refuse when the owning company cannot be proven, in every mechanism, as the accrual wizard already does. | §4 company row |
| `R-06` | Teardown of a schedule must resolve its generated effects before the schedule is destroyed. | §4 teardown row |
| `R-07` | Duplicate control must key on the recognition event, never on a date-and-state proxy. | §4 duplicate row |
