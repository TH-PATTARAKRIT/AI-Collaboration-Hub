> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.**
> This review carries `file:line -- method` citations into a reference ERP source tree.
> Boss / PMO / AI-Audit visible only. Must NOT be transcribed into any Layer 1 clean-room package,
> into Team B design input, or into any downstream reference package. Its clean-room derivatives are
> the numbered files in the package root, which cite `EV-0NN` / `COR-0N` identifiers only.

# X2 — EXPERT 2 REVIEW: LEADERSHIP DATABASE DESIGN

Session: `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`
Wave: `WAVE A — CORE LEDGER & CLOSING`
Reviewer: Expert 2 — Leadership Database Design (independent)
Date: 2026-09-04

> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.**
> This review cites a reference ERP source tree by `file:line`. It is Boss / PMO / AI-Audit
> visible only and must not be transcribed into any Layer 1 clean-room package or into
> Team B design input. Clean-room derivation rule applies: SMEsPlus requirements below are
> derived from *business semantics*, never from the reference schema or ORM architecture.

## Scope and method

Lens: financial fact modelling; canonical identity; relationships; lifecycle; temporal model;
referential and transactional integrity; reconciliation data model. Out of lens and not
addressed here: UI, security/RBAC, reporting presentation, tax computation, performance tuning.

Method: I read `E00_PRIMARY_EVIDENCE_BASE.md` first, then independently re-derived every
finding below from the primary source at
`/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/` (read-only).
Twelve distinct claims were verified against primary source this session, exceeding the
six-claim floor. Every `EVIDENCE` citation below is one I personally opened this session.
Nothing under `/Volumes/iMacSys/CLAUDE AI/` was modified.

Evidence classes used: `VERIFIED FACT`, `REFERENCE BEHAVIOUR`, `INFERENCE`,
`RECOMMENDATION`, `UNKNOWN — EVIDENCE REQUIRED`.
Verdict vocabulary used: `CONFIRMED`, `CONFIRMED WITH CAVEAT`, `CONTRADICTED`, `UNKNOWN`,
`HOLD`, `VETO`.

Findings 4, 6 and 9 disagree with or materially qualify the evidence base.

---

## FINDING X2-01 — Account code uniqueness is not merely unconstrained; the chosen storage form forecloses a database constraint

**Verdict: CONFIRMED WITH CAVEAT** (EV-002 is correct but understates the cause)

### OBSERVATION

`VERIFIED FACT` — EV-002 reports that account code uniqueness has no database constraint and
is enforced only by the application method `_ensure_code_is_unique`. That is accurate. The
deeper structural fact, which EV-002 does not state, is *why* no constraint exists: the code
is not stored in a scalar column at all. It is stored in a `jsonb` column keyed by company id.
A conventional `UNIQUE (company_id, code)` index is therefore not merely absent — it is not
expressible against this storage form without a functional index per company, which cannot be
declared statically because the company set is data.

`VERIFIED FACT` — the application check is a read-then-write pattern with no lock. It resolves
duplicates with `search_fetch(...)`, an ordinary SELECT. Under PostgreSQL READ COMMITTED, two
concurrent transactions each inserting account code `1100` for the same company both execute
their SELECT before either COMMIT, both observe no duplicate, and both commit. No database
object rejects the second.

`VERIFIED FACT` — a documented context flag `defer_account_code_checks` suppresses the check
entirely on both the create and the write path. The create path sets it unconditionally on the
inner `super().create(...)` call and re-runs the check once afterwards on the union of created
records; the write path sets it and re-runs only when the vals touch `company_ids`, `code` or
`code_mapping_ids`.

`INFERENCE` — three concrete failure modes follow, in ascending order of likelihood:
(a) *concurrency* — two simultaneous account creations in one company, e.g. two users, or one
user and one background integration, produce a duplicate code with no rejection;
(b) *bulk import* — a loader that enters through the deferring path and does not re-invoke the
check on the full set imports duplicates silently; the check is only as good as the caller's
discipline in re-running it over the right recordset;
(c) *concurrent merge and create* — the merge wizard writes codes at the end of its run
explicitly to avoid the duplicate-code constraint, so a create landing in that window is
checked against a transient intermediate state.

`INFERENCE` — the corruption is silent and downstream-only. A duplicated code inside one
company does not fail any posting. It surfaces later as a code-ordered report showing two rows
under one code, or as a code-keyed mapping (chart import, statutory report line mapping,
consolidation mapping) that binds to whichever row it happened to match.

### EVIDENCE

- `account/models/account_account.py:50` — `code = fields.Char(... compute='_compute_code', search='_search_code', inverse='_inverse_code')`; `:51` — `code_store = fields.Char(company_dependent=True)`.
- `odoo/fields.py:774` — `return ('jsonb', 'jsonb') if self.company_dependent or self.translate else self._column_type` — a company-dependent field's SQL column type is `jsonb`.
- `odoo/fields.py:180` — docstring, verbatim intent: the value is stored on the model table as a jsonb dict keyed by company id.
- `account/models/account_account.py:1468` — the sole `_sql_constraints` block in the file; it belongs to the account *group* model and constrains prefix length only. No `_sql_constraints` on the account model itself.
- `account/models/account_account.py:1074-1084` — Check 2.2 is `self.with_company(company).sudo().search_fetch([...], ['code_store'])`, an unlocked read.
- `account/models/account_account.py:1004` — `defer_account_code_checks=True` supplied to the inner create; `:1012` — `records._ensure_code_is_unique()` re-run afterwards.
- `account/models/account_account.py:1030` — `super(AccountAccount, self.with_context(defer_account_code_checks=True)).write(vals)`; `:1032` — re-check only `if not self.env.context.get('defer_account_code_checks') and {'company_ids','code','code_mapping_ids'} & vals.keys()`.
- `account/models/account_account.py:108-110` — comment, verbatim intent: `code_mapping_ids.write_sequence = 19` exists so that code mappings are written before `company_ids`, specifically to avoid triggering `_ensure_code_is_unique` mid-write.

### CONTRADICTION

The evidence base frames this as "no database constraint was declared". My reading is that the
absence is a *consequence* of a prior modelling decision — making the code company-dependent —
and that the reference authors accepted an unenforceable uniqueness rule as the price of
per-company codes. That is a materially different finding for SMEsPlus, because it means
"just add a unique index" is not an available remedy if SMEsPlus adopts per-company codes in
the same storage shape. The remedy has to be a different storage shape.

