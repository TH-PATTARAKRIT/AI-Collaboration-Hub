# P06_EDGE_CASE_MATRIX.md

**Session:** SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001 · **Process:** P06 Bank-to-Reconcile
**Branch:** research/account-p06-bank-to-reconcile-2026-09-04-001 (base `88f52cd`)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Scope model:** `[SMEPLUS-26-09-04-ACC-REV2-CORR1]` applied.

---

## 0. What this file covers

Money that does **not** cleanly settle. For each case: is there a first-class concept, or only an emergent pattern? Where does the money sit? What makes it visible and ageable? How is it cleared?

The recurring answer, stated once so it need not be repeated: **most of these have an account but no clock.** The reference gives unsettled money a home; it rarely gives it a deadline or a report.

---

## E1 — Unidentified receipt

**(i) Concept:** an account, not a model. `journal.suspense_account_id` (`$V18E/account/models/account_journal.py:116-122`), defaulting from `company.account_journal_suspense_account_id` (`:420-429`), domain-restricted to `asset_current` (`:121`).
**(ii) Account:** forced as the counterpart of every new statement line, and its absence is a hard stop (`$V18E/account/models/account_bank_statement_line.py:645-652`). This is correct design.
**(iii) Visibility:** classification is by **account identity**, not a flag (`:709-710`). The bank reconciliation report surfaces unreconciled lines via `is_reconciled` (`$V18E/account_reports/models/bank_reconciliation_report.py:245`).
**(iv) Clearing:** by rewriting the counterpart line through the widget.

**EC-F-01 — There is no ageing over the suspense balance, and the standard ageing report is structurally incapable of covering it.**
PATTERN `-i suspense` over `$V18E/account_reports`: **7 hits, all in `tests/test_reconciliation_report.py`. Non-test hits = 0.**
And `$V18E/account_reports/models/account_aged_partner_balance.py:156` scopes by `account_id.account_type`, where `internal_type` is only ever `asset_receivable` or `liability_payable` (`:85,88`) — an `asset_current` suspense account can never appear.
**Class A within `$V18E/account_reports`.** Whether a custom report in the SMEsPlus trees does this was **not searched** — Class C, `P06-OQ-60`.
**Consequence:** money the business cannot identify accumulates where no standard ageing report can see it. For a Thai SME this is the classic year-end surprise. `P06-B-18`.

---

## E2 — Overpayment

**(i) Concept:** none. Two emergent paths, and the only control is a two-value selection: `payment_difference_handling` ∈ {`open`, `reconcile`} (`$V18E/account/wizard/account_payment_register.py:133-139`), defaulting to `open` unless early-discount mode (`:839-844`).
**(ii) Account:**
- `open` → the excess stays as an unreconciled residual on the **receivable/payable** account (`$V18E/account/models/account_payment.py:354-364`).
- `reconcile` → the user's chosen `writeoff_account_id` (`:1018-1024`).
- Bank-rec widget → an `auto_balance` line, landing on receivable/payable **if a partner is resolvable**, otherwise on **suspense** (`$V18E/account_accountant/models/bank_rec_widget.py:449-466`).
**(iii) Visibility:** good when it lands on AR/AP — it appears in the ageing report. When it lands on suspense it inherits E1's blind spot.
**(iv) Clearing:** by later reconciling against a future invoice, or by write-off.

**EC-F-02 — There is no "customer credit" or "money on account" object.**
PATTERN `payment_difference_handling` over `$V18E/account`: **6 hits, all in the register wizard.** An overpayment is a negative residual, not a thing. **Class A within that scope.**
**Consequence:** a customer's credit balance cannot be confirmed to the customer, cannot be aged as a liability, and cannot be reported separately from ordinary receivables. For Thai statutory reporting this may matter — routed to Accounting-Tax as **HOLD**.

**EC-F-03 — Overpayment bypasses the tolerance check entirely and permits auto-reconcile.**
`$V18E/account_accountant/models/account_reconcile_model.py:542-546`, with the in-code comment: *"the payment amount is higher than the sum of invoices … don't check the tolerance and don't try to generate any write-off."*

---

## E3 — Underpayment / partial payment

**(i) Concept:** yes — `payment_state = 'partial'` (`$V18E/account/models/account_move.py:52,543-546`), derived from the residual (`:1189,1214-1216`).
**(ii) Account:** the shortfall is not moved; it stays as the residual on AR/AP.
**(iii) Visibility:** good — AR/AP, so in the ageing report.
**(iv) Clearing:** further payment, or write-off.

