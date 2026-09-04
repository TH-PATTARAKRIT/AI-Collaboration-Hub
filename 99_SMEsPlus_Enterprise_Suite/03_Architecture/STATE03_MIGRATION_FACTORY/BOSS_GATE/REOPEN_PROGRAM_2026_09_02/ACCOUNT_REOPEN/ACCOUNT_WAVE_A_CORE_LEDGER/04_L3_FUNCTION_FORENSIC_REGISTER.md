# 04 — LEVEL 3: FUNCTION FORENSIC REGISTER

Layer 1 clean-room · cites `EV-0NN` · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

Each function is traced `Trigger → Preconditions → Processing → Validation → Accounting Effect →
Failure → Correction → Audit`, then stress-tested against the mandatory path list.

---

## FN-01 — Create an account

**Trigger** user action, chart template provisioning, or automatic creation of a journal default account.
**Preconditions** at least one owning company; a code for every owning company.
**Processing** the record is created; the code is written into per-company storage; uniqueness is asserted afterwards.
**Validation** code character set; a code present for every company; no parent or child company already holds that code; type consistency with journal usage; liquidity accounts single-company.
**Accounting effect** none until an item is posted to it.
**Failure** duplicate code inside a company is rejected only if the check runs.
**Correction** edit the code, or merge (destructive).
**Audit** code, name, type, reconcilability, tags and deprecation carry change tracking.

| Path | Behaviour | Evidence |
|---|---|---|
| Alternate | The same account may be extended to further companies with a different code in each | `EV-001` |
| Exception | Uniqueness is asserted by application logic with **no storage-level constraint**, and a documented deferral context suppresses it during multi-step writes | `EV-002` |
| Concurrency | Two simultaneous creates of the same code in one company can both satisfy their own check and both commit | `INFERENCE` from `EV-002` |
| Missing configuration | An account with no owning company is rejected | `EV-019` |
| Permission boundary | Not established at this level — see file 14 | `GAP-C01` |

---

## FN-02 — Deprecate an account

**Trigger** user sets the deprecation flag.
**Preconditions** the account is not used in a tax distribution.
**Processing** a boolean is set.
**Validation** the tax-distribution check only.
**Accounting effect** none. Balances remain; the account remains postable through configuration paths.
**Failure** none observed.
**Correction** unset the flag.
**Audit** tracked.

| Path | Behaviour | Evidence |
|---|---|---|
| Exception | There is **no** check for a non-zero balance, unreconciled items, or use as a journal default | `EV-003` |
| Invalid state | A deprecated account nominated as a journal default continues to receive automatic postings | `INFERENCE` from `EV-003` |
| Archive | No archive state exists in the scope read | `EV-003` |

`RECOMMENDATION:` SMEsPlus should separate three states the reference model conflates into one flag —
*not offered for new selection*, *closed to all posting*, and *archived from the working chart but
retained for history*. Only the third is a lifecycle end.

---

## FN-03 — Merge accounts

**Trigger** user action on two or more selected accounts.
**Preconditions** write access to all of them and access to every owning company.
**Processing** one account survives and is extended to the others' companies, keeping their codes; every reference — **including posted journal items** — is retargeted to the survivor; the others are deleted.
**Validation** access rights; company access.
**Accounting effect** balances are preserved. **Provenance is not**: a posting made years ago now reports the surviving account, and the account it originally named no longer exists.
**Failure** none observed at this level.
**Correction** **none identified — this operation appears irreversible.** `UNKNOWN — EVIDENCE REQUIRED`.
**Audit** not established — `GAP-C02`.

| Path | Behaviour | Evidence |
|---|---|---|
| Exception | Where entries are hashed, the account holding them is forced to be the survivor so its identity is preserved and the hash stays valid | `EV-004` |
| Consequence | That protection exists **only when hashing is enabled**, which is off by default | `EV-004`, `EV-011` |

`RECOMMENDATION:` this is the clearest case in Wave A where the reference behaviour must be
classified `REJECT`. A ledger that rewrites the account on a posted item is not auditable. SMEsPlus
should model account *replacement* as a forward-dated succession relationship, never as a rewrite.