`INFERENCE` — I also disagree with any reading that the deferred-check flag is the primary
risk. The flag is a visible, greppable, reviewable bypass. The unlocked `search_fetch` is the
larger exposure because it fails with no bypass invoked, under ordinary correct usage, purely
as a function of concurrency.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED` — whether any reference deployment tooling adds a database-level
uniqueness guarantee outside the module source (a migration script, a DBA-applied index, a
SaaS-platform constraint). Not found in `addons/account/` this session; I did not search
deployment or migration trees, which are outside `SRC-A`/`SRC-B`/`SRC-C`.

`UNKNOWN — EVIDENCE REQUIRED` — the actual isolation level used at runtime. If a deployment
ran SERIALIZABLE, failure mode (a) would be reduced to a serialization error rather than a
duplicate. Not determinable from the model source read this session.

### RECOMMENDATION

`RECOMMENDATION` — Boss decision required, not an approval.

1. SMEsPlus should treat "account code is unique within a company at a point in time" as a
   `Tolerance = 0` integrity rule under Constitution principle 13, and require it to be
   enforced by a database object, not by application code.
2. To make that enforceable, SMEsPlus should model the per-company code as a **row**, not as a
   per-company value inside the account row: an account-code assignment entity keyed
   `(company, code)` with a unique constraint, referencing the account. This is a clean-room
   requirement derived from the business semantics — "a company's chart assigns exactly one
   code to one account" is a relationship, and relationships are rows — not a copy of the
   reference structure, which does the opposite.
3. Any bulk-import path must acquire the same constraint, not a deferred variant of it. If
   import performance requires deferral, use a deferred *database* constraint that still fires
   at COMMIT, so the transaction fails rather than the data drifting.

---

## FINDING X2-02 — `balance` is the canonical amount and debit/credit are presentation; entry balance is enforced only in Python and is switchable off

**Verdict: CONFIRMED** on EV-013; **new material finding** on entry-level balance enforcement

### OBSERVATION

`VERIFIED FACT` — EV-013 is correct and I can strengthen it. `balance` is not merely writable;
it is the field the system *rewrites every input into*. A write of `{'debit': X}` or
`{'credit': Y}` is collapsed by `_sanitize_vals` into `{'balance': X - Y}` before it reaches
storage, and if `balance` is present alongside debit/credit, the debit and credit keys are
discarded outright. The debit/credit pair is therefore a derived, stored projection with an
inverse setter for convenience; the signed company-currency `balance` is the single canonical
posted amount.

`VERIFIED FACT` — on the question the task poses directly: **there is no database constraint
enforcing that an entry's debits equal its credits.** I went looking for one and it is not
there. What exists is a Python context manager, `_check_balanced`, wrapped around `create` and
`write`, which after the fact runs an aggregate SQL query and raises a `UserError` if any move
in the container has a non-zero rounded sum. It is a check, not a constraint.

`VERIFIED FACT` — that check is explicitly switchable off. It opens with
`self._disable_recursion(container, 'check_move_validity', default=True, target=False)`, which
means a caller that sets `check_move_validity` falsely in the environment context causes the
generator to return before the query runs. The move is then created or written unbalanced with
nothing rejecting it.

`VERIFIED FACT` — by contrast, real database `CHECK` constraints *do* exist at the **line**
level: a line may not carry both a debit and a credit; the transaction-currency amount must
carry the same sign as the balance; an accountable line must have an account; a
section/note line must carry no amounts and no account.

`INFERENCE` — the reference model's integrity guarantees are therefore split across two tiers
with a gap in the middle. Intra-line coherence is database-enforced. Intra-entry balance —
the single defining property of double-entry bookkeeping — is application-enforced and
bypassable. That is the inverse of the priority a ledger designer would choose.

### EVIDENCE

- `account/models/account_move_line.py:123-128` — `balance = fields.Monetary(compute='_compute_balance', store=True, readonly=False, precompute=True, currency_field='company_currency_id', tracking=True)`; writable and the tracked field.
- `account/models/account_move_line.py:113-122` — `debit` and `credit` both `compute='_compute_debit_credit', store=True` with inverse setters.
- `account/models/account_move_line.py:1434-1441` — `_sanitize_vals`: if `debit` or `credit` in vals, then if `balance` also present both are popped, else `vals['balance'] = vals.pop('debit', 0) - vals.pop('credit', 0)`.
- `account/models/account_move_line.py:429-459` — `_sql_constraints`: `check_credit_debit` = `CHECK(display_type IN ('line_section','line_note') OR credit * debit=0)`; `check_amount_currency_balance_sign`; `check_accountable_required_fields`; `check_non_accountable_fields_null`. These are genuine database CHECK constraints.
- `account/models/account_move.py:713-715` — the move model's `_sql_constraints` contains exactly one entry, `('unique_name', "", "Another entry with the same name already exists.")`, whose SQL definition string is **empty**. No balance constraint is declared here or anywhere else in the move model.
- `account/models/account_move.py:2330-2338` — `_check_balanced` opens with `with self._disable_recursion(container, 'check_move_validity', default=True, target=False) as disabled:` then `yield`, then `if disabled: return`.
- `account/models/account_move.py:2364-2375` — the balance test is an application-issued `SELECT ... GROUP BY line.move_id ... HAVING ROUND(SUM(line.balance), currency.decimal_places) != 0`.
- `account/models/account_move.py:3188` — `with self._check_balanced(container):` wrapping `create`.

### CONTRADICTION

None identified against EV-013 itself, which I read as accurate and well-scoped. I record a
gap rather than a contradiction: EV-013 documents the amount model but does not state that the
entry-balance rule has no database carrier, which is the more consequential fact for SMEsPlus.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED` — which callers in the wider reference tree actually set
`check_move_validity` falsely. I grepped `addons/account/` and found the key referenced at
exactly one site, the check's own definition, meaning no in-module caller disables it. Not
found in `addons/account/` — I did not sweep the full 797-module tree, so I cannot state that
no module does.

`UNKNOWN — EVIDENCE REQUIRED` — whether a database-level per-entry balance constraint is
practically implementable given that lines are inserted before the entry is complete. A
deferred constraint or a constraint trigger firing at COMMIT is the standard answer, but its
interaction with SMEsPlus's chosen write pattern has not been designed and cannot be asserted
here.

### RECOMMENDATION

`RECOMMENDATION` — Boss decision required.

1. SMEsPlus canonical amount model: adopt **one signed amount per journal item in the entity's
   functional currency** as the single stored fact, with debit/credit exposed only as a
   presentation derivation. This matches the reference conclusion but is derivable
   independently from the business semantics: a posting has one magnitude and one direction,
   and storing that as two mutually-exclusive non-negative columns creates a two-column
   invariant that must then be separately defended.
2. Alongside it, store the transaction-currency amount and an explicit transaction currency on
   every item, always populated even when it equals the functional currency. Never allow a null
   currency to mean "functional currency" — a null that means something is a fact that cannot
   be constrained.
3. Entry balance must be enforced by a **deferred database constraint evaluated at commit**,
   with no application-level bypass path. An unbalanced entry must be impossible to commit, not
   merely difficult to create. Classify this `Tolerance = 0`.
4. Retain the line-level coherence checks as database CHECK constraints — sign agreement
   between functional and transaction amounts, and mandatory account on accountable lines.

---

## FINDING X2-03 — Reconciliation is a three-part model, and its derived state is stored without a stated reconstruction contract

**Verdict: CONFIRMED WITH CAVEAT** on EV-014

### OBSERVATION

