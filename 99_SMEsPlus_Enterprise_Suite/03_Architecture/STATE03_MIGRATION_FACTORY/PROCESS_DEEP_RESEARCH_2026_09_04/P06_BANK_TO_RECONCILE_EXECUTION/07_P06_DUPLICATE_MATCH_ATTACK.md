# P06_DUPLICATE_MATCH_ATTACK.md

**Session:** SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001 · **Process:** P06 Bank-to-Reconcile
**Branch:** research/account-p06-bank-to-reconcile-2026-09-04-001 (base `88f52cd`)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Scope model:** `[SMEPLUS-26-09-04-ACC-REV2-CORR1]` applied — see the Scope Ownership Matrix.

---

## 0. Method and honesty rules for this file

The directive requires a **mandatory duplicate settlement/posting attack**. Each attack below states its **precondition**, its **mechanism**, the **guard that exists or was not found** (with the exact search boundary), the **accounting consequence**, and a **classification** from:

- **CONFIRMED DEFECT** — provable from quoted source alone, no interpretation required
- **PLAUSIBLE** — the mechanism is evidenced but reachability depends on something not in the searched scope
- **NOT DECIDABLE FROM STATIC EVIDENCE** — requires a runtime test or data
- **HOLD — SCOPE EVIDENCE REQUIRED** — requires a scope determination under CORR1

**No attack was executed.** Nothing in this session ran against any system. These are static findings about reachable code paths.

---

## A1 — Duplicate imported bank transaction

**Precondition:** a bank journal receiving transactions from more than one channel, or any user with statement-line create rights.

**Mechanism.** Seven ingestion doors exist (Bank Event Register §4); **four attach no identity at all** — CSV import, QIF import, OCR extraction, and manual keying. The identity system then fails **open** at all three enforcement points for a null identity:
- Python import filter: `$V18E/account_bank_statement_import/models/account_journal.py:262-264` — a missing or empty `unique_import_id` short-circuits to "accept".
- Python sync filter: `$V18E/account_online_synchronization/models/account_online.py:301` — a falsy identifier falls through the walrus guard unfiltered.
- The SQL UNIQUE index: PostgreSQL NULLs are not equal, so it constrains nothing.

**Additional vectors:**
- **CAMT degrades to a positional key.** `$V18E/account_bank_statement_import_camt/lib/camt.py:760-771` — when `AcctSvcrRef` is missing, all-zeros, or `NOTPROVIDED`, the identity becomes `'{}-{}-{}'.format(name, date, sequence)`. A re-import under a different statement name or row order yields a different identity.
- **`copy()` produces a line with both identity fields blank.** Both are `copy=False`; PATTERN `def copy|def copy_data` over the seven files declaring or inheriting `account.bank.statement.line` in `$V18E`: **0 hits**, so `copy()` falls through to the base ORM.
- **Cross-journal.** Because the import key embeds `journal.id`, the same real transaction imported into two journals produces two distinct keys and both are accepted.
- **The two keyspaces never intersect.** PATTERN `unique_import_id.*online_transaction_identifier` over `$V18E`: **NOT FOUND.** No code correlates a file-imported line with a sync-fetched one.

**Guard found:** one SQL UNIQUE (`$V18E/account_bank_statement_import/models/account_bank_statement.py:14-19`), covering only the 2 of 7 doors that populate it.
**Guard NOT FOUND:** any cross-channel dedup; any uniqueness on `online_transaction_identifier` (PATTERN `_sql_constraints` over `account_online_synchronization` and `account_bank_statement_extract`: **0 hits**); any dedup on copied or manually created lines; any dedup in base `account` (PATTERN `_sql_constraints` over `account/models/account_bank_statement_line.py`: **0 hits**).

**The post-hoc wizard is detection, not prevention**, and its existence is itself evidence: `$V18E/account_online_synchronization/models/account_journal.py:281-294` queries for **repeated `online_transaction_identifier`** — dead code if the Python filter were sufficient. The in-code comment at `:238-239` says the fuzzy heuristic exists precisely to catch what the identifier cannot.

**Accounting consequence.** The bank ledger is overstated by the duplicated amount. The duplicate can be independently reconciled, producing either a phantom settlement of a second obligation or a suspense residue. The statement footing will not necessarily reveal it, because the import silently adds a *skipped* duplicate's amount back into `balance_start` (`:266-269`) — the footing hides the suppression, and says nothing about an accepted duplicate.

