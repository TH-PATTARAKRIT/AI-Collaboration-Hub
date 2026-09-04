# E00 — PRIMARY EVIDENCE BASE (LAYER 2 / AUDIT QUARANTINE)

Session: `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`
Wave: `WAVE A — CORE LEDGER & CLOSING`
Branch: `research/account-wave-a-core-2026-09-04-001`
Repository base commit: `8d2c8aa`
Date: 2026-09-04

> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.**
> This file contains `file:line -- method` citations to a reference ERP source tree.
> It is Boss / PMO / AI-Audit visible only. It must NOT be transcribed into any
> Layer 1 clean-room package, into Team B design input, or into any downstream
> reference package. The clean-room derivative of this file is
> `LAYER1_CLEANROOM/L1_SEMANTIC_TRANSFER_REGISTER.md`, which is vendor-token free.

## EV-000 — Evidence Source Registry

| Ref | Source | Location | Access |
|---|---|---|---|
| `SRC-A` | Reference ERP Enterprise source, v18 line, build 20250608 | `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account/` | Read, verified this session |
| `SRC-B` | Reference ERP reporting layer (same build) | `.../addons/account_reports/` | Read, verified this session |
| `SRC-C` | Reference ERP framework base models (same build) | `.../addons/base/models/` | Read, verified this session |
| `SRC-D` | Repository bootstrap layer | this clone, `99_SMEsPlus_Enterprise_Suite/` | Read, verified this session |

Module scale, `SRC-A` models directory: 30,127 lines across 49 model files; largest units
`account_move` (6,297), `account_move_line` (3,524), `account_tax` (2,923), `account_account` (1,597).

### Evidence-class legend (used throughout this package)

| Class | Meaning |
|---|---|
| `VERIFIED FACT` | Read directly from primary source this session; citation given |
| `REFERENCE BEHAVIOUR` | What the reference implementation does — not automatically a requirement |
| `INFERENCE` | Reasoned from verified facts; explicitly labelled, never promoted |
| `RECOMMENDATION` | Proposed SMEsPlus position; requires Boss decision |
| `UNKNOWN — EVIDENCE REQUIRED` | Cannot be decided from available evidence |

---

## EV-001 — Chart of Accounts: account identity is NOT the account code

**Class: VERIFIED FACT**

`account_account.py:50-52` — the account code is exposed as a computed field `code` backed by
a stored field `code_store` declared `company_dependent=True`. Company-dependent storage means
the value is held per company in a key/value column, not as a single scalar on the row.

`account_account.py:387-400` — `_compute_code` / `_inverse_code` read and write `code_store`
against `self.env.company.root_id`, i.e. the code resolved for a record depends on which company
the reader is acting for.

`account_account.py:106` — company linkage is `company_ids`, a many-to-many to companies, not a
single owning company.

`account_account.py:143-152` — `placeholder_code` falls back to "code in the first company the
account belongs to, suffixed with that company's name" when the active company has no mapping.

`account_code_mapping.py` (whole file) — a non-stored pseudo-model (`_auto = False`,
`_table_query = '0'`) exists purely to render the per-company code grid in the UI.

**Consequence.** In the reference implementation, one account record can legitimately carry a
different code in every company that uses it. The code is therefore a *per-company presentation
and ordering attribute*, not the account's identity. The record id is the identity.

**This independently corroborates the existing Boss-approved principle** that Account Code /
Account Name must not become the sole canonical identity. The reference system reached the same
conclusion and restructured its own storage to enforce it.

---

## EV-002 — Account code uniqueness has no database constraint

**Class: VERIFIED FACT**

`account_account.py:1037` — `_ensure_code_is_unique` is an application-level method invoked from
`create` (`:1012`) and from `write` (`:1033`). It performs two checks: that a code is set for every
company the account belongs to, and that no parent or child company already holds that code.

`account_account.py` contains **no `_sql_constraints` for the account model**. The only
`_sql_constraints` block in the file (`:1468`) belongs to the account *group* model and constrains
prefix length only.