`VERIFIED FACT` — EV-014's three-part characterisation is correct and I verified each part.
The *record* is a partial-reconciliation row linking exactly one debit item to exactly one
credit item, both `required=True`, carrying three separate monetary amounts — one in company
currency and one in each side's own transaction currency — plus a stored, precomputed
`max_date`. The *state* is `amount_residual`, `amount_residual_currency` and `reconciled`,
all three produced by one stored compute, plus an indexed `matching_number` marker. The
*event* is that unlinking a full reconciliation reverses the exchange-difference entries it
created, by posting new reversal moves.

`VERIFIED FACT` — the task asks what happens if recomputation is missed. The answer is precise:
`amount_residual`, `amount_residual_currency` and `reconciled` are stored columns whose values
are only as current as the last time the ORM's dependency graph fired. If a write path mutates
the partial-reconciliation rows outside the ORM — raw SQL, a restore, a migration, a partial
rollback — the stored state is stale and **nothing in the database detects it**. The stored
residual and the sum of partials can disagree indefinitely. A ledger will then show an invoice
as open that is matched, or as matched that is open, and both the ageing report and the
statement of account inherit the error.

`VERIFIED FACT` — a reconstruction path does exist in principle, and is stronger than I
expected. The residual compute derives entirely from the partial rows reachable through
`matched_debit_ids` / `matched_credit_ids`, so the partials are the authoritative record and
the state is fully re-derivable from them. Separately, an `@api.constrains` on
`matching_number` cross-checks the marker against the presence of partials and the full
reconciliation in both directions — a `P` marker with no partials is rejected, a `P` marker
that also carries a full reconciliation is rejected, a numeric marker without a full
reconciliation is rejected, and a numeric marker that does not equal the full reconciliation's
id is rejected.

`INFERENCE` — so the reference model has a *derivation* path and a *marker* consistency check,
but no *reconciliation* between stored residual and re-derived residual. The constrains method
guards the cheap text marker and leaves the money alone. There is no residual-integrity report
analogous to the hash-integrity report.

### EVIDENCE

- `account/models/account_partial_reconcile.py:14-19` — `debit_move_id` and `credit_move_id`, both `index=True, required=True`; exactly one of each per row.
- `account/models/account_partial_reconcile.py:42-50` — three amount fields: `amount` (company currency), `debit_amount_currency`, `credit_amount_currency`.
- `account/models/account_partial_reconcile.py:57-62` — `max_date = fields.Date(store=True, precompute=True, compute='_compute_max_date')`.
- `account/models/account_partial_reconcile.py` — grep for `_sql_constraints` returns **no match**; the only declarative check in the file is `@api.constrains('debit_currency_id','credit_currency_id')` at `:69`. There is no database constraint that the sum of partials against an item cannot exceed that item's amount.
- `account/models/account_move_line.py:244-257` — `amount_residual`, `amount_residual_currency` and `reconciled` all `compute='_compute_amount_residual', store=True`.
- `account/models/account_move_line.py:716-722` — the compute's docstring and its filter on reconcilable / cash / credit-card accounts; the derivation source is the partials.
- `account/models/account_move_line.py:1340-1354` — `@api.constrains('matching_number','matched_debit_ids','matched_credit_ids')` with four distinct rejection branches cross-checking the marker against partials and `full_reconcile_id`.
- `account/models/account_full_reconcile.py:13-35` — `unlink` captures `self.exchange_move_id`, calls super, then `moves_to_reverse._reverse_moves(default_values_list, cancel=True)` — unreconciling posts new entries.
- `account/models/account_move_line.py:283` — comment, verbatim intent: the marker can also start with `I` for imports.

### CONTRADICTION

