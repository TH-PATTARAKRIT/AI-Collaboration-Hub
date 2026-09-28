> Domain: PERIOD_CUTOFF_VALIDATION_PILOT (Gx6) | Business Trace | Documentation-Tier

# 06 — BUSINESS RULE REGISTER (Gx6)

### PCO-F01 — Lock Dates

- **WHAT**: System settings restrict creating/modifying accounting entries before a specified date. Documented types include an "Everything" lock and a "Hard Lock" (explicitly irreversible, to meet inalterability requirements in certain countries).
- **WHY**: Once a period's figures are reported/audited, they must not silently change.
- **BUSINESS RULE**: Setting a Lock Everything date to the last day of the preceding fiscal year is documented good practice; entries dated on/before the lock cannot be created or modified.
- **STATE**: Open period → locked (soft) → Hard Locked (irreversible).
- **DATA CONCEPT**: A lock date is a single cutoff value per lock type, not a per-transaction flag.
- **CONTROL**: Hard Lock is documented as irreversible — a materially stronger control than any other reversal/correction mechanism found in this Deep Study so far (all prior reversal mechanisms — Reverse Transfer, Credit Note, Vendor Refund — remain themselves reversible/correctable; a Hard Lock is not).
- **DEPENDENCY**: Interacts with every other pilot's "reversal" functions (GRV-F07, SDV-F06/F07) — a return dated before a Hard Lock would need special handling, not evidenced this round.
- **EVENT**: "Period locked."
- **RISK**: A design must not assume every correction path (return, credit note, adjustment) remains available indefinitely — Hard Lock is a genuine, documented dead end requiring a different mechanism (undocumented this round) to handle a post-Hard-Lock correction need.
- **UNKNOWN**: What mechanism, if any, handles a correction need discovered after a Hard Lock (a new-period correcting entry, presumably, but not documented explicitly this round) — `SOURCE/RUNTIME VERIFICATION REQUIRED`.

### PCO-F02 — Fiscal Year / Period configuration

- **WHAT**: Fiscal year defaults to 12 months ending December 31; configurable via Accounting → Configuration → Settings → Fiscal Periods → Last Day.
- **WHY**: Businesses operate on different fiscal calendars.
- **BUSINESS RULE / STATE / DATA CONCEPT / CONTROL / DEPENDENCY / EVENT**: Standard configuration surface, no unusual behavior documented.
- **RISK**: None identified — lowest-risk function in this Gx (matches C3).
- **UNKNOWN**: Interaction with the Annual Inventory Day/Month default found in Gx4 (`IAV-F05`) — both are period-related defaults; whether they must be kept in sync is not documented.

### PCO-F03 — Month-end Stock Closing + accrual entries (THE RESOLVING FINDING)

- **WHAT**: At period end (default: end of the fiscal period, though an alternate valuation date can be selected), a "Generate Entry" action produces a draft **Stock Closing entry**; once posted, it updates the Stock Valuation and Stock Variation accounts in the general ledger. Separately, an "Accounting → Review" screen surfaces pending mismatches (Bill To Receive, Invoices To Be Issued, Billed Not Received, Invoiced Not Delivered) for which **Create Accrual Entries** generates the bridging entries, each with its own Accrual Account and Reversal Date.
- **WHY**: Since ordinary postings wait for the invoice/bill event (per Gx2's finding), anything physically moved but not yet invoiced by period end would otherwise be missing from the Balance Sheet — this mechanism closes that gap once per period rather than requiring every individual movement to post immediately.
- **BUSINESS RULE — THE RESOLUTION**: *"Odoo 19 no longer creates journal entries upon the physical receipt or delivery of goods... posting at the time of the financial transaction (vendor bill/customer invoice), and finalizing the period's valuation with a single, comprehensive month-end journal entry"* via the accrual mechanism above. This directly reconciles Gx1's `GRV-F04` (which recorded the older/generic "posts at movement" claim) and Gx2's `SDV-F05` (which found the "posts at invoice" claim) — the invoice-time claim is the accurate one for ordinary operation; the Stock Closing/accrual mechanism is what makes that architecture still complete at period end.
- **STATE**: Period open (movements accumulate in Stock Variation buffer, uninvoiced items untouched) → period-end Generate Entry + Create Accrual Entries → period closed, Balance Sheet complete → next period opens with a Reversal Date undoing the accrual so the real invoice (when it lands) doesn't double-count.
- **DATA CONCEPT**: An accrual entry is explicitly paired with a Reversal Date — a self-cancelling mechanism, not a permanent one.
- **CONTROL**: This is the actual "controlled financial interface" the Backbone Roadmap's Lane C scenario 6 asks about — cut-off consistency is achieved *by this closing process*, not by every individual movement posting on time.
- **DEPENDENCY**: Directly resolves the open question in `GRV-F04`, `SDV-F05`/`GAP-SDV-01`, `IAV-F03`/`GAP-IAV-01` (see cross-references added to each).
- **EVENT**: "Stock Closing entry posted," "Accrual entries created" (paired with their own future reversal).
- **RISK**: A design that only implements per-transaction posting (assuming Gx1's original generic claim) and skips a period-close/accrual mechanism would produce an incomplete Balance Sheet for any uninvoiced movement — this closing step is not optional if the invoice-time posting model is used.
- **UNKNOWN**: Exact triggering — is Stock Closing a required manual monthly action, or can it be scheduled/automated? Not documented this round. Whether skipping a period's Stock Closing has any hard block or just leaves the Balance Sheet incomplete — `SOURCE/RUNTIME VERIFICATION REQUIRED`.

### PCO-F04 — Physical-date vs. recorded-date cut-off consistency

- **WHAT**: The literal question of whether a stock movement's physical date and its financial posting date can diverge, and how.
- **WHY / BUSINESS RULE**: Answered by `PCO-F03` — they routinely diverge (physical movement now, invoice/posting later, possibly next period), and the Stock Closing/accrual mechanism is the documented bridge across that divergence at period boundaries specifically.
- **STATE / DATA CONCEPT / CONTROL / DEPENDENCY / EVENT**: Same as `PCO-F03` — this function doesn't introduce new mechanics, it names the scenario that `PCO-F03` answers.
- **RISK**: Same as `PCO-F03`.
- **UNKNOWN**: Whether a *received-quantities-policy* bill created before receipt (Gx5 `PDT-F03`, if runtime-confirmed as a real control gap) would also require its own accrual/reversal handling, or whether it simply posts immediately at bill-creation regardless of the missing receipt — an interesting compound question across two still-partially-open findings, not resolved here.