**Consequence — control weakness.** Account code uniqueness is enforced only inside the
application transaction path. Two concurrent transactions, a bulk import that suppresses the check,
or any write path that sets the `defer_account_code_checks` context (`account_account.py:1015`,
`:1032`) can produce duplicate codes within one company with no database-level rejection.

`INFERENCE:` for SMEsPlus this is a candidate `Tolerance = 0` data-integrity control, because a
duplicated account code inside one company silently corrupts every code-ordered report and every
code-based mapping.

---

## EV-003 — Accounts have no archive state; only a `deprecated` flag

**Class: VERIFIED FACT**

`account_account.py:52` — `deprecated = fields.Boolean(default=False, tracking=True)`.

Searching the account model for an `active` field returns nothing. The account model therefore does
**not** participate in the framework's standard archive/`active` mechanism, unlike the journal model
which does (`account_journal.py:92` — `active = fields.Boolean(default=True, ...)`).

`account_account.py:1027` — the only guard on deprecation is that an account used in a tax
distribution cannot be deprecated. There is no guard on open balances, no guard on unreconciled
items, no guard on being a control account, and no guard on being referenced as a journal default.

**Consequence.** "Active / UnActive / Archived" is a three-state expectation in the Boss scope, but
the reference model supplies only a two-state boolean, and that boolean does not prevent the
account from continuing to hold balances or from being selected by automated postings that
reference it by configuration rather than by user choice.

`UNKNOWN — EVIDENCE REQUIRED:` whether any reference behaviour blocks *posting* to a deprecated
account. The `deprecated` flag appears in selection domains (e.g. `company.py:110` transfer account
domain, `account_move_line.py:777` filter) but a domain filters pickers, it does not constrain
programmatic posting. Not decidable from the evidence read this session.

---

## EV-004 — Account merge rewrites posted history and deletes account records

**Class: VERIFIED FACT**

`wizard/account_merge_wizard.py:134-141` — `_action_merge` docstring, verbatim intent: the first
account is extended to each company of the others keeping their codes and names; **the others are
deleted**; and journal items and other references are **retargeted to the first account**.

`wizard/account_merge_wizard.py:112` — the surviving account is chosen by sorting on
`account_has_hashed_entries` descending, "to ensure that if one account in the group has hashed
entries, it appears first, ensuring that its ID doesn't get changed by the merge."

**Consequence.** Merging accounts is a destructive history rewrite. After a merge, a journal item
posted years earlier reports the *surviving* account, and the account it was actually posted to no
longer exists as a record. Historical reporting continuity is preserved only in the sense that
balances still add up; provenance ("which account did this posting actually name at the time")
is lost.

The hash-ordering trick shows the reference authors were aware of exactly this: they protect the
integrity hash by preserving the id of the hashed account, because the account id is a hashed field
on the line (see EV-010). Where hashing is off, no such protection applies.

---

## EV-005 — Journal numbering is derived from data, not from a sequence object

**Class: VERIFIED FACT**

`sequence_mixin.py:267-309` — `_get_last_sequence` obtains the previous number by executing a
`SELECT <sequence field> ... ORDER BY sequence_number DESC LIMIT 1` against the model's own table,
restricted to the prefix of the most recently created record. There is no counter table and no
database sequence object.

`sequence_mixin.py:31-45` — the number is decomposed by regular expression into
prefix / year / month / sequence / suffix groups. `account_journal.py:147` exposes
`sequence_override_regex` so a journal can override that parsing.

`sequence_mixin.py:270-278` — documented consequence, verbatim intent: the next number is the
greatest *alphabetical* value in the domain, so renaming a record's prefix mid-period does not
re-base the sequence.

**Consequence.** Sequence integrity is a property of the stored data, not of a protected counter.
Any operation that changes the name of the highest record changes what the next number will be.

---

## EV-006 — Numbering uniqueness is guaranteed only for posted entries

**Class: VERIFIED FACT**

`account_move.py:730-735` — a **partial** unique index is created:
`account_move_unique_name ON account_move(name, journal_id) WHERE (state = 'posted' AND name != '/')`.

