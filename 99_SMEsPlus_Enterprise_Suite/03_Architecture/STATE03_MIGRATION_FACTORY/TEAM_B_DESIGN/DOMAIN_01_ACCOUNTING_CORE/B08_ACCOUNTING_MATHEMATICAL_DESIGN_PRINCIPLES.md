# B08 — Accounting & Mathematical Design Principles

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B8 — Accounting & Mathematical Design Principles |
| Method | Extends Team A's MR-01..08 (evidence of what the reference system does or fails to guarantee) into this domain's own mathematical design commitments. No implementation — formulas are stated over the conceptual entities of B07, not over any storage structure. |

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

### MP-02 — Accounting Equation (Aggregate Corollary, Not a Separate Check)

```
Principle:    Assets = Liabilities + Equity, evaluated across the whole Ledger for one Company
              at one point in time
Inputs:       every COMMITTED Line for the Company, each Line's Account Category (B07)
Outputs:      a value that must be zero: (Assets) − (Liabilities + Equity)
Invariant:    PR-02, derivable — not independently enforced
Boundary:     **This is not a fourth check alongside MP-01.** If (a) every Entry satisfies
              MP-01 individually, and (b) every Account's Category correctly determines its
              normal balance side (BINV-09), the accounting equation holds in aggregate as a
              mathematical consequence — it does not require its own separate validation
              pass. Stating this explicitly matters: a design that checked the equation
              independently would be doing redundant work and could mask a Category-mapping
              defect by "fixing" the aggregate number without fixing the root cause.
Rounding:     inherits MP-04; since it is a sum of already-balanced, already-rounded Entries,
              no new rounding is introduced at the aggregate level
Exception:    none
Proof requirement: this domain's design obligation is to keep MP-01 and the Category-to-
              normal-balance mapping (CAP-01) correct — the equation's truth is evidence that
              both hold, and its failure would indicate a defect in one of them, not in some
              separate "equation-enforcement" mechanism this domain does not build
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
Rounding:     MP-04 applies to any newly computed amount (e.g., a delta)
Exception:    none
Proof requirement: regardless of shape, the correction Entry must pass MP-01 exactly as any
              other Entry would — this is what distinguishes a correction from a privileged,
              unchecked operation
```

### MP-09 — Aggregation (Account Balance / Trial Balance)

```
Principle:    balance(Account A, Company C, as-of date D) = Σ (signed amount of every Line
              referencing A) over every COMMITTED Entry belonging to C with date ≤ D, EXCLUDING
              Lines belonging to a VOIDED Entry, and INCLUDING Lines belonging to a SUPERSEDED
              Entry (a correction adjusts the aggregate by adding its own Lines to the sum —
              it does not remove the original's Lines from it)
Inputs:       every COMMITTED Line for the Company up to date D
Outputs:      a single signed amount per Account (a trial balance is this formula evaluated
              for every Account of a Company simultaneously)
Invariant:    this is the formula every downstream reporting capability (outside this domain,
              B03 §3) is entitled to assume is available and correct
Boundary:     "as-of date D" — not "as-of period," to allow both an as-of-today balance and a
              reconstructed historical balance using the same formula
Rounding:     the sum of already-rounded Line amounts; no re-rounding of the aggregate itself
              (a trial balance total must equal the exact sum of its already-exact
              components — this is precisely what MP-03's precision floor exists to guarantee)
Exception:    none — this is the one formula every other capability in the domain exists to
              keep trustworthy; it has no special cases by design
Proof requirement: re-evaluating this formula for the same (A, C, D) at two different times
              must produce the same result if nothing new has been committed with date ≤ D in
              between — this is the mathematical restatement of BINV-06/BINV-07 (immutability
              plus consumption permanence): a closed-period balance is a fixed point of this
              formula, not a moving target
```

### MP-10 — Period Cutoff Stability

```
Principle:    once a Period closes (CAP-04), MP-09 evaluated as of that Period's end date
              produces the same result forever afterward, for that Company
Inputs:       a closed Period's end date; MP-09's aggregation
Outputs:      a stable, reproducible balance
Invariant:    BINV-02 + BINV-06 combined — this principle is where those two invariants meet:
              period closure is treated as a Consumption trigger (B04 §4) specifically because
              it is what makes this stability property true
Boundary:     an authorized, recorded period reopen (B09) breaks this stability deliberately
              and visibly — the principle holds "as long as the Period remains closed," not
              unconditionally forever, and a reopen event is itself an Audit Event that
              explains any subsequent change in the reported result
Rounding:     none beyond MP-04/MP-09
Exception:    an authorized reopen, per B09 — never a silent one
Proof requirement: this domain's design obligation is that stability is achievable *because*
              of BINV-06's enforcement, not achievable *despite* mutability still being
              possible through some other path — the two must be the same mechanism, not two
              independent hopes
```

## Acceptance Check

```
All 11 mandated areas addressed : CONFIRMED (Double-entry=MP-01, Accounting equation=MP-02,
  Monetary precision=MP-03, Rounding=MP-04, Currency conversion=MP-05, Functional currency=
  MP-06, Foreign currency=MP-05/06, Reversal arithmetic=MP-07, Correction arithmetic=MP-08,
  Aggregation=MP-09, Period cutoff=MP-10)
No implementation proposed                : CONFIRMED — every formula is over B07's conceptual
                                             entities, none over a storage structure
Rounding gap (Team A OQ-03) not left silent: CONFIRMED — MP-04 proposes a default and flags it
                                             explicitly as requiring gate confirmation
```

**B8 = COMPLETE.**