---

## FN-04 — Assign an entry number

**Trigger** posting an entry that has no number.
**Preconditions** a journal; a date; an existing series to extend, or a starting pattern.
**Processing** the highest existing number under the same prefix is read from the ledger itself, parsed by pattern into prefix/year/month/counter, and incremented.
**Validation** the encoded period must match the entry's date — **unless** the entry's date is on or before a configuration parameter, in which case the check is skipped entirely.
**Accounting effect** the entry acquires its identity in the series.
**Failure** a prefix change mid-period does not re-base the series, because the "previous" number is the greatest by text ordering.
**Correction** a resequencing operation exists; gaps are flagged rather than prevented.
**Audit** gaps are marked on the entry and surfaced on the journal.

| Path | Behaviour | Evidence |
|---|---|---|
| Concurrency | Uniqueness is a **partial** storage constraint covering posted entries only; the increment takes its lock through that constraint | `EV-006` |
| Exception | Because the constraint does not cover drafts, two draft entries may hold the same number; the conflict surfaces at posting | `EV-006` |
| Invalid state | A tenant-wide configuration parameter can disable the date/number alignment control | `EV-007` |
| Retry / idempotency | Not established — `GAP-C03` |

---

## FN-05 — Post an entry

**Trigger** user action, scheduled auto-post, or a producing module.
**Preconditions** state is draft; at least one substantive item; the journal is active; posting permission held.
**Processing** the accounting date is resolved against the effective lock and **re-dated forward if locked**; a number is assigned; state becomes posted and the "has been posted" flag is set permanently; reversal counterparts are auto-matched; items marked for matching are reconciled; where the journal is in secure mode, the entry and its predecessors back to the last hashed entry are hashed.
**Validation** completeness, balance, date, journal.
**Accounting effect** **this is the accounting event.** The ledger now asserts the fact.
**Failure** posting is refused for a non-draft entry, an empty entry, or an inactive journal.
**Correction** un-post (destructive), reverse (additive), or cancel (routes through un-post).
**Audit** state change is tracked; hashing writes a log message to the entry's thread.

| Path | Behaviour | Evidence |
|---|---|---|
| Backdating | Silently re-dated to the day after the lock — **not rejected** | `EV-009` |
| Locked period | As above; the lock is a re-dating rule, not a refusal rule | `EV-009` |
| Duplicate event | Guarded only by number uniqueness at posting; no business-level idempotency key found | `GAP-C03` |
| Multi-currency | Both amounts are carried; the rate is resolved from the daily table | `EV-013`, `EV-018` |
| Permission boundary | An invoicing-level group is required; there is no separate *approval* step before posting | `EV-011` |
| Partial state | Posting is transactional; a partially posted batch was not observed |

---

## FN-06 — Reset an entry to draft (un-post)

**Trigger** user action.
**Preconditions** state is posted or cancelled; no cancellation-request requirement; not an exchange-difference entry; not a cash-basis tax entry; **not hashed**; the entry's date is not inside a locked period.
**Processing** in order — **every analytic line of every item is deleted**; **every reconciliation on those items is removed**; state becomes draft; generated document attachments are detached and renamed.
**Validation** as preconditions.
**Accounting effect** the accounting event is retracted. Two subledgers are destroyed as a side effect.
**Failure** refused for the categories above.
**Correction** re-post — which regenerates analytic lines but does **not** restore the previous matching.
**Audit** state change tracked; the destruction of analytic lines and matches is not itself an accounting record.

| Path | Behaviour | Evidence |
|---|---|---|
| Exception | Hashed entries cannot be un-posted — this is the only unconditional immutability in Wave A | `EV-012` |
| Locked period | Un-posting inside a locked period is refused | `EV-022` |
| Consequence | The number is retained, so the series is not disturbed; the "has been posted" flag also persists | `EV-011` |

`RECOMMENDATION:` classify un-posting `REJECT` for SMEsPlus as a general correction path. Its
destruction of matching history and analytic records is silent and unrecoverable. Correction of a
posted fact should be additive.