`sequence_mixin.py:352-368` — `_locked_increment` docstring states that the lock is taken by
updating a row covered by that unique constraint, acquiring an exclusive lock on the B-tree index
entry, and — verbatim intent — that at entry the record must already be governed by the unique
constraint (for a move, it must be posted), **otherwise the lock is not taken and sequence numbers
may not be unique when returned**.

**Consequence.** Draft entries can hold duplicate numbers. Uniqueness is asserted at the moment of
posting, per (name, journal). Uniqueness is *not* scoped by company in the index itself; it is
company-scoped only transitively, because a journal belongs to exactly one company
(`account_journal.py:132`).

---

## EV-007 — A configuration parameter can globally disable the date/number alignment control

**Class: VERIFIED FACT**

`sequence_mixin.py:154-179` — `_constrains_date_sequence` refuses a record whose date does not
match the year/month encoded in its number. The constraint is skipped entirely for any record whose
date is on or before the value of the configuration parameter
`sequence.mixin.constraint_start_date`, which defaults to `1970-01-01`.

The code comment attached to it states, verbatim intent, that the bypass exists to allow editing
already-inconsistent documents and must not be used to disable the constraint completely, as that
would make the mechanism unreliable.

**Consequence — SaaS control finding.** A single tenant-writable configuration value moves the
date on which a core numbering control begins to apply. Setting it to a future date disables the
control for the whole tenant, silently, with no accounting-level trace.

---

## EV-008 — Five lock dates, four soft and one hard

**Class: VERIFIED FACT**

`company.py:54-63` — the lock model is declared as two lists: soft locks
(`fiscalyear_lock_date`, `tax_lock_date`, `sale_lock_date`, `purchase_lock_date`) and the full set,
which adds `hard_lock_date`.

`company.py:73-99` — field declarations. The help text of each soft lock states, verbatim intent,
that any entry up to and including that date **will be postponed to a later time in accordance with
the journal's sequence** — not that it will be rejected. `hard_lock_date` help adds that it is
irreversible and allows no exception.

`company.py:492-500` — write guard on `hard_lock_date`: it cannot be removed once set, and a new
value must be on or after the previous value.

`company.py:501-517` — setting `hard_lock_date` is refused while draft entries exist on or before
that date; setting any fiscal-effective lock is refused while unreconciled bank statement lines
exist in the period.

`company.py:396-401` — a company's effective hard lock is the `max()` of the hard lock of every
company in its parent chain; a parent's hard lock therefore cascades to subsidiaries.

`company.py:565-577` — `_get_user_fiscal_lock_date(journal)` composes the effective lock for a
posting as `max(fiscal-year lock, hard lock)`, raised further to the sale lock for sale journals or
the purchase lock for purchase journals.

---

## EV-009 — The lock date re-dates entries; it does not reject them

**Class: VERIFIED FACT**

`account_move.py:3127-3129`:

- the effective user fiscal lock date is resolved for the move's journal;
- if the intended date is on or before that lock date, the values dictionary is **rewritten** so
  that `date = lock_date + 1 day`.

`account_move.py:5702-5712` — the user-facing message confirms the semantic, verbatim intent: the
date is prior to the stated lock, and the journal entry **will be accounted on** the shifted date
upon posting.

`account_move.py:4936` — at posting, `_post` re-resolves the accounting date the same way.

**Consequence — this is the single most load-bearing semantic in section F.** A late or backdated
source document is not refused. Its *accounting date* is silently moved forward into the first open
period, while its *document date* is unchanged. The ledger and the document therefore legitimately
disagree on date, by design.

`INFERENCE:` for a Thai filing context this behaviour must be examined against VAT and WHT period
attribution before it is adopted, because it changes which statutory period a late document lands
in. Raised as a Wave D carry-forward, not decided here.

---

## EV-010 — What the inalterability hash actually covers

**Class: VERIFIED FACT**

