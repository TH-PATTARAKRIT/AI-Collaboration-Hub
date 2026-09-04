# P06_BANK_EVENT_REGISTER.md

**Session:** SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001 · **Process:** P06 Bank-to-Reconcile
**Branch:** research/account-p06-bank-to-reconcile-2026-09-04-001 (base `88f52cd`)
**Classification:** LAYER 2 — AUDIT QUARANTINE (contains reference-ERP `file:line`)
**Evidence root `$V18E`:** `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons` (source S-01)

---

## 1. Scope of this register

A **bank event** is any assertion entering the system that money moved at a bank. This register enumerates the doors through which such assertions arrive, the identity each door attaches, and whether that identity is enforceable. It answers one question above all: **can the system tell that two records describe the same real-world bank transaction?**

**DENOMINATOR — INGESTION DOORS.** POPULATION: modules under `$V18E` matching the S-01 pattern that create or populate `account.bank.statement.line`. PATTERN: creation sites of that model plus population of any identity field. PATH SET: `$V18E/account`, `$V18E/account_bank_statement_import{,_camt,_csv,_ofx,_qif}`, `$V18E/account_online_synchronization`, `$V18E/account_bank_statement_extract`. UNIT: distinct ingestion door. **RESULT: 6 doors.** Doors outside this path set were not enumerated — negatives below are Class B beyond it.

---

## 2. The bank event object

**BER-F-01 — A bank statement line *is* a journal entry, by delegation.**
`$V18E/account/models/account_bank_statement_line.py:12` — `_inherits = {'account.move': 'move_id'}`, with the move `required=True, readonly=True, ondelete='cascade'` (line 24-29).
**Consequence:** there is no such thing as an unposted, non-accounting bank observation. The moment a bank event is recorded it has already produced a journal entry. `create` force-posts it: `st_lines.move_id.action_post()` (`:435`). **The system has no "observed but not yet accounted" state for bank data.** This is the structural root of the canonical-question answer in the Payment State Model file: *bank confirmation state and accounting posting state are fused at the point of ingestion, by design.*

**BER-F-02 — The counterpart of every new bank event is the journal suspense account, and its absence is a hard stop.**
`$V18E/account/models/account_bank_statement_line.py:645-652` — the counterpart is `self.journal_id.suspense_account_id.id`; without one, `UserError: "You can't create a new statement line without a suspense account set on the %s journal."`
**Consequence:** unmatched bank money is always parked in one named account per journal. That is the correct shape. What is missing is ageing over it — see the Edge Case Matrix, E1.

**BER-F-03 — `payment_ref` is a label, never an identifier.**
`$V18E/account/models/account_bank_statement_line.py:672,684` — `payment_ref` is copied into the move line names. It has no uniqueness and no constraint. Matching rules read it as text.

---

## 3. The two identity fields, and what backs them

| # | Field | Model | Type | DB constraint | Enforcement scope | Populated by |
|---|---|---|---|---|---|---|
| I-1 | `unique_import_id` | `account.bank.statement.line` | Char, `readonly=True, copy=False` | **`unique (unique_import_id)`** — single column, **database-global** | Python pre-search (global, `sudo`, no journal/company domain) **+** DB UNIQUE backstop | File import: CAMT, OFX **only** |
| I-2 | `online_transaction_identifier` | `account.bank.statement.line` | Char, `readonly=True` | **none** | Python filter at fetch time, **scoped to one journal** | Online synchronisation only |
| — | `internal_index` | same | Char | non-unique index | ordering key only | computed, always |
| — | `transaction_details` | same | Json, `readonly=True` | none | — | provider payload only |

**BER-F-04 — `unique_import_id` is namespaced by *value*, not by *schema*.**
`$V18E/account_bank_statement_import/models/account_bank_statement.py:14-19` declares the constraint on the bare column. `$V18E/account_bank_statement_import/models/account_journal.py:223-226` builds the value as `sanitized_account_number + '-' + journal_id + '-' + raw_id`, and **the account-number prefix collapses to empty when the file supplies no account number**, leaving `journal_id-raw_id`.
**Consequences:** (a) uniqueness is only as good as the prefix construction; (b) because the constraint is global rather than per-company, a collision is a **hard database error**, not a graceful skip; (c) `sanitize_account_number` was **not read** in this pass — the residual cross-company collision question is carried as open item `P06-OQ-01`. **Class D (unknown), not Class A.**