---

## FN-07 — Reverse an entry

**Trigger** user action or an automatic consequence (unreconciliation, cancellation of a generated entry).
**Preconditions** the original is posted.
**Processing** a new entry is created with mirrored amounts, at a date resolved through the same lock rules, linked to the original.
**Validation** standard entry validation.
**Accounting effect** **an additive accounting event.** The original remains.
**Failure** the reversal itself is re-dated if its natural date is locked.
**Correction** reverse the reversal.
**Audit** the link between original and reversal is stored, and a message is written to both.

| Path | Behaviour | Evidence |
|---|---|---|
| Alternate | When cancelling, the reversal is posted and auto-matched to the original so both drop out of open items | `EV-012` |
| Locked period | The reversal lands in the first open period, not the original period | `EV-009`, `EV-015` |

---

## FN-08 — Delete an entry

**Trigger** user action.
**Preconditions** depend entirely on configuration. Where the audit-trail flag is on: an entry that has ever been posted **cannot** be deleted. Where it is off: it can. Additionally, an entry that is not the last in its number series cannot be deleted without elevated rights, to avoid creating a gap.
**Processing** items are deleted, then the entry.
**Validation** as above.
**Accounting effect** the accounting fact ceases to exist.
**Failure** refused per configuration.
**Correction** none — deletion is terminal.
**Audit** where the protection is bypassed by context, a formatted description of the deleted entry and its account balances is written to the **application log, not to the database**.

| Path | Behaviour | Evidence |
|---|---|---|
| Exception | The bypass exists as a context flag, not as an authorised user action with a reason | `EV-011` |
| SaaS consequence | The only surviving evidence of a bypassed deletion leaves the tenant database entirely | `EV-011` |

`RECOMMENDATION:` classify `REJECT`. In SMEsPlus, a posted accounting event must not be deletable
by any path, and any deletion evidence must live inside the tenant's own data.

---

## FN-09 — Reconcile items

**Trigger** user action, automatic matching rule, payment registration, or posting of a reversal.
**Preconditions** items are on a reconcilable account, unbalanced, and share a partner and account context.
**Processing** pairwise match records are created carrying the matched amount in company currency and in each side's transaction currency; residuals are recomputed and stored; the matching marker is set; when residual reaches zero a full match is created; where the two sides' rates differ, an **exchange difference entry is created and posted**; where cash-basis tax applies, **cash-basis tax entries are created and posted**.
**Validation** both sides must carry a resolved transaction currency.
**Accounting effect** settlement state changes **and** new accounting events may be emitted.
**Failure** a generated entry whose natural date is locked is dated **today** instead.
**Correction** unreconcile — which reverses the exchange entry, itself an accounting event.
**Audit** match records persist; a dedicated matching history artefact was not identified.

| Path | Behaviour | Evidence |
|---|---|---|
| Partial | Residual is reduced; the marker is `P`; no full match exists; ageing uses the maximum matched date | `EV-014` |
| Multi-currency | Three amounts per match make the difference computable | `EV-014` |
| Locked period | Generated consequences relocate to the current period, breaking period attribution | `EV-015` |
| Reversal after reconciliation | Removing a full match reverses the exchange entry and re-matches the reversal against the original so the counterparty account does not show a residue | `EV-014` |

---

## FN-10 — Set or move a lock date

**Trigger** user action, or automatically when a tax return is posted (tax lock only).
**Preconditions** for the hard lock: no draft entries on or before the intended date; the new value is on or after the current value; it may never be cleared. For any fiscal-effective lock: no unreconciled bank statement lines remain in the period.
**Processing** the date is written; effective locks are recomputed per user, taking exceptions into account.
**Validation** as preconditions.
**Accounting effect** none directly. It changes how *subsequent* postings are dated.
**Failure** the two preconditions are the only refusals.
**Correction** soft locks move backwards freely — **this is reopening, and it requires no ceremony**. The hard lock never moves backwards.
**Audit** lock dates carry change tracking on the company record.