`account_move.py:3832-3839` — `_get_integrity_hash_fields` for the entry returns, at the current
hash version (`MAX_HASH_VERSION = 4`, `account_move.py:46`):
`['name', 'date', 'journal_id', 'company_id']`.

`account_move_line.py:3283-3290` — for the item it returns:
`['name', 'debit', 'credit', 'account_id', 'partner_id']`.

`account_move.py:3990-4022` — `_calculate_hashes` builds a dictionary of exactly those move fields
plus, per line, keys of the form `line_<line id>_<field>`, serialises it deterministically, and
chains `sha256(previous_hash + current_record)`. From version 3 onward monetary values are
serialised through a fixed-decimal representation; from version 4 the stored value is prefixed
`$<version>$`.

**Fields that are NOT covered by the hash**, and are therefore neither blocked on write nor
detected by the integrity report:

| Not hashed | Why it matters |
|---|---|
| `amount_currency` | the foreign-currency amount of the item |
| `currency_id` | the item's transaction currency |
| tax fields (`tax_ids`, tax repartition, tax tags) | the tax dimension of the posting |
| `analytic_distribution` | the analytic dimension of the posting |
| `date_maturity` | the due date driving ageing |
| entry-level `partner_id`, `ref`, `narration` | counterparty and reference metadata |

`account_move.py:3202-3214` and `account_move_line.py:1554-1563` — the write guards raise only for
fields inside those same hash lists.

**Consequence — headline contradiction.** On a hashed, "secured" entry, the foreign-currency amount
can be changed after the fact: the write guard permits it because `amount_currency` is not a hashed
field, and the integrity report cannot detect it because the recomputed hash does not include it.
For a single-currency ledger the hash is sound; for a multi-currency ledger it does not secure the
transaction-currency amount. Recorded in the contradiction register as `CONTRA-01`.

---

## EV-011 — Immutability is opt-in at two independent levels

**Class: VERIFIED FACT**

Level one — hashing. `account_journal.py:123-124` — `restrict_mode_hash_table` is a per-journal
boolean, default off. `account_journal.py:651-658` — once entries in that journal are hashed the
flag cannot be switched off. `account_move.py:3871-3882` — hashing runs on post for journals in
restrict mode, and can also be run on demand (`wizard/account_secure_entries_wizard.py`), which
also grants the "secured" group.

Level two — deletion protection. `company.py` exposes `check_account_audit_trail` as a company
boolean. `account_move.py:3352-3358` — when it is on, an entry that has ever been posted cannot be
deleted; the user is told to cancel instead. `account_move.py:3311` and `:3330-3345` — when the
`force_delete` context is present the block is bypassed and the deletion is recorded by writing a
formatted message through the **application logger**, not to a database audit record.

`account_move.py:4805-4809` — `_can_be_unlinked` composes all three conditions: not hashed, dated
after the effective fiscal lock, and not protected by the audit trail.

**Consequence.** Neither immutability nor deletion protection is a property of the ledger. Both are
configuration. With both switches off — the shipped default for hashing — a posted entry is an
ordinary mutable, deletable row. Where the deletion bypass is used, the only surviving evidence
leaves the tenant database entirely.

---

## EV-012 — Resetting to draft destroys reconciliation and analytic records

**Class: VERIFIED FACT**

`account_move.py:5274-5286` — `button_draft`, in order: refuses non-posted/non-cancelled entries;
refuses entries needing a cancellation request; runs `_check_draftable`; then
**unlinks every analytic line** of every item (`line_ids.analytic_line_ids.unlink()`);
then **removes every reconciliation** on those items (`remove_move_reconcile()`);
then sets state to draft and detaches generated document attachments.

`account_move.py:5317-5354` — `_check_draftable` refuses only three categories: exchange-difference
entries, tax cash-basis entries, and hashed entries.

`account_move.py:3239-3242` — separately, `write` calls the fiscal-lock check when the state moves
away from posted, so un-posting inside a locked period is refused by that path.

