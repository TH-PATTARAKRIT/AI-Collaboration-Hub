# C07 — ACCOUNT_WAVE_A_DATE_SEMANTIC_MATRIX

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001` · Layer 2 / audit quarantine

> Re-opens `COR-02` / `CONTRA-12`. The parent established that the accounting date is system-derived.
> This forensic separates the seven date concepts the Boss named, establishes which have carriers,
> and states the derivation rule exactly — including a case the parent did not report.

---

## 1. Seven concepts, four carriers

**`VERIFIED FACT`** — enumeration of every date field on the entry
(`account_move.py:337-358`, `:137`, `:707`) and on the item
(`account_move_line.py:70-79`, `:347`, `:398`, `:420`).

| # | Business concept | Carrier | Status |
|---|---|---|---|
| 1 | **Document date** | `invoice_date` on the entry; a stored *related* copy on the item | exists, user-owned |
| 2 | **Accounting date** | `date` on the entry; a stored *related* copy on the item | exists, **system-derived** |
| 3 | **Recognition date** | — | **no carrier.** Collapsed into the accounting date |
| 4 | **Tax date / tax point** | — | **no carrier.** The tax lock and the statutory extracts both operate on the **accounting** date |
| 5 | **Statutory filing date** | — | no carrier in the ledger; it belongs to the return, not the entry |
| 6 | **Due date** | `invoice_date_due` on the entry; `date_maturity` on the item | exists |
| 7 | **Posting timestamp** | — | **no carrier.** Only the framework's generic record-audit fields; there is no accounting fact recording *when* a posting occurred |

One further date exists that the Boss list did not name:

| 8 | **Delivery date** | `delivery_date` on the entry (`:350-357`) — stored, computed, user-overridable | exists; **not found to drive any ledger, tax or reporting behaviour** within `addons/account/models/` and `addons/account/report/` (search boundary stated per `DR-NC-02`). Its presence is notable because in several VAT regimes the supply date *is* the tax point |

### The load-bearing result

> **Three of the seven concepts have no carrier, and the missing one with the greatest consequence is
> the tax date.** Because there is no tax point, the tax lock, the tax return population and the
> statutory extracts all fall back on the accounting date — the one date in the system that the user
> does not control and that the system silently moves.

---

## 2. The derivation rule, stated exactly

**`VERIFIED FACT`** — `account_move.py:5655-5691`, `_get_accounting_date(invoice_date, has_tax, lock_dates)`.

Inputs: the document date; whether the entry carries tax; the violated lock dates. It also reads
`highest_name` — the highest existing number in the journal — and deduces from it a
`number_reset` pattern (`month`, `year`, `year_range_month`, or none).

```
if lock_dates:            invoice_date := latest violated lock date + 1 day

if the document is a SALE document:
    if lock_dates:
        if no highest_name or number_reset == 'month':  return min(today, end_of_month(invoice_date))
        if number_reset == 'year':                      return min(today, end_of_year(invoice_date))
    (no lock -> falls through, returns the document date unchanged)

else  (NON-SALE: vendor bills, and any entry carrying a document date):
    if no highest_name or number_reset in ('month','year_range_month'):
        if (today.year, today.month) > (doc.year, doc.month):  return end_of_month(doc)
        else:                                                  return max(doc, today)
    if number_reset == 'year':
        if today.year > doc.year:                              return 31 December of doc.year
        else:                                                  return max(doc, today)

