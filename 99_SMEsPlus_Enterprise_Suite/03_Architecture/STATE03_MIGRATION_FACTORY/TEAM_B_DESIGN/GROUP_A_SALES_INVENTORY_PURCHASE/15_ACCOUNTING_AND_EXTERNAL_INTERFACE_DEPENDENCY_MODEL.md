> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 10 — Accounting / External Interface Dependency Design

# 15 — ACCOUNTING AND EXTERNAL INTERFACE DEPENDENCY MODEL

## 00 — Hard Boundary Statement

Per governing prompt §10, TEAM B designs only the business-semantic handoff/interface where Sales, Purchase, or
Inventory creates a financial consequence. Chart of Accounts, GL posting engine, journal architecture, WHT engine,
tax engine internals, fiscal-position internals, valuation-accounting internals, and AR/AP internal posting logic
are Accounting Core's own domain and are not designed, redesigned, or second-guessed here.

## 01 — The Financial Handoff Contract

| Field | Content |
|---|---|
| What crosses the boundary | Billable-Now quantity (Sales and Purchase, each independently) + the resolved Party/Product/Currency/Payment-Term/Tax-candidacy/Cost-Dimension identities the line already carries |
| Who writes it | Sales / Purchase, at each Billing Event |
| Who owns everything past it | Accounting Core |
| What comes back | A durable posted-record reference, read backward by Sales/Purchase to re-derive Invoiced quantity |
| Traceability requirement | The posted record must carry a durable, application-visible link back to the originating Commercial/Supply Commitment line — elevated from a database-only FK, per [03](03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md) §06's general traceability requirement |

## 02 — Which Business Event Makes a Transaction Financially Relevant

Answer, independently reasoned from evidence: **the Billing Event** ([09](09_CANONICAL_BUSINESS_EVENT_CATALOG.md)
§01/§02), not commitment confirmation and not physical execution. A committed, even fully fulfilled, order/PO has
no financial consequence until Billable-Now is actually written to the Financial Handoff. This directly restates
one of the Never-Assume-Equivalence reminders in
[10](10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md) §03 as the governing answer for this file.

## 03 — What Business Fact Accounting Must Consume

- Billable-Now quantity (the amount to post)
- The resolved Tax Rule candidacy for the line (Accounting performs the actual substitution/computation —
  Sales/Purchase only supply candidacy, never compute the final tax amount themselves)
- The resolved Payment Term (snapshotted at commitment time, per [04](04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md) §04)
- The frozen Currency/Rate snapshot from commitment time
- The Cost Dimension allocation, if any, carried on the line

## 04 — Identity/Reference Traceability Requirement

Every value crossing the Financial Handoff must carry the originating Commercial/Supply Commitment's durable
reference and line identity, so a posted financial record can always be traced back to the exact commitment line
that produced it, and vice versa (the backward-read for Invoiced quantity depends on this being reliable). TEAM B
treats this as non-negotiable given evidence shows the reference system's own round-trip (`qty_invoiced` reading
back from posted entries) depends entirely on this linkage existing and being correct.

## 05 — Correction/Reversal Signal

When a posted financial record is corrected or reversed on Accounting's side, Sales/Purchase must observe this on
their next read of the backward Invoiced-quantity computation (per
[09](09_CANONICAL_BUSINESS_EVENT_CATALOG.md) §04's "Financial Record Reversed/Corrected" event) — TEAM B does not
require a push notification mechanism (not evidenced as needed) but does require the backward read to always
reflect the current state of Accounting's record, never a stale cached value.

## 06 — Fiscal/Tax Substitution — Preserved as an Interface Unknown

Both Sales and Purchase invoke a tax-substitution step (Party- and, for Purchase, Company-keyed) whose base
implementation was never located anywhere in the evidence's source tree — confirmed absent by the Independent
Evidence Review as well as Team A. TEAM B designs only the **fact that a substitution step exists and must be
invoked with the line's tax candidacy and the transaction's Party/Company context** — the substitution algorithm
itself is `CONTROLLED CARRY-FORWARD`, not designed, guessed, or assumed here. See
[18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md](18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md).

## 07 — Withholding Tax (WHT) — Confirmed Out of Scope for This Domain

Evidence confirms a complete WHT subsystem exists but attaches exclusively to Accounting-internal concepts
(posted financial records, payments, Product master), with **zero** references to Commercial or Supply Commitment
documents anywhere in the source tree (exhaustive grep, five modules). TEAM B confirms this boundary and designs
no WHT-related capability into Sales, Inventory, or Purchase — it is entirely Accounting Core's domain, reached
only through the Financial Handoff described above.

## 08 — Explicit Non-Design List (Restated for This File)

Not designed here, per governing prompt §10: Chart of Accounts; GL posting engine; journal numbering/architecture;
WHT engine internals; tax engine internals; fiscal-position internals; inventory-valuation-accounting internals;
AR/AP internal posting logic. Any of these referenced above is referenced only as "Accounting owns this," never
with an opinion on its internal shape.
