> DOMAIN_01 — Accounting Core | Team A PART 2 (Sonnet) | Input: committed Part 1 evidence | No SMEsPlus design

# 07 — MATHEMATICAL REASONING

Each model restated with formula, inputs, outputs, invariant, assumptions, boundary
conditions, rounding, failure condition, evidence and confidence. No equation is asserted
without a direct evidence anchor.

## MR-01 — Balance identity (formalizes MM-01)
```
Formula:      Σ debit(l) = Σ credit(l)   for all lines l in entry E
Inputs:       the set of account_move_line rows sharing one account_move_id
Outputs:      boolean — balanced / not balanced
Invariant:    must hold for E to be a valid posted accounting fact
Assumptions:  all lines of E are visible in the same query context at validation time
Boundary:     display_type in (section/subsection/note) lines are exempt — presentation only,
              carry no financial content (enforced by DB CHECK, see MR-05)
Rounding:     not addressed by this identity alone; see MR-06
Failure:      Σdebit ≠ Σcredit — application raises UserError UNLESS the check is suppressed
Evidence:     P1 account_move.py:2765-2782 (_check_balanced, _get_unbalanced_moves)
Confidence:   HIGH (mechanism) / EVIDENCE_MISSING (whether ever violated in stored data)
```
**Reasoning note.** This is an *aggregate* identity over a set of rows. PostgreSQL CHECK
constraints are evaluated per-row and structurally cannot express it — this is a property of
the constraint mechanism itself, not a vendor oversight. A trigger (`AFTER INSERT/UPDATE`,
statement- or row-level with aggregation) is the only DB-native way to enforce MR-01, and the
census confirms **zero triggers exist**. This closes the reasoning gap Part 1 could not close
without direct DB observation.

## MR-02 — Signed balance redundancy (formalizes MM-02)
```
Formula:      balance = debit − credit   (implied; not independently observed as a stored
              computation, only as three co-existing numeric columns)
Inputs:       debit, credit (both numeric, both >= 0 by convention implied by MR-05's CHECK
              constraint check_credit_debit: credit*debit=0, i.e. at most one is non-zero)
Outputs:      balance (signed numeric)
Invariant:    the three columns must agree; violated storage would show balance != debit-credit
Assumptions:  debit and credit are never both non-zero on one line — ENFORCED by DB CHECK
              (check_credit_debit), so this assumption is now verified, not assumed
Boundary:     presentation lines carry all three as zero (check_non_accountable_fields_null)
Rounding:     inherited from debit/credit precision — see MR-06
Failure:      if balance is written independently of debit/credit (e.g., by a bulk update that
              only touches one of the three columns), the trio can disagree — no CHECK
              constraint was found enforcing balance = debit - credit specifically
Evidence:     P2 column definitions; P1 SE-15/16; DB check_credit_debit constraint
Confidence:   HIGH on the redundancy existing; MEDIUM on whether it is DB-enforced (no
              constraint found tying balance arithmetically to debit/credit)
```
**Reasoning note — new finding this round.** The evidence pack documents that all three
columns are `numeric`, and that a CHECK constraint prevents debit and credit being
simultaneously non-zero. **No CHECK constraint was found that ties `balance` arithmetically to
`debit − credit`.** This means the three-column redundancy (MC-13 in Part 1: "normalize") is a
**real integrity gap distinct from CF-01** — three columns encode what should be two degrees
of freedom, and the third (`balance`) has no observed guarantee of consistency with the other
two. Recorded as a new sub-finding, not previously isolated this precisely in Part 1.

## MR-03 — Exact decimal arithmetic (formalizes MM-03)
```
Formula:      no arithmetic identity; a representation guarantee
Inputs/Outputs: any monetary column value
Invariant:    stored value has no binary floating-point representation error
Assumptions:  PostgreSQL `numeric` type behaves as documented (arbitrary-precision decimal)
Boundary:     precision/scale of the `numeric` columns was not enumerated (unread:
              decimal_precision.py, GAP-D01-04) — exactness of STORAGE is proven; the actual
              number of decimal places used per currency is NOT proven
Rounding:     UNKNOWN — this is exactly the open question MR-03 cannot answer
Failure:      would require binary float storage, which is directly disproven
Evidence:     P2 direct column type observation
Confidence:   HIGH (storage type) / UNKNOWN (rounding policy)
```