**Classification: CONFIRMED DEFECT** for the copy, manual-keying, CSV, QIF, OCR and cross-journal vectors — each provable from quoted source. **PLAUSIBLE** for the import-then-sync collision, which depends on provider payload behaviour outside the codebase.
**Scope note (CORR1):** the identity is COMPANY-owned but enforced database-globally and filtered with **no company domain at all** (`:261-267`, a `sudo()` search). See SCOPE-F-09. Raised as `P06-B-29`.

---

## A2 — Same payment matched twice

**Precondition:** a posted payment whose outstanding line has non-zero residual.

**Mechanism.** Reconciliation is residual-driven, not "used-once"-driven. The guard is:
`$V18E/account/models/account_move_line.py:2326-2327` — `if any(aml.reconciled for aml in self): raise UserError(...)`, where `reconciled` is computed as *residual is zero* (`:778-780`).
**There is no uniqueness on the `(debit_move_id, credit_move_id)` pair** — PATTERN `_sql_constraints|unique(` over `account_partial_reconcile.py` and `account_full_reconcile.py`: **0 hits**. The same aml pair may carry N partials while residual remains.

Within a single transaction the allocation is correctly capped (`$V18E/account/models/account_move_line.py:2201-2204`). The exposure is **across concurrent transactions**: two bank-rec validations each read residual before the other commits.
**Guard NOT FOUND:** PATTERN `FOR UPDATE|select_for_update|_lock` over the reconcile region `account_move_line.py:2313-3090` and over `bank_rec_widget.py`: **0 hits.** No pessimistic row lock is taken before residual is read.

**Accounting consequence.** One payment allocated to two statement lines; the outstanding account driven negative; two obligations relieved by one cash receipt.

**Classification: PLAUSIBLE.** The single-transaction path is correctly guarded. The concurrent path has no lock visible in static evidence, but whether database isolation plus stored-field recompute serialises it is **NOT DECIDABLE FROM STATIC EVIDENCE**. Carried as `P06-OQ-24`.
**Note the corroborating design signal:** the online-sync importer defends its own concurrency with a bare `cr.commit()` and an in-code comment saying so (`$V18E/account_online_synchronization/models/account_online.py:830-831`). Concurrency in this domain is handled by commit placement, not by locking.

---

## A3 — Duplicate payment registration against the same invoice

**Precondition:** a user with payment rights and an invoice that is fully paid, partially paid, or still draft.

**Mechanism.** Duplicate detection exists and is **advisory at every call site.**
- `duplicate_payment_ids` is consumed in exactly two places, both non-blocking banners: `$V18E/account/views/account_payment_view.xml:165-167` and `$V18E/account/wizard/account_payment_register_views.xml:50-52`, each `class="alert alert-warning"`.
- PATTERN `raise UserError.*duplicate|raise ValidationError.*duplicate` over `account/models/account_payment.py` and `account/wizard/account_payment_register.py`: **0 hits.** `action_create_payments` (`:1267`) never reads the field.
- The in-flight guard is likewise inert: `$V18E/account/wizard/account_payment_register.py:566-577` builds `actionable_errors['unpaid_matched_payments']` with the text *"There are payments in progress. Make sure you don't pay twice."* — a `fields.Json` display field (`:162`) never consulted in `_create_payments` (`:1194-1258`).

**The match predicate is narrow and does not key on the invoice.**
`$V18E/account/models/account_payment.py:793-798` — partner, company, date, payment type, amount. **Changing the date by one day or splitting the amount defeats it entirely.**

**And one call site passes a state value absent from the v18 selection** *(Class A within the declared scope of `$V18E/account/models/account_payment.py:38-51`)*.
`$V18E/account/wizard/account_payment_register.py:889` — `matching_states=('draft', 'posted')`, while the v18 selection is `draft/in_process/paid/canceled/rejected` (`account_payment.py:38-51`). **The wizard's duplicate query can only ever match `draft` payments** — `in_process` duplicates, the dangerous ones, are invisible to it.

**Guard found:** a residual filter in `default_get` (`:940-952`) that skips zero-residual lines, and a `UserError` at `:951-952` — but **only when *no* selected line has residual.** A batch containing one open and one settled invoice proceeds silently on both.
Draft invoices are explicitly permitted (`:886-887`, `:1268-1269`).

**Accounting consequence.** A second payment against a settled invoice posts; with no residual to absorb it, it sits unreconciled in the outstanding account where a later bank line can absorb it — converting an over-collection into a silent write-off or an unexplained balance. On a draft invoice the payment posts before the receivable exists.

