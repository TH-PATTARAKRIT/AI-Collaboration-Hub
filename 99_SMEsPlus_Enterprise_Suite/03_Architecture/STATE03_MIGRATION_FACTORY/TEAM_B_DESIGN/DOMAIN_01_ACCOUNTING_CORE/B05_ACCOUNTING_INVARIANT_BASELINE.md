# B05 — Accounting Invariant Baseline

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B5 — Business Invariant Baseline |
| Method | Starts from Team A's INV-01..06 (`04_BUSINESS_INVARIANT_REGISTER.md`), independently re-evaluated against this domain's own B02–B04 design, plus six independently justified additions |
| **Corrected** | **CORR-B01 / CORR-B02 / CORR-B03 (2026-08-29)** — ChatGPT Independent Design Audit (`aa60c2d0497cefe804d37953bbfaa597c3476d79`) prompted corrections to BINV-06 (period-close no longer a Consumption trigger, per B04 §4), BINV-10 (now explicitly states the Current Earnings transfer that makes MP-02's corrected proof hold post-closing), and a new BINV-11 (historical as-of reproducibility). See [CORR_B01_B02_B03_CORRECTIVE_ROUND.md](CORR_B01_B02_B03_CORRECTIVE_ROUND.md). |
| **Corrected (Round 2)** | **CORR-B2-01/02/03/04 (2026-08-29)** — ChatGPT's Round 2 re-audit (`04e44b06489d8bea6c8d39410050d68cf08bce21`) found BINV-11's Round-1 guarantee insufficient against backdated Corrections (`M-AUD-04`) and BINV-10's "Period close" scope overgeneralized Team A's year-end-specific evidence (`M-AUD-05`). BINV-10 and BINV-11 both substantially rewritten below; new BINV-12 added (Recorded At immutability — the mechanism BINV-11's Round-2 guarantee depends on). See [CORR_B2_CORRECTIVE_ROUND.md](CORR_B2_CORRECTIVE_ROUND.md). |
| **Corrected (Round 3)** | **CORR-B3-04/05 (2026-08-29)** — ChatGPT's Round 3 re-audit (`f6fb633fd141f45caf047bc94d75f84420e1cc6d`) found BINV-10's Round-2 text still described Fiscal Year Close as posting a Current-Earnings-transfer Entry (`M-AUD-07`), and found no invariant guaranteed IAS 8's mandatory exclusion of material prior-period errors from current-period profit or loss (`M-AUD-06`). BINV-10 rewritten again below (no-posted-close model); new BINV-13 added (material prior-period error P&L exclusion). See [CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md](CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md). |
| **Corrected (Round 4)** | **CORR-B4-01/02/03 (2026-08-30)** — ChatGPT's Round 4 re-audit (`9c0a3f2d179994a20f01db16d5713989a78c0b2a`) found BINV-10's Round-3 formula double-counted the designated Retained Earnings account against ledger Equity (`M-AUD-08`), and gated Fiscal-Year earnings inclusion on `FiscalYearClosed`'s declaration timing rather than the Fiscal Year's own calendar boundary (`M-AUD-09`). BINV-10 rewritten a fourth time; new BINV-14 added (Reported Equity non-duplication and declaration-independence). See [CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md](CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md). |
| **Corrected (Round 5)** | **CORR-B5-01/02/05 (2026-08-30)** — ChatGPT's Round 5 re-audit (`de7492afd0af0f58185f3f36940a77f2389aa8b8`) found MP-09's mixed-horizon output was silently treated as a balanced Trial Balance when it is not, once a Fiscal Year has elapsed (`M-AUD-11`), and found no invariant protected a Fiscal Year's boundary dates from silent retroactive editing (`M-AUD-12`). New BINV-15 added (Trial Balance output non-confusion); new BINV-16 added (Fiscal Year boundary historical safety). See [CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md](CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md). |
| **Corrected (Round 6)** | **CORR-B6-01/02/03 (2026-08-30)** — ChatGPT's Round 6 re-audit (`b0ce666dad72909411a49690d0f642313d94dd13`) found BINV-16 protected the boundary from silent editing but never guaranteed the Elapsed test's own viewpoint-consistency (`M-AUD-13`), nor that an Entry's Fiscal-Year membership resolves to exactly one authoritative answer per viewpoint once a post-reliance change legitimately occurs (`M-AUD-14`). New BINV-17 added (Fiscal-Year Membership Viewpoint Coherence). See [CORR_B6_FISCAL_CALENDAR_VIEWPOINT_MEMBERSHIP_CORRECTIVE_ROUND.md](CORR_B6_FISCAL_CALENDAR_VIEWPOINT_MEMBERSHIP_CORRECTIVE_ROUND.md). |

## 1. Independent Evaluation Method

Each invariant below states not just *what* must hold (Team A already established this) but
*how this domain's own design enforces it* — the "Enforcement Objective" column is Team B's
contribution, not a restatement of Team A's observation. Where Team A found the reference
system does not guarantee an invariant, this baseline does not inherit that gap; it states
the enforcement objective this domain commits to instead.

## 2. Baseline

### BINV-01 — Balanced Entry

```
Independent statement: For every COMMITTED Entry, Σdebit(lines) = Σcredit(lines), in the
                        entry's functional currency, at the moment it becomes COMMITTED.
Why required:          The foundational integrity check of double-entry accounting; every
                        report built on the Ledger assumes this holds for every entry it sums.
Accounting basis:       PR-01 (double-entry bookkeeping), PR-02 (accounting equation)
Regulatory basis:       Not independently regulatory — this is an accounting-principle
                        invariant, not a statutory one
Failure consequence:    An unbalanced entry silently corrupts the trial balance and every
                        derived report; undetectable after the fact without a compensating
                        check (Team A CF-01)
Enforcement objective:  Balance validation is structurally synchronous with Posting (B04 §7)
                        — not a separate, skippable, or suppressible step. There is no
                        "commit now, validate later" path. This directly closes the gap Team A
                        found (app-only, suppressible, no DB backstop, 0 triggers).
Evidence:               INV-01, MR-01, ADV-01
Residual assumption:    Whether any entry in a migrated source snapshot is itself unbalanced
                        is a migration-time question (see B10 MG-01), not a design assumption
                        this invariant can resolve — it governs facts committed *through* this
                        domain's own Posting, not facts asserted to have been valid elsewhere.
```

### BINV-02 — Valid Period (Single Authority)

```
Independent statement: For any Entry, there is exactly one authoritative open/closed
                        determination for its date, company, and applicable document class,
                        and Posting consults it directly (never assumes the caller already did).
Why required:           Protects the integrity of previously reported financial statements
                        (period cutoff control).
Accounting basis:       PR-05
Regulatory basis:       Regulatory-adjacent (statutory reporting relies on period finality);
                        no specific Thai statute cited for this invariant itself
Failure consequence:    If multiple independent controls can disagree, a transaction can post
                        under one control's belief the period is open while another would have
                        refused it — a restatement risk with no single source of truth to
                        audit against (Team A CF-03)
Enforcement objective:  One authoritative answer per (date, company, document class), per
                        CAP-04 (B02) — this domain deliberately does not replicate the
                        reference system's six-independent-field shape; ADV-03's objective
                        (fewer controls to inspect) is a direct design input, not a stretch
                        goal.
Evidence:               INV-02, ADV-03, NetSuite cross-ERP triangulation (08_CROSS_SOURCE_
                        TRIANGULATION.md via candidate input)
Residual assumption:    Any authorized override/exception to a closed period must itself be a
                        recorded, non-bypassable action (see B09) — this invariant assumes
                        that control exists; it does not itself design the override mechanism.
```

### BINV-03 — Company Boundary

```
Independent statement: Every Line belongs to exactly one company; no Entry's lines span more
                        than one company; no cross-company reference exists without an
                        explicitly separate, out-of-scope consolidation capability.
Why required:           Legal-entity separation of financial records.
Accounting basis:       Implicit in AP-08's "financial statements per entity" framing
Regulatory basis:       Entity-level statutory reporting requirement (general, not
                        Thailand-specific in the evidence available)
Failure consequence:    Cross-entity contamination of financial statements; legal/statutory
                        risk; a consolidated-looking figure that is not actually a designed
                        consolidation.
Enforcement objective:  Company-boundary check is part of CAP-02's synchronous Posting gate
                        (B02 §2, B04 §7), not a convention assumed to be followed upstream.
Evidence:               INV-03
Residual assumption:    This invariant was flagged MEDIUM confidence by Team A (not
                        independently triangulated as its own topic) — carried forward as a
                        residual assumption, not silently upgraded to HIGH by this phase.
```

### BINV-04 — Currency Consistency

```
Independent statement: (a) A Line's functional-currency amount and transaction-currency
                        amount must agree in sign. (b) Every foreign-currency monetary balance
                        must be remeasured to functional currency at each reporting date.
Why required:           (a) prevents nonsensical mixed-sign postings; (b) IAS 21 compliance —
                        recognition alone is not the whole obligation.
Accounting basis:       PR-06 is not applicable here; basis is AP-07 / RG-05 (IAS 21)
Regulatory basis:       IFRS IAS 21 (international; Thailand's TFRS is IFRS-aligned per the
                        evidence available, not independently re-verified this phase)
Failure consequence:    (a) is prevented at the design's persistence gate; (b) if
                        remeasurement is skipped, foreign-currency exposure is misstated in
                        every report that includes it.
Enforcement objective:  (a) is a Line-level check at CAP-02. (b) is CAP-06's defining
                        obligation — remeasurement is designed as a scheduled, non-optional
                        capability output (a Remeasured event, B04 §3), not a feature that may
                        or may not exist. This is a deliberate design commitment made
                        *because* Team A found (a) implemented but (b) genuinely unknown
                        (INV-04b, ADV-08) — this domain does not assume (b) is satisfied
                        elsewhere; it designs for it explicitly.
Evidence:               INV-04, MR-04, ADV-08
Residual assumption:    Rounding policy per currency (OQ-03/GAP-D01-04) remains open — this
                        invariant requires remeasurement to occur; it does not yet specify the
                        rounding rule that governs its arithmetic. See B08.
```

### BINV-05 — Traceable Correction

```
Independent statement: A correction to a COMMITTED Entry is always a new Entry, permanently
                        and bidirectionally linked to the one it corrects; the original's
                        content is never overwritten.
Why required:           Preserves the ability to show what was originally recorded versus what
                        was later understood to be correct — core to audit and fraud detection.
Accounting basis:       PR-06 (correction-by-reversal, cross-ERP validated pattern)
Regulatory basis:       Not independently regulatory; supports AU-03/PR-07 auditability
Failure consequence:    Loss of the original record defeats the purpose of having a ledger at
                        all — the reference system's own reversal mechanism (a genuine
                        strength, Team A CF-04) shows this is achievable.
Enforcement objective:  The correction relationship is first-class and chainable (B04 §6); a
                        correction is subject to every Posting gate (BINV-01/02/03) exactly
                        like any other Entry — no exemption for "it's just a correction."
Evidence:               INV-05, ADV-04, SAP Business One cross-ERP triangulation
Residual assumption:    None material — this is the domain's most confidently evidenced
                        invariant (HIGH confidence in both Team A's finding and the design
                        response).
```

### BINV-06 — Immutability of Consumed Fact

```
Independent statement: Once a COMMITTED Entry is consumed (B04 §4, corrected at CORR-B01:
                        filed, reconciled, or referenced downstream — period close is
                        deliberately NOT one of these triggers, see below), its content is
                        permanently frozen; the only path to changing what it effectively
                        represents is a linked correction (BINV-05), never in-place mutation.
Why required:           The audit trail is only as strong as its weakest mutability control —
                        this is the single most important invariant in the domain (Team A
                        INV-06 finding: this is CURRENTLY VIOLATED by the reference system).
Accounting basis:       PR-07 (traceability), directly threatened by unconstrained mutability
Regulatory basis:       Supports AU-02/AU-03 and the narrow but real Thai integrity
                        requirements (RG-03/RG-04) for the document classes they cover
Failure consequence:    Silent restatement of history with no forced trace — Team A's
                        single largest identified audit-control weakness (CF-06), directly
                        contradicted by peer practice (SAP B1 forbids editing posted entries).
Enforcement objective:  This is what B04's consumption gate exists to guarantee structurally,
                        not procedurally — "should not be mutated" becomes "cannot be
                        mutated once consumed" at the design level. This is the direct
                        response to ADV-04 (this domain's highest-priority advancement
                        objective).
Evidence:               INV-06, CF-06, ADV-04, ADV-07, disagreement-03 (priority elevation)
Residual assumption:    The consumption-trigger list (B04 §4, now three items, not four) is
                        this domain's own design judgment, not something Team A's evidence
                        dictated in this exact form — flagged explicitly as a Team B design
                        assumption requiring gate review (see B13, B16). **Corrected at
                        CORR-B01:** period close was originally a fourth trigger here; removing
                        it was necessary, not optional — the original wording was internally
                        contradictory against BINV-07 below, not merely an assumption someone
                        might reasonably have chosen differently. Period status now governs
                        Amendment availability through a separate mechanism (B04 §4's Period
                        Lock), never through this invariant.
```

### BINV-07 — Consumption Record Permanence *(new, Team B addition)*

```
Independent statement: Once a Consumed event is recorded against an Entry, it is never
                        retracted, deleted, or reversed by a later action.
Why required:           BINV-06 depends entirely on consumption being a one-way gate. If a
                        Consumed marker could be cleared, the immutability guarantee it
                        protects would be only as strong as whoever can clear that marker —
                        reintroducing exactly the kind of silent-bypass risk Team A found in
                        the reference system's suppressible balance check (CF-01) and
                        bypassable lock check (CF-03), applied to a different mechanism.
Accounting basis:       Derived from PR-07/AU-03, not a restatement of any single Team A ID
Regulatory basis:       None specific — an internal-control design invariant
Failure consequence:    A "consumed" entry could be artificially un-consumed to reopen a
                        mutation path, defeating BINV-06 entirely while appearing compliant.
Enforcement objective:  Consumption events live only in Audit Evidence (CAP-08), which is
                        itself append-only by design (B02 CAP-08, B04 §3) — there is no
                        operation in this domain's capability model that clears a Consumed
                        event, by construction, not by policy.
Evidence:               Derived design requirement; no direct Team A source ID (independently
                        justified per directive §B5's explicit allowance to add invariants)
Residual assumption:    None — this is a closure requirement on this domain's own design, not
                        an external fact requiring evidence.
```

### BINV-08 — Audit Evidence Independence *(new, Team B addition)*

```
Independent statement: The complete history of state-changing actions against any Entry must
                        be reconstructable from Audit Evidence (CAP-08) alone, without relying
                        on the Entry's own current content having preserved anything.
Why required:           Operationalizes LC-04's distinction (the event log's forced,
                        append-only nature is separate from the record's own mutability) as a
                        checkable invariant rather than leaving it as design narrative only.
Accounting basis:       PR-07 (traceability)
Regulatory basis:       Supports AU-03 and general audit-evidence retention (RG-02, 5–7 years)
Failure consequence:    If Audit Evidence ever depends on reading the current Entry to
                        reconstruct history, then any future change to how Entries are stored
                        can silently break auditability — the reference system's optional,
                        bolted-on chatter mechanism (Team A CF-02, LC-04) is the cautionary
                        example this invariant is designed to structurally prevent from
                        recurring.
Enforcement objective:  Audit Evidence is written at the same moment as every CAP-02/03/04
                        state change (B04 §3 event table) and is never derived after the fact
                        from Entry content.
Evidence:               LC-04, CF-02, AU-03
Residual assumption:    None material.
```

### BINV-09 — Account Category Immutability *(new, Team B addition)*

```
Independent statement: An account's accounting category (the classification governing
                        statement placement and carry-forward behavior) does not change once
                        the account has been used in any COMMITTED Entry.
Why required:           If an account's category could change retroactively, every historical
                        statement that placed its balance under the old category becomes
                        silently wrong without any Entry itself having changed — a subtler,
                        structural analogue of BINV-06's concern, applied to CAP-01 rather
                        than to Entries directly.
Accounting basis:       BF-10 / GR-08 ("account type is set and immutable in category meaning")
Regulatory basis:       Supports the general reliability of previously issued statements
                        (same underlying concern as BINV-02)
Failure consequence:    Comparative/historical statements silently misstate prior periods with
                        no Entry-level trace of why — a failure mode Team A's own register
                        named but did not develop into its own invariant.
Enforcement objective:  CAP-01 (B02) permits account creation and, before first use, revision;
                        once an account has been referenced by any COMMITTED Entry, its
                        category becomes frozen — a new account (not a category change) is
                        required to reclassify going forward.
Evidence:               GR-08 (Team A), independently elevated to invariant status this phase
Residual assumption:    Whether accounts may be deprecated (stop accepting new activity)
                        independent of category change is a business-rule question (see B06),
                        not this invariant's concern.
```

### BINV-10 — Carry-Forward Correctness *(new, Team B addition; rewritten at CORR-B2-03/04, CORR-B3-05, and CORR-B4-01/02/03)*

```
ROUND 1 STATEMENT (kept visible, not deleted): "The opening balance of period N+1 ... equals
the closing balance of period N ..., computed by CAP-09 [as a posted fact] ... closing a
PERIOD must additionally transfer Current Earnings ... and reset every Revenue/Expense
account ..." ChatGPT's Round 2 audit (`M-AUD-05`) found this both overgeneralized Team A's
year-end-specific evidence (BF-09) to every ordinary Period, AND — combined with MP-09's
all-time summation — created a genuine double-counting risk (a posted opening-balance Entry
plus the historical activity it repeats). Rewritten below.

Independent statement: **Carry-forward across an ordinary Period boundary is implicit, not a
                        posted fact.** Asset/Liability/Equity account balances accumulate
                        all-time (MP-09); nothing is posted merely because one ordinary
                        Period ends and the next begins, so nothing can double-count.
                        **Fiscal Year Close (CAP-09, redefined) is the only event that posts
                        a new fact for this purpose** — exactly one Entry (MP-11) transferring
                        Current Earnings (Revenue − Expenses for the closing Fiscal Year,
                        MP-02) into a designated formal Equity account. Revenue/Expense
                        accounts are never "reset" by any posted action — their zero-point
                        for a new Fiscal Year follows automatically from MP-09's Fiscal-Year
                        lower bound on Income Statement categories (B07 §1d).
Why required:           Team A's authorized evidence (BF-09) is explicitly year-end, not
                        "every Period" — generalizing it silently changes the meaning of YTD
                        reporting and, combined with an all-time aggregation formula, creates
                        exactly the double-count `M-AUD-05` identified. Restricting the one
                        posted carry-forward action to Fiscal Year Close, and making ordinary
                        carry-forward implicit, closes both problems from the same root cause.
Accounting basis:       BF-09 (year-end, as actually evidenced — not generalized), MP-02/MP-11
                        (corrected)
Regulatory basis:       None specific — supports general statement reliability
Failure consequence:    (as originally identified) a posted opening-balance Entry at every
                        ordinary Period boundary, combined with all-time summation, counts the
                        same balance-sheet amount twice; (newly avoided) resetting Revenue/
                        Expense at every month/quarter close would misstate YTD reporting,
                        which Team A's evidence never authorized in the first place.
Enforcement objective:  MP-09's category-bounded aggregation (B08, corrected) IS the
                        enforcement mechanism — there is no separate "carry-forward posting"
                        capability left to get wrong, because there is no such posting for
                        ordinary Periods. Fiscal Year Close's one Entry (MP-11) is posted
                        through the same CAP-02 gates as any other Entry, not a special step.
Evidence:               AP-14 / BF-09 (now respected at its actual year-end scope), MP-02/MP-11
                        (corrected), `M-AUD-05` (the corrective trigger)
Residual assumption:    The year-end closing *process* that triggers this computation was
                        noted by Team A as unread/unobserved (MR-07 residual note) — this
                        invariant states the required outcome; it does not assume any
                        particular closing procedure achieves it.
```

```
ROUND 3 CORRECTION (CORR-B3-05, kept visible — do not delete the Round 2 statement above):
ChatGPT's Round 3 audit (`M-AUD-07`) found the Round-2 statement above still describes Fiscal
Year Close as posting "exactly one Entry (MP-11) transferring Current Earnings ... into a
designated formal Equity account." This directly contradicts the same statement's own next
sentence ("Revenue/Expense accounts are never 'reset' by any posted action") — MP-11 as
originally drafted was literally a Revenue/Expense-resetting Entry — and, traced through MP-09's
all-time-but-category-bounded aggregation, would corrupt the closing Fiscal Year's own
historical query (an Entry dated inside the year it closes changes what MP-09 Mode 1/Mode 2
compute for any as-of date within that year). The independent statement is corrected below.

Independent statement (superseding the Round 2 text above):
                        **Fiscal Year Close posts NO Entry at all.** It is a purely declarative
                        Audit Event (`FiscalYearClosed`, B04, corrected at CORR-B3-05) that
                        locks the Fiscal Year and marks its Current Earnings as closed. What
                        was previously called the "Current-Earnings transfer" is not a posted
                        fact but a **reporting-time derivation**: Reported Retained Earnings
                        (B07 §1e, new) = the formally-designated Retained Earnings account's
                        own direct-posting balance (e.g. dividend declarations) + the sum, over
                        every closed Fiscal Year, of that year's Current Earnings computed via
                        MP-09 Mode 2. No Entry ever debits Revenue or credits Expense to
                        "close" a year; Revenue/Expense read zero for a new Fiscal Year purely
                        because MP-09's aggregation is Fiscal-Year-bounded for those categories
                        (unchanged from the Round-2 reasoning above) — carry-forward across a
                        Fiscal Year boundary is exactly as implicit as carry-forward across an
                        ordinary Period boundary, just additionally gated on the year being
                        closed.
Why required:           A posted closing Entry is not merely inelegant — it is a genuine
                        arithmetic bug once combined with this domain's own all-time-summation
                        model (MP-09), and it directly contradicts BINV-10's own stated
                        Revenue/Expense-never-reset principle. Removing it removes both defects
                        by removing the one posted fact that could ever violate them, consistent
                        with `M-AUD-07`'s explicit direction to resolve the contradiction by
                        choosing exactly one coherent model.
Accounting basis:       B07 §1d/§1e (new), MP-09 Mode 1/Mode 2 (B08, unchanged mechanism),
                        MP-11 (B08, corrected at CORR-B3-05 to match)
Regulatory basis:       None specific — supports general statement reliability and internal
                        consistency of the domain's own posted-fact model
Failure consequence:    (unchanged from Round 2) a posted opening-balance Entry at ordinary
                        Period boundaries double-counts; (Round 3 addition) a posted
                        Fiscal-Year-Close Entry corrupts the closing year's own historical
                        query and contradicts this domain's Revenue/Expense-never-reset claim
                        — both are now structurally impossible because no such Entry exists.
Enforcement objective:  Reported Retained Earnings is computed, not stored — there is no
                        posted balance to corrupt, and no closing-Entry code path to omit,
                        double-post, or get the sign wrong on. CAP-09 (B02, corrected) exposes
                        only a declare-closed action, never an entry-posting action, for
                        Fiscal Year Close.
Evidence:               `M-AUD-07` (the corrective trigger), B07 §1e (the replacement formula),
                        [B20](B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md) Tests 9-11
                        (numeric verification)
Residual assumption:    Unchanged from Round 2 — the year-end closing *process* that triggers
                        the `FiscalYearClosed` declaration was noted by Team A as
                        unread/unobserved (MR-07); this invariant states the required outcome,
                        not a particular UI/workflow for reaching it.
```

```
ROUND 4 CORRECTION (CORR-B4-01/02/03, kept visible — do not delete the Round 2/3 statements
above): ChatGPT's Round 4 audit found two further defects in the Round-3 statement above.
`M-AUD-08`: "the formally-designated Retained Earnings account's own direct-posting balance...
+ the sum... of that year's Current Earnings" — added to a separately-stated "ledger Equity"
figure elsewhere in this design (B08 MP-02) — double-counts that account's balance, since it
sits inside both. `M-AUD-09`: "every closed Fiscal Year" made this invariant depend on
`FiscalYearClosed`'s *declaration* timing, not the Fiscal Year's own calendar boundary — a
delayed declaration would silently drop a real, already-elapsed year's earnings from every
report. Both corrected below.

Independent statement (superseding the Round 3 text above):
                        **Carry-forward across a Fiscal Year boundary is boundary-driven and
                        non-overlapping, not declaration-driven or double-counted.** Reported
                        Retained Earnings (B07 §1e, corrected) sums the designated Retained
                        Earnings account's direct-posted balance plus every ELAPSED Fiscal
                        Year's Current Earnings (End Date <= query date — a calendar fact,
                        never gated on `FiscalYearClosed` having been declared). Reported
                        Equity (B07 §1f, new) is Other Ledger Equity (every Equity-category
                        account EXCEPT the designated Retained Earnings account) plus Reported
                        Retained Earnings — a partition of the Equity category into two
                        disjoint sets of accounts, so every account contributes exactly once.
                        `FiscalYearClosed` continues to lock the Fiscal Year against ordinary
                        posting/amendment (unchanged from Round 3) but has no bearing
                        whatsoever on either sum.
Why required:           A double-counted Retained Earnings balance overstates Reported Equity
                        by exactly that balance — as material an error as the double-count
                        `M-AUD-05` originally found in Round 2, just relocated to a different
                        term. A declaration-gated boundary makes reporting truth depend on
                        operator timing, which is precisely the kind of dependency the
                        Continuous Ledger philosophy (B07 §1d, since Round 2) exists to avoid.
                        Both are closed by the same two changes: partition Equity
                        non-overlappingly, and gate Fiscal-Year inclusion on the calendar
                        boundary rather than the declaration.
Accounting basis:       B07 §1e/§1f (corrected/new), B08 MP-12 (new — full re-derivation from
                        the raw ledger identity, Proofs A-G)
Regulatory basis:       None specific — supports general statement reliability
Failure consequence:    (`M-AUD-08`) Reported Equity overstated by the designated Retained
                        Earnings account's own balance, every single time it is computed —
                        not an edge case, a standing error in every report under the Round-3
                        formula; (`M-AUD-09`) Reported Equity understated by exactly an
                        elapsed-but-undeclared Fiscal Year's Current Earnings, for as long as
                        the operational close process takes — routinely days to weeks, not a
                        rare edge case either.
Enforcement objective:  Both defects are closed structurally, by the formula's own shape, not
                        by a rule someone must remember to follow: `M-AUD-08` cannot recur
                        because Other Ledger Equity is DEFINED to exclude the one account
                        Reported Retained Earnings already covers; `M-AUD-09` cannot recur
                        because `FiscalYearClosed` is not a term, or inside any term, of either
                        formula (B08 MP-12 Proof F proves Reported Equity is referentially
                        identical immediately before and after the declaration, absent new
                        financial facts).
Evidence:               `M-AUD-08`/`M-AUD-09` (the corrective triggers), B08 MP-12 Proofs A-G
                        (the full re-derivation), [B21](B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md)
                        Tests 1-7 (numeric verification, including the delayed-close scenario)
Residual assumption:    Unchanged from Round 2/3 — the year-end closing *process* that
                        triggers the `FiscalYearClosed` declaration remains an operational
                        matter this invariant does not prescribe. New this round: which
                        specific ledger account is "the designated Retained Earnings account"
                        for a Company is a one-time chart-configuration fact (CAP-01, B10
                        MG-C03) this invariant assumes is correctly and uniquely set, not
                        itself re-derived or validated by this formula.
```

### BINV-11 — Historical As-of Reproducibility *(new, added at CORR-B03; rewritten at CORR-B2-01/02)*

```
ROUND 1 STATEMENT (kept visible, not deleted): "... identical result ... PROVIDED no
Correction or Void dated <= D has been committed since ..." ChatGPT's Round 2 audit
(`M-AUD-04`) found this proviso insufficient: a Correction committed AFTER the fact can still
carry a business date <= D (a "backdated" Correction, B11 Scenario 10 permitted this with no
special rule), which the Round-1 proviso does not rule out. Rewritten below using the two
temporal properties introduced at B07 §1c.

Independent statement: For any account, company, business-date D, and recording-time T,
                        MP-09's Mode-1 aggregation `balance_known(A, C, D, T)` — filtered by
                        Effective Date <= D AND Recorded At <= T — is a **fixed point once T
                        has passed: no future action can ever change it, unconditionally, with
                        no proviso.** This is what "as originally reported / as known at time
                        T" means, and it is now the guarantee this invariant actually states
                        (Round 1's guarantee, filtered by Effective Date alone, is what
                        `M-AUD-04` showed was not actually unconditional). MP-09's Mode-2
                        aggregation `balance_current(A, C, D)` is a DIFFERENT, equally
                        well-defined query — "current best understanding of the position as of
                        D" — and is explicitly allowed to change when a later, dated
                        Correction or Restatement (B04 §5/§6) is committed. **The two modes
                        must never be presented as if they were the same number** (CO-14, B09,
                        new).
Why required:           A financial report issued "as of D" (Mode 1, at the recording-time it
                        was generated) is itself a historical fact whose reproducibility must
                        not depend on trusting that no one ever backdates a correction into
                        the period it covers. Recording Time (BINV-12, new) is what makes this
                        provable rather than merely likely.
Accounting basis:       Direct consequence of BINV-05 (traceable correction is additive,
                        dated) applied to aggregation, combined with BINV-12's Recorded-At
                        immutability
Regulatory basis:       Supports RG-01/RG-02 — an independently audited, retained financial
                        record must mean the same thing on re-examination as it did when issued
Failure consequence:    `M-AUD-04`, concretely: a Correction committed today, backdated to an
                        already-consumed historical period (e.g., because that period was
                        reopened), would appear in a Round-1-style "balance as of D1" query —
                        even though no one could possibly have known about it as of D1.
Enforcement objective:  MP-09 Mode 1 (B08, corrected Round 2) filters by Recorded At <= T, not
                        merely Effective Date <= D. Recorded At cannot be backdated (BINV-12),
                        so Mode 1 is structurally, not procedurally, safe — no business rule
                        has to be followed correctly for the guarantee to hold; a rule that
                        could be violated is exactly what `M-AUD-04` found in the Round-1
                        formula.
Evidence:               Derived design requirement, prompted by ChatGPT's independent audits
                        `D01-B-AUD-03` (Round 1) and `M-AUD-04` (Round 2); no direct Team A
                        source ID
Residual assumption:    None material for Mode 1 — a direct, provable consequence of MP-09's
                        Round-2 formula and BINV-12. Whether Mode 2 ("current/restated") is
                        ever exposed to end users without also showing Mode 1, or how a formal
                        Restatement is surfaced in reporting, is a usability question properly
                        deferred past this domain-design phase (same category as B08 MP-08's
                        residual note on correction-shape usability).
```

### BINV-12 — Recorded-At Immutability *(new, added at CORR-B2-01/02)*

```
Independent statement: Every Entry's Recorded At timestamp (B07 §1c) is assigned exactly
                        once, by the system, at the instant CAP-02 accepts it as authoritative
                        — never before, never chosen or edited by whoever proposes the Entry,
                        and never adjustable afterward by any capability in this domain.
Why required:           This is the single mechanism BINV-11's Mode-1 guarantee depends on
                        entirely. If Recorded At could be set to any value (like Effective
                        Date legitimately can), a backdated Correction could claim an early
                        Recorded At too, and the fix to `M-AUD-04` would collapse back into
                        the same defect it was designed to close.
Accounting basis:       Derived design requirement, not an accounting principle per se — an
                        internal-control/data-integrity invariant this domain's mathematical
                        guarantees (BINV-11) depend on
Regulatory basis:       None specific
Failure consequence:    Every reproducibility claim in BINV-11 becomes advisory rather than
                        structural — exactly the gap between "provided X is followed" (Round 1,
                        insufficient) and "X cannot be violated" (Round 2's actual fix).
Enforcement objective:  No capability in B02's model (CAP-01 through CAP-09) exposes a way to
                        set or alter Recorded At — it is a byproduct of CAP-02's commitment
                        act itself, analogous to how Audit Event identity (B07 §1, point 3)
                        is append-only by construction, not by policy.
Evidence:               Derived design requirement, prompted by `M-AUD-04`; no direct Team A
                        source ID
Residual assumption:    None — this is a closure requirement on this domain's own design
                        (same category as BINV-07), not an external fact requiring evidence.
```

### BINV-13 — Material Prior-Period Error P&L Exclusion *(new, added at CORR-B3-04)*

```
Independent statement: When an Entry (or Correction/Void) is classified a **Material
                        Prior-Period Error** (B04 §3b's decision tree, grounded in IAS 8 paras
                        5/41/46), its correction is never reported as part of the current
                        period's profit or loss. Under Mode 2 (current/restated) aggregation,
                        the correction's effect appears only in: (a) the restated comparative
                        amount(s) for the specific prior period(s) presented that it affects,
                        and (b) the opening balance of Retained Earnings (via B07 §1e's formula)
                        for the earliest period presented, if the error predates every
                        comparative period shown. It never appears as a line item inside the
                        current period's own Revenue/Expense aggregation.
Why required:           IAS 8 para 42 requires an entity to correct material prior-period
                        errors retrospectively by restating comparative amounts, and para 46
                        makes explicit this correction "is not included in profit or loss for
                        the period in which the error is discovered." Without a named invariant,
                        nothing structurally prevents a future implementation from doing the
                        simpler thing — dumping the correction into the current period's own
                        P&L, which is exactly the defect `M-AUD-06` found in this domain's own
                        Round-2 design (B19 Test 11's unqualified "ordinary current-dated Entry
                        is sufficient" conclusion).
Accounting basis:       IAS 8 paras 41, 42, 46 (verified from primary-source PDF text, not
                        secondary summary); TAS 8 (secondary-source confirmed alignment only —
                        confidence distinction preserved per B14's provenance discipline)
Regulatory basis:       IAS 8 / TAS 8 — Accounting Policies, Changes in Accounting Estimates
                        and Errors
Failure consequence:    A material prior-period error corrected through the current period's
                        own P&L overstates or understates that period's genuine operating
                        result, misleading any reader comparing current-period performance
                        against prior periods or against budget/forecast — precisely the
                        distortion IAS 8's retrospective-restatement requirement exists to
                        prevent.
Enforcement objective:  B04 §3b's classification decision tree is the enforcement mechanism —
                        every Entry/Correction/Void must be classified before it is committed,
                        and only the Material-Prior-Period-Error branch (§3c) reaches the
                        restatement path described above; every other branch (current-period
                        error, estimate change, immaterial error) is explicitly permitted to
                        use ordinary current-dated recognition instead (B04 §3b/§3c) — this
                        invariant does not overclaim more restriction than the standard itself
                        requires.
Evidence:               `M-AUD-06` (the corrective trigger), B04 §3b/§3c (the classification
                        and mechanics), [B20](B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md)
                        Tests 2-5 (numeric verification across the four IAS-8-driven
                        sub-cases: ordinary material error, error before earliest comparative,
                        both impracticability sub-cases)
Residual assumption:    **Materiality itself is never computed or invented by this domain's
                        design** (CO-16, B09, new) — it is supplied as a policy/judgment input
                        by whoever authorizes the correction, consistent with IAS 8's own
                        refusal to state a numeric threshold. This invariant is conditioned on
                        that classification already having been made correctly; it does not
                        itself validate the materiality judgment.
```

### BINV-14 — Reported Equity Non-Duplication and Declaration-Independence *(new, added at CORR-B4-01/02/03)*

```
Independent statement: For every Company C and date D: (a) **Non-duplication** — no
                        Equity-category account's balance is ever summed into more than one of
                        {Other Ledger Equity, Reported Retained Earnings} (B07 §1f); the
                        designated Retained Earnings account contributes through Reported
                        Retained Earnings alone, every other Equity account through Other
                        Ledger Equity alone. (b) **Declaration-independence** — Reported Equity
                        (C, D) is a function only of (i) which Entries are COMMITTED as of D
                        and (ii) which Fiscal Years have ELAPSED as of D (B07 §1e); no
                        `FiscalYearClosed` Audit Event's presence, absence, or timing appears
                        in the computation. Consequently, for any two moments D1 < D2 with no
                        Entry committed and no Fiscal Year End Date crossed between them,
                        ReportedEquity(C, D1) = ReportedEquity(C, D2), regardless of any
                        `FiscalYearClosed` declaration recorded between D1 and D2.
Why required:           (a) closes `M-AUD-08` — without an explicit non-duplication guarantee,
                        nothing structurally prevents a future implementation from summing the
                        designated Retained Earnings account's balance twice (once directly,
                        once inside Reported Retained Earnings), overstating every report by
                        that amount. (b) closes `M-AUD-09` — without an explicit declaration-
                        independence guarantee, nothing structurally prevents a future
                        implementation from silently gating Reported Retained Earnings on
                        `FiscalYearClosed` (the most tempting, name-matching implementation
                        choice, and exactly the mistake the Round-3 formula itself made),
                        reintroducing the delayed-close reporting hole.
Accounting basis:       B07 §1e/§1f (corrected/new), B08 MP-12 Proofs B and F
Regulatory basis:       None specific — internal consistency and reporting reliability
Failure consequence:    (a) Reported Equity systematically overstated by the designated
                        Retained Earnings account's own balance; (b) Reported Equity
                        systematically understated by every elapsed-but-undeclared Fiscal
                        Year's Current Earnings, for the duration of the operational close gap
Enforcement objective:  B07 §1f's account partition IS the (a) enforcement mechanism — there is
                        no separate "exclude RE from ledger Equity" step to omit, because Other
                        Ledger Equity is defined by exclusion from the start. B07 §1e's Elapsed
                        test IS the (b) enforcement mechanism — there is no
                        `FiscalYearClosed`-checking step in the Reported Retained Earnings
                        formula to accidentally add, because the formula never references that
                        event at all (B08 MP-12 Proof F derives (b) from this fact directly,
                        not as a separately-argued property)
Evidence:               `M-AUD-08`/`M-AUD-09` (the corrective triggers), B08 MP-12 (Proofs B, F),
                        [B21](B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md) Tests 1, 2, 5, 6, 7
                        (numeric verification of both (a) and (b))
Residual assumption:    Same as BINV-10's Round-4 residual note — which account is "the
                        designated Retained Earnings account" is assumed correctly and uniquely
                        configured per Company (CAP-01), not re-derived by this invariant.
```

### BINV-15 — Trial Balance Output Non-Confusion *(new, added at CORR-B5-01/02)*

```
Independent statement: This domain's design produces (at most) three distinct, precisely-named
                        outputs that could each colloquially be called a "balance" or
                        "trial balance" — and they are never confused with one another, in any
                        report, artifact, or design document this domain produces:
                        (a) the **Raw Cumulative Trial Balance** — every Account Category on
                        one common horizon (ledger inception through D, MP-09
                        `CumulativeAccountBalance`), balanced directly and unconditionally;
                        (b) the **Current-Fiscal-Year Reporting Balance** — Balance Sheet
                        cumulative, Income Statement Fiscal-Year-bounded (MP-09
                        `FiscalYearActivity` for Revenue/Expense) — a genuine reporting view,
                        but NEVER itself labeled "balanced" or "a Trial Balance," because it
                        is not, once any Fiscal Year has elapsed; (c) the **Balanced
                        Presentation Trial Balance**, if retained — (b) plus one explicit,
                        clearly-labeled, never-posted derived bridge line (MP-12 Proof G3).
Why required:           ChatGPT's Round 5 audit (`M-AUD-11`) found this domain's own Round-4
                        design (MP-12 Proof G) silently conflated (a) and (b) — claiming (b)
                        balances "via Proof A" when Proof A's precondition (one common horizon)
                        does not hold for (b) once a Fiscal Year has elapsed. Verified failure:
                        Company X, D = Jan 5 2025 — (b)'s mixed-horizon sum is off by exactly
                        250 (the prior elapsed Fiscal Year's Current Earnings). Without a named
                        invariant forbidding this conflation, a future implementation (or a
                        future corrective round) could silently reintroduce it, exactly as
                        Round 4 did despite Round 4's own Proof A/B being careful about
                        horizons everywhere except Proof G.
Accounting basis:       B08 MP-09 (renamed/split), MP-12 Proofs G1-G4 (rebuilt) — internal
                        mathematical consistency, not an external accounting-standard citation
Regulatory basis:       None specific — internal consistency and reporting reliability
Failure consequence:    A reader (or an implementation) trusting (b) as if it were a balanced
                        Trial Balance would observe an unexplained imbalance equal to every
                        elapsed Fiscal Year's accumulated Current Earnings — and, worse, might
                        "fix" the apparent imbalance by reintroducing a posted closing Entry
                        (exactly the `M-AUD-07`/`M-AUD-09` defects this design has twice now
                        rejected) rather than recognizing that (b) was never supposed to
                        balance on its own.
Enforcement objective:  MP-09's renaming (CumulativeAccountBalance vs. FiscalYearActivity, no
                        formula named merely "Account Balance / Trial Balance" any longer) and
                        MP-12's G1/G2/G3 structure ARE the enforcement mechanism — there is no
                        single formula left in this design whose name or output could be
                        mistaken for "the balanced Trial Balance" without the reader first
                        choosing which of G1/G2/G3 they mean.
Evidence:               `M-AUD-11` (the corrective trigger), B08 MP-09/MP-12 (corrected),
                        [B22](B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md)
                        Tests 1-4 (numeric verification, including the exact failure case)
Residual assumption:    None beyond MP-12's own — this is a closure requirement on this
                        domain's own design terminology (same category as BINV-07), not an
                        external fact requiring evidence.
```

### BINV-16 — Fiscal Year Boundary Historical Safety *(new, added at CORR-B5-05)*

```
Independent statement: A Fiscal Year's Start/End boundary that has governed any COMMITTED
                        accounting fact, has elapsed, or has been referenced by an issued/
                        consumed report cannot be changed in place in a way that silently
                        changes historical classification or reporting. A post-reliance
                        boundary change is always a formal, audited, CO-15-tier-or-stricter
                        action (B07 §1h, new), recorded as a new versioned fact, never a
                        silent overwrite of the old value — and, by default, never
                        retroactively moves an already-COMMITTED Entry's Fiscal-Year
                        membership without a further, separately-gated reclassification
                        action.
Why required:           ChatGPT's Round 5 audit (`M-AUD-12`) found that B07 §1e's Elapsed test
                        (CORR-B4-03) — a pure calendar comparison, deliberately given no
                        viewpoint parameter — depends entirely on a Fiscal Year's Start/End
                        boundary being a fixed, trustworthy fact. Nothing in the Round-4 design
                        actually protected that boundary from retroactive editing. `Recorded
                        At` (BINV-12) protects Entry-level backdating; nothing protected the
                        calendar configuration those Entries are measured against.
Accounting basis:       B07 §1h (new) — an internally-derived historical-reproducibility
                        requirement, the same category as BINV-11/BINV-12, not a cited external
                        accounting standard
Regulatory basis:       None specific — no Thai-specific regulatory requirement is invented for
                        this control (explicitly, per directive instruction); it is derived
                        entirely from this domain's own historical-reproducibility discipline
Failure consequence:    Without this invariant, an administrator could silently change which
                        Fiscal Years are Elapsed at any date D, which Revenue/Expense Lines
                        belong to which Fiscal Year's Current Earnings, which terms enter
                        Reported Retained Earnings, and what `ReportedEquity_Known(C,D,T)`
                        reconstructs — all without any Entry, Correction, Restatement, or
                        (before this correction) even an Audit Event — defeating BINV-11's
                        reproducibility guarantee from a direction Entry-level immutability
                        never covered.
Enforcement objective:  B07 §1h's Versioned Fiscal Calendar model IS the enforcement mechanism
                        — pre-reliance changes update the one current version harmlessly
                        (nothing yet depends on the old value); post-reliance changes require
                        the new `FiscalYearBoundaryChanged` Audit Event (B04, new) at an
                        authorization tier at least as strict as Restatement (CO-15, reused),
                        and the old version remains permanently queryable for any
                        Known-viewpoint reconstruction with T fixed before the change.
Evidence:               `M-AUD-12` (the corrective trigger), B07 §1h (the model and its
                        comparison against boundary-immutability-after-use),
                        [B22](B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md)
                        Tests 12-15 (numeric verification, including an attempted silent edit
                        being rejected/routed through controlled semantics, a post-consumption
                        report remaining reproducible, an authorized future-dated change, and
                        multi-company calendar isolation)
Residual assumption:    The exact authorization tier for a post-reliance boundary change is a
                        genuine open Boss-level policy question (flagged as new Team B
                        assumption #7, [B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §6, and
                        [H](DOMAIN_01_ACCOUNTING_CORE_H_DESIGN_FINAL_GATE_CANDIDATE.md)) — this
                        invariant states CO-15's tier as the working default (reusing an
                        existing tier rather than inventing a new one), not as a settled,
                        evidence-derived answer the way CO-16's materiality-policy-input
                        decision was.
```

### BINV-17 — Fiscal-Year Membership Viewpoint Coherence *(new, added at CORR-B6-01/02/03)*

```
Independent statement: (a) **Viewpoint-consistent boundary lookup** — every Elapsed
                        determination and every Fiscal-Year-boundary lookup embedded in a
                        `_Known(...,T)` formula uses the boundary version knowable/authoritative
                        AT T (`FiscalYearDefinition_Known`/`Elapsed_Known`, B07 §1i), never
                        today's `_Current` boundary; a `_Current` formula uses today's latest
                        authoritative version. The two are never mixed within one report. (b)
                        **Single authoritative membership per viewpoint** — for any Entry E and
                        any fixed viewpoint (a Known cutoff T, or Current), exactly one Fiscal
                        Year is E's authoritative membership (`Membership_Known(E,T)`/
                        `Membership_Current(E)`, B07 §1j); an Entry is never left interpretable
                        under two incompatible calendar versions at once. (c) **No unresolved
                        hybrid state** — a post-reliance boundary change and any affected Entry's
                        membership reclassification occur atomically, in one action
                        (`FiscalYearMembershipRestated`, B04/B07 §1j); there is no reachable
                        state where a new boundary version exists for an already-relied-upon
                        Fiscal Year while affected Entries' Current-viewpoint membership has not
                        yet been updated to match.
Why required:           ChatGPT's Round 6 audit found two related gaps in Round 5's own new
                        design surface: `M-AUD-13` — B07 §1g's claim that Elapsed "never takes a
                        viewpoint parameter" directly contradicted §1h's own Known/Current
                        boundary model, meaning a literal implementation could silently use
                        today's calendar inside a historical reconstruction. `M-AUD-14` — §1h
                        permitted a post-reliance boundary version to exist without a
                        synchronized Entry-membership update, leaving Current-viewpoint
                        reporting formulas with no defined answer during the gap. Both are, in
                        different ways, a single underlying risk: a report that is not
                        consistently anchored to one viewpoint throughout.
Accounting basis:       B07 §1i/§1j (new) — an internally-derived coherence requirement, the
                        same category as BINV-11/BINV-12/BINV-16, not a cited external
                        accounting standard
Regulatory basis:       None specific — no Thai-specific regulatory requirement is invented for
                        this control; it is derived entirely from this domain's own
                        historical-reproducibility discipline, extended to the calendar's
                        membership semantics
Failure consequence:    Without (a), a Known-viewpoint report (e.g., a reconstruction of a
                        Balance Sheet originally issued at T) could silently change after a
                        later, legitimate calendar policy change — defeating BINV-11's guarantee
                        from a direction Entry-level immutability alone cannot reach. Without
                        (b)/(c), a Current-viewpoint report generated during an unsynchronized
                        gap could show December activity under FY2024 in one query and FY2025 in
                        another, with no way to tell which is authoritative — a silent internal
                        contradiction, not merely an inconvenience.
Enforcement objective:  (a) is enforced structurally by B07 §1i's Recorded-At-filtered
                        `FiscalYearDefinition_Known` — the same mechanism BINV-11/12 already
                        prove unconditional, applied one level up. (b)/(c) are enforced by B07
                        §1j's adopted change model (Option A, refined): `FiscalYearBoundaryChanged`
                        is constitutionally barred from reaching backward over reliance, so the
                        only mechanism that CAN move a relied-upon Entry's membership
                        (`FiscalYearMembershipRestated`) is defined to do so atomically, by
                        construction — there is no intermediate, partially-applied state for an
                        implementation to accidentally expose.
Evidence:               `M-AUD-13`/`M-AUD-14` (the corrective triggers), B07 §1i/§1j (the
                        formulas and the adopted model),
                        [B23](B23_CORR_B6_FISCAL_CALENDAR_VIEWPOINT_AND_MEMBERSHIP_REGRESSION.md)
                        (numeric verification, all 15 mandatory scenarios)
Residual assumption:    Same as BINV-16's — the exact authorization tier for a post-reliance
                        change (now covering both `FiscalYearBoundaryChanged`'s pre-reliance/
                        future-only scope and the new `FiscalYearMembershipRestated`) remains the
                        genuine open Boss-level policy question flagged as Team B assumption #7
                        ([B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §6) — unchanged, not narrowed
                        or widened, by this round's corrections, since this round selects WHICH
                        mechanism applies WHEN, not WHAT tier governs it.
```

## 3. Coverage Check Against Mandatory Areas

```
Debit/Credit balance    : BINV-01                              — COVERED
Period validity         : BINV-02                              — COVERED
Company boundary        : BINV-03                              — COVERED
Currency consistency    : BINV-04                              — COVERED
Correction traceability : BINV-05                               — COVERED
Auditability            : BINV-06, BINV-07, BINV-08             — COVERED (three, not one —
                           judged insufficient to cover with a single invariant given this is
                           the domain's central weakness)
Independently added     : BINV-09 (classification integrity), BINV-10 (continuity integrity,
                           rewritten Round 2, Round 3, and Round 4), BINV-11 (historical
                           reproducibility, rewritten Round 2), BINV-12 (recording-time
                           immutability, added Round 2), BINV-13 (material prior-period error
                           P&L exclusion, added Round 3), BINV-14 (Reported Equity
                           non-duplication and declaration-independence, added Round 4),
                           BINV-15 (Trial Balance output non-confusion, added Round 5),
                           BINV-16 (Fiscal Year boundary historical safety, added Round 5),
                           BINV-17 (Fiscal-Year Membership Viewpoint Coherence, added Round 6)
```

**B5 = COMPLETE.** *(Corrected at CORR-B01/B02/B03/CORR-B2-01..04/CORR-B3-04/05/CORR-B4-01..03/
CORR-B5-01/02/05/CORR-B6-01/02/03 — see header. Corrections are additive to this record, not a
rewrite of it: BINV-01..05, 07..09 are unchanged since the original B5 pass. BINV-06 was amended
once (Round 1). BINV-11 was amended once (Round 1), then substantially rewritten (Round 2).
BINV-10 was amended once (Round 1), substantially rewritten (Round 2), rewritten a third time
(Round 3, `M-AUD-07` — no-posted-close model), then rewritten a fourth time (Round 4,
`M-AUD-08`/`M-AUD-09` — non-overlapping decomposition and boundary-driven inclusion) — every
prior version kept visible at each step. BINV-12 was new at Round 2. BINV-13 is new at Round 3
(`M-AUD-06` — material prior-period error P&L exclusion, IAS 8 paras 41/42/46). BINV-14 is new
at Round 4 (`M-AUD-08`/`M-AUD-09`). BINV-15/16 are new at Round 5 (`M-AUD-11`/`M-AUD-12` — Trial
Balance output non-confusion and Fiscal Year boundary historical safety). BINV-17 is new this
round (Round 6, `M-AUD-13`/`M-AUD-14` — Fiscal-Year membership viewpoint coherence, the fourth
consecutive round in which independent re-audit found a gap in this domain's own immediately
prior round's new design surface).)*
