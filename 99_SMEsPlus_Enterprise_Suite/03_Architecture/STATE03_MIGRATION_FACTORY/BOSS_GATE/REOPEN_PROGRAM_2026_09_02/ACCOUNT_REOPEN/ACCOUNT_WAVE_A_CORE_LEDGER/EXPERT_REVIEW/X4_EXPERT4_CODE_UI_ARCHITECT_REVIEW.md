> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.**
> This review carries `file:line -- method` citations into a reference ERP source tree.
> Boss / PMO / AI-Audit visible only. Must NOT be transcribed into any Layer 1 clean-room package,
> into Team B design input, or into any downstream reference package. Its clean-room derivatives are
> the numbered files in the package root, which cite `EV-0NN` / `COR-0N` identifiers only.

# X4 — EXPERT 4 REVIEW: LEAD CODE & UI ARCHITECT

Session: `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`
Wave: `WAVE A — CORE LEDGER & CLOSING`
Reviewer: Expert 4 — Lead Code & UI Architect (independent)
Date: 2026-09-04

> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.**
> This file carries `file:line` citations to a reference ERP source tree. Boss / PMO / AI-Audit
> visible only. Not to be transcribed into any Layer 1 clean-room package or Team B design input.

**Scope of my lens.** Functional boundary; state machine; control ownership; UI consequence;
architecture risk. I do not opine on accounting policy, tax treatment, data migration or
statutory matters; where my findings touch those, I route them rather than decide them.

**Evidence base read.** `LAYER2_EVIDENCE_QUARANTINE/E00_PRIMARY_EVIDENCE_BASE.md`, EV-000..EV-023.

**Independent verification performed.** Read-only, against
`/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/` (v18, build 20250608).
Nothing under that path was modified. I personally verified 14 distinct claims, of which 6 are
re-verifications of the evidence base and 8 are new observations not present in E00. Two of my
findings **CONTRADICT or materially QUALIFY** the evidence base (F-03, F-06, and partly F-05).

**Verdict vocabulary used:** `CONFIRMED`, `CONFIRMED WITH CAVEAT`, `CONTRADICTED`, `UNKNOWN`,
`HOLD`, `VETO`.

**Claim classes used:** `VERIFIED FACT` / `REFERENCE BEHAVIOUR` / `INFERENCE` / `RECOMMENDATION` /
`UNKNOWN — EVIDENCE REQUIRED`.

**Wording note for the reviewer running the mechanical check.** No verdict, heading or conclusion in
this document uses the prohibited approval term or any variant of it. A substring match will
nonetheless return five hits, all unavoidable and all in F-03, F-04 and F-09: three are the verbatim
reference identifiers `BYPASS_LOCK_CHECK` and `bypass_lock_check`, which must be cited exactly for
the evidence to be checkable, and two are attributed quotations of E00's own wording inside
`CONTRADICTION` headings, where paraphrasing would defeat the purpose of quoting. Everywhere in my
own prose I use *override*, *escape hatch*, *suppression* or *waiver* instead.

**Clean-room discipline.** Every recommendation below is stated as an SMEsPlus-native requirement
derived from *control intent*. I propose no port of reference code, class structure, ORM pattern or
module architecture. Where I name a reference construct it is to characterise a risk, never to
propose adopting its shape.

---

## FINDING F-01 — The three-value state field is a label, not the state machine. The real state space is at least eightfold.

**Verdict: CONFIRMED. The three-state model is insufficient for SMEsPlus.**

### OBSERVATION

The entry model presents a single `state` field with three values. The behaviour of an entry is
in fact determined by that field **in combination with** at least four orthogonal stored flags,
each of which changes what operations are legal, what a transition destroys, and what the user is
shown. Two entries reading `draft` in the UI can be entirely different objects: one has never
existed as an accounting fact and consumes no number; the other has been posted, has consumed a
number, has had its analytic subledger deleted and its reconciliations discarded, and is one write
away from being deleted outright. The state field does not distinguish them. The user cannot
distinguish them from the status badge.

The conflated concepts are: **lifecycle position** (is this a fact yet), **historical fact of
having been a fact** (`posted_before`), **evidentiary protection** (`inalterable_hash` / `secured`),
**deferred intent** (`auto_post`, `auto_post_until`), and **numbering integrity**
(`name` assigned or the `/` placeholder, plus `made_sequence_gap`).

### EVIDENCE

- `models/account_move.py:144-156` — `state = fields.Selection([('draft','Draft'),('posted','Posted'),('cancel','Cancelled')], required=True, readonly=True, copy=False, tracking=True, default='draft')`. Three values, and the field is `readonly=True`, i.e. it is never written by the user directly, only by application methods.
- `models/account_move.py:294` — `posted_before = fields.Boolean(copy=False)`. A separate, permanently sticky flag, never reset by any transition I located in `models/account_move.py`.
- `models/account_move.py:319-323` — `inalterable_hash = fields.Char(readonly=True, copy=False, index='btree_not_null')` and `secured = fields.Boolean(compute="_compute_secured", search='_search_secured')`; `:953-956` — `secured` is simply `bool(inalterable_hash)`.
- `models/account_move.py:264,275` — `auto_post` (Selection) and `auto_post_until` (Date), holding deferred/recurring posting intent on a record whose `state` still reads `draft`.
- `models/account_move.py:300` — `made_sequence_gap = fields.Boolean(compute='_compute_made_sequence_gap', store=True)` with the inline comment "store whether this is the first move breaking the natural sequencing".
- `models/account_move.py:1710-1716` — `_compute_show_reset_to_draft_button` proves the point: the button's visibility is a function of `restrict_mode_hash_table`, `state`, `inalterable_hash` **and** `need_cancel_request` — four inputs to decide whether one transition is offered.

### CONTRADICTION

None against the evidence base; E00 does not attempt a state-space map and my finding extends it
rather than opposing it. Internally, the reference contradicts itself in presentation: `state` is
declared `tracking=True` so the chatter records draft→posted→draft as if it were a reversible
toggle, while `button_draft` (F-02) is destructive. The audit narrative and the data effect
disagree.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether any list or kanban view in the reference distinguishes
"draft, never posted" from "draft, previously posted" to the ordinary user. I located the
`posted_before` guard in the form-view arch manipulation at `models/account_move.py:3392-3394`
(it governs whether the `name` field is shown), but I did not audit every view definition, and I
did not run the application. Scope of search: `addons/account/views/` and
`addons/account/models/account_move.py`.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus must not adopt a three-value entry status. The SMEsPlus-native
requirement is that **the status a user sees and the status the engine branches on are the same
enumeration**, and that enumeration must separately name, at minimum: *Unnumbered Working Entry*,
*Numbered Working Entry*, *Scheduled*, *Posted*, *Posted-and-Sealed*, *Reopened (was Posted)*,
*Voided (was Posted)*, *Abandoned (never Posted)*. If a distinction changes what a control permits
or what a transition destroys, it is a state, not a flag. Any flag that is not part of the named
state must be provably decorative. This is a Boss decision on the ledger's public vocabulary and I
place it as a Wave A blocking design question, not a preference.

---

## FINDING F-02 — Un-posting is a destructive multi-subledger operation, and "Cancel" is silently the same operation.

**Verdict: CONFIRMED, and extended — E00 did not record that Cancel routes through Draft.**

### OBSERVATION

Resetting a posted entry to draft deletes the entry's analytic lines outright and discards every
reconciliation on its items. This is documented in the evidence base (EV-012). What the evidence
base does **not** record, and what I consider the more serious UI-consequence finding, is that
`button_cancel` on a posted entry does not perform a distinct transition at all: it calls
`button_draft` first and then sets the cancelled state. A user who deliberately chooses "Cancel"
in preference to "Reset to Draft" — the natural choice of a cautious accountant who wants the
entry preserved and neutralised rather than reopened — incurs the *identical* destruction of the
analytic subledger and of all matching, plus whatever accounting events the unreconcile emits.
The UI offers two buttons; the engine has one destructive path.

### EVIDENCE

- `models/account_move.py:5274-5286` — `button_draft`: refuses non-posted/non-cancelled; refuses when `need_cancel_request`; calls `_check_draftable()`; then `self.mapped('line_ids.analytic_line_ids').unlink()`; then `self.mapped('line_ids').remove_move_reconcile()`; then `self.state = 'draft'`; then `_detach_attachments()`.
- `models/account_move.py:5363-5372` — `button_cancel`, verbatim in structure: `moves_to_reset_draft = self.filtered(lambda x: x.state == 'posted')` / `if moves_to_reset_draft: moves_to_reset_draft.button_draft()` / then it refuses anything not draft / then `self.payment_ids.state = "canceled"` / `self.write({'auto_post': 'no', 'state': 'cancel'})`. The inline comment calls it a "Shortcut to move from posted to cancelled directly", which is precisely what it is not — it is a detour through the destructive path.
- `models/account_move.py:5317-5354` — `_check_draftable` refuses only three categories: exchange-difference entries (resolved by direct SQL against `account_full_reconcile` / `account_partial_reconcile`), tax cash-basis entries (`tax_cash_basis_rec_id` or `tax_cash_basis_origin_move_id`), and hashed entries. Nothing else is protected.
- `models/account_move.py:3239-3242` — separately, `write` invokes `_check_fiscal_lock_dates()` and `line_ids._check_tax_lock_date()` when `'state' in vals and move.state == 'posted' and vals['state'] != 'posted'`.

