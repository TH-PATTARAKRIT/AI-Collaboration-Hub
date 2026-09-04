# P06_FX_FEE_INTEREST_MATRIX.md

**Session:** SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001 · **Process:** P06 Bank-to-Reconcile
**Branch:** research/account-p06-bank-to-reconcile-2026-09-04-001 (base `88f52cd`)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Scope model:** per `[SMEPLUS-26-09-04-ACC-REV2-CORR1]` — see the Scope Ownership Matrix for the scope of each configuration point named below.

---

## PART A — FOREIGN EXCHANGE

## A1. Which rate governs a bank settlement

**FX-F-01 — The statement line derives its own implicit rates from the amounts the bank reported. It does not consult the rate table.**
`$V18E/account/models/account_bank_statement_line.py:605-606`:
```
rate_journal2foreign_curr = abs(transaction_amount) / abs(journal_amount) if journal_amount else 0.0
rate_comp2journal_curr = abs(journal_amount) / abs(company_amount) if company_amount else 0.0
```
The docstring is explicit (`:588-590`): *"Convert the amounts passed as parameters to the statement line currency using the rates provided by the bank."*

**This answers the open FX question carried from Account Wave A (blocker GB-08 / cross-process F-10) for the bank path specifically: at settlement, the bank's implied rate governs, not the rate table.** The difference against the invoice's own rate is resolved into an exchange-difference move. That is defensible accounting — the bank's rate is the realised rate — but it means **the rate table is not the single source of truth for realised FX**, and any control that reconciles realised FX to the rate table will disagree with the ledger by design.

**FX-F-02 — Four silent zero-rate branches.**
`$V18E/account/models/account_bank_statement_line.py:613-626`. When `journal_amount` or `company_amount` is zero, the derived rate is `0.0` and the resulting balance is set to `0.0`:
```
if rate_comp2journal_curr:
    new_balance = company_currency.round(journ_amount_currency / rate_comp2journal_curr)
else:
    new_balance = 0.0
```
**A zero-amount leg silently produces a zero-balance counterpart rather than an error.** Combined with SD-1 (zero-amount imported transactions are discarded), zero is a value the ingestion and conversion layers both treat as "nothing to do" rather than "something is wrong."

**FX-F-03 — Only one of three branches falls back to the dated rate table.**
`$V18E/account/models/account_bank_statement_line.py:621-624` — the fallback applies when the currency is neither the transaction nor the journal currency **and** `balance is None`.

**FX-F-04 — The source of `transaction_amount` flips depending on reconciliation cleanliness.**
`$V18E/account/models/account_bank_statement_line.py:570-576`:
```
if suspense_line and not other_lines:
    transaction_amount = -suspense_line.amount_currency
else:
    # In case of to_check or partial reconciliation, we can't trust the suspense line.
```
**The rate a partially reconciled statement line implies is computed from a different input than the rate a cleanly reconciled one implies.** The in-code comment states the reason plainly. For P06 this means the realised rate on a partial settlement is not derived the same way as on a full one.

**FX-F-05 — Five callers consume the statement-line rate; five of them are inside the reconciliation widget.**
**DENOMINATOR:** PATTERN `_prepare_counterpart_amounts_using_st_line_rate` over `$V18E`, excluding `.pyc`. UNIT: occurrence. **RESULT = 9**: 1 definition, 2 tests, 1 in `account_accountant/models/account_reconcile_model.py:526`, and **5 in `account_accountant/models/bank_rec_widget.py` (742, 781, 851, 937, 1055)**. The bank-rec widget is the principal consumer of bank-implied rates.

## A2. The 1.0 fallback chain

**FX-F-06 — The silent parity fallback is in SQL, and it stacks two degradations.**
The methods are **not** in `$V18E/account/models/res_currency.py` (full read, 336 lines — NOT FOUND, PATTERN `_get_conversion_rate|_convert`). They are on the base model:
`$V18E/base/models/res_currency.py:138-141`:
```
SQL("COALESCE((%s), (%s), 1.0)", rate_query.select(rate), rate_fallback.select(rate))
```
Degradation 1: **no rate at or before the date → the earliest rate ever recorded is substituted.** Degradation 2: **no rate at all → 1.0.** Neither is reported.
A second parity fallback sits in the Python compute (`:156-158`), and `_get_conversion_rate` (`:266-271`) performs no validation, inheriting both.

