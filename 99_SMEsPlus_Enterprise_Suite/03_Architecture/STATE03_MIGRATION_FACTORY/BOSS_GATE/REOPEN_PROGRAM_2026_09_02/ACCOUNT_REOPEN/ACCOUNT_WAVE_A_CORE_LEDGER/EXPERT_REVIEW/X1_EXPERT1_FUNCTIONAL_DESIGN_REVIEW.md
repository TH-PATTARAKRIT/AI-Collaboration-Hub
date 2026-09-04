> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.**
> This review carries `file:line -- method` citations into a reference ERP source tree.
> Boss / PMO / AI-Audit visible only. Must NOT be transcribed into any Layer 1 clean-room package,
> into Team B design input, or into any downstream reference package. Its clean-room derivatives are
> the numbered files in the package root, which cite `EV-0NN` / `COR-0N` identifiers only.

# X1 — EXPERT 1 REVIEW: LEADER FUNCTIONAL DESIGN

Session: `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`
Wave: `WAVE A — CORE LEDGER & CLOSING`
Reviewer: Expert 1 — Leader Functional Design (business process, accounting usability, workflow, exception handling, user operations)
Date: 2026-09-04
Input read: `LAYER2_EVIDENCE_QUARANTINE/E00_PRIMARY_EVIDENCE_BASE.md` (EV-001..EV-023)
Primary source personally read this session: reference ERP v18 build 20250608, `addons/account/`, `addons/account_accountant/`, `addons/base/models/`

> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.** This review contains `file:line` citations
> to a reference ERP source tree and must not be transcribed into any Layer 1 clean-room package.

## Scope and lane

This review evaluates **what a Thai SME accounting team would actually do, day to day, in a SaaS
ERP** built on the semantics described in the evidence base. It does not evaluate schema design,
performance, tenant isolation, or tax computation — those belong to Experts 2/3/4 and to the
Accounting-Tax track.

**Verification performed.** I independently read the primary source for EV-003, EV-004, EV-009,
EV-012, EV-016 and EV-021 rather than relying on the evidence base, plus the reversal and
delete-or-reverse paths that the evidence base does not cover. Eight of my ten findings cite lines
I opened myself. Three findings **contradict or materially qualify** the evidence base.

**Evidence-class legend used below:** `VERIFIED FACT` (read directly from primary source this
session), `REFERENCE BEHAVIOUR` (what the reference implementation does — a benchmark, never an
authority), `INFERENCE`, `RECOMMENDATION`, `UNKNOWN — EVIDENCE REQUIRED`,
`HOLD / EVIDENCE REQUIRED` (Thai statutory matter, routed to Accounting-Tax track).

**Status vocabulary used:** `CONFIRMED`, `CONFIRMED WITH CAVEAT`, `CONTRADICTED`, `UNKNOWN`,
`HOLD`, `VETO`. This review approves nothing. Boss is the sole final approver.

---

## 1. The lock date re-dates the document — and the bookkeeper is told so only in a dismissible banner, only while the entry is draft

**Status: CONFIRMED WITH CAVEAT (EV-009)**

### OBSERVATION

A Thai SME bookkeeper's most common single act is entering a supplier invoice that arrived late.
In the reference behaviour, when that document's date falls inside a locked period, the system does
not refuse it and does not ask a question. It rewrites the accounting date forward and posts. The
document keeps its own date; the ledger carries a different one. The bookkeeper's only signal is an
inline alert on the form, and that alert is rendered **only while `state == 'draft'`**. Once the
entry is posted, the surface that told the user "this will be accounted on a different date"
disappears from the record entirely.

The lived consequence: a clerk enters ten late bills on 5 April for a March period that was locked
on 2 April. All ten silently become April. Nobody re-reads the banner. At the April month-end the
expense line is over by ten bills; at the March close the accrual was never raised because the
entries "went in". The variance is discovered by the accountant, not by the system, and it is
discovered a month later.

### EVIDENCE

`VERIFIED FACT` — `addons/account/models/account_move.py:4933-4936` — in `_post`, for each move to
post: `lock_dates = move._get_violated_lock_dates(move.date, affects_tax_report)`, and if any lock
is violated, `move.date = move._get_accounting_date(...)`. No exception is raised; the field is
reassigned.

`VERIFIED FACT` — `addons/account/models/account_move.py:5704-5718` — `_get_lock_date_message`
returns a string stating that the date is prior to the named lock and the entry "will be accounted
on" the shifted date upon posting. It is a message, not a refusal.

`VERIFIED FACT` — `addons/account/views/account_move_views.xml:803-806` — the alert div carrying
`tax_lock_date_message` is guarded `invisible="state != 'draft' or not tax_lock_date_message"`.
The warning is therefore not visible on the posted record.

`VERIFIED FACT` — `addons/account/models/account_move.py:1681-1685` — `_compute_tax_lock_date_message`
is a non-stored computed `Char`; no permanent trace of the warning is written to the entry.

EV-009 corroborated by my own read; the "banner disappears once posted" consequence is my own
addition, not present in the evidence base.

### CONTRADICTION

None identified against the substance of EV-009. One citation-precision issue is raised separately
as Finding 2.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether the reference behaviour writes any durable record (chatter
message, tracked field) at the moment the date is shifted at post time. I found the shift at
`account_move.py:4936` and no `message_post` adjacent to it, but I did not trace every override
hook that could add one. Not decidable from what I read this session.

`HOLD / EVIDENCE REQUIRED:` whether Thai VAT and withholding-tax period attribution tolerates a
document whose accounting period differs from its document date, and under what conditions. I make
no assertion about Thai law. Routed to the Accounting-Tax track as a Wave A dependency.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus should treat silent re-dating as a **workflow-level defect**, not a
convenience, and should replace it with an explicit, named user decision. Three concrete positions
for Boss:

1. **Refuse by default.** A backdated document into a closed period is rejected with a named reason,
   and the operator must choose one of two labelled paths: (a) request a lock exception, or
   (b) post to the current open period **as a deliberate late entry**.
2. If path (b) is taken, the shift must be a **first-class, durable attribute of the entry** — a
   stored "original document date", a stored "accounting date", a stored "period-shift reason", and
   a stored actor and timestamp — visible on the posted record forever, not a draft-only banner.