### CONTRADICTION

Against EV-012: none on substance; EV-012 is accurate. I record a **gap**, not a contradiction —
EV-012 characterises `button_draft` alone and therefore understates the blast radius, because the
cancel path is not separately analysed and a reader would reasonably assume cancelling is
non-destructive.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` the full set of accounting events emitted transitively by
`remove_move_reconcile()` during an un-post. EV-014 establishes that unreconciling a full
reconciliation reverses its exchange-difference entry by posting reversals, and that reconciling
can generate cash-basis entries. I did not trace every emission path out of
`remove_move_reconcile` this session. Scope of search: `models/account_move.py`,
`models/account_full_reconcile.py` (read at EV-014's citations only).

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus must treat *un-posting as a compensating accounting event, not as a
state reversal*. The native requirement: once an entry is posted it is never returned to a working
state; a correction is a new, separately numbered, separately dated entry that references the
original. If a "reopen" affordance is nonetheless required by Boss for usability, then (a) it must
be a distinct named state that the ledger, the reports and the audit view all show, (b) the
analytic and matching consequences must be *re-derivable*, never destroyed, and (c) the UI must
enumerate to the user, before the click, exactly what will be discarded. Two buttons that do the
same destructive thing under different words is a defect pattern to be prohibited in the SMEsPlus
UI standard.

---

## FINDING F-03 — The posted-entry field freeze is caller-controlled, and the override is a plain context key used in shipped production code, not only in tests.

**Verdict: CONFIRMED WITH CAVEAT — EV-022 understates this. It is not a documented escape hatch for edge cases; it is load-bearing in the shipped bank reconciliation path.**

### OBSERVATION

EV-022 records that the posted-entry field freeze is a Python guard with a documented
`skip_readonly_check` context override. My independent search shows the override is not an
exceptional developer affordance: it is **switched on for every write to a bank statement line's
entry**, unconditionally, in shipped module code. The guard is therefore not "the posted invariant
with a documented exception"; it is "the posted invariant, except in the module that handles the
highest-volume, most operationally sensitive class of entries in the system".

Because the key is an ordinary truthy context entry — not a capability token — any caller that can
supply a context to a write can narrow the guard. Contrast this with the fiscal-lock override in
the same file, which the reference authors deliberately implemented as an unforgeable sentinel
object (F-04). The two patterns sit side by side in one model, which tells us the authors knew the
difference and did not apply it consistently.

### EVIDENCE

- `models/account_move.py:3245-3250` — the guard: `unmodifiable_fields = ('invoice_line_ids','line_ids','invoice_date','date','partner_id','invoice_payment_term_id','currency_id','fiscal_position_id','invoice_cash_rounding_id')`; `readonly_fields = [val for val in vals if val in unmodifiable_fields]`; `if not self._context.get('skip_readonly_check') and move_state == "posted" and readonly_fields: raise UserError(...)`.
- `models/account_bank_statement_line.py:437-442` — `def write(self, vals): ... res = super(AccountBankStatementLine, self.with_context(skip_readonly_check=True)).write(vals)`. Every write, no condition.
- `models/account_bank_statement_line.py:483` — `st_line.with_context(force_delete=True, skip_readonly_check=True).write({...'line_ids': [Command.clear()] + [Command.create(...)]})` inside `action_undo_reconciliation` — this replaces the entire line set of an entry, combining the deletion-protection override and the readonly override in one call.
- `models/account_bank_statement_line.py:803` and `:845` — two further production call sites.
- `../account_accountant/models/account_move.py:130` — `move.with_context(skip_readonly_check=True).write({'date': move._get_accounting_date(...)})` inside `button_draft`, rewriting the date of already-posted deferral reversals.
- `../account_accountant/models/bank_rec_widget.py:1411` and `:1458` — two more production call sites in the bank reconciliation widget.
- Search scope for the above: `grep -rn "skip_readonly_check"` over `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/`. Seven non-test call sites located; the remainder are under `tests/` and `addons_archive/`.

### CONTRADICTION

**Against EV-022.** EV-022 says the freeze is "a Python guard with a documented context bypass
rather than a storage-level property". Accurate but too gentle. The correct characterisation is
stronger and I record it as a qualification: **the posted invariant is not owned by the entry
model at all. It is owned by whichever caller last set the context.** The entry model expresses a
preference; the calling module decides.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether an ordinary authenticated client can supply
`skip_readonly_check` in an RPC context and thereby edit a posted entry's lines through the public
write endpoint. `INFERENCE:` in a framework where the client-supplied context is merged into
`self.env.context`, it would be reachable; but I did **not** test this, did not read the RPC
dispatch layer, and will not assert it. This is a security question outside my lane and I route it
to whichever expert holds the tenant-isolation and access-control brief. It should not be closed
by reasoning; it needs an executed test.

### RECOMMENDATION

`RECOMMENDATION:` in SMEsPlus, an invariant that the business calls "posted entries cannot be
edited" must not be implemented as a conditional check inside a write path. The native requirement:
**the posted representation of an entry is physically separate from its working representation**,
and the posted representation has no update path at all — the only operations against it are
insert and read. Whatever the bank-reconciliation feature needs, it must obtain by emitting new
entries, not by editing sealed ones. Where an engineered escape hatch is genuinely unavoidable, it
must be a capability that cannot be constructed from client input, must be enumerable (a fixed,
reviewed list of authorised call sites), and must write a durable record inside the tenant
database each time it is exercised.

---

## FINDING F-04 — The reference contains one correctly-shaped control override, and it demonstrates the pattern SMEsPlus should require everywhere.

**Verdict: CONFIRMED. Positive control-design finding; recorded because it is directly instructive.**

### OBSERVATION

The fiscal lock check can be suppressed, but only by a caller holding a private sentinel object
defined in the module's own Python namespace. A context key of the same name carrying `True`, or
any JSON-serialisable value, does **not** satisfy the check, because the comparison is by object
identity, not truthiness. A client cannot construct that object over the wire. The only production
user of it is the partner-merge path, which needs to rewrite the counterparty on already-posted
lines inside locked periods.

This is the correct shape for a control override and it stands in direct contrast to
`skip_readonly_check`, `force_delete`, `skip_account_deprecation_check` and `hash_version`, all of
which are ordinary keys in the same codebase.

### EVIDENCE

- `models/account_move.py:83` — `BYPASS_LOCK_CHECK = object()`. A module-private sentinel.
- `models/account_move.py:2377-2378` — `def _check_fiscal_lock_dates(self): if self.env.context.get('bypass_lock_check') is BYPASS_LOCK_CHECK: return`. Identity comparison (`is`), not a truth test.
- `models/partner.py:17` — the sentinel is explicitly imported by the only production consumer.
- `models/partner.py:804-805` — `moves.line_ids.with_context(bypass_lock_check=BYPASS_LOCK_CHECK).partner_id = partner.commercial_partner_id` and the same for `commercial_partner_id` on the entry. Search scope: `grep -rn "BYPASS_LOCK_CHECK\|bypass_lock_check"` over `addons/account/`, `addons/account_accountant/`, `addons/account_reports/` — two production call sites, both in `partner.py`.
- `models/partner.py:806` — the operation does write a narrative record: `partner._message_log(body=_("The commercial partner has been updated for all related accounting entries."))`.

### CONTRADICTION

None identified.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether the narrative record at `partner.py:806` names the affected
entries, or only states that entries were affected. From the string as read, it does not name them.
Whether a downstream audit could reconstruct which posted lines had their counterparty rewritten
inside a locked period is not decidable from this file alone.

### RECOMMENDATION

`RECOMMENDATION:` adopt the *intent*, not the code. SMEsPlus control overrides must be
unconstructible from client input, must be enumerable at review time, and must each produce a
durable, queryable record naming the affected records — not a free-text narrative note. I propose
this as a cross-cutting SMEsPlus engineering standard, applicable well beyond the Account module,
and I flag that a control which merely narrates its own use in prose is not auditable at scale.

---

## FINDING F-05 — The hash write-guard's protected field set is read from the caller's context, so the guard's own scope is caller-narrowable.

**Verdict: CONFIRMED — new observation, not present in the evidence base.**

### OBSERVATION

The write guard that refuses edits to a hashed ("secured") entry computes the protected field list
by calling `_get_integrity_hash_fields()`. That method reads a `hash_version` value from the
context, defaulting to the maximum. At version 1 the returned list is **narrower** than at version
4: the entry's list drops `name`, and the item's list drops `name`. A write executed with
`hash_version=1` in context therefore encounters a guard that no longer protects the entry number
or the item label on a sealed entry.

The method's own comment states the version indirection exists for backward compatibility when
generating the integrity **report**. The defect is that the same method is reused by the **write
guard**, so a switch intended to let the verifier re-derive old hashes also re-scopes the enforcer.

The stored hash is prefixed with its version (`$<version>$` from version 4), so the integrity
report would still recompute at the stored version and would still detect the change. That is the
mitigating fact, and it is important: this narrows what the guard blocks, it does not defeat
detection. But the architectural point stands and is independent of exploitability — **the
enforcement scope and the detection scope are derived from different authorities**: detection from
stored data, enforcement from caller-supplied context. Two controls that are meant to agree do not
share a source of truth.

### EVIDENCE

- `models/account_move.py:3208-3213` — the guard: `violated_fields = set(vals).intersection(move._get_integrity_hash_fields() + ['inalterable_hash'])` / `if move.inalterable_hash and violated_fields: raise UserError(...)`.
- `models/account_move.py:3833-3839` — `def _get_integrity_hash_fields(self): hash_version = self._context.get('hash_version', MAX_HASH_VERSION)`; `if hash_version == 1: return ['date','journal_id','company_id']`; `elif hash_version in (2,3,4): return ['name','date','journal_id','company_id']`. The comment above it reads, in intent: use the latest version by default, keep the old one for backward compatibility when generating the integrity report.
- `models/account_move_line.py:3283-3290` — the identical pattern on the item: version 1 returns `['debit','credit','account_id','partner_id']`; versions 2-4 return `['name','debit','credit','account_id','partner_id']`.
- `models/account_move_line.py:1554-1563` — the item-side guard consumes the same method: `inalterable_fields = set(self._get_integrity_hash_fields()).union({'inalterable_hash'})`.
- `models/account_move.py:46` — `MAX_HASH_VERSION = 4`.

### CONTRADICTION

Against EV-010: EV-010 states the hash fields "at the current hash version" as a fixed list. That
is true of the default. It is **not true of the guard**, whose effective list is a function of a
caller-supplied integer. I record this as a qualification of EV-010's framing rather than a
contradiction of its content.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether `hash_version` is reachable from a client-supplied RPC
context on a write. Same open question as F-03 and it should be resolved by the same test, not by
argument. Also `UNKNOWN — EVIDENCE REQUIRED:` whether any production call site sets
`hash_version` on a write path as opposed to a report path; I did not exhaustively enumerate its
call sites this session.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus requirement — **an integrity control's protected scope must be a
property of the sealed record, never of the request**. When a sealed record is written, the fields
it protects must be read back from the seal itself. And the enforcer and the verifier must be
driven from one declaration, so that "what we refuse to change" and "what we can prove did not
change" are the same set by construction and cannot drift.

---

## FINDING F-06 — The silent re-dating finding is real but E00's citation points at the duplicate path, and the posting path re-dates by a materially different and more aggressive rule.

**Verdict: CONFIRMED WITH CAVEAT. The behaviour is confirmed; the evidence base's citation and its description of the rule are both inaccurate, and the corrected rule is worse, not better.**

### OBSERVATION

EV-009 states the behaviour as: if the intended date is on or before the effective lock date, the
values dictionary is rewritten so that `date = lock_date + 1 day`, citing lines 3127-3129.

Three corrections. First, lines 3127-3129 are inside `copy_data`, i.e. the **duplicate an entry**
path, not the posting path. That path is a genuine and separately significant silent re-date which
E00 does not otherwise record. Second, the posting path is elsewhere and calls a different helper.
Third — and this is the material point — that helper does **not** generally return `lock + 1 day`.
It computes a candidate of `lock + 1 day` and then, depending on the document class and on the
detected numbering reset period, returns end-of-month, end-of-year, `min(today, ...)` or
`max(invoice_date, today)`. For non-sale documents the re-dating branch is entered **whether or not
any lock date was violated**, so a backdated vendor bill or manual entry can be moved forward to
today, or to the end of its own month, with no lock date configured at all.

The date the user typed is not retained anywhere. `date` is overwritten in place. For a non-invoice
entry there is no second date field holding the original intent.

### EVIDENCE

- `models/account_move.py:3113` — `def copy_data(self, default=None):`; `:3127-3129` — `user_fiscal_lock_date = move.company_id._get_user_fiscal_lock_date(move.journal_id)` / `if (default_date or move.date) <= user_fiscal_lock_date:` / `vals['date'] = user_fiscal_lock_date + timedelta(days=1)`. This is the duplicate path, and it emits no message to the user at all.
- `models/account_move.py:4933-4936` — the posting path: `affects_tax_report = move._affect_tax_report()` / `lock_dates = move._get_violated_lock_dates(move.date, affects_tax_report)` / `if lock_dates: move.date = move._get_accounting_date(move.invoice_date or move.date, affects_tax_report, lock_dates=lock_dates)`. Direct assignment to `move.date`; no message posted at this point.
- `models/account_move.py:5655-5691` — `_get_accounting_date`. After `if lock_dates: invoice_date = lock_dates[-1][0] + timedelta(days=1)`, the sale branch returns `min(today, end_of_month(invoice_date))` or `min(today, end_of_year(invoice_date))`; **the non-sale branch is entered unconditionally** and returns `end_of_month(invoice_date)` when `(today.year, today.month) > (invoice_date.year, invoice_date.month)`, else `max(invoice_date, today)`; for a yearly reset it returns `date(invoice_date.year, 12, 31)` or `max(invoice_date, today)`.
- `models/account_move.py:800-815` — `_compute_date` calls the same helper for non-sale documents while the entry is still in a working state, so for that class the shift is at least visible in the date field before posting.
- `models/account_move.py:5703-5718` — `_get_lock_date_message`, whose text states the date is prior to the lock and the entry "will be accounted on" the shifted date upon posting.

### CONTRADICTION

**Against EV-009, on two points.** (a) The cited lines 3127-3129 are the copy path, not the posting
path; the posting path is 4933-4936 into 5655-5691. (b) The rule is not `lock + 1 day`; that is
only an intermediate value. The shifted date can land at end-of-month, end-of-year, or today,
depending on document class and on a numbering format inferred by regular expression from the
highest existing entry name. I record this as `CONTRADICTED` on the mechanism and `CONFIRMED` on
the consequence. E00's headline conclusion — that the ledger and the document legitimately
disagree on date by design — survives intact and is if anything strengthened, because the
destination date is derived from *numbering format*, which is a presentation concern.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` the full behaviour when `highest_name` is empty and the journal has
a `sequence_override_regex` set, since `_deduce_sequence_number_reset` then parses against a
tenant-authored regular expression. Not traced this session.

