# B07 — Conceptual Information Model

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B7 — Conceptual Information Model |
| Scope | Business concepts, meaning, ownership, relationships, cardinality, identity. **No physical schema, SQL, ORM, index, or vendor field/PK/FK below.** |
| **Corrected** | **CORR-B02 (2026-08-29)** — §1a's closing claim ("this is what makes Assets = Liabilities + Equity meaningful") overstated what Normal Balance Side alone proves; corrected below, and a new §1b defines Current Earnings. **CORR-B01** — the Consumption Record row's "four B04 §4 trigger kinds" corrected to three (period close removed as a trigger). See [CORR_B01_B02_B03_CORRECTIVE_ROUND.md](CORR_B01_B02_B03_CORRECTIVE_ROUND.md). |

## 1. Conceptual Entities

| Entity | Business meaning | Identity principle | Owning capability |
|---|---|---|---|
| **Company** | A legal entity whose books are kept separately (CAP-05) | A stable business identifier, independent of any source-system internal ID | CAP-05 |
| **Account Category** | A fixed classification governing statement placement and year-end carry-forward behavior (BINV-09) | A closed, small set defined at the domain level, not per company | CAP-01 |
| **Account** | A node in one Company's chart of accounts | Stable once created; its Category is mutable only before first use (BR-08) | CAP-01 |
| **Period** | A bounded span of time with one authoritative open/closed status (BINV-02) | Identified by its Company and the span it covers; never two overlapping Periods answer for the same date/company/class | CAP-04 |
| **Entry** | A Financial Fact expressed in double-entry form (B03 §2) | A permanent, system-assigned identity that exists independently of any human-readable document number (see §4) | CAP-02 |
| **Line** | One attribution within an Entry (B03 §2) | Identified only in relation to its owning Entry — a Line has no independent existence | CAP-02 |
| **Currency Context** | The relationship between a transaction currency and a Company's functional currency for a given Entry (B03 §2) | Identified by the (Entry, currency pair) it applies to, not stored independently of the Entry it values | CAP-06 |
| **Exchange Rate** | A (currency pair, date) → rate fact, external to this domain's own authority but consumed by it | Identified by currency pair and date | CAP-06 (consumer, not source of truth) |
| **Correction Link** | The permanent, directed relationship between a correcting Entry and the Entry it corrects (B04 §6) | Identified by the ordered pair (correcting Entry, corrected Entry); see §3 cardinality rule | CAP-03 |
| **Audit Event** | One immutable record of a state-changing action (B04 §3) | A permanent, append-only identity; never reused, never edited | CAP-08 |
| **Consumption Record** | A specialization of Audit Event marking that a specific COMMITTED Entry has been consumed, and by which of the three B04 §4 trigger kinds *(corrected at CORR-B01 — was four; period close is no longer one of them)* | Identified by (Entry, trigger kind, occurrence) — an Entry may accumulate multiple Consumption Records over time (e.g., filed, *then* separately referenced downstream); only the *first* one matters for BINV-06, but all are retained (BINV-07) | CAP-08, triggered by whichever capability observes the external event (filing/reconciliation are typically reported by domains outside this one, per B03 §3; downstream reference — including CAP-09's own carry-forward, which references the prior period's closing Entries — is observed within this domain) |

### 1a. Account Category — Normal Balance Side *(added at B16 §11, Persona 1 fix; corrected at CORR-B02)*

The red-team pass found that [MP-02](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md)'s
proof of the accounting equation as a corollary of MP-01 depends on "Account Category
correctly determines its normal balance side" — a property this entity list never actually
stated. Stated explicitly now: **every Account Category carries a Normal Balance Side
(debit-normal or credit-normal)**, fixed for the category (**Asset and Expense** categories
are debit-normal; **Liability, Equity, and Revenue** categories are credit-normal — standard
accounting convention, PR-01/PR-02, not an independent invention). An Account's aggregate
balance (MP-09) is interpreted against its Category's Normal Balance Side.

**Corrected at CORR-B02:** the previous version of this paragraph claimed Normal Balance Side
alone is "what makes `Assets = Liabilities + Equity` meaningful." ChatGPT's independent audit
(`D01-B-AUD-02`) correctly found this incomplete — Normal Balance Side alone proves the
*expanded* equation (`Assets + Expenses = Liabilities + Equity + Revenue`), which holds at
every moment, open period or not. The *simple* equation is a special case of the expanded one
(true exactly when Revenue and Expenses are both zero — i.e., after closing) — see §1b and
[B08](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md) MP-02 for the corrected proof.

