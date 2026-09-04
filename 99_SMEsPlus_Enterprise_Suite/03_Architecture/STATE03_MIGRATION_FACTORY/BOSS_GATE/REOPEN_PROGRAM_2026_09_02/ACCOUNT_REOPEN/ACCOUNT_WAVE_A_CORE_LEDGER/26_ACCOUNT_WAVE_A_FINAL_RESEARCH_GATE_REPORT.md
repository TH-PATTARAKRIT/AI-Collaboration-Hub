# 26 — ACCOUNT WAVE A — FINAL RESEARCH GATE REPORT

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001` · Wave A — Core Ledger & Closing
Branch `research/account-wave-a-core-2026-09-04-001` · Base commit `8d2c8aa` · 2026-09-04

> **This is a research recommendation. It approves nothing, moves no gate, authorises no
> implementation, and does not start Wave B. Boss is the sole Final Approver.**

---

## 1. EXECUTIVE SUMMARY

### What was learned

Wave A studied the core ledger against primary source — a 30,000-line accounting module in a verified
Enterprise build, plus its advanced accounting, reporting, framework and Thai localization
companions. It did not study documentation.

The central result is a single sentence:

> **The reference core ledger is arithmetically consistent but not self-proving. Its correctness is a
> property of the code paths that wrote it, not of the data it holds.**

Fourteen accounting invariants were mapped. **Three are enforced by the database, and all three are
per-row checks on a single line item.** No cross-record invariant in the entire domain is enforced
below the application layer — including the defining invariant of double-entry accounting, which is
an application check with a named suppression flag.

### What changed from previous understanding

| Previously assumed | Established this Wave |
|---|---|
| The account code identifies the account | The account **record** is the identity; the code is a **per-company label**. The reference system restructured its own storage to enforce this — independently corroborating the standing Boss-approved principle |
| A journal entry is the source of truth | It is the **representation** of an accounting event — and, because no accounting-event object exists, it is also that event's only durable record. This conflation is the root cause of four separate downstream problems |
| Reconciliation is a matching state | It is **three things at once**: a stored settlement fact, a derived state, and an **emitter of new accounting events**. Unreconciling is not an undo — it posts reversals |
| A lock date prevents posting into a closed period | It **re-dates the entry instead**. And for vendor bills, the accounting date is moved **even when no lock date is configured at all** — subordinating period attribution to number sequencing |
| Year-end produces a closing entry | **There is none.** The year's result is computed **at report time**. A fiscal-year entity exists but is an optional, mutable calendar override with no state, no close and no link to any entry |
| "Secured" entries are immutable | Hashing covers four entry fields and five item fields. The **transaction-currency amount, currency, tax fields, analytic distribution and due date are neither blocked nor detected** |
| Debit and credit are the stored amounts | The **signed balance** is the canonical stored fact; debit and credit are derived from it |

### Major contradictions discovered

Fifteen, in file 20. The four that block a research gate:

| # | Contradiction |
|---|---|
| `CONTRA-08` | **A posting in a currency with no configured rate converts at 1:1, silently.** The entry balances, satisfies every constraint, and is indistinguishable from a correct one. Most likely to occur during onboarding and migration |
| `CONTRA-05` | **Debits equal credits has no storage-level enforcement and is suppressible by a flag**, while four lesser per-item rules are genuine database constraints. The control tiering is inverted relative to accounting significance |
| `CONTRA-12` | **The accounting date is not a user input.** It is moved by a lock rule and by a numbering-convenience rule that operates with no lock set. The warning is hidden once posted, so the record carries no trace |
| `CONTRA-03` / `COR-08` | **Account merge rewrites posted history**, deletes the predecessor by direct statement past the ledger's own deletion guards, records nothing, and cannot be undone |

### Major architectural consequences

1. **Separate the accounting event from the journal entry.** One separation resolves duplicate
   detection, correction semantics, period re-attribution, migration provenance, and the audit
   question "what did we recognise, as distinct from how we wrote it down". This is the single
   highest-leverage position available to SMEsPlus (`ST-15`).
2. **Enforce invariants at storage level.** The ledger's correctness must be a property of its data
   (`ST-17`).
3. **Immutability is unconditional or it is not immutability** (`ST-12`).
4. **Correction is additive, always.** Ten reference behaviours are rejected, clustering in
   correction semantics, silent behaviour, and control ownership (`ST-22` to `ST-31`).
5. **A closed period is a record, not a date** (`ST-14`).
6. **Measurement is stored once per date; valuation bases are derived** (`ST-05`).
7. **Tenancy must be a first-class boundary.** The reference model's outermost boundary is the
   company group; one configuration store has no company dimension at all (`ST-29`).

### Unresolved unknowns

Twenty-eight, in file 21. Two must be resolved before any SMEsPlus control design is finalised:

- `GAP-C04` — whether the control-suppression flags are reachable from an external interface.
  **Requires an executed test, not source reading.** It determines whether the suppression pattern is
  an internal engineering convenience or an externally reachable control bypass, and it changes the
  severity of four findings.
- `CL-02` / `ST-32` — whether retained earnings is posted or computed at year end. **No reference
  implementation exists either way.** Migration cannot state an opening equity position without it.

---

## 2. COVERAGE

Percentages are given only where a denominator and an evidence baseline exist. No progress figure is
estimated.

| Measure | Denominator | Result |
|---|---|---|
| Function coverage — semantically covered | 155 enumerated Wave A functions | **104 = 67.1%** |
| Function coverage — with a named partial gap | 155 | 41 = 26.5% |
| Evidence coverage — functions carrying a primary-source reference | 155 | **148 = 95.5%** |
| Contradiction resolution | 15 reference-system contradictions | **0 resolved = 0%** — and **none is resolvable by this session**. Each describes reference behaviour, which Wave A may only learn from. All 15 are carried into decisions |
| Self-contradiction resolution | 6 research-team claims contradicted by reviewers | **6 = 100%** — all corrected and re-verified |
| Boss questions answered from evidence | 20 required | **16 answered · 4 `UNKNOWN`** — see §5 |
| Level completion | 12 required + 4 added beyond the Asset baseline | 12 of 12 |
| Open unknowns | — | **28** |
| Failure challenges reachable | 35 tested | 24 reachable · 6 prevented · 2 detected · 3 unknown |
| Proof equations holding as stated | 7 required | **0 unconditionally** · 3 with qualification · 3 failing · 1 not provable |

**Coverage is deliberately not reported as a single number.** Evidence coverage is high (95.5%) while
semantic coverage is moderate (67.1%), and the gap between them is the finding: the weakest scopes —
Chart of Accounts at 53.8% and Currencies at 52.9% — are weak not because less was read, but because
the reference model supplies *less structure than the Boss scope assumes* (no archive, no versioning,
no control-account concept) or *no mechanism at all* (revaluation posting). Neither gap closes with
more reading. Both require Boss direction.

---

## 3. CORE FINDINGS

| Model | Finding |
|---|---|
| **Ledger semantic** | Seven facts: classification identity, accounting event, financial fact, settlement fact, measurement fact, finality declaration, provenance. The reference implements four as durable objects, implements finality as a bare date, and **does not implement provenance at all** (file 06) |
| **Accounting event** | **No accounting-event object exists.** The entry is both the representation and the only durable record. Root cause of duplicate exposure, destructive correction, lost lineage (`GAP-B02`) |
| **COA identity** | Identity is the record; the code is a per-company label; uniqueness is application-enforced and a conventional constraint is **not expressible** against the chosen storage. No archive state. No temporal validity. Merge destroys identity (files 02, 15) |
| **Journal** | A numbering and control domain, not a container. Numbering is derived from stored data by pattern, not from a counter; uniqueness is a **partial** constraint covering posted entries only (file 03) |
| **Reconciliation** | Record + derived state + emitted event, simultaneously. **Unbounded against the item it settles, in any currency configuration.** Destroyed silently by an entry-level operation (file 11) |
| **Close** | No period object; no year-end entry; close is a date moved forward; reopening is unguarded; the year's result is computed at report time. **Month 12 is procedurally identical to any other month — independently corroborating the Boss baseline** (file 12) |
| **FX** | All five chain links exist. Measurement stored once per date; valuation bases derived at query time — the right principle. **A missing rate resolves to 1:1, silently** (file 13) |
| **Immutability** | **Exactly two things are unconditionally immutable**: a hashed entry, and the hard lock's forward-only movement. Everything else is configuration, caller-dependent, or unguarded. Hash coverage is partial, precision-blind, and keyed on storage identifiers so it cannot survive migration (file 15) |
| **SaaS boundary** | **No tenant concept.** The outermost boundary is the company group. Four genuine boundary failures, the worst being a configuration store with **no company dimension at all** (file 16) |

---

## 4. DECISION REGISTER — SUMMARY

Full register in file 22. Forty decisions.

| Classification | Count | Concentration |
|---|---|---|
| `ADAPT` | 11 | identity, currency handling, pairwise settlement, close preconditions |
| `EXTEND` | 10 | immutability, tamper-evidence, close as a record, event identity, override segregation |
| `REJECT` | 10 | **correction semantics, silent behaviour, control ownership** |
| `UNKNOWN` | 9 | retained earnings, revaluation, matching history, statutory positions |

Five `Tolerance = 0` candidates are **proposed to Boss** under constitution principle 13 — this
session does not designate them: entry balance; posting without a measurement; deletion or rewrite of
a posted fact; tenant isolation; over-reconciliation.

---

## 5. THE TWENTY REQUIRED QUESTIONS

| # | Question | Answer |
|---|---|---|
| 1 | What is the canonical accounting event in SMEsPlus? | **`RECOMMENDATION`** — an event with its own identity, distinct from the entry representing it. **No such object exists in the reference**, and its absence is the root cause of four downstream problems |
| 2 | What constitutes a posted financial fact? | A signed company-currency amount with an explicit transaction currency and amount, against one classification, within a balanced entry, at an accounting date. `VERIFIED FACT` |
| 3 | Which accounting facts must become immutable? | The accounting event, the financial fact, the settlement fact, and provenance. In the reference **only two things are unconditionally immutable** |
| 4 | How must corrections occur? | **Additively — reversal plus re-entry, with an explicit link between them.** The reference's destructive path is `REJECT` (`ST-24`) |
| 5 | Relationship between source document and journal entry? | Currently **none is carried**. There is no general source reference (`GAP-B02`) |
| 6 | Is the journal entry the source of truth, or a representation? | **A representation** — and, absent an event object, also the event's only durable record. This conflation is the central architectural finding |
| 7 | Semantic role of the journal item? | The **atomic financial fact** and the **unit of settlement**. Not a child row |
| 8 | What does reconciliation mean? | **Three things simultaneously**: a stored settlement fact, a derived state, and an emitter of accounting events |
| 9 | What changes when reconciliation is partial? | Residual falls in both currencies; the item stays open; the marker becomes provisional; **ageing moves to the latest matched date**; and **nothing bounds further matches against the residual** |
| 10 | What does the lock date control? | **A range of accounting dates, per company, per lock kind — and it re-dates rather than rejects.** Not documents, not entries, not periods |
| 11 | How should reopening be governed? | **`RECOMMENDATION`** — a governed event with a distinct authority and an artefact. The reference requires neither (`ST-31`) |
| 12 | How do month close and year close differ? | **They do not.** No year-close event exists — corroborating the Boss baseline |
| 13 | How should retained earnings behave? | **`UNKNOWN` — Boss decision required.** No reference implementation exists either way (`CL-02`) |
| 14 | How should opening balance retain provenance? | **`RECOMMENDATION`** — provenance travels with the fact. The reference provides **no carrier** (`MG-01`) |
| 15 | How must company and tenant boundaries be enforced? | Company: journal-exclusive, liquidity accounts unshared. **Tenant: no concept exists**; four boundary failures identified (file 16) |
| 16 | Which COA concepts are standard template versus tenant configuration? | **`UNKNOWN` — no reference answer exists.** Once provisioned, template and tenant accounts are indistinguishable. SMEsPlus must invent this (`TI-05`) |
| 17 | How should account identity survive a code or name change? | By **not being the code**. `VERIFIED FACT` — corroborates the standing Boss principle. But merge destroys it (`CONTRA-03`) |
| 18 | How are FX realisation and revaluation distinguished? | **Realisation is caused by an event (settlement); revaluation by a date.** Only the first belongs to settlement. The reference implements the first and **has no posting mechanism for the second** |
| 19 | How can GL, TB, subledger and statements be proven consistent? | **They cannot be, as stated.** Three of seven equations fail, one is a tautology, three hold only with material qualification (file 18) |
| 20 | Which controls prevent duplicate or missing accounting events? | **None.** No event identity, no idempotency key, no completeness control (`XM-01`, `FE-01`, `FE-02`) |

**Sixteen answered from evidence. Four `UNKNOWN`** — questions 13 and 16 because no reference answer
exists, and parts of 1 and 14 because they are recommendations awaiting Boss decision.

---

## 6. GATE RECOMMENDATION

Selected from the four values defined in the execution authorisation:

# `RECOMMEND HOLD`

**This is a recommendation only. Boss makes the Final Decision.**

### Why not a stronger recommendation

The research itself is complete to the maximum available evidence. Levels 1 through 12 executed, four
Levels added beyond the Asset baseline, five independent review units, twenty corrections accepted
and re-verified, 95.5% evidence coverage. **The research work is not what is being held.**

`HOLD` is recommended because **four Wave A decisions cannot be made by research, and everything
downstream depends on them**:

| # | Blocker | Why it blocks |
|---|---|---|
| `B-01` | **`CL-02` — retained earnings posted or computed at year end** | No reference implementation exists either way. Migration cannot state an opening equity position, and the close model cannot be designed, without it |
| `B-02` | **`ST-15` — accounting event identity and idempotency** | The root cause of duplicate exposure, destructive correction and lost provenance. Every producing Wave's handoff contract depends on the answer |
| `B-03` | **`TI-05` — standard template versus tenant configuration** | Boss question 16 has **no reference answer**. The chart-of-accounts gate cannot close without it |
| `B-04` | **`GAP-C04` — external reachability of the control-suppression flags** | Requires an **executed test**. Changes the severity of four findings and the whole control design |

Three of the four are Boss decisions; the fourth is a test this session could not run.

### What this recommendation does not say

- It does **not** say the reference model is unsuitable as a learning benchmark. It taught the
  identity separation, the pairwise settlement model, the measurement/valuation separation, and the
  close-precondition pattern — four positions Wave A adopts.
- It does **not** hold any other Wave. Wave A's ledger-side contract (file 05 §2) is stable enough for
  other Waves to design against.
- It does **not** move, close, or open any Account-module gate. The gates recorded in the prior Batch
  A routing session remain exactly as they were; Wave A supplies evidence toward them and adjudicates
  none.

### Recommended next actions, for Boss direction

1. Decide `B-01`, `B-02`, `B-03`.
2. Commission the executed test for `B-04`.
3. Route the seven Thai statutory items to the Accounting-Tax track, beginning with the chain from
   the system-derived accounting date to the statutory extracts (`COR-20`).
4. Consider the five `Tolerance = 0` candidates under constitution principle 13.
5. Do **not** authorise Wave B from this package. Wave A was authorised alone.

---

## 7. TERMINAL STATE

# `ACCOUNT WAVE A — READY FOR BOSS FINAL RESEARCH GATE`

Research complete to the maximum available evidence. Material blockers remain and are named,
scoped and owned. No approval issued, no gate moved, no implementation authorised, no Wave B started.

**Boss is the sole Final Approver.**