**EC-F-04 — A tolerated shortfall CAN silently close an invoice, and the shipped defaults are safe.**
Both halves matter, and both are stated.
The mechanism: `$V18E/account_accountant/models/account_reconcile_model.py:548-560` — `payment_tolerance_param == 0` returns `{'rejected'}`; a shortfall within a fixed or percentage gap returns `{'allow_write_off', 'allow_auto_reconcile'}`.
The shipped defaults: `$V18E/account/models/chart_template.py:1116-1135` — `reconcile_perfect_match` has `auto_reconcile: True` **with gap 0**; `reconcile_partial_underpaid` has `auto_reconcile: False` and `allow_payment_tolerance: False`. **Out of the box a shortfall is rejected.**
**The exposure is a configuration change with no approval gate.** The three tolerance fields carry `tracking=True` and nothing else (`$V18E/account/models/account_reconcile_model.py:286,293,301`). **NOT FOUND: any approval, limit or group restriction** — see EC-F-08 for the exact search scopes.
**DENOMINATOR:** PATTERN `payment_tolerance` over `$V18E`, py+xml. Consumers outside `addons/account/`: **4 lines, all in `account_accountant/models/account_reconcile_model.py` (520, 548, 553, 558).**
**And note the inversion (RM-F-17):** switching `allow_payment_tolerance` **off** does not tighten the control — `:520-521` returns `{'allow_write_off','allow_auto_reconcile'}` unconditionally. The safe setting is *on* with a gap of zero. A field named "Payment Tolerance" behaves opposite to how its label reads. `P06-B-32`.

---

## E4 — Advance and deposit

**EC-F-05 — An advance is an INVOICE in three of four implementations, and an `account.payment` in none of them.**

| Path | Object | Account | Evidence |
|---|---|---|---|
| Customer advance | customer invoice, `is_downpayment=True` | product `downpayment` account, **falling back to plain income** | `$V18E/sale/wizard/sale_make_invoice_advance.py:229,252-253` |
| Vendor down payment (reference) | PO line + bill wizard | product accounts | `$V18E/purchase/models/purchase_order.py:625`, `wizard/bill_to_po_wizard.py:43,56,65-66` |
| Vendor advance (custom) | vendor bill | **the product's EXPENSE account** | `$CUST18/scgl_purchase_advance_payment/wizard/purchase_advance.py:21-22,93` |
| Employee advance (custom) | **a first-class model** | request-line account, defaulted from the product expense account | `$CUST18/scgl_advance_expense_request/models/advance_expense_request.py:15-16` |

**EC-F-06 — Only the employee-advance custom module gives an advance a first-class model with an approval state machine.**
`$CUST18/scgl_advance_expense_request/models/advance_expense_request.py:6-12` — states `draft, to_approve, approved, rejected, done`; exposure fields `amount_residual`, `amount_toclear`, `is_clear` (`:114-116`); clearing via two wizards (`wizard/advance_request_reconcile.py:35-40,62-86`).
**This is the best-designed object in the entire P06 evidence set**, and it is a custom module, not a platform capability. Worth carrying forward as a pattern.

**EC-F-07 — The custom vendor-advance path defaults to the product's expense account with no prepayment-asset fallback.**
Restated from EGL-F-10 with its qualification intact: the sale-side path prefers a dedicated `downpayment` account; the custom purchase-side path resolves to `_get_product_accounts()['expense']` and writes it onto the product template. **Whether the configured product points at a balance-sheet prepayment account or a profit-and-loss expense account is a data question this session cannot answer** (NC-01). The product is chosen by a system parameter (`models/res_config_settings.py`, `config_parameter='purchase.advance_default_product_id'`).
**Classification: PLAUSIBLE DEFECT, DATA-DEPENDENT. HOLD / EVIDENCE REQUIRED**, routed to Accounting-Tax. `P06-B-21`.

**Note on parity:** a `purchase.advance.payment.inv` wizard equivalent to the sale side is **NOT FOUND** — `$V18E/purchase/wizard/` contains only `__init__.py`, `bill_to_po_wizard.py` and its view. That absence is why the custom module exists.

---

## E5 — Write-off

