# B02 — Accounting Core Capability Model

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B2 — Accounting Core Capability Model |
| Method | Derived from business responsibility (B01 register), not from reference-system module boundaries |

## 1. Framing

A capability is identified here by asking: *what must be true of the business's financial
record for the enterprise to be solvent, compliant, and auditable* — not by asking what a
reference system happens to bundle into one installable unit. Nine capabilities were
identified. Each is stated independently of how (or whether) a reference system implements it.

## 2. Capability Register

### CAP-01 — Chart of Accounts Governance

- **What exists:** the classification structure (a fixed set of accounting categories, per
  BR-08/BF-10) that every financial fact must land in, and the rules for creating, retiring,
  and reclassifying accounts within it.
- **Why it exists:** without a stable classification, "total debits = total credits" is
  arithmetically satisfiable but commercially meaningless — the ledger must also be
  *organized* correctly to produce a balance sheet and income statement.
- **Owner:** Accounting Core. Not owned by any originating business domain (Sales, Purchasing,
  etc.) — they reference accounts, they do not define them.
  Legal Entity Owner is the entity's Accounting Core instance (see [B03](B03_DOMAIN_BOUNDARY_MODEL.md)).
- **Financial truth maintained:** every account has exactly one category, and that category
  governs statement placement and year-end behavior; a deprecated account cannot silently
  keep accepting activity through a use it wasn't guarded against (BR-13's partial-guard
  weakness in the reference system is the negative example this capability must not repeat).
- **Inputs:** account creation/edit requests; deprecation requests.
- **Outputs:** a queryable, versioned chart of accounts; a category-membership answer for
  every account, for every point in time.
- **Downstream dependents:** CAP-02 (every line needs a valid account), CAP-06 (statement
  placement), all reporting/consolidation capabilities outside this domain.

### CAP-02 — Financial Fact Capture & Commitment

- **What exists:** the single choke point through which any proposed financial fact — however
  it originated — becomes part of the authoritative ledger.
- **Why it exists:** this is the capability the entire domain organizes around: it is where
  IV-01 (Σdebit=Σcredit) either holds or the fact does not become authoritative. Per ADV-01,
  this guarantee must be non-optional at the point data becomes durable, not a courtesy
  application check.
- **Owner:** Accounting Core exclusively. No other domain may write directly to the ledger;
  they may only submit proposed facts to this capability.
- **Financial truth maintained:** every fact that is queryable as "committed" is balanced,
  attributed to exactly one company and one account per line, and dated within a period this
  capability has independently confirmed is open (via CAP-04).
  self-check against the closed-period case is deliberate: commitment must consult CAP-04, not
  assume the caller already did.
- **Inputs:** a proposed fact (a set of lines, each with account, amount, currency, date,
  company) from any originating capability, including manual entry.
- **Outputs:** a committed financial fact with a permanent identity; a rejection with reason,
  if the fact fails balance, account-validity, or period-validity checks.
- **Downstream dependents:** every capability in §2 that reads "the ledger"; every domain
  outside Accounting Core that reports on, reconciles against, or audits financial history.

### CAP-03 — Correction & Reversal

- **What exists:** the sole mechanism for changing what a *consumed* committed fact says,
  without destroying what it originally said.
- **Why it exists:** IV-05/IV-06/BR-06/BR-07 and ADV-04 (this domain's highest-priority
  advancement objective) all converge on one requirement: correction must be additive. This
  capability exists specifically so "the entry was wrong" never has to mean "the history is
  gone."
- **Owner:** Accounting Core. A correction is itself a financial fact and must pass through
  CAP-02 like any other.
- **Financial truth maintained:** for any committed fact that has been consumed downstream
  (LC-03 — reported, reconciled, filed, or otherwise relied upon outside this entity's own
  books), the only available correction path produces a new, linked fact; the original is
  never mutated. Below the consumption threshold, in-place correction may be legitimate (see
  [B04](B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md) §3) but is a distinct, narrower operation this
  capability must still gate and record, not a silent bypass of the rule.
- **Inputs:** a correction or reversal request referencing an already-committed fact.
- **Outputs:** a new committed fact linked to the one it corrects; the original, unchanged and
  still queryable.
- **Downstream dependents:** CAP-08 (Audit Trail), any downstream domain that already consumed
  the original fact and needs to know it was corrected rather than silently changed underneath
  it.

### CAP-04 — Period Control

- **What exists:** the single authoritative answer to "is this date, for this transaction
  class, open for posting right now" — and the mechanism for closing that answer off.