**BER-F-05 — `online_transaction_identifier` has no database constraint at all.**
`$V18E/account_online_synchronization/models/account_bank_statement.py:16`. NOT FOUND: any `_sql_constraints` in `account_online_synchronization` or `account_bank_statement_extract` (PATTERN `_sql_constraints`, PATH SET those two module trees, `--include="*.py"`, zero matches). **Class A within that declared scope.**
The dedup filter is Python, per journal: `$V18E/account_online_synchronization/models/account_online.py:284-306`, domain `('journal_id','=',journal_id.id)` on `journal_ids[0]` only.
Its concurrency defence is a bare commit, and the code says so: `:830-831` — `# Committing here so that multiple thread calling this method won't execute in parallel and import duplicates transaction` / `self.env.cr.commit()`. **There is no advisory lock and no unique index to fall back on.**

**BER-F-06 — A null identifier is treated as "not a duplicate".**
`$V18E/account_online_synchronization/models/account_online.py:301` uses a walrus guard — transactions with a falsy identifier fall through unfiltered. `$V18E/account_bank_statement_import/models/account_journal.py:262-264` likewise treats a missing/empty `unique_import_id` as passing the filter. And in PostgreSQL, NULLs are not equal to one another, so the UNIQUE index does not constrain them either.
**This is the load-bearing defect of the whole ingestion layer:** the identity system fails *open*, at all three enforcement points, for exactly the records that have no identity.

---

## 4. The six ingestion doors

| Door | Path | Identity attached | Duplicate defence | Classification |
|---|---|---|---|---|
| D-1 CAMT file import | `$V18E/account_bank_statement_import_camt` | `unique_import_id` from `AcctSvcrRef`/`NtryRef` | DB UNIQUE + Python | **Partial — fails open on fallback, see BER-F-07** |
| D-2 OFX file import | `$V18E/account_bank_statement_import_ofx` | `unique_import_id` = `FITID` | DB UNIQUE + Python | **Strongest of the six** |
| D-3 CSV file import | `$V18E/account_bank_statement_import_csv` | **none** | **none** | **No defence** |
| D-4 QIF file import | `$V18E/account_bank_statement_import_qif` | **none** | **none** | **No defence** |
| D-5 Online synchronisation | `$V18E/account_online_synchronization` | `online_transaction_identifier` | Python only, per journal | **Weak — no DB backstop** |
| D-6 OCR statement extraction | `$V18E/account_bank_statement_extract` | **none** | **none** | **No defence** |
| D-7 Manual keying (UI / `create`) | `$V18E/account` core | **none** | **none** | **No defence** |

*(Seven rows: D-7 manual keying is the seventh door and is counted here because it produces the same object through the same `create`. The "6 doors" denominator in §1 counted module-borne doors only; the corrected denominator for *all* ways a bank event can be created is **7**. This correction is recorded rather than silently applied — see the Revision Log.)*

**BER-F-07 — CAMT identity degrades to a positional key.**
`$V18E/account_bank_statement_import_camt/lib/camt.py:760-771`: when `AcctSvcrRef` is missing, all-zeros, or the literal `NOTPROVIDED`, the identity becomes `'{}-{}-{}'.format(name, date, sequence)` — statement name plus date plus row position.
**Consequence:** re-importing the same economic transactions under a different statement name, or in a different row order, yields **different** identities. Dedup silently fails open with no warning. Thai bank CAMT profiles vary in whether `AcctSvcrRef` is populated; **whether any specific Thai bank populates it is HOLD / EVIDENCE REQUIRED** (source NC-03, not held).