I qualify EV-014 in one respect. EV-014 concludes that "any SMEsPlus model that treats
reconciliation as a pure state flag will be wrong in exactly the multi-currency and
cash-basis-tax cases". I read the exposure as wider than those two cases. Because there is no
database constraint bounding the partials against the item amount, over-reconciliation is a
structurally reachable state in *any* currency configuration, not only multi-currency ones —
it is prevented by application arithmetic, in the same tier as the entry-balance check in
X2-02, and with the same class of exposure. The two named cases are where the model is
*semantically* wrong; the unbounded partial sum is where it is *structurally* unguarded.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED` — whether the reference tree ships any residual-recomputation or
residual-verification utility (a maintenance action, a scheduled job, a consistency report).
Not found in `addons/account/models/` this session. I did not examine `addons/account/wizard/`
in full or the maintenance/upgrade trees.

`UNKNOWN — EVIDENCE REQUIRED` — the exact semantics of the `I` import marker and whether an
imported matching state is re-derivable at all, given that an `I`-marked line is explicitly
constrained to have *no* partials. If a migrated matching state carries a marker but no
partial rows, the derivation path does not exist for that data. This bears directly on Wave A
migration and needs its own dedicated evidence review.

### RECOMMENDATION

`RECOMMENDATION` — Boss decision required.

1. SMEsPlus should model reconciliation as an explicit **matching-record entity** — the
   authoritative, immutable-once-created fact — and treat settlement state as strictly derived.
   Derive it on read where volume permits; where it must be materialised for performance,
   materialise it under a stated **reconstruction contract**: the derivation must be
   idempotent, re-runnable at any time from the matching records alone, and covered by a
   scheduled verification that compares stored to re-derived and reports divergence.
2. Constrain the money at the database: the sum of matched amounts against an item must not
   exceed that item's amount, in both functional and transaction currency. Classify
   over-reconciliation `Tolerance = 0`.
3. Model un-matching as a **new event**, never as deletion of the matching record. The
   reference already demonstrates that un-matching emits accounting consequences; a design that
   deletes the match loses the fact that a match once existed, which is exactly the fact an
   auditor asks about.
4. Migrated matching state must carry provenance and must either carry re-derivable matching
   records or be explicitly flagged as non-derivable. See X2-08.

---

## FINDING X2-04 — The integrity hash is keyed on derived fields, not on the canonical fact; a write to the canonical amount is not blocked

**Verdict: CONTRADICTED in part** — EV-010's conclusion holds but its stated mechanism is
incomplete, and the gap is larger than EV-010 records

### OBSERVATION

`VERIFIED FACT` — EV-010's field lists are exactly right. At the current hash version the entry
contributes `['name','date','journal_id','company_id']` and each item contributes
`['name','debit','credit','account_id','partner_id']`. The omissions EV-010 tabulates —
transaction currency and amount, tax dimension, analytic dimension, maturity date, entry-level
reference metadata — are all real.

`VERIFIED FACT` — but there is a further omission EV-010 does not record, and it is structural
rather than dimensional. **The hash covers `debit` and `credit`, which are derived fields. It
does not cover `balance`, which is the canonical stored amount (X2-02).** The write guard on a
hashed item is computed as `set(vals) & inalterable_fields`, where `inalterable_fields` is
built from that same hash field list. `balance` is not in it.

`VERIFIED FACT` — and the ordering matters. The guard runs at line 1554-1563 of the item's
`write`. The `_sanitize_vals` call that would have collapsed a debit/credit write into a
balance write runs *afterwards*, at line 1566. So the two paths diverge:

- writing `{'debit': X}` on a hashed item — `debit` is in the hash list, the guard raises,
  the write is **blocked**;
- writing `{'balance': X}` on the same hashed item — `balance` is not in the hash list, the
  guard does not raise, the write **proceeds**, and the stored `debit`/`credit` are then
  recomputed from the new balance by their own dependency.

`INFERENCE` — the practical consequence is that the amount of a "secured" journal item can be
changed through the canonical field. The change is *detectable* after the fact, because the
recomputed debit/credit no longer match the chained hash and an integrity report would
recompute a different digest. But it is not *prevented*, and the guard's user-facing promise —
"you cannot edit the following fields" — does not hold for the field that actually carries the
money.

`INFERENCE` — this compounds EV-010's own headline. EV-010 established that
`amount_currency` is neither blocked nor detected. I add that `balance` is not blocked, only
detected. Between the two, on a hashed multi-currency item, neither of the two amounts is
write-protected by the guard.

`VERIFIED FACT` — a further sensitivity: the derivation of debit/credit from balance is not a
pure function of balance. It inverts under storno, which is driven by a company-level
configuration flag combined with the move type. The same stored balance therefore maps to a
different hashed debit/credit pair depending on configuration.

### EVIDENCE

- `account/models/account_move.py:3832-3839` — `_get_integrity_hash_fields` returns `['name','date','journal_id','company_id']` for versions 2, 3 and 4.
- `account/models/account_move.py:46` — `MAX_HASH_VERSION = 4`.
- `account/models/account_move_line.py:3283-3290` — the item's `_get_integrity_hash_fields` returns `['name','debit','credit','account_id','partner_id']` for versions 2, 3 and 4. `balance` is absent; `amount_currency` and `currency_id` are absent.
- `account/models/account_move_line.py:1554-1556` — `inalterable_fields = set(self._get_integrity_hash_fields()).union({'inalterable_hash'})`; `hashed_moves = self.move_id.filtered('inalterable_hash')`; `violated_fields = set(vals) & inalterable_fields`.
- `account/models/account_move_line.py:1557-1563` — the guard raises only when `hashed_moves and violated_fields`.
- `account/models/account_move_line.py:1566` — `vals = self._sanitize_vals(vals)` — executed **after** the guard at 1554-1563, so the debit-to-balance collapse cannot rescue the guard.
- `account/models/account_move_line.py:123-128` — `balance` is `store=True, readonly=False`.
- `account/models/account_move_line.py:650-658` — `_compute_debit_credit`, `@api.depends('balance','move_id.is_storno')`; under storno the debit and credit assignments are inverted.
- `account/models/account_move.py:880-882` — `_compute_is_storno` derives from `move_type` in refunds and `company_id.account_storno`, a company configuration flag.
- `account/models/account_move.py:3208-3214` — the entry-level guard uses the same `_get_integrity_hash_fields()` list, so the same class of omission applies at the entry level.

### CONTRADICTION

This finding **contradicts in part** the implicit model in EV-010 that the write guard and the
hash together define what is protected. They do not, because the guard is keyed on the derived
projection of the amount rather than on the amount. EV-010 records
`account_move_line.py:1554-1563` as "the write guards raise only for fields inside those same
hash lists", which is literally true and is exactly the defect — the lists name derived
fields. EV-010 stops one step short of the consequence.

I also record a partial disagreement with EV-010's framing that "for a single-currency ledger
the hash is sound". On my reading it is not sound even single-currency, because `balance` is
writable through the guard in any currency configuration. Single currency reduces the defect
from *undetectable* to *detectable-but-not-prevented*, which is a real difference, but it is
not soundness. `CONTRA-01` should be widened accordingly.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED` — whether the ORM in this build actually recomputes a stored
computed field when its dependency is written inside the same transaction in every write path,
or whether some paths defer or skip the recompute. If a path skips it, the balance write would
be neither blocked *nor* detected, which would be strictly worse. I read the field declaration
and the depends decorator; I did not trace the ORM's recompute scheduler.

`UNKNOWN — EVIDENCE REQUIRED` — whether the shipped integrity report recomputes hashes using
stored `debit`/`credit` or re-derives them. Not examined this session.

### RECOMMENDATION

`RECOMMENDATION` — Boss decision required.

1. SMEsPlus must define its immutability guarantee over the **canonical stored facts**, never
   over a derived projection of them. If the functional-currency signed amount is canonical
   (X2-02), it is the amount that must be sealed.
2. The sealed field set must be **complete over the accounting substance**, and specified as a
   closed list that a reviewer can read: entry identity, accounting date, journal, entity,
   and for each item — account, counterparty, functional amount, transaction currency,
   transaction amount, tax dimension, analytic dimension, maturity. An integrity mechanism that
   omits the tax and currency dimensions does not secure a Thai-context ledger, where the tax
   dimension is the filed fact.
3. Prevention and detection must be the **same list**, derived from one declaration. The
   reference's defect is reachable precisely because the guard list and the substance list were
   allowed to differ. In SMEsPlus, generate the write guard from the sealed-field declaration
   so they cannot drift.
4. Do not seal a field whose value depends on configuration. If SMEsPlus supports a
   reversal-presentation convention, seal the signed amount and derive the presentation, so
   that a configuration change cannot alter a sealed value.

---

## FINDING X2-05 — Entry-number uniqueness is a posted-only partial index, with an unusual declaration and a lock that depends on it

**Verdict: CONFIRMED** on EV-006

### OBSERVATION

`VERIFIED FACT` — EV-006 is accurate. The unique index is created imperatively at schema
initialisation as `CREATE UNIQUE INDEX account_move_unique_name ON account_move(name, journal_id)
WHERE (state = 'posted' AND name != '/')`. Its predicate restricts it to posted entries with a
real name, so draft entries and placeholder-named entries are outside it and may duplicate
freely.

`VERIFIED FACT` — a detail EV-006 does not record, which I find diagnostic: the model declares
`_sql_constraints = [('unique_name', "", "Another entry with the same name already exists.")]`
with an **empty SQL definition string**. The declaration exists only to attach a human-readable
message to a constraint the ORM did not create. The real object is the hand-written partial
index. This is a schema whose most important uniqueness guarantee is not visible in the
declarative constraint layer at all.

`VERIFIED FACT` — the sequence allocator's cross-transaction safety is built *on* that index.
`_locked_increment` obtains its exclusive lock by touching a row covered by the unique
constraint, and its own docstring states that if the record is not governed by the constraint —
for an entry, if it is not posted — the lock is not taken and returned numbers may not be
unique.

`INFERENCE` — uniqueness and the allocation lock are therefore the same mechanism, and both
switch on at the moment of posting. Before posting there is neither. For SMEsPlus the relevant
consequence is not that drafts can share a number; it is that **the number is not an identity
until posting**, so nothing upstream — a document reference, an approval record, an external
integration — may treat a pre-posting number as a stable key.