- **Why it exists:** IV-02/BR-05, and the CF-03 finding that a *fragmented* answer (multiple
  independent controls that can disagree) is a real, demonstrated risk, not a hypothetical one.
  ADV-03 specifically targets reducing the number of controls one must inspect to get this
  single answer.
- **Owner:** Accounting Core, scoped per company (CAP-05).
- **Financial truth maintained:** for any given transaction date, class, and company, there is
  exactly one authoritative open/closed answer, and CAP-02 consults it — the answer is never
  something an originating domain is trusted to have already checked.
- **Inputs:** period-close requests; override/exception requests (which must themselves be
  authorized and recorded, not a silent code-level bypass — see [B09](B09_CONTROL_AUDIT_DESIGN_OBJECTIVES.md)).
- **Outputs:** an open/closed determination, consultable by CAP-02 for every commitment
  attempt; a closed-period record that CAP-06 relies on for carry-forward.
- **Downstream dependents:** CAP-02 (gates every commitment), CAP-06 (defines when carry-
  forward is triggered), external financial reporting (defines what's frozen).

### CAP-05 — Company / Entity Boundary Enforcement

- **What exists:** the guarantee that a financial fact belongs to exactly one legal entity and
  cannot leak into or reference another's books.
- **Why it exists:** IV-03 — legal-entity separation is a business/regulatory requirement, not
  an implementation convenience; each entity must be independently reportable and auditable.
- **Owner:** Accounting Core, as a cross-cutting constraint enforced at CAP-02.
- **Financial truth maintained:** no committed fact's lines span more than one company; no
  account, journal, or period-control answer is shared across companies without an explicit,
  separately-designed consolidation capability (out of scope for this domain — see
  [B03](B03_DOMAIN_BOUNDARY_MODEL.md) §4).
- **Inputs:** company context on every proposed fact.
- **Outputs:** an accept/reject boundary check consumed by CAP-02.
- **Downstream dependents:** every other capability in this register is implicitly scoped by
  this one.

### CAP-06 — Currency Recognition & Remeasurement

- **What exists:** the capability that keeps a foreign-currency-denominated fact's functional-
  currency value honest, both at initial recognition and over time.
- **Why it exists:** RG-05/BF-05 (IAS 21) — recognition alone is not compliance; remeasurement
  at each reporting date is a distinct, ongoing obligation. OQ-02/ADV-08 record that whether a
  reference implementation actually does this is genuinely unknown — this capability is
  designed on the principle's requirement, not on an assumption that some existing system
  already satisfies it.
- **Owner:** Accounting Core.
- **Financial truth maintained:** every foreign-currency fact is recognised at a valid rate on
  its date (IV-04a: sign-consistency between the two currency views is a **minimum**, not a
  substitute, check); functional-currency balances are remeasured at each reporting date, and
  the remeasurement itself is a financial fact traceable through CAP-02/CAP-08.
- **Inputs:** a proposed fact carrying a non-functional currency amount and rate; a
  reporting-date remeasurement trigger.
- **Outputs:** functional-currency committed amounts; remeasurement adjustment facts.
- **Downstream dependents:** CAP-02 (every foreign-currency commitment routes through this),
  financial reporting outside this domain.

### CAP-07 — Regulated Document Integrity

- **What exists:** the narrow, statute-scoped guarantee of content integrity, origin
  authenticity, and/or sequential numbering for the specific document classes Thai law
  actually names — not a general claim extended to the whole ledger.
- **Why it exists:** RG-03/RG-04 (BF-06/BF-07) are real, officially-sourced obligations for
  e-Tax invoices/receipts and tax invoices specifically. GR-11/GR-12 record that the reference
  system implements the mechanism as an admin-configurable opt-in — AO-02 states the
  independent objective (default coverage, not opt-in memory) without assuming a stronger
  legal scope than is evidenced.
- **Owner:** Accounting Core, in coordination with whatever domain issues the regulated
  document (this domain owns the integrity/numbering guarantee once a fact is committed under
  a regulated document type; it does not own tax computation).
- **Financial truth maintained:** every fact tagged as belonging to a regulated document class
  automatically carries the integrity/numbering guarantee that class requires — coverage is a
  property of the class, not a remembered setting. This capability does **not** claim
  general-ledger-wide tamper evidence or universal gapless numbering (OQ-01) — doing so would
  be exactly the overclaim [B01](B01_AUTHORIZED_INPUT_REGISTER.md) §12 forbids.
- **Inputs:** a proposed fact tagged with a regulated document class.
- **Outputs:** an integrity-sealed, sequentially-numbered committed fact for that class.
- **Downstream dependents:** statutory filing/compliance capabilities outside this domain;
  CAP-08 for the evidentiary record.

### CAP-08 — Audit Trail & Evidence Provision

- **What exists:** the append-only record of every state-changing action taken against the
  ledger — who, what, when, before/after — independent of and orthogonal to whether the
  underlying fact itself is mutable.
- **Why it exists:** AU-03/PR-07/INV-06. LC-04 makes the key distinction this capability is
  built on: the *event log* being forced and append-only is a separate guarantee from whatever
  mutability rule governs the *record*. The reference system's version of this is optional
  (chatter/tracking); this capability treats it as non-negotiable.
- **Owner:** Accounting Core.
- **Financial truth maintained:** for any committed fact, its complete history of
  commitment/correction/void events is independently reconstructable without relying on the
  mutable record having preserved it.
- **Inputs:** every state-changing action from CAP-02, CAP-03, CAP-04.
- **Outputs:** an immutable event stream, queryable per fact, per period, per actor.
- **Downstream dependents:** internal/external audit, [B09](B09_CONTROL_AUDIT_DESIGN_OBJECTIVES.md)
  control objectives, dispute resolution.

### CAP-09 — Period-End Carry-Forward

- **What exists:** the mechanics of transitioning balances from one accounting period to the
  next: balance-sheet accounts carry forward, income-statement accounts reset to zero (BF-09).
- **Why it exists:** without this, "period closed" (CAP-04) has no defined effect on opening
  positions for the next period — the two capabilities are related but distinct: one answers
  *whether* posting is allowed, the other defines *what carries over* when it stops being
  allowed.
- **Owner:** Accounting Core.
- **Financial truth maintained:** opening balance of period N+1 for account A equals the
  closing balance of period N if A's category carries forward, else zero — computed, not
  manually re-entered, and itself a traceable fact through CAP-02/CAP-08.
- **Inputs:** a period-close event from CAP-04.
- **Outputs:** opening-balance facts for the new period.
- **Downstream dependents:** CAP-02 (opening balances are themselves committed facts),
  financial reporting.

## 3. Deliberately Not Vendor Module Boundaries

Three points where this model was checked against — and diverges from — the reference
system's actual module shape, to demonstrate independence rather than merely assert it:

1. The reference system stores journal entries, customer invoices, vendor bills, and credit
   notes in one overloaded table distinguished by a type field (ADV-05). This model does not
   define capability boundaries around document type at all — CAP-02 (Financial Fact Capture
   & Commitment) is defined around the *business event* (a proposed fact becoming
   authoritative), which is identical regardless of what business process produced the
   proposal. Document type is an attribute of the proposal, not a capability boundary.
2. The reference system implements period control as six independently-settable fields plus
   an exception object plus a code-level bypass (CF-03). This model defines CAP-04 as a single
   capability with one authoritative answer *by design requirement*, not because a reference
   implementation has one field for it — the requirement (ADV-03) is stated first, independent
   of whatever mechanism count a peer or the reference system happens to use.
3. The reference system does not appear to treat the audit/event log as a first-class,
   forced capability — it is optional tracking bolted onto individual models (CF-02 finding,
   LC-04 reasoning). CAP-08 is elevated here to a top-level capability specifically because the
   domain's central weakness (INV-06 / ADV-04) is a *consequence* of audit evidence being
   treated as elective rather than foundational — this is an independent structural decision,
   not an inherited one.

## 4. Capability Dependency Summary

```
CAP-01 (Chart of Accounts) ──┐
CAP-05 (Company Boundary) ───┼──▶ CAP-02 (Capture & Commitment) ──┬──▶ CAP-08 (Audit Trail)
CAP-04 (Period Control) ─────┘                                    │
CAP-06 (Currency) ───────────────────────────────────────────────┤
CAP-07 (Regulated Document Integrity) ────────────────────────────┤
                                                                    │
CAP-03 (Correction & Reversal) ───────────────────────────────────┤
                                                                    │
CAP-04 (Period Control) ──▶ CAP-09 (Carry-Forward) ────────────────┘
```

Every arrow into CAP-02 represents a capability CAP-02 must consult before a fact becomes
authoritative — this is the structural expression of ADV-01: the guarantee is non-optional
because nothing downstream of CAP-02 is trusted to have already checked it.

**B2 = COMPLETE.**
