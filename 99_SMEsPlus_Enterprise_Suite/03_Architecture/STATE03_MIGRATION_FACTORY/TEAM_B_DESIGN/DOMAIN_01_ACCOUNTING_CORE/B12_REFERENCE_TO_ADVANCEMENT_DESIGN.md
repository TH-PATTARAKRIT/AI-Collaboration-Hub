# B12 — Reference-to-Advancement Design

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B12 — Reference-to-Advancement Design (mandatory) |
| Principle | Understand the reference deeply. Rebuild independently. Improve measurably. Do not copy the reference. Do not merely match it. |

Team A's `12_REFERENCE_TO_ADVANCEMENT_REGISTER.md` supplied eight candidate problem
statements (ADV-01..08), explicitly as input, not approved design. This phase converts each
into an actual design commitment — the specific mechanism from B02–B11 that answers it — and
adds one advancement candidate this domain's own design process surfaced independently.

---

### AD-01 — Non-Optional Balance Guarantee

| Field | Content |
|---|---|
| Reference capability | Entry balance validation |
| Observed limitation/risk | Application-only check, suppressible, zero database-level backstop (Team A CF-01, MR-01) |
| Independent business requirement | Double-entry integrity must hold provably at the point a fact becomes durable, not merely when application code chooses to check it |
| SMEsPlus advancement objective | ADV-01 — make the balance guarantee non-optional at persistence |
| Design option (chosen, from B02–B08) | Balance validation is structurally synchronous with Posting (B04 §7, MP-01) — CAP-02 has no "commit now, validate later" path; there is no suppression mechanism in this design at all, not merely a discouraged one |
| Measurement criterion | Number of code paths capable of producing a COMMITTED, unbalanced Entry: **target zero, structurally** — not "rare" or "logged and caught later" |
| Evidence | CF-01, MR-01, BINV-01, BR-01 |
| Residual assumption | None — this is the domain's most structurally closed advancement item |

---

### AD-02 — Tamper-Evidence as Default, Not Opt-In

| Field | Content |
|---|---|
| Reference capability | Ledger tamper-evidence (per-journal opt-in hash protection) |
| Observed limitation/risk | Opt-in; default value never independently confirmed (GAP-D01-14); Thai law confirms this is mandatory for e-Tax invoices specifically, narrower than a general-ledger claim |
| Independent business requirement | Regulatory-grade documents require provable integrity that does not depend on an administrator remembering to enable a setting |
| SMEsPlus advancement objective | ADV-02 — tamper-evidence as a default property of the classes that require it, extended by independent design choice (not regulatory claim) to the whole Audit Evidence trail |
| Design option (chosen) | CAP-07 (B02) makes coverage automatic per regulated document class (BR-11); CO-07 (B09) independently extends tamper-evidence to the entire Audit Evidence stream as this domain's own control-design choice, explicitly separated from the narrower, evidenced legal requirement (OQ-01 stays open, not silently resolved) |
| Measurement criterion | Percentage of regulated-class documents with integrity coverage present at commitment time: target 100%, by construction (not audited after the fact) |
| Evidence | CF-02, ADV-02, RG-03, RG-04, CO-07 |
| Residual assumption | Whether Thai law extends this requirement beyond e-Tax invoices/tax invoices remains OQ-01 — CO-07's broader coverage is offered as good practice, not represented as closing that open question |

---

### AD-03 — Single-Authority Period Control

| Field | Content |
|---|---|
| Reference capability | Period cutoff control |
| Observed limitation/risk | Six independent date fields, per-user computed variants, an exception object, and a code-level bypass sentinel — a fragmented answer to one question, vs. a peer (NetSuite) using one 3-state object plus one override permission |
| Independent business requirement | One authoritative answer to "is this period open for this posting" |
| SMEsPlus advancement objective | ADV-03 — reduce the number of independent, potentially-disagreeing controls |
| Design option (chosen) | CAP-04 (B02) is designed from the requirement first: one authoritative determination per (date, company, document class), consulted synchronously by CAP-02 (B04 §7) — not derived by counting the reference system's fields down to some smaller number |
| Measurement criterion | Number of independent mechanisms that must be inspected to answer "can this post": target 1 (the CAP-04 determination) plus, where applicable, one explicit, logged override — vs. the reference system's 8+ |
| Evidence | CF-03, ADV-03, NetSuite triangulation, BINV-02 |
| Residual assumption | Whether the six reference-system controls have ever actually disagreed in practice was never data-tested by Team A (no representative dataset) — irrelevant to this design's correctness, since AD-03 does not depend on replicating or diagnosing that specific history |

