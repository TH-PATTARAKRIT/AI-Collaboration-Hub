> DOMAIN_01 — Accounting Core | Team A PART 2 (Sonnet) | Input: committed Part 1 evidence | No SMEsPlus design

# 04 — BUSINESS INVARIANT REGISTER

Every invariant below is proven, not assumed — each has a reference evidence anchor. Where
the reference system does **not** currently guarantee an invariant it should logically hold,
that is stated explicitly as the finding, not smoothed over.

## INV-01 — Balanced accounting entry
```
Statement:            Σdebit(entry) = Σcredit(entry) for every posted entry
Business purpose:     the fundamental integrity check of double-entry accounting
Accounting basis:     AP-01
Failure consequence:  trial balance and all derived reports become internally inconsistent
Reference evidence:   P1 account_move.py:2765 (asserted) / P2 pg_restore -l (not DB-enforced
                       at the aggregate level — 0 triggers, only row-level CHECKs)
Independent evidence: AP-01 (universal principle)
Classification:       A (principle) — but CURRENTLY UNGUARANTEED by this reference system
                       at the persistence layer (E — vendor implementation gap)
Confidence:            HIGH (mechanism); EVIDENCE_MISSING (data-level, GAP-D01-11)
Migration relevance:   MUST re-establish independently; do not trust source state alone
Audit relevance:       compensating control required; source provides none
```

## INV-02 — Valid accounting period
```
Statement:            a transaction dated within an already-reported/closed period must not
                       post without a discoverable, authorized override
Business purpose:     protects the integrity of previously reported financial statements
Accounting basis:     AP-06 (period cutoff control)
Failure consequence:  restated financials, loss of confidence in previously issued reports
Reference evidence:   P1 company.py:60-113, account_lock_exception.py, BYPASS_LOCK_CHECK
Independent evidence: AP-06 (NetSuite triangulation)
Classification:       A (principle, cross-ERP validated) / E (reference system's 6-control
                       fragmented shape, vendor-specific and more complex than peer)
Confidence:           HIGH (mechanism exists); MEDIUM (whether the 6 controls can disagree
                       in practice was not data-tested, no representative dataset)
Migration relevance:  must evaluate ALL SIX controls, not one, per historical transaction
Audit relevance:      higher audit burden than a single period-state model
```

## INV-03 — Valid company context (multi-company boundary)
```
Statement:            every journal, account and move belongs to exactly one company; a
                       transaction must not span or leak across company boundaries
Business purpose:     legal-entity separation of financial records
Accounting basis:     BUSINESS REQUIREMENT — legal entities must report separately
Failure consequence:  cross-entity contamination of financial statements; legal/statutory risk
Reference evidence:   P1 SE-15 (company_currency_id related from move); P2 company_id FKs on
                       account_move, account_journal, account_account
Independent evidence: not separately triangulated this round (multi-company is implicit in
                       AP-08's "financial statements per entity" framing, not directly cited)
Classification:       B (business/regulatory requirement, inferred from AP-08) — confidence
                       lowered because not independently triangulated as its own topic
Confidence:           MEDIUM
Migration relevance:  company scoping must be preserved as a hard boundary
Audit relevance:      standard requirement for any multi-entity accounting system
```

## INV-04 — Currency consistency
```
Statement:            (a) balance and amount_currency must agree in sign; (b) foreign-currency
                       transactions must be recognised at a valid spot rate and remeasured at
                       each reporting date per functional-currency rules
Business purpose:     (a) prevents nonsensical mixed-sign postings; (b) IAS 21 compliance
Accounting basis:     AP-07 (IAS 21)
Failure consequence:  (a) prevented at DB level — a real strength; (b) if remeasurement is
                       not performed, foreign-currency exposure misstates reported values
Reference evidence:   (a) P2 direct — check_amount_currency_balance_sign CHECK constraint,
                       DIRECTLY DB-ENFORCED; (b) P1 BR-06 (header-level rate validation only)
Independent evidence: AP-07
Classification:       (a) D — cross-ERP/DB-enforced pattern, VERIFIED FACT, genuine strength;
                       (b) G — UNKNOWN whether periodic remeasurement is implemented at all
Confidence:           HIGH (a) / UNKNOWN (b)
Migration relevance:  (a) preserve or better; (b) must independently confirm remeasurement
                       logic exists somewhere before assuming IAS 21 compliance
Audit relevance:      (b) is a material open question for any statutory audit
```

## INV-05 — Traceable correction
```
Statement:            a correction to a posted fact must be a new, linked record; the
                       original must remain intact and discoverable
Business purpose:     preserves the audit trail through the correction process
Accounting basis:     AP-05 (peer-validated pattern)
Failure consequence:  loss of ability to show what was originally recorded vs. later corrected
Reference evidence:   P1 account_move.py:5433 (_reverse_moves), reversed_entry_id linkage
Independent evidence: AP-05 (SAP B1)
Classification:       D (cross-ERP common pattern) — genuine reference-system strength
Confidence:           HIGH
Migration relevance:  the reversal LINK is business data to carry forward; the mechanism is not
Audit relevance:      positive; matches peer practice
```

## INV-06 — Historical auditability / immutability of committed fact
```
Statement:            once a fact has been committed to the ledger — and especially once
                       consumed downstream (reported externally, reconciled, filed) — its
                       content should not be silently mutable
Business purpose:     the audit trail is only as strong as its weakest mutability control
Accounting basis:     AP-13 (traceability); directly threatened by CF-06
Failure consequence:  silent restatement of history with no forced trace — THE central
                       control weakness identified in this domain
Reference evidence:   P1 account_move.py:6108-6109 (button_draft accepts posted/cancel) —
                       THIS INVARIANT IS **CURRENTLY VIOLATED BY REFERENCE-SYSTEM DESIGN**
Independent evidence: AP-05 / CF-06 triangulation — SAP B1 forbids exactly this
Classification:       A (principle, should hold) — E (reference system does not enforce it;
                       vendor-specific divergence from at least one major peer)
Confidence:           HIGH
Migration relevance:  cannot assume migrated "posted-once" history is what it appears to be
                       without also migrating and interrogating change-tracking data
Audit relevance:      THE single most important audit finding in this domain — see
                       12_REFERENCE_TO_ADVANCEMENT_REGISTER ADV-04
```