**FX-F-07 — Two further parity fallbacks exist in the reporting-currency layer.**
`$V18E/account/models/res_currency.py:178` and `:206` — `CASE WHEN rate.id IS NOT NULL THEN ... ELSE 1 END`; `:307` — `COALESCE(out_period_rate.rate, 1.0) AS rate`.
**Four independent 1.0 fallbacks across the conversion and reporting stack.** This corroborates and extends the Account Wave A finding of a silent 1:1 FX fallback: it is not one branch, it is a pattern.

**FX-F-08 — `_convert` asserts only on empty recordsets.**
`$V18E/base/models/res_currency.py:282-289` — `assert self, "convert amount from unknown currency"`. Rate availability is never asserted.

## A3. Exchange difference posting

**FX-F-09 — Journal and accounts are company configuration with no fallback; gain/loss is chosen purely by sign.**
`$V18E/account/models/account_move_line.py:2718-2724`. Config validation is **deferred to move-creation time** (`:2841-2851`), and if the FX journal is unset the accounting date is computed as `date.min` (`:2745`) before that guard fires.

**FX-F-10 — Undoing a reconciliation reverses the exchange-difference move rather than deleting it, into a possibly different period.**
`$V18E/account/models/account_partial_reconcile.py:115-133`, with the lock-aware forward shift at `$V18E/account/models/account_move.py:5669-5674`. Exchange-difference entries can never be reset to draft (`$V18E/account/models/account_move.py:5343-5345`).

---

## PART B — BANK FEES AND BANK INTEREST

**FFI-F-01 — There is no bank-fee or bank-charge concept anywhere in the searched scope.**
**DENOMINATOR:** PATH SET: `$V18E/account`, `$V18E/account_accountant`, `$V18E/payment`, `$V18E/account_online_synchronization`, recursive, all file types. PATTERN: `bank_fee|bank_charge|transaction_fee`, case-insensitive. UNIT: matching line. **RESULT = 0.**
**Class A within that declared scope.** Not a claim about Odoo 18 in general; a claim about those four modules as read.

**FFI-F-02 — There is no bank-interest concept either.**
PATTERN `interest`, case-insensitive. `$V18E/account/models/*.py` + `$V18E/account/wizard/*.py`: **1 hit**, and it is an English comment about the dashboard (`$V18E/account/models/account_move.py:3913`). `$V18E/account_accountant` recursive: **0**. `$V18E/account_online_synchronization/models/*.py`: **0**.
**Class A within those declared scopes.**

**FFI-F-03 — The only bank-fee artefact in the reference is a chart-of-accounts row that no code references.**
`$V18E/account/data/template/account.account-generic_coa.csv:37` — `"expense_finance","Bank Fees","6200","expense",...`. An account exists; nothing posts to it automatically.

**FFI-F-04 — The only available mechanism is a reconcile-model write-off line, and for a variable fee that means a regex over the bank's free-text narrative.**
`$V18E/account_accountant/models/account_reconcile_model_line.py:96-107`:
```
elif self.amount_type == 'regex':
    match = re.search(self.amount_string, st_line.payment_ref)
...
    extracted_balance = float(extracted_match_group.replace(decimal_separator, '.'))
```
and `:104-107` — **a `ValueError` is swallowed to `0.0`, and a non-match also yields `0.0`.**
**Consequence: a mis-specified or drifted regex silently books a zero fee.** The entry balances, the statement reconciles, and the fee expense is simply absent. There is no error, no flag, and no difference to notice — because the amount that failed to parse is the amount that was not posted.
The four amount types are `fixed`, `percentage`, `percentage_st_line`, `regex` (`$V18E/account/models/account_reconcile_model.py:68-71`); zero-amount write-off lines are dropped entirely (`$V18E/account_accountant/models/account_reconcile_model.py:33-37`).

