# P01 — SERIES-16 PERIOD CLOSE / CUT-OFF MATRIX

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S16-08` · Deployment `45a8e08e`

---

## 1. THE CONTROL ENVIRONMENT

| Lock | Value |
|---|---|
| `period_lock_date` | **NULL** |
| `fiscalyear_lock_date` | **NULL** |
| `tax_lock_date` | **NULL** |
| `po_lock` | `edit` |

**No period is closed in the accounting sense.** Every statement below describes behaviour in a system where
nothing refuses and nothing re-dates, because there is no boundary to enforce.

---

## 2. BILL CUT-OFF — MEASURED ON A CLEAN-DATED POPULATION

**POPULATION:** 36,867 posted vendor bills. **Excluded: 2** — one with `invoice_date` year 2568, one with 1967.
**Clean population: 36,865.** The exclusion is declared because two rows would otherwise drive the extremes.

| Measure | Value |
|---|---|
| days(`date` − `invoice_date`) min | **−105** |
| p10 | **−6** |
| **p50** | **0** |
| p90 | 0 |
| max | **+366** |
| Same month | 34,828 |
| **Different month** | **2,037 (5.53%)** |
| **Posted EARLIER than the invoice date** | **5,601 (15.19%)** |
| Posted more than 31 days after | 25 |

### 2.1 The median is the reassuring number and the tail is the finding

The typical bill is posted **on its invoice date** (p50 = 0, p90 = 0). Recognition is not systematically late.

But **15.19% of posted vendor bills carry an accounting date EARLIER than the vendor's own document date**,
p10 at −6 days and reaching −105. The liability and expense are recognised in the ledger **before the document
that evidences them is dated**. And **2,037 bills (5.53%) land in a different month from their invoice date.**

**This is the opposite direction from the series-18 OCC deployment**, where 0 of 1,879 bills crossed a month
and 1,747 carried a deliberate month-end date. Two deployments, two conventions, and only one of them keeps
recognition inside the document's own period.

**CLASSIFICATION: `FACT VERIFIED` as to the distribution. Whether pre-dating is a deliberate accrual practice
or an uncontrolled default is `UNRESOLVED — EVIDENCE REQUIRED`**, and the judgement is **P08's**, not P01's.

---

## 3. BUDDHIST-ERA DATE LEAKAGE

**Sweep of every date column on `account_move` — a bounded sweep, see the correction below:**

| Column | Rows with year > 2100 | Years |
|---|---|---|
| `date` | **30** | 2567 |
| `invoice_date` | **1** | 2568 |
| `invoice_date_due` | 0 | — |

The 30 are **all `move_type = entry`, all POSTED**, named `CABA2567…`, dated `2567-04-10` and similar.
BE 2567 = CE 2024.

**Consequence.** A Gregorian date column holding a Buddhist-era year places those entries **543 years in the
future**. Any fiscal-year close, ageing bucket, period report or date-bounded query treats them as year 2567:
they will never fall inside a current-period selection, and they will never age.

> ### CORRECTED — the leakage is 16× wider than this
>
> AAS-03 Expert 2 swept **every date column in every extracted table**, which this section did not:
> **484 Buddhist-era values across 14 columns in 11 tables**, plus **11 values at year 8202** — a second,
> undiagnosed class. And it is **bidirectional**: 30 moves carry a BE `date` with a sound `tax_period`,
> while **7 carry a sound `date` with a BE `tax_period`**.
>
> **No date column in this database is reliably Gregorian**, and a sweep bounded to `account_move`
> could not have discovered that. The "full sweep" in the table above was full only of *one table*.
>
> The BE items are **balanced**, so the trial balance still balances and nothing draws attention to them.
> They touch Input VAT ฿7,396.98, Undue VAT ฿7,396.98 and Dummy Service ฿211,342.14, and they are
> **period-invisible with all three lock dates NULL**.

*Separately, 1,733 moves are dated 2005–2012 — opening and migration data, recorded so the early tail is not
mistaken for the same defect.*

**CLASSIFICATION: `FACT VERIFIED`.** Whether these were written by code or imported is
**UNRESOLVED — EVIDENCE REQUIRED**; determining it was assigned to AAS-03 Expert 4, including whether the
installed `scgl_tax_period_date` module is implicated.

---

## 4. RECEIPT-BEFORE-BILL CARRY-FORWARD

Because the GRNI bridge executes here (see `P01_S16_RECEIPT_VALUATION_CLEARING_DIRECT_PROOF.md §6`), a receipt
in one period and its bill in another **is carried in the ledger** by account 39, not left off-ledger.

| Measure | Value |
|---|---|
| GRN account net at archive date | **฿72,097,814.25** |
| Received-not-invoiced on PO lines | 79 lines, ฿12,678,776.50 |
| Invoiced-not-received | 49 lines, ฿11,512,304.52 |

**The GRN residual is an order of magnitude larger than the PO-line received-not-invoiced position.**
That is consistent with §1 of the AP trace — most bills are not PO-linked, so the PO-line comparison sees only
a slice — but the gap is **not explained** by this package and is handed to P08 and P11.

---

## 5. MATRIX

| Cut-off path | Behaviour here | Classification |
|---|---|---|
| Bill posted before its invoice date | occurs in **5,601 of 36,865** | **FACT VERIFIED**; intent unresolved |
| Bill posted in a different month | **2,037 of 36,865** | **FACT VERIFIED** |
| Receipt in one period, bill in another | carried by GRN account 39 | **FACT VERIFIED** |
| Reversal in a different month from its original | **22** | **FACT VERIFIED** |
| Reversal dated before its original | **2** | **FACT VERIFIED** |
| Lock refuses a late posting | **cannot — no lock configured** | **NOT REACHABLE** |
| Lock silently re-dates a late posting | **cannot — no lock configured** | **NOT REACHABLE** |
| BE-year entries in period selections | 30 `date` + 1 `invoice_date` | **FACT VERIFIED** |