**BER-F-08 — CSV and QIF have zero duplicate defence.**
NOT FOUND: `unique_import_id` anywhere in `$V18E/account_bank_statement_import_csv` or `..._qif` (PATTERN `unique_import_id`, recursive, all file types, zero matches). **Class A within that declared scope.** Re-importing an identical CSV or QIF file creates a complete second set of statement lines **and** a second set of posted journal entries, silently.
**This is the single highest-severity finding in this register.** For a Thai SME, CSV is the most likely bank-file format on offer.

**BER-F-09 — OCR-created lines are indistinguishable from manual lines.**
`$V18E/account_bank_statement_extract/models/account_bank_statement.py:48-53` sets exactly four fields: `amount`, `date`, `journal_id`, `payment_ref`. No identity field of any kind. And `:63-70` — with `extract_bank_statement_digitalization_mode == 'auto_send'` digitisation fires **automatically on attachment**, no user action.
`:44-46` — OCR writes `balance_start` and `balance_end`. Note it writes the *computed* `balance_end`, not the user-asserted `balance_end_real`. Combined with BER-F-11 this means the OCR path can satisfy the completeness check without any independent figure ever being supplied.

---

## 5. Statement-level controls, and why they are weaker than they appear

**BER-F-10 — `balance_start` is derived, not asserted.**
`$V18E/account/models/account_bank_statement.py:142-165` walks back to the previous statement's `balance_end_real`.

**BER-F-11 — `balance_end_real` defaults to the computed `balance_end`.**
`$V18E/account/models/account_bank_statement.py:173-176` — `stmt.balance_end_real = stmt.balance_end`.
**Consequence:** `is_complete` (`:189-192`) compares `balance_end == balance_end_real`. **Unless a human overrides the ending balance, this control compares a number against itself and is satisfied by construction.** A freshly created statement is auto-complete. This is a control that reports green without having tested anything.

**BER-F-12 — `balance_end` counts posted lines only.**
`$V18E/account/models/account_bank_statement.py:168-171` — `lines = stmt.line_ids.filtered(lambda x: x.state == 'posted')`. Draft and cancelled lines are silently excluded from the footing.

**BER-F-13 — `is_valid` is not persisted.**
`$V18E/account/models/account_bank_statement.py:91-94` — non-stored computed with a custom `search`. It cannot be used as a durable control state, cannot be audited historically, and its per-journal SQL join (`:247-262`) carries **no company predicate** — chaining is journal-scoped only. Given the runtime finding that journal codes repeat across companies (Cross-Process Ownership CPO-F-04), a journal-only chain is not a company-safe control.

**BER-F-14 — The first statement of a journal is unconditionally valid.**
`$V18E/account/models/account_bank_statement.py:228-239` — `return not previous or ...`. The opening position of every bank journal is unverified by construction. Combined with BER-F-15 this means the opening balance can be a plug.

**BER-F-15 — Online sync can create a synthetic opening line that is a plug.**
`$V18E/account_online_synchronization/models/account_bank_statement.py:77-83` — when a journal has no lines and `online_account.balance - total != 0`, a posted statement line is created for the difference, labelled `"Opening statement: first synchronization"`. It is a real posted journal entry with **no bank counterpart transaction**.
**Consequence for P06:** on first sync, any historical mismatch is absorbed into a plug rather than surfaced. It must be treated as an audit item, not as an opening balance.

**BER-F-16 — `problem_description` is advisory only.**
`$V18E/account/models/account_bank_statement.py:207-215`. Computed text, never persisted, never blocking.

**BER-F-17 — `_check_attachments` validates nothing.**
`$V18E/account/models/account_bank_statement.py:331-349` — a context manager that re-points `ir.attachment.res_id`/`res_model` after create/write. No content, count or presence validation. And `write` **silently drops** `attachment_ids` on multi-record writes (`:351-365`). The bank's own statement document is therefore not a controlled artefact.

---

## 6. Mutability and deletability of bank evidence

**BER-F-18 — The line's `write` bypasses readonly protection wholesale.**
`$V18E/account/models/account_bank_statement_line.py:438-443` — `super(...).with_context(skip_readonly_check=True).write(vals)`. Fields declared `readonly=True` — including both identity fields — are writable through this path.