`INFERENCE` — EV-006 is right that company scoping is only transitive through the journal. That
transitivity is load-bearing: it holds only for as long as a journal belongs to exactly one
entity. If SMEsPlus ever permits a shared journal, the index silently stops being
entity-scoped, with no error.

### EVIDENCE

- `account/models/account_move.py:730-735` — inside `_auto_init`: `CREATE UNIQUE INDEX account_move_unique_name ON account_move(name, journal_id) WHERE (state = 'posted' AND name != '/')`.
- `account/models/account_move.py:713-715` — `_sql_constraints = [('unique_name', "", "Another entry with the same name already exists.")]` — empty definition string.
- `account/models/account_move.py:717-735` — the index is created in `_auto_init` alongside two non-unique performance indexes, i.e. in the imperative schema hook rather than the declarative layer.
- `account/models/sequence_mixin.py:352-368` — `_locked_increment` docstring, verbatim intent: the lock is taken through the unique constraint; at entry the record must already be governed by that constraint (for an entry, it must be posted), otherwise the lock is not taken and sequence numbers may not be unique when returned.

### CONTRADICTION

None identified. I confirm EV-006 as read and add the empty-definition detail and the
lock-coupling as supporting structure.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED` — whether the reference permits an entry to be deleted or
re-numbered after posting in a way that frees a number for reuse, producing a gap or a
duplicate across time. EV-011 and EV-022 bear on this but I did not trace the interaction with
the index predicate this session.

### RECOMMENDATION

`RECOMMENDATION` — Boss decision required.

1. SMEsPlus should treat the entry number as **assigned at posting and unique from that moment,
   forever**, enforced by a database unique constraint explicitly scoped
   `(entity, journal, number)` — scoped directly, never inherited transitively from the
   journal's ownership, so that the guarantee survives any future change to journal sharing.
2. Draft entries must carry no number, or carry a visibly non-numeric placeholder. They must
   never carry a candidate number that could be mistaken for the final one, because a number
   that changes is worse than a number that is absent.
3. Number allocation must not depend for its locking on the same index that provides
   uniqueness. Couple them and you inherit the reference's property that neither guarantee
   exists before posting.
4. Declare the constraint in the schema definition, not in an imperative initialisation hook.
   An integrity guarantee that cannot be read off the schema cannot be reviewed.

---

## FINDING X2-06 — Account merge bypasses the ORM entirely: raw SQL FK sweep and raw SQL DELETE past the guards that forbid it

**Verdict: CONFIRMED WITH CAVEAT** — EV-004's conclusion is right; the mechanism is
substantially more severe than EV-004 states

### OBSERVATION

`VERIFIED FACT` — EV-004 correctly reports that merge deletes account rows and retargets
journal items. What EV-004 does not report is *how*, and the how changes the risk assessment.

`VERIFIED FACT` — the retarget is not an ORM write. It is a generic foreign-key sweep: the
routine queries the database catalogue for **every table carrying a foreign key to the account
table**, then issues raw `UPDATE` statements rewriting the referencing column from each doomed
account id to the surviving id. It discovers its targets from `information_schema`, so it
rewrites references in tables the accounting module has never heard of — any installed module,
any customisation, any extension that references an account.

`VERIFIED FACT` — the deletion is likewise raw: `DELETE FROM account_account WHERE id IN (...)`
executed directly against the cursor, preceded by `self.env.invalidate_all()` and followed by a
registry cache clear.

`VERIFIED FACT` — and this is the finding. The account model declares an `@api.ondelete` guard,
`_unlink_except_contains_journal_items`, which refuses deletion of any account that has journal
items. There are two further such guards for fiscal-position mappings and tax repartition
lines. **A raw SQL `DELETE` does not invoke `unlink()`, so none of these three guards fire.**
The merge therefore deletes accounts that the model itself declares undeletable, and it does so
by construction, not by accident — the deletion is written as raw SQL in a routine whose whole
purpose is to delete accounts that have journal items.

`INFERENCE` — the consequences for the SMEsPlus data model are three, in descending severity:

(a) **No write path is observed.** Because the retarget is raw SQL, no ORM `write` runs on any
    affected journal item. No field tracking is recorded, no hash guard is consulted, no
    lock-date check is applied. Journal items inside a hard-locked, hashed period have their
    account rewritten with none of the period's protections engaging. The hash-ordering trick
    EV-004 identifies protects the *surviving* account's id; it does nothing for the items
    being retargeted off the deleted accounts.

(b) **Provenance is destroyed with no carrier.** EV-004 says this and is right. I add that the
    destruction is unrecoverable in principle, not merely in practice: the deleted account's
    row is gone, its id is unreferenced, and the only trace is the merged name translation
    written onto the survivor. There is no merge record, no superseded-by link, no event row.
    An auditor asking "what account did this 2024 posting name when it was made" has no
    artefact to consult.

(c) **The blast radius is undeclared.** Because the FK sweep is catalogue-driven, the set of
    tables affected by a merge is a property of what is installed, not of what was designed. No
    reviewer can enumerate it from the source.

### EVIDENCE

- `account/wizard/account_merge_wizard.py:134-141` — `_action_merge` docstring, verbatim intent: the first account is extended to each company of the others keeping their codes and names; the others are deleted; journal items and other references are retargeted to the first account.
- `account/wizard/account_merge_wizard.py:162-163` — `wiz = self.env['base.partner.merge.automatic.wizard'].new()` then `wiz._update_foreign_keys_generic('account.account', accounts_to_remove, account_to_merge_into)`.
- `base/wizard/base_partner_merge.py:103-111` — `_update_foreign_keys_generic` docstring, verbatim intent: update all foreign keys from the source records to the destination record for any model; `relations = self._get_fk_on(self.env[model]._table)`.
- `base/wizard/base_partner_merge.py:121-122` — `SELECT column_name FROM information_schema.columns WHERE table_name LIKE '%s'` — target columns discovered from the database catalogue at runtime.
- `base/wizard/base_partner_merge.py:136-149` — raw `UPDATE "<table>" SET "<column>" = %s WHERE "<column>" = %s ...` executed per source record via `self._cr.execute`.
- `account/wizard/account_merge_wizard.py:194-203` — `self.env.invalidate_all()` then `self.env.cr.execute(SQL("DELETE FROM account_account WHERE id IN %(account_ids_to_delete)s", ...))` — raw SQL delete, not `unlink()`.
- `account/models/account_account.py:1095-1098` — `@api.ondelete(at_uninstall=False) def _unlink_except_contains_journal_items(self):` raises `You cannot perform this action on an account that contains journal items.` — the guard the raw DELETE bypasses.
- `account/models/account_account.py:1100-1108` — two further `@api.ondelete` guards, for fiscal-position mappings and tax repartition lines, equally bypassed.
- `account/wizard/account_merge_wizard.py:112` — the survivor is chosen by `sorted('account_has_hashed_entries', reverse=True)` with the comment, verbatim intent, that this ensures a hashed account's id does not get changed by the merge.

### CONTRADICTION

I qualify EV-004. EV-004 characterises merge as "a destructive history rewrite" whose cost is
lost provenance. That is correct but incomplete: the operation also **bypasses the model's own
declared deletion guards and every ORM-level control** — tracking, hash guard, lock-date check.
EV-004's closing observation that "where hashing is off, no such protection applies" understates
it; even where hashing is on, protection applies only to the surviving account's identity, not
to the retargeted items or to the deleted rows.

For SMEsPlus this reclassifies merge from "a design decision about provenance" to "a control
bypass", which is a different gate.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED` — whether the reference records any durable audit artefact of a
merge. I found an access-rights check and a success notification; I did not find a message-log
write, a merge-history model, or any row persisting what was merged into what. Not found in
`account/wizard/account_merge_wizard.py` — I did not search for a mixin that might add one.

