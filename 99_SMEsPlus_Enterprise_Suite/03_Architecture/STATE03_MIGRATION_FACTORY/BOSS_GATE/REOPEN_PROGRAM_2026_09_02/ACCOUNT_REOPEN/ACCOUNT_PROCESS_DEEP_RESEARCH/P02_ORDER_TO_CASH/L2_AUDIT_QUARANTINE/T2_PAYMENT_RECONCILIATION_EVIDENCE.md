# T2 EVIDENCE EXTRACT — RECEIPT / SETTLEMENT / RECONCILIATION / DEPOSITS / FX / BAD DEBT

`LAYER 2 — AUDIT QUARANTINE` · Parallel research track T2 · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`
Reference root: `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons` (`<ROOT>`)

## §0 DENOMINATOR

**POPULATION** — measured, not author-chosen: `find <ROOT> -name '*.py'` = **9,431 files** across **791 addon
directories**.

**PATTERN** — symbol-level greps over the whole population, per question:
P1 `payment_state`, `PAYMENT_STATE_SELECTION`, `_get_invoice_in_payment_state` ·
P2 `_prepare_reconciliation_*`, `_compute_amount_residual`, `amount_residual(_currency)?` ·
P3 `_create_exchange_difference_move(s)?`, `_prepare_exchange_difference_move_vals`,
`_get_exchange_(journal|account)`, `_get_conversion_rate`, `_convert`, `_get_rates` ·
P4 `downpayment`, `is_downpayment`, `property_account_downpayment_categ_id`, `_prepare_down_payment_*` ·
P5 `outstanding_account_id`, `payment_account_id`, `is_matched` ·
P6 `write_off|writeoff` (-i), `bad.?debt|doubtful|allowance for` (-i) ·
P7 `remove_move_reconcile`, `action_draft`, `action_cancel`, `button_draft`, `_check_fiscal_lock_dates`,
`_check_draftable`, `_check_reconciliation`.

**PATH SET** — the population above; files returning hits were read in the relevant blocks.

**UNIT** — one *material statement* (one behavioural assertion, one tag, and for `FACT VERIFIED` at least
one `path:line`). §8 uses **one selection value** as the unit, with the field's own selection literal as the
denominator.

**DECLARED EXCLUSIONS** — `/i18n/*.po`; `/tests/` (consulted for corroboration only, never as the basis of a
`FACT VERIFIED`); front-end assets. **Material caveat:** this tree contains only **2** localisation modules
(`l10n_th`, `l10n_th_reports`), which bounds every claim about chart-of-accounts defaults.

## §1 Payment and reconciliation are separate events

- Registering a payment executes three separable steps in order — create, post, then match —
  `account/wizard/account_payment_register.py:1256-1258`. — `FACT VERIFIED`
- What the payment posts: a two-line entry. The liquidity line hits the **outstanding** account
  (`account/models/account_payment.py:352`); the counterpart hits the partner's receivable control account
  (`:364`). **It does not touch the bank account at this moment.** — `FACT VERIFIED`
- The outstanding account comes from the **payment method line**, not the journal —
  `account/models/account_payment.py:589`. Seeded defaults are two reconcilable current-asset accounts —
  `account/models/chart_template.py:844-857`. — `FACT VERIFIED`
- The receivable line becomes reconciled at a **later, separate** moment, when matching is invoked per
  account — `account/wizard/account_payment_register.py:1184-1192`; matching itself delegates to the
  reconciliation plan — `account/models/account_move_line.py:3074-3076`. — `FACT VERIFIED`
- **MATERIAL, AND CONTRARY TO THE COMMON MENTAL MODEL:** in this version a payment may post **no journal
  entry at all**. Entry generation is filtered to payments that have an outstanding account —
  `account/models/account_payment.py:1002` — and an outstanding account is force-assigned **only when the
  full-accounting module is absent** (`:874-878`, gate at `:873`; chart seeding gate at
  `account/models/chart_template.py:842`). The "outstanding receipts then bank" narrative therefore describes
  the **invoicing-only** configuration. — `FACT VERIFIED`
- Settlement state is a stored, tracked computed selection — `account/models/account_move.py:543-549`,
  compute at `:1133`, dependencies at `:1132`. — `FACT VERIFIED`
- Those dependencies make settlement state a **consequence of reconciliation**, not of payment creation.
  A payment that exists but is unmatched moves it only through the matched-payment leg. — `SUPPORTED INTERPRETATION`

## §2 Partial settlement — valuation and residual

- The three relevant methods are `_prepare_reconciliation_single_partial`
  (`account/models/account_move_line.py:1908`), `_prepare_reconciliation_amls` (`:2213`) and
  `_prepare_reconciliation_plan` (`:2280`). — `FACT VERIFIED`
- A partial allocation carries **three** amounts, not one: company-currency amount plus a debit-side and a
  credit-side foreign-currency amount — `account/models/account_partial_reconcile.py:42-50`, emitted at
  `account/models/account_move_line.py:2194-2200`. — `FACT VERIFIED`
- Valuation rule: the reconciliation currency prefers a non-company currency common to both sides, else
  company currency (`:1955-1966`); the allocated quantum is the **smaller** of the two residuals in that
  currency (`:1994`). — `FACT VERIFIED`
- Both residual fields are **stored computes** — `:244-256`; arithmetic at `:776-777`. — `FACT VERIFIED`
- **A line counts as reconciled only when BOTH residuals are zero** — `:778-780`. A line can be zero in
  company currency and non-zero in foreign currency and is then not reconciled — precisely the state the FX
  difference entry exists to clear. — `FACT VERIFIED`
- Residuals are computed only for lines on reconcilable accounts plus cash/credit-card (`:719`); all others
  are hard-set to zero (`:757-760`). **Residual is not a general property of a journal item.** — `FACT VERIFIED`
- What remains after a partial is therefore **a pair of residuals that can diverge under multi-currency**.
  Any ageing, dunning or receivable-balance logic reading only one will disagree with the reconciled flag in
  exactly the multi-currency cases. — `SUPPORTED INTERPRETATION`

## §3 FX on settlement

- Realised FX is recognised **at reconciliation time**, not payment time —
  `account/models/account_move_line.py:2115`, emitted at `:2178-2185`. — `FACT VERIFIED`
- Journal: the company's currency-exchange journal — `:2718-2719`. — `FACT VERIFIED`
- Account, hence gain vs loss: sign-driven — `:2721-2724`. — `FACT VERIFIED`
- **Date: not the settlement date as entered.** It is the exchange journal's lock-adjusted accounting date,
  then raised to the latest involved line date — `:2745`, `:2758`; the date passed in is the later of the two
  line dates (`:2180-2184`); the journal's accounting date routes through the same forward-shifting helper
  (`account/models/account_journal.py:433-438`, `account/models/account_move.py:5655`, `:5673-5674`). — `FACT VERIFIED`
- The exchange entry is created, hard-posted, then immediately matched back under a recursion guard —
  `:2853-2865`. Missing exchange journal or gain/loss account raises rather than degrading silently
  (`:2826-2851`). — `FACT VERIFIED`

### The missing-rate fallback — headline finding of this track

- **There IS a silent fallback, and it is a two-stage degradation, both silent.**
  `base/models/res_currency.py:121-141`, exact branch at `:140`:
  `COALESCE((latest rate <= date), (earliest rate of ANY date), 1.0)`.
  - the second arm (`:133-136`) has **no date filter at all** and is ordered ascending;
  - the third arm is the literal `1.0`.
  Neither path logs, warns or raises. — `FACT VERIFIED`
- A second independent `or 1.0` sits one layer up — `base/models/res_currency.py:157`. — `FACT VERIFIED`
- Zero-amount and same-currency short circuits (`:266-289`) are legitimate, not the fallback. — `FACT VERIFIED`
- **Which date the rate lookup uses is asymmetric.** For an invoice line it uses the **document date**, not
  the settlement date — `account/models/account_move_line.py:1851-1855`. For a payment or statement line the
  rate is not looked up at all; it is back-derived from what was booked (`:1857-1861`). — `FACT VERIFIED`
- The payment register can override the rate outright via context, taking precedence over every other branch
  — `:1847-1848`, injected at `account/wizard/account_payment_register.py:1177`. — `FACT VERIFIED`
- The realised FX amount is therefore the difference between the rate implicit in the invoice booking and the
  rate implicit in the payment booking. The rate table is consulted at exactly one point in this path, and
  that point is exposed to the fallback above. — `SUPPORTED INTERPRETATION`
- Whether any deployment-level guard prevents a company operating with an empty rate table is not
  determinable from source. — `UNRESOLVED — EVIDENCE REQUIRED`

## §4 Customer deposit / advance receipt / down payment

- A down payment produces a **real posted customer invoice** —
  `sale/wizard/sale_make_invoice_advance.py:170-172`. — `FACT VERIFIED`
- **The decisive line** — `sale/wizard/sale_make_invoice_advance.py:253`:
  `account = product_account.get('downpayment') or product_account.get('income')`. — `FACT VERIFIED`
- The down-payment key resolves to a product-category property (`sale/models/product_template.py:248`); the
  income key resolves to the product's or category's income account
  (`account/models/product.py:63-66`). — `FACT VERIFIED`
- **Therefore liability vs revenue is a configuration outcome, not a design guarantee. If the down-payment
  property is unset, the down payment lands in the income account — immediate revenue.** — `FACT VERIFIED`
- The property is company-dependent and its domain **permits but does not require** a liability account; it
  excludes receivable, payable, cash, credit-card and off-balance types, **leaving income accounts fully
  legal** — `sale/models/product_category.py:7-17`. — `FACT VERIFIED`
- It is configured on the **product category**, per company (`sale/views/product_views.xml:143`), and a
  post-install hook seeds it from a chart-template key (`sale/__init__.py:22-35`, key registered at
  `sale/models/chart_template.py:9`). — `FACT VERIFIED`
- **Negative, scoped (N-1):** no chart template in this tree supplies that key. Full enumeration returns 48
  files, of which 44 are translation catalogues and 4 are the sales module's own definition and consumption
  sites; the generic chart template does not contain it. **Consequence in this tree as shipped: the hook
  finds nothing, the property stays empty, and the fallback at `:253` reaches the income account.** — `FACT VERIFIED`
- The down-payment "section" is display-only (`sale/wizard/sale_make_invoice_advance.py:224-231`); the real
  down-payment order line carries zero ordered quantity (`:326-334`). — `FACT VERIFIED`
- **On the final invoice the down payment is reversed out as a negative line on the same account**, not
  cleared by a separate liability-release entry: billable quantity becomes −1
  (`sale/models/sale_order_line.py:967`); negative lines are picked up only with the final-invoice option
  (`sale/models/sale_order.py:1493`), which is a user-facing checkbox defaulting on
  (`sale/wizard/sale_make_invoice_advance.py:31`, passed at `:154`); and the final line reuses **the same
  account as the down-payment line** (`sale/models/sale_order_line.py:1411-1413`). — `FACT VERIFIED`
- Net effect where the account is left at income: revenue is recognised on the down-payment invoice and
  un-recognised on the final invoice. Where a liability account is configured, a liability is raised then
  released. Both reach the same final balance; **they differ entirely in the interim period's reported
  revenue.** — `SUPPORTED INTERPRETATION`
- **`CONTRADICTED`** — the reading that the down-payment state helper reports whether a deposit has been
  *received*. It returns only draft / cancel / empty and reads the parent document's status only
  (`sale/models/sale_order_line.py:860-872`, `:866-872`); a posted-and-unpaid and a posted-and-paid down
  payment both return empty. Its only use is deciding what prints on the order
  (`sale/models/sale_order.py:1838-1854`).

## §5 Overpayment and underpayment

- The difference is a single signed figure covering both directions —
  `account/wizard/account_payment_register.py:812-823`. — `FACT VERIFIED`
- Handling is a two-value selection, keep-open or mark-fully-paid — `:135-141`; default keep-open unless
  early-payment-discount mode applies (`:839-845`). — `FACT VERIFIED`
- Under keep-open **no write-off line is generated** — the entire construction sits inside the
  mark-fully-paid branch (`:986`). The payment posts its full amount to the receivable control account and
  matching consumes only the smaller residual, **so the excess remains as an open residual credit on the
  payment's own receivable line.** — `FACT VERIFIED`
- The excess therefore sits **inside the receivable control account** as unapplied cash. **There is no
  separate customer-advances or unapplied-receipts landing account in this path.** — `SUPPORTED INTERPRETATION`
- Resulting settlement state for an overpayment: the **invoice** reaches zero residual and reads as paid
  (`account/models/account_move.py:1188-1196`). **The overpaid excess is invisible to the invoice's settlement
  state entirely; it lives only on the payment.** — `FACT VERIFIED`
- Underpayment: non-zero residual with partials present → partial (`:1218-1219`). — `FACT VERIFIED`

### In-payment semantics

- In-payment is a **module-gated** state: the base hook returns paid
  (`account/models/account_move.py:6237-6241`); one override, in the full-accounting module, returns
  in-payment (`accountant/models/account_move.py:7-9`). Complete enumeration over 9,431 files: exactly one
  non-test override. — `FACT VERIFIED`
- The producing condition: residual zero, a payment or statement line involved, but **not every involved
  payment is matched** — `account/models/account_move.py:1190-1196`. It means the money has cleared the
  receivable subledger but has not been confirmed against the bank. — `FACT VERIFIED`
- The matched flag has four branches — `account/models/account_payment.py:428-456` (`:437`, `:440`, `:443`,
  `:446-449`, `:451`). — `FACT VERIFIED`
- The immediate-match branch (`:446-449`) is why in-payment never appears for payments booked straight to the
  bank account: such payments are declared matched at creation. **In-payment is specifically the
  outstanding-account configuration's intermediate state.** — `SUPPORTED INTERPRETATION`
- The configuration point is domain-restricted to current asset / current liability or the journal's own
  default account (`account/models/account_payment_method.py:110-117`), and setting it **silently flips the
  target account's reconcilable flag on** (`:166-186`). — `FACT VERIFIED`

## §6 Write-off and bad debt

- Complete field list on the payment register — `account/wizard/account_payment_register.py:131-152`. — `FACT VERIFIED`
- **Which account: whatever the user picks.** The only domain constraint is not-deprecated (`:140-146`). No
  account-type restriction, no default, no company-level configured write-off account. — `FACT VERIFIED`
- **Which date: the payment date**, not a separately controllable write-off date (`:1024`;
  `account/models/account_payment.py:366`, `:1010`). — `FACT VERIFIED`
- Special case: if the chosen account is one of the company's FX gain/loss accounts, the difference is
  reclassified as an exchange difference (`:825-836`, `:1002-1008`). — `FACT VERIFIED`
- The write-off UI is **suppressed entirely** when the payment method line has no outstanding account
  (`:310-318`) — i.e. hidden in the full-accounting configuration described in §1/§5. — `FACT VERIFIED`
- A **second, independent** write-off mechanism exists — the reconcile wizard
  (`account_accountant/wizard/account_reconcile_wizard.py:553-592`, posted at `:594-611`), journal restricted
  to general (`:85-94`), account domain excluding only deprecated and off-balance (`:95-99`). — `FACT VERIFIED`
- That second mechanism handles the lock date by **silently re-dating** rather than blocking (`:601`, helper
  `:492-496`), warning via a computed message (`:421-430`). — `FACT VERIFIED`
- **Bad debt — negative finding, scoped (N-2):** no dedicated bad-debt / doubtful-debt / allowance mechanism
  was found. Case-insensitive search for `bad.?debt|doubtful|allowance for` across all `*.py`, `*.xml`, `*.csv`
  in the 9,431-file population, excluding translation catalogues, returned **2 hits, both unrelated**: a
  payroll demo record and a partner **trust-rating** selection (`account/models/partner.py:570`) which is a
  credit-risk label with no accounting consequence. — `FACT VERIFIED`
- Bad debt is therefore expressed as a **generic write-off**: the user picks an expense account by hand on one
  of the two wizards. **No provision matrix, no ageing-triggered impairment, no allowance account, no
  reversal-of-provision on recovery.** Scope: no evidence found under the stated pattern in the stated
  population; **not** a claim that the capability cannot be configured by an accountant using the generic
  write-off, nor a claim about the 789 addons that did not surface under these patterns. — `SUPPORTED INTERPRETATION`

## §7 Reversing a payment / unreconciling

- Removing matching is one line: it unlinks the partials — `account/models/account_move_line.py:3078-3080`. — `FACT VERIFIED`
- Unlinking a partial then cascades — `account/models/account_partial_reconcile.py:100-136`: the parent full
  reconcile is unlinked (`:124`); cash-basis and exchange entries are **reversed, not deleted**
  (`:117-119`, `:127-132`), each reversal re-dated forward (`:129`); matching numbers recomputed (`:134`);
  affected payments reset to in-process (`:135`). — `FACT VERIFIED`
- The full reconcile independently reverses its own exchange entry (`account/models/account_full_reconcile.py:13-35`). — `FACT VERIFIED`
- Effect on the receivable ledger: residuals are stored computes depending on the matching relations
  (`account/models/account_move_line.py:714-716`), so removing partials restores the full balance. — `FACT VERIFIED`
- Effect on settlement state: it recomputes off the residual (`account/models/account_move.py:1132`) and drops
  back to partial or not-paid; deleting a payment forces the recompute explicitly
  (`account/models/account_payment.py:926`). — `FACT VERIFIED`
- Payment draft/cancel — `account/models/account_payment.py:1087-1089`, `:1078-1082`. Resetting an accounting
  document to draft removes matching on **all** its lines as a matter of course
  (`account/models/account_move.py:5283`), so resetting a payment unreconciles every invoice it touched. — `FACT VERIFIED`

### What a locked period does and does not block here

- **MATERIAL: the unreconcile path itself is not lock-date gated.** The fiscal-lock check has exactly three
  call sites in the reconciliation-relevant models — `account/models/account_move_line.py:1578`, `:1703`, and
  `account/models/account_move.py:3235`, `:3240`, `:3282`. **The partial-reconcile model returns zero hits.**
  Unlinking a partial is therefore not itself a lock violation; only the consequential reversal entries are
  re-dated forward (`account/models/account_partial_reconcile.py:129`). — `FACT VERIFIED`
- What does block: reset-to-draft refuses non-posted/non-cancelled documents and documents flagged as needing
  a cancellation request (`account/models/account_move.py:5275-5278`, hook `:1636-1641`); a further guard
  covers exchange-difference entries (`:5317-5337`). — `FACT VERIFIED`
- Independently, a reconciled line's account, date, balance, currency amount, currency and partner cannot be
  edited (`account/models/account_move_line.py:1292-1297`, invoked at `:1585-1600`, protected set at `:3370`),
  **with a write-time carve-out** permitting partner and account changes when the whole reconciliation set is
  in the same write (`:1595-1600`). — `FACT VERIFIED`
- The fiscal-lock check is **bypassable by context** — `account/models/account_move.py:2378-2379`. — `FACT VERIFIED`
- The design treats the lock date as a constraint on **journal entries**, not on **matching state**.
  Reconciliation and unreconciliation are modelled as subledger metadata that may be freely rewritten across a
  closed period, with only the derived FX and cash-basis entries pushed into an open one. — `SUPPORTED INTERPRETATION`

## §8 Settlement-state enumeration — complete

**DENOMINATOR** — POPULATION: the settlement-state selection literal,
`account/models/account_move.py:48-56` — **7 values**, author-independent because it is the field's own
definition. PATTERN: every assignment inside the compute (`:1133-1220`) **plus** every literal assignment
anywhere in the 9,431-file population, so values reachable only from outside the compute are not dropped.
UNIT: one selection value. External-writer sweep found exactly two sites in non-test accounting code
(`account/models/account_move.py:5379`, `:5384`) plus one raw-SQL migration writer
(`account_accountant/models/res_company.py:96-139`).

| # | Value | Exact condition | Citation |
|---|---|---|---|
| 1 | legacy-invoicing | **Never assigned by this compute** — the group is deliberately frozen. Set only externally, by raw SQL migration. | `:1134-1140`; `account_accountant/models/res_company.py:119` |
| 2 | blocked | **Never assigned by this compute** — grouped and left untouched. Set only by the user action, which refuses if already paid or in-payment. | `:1134-1140`; `:5382-5384` |
| 3 | not paid | (a) any document not in the legacy/blocked/posted-invoice groups is bulk-set; (b) a posted invoice retains the initialiser when residual is non-zero, no in-process unlinked payment matches, no partials exist, and no paid unlinked payment matches. | (a) `:1140`; (b) `:1187` falling through `:1212-1219` |
| 4 | paid | Two disjoint routes: (i) zero residual **and** a payment or statement counterpart exists **and** all payments matched; (ii) zero residual **and** no payment or statement counterpart — the reversal route, before the reversed test overrides it. | (i) `:1188-1194`; (ii) `:1197-1198` |
| 5 | in payment | Three disjoint routes, all via the module-gated hook: (i) zero residual, a payment/statement counterpart, **not** all matched; (ii) non-zero residual **and** a moveless payment in process; (iii) non-zero residual, no partials, **and** a moveless paid payment. | (i) `:1193-1196`; (ii) `:1213-1214`; (iii) `:1217-1218`; hook `:6237-6241` / `accountant/models/account_move.py:7-9` |
| 6 | partial | Non-zero residual, route (ii) of in-payment did not fire, and partials exist against receivable/payable lines. | `:1215-1216` |
| 7 | reversed | Zero residual, no payment/statement counterpart, and the counterpart document-type set matches one of exactly three shapes. Overwrites the paid set at `:1198`. | `:1200-1211` |

- **Gating precondition applying to rows 4–7:** reachable only for posted invoices (`:1136`); every other
  document is forced to not-paid at `:1140`. — `FACT VERIFIED`
- **Scope filter applying to rows 4–7:** the reconciliation set is filtered to receivable and payable account
  types (`:1185`). **Reconciliations on any other account type are invisible to settlement state.** — `FACT VERIFIED`
- **Currency selection:** the zero test uses the single currency of the relevant lines if unambiguous, else
  company currency (`:1180-1181`). On a mixed-currency invoice the residual is tested in company currency —
  a **different test** from the one the reconciled flag performs (§2). — `FACT VERIFIED`

**Enumeration complete against the declared denominator: 7 of 7, including the 2 this compute provably never
assigns.**

## §9 CONTRADICTIONS / SURPRISES

- **T2-S1 — the current-rate compute ignores its own resolved company.** The company is resolved from context
  (`base/models/res_currency.py:152`) but the rate fetch two lines later passes the environment company
  instead (`:155`), while the comparison uses the resolved one (`:159`). In a multi-company estate a
  conversion requested with a company in context may be priced using the **acting user's** company rate table.
  — `SUPPORTED INTERPRETATION`; whether any settlement-path caller reaches this with a divergent context
  company is `UNRESOLVED — EVIDENCE REQUIRED` and must not be reported as a defect without a runtime
  reproduction.
- **T2-S2 — the rate fallback is worse than 1:1 in the more common case.** The genuinely dangerous arm of
  `base/models/res_currency.py:140` is not the literal 1.0 but the **undated, ascending-ordered earliest-rate**
  arm (`:133-136`). A company that begins loading rates on 1 March will price every February settlement at the
  1 March rate, silently. A 1:1 result is at least conspicuous; this is not.
- **T2-S3 — a payment may post nothing** (`account/models/account_payment.py:1002`). Any design assuming a
  payment always has a journal entry is wrong under the full-accounting configuration.
- **T2-S4 — the write-off account is unconstrained** (`account/wizard/account_payment_register.py:143`).
  Nothing prevents writing an unrecoverable receivable off to a revenue account, a liability, or another
  receivable.
- **T2-S5 — two write-off mechanisms with different date behaviour.** The register forces the payment date;
  the reconcile wizard silently re-dates past the lock and only warns
  (`account_accountant/wizard/account_reconcile_wizard.py:601`, `:421-430`). Same accounting event, two
  different period-assignment rules.
- **T2-S6 — the accounting date is absent from the fiscal-lock protected field set**
  (`account/models/account_move_line.py:3369`); it appears in the reconciliation-protected set (`:3370`) only.
  Line-level date changes are gated by the reconciliation check, not the lock check, on this path.
  Whether move-level date changes are separately gated is `UNRESOLVED — EVIDENCE REQUIRED`.
- **T2-S7 — reconciliation state is not period-locked** (§7). The audit trail of *what was matched against
  what* in a closed period is mutable in a way the entries themselves are not.
- **T2-S8 — overpayment has no dedicated home** (§5). Excess cash sits as an unapplied credit inside the
  receivable control account, and the invoice reads as paid while the excess is still outstanding.
- **T2-S9 — down payment defaults to revenue in this tree** (§4 with N-1).

## §10 NEGATIVE CLAIMS (each with search scope)

- **T2-N1.** A chart template supplying the down-payment account key was **not found** in the whole root
  (all `*.py`, `*.xml`, `*.csv`) under that key's exact name; 48 files match, 44 being translation catalogues
  and 4 the sales module's own sites; the generic chart template does not contain it. **Material caveat:**
  this tree carries only 2 localisation modules, so the absence is consistent with the key being supplied by
  localisations not present here. `NOT FOUND IN SEARCHED SCOPE`
- **T2-N2.** A dedicated bad-debt / doubtful-debt / allowance mechanism was **not found** in the whole root
  (all `*.py`, `*.xml`, `*.csv`, excluding translation catalogues) under the case-insensitive pattern
  `bad.?debt|doubtful|allowance for`; 2 hits, both unrelated. Not a claim that impairment cannot be effected
  via the generic write-off; **the terms "provision", "impairment" and "credit loss" were not searched.**
  `NOT FOUND IN SEARCHED SCOPE`
- **T2-N3.** A method literally named `_prepare_reconciliation_partials` was **not found**; three related
  methods exist under different names. The capability is present. `VERIFIED ABSENCE` of the name only.
- **T2-N4.** A lock-date check invoked from the reconcile/unreconcile path was **not found** in the
  partial-reconcile model (zero hits for the lock-date patterns in that file). **Not** a claim that no lock
  enforcement exists anywhere: a hard-lock concept is referenced from
  `account/models/account_move.py:2382-2388`, and `account/models/account_lock_exception.py` **was not read** —
  that file is the most likely home of a control not examined here. `NOT FOUND IN SEARCHED SCOPE`
- **T2-N5.** A warning, log line or exception on a missing currency rate was **not found** in
  `base/models/res_currency.py` within the three rate methods, under the patterns `_logger`, `raise`,
  `warning`. The degradation at `:140` and `:157` is unannounced. Not a claim that no monitoring exists
  outside this file. `NOT FOUND IN SEARCHED SCOPE`
- **T2-N6.** An override of the in-payment-state hook other than the full-accounting module's was **not
  found** across all 9,431 files. All other hits are call sites. `VERIFIED ABSENCE` within the population.
- **T2-N7.** A test pinning the down-payment account type was **not found** in the sales module's test
  directory under the relevant patterns. The behaviour at
  `sale/wizard/sale_make_invoice_advance.py:253` is therefore **not pinned by a regression test in this tree**.
  Not a claim that down payments are untested generally. `NOT FOUND IN SEARCHED SCOPE`
