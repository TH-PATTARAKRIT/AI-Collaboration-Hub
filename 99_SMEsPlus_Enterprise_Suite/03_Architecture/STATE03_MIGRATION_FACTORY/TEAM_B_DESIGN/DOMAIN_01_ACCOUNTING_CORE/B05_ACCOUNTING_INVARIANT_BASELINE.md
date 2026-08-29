# B05 — Accounting Invariant Baseline

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B5 — Business Invariant Baseline |
| Method | Starts from Team A's INV-01..06 (`04_BUSINESS_INVARIANT_REGISTER.md`), independently re-evaluated against this domain's own B02–B04 design, plus five independently justified additions |
| **Corrected** | **CORR-B01 / CORR-B02 / CORR-B03 (2026-08-29)** — ChatGPT Independent Design Audit (`aa60c2d0497cefe804d37953bbfaa597c3476d79`) prompted corrections to BINV-06 (period-close no longer a Consumption trigger, per B04 §4), BINV-10 (now explicitly states the Current Earnings transfer that makes MP-02's corrected proof hold post-closing), and a new BINV-11 (historical as-of reproducibility). See [CORR_B01_B02_B03_CORRECTIVE_ROUND.md](CORR_B01_B02_B03_CORRECTIVE_ROUND.md). |

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

### BINV-10 — Carry-Forward Correctness *(new, Team B addition; strengthened at CORR-B02)*

```
Independent statement: The opening balance of period N+1 for a carry-forward (Asset/
                        Liability/Equity) account equals the closing balance of period N for
                        that account, computed by CAP-09, never independently keyed.
                        **Strengthened at CORR-B02:** closing a period must additionally
                        transfer the closing Current Earnings (Revenue − Expenses for the
                        period, MP-02) into a designated formal Equity account, and reset every
                        Revenue/Expense account to zero for period N+1 — this is what makes
                        MP-02's simple equation (Assets = Liabilities + Equity) hold again
                        immediately after close, as a special case of the expanded equation
                        (Assets + Expenses = Liabilities + Equity + Revenue) with Expenses and
                        Revenue both reset to zero.
Why required:           A manually entered opening balance that does not tie to the prior
                        period's actual close is a silent break in the ledger's continuity —
                        the kind of gap that would be invisible until an audit specifically
                        checks the roll-forward. Separately, if Current Earnings were not
                        transferred into Equity at close, the closing balance sheet would not
                        balance under the simple equation at all — a defect distinct from, but
                        related to, the one ChatGPT's audit found in the open-period proof.
Accounting basis:       BF-09 (balance-sheet carry-forward / P&L reset), MP-02 (corrected)
Regulatory basis:       None specific — supports general statement reliability
Failure consequence:    Opening and closing balances diverge across a period boundary with no
                        forced mechanism to catch it — comparative statements silently
                        disagree with each other; or, if Current Earnings is not transferred,
                        a "closed" balance sheet still fails to balance under the simple
                        equation, contradicting the very point of closing.
Enforcement objective:  CAP-09's carry-forward output (B02 §2) is itself a CAP-02-committed
                        fact (B04 §3 `CarriedForward` event) — computed and posted through the
                        same gates as any other Entry, not a special manual step outside them.
                        The Current Earnings transfer is part of this same computed, posted
                        event, not a separate manual journal entry a user must remember.
Evidence:               AP-14 / BF-09, MP-02 (corrected at CORR-B02), independently elevated to
                        invariant status this phase
Residual assumption:    The year-end closing *process* that triggers this computation was
                        noted by Team A as unread/unobserved (MR-07 residual note) — this
                        invariant states the required outcome; it does not assume any
                        particular closing procedure achieves it.
```

### BINV-11 — Historical As-of Reproducibility *(new, added at CORR-B03)*

```
Independent statement: For any account, company, and historical date D, re-evaluating
                        MP-09's balance-as-of-D aggregation must produce an identical result
                        regardless of when the computation is performed, PROVIDED no
                        Correction or Void dated <= D has been committed since (a Correction
                        or Void is itself a new, separately-dated Entry, so in practice this
                        proviso is never violated — see below). **Precision added during
                        CORR-B05 regression testing:** this guarantee is UNCONDITIONAL only
                        for CONSUMED facts, because BR-07 makes Amendment impossible on a
                        consumed Entry — the only way to change its effective content is a
                        Correction/Void, which is separately dated and therefore cannot alter
                        an as-of-D result for D before that date. For an UNCONSUMED Entry, an
                        in-place Amendment performed after D but before the query genuinely
                        CAN change what "as of D" reports — this is intentional, not a defect:
                        "unconsumed" precisely means nothing has yet relied on the value, so
                        there is no historical truth to protect. BINV-11 is a guarantee about
                        RELIED-UPON history, not about every number that was ever transiently
                        visible before anyone depended on it.
Why required:           A financial report issued "as of D" is itself a historical fact; a
                        later discovery that something dated before D should be voided or
                        corrected does not change what was true and reported as of D — it
                        creates a new fact, dated at or after the discovery, that changes the
                        position from that point forward. Silently rewriting a historical as-of
                        result breaks exactly the audit/reproducibility property this domain
                        exists to protect.
Accounting basis:       Direct consequence of BINV-05 (traceable correction is additive,
                        dated) applied to aggregation, not merely to individual Entries
Regulatory basis:       Supports RG-01/RG-02 — an independently audited, retained financial
                        record must mean the same thing on re-examination as it did when issued
Failure consequence:    ChatGPT's independent audit (`D01-B-AUD-03`) found this concretely:
                        under the original design, an Entry valid and committed at D1, later
                        voided at D2, would be silently excluded from a "balance as of D1"
                        query performed after D2 — a later event retroactively rewriting an
                        earlier historical truth.
Enforcement objective:  MP-09 (B08, corrected) no longer filters by an Entry's *current*
                        status at all — every COMMITTED Entry's own Lines count at their own
                        date, unconditionally; a Void or Correction is itself a separately
                        dated Entry (B04 §5/§6) whose own Lines only affect aggregations dated
                        on or after *that* Entry's own date. Historical reproducibility is
                        therefore a structural consequence of date-based filtering, not a
                        separately maintained guarantee that could drift out of sync with it.
Evidence:               Derived design requirement, prompted by ChatGPT's independent audit
                        `D01-B-AUD-03`; no direct Team A source ID
Residual assumption:    None material — this invariant is a direct, provable consequence of
                        MP-09's corrected formula (B08), not an independent judgment call.
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
Independently added     : BINV-09 (classification integrity), BINV-10 (continuity integrity),
                           BINV-11 (historical reproducibility, added at CORR-B03)
```

**B5 = COMPLETE.** *(Corrected at CORR-B01/B02/B03 — see header. Corrections are additive
to this record, not a rewrite of it: BINV-01..05, 07..09 are unchanged from the original
B5 pass; BINV-06 and BINV-10 were amended in place with the amendment visible; BINV-11 is new.)*