return invoice_date
```

**`VERIFIED FACT`** — the non-sale branch is entered **without any reference to `lock_dates`**. It is
invoked on every change of the document date (`account_move.py:800-815`, `_compute_date`) and again
at posting (`:4933-4936`).

### Three consequences, one of which the parent did not report

| # | Consequence | Illustration |
|---|---|---|
| A | A vendor bill from a **past month** takes that month's **last day** as its accounting date, with no lock configured | bill dated 15 January, entered 3 March, monthly numbering → accounting date **31 January** |
| B | **NEW — not reported by the parent.** A vendor bill from the **current month** takes **today**, not its document date | bill dated 2 September, entered 4 September → `max(doc, today)` → accounting date **4 September** |
| C | The branch taken depends on `number_reset`, which is **deduced from the highest existing number in the journal** | the accounting date of a bill depends on the numbering format of previously entered documents |

Consequence B means that for non-sale documents the accounting date is, in the ordinary case,
**never the document date** — it is either the end of a past month or today. The parent package
reported only case A and therefore understated the reach: the behaviour applies to routine
same-month entry, not only to late entry.

Consequence C is the "sequence relationship" the Boss asked about, and it is the wrong dependency
direction: **period attribution, an accounting fact, is derived from a numbering format, which is a
presentation artefact derived from existing data.**

---

## 3. The date semantic matrix

| Date | Owner | Source of truth | User editable | Derived | Mutable before posting | Mutable after posting | Lock controlled | Tax relevance | Reporting relevance | Correction method | Historical provenance |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Document date** | the counterparty / the source document | `SOURCE FACT` | **yes** | no | yes | **no** — in the frozen-field list (`account_move.py:3247-3252`) | no | indirect: it drives the accounting date | printed on documents | reset to draft, or reverse | none |
| **Accounting date** | **the system** | `ACCOUNTING FACT` | nominally yes, but **overwritten** by the derivation on every document-date change and at posting | **yes** | yes, but re-derived | **no**, and a change is lock-checked (`:3231-3237`) | **yes** | **yes — this is the field the tax lock and the statutory extracts use** | period attribution | reverse and re-enter | **none — the intended date is not retained** |
| **Recognition date** | — | — | — | — | — | — | — | — | — | — | **no carrier** |
| **Tax date / tax point** | — | — | — | — | — | — | — | — | — | — | **no carrier** |
| **Statutory filing date** | the return | belongs to `WAVE-D TAX` | — | — | — | — | tax lock is set by posting the return | yes | yes | — | on the return |
| **Due date** | payment terms | `SOURCE FACT` | yes | computed from terms, overridable | yes | entry-level: no. Item-level `date_maturity`: **not in the frozen-field list, and outside hash coverage** | no | no | ageing | edit | none |
| **Delivery date** | the source document | `SOURCE FACT` | yes | computed, overridable | yes | not in the frozen-field list | no | **none found in the searched scope** | none found | edit | none |
| **Posting timestamp** | — | — | — | — | — | — | — | — | — | — | **no carrier — "when was this posted" is not an accounting fact** |
| **Maximum match date** | the settlement | `DERIVED FACT` | no | yes | n/a | recomputed | no | inherited by cash-basis entries | ageing placement | unmatch | none |

---

## 4. The vendor-bill chain, end to end

Traced as the Boss required.

```
document timing        bill dated 15 January, received and entered 3 March
        ↓
derivation             _compute_date fires on the document-date change
                       non-sale branch, no lock consulted
                       number_reset deduced from the journal's highest existing number
        ↓