## MR-04 — Dual-currency amount pair (formalizes MM-04)
```
Formula:      amount_currency (transaction currency) coexists with debit/credit/balance
              (company currency); IAS 21 requires functional-currency remeasurement of
              monetary items at each reporting date
Inputs:       transaction amount, exchange rate at transaction date, functional currency
Outputs:      company-currency debit/credit/balance + transaction-currency amount_currency
Invariant (source, BR-06):  invoice_currency_rate must be valid — validated at header, not
              per-line
Invariant (IAS 21, external): initial recognition at spot rate; monetary items remeasured at
              subsequent reporting dates — https://www.ifrs.org/issued-standards/list-of-standards/ias-21-the-effects-of-changes-in-foreign-exchange-rates/
Boundary:     revaluation/remeasurement mechanics at period-end were NOT analysed this pass —
              new gap, see §11
Rounding:     inherits MR-03's open question
Failure:      currency-rate validation failure at header level (BR-06); no evidence of
              per-line remeasurement logic
Evidence:     P1 SE-15/16, BR-06; P1 (external) IAS 21
Confidence:   MEDIUM — the STRUCTURE is verified; the REMEASUREMENT PROCESS (a core part of
              IAS 21 compliance) was never observed
```
**Reasoning note.** IAS 21 compliance is not just "store two amounts" — it requires periodic
remeasurement of monetary items and recognition of exchange differences. **This domain pass has
no evidence either way on whether that remeasurement is implemented.** Recorded as GAP
(new, §11), not silently assumed satisfied by the presence of `amount_currency`.

## MR-05 — Row-level guarantees (new formalization, was absent from Part 1's math register)
```
check_credit_debit:                  credit × debit = 0        (at most one side populated)
check_amount_currency_balance_sign:  sign(balance) = sign(amount_currency)  (or both zero)
check_accountable_required_fields:   account_id required unless a presentation line
check_non_accountable_fields_null:   presentation lines carry zero financial content
Evidence:     P2 direct pg_restore -l; P1 account_move_line.py:463-478
Confidence:   HIGH — directly verified database-enforced guarantees
```
These four are genuine, verified mathematical guarantees the reference system provides at the
row level — the positive counterpart to MR-01's negative finding. They should be recorded
alongside MR-01, not overshadowed by it: the database enforces *some* accounting arithmetic,
just not the aggregate identity.

## MR-06 — Rounding policy (UNKNOWN — recorded honestly, not fabricated)
No formula can be stated. `decimal_precision.py` exists in the readable module set and was not
opened. Any statement about rounding method (banker's rounding, round-half-up, per-currency
decimal places) would be fabrication. **Status: UNKNOWN, not inferred.**

## MR-07 — Carry-forward rule (formalizes MM-06)
```
Formula:      opening_balance(year N+1, account A) =
                closing_balance(year N, account A)   if include_initial_balance(A.type)
                0                                     otherwise
Invariant:    balance-sheet account types carry forward; P&L types reset to zero annually
Evidence:     P1 SE-18 (include_initial_balance computed from account_type)
Confidence:   HIGH (mechanism) — the actual year-end closing PROCESS that computes this was
              not traced in this pass (new gap)
```

## MR-08 — Gapless sequence arithmetic (formalizes MM-07)
```
Formula:      secure_sequence_number(n+1) = secure_sequence_number(n) + 1, strictly, no gaps,
              scoped per hash-protected journal
Invariant:    no reuse, no gap, distinct from the human-readable display name
Evidence:     P1 SE-13
Confidence:   HIGH (mechanism) — whether the reference system's gapless sequence is what Thai
              Revenue Code §86 sequential-numbering practice expects for TAX INVOICES
              specifically is plausible but not directly evidenced as satisfying that statute
              (see 08_CROSS_SOURCE_TRIANGULATION T-09)
```