`UNKNOWN — EVIDENCE REQUIRED` — the behaviour of the FK sweep against tables where the
retarget would violate a unique constraint. The routine contains a `NOT EXISTS` guard in its
single-column branch, implying the authors anticipated collisions, but the disposition of rows
that fail the guard — silently left pointing at a row about to be deleted, and thus orphaned or
cascade-deleted — was not traced this session. This should be resolved before any SMEsPlus
merge design is drafted.

### RECOMMENDATION

`RECOMMENDATION` — Boss decision required. I record this one as `HOLD`.

1. `HOLD` — SMEsPlus should **not** adopt a destructive account merge for accounts carrying
   posted history, pending Boss decision. Posted history names an account; that naming is a
   historical fact and facts are not editable.
2. Derive the requirement from the business semantics instead: what the business needs is
   *"these two accounts are the same thing from now on, and reports should combine them"*. That
   is a **supersession relationship**, modelled as a row — superseded account, surviving
   account, effective date, reason, actor — with both account records retained. Reports
   traverse the relationship; history keeps its original reference. This satisfies the business
   need without a rewrite and gives the auditor the artefact the reference destroys.
3. If Boss nevertheless requires physical merge for a bounded case — say, accounts with no
   posted items — it must run **through** the integrity controls, not around them, and must
   write a durable merge record before it writes anything else.
4. As a standing architectural rule: no SMEsPlus operation may modify posted financial data by
   a path that bypasses the platform's own integrity guards. Classify a violation
   `Tolerance = 0`.

---

## FINDING X2-07 — One rate per day per currency per entity group, database-enforced, with no rate-type dimension

**Verdict: CONFIRMED** on EV-018

### OBSERVATION

`VERIFIED FACT` — EV-018 is accurate and I verified it directly. The rate entity is keyed by a
date, a currency and a company, with two real database constraints: `unique (name, currency_id,
company_id)` and `CHECK (rate>0)`. The company defaults to the acting company's root, so rates
are shared across an entity group rather than held per entity.

`VERIFIED FACT` — the stored scalar is a single technical rate. The two other rate fields are
computed inversions of it, not independent stored facts.

`INFERENCE` — the modelling consequence is that the rate table's grain is
`(date, currency, entity-group) -> one number`. Any business requirement whose grain is finer
has no carrier. Concretely, and these are ordinary requirements rather than exotic ones:

- a **closing rate** distinct from the transaction-date rate, for period-end revaluation;
- an **average rate** for the period, for translating results;
- a **historical rate** attached to a non-monetary item and held constant across periods;
- a **contracted or hedged rate** on a specific transaction;
- more than one rate on one day where a currency is quoted intraday.

`INFERENCE` — note what the model does provide, which is worth keeping: uniqueness and
positivity are enforced by the database, not by application code. This is the one place in the
core ledger where the integrity tier is the correct one. It is a useful internal benchmark: the
reference authors were willing and able to use database constraints, so the absence of a balance
constraint in X2-02 and of a code constraint in X2-01 reflects choices, not a house style.

### EVIDENCE

- `base/models/res_currency.py:336-338` — `class CurrencyRate`, `_name = "res.currency.rate"`, `_check_company_domain = models.check_company_domain_parent_of`.
- `base/models/res_currency.py:340-341` — `name = fields.Date(string='Date', required=True, index=True, ...)`; the date is the entity's key, one row per day.
- `base/models/res_currency.py:342-347` — `rate = fields.Float(digits=0, aggregator="avg", string='Technical Rate')` — the single stored scalar.
- `base/models/res_currency.py:348-361` — `company_rate` and `inverse_company_rate` are `compute=` with inverses; derived presentations.
- `base/models/res_currency.py:363-365` — `company_id = fields.Many2one('res.company', default=lambda self: self.env.company.root_id)` — grain is the entity group's root, not the entity.
- `base/models/res_currency.py:367-370` — `_sql_constraints = [('unique_name_per_day', 'unique (name,currency_id,company_id)', ...), ('currency_rate_check', 'CHECK (rate>0)', ...)]` — genuine database constraints.

### CONTRADICTION

