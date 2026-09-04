# L12B — FRESH INDEPENDENT ADVERSARIAL REVIEW B

**Session** `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001` · correction round on parent `…-CORE-001`
**Reviewer** Fresh Independent Adversarial Reviewer B — did not author the package, did not
participate in the earlier review round.
**Remit** Disprove the corrected canonical model on: **negative claims**, **close / reopen**,
**SaaS boundary**, **migration**, and **"balanced but wrong" entries**.
**Not my remit** FX rate forensics and date-forensic mechanics (Reviewer A). Where a finding of mine
touches those, I cite them only as context and do not re-adjudicate them.

**Governing rule applied throughout:** `NO EVIDENCE FOUND ≠ FUNCTION DOES NOT EXIST`.
No `B`, `C` or `D` classification has been promoted to `A`. Every negative below carries its search
boundary.

**Approval status:** nothing here is approved. Boss is sole Final Approver. Research only.

---

## PART 0 — Method and declared search boundary

`VERIFIED FACT` — the evidence for this review was read from the reference build at
`/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/` (read-only; nothing under
that path was modified). Search boundary actually covered by me, stated once and referenced by every
row below as **SB-R**:

| Scope token | Directories actually searched by me |
|---|---|
| `S-CORE` | `account/` (models, views, wizard) |
| `S-ACCT` | `account_accountant/` (models, wizard) |
| `S-REP` | `account_reports/` (models, wizard) |
| `S-BANK` | `account_bank_statement_import*/`, `account_online_synchronization/` |
| `S-EDI` | `account_edi/` (model field inventory only) |
| `S-STUDIO` | `web_studio/models/studio_approval.py` |
| `S-BASE` | `base/models/res_currency.py` |
| `S-TH` | `l10n_th/`, `l10n_th_reports/` (file inventory + `l10n_th/models/account_move.py`) |
| `S-ADDONS` | whole-`addons` `grep` for named tokens only (`unique_import_id`, `control account`, `closing entry`, `unaffected_earnings`) — **token search, not a read** |

**Not searched by me — declared, not inferred:** runtime behaviour, HTTP/RPC reachability, ORM
framework internals beyond `res_currency.py`, `mail/` internals, `base_import/`, POS, asset,
localization modules other than `l10n_th*`, and any database instance. Anything I could not read is
recorded as `UNKNOWN — EVIDENCE REQUIRED`, never as absence.

---

## PART 1 — NEGATIVE CLAIM AUDIT TABLE

Classification key: `A. VERIFIED ABSENCE` (proven absent within an explicitly stated scope) ·
`B. NOT FOUND IN SEARCHED SCOPE` · `C. NOT YET SEARCHED` · `D. UNKNOWN` · `E. CONTRADICTED`.

### 1.1 The ten targeted negatives

