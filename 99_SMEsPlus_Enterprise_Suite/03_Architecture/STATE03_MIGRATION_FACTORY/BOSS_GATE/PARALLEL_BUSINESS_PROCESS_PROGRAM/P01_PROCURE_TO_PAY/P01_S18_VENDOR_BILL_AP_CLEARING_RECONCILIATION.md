# P01 — SERIES-18 VENDOR BILL / AP / CLEARING RECONCILIATION

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S18-07`
Method: **read-only.** No transaction was created, no database was modified.


> ### PEER DELTA APPLIED — BOUND TO ONE IDENTITY
>
> Peer **P04** (`9e377e30`, `P04-F-101`) records **three** series-18 database identities on this
> host, not one: `551ab874` (361 modules — the one analysed here), `4b766580` (478 modules), and
> `96548e18` (`T805efaplus`, 123 modules, never transacted). **Everything in this document is
> bounded to `551ab874` @ 2026-08-30** and is not a claim about the series-18 generation as
> deployed elsewhere. See `P01_S18_PEER_DELTA_HANDOFF.md §2.2`.

---

## 1. POPULATION

| Object | Rows |
|---|---|
| `account_move` `move_type = in_invoice` | **1,904** (posted 1,879) |
| `account_move` `move_type = in_refund` | **1** |
| Journal items on vendor bills | **6,914** |
| — `display_type = product` | 3,375 |
| — `display_type = tax` | 1,635 |
| — `display_type = payment_term` | 1,904 |
| `account_payment` | 3,508, of which **1,183 supplier** |
| `account_partial_reconcile` | 5,071 |
| `account_full_reconcile` | 2,343 |

Bill accounting dates run 2026-01-31 → 2026-08-30. Companies 1 and 2 only.

---

## 2. WHERE A VENDOR BILL POSTS

| Account type | Journal items on vendor bills |
|---|---|
| `expense_direct_cost` | 2,814 |
| `liability_payable` | 1,894 |
| `asset_current` (input VAT) | 1,635 |
| `expense` | 477 |
| `liability_current` | 51 |
| `asset_cash` | 36 |
| `income` | 4 |
| `liability_non_current` | 2 |

Largest product-line accounts: **186 (`510000 Cost of Revenue`, company 1) — 1,062 lines**;
**72 (`510000`, company 2) — 966 lines**.

**No vendor bill line posts to a stock valuation account or to the `210300` clearing account.**
The bill recognises expense and a payable directly. Under periodic valuation this is the correct
and only available treatment: there is no interim balance to clear, because the receipt created none.

---

## 3. THE CLEARING BRIDGE IS BYPASSED, NOT BROKEN

| Question | Answer | Evidence |
|---|---|---|
| Does the receipt post to the clearing account? | No | 0 items on accounts 176/62/100/138 |
| Does the bill post to the clearing account? | No | 0 of 3,375 product lines |
| Is there anything for the bill to clear? | No | the receipt created no interim balance |
| Is the bridge broken? | **No — it is not engaged** | policy is `manual_periodic`; the gate at `stock_valuation_layer.py:81` never opens |

**There is no reconciliation failure here.** A failure would be a clearing balance that never
clears. What exists is a clearing account that is never used, and a chain in which receipt and bill
are connected by **quantity** (`purchase_order_line.qty_received` / `qty_invoiced`) and not by
**value in the ledger**.

---

## 4. THE TIMING DIFFERENCE, AND WHAT CARRIES IT

Under a perpetual bridge, receipt and bill are held together by a reconcilable interim balance.
Here the only link between them is the quantity fields on the purchase order line.

| Position (orders not `cancel`/`draft`; **tax-exclusive**, THB) | Lines | Value |
|---|---|---|
| Received not invoiced — **tax-exclusive** | **1,580** | **฿29,029,467.66** |
| — of which backed by a goods receipt | 1,411 | ฿27,490,865.80 |
| — of which operator-typed service quantities, **no receipt document** | 169 | ฿1,538,601.86 |
| Invoiced not received — tax-exclusive | 183 | ฿1,663,518.07 |
| *(as first published, mixing two tax bases — `ERR-P01-28`)* | *1,580* | *฿30,080,689.78* |

**No accrual is booked.** 0 of 15,522 journal entries carry `accru` in `ref`
(*positive control:* 15,434 of 15,522 have a non-empty `ref`).

So between receipt and bill the obligation is carried **only by the purchase order document**, not
by the ledger. The exposure is a completeness question at any reporting date, and it is raised in
`P01_S18_GRNI_CLEARING_ACCOUNT_PROOF.md §6` rather than decided here.

---

## 5. BILL POSTING BEHAVIOUR — A CANDIDATE CUTOFF FINDING THAT DID NOT SURVIVE

**The candidate.** 1,667 of 1,879 posted vendor bills have an accounting `date` different from
their `invoice_date` — median **+13 days**, maximum **+30**, and **never negative**. On its face
this looks like systematic late posting and a cutoff risk.

**The discriminating test.** Recompute by month and by day-of-month:

| Test | Result |
|---|---|
| Bills whose `date` falls in a different **month** from `invoice_date` | **0 of 1,879** |
| Bills whose accounting date is the **last day of its month** | **1,747 of 1,879** |
| Next most common day | day 25 — 124 bills |
| Remaining | 8 bills across days 27–30 |

**This is a month-end posting convention, not a cutoff violation.** Every bill is recognised in
the month of its own invoice date; the accounting date is set to the period end (or to a day-25
cut-off) while the invoice date preserves the vendor's document date. That is orthodox.

**The candidate finding is withdrawn before publication**, and is recorded here rather than deleted
because the withdrawal is the useful part: the aggregate `date != invoice_date` statistic was
directionally alarming and substantively meaningless. It is registered in
`P01_FALSE_ZERO_CONTROL_REGISTER.md §7` as a **false-positive** counterpart to the false-zero class.

---

## 6. AP RESOLUTION AND PAYMENT

| Measure | Value |
|---|---|
| AP journal items on vendor bills | 1,894 (credit ฿52,771,761.21, debit ฿0.00) |
| …of which `reconciled` | **1,370 (72.3%)** |
| All AP journal items in the ledger | 3,008 |
| …of which `reconciled` | 2,045 (68.0%) |
| Net open AP residual | **฿8,909,098.18** |
| Supplier payments | 1,183 of 3,508 |

Reconciliation machinery is in active use — 5,071 partial and 2,343 full reconciliations. The
receipt-to-bill leg is the only leg of the chain not carried in the ledger.

---

## 7. TEN BILLS WHOSE LIABILITY IS OUTSIDE THE PAYABLES SUBLEDGER

Ten of the 1,904 payment-term lines sit on accounts that are **not** of type `liability_payable`:
nine on `218001 เจ้าหนี้อื่น` (`liability_current`, ฿1,788.27 total) and one on
`221002 เจ้าหนี้เช่าซื้อ/ลีสซิ่ง - ระยะยาว` (`liability_non_current`, ฿11,181.00). All posted, all
company 2. Full list in `P01_S18_RECEIPT_VALUATION_ACCOUNTING_TRACE.md §7`.

Total ฿12,969.27 — immaterial in amount, structural in kind: an ageing or a payment-matching
routine scoped to the payable account type will not see them.

**CLASSIFICATION: FACT VERIFIED.** Intent **UNRESOLVED — EVIDENCE REQUIRED**. Handed to P08 and P11.

---

## 8. INPUT VAT

1,635 tax lines on vendor bills, all on `asset_current` accounts. `l10n_th 18.0.2.0` is installed.
Withholding-tax structures exist in the schema (`account_withholding_tax`, `withholding_tax_cert`,
`withholding_tax_cert_line`, `withholding_tax_report`, and `account_payment.wt_tax_id` /
`wt_cert_cancel`). Their deployed exercise is examined by AAS-03 Expert C and reported in
`P01_S18_AAS03_FRESH_CHALLENGE.md`.

**No statutory conclusion is drawn here.** Thai VAT and withholding-tax statutory questions belong
to **P07**. Any conclusion that would require statutory authority is recorded as
`HOLD — STATUTORY EVIDENCE REQUIRED` and routed there. Source behaviour is not statutory truth.

---

## 9. CLASSIFICATION SUMMARY

| Item | Classification |
|---|---|
| Vendor bills post expense + payable directly | **FACT VERIFIED** |
| No bill line reaches a valuation or clearing account | **FACT VERIFIED** |
| The clearing bridge is bypassed, not broken | **SUPPORTED INTERPRETATION** — rests on the policy proof |
| Receipt and bill are linked by quantity, not by ledger value | **FACT VERIFIED** |
| ฿29,029,467.66 tax-exclusive received-not-invoiced, unaccrued | **FACT VERIFIED** on a declared basis; ฿30,080,689.78 as first published is **CORRECTED — `ERR-P01-28`** |
| Month-end posting convention, not a cutoff violation | **FACT VERIFIED** — candidate finding withdrawn |
| 72.3% of bill AP lines reconciled; ฿8.9M open | **FACT VERIFIED** |
| 10 bills outside the payables subledger | **FACT VERIFIED**; intent **UNRESOLVED — EVIDENCE REQUIRED** |
| Whether unaccrued GRNI is acceptable at a reporting date | **NOT A P01 DECISION** — Boss package, P08, P11 |
| Thai WHT / PND treatment | **HOLD — STATUTORY EVIDENCE REQUIRED**, routed to P07 |