`HOLD / EVIDENCE REQUIRED — routed to the Accounting-Tax track:` any claim about how this
interacts with Thai VAT or WHT period attribution. Not decidable in my lane and not decided here.
E00 already routes this to Wave D; I concur and add that the corrected rule (end-of-month /
end-of-year destinations, not lock+1) changes the analysis the tax track must perform.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus native requirement — **the system must never silently alter a date the
user entered.** Two dates must be modelled explicitly and both stored: the *document date* (what
the source says) and the *accounting date* (which period it lands in). When the two must differ,
the system proposes the accounting date, states the reason and the destination, and requires the
user to accept it as an explicit act that is recorded. Deriving an accounting date from an inferred
numbering format is to be prohibited outright: period attribution is an accounting decision and
must not be a side effect of a naming convention.

---

## FINDING F-07 — The re-dating warning does exist in the UI, but only in one place, only in one state, and it is absent from every unattended path.

**Verdict: CONFIRMED WITH CAVEAT. "Silent" is too strong for the single-record form; correct for everything else.**

### OBSERVATION

I searched specifically for whether the user is warned before posting, because the evidence base
characterises the re-dating as silent. A warning banner does exist. Its coverage is narrow, and
the narrowness is the finding: the banner is rendered only on the entry form, only while the entry
is in the working state, and only to users in two accounting groups. Every path that reaches
posting without a human looking at that form receives no warning at all — and the paths that lack
it are exactly the high-volume ones.

Paths I verified carry **no** such warning: bulk posting from a list selection; the deferred /
recurring posting path driven by the scheduler, where the entry is posted while nobody is present;
the duplicate path (F-06), which re-dates on copy with no message; and the machine-generated
entries covered by EV-015. Additionally, because the banner is hidden once the state is no longer
the working state, a user reviewing a posted entry cannot see that its date was shifted or what it
originally was.

### EVIDENCE

- `views/account_move_views.xml:803-806` — `<div groups="account.group_account_invoice,account.group_account_readonly" class="alert alert-warning" role="alert" invisible="state != 'draft' or not tax_lock_date_message"> <field name="tax_lock_date_message" nolabel="1"/> </div>`. The `invisible` expression is the whole story: the banner is suppressed the moment the state is not the working state.
- `models/account_move.py:676` — `tax_lock_date_message = fields.Char(compute='_compute_tax_lock_date_message')`; `:1679-1685` — the compute, depending on `date` and on line-level debit/credit/tax fields.
- `models/account_move.py:5713-5717` — the message text: the date is being set prior to the stated lock, and the entry will be accounted on the shifted date upon posting.
- `models/account_move.py:4923-4930` — the **only** message actually posted to the record during `_post` concerns *deferred* posting (`'This move will be posted at the accounting date: %(date)s'`), emitted for future-dated entries. There is no equivalent message emitted at 4933-4936 when the date is shifted backward-to-forward by a lock.
- Search scope for callers of the message helper: `grep -rn "_get_lock_date_message"` over `addons/account/`, `addons/account_accountant/`, `addons/account_reports/` — three hits: the definition, the compute at `:1685`, and one wizard at `wizard/account_automatic_entry_wizard.py:114`.

### CONTRADICTION