**(i)/(ii)** Five to six entry points; account chosen freely with **no account-type restriction** (`$V18E/account/wizard/account_payment_register.py:143` — domain is only `[('deprecated','=',False)]`). Full table in the FX/Fee/Interest Matrix, Part D.
**(iii)** A posted move; the reconcile wizard offers only a soft `to_check` flag (`$V18E/account_accountant/wizard/account_reconcile_wizard.py:117-119`, consumed as `'checked': not self.to_check` at `:602`).

**EC-F-08 — There is no approval and no amount limit on a write-off. Three independent search scopes, all zero.**
1. PATTERN `writeoff.*(limit|approv)|(limit|approv).*writeoff`, case-insensitive, over `$V18E/account` + `$V18E/account_accountant`, py+xml: **0 hits.**
2. PATTERN `groups=|check_access|has_group|limit` over `$V18E/account_accountant/wizard/account_reconcile_wizard.py`: **2 hits, both unrelated** (a `search(..., limit=1)` at `:188`, a comment at `:462`).
3. PATTERN `writeoff` over `$V18E/account/wizard/account_payment_register_views.xml`: **10 hits, none carrying a `groups=` attribute.**
**RE-CLASSIFIED Class A → Class B by AAS2-C-04.** All three scopes are inside `$V18E`. The custom estate contains `multi_level_approval`, `multi_level_approval_configuration` and `multi_level_approval_hr` (`$CUST18`), **none of which was searched for write-off or reconciliation coverage.** The correct statement is therefore *not found in the reference modules searched* — not *absent from the system*. New open item `P06-OQ-81`. `P06-B-22` is retained at Class B pending that search.

---

## E6 — Internal transfer between two own bank accounts

**(i) Concept: substantially degraded in this build.** The transit account is first-class (`$V18E/account/models/company.py:110-112`, domain-forced to `reconcile=True` and `asset_current`); the **payment-pairing machinery is orphaned**.
- `paired_internal_transfer_payment_id` — **2 occurrences in the whole tree**: the field declaration (`$V18E/account/models/account_payment.py:70-73`) and an invisible view field (`$V18E/account/views/account_payment_view.xml:186`). **Never written.** Its help text describes behaviour with no producer.
- `is_internal_transfer` as a field — **NOT FOUND**; the sole occurrence is a dangling context default (`$V18E/account/models/account_journal_dashboard.py:1052`), on an action whose domain is empty (`account_payment_view.xml:383-388`).
- `destination_journal_id` — **0 occurrences.**
**Class A within the declared tree-wide scope.**

**(ii) The double entry that actually works:** a `writeoff_button` reconcile model applied to **both** statement lines — `$V18E/account/models/chart_template.py:1149-1158`, wired to the transit account at install (`:724-727`). Bank A: Dr Transit / Cr Bank A. Bank B: Dr Bank B / Cr Transit.

**EC-F-09 — Nothing links the two legs, and nothing ages the transit balance.**
There is no shared transaction id, no pairing record, and no constraint. **A single-sided transfer is prevented by nothing except a non-zero balance left on the transit account** — and that account is `asset_current`, therefore in the same reporting blind spot as the suspense account (EC-F-01).
**Consequence:** the one control over money in transit between a business's own bank accounts is a balance that no standard report ages. `P06-B-16`, `P06-B-18`.

---

## E7 — Intercompany payment

**EC-F-10 — `account_inter_company_rules` handles invoices and credit notes only. Payments: NOT FOUND.**
**DENOMINATOR:** POPULATION: all files under `$V18E/account_inter_company_rules` — the module contains **5 non-test `.py` files**. PATTERN `-i payment` over py+xml excluding tests: **2 hits, both incidental invoice fields** (`models/account_move.py:95,99`). PATTERN `account\.payment|account_payment` over the whole module: hits **only** in `/i18n/*.po` — stale catalogue entries (`field_account_payment__auto_generated`) with no corresponding Python.
The manifest states the scope itself (`__manifest__.py:9`): *"Supported documents are invoices/credit notes."*
**Class A within that module's declared scope.**
**Scope reading (CORR1):** an intercompany settlement is **two COMPANY-owned financial effects inside one TENANT**, requiring a tenant-scoped carrier that owns neither but proves both. No such object exists. `P06-B-20`, SCOPE-F-10.

---

## E8 — Cash, not bank

