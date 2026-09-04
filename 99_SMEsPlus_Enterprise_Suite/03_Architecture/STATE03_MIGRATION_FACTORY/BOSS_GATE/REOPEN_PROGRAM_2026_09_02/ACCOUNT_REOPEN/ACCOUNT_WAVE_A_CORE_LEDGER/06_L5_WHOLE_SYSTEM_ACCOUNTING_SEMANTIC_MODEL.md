> **CORR1 CORRECTION NOTICE.** Amended by session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`.
> Corrections landing here: `COR-01, COR-02, COR-10`. Governing text where they conflict with the body below: CORR1/C04; CORR1/C07.
> Prior findings are retained unedited for lineage; see `CORR1/C02_..._ACCEPTED_CORRECTIONS_REGISTER.md`.

# 06 — LEVEL 5: WHOLE-SYSTEM ACCOUNTING SEMANTIC MODEL

Layer 1 clean-room · cites `EV-0NN` and `COR-0N` · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

At this Level the menus are set aside. The domain is reconstructed from financial facts alone.

---

## 1. The seven facts

Everything in Wave A reduces to seven facts. Each has exactly one owner, one lifetime, and one
rule about change.

| # | Fact | What it asserts | Owner | Lifetime | May it change? |
|---|---|---|---|---|---|
| `F1` | **Classification identity** | this bucket exists and means this | configuration | indefinite, longer than any label it wears | its labels may; its identity must not |
| `F2` | **Accounting event** | the business recognised something, on this date, for this amount, against these classifications | the ledger | permanent from the moment of recognition | **never** |
| `F3` | **Financial fact** (the item) | this signed amount, in this currency, belongs to this classification | the accounting event that carries it | as long as its event | **never** |
| `F4` | **Settlement fact** | this much of that obligation has been discharged, by this counter-fact, on this date | the matching record | permanent | **never** — it is undone by a new fact, not by erasure |
| `F5` | **Measurement fact** | this rate applied on this date | the rate table | permanent per date | may be corrected, but the correction is itself dated |
| `F6` | **Finality declaration** | this period is no longer open | governance | permanent once hard | soft ones may move; hard ones may only advance |
| `F7` | **Provenance** | this fact came from there, by this route | the producer | as long as the fact | **never** |

Facts `F2`, `F3`, `F4` and `F7` are immutable. `F1`, `F5` and `F6` are governed.

**The reference model implements four of these seven as durable objects** (`F1`, `F2`+`F3` together,
`F4`, `F5`). It implements `F6` as a bare date with no object behind it (`EV-016`, `COR-01`), and it
does not implement `F7` at all (`EV-017`, `GAP-B02`). Those two absences are the largest structural
findings of this Wave.

---

## 2. Source of truth — resolved

The Wave A question "is the journal entry the source of truth, or the accounting representation of
another fact?" resolves as follows, from evidence rather than convention.

**The journal entry is the accounting representation of an accounting event — and in the reference
model it is also, in practice, the event's only durable record.** There is no separate accounting-event
object. The consequences are visible throughout the evidence:

- the number, the date, the lock, the hash and the reversal all attach to the *entry*, not to an
  event behind it (`EV-005`, `EV-009`, `EV-010`, `EV-012`);
- a producing module's business event has no identity of its own once posted (`GAP-B02`), so the same
  business event posted twice produces two equally valid entries and nothing detects it (`XM-01`);
- because there is no event object, "correcting the event" and "editing its representation" collapse
  into the same operation — which is exactly why the destructive correction path exists (`EV-012`).

`RECOMMENDATION — the single most consequential design position in this Wave.` SMEsPlus should
separate the **accounting event** from the **journal entry that represents it**. The event carries
identity, provenance, source reference and idempotency key; the entry carries presentation, numbering
and period placement. This one separation resolves five otherwise independent problems at once:
duplicate detection, correction semantics, period re-attribution, migration provenance, and the
audit question "what did we recognise, as distinct from how we wrote it down".

This is offered as a `RECOMMENDATION`, not a decision. It is a Boss-level architectural position.

---

## 3. Mutable, immutable, derived — the classification

| Element | Class | Evidence | Note |
|---|---|---|---|
| Account identity | immutable | `EV-001` | but destroyed by merge — `COR-08` |
| Account code, name, tags, notes | mutable metadata | `EV-001` | per-company for the code |
| Account type | governed | `EV-016` | changes reporting behaviour retroactively |
| Entry existence and amounts | **immutable** | `EV-022` | in the reference: frozen by an application guard with a documented bypass |
| Entry number | immutable once assigned | `EV-006` | uniqueness asserted only at posting |
| Entry accounting date | **system-derived, not user input** | `COR-02` | moved by a lock rule *and* by a numbering-convenience rule |
| Entry document date | source fact | `COR-02` | the only date the user actually owns |
| Entry reference, narration | mutable metadata | `EV-022` | writable even when posted |
| Item balance | **the canonical financial fact** | `EV-013` | debit and credit are derived from it |
| Item transaction currency and amount | financial fact | `EV-013` | sign is DB-constrained against balance; magnitude is not (`COR-06`) |
| Item analytic distribution | **intent** | `EV-012` | the attribution the user meant |
| Analytic lines | **derived, destructible** | `EV-012` | deleted on un-post, regenerated on repost |
| Matching record | settlement fact | `EV-014` | unconstrained against the item it matches (`COR-09`) |
| Residual, reconciled, matching marker, payment state | **derived, stored** | `EV-014` | capable of drifting from their inputs |
| Current-year earnings | **derived, never stored** | `EV-016` | computed at report time |
| Lock dates | governance state | `EV-008` | |
| Fiscal year record | **calendar override, fully mutable** | `COR-01` | no state, no close, no link to any entry |

The recurring pattern: **the reference model stores many derived values and persists almost no
provenance.** Every stored-computed value is a reconciliation risk; every absent provenance carrier
is an audit gap.

---

## 4. Temporal semantics

Wave A found **no temporal validity model anywhere**: no effective dating on accounts or journals, no
versioning, no period entity carrying state. The complete temporal apparatus is:

1. one accounting date per entry — system-derived (`COR-02`);
2. one document date per document — user-owned;
3. one due date per item;
4. one maximum-match date per settlement, used for ageing (`EV-014`);
5. five lock dates per company, one of them monotonic (`EV-008`);
6. one rate per currency per day per company group (`EV-018`);
7. optionally, named non-overlapping fiscal-year records used only to derive boundaries (`COR-01`).

**Consequence.** The question "what did this account mean on that date?" is unanswerable. A chart
reorganisation, a type change, or a merge applies retroactively to all history. For SMEsPlus,
comparative reporting across a chart change has no support in this model.

---

## 5. Dimensional semantics

Three dimensions ride on the item and are of three different kinds:

| Dimension | Kind | Consequence |
|---|---|---|
| Account | **structural** — the item cannot exist without it | DB-enforced (`COR-07`) |
| Counterparty | **relational** — required only where a subledger is involved | hash-covered at item level |
| Analytic | **derived from intent** — stored as a distribution, expanded into a subledger | the subledger is destroyed by an ordinary correction (`EV-012`) |
| Tax | **computed** — driven by an engine, materialised as items | outside hash coverage (`COR-06`); Wave D |

Only the first is protected at storage level. `INFERENCE:` SMEsPlus should decide, per dimension,
whether it is a *fact* (immutable, part of the event) or an *attribution* (restatable). The reference
model never makes that distinction explicit, which is why analytic attribution can be silently
destroyed while the account cannot.

---

## 6. Tenancy and company boundary

| Boundary | Reference position | Evidence |
|---|---|---|
| Journal → company | strict, one only | `EV-006` |
| Entry → company | strict, via journal | `EV-006` |
| Account → company | **many-to-many**, with per-company codes | `EV-001` |
| Liquidity account → company | strict, sharing refused | `EV-019` |
| Lock date → company | per company, with the hard lock cascading down the parent chain | `EV-008` |
| Currency rate → company | per company **group** (root), not per company | `EV-018` |
| Fiscal year → company | **root companies only**; child companies refused | `COR-01` |
| Tenant | **no tenant concept exists** | `EV-020` |

The last row is the important one. The reference model's outermost boundary is the *company group*,
not a tenant. Several structures are keyed to the root company — codes, rates, fiscal years — which
means that in a deployment where many tenants share one database, those structures are shared at
exactly the level SMEsPlus would need to keep separate. Detail in file 16.

---

## 7. Correction semantics — the resolved position

From `EV-012`, `EV-022` and `COR-02`, three correction routes exist in the reference model:

| Route | What it does | Destroys | Verdict for SMEsPlus |
|---|---|---|---|
| Edit while draft | changes the entry before it is a fact | nothing | `ADAPT` |
| Un-post, edit, re-post | retracts the fact, changes it, re-asserts it | **matching history and analytic lines, silently and unrecoverably** | `REJECT` as a general path |
| Reverse and re-enter | adds a counter-fact, then a corrected fact | nothing | `ADAPT` — this must be the default |

**Resolved principle.** Once an accounting event exists, it is corrected only by further accounting
events. The reference model offers a destructive alternative and makes it the convenient one; that
convenience is the defect.

---

## 8. The model in one statement

> A **classification identity** is given meaning by configuration. A **producer** recognises a
> business event and hands the ledger an **accounting event**, which the ledger records as an
> **entry** carrying **financial facts** — signed amounts in stated currencies against
> classifications, with attributions. Facts are permanent. Obligations they create are discharged by
> **settlement facts**, which may themselves emit further accounting events where measurement has
> moved. **Measurement** is dated and never retroactive. **Finality** is declared over date ranges by
> governance, and once hard is irreversible. Everything else — balances, residuals, ageing, results,
> current-year earnings — is **derived and must be reconstructible from the facts alone**.

Every clause is evidence-backed. The two clauses the reference model does **not** implement are
"hands the ledger an accounting event" (there is no event object — `GAP-B02`) and "facts are
permanent" (immutability is configuration — `EV-011`, `COR-07`).

---

## CHECKPOINT L5

| Item | Record |
|---|---|
| Scope completed | Seven-fact model; source-of-truth resolved; mutability classification; temporal, dimensional and tenancy semantics; correction semantics |
| Evidence inspected | `EV-001`–`EV-023`, `COR-01`–`COR-09` |
| Verified findings | The entry is the representation *and* the only durable record of the event; there is no temporal validity model; the outermost reference boundary is the company group, not a tenant; stored-derived values are pervasive and provenance is absent |
| Contradictions | Carried: `CONTRA-01a`/`01b`, `CONTRA-02`, `CONTRA-03`, `CONTRA-04`; new `CONTRA-05` (entry balance invariant switchable) from `COR-07` |
| Unknowns | Whether any reference mechanism reconstructs stored-derived settlement values after drift (`GAP-E03`) |
| Risks | The absence of an accounting-event identity is the root cause of four separate downstream problems |
| Expert disagreements | Two expert reviews returned and produced nine accepted corrections; recorded in `E01` and file 23 |
| Audit challenges | Challenge unit running against the evidence base |
| Next research target | Level 6 — contradiction, failure and edge case |

`CHECKPOINT L5 RECORDED — CONTINUING AUTOMATICALLY.` Not Boss approval.
