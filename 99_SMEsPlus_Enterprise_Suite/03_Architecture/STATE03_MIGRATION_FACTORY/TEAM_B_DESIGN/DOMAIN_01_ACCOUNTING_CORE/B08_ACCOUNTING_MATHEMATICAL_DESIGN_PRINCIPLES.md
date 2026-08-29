# B08 — Accounting & Mathematical Design Principles

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B8 — Accounting & Mathematical Design Principles |
| Method | Extends Team A's MR-01..08 (evidence of what the reference system does or fails to guarantee) into this domain's own mathematical design commitments. No implementation — formulas are stated over the conceptual entities of B07, not over any storage structure. |
| **Corrected** | **CORR-B02 / CORR-B03 (2026-08-29)** — ChatGPT Independent Design Audit (`aa60c2d0497cefe804d37953bbfaa597c3476d79`) found MP-02's original proof mathematically incomplete for an open reporting period, and MP-09's original VOID handling time-inconsistent for historical as-of queries. Both are corrected below, in place, with the original reasoning kept visible rather than deleted. Full comparison of alternatives: [CORR_B01_B02_B03_CORRECTIVE_ROUND.md](CORR_B01_B02_B03_CORRECTIVE_ROUND.md). |

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

Current Earnings (B07 §1b): define Current Earnings = Revenue − Expenses (both measured
              since the last close). Regrouping the proven expanded equation:
              Assets = Liabilities + (Equity + Current Earnings)
              — i.e., for REPORTING purposes, "Equity + not-yet-closed Current Earnings"
              plays the role the simple equation expects "Equity" to play. This is an
              algebraic regrouping of the proven identity, not a new assumption.

Post-closing special case: at period close, CAP-09/BINV-10 (corrected) transfers Current
              Earnings into a formal Equity account and resets Revenue/Expense to zero for
              the new period. Substituting Revenue = Expenses = 0 into the expanded equation
              collapses it exactly to the simple form: Assets = Liabilities + Equity — using
              the NOW-UPDATED Equity figure. The simple equation is therefore proven as the
              special case of the expanded one where Revenue = Expenses = 0, not asserted
              independently for "after closing" as a separate claim.

Inputs:       every COMMITTED Line for the Company, each Line's Account Category and Normal
              Balance Side (B07 §1a)
Outputs:      the expanded equation always; the simple equation exactly when Revenue =
              Expenses = 0 (i.e., post-close, or a company/period with no P&L activity yet)
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
              balance mapping (CAP-01), and the CAP-09 Current-Earnings-transfer step (BINV-10,
              corrected) correct — the expanded equation's truth is evidence all three hold;
              the simple equation's truth, specifically, is additionally evidence that closing
              was performed correctly for the period in question
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

### MP-09 — Aggregation (Account Balance / Trial Balance) — Corrected at CORR-B03

```
ORIGINAL FORMULA (kept visible, not deleted): "...EXCLUDING Lines belonging to a VOIDED
Entry..." — filtered by the Entry's CURRENT status. ChatGPT's independent audit
(`D01-B-AUD-03`) correctly found this time-inconsistent: an Entry valid at D1 and voided
later at D2 would vanish from a "balance as of D1" query performed after D2, even though it
was genuinely part of the truth as of D1. A later event must not rewrite an earlier as-of
result. The corrected formula below removes the status-based exclusion entirely.

Principle (corrected): balance(Account A, Company C, as-of date D) = Σ (signed amount of
              every Line referencing A) over every COMMITTED Entry belonging to C with
              date <= D. **No status-based exclusion of any kind** — not for VOIDED, not for
              SUPERSEDED. Every COMMITTED Entry's own Lines count at their own date,
              unconditionally.
Why this is now correct for VOID: per B04 §5 (corrected), voiding is itself a dated
              Correction Entry (a full reversal, MP-07, tagged as void) — it is not a status
              flip on the original. The voiding Entry's own (negating) Lines are dated at
              *its own* date (the point the void was recorded), and therefore only enter this
              sum for D >= that date, through the ordinary "date <= D" filter — no special
              case is needed, because voiding was never structurally different from any other
              correction once §5 was fixed. This is why the correction to MP-09 is a
              SIMPLIFICATION (one fewer special case) rather than added complexity.
Inputs:       every COMMITTED Line for the Company with date <= D
Outputs:      a single signed amount per Account (a trial balance is this formula evaluated
              for every Account of a Company simultaneously)
Invariant:    BINV-11 (new, added at CORR-B03) — this is the formula every downstream
              reporting capability (outside this domain, B03 §3) is entitled to assume is
              available, correct, AND time-consistent
Boundary:     "as-of date D" — not "as-of period," to allow both an as-of-today balance and a
              reconstructed historical balance using the same formula, with the same
              guarantee, for both
Rounding:     the sum of already-rounded Line amounts; no re-rounding of the aggregate itself
              (a trial balance total must equal the exact sum of its already-exact
              components — this is precisely what MP-03's precision floor exists to guarantee)
Exception:    none — this is the one formula every other capability in the domain exists to
              keep trustworthy; it now has *fewer* special cases than the original, not more
Proof requirement: re-evaluating this formula for the same (A, C, D) at two different times
              must produce the identical result, PROVIDED no Correction or Void dated <= D has
              been committed since — and, per the corrected formula, a Correction or Void
              dated > D structurally cannot affect the result at all, because it is filtered
              out by date before status is ever considered. **Scope precision (added at
              CORR-B05):** this is unconditional for CONSUMED facts (BR-07 forecloses
              Amendment, leaving Correction/Void — both dated — as the only path). For an
              UNCONSUMED fact, an in-place Amendment is a different operation from a
              Correction/Void, is not date-anchored the same way, and CAN legitimately change
              an as-of-D result computed before consumption occurs — by design, per BINV-11.
              This is now a structural guarantee of the formula's shape for the case that
              matters (relied-upon history), not a blanket claim for every number ever
              transiently computed.
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
MP-02 proof mathematically complete for open AND closed periods (CORR-B02) : CONFIRMED
MP-09 time-consistent for historical as-of queries (CORR-B03)              : CONFIRMED
```

**B8 = COMPLETE.** *(Corrected at CORR-B02/CORR-B03 — MP-02 and MP-09 amended in place, with
the original claims kept visible above each correction, not deleted. MP-01, MP-03..08, MP-10's
lock/consumption separation are otherwise unchanged from the original B8 pass; MP-10's
invariant line was also corrected, at CORR-B01, to match B04/B05's fix.)*