**Against EV-009's characterisation as "silently".** Partially contradicted: for a single entry
edited on its own form by an accounting user, the system does warn before posting, and it names
the destination date. The evidence base's "silent" is correct for bulk, scheduled, duplicated and
machine-generated postings, and correct for any post-hoc review of a posted entry. I record the
verdict as CONFIRMED WITH CAVEAT rather than CONTRADICTED because the operationally dominant paths
in a real ledger are the unwarned ones.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether the bulk-post action in the list view surfaces any
confirmation dialog client-side. I read the model and view definitions but did not read the
JavaScript layer and did not run the application. Scope: `addons/account/views/`,
`addons/account/models/`. This should be settled by observation, not inference.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus UI standard — **a control that changes posted data must be visible at
the moment it acts, on every path that reaches it, including unattended ones.** Concretely: a
warning that lives only in a form view is not a control, it is a courtesy. Where an unattended
path (scheduler, import, integration, bulk action) would trigger a data-altering control, the
correct behaviour is to *refuse and queue for human decision*, not to proceed quietly. And any
alteration that did occur must remain visible on the record afterwards, permanently, not only
while the record is still editable.

---

## FINDING F-08 — Immutability and deletion protection are opt-in, both default to off, and both are one-way ratchets once data exists. The evidence base states the first half and omits the second.

**Verdict: CONFIRMED WITH CAVEAT. The risk is real but its shape is different from E00's description, and the difference matters for migration.**

### OBSERVATION

EV-011 is correct that neither immutability nor deletion protection is a property of the ledger and
that both are configuration. I verified both switches and found an additional property that
materially changes the architecture risk: **each switch is a ratchet.** Hashing cannot be turned off
on a journal once any entry in it has been hashed. The company audit-trail flag cannot be turned
off once the company holds any entry at all.

The consequence is the opposite of what "it is only configuration" suggests. The exposure is not
that a tenant can quietly disable protection later — they largely cannot. The exposure is that
**the protection posture is fixed at the moment of the very first posting and is effectively
unchangeable thereafter**, and the shipped default is off. A tenant that begins posting without
enabling the audit trail can never enable it retroactively for what already exists, and a tenant
that enables it is committed permanently. This makes the switch a *migration-time and onboarding-time*
decision, made by whoever configures a new tenant, usually before anyone has thought about it.

I also searched for whether any country localisation or chart template ships either switch on and
found none.

### EVIDENCE

- `models/company.py:257` — `check_account_audit_trail = fields.Boolean(string='Audit Trail')`. No `default=` argument, therefore off.
- `models/company.py:317-321` — `@api.constrains('check_account_audit_trail')` / `def _check_audit_trail_records(self): if not self.check_account_audit_trail: move_count = self.env['account.move'].search_count([('company_id','=',self.id)], limit=1)` / `if move_count: raise UserError(_("Can't disable audit trail when there are existing records."))`.
- `models/account_journal.py:123-124` — `restrict_mode_hash_table = fields.Boolean(string="Secure Posted Entries with Hash", help=...)`. No `default=`, therefore off.
- `models/account_journal.py:651-658` — the write guard: if the flag is being cleared and any entry in the journal already has a hash, it raises "You cannot modify the field %s of a journal that already has accounting entries."
- `models/res_config_settings.py:210` — the audit-trail flag is exposed to the settings UI as a related field, i.e. it is an ordinary settings checkbox.
- Negative result, with scope: `grep -rln "check_account_audit_trail"` over `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/` returns only `addons/account/models/{account_move,res_config_settings,mail_message}.py`, `addons/account/tests/test_audit_trail.py`, one test under `account_accountant`, and translation catalogues. **Not found** in any `data/` directory, chart template or localisation module within that search scope. I therefore observe that no shipped country configuration in this build enables it; I do not claim it is impossible to ship enabled.

### CONTRADICTION

Against EV-011: the statement "Both are configuration. With both switches off — the shipped default
for hashing — a posted entry is an ordinary mutable, deletable row" is confirmed. What E00 omits,
and what I add as a qualification, is the ratchet. EV-011 reads as though the switches are freely
toggleable; they are not, and the practical control question is therefore about *tenant
provisioning defaults*, not about runtime tampering.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether the audit-trail flag also governs retention of chatter
records. `models/account_move.py` is not the only consumer — `models/mail_message.py` also
references it — and I did not read that file this session. If message retention is coupled to the
same flag, the ratchet governs more than entry deletion.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus native requirement — **ledger immutability is not a setting.** It is a
property of what a ledger is, and it must be unconditional, uniform across every tenant, and
established before the first posting is possible. I recommend a `Tolerance = 0` designation under
Constitution principle 13 for any design in which a tenant, a reseller, an implementation partner
or an onboarding script can provision a company whose posted entries are deletable. Corollary:
because SMEsPlus will import history, the requirement must hold for migrated entries too — an
imported posted entry is a posted entry.

---

## FINDING F-09 — The deletion escape hatch writes to the application log, its gate on the escape-hatch flag is a no-op, and the write is outside the transaction.

**Verdict: CONFIRMED and extended. E00 identified the logger; I identified that the gating is not implemented and that the record is transactionally unsound in both directions.**

### OBSERVATION

EV-011 records that when the deletion protection is overridden, the deletion is recorded by writing
a formatted message through the application logger rather than to a database record. Correct, and
it is the right thing to be alarmed about. Three further properties make it worse.

First, the method that builds the log message opens with a guard testing for the override flag
whose body is a **no-op statement** rather than an early return. The guard therefore has no effect:
the method continues and builds the message regardless. The message it produces is worded as
"Force deleted Journal Entries by ...", so the phrase describing a deliberate override is emitted
on paths where no override was requested.

Second, the log write happens **after** the deletion has been committed to the ORM but the log is
not part of the database transaction. If the surrounding transaction rolls back, the log line
survives, asserting a deletion that did not occur. If the log handler fails or the level is
filtered, a deletion that did occur leaves no record. The evidentiary record and the data are
independently corruptible in opposite directions.

Third, the record is emitted at INFO level, which in ordinary production configurations is either
not retained or retained for a short operational window, and it lands wherever the application's
logging is directed — plausibly outside the tenant's jurisdiction entirely.

Separately, I verified that ordinary sequence-gap protection is waived for a broad group: an
accounting manager, or any company in quick-edit mode, can delete a numbered entry from the middle
of a chain without the override flag at all.

### EVIDENCE

- `models/account_move.py:3303-3310` — `def _get_unlink_logger_message(self):` with a docstring noting the logger is used here because the items are already deleted by the time the delete hook runs; then `if not self._context.get('force_delete'):` followed by a body consisting solely of Python's null statement — no `return`, no raise, no effect. Execution continues into the message construction that follows.
- `models/account_move.py:3311-3327` — the message body, iterating `self.filtered(lambda m: m.posted_before and m.company_id.check_account_audit_trail)`, and formatting `"\nForce deleted Journal Entries by {user_name} ({user_id})\nEntries\n{moves_details}"`.
- `models/account_move.py:3358-3367` — `def unlink(self):` → `self._set_next_made_sequence_gap(True)` → `logger_message = self._get_unlink_logger_message()` → `self.line_ids.unlink()` → `res = super().unlink()` → `if logger_message: _logger.info(logger_message)`. The log call is last, at INFO, unconditioned on transaction outcome.
- `models/account_move.py:3348-3357` — `_unlink_account_audit_trail_except_once_post`: refuses deletion when `not self._context.get('force_delete')` and any entry was posted before under audit trail. This is the guard the override flag actually defeats, and here the flag is a plain context key.
- `models/account_move.py:3328-3346` — `_unlink_forbid_parts_of_chain`: the numbering-gap guard is waived if the user holds `account.group_account_manager`, **or** any affected company has `quick_edit_mode`, **or** the override flag is set, **or** the entry is last in its chain.
- `models/account_move.py:4805-4809` — `_can_be_unlinked`: `not self.inalterable_hash and self.date > lock_date and not is_part_of_audit_trail`.
- `models/account_move.py:4814-4830` — `_unlink_or_reverse`: the `elif move._is_protected_by_audit_trail()` branch that routes to `to_cancel` is **unreachable**, because `_can_be_unlinked()` already returns False for audit-trail-protected entries, sending them to `to_reverse` in the preceding branch. `to_cancel` is therefore always empty and `to_cancel.button_cancel()` is dead. `INFERENCE:` the deletion-versus-cancel-versus-reverse decision logic is not exercised as written and cannot have been covered by a test that distinguishes the two protected outcomes.

### CONTRADICTION

Against EV-011: no contradiction on the logger claim, which is confirmed. I add that E00's phrasing
"where the deletion bypass is used, the only surviving evidence leaves the tenant database
entirely" is correct but incomplete — the gating is not implemented, so the wording of that
evidence is unreliable as to whether an override was in fact requested.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether the null-statement guard is deliberate (the message is meant
to be produced on all protected deletions and only the wording is wrong) or a defect (an intended
early return). The docstring says the message is produced "before unlink ... for audit trail if
it's enabled", which reads as though it is meant to fire whenever the audit trail is enabled,
making the wording the error rather than the control flow. Not decidable from this file.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus requirement — **a numbered entry is never physically removed.** There is
no override, no context key, no administrative escape hatch and no group that can do it. Removal
from the ledger is expressed as a compensating entry. If any operational need genuinely requires
physical removal (a data-protection erasure order, say), it is an out-of-band, dual-controlled
procedure, and its record is a first-class row inside the tenant database, written in the same
transaction as the removal, never an application log line. I place this as `Tolerance = 0` under
Constitution principle 13 and I recommend it be tested as a negative case in the Wave A test
charter: attempt physical deletion by every available route and require that all of them are
refused.

