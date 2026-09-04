> **CORR1 CORRECTION NOTICE.** Amended by session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`.
> Corrections landing here: `COR-14, COR-15, COR-16`. Governing text where they conflict with the body below: CORR1/C05.
> Prior findings are retained unedited for lineage; see `CORR1/C02_..._ACCEPTED_CORRECTIONS_REGISTER.md`.

# 22 — ACCOUNT_WAVE_A_SEMANTIC_TRANSFER_REGISTER

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

**Nothing here is classified `ADAPT` because the reference system does it.** Each decision states a
business, financial or control reason. `REJECT` entries state why. `UNKNOWN` entries state exactly
what is missing.

Every `ADAPT` and `EXTEND` carries: business reason · financial reason · control reason · SMEsPlus
semantic · source of truth · event owner · affected modules · SaaS implication.

---

## ADAPT — learn and carry forward

### `ST-01` Account identity is the record, never the code
- **Business** an account is a classification that survives every renaming and renumbering of it.
- **Financial** comparability across periods requires the classification to be stable.
- **Control** a code-keyed identity makes a renumbering into a data migration.
- **SMEsPlus semantic** the account is an identity; codes and names are labels resolved in a context.
- **Source of truth** configuration owns the identity; the label is per company.
- **Event owner** configuration.
- **Affected** every module that posts; all reporting.
- **SaaS** allows one shared classification with per-company presentation.
- **Evidence** `EV-001` — and this independently corroborates the standing Boss-approved principle.

### `ST-02` Every item always carries an explicit transaction currency
- **Business** the currency agreed is part of what was agreed.
- **Financial** without it, revaluation and settlement difference are not computable.
- **Control** removes the "is this already converted?" ambiguity entirely.
- **SMEsPlus semantic** currency is never implicit, even when it equals the company currency.
- **Evidence** `EV-013`.

### `ST-03` Signed balance is the canonical amount; debit and credit are presentation
- **Financial** one stored amount cannot disagree with itself; a stored pair can.
- **Control** halves the fields needing protection.
- **SMEsPlus semantic** one signed company-currency amount per item, presented as debit or credit.
- **Evidence** `EV-013`.

### `ST-04` Reconciliation is pairwise between items, carrying three amounts
- **Business** settlement happens between specific obligations, not between totals.
- **Financial** the three amounts are exactly what makes the exchange difference computable.
- **Control** pairwise records are auditable; net positions are not.
- **SMEsPlus semantic** a settlement fact links two financial facts.
- **Evidence** `EV-014`.

### `ST-05` One dated measurement series; valuation bases derived from it
- **Financial** a closing rate is a *selection rule* over measurements, not a second measurement.
- **Control** one fact to govern rather than four to reconcile.
- **SMEsPlus semantic** rates are stored once per date; current, closing, historical and average are derivations.
- **Evidence** `COR-10` — established only after the challenge unit corrected this session's own claim.

### `ST-06` Liquidity accounts are never shared across companies
- **Business** a bank account belongs to one legal entity.
- **Evidence** `EV-019`.

### `ST-07` Closing has data preconditions the ledger enforces
- **Business** a close that can be declared over incomplete data is not a close.
- **Control** turns closing from a typed date into a state the data must earn.
- **SMEsPlus semantic** a close is refused, with a route to the offending records, while drafts, unreconciled bank items, or unsecured entries remain.
- **Evidence** `EV-008`, `EV-019` — the single best control pattern found in Wave A.

### `ST-08` The irreversible lock is monotonic and cascades
- **Control** an irreversible control that can be walked back is not irreversible.
- **SMEsPlus semantic** adopt monotonicity; the cascade is subject to decision `CL-05`.
- **Evidence** `EV-008`.

### `ST-09` Correction of a posted fact is additive
- **Financial** a withdrawn fact is itself a fact.
- **Control** an additive correction leaves both states visible.
- **SMEsPlus semantic** reversal plus re-entry, with an explicit link between them — which the reference does **not** provide.
- **Evidence** `EV-012`.

### `ST-10` Month 12 is an ordinary month close
- **Business** the Boss baseline.
- **Evidence** `EV-016` — the reference has no year-close event at all, independently corroborating the baseline.

### `ST-11` Retiring a classification blocks new posting
- **Evidence** `COR-03`.

---

## EXTEND — adopt the intent, strengthen the mechanism

### `ST-12` Immutability is unconditional
- **Reason** in the reference it is two opt-in switches, defaulting off, fixed at provisioning and first posting; and the guard fails open for the canonical amount field.
- **SMEsPlus semantic** a posted accounting fact is immutable as a property of the ledger — not a journal setting, not a company flag, not dependent on the calling module.
- **Evidence** `EV-011`, `COR-06`, `COR-15`, `COR-19`.

### `ST-13` Tamper-evidence covers every financial field and keys on business identity
- **Reason** the reference hash omits the transaction-currency amount, currency, tax, analytic and due date; rounds at the wrong currency's precision; and is keyed on storage row identifiers so it cannot survive migration.
- **SMEsPlus semantic** coverage is the full financial fact; the chain keys on the accounting-event identity.
- **Evidence** `CONTRA-01b`, `CONTRA-06`, `CONTRA-07`.

### `ST-14` A closed period is a record
- **Reason** the reference has only a date, so "who closed this, when, and on what basis" is unanswerable.
- **SMEsPlus semantic** a close is an event with an actor, a timestamp, a basis and a checklist result; reopening is a further event.
- **Evidence** `GAP-G01`, `EV-016`; subject to decisions `CL-01`, `CL-03`.

### `ST-15` The accounting event has identity, provenance and an idempotency key
- **Reason** their absence is the root cause of duplicate-posting exposure, the collapse of correction semantics, lost migration lineage, and the un-answerability of "what did this posting originally refer to".
- **SMEsPlus semantic** the event is the immutable unit; the entry is its representation.
- **Evidence** `GAP-B02` — **the most consequential single gap in Wave A**.

### `ST-16` Overrides are justified, time-boxed, scoped and segregated
- **Reason** the reference permits an override that applies to everyone, forever, with an optional reason, granted and revoked by one role.
- **SMEsPlus semantic** a reason is mandatory, an expiry is mandatory, scope is explicit, and granting, revoking and posting are three different authorities.
- **Evidence** `EV-021`, `COR-04`, `CONTRA-11`.

### `ST-17` Every invariant that can be enforced at storage level is
- **Reason** three of fourteen invariants are storage-owned, all per-row; the defining cross-record invariant is suppressible.
- **SMEsPlus semantic** the ledger's correctness is a property of its data, not of its write paths.
- **Evidence** `COR-07`, `CONTRA-05`; `T0-01`.

### `ST-18` Control evidence lives inside the tenant's own data
- **Evidence** `EV-011`, `SB-04`, `CONTRA-14`.

### `ST-19` Template-derived and tenant-created configuration stay distinguishable
- **Reason** the reference retains no record of which accounts came from the template, so Boss question 16 is unanswerable there.
- **Evidence** `TI-05` — **no reference answer exists; this must be invented**.

### `ST-20` Derived values are reconstructible by contract
- **Reason** residual, reconciled state, payment state, ageing and analytic lines are all stored-derived, and no reconstruction path was identified.
- **Evidence** `GAP-E03`.

### `ST-21` Settlement is bounded by the obligation
- **Evidence** `COR-09`, `CONTRA-09`; `T0-05`.

---

## REJECT — do not carry forward

### `ST-22` Re-dating a document for numbering convenience — **REJECT**
Period attribution is an accounting fact; sequence monotonicity is a presentation concern. The
reference subordinates the first to the second, and does so **even with no lock configured**. The
dependency must run the other way: the number follows the period. `COR-02`, `CONTRA-12`.

### `ST-23` Silent re-dating under lock — **REJECT as a silent behaviour**
Re-dating may be a legitimate *policy*, but it must be an explicit, recorded, per-event-class
decision that leaves the original intent visible on the posted record. In the reference the warning
is hidden once the entry is posted. `COR-02`; policy choice is decision `CL-04`.

### `ST-24` Destructive un-posting — **REJECT as a general correction path**
It deletes matching records and analytic lines silently and unrecoverably, and "Cancel" routes
through it while presenting as the safe option. `EV-012`, `CONTRA-10`.

### `ST-25` Deletion of a posted fact — **REJECT**
`EV-011`, `CONTRA-14`; `T0-03`.

### `ST-26` Destructive account merge — **REJECT**
It rewrites posted history, deletes the predecessor by direct statement past the ledger's own
deletion guards, records nothing, and cannot be undone. Replacement must be a forward-dated
succession relationship. `COR-08`, `CONTRA-03`; `T0-03`.

### `ST-27` Defaulting a missing exchange rate to 1:1 — **REJECT**
It asserts a measurement the business never agreed to and produces an entry indistinguishable from a
correct one. An unavailable measurement must halt the posting. `COR-14`, `CONTRA-08`; `T0-02`.

### `ST-28` Control suppression by caller-supplied flags — **REJECT as a pattern**
Reasonable for a general framework; unreasonable for a ledger, because the suppression leaves no
accounting trace. `COR-07`, `COR-15`, `CONTRA-13`.

### `ST-29` Configuration without a tenant dimension — **REJECT**
`COR-16`, `CONTRA-15`; `T0-04`.

### `ST-30` Identity encoded as arithmetic over identifiers — **REJECT**
`EV-020`, `COR-18`, `CONTRA-02`.

### `ST-31` Unguarded reopening — **REJECT**
Closing and reopening must not be the same authority, and reopening must leave an artefact.
`EV-008`; decision `CL-03`.

---

## UNKNOWN — evidence or decision missing

| # | Item | What is missing |
|---|---|---|
| `ST-32` | Retained earnings: posted or computed at year end | **no reference implementation either way** — `CL-02`, Boss |
| `ST-33` | Whether a control account is a distinct concept or an account type | `GAP-A01` |
| `ST-34` | Write-off policy semantics | `GAP-E01` |
| `ST-35` | Unrealised FX and revaluation posting | `GAP-H01` — a valuation mechanism exists; a posting mechanism was not found |
| `ST-36` | Effect of correcting a past rate on posted entries | `GAP-H02` |
| `ST-37` | Chart-template versioning and rollback | `GAP-S01` |
| `ST-38` | Matching history | `GAP-E02` |
| `ST-39` | Whether suppression flags are externally reachable | `GAP-C04` — **requires an executed test** |
| `ST-40` | Every Thai statutory position | `HOLD / EVIDENCE REQUIRED`, Accounting-Tax track |

---

## Counts

| Classification | Count |
|---|---|
| `ADAPT` | 11 |
| `EXTEND` | 10 |
| `REJECT` | 10 |
| `UNKNOWN` | 9 |
| **Total** | **40** |

**Ten rejections is a high proportion, and it is the honest result.** They cluster in three places:
correction semantics (`ST-24`, `ST-25`, `ST-26`), silent behaviour (`ST-22`, `ST-23`, `ST-27`), and
control ownership (`ST-28`, `ST-29`, `ST-30`, `ST-31`). Those three clusters are the substance of
what Wave A learned.