3. A standing **"documents shifted out of their document period"** operational report must exist, so
   the month-end reviewer sees the population rather than discovering it line by line.

`RECOMMENDATION:` mark this a `Tolerance = 0` candidate under Constitution principle 13 (financial
integrity), on the grounds that a ledger silently disagreeing with its source document about period
is a financial-integrity failure, not a usability preference.

---

## 2. The re-dating algorithm is not "lock date plus one day", and it also fires with no lock at all

**Status: CONTRADICTED IN DETAIL (EV-009) — the evidence base cites the wrong path and understates the scope**

### OBSERVATION

EV-009 describes the mechanism as: "if the intended date is on or before that lock date, the values
dictionary is **rewritten** so that `date = lock_date + 1 day`," citing `account_move.py:3127-3129`.

Two problems.

**(a) The cited lines are the copy path, not the posting path.** Lines 3126-3128 sit inside
`copy_data`, i.e. they govern duplicating an entry (and therefore reversals, which are built by
`copy`). The general posting path is `_get_accounting_date` at `account_move.py:5655-5691`, and it
is materially more complex than "+1 day".

**(b) The real algorithm can move a date without any lock being involved at all.** For a
**non-sale** document — a vendor bill, the single highest-volume document type in a Thai SME —
`_compute_date` calls `_get_accounting_date` on every change of `invoice_date`, unconditionally.
Inside it, when the journal's numbering resets monthly and today's month is later than the invoice
month, the accounting date is set to the **last day of the invoice's own month**. A bill dated
15 January, entered on 3 March, is therefore booked to 31 January — not to 15 January, and not
because of any lock.

This matters enormously for the bookkeeper's mental model. The evidence base leaves the reader
believing "my date is preserved unless a lock is in the way". That is not what the reference does.
The reference treats the accounting date of a purchase document as a **derived** value at all times.

### EVIDENCE

`VERIFIED FACT` — `addons/account/models/account_move.py:3126-3128` (inside `copy_data`):
`user_fiscal_lock_date = move.company_id._get_user_fiscal_lock_date(move.journal_id)` then
`if (default_date or move.date) <= user_fiscal_lock_date: vals['date'] = user_fiscal_lock_date + timedelta(days=1)`.
This is the copy/reversal path. EV-009's citation points here.