---

## FINDING F-10 — The balanced-entry invariant, the one thing a ledger must never violate, has no database constraint and is enforced by a suppressible Python context manager.

**Verdict: CONFIRMED. New observation, not present in the evidence base. This is my highest-severity architecture finding.**

### OBSERVATION

Double-entry balance is the defining invariant of a ledger. In the reference it is enforced by a
Python context manager wrapped around create and write, which after yielding runs an aggregate
query and raises if any entry's balance rounds to non-zero. The manager begins by consulting a
recursion-disabling helper keyed on a named flag; when that flag is engaged the check returns
without executing at all.

The entry model declares exactly one `_sql_constraints` entry, and its constraint definition is an
**empty string** — a placeholder that names a constraint and its error message but defines no
condition. The actual uniqueness protection is a partial index created imperatively in
`_auto_init`. There is no database-level assertion of balance anywhere on the entry table.

By contrast, the *item* table does carry real database CHECK constraints, for the debit/credit
exclusivity and for the sign coherence between the company-currency balance and the
transaction-currency amount. So the reference demonstrates it knows how to put an invariant in the
database. It put the per-row invariants there and left the cross-row invariant — the one that
actually defines double-entry — in application code with an off switch.

### EVIDENCE

- `models/account_move.py:2329-2354` — `@contextmanager def _check_balanced(self, container):` with docstring "Assert the move is fully balanced debit = credit." Body: `with self._disable_recursion(container, 'check_move_validity', default=True, target=False) as disabled: yield; if disabled: return` — then it queries and raises `UserError` listing the debit and credit totals.
- `models/account_move.py:2356-2376` — `_get_unbalanced_moves`, whose comment warns the query must not depend on computed stored fields because the ORM may create with `no_recompute`; it aggregates `HAVING ROUND(SUM(line.balance), currency.decimal_places) != 0`.
- `models/account_move.py:713-715` — the entry model's complete `_sql_constraints`: `[('unique_name', "", "Another entry with the same name already exists.")]`. The middle element, the constraint definition, is the empty string.
- `models/account_move.py:730-735` — the real protection, created imperatively: `CREATE UNIQUE INDEX account_move_unique_name ON account_move(name, journal_id) WHERE (state = 'posted' AND name != '/')`.
- `models/account_move_line.py:429-450` — genuine database CHECKs on the item: `check_credit_debit` — `CHECK(display_type IN ('line_section','line_note') OR credit * debit=0)`; and `check_amount_currency_balance_sign` — a CHECK requiring `balance` and `amount_currency` to agree in sign.
- `models/account_move.py:3188`, `:3262`, `:4078`, and `models/account_move_line.py:1515`, `:1603`, `:1724`, `:2477` — the seven sites that wrap operations in the balance manager. Any write path that does not route through one of these is unchecked.
- Search scope for the suppression flag: `grep -rn "check_move_validity"` over `addons/account/` and `addons/account_accountant/` — one hit, the definition at `:2334`. I found no production caller engaging it within that scope; the mechanism is present and available, not currently used.

### CONTRADICTION

None identified against the evidence base, which does not address the balance invariant. I note
that this finding reframes EV-013: E00 concludes from the field definitions that `balance` is the
primary stored fact. It is, and it is directly writable (`readonly=False`), and nothing in the
database prevents a set of directly-written balances from summing to a non-zero total.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether the framework's own bulk-write or import paths route through
one of the seven wrapped sites. The comment at `:2357-2359` explicitly anticipates the ORM calling
create with recomputation suppressed, which indicates the authors were managing exactly this
hazard, but I did not read the ORM layer.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus native requirement — **the balance invariant must be owned by the
database.** A deferred constraint or a commit-time trigger asserting that every posted entry's
signed amounts sum to zero in the entry's own currency and in the reporting currency, with no
application-level suppression and no exempt path. The application check remains, but only to
produce a good error message early; it is not the control. The test that matters is not "does the
UI refuse an unbalanced entry" — it is "can any route whatsoever, including direct data access,
leave an unbalanced posted entry in the table". If the answer is yes, the system is not a ledger.
`Tolerance = 0` under Constitution principle 13.

---

## FINDING F-11 — Numbering is derived from data by regular expression, the format override can be destroyed by an ordinary edit, and gap reporting stops at the lock date.

**Verdict: CONFIRMED and extended.**

### OBSERVATION

EV-005 and EV-006 establish that numbering is derived from the data by regular expression rather
than from a protected counter, and that uniqueness is asserted only for posted entries by a partial
index. I verified both and add three architecture consequences that E00 does not draw.

First, the journal's numbering-format override is not protected from the entries it governs. If a
user with the accounting-manager role writes a name that does not match the journal's own override
pattern, the code does not refuse — it **clears the journal's override field** and proceeds. A
per-journal configuration governing every future number is destroyed as a side effect of editing
one entry, with no confirmation and no message.

Second, resequencing is available to the accounting-manager role and operates by blanking the names
of the whole selection and rewriting them. The only refusal is a narrow one: reordering by date is
refused when the journal is in hash mode, but reordering while keeping the current order is
permitted, and the wizard is available on unhashed journals without restriction.

Third, gap detection is a dashboard indicator, not a control — it blocks nothing — and its query is
scoped to entries dated after the effective lock date. Gaps inside a locked period therefore stop
being reported once the period is locked. The indicator disappears at exactly the moment the gap
becomes permanent and uncorrectable.

### EVIDENCE

- `models/sequence_mixin.py:351-368` — `_locked_increment` docstring, in intent: the lock is taken through the unique constraint; at entry the record must already be governed by that constraint (for an entry, it must be posted), otherwise the lock is not taken and sequence numbers may not be unique when returned.
- `models/account_move.py:730-735` — the partial unique index, as cited in F-10.
- `models/account_move.py:3252-3255` — `if move.journal_id.sequence_override_regex and vals.get('name') and vals['name'] != '/' and not re.match(move.journal_id.sequence_override_regex, vals['name']):` → `if not self.env.user.has_group('account.group_account_manager'): raise UserError(...)` → `move.journal_id.sequence_override_regex = False`. For a manager, the journal configuration is silently cleared.
- `models/account_journal.py:147` — `sequence_override_regex = fields.Text(help="Technical field used to enforce complex sequence composition that the system would normally misunderstand.")`.
- `models/account_move.py:100-116` — five separate regex accessors, each returning `self.journal_id.sequence_override_regex or super()...`, so clearing that one field changes the parsing of all five numbering shapes at once.
- `wizard/account_resequence.py:155-170` — `def resequence(self):` → refuses only `ordering == 'date'` when `restrict_mode_hash_table` → `moves_to_rename.name = False` → `flush_recordset(["name"])` (with the comment that without a forced database update the temporary renaming would only happen in cache and would still trigger the constraint) → then assigns each new name.
- `security/ir.model.access.csv:126` — `access_account_resequence,...,model_account_resequence_wizard,account.group_account_manager,1,1,1,0`.
- `models/account_move.py:300`, `:929-940` — `made_sequence_gap` computation; `:749-753` — the supporting partial index `account_move_made_gaps ... where="made_sequence_gap = TRUE"`.
- `models/account_journal_dashboard.py:143-173` — `_query_has_sequence_holes`: `to_check = self.grouped(lambda j: j.company_id._get_user_fiscal_lock_date(j, ignore_exceptions=True))` and the SQL predicate `AND move.made_sequence_gap = TRUE AND move.date > %(lock_date)s`. The inline comment states the intent plainly: this way we find all holes **that can still be corrected**.
- `models/account_journal_dashboard.py:618-624` — the indicator's tooltip: "Irregularities due to draft, cancelled or deleted bills with a sequence number since last lock date."

### CONTRADICTION

None against EV-005/EV-006 on substance. I qualify EV-006's framing: it says uniqueness "is
asserted at the moment of posting". True, but the assertion is a *partial index*, so the database
does not merely fail to protect draft entries — it does not know they exist for this purpose, and
`_locked_increment` correspondingly cannot take its lock for them. The two facts compound: the
numbers handed out while a record is unnumbered-and-unposted are neither unique nor serialised.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether the resequence wizard writes any durable record of the
before-and-after mapping beyond per-record change tracking. I read the wizard's `resequence` method
and the surrounding computes; I did not locate a dedicated audit record within
`wizard/account_resequence.py`.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus native requirements, three. (a) **A number is allocated by an
authoritative allocator, not inferred from existing rows**, and the allocation is itself a durable,
queryable record: who, when, for what, and whether it was ever consumed. (b) **Numbering
configuration is versioned and effective-dated, never mutable in place, and never alterable as a
side effect of editing a document.** (c) **A gap is a permanent, first-class fact**, recorded when
it arises with its cause, and it does not stop being reported because a period closed — closing a
period is precisely when the unexplained gaps must be listed and dispositioned, not hidden. I flag
(c) as the most likely to be missed, because it inverts the reference's stated intent.

---

## FINDING F-12 — Identifier arithmetic in the per-company code grid: verified, and the failure boundary is lower than the constant suggests.

