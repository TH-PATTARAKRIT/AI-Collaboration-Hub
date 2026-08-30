# B08 — Accounting & Mathematical Design Principles

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B8 — Accounting & Mathematical Design Principles |
| Method | Extends Team A's MR-01..08 (evidence of what the reference system does or fails to guarantee) into this domain's own mathematical design commitments. No implementation — formulas are stated over the conceptual entities of B07, not over any storage structure. |
| **Corrected** | **CORR-B02 / CORR-B03 (2026-08-29)** — ChatGPT Independent Design Audit (`aa60c2d0497cefe804d37953bbfaa597c3476d79`) found MP-02's original proof mathematically incomplete for an open reporting period, and MP-09's original VOID handling time-inconsistent for historical as-of queries. Both are corrected below, in place, with the original reasoning kept visible rather than deleted. Full comparison of alternatives: [CORR_B01_B02_B03_CORRECTIVE_ROUND.md](CORR_B01_B02_B03_CORRECTIVE_ROUND.md). |
| **Corrected (Round 2)** | **CORR-B2-01/02/03/04/05 (2026-08-29)** — ChatGPT's Round 2 re-audit (`04e44b06489d8bea6c8d39410050d68cf08bce21`) found the Round-1 MP-09 fix still incomplete (a backdated Correction could rewrite history — `M-AUD-04`) and MP-02's "Current Earnings since the last close" wording repeated the exact period/fiscal-year ambiguity CAP-09 had (`M-AUD-05`). MP-09 rebuilt with a two-mode temporal model; MP-02 and a new MP-11 reconciled to Fiscal Year Close specifically. Full record: [CORR_B2_CORRECTIVE_ROUND.md](CORR_B2_CORRECTIVE_ROUND.md). |
| **Corrected (Round 3)** | **CORR-B3-05 (2026-08-29)** — ChatGPT's Round 3 re-audit (`f6fb633fd141f45caf047bc94d75f84420e1cc6d`, finding `M-AUD-07`) found MP-11 (Round 2, below) literally defined a posted Entry debiting Revenue and crediting Expense — directly contradicting this same document's and B07's repeated claim that Revenue/Expense are never reset by a posted action, and, traced through MP-09's aggregation, a genuine arithmetic bug (it would corrupt the closing year's own historical query). MP-11 rewritten below to the no-posted-close, derived-Reported-Retained-Earnings model (B07 §1e); MP-02's post-closing special case paragraph corrected to match. Full record: [CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md](CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md). |
| **Corrected (Round 4)** | **CORR-B4-01/02/03/05 (2026-08-30)** — ChatGPT's Round 4 re-audit (`9c0a3f2d179994a20f01db16d5713989a78c0b2a`) found MP-02's "Reported Equity" formula double-counted the designated Retained Earnings account's balance (`M-AUD-08`) and that Reported Retained Earnings depended on `FiscalYearClosed` declaration timing rather than the Fiscal Year's own calendar boundary (`M-AUD-09`). MP-02's post-boundary paragraph and MP-11 both corrected to cross-reference the fix; new MP-12 added, formally re-proving the Raw Ledger Identity → Reported Financial-Statement Identity transformation (Proofs A-G) that Round 3 had not actually re-derived after introducing mixed-horizon reporting. Full record: [CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md](CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md). |
| **Corrected (Round 5)** | **CORR-B5-01/02/03/04 (2026-08-30)** — ChatGPT's Round 5 re-audit (`de7492afd0af0f58185f3f36940a77f2389aa8b8`) found MP-09's category-bounded aggregation, silently reused by MP-12 Proof G as "the Raw Trial Balance," does NOT actually balance once a Fiscal Year has elapsed (`M-AUD-11`, CRITICAL — a genuine arithmetic contradiction, not a labeling nuance, verified against Team B's own B21 Test 5 numbers). MP-09 renamed and split into `CumulativeAccountBalance` (the true single-horizon raw formula) and `FiscalYearActivity` (the Revenue/Expense-only, Fiscal-Year-bounded formula, never itself called a Trial Balance); MP-12 Proof G rebuilt into G1 (Raw Cumulative Trial Balance)/G2 (Current-FY Reporting Balance, not balanced)/G3 (Balanced Presentation Trial Balance, with an explicit never-posted derived bridge line)/G4 (Known vs. Current). Full record: [CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md](CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md). |

### MP-01 — Double-Entry Balance

```
Principle:    Σ debit(l) = Σ credit(l), for all Lines l belonging to one Entry
Inputs:       the set of Lines belonging to one Entry
Outputs:      boolean — balanced / not balanced
Invariant:    BINV-01 — must hold for an Entry to become COMMITTED
Boundary:     evaluated per Entry, in the Entry's functional-currency amounts; presentation-
              only Lines (B07 Line/Account relationship) carry no financial content and are
              excluded from the sum
Rounding:     the sum is evaluated on already-rounded Line amounts (MP-04) — balance is
              checked on what will actually be stored, not on higher-precision intermediate
              values that are never themselves committed
Exception:    none — this check has no bypass in this design (B04 §7)
Proof requirement: a Posting attempt (CAP-02) must be able to demonstrate, for any Entry it
              accepts, that this sum was evaluated and passed at the moment of commitment —
              not merely that it was true when the Entry was first drafted
```

### MP-02 — Accounting Equation (Corrected at CORR-B02)

```
ORIGINAL CLAIM (kept visible, not deleted): "If every Entry satisfies MP-01 and every
Account Category has the correct normal balance side, then Assets = Liabilities + Equity
holds across the whole Ledger as a mathematical corollary — during an open period, with no
further condition." ChatGPT's independent audit (`D01-B-AUD-02`) correctly found this
INCOMPLETE: it silently assumed Revenue and Expense accounts are empty or already closed,
which is not true during an open reporting period. The corrected proof below does not
require that assumption.

Principle (corrected — expanded form, holds unconditionally):
              Assets + Expenses = Liabilities + Equity + Revenue
              — true at every point in time, open period or closed, with no additional
              assumption beyond MP-01 and Normal Balance Side (B07 §1a).

Proof:        Sum MP-01 (Σdebit = Σcredit per Entry) over every COMMITTED Entry for the
              Company: total debit postings, all accounts = total credit postings, all
              accounts (grand totals; a direct sum of a per-entry identity that holds for
              every entry is itself an identity — no new assumption introduced).
              Partition all accounts into two groups by Normal Balance Side (B07 §1a):
              DEBIT-NORMAL = Asset ∪ Expense; CREDIT-NORMAL = Liability ∪ Equity ∪ Revenue.
              Let D_dn, C_dn = total debit/credit postings to the debit-normal group;
              D_cn, C_cn = total debit/credit postings to the credit-normal group.
              Grand-total identity: D_dn + D_cn = C_dn + C_cn.
              Rearrange:            D_dn − C_dn = C_cn − D_cn.
              By definition, balance(debit-normal account) = debit − credit, so the left
              side is exactly Σ(Asset balances) + Σ(Expense balances) = Assets + Expenses.
              By definition, balance(credit-normal account) = credit − debit, so the right
              side is exactly Σ(Liability) + Σ(Equity) + Σ(Revenue) balances.
              Therefore: Assets + Expenses = Liabilities + Equity + Revenue. QED — no
              assumption about period state was used anywhere in this derivation.

Current Earnings (B07 §1b): define Current Earnings = Revenue − Expenses, **both measured
              since the start of the current Fiscal Year — corrected at CORR-B2-03/04**
              (round 1's "since the last close" wording was exactly the period/fiscal-year
              ambiguity ChatGPT's Round 2 audit flagged, `M-AUD-05`; an ordinary Period close
              is a posting lock only, B07 §1d, and does not bound this sum). Regrouping the
              proven expanded equation:
              Assets = Liabilities + (Equity + Current Earnings)
              — i.e., for REPORTING purposes, "Equity + not-yet-closed Current Earnings"
              plays the role the simple equation expects "Equity" to play. This is an
              algebraic regrouping of the proven identity, not a new assumption.

Post-Fiscal-Year-boundary special case: **corrected at CORR-B2-03/04 — this is Fiscal Year
              boundary, not ordinary Period close.** ~~At Fiscal Year Close, CAP-09/BINV-10
              (redefined, B07 §1d) transfers Current Earnings into a formal Equity account via
              exactly one new committed Entry.~~ **Corrected again at CORR-B3-05 (kept struck
              through, not deleted): this is exactly the defect `M-AUD-07` found — no Entry is
              ever posted at Fiscal Year Close.** Revenue/Expense are not "reset" by any posted
              action — their zero-point for the new Fiscal Year follows automatically from the
              Fiscal-Year-bounded aggregation (MP-09, corrected), unchanged from the Round-2
              reasoning. What changes at CORR-B3-05 is what happens to the *elapsed* Fiscal
              Year's Current Earnings: it becomes part of Reported Retained Earnings, a
              **derived reporting figure** (B07 §1e, new formula), not a posted Equity-account
              balance. An ordinary Period close (month/quarter) does none of this — it only
              locks posting/amendment (B07 §1d) — so the expanded equation's Revenue/Expense
              terms continue accumulating uninterrupted across ordinary Period boundaries
              within the same Fiscal Year, which is what makes YTD reporting correct (verified
              numerically, [B19](B19_CORR_B2_FOCUSED_RED_TEAM_REGRESSION.md) Test 8).
              ~~Immediately after Fiscal Year Close, Revenue = Expenses = 0 for the new Fiscal
              Year (again, automatic from MP-09's category bound — no entry required).
              Substituting Revenue = Expenses = 0 into the expanded equation collapses it
              exactly to the simple form: Assets = Liabilities + Equity — using the
              NOW-UPDATED **Reported** Equity figure, i.e. Equity(ledger, all-time) + Reported
              Retained Earnings(B07 §1e), not a single all-in-one ledger Equity balance.~~
              **Corrected at CORR-B4-01/02/03 (kept struck through, not deleted — this is
              exactly the defect `M-AUD-08`/`M-AUD-09` found):** two errors in the passage
              above. First, "Equity(ledger, all-time) + Reported Retained Earnings" **double-
              counts** the designated Retained Earnings account's own balance, since that
              account is itself inside `Equity(ledger, all-time)` — corrected to the
              non-overlapping decomposition B07 §1f defines (`Other Ledger Equity` +
              `Reported Retained Earnings`, no account in both). Second, "immediately after
              Fiscal Year Close" tied the transition to the operator's *declaration*, not the
              Fiscal Year's own calendar boundary — corrected to trigger on the Fiscal Year
              having **elapsed** (B07 §1e), so the transition happens on time even if the
              `FiscalYearClosed` declaration is delayed. **Corrected form:** the moment a
              Fiscal Year Y elapses (its End Date passes), and for any later Fiscal Year Y'
              in progress where Y' has zero Revenue/Expense so far, the expanded equation
              collapses to the simple form using the corrected Reported Equity figure —
              `Assets = Liabilities + Reported Equity`, where `Reported Equity = Other Ledger
              Equity(B07 §1f) + Reported Retained Earnings(B07 §1e, corrected)`. Full
              re-derivation from the raw ledger identity, including the Fiscal-Year-boundary
              invariant and both reporting viewpoints: [MP-12](#mp-12--reported-equity-
              reconciliation-new-added-at-corr-b4-01020305), new this round.

Inputs:       every COMMITTED Line for the Company, each Line's Account Category and Normal
              Balance Side (B07 §1a)
Outputs:      the expanded equation always; the simple equation exactly when Revenue =
              Expenses = 0 for the Fiscal Year in progress (i.e., once the prior Fiscal Year
              has elapsed and before the new one records any activity)
Invariant:    the expanded form is now stated as the actual invariant this domain relies on;
              the simple form is a derived special case, never assumed to hold mid-period
Boundary:     **Still not a fourth check alongside MP-01.** The expanded equation is a proven
              corollary of MP-01 + Normal Balance Side, exactly as the (incomplete) original
              claimed for the simple form — the correction is to *which* equation is claimed
              unconditionally, not to the "no separate check needed" design principle itself,
              which remains correct and is now on solid mathematical ground.
Rounding:     inherits MP-04; since it is a sum of already-balanced, already-rounded Entries,
              no new rounding is introduced at the aggregate level
Exception:    none
Proof requirement: this domain's design obligation is to keep MP-01, the Category-to-normal-
              balance mapping (CAP-01), and the elapsed-Fiscal-Year Reported Retained Earnings
              step (BINV-10, corrected) correct — the expanded equation's truth is evidence
              both hold; the simple equation's truth, specifically, is additionally evidence
              that the boundary-driven transition computed correctly for the Fiscal Year in
              question. **This principle no longer names "closing was performed correctly" as
              the thing the simple equation's truth is evidence of — corrected at CORR-B4-03,
              since the transition no longer depends on a closing action having occurred at
              all.**
```

### MP-03 — Monetary Precision

```
Principle:    a stored monetary amount has no binary floating-point representation error
Inputs/Outputs: any monetary value, at any point from recognition through reporting
Invariant:    BR-10, BF-02
Boundary:     applies to every monetary value this domain produces or stores; does not by
              itself specify how many decimal places are meaningful for a given currency —
              that is MP-04's concern
Rounding:     not addressed by this principle alone (see MP-04)
Exception:    none
Proof requirement: an exact-decimal (arbitrary-precision) representation is a design floor,
              not an aspiration — already correctly identified as achievable by Team A (CF-05)
              and inherited here as a non-negotiable baseline, correctly scoped as a
              computing-correctness norm rather than overclaimed as a cited accounting
              standard (disagreement-02)
```

### MP-04 — Rounding Policy *(Team B design decision — Team A left this open, OQ-03/MR-06)*

```
Principle:    every currency has a defined minor-unit precision (e.g., 2 decimal places for
              THB and USD), sourced from an authoritative currency reference, not invented
              per transaction; every Line amount is rounded to its currency's minor-unit
              precision using one consistently-applied method
Inputs:       a computed amount at higher-than-storage precision (e.g., the result of a
              tax or allocation calculation); the currency's defined minor-unit precision
Outputs:      a Line amount at exactly that precision
Invariant:    supports MP-01 — rounding must never be what silently breaks a balance check
Boundary:     applies at the point an amount becomes a Line — intermediate calculation may
              use higher precision, but nothing is committed at higher precision than the
              currency defines
Rounding method: **round-half-up (arithmetic rounding) is proposed as the default**, in
              preference to round-half-to-even (banker's rounding), on the grounds that it is
              the convention most familiar for manual verification of financial documents and
              is the safer default absent a confirmed statutory requirement either way. This
              is an explicit Team B design assumption, not a fact Team A's evidence
              established — OQ-03 remains genuinely open regarding any Thai-specific mandated
              method, and this default must be confirmed, not silently treated as settled, at
              the design gate (see B13, B16).
Exception:    **when a computation (e.g., splitting one total across several Lines, or a
              multi-line tax allocation) produces a rounding difference that would break
              MP-01 at the target precision, the difference must appear as its own visible
              Line (or be absorbed into one designated Line by an explicit, documented rule)
              — never silently redistributed across other Lines in a way that hides that
              rounding occurred.** This is the specific mathematical response to the
              reference system's unaddressed rounding gap (MR-06): rounding differences are
              made visible by design, not merely "handled."
Proof requirement: for any Entry produced by a computation involving splits or allocations,
              the sum of rounded Line amounts must equal the rounded total independent of
              order of operations — this is a property the computation method must guarantee,
              not something checked after the fact only by luck
```

### MP-05 — Currency Recognition & Conversion

```
Principle:    a transaction-currency amount is converted to the functional-currency amount
              using the Exchange Rate (B07) valid on the Entry's date
Inputs:       transaction amount, transaction currency, functional currency, Entry date
Outputs:      functional-currency amount (subject to MP-04)
Invariant:    BINV-04a (sign consistency between the two amounts)
Boundary:     recognition happens exactly once, at Entry date — this principle does not cover
              what happens afterward (that is MP-06)
Rounding:     MP-04 applies to the converted result
Exception:    none — every foreign-currency Line requires a valid rate; there is no
              "recognise now, find a rate later" path in this design
Proof requirement: the specific Exchange Rate used for a given conversion must be
              individually traceable (which rate, as of which date, from which source) — not
              merely that "a rate was applied"
```

### MP-06 — Functional Currency & Remeasurement

```
Principle:    a Company's functional currency is the currency its Ledger's authoritative
              balances are stated in; monetary balances arising from foreign-currency
              recognition (MP-05) are remeasured to functional currency at each reporting date
Inputs:       the Company's functional currency; a monetary balance previously recognised in
              a foreign currency; a new Exchange Rate as of the reporting date
Outputs:      a Remeasured Entry (B04 §3) capturing the exchange difference
Invariant:    BINV-04b, RG-05 (IAS 21)
Boundary:     this principle governs monetary balances only (cash, receivables, payables) —
              non-monetary items (e.g., anything carried at historical cost) are outside this
              principle's scope; that boundary is stated here explicitly because Team A's
              evidence never analysed it (new scope note, not present in the source pack)
Rounding:     MP-04 applies to the resulting exchange-difference amount
Exception:    none — this design commits to remeasurement as a designed, non-optional
              capability (CAP-06) specifically because Team A found its presence in the
              reference system genuinely unknown (ADV-08) rather than assuming it exists
              elsewhere in a full system
Proof requirement: a full audit of a Company's foreign-currency exposure must be able to
              reconstruct every recognition and every remeasurement as individually committed,
              linked facts — not as a single opaque "revaluation" number with no lineage
```

### MP-07 — Reversal Arithmetic

```
Principle:    a reversal's Lines are the exact negation of the original Entry's Lines — same
              Accounts, same amounts, debit and credit swapped
Inputs:       the original Entry's Lines
Outputs:      a new Entry's Lines, each (account_i, credit_i, debit_i) where the original was
              (account_i, debit_i, credit_i)
Invariant:    BINV-05 (traceable correction), a specialization of BR-06
Boundary:     applies only to a full reversal (see MP-08 for the more general correction case)
Rounding:     none introduced — a reversal reuses the original's already-rounded amounts
              exactly, it does not recompute them
Exception:    none
Proof requirement: **a reversal constructed this way is provably balanced without a separate
              check** — since the original satisfied Σdebit_i = Σcredit_i (MP-01), the
              reversal's Σcredit_i = Σdebit_i is the same equation restated, and therefore
              holds automatically. This is stated as a proof, not merely asserted: it is the
              mathematical reason a full reversal can never be the source of a balance defect,
              which is exactly why cross-ERP practice (SAP B1 triangulation) treats it as the
              safe correction path.
```

### MP-08 — Correction Arithmetic (General Case)

```
Principle:    a correction Entry's Lines express whatever adjustment is needed to represent
              the intended change, and must independently satisfy MP-01 on their own — a
              correction never "borrows" balance from the Entry it links to
Inputs:       the original Entry (for linkage only, per B07 Correction Link), the intended
              corrected position
Outputs:      a new Entry, independently balanced, linked to the original
Invariant:    BINV-05, BR-06
Boundary:     this design does not mandate one mechanical shape for every correction — a full
              reversal-and-repost (two Entries: MP-07's reversal, plus a fresh correct Entry)
              and a single delta Entry (capturing only the difference between wrong and right)
              are both valid instances of this principle. The choice between them is a
              usability question for a later, non-domain-design phase (how a user expresses a
              correction), not a mathematical one — either shape satisfies BINV-05 identically.
              **Void (B04 §5, corrected at CORR-B03) is the specific instance of this pattern
              where the correction is a pure MP-07 reversal with no accompanying replacement
              value** — not a fourth arithmetic shape, just the "zero net effect" special case
              of what this principle already covers.
Rounding:     MP-04 applies to any newly computed amount (e.g., a delta)
Exception:    none
Proof requirement: regardless of shape, the correction Entry must pass MP-01 exactly as any
              other Entry would — this is what distinguishes a correction from a privileged,
              unchecked operation
```

### MP-09 — Cumulative Account Balance & Fiscal-Year Activity *(renamed from "Aggregation (Account Balance / Trial Balance)" at CORR-B5-02 — "Trial Balance" removed from this principle's own name; corrected at CORR-B03)*

```
ORIGINAL FORMULA (kept visible, not deleted): "...EXCLUDING Lines belonging to a VOIDED
Entry..." — filtered by the Entry's CURRENT status. ChatGPT's independent audit
(`D01-B-AUD-03`) correctly found this time-inconsistent. **CORR-B03's fix (also kept
visible, not deleted):** removed the status-based exclusion, filtering only by Effective
Date <= D. **That fix was still incomplete**, per ChatGPT's Round 2 audit (`M-AUD-04`):
Effective Date alone does not prevent a Correction from being *backdated* — committed today,
but claiming an Effective Date in an already-relied-upon historical period (e.g., because
that period was reopened). A single-date formula cannot distinguish "this was always going
to affect D1" from "this was made to affect D1 after the fact." Corrected again below —
this time by introducing the second temporal axis (B07 §1c) the single-date formula was
missing, and by making the aggregation category-aware (B07 §1d) to close `M-AUD-05` in the
same pass.

**Two aggregation MODES are now defined, not one — this is the structural fix, not a patch:**

Principle (corrected, Round 2):
  MODE 1 — AS ORIGINALLY KNOWN, as-of business date D, as of recording-time T:
    balance_known(A, C, D, T) = Σ (signed amount of every Line referencing A) over every
    COMMITTED Entry belonging to C where Effective Date <= D AND Recorded At <= T
  MODE 2 — CURRENT / RESTATED, as-of business date D (T implicitly "now"):
    balance_current(A, C, D) = Σ (signed amount of every Line referencing A) over every
    COMMITTED Entry belonging to C where Effective Date <= D
    (equivalently, balance_current(A,C,D) = balance_known(A,C,D,now) )
  ~~BOTH modes are additionally CATEGORY-BOUNDED (B07 §1d):
    Asset/Liability/Equity (Balance Sheet): no lower Effective-Date bound (all-time)
    Revenue/Expense (Income Statement): lower-bounded by the start of the Fiscal Year
    containing D~~

**CORRECTED AT CORR-B5-01/02 (kept struck through above, not deleted — this is exactly what
ChatGPT's Round 5 audit, `M-AUD-11`, found wrong):** baking category-bounding directly into
`balance_known`/`balance_current` silently made this principle's own base formula a
MIXED-HORIZON quantity (all-time for Balance Sheet categories, Fiscal-Year-bounded for Income
Statement categories) — and MP-12 Proof G (Round 4) then incorrectly treated that mixed-horizon
output as if it were, by itself, a balanced Raw Trial Balance. It is not: at any query date
after a Fiscal Year has elapsed, summing debit-normal mixed-horizon balances against
credit-normal mixed-horizon balances does NOT reproduce MP-01's per-Entry identity, because
Revenue/Expense Lines dated in an elapsed Fiscal Year are excluded from one side of the sum
while the Asset/Liability/Equity Lines they originally balanced against remain included on the
other (worked failure case, Company X, D = Jan 5 2025: mixed-horizon Debit = Assets 1250,
mixed-horizon Credit = direct Equity 1000 — off by exactly 250, the prior elapsed Fiscal Year's
Current Earnings — see [B22](B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md)
Test 3 for the full worked reproduction).

**`balance_known`/`balance_current` are corrected to be the pure CUMULATIVE aggregation —
ONE common Effective-Date lower bound for every Account Category alike, with NO
category-specific exception — and are renamed accordingly (same formula shape, same Mode
1/Mode 2 viewpoint mechanism, unchanged; only the erroneous category-bounding clause is
removed):**

  CumulativeAccountBalance_Known(A, C, D, T)  ≡  balance_known(A, C, D, T), corrected:
    = Σ (signed amount of every Line referencing A) over every COMMITTED Entry belonging to C
      where Effective Date <= D AND Recorded At <= T
      — measured from ledger inception through D, for EVERY Account Category alike (Asset,
      Liability, Equity, Revenue, Expense) — no category-specific lower bound, ever
  CumulativeAccountBalance_Current(A, C, D)  ≡  balance_current(A, C, D), corrected:
    = Σ (signed amount of every Line referencing A) over every COMMITTED Entry belonging to C
      where Effective Date <= D
      (equivalently, CumulativeAccountBalance_Current(A,C,D) =
       CumulativeAccountBalance_Known(A,C,D,now))

**A separate, new, narrower pair of formulas captures Fiscal-Year-bounded activity — meaningful
for Revenue/Expense specifically, and NEVER itself claimed to be a balanced Trial Balance:**

  FiscalYearActivity_Known(A, C, D, T)   [A a Revenue or Expense account]
    = Σ (signed amount of every Line referencing A) over every COMMITTED Entry belonging to C
      where FiscalYearStart(C, D) <= Effective Date <= D AND Recorded At <= T
  FiscalYearActivity_Current(A, C, D)    [A a Revenue or Expense account]
    = Σ (signed amount of every Line referencing A) over every COMMITTED Entry belonging to C
      where FiscalYearStart(C, D) <= Effective Date <= D
    (equivalently, FiscalYearActivity_Current(A,C,D) = FiscalYearActivity_Known(A,C,D,now))

  where FiscalYearStart(C, D) is the Start Date of the Fiscal Year that contains D for Company
  C (B07 §1, corrected at CORR-B5-05 to be a versioned, historically-safe fact — see §1h).

B07 §1b's Current Earnings is FiscalYearActivity_Current(Revenue,C,D) minus
FiscalYearActivity_Current(Expense,C,D) — a direct renaming/clarification of what this
principle already computed for that concept, not a new calculation. B07 §1e's Reported
Retained Earnings formula is corrected to cite `FiscalYearActivity` explicitly (not bare
"Mode 2") for exactly this reason.

Why this closes M-AUD-04 (unchanged from Round 2): Recorded At (B07 §1c) is system-generated at
              the instant of commitment and can never be set to a value earlier than the actual
              moment of commitment. Therefore, for any fixed T, no Entry committed after T can
              EVER satisfy "Recorded At <= T" — not now, not ever in the future — regardless of
              what Effective Date it claims. `CumulativeAccountBalance_Known(A, C, D, T)` (and,
              by the identical mechanism, `FiscalYearActivity_Known`), once T has passed, is a
              PROVABLY fixed point: nothing that happens after T can change it. This is what
              BINV-11 (corrected below) now guarantees, and the guarantee is structural (a
              property of the formula's shape), not procedural.
Why this closes M-AUD-05 (unchanged from Round 2, now correctly scoped): `FiscalYearActivity`
              being lower-bounded by the current Fiscal Year, while `CumulativeAccountBalance`
              remains unbounded for every category including Revenue/Expense, is what B07
              §1d's Continuous Ledger model requires — see B07 §1d for why this eliminates the
              double-counting risk entirely. Verified numerically:
              [B19](B19_CORR_B2_FOCUSED_RED_TEAM_REGRESSION.md) Tests 1, 8, 9 and
              [B22](B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md) Tests 1-3.
`_Current` is what an ordinary "what is the balance/activity today" or "as of a past date,
              using everything we know now" query returns — it is intentionally allowed to
              reflect a later, legitimate Restatement (B04 §3a/§3c). The two viewpoints are
              NEVER interchangeable, and a consumer of either must know which one it is looking
              at (CO-14, extended). **Neither `CumulativeAccountBalance` alone, summed across
              every Account, NOR `FiscalYearActivity` mixed into a per-Account "reporting
              balance" (Balance Sheet cumulative + Income Statement Fiscal-Year-bounded) is,
              by that fact alone, a "Trial Balance" — see MP-12 Proof G1/G2/G3 (corrected) for
              the three precisely-named, precisely-scoped outputs this domain actually
              produces, and which one (if any) is a genuinely balanced object.**
Inputs:       every COMMITTED Line for the Company, each with Effective Date and Recorded At
              (B07 §1c); the query's (D) and, for the Known viewpoint, (T); for
              `FiscalYearActivity`, additionally the Fiscal Year definition governing D
              (B07 §1h, corrected — a versioned, historically-safe fact, not a bare date pair)
Outputs:      a single signed amount per Account, per formula (`CumulativeAccountBalance` or
              `FiscalYearActivity`), per viewpoint (Known or Current). **Corrected at
              CORR-B5-02: this principle's output is never itself labeled "a Trial Balance" —
              that label, and the precise conditions under which a balanced object exists, are
              defined exclusively in MP-12 (corrected).**
Invariant:    BINV-11 (corrected, Round 2) for the Known viewpoint of both formulas; BINV-10
              (corrected) for the Continuous Ledger model `FiscalYearActivity`'s bounding
              depends on; the new BINV-15 (B05, CORR-B5-05) for the Fiscal Year definition's
              own historical safety, which `FiscalYearActivity` and the Elapsed test (B07 §1e)
              both now depend on
Boundary:     "as-of business date D" — allows both a current and a reconstructed historical
              balance/activity figure; "as-of recording-time T" (Known viewpoint only) — allows
              reconstructing what a report generated at any past moment actually showed
Rounding:     the sum of already-rounded Line amounts; no re-rounding of the aggregate itself
              (MP-03's precision floor)
Exception:    none for the Known viewpoint (structurally guaranteed, see above). The Current
              viewpoint has no exception either — it is DEFINED to reflect all currently-known
              facts, so there is nothing for an exception to carve out
Proof requirement: for any fixed (A, C, D, T), `CumulativeAccountBalance_Known(A, C, D, T)` (and
              `FiscalYearActivity_Known`) must return the identical value no matter when it is
              computed, with NO proviso — unconditional, per BINV-11/12's structural guarantee,
              exactly as established at CORR-B2-01/02 and unaffected by this round's renaming.
```

### MP-10 — Period Cutoff Stability — Corrected at CORR-B01

```
Principle:    once a Period closes (CAP-04), no new Posting or Amendment can occur within it
              (BR-05, BR-14 corrected) while it remains closed — this is a **lock** property,
              distinct from BINV-11's **historical reproducibility** property (MP-09), which
              holds regardless of Period status entirely.
Inputs:       a Period's open/closed status; MP-09's aggregation
Outputs:      no new activity enters a closed Period while it stays closed
Invariant:    BINV-02 (period lock) — **corrected: no longer BINV-02 + BINV-06 combined.**
              The original version of this principle treated period closure as a Consumption
              trigger, conflating a timing/lock property with a permanence/immutability
              property. ChatGPT's independent audit (`D01-B-AUD-01`) found this produced a
              direct contradiction against BINV-07's "never retracted" guarantee once reopen
              was also described as restoring correctability. The two properties are now
              cleanly separated (B04 §4): **Period Lock** (this principle) governs *whether
              new activity can enter*, and is reversible by an authorized reopen (CO-08).
              **Consumption** (BINV-06/07, unaffected by Period status) governs *whether an
              already-committed fact can ever be mutated*, and is never reversible. Historical
              reproducibility (BINV-11, MP-09) holds unconditionally, independent of both.
Boundary:     an authorized, recorded period reopen (CO-08) restores Posting/Amendment
              eligibility for that Period going forward — and, because Consumption was never
              entangled with Period status, reopen restores Amendment specifically only for
              entries that are independently still unconsumed (B04 §4's corrected gate rule).
              A reopen never resurrects an already-consumed entry's amendability, and never
              changes any historical as-of result (BINV-11) for dates before the reopen.
Rounding:     none beyond MP-04/MP-09
Exception:    an authorized reopen, per CO-08 — never a silent one; its effect is now
              precisely scoped (previous paragraph), not "everything in the period becomes
              correctable again"
Proof requirement: this domain's design obligation is that Period Lock and Consumption remain
              two independently checkable conditions on Amendment (B04 §4's gate rule) — never
              re-merged into one mechanism, which is exactly the conflation that produced the
              original contradiction
```

**Distinguished from MP-11 (new, below):** MP-10 governs ordinary Period locking only. It has
no bearing on Revenue/Expense's zero-point or Current Earnings' becoming reportable — that is
exclusively MP-11's concern, per CORR-B2-03/04 *(and, per CORR-B3-05, MP-11's concern is now a
declaration + derived-formula computation, not a posting — the boundary between MP-10 and
MP-11 is unaffected by that change)*. Conflating the two was the exact shape of `M-AUD-05`.

### MP-11 — Fiscal Year Close Arithmetic *(new, added at CORR-B2-03/04; rewritten at CORR-B3-05)*

```
ROUND 2 STATEMENT (kept visible, not deleted — this is exactly what ChatGPT's Round 3 audit,
`M-AUD-07`, found wrong):

Principle:    Fiscal Year Close commits exactly one new Entry per Company: Lines that debit
              Revenue accounts (zeroing their Fiscal-Year-bounded contribution going forward,
              per MP-09's category bound — no other Revenue/Expense Line is touched) and
              credit Expense accounts, with the net difference (Current Earnings) posted to
              a designated formal Equity account (Retained Earnings or equivalent) — or the
              reverse direction if Current Earnings is negative (a loss)
Inputs:       Current Earnings for the closing Fiscal Year (MP-02's derived value, computed
              from MP-09 Mode 2 over the Fiscal Year's own bound)
Outputs:      one new, ordinary, independently-balanced Entry (MP-01 applies to it exactly
              like any other), dated at the Fiscal Year's end
Invariant:    BINV-10 (corrected) — this is the ONE genuine new committed fact Fiscal Year
              Close produces; everything else (Revenue/Expense's zero-point for the new
              Fiscal Year, Asset/Liability/Equity's carry-forward) is implicit in MP-09's
              category-bounded aggregation and requires no additional posted fact (B07 §1d)
Boundary:     this Entry's Lines only ever touch Revenue, Expense, and one designated Equity
              account — never Asset or Liability accounts, which need no closing action at
              all under the Continuous Ledger model

WHY THIS WAS WRONG (`M-AUD-07`, verified by tracing the literal wording, not just by the
audit's say-so): two independent defects, not one.
  (1) Internal contradiction — this same document's own MP-02 post-closing paragraph, and
      B07 §1d, both state "Revenue/Expense are never reset by any posted action." A Line that
      debits every Revenue account and credits every Expense account IS a posted reset of
      those exact accounts. The two claims cannot both be true; this MP-11 text was the one
      that had to give, since the "never reset" claim is required elsewhere (MP-09's category-
      bounded aggregation is what actually zeroes the new year — a posted zeroing Entry is
      redundant with it at best, and double-zeroes at worst).
  (2) Real arithmetic bug, not just inconsistency — MP-09 sums Revenue/Expense by Effective
      Date within the current Fiscal Year (Mode 1 and Mode 2 alike). An Entry dated at the
      closing Fiscal Year's own end, with Lines touching Revenue and Expense, has an Effective
      Date INSIDE that same Fiscal Year. MP-09, evaluated for any as-of date D within the
      closing year up to and including the close date, would include this Entry's Revenue/
      Expense Lines in that year's OWN Current Earnings computation — corrupting the very
      figure the Entry was trying to record. (Dating it one day into the NEW Fiscal Year
      avoids that specific corruption but reintroduces defect (1) by posting into the new
      year's own Revenue/Expense, and still contradicts "never reset by any posted action."
      There is no dating choice that rescues the posted-Entry model — this is what makes it a
      genuine bug, not a wording problem.)

CORRECTED STATEMENT (CORR-B3-05, supersedes the Round-2 statement above):

Principle:    Fiscal Year Close commits **no Entry**. It performs exactly one thing: an
              authorized declaration (the `FiscalYearClosed` Audit Event, B04, corrected)
              that (a) locks the Fiscal Year to further ordinary posting [subsuming CAP-04's
              Period Lock for every Period within it] and (b) marks that Fiscal Year's Current
              Earnings as **closed** — eligible for inclusion in Reported Retained Earnings.
              ~~"Fiscal Year Close Arithmetic" is now the arithmetic of a REPORTING FORMULA
              (B07 §1e), not of a posted Entry:
                Reported Retained Earnings(Company C, as of date D) =
                    balance_current(the formally-designated Retained Earnings account, C, D)
                      (direct postings only — e.g. dividend declarations; MP-09 Mode 2,
                      all-time, exactly like any other Equity account)
                  + Σ over every Fiscal Year Y that closed before D of:
                      CurrentEarnings(C, Y) computed via MP-09 Mode 2, Fiscal-Year-bounded,
                      for Y~~
Inputs:       ~~the set of Fiscal Years closed before date D~~ (a fact recorded by
              `FiscalYearClosed` events, not by any Entry); MP-09 Mode 2 aggregation for each
Outputs:      no Entry. One `FiscalYearClosed` Audit Event per Fiscal Year closed (CAP-08),
              consumed by the Reported Retained Earnings formula above wherever Equity is
              reported.
Invariant:    BINV-10 (corrected again, Round 3) and the new BINV-13 (B05) — the formula above
              IS the enforcement mechanism; there is no posted fact for either invariant to
              protect, so no posted fact can violate them
Boundary:     the formula's summation term only ever reads Revenue/Expense Lines already
              governed by MP-09's existing category bound — it introduces no new Line, no new
              Entry, and touches no Asset or Liability account, exactly preserving the Round-2
              boundary's intent (Balance Sheet categories need no closing action) while
              removing the one posted fact that violated it
Rounding:     MP-04 applies to each Fiscal Year's computed Current Earnings term exactly as to
              any other computed value; the formula is a sum of already-rounded terms, so no
              new rounding is introduced by the summation itself
Exception:    none — declaring a Fiscal Year closed is itself gated by an authorized action
              (extends CO-08's tiering, at least as strict as ordinary Period reopen, since its
              blast radius — an entire Fiscal Year — is larger); this is unchanged from Round 2,
              only the thing being gated (a declaration, not a posting) has changed

**CORRECTED AGAIN AT CORR-B4-01/02/03 (kept struck through above, not deleted — this is
exactly what ChatGPT's Round 4 audit, `M-AUD-08`/`M-AUD-09`, found wrong):** two further
defects in the Round-3 statement's formula, both in B07 §1e (which this principle only
restated, so the fix is defined there and cross-referenced here, not duplicated):
  (1) `M-AUD-08` — the formula's own reference to "Retained Earnings account, C, D ... exactly
      like any other Equity account" invited exactly the double-count `M-AUD-08` found in
      B08 MP-02's companion "Reported Equity" formula: the designated Retained Earnings
      account is inside the Equity category, so summing it here AND inside a separate
      "Equity(ledger, all-time)" term (as MP-02's post-boundary paragraph did) counts it
      twice. Corrected: B07 §1f now defines "Other Ledger Equity" to explicitly exclude the
      designated Retained Earnings account, so Reported Equity's two terms never overlap.
  (2) `M-AUD-09` — "Fiscal Year Y that **closed** before D" made Reported Retained Earnings
      depend on when the `FiscalYearClosed` *declaration* happened, not on the Fiscal Year's
      own calendar end — a real reporting hole if that declaration is ever delayed past the
      year's actual end (worked failure scenario: [B21](B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md)
      Test 5). Corrected: B07 §1e now sums over every Fiscal Year that has **elapsed** as of
      D (End Date <= D, a pure calendar fact) — completely independent of whether
      `FiscalYearClosed` has been declared. **This principle's own "eligible for inclusion"
      language above is corrected by this note: `FiscalYearClosed` marks a Fiscal Year
      LOCKED, not eligible — eligibility for Reported Retained Earnings was never actually
      this event's concern, once elapsed replaces closed as the reporting-inclusion test.**
The authoritative formula, both non-overlapping and boundary-driven, together with its full
re-derivation from the raw ledger identity, now lives at [B07](B07_CONCEPTUAL_INFORMATION_MODEL.md)
§1e/§1f/§1g and [MP-12](#mp-12--reported-equity-reconciliation-new-added-at-corr-b4-01020305)
below — this principle's role is now limited to what `FiscalYearClosed` itself does (a
declaration/lock, nothing more), not the reporting arithmetic that follows from it.

Proof requirement: **worked numerically, not just symbolically** —
              [B20](B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md) Tests 9-11 trace a full
              example from pre-close Balance Sheet and P&L, through Fiscal Year Close (no
              Entry posted), to the post-close Reported Retained Earnings figure, confirming
              (a) the simple equation holds immediately after close using the derived Reported
              Equity figure, (b) no Balance Sheet amount is duplicated, (c) the new Fiscal
              Year's Revenue/Expense correctly start from zero with no entry required, and
              (d) — the specific defect (2) above — that the closing year's OWN historical
              query, evaluated as-of any date up to and including the close date, is
              unaffected by the close itself (nothing was posted, so there is nothing for such
              a query to pick up)
```

### MP-12 — Reported Equity Reconciliation *(new, added at CORR-B4-01/02/03/05; Proof G rebuilt at CORR-B5-03/04)*

```
Principle:    three precisely-named, precisely-scoped outputs — the Raw Cumulative Trial
              Balance (every account, one consistent horizon, ledger inception through D), the
              Current-Fiscal-Year Reporting Balance (Balance Sheet cumulative, Income Statement
              Fiscal-Year-bounded — a genuine reporting view, but NOT itself balanced), and,
              where retained, the Balanced Presentation Trial Balance (the reporting balance
              plus one explicit, never-posted derived bridge line) — are all reconciled here to
              the SAME underlying ledger. This principle proves the transformation between them
              is valid, non-double-counting, and viewpoint-safe, required by ChatGPT's Round 4
              audit (`M-AUD-08`) after Round 3 introduced mixed-horizon reporting concepts
              (B07 §1d/§1e) without formally re-deriving the equation from MP-02's original,
              single-horizon proof, and corrected again at CORR-B5-03/04 after ChatGPT's Round
              5 audit (`M-AUD-11`) found Proof G had, despite Proof A/B's own care, silently
              re-conflated the mixed-horizon reporting view with a claim of balance that only
              the true Raw Cumulative Trial Balance is entitled to.

PROOF A — Raw Ledger Identity:
              Exactly [MP-02](#mp-02--accounting-equation-corrected-at-corr-b02)'s proven
              expanded equation, with every term measured over the SAME horizon (all-time, no
              Fiscal-Year bound applied to any category, including Revenue/Expense):
                RawAssets + RawExpenses(all-time) = RawLiabilities + RawEquity(all-time)
                                                     + RawRevenue(all-time)
              Already proven (MP-02) as a direct corollary of MP-01 + Normal Balance Side
              (B07 §1a) — not reproven here, only cited as the base identity this principle
              transforms.

PROOF B — Reporting Transformation (raw identity to reported identity):
              Every Line has exactly one Effective Date, and exactly one Fiscal Year contains
              any given date for a Company (B07 §1, Fiscal Year's identity principle) — so
              Revenue/Expense partition exhaustively and disjointly by Fiscal Year:
                RawRevenue(all-time) = Σ over every Fiscal Year Y of Revenue(Y)
                RawExpenses(all-time) = Σ over every Fiscal Year Y of Expense(Y)
              Define CE(Y) = Revenue(Y) − Expense(Y) for each Fiscal Year Y, where Revenue(Y)/
              Expense(Y) are MP-09's `FiscalYearActivity_Current` formula (corrected at
              CORR-B5-02) evaluated for Fiscal Year Y specifically — B07 §1b's Current Earnings
              concept, applied to every Fiscal Year, not only the current one. Rearranging
              Proof A:
                RawAssets − RawLiabilities − RawEquity(all-time) = Σ over every Y of CE(Y)
              As of any query date D, only Fiscal Years up to and including the one containing
              D can have any Lines dated into them — split the sum into every ELAPSED Fiscal
              Year (End Date <= D, B07 §1e) plus the one Fiscal Year currently in progress
              (call it FY_now, the Fiscal Year containing D):
                RawAssets − RawLiabilities − RawEquity(all-time)
                    = Σ over every ELAPSED Y of CE(Y)  +  CE(FY_now)
              Decompose RawEquity(all-time) per B07 §1f — exhaustively and disjointly, since
              "Other Ledger Equity" is defined as every Equity-category account EXCEPT the one
              designated Retained Earnings account:
                RawEquity(all-time) = DirectRE(all-time) + OtherLedgerEquity(all-time)
              Substitute and regroup:
                RawAssets = RawLiabilities + OtherLedgerEquity(all-time)
                    + [DirectRE(all-time) + Σ over every ELAPSED Y of CE(Y)]  +  CE(FY_now)
              The bracketed term is exactly B07 §1e's corrected Reported Retained Earnings
              formula. Substituting B07 §1f's ReportedEquity = OtherLedgerEquity +
              ReportedRetainedEarnings:
                RawAssets = RawLiabilities + ReportedEquity  +  CE(FY_now)
              Since CE(FY_now) = Revenue(FY_now) − Expense(FY_now):
                Assets + Expense(FY_now) = Liabilities + ReportedEquity + Revenue(FY_now)
              QED — the Reported Financial-Statement Identity is derived from the Raw Ledger
              Identity by substitution alone, introducing no new assumption beyond Proof A,
              B07 §1e's elapsed-boundary definition, and B07 §1f's non-overlapping
              decomposition. (Asset and Liability categories require no transformation at all
              — they are all-time in both the raw and reported views; only Equity is
              re-grouped, and only Revenue/Expense are Fiscal-Year-partitioned.)

PROOF C — Current-Fiscal-Year Reporting Form (Proof B's conclusion, stated as the target form
              CORR-B4-05 requires):
                Assets + CurrentFY Expenses = Liabilities + Reported Equity + CurrentFY Revenue
              — where Reported Equity = Other Ledger Equity (B07 §1f) + Reported Retained
              Earnings (B07 §1e), non-overlapping by construction.

PROOF D — Historical Mode 1 (as-originally-known):
              Proof A's grand-total identity (Σdebit = Σcredit per COMMITTED Entry) holds for
              ANY consistent subset of Entries summed over — in particular, restricting to
              Entries with Recorded At <= T (MP-09 Mode 1) is exactly as valid a subset as "all
              Entries," since the per-Entry identity MP-01 requires is unaffected by which
              Entries are included. Proof B's algebra therefore goes through unchanged with
              every term replaced by its Mode-1/`_Known(D,T)` counterpart (B07 §1g):
                Assets_Known(D,T) + CurrentFY Expenses_Known(D,T)
                    = Liabilities_Known(D,T) + ReportedEquity_Known(D,T)
                      + CurrentFY Revenue_Known(D,T)
              Nothing in Proof A-C's derivation referenced "now" or "all currently-known
              facts" — it is viewpoint-agnostic by construction, so this equation is not a new
              proof, only Proof C evaluated at a fixed recording-time cutoff.

PROOF E — Restated Mode 2 (current/restated, after a legitimate Restatement):
              A Restatement is itself an ordinary, MP-01-balanced Correction Entry (B04 §3a/
              §3c) — it adds new Lines to the "as of now" set Mode 2 sums over. Since Proof
              A-C make no assumption about WHICH Entries exist, only that MP-01 holds for
              each, the equation holds after a Restatement's Lines are added exactly as it
              held before — no special-casing required. This is the formal justification for
              the qualitative claim B07 §1e property 2 already made (a Restatement "flows
              through" with no separate posted adjustment): it flows through because Proof
              A-C's derivation is agnostic to which specific balanced Entries exist at query
              time, restated or not.

PROOF F — Fiscal Close Declaration Invariant (CORR-B4-03's mandatory requirement):
              Let D_before and D_after be two query moments with no Entry committed between
              them (no new financial fact) and no Fiscal-Year End Date crossed between them.
              Every term in Proof C's equation — Assets, Liabilities, Other Ledger Equity,
              Reported Retained Earnings, CurrentFY Revenue/Expense — is a function purely of
              (a) which Entries are COMMITTED as of the query moment and (b) which Fiscal
              Years have ELAPSED as of the query moment (B07 §1e, a pure calendar fact). A
              `FiscalYearClosed` declaration is **neither** — it changes no Entry's commitment
              status and it changes no Fiscal Year's End Date. It does not appear as a term,
              or inside any term's definition, anywhere in Proof A-E. Therefore:
                ReportedEquity(D_before) = ReportedEquity(D_after)
              — not merely provably equal, but computed from the identical inputs, since the
              declaration is not one of those inputs. This satisfies CORR-B4-03's mandatory
              invariant by construction, not by a separate argument bolted onto the formula.

PROOF G — Trial Balance vs. Financial Statements *(REBUILT at CORR-B5-03/04 — see below;
              Round-4 version kept visible immediately after, struck through, per `M-AUD-11`)*:

~~The Raw Trial Balance is MP-09's direct output for every account, each under its own
natural bound (Balance Sheet categories all-time, Income Statement categories
current-Fiscal-Year-bounded — exactly what MP-09 (B08, unchanged) already computes, no
further transformation). It balances via Proof A + MP-09's existing category-bounded
aggregation. The Reported Financial Statements presentation applies exactly one further
transformation beyond the raw Trial Balance: re-grouping the Equity category's own account
balances into "Other Ledger Equity" + "Reported Retained Earnings" (B07 §1f)...~~

**WHY THIS WAS WRONG (`M-AUD-11`, CRITICAL — verified by tracing the literal claim against
Team B's own numbers, not just by the audit's say-so):** the struck-through text called
MP-09's *mixed-horizon* per-account output (Balance Sheet cumulative, Income Statement
Fiscal-Year-bounded) "the Raw Trial Balance," and claimed it balances "via Proof A." But
Proof A's identity holds only when EVERY category shares ONE common horizon — the moment
Revenue/Expense are truncated to the current Fiscal Year while Equity remains all-time
(uncorrected for prior elapsed years' earnings), the resulting SET of numbers no longer sums
to Proof A's identity on its own. Direct failure, Company X, D = Jan 5 2025 (FY2024 elapsed,
FY2025 in progress, no activity yet): MP-09's mixed-horizon output gives Assets(cumulative)
1250 debit, direct RE(cumulative) 1000 credit, Revenue(FY2025-bounded) 0, Expense
(FY2025-bounded) 0 — mixed-horizon debit total 1250 vs. credit total 1000, off by exactly 250
(FY2024's Current Earnings). This is not a rounding slip or an edge case; it is the direct,
inevitable consequence of truncating one side of a balanced equation and not the other. The
struck-through Proof G never actually re-derived a balance for this mixed-horizon object —
it merely asserted one, reusing Proof A's name without re-checking whether Proof A's
precondition (one common horizon) still held. It did not.

**CORRECTED — three separate, precisely-named, precisely-scoped outputs (supersedes the
struck-through text above), exactly as CORR-B5-01 requires:**

PROOF G1 — Raw Cumulative Trial Balance (Output A):
              Every Account Category, EVERY one, aggregated via
              `CumulativeAccountBalance_Current` (MP-09, corrected at CORR-B5-02 — one common
              lower horizon, ledger inception through D, no category-specific exception):
                Σ CumulativeAccountBalance_Current(A, C, D) over every debit-normal A
                  = Σ CumulativeAccountBalance_Current(A, C, D) over every credit-normal A
              This is EXACTLY Proof A's per-account generalization — it balances directly and
              unconditionally, for the same reason Proof A does (a direct sum of MP-01's
              per-Entry identity over a single, common, consistently-applied horizon). Company
              X, D = Jan 5 2025: debit 1250 (Assets) + 150 (cumulative Expense, NOT
              FY2025-bounded) = 1400; credit 1000 (direct RE) + 400 (cumulative Revenue, NOT
              FY2025-bounded) = 1400. BALANCED — this is the genuine Raw Cumulative Trial
              Balance, and it is the ONLY object in this principle entitled to be called a
              "Trial Balance" without further qualification.

PROOF G2 — Current-Fiscal-Year Reporting Transformation (Output B, from Proof B above):
              `FiscalYearActivity_Current` (MP-09, corrected) partitions cumulative Revenue/
              Expense into every elapsed Fiscal Year's contribution plus the Fiscal Year in
              progress — exactly Proof B's derivation, restated using the corrected MP-09
              names:
                Σ over every ELAPSED Y of CE(Y)  +  CE(FY_now)
                  = RawAssets − RawLiabilities − RawEquity(all-time)   [Proof B, rearranged]
              The resulting per-account "reporting balance" set — Balance Sheet accounts at
              `CumulativeAccountBalance_Current`, Revenue/Expense accounts at
              `FiscalYearActivity_Current` — is a genuine, useful REPORTING view (it is what
              Balance Sheet + current-period P&L accounts actually read), but it is **NOT, by
              itself, a balanced Trial Balance** — Company X, D = Jan 5 2025: this mixed set
              gives exactly the 1250-vs-1000 imbalance traced above. Stating this explicitly,
              by name, is the direct fix for `M-AUD-11`: this output is named "Current-Fiscal-
              Year Reporting Balance," never "Trial Balance," anywhere in this design pack.

PROOF G3 — Balanced Presentation Trial Balance (Output C, if a balanced current-FY-style
              presentation is wanted under the no-posted-close model):
              Take Proof G2's reporting-balance set and add exactly ONE further line —
              the same accumulated-elapsed-Fiscal-Year-earnings quantity Proof B already
              derives as Reported Retained Earnings' second summand:
                DERIVED PRESENTATION COMPONENT — NOT A POSTED FINANCIAL FACT:
                  "Accumulated Elapsed-Fiscal-Year Earnings" = Σ over every ELAPSED Y of CE(Y)
              Adding this one line to Proof G2's set restores balance exactly:
                Σ (G2 debit-normal balances)
                  = Σ (G2 credit-normal balances) + Σ over every ELAPSED Y of CE(Y)
              Company X, D = Jan 5 2025: debit 1250 (Assets) + 0 (FY2025 Expense) = 1250;
              credit 1000 (direct RE) + 0 (FY2025 Revenue) + 250 (the derived bridge line,
              exactly FY2024's Current Earnings) = 1250. BALANCED. This bridge line is
              **never posted, never a committed Entry, never a Line** — it exists only inside
              a presentation computation, is recomputed fresh every time the presentation is
              produced, and is IDENTICAL to Reported Retained Earnings' own second term
              (B07 §1e) — this is not a fourth quantity to keep synchronized, it is the same
              quantity, reused. A presentation carrying this bridge line MUST display the
              label above verbatim (or an equivalent explicit "derived, not posted"
              annotation) — [CO-14](B09_CONTROL_AUDIT_DESIGN_OBJECTIVES.md), extended at
              CORR-B5-02, requires this exactly as it requires Mode/viewpoint labeling.

PROOF G4 — Known vs. Current, applied to G1/G2/G3:
              Every quantity in G1/G2/G3 has a Known-viewpoint counterpart, built the same way
              every other Known-viewpoint quantity in this design is built (MP-09's Known
              formulas, B07 §1g): substitute `CumulativeAccountBalance_Known(A,C,D,T)` for
              `_Current` and `FiscalYearActivity_Known(A,C,D,T)` for `_Current` throughout.
              G1's Raw Cumulative TB, G2's Reporting Balance, and G3's bridge line all balance
              identically under the Known viewpoint, for the same reason Proof D established:
              Proof A's grand-total identity holds for any consistent Entry subset, including
              the Recorded-At-filtered one. A later Restatement can change every Current-view
              figure in G1/G2/G3 (as Proof E already establishes) while every Known-view figure
              (fixed T) remains exactly reproducible — including the G3 bridge line itself,
              which is exactly why B07 §1g's viewpoint parameterization was required in the
              first place (`M-AUD-10`).

No financial fact exists in G2 or G3 that G1 does not already contain individually —
Reported Retained Earnings, Other Ledger Equity, and G3's bridge line are all computed
regroupings of balances G1 already shows, never synthetic or posted lines of their own.
[B22](B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md) Tests 1-4 verify all four
proofs with real numbers, including the exact failure case above, now shown to pass once each
output is correctly named and scoped.

Inputs:       every COMMITTED Line for the Company (Proof A/B/G1); the query date D and, for
              the Known viewpoint, the recording-time cutoff T (Proof D/G4); which Fiscal Years
              have elapsed as of D (B07 §1e, corrected — a versioned, historically-safe fact,
              §1h); which Equity account is the designated Retained Earnings account for the
              Company (B07 §1f, a one-time chart-configuration fact, CAP-01/MG-C15)
Outputs:      Reported Equity, Reported Retained Earnings, Other Ledger Equity, the Raw
              Cumulative Trial Balance (G1), the Current-Fiscal-Year Reporting Balance (G2, not
              itself balanced), and — if retained — the Balanced Presentation Trial Balance
              (G3, with its explicit derived bridge line), each in both reporting viewpoints
              (B07 §1g) — never silently blended, and never mislabeled as one another
Invariant:    BINV-10 (corrected again, Round 4) and BINV-14 (B05) for the non-duplication and
              declaration-independence properties; the new BINV-15 (B05, CORR-B5-01/02) for
              the requirement that G1/G2/G3 are never confused with one another in any report
              or artifact this domain produces
Boundary:     this principle proves the RELATIONSHIP between the raw cumulative ledger and the
              reported/presentation identities; it does not change MP-01, MP-09, or the
              Elapsed/Closed definitions themselves (B07 §1e/§1d) — it is a reconciliation
              proof, not a new posting rule. G3's bridge line is explicitly, permanently
              excluded from ever becoming a postable/committable fact — introducing a posted
              version of it would silently resurrect exactly the posted-closing-Entry model
              this design rejected at CORR-B3-05/CORR-B4-03 for `M-AUD-07`/`M-AUD-09`.
Rounding:     inherits MP-04 throughout; every term summed is already a rounded, already-
              balanced quantity, so no new rounding is introduced by the regrouping itself
Exception:    none
Proof requirement: **worked numerically, not just symbolically** —
              [B22](B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md) Tests 1-4
              verify G1 (mid-first-Fiscal-Year and post-boundary), G2 (numerically distinct
              from G1, and explicitly NOT claimed balanced), and G3 (the bridge line,
              balancing exactly once); [B21](B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md)
              Tests 1-4 remain valid for what they actually verified (Proofs A-C and the
              Reported Equity non-double-counting property) and are not superseded by this
              correction, only more precisely named
```

## Acceptance Check

```
All 11 mandated areas addressed : CONFIRMED (Double-entry=MP-01, Accounting equation=MP-02,
  Monetary precision=MP-03, Rounding=MP-04, Currency conversion=MP-05, Functional currency=
  MP-06, Foreign currency=MP-05/06, Reversal arithmetic=MP-07, Correction arithmetic=MP-08,
  Aggregation=MP-09 (renamed "Cumulative Account Balance & Fiscal-Year Activity" at
  CORR-B5-02 — "Trial Balance" removed from this principle's own name), Period cutoff=MP-10,
  Fiscal Year Close=MP-11, rewritten Round 3, further corrected Round 4; MP-12 new at Round 4,
  beyond the 11 mandated — Reported Equity Reconciliation, Proof G rebuilt Round 5)
No implementation proposed                : CONFIRMED — every formula is over B07's conceptual
                                             entities, none over a storage structure
Rounding gap (Team A OQ-03) not left silent: CONFIRMED — MP-04 proposes a default and flags it
                                             explicitly as requiring gate confirmation
MP-02 proof mathematically complete for open AND closed periods (CORR-B02) : CONFIRMED
MP-09 time-consistent for historical as-of queries, backdating-proof (CORR-B03, CORR-B2-01/02) : CONFIRMED
MP-09 category-bounded, no carry-forward double-counting (CORR-B2-03/04)   : CONFIRMED,
  verified numerically (B19)
MP-11 posts no Entry; no internal contradiction with "Revenue/Expense never reset by a
  posted action"; no corruption of the closing year's own historical query (CORR-B3-05,
  `M-AUD-07`)                                                              : CONFIRMED,
  verified numerically (B20)
Reported Equity does not double-count the designated Retained Earnings account; Reported
  Retained Earnings inclusion is boundary-driven (Elapsed), not declaration-driven (Closed);
  Raw Ledger Identity formally re-derived into the Reported Financial-Statement Identity via
  Proofs A-G (CORR-B4-01/02/03/05, `M-AUD-08`/`M-AUD-09`)                  : CONFIRMED,
  verified numerically (B21)
MP-09's mixed-horizon per-account output is never claimed to be a balanced Trial Balance;
  the true Raw Cumulative Trial Balance (Proof G1), the Current-Fiscal-Year Reporting Balance
  (Proof G2, explicitly not balanced), and the Balanced Presentation Trial Balance (Proof G3,
  with an explicit never-posted bridge line) are three separately-named, separately-scoped
  outputs (CORR-B5-01/02/03/04, `M-AUD-11`)                                : CONFIRMED,
  verified numerically (B22), including the exact failure case the audit traced
```

**B8 = COMPLETE.** *(Corrected at CORR-B02/CORR-B03/CORR-B2-01..05/CORR-B3-05/CORR-B4-01..05/
CORR-B5-01..04 — MP-02, MP-09 amended in place multiple times each, MP-10 clarified, MP-11 new
at Round 2 then rewritten at Round 3 then cross-reference-corrected at Round 4, MP-12 new at
Round 4 then Proof G rebuilt at Round 5, with every prior claim kept visible above each
correction, not deleted. MP-01, MP-03..08 are unchanged since their respective original passes
(MP-08 amended once, CORR-B03, a cross-reference to Void). MP-10's invariant line was corrected
at CORR-B01 to match B04/B05's Period-Lock/Consumption separation, and again clarified at
CORR-B2-03 to distinguish it from the new MP-11, with a light Round-3 note confirming that
boundary is unaffected by MP-11's own rewrite. MP-11 itself was rewritten at CORR-B3-05 from a
posted-closing-Entry model to a no-posted-close, derived-Reported-Retained-Earnings-formula
model, per `M-AUD-07`, then corrected again at CORR-B4-01/02/03 to remove its own copy of the
now-fixed formula in favor of a cross-reference to B07 §1e/§1f. MP-02's post-boundary paragraph
was corrected a third time at CORR-B4-01/02/03. MP-12 was new at Round 4, formally proving what
Round 3 had only asserted — and its own Proof G was found, at Round 5, to have silently
re-introduced a mixed-horizon-vs-balance conflation despite Proof A/B's own care; rebuilt into
G1-G4, per `M-AUD-11`. MP-09 itself was renamed at CORR-B5-02, removing "Trial Balance" from
its own title — the single word choice that most directly enabled Round 4's Proof G to
misdescribe MP-09's output as already-balanced.)*
