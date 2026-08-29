# B07 — Conceptual Information Model

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B7 — Conceptual Information Model |
| Scope | Business concepts, meaning, ownership, relationships, cardinality, identity. **No physical schema, SQL, ORM, index, or vendor field/PK/FK below.** |
| **Corrected** | **CORR-B02 (2026-08-29)** — §1a's closing claim ("this is what makes Assets = Liabilities + Equity meaningful") overstated what Normal Balance Side alone proves; corrected below, and a new §1b defines Current Earnings. **CORR-B01** — the Consumption Record row's "four B04 §4 trigger kinds" corrected to three (period close removed as a trigger). See [CORR_B01_B02_B03_CORRECTIVE_ROUND.md](CORR_B01_B02_B03_CORRECTIVE_ROUND.md). |
| **Corrected (Round 2)** | **CORR-B2-01/02/03/04 (2026-08-29)** — ChatGPT's Round 2 re-audit (`04e44b06489d8bea6c8d39410050d68cf08bce21`) found two further defects: an Entry's single "date" property let a backdated Correction rewrite relied-upon history (M-AUD-04), and Current Earnings (§1b) was bounded "since the last close" — ambiguous between ordinary Period close and Fiscal-Year close, matching M-AUD-05's finding that CAP-09 overgeneralized BF-09's year-end-specific rule. Fixed below: Entry now has two distinct temporal properties (§1c), and a new **Fiscal Year** entity is added. See [CORR_B2_CORRECTIVE_ROUND.md](CORR_B2_CORRECTIVE_ROUND.md). |

## 1. Conceptual Entities

| Entity | Business meaning | Identity principle | Owning capability |
|---|---|---|---|
| **Company** | A legal entity whose books are kept separately (CAP-05) | A stable business identifier, independent of any source-system internal ID | CAP-05 |
| **Account Category** | A fixed classification governing statement placement and carry-forward behavior (BINV-09) — **corrected Round 2:** carry-forward behavior is now defined precisely per §1b/§1d, not a generic "year-end" gloss | A closed, small set defined at the domain level, not per company | CAP-01 |
| **Account** | A node in one Company's chart of accounts | Stable once created; its Category is mutable only before first use (BR-08) | CAP-01 |
| **Fiscal Year** *(new, Round 2)* | A bounded span of time, composed of one or more contiguous Periods, that defines the horizon over which Income Statement (Revenue/Expense) activity accumulates before being closed to Equity (§1b, §1d) | Identified by its Company and the span it covers; exactly one Fiscal Year contains any given date for a Company | CAP-09 (renamed/rescoped, §2) |
| **Period** | A bounded span of time with one authoritative open/closed status (BINV-02) — an ordinary **posting lock**, distinct from and nested within a Fiscal Year; closing a Period never itself resets or transfers anything (corrected Round 2 — see §1d) | Identified by its Company and the span it covers; never two overlapping Periods answer for the same date/company/class; belongs to exactly one Fiscal Year | CAP-04 |
| **Entry** | A Financial Fact expressed in double-entry form (B03 §2) | A permanent, system-assigned identity that exists independently of any human-readable document number (see §4); **carries two distinct temporal properties, not one — see §1c (Round 2 correction)** | CAP-02 |
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

### 1b. Current Earnings *(new, added at CORR-B02; re-bounded at CORR-B2-03/04)*

