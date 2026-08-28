> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 08 — MATHEMATICAL MODEL REGISTER

## MM-01 — The balance identity
For every entry E: `Σ debit(lines of E) = Σ credit(lines of E)`.
Asserted in application code only (BR-01/BR-03).

## MM-02 — Signed balance representation
Each line carries `debit`, `credit` **and** `balance` as three stored `numeric` columns.
`balance` is the signed representation of the debit/credit pair. Three columns encode two
degrees of freedom — a redundancy that must be reconciled, not copied blindly, on migration.
Evidence: DB column observation.

## MM-03 — Exact decimal arithmetic
`debit`, `credit`, `balance`, `amount_currency` are all `numeric`. **No floating point.**
Evidence: DB column observation. This is a positive finding — the reference system is correct
here and any target must match or better it.

## MM-04 — Dual-currency amount pair
A line holds the company-currency amount (debit/credit/balance) and the transaction-currency
amount (`amount_currency`) with an associated currency. Monetary fields are declared against
`company_currency_id`, which is stored/related from the move. Evidence: SE-15, SE-16.
Conversion rate is validated at header level (BR-06).

## MM-05 — Reconciliation arithmetic
Partial reconciliations carry amounts and accumulate; a full reconcile marks the point at which
matched debits and credits net to zero. Evidence: DB inventory (partial 17 cols, full 5 cols).

## MM-06 — Carry-forward rule
Whether an account's balance carries across fiscal years is derived from its type
(`include_initial_balance`): balance-sheet types carry, profit-and-loss types reset.
Evidence: SE-18.

## MM-07 — Gapless sequence arithmetic
Hash-protected journals maintain `secure_sequence_number`, a strictly incrementing gapless
counter distinct from the display name. Evidence: SE-13.

## Precision note — UNKNOWN
Rounding and decimal-precision configuration (`decimal_precision.py` exists in the module set)
was **not** analysed in this domain pass. Recorded as GAP-D01-04.
