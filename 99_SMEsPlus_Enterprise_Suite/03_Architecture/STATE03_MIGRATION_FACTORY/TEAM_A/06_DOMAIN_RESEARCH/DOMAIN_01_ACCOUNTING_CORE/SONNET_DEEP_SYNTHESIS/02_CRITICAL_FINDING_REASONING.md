> DOMAIN_01 — Accounting Core | Team A PART 2 (Sonnet deep synthesis) | Session SMEPLUS-26-08-29-MIG-A-D01-SONNET-001
> Input: committed Part 1 evidence pack (source of truth). No new source reading except where cited.
> No SMEsPlus design. Boss sole Final Approver.

# 02 — CRITICAL FINDING REASONING (13-point analysis, all 6 findings, independently challenged)

Method: each finding is re-derived from the committed evidence, not assumed correct because
Fable wrote it. Where this pass disagrees with or sharpens Part 1, it is flagged and carried
to `FABLE_SONNET_DISAGREEMENT_REGISTER.md`.

---

## CF-01 — Entry-level debit/credit balance enforcement

1. **Observed:** `_check_balanced` asserts `Σdebit = Σcredit` per entry and raises `UserError`;
   wrapped in `_disable_recursion(..., 'check_move_validity', default=True, target=False)`.
   `account_move_line` carries 4 row-level CHECK constraints (none aggregate). Database-wide
   trigger count = **0** (direct `pg_restore -l`).
2. **Evidence:** P1 `account_move.py:2765,2769`; P2 direct TOC census.
3. **Fact:** the enforcement mechanism (application-only, suppressible, no aggregate DB
   backstop) is now **directly observed**, not inferred.
4. **Inference:** that this constitutes a *financial-correctness risk* is an interpretive
   judgment layered on the fact — clearly labeled as such, not itself evidence.
5. **Business meaning:** the double-entry guarantee depends entirely on disciplined execution
   of application code that can be turned off for a block of work.
