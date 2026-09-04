> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.**
> This review carries `file:line -- method` citations into a reference ERP source tree.
> Boss / PMO / AI-Audit visible only. Must NOT be transcribed into any Layer 1 clean-room package,
> into Team B design input, or into any downstream reference package. Its clean-room derivatives are
> the numbered files in the package root, which cite `EV-0NN` / `COR-0N` identifiers only.

# X3 — EXPERT 3 REVIEW: LEAD INTEGRATION & LOCALIZATION

Session: `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`
Wave: `WAVE A — CORE LEDGER & CLOSING`
Reviewer: Expert 3 — Lead Integration & Localization (independent)
Date: 2026-09-04

> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.**
> This file carries `file:line` citations into a reference ERP source tree. Boss / PMO / AI-Audit
> visible only. Not to be transcribed into any Layer 1 clean-room package, Team B design input, or
> downstream reference package. Clean-room learning only; no implementation or localization module
> was copied, and no reference code is reproduced here beyond the minimum needed to state a finding.

## Scope and method

Lens: upstream/downstream integration; Thai localization; VAT / WHT implications; external
interfaces; multi-company. Deliberately **out of my lane and not reviewed here**: database
structure and constraint design (Expert 2), functional/UX design of the core ledger (Expert 1),
security and hashing architecture (Expert 4).

Sources read directly this session, read-only, nothing modified:

| Ref | Path |
|---|---|
| `SRC-A` | `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account/` |
| `SRC-B` | `.../addons/account_reports/` |
| `SRC-C` | `.../addons/base/models/res_currency.py` |
| `SRC-TH` | `.../addons/l10n_th/` and `.../addons/l10n_th_reports/` (located by the required `ls | grep -i l10n_th`; exactly two modules found in the 797-module tree) |

Claims independently verified against primary source this session (more than the required five):
EV-001, EV-008, EV-009, EV-015, EV-016, EV-018, EV-019, plus the tax closing entry mechanism and
the entire Thai localization surface.

### Evidence-class legend used below

`VERIFIED FACT` — read from primary source this session, citation given.
`REFERENCE BEHAVIOUR` — what the reference implementation does; not automatically a requirement.
`INFERENCE` — reasoned from verified facts, never promoted.
`RECOMMENDATION` — proposed SMEsPlus position, requires Boss decision.
`UNKNOWN — EVIDENCE REQUIRED` — not decidable from what was read.
`HOLD / EVIDENCE REQUIRED` — Thai statutory / Revenue Department / VAT / WHT matter, routed to the
Accounting-Tax track, never asserted as settled law by this reviewer.

### Verdict vocabulary

`CONFIRMED`, `CONFIRMED WITH CAVEAT`, `CONTRADICTED`, `UNKNOWN`, `HOLD`, `VETO`.
No approval is granted anywhere in this document. Boss is sole final approver.

### Standing statutory rule applied throughout

Every statement in this review about what Thai law, the Thai Revenue Department, the Revenue Code,
VAT (PP30), withholding tax (PND1 / PND3 / PND53 / PND54 / PP36), the Civil and Commercial Code,
TFRS/TFRS for NPAEs, or the DBD requires is marked `HOLD / EVIDENCE REQUIRED` and routed to the
Accounting-Tax track. This reviewer describes only *what a requirement would have to specify* in
order for a design decision to be made. No Thai statutory position is cited from memory, and none
of it is treated as verified. Every Thai account name, report name, and form name appearing below
is **candidate / UNVALIDATED**.

---

## FINDING 1 — EV-009 is directionally right but the shift rule is materially different from "lock_date + 1 day"

**Class: VERIFIED FACT (mechanism) / CONFIRMED WITH CAVEAT (EV-009)**

### OBSERVATION

EV-009 states that a backdated entry has its date rewritten to `lock_date + 1 day`. That is true of
exactly one code path — record duplication. The path that actually governs posting computes a
substantially different date, and the rule differs between sale documents and everything else.

`_get_accounting_date(invoice_date, has_tax, lock_dates)` behaves as follows:

- If any lock is violated, the candidate date is first moved to `latest violated lock + 1 day`.
- For a **sale** document it is then moved forward again to the **end of the month or end of the
  year** implied by the journal's sequence reset pattern, and then capped at **today**.
- For a **non-sale** document (purchase, miscellaneous) with month-reset numbering, if today's
  (year, month) is later than the candidate's, the date becomes the **last day of the candidate's
  month**; otherwise it becomes `max(candidate, today)`.
- For year-reset numbering the equivalent rule lands the entry on **31 December of the candidate's
  year**.

So the landing date is not "the day after the lock". It is "the end of the first open accounting
period, or today, whichever the sequence pattern and the calendar dictate". For a Wave A design
this is a different requirement to specify, a different figure to show the user, and a different
outcome for period attribution.

### EVIDENCE

- `SRC-A account/models/account_move.py:5655-5691` — `_get_accounting_date`; the docstring itself
  states the intent that, where a tax lock date and taxes are involved, the invoice is registered
  at the last date of the first open period. Lines 5673-5674 apply `lock + 1 day`; 5675-5680 apply
  the sale-document month/year-end-capped-at-today rule; 5681-5690 apply the non-sale rule.
- `SRC-A account/models/account_move.py:3127-3129` — inside `copy_data`, the simple
  `date = user_fiscal_lock_date + timedelta(days=1)` rewrite. This is the duplication path only,
  and is the behaviour EV-009 describes.
- `SRC-A account/models/account_move.py:4933-4936` — inside `_post`, the posting path resolves the
  violated locks and then assigns `move.date = move._get_accounting_date(...)`. This, not
  `copy_data`, is the load-bearing path.
- `SRC-A account/models/account_move.py:5702-5712` — the user-facing message resolves the landing
  date through the same `_get_accounting_date`, so the message shown to the user is consistent with
  the complex rule, not with `lock + 1`.

### CONTRADICTION

