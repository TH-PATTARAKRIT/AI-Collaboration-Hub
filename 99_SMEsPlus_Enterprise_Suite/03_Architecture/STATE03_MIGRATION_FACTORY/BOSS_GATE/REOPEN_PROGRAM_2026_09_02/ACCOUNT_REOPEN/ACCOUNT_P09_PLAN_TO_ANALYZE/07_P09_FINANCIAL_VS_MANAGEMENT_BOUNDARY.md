# P09_FINANCIAL_VS_MANAGEMENT_BOUNDARY

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Process:** P09 Plan-to-Analyze
**Layer:** 1 — clean-room business learning. Evidence identifiers `EV-P09-nnn` resolve in the Layer 2 quarantine; no reference-product identifier appears here.
**Constitution clause under test:** *Financial Ledger Truth must remain distinct from Management Accounting Truth.*
**Revalidated under:** `SMEPLUS-26-09-04-ACC-REV2-CORR1` (Scope-Aware Constitution Correction). Positions B-01 to B-08 were re-read against the corrected scope model; none depended on the superseded tenant-and-company-everywhere assumption and none is withdrawn. B-09 is added. See `P09_REVISION_LOG` §R1.

---

## 1. THE QUESTION THIS DOCUMENT SETTLES

The P09 directive asks whether analytic distribution **creates a financial posting** or **annotates / allocates financial truth**. Studied against the reference pattern, the question has three answers, not one, because the reference pattern contains three different mechanisms and only one of them is annotation.

| # | Mechanism | Direction | Does it post to the ledger? | Evidence |
|---|---|---|---|---|
| M1 | Analytic distribution on a ledger row | ledger → management | **No.** It is a percentage map stored on the row; at posting it spawns separate management records. Balance, debit and credit are untouched. | EV-P09-016, EV-P09-100..103 |
| M2 | Direct analytic production by an operational document | management only | **No — and there is no ledger record at all.** A timesheet, a work-order duration, an inventory estimation write a costed management record with no journal entry. | EV-P09-110, EV-P09-111, EV-P09-113 |
| M3 | Automatic transfer | management rule → ledger | **Yes.** A periodic reallocation rule, optionally *selected by analytic account*, creates real journal entries in a real journal. | EV-P09-040..049 |

**The answer to the directive's question is therefore: M1 annotates, M2 fabricates management truth with no financial counterpart, and M3 converts a management allocation into financial truth.** A design that adopts only M1 would satisfy the constitution. The reference pattern ships all three, enabled, with no boundary marker between them.

---

## 2. THE BOUNDARY AS BUILT

### 2.1 The management record is structurally independent of the ledger

At its own definition layer the management record (the *analytic line*) has no reference to a journal entry, a journal row, or a general ledger account. Those links are added by a higher layer and are **optional there too** (EV-P09-025, EV-P09-002/PRD-02 in Layer 2).

Three populations of management record therefore exist:

| Population | Ledger link | How created | Evidence |
|---|---|---|---|
| **F — financially backed** | present | produced at posting from the distribution on a ledger row; destroyed on reset-to-draft | EV-P09-103, EV-P09-104 |
| **O — operationally produced** | absent by construction | written directly by a timesheet, a work-order duration change, or an inventory estimation | EV-P09-110, EV-P09-111 |
| **V — valuation-derived, link discarded** | absent **although a ledger entry exists** | the amount is read from the posted entry, then written through a builder that carries no link field | COR-P09-05 |

Population **V** is the one that breaks the model. In F the link is present; in O there is nothing to link to; in V there *is* a ledger entry and the link is thrown away. A reconciliation between management and financial truth is impossible for population V without re-deriving the join from amounts and dates.

### 2.2 The sign convention is inverted

Management amounts carry the opposite sign to the ledger: cost is negative in management data and debit-positive in the ledger. The reference pattern's own reporting layer confirms this by negating the amount when it maps management data onto the ledger schema (EV-P09-031, EV-P09-053).

**Consequence for SMEsPlus:** any equation asserted between a management total and a ledger total must state its sign convention explicitly. An unstated sign convention is the most probable source of a silent reconciliation failure.

### 2.3 The management record has no transaction currency

The management record stores one amount, in the company currency, with a currency field that is merely *derived from the company*. There is no document-currency amount and no rate (EV-P09-026).

**Consequence:** management reporting on a foreign-currency business is not reproducible from the management record alone. The conversion is performed once, at write time, and the inputs are discarded.

### 2.4 Management balances are not stable over time

The balance of a management dimension is computed by converting each currency group **at today's rate**, into **the reading user's active company currency** (EV-P09-031). Three consequences follow, each independently disqualifying for a controlled ledger:

1. the same dimension reports a different balance on a different day with no underlying change;
2. the same dimension reports a different balance to a different user;
3. management records whose company is empty are included in **every** company's balance.

### 2.5 The boundary is crossed by the reporting layer, in the wrong direction

This is the most consequential finding of the session.

When a financial report is asked for an analytic column, the reporting layer **substitutes a temporary view built from management records in place of the ledger table** for the remainder of that report's queries (EV-P09-050).

Inside that view:

- the entry-state column is set to the **literal value "posted"** for every row (EV-P09-051);
- rows are admitted whose ledger link is empty, via an outer join (EV-P09-051);
- the only filter is that the row names a general ledger account;
- the balance is the **negated** management amount (EV-P09-053);
- the behaviour has a user-facing switch whose visible caption offers to include analytic data that has no ledger counterpart (EV-P09-052).