**BER-F-19 — Only 6 fields propagate to the journal entry.**
`$V18E/account/models/account_bank_statement_line.py:813-817` — `_synchronize_to_moves` fires only for `payment_ref, amount, amount_currency, foreign_currency_id, currency_id, partner_id`.
**Consequence:** `transaction_details`, `transaction_type`, `internal_index`, `statement_id` and every identity field can be changed **without any trace on the journal entry**. The audit trail on the accounting side does not cover the identity of the bank event it represents.

**BER-F-20 — Deletability of bank evidence is a company setting.**
`$V18E/account/models/account_bank_statement_line.py:445-452` — with `check_account_audit_trail` the move is cancelled and retained; without it, `moves_to_delete.with_context(force_delete=True).unlink()`.
**Consequence:** whether a bank event can be erased is configuration, not invariant. For P06 this must become a **tenant-level locked setting**, not a company preference.

**BER-F-21 — The statement line ↔ journal entry link is 1:1 by convention only.**
`$V18E/account/models/account_move.py:225-231` — `statement_line_id` is indexed `btree_not_null`, **an ordinary partial index, not UNIQUE**. NOT FOUND: any unique index or `_sql_constraints` entry involving `statement_line_id` (PATTERN `_sql_constraints|unique|UNIQUE` over that file, 5 hits, all `unique_name` on `(name, journal_id)`). **Class A within that file's scope.**
The reverse relation is declared **plural** — `$V18E/account/models/account_bank_statement_line.py:848-854`, `statement_line_ids = fields.One2many(...)`. The schema contemplates *n* lines per move.
Cascade is **asymmetric**: line→move is `ondelete='cascade'`; move→line has no `ondelete`, so the default applies and deleting a line can orphan the move's back-pointer.

---

## 7. Silent-drop behaviours (events that vanish without a record)

| ID | Behaviour | Evidence | Why it matters to P06 |
|---|---|---|---|
| SD-1 | Any imported transaction with `amount == 0` is discarded | `account_bank_statement_import/models/account_journal.py:261` | Zero-value bank events (reversals netting to nil, informational rows) never enter the record |
| SD-2 | A duplicate's amount is **added back into `balance_start`** so the statement still foots | same file `:266-269` | The statement reconciles *because* the duplicate was suppressed — the footing hides the suppression |
| SD-3 | Re-fetched online transactions are `continue`d with no log, no counter, no notification | `account_online_synchronization/models/account_online.py:301-304` | No evidence remains of what was suppressed or why |
| SD-4 | "Zero Balancing" lines are imported then their moves cancelled post-hoc, driven by an **untrusted provider flag** inside `transaction_details` | `account_online_synchronization/models/account_bank_statement.py:39-43` | A remote payload field decides whether an accounting entry stands |
| SD-5 | Import of an all-duplicate file raises a message that conflates "duplicate file" with "empty result" | `account_bank_statement_import/models/account_journal.py:286-287` | Operator cannot distinguish the two |
| SD-6 | Mid-import `cr.commit()` between 500-line batches; a failed sync leaves partial data committed | `account_online_synchronization/models/account_bank_statement.py:91-111` | Partial bank days are a normal outcome of failure, not an exception |

---

## 8. Post-hoc duplicate detection — advisory only

A detection layer exists and is **not** a prevention layer: `account.duplicate.transaction.wizard`, `$V18E/account_online_synchronization/wizard/account_journal_duplicate_transactions.py:7-8,32`.

Two heuristics, UNIONed (`$V18E/account_online_synchronization/models/account_journal.py:269-294`):
1. Fuzzy: same `currency_id + amount + account_number + move.date`, `HAVING count > 1`. **This cannot distinguish a duplicate from two genuinely identical transactions** — two identical daily fees will be flagged.
2. Repeated `online_transaction_identifier` within a 3-month back-window.