6. **Accounting principle:** double-entry bookkeeping — every transaction recorded as equal and
   opposite debits and credits; foundational and universal ([Double-entry bookkeeping —
   Wikipedia](https://en.wikipedia.org/wiki/Double-entry_bookkeeping),
   [Accounting equation — Wikipedia](https://en.wikipedia.org/wiki/Accounting_equation)).
7. **Universal vs vendor-specific:** the *requirement* is universal. The *implementation*
   (app-only, suppressible, no trigger) is vendor-specific — and is a weaker realization of the
   principle than the mechanism inventory shows the vendor is capable of (they wrote 4 CHECK
   constraints elsewhere; they chose not to write a trigger for this one).
8. **Invariant that must be preserved:** every posted journal entry must have total debits
   equal to total credits, in the entry's company currency, provably at the point of persistence.
9. **Failure consequence:** an unbalanced entry silently corrupts the trial balance and every
   report built on it; nothing in the reference system detects this after the fact.
10. **Migration consequence:** migrated entries must be independently validated for balance;
    `state = 'posted'` is not proof of validity.
11. **Audit/control consequence:** an auditor cannot treat ledger presence as proof of balance;
    a compensating aggregate check (per `move_id`) is required and the source system does not
    supply one.
12. **Remains unknown:** whether any entry in the actual snapshot is unbalanced
    (**EVIDENCE_MISSING**, data-level, GAP-D01-11); whether `account_move` itself carries
    header-level CHECK constraints beyond what was enumerated (GAP-D01-13).
13. **What Team B should understand without seeing Odoo:** a journal entry is valid only if its
    debits equal its credits; this system does not guarantee that at the database layer, so any
    successor system must decide, deliberately, where that guarantee lives.

---

## CF-02 — Tamper / audit evidence behaviour

1. **Observed:** `restrict_mode_hash_table` (journal-level boolean) opts a journal into
   `inalterable_hash` + `secure_sequence_number`; disabling is guarded once hashed entries
   exist, but the guard is application-level.
2. **Evidence:** P1 `account_journal.py:145,794–800`.
3. **Fact:** the opt-in field and its disable-guard are directly read.
4. **Inference — CHALLENGED THIS ROUND.** Part 1 characterized this as "opt-in… off by
   default." **The default value of `restrict_mode_hash_table` was never independently
   confirmed by a direct read of the field declaration's `default=` argument in this evidence
   chain.** Only the field's *existence and guard* are confirmed. "Off by default" is a
   reasonable but **unverified** inference from naming convention, not a read fact. Recorded as
   a new unknown (see §11 register) rather than silently preserved as fact.
5. **Business meaning:** ledger tamper-evidence is treated as an elective property of a book of
   record, not a system-wide guarantee.
6. **Accounting principle:** integrity of the audit trail. Genuine external triangulation this
   round: Thailand's e-Tax invoice regime (Electronic Transactions Act) requires "reliable
   methods to maintain message integrity… information… kept so it can be accessed and reused,
   and the meaning does not change," enforced via a digital signature from an ETDA-licensed
   Certification Authority
   ([Can I use a digital signature for e-Tax invoices in Thailand? —
   esignglobal](https://www.esignglobal.com/blog/use-digital-signature-e-tax-invoices-thailand-rd)).
7. **Classification:** the Thai finding is **narrower than the reference system's mechanism** —
   it is scoped to **e-Tax invoices/receipts**, not the general ledger. It is real regulatory
   evidence (**Class B**) for that document class; it does **not** establish that every journal
   entry requires tamper evidence under Thai law. That broader claim remains **G — Unknown**.
8. **Invariant:** an accounting document that has been formally issued or externally reported
   must not silently change without a discoverable trace; for e-Tax invoices specifically, Thai
   law requires this.
9. **Failure consequence:** in a journal without hash protection, a direct alteration of a
   posted entry leaves no system-level trace for that journal.
10. **Migration consequence:** journals lacking hash protection carry a pre-existing audit
    weakness; migrated history from them cannot be assumed tamper-evident by the source
    system's own guarantees.
11. **Audit/control consequence:** integrity status is a per-journal fact, not a system fact;
    an auditor must interrogate each journal's history rather than read one flag.
12. **Remains unknown:** default value of `restrict_mode_hash_table` (newly flagged); whether
    Thai law's e-Tax invoice integrity requirement extends, in substance, to the underlying
    journal entries that back those invoices — plausible but **not evidenced**.
13. **What Team B should understand:** certain accounting documents must be provably unaltered
    once issued — confirmed by Thai statute for e-Tax invoices specifically. Whether that
    extends to the general ledger is an open regulatory question, not something to assume
    either way.

---

## CF-03 — Period lock controls and bypass

1. **Observed:** six company lock-date fields (`fiscalyear_lock_date`, `tax_lock_date`,
   `sale_lock_date`, `purchase_lock_date`, `hard_lock_date`) plus computed `user_*` variants,
   plus `account.lock.exception`, plus a `BYPASS_LOCK_CHECK` context sentinel
   (`bypass_lock_check` in context) that provides a programmatic escape from lock enforcement.
2. **Evidence:** P1 `company.py:60–113`; `account_lock_exception.py`; `account_move.py:69,2807`.
3. **Fact:** existence of all six mechanisms is directly read.
4. **Inference:** "there is no single answer to 'is this period closed'" is a synthesis of the
   fact pattern (independent, potentially-disagreeing controls), not itself a separately
   observed fact. Labeled as inference.
5. **Business meaning:** period close is not one business event here; it is a composite of
   several independently-settable dates governing different transaction classes, with a
   recorded exception path and a code-level bypass.
6. **Accounting principle:** period cutoff control — a core internal-control requirement
   ensuring transactions are not posted into an already-reported period.
7. **Classification:** the *requirement* is universal/regulatory-adjacent. Real cross-ERP
   triangulation: NetSuite expresses it as **one period object with three states (Unlocked /
   Locked / Closed) plus a single override permission**
   ([Locking and Unlocking Accounting Periods —
   NetSuite](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1451780.html)).
   The reference system's *shape* — six independent fields, per-user computed variants, an
   exception object, and a programmatic bypass — is **vendor-specific and more fragmented**
   than at least one major peer's design.
8. **Invariant that must hold:** a transaction dated within a reported/closed period must not
   post, edit, or reverse without a discoverable, authorized override.
9. **Failure consequence:** if the six controls disagree, a transaction can post under one
   control's belief that the period is open while another control would have refused it —
   creating a restatement risk that is hard to detect because no single source of truth exists.
10. **Migration consequence:** historical data must be evaluated against **all six** controls,
    not one, to know what was actually enforceable at any point; the bypass sentinel means
    "locked" cannot be assumed from configuration alone.
11. **Audit/control consequence:** materially higher audit burden than a single period-state
    object — six fields, an exception table, and (if source were available) every code path
    using the bypass sentinel would need review.
12. **Remains unknown — CHALLENGED THIS ROUND.** Part 1's BR-14 states `hard_lock_date` "is not
    reversible in the way other locks are," citing only SE-24 — which shows the field's
    *existence*, not a write-guard proving irreversibility. **No specific mechanism anchor for
    irreversibility was ever read.** This claim is downgraded from VERIFIED FACT to
    **SUPPORTED INFERENCE (unconfirmed)** — see disagreement register.
13. **What Team B should understand:** multiple independent controls govern whether a period is
    open; a correct system needs exactly one authoritative answer per transaction date and
    type, and any override must be visible and permanent on the record — however many controls
    implement it internally.

---

## CF-04 — Reversal relationship

1. **Observed:** lifecycle states are only draft/posted/cancel. Reversal creates a **new**
   move linked via `reversed_entry_id` (inverse `reversal_move_ids`); on posting, a draft
   reversal of a posted original is auto-reconciled against it.
2. **Evidence:** P1 `account_move.py:129–133,623,631,5433,5663,5712`.
3. **Fact:** directly read; minimal inference required.
4. **Business meaning:** correcting a posted mistake does not erase or mark the original wrong
   — it creates a new, linked, independent accounting fact that offsets it. The original stays
   exactly as it was posted.
5. **Accounting principle:** correction-by-reversal. Now **genuinely triangulated as a
   cross-ERP common pattern**: SAP Business One documents that posted journal entries **cannot
   be deleted** — only reversed — explicitly to protect the audit trail
   ([Reverse Journal Entry in SAP Business One —
   sap-business-one-tips.com](https://www.sap-business-one-tips.com/en/reverse-journal-entry/);
   [SAP Community — deleting a Journal Entry
   document](https://community.sap.com/t5/enterprise-resource-planning-q-a/how-to-delele-journal-entry-document-in-sap-business-one/qaq-p/482022)).
6. **Universal/common/vendor-specific:** the *principle* (preserve original, link a correcting
   entry) is now Class **D — cross-ERP common pattern**, upgraded from a solitary observation.
   The *mechanism* (`reversed_entry_id` field, `_reverse_moves` method) remains vendor-specific
   and quarantined.
7. **Invariant:** a correction to a posted fact must never delete or silently mutate the
   original; it must create a new, traceable, linked record.
8. **Failure consequence if violated:** loss of the ability to show what was originally
   recorded versus later understood to be correct — undermines audit and fraud detection.
9. **Migration consequence:** the reversal *relationship* (which move reverses which) is
   business data that must be carried forward; the specific field/table shape must not be
   copied verbatim.
10. **Audit/control consequence:** this is a genuine strength of the reference system, validated
    against peer practice.
11. **Remains unknown:** whether reversal is the *only* correction path in practice, or merely
    available alongside a weaker one — **it is not the only path**, see CF-06. This is the
    central tension in the domain.
12. **What Team B should understand:** correcting a posted fact means posting a new, linked,
    offsetting entry — never altering or deleting the original. This is validated cross-ERP
    practice, not an Odoo idiosyncrasy.

---

## CF-05 — Exact decimal money

1. **Observed:** `debit`, `credit`, `balance`, `amount_currency` are all `numeric` — exact
   decimal, not binary floating point.
2. **Evidence:** P2 direct column-definition observation (strongest evidence class in this
   pack — unambiguous structural fact).
3. **Fact:** fully verified at the database level; no inference involved.
4. **Business meaning:** monetary amounts are stored exactly; summed columns reconcile to the
   cent/satang without representation error.
5. **Accounting principle — CHALLENGED THIS ROUND.** Part 1 classified this as a "universal
   accounting principle." **That overstates its provenance.** No IFRS/IAS clause specifically
   mandating decimal-over-float storage was located or exists to be cited; this is a
   **software/financial-computing engineering norm**, not a formal accounting standard.
   **Reclassified from A to D — cross-vendor/computing common pattern.** The underlying need
   (money must not lose precision) is universally understood, but citing it as "IFRS-grade"
   would be exactly the kind of unsupported authority claim §12 forbids.
6. **Classification:** the one finding where the reference system's implementation is
   **correct** and should be matched or bettered, not challenged.
7. **Invariant:** monetary values must never lose precision to binary floating-point
   representation; a summed column must reconcile exactly to its parts.
8. **Failure consequence (if violated):** silent fractional-currency discrepancies accumulate;
   trial balances fail to tie out; reconciliation becomes unreliable.
9. **Migration consequence:** exact-decimal representation must be preserved or strengthened —
   a correctness floor, not an aspiration.
10. **Audit/control consequence:** none to flag; this is a clean pass.
11. **Remains unknown:** the *rounding rules* applied during computation (decimal places per
    currency, rounding method) were never analysed — `decimal_precision.py` exists and is
    unread (GAP-D01-04). The storage type is verified exact; the arithmetic policy is not.
12. **What Team B should understand:** money is exact decimal, always. This is table stakes,
    already correctly implemented in the reference system.

---

## CF-06 — Mutability of posted history

1. **Observed:** `button_draft`'s guard permits a move currently in `posted` **or** `cancel` to
   return to `draft` — an already-posted, numbered entry can become editable again.
2. **Evidence:** P1 `account_move.py:6108,6109`.
3. **Fact:** the guard condition is directly read.
4. **Inference:** "history is mutable by design" is an interpretive framing of what the guard
   condition implies for audit purposes — labeled as such.
5. **Business meaning:** an entry that has been posted — and possibly externally reported — can
   be pulled back into an editable state and changed, without a forced reversal or any
   structural trace of what changed.
6. **Accounting principle — DIRECTLY IN TENSION WITH CF-04.** The reference system supports a
   sound correction pattern (reversal, CF-04) and an unsound one (reset-to-draft) for the same
   underlying need, and nothing observed forces the sound path.
7. **Classification:** peer-ERP evidence is **directly contradictory** here. SAP Business One
   documents that posted entries **cannot** be edited or deleted — reversal is the *only*
   correction path
   ([sap-business-one-tips.com](https://www.sap-business-one-tips.com/en/reverse-journal-entry/)).
   This makes reset-to-draft **vendor-specific divergence from at least one major peer**, not
   an industry norm. **Class E.**
8. **Invariant that should hold (per principle and peer practice):** once posted — and
   especially once externally reported — an entry's content should be immutable except via a
   new, linked correcting entry.
9. **Failure consequence:** loss of audit trail — original values are overwritten with no
   forced record of what changed, when, or why, beyond whatever optional chatter/tracking
   happens to be configured on the field (a separate, non-blocking mechanism).
10. **Migration consequence:** a migrated entry that was posted, reset, edited and reposted is
    **indistinguishable from data alone** from one posted correctly once — unless message
    history is also migrated and interrogated, which is heavier and less reliable proof.
11. **Audit/control consequence:** the single largest audit-control weakness identified in this
    domain. Combined with CF-01 (suppressible balance check) and CF-02 (opt-in tamper
    evidence), a posted entry in an unprotected journal can be silently altered with no
    database trace and no guaranteed re-validation of balance.
12. **Remains unknown:** whether Enterprise-layer UI (`account_accountant`, OEEL-1, black-box)
    adds friction beyond the core guard — **cannot be determined; the module is unread by
    clean-room rule, not merely unresearched.**
13. **What Team B should understand:** a posted accounting entry should not be silently
    returned to an editable state and altered. The reference system permits this at the core
    data-model level; peer practice forbids it. **This is the strongest identified advancement
    candidate in the domain**, because it directly undermines the very reversal pattern the
    same system otherwise implements well.