---

### AD-04 — Additive-Only Correction for Consumed Facts *(highest priority)*

| Field | Content |
|---|---|
| Reference capability | Correction of a posted entry |
| Observed limitation/risk | The reference system offers **both** a sound pattern (reversal) and an unsound one (reset-to-draft on already-posted history) for the identical business need, and nothing in the reference system forces the sound one — a peer (SAP Business One) explicitly forbids the unsound alternative outright |
| Independent business requirement | Once committed and consumed downstream, a fact must be correctable only additively |
| SMEsPlus advancement objective | ADV-04 — eliminate or gate the destructive correction path so the additive path is the only one available for committed, downstream-consumed facts |
| Design option (chosen) | The entire B04 lifecycle model (§4 Consumption Gate) is built around this objective specifically: BR-07 refuses in-place mutation of a consumed Entry outright; BR-06/MP-07/MP-08 make the additive path the *only* path once consumed; CO-06 additionally requires the safe path never be bureaucratically harder than the eliminated one |
| Measurement criterion | Percentage of corrections to *consumed* committed Entries that are additive (Correction-Link-based) vs. destructive (in-place edit): **target 100% additive, structurally enforced**, not merely encouraged — directly matches Team A's own proposed metric (ADV-04), now backed by an actual mechanism rather than stated as an aspiration |
| Evidence | CF-04, CF-06, ADV-04, disagreement-03 (priority elevation), INV-06, BINV-06, BINV-07 |
| Residual assumption | The specific consumption-trigger list (B04 §4) that operationalizes "downstream-consumed" is this domain's own design judgment — flagged for B13/B16 review, as already noted in B05 BINV-06 |

---

### AD-05 — Reduced Type-Branching Burden