`VERIFIED FACT` — `addons/account/models/account_move.py:5655-5691` — `_get_accounting_date`. When
locks are violated it first sets `invoice_date = lock_dates[-1][0] + timedelta(days=1)`, then for
sale documents returns `min(today, end_of_month_or_year(invoice_date))`, and for non-sale documents
returns either `date_utils.get_month(invoice_date)[1]` (end of the invoice's month) or
`max(invoice_date, today)`. The outcome is therefore frequently **not** `lock_date + 1 day`.

`VERIFIED FACT` — `addons/account/models/account_move.py:800-810` — `_compute_date`, depends on
`invoice_date` and `company_id`: `if not move.is_sale_document(...): accounting_date = move._get_accounting_date(move.invoice_date, move._affect_tax_report())`.
No lock-date test guards this call.

### CONTRADICTION

Yes — this is my first explicit disagreement with the evidence base. EV-009 is classed
`VERIFIED FACT` and describes a "+1 day" rewrite driven by lock dates. My own read shows (i) the
cited lines govern copying, (ii) the posting-path algorithm is a period-end/today calculation, and
(iii) for purchase documents the calculation runs whether or not a lock exists. The **conclusion**
of EV-009 — that the ledger and the document legitimately disagree on date by design — survives and
is in fact strengthened. The **mechanism description** does not, and must be corrected before it is
carried into any Layer 1 semantic transfer register or Team B design input.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` the practical frequency of the no-lock re-dating in a real tenant
depends on `_deduce_sequence_number_reset(highest_name)` — the monthly-versus-yearly numbering
shape of each journal. I did not enumerate which shipped journal configurations produce monthly
reset. Deferred; requires a configuration survey, not a code read.

### RECOMMENDATION

`RECOMMENDATION:` the evidence base entry EV-009 should be **amended, not deleted** — citation
corrected to `account_move.py:5655-5691` and `:800-810`, mechanism restated, and the copy-path
behaviour split out as a separate observation because it governs reversals.

`RECOMMENDATION:` for SMEsPlus, the design position should be that the **accounting date of a
document is entered or explicitly confirmed by a human, never silently derived**. If a derivation
rule is wanted (e.g. "late supplier invoices book to end of their own month"), it must be a named,
configured, visible policy that the bookkeeper is shown before posting — not an invisible property
of the numbering format of the journal.

---

## 3. Reset-to-draft is a destructive operation wearing the vocabulary of an undo

**Status: CONFIRMED (EV-012)**

### OBSERVATION

For an SME bookkeeper, "reset to draft" reads as *unlock so I can fix a typo*. It is not that. In
the reference behaviour the single button, in one gesture and with no confirmation dialogue in the
method itself, deletes every analytic line attached to every item of the entry and discards every
reconciliation those items participate in.

The everyday consequence chain:

- **Cost-centre / project reporting silently changes.** A Thai SME running job costing or
  department analysis via analytic distribution sees the analytic subledger for that entry vanish
  and be rebuilt on re-post — rebuilt from `analytic_distribution` only. Any analytic line that was
  not derived from that JSON field is destroyed and not recreated.
- **Payment matching is lost.** If the entry was a customer invoice matched against a receipt, the
  match is gone. The receipt becomes an unallocated credit, the invoice becomes open, ageing
  changes, and the collections clerk chasing that customer now has wrong information. Nobody told
  the collections clerk.
- **The person who fixes the typo is rarely the person who did the matching.** The cost of the
  correction is borne by a different role than the one who chose it.

### EVIDENCE

`VERIFIED FACT` — `addons/account/models/account_move.py:5274-5288` — `button_draft`: refuses
non-posted/non-cancelled entries; refuses entries needing a cancellation request; calls
`self._check_draftable()`; then `self.mapped('line_ids.analytic_line_ids').unlink()`; then
`self.mapped('line_ids').remove_move_reconcile()`; then `self.state = 'draft'`; then
`self._detach_attachments()`. Read directly this session.

`VERIFIED FACT` — `addons/account/models/account_move.py:5317-5357` — `_check_draftable` refuses
exactly three categories: exchange-difference entries, tax cash-basis entries
(`tax_cash_basis_rec_id or tax_cash_basis_origin_move_id`), and hashed entries
(`if move.inalterable_hash`). Nothing else is protected.

`VERIFIED FACT` — `addons/account/models/account_move_line.py:389-392` — `analytic_line_ids` is a
one2many on `account.analytic.line` via `move_line_id`, i.e. it includes **every** analytic line
pointing at that item, not only the ones the entry generated.

`VERIFIED FACT` — `addons/account/models/account_move_line.py:3149-3172` — `_create_analytic_lines`
regenerates analytic lines **solely** from `line.analytic_distribution`
(`_prepare_analytic_lines`: `if self.analytic_distribution:`). Analytic lines with any other origin
are therefore deleted by `button_draft` and are not restored by re-posting.

EV-012 corroborated by my own read of `account_move.py:5274-5288` and `:5317-5357`. The
"deleted but not regenerated" asymmetry at `account_move_line.py:389-392` versus `:3161-3172` is my
own addition.

### CONTRADICTION

None identified. EV-012 is accurate as written.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether any reference module restores non-distribution analytic
lines after a re-post. I read only the `account` module's regeneration path; timesheet-style modules
were not examined this session.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus should not ship a general-purpose "reset to draft" on a posted entry at
all. The correction path for a posted entry should be a **new accounting event** (see Finding 5).
Where an un-post capability is retained for a narrow, named case, it must:

1. be a **separate, named, permissioned action** ("Un-post for correction"), not a state toggle;
2. **enumerate the collateral damage before acting** — "this will unmatch 3 payments totalling
   THB 412,000 and delete 7 analytic allocations" — and require typed confirmation;
3. record an **irreversible operational log entry** naming the actor, the timestamp, the reason, and
   the specific reconciliations and analytic allocations destroyed;
4. be **blocked entirely** for any entry whose items are reconciled against a bank-cleared item.

`RECOMMENDATION:` treat the analytic subledger as a **derived projection with its own audit trail**,
not as disposable child rows. If analytic lines can be deleted with no surviving record, then
analytic reporting is not auditable, and a Thai SME using job costing for management decisions has
no way to reconstruct why a prior-period cost report changed.

---

## 4. The same user gesture produces three different accounting outcomes, decided by hidden configuration

**Status: CONFIRMED — new finding, not in the evidence base**

### OBSERVATION

The reference behaviour contains a single internal entry point that decides, per record, whether a
user's "get rid of this" action results in **hard deletion**, **cancellation**, or **a posted
reversing entry**. The decision is made from three conditions the user cannot see at the moment of
acting: whether the entry is hashed, whether its date is after the effective fiscal lock, and
whether the company's audit-trail switch is on.

From the accounting team's point of view this is the single worst usability property in the whole
correction area, because **the audit consequence of an action is not a property of the action**. The
same clerk, doing the same thing, on two entries that look identical on screen, produces in one case
a document that no longer exists and in the other case a permanent pair of offsetting entries that
the auditor will ask about. Neither outcome was chosen; both were inherited from configuration set
by someone else, possibly months earlier.

For a Thai SME this is aggravated by the shipped defaults: hashing is off per journal by default,
so early in a tenant's life the "delete" branch is the common branch, and the tenant's earliest
accounting history is its least protected.

### EVIDENCE

`VERIFIED FACT` — `addons/account/models/account_move.py:4805-4809` — `_can_be_unlinked` returns
`not self.inalterable_hash and self.date > lock_date and not is_part_of_audit_trail`, where
`is_part_of_audit_trail = self.posted_before and self.company_id.check_account_audit_trail`.

`VERIFIED FACT` — `addons/account/models/account_move.py:4814-4830` — `_unlink_or_reverse` sorts the
recordset into three buckets: `to_reverse` (cannot be unlinked), `to_cancel` (protected by audit
trail), `to_unlink` (everything else); then calls `button_draft()` and `unlink()` on the third
bucket, `button_cancel()` on the second, and `_reverse_moves(cancel=True)` on the first.

`VERIFIED FACT` — `addons/account/models/account_move.py:4760-4803` — `_reverse_moves` builds the
reversal by `copy`, negating `balance` and `amount_currency`, and when `cancel=True` posts the
reversal immediately and reconciles it against the original.

`REFERENCE BEHAVIOUR` — EV-011 (evidence base) records that hashing is per-journal and off by
default and that the audit-trail block has a documented `force_delete` context bypass. I did not
re-verify the bypass line myself this session; treated as evidence-base assertion, not as my own
verified fact.

### CONTRADICTION

None identified against the evidence base — this behaviour is simply absent from it. EV-011 and
EV-012 each describe a piece; the composing method that turns them into a user-visible branch is not
cited anywhere in EV-001..EV-023. I record it as a **coverage gap in the evidence base**, not as an
error in it.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` which user-facing buttons in the reference UI route to
`_unlink_or_reverse` versus to `button_draft` + delete directly. I traced the method, not its
callers, this session.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus should adopt the inverse principle: **the audit outcome is chosen by the
user, from a fixed menu, and is never inferred from configuration.** A correction dialogue should
offer named outcomes ("Reverse in the current period", "Reverse in the original period", "Cancel and
reissue") and state, before the user commits, exactly which documents will exist afterwards.

`RECOMMENDATION:` deletion of a posted accounting document should not be a shipped capability of the
SMEsPlus ledger at all, at any permission level, in any configuration. If Boss wishes to retain it
for data-migration remediation, it should be an out-of-band operation with its own approval record,
not a button in the accounting UI.

---

## 5. Correction methodology: the boundary between "edit" and "new accounting event"

**Status: CONFIRMED WITH CAVEAT — position statement, drawing on EV-012, EV-022 and my own reads**

### OBSERVATION

The question posed to me is: *when must a correction be a new accounting event rather than an edit?*
My position, stated as a design recommendation and not as a verified fact about any system:

**A correction must be a new accounting event from the moment the entry has been relied upon by
anyone outside the person who made it.** Reliance, not posting, is the boundary. Concretely, an
entry has been relied upon once any of the following is true:

1. it has been **matched** against another item (a payment, a receipt, a bank line);
2. it has been **included in a filed or issued output** — a tax return, a financial statement, a
   customer-facing document that left the building;
3. it falls in a **period that has been closed and reported**;
4. it has been **numbered in a statutory sequence** that a third party can reference.

Below that boundary, editing a draft is not a correction — it is authoring. Above it, an edit is a
falsification of the historical record even when the resulting balances are correct, because the
record no longer shows what the organisation believed at the time it acted.

The reference behaviour does not draw this line. It draws a different one: "posted" freezes the
accounting substance (lines, amounts, date, counterparty) but leaves descriptive metadata writable,
and the freeze is a Python guard with a documented context bypass rather than a storage property
(EV-022). That line is drawn at the wrong place for an SME: it protects the numbers a bookkeeper
rarely needs to change and leaves open the references an auditor uses to trace the transaction.

### EVIDENCE

`VERIFIED FACT` — `addons/account/models/account_move.py:5274-5288` — the reference's own
reset-to-draft path destroys reconciliation (`remove_move_reconcile()`), i.e. it destroys precisely
the "reliance" evidence that my proposed boundary uses. Read directly this session.

`VERIFIED FACT` — `addons/account/wizard/account_move_reversal.py:15-20` — the reversal wizard's
`reason` field is a plain optional `Char` ("Reason displayed on Credit Note") and `date` defaults to
`fields.Date.context_today`. A reversal therefore carries **no mandatory justification** and lands
in today's period by default rather than the original period.

`REFERENCE BEHAVIOUR` — EV-022 (evidence base): on a posted entry, `ref`, `narration` and
`journal_id` are outside the refusal list at `account_move.py:3247-3252`, and the guard is skipped
under the `skip_readonly_check` context. Cited as evidence-base assertion; I did not personally
re-read `:3247-3252` this session.

### CONTRADICTION

I **qualify** the evidence base's framing here. EV-022 presents the posted-entry guard as freezing
"the accounting substance ... but not the descriptive metadata". For a Thai SME that framing
inverts the risk. The supplier reference on a bill (`ref`) is frequently the *only* link between the
ledger and the physical tax invoice; the ability to rewrite it silently on a posted entry, at any
time, with no tracked change, is a more serious control weakness than the ability to change a
narration. "Descriptive metadata" is not a safe category.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether `ref` and `narration` carry `tracking=True` in the reference
model, which would at least leave a chatter trail of the change. I did not verify the field
declarations this session.

`HOLD / EVIDENCE REQUIRED:` whether Thai statutory record-keeping requires a specific correction
form (reversal-and-reissue versus adjusting entry) for a document that has been issued to a
counterparty, and whether a reversal must carry the original document's date or the correction date.
I assert nothing about Thai law. Routed to the Accounting-Tax track; this is a **blocking dependency
for the SMEsPlus correction design**, not a nice-to-have.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus should define, in Wave A, a single **Correction Methodology** document
with exactly three named user operations and no fourth:

| Operation | Available when | Produces |
|---|---|---|
| **Amend draft** | entry never posted | no accounting event; authoring only |
| **Reverse and reissue** | entry posted, period open | two new posted entries, both permanent |
| **Adjust in current period** | entry posted, period closed | one new posted entry referencing the original |

`RECOMMENDATION:` a reversal must require a **mandatory structured reason** (selected from a
governed list, plus free text), must default to the **original document's period where that period
is open**, and must create a permanent bidirectional link that both documents display. The
reference's optional `Char` reason is below the standard an SME audit file needs.

`RECOMMENDATION:` `ref` and any field carrying an external document identifier must be inside the
frozen set on a posted entry, not outside it.

---

## 6. Accounts have two states where chart housekeeping needs three — but the evidence base's open question is answerable, and the answer is more favourable than recorded

**Status: CONTRADICTED IN PART (EV-003) — the recorded `UNKNOWN` is resolved by my own read**

### OBSERVATION

EV-003 states that the account model carries only a `deprecated` boolean, does not participate in
the framework's archive mechanism, and records as `UNKNOWN — EVIDENCE REQUIRED` whether any
reference behaviour blocks *posting* to a deprecated account — noting that the flag appears only in
selection domains, and "a domain filters pickers, it does not constrain programmatic posting."

**That question is answerable and the answer is that posting is blocked, in three places.** The
reference does not rely on domains alone. It raises at line-write time, at line-validation time, and
again at post time.

This changes the finding's weight materially. `deprecated` is not merely a cosmetic picker filter;
it is an enforced posting block. The remaining problem is narrower but still real, and it is a
**workflow** problem rather than a control problem:

- The block is **absolute and immediate**. There is no "no new postings, but let the existing open
  items run off" state. A Thai SME closing a bank account, retiring a project cost centre, or
  cleaning up a chart inherited from a migration needs exactly that intermediate state, because the
  account still holds a balance and still has open items to clear.
- Consequently the practical bookkeeper behaviour will be: *do not deprecate anything until it is
  fully cleared*, which in practice means *never deprecate anything*. The chart grows monotonically.
- There is **no guard on deprecating an account that still holds a balance**, only on accounts used
  in a tax distribution. So the one thing the flag does not prevent is the thing most likely to
  cause a wrong trial balance: an account with a live balance being taken out of circulation while
  its balance stays in the statements with no owner.

### EVIDENCE

`VERIFIED FACT` — `addons/account/models/account_account.py:52` —
`deprecated = fields.Boolean(default=False, tracking=True)`. Confirmed; and a search of the model
for an `active` field declaration returns nothing, whereas
`addons/account/models/account_journal.py:92` declares
`active = fields.Boolean(default=True, help="Set active to false to hide the Journal without removing it.")`.
EV-003's two-state observation is corroborated.

`VERIFIED FACT` — `addons/account/models/account_move.py:4911-4912` — in `_post`:
`if move.line_ids.account_id.filtered(lambda account: account.deprecated) and not self._context.get('skip_account_deprecation_check'): validation_msgs.add(_("A line of this move is using a deprecated account, you cannot post it."))`.
**Posting is blocked.**

`VERIFIED FACT` — `addons/account/models/account_move_line.py:1212-1213` —
`if account.deprecated and not self.env.context.get('skip_account_deprecation_check'): raise UserError(_('The account %(name)s (%(code)s) is deprecated.', ...))`.

`VERIFIED FACT` — `addons/account/models/account_move_line.py:1550-1552` — "Check writing a
deprecated account." `if account_to_write and account_to_write.deprecated: raise UserError(_('You cannot use a deprecated account.'))`.

`VERIFIED FACT` — `addons/account/models/account_account.py:1027-1028` — the only guard on setting
`deprecated` is the tax-distribution check. No balance check, no open-item check, no
control-account check, no journal-default check. EV-003 corroborated on this point.

### CONTRADICTION

Yes — my second explicit disagreement. EV-003's `UNKNOWN — EVIDENCE REQUIRED` ("whether any
reference behaviour blocks posting to a deprecated account ... Not decidable from the evidence read
this session") is **decidable and decided**: three enforcement points exist. The evidence base
should be amended to close this open question, because leaving it open understates the reference
behaviour and would lead Team B to over-engineer a control that the benchmark already has.

I also note a secondary qualification: all three enforcement points share a **context bypass**
(`skip_account_deprecation_check`). So the block is a Python guard, not a storage property — the
same architectural pattern EV-011 and EV-022 criticise elsewhere. The evidence base is consistent in
flagging that pattern; it simply did not apply the pattern here.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether automated postings that select an account **by configuration**
(journal default account, payment method account, tax repartition account, product category
accounts) route through `_post` and therefore hit the block, or whether any of them post under a
context that suppresses it. This is the residue of EV-003's original concern and it remains open. It
is the question that actually matters operationally and it deserves a targeted trace.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus should model account lifecycle as an explicit **state**, not a boolean,
with at least: `Active` → `Closing` (no new postings; open items may be cleared; balance may run
off) → `Inactive` (no postings, balance must be zero) → `Archived` (hidden from all pickers, retained
for history). The three-state expectation in the Boss scope is right; the reference's two-state
boolean is the weaker design and should be treated as a benchmark to beat, not to copy.

`RECOMMENDATION:` transition into `Inactive` must be **guarded on balance and open items**, and the
guard must be a validation the user sees as a checklist ("this account has THB 84,200 and 6 open
items — clear them or reassign them"), not a bare refusal.

`RECOMMENDATION:` amend EV-003 in the evidence base to record the three enforcement points and to
re-scope its `UNKNOWN` to the configuration-driven posting paths only.

---

## 7. Account merge is a destructive history rewrite performed by raw SQL with no accounting record of the event

**Status: CONFIRMED AND ESCALATED (EV-004)**

### OBSERVATION

EV-004 correctly describes account merge as deleting accounts and retargeting history. My own read
found the operation is **worse from a user-operations standpoint than the evidence base conveys**,
in three specific ways:

1. **It is available to any accounting manager, in one step, with no approval and no undo.** There
   is no second-person authorisation, no dry-run report of what will be rewritten, and no way back.
2. **It leaves no accounting record that it happened.** The 351-line wizard contains **no**
   `message_post`, no `_message_log`, and no logger call anywhere. Compare this with the lock
   exception mechanism (Finding 8), which does write to the company chatter. A merge — a far more
   destructive act — writes nothing.
3. **The deletion and the history rewrite are executed as direct SQL**, bypassing ORM `unlink`
   hooks, tracking, and any override a localisation might have added. A `DELETE FROM account_account`
   statement is issued against the account ids, and foreign keys across the database are repointed
   generically.

What this looks like on the ground: a manager tidying a migrated chart merges "1210 Trade
Debtors — old" into "1210 Trade Debtors". Three years of journal items now report the surviving
account. The prior-year trial balance the auditor holds on paper no longer reproduces from the
system, and there is nothing in the system that explains why. The bookkeeper who prints it next
month simply sees different numbers and has no lead to follow.

The one protection the reference does have is telling: it sorts so that an account with hashed
entries survives, specifically to avoid changing an id that a hash covers. The authors knew the
operation breaks integrity evidence; they protected only the case where the breakage would be
*detected*.

### EVIDENCE

`VERIFIED FACT` — `addons/account/wizard/account_merge_wizard.py:134-141` — `_action_merge`
docstring: the first account is extended to each company of the others keeping their codes and
names; "the others are deleted"; "journal items and other references are retargeted to the first
account."

`VERIFIED FACT` — `addons/account/wizard/account_merge_wizard.py:110-112` — the group is sorted
`sorted('account_has_hashed_entries', reverse=True)` with the comment "This ensures that if one
account in the group has hashed entries, it appears first, ensuring that its ID doesn't get changed
by the merge."

`VERIFIED FACT` — `addons/account/wizard/account_merge_wizard.py:161-165` — foreign keys and
reference fields are retargeted through
`self.env['base.partner.merge.automatic.wizard'].new()._update_foreign_keys_generic(...)` and
`_update_reference_fields_generic(...)`.

`VERIFIED FACT` — `addons/account/wizard/account_merge_wizard.py:194-202` — deletion is executed as
raw SQL: `self.env.cr.execute(SQL("DELETE FROM account_account WHERE id IN %(account_ids_to_delete)s", ...))`,
preceded by `self.env.invalidate_all()`.

`VERIFIED FACT` — a grep for `message_post`, `_message_log` and `_logger` across the whole
351-line file returns **no match**. Negative scope: not found in
`addons/account/wizard/account_merge_wizard.py` as read this session; I did not search other modules
for an override that might add logging.

`VERIFIED FACT` — `addons/account/security/ir.model.access.csv:152-153` —
`access_account_merge_wizard_manager,...,account.group_account_manager,1,1,1,1`. Full rights for the
accounting-manager group; no narrower group.

### CONTRADICTION

None identified against EV-004. I escalate rather than dispute it: EV-004 classes the loss as
"provenance ... is lost". My reading is that the loss is broader — not merely which account a
posting named, but **the fact that a rewrite occurred at all**, which is the thing an auditor needs
in order to ask any question.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether the reference blocks merging accounts that carry balances, or
accounts of different types (e.g. an expense account into an asset account). I read the merge
execution path, not the grouping-key validation that precedes it.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus should **not** offer account merge as a routine chart-housekeeping
operation. The user need behind it — "I have two accounts that mean the same thing" — is served
correctly by mapping and re-presentation, not by deleting one and rewriting history.

`RECOMMENDATION:` if a merge capability is required for migration remediation, it must be: (a)
restricted to a migration role distinct from the day-to-day accounting-manager role; (b) preceded by
a **mandatory impact report** the operator must review (how many items, which periods, which closed
periods); (c) blocked outright for any period covered by a lock or already reported; (d) recorded as
a **permanent, non-deletable operational event** naming actor, timestamp, reason, both accounts, and
the affected item count; and (e) accompanied by a retained "as-posted account" attribute on every
rewritten item, so the historical trial balance remains reproducible.

`RECOMMENDATION:` flag as a `Tolerance = 0` candidate under Constitution principle 13. A silent,
unlogged, un-undoable rewrite of posted history available to a single ordinary role is a financial
integrity failure by any reasonable reading.

---

## 8. Lock exceptions: append-only is not the same as controlled, and the ACL is not the real control

**Status: CONFIRMED WITH CAVEAT (EV-021) — with two corrections to the evidence base**

### OBSERVATION

EV-021's operational conclusion is right and important: a single accounting manager can create an
exception that applies to **every user** with **no expiry** and **no stated reason**, which is a
permanent global unlock wearing the vocabulary of a temporary one. I confirm all three properties.

Two corrections to the evidence base's framing, both of which I regard as making the picture
somewhat *better* on paper and somewhat *worse* in practice:

**(a) Exceptions are not strictly append-only; they are revocable, and the ACL does not say so.**
The evidence base reads the access CSV (`create/write/delete = 1,0,1,0`) and concludes the records
are append-only. But `action_revoke` exists, checks the manager group in Python, and then writes
through `.sudo()` — deliberately escalating past the very ACL row the evidence base cites. So the
real control is a group check inside a method, not the ACL. This is the same "control is a Python
guard, not a property" pattern the evidence base flags elsewhere; it should be flagged here too.

**(b) The same single role both grants and revokes.** There is no segregation of duties. The
manager who opens a permanent global unlock is the only role that can close it, and nothing forces a
review. An exception created in a hurry during a March close is still live in December unless
somebody remembers.

The workflow consequence for a Thai SME with one accounting manager — which is the typical shape —
is that the lock-exception mechanism provides **zero** independent restraint. It is a self-service
unlock with a chatter note.

### EVIDENCE

`VERIFIED FACT` — `addons/account/models/account_lock_exception.py:36-40` — `user_id` comment: "An
exception w/o user_id is an exception for everyone".

`VERIFIED FACT` — `addons/account/models/account_lock_exception.py:41-47` — `reason = fields.Char()`
(no `required=True`); `end_datetime` comment: "An exception without `end_datetime` is valid forever".

`VERIFIED FACT` — `addons/account/security/ir.model.access.csv:18-19` —
`base.group_user,1,0,0,0` and `account.group_account_manager,1,0,1,0`. Read directly; matches
EV-021.

`VERIFIED FACT` — `addons/account/models/account_lock_exception.py:258-266` — `action_revoke`:
`if not self.env.user.has_group('account.group_account_manager'): raise UserError(...)`, then for
each active record `record_sudo = record.sudo(); record_sudo.active = False; record_sudo.end_datetime = fields.Datetime.now()`.
The write happens under `sudo()`, past the `write = 0` ACL.

`VERIFIED FACT` — `addons/account/models/account_lock_exception.py:211-237` — creation posts to the
company chatter with a tracking value, naming the user or "everyone", the end datetime or nothing,
and the reason or nothing.

`VERIFIED FACT` — `addons/account/models/account_lock_exception.py:242-243` — `copy` raises
"You cannot duplicate a Lock Date Exception." A genuine control, not mentioned in EV-021.

`VERIFIED FACT` — `addons/account/models/company.py:565-577` — `_get_user_fiscal_lock_date(journal, ignore_exceptions=False)`
composes `max(user_fiscalyear_lock_date, user_hard_lock_date)`, raised to the sale or purchase lock
by journal type. EV-021's and EV-008's resolution description corroborated.

### CONTRADICTION

Yes — my third disagreement, though a narrower one than Findings 2 and 6. EV-021 characterises
exceptions as "append-only and logged". They are logged; they are **not** append-only, because
`action_revoke` deactivates them under `sudo()`. And the access-control row EV-021 quotes as
evidence of that append-only status is bypassed by the very method that revokes. The corrected statement is:
*exception records are never deleted and their creation is always logged, but their active state is
mutable by any accounting manager through a sudo-escalating method.* I did not find a chatter post
on revocation — negative scope: not found in `account_lock_exception.py:258-266` as read this
session.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether revocation is logged anywhere (company chatter, tracking, or
otherwise). Creation is logged at `:211-237`; I found no equivalent on the revoke path, but I did
not search beyond this file.

`UNKNOWN — EVIDENCE REQUIRED:` whether the reference surfaces active exceptions anywhere a closer
would see them during month-end — a dashboard, a close checklist, a warning on the lock-date screen.
Not examined.

### RECOMMENDATION

`RECOMMENDATION:` in SMEsPlus, a lock exception must carry, as **mandatory** fields: a structured
reason, a named beneficiary user (never "everyone"), and a hard expiry with a governed maximum
duration. "Applies to all users, forever" should not be expressible.

`RECOMMENDATION:` grant and revoke must be **separable roles**, and a tenant with a single
accounting manager must be forced to nominate a second approver at setup — otherwise the control is
decorative. This is a SaaS-onboarding requirement, not only a permissions requirement.

`RECOMMENDATION:` active exceptions must appear on the **month-end close checklist** as a mandatory
review item, with the closer required to confirm each one before the period can be marked closed.

---

## 9. There is no year-close event — but a fiscal year entity does exist, and the evidence base's whole-tree negative is wrong

**Status: CONTRADICTED IN PART (EV-016) — core conclusion stands, supporting negative does not**

### OBSERVATION

EV-016 asserts: "A search for a fiscal-year model definition across the entire 797-module reference
tree returns **no result**. The fiscal year exists only as two integers on the company."

The first sentence is incorrect. A fiscal-year model exists, in a sibling module of the one the
evidence base searched. It is a first-class entity with a name, a start date, an end date, a
company, a non-overlap constraint, and a rule that child companies cannot own one. It is optional —
gated behind a settings group — and it exists precisely to support the case the two company integers
cannot express: a fiscal year that is not a whole number of months, or a transitional short or long
year, both of which occur in real SME life (incorporation year, change of year end, group
alignment).

**The core of EV-016 nevertheless survives intact and I endorse it**: there is no year-close event,
no carry-forward posting, and no reopening operation; the profit-to-equity transfer is a report-time
computation attributed to a designated "Current Year Earnings" account rather than a posted entry.
A period is closed exactly to the extent that a lock date covers it. That conclusion is unaffected
by the existence of a fiscal-year calendar entity, because the entity defines *boundaries*, not
*events*.

This distinction matters for the Boss baseline that "close is monthly, month 12 is still a month
close". The reference evidence supports that baseline for the *closing event*. It does **not**
support dispensing with a fiscal-year *entity*, and the evidence base's overstated negative could
lead Team B to design one out. A Thai SME accounting team needs a named period object to hang a
close checklist, a status, an owner, and a sign-off on — regardless of whether a closing journal
entry is ever posted.

### EVIDENCE

`VERIFIED FACT` — `addons/account_accountant/models/account_fiscal_year.py:11-20` —
`_name = 'account.fiscal.year'`, `_description = 'Fiscal Year'`, with `name` (required Char),
`date_from` (required Date, "Start Date, included in the fiscal year"), `date_to` (required Date),
and `company_id` (required Many2one). Read in full this session.

`VERIFIED FACT` — `addons/account_accountant/models/account_fiscal_year.py:22-55` — `_check_dates`
constrains `date_to >= date_from`, refuses a fiscal year on a child company
(`if fy.company_id.parent_id: raise ValidationError(...)`), and refuses any overlap between two
fiscal years of the same company.

`VERIFIED FACT` — `addons/account_accountant/models/res_config_settings.py:14` —
`group_fiscal_year = fields.Boolean(string='Fiscal Years', implied_group='account_accountant.group_fiscal_year')`.
The entity is an **optional, settings-gated feature**, which is very likely why the evidence base's
search missed it.

`VERIFIED FACT` — `addons/account_accountant/models/res_company.py:162, 185, 193` — the company's
fiscal-year date computation searches `self.env['account.fiscal.year']` first and falls back to
`date_utils.get_fiscal_year(...)` derived from the two integers only when no record matches
(`res_company.py:174`).

`VERIFIED FACT` — `addons/account/models/company.py:71-72` — `fiscalyear_last_day = fields.Integer(default=31, required=True)`
and `fiscalyear_last_month = fields.Selection(MONTH_SELECTION, default='12', required=True)`;
`company.py:300-314` — the constraint refusing a 29 February year end. EV-016 corroborated on these
points.

`VERIFIED FACT` — `addons/account/models/account_account.py:67` — the account type
`("equity_unaffected", "Current Year Earnings")`; `account_account.py:36` — a domain restricting to
that type. EV-016's report-time-attribution conclusion is consistent with what I read.

### CONTRADICTION

Yes — my fourth and most consequential disagreement. EV-016 is classed `VERIFIED FACT` and rests a
design conclusion partly on a whole-tree negative that is false. The correct negative, with scope
attached, is: **a fiscal-year model definition is not found in `addons/account/` as searched; one is
found at `addons/account_accountant/models/account_fiscal_year.py:11`.** This is exactly the failure
mode the hard rule about scoped negatives exists to prevent, and it is also the pattern recorded in
project memory as the "never declare no code access from a narrow search" defect.

The design conclusion EV-016 draws — no year-close event, retained-earnings handling is entirely an
SMEsPlus decision — is **not** invalidated by this correction, and I endorse it independently.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether the fiscal-year records participate in lock-date behaviour or
only in reporting-period derivation and the currency table bounds. My read shows uses at
`res_company.py:162-193` and `res_currency.py:10-12`; I did not trace whether anything in the
locking path consults them.

`UNKNOWN — EVIDENCE REQUIRED:` whether the reporting layer offers a year-end result presentation
distinct from the general-ledger attribution EV-016 cites. Not examined this session.

### RECOMMENDATION

`RECOMMENDATION:` amend EV-016 in the evidence base — restate the negative with its search scope,
add the `account_accountant` citation, and preserve the design conclusion unchanged.

`RECOMMENDATION:` SMEsPlus should adopt the Boss baseline (close is monthly; month 12 is a month
close) **and** define a first-class **Accounting Period** entity — with a state, an owner, a
checklist, a sign-off, and a reopen record — grouped into a first-class **Fiscal Year** entity that
supports short and long transitional years. The reference's report-time year-end result is a
legitimate benchmark for *not posting a closing entry*; it is not a reason to have no period object.

`RECOMMENDATION:` retained-earnings treatment is, as EV-016 says, an open SMEsPlus decision with no
reference implementation to adapt. I recommend Boss decide it as a **user-visible workflow question**
first — "does the SME's accountant expect to see a closing entry in the ledger?" — before it is
decided as a data question.

`HOLD / EVIDENCE REQUIRED:` whether Thai statutory reporting expects a posted year-end closing
entry, and whether the absence of one affects the acceptability of the ledger to a Thai auditor or
the Revenue Department. I assert nothing. Routed to the Accounting-Tax track.

---

## 10. Month-end close has real preconditions in the reference, and they are the most usable thing in the whole area

**Status: CONFIRMED — a positive finding, drawn from EV-008 and EV-019 and my own read**

### OBSERVATION

Almost everything in this review is a criticism, so it is worth recording what the reference gets
right, because it is directly transferable as a **workflow** idea (not as code).

Setting the irreversible hard lock is refused while **draft entries** exist in the period, and the
refusal is not a bare error — it is a redirect that opens the list of the offending entries so the
user can act on them. Setting any fiscally effective lock is refused while **unreconciled bank
statement lines** remain in the period. That is a close checklist expressed as a system precondition
rather than as a document somebody is supposed to follow.

For a Thai SME with a small accounting team and no dedicated closer, this pattern — *the system
knows what "ready to close" means and shows you the exceptions* — is worth more than most of the
feature surface around it. It is also the correct answer to the workflow gap created by silent
re-dating (Finding 1): if the system will not let you lock a period that still has draft or
unmatched items, the population of documents that could later be silently shifted is small and
known.

The gap is that the checklist stops at two items. A working SME close also needs: unposted
recurring entries, unreviewed bank suspense items, open lock exceptions (Finding 8), documents
shifted out of period (Finding 1), and accounts flagged for closure that still carry balances
(Finding 6).

### EVIDENCE

`VERIFIED FACT` — `addons/account/models/company.py:501-516` — when a `hard_lock_date` is being set,
the company searches for `('state', '=', 'draft'), ('date', '<=', hard_lock_date)` and raises a
`RedirectWarning` — "There are still draft entries in the period you want to hard lock. You should
either post or delete them." — carrying an action that opens that exact list with a named list and
form view. Read directly this session.

`VERIFIED FACT` — `addons/account/models/company.py:492-499` — the hard lock cannot be removed
("The Hard Lock Date cannot be removed.") and a new value must be on or after the previous one
("A new Hard Lock Date must be posterior (or equal) to the previous one.").

`VERIFIED FACT` — `addons/account/models/company.py:518-519` — a further check block for
unreconciled bank statement lines follows the draft-entry check, gated on `if fiscal_lock_date:`.
EV-008 and EV-019 corroborated on this point.

### CONTRADICTION

None identified. I note only that the evidence base records these as control facts under EV-008 and
EV-019 without drawing the workflow lesson, which is the part most useful to Team B.

### UNKNOWN

`UNKNOWN — EVIDENCE REQUIRED:` whether the soft locks (as opposed to the hard lock) carry the same
draft-entry precondition, or only the bank-statement one. My read shows the draft-entry check inside
`if hard_lock_date:` and the bank check inside `if fiscal_lock_date:`, which suggests they differ,
but I did not trace the full conditional structure.

### RECOMMENDATION

`RECOMMENDATION:` SMEsPlus should make the close a **first-class guided operation** with an explicit,
extensible precondition list, each item showing its exception population and offering a direct route
to clear it. Every finding in this review that describes a silent failure should have a
corresponding close-checklist item, so that failures surface once a month at a known moment rather
than at audit.

`RECOMMENDATION:` adopt the *irreversibility* property of the hard lock (cannot be removed, can only
move forward) for the SMEsPlus final period lock. It is the single strongest control in the reference
behaviour and it is cheap. Adopt it as a **behavioural requirement**, derived from observing the
benchmark — not by adapting any implementation.

---

# EXPERT 1 POSITION

My overall view is that the reference behaviour, read through a business-process lens, is built for
a user who is assumed to be an accountant with system knowledge, working alone, who will notice
things. A Thai SME accounting team is none of those. It is typically one or two people, often with a
part-time external accountant, working under time pressure at month end, using a system whose
defaults were set once during onboarding and never revisited. Design decisions that are merely
*inconvenient* for the assumed user are *invisible* for the actual one, and invisibility is the
recurring failure mode here.

Four patterns run through everything I examined, and I would ask Boss to treat them as the actual
findings, with the ten numbered sections as their evidence.

**First, silent state changes.** A lock date re-dates a document instead of refusing it (Finding 1),
and it does so through an algorithm that also fires with no lock present at all (Finding 2).
Machine-generated consequences of past events relocate to the current period when their own period
is closed (EV-015, which I did not re-verify but which is the same pattern). In each case the system
resolves an accounting question on the user's behalf, in a way the user was not asked about and
cannot see afterwards. My position is that **an SME ledger must never resolve a period question
silently**. Where the system knows the answer, it should still make the human own it, because the
human is the one who will be asked about it.

**Second, destructive operations dressed as ordinary ones.** Reset-to-draft deletes two subledgers
(Finding 3). Account merge deletes records and rewrites years of posted history by raw SQL, with no
log entry anywhere in the wizard (Finding 7). The same "remove this" gesture yields deletion,
cancellation or a posted reversal depending on configuration the operator cannot see (Finding 4).
None of these carries a mandatory reason, an impact preview, a second approval, or a durable record.
My position is that **destructiveness must be proportional to ceremony**, and that the SMEsPlus
ledger should offer no path by which a posted accounting document ceases to exist.

**Third, controls that are conventions rather than properties.** The deprecated-account block, the
posted-entry field freeze, the audit-trail deletion guard and the lock-exception access model are all
enforced in application code, and several carry documented context bypasses or sudo escalation
(Findings 6 and 8). This is not automatically wrong — but it means that in SMEsPlus, every one of
these must be re-derived as a deliberate requirement with a stated enforcement level, rather than
inherited as an assumption. The clean-room posture actually helps here: we are obliged to restate
each control in our own terms, and that is the right occasion to decide which ones must hold at
storage level.

**Fourth, and most useful, the close as a system-enforced checklist.** The refusal to hard-lock a
period containing draft entries, delivered as a redirect into the offending list, is the best
workflow idea I found (Finding 10). I would build the SMEsPlus close around that pattern and hang
every other finding off it as a checklist item.

On the evidence base itself: it is strong, dense and mostly accurate, and its `file:line` discipline
made independent verification straightforward. I disagree with it in four places. Two are citation or
scope errors that must be corrected before Layer 1 transfer — EV-009's mechanism description points
at the copy path and understates the behaviour (Finding 2), and EV-016's whole-tree negative about
the fiscal year is false, with the entity living one module away in `account_accountant` (Finding 9).
One is an open question that is answerable and answered in the reference's favour — EV-003's
`UNKNOWN` about posting to a deprecated account, which is blocked in three places (Finding 6). One is
a framing correction — EV-021's "append-only" characterisation of lock exceptions, which a
sudo-escalating revoke method contradicts (Finding 8). I record all four as amendments, not as
grounds to reject the package; the design conclusions the evidence base draws survive every one of
them, and in the EV-016 case the conclusion is right for reasons better than the one given.

Two items I flag as `Tolerance = 0` candidates under Constitution principle 13, for Boss to rule on:
**silent period re-dating** (Finding 1) and **unlogged destructive account merge** (Finding 7).

Three items I place on `HOLD / EVIDENCE REQUIRED` and route to the Accounting-Tax track, asserting
nothing about Thai law myself: the acceptability of a ledger date differing from a document date for
VAT and withholding-tax period attribution; the required form of a correction to a document already
issued to a counterparty; and whether Thai statutory reporting expects a posted year-end closing
entry. The first and second of these are **blocking dependencies for the SMEsPlus correction and
period design**, not background questions, and I would not want Wave A closed while they are open.

I approve nothing. These are observations and recommendations for Boss decision.

— Expert 1, Leader Functional Design