### 1b. Current Earnings *(new, added at CORR-B02)*

**Current Earnings** is a derived concept, not a separately stored entity — like Ledger
(B03 §2), it is a computed view, not something with its own identity or lifecycle. It is
defined as: `Current Earnings = (sum of Revenue-category account balances) − (sum of
Expense-category account balances)`, for the accounting period since the last close. It
exists specifically to answer the question the simple accounting equation cannot answer on
its own during an open period: where does the net effect of not-yet-closed Revenue and
Expense activity sit, for reporting purposes? Two equivalent ways to state the answer:

- **Expanded form (always true, open or closed):** `Assets + Expenses = Liabilities + Equity
  + Revenue` — a direct corollary of BINV-01 (every Entry balances) plus Normal Balance Side
  (§1a), with no additional assumption.
- **Reporting form (regroup the same equation):** `Assets = Liabilities + (Equity + Current
  Earnings)` — i.e., for reporting purposes, Equity-plus-not-yet-closed-Current-Earnings
  behaves as the simple equation's "Equity" term. This is a restatement, not a separate fact.

At period close (CAP-09, BINV-10), Current Earnings is transferred into a formal Equity
account and Revenue/Expense accounts reset to zero for the new period — after which Current
Earnings is zero again and the simple equation holds directly, using the now-updated formal
Equity figure. See [B08](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md) MP-02 for the full
proof.

## 2. Deliberately Excluded From This List

Per directive §7, physical concerns are excluded even though they will eventually need
addressing: how an Account's chart relates to a shared template across companies
(`GAP-D01-05`, chart-template mechanics, remains genuinely unresolved — carried to
[B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) as an open design option, not decided here by
default); the specific data type used to store an amount; any notion of a "row" or "table."

## 3. Relationships and Cardinality

Cardinality is stated only where it carries business meaning — i.e., where getting it wrong
would silently violate an invariant from [B05](B05_ACCOUNTING_INVARIANT_BASELINE.md).

| Relationship | Cardinality | Business-significance |
|---|---|---|
| Company — Account | one Company has many Accounts; one Account belongs to exactly one Company | Enforces BINV-03 at the modeling level — there is no shape in which an Account could be shared across Companies |
| Account Category — Account | one Category classifies many Accounts; one Account has exactly one Category at any point in time | Supports BINV-09 — "exactly one at any point in time" is deliberate: it allows a *history* of category (before first use) without ever allowing an Account to have two simultaneous categories |
| Company — Period | one Company has many Periods; one Period belongs to exactly one Company | Supports BINV-02's "per company" scoping — no shared period state across Companies |
| Entry — Line | one Entry has one or more Lines; each Line belongs to exactly one Entry | An Entry with zero Lines cannot be balanced (BINV-01) and is not a meaningful concept — "one or more" is a business minimum, not an implementation default |
| Line — Account | many Lines may reference one Account; a Line references at most one Account (financial lines: exactly one, per BR-04) | Supports traceability (PR-07) — a Line's financial meaning is entirely mediated through its one Account |
| Entry — Company | every Line's Account determines the Entry's Company; an Entry's Lines must all resolve to the same Company | This is the precise, checkable form of BINV-03 — company consistency is a property of the *set* of an Entry's Lines, not a separate field asserted independently of them |
| Entry — Period | an Entry's date places it within exactly one Period of its Company | Supports BINV-02 — there is exactly one period-validity answer to consult, never an ambiguous match |
| Entry — Currency Context | an Entry has exactly one Currency Context if any Line carries a non-functional-currency amount; none if all Lines are already in the functional currency | Avoids forcing every domestic-currency Entry to carry a vacuous currency relationship |
| Currency Context — Exchange Rate | a Currency Context resolves to exactly one Exchange Rate at recognition, and consults a (possibly different) Exchange Rate at each subsequent remeasurement (BR-09) | Makes explicit that recognition and remeasurement are two distinct rate-lookups, not one rate frozen for the Entry's lifetime |
| Entry — Correction Link | **an Entry may be the *target* (corrected side) of at most one direct Correction Link.** An Entry may be the *source* (correcting side) of any number of Correction Links (in practice, business logic will usually keep this to one, but the model does not need to forbid a single correcting Entry from documenting linkage to more than one original if a future business need justifies it — the hard constraint is on the target side) | This is the precise cardinality rule that makes "chains, not trees" (B04 §6) checkable: at most one direct corrector per corrected Entry prevents two independent, potentially-conflicting corrections from both claiming to supersede the same original. Fixing an already-corrected Entry further means correcting the correction, not adding a second direct link to the original. |
| Entry — Audit Event | one Entry has many Audit Events over its lifetime; every Audit Event references at most one Entry (plus, for Period/Account-level events, the Period or Account instead) | Direct model of B04 §3's event table — nothing changes state without producing exactly one Audit Event |
| Entry — Consumption Record | one Entry has zero or more Consumption Records; the first one is what triggers BINV-06's immutability | Distinguishes "never consumed" from "consumed once" from "consumed multiple ways" without losing any of the history (BINV-07) |