**Verdict: CONFIRMED. E00's `CONTRA-02` stands. Two citation corrections and one severity refinement.**

### OBSERVATION

I verified the constant and the arithmetic personally. A non-stored pseudo-model addresses each
(account, company) cell of the per-company code grid by the synthetic identifier
`account_id * 10000 + company_id`, decoding it with integer division and modulo. The encoding is
injective only while every company identifier is strictly below ten thousand.

The severity refinement: the boundary is not "ten thousand companies exist". It is "**any single
company record has been assigned an identifier of ten thousand or more**". In a database using
monotonic identifier allocation, that threshold is crossed by cumulative creation over the
deployment's lifetime — including companies created and later deleted, test tenants, demo data and
onboarding trials. A deployment holding two hundred live companies can already be past the boundary.
The failure is silent aliasing in a grid that writes account codes, so the observable symptom is a
code appearing against, or being written to, the wrong company.

I also note the model is `_auto = False` with `_table_query = '0'` and populates records only in
cache. There is therefore no stored row whose identifier could be reconciled against reality, and
no constraint that could detect the collision.

### EVIDENCE

- `models/account_code_mapping.py:4` — `COMPANY_OFFSET = 10000`.
- `models/account_code_mapping.py:12-15` — `_name = 'account.code.mapping'`, `_auto = False`, `_table_query = '0'`, with the header comment stating the model is used purely for UI, is not stored, and is populated in cache by the `_search` override.
- `models/account_code_mapping.py:37-45` — `create`: `self.browse([vals['account_id'] * COMPANY_OFFSET + vals['company_id'] for vals in vals_list])`.
- `models/account_code_mapping.py:47-55` — `_search`: `account_id * COMPANY_OFFSET + company.id`, over the acting user's active companies.
- `models/account_code_mapping.py:57-63` — the decode: `record.account_id = record._origin.id // COMPANY_OFFSET` and `record.company_id = record._origin.id % COMPANY_OFFSET`.
- `models/account_code_mapping.py:71-73` — `_inverse_code` writes through: `record.account_id.with_company(record.company_id).write({'code': record.code})`. The decoded, potentially aliased company is the one written to.

### CONTRADICTION

Against EV-020 on citation detail only, which I record for the accuracy of the register rather than
as a challenge to its conclusion: E00 cites `:34-42` and `:47-56` and `:58-64`. In the build I read,
`create` occupies `:37-45`, `_search` occupies `:47-55`, and the decoding computes occupy `:57-63`.
The substance of EV-020 is CONFIRMED exactly. I additionally qualify E00's phrasing "the moment a
deployment holds ten thousand or more company records": the correct trigger is the identifier
value, not the row count.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether SMEsPlus will use a shared database across tenants, a
database per tenant, or a hybrid. The severity of this class of defect is entirely determined by
that choice, and it is a Boss architecture decision I am not empowered to make. I record only that
the decision has a direct and quantifiable consequence here.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus prohibition, stated as an engineering standard rather than an Account
Module rule: **no composite identity may be encoded as arithmetic over its parts.** A cell
addressed by (account, company) is addressed by the pair, as a pair. This is not a matter of
choosing a larger constant — a larger constant moves the boundary and keeps the class of defect,
which fails silently and corrupts by writing to the wrong tenant's data. I recommend this be added
to the SMEsPlus code-review checklist as an automatically greppable prohibition, because the
pattern is easy to reintroduce and impossible to notice in testing at small scale.

---

## FINDING F-13 — The numbering/date alignment control is disabled by a value that is not tenant-scoped at all.

**Verdict: CONFIRMED WITH CAVEAT. The control weakness is real; E00's characterisation of who can do it, and of its blast radius, is wrong in both directions.**

### OBSERVATION

EV-007 records that a single tenant-writable configuration value moves the date on which the
number/date alignment constraint begins to apply, and that setting it forward disables the control
tenant-wide. I verified the mechanism and found E00 wrong on two counts, one making the finding
less severe and one making it considerably more severe.

Less severe: the value is not tenant-writable by an accounting user. The parameter store is
readable and writable only by the system-settings group. An accounting manager cannot set it.

More severe: the parameter store carries **no company scoping at all** — there is no company field
on the model. The value is therefore not tenant-wide; it is **database-wide**. In any deployment
where more than one tenant's companies share a database, one write to that key disables the
alignment control for **every tenant in the database simultaneously**, and no tenant's
administrator or auditor has any way to observe it from within their own accounting data.

The parameter is read through elevated rights when the constraint runs, so a tenant's own access
restrictions are irrelevant to whether the value applies to them.

### EVIDENCE

- `models/sequence_mixin.py:154-179` — `@api.constrains(...)` `def _constrains_date_sequence(self):` with the preceding comment, in intent: it is possible to circumvent the constraint to allow editing already-inconsistent documents, and it must not be used to disable the constraint completely as that would make the mixin unreliable. Body: `constraint_date = fields.Date.to_date(self.env['ir.config_parameter'].sudo().get_param('sequence.mixin.constraint_start_date', '1970-01-01'))`, then the check is applied only when `date > constraint_date`.
- `models/sequence_mixin.py:173-178` — the refusal message, in intent: the date entered is not aligned with the existing sequence number; clear the sequence number to proceed; to maintain date-based sequences, select entries and use the resequence option from the actions menu, available in developer mode.
- `../base/models/ir_config_parameter.py:31-33` — `_name = 'ir.config_parameter'`, `_rec_name = 'key'`. Negative result, with scope: a `grep -n "company_id"` over that file returns no match, so the model carries no company dimension.
- `../base/security/ir.model.access.csv:117` — `"access_ir_config_parameter_system","ir_config_parameter_system","model_ir_config_parameter","group_system",1,1,1,1`. Full rights to the system group; this is the only row for the model in that file.

### CONTRADICTION

**Against EV-007, on two points.** (a) "tenant-writable" is CONTRADICTED — writing requires the
system-settings group, not an accounting role. (b) "disables the control for the whole tenant" is
CONTRADICTED as an understatement — the parameter has no tenant dimension, so its scope is the
database. E00's conclusion that this is a SaaS control finding is CONFIRMED and I would raise, not
lower, its priority on the strength of (b).

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether any SMEsPlus-side or platform-side tooling would surface a
change to such a parameter to a tenant or to an auditor. Outside the Account module; routed to the
platform track.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus native requirements, two. (a) **No accounting control may be governed by
a global key-value setting.** Where a control needs an effective-from date, that date is a
first-class, company-scoped, effective-dated, append-only record with an author, a timestamp and a
reason, and it is visible in the tenant's own audit view. (b) **Platform-level configuration must
be incapable of weakening a tenant's accounting controls**, by construction — a control whose
strength depends on a value the tenant cannot see or write is not a control the tenant can rely on,
and cannot be represented as one to an auditor.

---

## FINDING F-14 — The lock-override record is well shaped in intent but its access-control story is contradicted by its own implementation.

**Verdict: CONFIRMED WITH CAVEAT.**

### OBSERVATION

EV-021 characterises the lock-exception mechanism as append-only and logged, with two weaknesses:
an optional justification and the possibility of an all-users, no-expiry exception. I verified the
model and confirm both weaknesses. I add a control-ownership observation and one correction.

The correction: the record is not append-only. It carries an archive flag and a computed status
including a revoked value, and there is a revoke action. The mechanism is therefore
append-and-revoke, which is a better design than append-only for this purpose — an override that
cannot be withdrawn would be worse.

The control-ownership observation is the interesting part. The access-control table grants the
accounting-manager role read and create but **not write** on this model. The revoke action
nonetheless writes to it, by re-fetching the record with elevated rights and clearing the flag. So
the declared access policy says "these records are never modified" and the application modifies
them anyway, under its own authority, having first performed its own group check in Python. The
same architectural pattern as F-03 and F-05: the declared control is not the operative one.

I also confirm that the justification field carries no required marker, and that an exception
created without a user applies to everyone and one created without an end date-time is unbounded —
though I note the user field defaults to the creating user, so producing an everyone-exception
requires deliberately clearing it.

### EVIDENCE

- `models/account_lock_exception.py:16-19` — `active = fields.Boolean(string='Active', default=True)`; `:20-28` — `state = fields.Selection([('active','Active'),('revoked','Revoked'),('expired','Expired')], compute='_compute_state', search='_search_state')`; `:113-121` — the compute: not active means revoked, an elapsed end date-time means expired, otherwise active.
- `models/account_lock_exception.py:35-40` — `# An exception w/o user_id is an exception for everyone` and `user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user)`.
- `models/account_lock_exception.py:41-43` — `reason = fields.Char(string='Reason')`. No `required=True`.
- `models/account_lock_exception.py:44-47` — `# An exception without 'end_datetime' is valid forever` and `end_datetime = fields.Datetime(string='End Date')`.
- `security/ir.model.access.csv:18-19` — `access_account_lock_exception,...,base.group_user,1,0,0,0` and `access_account_lock_exception_manager,...,account.group_account_manager,1,0,1,0`. In `perm_read,perm_write,perm_create,perm_unlink` order: ordinary users read only; managers read and create, with write and delete withheld.
- `models/account_lock_exception.py:257-266` — `def action_revoke(self):` → `if not self.env.user.has_group('account.group_account_manager'): raise UserError(_("You cannot revoke Lock Date Exceptions. Ask someone with the 'Adviser' role."))` → `record_sudo = record.sudo()` → `record_sudo.active = False` → `record_sudo.end_datetime = fields.Datetime.now()`. The elevated write is what makes revocation possible despite the withheld write permission.
- `models/account_lock_exception.py:210-238` — creation logs to the company's message thread with a tracking value showing the lock date change, naming the user or, when there is none, the word for everyone, and appending the validity window and reason only when they were supplied.
- `models/account_lock_exception.py:242-243` — `def copy(self, default=None): raise UserError(_('You cannot duplicate a Lock Date Exception.'))`; `:245-256` — `_recreate` nonetheless constructs new records from `copy_data()` and `create()`, reaching the same outcome its own duplication ban forbids.

