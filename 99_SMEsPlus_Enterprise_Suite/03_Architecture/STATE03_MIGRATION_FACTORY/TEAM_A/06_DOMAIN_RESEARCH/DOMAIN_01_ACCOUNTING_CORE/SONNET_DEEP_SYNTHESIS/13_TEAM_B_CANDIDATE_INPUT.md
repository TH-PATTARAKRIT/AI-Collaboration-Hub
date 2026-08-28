> TEAM B CANDIDATE INPUT — PENDING CHATGPT AUDIT / PMO / BOSS GATE
> Sanitized. No vendor object, method, field or table name below. No target code, schema,
> API, DTO, class, service or workflow. Vendor evidence lives only in the linked registers.

# 13 — TEAM B CANDIDATE INPUT (sanitized)

## BUSINESS FACTS
- Every committed accounting entry must have total debits equal to total credits.
- Money must be represented as exact decimal values, never binary floating point.
- Accounting periods, once formally closed and reported, must not silently accept new or
  altered transactions.
- A correction to an already-committed entry should be additive (a new, linked, offsetting
  record), never destructive (in-place alteration of the original).
- Foreign-currency transactions must be recognised at a valid exchange rate and — per IFRS —
  monetary balances must be remeasured to the functional currency at each reporting date.
- Certain statutorily regulated documents (confirmed by official source: Thai e-Tax
  invoices/receipts) must carry provable content integrity and origin authenticity, and be
  retained for a defined period.
- Statutorily numbered documents (confirmed by official source: Thai tax invoices) must state
  a serial number as a mandatory particular; a stronger "must be gapless / gaps are audited"
  characterization is plausible but remains secondary-sourced, not officially confirmed.
- Accounting records generally must be retained for a defined statutory period (Thailand:
  5–7 years) and be available for independent audit.

## ACCOUNTING PRINCIPLES
Double-entry bookkeeping · the accounting equation (Assets = Liabilities + Equity) · journal as
book of original entry, ledger as authoritative source · posting as the finalization step ·
period cutoff control · correction-by-reversal · exact-decimal monetary representation ·
functional-currency remeasurement (IAS 21).

## GENERIC BUSINESS RULES
See `05_GENERIC_BUSINESS_RULE_REGISTER.md`, GR-01 through GR-13 — all neutral statements.

## BUSINESS INVARIANTS
See `04_BUSINESS_INVARIANT_REGISTER.md`, INV-01 through INV-06.

## NEUTRAL BUSINESS EVENTS AND LIFECYCLE
A financial fact moves through: capture (not yet committed) → commitment (part of the
authoritative record) → optionally, voiding (retained but excluded) → optionally, correction
(a new, linked fact that never mutates the original). Whether a committed fact may ever be
mutated in place should depend on whether it has been consumed by anything outside the
entity's own books — not merely on its raw status. Full reasoning: `06_STATE_EVENT_LOGIC_ANALYSIS.md`.

## MIGRATION REQUIREMENTS
- Migrated entries must be independently validated for debit/credit balance; source-system
  presence in a "posted" state is not proof of validity.
- All applicable period-control mechanisms (however many exist) must be evaluated together for
  historical data, not assumed consistent.
- Reversal/correction linkages between records are business data and must be preserved as such.
- A migrated "committed-once" record cannot be assumed free of later, undisclosed alteration
  unless change history is also migrated and interrogated.

## AUDIT REQUIREMENTS
- A compensating balance-check must exist independent of source-system trust.
- Every regulated document class's integrity requirement must be honored regardless of any
  configuration default.
- The audit trail (who changed what, when) should be a forced, non-optional property of every
  committed fact, separate from whether the fact itself is mutable.

## REGULATORY REQUIREMENTS (Thailand, evidenced this round)
- Financial statements: prepared, retained, independently audited (Accounting Act B.E. 2543).
- Record retention: 5–7 years.
- e-Tax invoices/receipts: provable content integrity and origin authenticity (ETDA, official
  source, RETS 21-2562) — confirmed narrow scope, not confirmed to extend to the general ledger.
- Tax invoices: mandatory serial number (Revenue Department of Thailand, official source,
  Revenue Code §86) — confirmed narrow scope; the stronger gapless-numbering characterization
  remains P4 secondary-source only, not confirmed to extend to all journal entries.

## CROSS-ERP COMMON PATTERNS
Reversal (not deletion/edit) as the correction mechanism for posted documents (validated
against SAP Business One, which prohibits editing/deleting posted entries). Single-authority
period-state modeling (validated against NetSuite's 3-state + 1-permission design, contrasted
with the reference system's 6-field, per-user, exception-plus-bypass shape).

## ADVANCEMENT OBJECTIVES
See `12_REFERENCE_TO_ADVANCEMENT_REGISTER.md` ADV-01 through ADV-08. Highest priority: ADV-04
(force additive correction for committed, downstream-consumed facts) and ADV-07 (gate
mutability on downstream consumption, not raw status).

## OPEN BUSINESS QUESTIONS (not answered — carried to Team B as questions, not conclusions)
Does Thai law require tamper-evidence or gapless numbering for the general ledger, beyond the
confirmed e-Tax-invoice and tax-invoice scopes? Is periodic currency remeasurement (IAS 21)
a requirement this domain must independently implement, or is it satisfied elsewhere? What is
the correct rounding policy per currency? Full list: `11_RESIDUAL_UNKNOWN_REGISTER.md`.