## 4. Identity Principles (consolidated)

1. **No entity in this domain uses a source-system internal identifier as its own identity.**
   This is a direct design commitment carried forward from the migration-requirements input
   (B01 §8, "never use Odoo internal ID as SMEsPlus identity") and applied here as a
   conceptual-modeling principle, not deferred to migration time only.
2. **An Entry's identity is independent of its human-readable document number.** A tax invoice
   number, a check number, or any other printed/displayed reference is an *attribute* of an
   Entry (or, for regulated classes, a property CAP-07 manages under BR-12), never the means by
   which the Entry itself is identified or looked up internally. This deliberately avoids a
   failure mode common across ERPs generally: display numbers get voided, reset per fiscal
   year, or reused across document series, and none of that may ever be allowed to collide with
   or reassign an Entry's actual identity.
3. **Audit Events are the one entity class explicitly designed to never be identified by
   anything other than an append-only sequence.** No business meaning is allowed to attach to
   an Audit Event's identity (unlike an Entry's, which does carry business-meaningful
   attributes) — this keeps CAP-08 simple and resistant to the kind of misuse that could
   otherwise motivate someone to "renumber" history. **Amended at B16 §11 (Persona 5 fix):**
   this append-only sequence must be scoped at least per-Company — never a single sequence
   shared across an entire tenant, and never platform-global across tenants. A shared
   sequence would leak relative activity volume across the boundary it crosses (a
   competitor-adjacent tenant could infer another tenant's transaction volume purely from
   watching identifier gaps), which directly violates CO-10 even though no Entry content
   would be exposed. This is the same reasoning [B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md)
   DT-06 already applied to CAP-07's document-numbering sequence, applied here to Audit Event
   identity as well — an inconsistency the red-team pass specifically caught.

## 5. Conceptual Diagram

```mermaid
erDiagram
    COMPANY ||--o{ ACCOUNT : "owns"
    COMPANY ||--o{ PERIOD : "owns"
    ACCOUNT_CATEGORY ||--o{ ACCOUNT : "classifies (one at a time)"
    ACCOUNT ||--o{ LINE : "is referenced by"
    ENTRY ||--|{ LINE : "has (one or more)"
    ENTRY }o--|| PERIOD : "dated within exactly one"
    ENTRY |o--o| CURRENCY_CONTEXT : "has, if non-functional currency involved"
    CURRENCY_CONTEXT }o--|| EXCHANGE_RATE : "resolves via (recognition + remeasurement)"
    ENTRY |o--o| CORRECTION_LINK : "may be corrected by at most one direct link"
    ENTRY ||--o{ AUDIT_EVENT : "generates over its lifetime"
    ENTRY ||--o{ CONSUMPTION_RECORD : "accumulates zero or more"
```

*(Conceptual relationships only — no attributes, types, keys, or physical structure implied.)*

## 6. Acceptance Check

```
No physical table/column/index/type            : CONFIRMED
No vendor field/method/PK/FK name               : CONFIRMED
Every entity has an explicit owning capability   : CONFIRMED (traces to B02)
Every cardinality rule ties to a B05 invariant   : CONFIRMED (see §3 right-hand column)
```

**B7 = COMPLETE.**
