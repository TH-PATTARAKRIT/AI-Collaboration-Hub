# P11 — WHOLE ACCOUNTING SEMANTIC MODEL

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room
Incorporates constitution correction `SMEPLUS-26-09-04-ACC-REV2-CORR1` (scope-aware).

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. The model in one statement

> A **classification identity**, at its declared **scope**, is given meaning by configuration. A
> **producer process** recognises a business event and hands the ledger an **accounting event** —
> carrying its own identity, its owner, its provenance, its idempotency key and the **company** whose
> financial effect it is. The ledger records that event as an **entry** carrying **financial facts**:
> signed amounts, in stated currencies, against classifications, with attributions. **Facts are
> permanent.** Obligations they create are discharged by **settlement facts**, which may themselves
> emit further accounting events where measurement has moved. **Measurement** is dated and never
> retroactive. **Finality** is declared over date ranges by governance, as an act with an actor, a
> date, a basis and an artefact. Everything else — balances, residuals, ageing, results, current-year
> earnings, absorbed cost — is **derived and must be reconstructible from the facts alone**.

Every clause is traceable. **Four clauses are not implemented anywhere in the evidence base**, and
each is named where it appears below: *"hands the ledger an accounting event"* (`UAE-29`), *"facts are
permanent"* (immutability is configuration), *"as an act with an actor, a date, a basis and an
artefact"* (`UAE-26`), and *"at its declared scope"* (`SCP-01`).

---

## 2. The eight facts

Wave A resolved **seven**. P11 adds an eighth, and re-scopes all eight under the corrected
constitution.

| # | Fact | Asserts | Owner | Scope | May it change? |
|---|---|---|---|---|---|
| `F1` | **Classification identity** | this bucket exists and means this | configuration | `PLATFORM` for the standard template, `COMPANY` for the instance | labels may; identity must not |
| `F2` | **Accounting event** | the business recognised something, on this date, for this amount, against these classifications | the **owning process** | `COMPANY` | **never** |
| `F3` | **Financial fact** (the item) | this signed amount, in this currency, belongs to this classification | its accounting event | `COMPANY` | **never** |
| `F4` | **Settlement fact** | this much of that obligation is discharged, by this counter-fact, on this date | the matching record | `COMPANY` | **never** — undone by a new fact, not by erasure |
| `F5` | **Measurement fact** | this rate applied on this date | the rate table | **`PLATFORM` for the observation, `COMPANY` for the selection** (`SC-05`) | corrected only by a dated correction |
| `F6` | **Finality declaration** | this period is no longer open | governance | `COMPANY` | soft may move; hard may only advance |
| `F7` | **Provenance** | this fact came from there, by this route | the producer | `COMPANY`, with a `TENANT`-scoped batch identity | **never** |
| ~~**`F8`**~~ | ~~Scope declaration~~ **WITHDRAWN per `X2-F01`** — `F8` was this table's own **Scope column** promoted to a row, and its own scope cell read *"itself"*, which is not a member of `{PLATFORM, TENANT, COMPANY}`. **Scope is a mandatory non-null attribute of every fact (`SCP-01`), not an eighth fact.** The model carries **seven** facts | — | — | — |

`F8` is **new at P11**, introduced by the constitution correction. It is a fact and not a control
because `MISSING REQUIRED SCOPE = DENY` cannot be evaluated unless the scope is itself a stored,
non-null property.

**Implementation status in the evidence base:** `F1`, `F2`+`F3` collapsed together, `F4` and `F5` exist
as durable objects. `F6` exists as **a bare date with no object behind it**. `F7` **is not implemented
at all**. `F8` does not exist. **Four of eight absent or degenerate** — `F2` is included, and it is the headline: the accounting
event, whose absence (`UAE-29`) is this package's root blocker. *(~~Three of eight~~ → **Four of eight** per `X4-F13`; superseded value retained so erasure is detectable.)*

---

## 3. The four unified semantic layers

### Layer 1 — Operational truth

Owned by the operating process. Quantity, location, hours, condition, dates. **No financial effect.**
`P01` receipts, `P02` deliveries, `P03` time logs, `P04` service status, `P06` bank lines.

The boundary is stated by Boss-approved lineage and is not reopened:
`Inventory Core = Stock Truth Owner. Accounting Core = Financial Truth Owner.`
**P11 generalises it:** *every* producing process is a truth owner for its own operational facts, and
none of them owns financial truth.

### Layer 2 — Valuation / cost

Converts an operational fact into an amount. **This layer is where the programme is most blocked.**
Costing method, cost basis, absorption rate, landed-cost allocation, day convention. Six of the
fifteen producer rows in the event-to-GL matrix are blocked *here*, and **not one of the six is
blocked on a peer process failing to publish** — they are blocked on `JT-02`, `JT-03`, `JT-04`,
`JT-05`, `JT-08` and `BLK-07`.

### Layer 3 — Accounting event