**Classification: CONFIRMED DEFECT.** The advisory-only nature is provable from the two view files plus the zero-hit grep; the non-existent state value is provable from two verbatim cross-file quotes.

---

## A4 — Cross-company bank misuse

**Precondition:** a multi-company database.

**Mechanism — three distinct vectors, now separated by scope per CORR1.**

**Vector 4a — sibling branch companies under one root.**
`$V18E/account/models/account_move_line.py:2336-2340` raises only when `len(self.company_id.root_id) > 1`. The bank-rec matching domain is widened to match: `$V18E/account/models/account_bank_statement_line.py:518` uses `child_of self.company_id.root_id.id`, and `:525` carries an in-code comment stating the widening is deliberate. `_action_validate` performs no independent company re-check — PATTERN `company_id` over `bank_rec_widget.py:1396-1470`: **0 hits**.
The payment-register wizard is root-scoped in the same way (`$V18E/account/wizard/account_payment_register.py:953-956`).
**Classification: HOLD — SCOPE EVIDENCE REQUIRED.** Whether this crosses a COMPANY boundary depends on whether companies sharing a `root_id` are branches of one legal entity or distinct legal entities — SCOPE-F-04, blocker `P06-B-27`. **This is a deliberate downgrade from the pre-correction reading, recorded as such.**

**Vector 4b — bank accounts with no company at all.**
`$V18E/base/models/res_bank.py:86` — `company_id` is an optional, derived, read-only related field. Three guards each explicitly admit `False`:
- `check_company_domain_parent_of` (ORM core `odoo/models.py:188-194`) admits `company_id = False` by contract;
- `$V18E/account/models/account_journal.py:469` — `if journal.bank_account_id.company_id and ...` skips the check when it is `False`;
- `$V18E/account/models/account_bank_statement_line.py:514` — `filtered(lambda x: x.company_id.id in (False, self.company_id.id))`.
The uniqueness constraint is partner-scoped, not company-scoped (`res_bank.py:89-93`).
**Classification: CONFIRMED DEFECT.** Under CORR1, an object whose ownership cannot be proven is a DENY condition; here an unowned bank account is admitted into every company by three independent paths. **Unaffected by the SCOPE-F-04 ambiguity** — this vector stands regardless of how `root_id` is read. Raised as `P06-B-26`.

**Vector 4c — payment tokens visible beyond their owner.**
`$V18E/payment/security/payment_security.xml:31-35` — the token rule is `[('company_id', 'parent_of', company_ids)]`, while the transaction rule directly above it is the narrower `[('company_id', 'in', company_ids)]` (`:14-18`). A stored payment instrument is visible to a wider scope than the transactions made with it. And for *validation* operations the token search widens further, to the commercial partner, ignoring provider availability (`$V18E/payment/models/payment_token.py:137-143`).
**Classification: CONFIRMED DEFECT** — availability exceeds ownership for a credential-bearing object (SCOPE-F-07). Raised as `P06-B-28`.

**Accounting consequence (4a and 4b).** One company's bank receipt relieves another's receivable with no intercompany account raised. Each standalone trial balance is misstated in opposite directions; consolidation eliminations will not balance.

---

## A5 — Reversal after reconciliation

**Precondition:** an invoice matched to a bank statement line; the invoice is then reversed or reset.

**Mechanism.** Two independent paths destroy the reconciliation silently:
- `$V18E/account/models/account_move.py:5283` (`button_draft`) — `self.mapped('line_ids').remove_move_reconcile()`
- `$V18E/account/models/account_move.py:4771-4775` (`_reverse_moves` with `cancel=True`)
and the primitive is a bare unlink (`$V18E/account/models/account_move_line.py:3078-3080`).
The reversal wizard reaches the second path (`$V18E/account/wizard/account_move_reversal.py:143`).

**Guard NOT FOUND:** PATTERN `statement_line_id|bank.statement` over `account_move.py:5274-5290` and `:4760-4803`: **0 hits.** Neither method knows it is invalidating a bank reconciliation, and neither re-opens or flags the statement line. **Class A within that declared scope.**

**Ordering defect.** In `button_draft`, the destructive call at `:5283` **precedes** the state write at `:5284` that triggers the lock check at `:3238-3241`. Within one transaction a raise still rolls back; any path reaching `:5283` without the subsequent state write is unprotected.

**Accounting consequence.** The statement line silently returns to unreconciled and its counterpart to suspense. A bank reconciliation signed off before the reversal is retroactively invalidated with no audit event tying the two.