**(i) Concept:** cash is a **journal type**, reusing the bank-statement machinery verbatim. `$V18E/account/models/account_journal.py:93-99`; cash is grouped with bank throughout (`:238,328,389,401,422,580,673,791,824`). Notably `:422` — **cash journals do use suspense and do use statement lines.** The dashboard routes cash to the statement view (`$V18E/account/models/account_journal_dashboard.py:994-995`).
**(ii) Cash difference accounts are first-class:** `$V18E/account/models/company.py:117-118`, auto-assigned at journal creation (`$V18E/account/models/account_journal.py:835-838`), and the field help still names the till (`:182-184`).

**EC-F-11 — There is no cash register, session, custodian or blind-count model outside point-of-sale.**
PATTERN `-i "cash_control|cashbox"` over `$V18E/account*` (**39 modules**): **0 hits.** Whole-tree scope: matches confined to the point-of-sale family and to cash-drawer **hardware** drivers.
**Class A within that declared scope.**
**Consequence:** without point-of-sale, a cash till has a declared-versus-computed balance and profit/loss accounts, but **no session, no named custodian, no blind count, no two-person close.** For a Thai SME running petty cash this is a material internal-control gap. `P06-B-33`.
Whether point-of-sale is in P06 scope is an **open question** — `P06-OQ-61`.

---

## E9 — Cheque

**(i) States:** there is **no cheque state machine.** A cheque is a payment plus one boolean — "printed" is `is_sent` (`$V18E/account_check_printing/models/account_payment.py:207`), and printing is gated on it (`:155`).
**(ii) Account:** unchanged from any payment. `$V18E/account_check_printing/models/account_journal.py` adds exactly **4 fields** — `check_manual_sequencing`, `check_sequence_id`, `check_next_number`, `bank_check_printing_layout` — **none of them an account.** There is no "cheques issued, not presented" account.
**(iii) Number:** stored on the payment (`$V18E/account_check_printing/models/account_payment.py:21-26`), assigned from the journal sequence at post time (`:145-150`).
**(iv) Void:** exists, and is destructive-by-reset — `:195-197`, `action_void_check` is `action_draft()` then `action_cancel()`.

**EC-F-12 — A voided cheque number returns to the pool.**
Uniqueness spans **posted moves only** (`$V18E/account_check_printing/models/account_payment.py:74-77` — `AND move.state = 'posted' AND other_move.state = 'posted'`). There is no `voided` state and no stop-list. A cancelled or drafted cheque number leaves the constraint's scope and can be silently re-issued.
Whether the deployed database contains re-used numbers is a **data question** (`P06-OQ-62`). `P06-B-19`.

**EC-F-13 — Post-dated cheques do not exist in the reference v18 line, and the v14 custom implementation was not migrated.**
PATTERN `-i "post.dated|\bpdc\b"` over the entire `$V18E`, py+xml, excluding `/i18n/`: **0 hits. Class A within that scope.**
The v14 tree carries a full implementation — `$CUST14/post_dated_cheque_mgt_app`, **16 `.py` files**, including a delegated payment model (`models/account_pdc_payment.py:5-7`, `_inherits = {'account.move': 'move_id'}`), its own state vocabulary (`draft, cancelled, returned, bounced, deposited, collect_cash`), and **6 state-transition wizards**. Plus `$CUST14/pdc_generate_cheque_reference` and `$CUST14/cheque_control`.
**None has a v18 counterpart.** DENOMINATOR: PATH SET the three v18 custom roots (65 + 57 + 47 = 169 module directories). PATTERN A: directory names matching cheque/check/pdc/payment_return/bank_statement/petty_cash. PATTERN B, to catch renamed ports: `grep -rln --include="*.py" "cheque\.code\|cheque\.generate\|pdc\.code\|account\.pdc\.payment\|payment\.return\|account\.bank\.statement\.import"` → **zero files in all three roots.**
**Class A within that declared scope.**
**Consequence:** post-dated cheques are ordinary Thai commercial practice. In v18 they can only be modelled as a payment with a future date — no distinct account, no maturity, no ageing, no bounce path.
**Baseline declared (narrowed by AAS4-C-02):** this is the **largest functional capability present in the v14 custom set and absent from all three v18 custom sets**. It is *not* a claim that the v14 modules were installed, used, or hold data — that is `P06-OQ-82`, answerable only from the v14 database. The capability question stands regardless of past usage, because the commercial practice is current. `P06-B-34`.