EV-009's citation `account_move.py:3127-3129` is correct as a citation but is attached to the wrong
conclusion: it documents the *copy* behaviour and presents it as the *posting* behaviour. The
consequence paragraph in EV-009 ("its accounting date is silently moved forward into the first open
period") is right in substance; the stated rule is wrong in detail. Recorded as `X3-CONTRA-01`.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether the sale-document cap at `today` can produce a landing date
that is *earlier* than the lock date + 1 when `today` itself precedes the lock (a future-dated lock).
`min(today, month_end)` with `today < lock+1` would return a date on or before the lock. Not
reproduced or tested this session; a runtime test is required before this is asserted either way.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus must not inherit this rule by default. Specify the late-document policy
explicitly and separately from numbering: (a) reject, (b) accept at document date with an exception
record, or (c) accept at a stated re-dated accounting date **with both dates stored and both
reportable**. Whichever is chosen, the ledger must carry `document_date` and `accounting_date` as
two distinct, separately queryable, separately reportable fields — the reference model already has
`invoice_date` vs `date` but does not surface the divergence anywhere the tax exports can see it
(see Findings 3 and 4). Boss decision required. Carry-forward: `WAVE-D TAX`.

---

## FINDING 2 — Purchase and miscellaneous documents are re-dated even when NO lock date exists

**Class: VERIFIED FACT / CONTRADICTED (EV-009 framing)**

### OBSERVATION

EV-009 frames re-dating as a *lock-date* behaviour. It is not only that. For any document that is
not a sale document, the accounting date is computed through `_get_accounting_date`
**unconditionally**, on every recompute of the date, whether or not any lock date exists.

Worked through with the code, in a company with month-reset numbering and no lock dates set at all:

- A vendor bill with document date 2026-08-15, entered 2026-09-04 → accounting date becomes
  **2026-08-31**.
- A vendor bill with document date 2026-09-01, entered 2026-09-04 → accounting date becomes
  **2026-09-04** (`max(invoice_date, today)`).

The document date and the ledger date therefore diverge on ordinary vendor bills in a completely
unlocked, freshly configured system. Sale documents are exempted from this (line 808 guards on
`is_sale_document`), so customer invoices keep their document date while vendor bills do not. The
asymmetry is deliberate in the reference design but is not described anywhere in the evidence base.

### EVIDENCE

- `SRC-A account/models/account_move.py:801-815` — `_compute_date`; line 808 tests
  `if not move.is_sale_document(include_receipts=True):` and line 809 then assigns
  `accounting_date = move._get_accounting_date(move.invoice_date, move._affect_tax_report())`.
  There is no lock-date precondition on this call.
- `SRC-A account/models/account_move.py:5681-5690` — the non-sale branch of `_get_accounting_date`
  executes on its own terms when `lock_dates` is empty, returning month-end or `max(date, today)`.

### CONTRADICTION

Directly qualifies EV-009. Re-dating is a **document-type** behaviour first and a **lock-date**
behaviour second. A Wave A design that implements lock-date re-dating only, and assumes document
date equals ledger date in the absence of locks, will not reproduce the reference behaviour and —
more importantly — will produce a different VAT/WHT period attribution for vendor bills than the
reference does. Recorded as `X3-CONTRA-02`.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether any shipped localization overrides `_compute_date` to
suppress this for its own country. `SRC-TH` does not (see Finding 11) — `l10n_th/models/account_move.py`
overrides only `_get_name_invoice_report`. Whether other localizations do was not searched.

### RECOMMENDATION

`RECOMMENDATION:` treat "what date does a purchase document post on" as an explicit Wave A decision
with a written rule, not as an emergent property of a sequence pattern. Carry-forward:
`WAVE-C AP` (the rule) and `WAVE-D TAX` (its tax-period consequence).

---

## FINDING 3 — The Thai VAT report exports the ACCOUNTING date under the column heading "Invoice Date"

**Class: VERIFIED FACT (mechanism) / HOLD (statutory consequence)**

### OBSERVATION

This is the point at which Findings 1 and 2 become a filing risk rather than a modelling curiosity.

The Thai localization ships two XLSX exports — candidate / UNVALIDATED names "Sales Tax Report" and
"Purchase Tax Report". Both:

1. **select** the population by `move.date` (the accounting date) between the report period bounds;
2. **print** `move.date` into a column whose header is the translated string `Invoice Date`.

So a vendor bill whose document date is 15 August but whose accounting date was moved to 31 August
(Finding 2) or forward into September (Finding 1) appears in the export with a date that is not its
tax invoice date, in the period determined by the shifted date, under a heading that asserts it is
the invoice date. Nothing in the export reveals the divergence. The input-tax report and the
output-tax report are equally affected.

### EVIDENCE

- `SRC-TH l10n_th_reports/models/tax_report_vat.py:62` —
  `domain += [('date', '>=', date_from), ('date', '<=', date_to)]` — period selection on the
  accounting date.
- `SRC-TH l10n_th_reports/models/tax_report_vat.py:114` — the header list contains
  `_("Invoice Date")` in position 4.
- `SRC-TH l10n_th_reports/models/tax_report_vat.py:138` — `sheet.write(y_offset, 3, move.date, ...)`
  writes `move.date` into that column. `invoice_date` is not referenced anywhere in the file.
- Combined with `SRC-A account/models/account_move.py:801-815` and `:5655-5691` (Findings 1 and 2),
  which establish that `move.date` is a derived, shiftable field for exactly the purchase documents
  that populate the input-tax report.

### CONTRADICTION

None internal to the reference implementation — it is self-consistent, because the reference treats
the accounting date as the tax point. The contradiction is between that treatment and the column
label presented to the filer. Recorded as `X3-CONTRA-03` (labelling defect, low ambiguity).

### UNKNOWN

`HOLD / EVIDENCE REQUIRED — ACCOUNTING-TAX TRACK.` The following must be established by the
Accounting-Tax track before any Wave D design position is taken. This reviewer states them as
questions, not as law:

- Which date does the Thai Revenue Department treat as determining the VAT period for output tax —
  the tax invoice date, the delivery/service date, or the date of entry in the books?
- Which date determines the period in which input tax may be claimed, and is there a permitted
  window for claiming input tax in a later period than the tax invoice date?
- Is there a statutory requirement that the input/output tax reports (candidate / UNVALIDATED:
  "Input Tax Report", "Output Tax Report") be maintained in tax-invoice-date order and sequence,
  and if so, does a re-dated accounting date break that ordering?
- What is the consequence, if any, of a document appearing in a later period's report than its tax
  invoice date implies?

Until those are answered, no Wave A decision may be taken that treats accounting date and tax point
as the same thing.

### RECOMMENDATION

`RECOMMENDATION:` `HOLD` on any SMEsPlus adoption of accounting-date-driven VAT period attribution.
Design the ledger so that a **tax point date** is a first-class field on the tax line, independent
of both `document_date` and `accounting_date`, and so that VAT reporting selects on the tax point.
This is a Wave A *structural* requirement (the field must exist in the core ledger) even though the
Wave D decision on how to populate it is not taken here. Carry-forward: `WAVE-D TAX`.

---

## FINDING 4 — The Thai WHT (PND) export has three independent defects: wrong date semantics, recomputed amounts, and a hardcoded rate-to-type map

**Class: VERIFIED FACT (mechanism) / HOLD (statutory consequence)**

### OBSERVATION

The PND3 and PND53 CSV exports (candidate / UNVALIDATED names) share one SQL builder. Three separate
problems, each independently material:

**(a) Date semantics.** The exported date column is headed `Invoice/Bill Date` but is populated from
`move.date` — the accounting date. Every consequence in Finding 3 applies identically, and applies
*more* strongly, because WHT arises on purchase-side documents, which are exactly the document type
that is re-dated even without a lock (Finding 2). Additionally, the report period is a `strict_range`
on the report options, which are date-driven the same way.

**(b) The WHT amount is recomputed, not read.** The exported WHT amount is calculated in SQL as
`ABS(tax.amount * account_move_line.tax_base_amount / 100)` — the *tax rate on the tax record*
multiplied by the *stored base*. It is not the posted balance of the withholding tax line. Any
rounding applied at posting, any manual adjustment to the tax line, any partial withholding, and any
subsequent edit to the rate on the tax record will cause the statutory export to disagree with the
ledger, silently, with no reconciliation point between them.

**(c) The tax type is a hardcoded four-way map on the rate.** The exported "Tax Type" column is a
`CASE` on `tax.amount` mapping `-1 → Transportation`, `-2 → Advertising`, `-3 → Service`,
`-5 → Rental`, everything else `''`. The nature of the payment is therefore inferred from its
percentage, not recorded. Two different payment natures that happen to share a rate are
indistinguishable, and any rate outside those four exports a blank type. The "WHT Condition" column
is the literal string `'1'` for every row.

### EVIDENCE

- `SRC-TH l10n_th_reports/models/tax_report_pnd.py:22-23` — the header row, including
  `_('Invoice/Bill Date')`, `_('WHT Amount')`, `_('WHT Condition')`, `_('Tax Type')`.
- `SRC-TH l10n_th_reports/models/tax_report_pnd.py:43` —
  `TO_CHAR(account_move_line__move_id.date, 'dd/mm/YYYY') as date` — the accounting date under that
  heading.
- `SRC-TH l10n_th_reports/models/tax_report_pnd.py:46` —
  `ROUND(ABS(tax.amount * account_move_line.tax_base_amount / 100), ...) as wht_amount` — recomputed.
- `SRC-TH l10n_th_reports/models/tax_report_pnd.py:47` — `'1' as wht_condition` — literal constant.
- `SRC-TH l10n_th_reports/models/tax_report_pnd.py:48-54` — the four-way `CASE tax.amount` map.
- `SRC-TH l10n_th_reports/models/tax_report_pnd.py:91-108` and `:128-145` — the PND53 and PND3
  exports; population is selected by `tax_tag_ids` against three tag templates each.
- `SRC-TH l10n_th/data/template/account.tax-th.csv:26-57` — the eight purchase-side WHT taxes, each
  a `percent` tax with a **negative** amount (`-1.0`, `-2.0`, `-3.0`, `-5.0`), `type_tax_use` =
  `purchase`, all posting to a single account `a_wht`.
- `SRC-TH l10n_th/data/template/account.account-th.csv:15` — `a_wht`, candidate / UNVALIDATED name
  "Withholding Tax", code 2320, `liability_current`.

### CONTRADICTION

Defect (b) is a genuine internal contradiction in the reference implementation: the ledger and the
statutory export can disagree about the same number, and the reference provides no control that
detects it. Recorded as `X3-CONTRA-04`. This one I regard as the most serious purely-technical
defect found in the localization layer, independent of any statutory question.

### UNKNOWN

`HOLD / EVIDENCE REQUIRED — ACCOUNTING-TAX TRACK.` Questions that must be answered before any WHT
design position:

- Which date does a withholding tax certificate and the corresponding return use — the payment date,
  the invoice date, or the date of entry? (The reference exports the accounting date under an
  invoice-date label, which can be none of these.)
- Is the WHT obligation triggered at invoice or at payment, and does that differ by payment nature?
- What is the complete set of payment natures and rates that must be distinguishable, and must the
  nature be recorded on the transaction rather than inferred from the rate?
- What returns exist beyond PND3 and PND53 (candidate / UNVALIDATED: PND1 for employment,
  PND54 and PP36 for remittances abroad), and does the ledger need to distinguish them?
- What are the filing deadlines for each return, and do they differ from the VAT deadline?
  (Finding 5 shows the reference has a single lock date and a single periodicity for all of them.)
- What must a withholding tax certificate contain, and must it be reproducible from the ledger?

### RECOMMENDATION

`RECOMMENDATION:` `HOLD`. For Wave A, the structural requirements this raises are: a WHT line must
carry (i) its own tax point date, (ii) a recorded payment-nature classification independent of the
rate, (iii) the posted amount as the single source of truth for any export, and (iv) a link to the
certificate issued. Modelling WHT as a negative-rate purchase tax, as the reference does, delivers
none of (i)-(iv). Carry-forward: `WAVE-D TAX`, with `WAVE-C AP` for the payment-time trigger and
`WAVE-B AR` for the receipt-side case in Finding 12.

---

## FINDING 5 — Tax lock and fiscal lock are different mechanisms with opposite failure modes, and one tax lock serves every tax return

**Class: VERIFIED FACT**

### OBSERVATION

This was the specific question put to me. The interaction is not a hierarchy; it is two mechanisms
with different scopes, different trigger conditions, and — critically — **opposite behaviours on
violation**.

**Scope.** The "user fiscal lock date" that governs most of the ledger is composed as
`max(fiscal-year lock, hard lock)`, raised to the sale lock for sale journals or the purchase lock
for purchase journals. **The tax lock date is not in that composition at all.** The tax lock is
consulted only through a separate resolver, and only when the move actually carries tax
(`has_tax`). A move with no tax lines is entirely unaffected by the tax lock.

**Failure mode.** When a *new* entry's date violates a lock, the date is **shifted** (Findings 1-2).
When an *existing posted* entry with tax-relevant lines is modified — its date or name changed, or
it is taken out of posted state — the tax lock **raises a UserError and refuses the operation**.
The same lock therefore silently re-dates on the way in and hard-blocks on the way back out.

**Granularity.** The tax closing entry sets `company.tax_lock_date` to the closing entry's own date,
using `sudo()`, gated on the caller holding the accounting-manager group. There is exactly **one**
`tax_lock_date` per company and exactly **one** `account_tax_periodicity` per company. The Thai
localization registers three separate tax reports — the VAT report and both PND returns — all with
`root_report_id` pointing at the generic tax report and all with custom handlers inheriting the
generic tax report handler. They therefore share that single lock date and single periodicity.

`INFERENCE:` if VAT and withholding returns have different statutory deadlines or different
periodicities, a single company-level tax lock date and a single periodicity cannot express both.
Closing one return locks the period for the other. Whether Thai deadlines actually differ is
`HOLD / EVIDENCE REQUIRED` and routed to the Accounting-Tax track — I do not assert it.

**Draft-reset guard.** Resetting a tax closing entry to draft is refused if it would delete carryover
values impacting an already-locked period, and refused if a later closing entry has been posted.

### EVIDENCE

- `SRC-A account/models/company.py:565-576` — `_get_user_fiscal_lock_date`; line 573 is
  `lock = max(company.user_fiscalyear_lock_date, company.user_hard_lock_date)`, then sale/purchase
  by journal type. `tax_lock_date` does not appear.
- `SRC-A account/models/company.py:598-631` — `_get_lock_date_violations`, taking independent
  booleans `fiscalyear`, `sale`, `purchase`, `tax`, `hard`.
- `SRC-A account/models/company.py:646-665` — `_get_violated_lock_dates`, which supplies
  `tax=has_tax`; the tax lock is checked only when the move carries tax.
- `SRC-A account/models/account_move_line.py:1269-1271` — `_affect_tax_report` returns true when the
  line has `tax_ids`, a `tax_line_id`, or tax tags with applicability `taxes`.
- `SRC-A account/models/account_move_line.py:1273-1290` — `_check_tax_lock_date`; it calls
  `_get_lock_date_violations(move.date, fiscalyear=False, sale=False, purchase=False, tax=True,
  hard=True)` and **raises** a UserError stating the operation would impact an already issued tax
  statement. This is a rejection, not a shift.
- `SRC-A account/models/account_move.py:3230-3241` — the write guards that invoke
  `_check_fiscal_lock_dates()` and `line_ids._check_tax_lock_date()` when name or date change on a
  posted move, or when state leaves posted.
- `SRC-A account/models/account_move.py:3281-3283` — after the write, posted moves are re-checked;
  `posted_move.line_ids._check_tax_lock_date()`.
- `SRC-B account_reports/models/account_move.py:116-121` — the `_close_tax_period` docstring stating
  that the tax lock date of each move's company will be set to the move's date once all closings are
  performed.
- `SRC-B account_reports/models/account_move.py:126-127` — the operation is refused unless the user
  holds `account.group_account_manager` ("Only Billing Administrators are allowed to change lock
  dates!").
- `SRC-B account_reports/models/account_move.py:132-134` — `self.company_id.sudo().tax_lock_date =
  self.date`, guarded on there being no foreign-VAT fiscal position and the new date being later.
- `SRC-B account_reports/models/account_move.py:57-79` — `button_draft` override refusing the reset
  when carryover values would be destroyed inside a tax-locked period, and refusing it when a later
  closing entry is posted.
- `SRC-B account_reports/models/res_company.py:20-26` — `account_tax_periodicity`, one Selection
  field per company, default `monthly`.
- `SRC-B account_reports/models/res_company.py:369-374` — `_get_tax_periodicity(report)` returns
  `main_company.account_tax_periodicity` — the same value regardless of which report is supplied as the argument.
- `SRC-TH l10n_th_reports/data/account_tax_report_data.xml:3-11` — all three Thai reports (VAT,
  PND53, PND3) bound to custom handlers; `SRC-TH l10n_th/data/account_tax_report_data.xml:3-8` and
  `:174-178` and `:232-238` — each declared with `root_report_id` = the generic tax report and
  `country_id` = Thailand.

### CONTRADICTION

Internal to the reference: the tax lock is documented on the field as behaving like the other soft
locks ("Any entry with taxes up to and including that date will be postponed to a later time"), but
`_check_tax_lock_date` rejects rather than postpones for modifications, and the tax lock is excluded
from the composed fiscal lock that most of the code consults. Two different semantics under one
name. Recorded as `X3-CONTRA-05`.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether posting a **PND** closing entry actually reaches the
`tax_lock_date` assignment, or whether tax closing entry generation is in practice only wired for
the VAT report. The code path is generic and would set the same field; whether the PND reports are
included in `_get_tax_closing_entries_for_closed_period` was not traced to a conclusion this
session. This must be resolved before Wave D relies on either answer.

`HOLD / EVIDENCE REQUIRED — ACCOUNTING-TAX TRACK:` the filing periodicities and deadlines for the
Thai VAT return and each withholding return, and whether a single period-lock concept can serve them
all.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus should not adopt a single company-scalar tax lock. Specify locks as
`(lock_domain, period, effective_date)` records where `lock_domain` distinguishes at minimum VAT
from each withholding return, so that closing one return does not lock another. Also specify one
consistent violation semantic — shift or reject — rather than the reference's split. Carry-forward:
`WAVE-D TAX`.

---

## FINDING 6 — EV-015 is half right: the cash-basis path does not silently relocate into a tax-locked period, it hard-fails the reconciliation

**Class: VERIFIED FACT / CONFIRMED WITH CAVEAT (EV-015)**

### OBSERVATION

EV-015 states that tax cash-basis entries are dated today when their natural date falls in a locked
period, and treats this as a silent relocation. The date-selection half is confirmed exactly. The
"silent" half is not, and the corrected behaviour is worse for operations, not better.

The date chosen for a generated cash-basis entry is `partial.max_date` if that date is after the
**user fiscal lock date**, otherwise **today**. The lock consulted is
`_get_user_fiscal_lock_date(journal)`, which — per Finding 5 — **excludes the tax lock date**. The
cash-basis entry is by construction a tax entry.

So there is a window: `fiscal_lock < max_date <= tax_lock`. In that window the code selects
`max_date` (because it clears the fiscal lock), the entry is created and posted, and the post-write
guard at `account_move.py:3283` then calls `_check_tax_lock_date`, which **raises**. The user's
reconciliation transaction fails with an error about impacting an already-issued tax statement.

This window is not exotic. It is the normal configuration: the tax lock advances every filing period
as returns are closed, while the fiscal-year lock is typically set far less often and therefore sits
behind it. Any attempt to reconcile a payment against an older cash-basis-VAT invoice will land in
this window and fail.

Outside that window — `max_date <= fiscal_lock` — the entry is dated **today** and EV-015's
year-boundary concern is exactly right: a cash-basis tax consequence of a prior-year event is booked
into the current year, with the origin link preserved but the period attribution lost.

The same `_get_accounting_date` shift applies to reversals of exchange difference entries when a
full reconciliation is unlinked, which EV-015 states correctly.

### EVIDENCE

- `SRC-A account/models/account_partial_reconcile.py:512-514` — `journal = partial.company_id.
  tax_cash_basis_journal_id`; `lock_date = move.company_id._get_user_fiscal_lock_date(journal)`;
  `move_date = partial.max_date if partial.max_date > lock_date else today`.
- `SRC-A account/models/company.py:565-576` — establishes that `_get_user_fiscal_lock_date` does not
  include `tax_lock_date` (Finding 5).
- `SRC-A account/models/account_move.py:3281-3283` — the post-write re-check that raises via
  `_check_tax_lock_date`.
- `SRC-A account/models/account_move_line.py:1273-1290` — the raising implementation.
- `SRC-A account/models/account_full_reconcile.py:29-33` — reversal of exchange moves on unlink,
  with `'date': move._get_accounting_date(move.date, move._affect_tax_report())`, i.e. the same
  shift rule as Findings 1-2.
- `SRC-A account/models/account_move.py:5317-5354` (per evidence base EV-012, spot-checked) —
  cash-basis and exchange-difference entries cannot be reset to draft, so the operator has no
  in-product remedy other than moving a lock date.

### CONTRADICTION

Qualifies EV-015. "Silently relocate" is accurate only in the fiscal-lock case. In the tax-lock
window the behaviour is a hard operational failure of an ordinary business action (reconciling a
receipt), not a silent relocation. Recorded as `X3-CONTRA-06`.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether the reference ships a guard that prevents the user reaching
this state (for example by excluding cash-basis-eligible partials from reconciliation while a tax
lock covers them). Not found in what was read; absence is asserted only for
`account/models/account_partial_reconcile.py` and `account/models/account_move.py` as read this
session, not for the module as a whole.

`HOLD / EVIDENCE REQUIRED — ACCOUNTING-TAX TRACK:` whether Thai VAT is or may be accounted on a
payment basis for any category of supply, and if so, in which period the tax point falls. This
determines whether the cash-basis mechanism is in SMEsPlus scope at all. Note that the shipped Thai
tax template does not configure it (Finding 11).

### RECOMMENDATION

`RECOMMENDATION:` any SMEsPlus mechanism that generates an accounting consequence of a past event
must, as a Wave A structural rule, carry **three** dates: the origin event date, the generating
event date, and the posting date; and must be refused at generation time with a clear message rather
than failing at post time inside another user's transaction. Carry-forward: `WAVE-D TAX` for the
cash-basis question, `WAVE-H BANKING` for the reconciliation-time failure path.

---

## FINDING 7 — EV-018 understates the model: rate types DO exist, but only as a report-time consolidation artefact, and a missing rate silently becomes 1.0

**Class: VERIFIED FACT / CONFIRMED WITH CAVEAT (EV-018)**

### OBSERVATION

EV-018's core statement is correct and I confirm it: the stored rate model permits exactly one rate
per (date, currency, company root), enforced by a database unique constraint, with a positivity
check. EV-018 then states there is "no rate *type* dimension — no separate spot, average, closing or
historical rate". That is true of the **posting layer** and false of the **reporting layer**, and
EV-018's own deferred `UNKNOWN` on whether an average rate is synthesised is answered by the same
code.

There is a `rate_type` dimension with values `historical`, `current`/`closing`, and `average`. It
lives in a **temporary table built per report run** and dropped on commit. Its purpose is narrow:
translating the balances of companies whose main currency differs from the reporting company's, for
consolidation. It is not a posting-layer concept and it does not translate foreign-currency
transactions inside a single company.

How each is derived, all from the same single daily scalars:

- `historical` — the daily rates themselves, applied at the date of each operation.
- `closing`/`current` — the most recent rate within the period.
- `average` — a **days-weighted average** of the stored daily rates across the period, computed in
  SQL at report time, never stored.

Applied by account type: equity accounts get `historical`; income, expense and the current-year
earnings account get `average`; everything else gets `closing`.

Two further findings of my own, beyond EV-018:

**(a) Stale rate carry-forward.** Rate lookup takes the last rate dated on or before the requested
date. If no rate was entered for the period, the last known rate is used with no indication that it
is stale.

**(b) Silent 1.0.** If no rate record exists at all for a currency, the lookup coalesces to **1.0** —
a silent one-to-one conversion. The same `COALESCE(..., 1.0)` appears in the average-rate builder.
For a THB-functional ledger transacting in a currency whose rates were never loaded, foreign amounts
would post at par with no error and no warning.

### EVIDENCE

- `SRC-C base/models/res_currency.py:335-371` — the rate model: `name` (Date, indexed, required),
  `currency_id`, `company_id` defaulting to `self.env.company.root_id`; `_sql_constraints` at
  `:368-371` with `unique (name,currency_id,company_id)` and `CHECK (rate>0)`.
- `SRC-C base/models/res_currency.py:121-141` — `_get_rates`; the primary search is
  `('name', '<=', date)` ordered `name DESC limit 1` (stale carry-forward), a fallback is the
  earliest rate, and the SQL is `COALESCE((rate_query), (rate_fallback), 1.0)` — the silent 1.0.
- `SRC-A account/models/res_currency.py:85-89` — the `_create_currency_table` docstring defining
  `rate_type` as `'historical'`, `'current'` or `'average'` and describing each.
- `SRC-A account/models/res_currency.py:75-78` — the same docstring stating the table's purpose is
  aggregating amounts belonging to **companies with different main currencies**, i.e. consolidation.
- `SRC-A account/models/res_currency.py:114-121` — CTA mode builds closing, historical and average
  builders; non-CTA mode builds only `current`.
- `SRC-A account/models/res_currency.py:126-138` — the table is created as a `TEMPORARY TABLE ...
  ON COMMIT DROP`; nothing is persisted.
- `SRC-A account/models/res_currency.py` `_get_table_builder_average` — the days-weighted average:
  `SUM(factor / rate * number_of_days) / SUM(number_of_days)`, with `number_of_days` derived by a
  `LEAD()` window over rate dates, and a `COALESCE(out_period_rate.rate, 1.0)` fallback.
- `SRC-B account_reports/models/account_report.py:1413-1417` — the account-type-to-rate-type `CASE`:
  equity → `historical`; income, expense and `equity_unaffected` → `average`; else `closing`.

### CONTRADICTION

Qualifies EV-018 in both directions: rate types exist (so EV-018 overstates the absence), but they
are ephemeral, consolidation-only, and derived from the same single scalars (so EV-018's practical
conclusion — that a closing rate distinct from the transaction-date rate has no carrier in the
posting layer — stands). EV-018's deferred `UNKNOWN` about an average rate is hereby answered:
yes, days-weighted, at report time only. Recorded as `X3-CONTRA-07`.

The silent 1.0 fallback is a defect I raise independently; it is not in the evidence base.

### UNKNOWN

`HOLD / EVIDENCE REQUIRED — ACCOUNTING-TAX TRACK:` what rate a Thai reporting entity must use for
(i) initial recognition of a foreign-currency transaction, (ii) translation of monetary items at the
reporting date, (iii) non-monetary items at historical cost, and (iv) whether a specific published
rate source (candidate / UNVALIDATED: a central bank reference rate, and a distinction between
buying, selling and average rates) is mandated for tax purposes as distinct from financial reporting
purposes. If a buying/selling/average distinction is mandated, the single-scalar model cannot carry
it and this becomes a Wave A structural requirement.

### RECOMMENDATION

`RECOMMENDATION:` model the rate as `(date, currency, rate_type, source)` in the **posting** layer,
not only in a report-time temporary table, and make a missing rate an error rather than 1.0. The
rate actually applied to a posting must be recoverable from the posting itself. Carry-forward:
`WAVE-G REPORTING` for presentation translation, `WAVE-A` for the posting-layer rate structure.

---

## FINDING 8 — Revaluation at closing rate is a self-reversing provision, and the closing rate can be typed into the report and is never stored

**Class: VERIFIED FACT**

### OBSERVATION

The reference does have a multicurrency revaluation mechanism, which EV-018 does not mention. Its
design has three properties that matter for a Thai statutory context:

**(a) It is a provision, reversed the next day.** The wizard defaults the entry date to the report
period end and the **reversal date to period end + 1 day**. The revaluation therefore never adjusts
the carrying amount of the underlying receivable or payable; it books a provision to a dedicated
expense or income account and immediately unwinds it. The subledger balance is untouched.

**(b) The closing rate is user-typable at report time.** The report resolves rates for the period-end
date, but if the report options carry a user-supplied rate for a currency, **that value is used
instead**. The only control is a UI warning banner flagged when any supplied rate differs from the
stored rate.

**(c) The rate used is not stored anywhere.** It exists only in the report options for that run. The
posted provision entry does not carry the rate that produced it. There is no record, after the fact,
of what closing rate was applied to produce a given revaluation.

**(d) The provision accounts are company-level configuration**, set through the same wizard by
`sudo()` inverse writes.

### EVIDENCE

- `SRC-B account_reports/wizard/multicurrency_revaluation.py:26` — `date` defaults to the report
  options' `date_to`.
- `SRC-B account_reports/wizard/multicurrency_revaluation.py:52-54` — `reversal_date` defaults to
  `date_to + relativedelta(days=1)`.
- `SRC-B account_reports/wizard/multicurrency_revaluation.py:95-105` — `_inverse_revaluation_journal`,
  `_inverse_expense_provision_account`, `_inverse_income_provision_account`, each writing to the
  company with `sudo()`.
- `SRC-B account_reports/models/account_multicurrency_revaluation_report.py:41` —
  `rates = active_currencies._get_rates(self.env.company, options.get('date').get('date_to'))`.
- `SRC-B account_reports/models/account_multicurrency_revaluation_report.py:52-54` — the stored rate
  is used **only if** `previous_options['currency_rates'][...]['rate']` is absent; otherwise the
  user-supplied float wins.
- `SRC-B account_reports/models/account_multicurrency_revaluation_report.py:63-64` and `:74-75` —
  `options['custom_rate']` is computed and, when true, sets a warning key
  `multi_currency_revaluation_report_warning_custom_rate` with `alert_type: 'warning'`. A warning,
  not a block, and not a stored record.
- `SRC-B account_reports/models/account_multicurrency_revaluation_report.py:208-210` and
  `:332-333` — the supplied rates are injected as a literal `VALUES` list into the SQL and the
  adjustment is `amount_currency / rate - balance`.

### CONTRADICTION

None identified within the reference. The contradiction is with the audit expectation implied by
Wave A: a period-end adjustment whose determining input is neither stored nor recoverable is not
reproducible, and therefore not auditable, even though the entry itself is a normal posted move
subject to hashing and locks.

### UNKNOWN

`HOLD / EVIDENCE REQUIRED — ACCOUNTING-TAX TRACK:` whether an unrealized foreign exchange gain or
loss on monetary items is recognized for Thai tax purposes at period end, whether the treatment
differs between financial reporting and tax computation, and whether a self-reversing provision
satisfies the requirement or whether the carrying amount itself must be adjusted. Also whether the
rate source used for a statutory revaluation must be evidenced.

### RECOMMENDATION

`RECOMMENDATION:` if SMEsPlus supports revaluation, the applied rate and its source must be stored
on the generated entry as posted data, and a rate that differs from the stored rate table must
require an authorised, reasoned override record — not a dismissible banner. Carry-forward:
`WAVE-G REPORTING` for the report, `WAVE-A` for the requirement that the rate be stored on the entry.

---

## FINDING 9 — EV-016 confirmed; what a Thai statutory year-end would require that this does not provide

**Class: VERIFIED FACT (mechanism) / HOLD (statutory requirement)**

### OBSERVATION

EV-016 is confirmed on the mechanism. I independently verified that the only thing in the reference
tree bearing a "financial year" name is a **TransientModel configuration wizard**, not an entity: it
holds the opening date and the two fiscal-year-end integers as related fields on the company, and
the reporting layer extends it with the tax periodicity settings. A transient wizard has no records,
no history, and no state. There is no fiscal year record, no period record, no year-close event, and
no carry-forward posting; the current-year result is attributed to the "Current Year Earnings"
account at report time.

I also confirm that the only entity called a closing entry is the tax closing entry, which is an
unrelated concept (Finding 5).

What a Thai statutory year-end and a set of audited financial statements would require, that this
does not provide — stated as requirements to be **established**, not asserted:

`HOLD / EVIDENCE REQUIRED — ACCOUNTING-TAX TRACK.`

1. **A defined, closed accounting period as a record.** Statements are signed for a period. A lock
   date that can be moved backward (all four soft locks can) is not a period; it is a setting. A
   requirement would need to specify whether a closed period must be an immutable record with a
   closing act, an actor, and a timestamp.
2. **A posted year-end result appropriation.** The reference computes the year result for display.
   A requirement would need to specify whether the transfer of the year result to retained earnings
   must exist as a posted journal entry, and whether a legal reserve appropriation must be posted.
3. **A reopening / prior-period-adjustment concept.** Audit adjustments arrive after the books are
   closed. A requirement would need to specify whether they are posted into the closed year, into
   the opening balances of the new year, or into the current year with disclosure — and what
   evidence chain is required. The reference has no concept for any of the three.
4. **Statement-level identity and comparatives.** A requirement would need to specify the statutory
   statement set, the prescribed line structure, the comparative-period rule, and whether restated
   comparatives must be distinguishable from originals.
5. **A filing artefact and its retention.** A requirement would need to specify what must be filed,
   in what format, to which authority, by when, and what must be retained and for how long.
6. **The fiscal year end itself.** The Thai localization template does **not** set the fiscal year
   end (Finding 11), so a Thai company created from it defaults to 31 December. Whether non-calendar
   accounting periods are permitted or common, and whether a change of accounting period requires
   approval, is `HOLD / EVIDENCE REQUIRED`.

### EVIDENCE

- `SRC-A account/wizard/setup_wizards.py:10-21` — `class FinancialYearOpeningWizard(models.
  TransientModel)`, `_name = 'account.financial.year.op'`; its fields `opening_date`,
  `fiscalyear_last_day`, `fiscalyear_last_month` are all `related=` fields on `res.company`. It is a
  settings dialog, not a fiscal year entity. This is the nearest thing in the tree to a fiscal year
  model and it confirms rather than contradicts EV-016.
- `SRC-B account_reports/wizard/fiscal_year.py:9-15` — the reporting layer's extension of that same
  TransientModel, adding tax periodicity settings. Also transient.
- `SRC-B account_reports/models/account_general_ledger.py:199-223` — the current-year result is
  computed as a query result keyed `unaffected_earnings` and **attributed at render time** to the
  first account of type `equity_unaffected` belonging to the company's root. No posting occurs.
- `SRC-B account_reports/models/account_general_ledger.py:314-343` — `_get_options_unaffected_earnings`
  and the query that emits `'unaffected_earnings' AS key`.
- `SRC-TH l10n_th/models/template_th.py:18-31` — the Thai company template sets fiscal country,
  account code prefixes, exchange gain/loss accounts and default taxes. It sets neither
  `fiscalyear_last_day` nor `fiscalyear_last_month`, so the framework defaults apply.

### CONTRADICTION

None identified against EV-016 — I reached the same conclusion by an independent route and found the
one candidate counter-example (`account.financial.year.op`) to be a transient wizard that
strengthens rather than weakens EV-016. EV-016's negative claim should nonetheless be restated with
scope: "no fiscal year *entity* was located in the module tree read this session", not "does not
exist".

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether any of the 797 modules outside `account`, `account_reports`
and `base` introduces a period entity (some localizations historically have). Not searched
exhaustively this session; EV-016's tree-wide search is recorded but I did not re-run it.

### RECOMMENDATION

`RECOMMENDATION:` treat the closed-period record as a **Wave A** structural requirement, not a Wave G
reporting one, because it must exist in the ledger before any close can be evidenced. Treat the
year-end appropriation posting and the prior-period-adjustment route as Boss decisions with no
reference implementation to adapt. Carry-forward: `WAVE-G REPORTING` for statements,
`WAVE-D TAX` for the filing artefact.

---

## FINDING 10 — Multi-company: an intercompany pair can post on two different accounting dates, and liquidity accounts are the one thing that cannot be shared

**Class: VERIFIED FACT**

### OBSERVATION

Three multi-company behaviours combine into one integration risk.

**(a) Intercompany documents do not carry the accounting date across.** The counterpart document is
built with the originator's `invoice_date`, `invoice_date_due`, currency, partner and reference —
but **not** its accounting date. The counterpart is a **purchase** document, so its accounting date
is derived independently in the receiving company by `_compute_date` (Finding 2) and shifted again
at posting by the receiving company's own lock dates (Finding 1). The two legs of a single
intercompany transaction can therefore legitimately post on different accounting dates, in different
months, and — across a year boundary — in different fiscal years, while sharing a document date.

**(b) The hard lock cascades down the company tree.** A company's effective hard lock is the maximum
hard lock across its whole parent chain. A parent company setting a hard lock therefore locks every
subsidiary, and — because the hard lock can only ever move forward — irreversibly. Combined with (a),
a parent's lock can force a subsidiary's leg of an intercompany transaction into a later period than
the parent's own leg.

**(c) Accounts are shared with per-company codes, except liquidity accounts, which cannot be shared.**
EV-001 and EV-019 are both confirmed. The account is a many-to-many to companies with a
company-dependent code; but an account of type `asset_cash` belonging to more than one company is
rejected outright, and a company cannot be detached from an account while its journal items
reference it.

`INFERENCE:` the asymmetry in (c) is coherent — a bank account is a real-world object owned by one
legal entity — but it means a shared chart of accounts is not uniformly shared, and any SMEsPlus
consolidation mapping must handle liquidity accounts as a special case from the start.

**(d) Currency rates are shared from the company root** (Finding 7), so every company in a group is
forced onto one rate table per currency per day, while each may have a different functional currency.

### EVIDENCE

- `SRC-A account_inter_company_rules/models/account_move.py:88-99` — `invoice_vals`, containing
  `'invoice_date': self.invoice_date` at `:93` and `'invoice_date_due'` at `:94`. There is no
  `'date'` key; the accounting date is not transferred.
- `SRC-A account_inter_company_rules/models/account_move.py:97` —
  `'journal_id': self.env.company.intercompany_purchase_journal_id.id` — the counterpart is a
  purchase document, which is precisely the document class subject to unconditional re-dating
  (Finding 2).
- `SRC-A account_inter_company_rules/models/account_move.py:66-68` — the counterpart is posted
  immediately when `intercompany_document_state == "posted"`, so the shift at `_post` applies.
- `SRC-A account/models/company.py:396-402` — `_compute_user_hard_lock_date` takes the `max()` of
  `hard_lock_date` across `company.parent_ids`; confirms EV-008's cascade.
- `SRC-A account/models/company.py:54-64` — `SOFT_LOCK_DATE_FIELDS` (four) and `LOCK_DATE_FIELDS`
  (five); confirms EV-008's structure.
- `SRC-A account/models/account_account.py:49-50` — `code` computed over `code_store`, declared
  `company_dependent=True`; confirms EV-001.
- `SRC-A account/models/account_account.py:106-107` — `company_ids = fields.Many2many('res.company',
  ..., required=True)`; confirms EV-001.
- `SRC-A account/models/account_account.py:300-301` — `if self.filtered(lambda a: a.account_type ==
  'asset_cash' and len(a.company_ids) > 1): raise ValidationError(_("Bank & Cash accounts cannot be
  shared between companies."))`. Confirms EV-019. **Note:** EV-019 cites this as `:301-302`; the
  verified lines are `:300-301`. A one-line citation drift, recorded for accuracy, not a substantive
  disagreement.
- `SRC-A account/models/account_account.py:303-309` — the guard refusing to unlink a company from an
  account while that company's journal items reference it.
- `SRC-C base/models/res_currency.py:365-366` — `company_id` defaulting to
  `self.env.company.root_id`, and `:340` `_check_company_domain = models.check_company_domain_parent_of`.

### CONTRADICTION

None identified against EV-001, EV-008 or EV-019 — all three confirmed, with the one-line citation
correction noted above. The contradiction I raise is between (a) and any expectation that an
intercompany pair reconciles period-by-period: it does not, by construction.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether the reference provides any control that detects an
intercompany pair whose two legs fell into different periods. Not found in
`account_inter_company_rules/models/` as read this session; absence asserted only for that directory.

`HOLD / EVIDENCE REQUIRED — ACCOUNTING-TAX TRACK:` Thai requirements on related-party transactions,
transfer pricing documentation, and whether intercompany balances must agree by period for group
reporting or tax purposes.

### RECOMMENDATION

`RECOMMENDATION:` for SMEsPlus, an intercompany transaction must be a single logical object with a
single agreed accounting period, and a period mismatch between its legs must be a detectable,
reportable exception rather than a silent outcome. Liquidity accounts should be modelled as
entity-owned from the outset. Carry-forward: `WAVE-H BANKING` (liquidity account ownership),
`WAVE-G REPORTING` (consolidation and intercompany elimination).

---

## FINDING 11 — The shipped Thai localization is thin, and several things a Thai deployment would need are simply not configured

**Class: VERIFIED FACT (what is present) / HOLD (what is required)**

### OBSERVATION

`ls | grep -i l10n_th` over the 797-module tree returns exactly two modules: `l10n_th` (Chart of
Accounts, LGPL-3, authored by a third party, version 2.0) and `l10n_th_reports` (Enterprise licence,
version 1.0, auto-install). Their combined content is 26 files. What is actually in them:

**Present.** A 27-account chart; VAT at 7% input and output plus zero-rated and exempt variants;
eight purchase-side WHT taxes and four sale-side WHT taxes; five tax groups; three report
definitions (VAT, PND53, PND3); two XLSX exports and two CSV exports; an EMV QR code payment
integration on the invoice report; a computed partner branch label; and an invoice report template.

**Verified absences** (scope: the two modules named, as read this session):

1. **No deferred / undue VAT accounts.** The chart has input VAT and output VAT only. There is no
   "VAT suspense", "undue input tax" or "undue output tax" account.
2. **No cash-basis tax configuration.** None of the Thai taxes sets `tax_exigibility`; the framework
   default is `on_invoice`. No `cash_basis_transition_account_id` is set on any Thai tax, and the
   company template does not set a `tax_cash_basis_journal_id`. The cash-basis machinery examined in
   Finding 6 is therefore inert for a stock Thai company.
3. **No tax payable account on any tax group.** The tax group template carries only id, name and
   country. Consequently `_get_tax_to_pay_on_closing` — which sums lines posted to tax groups'
   `tax_payable_account_id` — finds no accounts and returns zero, so the "Pay tax" follow-up activity
   is never scheduled for a Thai company.
4. **No Thai-language names for accounts or taxes.** The chart ships English names. The Thai
   translation catalogue for `l10n_th` contains 30 message ids, of which the only accounting-data
   entries are the five tax **group** names; no `account.account` name is translated. The one Thai
   string in executable code is a hardcoded literal used as the "Title" column for the PND53 export.
5. **No fiscal year end** is set by the template (Finding 9); a Thai company defaults to 31 December.
6. **No sale-side WHT tags.** The four sale-side withholding taxes carry **empty tag columns** on
   every repartition line, so they appear in no tax report at all (Finding 12).
7. **Zero-rated and exempt taxes have no tax group.** Only the 7% taxes are grouped. The XLSX VAT
   export sums tax only from the 7% group, while taking the untaxed base from the move total — so a
   move mixing 7% and exempt lines reports the whole move's untaxed amount against the 7% group.
8. **Only four WHT rates** (1%, 2%, 3%, 5%) and only two returns (PND3, PND53) are modelled.

All Thai account, tax, report and form names above are **candidate / UNVALIDATED**.

### EVIDENCE

- `SRC-TH l10n_th/__manifest__.py:1-29` — name "Thailand - Accounting", `countries: ['th']`, version
  2.0, LGPL-3, `auto_install: ['account']`, depends on `account_qr_code_emv` and `account`.
- `SRC-TH l10n_th_reports/__manifest__.py:1-23` — depends on `l10n_th` and `account_reports`,
  `auto_install: True`, OEEL-1.
- `SRC-TH l10n_th/data/template/account.account-th.csv` — 28 lines including header, i.e. 27
  accounts. Lines `:8`, `:9`, `:14`, `:15` are the four tax accounts: `a_input_vat` (1510),
  `a_wht_income` (1520), `a_output_vat` (2310), `a_wht` (2320). No account matching
  `undue|suspense|deferred` is present.
- `SRC-TH l10n_th/data/template/account.tax-th.csv:1` — the header row; the column list contains no
  `tax_exigibility` and no `cash_basis_transition_account_id` column.
- `SRC-A account/models/account_tax.py:180-184` — `tax_exigibility` Selection with
  `default='on_invoice'`.
- `SRC-TH l10n_th/data/template/account.tax.group-th.csv` — 6 lines: header plus five groups
  (`tax_group_1`, `_2`, `_3`, `_5`, `tax_group_vat_7`), columns `id,name,country_id` only. No
  `tax_payable_account_id`.
- `SRC-B account_reports/models/account_move.py:93-99` — `_get_tax_to_pay_on_closing` searches tax
  groups for `tax_payable_account_id` and sums matching lines; with no such account, the result is
  zero, and `:230-236` gates the "Pay tax" activity on that result being positive.
- `SRC-TH l10n_th/data/template/account.tax-th.csv:10,14,18,22` — the zero-rated and exempt taxes,
  each with an empty `tax_group_id` field.
- `SRC-TH l10n_th_reports/models/tax_report_vat.py:124` and `:131-134` — only
  `tax_group_vat_7` contributes to the exported VAT amount; `:128` takes
  `move.amount_untaxed_signed` for the whole move.
- `SRC-TH l10n_th/i18n/th.po` — 170 lines, 30 `msgid` entries; the only accounting-data references
  are `model:account.tax.group,name` at `:120`, `:125`, `:130`, `:135`, `:163`.
- `SRC-TH l10n_th_reports/models/tax_report_pnd.py:98` — the hardcoded Thai literal supplied as the
  `title` argument for the PND53 export.
- `SRC-TH l10n_th/models/template_th.py:9-31` — the complete company and chart template data.
- `SRC-TH l10n_th/models/account_move.py:6-10` — the only `account.move` override in the Thai
  localization: `_get_name_invoice_report`. Nothing about dates, taxes or locks.
- `SRC-TH l10n_th/models/res_partner.py:8-16` — `l10n_th_branch_name`, a **computed, non-stored**
  Char returning `"Branch <company_registry>"` or `"Headquarter"` for Thai company partners.

### CONTRADICTION

The branch label at `res_partner.py:8-16` is a presentation string derived from a generic
`company_registry` field. It is not a modelled branch identity: it is not stored, not selectable, and
carries no relationship to a branch entity. Any design that reads the reference's presence of a
"branch name" as evidence that branch registration is modelled would be wrong. Recorded as
`X3-CONTRA-08`.

### UNKNOWN

`HOLD / EVIDENCE REQUIRED — ACCOUNTING-TAX TRACK.` Every item below is a question for that track, not
a claim by this reviewer:

- Is a deferred/undue VAT mechanism required for any category of Thai supply, and if so which?
- Are Thai financial statements and statutory books required to be presented in Thai, and does that
  extend to account names in the general ledger?
- Is branch-level VAT registration and per-branch reporting required, and what identifies a branch?
- What is the complete set of VAT rates, zero-rated categories and exemptions that must be modelled?
- What is the complete set of withholding rates and payment natures?
- Are there statutory books (candidate / UNVALIDATED: sales tax report, purchase tax report, and a
  bound/sequenced general journal) with prescribed formats and prescribed ordering?

### RECOMMENDATION

`RECOMMENDATION:` do not treat the shipped Thai localization as a reference specification. It is a
minimal chart plus four export files. SMEsPlus must derive its Thai requirements from the
Accounting-Tax track's evidence, using the reference only as a negative checklist of what a thin
implementation omits. Carry-forward: `WAVE-D TAX`, with `WAVE-G REPORTING` for the statutory books.

---

## FINDING 12 — WHT suffered on receipts is booked at invoicing and reported nowhere

**Class: VERIFIED FACT (mechanism) / HOLD (requirement)**

### OBSERVATION

The Thai localization models withholding tax in **two** directions, and only one of them works
end-to-end.

**Withheld by us on payments to suppliers** (purchase side): eight taxes, tagged, posting to `a_wht`,
exported by the PND3 and PND53 CSV builders. Complete, subject to Finding 4's defects.

**Withheld from us by customers on our income** (sale side): four taxes named
`tax_wht_income_1/2/3/5`, `type_tax_use` = `sale`, `tax_excluded`, posting to `a_wht_income`
(candidate / UNVALIDATED: "Withholding Income Tax", code 1520, `asset_current`). Every one of their
repartition lines has an **empty tag column**. Because both PND exports select their population by
`tax_tag_ids`, these lines match nothing. They appear in no shipped report.

Two consequences:

**(a) No carrier for the WHT credit asset.** The amount accumulates in an asset account with no
report that ages it, no link to the withholding certificate that should evidence it, and no
mechanism to reconcile the balance against certificates actually received. It is a receivable from
the revenue authority with no subledger.

**(b) Recognition timing.** These are invoice-time taxes. The amount is computed and posted when the
sales invoice is issued, on the assumption that the customer will in fact withhold, at that rate.
Where the customer withholds a different amount, withholds nothing, or pays without a certificate,
the ledger and reality diverge and nothing detects it.

`INFERENCE:` withholding is an act of the payer at payment. Modelling it as a tax on the seller's
invoice books an asset before the event that creates it. Whether that is acceptable is a matter for
the Accounting-Tax track; that it is a modelling choice with a detectable failure mode is a
verified-fact consequence of the structure.

### EVIDENCE

- `SRC-TH l10n_th/data/template/account.tax-th.csv:58-73` — the four sale-side WHT taxes. Each
  block is four rows (base/invoice, tax/invoice, base/refund, tax/refund) and the tag column is
  empty on **every** row; the account column is `a_wht_income` on the tax rows; `price_include_override`
  is `tax_excluded`.
- `SRC-TH l10n_th/data/template/account.tax-th.csv:26-57` — by contrast, every purchase-side WHT row
  carries a tag (`+Income PND53` / `+PND53` / `+Income PND3` / `+PND3` and their negatives).
- `SRC-TH l10n_th_reports/models/tax_report_pnd.py:98` and `:135` — both exports build their domain
  as `[('tax_tag_ids', 'in', tag_templates._get_matching_tags().ids)]`, so untagged lines are
  excluded by construction.
- `SRC-TH l10n_th/data/template/account.account-th.csv:9` — `a_wht_income`, code 1520,
  `asset_current`, `reconcile` = False. **Not reconcilable**, so it cannot even be matched
  certificate by certificate using the ledger's own matching mechanism.
- `SRC-A account/models/account_move_line.py:1269-1271` — `_affect_tax_report` returns true for these
  lines (they have `tax_line_id`), so they **are** subject to the tax lock (Finding 5) despite
  appearing in no tax report.

### CONTRADICTION

Internal to the reference: the sale-side WHT lines are treated as tax-report-affecting for locking
purposes but as invisible for reporting purposes. They can block an operation on account of a tax
statement they never appear in. Recorded as `X3-CONTRA-09`.

The `reconcile = False` setting on `a_wht_income` is a second, independent defect: an account holding
individually-evidenced claims is configured so that it cannot be matched item by item.

### UNKNOWN

`HOLD / EVIDENCE REQUIRED — ACCOUNTING-TAX TRACK:` when WHT suffered is recognized, what evidence is
required to claim it as a credit, whether a certificate must be held and for how long, whether the
credit must be reconciled to certificates, and in which period a credit is claimable when the
certificate arrives late.

### RECOMMENDATION

`RECOMMENDATION:` model WHT suffered as an evidenced, item-matched receivable with a certificate
record, not as an invoice-time tax on a non-reconcilable account. This is a Wave B requirement in
substance but imposes a Wave A structural requirement: the ledger must permit an item-level matching
dimension on a tax-driven account. Carry-forward: `WAVE-B AR` (recognition and certificate matching),
`WAVE-D TAX` (claimability and period).

---

## FINDING 13 — Producer→consumer inventory and the minimum handoff contract Wave A must define

**Class: VERIFIED FACT (module inventory) / RECOMMENDATION (contract)**

### OBSERVATION

Wave A defines the ledger that everything else posts into. Before Wave A closes, the **shape** of what
producers hand over must be fixed, or every later Wave will negotiate it separately.

Modules in the reference tree that reference or create journal entries — the producer population
Wave A must be able to consume — number 59. Grouped by the business event they emit:

| Producer domain | Representative modules found | Event emitted |
|---|---|---|
| Sales / AR | `sale`, `sale_stock`, `sale_mrp`, `sale_project`, `sale_timesheet`, `sale_subscription`, `website_sale`, `event_booth_sale`, `membership` | customer invoice, credit note, deferred revenue trigger |
| Purchase / AP | `purchase`, `purchase_stock`, `purchase_mrp`, `project_purchase`, `mrp_subcontracting_purchase` | vendor bill, refund, accrual |
| Inventory / costing | `stock_account`, `stock_accountant`, `stock_landed_costs`, `stock_dropshipping`, `mrp_account` | stock valuation entry, COGS, landed cost allocation |
| Assets | `account_asset` | acquisition, depreciation schedule, disposal |
| Payment / banking | `account_payment`, `account_batch_payment`, `account_check_printing`, `account_online_synchronization`, `pos_settle_due` | payment, settlement, statement line |
| Expense / payroll | `hr_expense`, `sale_expense`, `hr_payroll_account`, `hr_payroll_expense` | employee expense, payroll journal |
| Point of sale | `point_of_sale`, `pos_sale` | session closing entry |
| Treasury / internal | `account_auto_transfer`, `account_loans`, `account_inter_company_rules` | automatic transfer, loan schedule, intercompany mirror |
| Tax / reporting | `account_reports`, `account_reports_cash_basis`, `account_update_tax_tags`, `l10n_th_reports` | tax closing entry, cash-basis entry, tag remap |
| Service / documents | `helpdesk_account`, `helpdesk_stock_account`, `industry_fsm_sale`, `documents_account`, `account_edi`, `account_edi_ubl_cii`, `account_invoice_extract` | inbound/outbound document, extracted bill |

`INFERENCE:` the population is large enough that an implicit handoff contract will not hold. Every
one of these producers currently relies on `account.move` defaulting the accounting date for it —
which is exactly how Findings 1, 2, 6 and 10 arise.

`RECOMMENDATION:` the minimum handoff contract from any producer to the Wave A ledger must carry, as
mandatory fields:

1. **Producer identity** — the source module and the source record, as a durable reference that
   survives the source record's own lifecycle.
2. **Event identity** — an idempotency key, so a re-emitted event is detected rather than double-posted.
3. **Document date** — the date on the source document.
4. **Event date** — the date the economic event occurred, where different from the document date.
5. **Proposed accounting date** — what the producer believes the ledger date should be. The ledger
   may override it, but must record that it did, and to what, and why.
6. **Tax point date** — per tax line, independent of all of the above (Findings 3, 4).
7. **Company and currency**, with the rate the producer used and its source (Finding 7).
8. **Reversal policy** — whether the event is correctable by reversal, by amendment, or not at all.
9. **Period-closed behaviour** — what the producer requires the ledger to do when the target period
   is closed: reject, shift with notice, or queue. This must be the producer's declaration, not the
   ledger's silent choice (this is the direct remedy for Findings 1, 2 and 6).

### EVIDENCE

- Module inventory derived by a recursive grep for `account.move` references across
  `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/`, returning 59 module
  directories. The named modules above are drawn from that result.
- `SRC-A account_inter_company_rules/models/account_move.py:88-99` — a worked example of a producer
  handing over a document without an accounting date, letting the ledger derive it (Finding 10).
- `SRC-A account/models/account_move.py:801-815` — the ledger-side derivation that fills the gap,
  and the reason the gap is invisible to producers.
- `SRC-A account/models/account_partial_reconcile.py:512-514` — a second worked example: a producer
  (the reconciliation engine) choosing a date against a lock the ledger will re-check differently
  (Finding 6).

### CONTRADICTION

None identified.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` which of these producers are actually in SMEsPlus scope. The Boss
scope for Waves B through H was not read by this reviewer, so the inventory above is the reference
population, not the SMEsPlus population. It should be intersected with the approved scope before it
is used to size anything.

### RECOMMENDATION

`RECOMMENDATION:` Wave A should publish the handoff contract as a Wave A deliverable, and every later
Wave should be required to conform to it rather than extend it. Boss decision required on whether the
contract is a Wave A gate item. Carry-forward: all of `WAVE-B AR` through `WAVE-H BANKING`.

---

## EXPERT 3 POSITION

My position on Wave A, from the integration and localization lens, is `HOLD`. I do not identify a
`VETO` item, and I do not approve anything; Boss is sole final approver.

The single most important thing I found is not any one defect but a structural pattern that runs
through all of them: **the reference implementation treats the accounting date as a derived,
mutable, ledger-owned field, and every localization artefact then reads that field as though it were
the document's own date.** Finding 1 shows the derivation is more aggressive than the evidence base
records; Finding 2 shows it fires on purchase documents even with no lock in place; Findings 3 and 4
show that both Thai statutory exports print that derived date under headings that assert it is the
invoice or bill date, and select their filing populations by it. That chain is the highest-risk item
in my lens, and I want it recorded that the risk arises from the *combination*, not from the lock
mechanism alone. EV-009 identified the right area and, in my assessment, understated it.

I want to be precise about what I am and am not saying regarding Thailand. I am **not** saying the
reference behaviour produces an incorrect Thai VAT or withholding filing. I cannot say that, and I
have not tried to; every statement in this review about what Thai law requires is marked
`HOLD / EVIDENCE REQUIRED` and routed to the Accounting-Tax track, and every Thai account, report and
form name is marked candidate / UNVALIDATED. What I am saying is narrower and, I think, stronger:
the system **cannot demonstrate** which date it used as the tax point, because it does not store one.
The tax point is inferred from a field that three separate mechanisms are entitled to rewrite. That
is a structural evidentiary gap that exists independently of what the statute turns out to require,
and it will exist under any statute. It is therefore decidable now, in Wave A, and it should be:
`tax_point_date` must be a stored, first-class field on the tax line.

The second thing I would put in front of Boss is Finding 5. I was asked specifically how tax lock and
fiscal lock interact, and the honest answer is that they barely interact at all — they are two
mechanisms wearing one vocabulary. The tax lock is absent from the composed fiscal lock that most of
the ledger consults; it applies only to entries that carry tax; it shifts on the way in and rejects
on the way out; and there is exactly one of it per company, shared by the VAT return and both
withholding returns, alongside exactly one periodicity setting. Finding 6 shows the collision this
produces in ordinary use: reconciling a payment against an older cash-basis invoice fails inside the
user's transaction rather than at generation time. Whether Thai filing deadlines actually differ
between VAT and withholding is `HOLD`; but the design decision — one lock or several — does not
depend on the answer, because a design with several locks satisfies both cases and a design with one
lock satisfies only one. I would take the several-lock design and let the Accounting-Tax track tell
us later how many.

On EV-018 I disagree with the evidence base in a way that mostly strengthens its conclusion. Rate
types do exist — historical, closing and average — but only inside a temporary table dropped at the
end of each report run, built for the narrow purpose of consolidating companies with different
functional currencies, and derived entirely from the same single daily scalar. So EV-018's practical
conclusion holds: there is no posting-layer carrier for a closing rate distinct from a transaction
rate. Its deferred question about a synthesised average rate is answered — yes, days-weighted, at
report time. I add one defect of my own that the evidence base does not carry and that I consider
serious: when no rate record exists for a currency, the lookup silently returns 1.0. A foreign-currency
transaction in a currency whose rates were never loaded posts at par, with no error and no warning.
Combined with Finding 8 — where the closing rate used for revaluation can be typed into a report,
produces only a dismissible banner, and is never stored on the resulting entry — the multi-currency
story is that the most consequential numbers in the ledger are determined by inputs the ledger does
not retain.

On EV-016 I reached the same conclusion independently and found the one plausible counter-example —
a model actually named for the financial year — to be a settings dialog with no records. I confirm
it. What I would add is scope discipline: the finding should read "no fiscal year entity was located
in the tree searched", not "does not exist". And I would move the closed-period record forward into
Wave A rather than leaving it to Wave G, because a close cannot be evidenced by a setting that can
be moved backwards, and Wave A is where the ledger's own vocabulary is fixed.

On multi-company, EV-001, EV-008 and EV-019 are all confirmed, with one one-line citation drift
noted at EV-019. The integration consequence I would add is Finding 10(a): an intercompany pair
carries its document date across but not its accounting date, and the receiving leg is a purchase
document, so it is re-dated by the rule in Finding 2 and then again by the receiving company's own
locks. Two legs of one transaction can post in different months, or across a year boundary in
different years, with nothing detecting it. Combined with the hard lock cascading irreversibly down
the parent chain, a parent can force that divergence on a subsidiary and cannot undo it.

On the Thai localization itself I want to set expectations plainly, because I think there is a risk
of the reference being read as a specification. It is not one. It is two modules, 26 files, a
27-account chart with English names, four export files, and a QR code. It configures no deferred VAT,
no cash-basis exigibility, no tax payable account on any tax group — with the result that the
"pay the tax" follow-up never fires for a Thai company — and no fiscal year end, so a Thai company
defaults to 31 December. Its sale-side withholding taxes are untagged and therefore appear in no
report while still being subject to the tax lock, and they post to a non-reconcilable account, so the
withholding credit cannot be matched to the certificates that evidence it. Its withholding export
recomputes the tax amount from the rate rather than reading the posted balance, so the statutory file
and the ledger can disagree with no reconciliation point between them, and it infers the nature of
each payment from its percentage through a hardcoded four-way map. I regard that recomputation as the
most serious purely technical defect I found anywhere in the localization layer, because it is a
silent divergence between what was posted and what was filed.

Finally, Finding 13. Fifty-nine modules in the reference tree post into this ledger. Every one of
them currently relies on the ledger to choose the accounting date on its behalf, which is precisely
how Findings 1, 2, 6 and 10 arise. If Wave A closes without a published producer→consumer handoff
contract — one that makes the producer declare its document date, its event date, its proposed
accounting date, its tax point, its rate and source, and what it wants to happen when the target
period is closed — then each of Waves B through H will invent its own, and the divergences will be
discovered one at a time in production. I would make that contract a Wave A gate item.

Everything above is offered as evidence and analysis for Boss decision. Nothing here is an approval.

---

## CROSS-WAVE CARRY-FORWARD

| # | Dependency raised | From finding | Wave | Class | Status |
|---|---|---|---|---|---|
| X3-CF-01 | Late/backdated document policy: reject vs re-date vs accept-with-exception; the actual shift rule is period-end/today, not lock+1 | 1, 2 | `WAVE-D TAX` | VERIFIED FACT → decision | HOLD |
| X3-CF-02 | Purchase documents re-dated with no lock present; document date vs ledger date diverge by default | 2 | `WAVE-C AP` | VERIFIED FACT | HOLD |
| X3-CF-03 | `tax_point_date` as a stored first-class field on the tax line, independent of document and accounting date | 3, 4 | `WAVE-D TAX` | RECOMMENDATION (Wave A structural) | HOLD |
| X3-CF-04 | VAT period attribution: which date determines the Thai VAT period, and permitted input-tax claim window | 3 | `WAVE-D TAX` | HOLD / EVIDENCE REQUIRED | HOLD — Accounting-Tax track |
| X3-CF-05 | WHT export recomputes amount from rate instead of reading posted balance — ledger/filing divergence with no reconciliation point | 4 | `WAVE-D TAX` | VERIFIED FACT | HOLD |
| X3-CF-06 | Payment-nature classification must be recorded on the transaction, not inferred from the WHT rate | 4 | `WAVE-D TAX` | RECOMMENDATION | HOLD |
| X3-CF-07 | Withholding certificate as a record, reproducible from the ledger | 4, 12 | `WAVE-D TAX` | HOLD / EVIDENCE REQUIRED | HOLD — Accounting-Tax track |
| X3-CF-08 | Lock model: separate lock domains per return type; one consistent violation semantic (shift or reject, not both) | 5 | `WAVE-D TAX` | RECOMMENDATION (Wave A structural) | HOLD |
| X3-CF-09 | Filing periodicities and deadlines per Thai return; whether one periodicity setting can serve VAT and withholding | 5 | `WAVE-D TAX` | HOLD / EVIDENCE REQUIRED | HOLD — Accounting-Tax track |
| X3-CF-10 | Whether posting a PND closing entry sets the same company tax lock as the VAT closing | 5 | `WAVE-D TAX` | UNKNOWN — EVIDENCE REQUIRED | UNKNOWN |
| X3-CF-11 | Cash-basis VAT applicability in Thailand; the shipped Thai template configures none | 6, 11 | `WAVE-D TAX` | HOLD / EVIDENCE REQUIRED | HOLD — Accounting-Tax track |
| X3-CF-12 | Reconciliation fails inside the user transaction when the cash-basis date lands between fiscal and tax lock | 6 | `WAVE-H BANKING` | VERIFIED FACT | HOLD |
| X3-CF-13 | Generated entries must carry origin date, generating date and posting date | 6 | `WAVE-F TIME-BASED RECOGNITION` | RECOMMENDATION | HOLD |
| X3-CF-14 | Posting-layer rate model with rate type and source; missing rate must error, not default to 1.0 | 7 | `WAVE-G REPORTING` + Wave A structural | VERIFIED FACT → decision | HOLD |
| X3-CF-15 | Thai FX treatment: initial recognition, closing-rate translation of monetary items, historical rate for non-monetary, mandated rate source | 7, 8 | `WAVE-G REPORTING` | HOLD / EVIDENCE REQUIRED | HOLD — Accounting-Tax track |
| X3-CF-16 | Revaluation rate must be stored on the generated entry; custom rate must require an authorised override record | 8 | `WAVE-G REPORTING` | RECOMMENDATION | HOLD |
| X3-CF-17 | Closed-period record with actor and timestamp, as ledger structure rather than a movable setting | 9 | `WAVE-G REPORTING` (structure in Wave A) | RECOMMENDATION | HOLD |
| X3-CF-18 | Year-end result appropriation: posted entry vs report-time computation; legal reserve | 9 | `WAVE-G REPORTING` | HOLD / EVIDENCE REQUIRED | HOLD — Accounting-Tax track |
| X3-CF-19 | Prior-period adjustment and audit-adjustment route after close | 9 | `WAVE-G REPORTING` | HOLD / EVIDENCE REQUIRED | HOLD — Accounting-Tax track |
| X3-CF-20 | Fiscal year end not set by the Thai template; defaults to 31 December | 9, 11 | `WAVE-D TAX` | VERIFIED FACT | HOLD |
| X3-CF-21 | Intercompany legs can post in different periods/years; parent hard lock cascades irreversibly | 10 | `WAVE-G REPORTING` | VERIFIED FACT | HOLD |
| X3-CF-22 | Liquidity accounts are entity-owned and cannot be shared; consolidation mapping must special-case them | 10 | `WAVE-H BANKING` | VERIFIED FACT | CONFIRMED |
| X3-CF-23 | Thai-language presentation of accounts and statutory books; shipped chart is English-only | 11 | `WAVE-G REPORTING` | HOLD / EVIDENCE REQUIRED | HOLD — Accounting-Tax track |
| X3-CF-24 | Branch-level VAT registration and reporting; the reference has a computed label, not a branch entity | 11 | `WAVE-D TAX` | HOLD / EVIDENCE REQUIRED | HOLD — Accounting-Tax track |
| X3-CF-25 | Tax payable account per tax group is unset for Thailand; the tax-payment follow-up never fires | 11 | `WAVE-D TAX` | VERIFIED FACT | HOLD |
| X3-CF-26 | WHT suffered: item-matched receivable with certificate evidence; account currently non-reconcilable and untagged | 12 | `WAVE-B AR` | VERIFIED FACT → decision | HOLD |
| X3-CF-27 | WHT suffered recognized at invoice rather than at the customer's act of withholding | 12 | `WAVE-B AR` | INFERENCE | HOLD |
| X3-CF-28 | Producer→consumer handoff contract as a Wave A published deliverable | 13 | all of `WAVE-B AR` … `WAVE-H BANKING` | RECOMMENDATION | HOLD |
| X3-CF-29 | Inventory/costing producers (stock valuation, COGS, landed cost) must declare period-closed behaviour | 13 | `WAVE-F TIME-BASED RECOGNITION` | RECOMMENDATION | HOLD |
| X3-CF-30 | Analytic dimension is carried on the producer's line but is deleted on un-post (per EV-012, not re-verified here) | 13 | `WAVE-E ANALYTIC` | UNKNOWN — EVIDENCE REQUIRED | UNKNOWN |

---

*End of X3 — Expert 3 review. No approval granted. Boss is sole final approver.*