**Classification: CONFIRMED DEFECT** — silent, via two independent paths, with the destructive call sequenced before the protective one.

---

## A6 — Correction after period close

**Precondition:** a closed (fiscalyear- or hard-locked) period containing reconciled items.

**Mechanism.** Lock-date enforcement attaches to `account.move` date/state/line mutations, **not to the reconciliation relation.**
**DENOMINATOR:** PATTERN `lock_date|_get_violated_lock_dates|_check_fiscal_lock_dates|_get_lock_date_violations`. PATH SET: the five files on the reconcile/unreconcile chain. UNIT: matching line.

| Path | hits |
|---|---|
| `account/models/account_move_line.py` | 12 |
| `account/models/account_partial_reconcile.py` | 2 |
| `account/models/account_full_reconcile.py` | **0** |
| `account/models/account_bank_statement_line.py` | **0** |
| `account_accountant/models/bank_rec_widget.py` | **0** |

And the two hits in `account_partial_reconcile.py` are **not gates** — they are at `:513-514`, choosing the *date* of a cash-basis reversal:
```
lock_date = move.company_id._get_user_fiscal_lock_date(journal)
move_date = partial.max_date if partial.max_date > lock_date else today
```
i.e. **the lock date is used to relocate the entry so the operation succeeds, not to refuse it.**

`action_undo_reconciliation` (`$V18E/account/models/account_bank_statement_line.py:475-490`) contains no lock check. An **indirect** check fires downstream because the `Command.clear()` unlinks amls and `$V18E/account/models/account_move_line.py:1700-1703` checks posted moves — **but `self.move_id` there is the statement line's own move.** The counterpart invoice, whose residual and payment status are being retroactively changed, is never date-checked.

A second unreconcile entry point is wholly unguarded: `$V18E/account/models/account_move_line.py:3082-3087` (`action_unreconcile_match_entries`, the list-view action).

**A named bypass sentinel exists:** `$V18E/account/models/account_move.py:83` — `BYPASS_LOCK_CHECK = object()`, honoured at `:2378`. Callers in `$V18E` excluding tests: **2**, both in `account/models/partner.py:804-805` (partner merge). **The SMEsPlus custom addon trees were not searched for it** — Class C, `P06-OQ-21`. This matters: the Account Wave A programme has already recorded one instance of a hard lock being defeated through a contacts-role partner merge.

Locking a period *is* guarded against leaving unreconciled statement lines (`$V18E/account/models/company.py:519-528`), but that is a one-time gate; nothing re-asserts it afterwards.

**Accounting consequence.** A closed period's ageing, payment status and cash-basis tax position can be altered after the books are locked and after returns are filed, without a lock-date error and without a reversing entry in an open period.

**Classification: CONFIRMED DEFECT.** Un-reconciling is not a lock-gated operation; the lock protects the move, not the relation, and the one incidental check that fires is scoped to the wrong move.

---

## A7 — Statement line deletion

**Precondition:** a user with delete rights on bank statement lines.

**Mechanism.** The whole override is eight lines — `$V18E/account/models/account_bank_statement_line.py:445-452`:
```
tracked_lines = self.filtered(lambda stl: stl.company_id.check_account_audit_trail)
tracked_lines.move_id.button_cancel()
moves_to_delete = (self - tracked_lines).move_id
res = super().unlink()
moves_to_delete.with_context(force_delete=True).unlink()
```
PATTERN `lock_date|is_reconciled|state ==|raise UserError` over those eight lines: **0 hits.**

**Three problems, all visible in that quote:**
1. **`force_delete=True` is a deliberate bypass** of the audit-trail and sequence-chain guards, which test exactly that key (`$V18E/account/models/account_move.py:3349-3357` and `:3338-3341`). For any company with `check_account_audit_trail` off, **a posted bank statement line and its journal entry are hard-deleted with no trace.**
2. **Asymmetric handling when the audit trail is ON.** `tracked_lines.move_id` is cancelled but excluded from `moves_to_delete`, while `super().unlink()` deletes the statement-line row for *all* of `self`. `move_id` is `ondelete='cascade'` (`:27`) — cascade runs move→line, not line→move. Result: **an orphaned cancelled journal entry pointing at a deleted statement line**, still occupying a sequence number.
3. **Enabling the audit trail converts a hard refusal into a silent unreconcile.** The untracked branch reaches `_check_reconciliation` via aml unlink and raises; the tracked branch goes `button_cancel()` → `button_draft()` → `remove_move_reconcile()` (`account_move.py:5283`) and destroys the match instead.