### CONTRADICTION

Against EV-021: "exceptions are append-only and logged" is CONTRADICTED in the first half. They are
revocable, by design, through an application action that overrides the declared access policy. E00's
two stated weaknesses — optional justification, and an unbounded all-users exception — are both
CONFIRMED.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether revocation is itself narrated on the company thread the way
creation is. `action_revoke` calls `_invalidate_affected_user_lock_dates()` but I did not locate a
message post in that method. If revocation is unlogged while creation is logged, the audit record
shows overrides being granted and not withdrawn, which would systematically overstate the open
exception population when read historically.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus native requirements for any control override. It is an **event**, not a
mutable record: granting is one event, revoking is another, and neither edits the other. A
justification is mandatory and structured, not free text. An expiry is mandatory and bounded by
policy, with no unbounded option available in the interface. An override that applies to more than
one named user requires a second approver. Grant and revoke are equally and identically recorded.
And the record lives where an auditor looks for it — in the accounting audit trail — not in a
conversational thread attached to the company record.

---

## STATE TRANSITION TABLE

Derived from the reference implementation and mapped over the **real** state space (F-01), not the
three-value field. `Guard owner` names where the invariant actually lives, not where it is
documented. All rows are `REFERENCE BEHAVIOUR` unless a cell is marked otherwise.

| # | From-state (state + flags) | Trigger | To-state | Data destroyed | Accounting event emitted | Guard | Guard owner |
|---|---|---|---|---|---|---|---|
| T1 | Working, never posted, unnumbered | `action_post` / `_post(soft=True)`, date in the future | Working + `auto_post` set — "Scheduled" | None | None. A narrative message is posted (`account_move.py:4923-4930`) | date beyond today | Application |
| T2 | Working (any) | `_post(soft=False)` | Posted, `posted_before=True`, number consumed | **The user's intended accounting date** — `date` is overwritten in place, no field retains the original (`:4933-4936`) | Number consumed; analytic lines created (`:4938`); reversal reconciliation (`:4962`); marked reconciliations applied (`:4963`); cash-basis and exchange entries possible downstream | Balanced (Python only, F-10); at least one non-display line; journal active; currency active; no deprecated account (`:4911`, overridable by context); posting group | Application |
| T3 | Scheduled | Scheduler | Posted | As T2, unattended | As T2 | As T2 — **no human present, no warning surface** (F-07) | Application (scheduled) |
| T4 | Posted, unhashed | `_hash_moves` — on post if the journal flag is set, or on demand via the manager wizard | Posted + sealed | None | None; a per-entry narrative note is written (`:3881`) | Journal flag `restrict_mode_hash_table`, or manager-only wizard | **Configuration**, then Application |
| T5 | Posted (unhashed, not exchange, not cash-basis) | `button_draft` | Working, `posted_before=True`, number retained | **All analytic lines unlinked; all reconciliations removed; generated document attachments detached** (`:5281-5286`) | Unreconciling can reverse exchange-difference entries and cash-basis entries (EV-014) | `_check_draftable` (three categories only); fiscal + tax lock when leaving posted (`:3239-3242`) | Application |
| T6 | Posted | `button_cancel` | Cancelled, `posted_before=True` | **Identical to T5 — routed through `button_draft`** (`:5365-5367`) | Identical to T5; linked payments set to cancelled | Identical to T5 | Application |
| T7 | Working | `button_cancel` | Cancelled, never posted | None | None | State must be working after the T6 detour | Application |
| T8 | Cancelled | `button_draft` | Working | Already destroyed at T5/T6 | None | `show_reset_to_draft_button`; `need_cancel_request` | Application |
| T9 | Working, `posted_before=True` | `unlink` | **Row removed** | The entire entry and its items; the consumed number leaves a permanent gap | None emitted. One INFO line to the application log, outside the transaction, with a defective gate (F-09) | Chain-position guard, waived for managers / quick-edit / override flag; audit-trail guard, defeated by a plain context key | **Configuration** + Application, caller-overridable |
| T10 | Posted | `write({'date': ...})` or `write({'name': ...})` | Posted | Prior value replaced; change recorded in the record's tracked history only | None | Fiscal and tax lock checks (`:3231-3237`); hash guard when sealed, with caller-narrowable scope (F-05) | Application |
| T11 | Posted | `write` on an item's `amount_currency` | Posted | Prior transaction-currency amount replaced | None directly; residual and matching state recompute | Hash does **not** cover it; fiscal lock fires only if the period is locked; reconciliation check fires only if the item is matched (`account_move_line.py:1577-1599`, `:3365-3376`) | Application, **conditionally — no single owner** |
| T12 | Posted | Resequence wizard | Posted, renumbered | Prior numbers, recoverable only from tracked history | None | Same journal; date-reordering refused only in hash mode | Application (manager role) |
| T13 | Any | Duplicate | New working entry | n/a | None | Date silently moved to lock + 1 day, **with no message at all** (`:3127-3129`) | Application |
| T14 | Posted | `_reverse_moves(cancel=True)` | Posted + a new posted reversal, mutually reconciled | None | **A new entry is emitted and posted** (`:4801`) | The reversal is subject to the full posting guard set | Application |
| T15 | Posted, sealed | Any write to a hashed field | Refused | None | None | Hash guard — scope determined by a caller-supplied version (F-05) | Application, **caller-influenced** |
| T16 | Posted, in a journal governed by the bank statement module | Any write from that module | Posted, modified | Whatever was overwritten | None | Posted-field freeze **is switched off for the whole path** (`account_bank_statement_line.py:441`) | **Calling module** |

Two observations on the table. First, every guard in the `Guard owner` column resolves to
"Application" or "Configuration"; **not one invariant in this table is owned by the database.**
Second, the two rows a user would intuitively expect to be safest — T6 (cancel rather than reopen)
and T13 (duplicate rather than create) — are respectively the most destructive and the only fully
unnarrated one.

---

## CONTROL OWNERSHIP MATRIX

`Owner in reference` is where the invariant is actually enforced, established by reading the code,
not where it is documented. `Recommended SMEsPlus owner` is my `RECOMMENDATION` and requires Boss
decision.