The clean-room addition. The event carries: identity, owning process, source-document reference,
**idempotency key**, intended accounting date, company, tenant, scope, provenance, and the amounts.
**It does not carry presentation, numbering or period placement** — those belong to the entry.

> This single separation resolves, from the evidence, **six** otherwise independent problems: duplicate
> detection (`DC-01`), correction semantics (`UAE-08`), period re-attribution (`UAE-04`, `UAE-05`),
> migration provenance (`F7`, element 14), the audit question *what did we recognise as distinct from
> how we wrote it down*, and **ownership itself** — `C1` fails 44 of 44 without it.

### Layer 4 — Ledger representation

Entry, item, number, date placement, lock, hash, statement mapping. Owned by `P08`.

---

## 4. What the four layers fix that a three-layer model does not

The reference model has layers 1, 2 and 4. It has no layer 3, and every structural finding in the
inherited base is a consequence:

| Symptom, as each package recorded it | Root |
|---|---|
| *"the same business event posted twice produces two equally valid entries and nothing detects it"* | no layer 3 |
| *"correcting the event and editing its representation collapse into the same operation"* | no layer 3 |
| *"the accounting date is system-derived, not user input"* — moved by a lock rule **and** by a numbering-convenience rule | layer 4 rules reaching into layer 3's territory |
| *"element 15 — deterministic idempotency identity — fails on 10 of 10 handoffs"* | no layer 3 to carry the key |
| *"element 14 — migration/replay batch identity — fails on 10 of 10"* | no layer 3 to carry provenance |
| *"analytic lines are deleted on un-post and regenerated"* | attribution attached to layer 4, not layer 3 |
| *"the financial entry date defaults to the processing date, not the physical event date"* | layers 1 and 3 not distinguished |

**Seven symptoms, recorded independently by four different domain programmes, one root.** That
convergence is the strongest single result of this reconciliation, and it is the reason `UAE-29` is
`P11`'s top-ranked blocker.

---

## 5. Answering the fourteen mandatory whole-system questions

Answered for the **class** of economic fact, with the exceptions named. `?` = not determined.

| # | Question | Unified answer |
|---|---|---|
| 1 | **What happened?** | A business event, registered in `P11_UNIFIED_BUSINESS_EVENT_REGISTER.md` — 44 named, denominator `UNBOUNDED` |
| 2 | **Who owns the event?** | One process per event. **9 of 44 have no determined owner**; 3 are owned by the ledger itself and must be named as such |
| 3 | **What operational fact exists?** | Layer 1, owned by the producing process |
| 4 | **What financial fact exists?** | `F3`, created only by an accounting event. **27 of 32 accounting events have no verified posting pattern** |
| 5 | **When does it become accounting truth?** | At recognition — **which for cost of sales (`JT-04`) and return cost (`JT-05`) is `NOT DECIDABLE`**, and for goods-received value (`JT-03`) has no stable pattern to imitate |
| 6 | **Which journal effect occurs?** | Verified for 5 core-ledger events. Withheld for all 15 producer rows |
| 7 | **Which subledger owns the balance?** | See `P11_SUBLEDGER_ARCHITECTURE.md`. **Analytic is derived and destructible; it is not a subledger of record** |
| 8 | **How is it settled?** | `F4`. **Over-reconciliation is unguarded** (`T0-05`) |
| 9 | **How is it reconciled?** | See `P11_SETTLEMENT_RECONCILIATION_ARCHITECTURE.md`. Inventory-to-GL agreement **holds at the closing boundary, not continuously** |
| 10 | **How is it reversed?** | Reverse-and-re-enter only. **The reference default is destructive and is `REJECT`** |
| 11 | **How is it reported?** | See `P11_SOURCE_TO_FINANCIAL_STATEMENT_TRACE.md`. **The report definition object is scope-mismatched** (`SC-02`) |
| 12 | **What happens at period close?** | **Nothing posts.** There is no close event, no closer, no artefact — only a moved date (`UAE-26`) |
| 13 | **What tenant/company owns it?** | Determined per object in `P11_SCOPE_OWNERSHIP_MATRIX.md`. **4 objects `HOLD — SCOPE EVIDENCE REQUIRED`**; 9 scope mismatches registered |
| 14 | **Can another module create the same effect?** | **Yes, in 3 registered cases** (`C4-01`…`C4-03`), and **structurally in all cases** while `UAE-29` is absent |

---

## 6. What this model is, and is not

**It is** a reconciliation of twenty-one published packages into one semantic frame, with every
inherited terminal state carried forward unweakened.

**It is not** a converged model. It cannot be, and the reason is arithmetic rather than judgement:
its inputs include **zero** published artefacts from the ten processes it was commissioned to
reconcile, and **not one** of the twenty-one packages it does consume carries a terminal state
stronger than `HOLD`, `PARTIAL` or `PROVISIONAL`.

> A whole-system model assembled over unconverged parts inherits their non-convergence. **Presenting
> it as converged would be the `GB-06` failure mode — a headline that contradicts its own
> dispositions — committed at the highest level in the programme.** This model does not do that.
