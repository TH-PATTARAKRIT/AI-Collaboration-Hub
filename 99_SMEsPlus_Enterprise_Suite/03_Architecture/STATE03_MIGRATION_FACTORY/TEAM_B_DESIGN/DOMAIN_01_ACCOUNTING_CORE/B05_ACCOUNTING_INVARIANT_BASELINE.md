# B05 — Accounting Invariant Baseline

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B5 — Business Invariant Baseline |
| Method | Starts from Team A's INV-01..06 (`04_BUSINESS_INVARIANT_REGISTER.md`), independently re-evaluated against this domain's own B02–B04 design, plus six independently justified additions |
| **Corrected** | **CORR-B01 / CORR-B02 / CORR-B03 (2026-08-29)** — ChatGPT Independent Design Audit (`aa60c2d0497cefe804d37953bbfaa597c3476d79`) prompted corrections to BINV-06 (period-close no longer a Consumption trigger, per B04 §4), BINV-10 (now explicitly states the Current Earnings transfer that makes MP-02's corrected proof hold post-closing), and a new BINV-11 (historical as-of reproducibility). See [CORR_B01_B02_B03_CORRECTIVE_ROUND.md](CORR_B01_B02_B03_CORRECTIVE_ROUND.md). |
| **Corrected (Round 2)** | **CORR-B2-01/02/03/04 (2026-08-29)** — ChatGPT's Round 2 re-audit (`04e44b06489d8bea6c8d39410050d68cf08bce21`) found BINV-11's Round-1 guarantee insufficient against backdated Corrections (`M-AUD-04`) and BINV-10's "Period close" scope overgeneralized Team A's year-end-specific evidence (`M-AUD-05`). BINV-10 and BINV-11 both substantially rewritten below; new BINV-12 added (Recorded At immutability — the mechanism BINV-11's Round-2 guarantee depends on). See [CORR_B2_CORRECTIVE_ROUND.md](CORR_B2_CORRECTIVE_ROUND.md). |
| **Corrected (Round 3)** | **CORR-B3-04/05 (2026-08-29)** — ChatGPT's Round 3 re-audit (`f6fb633fd141f45caf047bc94d75f84420e1cc6d`) found BINV-10's Round-2 text still described Fiscal Year Close as posting a Current-Earnings-transfer Entry (`M-AUD-07`), and found no invariant guaranteed IAS 8's mandatory exclusion of material prior-period errors from current-period profit or loss (`M-AUD-06`). BINV-10 rewritten again below (no-posted-close model); new BINV-13 added (material prior-period error P&L exclusion). See [CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md](CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md). |

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

### BINV-10 — Carry-Forward Correctness *(new, Team B addition; rewritten at CORR-B2-03/04)*

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
                           rewritten Round 2, rewritten again Round 3), BINV-11 (historical
                           reproducibility, rewritten Round 2), BINV-12 (recording-time
                           immutability, added Round 2), BINV-13 (material prior-period error
                           P&L exclusion, added Round 3)
```

**B5 = COMPLETE.** *(Corrected at CORR-B01/B02/B03/CORR-B2-01..04/CORR-B3-04/05 — see header.
Corrections are additive to this record, not a rewrite of it: BINV-01..05, 07..09 are unchanged
since the original B5 pass. BINV-06 was amended once (Round 1). BINV-11 was amended once
(Round 1), then substantially rewritten (Round 2). BINV-10 was amended once (Round 1),
substantially rewritten (Round 2), then rewritten a third time (Round 3, `M-AUD-07` —
no-posted-close model) — every prior version kept visible at each step. BINV-12 was new at
Round 2. BINV-13 is new this round (Round 3, `M-AUD-06` — material prior-period error P&L
exclusion, IAS 8 paras 41/42/46).)*