| Field | Content |
|---|---|
| Reference capability | Document typing (one overloaded table for journal entries, invoices, bills, credit notes) |
| Observed limitation/risk | Every consumer of the model must branch on type to know what it is looking at |
| Independent business requirement | A correct system should not force every downstream consumer to special-case storage-shape decisions made upstream |
| SMEsPlus advancement objective | ADV-05 — reduce the branching burden inherited from one shape serving semantically distinct objects |
| Design option (chosen) | B02 §3 and B03 §1 make this structural rather than aspirational: CAP-02 (Financial Fact Capture & Commitment) is defined around the business event of commitment itself, identical regardless of originating process; document type is carried as an attribute of the proposal (an origin reference, B11 #15), never a capability-boundary distinction a consumer must branch on to use CAP-02 correctly |
| Measurement criterion | Number of distinct type-dependent behaviors a downstream consumer of CAP-02 must special-case to commit an Entry correctly: target 0 — type-specific behavior (e.g., CAP-07's regulated-class handling) is opt-in metadata on an otherwise uniform Entry, not a fork in the capability itself |
| Evidence | ADV-05 (carried from Part 1, not independently re-evidenced by Sonnet) |
| Residual assumption | This item has the thinnest independent evidence base of the nine (single-source, Part 1 only) — carried forward at the same confidence Team A assigned it, not upgraded here |

---

### AD-06 — Single Authoritative Monetary Representation

| Field | Content |
|---|---|
| Reference capability | Monetary column representation (debit/credit/balance as three columns) |
| Observed limitation/risk | Three columns encode two degrees of freedom; no CHECK constraint found tying `balance` to `debit − credit` — structurally possible for the trio to disagree (Team A's sharpened MR-02 finding, distinct from CF-01) |
| Independent business requirement | A single monetary fact should have a single authoritative representation, not several independently-writable views of the same thing |
| SMEsPlus advancement objective | ADV-06 — reduce the number of independently-writable columns representing one monetary fact |
| Design option (chosen) | B07's Line concept (§1) carries an amount and a direction (debit/credit) as the *only* independently-set values; any signed/net representation is treated as a **derived view for reading**, computed from those two, never a third independently-writable value that could drift from them |
| Measurement criterion | Whether the stored representation can ever disagree with itself: target structurally impossible (derived values are computed on read, not stored redundantly), vs. the reference system's "structurally possible, not disproven" status |
| Evidence | CF-05, MR-02, ADV-06 (sharpened this round per Team A's own synthesis pass) |
| Residual assumption | None material |

---

### AD-07 — Mutability Gated on Consumption, Not Status

| Field | Content |
|---|---|
| Reference capability | State/status representation (`state` field mixing "is this committed" with "should this still count") |
| Observed limitation/risk | The invariant that *should* gate mutability (external consumption) is not the invariant that *does* gate it (raw status) — Team A's sharpest structural diagnosis of the domain's central weakness |
| Independent business requirement | Correction-path availability should be gated on what actually matters |
| SMEsPlus advancement objective | ADV-07 — gate mutability on downstream consumption, not a status enum |
| Design option (chosen) | This is, in effect, the objective B04 §4's Consumption Gate exists to satisfy directly — not a secondary consequence of AD-04, but the same design decision viewed from the state-modeling angle rather than the correction-mechanism angle. Both AD-04 and AD-07 are satisfied by one mechanism, not two. |
| Measurement criterion | Whether "has this been consumed downstream" is knowable and enforced *before* a destructive path is ever offered: **yes, by construction** — BR-07 checks Consumption Record existence (B07), not raw State, before permitting any mutation decision |
| Evidence | `06_STATE_EVENT_LOGIC_ANALYSIS.md`, ADV-07 (Team A's newest-round finding, not present in Part 1) |
| Residual assumption | Same as AD-04 — the consumption-trigger list is a Team B judgment call, not a Team A evidence fact |

---

### AD-08 — Currency Remeasurement

| Field | Content |
|---|---|
| Reference capability | IAS 21 periodic remeasurement of monetary items |
| Observed limitation/risk | Whether the reference system implements this **at all** is genuinely unknown — Team A correctly declined to state a limitation without evidence (status: RESEARCH REQUIRED, not SUPPORTED) |
| Independent business requirement | IAS 21 compliance requires remeasurement at each reporting date, not merely recognition at transaction date |
| SMEsPlus advancement objective | Because Team A could not form a limitation statement, this domain forms the design objective directly from the accounting standard itself, independent of whatever the reference system does or does not do |
| Design option (chosen) | CAP-06 (B02) and MP-06 (B08) design remeasurement as a scheduled, non-optional capability output — a designed commitment, not a gap inherited or assumed closed by resemblance to the reference system |
| Measurement criterion | Whether every foreign-currency monetary balance has a Remeasured Entry (B04 §3) for every reporting date it spans: target 100%, independent of whether any reference system achieves this |
| Evidence | MR-04, INV-04b, ADV-08 |
| Residual assumption | This remains the one advancement item this domain designs *toward a standard* rather than *away from an observed reference-system weakness* — stated explicitly so it is not mistaken for the same evidentiary shape as AD-01 through AD-07 |

---

### AD-09 — Multi-Tenant-Safe Capability Design *(new — identified during Team B's own design process, not present in Team A's ADV-01..08)*

| Field | Content |
|---|---|
| Reference capability | N/A — the reference system was never evaluated as multi-tenant SaaS by Team A (out of scope for a single-deployment forensic pass) |
| Observed limitation/risk | Not an observed reference-system limitation — an independently identified design requirement arising from this project's own stated identity (directive §1: independent SaaS ERP), which the reference system's evidence simply never speaks to either way |
| Independent business requirement | No tenant's data — including aggregate or statistical data, not just line-level detail — may ever become visible to another tenant |
| SMEsPlus advancement objective | Ensure no capability in this domain's own design requires shared mutable state across tenants |
| Design option (chosen) | CO-10 (B09): every capability scoping decision in B02 was checked against this requirement; the one concrete example designed explicitly to satisfy it is CAP-07's document-numbering sequence, which must be scoped at least per-company, never shared platform-wide (a shared sequence would itself leak cross-tenant information — how many documents another tenant has issued) |
| Measurement criterion | Number of capabilities in B02 whose correctness depends on any cross-tenant shared mutable state: target 0 |
| Evidence | Directive §1 (project identity), CO-10 — no Team A source ID, by design, since this was never in Team A's evidence scope |
| Residual assumption | Full verification requires visibility into the platform layer beneath this domain, which is out of this domain's boundary (B03 §4) — this domain's obligation is only that its own design does not create a dependency that would make tenant isolation harder to enforce there |

---

## Acceptance Check

```
Reference not copied, not merely matched  : CONFIRMED — every AD-xx cites a specific
  independent design mechanism (B02–B11), not a closer imitation of the reference system
Every item has a measurable criterion     : CONFIRMED
Evidentiary shape distinctions preserved  : CONFIRMED (AD-08 explicitly marked as
  standard-derived rather than weakness-derived; AD-09 explicitly marked as having no Team A
  source ID)
```

**B12 = COMPLETE.**