**Consequence.** Un-posting is not a state toggle. It is a destructive operation on two subledgers:
the analytic subledger is deleted and regenerated, and the matching state is discarded. Analytic
lines are therefore derived artefacts with no independent history, and reconciliation history does
not survive an un-post.

---

## EV-013 — Debit and credit are derived; balance is the stored fact

**Class: VERIFIED FACT**

`account_move_line.py:113-128` — `debit` and `credit` are computed with
`compute='_compute_debit_credit'`, stored, with inverse setters. `balance` is computed, **stored,
and `readonly=False`**, i.e. directly writable, and is the field carrying `tracking=True`.

`account_move_line.py:139-147` — `amount_currency` is stored and writable; `currency_id` is stored,
writable and **required**, so every item always carries a transaction currency even when it equals
the company currency.

**Consequence.** The reference model treats the signed company-currency `balance` as the primary
posted amount, and the debit/credit pair as a presentation split of it. Two amounts coexist on
every item — company-currency `balance` and transaction-currency `amount_currency` — with the
currency always explicit.

---

## EV-014 — Reconciliation is simultaneously a record, a state and an event

**Class: VERIFIED FACT**

Record. `account_partial_reconcile.py:14-62` — a partial reconciliation is a first-class stored
record linking exactly one debit item and one credit item, carrying three amounts (company currency,
debit-side transaction currency, credit-side transaction currency) and a stored `max_date` used to
place the match on ageing reports.

`account_full_reconcile.py:9-11` — a full reconciliation aggregates partials and the items they
touch, and owns an `exchange_move_id`.

State. `account_move_line.py:244-283` — `amount_residual`, `amount_residual_currency` and
`reconciled` are **stored computed** fields recomputed from the partials; `matching_number` is an
indexed text marker, `'P'` while only partially matched, otherwise the name of the full
reconciliation.

Event. `account_full_reconcile.py:13-35` — un-linking a full reconciliation **reverses the exchange
difference entry** it created, by posting reversal entries. `account_partial_reconcile.py:495-530`
— reconciling can generate tax cash-basis entries, i.e. new journal entries.

**Consequence — direct answer to the Boss question.** Reconciliation is not one thing. It is a
stored matching record, from which a derived settlement state is computed, and which *conditionally
emits accounting events* (exchange differences, cash-basis tax). Unreconciling is likewise not an
undo: it emits further accounting events. Any SMEsPlus model that treats reconciliation as a pure
state flag will be wrong in exactly the multi-currency and cash-basis-tax cases.

---

## EV-015 — Generated entries silently relocate to today when their period is locked

**Class: VERIFIED FACT**

`account_partial_reconcile.py:512-514` — when building a tax cash-basis entry, the date chosen is
the reconciliation's `max_date` **if that date is after the effective fiscal lock, otherwise
today**.

`account_full_reconcile.py:29-33` — reversals of exchange entries are dated through
`_get_accounting_date`, which applies the same lock-shift as EV-009.

**Consequence.** A machine-generated accounting consequence of a past event can be booked into the
current period — potentially a different fiscal year — purely because its natural period is closed.
The link to its origin is preserved by `tax_cash_basis_origin_move_id`, but the period attribution
is not.

---

## EV-016 — There is no fiscal year entity and no year-end closing entry

**Class: VERIFIED FACT**

A search for a fiscal-year model definition across the entire 797-module reference tree returns
**no result**. The fiscal year exists only as two integers on the company:
`company.py:71-72` — `fiscalyear_last_day` (default 31) and `fiscalyear_last_month` (default 12),
with `company.py:1021` — `compute_fiscalyear_dates(current_date)` deriving a period on demand.

`company.py:300-315` — a constraint rejects a 29 February year end because the intent for
non-leap years cannot be inferred.

The profit-and-loss to equity transfer is **not** a posted entry. `account_account.py:66` declares
the account type `equity_unaffected` ("Current Year Earnings"), and
`account_account.py:33-42` enforces at most one such account per company.
`account_reports/models/account_general_ledger.py:199-223, 314-343` computes the current-year
result **at report time** and attributes it to that account for presentation.