**EC-F-14 — The returned/bounced-item capability was also not migrated.**
`$CUST14/account_payment_return` (v14, `14.0.1.0.4`, marked "Mature") implements exactly the capability the reference lacks — it breaks and re-makes reconciliations (`models/payment_return.py:246-249,214,277-278`) with a `draft/confirm/cancel` state machine. **No v18 counterpart found** under the same declared scope. This is missing event `E-BANK-06` from the Bank Event Register. `P06-B-35`.

---

## E10 — Batch payment, partial rejection

**(i) Concept:** a dedicated unwind wizard exists — `$V18E/account_accountant_batch_payment/models/account_batch_payment_rejection.py:5-7`. It selects the un-matched members not part of the statement line being reconciled (`:28-32`) and unwinds them lock-date-aware (`:48-57`): pre-lock-date moves are drafted and cancelled; post-lock-date moves are `_reverse_moves(cancel=True)`. The alternative is `button_continue` — *"Expect Payments Later"*.

**EC-F-15 — The wizard has no Python producer in this snapshot.**
**DENOMINATOR:** POPULATION: all files under `$V18E` excluding `/i18n/`. PATTERN `open_batch_rejection_wizard`. UNIT: hit line. **RESULT = 2, both JavaScript** (`static/src/components/bank_reconciliation/kanban.js:85,88`). The Python that would return `{'open_batch_rejection_wizard': <action>}` is **NOT FOUND**. Secondary scope `_action_validate_method|_js_action_validate|rejection` over that module's `.py` excluding tests: **4 hits, none producing the action.** The module's own `_action_validate` override returns nothing (`models/bank_rec_widget.py:270-276`), and the base sets `return_todo_command = {'done': True}` unconditionally (`$V18E/account_accountant/models/bank_rec_widget.py:1478`).
The module's own regression test bypasses the wizard and drives the state directly (`tests/test_bank_rec_widget.py:381-384`).
**Two readings are possible and this session does not choose between them:** either this evidence copy is an incomplete checkout of the enterprise addon, or the wizard is genuinely unreachable from the widget in this build. **Resolve by diffing the module against a known-good 18.0 enterprise distribution before relying on it as a control.** `P06-OQ-63`, Class D.
**In the meantime, the only verified partial-rejection route is a manual per-payment `action_reject()` / `action_cancel()`**, from a button visible only when `state == 'in_process' and is_sent` (`$V18E/account/views/account_payment_view.xml:146-147`).

**EC-F-16 — And the batch state ignores the rejected members.** Restated from SSM-F-04: the quorum filters out `canceled` and `rejected` (`$V18E/account_batch_payment/models/account_batch_payment.py:120-123`), so a batch with one bank-rejected payment still computes to `reconciled`.

---

## Summary — first-class versus emergent

| Case | First-class concept | Account | Ageable | Verdict |
|---|---|---|---|---|
| E1 Unidentified receipt | account only | suspense | **no** | needs a clock |
| E2 Overpayment | **none** | AR/AP or suspense | partly | needs an object |
| E3 Underpayment | yes (`partial`) | AR/AP | yes | tolerance control inverted |
| E4 Advance | invoice ×3, model ×1 | varies; one is P&L | yes | needs one shape |
| E5 Write-off | mechanism only | unconstrained | wherever posted | needs approval + limit |
| E6 Internal transfer | **orphaned** | transit | **no** | needs pairing |
| E7 Intercompany | **none** | — | — | needs a tenant carrier |
| E8 Cash | journal type only | cash + diff accounts | statement only | needs a session |
| E9 Cheque | number only | none dedicated | no | needs a state machine; PDC absent |
| E10 Batch rejection | wizard, **unreachable** | — | — | needs a verified route |

**10 cases. 2 adequately modelled (E3, and E4 only in the custom employee-advance module). 3 with no concept at all (E2, E7, and cheque state in E9).**

## Open items

| ID | Item | Class |
|---|---|---|
| P06-OQ-60 | Whether a custom SMEsPlus report ages the suspense balance — not searched. | C |
| P06-OQ-61 | Whether point-of-sale is in P06 scope (bears on E8). | D |
| P06-OQ-62 | Whether the deployed database contains re-used voided cheque numbers. | D |
| P06-OQ-63 | Whether `account_accountant_batch_payment` is an incomplete checkout or the wizard is genuinely unreachable. | D |

---

# End
