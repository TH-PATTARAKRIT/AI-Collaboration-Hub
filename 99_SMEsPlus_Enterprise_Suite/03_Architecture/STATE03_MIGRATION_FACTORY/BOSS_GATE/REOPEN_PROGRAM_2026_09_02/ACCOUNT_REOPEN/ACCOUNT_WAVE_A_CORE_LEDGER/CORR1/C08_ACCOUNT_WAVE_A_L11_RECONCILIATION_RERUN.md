# C08 — LEVEL 11 RECONCILIATION PROOF — RE-RUN

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001` · **supersedes parent file `18`**

Re-run after all 20 corrections. The governing instruction for this round:

> **Mathematical balance is not semantic correctness.**

Accordingly this re-run has two parts: the seven equations, and an explicit
**`BALANCED BUT WRONG`** register — entries that satisfy every equation while being economically or
legally incorrect.

Status: `HOLDS` · `HOLDS WITH QUALIFICATION` · `DOES NOT HOLD AS STATED` · `NOT PROVABLE`.

---

## PART 1 — THE SEVEN EQUATIONS, RE-RUN

### `P-01` — `Debit = Credit` — **`DOES NOT HOLD AS STATED`** *(unchanged; basis strengthened)*

The invariant is a suppressible application check with no database constraint (`COR-07`), while four
lesser per-item rules **are** genuine constraints. Reachability of the suppression path from outside
the application remains open (`GAP-C04`).

**Change from the parent:** none in verdict. The tiering argument is now the evidence, not the
observation.

### `P-02` — `GL → Trial Balance` — **`HOLDS WITH QUALIFICATION`** *(qualification strengthened)*

Arithmetically sound. Qualifications: a merge deletes the predecessor account **by direct statement
past the ORM's guards and records nothing** (`COR-08`), so a prior-period trial balance is not
reproducible and **no artefact reveals why**; no temporal validity on accounts, so a type change
restates prior classification; off-balance exclusion untraced (`WAVE-G`).

### `P-03` — `Opening + Movements = Closing` — **`HOLDS WITH QUALIFICATION`** *(materially worse)*

The arithmetic holds. **The periods it is stated over are less stable than the parent reported.**

Previously: period membership was said to be unstable *under lock*. Corrected: for non-sale documents
the accounting date is derived **unconditionally, with no lock configured** (`C07`), and in the
ordinary case is not the document date. Period membership is therefore unstable **by default**, in
every tenant, whether or not any close discipline exists.

Also: a fiscal-year *calendar* record exists but is fully mutable and deletable (`NC-01`), so the
boundaries this equation is stated over can themselves be edited or removed.

### `P-04` — `Subledger ↔ Control Account` — **`NOT PROVABLE`** *(unchanged)*

There is one set of items; the subledger is a view over it. The two sides cannot disagree, so the
check is a tautology yielding no assurance. Recommendation unchanged: keep the single-record model
(`ADAPT`); do not manufacture a break in order to check for it. Assurance must come from `P-06` and
from provenance.

### `P-05` — `Journal Entries ↔ Journal Items` — **`HOLDS WITH QUALIFICATION`** *(unchanged)*

Analytic lines are not items — they are a derived subledger destroyed on un-post and regenerated only
from a stored distribution.

### `P-06` — `Reconciled + Residual = Original Open Item` — **`DOES NOT HOLD AS STATED`** *(scope widened)*

The reconciliation model declares **zero** database constraints (`COR-09`). Over-reconciliation is
structurally reachable in **any** currency configuration — the parent framed it as multi-currency.
Residual and the reconciled flag are stored-derived with **no identified reconstruction path**
(`GAP-E03`), and matching records are deleted silently when an entry is reset to draft.

### `P-07` — `Company Currency ↔ Transaction Currency` — **sign `HOLDS`; magnitude `DOES NOT HOLD`** *(materially worse)*

Sign agreement is a genuine database constraint. Magnitude is unconstrained; on a secured entry it is
neither guarded nor detected (`CONTRA-01b`); the hash rounds company-currency amounts at the
**foreign** currency's precision (`COR-11`).

**And the corrected FX evidence makes this the worst equation in the set:** where a currency has no
rate rows — **the shipped default state** — the relationship between the two amounts is `× 1.0`, and
the resulting entry satisfies the sign constraint, balances, posts, hashes and reconciles (`C06`).

---

## PART 2 — `BALANCED BUT WRONG` REGISTER

Entries that satisfy every equation above while being economically or legally incorrect. This is the
required output of the re-run and it is where the domain's real risk lives.

| # | Case | How it arises | Controls it satisfies | Detectable? | Evidence |
|---|---|---|---|---|---|
| `BW-01` | **Wrong FX — par valuation** | Currency has no rate rows (shipped default). Every item on the entry takes the same 1.0 factor | balance; sign constraint; numbering; hash; reconciliation; trial balance | **No forward signal.** Retrospective only, when the recomputed rate stops agreeing with stored amounts | `C06` |
| `BW-02` | **Wrong period — derived date** | Non-sale document re-dated to end-of-month or today, with no lock configured | every control — the date is *supposed* to be derived | **No.** The warning is hidden once posted and the intended date is never stored | `C07` |
| `BW-03` | **Wrong period — generated consequence relocated** | Exchange or cash-basis entry whose natural date is locked is dated today, possibly in another year | every control | Partially — the origin link survives, so the discrepancy is reconstructible | `EV-015`, `COR-17` |
| `BW-04` | **Wrong account — retroactive merge** | Posted items retargeted to a surviving account; predecessor deleted; nothing recorded | every control | **No.** No artefact exists | `COR-08` |
| `BW-05` | **Wrong classification — retroactive type change** | An account's type is changed; no temporal validity exists, so prior periods restate | every control | Partially — the field change is tracked, but prior reports are not marked | `NC-08` |
| `BW-06` | **Duplicate event — machine-generated** | A producer retries; a second valid entry is created. The duplicate-reference control covers only sale and purchase documents and matches on a reference string | every control | **Only for sale/purchase documents with a matching reference**, and then only as a warning that suppresses auto-post | `NC-13` |
| `BW-07` | **Over-settlement** | Matches exceeding an item's residual; nothing bounds them | balance; sign; trial balance | Partially — a negative residual is visible if anyone looks | `COR-09` |
| `BW-08` | **Broken source linkage** | The source document is modified or deleted after posting; no general reference ties the two | every control | **No** general mechanism; typed origin links exist only for specific generated entries | `NC-05` |
| `BW-09` | **Silent tamper on a secured entry** | Transaction-currency magnitude, currency, tax or analytic fields edited on a hashed entry | every control **including the integrity report** | **No** | `CONTRA-01b` |
| `BW-10` | **Hash collision** | Two materially different company-currency amounts serialise identically because rounding uses the foreign currency's precision | every control including the integrity report | **No** | `COR-11` |
| `BW-11` | **Unbalanced entry stored** | The balance check is suppressed on the write path | numbering; hash; item-level constraints | **Yes** — a proof over stored data would catch it. The reference performs no such proof | `COR-07` |
| `BW-12` | **Wrong company / cross-tenant control state** | A configuration value with no company dimension changes a numbering control for every tenant in a shared database | every control | **No** | `COR-16` |

### What the register shows

**Eleven of twelve cases satisfy the full equation set.** Only `BW-11` is detectable by an
independent proof over stored data — and the reference model does not perform one.

> The seven equations are therefore **necessary and radically insufficient**. A ledger can satisfy
> every one of them and still be wrong about valuation, period, account, classification, uniqueness,
> settlement, lineage and integrity.

---

## PART 3 — CORE LEDGER READINESS, RE-ASSESSED

| Measure | Parent | Re-run |
|---|---|---|
| Equations holding unconditionally | 0 of 7 | **0 of 7** |
| Holding with qualification | 3 | 3 — but `P-03` and `P-07` are **materially worse** |
| Failing as stated | 3 | 3 |
| Not provable | 1 | 1 |
| `BALANCED BUT WRONG` cases | not assessed | **12 identified; 11 undetectable by the equation set** |

**The re-run's conclusion is stronger and more negative than the parent's**, and it is a different
conclusion in kind:

> The parent found that the ledger's correctness is a property of its write paths rather than of its
> data. The re-run finds that **even a ledger whose write paths behaved perfectly would still satisfy
> all seven equations while being wrong**, because the equations test internal consistency and the
> failures are failures of *external correspondence* — to a real exchange rate, a real period, a real
> account, a real distinct event, a real source document.

### Proposed readiness criterion for SMEsPlus

Wave A's proposed definition of an auditable ledger, revised by this re-run:

1. **Every equation provable from stored data alone**, independently of the code that wrote it —
   unchanged from the parent.
2. **Plus: every fact traceable to an external correspondent.** A valuation to a measurement the
   business agreed; a period to a date the business asserted; a posting to a distinct source event; a
   classification to a state that existed at the time.

Criterion 1 addresses `BW-11`. **Criterion 2 addresses the other eleven**, and it cannot be satisfied
by constraints alone — it requires the accounting-event identity and provenance carriers that Wave A
found absent (`ST-15`, `NC-05`).

`RECOMMENDATION:` this two-part criterion should replace the single-part criterion proposed in the
parent package, and should be the standard the eventual readiness gate applies.

---

## CHECKPOINT — L11 RE-RUN

| Item | Record |
|---|---|
| Scope completed | Seven equations re-run after 20 corrections; 12 `BALANCED BUT WRONG` cases identified; readiness criterion revised |
| Verified findings | `P-03` and `P-07` materially worse than the parent stated; 11 of 12 wrongness cases satisfy the full equation set |
| Contradictions | none new; existing contradictions surface here as proof failures |
| Unknowns | `GAP-C04` (suppression reachability), `GAP-E03` (reconstruction path), `FXU-04` (subsidiary rate visibility) |
| Risks | Internal consistency is being mistaken for correctness — the central risk of the domain |
| Next | Fresh L12 adversarial review, then CORR1 gate |

`CHECKPOINT RECORDED — CONTINUING.` Not Boss approval.