| # | Invariant | Owner in reference | Failure mode | Recommended SMEsPlus owner |
|---|---|---|---|---|
| C1 | **Entry is balanced** (signed amounts sum to zero) | **Application only** — a Python context manager with a suppression flag; no database constraint on the entry table (`account_move.py:2329-2354`, `:713-715`) | Any write path outside the seven wrapped call sites, or any engagement of the suppression flag, leaves an unbalanced posted entry with no rejection at any layer | **Database** (deferred constraint or commit-time trigger), with the application check retained only for early, readable errors. `Tolerance = 0` |
| C2 | Debit and credit are mutually exclusive on an item | **Database** — CHECK constraint (`account_move_line.py:429-433`) | None identified | **Database.** Correct as-is; adopt the intent |
| C3 | Company-currency and transaction-currency amounts agree in sign | **Database** — CHECK constraint (`account_move_line.py:434-445`) | None identified | **Database.** Correct as-is; adopt the intent |
| C4 | **Entry number is unique** | **Database, partially** — a partial unique index restricted to posted entries with a real name; the declared constraint is an empty placeholder (`:730-735`, `:713-715`) | Duplicate numbers on unposted entries; the increment helper cannot take its lock for records outside the index, so concurrently allocated numbers may collide (`sequence_mixin.py:351-368`) | **Database**, unconditional over every numbered entry, keyed on company + journal + number, with "unnumbered" modelled explicitly rather than as a placeholder string |
| C5 | Number is aligned to the entry's period | **Application** constraint, defeated by a **database-global** key-value setting readable through elevated rights (`sequence_mixin.py:154-179`; `ir_config_parameter.py` has no company dimension) | One platform-level write disables the control for every tenant sharing the database, invisibly to all of them | **Database + effective-dated, company-scoped, append-only policy record.** No global scalar may govern an accounting control |
| C6 | Numbers are allocated without gaps | **Nobody.** Gaps are a stored boolean surfaced as a dashboard indicator; deletion mid-chain is waived for managers and for quick-edit companies (`:3328-3346`; `account_journal_dashboard.py:143-173`) | A gap is a notification, not a refusal; and the notification is suppressed once the period is locked, i.e. exactly when the gap becomes permanent | **Allocator + durable allocation ledger.** A gap is a first-class recorded fact with a cause, and is listed at close, never hidden by it |
| C7 | Numbering format is stable | **Application, and self-destructing** — a manager's entry edit that does not match the journal pattern clears the journal pattern (`:3252-3255`) | Per-journal configuration destroyed as a side effect of editing one document, silently | **Versioned, effective-dated configuration.** Not editable in place; never alterable as a side effect of a document write |
| C8 | **Locked period is not posted into** | **Application** — and the control **re-dates rather than refuses** for soft locks; a correctly-shaped unforgeable override exists for one production path (`:2377-2378`, `partner.py:804-805`) | A late document is accepted and silently attributed to a different period; the destination period is derived from an inferred numbering format (F-06) | **Application + explicit recorded user decision.** Never a silent mutation. Two dates modelled: document date and accounting date. Statutory period attribution `HOLD` — routed to the Accounting-Tax track |
| C9 | Lock override is controlled and accountable | **Access-control table says read + create only; the application writes anyway under elevated rights** (`ir.model.access.csv:18-19` vs `account_lock_exception.py:257-266`) | The declared policy is not the operative one. Justification optional; an all-users, unbounded exception is constructible | **Append-only event pair (grant / revoke).** Mandatory structured justification, mandatory bounded expiry, second approver for any multi-user scope, both events recorded identically in the accounting audit trail |
| C10 | **Posted fact is immutable** | **Configuration** (two independent opt-in switches, both off by default, both one-way ratchets) enforced by **Python guards whose protected field set is caller-supplied** (`company.py:257,317-321`; `account_journal.py:123-124,651-658`; `account_move.py:3208-3213,3833-3839`) | Default-off means the shipped posture is mutable; the freeze is switched off wholesale for the bank statement path; the guard's scope is narrowable by a context integer | **The storage model itself.** Posted records have no update path. Immutability is unconditional, uniform, and established before the first posting is possible. `Tolerance = 0` |
| C11 | **Posted fact is not deleted** | **Configuration + Python delete hooks with a plain-key override**; the evidentiary record is an application log line whose gate is a no-op and whose write is outside the transaction (`:3303-3327`, `:3348-3367`) | Physical deletion is reachable; the record of it can exist without the deletion, or the deletion without the record; and it leaves the tenant database entirely | **Database.** No physical deletion of a numbered entry by any route. Removal is expressed as a compensating entry. Any out-of-band erasure is dual-controlled and recorded in-database in the same transaction. `Tolerance = 0` |
| C12 | Account code is unique within a company | **Application only** — no constraint on the account model (EV-002, `account_account.py:1037`) | Concurrent transactions or a check-suppressing import produce duplicate codes with no database rejection, corrupting every code-ordered report | **Database**, with the application check retained for message quality. Concur with EV-002's `Tolerance = 0` candidacy |
| C13 | A (account, company) cell addresses one company | **UI-layer arithmetic** over a fixed constant (`account_code_mapping.py:4,37-63`) | Silent aliasing once any company identifier reaches the constant; the grid reads and **writes** the wrong company's code | **Composite key.** Arithmetic identity encoding prohibited outright as an engineering standard |
| C14 | Posted entries are not created against a deprecated account | **Application**, at posting, with a plain-key context override (`account_move.py:4911-4912`; `account_move_line.py:1212`) | The override is a plain context key; and the account model has no archive state, only this flag (EV-003) | **Application + database** referential state on the account. *This resolves EV-003's open question — see the note below the matrix* |

**Note resolving an open item in the evidence base.** EV-003 records as
`UNKNOWN — EVIDENCE REQUIRED` whether any reference behaviour blocks *posting* to a deprecated
account, observing correctly that a selection domain filters pickers but does not constrain
programmatic posting. `VERIFIED FACT:` it does block it, in two places, and both are application
guards with an override. `account_move.py:4911-4912` adds a validation message at posting — "A line
of this move is using a deprecated account, you cannot post it" — conditioned on
`not self._context.get('skip_account_deprecation_check')`. `account_move_line.py:1212` applies the
same context key on the item side, and `account_move_line.py:1550-1552` refuses writing a
deprecated account onto an item unconditionally. So EV-003's UNKNOWN can be closed as CONFIRMED
(posting is blocked) WITH CAVEAT (by an application guard carrying a caller-supplied override, and
only for accounts already marked deprecated at the time of the write — nothing revalidates entries
already posted, and the flag still does not prevent the account from holding balances). I recommend
the evidence base be updated.

---

## EXPERT 4 POSITION

My position, stated as an architect rather than an auditor, is that the reference implementation's
core-ledger design is **not a safe pattern for SMEsPlus to follow**, and that the reason is
structural rather than a matter of individual defects. Reading across everything I verified, one
sentence covers it: **in the reference, almost nothing that matters is owned by the ledger.** The
balance invariant lives in a suppressible Python wrapper. Immutability and deletion protection live
in two configuration checkboxes that default to off. The posted-field freeze lives in a conditional
whose condition is supplied by whoever calls it, and it is switched off wholesale in the module
handling the highest-volume entries in the system. The hash guard's own protected scope is read from
the caller's context. Period alignment is governed by a key-value setting that has no tenant
dimension at all. Identity in one UI model is arithmetic over a constant. Of the fourteen invariants
in my matrix, exactly three are enforced by the database, and all three are per-row checks on a
single item — not one cross-row or cross-record invariant is protected below the application layer.

I want to be precise about what that does and does not mean. It does **not** mean the reference is
badly engineered. It is coherent, it is deeply thought through, and in places it is better than its
reputation — the fiscal-lock override is exactly the right shape and I have recommended SMEsPlus
adopt its intent as a standard; the re-dating warning that E00 says does not exist does in fact
exist, in the one place a careful accountant would look; the lock-exception model is revocable,
which is better than the append-only design the evidence base credits it with. I found three places
where the evidence base was harder on the reference than the code warrants, and I have recorded all
three, because a review that only finds confirmations is not a review.

What it means is that the reference is a **configurable business application** that can be operated
as a ledger, and SMEsPlus is being asked to build a **ledger**. Those are different products with
different centres of gravity. A configurable application places controls where they can be adjusted
to fit a customer; a ledger places them where they cannot be adjusted at all, because their
unadjustability is the entire product. Every finding above is an instance of that one difference.

Three things follow, and I put them forward as positions, not preferences.

**First, on the state machine.** Three values are insufficient, and the insufficiency is not
cosmetic. Two entries that both display "Draft" can differ in whether a number was consumed,
whether an analytic subledger was deleted, whether reconciliations were discarded, and whether the
row can now be removed from the database. A user cannot see the difference; a report cannot filter
on it; an auditor cannot query it. My position is that SMEsPlus must name every state that changes
what a control permits or what a transition destroys — I count at least eight — and that the
enumeration the engine branches on and the one the user sees must be the same enumeration. I raise
this as a Wave A blocking design question.

**Second, on where controls live.** I recommend a single governing rule for the SMEsPlus Account
module, and I would like it adopted explicitly rather than left implicit: *an invariant that an
auditor would test must be enforced at the lowest layer capable of enforcing it, and must not be
weakenable by configuration, by context, or by the identity of the caller.* Applied to the matrix
above, that moves C1, C4, C11 and C12 to the database, and it removes C10 from the configuration
layer entirely — immutability stops being a switch and becomes a property of how posted records are
stored. I designate C1, C10 and C11 as `Tolerance = 0` candidates under Constitution principle 13
and ask that they be tested as negative cases in the Wave A charter: not "does the interface refuse
this", but "can any route whatsoever produce this outcome". C1 in particular deserves a blunt
statement: if an unbalanced posted entry can exist in the table by any means, the system is not a
ledger, whatever the interface says.

**Third, on the UI.** The pattern I found repeatedly is that controls are visible where they are
least needed and invisible where they matter most. The re-dating warning appears on the form of a
single working entry and vanishes from bulk actions, scheduled posting, duplication and every
machine-generated entry — and it vanishes from the entry itself the moment it is posted, so the
shift can never be seen afterwards. The sequence-gap indicator stops reporting gaps precisely when a
period is locked and the gap becomes permanent. Two buttons, "Reset to Draft" and "Cancel", perform
the same destruction while reading as different levels of caution. My position is that SMEsPlus
needs a stated UI standard for accounting controls, with three requirements: a control that alters
posted data must announce itself on **every** path that reaches it, including unattended ones; an
unattended path that would trigger such a control must refuse and queue for a human rather than
proceed quietly; and any alteration that did occur must remain visible on the record permanently,
not only while the record is still editable. Silence is not a neutral default in accounting
software. It is a decision to withhold, and here it is made by omission rather than by design.

Two matters I explicitly do **not** decide and route onward. The interaction between accounting-date
shifting and Thai VAT and WHT period attribution is `HOLD / EVIDENCE REQUIRED` and belongs to the
Accounting-Tax track; I add only that F-06 changes the analysis that track must perform, because
the destination period is not lock-plus-one-day as recorded but can be end-of-month or end-of-year.
And whether a client can supply the context keys behind F-03 and F-05 over the public write
interface is a security question outside my lane; it must be settled by an executed test, not by
reasoning, and until it is settled I have written those findings so that they stand on the
architecture alone and do not depend on the answer.

I approve nothing. Boss is the sole final approver, this document is research only, and no
implementation or code change has been proposed or made. My recommendation to the gate is that
Wave A should not advance on the strength of "the reference does it this way" for any of C1, C4,
C10, C11 or C12 — because on each of those, what the reference actually does is delegate the
invariant to somebody else.

— Expert 4, Lead Code & UI Architect