accounting date        31 January  (end of the document's month)
        ↓
sequence               the number is then assigned from the series for that period,
                       and the date/number alignment constraint is satisfied because the
                       date was moved to fit the number, not the reverse
        ↓
lock interaction       if 31 January is itself locked, _get_accounting_date is re-entered
                       at posting and the date moves forward again, to the end of the
                       first open period
        ↓
statutory extract      the Thai VAT and withholding extracts select their population by,
                       and print, this derived accounting date, under a heading that
                       presents it as the document date
```

**`VERIFIED FACT` as to the ledger mechanics.** The final step's statutory *consequence* is
`HOLD / EVIDENCE REQUIRED` and is routed to `WAVE-D TAX`; this session records the ledger implication
only, as required.

### The ledger implication Wave A must preserve

Independently of any statutory question:

1. The ledger contains **no record of the date the business believed the transaction occurred on**,
   once the derivation has run. The document date survives, but the *intended accounting date* does
   not, because it never existed as a separate input.
2. Two entries with identical document dates can carry different accounting dates purely because
   they were entered on different days, or into journals with different numbering formats.
3. Any downstream consumer that treats the accounting date as "the date of the transaction" is
   reading a derived value. Within Wave A's scope, **every** such consumer does.

---

## 5. Corrected claim, replacing the parent's

**Parent claim (`CONTRA-12`)** — "the accounting date is moved by a lock rule and by a
numbering-convenience rule that operates with no lock configured."

**Corrected claim, at supported scope:**

> Within `addons/account`, for any entry carrying a document date, the accounting date is a
> **system-derived value** produced by `_get_accounting_date`. For sale documents the derivation is
> conditional on a violated lock date. For **non-sale documents it is unconditional**: it fires on
> every document-date change and at posting regardless of lock configuration, and returns either the
> end of the document's month, or today, or the end of the first open period — but, in the ordinary
> case, **not the document date**. The branch selected depends on the numbering format deduced from
> the journal's existing highest number.

**Disposition: `CORRECTED` and `RESCOPED`.** The parent's direction was right; its reach was
understated (consequence B) and its boundary was unstated.

---

## 6. Decisions carried forward

| # | Decision | Position |
|---|---|---|
| `DT-01` | Must SMEsPlus carry an explicit **tax point** distinct from the accounting date? | **`RECOMMENDATION` — yes.** Its absence is what forces statutory reporting onto a system-derived field. Content owned by `WAVE-D TAX`; the *carrier* is a Wave A ledger requirement |
| `DT-02` | Must SMEsPlus carry an explicit **recognition date** distinct from the accounting date? | `RECOMMENDATION` — yes, where recognition and period placement can differ; interacts with `WAVE-F` |
| `DT-03` | Must the **intended accounting date** be retained when the system relocates a posting? | **`RECOMMENDATION` — yes.** Without it, a relocation is undetectable after the fact |
| `DT-04` | Must a **posting timestamp** be an accounting fact? | `RECOMMENDATION` — yes; it is a precondition for attesting a close (`ST-14`) |
| `DT-05` | May period attribution ever depend on a numbering format? | **`REJECT`** — reaffirms `ST-22`; the dependency must run the other way |
| `DT-06` | Should the accounting date be user-owned, system-owned, or user-proposed and system-validated? | `UNKNOWN` — **Boss decision** `CL-04`. Wave A recommends *proposed and validated*: the user states intent, the system refuses or requires an override, and never silently substitutes |

---

## 7. Residual unknowns

| # | Unknown | Classification |
|---|---|---|
| `DTU-01` | Whether `delivery_date` drives behaviour in modules outside `addons/account` | `NOT YET SEARCHED` |
| `DTU-02` | Whether any localization introduces a distinct tax point | `NOT YET SEARCHED` — `WAVE-D TAX` |
| `DTU-03` | Whether the framework's record-audit fields are relied on anywhere as a posting timestamp | `NOT YET SEARCHED` |
| `DTU-04` | Thai statutory position on period attribution by derived date | `HOLD / EVIDENCE REQUIRED` → `WAVE-D TAX` |

---

# ADDENDUM A2 — CORRECTIONS FROM FRESH L12 REVIEW

Raised by Fresh Reviewer A. **Each re-verified by the research team.** Body retained unedited; where
it conflicts, **the addendum governs**.

## A2-01 — §1 "recognition date has no carrier" is CONTRADICTED

**Verification: `VERIFIED`.** `account_accountant/models/account_move.py:439` and its neighbours
declare **`deferred_start_date` and `deferred_end_date`** as stored, user-editable date fields on the
journal item, and `:278` and `:313` show a deferred-entry generator that creates real entries for the
periods those dates span. A separate depreciation-start date exists in the asset module.

**Corrected claim.** A recognition date **does** have carriers — but they are
**purpose-specific** (deferral, depreciation), live in modules outside `addons/account`, and there is
**no general recognition date on an arbitrary accounting event**. Row 3 of §1 is restated:
*"No general recognition-date carrier was found in `addons/account`. Purpose-specific carriers exist
in `addons/account_accountant` (deferral) and the asset module (depreciation start)."*

This is the **third** over-scoped negative committed by CORR1 itself. Recorded as `NC-20`.

## A2-02 — §1 versus §3 internal contradiction on the tax point

**Verification: `VERIFIED` — the reviewer is right that this document contradicts itself.**

§1 row 4 states the tax point has **no carrier**. §3 records that the maximum matched date is
"inherited by cash-basis entries" — i.e. a date that determines when tax becomes reportable. Those
two statements cannot both stand.

**Resolution.** A **derived** tax point exists for cash-basis taxes: the reconciliation's maximum
matched date, applied at `account_partial_reconcile.py:513`. There is **no stored tax-point field on
the entry or item**, and for accrual-basis taxes the tax lock and statutory extracts operate on the
accounting date.

Corrected §1 row 4: *"No stored tax-point field was found on the entry or item in `addons/account`.
A derived tax point exists for cash-basis taxes via the reconciliation date. Accrual-basis tax
attribution uses the accounting date."*

`DT-01` is unaffected and is reinforced: a derived, cash-basis-only tax point is not a general tax
point.

## A2-03 — §2 consequence B and the §5 corrected claim are BOTH too wide

**Verification: `VERIFIED` on all four counterexamples.** The research team re-read
`_compute_date` (`:800-815`) and `_get_accounting_date` (`:5655-5691`) and confirms:

| # | Counterexample | Effect on the claim |
|---|---|---|
| 1 | `_compute_date` gates on `is_invoice()`, which **excludes receipts and `entry`-type moves** | "any entry carrying a document date" is **too wide**. The population is **non-sale invoices and refunds** |
| 2 | `number_reset` may be `'never'` or `'year_range'`, which reach neither branch and **return the document date unchanged** (`:5691`) | "in the ordinary case not the document date" is **conditional on the journal's numbering pattern** |
| 3 | `max(invoice_date, today)` returns the **document date** whenever the document is dated today or later | "**never** the document date" is **false** |
| 4 | The posting-time call at `:4934` sits inside `if lock_dates:` | that call **is** lock-gated. Only the `_compute_date` path is not |

**Corrected claim, replacing §5.**

> Within `addons/account`, for **non-sale invoices and refunds** whose journal numbering resets
> monthly or yearly, the accounting date is derived from the document date by `_get_accounting_date`
> on every document-date change — **this path is not gated on any lock date**. It returns the end of
> the document's period when the document's period is past, and otherwise the later of the document
> date and today. Journals whose numbering does not reset by period return the document date
> unchanged. At posting, a **second, lock-gated** derivation may move the date again. Sale documents
> are re-dated only when a lock is violated.

The word **"never"** at line 81 of the body is **withdrawn**.

**What survives, and it is still the finding:** for a common and default configuration — a vendor
bill in a monthly-numbered purchase journal, entered after its month — the accounting date is moved
**with no lock configured**, and the intended date is not retained. `SF-03` stands; its population is
narrower and must be stated as above.

## A2-04 — §4 statutory chain independently confirmed

**Verification: `VERIFIED` as to ledger mechanics.** The reviewer independently confirmed that the
Thai VAT extract selects on the accounting date and prints it under an invoice-date heading.

**Statutory consequence remains `HOLD / EVIDENCE REQUIRED`, routed to `WAVE-D TAX`.** This session
records only that the extract reads a derived field. Thai names remain candidate / UNVALIDATED.

## Addendum summary

| # | Effect | Verification |
|---|---|---|
| `A2-01` | Recognition-date negative contradicted — **third CORR1 over-scoped negative** | `VERIFIED` |
| `A2-02` | Internal §1/§3 contradiction resolved; a derived cash-basis tax point exists | `VERIFIED` |
| `A2-03` | Population narrowed; "never" withdrawn; one of three paths is lock-gated after all | `VERIFIED` |
| `A2-04` | Statutory chain confirmed as ledger mechanics; consequence stays `HOLD` | `VERIFIED` |

**The matrix's decisions are unchanged.** `DT-01`–`DT-06` all stand. What changed is the **scope**
of the behaviour, not its existence or its consequence — which is the exact distinction the
negative-claim standard was written to enforce, and which this document failed to observe.