**FFI-F-05 — Thai bank narrative formats are not held by this session.** Whether any Thai bank's statement narrative carries a parseable fee amount is **HOLD / EVIDENCE REQUIRED** (source NC-03). No regex design can be validated here.

---

## PART C — PAYMENT PROVIDER FEES

**FFI-F-06 — Provider fee fields do not exist in v18.**
**DENOMINATOR:** PATH SET `$V18E/payment/models/*.py`. PATTERN `fees` for the specific names, and `fee` case-insensitive for the general case. **RESULT = 0.** `fees`, `fees_active` and `_compute_fees` are **NOT FOUND** on `payment.provider` or `payment.transaction`. **Class A within that path set.**

**FFI-F-07 — And no provider fee is posted to the general ledger.**
PATH SET `$V18E/account_payment`, recursive `.py`. PATTERN `fee`, case-insensitive. **RESULT = 0.** **Class A within that path set.**

**FFI-F-08 — Consequence: net-versus-gross settlement is unhandled.**
A provider that settles a batch net of its commission produces one bank credit that does not equal the sum of the transactions it settles. The reference has no fee concept to absorb the difference, so it becomes a manual write-off (Part B) with the same regex fragility, or it is left in suspense (EGL-F-06) where no ageing report can see it.
**This is the most operationally consequential gap in this file for a Thai SME accepting card or e-wallet payments.** Raised as `P06-B-25`.

**FFI-F-09 — The provider's landing journal is resolved implicitly, and silently defaults to the first bank journal found.**
`$V18E/account_payment/models/payment_provider.py:84-91`:
```
elif provider.state in ('enabled', 'test'):
    provider.journal_id = self.env['account.journal'].search([('company_id', '=', provider.company_id.id), ('type', '=', 'bank')], limit=1,)
```
**`limit=1` with no `order` clause.** In the 12-bank-journal estate evidenced at runtime (CPO-F-04), which journal a provider settles into is decided by whichever row the database returns first.
And the method line's account is inherited from a same-code sibling if one exists (`:70-72`), otherwise left unset — which then raises at payment time per the outstanding-account chain (EGL §1).

---

## PART D — WRITE-OFF, EARLY PAYMENT DISCOUNT, CASH BASIS

**FFI-F-10 — Six write-off entry points, none of which requires an account.**

| # | Entry point | Evidence | Account required? |
|---|---|---|---|
| W-1 | Payment register wizard | `$V18E/account/wizard/account_payment_register.py:140-148,1018-1025` | **No** at ORM level; domain is only `[('deprecated','=',False)]` |
| W-2 | FX-account special case — no write-off line; the balance is forced instead | `$V18E/account/wizard/account_payment_register.py:1004-1009`, detection at `:826-836` | n/a |
| W-3 | Early-payment-discount mode — the whole write-off section is hidden | `:847-849` | n/a |
| W-4 | Reconcile model, `writeoff_button` | `$V18E/account_accountant/models/bank_rec_widget.py:171-175` | **No** — the key is omitted if unset (`account_reconcile_model_line.py:53-55`) |
| W-5 | Automatic tolerance write-off | `$V18E/account_accountant/models/account_reconcile_model.py:554-560` | inherits W-4 |
| W-6 | Widget manual line (an edited `auto_balance`) | `$V18E/account_accountant/models/bank_rec_widget.py:389-392` | **No**; only the suspense account blocks validation (`:203-208`) |

**NOT FOUND: any approval or amount limit on a write-off.** Three independent search scopes, all zero — see the Edge Case Matrix E5 for the exact patterns. **Class A within those scopes.**

**FFI-F-11 — Early-payment discount selects its account by document direction, not by sign.**
`$V18E/account/models/account_move.py:4401-4404` — inbound → **loss** account, outbound → **gain** account. Two dedicated company accounts (`$V18E/account/models/company.py:120-121`), seeded from the generic chart (`template_generic_coa.py:52-53`).
Three tax treatments (`included`, `excluded`, `mixed` — `$V18E/account/models/account_payment_term.py:41`); only `included` **with taxes present** restates the tax base (`account_move.py:4392-4393,4410`). No discount percentage → nothing generated, silently (`:4356-4357`).