None identified. EV-018 is confirmed as read.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED` — EV-018's own open question, whether the reporting layer
synthesises an average rate for presentation, remains open. I did not examine
`addons/account_reports/` for rate synthesis this session; EV-018 defers it to Wave G and I
concur with that deferral.

`HOLD / EVIDENCE REQUIRED — routed to the Accounting-Tax track` — whether Thai statutory
reporting requires a rate basis distinct from the transaction-date rate, and which basis. This
is a statutory question and is out of my lane. It must be answered before the rate grain is
fixed, because the answer determines whether the extra dimension is optional or mandatory.

### RECOMMENDATION

`RECOMMENDATION` — Boss decision required.

1. SMEsPlus should model the exchange rate with an explicit **rate-purpose dimension** in the
   key — at minimum distinguishing the rate used to record a transaction from the rate used to
   revalue at period end — rather than assuming one rate serves both. Adding the dimension
   later is a data migration; leaving it out is cheap only until the first revaluation.
2. Keep the database-level guarantees the reference gets right: uniqueness on the full key and
   a positivity check. Extend with an explicit direction convention stored as data, so that
   "rate" is never ambiguous about which way it multiplies.
3. Decide explicitly whether the rate grain is the entity or the entity group. The reference
   chose the group. For a Thai SME group with entities on different functional currencies that
   choice is a constraint, not a convenience, and it should be a decision rather than an
   inheritance.
4. The rate actually applied to a posting must be **stored on the posting**, not looked up from
   the rate table at read time. A rate table row can be corrected; a posted translation must
   not silently change when it is.

---

## FINDING X2-08 — Opening balances carry no provenance, and there is no temporal validity model anywhere in the core

**Verdict: CONFIRMED** on EV-017, extended with a negative finding on the temporal model

### OBSERVATION

`VERIFIED FACT` — EV-017 is accurate. The opening position is an ordinary journal entry
referenced from the entity, dated one day before the stated opening date, balanced against the
current-year-earnings account. "Accounting is initialised" is defined as nothing more than that
entry existing and being posted. The per-account opening debit and credit are computed fields
with inverse setters writing into that one entry.

`INFERENCE` — the modelling consequence EV-017 draws is correct and I restate it in data terms.
An opening balance is, semantically, a **migration assertion**: someone asserts that as at a
date, per a named prior system, per a named extraction, this account stood at this amount, and
someone accepted that assertion. In the reference model none of those five facts — source
system, extraction identity, extraction date, asserting party, accepting party — has a column.
The assertion is flattened into an ordinary posting, indistinguishable from a manual journal
entry made on the same date.

`VERIFIED FACT` — separately, and directly answering the temporal-model question in my brief: I
searched the core account and journal models for effective-dating fields — `date_from`,
`date_to`, `valid_from`, `valid_until` — and found **none**. Master data in the reference core
is not effective-dated. An account's attributes are current-state only; changing an account's
type, its reconcilability, its currency restriction or its name changes it for all of history,
with the change visible only as a tracked message, not as a temporal record.

`VERIFIED FACT` — this composes with EV-016's finding, which I re-verified: a search for a
fiscal-year model definition returns no result. There is no fiscal-year entity.

`INFERENCE` — the reference system's complete temporal model for the core ledger is therefore:
one date on each entry, a set of lock dates on the entity, and the rate table's date. There is
no bitemporality, no effective-dating of master data, and no period entity. Everything else is
current state. That is a coherent and defensible minimalism for a single-entity SME, and it is
an actively poor fit for a system that must reproduce what a report said at a past date, or
explain why a report re-run today differs from the one filed last quarter.

### EVIDENCE

- `account/models/company.py:172-173` — `account_opening_move_id = fields.Many2one(string='Opening Journal Entry', comodel_name='account.move', help="The journal entry containing the initial balance of all this company's accounts.")` and the related opening journal.
- `account/models/company.py:174` — `account_opening_date = fields.Date(..., default=... .replace(month=1, day=1), required=True)`.
- `account/models/company.py:730-733` — the opening entry is prepared as an ordinary move with `'ref': _('Opening Journal Entry')` and `'date': self.account_opening_date - timedelta(days=1)`.
- `account/models/company.py:736-738` — `def opening_move_posted(self): return bool(self.account_opening_move_id) and self.account_opening_move_id.state == 'posted'` — initialisation is defined as existence plus posted state, nothing more.
- `account/models/company.py:740-745` — `get_unaffected_earnings_account` docstring, verbatim intent: returns the unaffected earnings account, creating one if none has yet been defined.
- `account/models/account_account.py:126-131` — `opening_debit` / `opening_credit` / `opening_balance` as `compute=` with `inverse='_set_opening_debit'` etc., writing into that single entry.
- Negative, scoped: grep for `date_from|date_to|valid_from|valid_until` across `account/models/account_account.py` and `account/models/account_journal.py` returns **no match** — not found in those two files. No effective-dating on core master data in that scope.
- Negative, scoped: grep for `_name = 'account.fiscal.year'` across `addons/` returns **no match** — not found in the addons tree searched this session, corroborating EV-016.

### CONTRADICTION

None identified against EV-017 or EV-016.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED` — whether any non-core reference module supplies effective-dated
master data or a period entity. My negative is scoped to `account/models/account_account.py`,
`account/models/account_journal.py` and a `_name` search across the addons tree; I did not read
every model in every module.

`HOLD / EVIDENCE REQUIRED — routed to the Accounting-Tax track` — the Thai statutory retention
and reproducibility requirement for opening balances on migration, and whether a filed report
must be reproducible as filed. This determines whether the temporal requirement in my
recommendation is a preference or an obligation. Out of my lane.

### RECOMMENDATION

`RECOMMENDATION` — Boss decision required.

1. SMEsPlus must model an opening balance as a **first-class migration assertion entity**, not
   as an ordinary entry. Required attributes, derived from the business semantics of migration:
   source system identity, extraction identity and timestamp, as-at date, asserting party,
   accepting party, acceptance timestamp, and the reconciliation status of the source position.
   The resulting ledger posting references that assertion; it does not replace it.
2. The assertion must be immutable once accepted. A correction is a new assertion superseding
   the prior one, with both retained — the same supersession pattern as X2-06.
3. `RECOMMENDATION` — SMEsPlus should decide deliberately whether core master data is
   **effective-dated**. My position: account classification and reconcilability must be
   effective-dated, because both change the meaning of history when altered, and neither can be
   reconstructed from a message log. Descriptive attributes such as the name may remain
   current-state.
4. `RECOMMENDATION` — adopt an explicit **accounting-period entity** rather than deriving
   periods from dates. A period that is a row can carry its own state, its own close record,
   its own reopening record and its own approvals. A period that is only a pair of dates can
   carry none of those, which is the root of why EV-016 finds no close event to point at.

---

## FINDING X2-09 — Which financial facts are immutable, which are mutable metadata, which are derived: the reference draws these boundaries by configuration, not by structure

**Verdict: CONFIRMED WITH CAVEAT** on EV-011 / EV-013 / EV-022, stated as a required SMEsPlus
classification

### OBSERVATION

`VERIFIED FACT` — the reference model does not classify its fields into immutable, mutable and
derived at the structural level. It classifies them at the *guard* level, and the guards are
optional. EV-011 established that hashing is a per-journal boolean defaulting off and that
deletion protection is a separate entity-level boolean. EV-022 established that the posted-state
guard is a Python list with a documented context bypass. X2-04 established that the guard list
names derived fields rather than canonical ones.

`INFERENCE` — the consequence for a database designer is that in the reference model
**immutability is not a property of any column**. It is a property of a configuration
combination evaluated at write time. Two entities running identical software can hold the same
posting under entirely different mutability regimes, and nothing in the row records which regime
applied when it was written.

`INFERENCE` — my brief asks me to state the classification explicitly for SMEsPlus. Derived
from the business semantics of a ledger rather than from the reference structure:

**Immutable once posted — the recorded financial fact.** These are assertions about what
happened; they cannot change, only be superseded by a correcting entry.
- entry identity and entry number
- accounting date and the period it falls in
- journal and reporting entity
- per item: the account, the counterparty, the signed functional amount, the transaction
  currency, the transaction amount, the exchange rate actually applied, the tax dimension, the
  analytic dimension
- the fact and identity of any matching applied to an item
- the identity, source and acceptance of a migrated opening position (X2-08)

**Mutable metadata — descriptive, non-financial, revisable with an audit trail.** These do not
change what happened, only how it is described.
- free-text reference, narration, internal notes, attachments
- non-accounting document links and classification tags that do not drive a report line
- workflow annotations and approval commentary
Every change here must be recorded as a change event with actor and timestamp; mutable is not
the same as untracked.

**Derived — never stored as an independent fact; always reconstructible.**
- the debit/credit presentation split of the signed amount
- settlement state: residual amounts and the matched flag
- account balances, trial balance, and every report aggregate
- the current-year result and its attribution to equity
- ageing buckets and the maturity classification
Where a derived value is materialised for performance, it must carry the reconstruction
contract of X2-03: idempotent, re-runnable from the immutable facts alone, and verified on a
schedule.