**Current Earnings** is a derived concept, not a separately stored entity — like Ledger
(B03 §2), it is a computed view, not something with its own identity or lifecycle. It is
defined as: `Current Earnings = (sum of Revenue-category account balances) − (sum of
Expense-category account balances)`, **for the current Fiscal Year** (from that Fiscal
Year's start date through the query date) — **corrected at CORR-B2-03/04: "since the last
close" (the original round-1 wording) was exactly the ambiguity ChatGPT's Round 2 audit
flagged (`M-AUD-05`).** An ordinary Period closing (a posting lock, §1d) never bounds this
sum — only a Fiscal Year boundary does. It exists specifically to answer the question the
simple accounting equation cannot answer on its own during an open Fiscal Year: where does
the net effect of not-yet-closed Revenue and Expense activity sit, for reporting purposes?
Two equivalent ways to state the answer:

- **Expanded form (always true, open or closed):** `Assets + Expenses = Liabilities + Equity
  + Revenue` — a direct corollary of BINV-01 (every Entry balances) plus Normal Balance Side
  (§1a), with no additional assumption.
- **Reporting form (regroup the same equation):** `Assets = Liabilities + (Equity + Current
  Earnings)` — i.e., for reporting purposes, Equity-plus-not-yet-closed-Current-Earnings
  behaves as the simple equation's "Equity" term. This is a restatement, not a separate fact.

**Corrected at CORR-B2-03/04:** at **Fiscal Year Close** (CAP-09, redefined — not ordinary
Period close), Current Earnings is transferred into a formal Equity account via exactly one
new committed Entry. Revenue/Expense accounts are **not reset by any posted action** — see
§1d: their zero-point for the new Fiscal Year is a consequence of how they are aggregated
(bounded by Fiscal Year start), not something anyone resets. After Fiscal Year Close, Current
Earnings is zero again for the new Fiscal Year (nothing has been dated into it yet) and the
simple equation holds directly, using the now-updated formal Equity figure. See
[B08](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md) MP-02 for the full proof.

### 1c. Entry Temporal Properties — Effective Date and Recorded At *(new, added at CORR-B2-01/02)*

ChatGPT's Round 2 audit (`M-AUD-04`) found that this domain's Entry concept had only one
temporal property ("date"), used for two different purposes at once: determining which
Period an Entry belongs to, *and* determining what counts toward a historical "as of"
aggregation (B08 MP-09). Collapsing these let a backdated Correction silently rewrite
already-relied-upon history — because nothing distinguished "when this economically
happened" from "when the system actually accepted this fact." Fixed by splitting Entry's
temporal identity into two independent properties, corrected here and reflected in B08's
aggregation model:

- **Effective Date** — the date the accounting effect belongs to, from the business
  perspective (e.g., "this sale happened on March 15"). Business-meaningful, chosen by
  whoever proposes the Entry (subject to the ordinary Period-lock check, BR-05), and the
  basis for "which Period is this in." This is what the pre-Round-2 design called "date."
- **Recorded At** — the moment CAP-02 actually accepted the Entry as authoritative (Posting,
  B04 §7). **System-generated, assigned exactly once, at the instant of commitment; never
  user-settable, never editable, never backdated** — this is the property that makes it
  structurally impossible to fake "this was known earlier than it actually was." See
  [B05](B05_ACCOUNTING_INVARIANT_BASELINE.md) BINV-12 (new).

Effective Date answers "what period does this belong to and what did it change." Recorded At
answers "when could anyone possibly have known about this." B08 MP-09's two aggregation
modes (§1c continued in B08) are built on exactly this distinction, and neither property is
redundant with the other — an ordinary, same-day Entry has Effective Date ≈ Recorded At, but
a Correction or Restatement typically does not, and the difference between them is precisely
what the historical-reproducibility guarantee depends on.

### 1d. Carry-Forward Is Implicit, Not a Posted Fact *(new, added at CORR-B2-03/04)*

ChatGPT's Round 2 audit (`M-AUD-05`) found that CAP-09/BINV-10 (round 1) described carry-
forward as an *explicit committed fact* — a new "opening balance" Entry posted at every
Period close — while B08 MP-09 sums *all* historical Lines dated ≤ D. Combined, these two
statements double-count: the original historical activity and the new opening-balance Entry
both contribute to the same balance. **Resolved by adopting a Continuous Ledger model**
(compared against a Segmented-Period alternative in
[B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md) DT-09):

- **Asset / Liability / Equity accounts (Balance Sheet categories) accumulate all-time** —
  their balance as of any date D is the sum of every Line ever posted against them with
  Effective Date ≤ D, with no periodic re-assertion. Carry-forward across an ordinary Period
  boundary is therefore **implicit** — a mathematical consequence of the aggregation formula,
  not a fact anyone has to post. Nothing is created, so nothing can double-count.
- **Revenue / Expense accounts (Income Statement categories) accumulate within the current
  Fiscal Year only** — bounded below by the current Fiscal Year's start date, not all-time.
  This is what makes YTD reporting correct across ordinary Period boundaries (B08 MP-09) and
  what makes the zero-point for a new Fiscal Year automatic rather than something that must
  be reset by a posted action.
- **The one genuine new fact Fiscal Year Close creates** is the Current Earnings transfer
  into formal Equity (§1b) — because Equity, unlike Revenue/Expense, *is* an all-time
  cumulative Balance Sheet category, and the transfer is a real economic event (this year's
  result becoming part of permanent capital), not a bookkeeping reset.

This is also why a **migration opening balance** (B10 MG-C03) is not an instance of this
pattern: under a Continuous Ledger, there is no recurring "carry-forward" business event to
be an instance of. A migration opening balance is a one-time, distinct act — establishing the
starting point of a ledger that has no prior history *in this system* to sum over — not a
periodic transfer between two periods that both already exist in the same ledger.

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