| Path | Behaviour | Evidence |
|---|---|---|
| Cascade | A parent company's hard lock raises every subsidiary's effective hard lock | `EV-008` |
| Reopening | A soft lock can be moved back by anyone who may edit company settings; there is no separate reopening authority | `EV-008` |

---

## FN-11 — Grant a lock exception (temporary unlock)

**Trigger** user action by an accounting manager.
**Preconditions** the exception must change exactly one lock field.
**Processing** a record is created naming the field, the relaxed date, the company's lock date at that moment, optionally a user, optionally an end date-time, and optionally a reason.
**Validation** exactly one field.
**Accounting effect** none directly; it lowers the effective lock for the named scope, so subsequent postings are no longer re-dated.
**Failure** none observed.
**Correction** revocation exists as a state; exceptions cannot be edited or deleted.
**Audit** creation is written to the company's message thread with a before/after tracking value.

| Path | Behaviour | Evidence |
|---|---|---|
| Exception | An exception with no user applies to **every** user; with no end date it is valid **forever** | `EV-021` |
| Control weakness | The reason is **optional**; there is no second-person approval | `EV-021` |
| Control strength | Exceptions are append-only and are logged with before/after values | `EV-021` |

---

## FN-12 — Close a period / close a year

**Trigger** — **there is no such function.**
**Processing** closing a month means moving a lock date forward. Closing a year means the same thing.
**Accounting effect** none is posted. The year's result is computed **at report time** and presented against the current-year-earnings account.
**Failure** none — there is nothing to fail.
**Correction** move the lock back, unless it is the hard lock.
**Audit** the lock change is tracked; there is no close artefact to attest, no closer, no close date, no close checklist.

| Consequence | Evidence |
|---|---|
| Month 12 is procedurally identical to any other month — consistent with the standing Boss baseline | `EV-016` |
| Retained-earnings handling has **no reference implementation to adapt**; it is entirely an SMEsPlus design decision | `EV-016` |
| There is no artefact recording *who* closed a period, *when*, or *on what basis* | `EV-016`, `GAP-G01` |

---

## FN-13 — Establish opening balances

**Trigger** company setup or migration.
**Preconditions** a current-year-earnings account exists, or is created on demand.
**Processing** an ordinary entry is created in a nominated journal; per-account opening amounts are written into it; it is balanced against the current-year-earnings account.
**Validation** ordinary entry validation.
**Accounting effect** the starting position becomes ledger fact.
**Failure** ordinary.
**Correction** edit the entry — subject to the same posted-entry guard as any other.
**Audit** ordinary.

| Consequence | Evidence |
|---|---|
| "Accounting is initialised" is defined as *this entry exists and is posted* | `EV-017` |
| There is **no carrier** for provenance — which legacy system, which extraction run, which reconciliation state each opening figure came from | `EV-017` |
| Opening balances inherit every property of ordinary entries, including deletability where the audit-trail flag is off | `EV-011`, `EV-017` |

---

## CHECKPOINT L3

| Item | Record |
|---|---|
| Scope completed | 13 functions traced end to end with mandatory path stress tests |
| Evidence inspected | `EV-001` through `EV-023` |
| Verified findings | Three functions destroy data as a silent side effect (un-post, merge, delete-with-bypass); one function does not exist at all (period close); one is silently re-dating rather than refusing (post under lock) |
| Contradictions | `CONTRA-03` (identity stability vs merge) confirmed at function level; `CONTRA-04` raised (reconciliation emits events into the wrong period under lock) |
| Unknowns | Merge reversibility and audit (`GAP-C02`); posting idempotency (`GAP-C03`); account permission boundary (`GAP-C01`) |
| Risks | The correction methodology is the highest-risk open decision: the reference default path is destructive |
| Expert disagreements | Deferred to Level 12 |
| Audit challenges | Challenge unit tasked against `EV-016` and `EV-010` |
| Next research target | Level 4 — cross-module accounting dependency |

`CHECKPOINT L3 RECORDED — CONTINUING AUTOMATICALLY.` Not Boss approval.