`INFERENCE` — the reference misplaces at least three items against this classification, each
verified above: the transaction-currency amount is treated as mutable on a sealed entry
(EV-010); the canonical functional amount is treated as mutable on a sealed entry (X2-04); and
matching state is stored as fact rather than derived under contract (X2-03).

### EVIDENCE

- `account/models/account_move.py:713-715` and `:730-735` — the move model's only declarative constraint is a message-only stub; the sole real uniqueness object is an imperatively created partial index. No column-level immutability is declared anywhere in the model.
- `account/models/account_move_line.py:429-459` — the four line-level `_sql_constraints` are coherence checks (`credit * debit=0`, sign agreement, required account, empty non-accountable line). **None of them is an immutability constraint**; the database permits any of these columns to be updated in place.
- `account/models/account_move_line.py:1554-1563` — immutability is evaluated in Python at write time from `self.move_id.filtered('inalterable_hash')`, i.e. conditional on whether that specific move was ever hashed.
- `account/models/account_move.py:3208-3214` — the entry-level equivalent, conditional on `move.inalterable_hash` being set.
- `account/models/account_move_line.py:123-128` vs `:113-122` — `balance` (canonical, writable, tracked) versus `debit`/`credit` (derived, stored, in the hash list) — the structural inversion described in X2-04.
- `account/models/account_move_line.py:244-257` — `amount_residual`, `amount_residual_currency`, `reconciled`: derived values given persistent storage with no declared reconstruction contract.
- `base/models/res_currency.py:367-370` — the counter-example proving intent rather than incapacity: where the authors wanted a database guarantee, they declared one.

### CONTRADICTION

I qualify EV-011's conclusion. EV-011 states that "neither immutability nor deletion protection
is a property of the ledger; both are configuration". Correct, and I would sharpen it: the
deeper problem is not that the switches default off but that **there is no column the switches
could protect**. Turning every switch on still yields Python-tier protection over a schema that
permits in-place update of every financial column. A configuration change cannot promote an
application check into a storage guarantee.

This matters for the SMEsPlus gate because it means "adopt the reference model and default the
switches on" is not an available mitigation. The classification above has to be built into the
schema, not layered over it.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED` — whether the reference deployment relies on database-level
controls outside the module source to make posted rows non-updatable (revoked UPDATE grants,
row-level security, append-only replication, a WORM audit log). Not found in `addons/account/`
this session; deployment and infrastructure trees were not in scope.

`UNKNOWN — EVIDENCE REQUIRED` — whether the SMEsPlus target platform can support deferred
constraints, constraint triggers and column-level update revocation. The recommendations below
assume it can; that assumption has not been evidenced.

### RECOMMENDATION

`RECOMMENDATION` — Boss decision required. This is the finding I would put first at the gate.

1. Adopt the three-way classification above as a **binding SMEsPlus data-model rule**, declared
   once and enforced generatively: the write guards, the sealed-field set for integrity
   verification, and the change-event schema must all be generated from one declaration so they
   cannot drift apart. The reference's central defect (X2-04) is drift between two hand-
   maintained lists.
2. Immutability of posted financial facts must be a **storage property**, not a configuration
   flag — enforced so that no application path, no context flag and no raw-SQL routine can
   update a posted financial column in place. Corrections happen by superseding entries.
   Classify a violation `Tolerance = 0`.
3. Derived values must never be the system of record. Where materialised, bind them to a
   reconstruction contract and verify it on a schedule.
4. Nothing above is approved by this review. Boss is sole final approver.

---

## EXPERT 2 POSITION

My position on the Wave A core ledger data model is that the evidence base is sound and, on the
points I re-derived independently, accurate. Twelve claims were verified against primary source
and none was found materially wrong. Three were found materially incomplete, and in each case
the incompleteness understated rather than overstated the exposure. I therefore endorse the
evidence base as a factual foundation while recording that it should not be read as a complete
risk statement.

The single structural conclusion I draw across all nine findings is this. The reference model
places almost every guarantee that matters in the application tier, and almost none in the
storage tier — and it does so by choice, not by limitation. The currency-rate entity proves the
point: where the authors wanted a database guarantee, they declared a unique constraint and a
positivity check, and they got one. Everywhere else in the core ledger they did not. There is no
database constraint that an entry balances. There is none that an account code is unique within
a company, and the storage form chosen for the code forecloses one. There is none bounding
matched amounts against the item being matched. There is none making a posted financial column
non-updatable. What exists instead is a layer of Python checks, several of which carry named,
documented bypasses, and at least one of which — the merge routine — is written specifically to
go around the model's own guards using raw SQL.

Three findings I would put in front of Boss ahead of the others. First, the integrity hash is
keyed on derived fields rather than on the canonical amount, with the result that a write to the
field that actually carries the money is not blocked on a sealed entry, only detected afterwards
(X2-04). This widens `CONTRA-01`: the hash is not sound for a single-currency ledger either.
Second, the account merge is not a provenance trade-off but a control bypass — a catalogue-driven
raw-SQL foreign-key sweep followed by a raw `DELETE` past three declared `@api.ondelete` guards,
one of which exists precisely to forbid deleting an account with journal items (X2-06). Third,
entry balance, the defining invariant of double-entry bookkeeping, is a Python check switchable
off through a context flag, while far less consequential line-level rules are genuine database
CHECK constraints (X2-02). The tiering is inverted against the importance of what is being
protected.

On the temporal model, my answer to the brief is short because the evidence is: there is
effectively none. One date per entry, lock dates on the entity, and a dated rate table. Master
data is not effective-dated in the core models I searched, there is no fiscal-year entity, and
there is no period entity. Everything else is current state. That is coherent minimalism for a
single-entity SME and a poor fit for any requirement to reproduce a prior report as filed or to
explain why today's re-run differs. Whether SMEsPlus is bound to such a requirement is a Thai
statutory question, which I hold and route to the Accounting-Tax track rather than answering.

What I would have SMEsPlus derive from all this — as clean-room requirements from business
semantics, not as a schema to copy — is a model in which the recorded financial fact is
immutable at the storage tier and corrected only by supersession; in which per-company code
assignment is a row with a unique constraint rather than a per-company value inside a row;
in which entry balance and matched-amount bounds are deferred database constraints with no
bypass; in which settlement state, presentation splits and all aggregates are derived under a
stated, verified reconstruction contract; in which migrated opening positions are first-class
assertions carrying source, extraction, asserter and accepter; and in which account supersession
replaces destructive merge entirely. Where SMEsPlus does materialise a derived value or does
permit a merge, both must run through the platform's integrity controls rather than around them.

I approve nothing. Findings X2-01, X2-02, X2-03, X2-04, X2-06 and X2-09 each require a Boss
decision before the Wave A data model can be considered settled; X2-06 I record as `HOLD`
pending that decision, and the Thai statutory dependencies in X2-07 and X2-08 are
`HOLD / EVIDENCE REQUIRED` routed to the Accounting-Tax track. Boss is sole final approver.

*Reviewed independently under Constitution principle 7. No part of this review assesses work
authored by this reviewer.*