**BER-F-22 — The existence of heuristic 2 is direct evidence that `online_transaction_identifier` can be duplicated in the database.** If the Python filter were sufficient, a query searching for repeats of that identifier would be dead code.
The code itself states the design intent (`:238-239`): the fuzzy heuristic exists because identifier filtering already happened upstream — i.e. it targets exactly the duplicates the identifier **cannot** catch: manual entry, a second file, a mixed source. And the UI says so plainly (`static/src/components/transient_bank_statement_line_list_view/transient_bank_statement_line_list_view.xml:8`): lines "not created using the online synchronization … might cause duplicate entries."

---

## 9. Pending transactions

**BER-F-23 — Pending transactions are fetched but never become statement lines.**
`$V18E/account_online_synchronization/models/account_online.py:252-261` returns `pendings` on a separate payload key. The only consumer is the missing-transactions wizard, which tags them `state='pending'` and then hard-blocks: `wizard/account_bank_statement_line.py:60-61` — `raise UserError(_("You cannot import pending transactions."))`.
**Identity gap:** because pendings are excluded, a pending transaction that later posts arrives as a *new* transaction. Whether it collides with anything depends entirely on the provider re-issuing the same identifier. **That is a provider-side contract not expressed anywhere in this codebase.** Class D (unknown) — carried as `P06-OQ-02`.

---

## 10. Bank event taxonomy for the target design

Derived from the above; every row states what P06 must supply that the reference does not.

| Event | Present in reference | Identity | Gap P06 must close |
|---|---|---|---|
| E-BANK-01 Credit received (customer/other) | yes | door-dependent | identity for D-3/D-4/D-6/D-7 |
| E-BANK-02 Debit paid (vendor/other) | yes | door-dependent | as above |
| E-BANK-03 Bank charge | **no first-class concept** | — | see FX/Fee/Interest Matrix |
| E-BANK-04 Bank interest | **no first-class concept** | — | as above |
| E-BANK-05 Inter-account transfer leg | yes (two legs) | door-dependent | single-counting proof |
| E-BANK-06 Returned/bounced item | **NOT FOUND in v18 pattern set**; a v14 custom module `account_payment_return` exists | — | migration gap, see Custom Delta |
| E-BANK-07 Cheque cleared | partial | cheque number on payment | post-dated cheque absent from v18 set |
| E-BANK-08 Provider settlement batch | via provider modules | provider reference | net-vs-gross settlement, see Provider Trace |
| E-BANK-09 Opening plug | yes (BER-F-15) | none | must be surfaced, never silent |
| E-BANK-10 Zero-value event | **discarded (SD-1)** | — | must be recorded, not dropped |

---

## 11. Blockers raised

| ID | Blocker |
|---|---|
| P06-B-10 | Bank transaction identity differs per door; **4 of 7 doors attach no identity at all**, and the identity system fails open at all three enforcement points for null identities. |
| P06-B-11 | `is_complete` compares a derived figure against a default copy of itself; the statement completeness control is satisfied by construction. |
| P06-B-12 | Bank evidence deletability is a company setting, not an invariant. |
| P06-B-13 | Identity fields can be mutated without any journal-entry trace (only 6 fields synchronise). |
| P06-B-14 | Six silent-drop behaviours remove bank events with no durable record of the removal. |
| P06-B-15 | The statement line ↔ journal entry relation is 1:1 by convention only; the schema permits *n*:1 and the cascade is asymmetric. |

## 12. Open items (not upgraded to findings)

| ID | Item | Class |
|---|---|---|
| P06-OQ-01 | Cross-company collision behaviour of `unique_import_id` depends on `sanitize_account_number`, which was not read. | D |
| P06-OQ-02 | Provider identifier stability across pending→posted is a provider contract not in this codebase. | D |
| P06-OQ-03 | `_get_protected_vals` semantics around the move write-back were not read. | C |
| P06-OQ-04 | Whether any specific Thai bank populates CAMT `AcctSvcrRef` — **HOLD / EVIDENCE REQUIRED**, routed to Accounting-Tax / vendor-contract track. | C |

---

# End