**FFI-F-12 — In the bank-rec widget, early-payment discount requires an EXACT amount match.**
`$V18E/account_accountant/models/bank_rec_widget.py:567-568`:
```
def _do_amounts_apply_for_early_payment(self, open_amount_currency, total_early_payment_discount):
    return self.transaction_currency_id.compare_amounts(open_amount_currency, total_early_payment_discount) == 0
```
**A one-satang rounding difference defeats automatic discount recognition**, and the amount then falls through to `auto_balance` or a write-off — i.e. a legitimate discount is silently reclassified as a difference. Gated on same-currency, and the EPD lines are torn down and rebuilt on every recompute (`:607-613`), carrying full tax payloads (`:637-641`).

**FFI-F-13 — Cash-basis entries are generated inside the reconciliation transaction, after partials and after exchange differences.**
`$V18E/account/models/account_move_line.py:2540-2552`. Ordering: partials → exchange difference → cash basis → full reconcile. Trigger: company `tax_exigibility` **and** the reconciled account is AR/AP (`:2545-2547`).
Two context keys silently suppress it: `move_reverse_cancel` and `no_cash_basis` (`:2551`). Account determination has a three-deep silent fallback (`$V18E/account/models/account_partial_reconcile.py:400`). Date is the partial's `max_date`, or **today** if that precedes the lock date (`:513-514`).
On undo, cash-basis moves are located by `tax_cash_basis_rec_id` and **reversed, not deleted** (`:115-133`), and can never be reset to draft — the code keeps `tax_cash_basis_origin_move_id` as a second permanent marker precisely because the first is emptied by the undo (`$V18E/account/models/account_move.py:5344-5350`).

---

## PART E — Summary of unowned money

| Money type | First-class concept? | Account owner | Ageing visibility |
|---|---|---|---|
| Realised FX difference | yes | company config | in P&L |
| Bank charge | **no** | **none** | n/a |
| Bank interest | **no** | **none** | n/a |
| Provider commission | **no** | **none** | n/a |
| Settlement write-off | mechanism only | **free choice, unconstrained** | wherever it was posted |
| Early payment discount | yes | company config | in P&L |
| Cash-basis tax | yes | 3-deep fallback | in tax reports |
| Unidentified receipt | account only | journal suspense | **none** — EGL-F-06 |
| Money in transit between own banks | account only | company transit | **none** — EGL-F-07 |

---

## Requirements arising

| ID | Requirement |
|---|---|
| FX-R-01 | The realised rate at settlement must be recorded on the settlement, with its source (bank-implied / rate table / manual) named. |
| FX-R-02 | No conversion may fall back to parity. A missing rate must deny, not default. |
| FX-R-03 | A zero derived rate must be an error, never a zero balance. |
| FFI-R-01 | Bank charges, bank interest and provider commissions must be first-class event types with owned accounts. |
| FFI-R-02 | A fee amount that cannot be determined must block, never post zero. |
| FFI-R-03 | Net settlement must be decomposable into gross plus fee, with a proof that the two reconcile to the single bank credit. |
| FFI-R-04 | Write-offs must be bounded by account type, by amount, and by approval. |
| FFI-R-05 | A discount defeated by rounding must be reported as a discount within tolerance, not silently reclassified. |
| FFI-R-06 | The provider settlement journal must be an explicit configuration, never an unordered `limit=1` search. |

## Open items

| ID | Item | Class |
|---|---|---|
| P06-OQ-30 | Which callers pass `no_cash_basis=True` or `move_reverse_cancel=True` on the P06 path was not enumerated. | C |
| P06-OQ-31 | Whether `writeoff_account_id` is enforced `required` at the view layer was traced in Python only. | C |
| P06-OQ-32 | Thai bank statement narrative formats — needed to assess FFI-F-04 in practice. | **HOLD / EVIDENCE REQUIRED** |

---

# End