**Classification: CONFIRMED DEFECT** for problems 1 and 3, both provable from the quoted lines plus the guard definitions. **PLAUSIBLE** for problem 2 — the orphan was inferred from the `ondelete` direction plus the set arithmetic; confirming it requires the `_inherits` delete semantics in the ORM core, which were not read. Carried as `P06-OQ-40`.
**Scope note (CORR1):** the setting governing this is COMPANY-scoped and correctly so, but it must be a one-way, non-decreasable policy rather than a toggle — SCOPE-R-10.

---

## A8 — Audit trail and immutability

**The hash chain exists, and its scope excludes the settlement facts.**

Fields: `$V18E/account/models/account_move.py:317-319` (`restrict_mode_hash_table`, `secure_sequence_number`, `inalterable_hash`); journal switch at `$V18E/account/models/account_journal.py:123`, **a per-journal opt-in with no `default=True`.**

**What the hash covers** — `$V18E/account/models/account_move.py:3832-3842`:
```
if hash_version == 1: return ['date', 'journal_id', 'company_id']
elif hash_version in (2, 3, 4): return ['name', 'date', 'journal_id', 'company_id']
```
plus a subset of line fields.

**Coverage against the P06 objects:**
- **Bank statement lines: covered only indirectly**, through `_inherits` to `account.move`. PATTERN `inalterable_hash|secure_sequence|restrict_mode_hash_table` over `account/models/account_bank_statement_line.py`: **0 hits.** `amount`, `payment_ref`, `partner_id`, `account_number`, and **both identity fields** are not hashed.
- **Payments: covered only indirectly**, same mechanism. Same PATTERN over `account/models/account_payment.py`: **0 hits.** `amount`, `partner_id`, `payment_type` are not hashed.
- **Reconciliation relations: NOT COVERED.** Same PATTERN over `account_partial_reconcile.py` and `account_full_reconcile.py`: **0 hits each.**

**This is the finding that makes A5 and A6 exploitable even on a fully hashed journal:** `remove_move_reconcile()` writes nothing to any hashed field, so destroying and re-making a match does not perturb the chain, and the integrity report (`$V18E/account/models/company.py:922-963`) still verifies clean.

**Classification: CONFIRMED** that reconciliation objects are outside the hash scope and that statement-line and payment business fields are absent from the hashed set — all four greps returned zero over their declared path sets. **PLAUSIBLE** that this is exploitable in practice, since it depends on an operator treating `restrict_mode_hash_table` as the control.

---

## Attack summary

| ID | Attack | Classification |
|---|---|---|
| A1 | Duplicate imported bank transaction | **CONFIRMED DEFECT** (6 vectors) + PLAUSIBLE (1) |
| A2 | Same payment matched twice | PLAUSIBLE / NOT DECIDABLE (concurrency) |
| A3 | Duplicate payment registration | **CONFIRMED DEFECT** |
| A4a | Cross-company, sibling branches | **HOLD — SCOPE EVIDENCE REQUIRED** *(downgraded under CORR1)* |
| A4b | Cross-company, unowned bank account | **CONFIRMED DEFECT** |
| A4c | Payment token visible beyond owner | **CONFIRMED DEFECT** |
| A5 | Reversal after reconciliation | **CONFIRMED DEFECT** |
| A6 | Correction after period close | **CONFIRMED DEFECT** |
| A7 | Statement line deletion | **CONFIRMED DEFECT** (2 of 3 problems) + PLAUSIBLE (1) |
| A8 | Immutability scope | **CONFIRMED** gap + PLAUSIBLE exploitation |

**Counted: 7 CONFIRMED DEFECT classifications, 1 HOLD, 3 PLAUSIBLE/NOT DECIDABLE.**

## Open items

| ID | Item | Class |
|---|---|---|
| P06-OQ-24 | A2 concurrency requires a runtime test. | D |
| P06-OQ-21 | `BYPASS_LOCK_CHECK` not searched in the SMEsPlus custom trees. | C |
| P06-OQ-40 | A7 problem 2 (orphaned move) needs the ORM `_inherits` delete semantics. | C |
| P06-OQ-41 | A4 cross-*root* reachability: not every `_reconcile_plan` caller was enumerated, and direct `account.partial.reconcile.create()` callers were not searched. | C |
| P06-OQ-42 | A4b exposure is data-dependent — whether deployed partners actually carry `company_id = False`. The code path is confirmed; the exposure is not. | D |

---

# End