| # | Claim as written in the package | Scope actually searched by me | Class | Corrected wording at the scope that is supported | Citation |
|---|---|---|---|---|---|
| `N1` | "**No accounting-event identity and no provenance carrier exist anywhere in the domain**" — file 21 `GAP-B02`; restated file 09 "Provenance / lineage — no owner — does not exist" and file 06 §1 "it does not implement `F7` at all" | `S-CORE`, `S-BANK`, `S-EDI`, `S-ADDONS` token sweep | **E. CONTRADICTED** | *At `S-CORE`+`S-BANK`+`S-EDI`:* **no single, general, mandatory provenance carrier applies to every accounting event.** Several **route-specific** carriers do exist and one of them is storage-enforced: a bank-statement line carries an import identity under a **database UNIQUE constraint**; entries carry typed origin links for the payment, statement-line, cash-basis, recurrence and reversal routes; a free-text source reference exists on invoices. The absence is **general and mandatory-scope**, not total. | `account_bank_statement_import/models/account_bank_statement.py:15` (`unique_import_id`, `readonly=True, copy=False`) and `:18` (`'unique (unique_import_id)'`, message "A bank account transactions can be imported only once!"); `account/models/account_move.py:207` `origin_payment_id`, `:225` `statement_line_id`, `:245` `tax_cash_basis_origin_move_id`, `:280` `auto_post_origin_id`, `:630` `invoice_origin`; `account_online_synchronization/models/account_bank_statement.py:16` `online_transaction_identifier`; `account_edi/models/account_edi_document.py:22-24` move↔format↔attachment linkage |
| `N2` | "**No controls prevent duplicate or missing accounting events**"; file 06 §2 "the same business event posted twice produces two equally valid entries and **nothing detects it**"; `CONTRA-09`/`XM-01` framing | `S-CORE`, `S-BANK` | **E. CONTRADICTED** on *detection*; `A` only for *prevention of arbitrary entries* | *Detection:* **three duplicate controls exist and were read.** (a) A computed duplicate-reference field on the entry, backed by a partial index, warns in the form view and **suppresses auto-posting**; (b) an equivalent duplicate check on payment registration; (c) a duplicate-transaction detector on bank statement lines matching on **either** amount+date+account **or** the online transaction identifier, exposed through a dedicated wizard. *Prevention:* only the bank-import route has a **blocking** control (the UNIQUE constraint at `N1`). Corrected wording: **"Outside the bank-import route no duplicate control blocks; the controls that exist warn or suppress auto-posting, and their coverage is partial (see `BW-01`)."** | `account/models/account_move.py:691` (`duplicated_ref_ids`), `:752-760` (`account_move_duplicate_bills_idx` on `ref` where `move_type IN ('in_invoice','in_refund')`), `:1831-1900` (`_fetch_duplicate_reference`), `:5034-5037` (auto-post disabled, chatter note posted); `account/views/account_move_views.xml:795-797` (warning alert, not a block); `account/models/account_payment.py:748-753`; `account_online_synchronization/models/account_journal.py:221-294` |
| `N3` | "**No tenant concept exists; the outermost boundary is the company group**" — file 06 §6, file 16 §1 | `S-CORE`, `S-REP`, `S-BASE` | **B → sharpened; the second half is `E. CONTRADICTED`** | First half stands at `S-CORE`+`S-REP`+`S-BASE`: **no tenant entity was found**. Second half is **wrong in the unsafe direction**: the outermost boundary is **the database, not the company group.** Two structures I read sit *above* the group: (i) a currency rate row with a **null company applies to every company in the database** — the resolution filter is `company_id IN (False, root_id)`; (ii) **report definitions carry no company dimension at all** (`account.report` has a country, not a company), so a report structure edited by one tenant is the structure every tenant reports on. Corrected wording: **"No tenant concept exists. The company group is the outermost boundary for ledger data; it is *not* the outermost boundary for currency rates, report definitions, or system configuration, all of which are database-wide."** | `base/models/res_currency.py:128-136` (`('company_id', 'in', (False, company.root_id.id))`) and `:298-308` (`JOIN res_company c ON (r.company_id is null or r.company_id = c.id)`); `:365-366` (`company_id` nullable, default `root_id`); `account/models/account_report.py:25-46` (no `company_id`; contrast `account/models/account_report.py:898` where the *external value* record does carry `company_id`) |
| `N4` | "**There is no period object; close is only a date**" (file 12 §1, file 15 §1) | `S-CORE`, `S-ACCT`, `S-REP` | **CONFIRMED WITH CAVEAT — rescoped correctly for the fiscal year, still over-stated for the tax period** | The rescoping to the fiscal-year record is **correct and I confirm it**: the fiscal-year record has a name, two dates, a company and an overlap constraint — **no state field, no close action, no link to any entry, deletable**. But the claim generalises beyond its evidence: a **tax-period close artefact does exist** — a posted entry bound to a report, with derivable period boundaries, whose posting **sets the tax lock date automatically**. That is a close that is a *record*, not a date, for one period type. Corrected wording: **"No fiscal-period object exists; the fiscal-year record carries no state. A tax-period close artefact does exist (a period-bound posted entry that advances the tax lock), and it is the only close in the searched scope that leaves a record."** | `account_accountant/models/account_fiscal_year.py` (whole file — 4 fields, 1 constraint, no state, no move link); `account_reports/models/account_move.py:19` (`tax_closing_report_id`), `:132-133` (`self.company_id.sudo().tax_lock_date = self.date`), `:221-222` (`_get_tax_closing_period_boundaries`) |
| `N5` | "**No temporal validity / effective dating anywhere**" — file 06 §4, file 15 §3 ("there is no temporal validity anywhere") | `S-CORE`, `S-ACCT`, `S-REP` | **B. NOT FOUND IN SEARCHED SCOPE** (not `A`) | I found **no effective dating on accounts, journals, taxes, payment terms or fiscal positions** in `S-CORE`/`S-ACCT`. That is a genuine negative *at that scope*. It is **not** "anywhere": dated records that behave as effective-dated facts do exist adjacent to the ledger — currency rates (date-keyed, DB-unique per day/currency/company) and report external values (`date` required, with carryover origin fields). Corrected wording: **"No effective dating exists on any classification or configuration entity in `account`/`account_accountant`. Dated-fact records exist for measurement (rates) and for report carryover values. Whether effective dating exists in modules outside the searched scope is `NOT YET SEARCHED`."** | `base/models/res_currency.py:368-370` (`unique (name,currency_id,company_id)`); `account/models/account_report.py:883-910` (`date` required; `carryover_origin_*`) |
| `N6` | "**No matching/reconciliation history artefact exists**" (`GAP-E02`, high priority) and `CONTRA-10` "**no record that a match ever existed**" | `S-CORE` | **E. CONTRADICTED in part; `D. UNKNOWN` for the match record itself** | There is **no artefact of the reconciliation record's own deletion** — I confirm that. But the surrounding claim "no record that a match ever existed" is **not supported**: journal-item create / update / delete on an entry that has been posted before are written as **in-database chatter messages with field-level before/after tracking values**, and those messages are **undeletable when audit trail is enabled**. Critically, **`matching_number`, `amount_residual`, `full_reconcile_id` and `amount_currency` are NOT among the tracked fields**, so the *match itself* leaves no tracked trace while the *lines* do. Corrected wording: **"Reconciliation state changes are not tracked; journal-item changes on previously posted entries are tracked, in-database, and become undeletable when audit trail is enabled. The gap is specific to reconciliation fields, not general."** `GAP-E02` should be re-opened at that narrower scope. | `account/models/account_move_line.py:1527-1539`, `:1638-1643`, `:1710-1722` (`_message_log(... tracking_value_ids=...)` for created / updated / deleted items, gated on `move_id.posted_before`); tracked fields are only `account_id` (`:104`), label (`:111`), `balance` (`:127`), `tax_ids` (`:198`), `tax_tag_ids` (`:233`), `date_maturity` (`:350`); `account/models/account_partial_reconcile.py:100-136` (`unlink` — no message, no artefact) |
| `N7` | "**No explicit control-account concept exists**" — file 18 `P-04` | `S-CORE`, `S-REP`, `S-ACCT` (string search + field read) | **E. CONTRADICTED as a functional negative; `A` only as a terminology negative — and the package contradicts itself** | The string "control account" does not occur in `account/`, `account_reports/` or `account_accountant/` — that is a **verified absence of the term**. The **function** exists and is explicit: an account-level "Allow Reconciliation" flag (tracked), a receivable/payable account type that forces it, and a `non_trade` discriminator separating trade from non-trade control balances, with a partner-ledger report aggregating the same items by counterparty. This is precisely the case the new project rule targets. **Internal contradiction:** file 18 asserts this negative as settled while file 21 still lists `GAP-A01` ("whether an explicit control-account concept exists") as an **open unknown closable by further reading**. Both cannot stand. | `account/models/account_account.py:98` (`reconcile = fields.Boolean('Allow Reconciliation', tracking=True)`), `:137` (`non_trade`), `:697` (`_compute_reconcile`); `account_reports/models/account_partner_ledger.py`; package files `18_…:P-04` vs `21_…:GAP-A01` |
| `N8` | "**No posting mechanism for unrealised FX / revaluation was found**" | `S-ACCT`, `S-REP` | **E. CONTRADICTED** | A full unrealised-FX revaluation posting mechanism exists — it is in `account_reports`, **not** in `account_accountant`, which is where the package appears to have looked. A report offers an "Adjustment Entry" action; the wizard builds an adjustment entry against configured expense/income provision accounts on a configured revaluation journal, **posts it, then reverses it at a chosen reversal date and posts the reversal.** It also warns when a custom rate is in use and when the previous period's entry was never reversed. Corrected wording: **"An unrealised-FX revaluation posting mechanism exists in the reporting layer (provision-entry plus dated reversal). It was not located in the core ledger or the accountant module."** | `account_reports/models/account_multicurrency_revaluation_report.py:69` (button), `:117-131` (wizard action), `:73-75` (multi-company and custom-rate warnings); `account_reports/wizard/multicurrency_revaluation.py:26-27` (`date`, `reversal_date`), `:59-66` (unreversed-previous-entry warning), `:163-179` (`action_post()`, `_reverse_moves(...)`, reversal `action_post()`) |
| `N9` | "**Exactly two things are unconditionally immutable in the reference core ledger**" (a hashed entry; the hard lock's forward-only movement) — file 15 §2 | `S-CORE` | **E. CONTRADICTED — there is a third** | Enabling the audit trail on a company is **irreversible once any entry exists for that company**: the constraint refuses to clear the flag whenever a single entry is present. Once enabled, (i) an entry that has been posted before **cannot be deleted** (the delete is rejected, and the destructive path is re-routed to *cancel*), and (ii) its notification messages **cannot be deleted** — a model-level restriction keyed on the company flag. This is a third unconditional immutability with the same monotonic shape as the hard lock. Corrected wording: **"Three things are unconditionally immutable: a hashed entry; the hard lock date's forward-only movement; and, once enabled on a company that has any entry, the audit-trail protection over previously posted entries and their tracking messages."** The package's own aside — "the audit-trail flag being off" defeats entry existence — is true only *before* the flag is turned on; it cannot be turned back off. | `account/models/company.py:257` (`check_account_audit_trail`), `:317-322` (`_check_audit_trail_records` — "Can't disable audit trail when there are existing records."); `account/models/account_move.py:3350-3358` (`_unlink_account_audit_trail_except_once_post`), `:4805-4830` (`_can_be_unlinked`, `_is_protected_by_audit_trail`, `_unlink_or_reverse` routing to cancel); `account/models/mail_message.py:7-16` (per-model audit domains including `account.move`, `account.account`, `account.tax`, `res.partner`, `res.company`) |
| `N10` | "**No maker-checker / approval-before-posting step exists anywhere**"; file 14 §2 "**no maker-checker anywhere in the core ledger**" | `S-CORE`, `S-ACCT`, `S-STUDIO` | **`A` at core-ledger scope; `E. CONTRADICTED` at domain scope** | At `S-CORE`+`S-ACCT` I confirm: **no approval step gates posting.** But the verified build contains a **generic approval-rule engine that patches named public methods on any model at registry load**, refuses to patch `create`/`write`/`unlink` and private methods, supports an approval group, delegated approvers with expiry, and an exclusive-approver mode — and it **special-cases `account.move` by name** when wiring its automation. An approval rule on the posting method is therefore configurable without code. Two caveats that matter more than the counterexample: it is **skipped entirely in an elevated environment** (logged as "ALLOWED"), and it is a *configuration capability*, not a shipped accounting control. Corrected wording: **"No maker-checker is shipped or enabled by default in the core ledger. A general, configurable approval-rule engine exists in the build, explicitly aware of the journal-entry model, and it is skipped under privilege elevation."** | `web_studio/models/studio_approval.py:66` (`method`), `:81` (`approval_group_id`), `:106` (`exclusive_user`), `:122-127` (must target exactly one of method/action), `:197-218` (`create`/`write`/`unlink` and private methods refused), `:267-273` (`account.move` special case), `:378-393` (`_register_hook` / `_patch`), `:397-425` (elevated environment skips the check) |

### 1.2 Further material negatives audited on my own initiative

| # | Claim as written | Scope searched | Class | Corrected wording | Citation |
|---|---|---|---|---|---|
| `N11` | file 12 — "**Reopening** — soft locks move backward **freely, with no distinct authority and no artefact**" | `S-CORE`, `S-ACCT` | **CONFIRMED on authority; `E. CONTRADICTED` on artefact** | Backward movement of the four soft locks is **not blocked** — I confirm; only the hard lock is guarded. But "no artefact" is wrong twice over: (i) **all five lock-date fields are tracked**, so every move of a lock — forward or backward — writes an in-database before/after tracking record on the company; (ii) a **persistent lock-exception record** exists with company, user (or everyone), reason, expiry, which lock field, and target date, which **cannot be duplicated**, and which offers an action listing **the audit-trail messages of entries touched while the exception was live**. Corrected wording: **"Reopening requires no distinct authority and no justification, and no precondition is re-tested on the way back. It is not traceless: the lock movement is field-tracked on the company, and lock exceptions are first-class records with a linked audit view."** | `account/models/company.py:73-96` (five lock fields, all `tracking=True`), `:475-500` (`_validate_locks` — hard lock only: cannot be removed, cannot decrease); `account/models/account_lock_exception.py:13-97`, `:242-243` (duplication refused), `:258-266` (revoke), `:277-325` (`_get_audit_trail_during_exception_domain`, `action_show_audit_trail_during_exception`) |
| `N12` | file 12 — "Who closed, when, on what basis — **no artefact** — only a tracked field change on the company record" (`GAP-G01`) | `S-CORE`, `S-REP` | **CONFIRMED WITH CAVEAT** | Correct for the fiscal close. Wrong as a general statement once the tax close is included (see `N4`), and the parenthetical "only a tracked field change" understates what a tracked field change *is* in this build: with audit trail enabled the resulting message is **undeletable** (`N9`). Corrected wording: **"For the fiscal close there is no closing artefact beyond a tracked field change on the company; that tracked change is itself in-database and, with audit trail enabled, undeletable. The tax close does produce an artefact."** | as `N4`, `N9`, `N11` |
| `N13` | file 16 §2 — "Deletion evidence — the **application log** … leaves the tenant's data entirely"; `CONTRA-14`; `SB-04` | `S-CORE` | **CONFIRMED WITH CAVEAT — understated in one direction, overstated in another** | The pre-delete detail message is indeed assembled for the logger. But in the configuration where deletion of a previously posted entry is *permitted*, audit trail is **off** — because with it on the deletion is refused outright and the operation is re-routed to cancel. So the exposure is real but narrower than stated: **it applies only to companies that have never enabled audit trail.** Separately, item-level deletions *within* a surviving entry are logged **in-database** (`N6`), which `SB-04` does not acknowledge. | `account/models/account_move.py:3304-3320` (`_get_unlink_logger_message`), `:3350-3358`, `:4805-4830`; `account/models/account_move_line.py:1710-1722` |
| `N14` | file 12 — "Year-end closing entry **does not exist anywhere in the tree**"; `E01` "there is still **no year-end closing entry** anywhere in the tree" | `S-ADDONS` token sweep + `S-CORE`, `S-ACCT`, `S-REP` | **`A` at the stated function; wording not supported at the stated scope** | No **fiscal-year** closing entry exists in `account`, `account_accountant` or `account_reports`; year-result equity is derived at report time. That function is genuinely absent at that scope. The phrase "anywhere in the tree" is **not supported**: the tree does contain objects named and behaving as closing entries — the tax closing entry, and a session closing entry in the point-of-sale module. Corrected wording: **"No fiscal-year closing entry exists in the accounting modules searched. Closing entries of other kinds (tax period, point-of-sale session) do exist in the build; the negative is about the fiscal-year function, not about the term."** | `account_reports/models/account_move.py:19-133`; `point_of_sale/models/pos_session.py` (token match only — not read); `account_reports/models/account_general_ledger.py:203-223` (unaffected earnings derived at report time) |
| `N15` | file 15 §4 — "Item → the source document that caused it — **no general carrier**" | `S-CORE` | **A. VERIFIED ABSENCE at `S-CORE`, item level** | Confirmed at item level in `account/models/account_move_line.py`: no source-document reference field. The carriers found under `N1` are **entry-level and route-specific**, so the claim survives *as stated about items*. It should not be generalised upward to the entry, where `N1` applies. | `account/models/account_move.py:207-285`, `:630` vs. item-level field inventory |
| `N16` | file 06 §1 / file 09 — "it does not implement `F7` (Provenance) at all" | `S-CORE`, `S-BANK` | **E. CONTRADICTED (same evidence as `N1`)** | "At all" is not sustainable against a storage-enforced import identity plus five typed origin links. Rewrite as: **"`F7` is implemented partially and per-route, never as a general obligation of the accounting event."** | as `N1` |
| `N17` | `CONTRA-01b` — on a secured entry, changes to transaction-currency amount, currency, tax fields, analytic distribution and due date are "**neither blocked nor detected**" | `S-CORE` (detection channel only — the hash mechanics are Reviewer A's) | **CONFIRMED for three of five; `E. CONTRADICTED` for two** | The list conflates *hash detection* with *detection*. **Tax fields, tax tags and the due date are tracked fields**, so a change to them on a previously posted entry writes an in-database before/after record — undeletable with audit trail on. **Transaction-currency amount, currency and analytic distribution are not tracked**, so for those three the claim stands. Corrected wording: **"…neither blocked nor hash-detected. Of the five, tax fields and the due date are still field-tracked in the chatter; the transaction-currency amount, its currency, and the analytic distribution are neither blocked, hash-detected, nor tracked."** That narrower version is a **sharper** finding, not a weaker one. | `account/models/account_move_line.py:104,111,127,198,233,350` (the complete tracked set) vs. the untracked `amount_currency`, `currency_id`, `analytic_distribution`, `matching_number`, `full_reconcile_id`, `amount_residual` |

### 1.3 Counts — Part 1

| Class | Count |
|---|---|
| `A. VERIFIED ABSENCE` (at an explicitly stated scope) | 3 (`N7` terminology only, `N14` function only, `N15`) |
| `B. NOT FOUND IN SEARCHED SCOPE` | 2 (`N3` first half, `N5`) |
| `C. NOT YET SEARCHED` | 0 stated as such by me; every unsearched area is declared in Part 0 |
| `D. UNKNOWN` | 1 (`N6`, for the reconciliation record itself) |
| `E. CONTRADICTED` (in whole or in a material part) | **9** (`N1`, `N2`, `N3` second half, `N6` in part, `N7` functionally, `N8`, `N9`, `N10` at domain scope, `N11` in part, `N16`, `N17` in part) |
| `CONFIRMED WITH CAVEAT` | 4 (`N4`, `N12`, `N13`, `N14`) |

---

## PART 2 — BALANCED-BUT-WRONG REGISTER

An entry is **balanced but wrong** when it satisfies every control the reference model applies — the
debit/credit check, the item-level database constraints, the lock composition, the sign constraint,
the hash where present — while being economically or legally incorrect. FX cases are excluded here by
division of labour (Reviewer A).

| # | Case | How it arises | Which controls it satisfies | Detectable? | Evidence |
|---|---|---|---|---|---|
| `BW-01` | **Duplicate vendor bill across a year boundary** | The vendor-bill duplicate detector matches on the reference **and requires the two documents to fall in the same calendar year of the invoice date**. The same supplier reference entered once in December and again in January is therefore not a duplicate to the control. Both entries balance, both are numbered, both post. | debit/credit; all four item constraints; lock composition; duplicate detector (returns empty); auto-post is *not* suppressed because there is no duplicate to report | **No, at year end.** Detectable only by human review or by an out-of-model query. The partial index is on `ref` alone, so the data to detect it exists; the rule does not use it. | `account/models/account_move.py:1861-1875` (`date_part('year', move.invoice_date) = date_part('year', duplicate_move.invoice_date)`), `:752-760` (index on `ref`) |
| `BW-02` | **Duplicate manual journal entry** | The duplicate detector filters to sale and purchase documents only. A miscellaneous entry (`move_type = 'entry'`) — accruals, provisions, payroll, inter-company postings, migration corrections — is **outside the control entirely**. Posting the same accrual twice yields two balanced, numbered, hashable entries. | every control without exception; the detector never runs | **No.** No mechanism in the searched scope compares two miscellaneous entries. | `account/models/account_move.py:1837-1839` (`filtered(lambda m: m.is_sale_document() or m.is_purchase_document() and m.ref)`) |
| `BW-03` | **Duplicate customer invoice with a different reference** | For customer documents the rule matches on **amount total plus invoice date**, ignoring the reference. Two genuinely distinct same-day, same-amount invoices to the same customer are flagged as duplicates (false positive), while a true duplicate re-keyed on a different date is not (false negative). The control's precision and its recall both fail, in opposite directions, on the same rule. | all | Partially, and unreliably — a warning that trains users to dismiss it. | `account/models/account_move.py:1845-1854` |
| `BW-04` | **Same bank transaction ingested twice by two different routes** | The file-import route enforces a **database-unique** import identity. The bank-synchronisation route uses a **different** identity field and de-duplicates by search, not by constraint. A transaction that arrives once by synchronisation and once by statement file has two different keys and **no constraint spans them**. The result is two statement lines, two balanced entries, and a bank balance that is right only if both are later matched to the same obligation — which they cannot be. | debit/credit; item constraints; the UNIQUE constraint (each key is unique on its own); lock composition | **Partly, after the fact.** A duplicate-transaction wizard exists that matches on amount+date+account, but it is **user-invoked, per journal, from a chosen date**, and it lives in the synchronisation module. It is a clean-up tool, not a control. | `account_bank_statement_import/models/account_bank_statement.py:15-18` vs `account_online_synchronization/models/account_bank_statement.py:16`; `account_online_synchronization/models/account_journal.py:221-232` (wizard), `:267-294` (the two disjoint queries) |
| `BW-05` | **Right amount, wrong period — the reversal pair split across a year end** | A reversal is created with a **freely chosen date** and posted; when the reversal is generated as a cancellation the pair is reconciled together. If the reversal date falls in the next fiscal year, each year in isolation is misstated by the full amount while the two years together net to zero and every entry balances. The revaluation wizard does exactly this **by design** (provision entry at period end, reversal on the following day) — which is correct there, and is the same mechanism that is incorrect when the dates are chosen carelessly. | debit/credit; lock composition (each entry is placed in an open period, legitimately); reconciliation; hash | **Only by a report that pairs an entry with its reversal across the period boundary.** The reversal→original link exists, so the data is present; no control uses it as a period-attribution test. | `account_reports/wizard/multicurrency_revaluation.py:26-27`, `:163-179`; `account/models/account_partial_reconcile.py:118-133` (cash-basis reversals re-dated through `_get_accounting_date`) |
| `BW-06` | **Right account record, wrong presented code** | An account is a single record shared across companies with a **per-company code mapping**. A posting made in one company reads under one code; the same item, viewed from a sibling company or in a consolidated view, reads under a different code. Nothing in the item records which code was in force at posting time (`N5`). A trial balance re-run later, or from a different company context, can present the same posted item under a different account label without any change to the ledger. | every control — the item is untouched | **No.** There is no stored code-at-posting-time to compare against. | `account/models/account_account.py:106-190` (`company_ids` many-to-many, per-company code resolution via `code_mapping_ids` and root-company arithmetic); package `COR-18`, `EV-020` for the encoding ceiling |
| `BW-07` | **Migration opening position anchored to a mutable, unlinked date** | The opening entry is created **one day before** a plain, freely mutable company date field, and is an ordinary entry. Once posted, further programmatic opening updates are refused — but the *date field itself* is not frozen, is not derived from the entry, and is not re-validated. After the opening date is edited the company's stated accounting start and its posted opening entry disagree, with no artefact recording the divergence and no provenance on either (`MG-01`). Every downstream "opening + movements = closing" proof is then stated over a boundary that is not the one the ledger actually holds. | debit/credit; the posted-state guard on the opening entry; lock composition | **No.** No constraint ties the date field to the entry's date after creation. | `account/models/company.py:172-174` (`account_opening_move_id`, `account_opening_date` — plain `Date`, `required=True`, default 1 January), `:733` (`'date': self.account_opening_date - timedelta(days=1)`), `:782-788` (update refused only when the move is not draft), `:899-902` (`_existing_accounting`) |
| `BW-08` | **Right entry, wrong tenant's measurement** | A currency rate row created with **no company** is used as the rate for **every company in the database**. In a shared deployment, one tenant's rate maintenance silently re-measures another tenant's foreign-currency postings. The affected entries balance in company currency and satisfy the sign constraint. | every control; the rate is a legitimately configured rate — just not that tenant's | **No, from inside the tenant.** The tenant cannot see or attribute a rate row it does not own. | `base/models/res_currency.py:128-140`, `:298-308`, `:365-366` |
| `BW-09` | **Right numbers, wrong report** | Report definitions carry **no company dimension**. A tenant that edits a report line, expression or column edits the definition every tenant renders. The ledger is untouched and every entry remains correct; the statements are not. | every ledger control — this is a presentation-layer corruption of correct data | **No, from inside the ledger.** The external *values* attached to reports are company-scoped; the *structure* is not. | `account/models/account_report.py:25-46`, `:310-348`, `:868-879` vs `:898` |
| `BW-10` | **Unchecked-but-posted entries counted as reviewed** | A per-journal setting decides whether an entry is marked reviewed on posting. Where it is off, entries post with the reviewed marker false and are included in every report identically to reviewed entries. There is no completeness control that a period contains no unreviewed postings, and the marker is not a precondition of any close. | debit/credit; lock composition; close preconditions (drafts and unreconciled bank lines only) | **Yes, trivially, by filtering — but nothing requires anyone to.** Adopt as a close-checklist item alongside the two the package already recommends. | `account/models/account_move.py:4915` (`move.checked = move.journal_id.autocheck_on_post`), `:282-289` (`checked`, `tracking=True`); `account/models/company.py:475-520` (close preconditions: drafts, then unreconciled bank lines — no reviewed-state test) |
| `BW-11` | **Silent loss of a settlement fact with a surviving derived state** | Reconciliation-record deletion writes **no message and no tracking value**, and `matching_number`, `full_reconcile_id`, `amount_residual` and `reconciled` are **not tracked fields**. So the removal of a settlement fact is the one class of change to a posted entry that leaves neither hash evidence nor chatter evidence, while the derived residual it feeds is a stored value. | every control | **No.** This is the narrowed, and therefore stronger, version of `CONTRA-10` — see `N6`. | `account/models/account_partial_reconcile.py:100-136`; `account/models/account_move_line.py:244-280` (untracked) vs `:104-350` (the tracked set) |

`RECOMMENDATION` — the eleven cases above share one shape: **a control that is a property of the
write path rather than of the stored data, or a key that is unique only within one route.** That is
the same diagnosis file 18 reaches for the seven proof equations, arrived at independently from a
different direction. `BW-01`, `BW-02`, `BW-04`, `BW-08` and `BW-09` are the ones I would put in
front of the Boss.

---

## PART 3 — INDEPENDENT FINDINGS

### `B-01` — The package's most consequential claim is the one that does not survive

- **CHALLENGE** — `GAP-B02` is described as "the most consequential single gap in Wave A" and is
  cited as the root cause of six downstream findings. It is stated as a total absence.
- **TARGET** — file 21 `GAP-B02`; file 09 "The two facts with no owner"; file 06 §1 and §2.
- **EVIDENCE** — `VERIFIED FACT`: a storage-enforced, copy-suppressed import identity exists on bank
  statement lines (`account_bank_statement_import/models/account_bank_statement.py:15,18`); five
  typed entry-level origin links exist (`account/models/account_move.py:207,225,245,280` and the
  reversal link); a free-text source reference exists (`:630`); an EDI document record links entry,
  format and attachment (`account_edi/models/account_edi_document.py:22-24`).
- **CLASSIFICATION** — `CONTRADICTED` as written; `CONFIRMED WITH CAVEAT` once rescoped.
- **REQUIRED RESOLUTION** — restate `GAP-B02` as: *no general, mandatory, route-independent
  accounting-event identity or provenance carrier exists; route-specific carriers exist, one of them
  storage-enforced, and they are the pattern SMEsPlus should generalise rather than invent.* The
  downstream conclusions (`XM-01`, correction-semantics collapse, migration lineage) **survive** — but
  the package must stop asserting a total absence it did not verify, because the surviving evidence
  makes the recommendation *stronger*: the reference system demonstrably knows how to enforce an
  idempotency key at storage level, and applies it to exactly one route.

### `B-02` — A third unconditional immutability exists and inverts a headline count

- **CHALLENGE** — "Exactly two things are unconditionally immutable in the reference core ledger."
- **TARGET** — file 15 §2 and its `CHECKPOINT L8` verified-findings row.
- **EVIDENCE** — `VERIFIED FACT`: `account/models/company.py:317-322` refuses to clear the audit-trail
  flag while any entry exists; `account/models/account_move.py:3350-3358` refuses deletion of a
  previously posted entry under that flag; `:4805-4830` re-routes the destructive path to cancel;
  `account/models/mail_message.py:7-16` extends the protection to the tracking messages themselves.
- **CLASSIFICATION** — `CONTRADICTED`.
- **REQUIRED RESOLUTION** — correct the count to three and, more importantly, correct the *character*
  of the finding. The reference model does contain a **monotonic, tenant-database-resident, control
  over destruction of posted facts**. `SB-04` and `CONTRA-14` are both scoped by it (see `N13`) and
  must be re-worded to say *"in companies that have never enabled audit trail"*.

### `B-03` — The SaaS boundary register understates the boundary in two structures

- **CHALLENGE** — "the outermost boundary is the company group"; the fifteen-row boundary register.
- **TARGET** — file 16 §1 and §2; file 06 §6.
- **EVIDENCE** — `VERIFIED FACT`: `base/models/res_currency.py:128-136` resolves rates with
  `company_id IN (False, root_id)` and `:298-308` joins every company to any null-company rate row;
  `:365-366` makes the company nullable. `account/models/account_report.py:25-46` defines the report
  with a country and **no company**, while `:898` gives the external *value* a required company.
- **CLASSIFICATION** — `CONTRADICTED` (understatement — the risk is larger than recorded).
- **REQUIRED RESOLUTION** — add two rows to the file-16 register: **currency rate with null company —
  database-wide**, and **report definition — no company dimension, database-wide**. Both belong in
  §3 as boundary failures alongside `SB-01`, and both are covered by requirement `TI-01`, which
  should be widened from "configuration value" to "**any control-affecting or measurement-affecting
  record**". Raised as `SB-05` (rate) and `SB-06` (report structure).

### `B-04` — Reopening is not traceless, and the close/reopen findings are internally inconsistent

- **CHALLENGE** — file 12 asserts reopening leaves "no artefact"; the same file's `GAP-G01` row says
  there is "only a tracked field change on the company record"; file 16 asserts control evidence
  "leaves the tenant".
- **TARGET** — file 12 §2 (Reopening row, and the "Who closed" row); file 16 `SB-04`.
- **EVIDENCE** — `VERIFIED FACT`: `account/models/company.py:73-96` — all five lock dates are tracked;
  `account/models/account_lock_exception.py:13-97,242,258-266,277-325` — a persistent exception
  record with reason, expiry, scope and a linked audit view.
- **CLASSIFICATION** — `CONTRADICTED` in part; the *governance* conclusion survives intact.
- **REQUIRED RESOLUTION** — reconcile the three statements to one: **"Reopening requires no distinct
  authority, no justification and no re-test of the close preconditions; it is recorded as a tracked
  field change, which is in-database and, with audit trail enabled, undeletable."** Decision `CL-03`
  is unaffected and remains a Boss decision. `SB-04` must be narrowed (see `B-02`).

### `B-05` — The control-account negative and the control-account unknown cannot both stand

- **CHALLENGE** — file 18 `P-04` asserts "there is no explicit control-account concept" as settled;
  file 21 `GAP-A01` lists the same question as an open unknown, closable by reading, priority medium.
- **TARGET** — files 18 and 21.
- **EVIDENCE** — `VERIFIED FACT`: the term does not occur in the three accounting modules I searched.
  `REFERENCE BEHAVIOUR`: the function is present and explicit —
  `account/models/account_account.py:98,137,697`, plus a partner-ledger aggregation of the same items.
- **CLASSIFICATION** — `CONTRADICTED` (as a functional negative) and **`VETO` on the register
  inconsistency**: a package may not simultaneously assert a negative and list it as unresolved.
- **REQUIRED RESOLUTION** — close `GAP-A01` with the evidence above, and restate `P-04` as: *the
  reference model has no control-account **entity**; it has a control-account **function** carried by
  an account-level reconcilability flag and account type.* The favourable conclusion `P-04` draws —
  one record, so subledger and control cannot disagree — **survives and is strengthened**, because the
  flag is the thing that forces the single-record model.

### `B-06` — An unrealised-FX posting mechanism exists; the negative was searched in the wrong module

- **CHALLENGE** — "No posting mechanism for unrealised FX / revaluation was found."
- **TARGET** — the `N8` claim as carried in the package's currency and reconciliation material.
- **EVIDENCE** — `VERIFIED FACT`:
  `account_reports/models/account_multicurrency_revaluation_report.py:69,73-75,117-131`;
  `account_reports/wizard/multicurrency_revaluation.py:26-27,59-66,163-179`.
- **CLASSIFICATION** — `CONTRADICTED`.
- **REQUIRED RESOLUTION** — record the mechanism, and record the two guards it ships that Wave A
  should adopt: a warning when a **custom rate** is in force, and a warning when the **previous
  period's provision entry was never reversed**. Both are precisely the "prove it from the data"
  discipline file 18 recommends, already implemented. Note for Reviewer A: the interaction between
  this wizard and the 1.0 rate fallback is in A's scope, not mine, and I have not adjudicated it.

### `B-07` — "Not hash-detected" has been written as "not detected" throughout

- **CHALLENGE** — `CONTRA-01b` and the derived rows in files 09, 15 and 18 assert that five field
  groups on a secured entry are "neither blocked nor detected".
- **TARGET** — `CONTRA-01b`; file 15 §2 row "Entry substance while hashed".
- **EVIDENCE** — `VERIFIED FACT`: `account/models/account_move_line.py` tracks exactly six item fields
  — `:104` account, `:111` label, `:127` balance, `:198` taxes, `:233` tax tags, `:350` due date — and
  `:1638-1643` writes each change as a chatter message with before/after values on any entry that has
  been posted before. `amount_currency`, `currency_id`, `analytic_distribution`, `matching_number`,
  `full_reconcile_id` and `amount_residual` are **not** in that set.
- **CLASSIFICATION** — `CONTRADICTED` for two of the five field groups; `CONFIRMED` and **sharpened**
  for the other three.
- **REQUIRED RESOLUTION** — split every affected row into *blocked* / *hash-detected* / *field-tracked*.
  The resulting statement is narrower and much harder to argue with: **the transaction-currency
  amount, its currency, and the analytic distribution are the fields that can be changed on a secured,
  previously posted entry with no evidence of any kind.**

### `B-08` — The migration boundary is anchored to an unversioned mutable date

- **CHALLENGE** — file 17 treats the opening position as a single summarised posted entry lacking
  provenance. That is true, and it misses a second defect in the same object.
- **TARGET** — file 17 §1 and `MG-01`, `MG-08`, `MG-13`, `MG-14`.
- **EVIDENCE** — `VERIFIED FACT`: `account/models/company.py:172-174` (`account_opening_date` is a
  plain mutable `Date`, defaulted to 1 January), `:733` (the opening entry is dated **one day before**
  it), `:782-788` (programmatic update refused only once the entry leaves draft).
- **CLASSIFICATION** — `CONFIRMED WITH CAVEAT` on the package's finding; **new finding** on the anchor.
- **REQUIRED RESOLUTION** — add `MG-15`: *the migration boundary date is itself a fact with
  provenance, is bound to the opening entry it produced, and cannot be altered after that entry is
  accepted.* `MG-13` (hard-lock the opening position) mitigates but does not close this, because the
  hard lock governs the **entries**, not the **company field**. See `BW-07`.

### `B-09` — A configurable approval engine exists in the build, and it is elevation-transparent

- **CHALLENGE** — "no maker-checker anywhere in the core ledger" was carried forward as if it settled
  the domain question.
- **TARGET** — file 14 §2 assessment; `IC-07`, `IC-08`, `IC-13`.
- **EVIDENCE** — `VERIFIED FACT`: `web_studio/models/studio_approval.py:378-393` patches named public
  methods at registry load; `:197-218` refuses `create`/`write`/`unlink`; `:267-273` special-cases the
  journal-entry model; `:81,106` provide an approval group and an exclusive-approver mode; **`:397-425`
  skips the check entirely under privilege elevation, logging the call as allowed.**
- **CLASSIFICATION** — `CONTRADICTED` at domain scope; `CONFIRMED` at core-ledger scope.
- **REQUIRED RESOLUTION** — re-word file 14, and record the **elevation-transparency** property as a
  Wave A design constraint: an approval control that a privileged code path skips is subject to the
  same criticism the package already makes of the suppression-flag pattern. This also **raises the
  priority of `GAP-C04`** (external reachability of suppression), because the same elevation escape
  now governs an approval control as well as four integrity controls.

### `B-10` — Duplicate detection exists and its coverage gaps are the real finding

- **CHALLENGE** — `XM-01` and file 06 §2 assert nothing detects a doubly posted business event.
- **TARGET** — `XM-01`; file 06 §2; `MG-02`.
- **EVIDENCE** — `VERIFIED FACT`: `account/models/account_move.py:691,752-760,1831-1900,5034-5037`;
  `account/models/account_payment.py:748-753`;
  `account_online_synchronization/models/account_journal.py:221-294`.
- **CLASSIFICATION** — `CONTRADICTED` as written; the **coverage analysis is the finding worth keeping**.
- **REQUIRED RESOLUTION** — replace the absolute negative with the coverage statement: *duplicate
  detection exists for customer documents (amount + date), vendor documents (reference, same calendar
  year), payments, and bank transactions (two disjoint keys). It does not cover miscellaneous entries
  at all, does not span a year boundary for vendor documents, does not span ingestion routes for bank
  transactions, and blocks nothing outside the bank-import unique constraint.* That statement supports
  `MG-02` better than the absolute one did. See `BW-01` to `BW-04`.

### `B-11` — The tax-period close is a counterexample the close model has not absorbed

- **CHALLENGE** — file 12 answers the Boss question "what exactly becomes locked" with "none of those
  — a range of accounting dates". For the tax period that is incomplete.
- **TARGET** — file 12 §1 and §2; decisions `CL-01`, `CL-03`.
- **EVIDENCE** — `VERIFIED FACT`: `account_reports/models/account_move.py:19` binds an entry to a
  report; `:132-133` posting it **advances the tax lock date**; `:221-222` derives the period
  boundaries; `:239-297` re-tests the lock on reset-to-draft and on carryover.
- **CLASSIFICATION** — `CONFIRMED WITH CAVEAT`.
- **REQUIRED RESOLUTION** — file 12 should record that the reference model **already contains one
  close-as-a-record**, for one period type, and that `CL-01` is therefore not a choice between an
  invented pattern and a bare date — there is a reference pattern to adapt. This materially changes
  the cost of the `CL-01` decision and should be in front of the Boss with it.

### `B-12` — Thai statutory items: nothing determined

- **CHALLENGE** — whether anything in my scope bears on Thai statutory requirements.
- **TARGET** — file 21 §D (`TX-01`–`TX-07`).
- **EVIDENCE** — `VERIFIED FACT`: the build contains `l10n_th/` and `l10n_th_reports/`; the Thai
  reporting module contains value-added-tax and withholding-tax report handlers and a tax report data
  file; the Thai base module's entry extension only selects an invoice report template.
  (`l10n_th/models/account_move.py`; `l10n_th_reports/models/tax_report_vat.py`,
  `tax_report_pnd.py`; `l10n_th_reports/data/account_tax_report_data.xml` — inventory read only.)
- **CLASSIFICATION** — `HOLD / EVIDENCE REQUIRED`.
- **REQUIRED RESOLUTION** — none by me. `TX-01`–`TX-07` remain routed to the Accounting-Tax track.
  I assert no Thai legal requirement. Any Thai account, tax or report name is **candidate /
  UNVALIDATED**. I note only that `B-11` (a tax close that is a record) and `N4` may be relevant
  evidence for `TX-05`, and hand that observation over without adjudicating it.

### `B-13` — What I could not close

- `UNKNOWN — EVIDENCE REQUIRED`: whether any reconstruction routine repairs drifted stored settlement
  values (`GAP-E03`). I searched `S-CORE` and found none; I did not search the framework's recompute
  facilities, so this stays `B. NOT FOUND IN SEARCHED SCOPE` and must not be written as absence.
- `UNKNOWN — EVIDENCE REQUIRED`: whether the elevation escape at `B-09` and the suppression flags at
  `GAP-C04` are reachable from an external interface. Reading cannot close it; this is the highest-
  value executed test in the programme and now governs one more control than the package recorded.
- `UNKNOWN — EVIDENCE REQUIRED`: whether template-derived and tenant-created chart entries are
  distinguishable anywhere. I did not read the chart-template loader; the package's `TI-05` position
  stands unchallenged by me, neither confirmed nor contradicted.
- `NOT YET SEARCHED`: every module listed as unsearched in Part 0. No negative in this review extends
  to them.

---

## PART 4 — REVIEWER B POSITION

`REVIEWER B POSITION` — **The corrected canonical model's conclusions largely survive; its negative
claims largely do not.** Of seventeen material negatives I audited, **nine are contradicted in whole
or in a material part**, four hold only with a caveat, and three are verifiable absences only once
their scope is narrowed to what was actually searched. In every contradicted case the *downstream
recommendation* is unharmed, and in five cases (`B-01`, `B-05`, `B-06`, `B-07`, `B-10`) the corrected,
narrower statement is a **stronger** finding than the absolute one it replaces. The package's real
defect is not its reasoning but its epistemics: it converted "not found" into "does not exist"
roughly forty times, and did so most confidently on its own headline claim.

Three findings change the substance rather than the wording: **a third unconditional immutability
exists** (`B-02`), which narrows two SaaS and contradiction-register entries; **the outermost boundary
is the database, not the company group** (`B-03`), which makes the tenancy risk larger than recorded;
and **a close-as-a-record already exists for the tax period** (`B-11`), which gives decision `CL-01` a
reference pattern it was said not to have.

I approve nothing. Boss is sole Final Approver.

### Counts

| Measure | Count |
|---|---|
| Negative claims audited | 17 |
| `E. CONTRADICTED` (whole or material part) | 9 |
| `CONFIRMED WITH CAVEAT` | 4 |
| `A. VERIFIED ABSENCE` at an explicitly stated scope | 3 |
| `B. NOT FOUND IN SEARCHED SCOPE` | 2 |
| `D. UNKNOWN` | 1 |
| `B`/`C`/`D` promoted to `A` by me | **0** |
| Balanced-but-wrong cases registered | 11 |
| — undetectable by any control in the searched scope | 8 (`BW-01`, `BW-02`, `BW-05`, `BW-06`, `BW-07`, `BW-08`, `BW-09`, `BW-11`) |
| Independent findings | 13 |
| — `CONTRADICTED` | 7 |
| — `CONFIRMED WITH CAVEAT` | 3 |
| — `CONFIRMED` | 0 standalone |
| — `HOLD` | 1 (`B-12`, Thai statutory) |
| — `VETO` | 1 (`B-05`, register self-inconsistency) |
| — `UNKNOWN` carried | 3 (`B-13`) |
| New SaaS boundary failures raised | 2 (`SB-05` database-wide rate, `SB-06` database-wide report structure) |
| New migration requirement raised | 1 (`MG-15`) |
| Thai statutory determinations made | **0** |
| Reference code, schema or architecture copied | **none** |

`L12B RECORDED — RESEARCH ONLY. Not Boss approval.`