The only entity called a "closing entry" in the reference tree is the **tax** closing entry
(`account_reports/models/account_move.py:74-118`), which posts a VAT return, sets the tax lock date,
and carries its own reset-to-draft restrictions — an unrelated concept.

**Consequence — direct answer to Boss section G.** In the reference model there is no year-close
event, no carry-forward posting, and no reopening operation, because there is nothing to reopen: a
period is "closed" exactly to the extent that a lock date covers it, and lock dates are ordinary
dates that can be moved (except the hard lock, which can only move forward).

**This is consistent with the Boss baseline** that close is monthly and that month 12 is still a
month close. The reference evidence goes further: it shows a design in which the year boundary is
purely a reporting construct. Retained-earnings handling is therefore *entirely* an SMEsPlus design
decision, with no reference implementation to adapt. Recorded as a decision requiring Boss input.

---

## EV-017 — Opening balances are an ordinary posted entry

**Class: VERIFIED FACT**

`company.py:172-173` — the company holds `account_opening_move_id`, a link to a normal journal
entry, and its journal.

`company.py:738` — "accounting is initialised" is defined as: that entry exists and is posted.

`company.py:829` and `:857` — the opening entry is created as a normal entry and is **balanced
against the current-year-earnings account** (`get_unaffected_earnings_account()`, `company.py:740-766`,
which creates the account on demand if absent).

`account_account.py:126-131` — `opening_debit` / `opening_credit` / `opening_balance` are computed
fields on the account with inverse setters that write into that single entry.

**Consequence.** Opening balances are journal entries, with all the properties of journal entries —
they can be un-posted, edited, and are subject to the same lock and hash rules. Provenance of a
migrated opening balance (which legacy system, which extraction, which reconciliation state) has no
carrier in this model. Recorded as a Level 10 requirement.

---

## EV-018 — Currency rates are one scalar per day per currency per company root

**Class: VERIFIED FACT**