**Stated plainly: a financial report can present, as posted ledger data, records that were never posted and in some cases can never be posted.** The mechanism is not a defect of an edge case; it is the designed implementation of the analytic column, and it is gated by the same single group that also grants schema-altering rights over the dimension structure (EV-P09-012, EV-P09-056).

---

## 3. THE BOUNDARY SMEsPlus MUST DRAW

The following are stated as **design positions for Boss decision**, not as approved requirements. None of them is authorised by this document.

### B-01 — One business fact, one financial effect; management representation is derived, never authored.
A management record shall exist only as a derivation of a financial event or of an explicitly declared **non-financial operational event**. It shall never be the sole record of a costed fact that a user believes to be accounted for.
*Basis:* M2 / population O (EV-P09-110, EV-P09-111).

### B-02 — Every management record declares its provenance class.
Each management record shall carry a mandatory, immutable provenance class distinguishing at minimum: derived-from-posted-ledger, derived-from-unposted-document, operational-only, and allocation-result. The class shall be part of the record's identity, not a mutable field.
*Basis:* the reference pattern has three indistinguishable populations F/O/V and the platform reports on the ledger-less population as a first-class case (EV-P09-113).

### B-03 — A management record derived from a ledger row shall carry an enforced, non-discardable link to that row.
Where a financial event exists, the link shall be required and shall be enforced by the storage layer, not by the producing code path.
*Basis:* COR-P09-05 — the reference pattern discards an available link.

### B-04 — Management data shall never be presented through a financial statement surface without an explicit, non-defaultable provenance marker on every affected figure.
A financial report column sourced from management records shall be labelled as such on the figure, not in a filter panel, and shall not be capable of asserting a posting state it does not have.
*Basis:* EV-P09-050, EV-P09-051, EV-P09-052.

### B-05 — Management allocation shall not create financial postings under a management rule.
Where a reallocation must reach the ledger, it shall be produced as a named accounting event with its own document identity, its own approval, and its own reversal, and shall carry the management dimension that caused it.
*Basis:* M3 — the reference pattern's transfer mechanism posts, regenerates itself daily until posted, never revisits a posted period, and writes **no analytic dimension at all** onto the entries it generates (EV-P09-041, EV-P09-042, EV-P09-047).

### B-06 — Management amounts shall carry transaction currency, rate and rate date, or shall carry an explicit declaration that they are single-currency.
*Basis:* EV-P09-026.

### B-07 — A management balance shall be a function of (dimension, period, currency, as-at date) and of nothing else.
It shall not depend on the reading user, the reading user's active company, or the date of reading.
*Basis:* EV-P09-031, EV-P09-032.

### B-08 — The sign convention of management data shall be declared once, at the model level, and every published equation shall state it.
*Basis:* EV-P09-031, EV-P09-053.

### B-09 — A management aggregate shall be computed within one declared scope, and any widening shall be explicit.
*(Added under `SMEPLUS-26-09-04-ACC-REV2-CORR1`.)* A dimension balance shall be computed within the scope declared for the aggregation — PLATFORM, TENANT or COMPANY — and records of a different or undeclared scope shall not be admitted implicitly. Where a tenant-level management figure legitimately spans several companies, that widening shall be a named cross-company aggregation with its own authorisation and its own presentation marker, not a consequence of an empty scope field.
*Basis:* EV-P09-031 — the reference pattern admits company-empty management records into **every** company's balance, and converts them into the reading user's active company currency. Under the corrected constitution the presence of scope-wide records is not itself the defect; the implicit, unmarked, unauthorised widening is.
*Scope note:* the management record itself is COMPANY-scoped (it carries an amount attributable to a legal entity). The aggregate over it may legitimately be TENANT-scoped. B-09 governs the transition between the two.

---

## 4. THE THREE-TRUTH MODEL PROPOSED FOR SMEsPlus

The constitution names two truths. The evidence shows that two is not enough: the reference pattern's failure is concentrated in records that are *neither* financial truth *nor* clean management truth, but management truth that has lost its provenance.

| Truth | Definition | Authority | May be restated as the other? |
|---|---|---|---|
| **T1 — Financial Ledger Truth** | the set of posted accounting events and their double-entry effects | the ledger, closed by period | never |
| **T2 — Management Dimension Truth** | the assignment of financial truth to dimensions and cost objects | derived from T1, versioned, re-derivable | **T2 may never be summed into a financial statement without B-04** |
| **T3 — Operational Measurement Truth** | costed operational facts with no financial event (labour hours, machine hours, estimated valuations) | operational documents | **T3 may never enter T2 or T1 without an explicit accounting event** |

The reference pattern merges T2 and T3 into a single record type with a single amount field and no discriminator, then allows T2+T3 to be presented as T1. **Separating T3 is the primary architectural requirement this process produces.**

---

## 5. WHAT THIS DOCUMENT DOES NOT DECIDE

- Whether SMEsPlus implements any allocation-to-ledger mechanism at all. Position B-05 constrains the shape if one is built; it does not authorise building one.
- Whether the reference pattern's behaviours described here are defects in that product or deliberate design. This study is a **process benchmark**, not a product assessment, and no such judgement is made or implied.
- Any Thai statutory requirement for cost-centre or management reporting. No such requirement is asserted anywhere in this package; see the HOLD list in `P09_CONTRADICTION_REGISTER`.

**Terminal state of this document: FINDINGS ISSUED — NO GATE MOVED.**