`base/models/res_currency.py:336-371` — the rate model is keyed by `name` (a Date), `currency_id`
and `company_id` (defaulting to the acting company's **root**), with database constraints
`unique (name, currency_id, company_id)` and `CHECK (rate > 0)`.

The stored `rate` is the technical rate; `company_rate` and `inverse_company_rate` are computed
presentations of it.

**Consequence.** The reference model supports exactly one rate per currency per day per company
group. There is no rate *type* dimension — no separate spot, average, closing or historical rate,
and no intraday rate. Any requirement for a closing rate distinct from the transaction-date rate,
or for historical rates on non-monetary items, has no carrier in this structure.

`UNKNOWN — EVIDENCE REQUIRED:` whether the reference reporting layer synthesises an average rate for
presentation. Not examined this session; deferred to Wave G.

---

## EV-019 — Bank and cash accounts cannot be shared between companies

**Class: VERIFIED FACT**

`account_account.py:301-302` — a validation refuses any account of type `asset_cash` that belongs to
more than one company.

`account_account.py:303-309` — a company cannot be detached from an account while journal items of
that company reference it.

`company.py:508-517` — a lock cannot be set while unreconciled bank statement lines remain in the
period being locked.

**Consequence.** Liquidity accounts are the one part of the chart the reference model refuses to
share across the company boundary, and bank reconciliation completeness is treated as a
precondition of period locking rather than as a reporting nicety.

---

## EV-020 — A hard numeric ceiling in the per-company code UI

**Class: VERIFIED FACT**

`account_code_mapping.py:4` — `COMPANY_OFFSET = 10000`.
`account_code_mapping.py:34-42` and `:47-56` — the pseudo-model addresses each row by the arithmetic
identifier `account_id * 10000 + company_id`, and decodes it with integer division and modulo
(`:58-64`).

**Consequence — SaaS boundary finding.** The encoding is only reversible while `company_id < 10000`.
The moment a deployment holds ten thousand or more company records, the encoding aliases: a
different (account, company) pair decodes to the same identifier, and the per-company code grid
shows or writes the wrong company's code. This is a UI-layer construct, so it does not corrupt
posted data, but it fails silently rather than raising.

For a multi-tenant SaaS whose company records accumulate across all tenants in one database, ten
thousand is not a large number. Recorded as `CONTRA-02`.

---

## EV-021 — Lock exceptions: who can grant them, and for how long

**Class: VERIFIED FACT**

`account_lock_exception.py:13-97` — an exception record names one soft lock field, the date it is
relaxed to, the original company lock date at the time of creation, an optional user, an optional
end date-time, and an **optional** free-text reason.

`account_lock_exception.py:36-40` — an exception with no user applies to **every** user.
`account_lock_exception.py:45-47` — an exception with no end date-time is, verbatim intent, valid
forever.

`company.py:589-596` and `:578-588` — resolution: for a given user and lock field, an active
exception relaxing that field lowers the effective lock date; `ignore_exceptions` recovers the
underlying company value.

Access control, `security/ir.model.access.csv:18-19` — all internal users may read exceptions;
the accounting-manager group may **read and create** them, but not write and not delete
(create/write/delete permissions are `1,0,1,0` and `1,0,0,0` respectively across the two rows).

`account_lock_exception.py:210-225` — creation is written to the company's message thread with a
tracking value showing the lock date change.

**Consequence.** The override control is well shaped in one respect — exceptions are append-only and
logged. It is weak in two: the justification is optional, and a single accounting manager can create
an exception that applies to **all users** with **no expiry**, which is a permanent global unlock
wearing the vocabulary of a temporary one.

---

## EV-022 — What a posted entry still permits

**Class: VERIFIED FACT**

`account_move.py:3247-3252` — on a posted entry the following are refused:
`invoice_line_ids`, `line_ids`, `invoice_date`, `date`, `partner_id`, `invoice_payment_term_id`,
`currency_id`, `fiscal_position_id`, `invoice_cash_rounding_id`.
The guard is skipped when the `skip_readonly_check` context is set.

`account_move.py:3231-3237` — the fiscal lock is consulted only when `name` or `date` changes on a
posted entry, and when the state leaves posted.

Fields **not** in the refusal list, and therefore writable on a posted entry, include `ref`,
`narration`, `journal_id` (subject to its own sequence guards at `:3215-3227`), and the
reconciliation and matching fields which are maintained by their own mechanisms.

**Consequence.** "Posted" freezes the accounting substance — the lines, the amounts, the date, the
counterparty — but not the descriptive metadata, and the freeze is a Python guard with a documented
context bypass rather than a storage-level property.

---

## EV-023 — Bootstrap layer verification

**Class: VERIFIED FACT**

Of the five bootstrap documents named in the execution authorisation, this clone at commit `8d2c8aa`
contains:

| Required | Present | Path |
|---|---|---|
| `PROJECT_CONSTITUTION.md` | yes | `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/PROJECT_CONSTITUTION.md` (v1.4, Approved, revision effective 2026-08-30) |
| `CHANGELOG.md` | yes | `99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/CHANGELOG.md` |
| `MASTER_INDEX.md` | no file of that name | nearest: `.../TEAM_A/SYSTEM_RESEARCH_MASTER_INDEX.md` |
| `PROJECT_SYSTEM_REGISTRY.md` | no file of that name | not located in this clone |
| `CURRENT_STATE.md` | no file of that name | nearest: domain-specific current-state reconciliation files under `BOSS_GATE/` and `TEAM_B_DESIGN/` |

Constitution provisions directly binding on this session: Repository is the single source of truth;
No Evidence = No Progress; No Gate Approval = No Move Forward; Boss holds final approval authority;
independent reviewers must not review their own work (principle 7); module-level approval does not prove
system readiness (principle 10); critical integrity, financial and tenant-isolation failures may be
designated `Tolerance = 0` (principle 13).

`INFERENCE:` the three absent filenames are naming drift rather than missing governance — equivalent
content exists under domain-specific names. Recorded in the evidence-gap register as `GAP-B01`,
non-blocking for Wave A because the constitution itself was read and applied.
