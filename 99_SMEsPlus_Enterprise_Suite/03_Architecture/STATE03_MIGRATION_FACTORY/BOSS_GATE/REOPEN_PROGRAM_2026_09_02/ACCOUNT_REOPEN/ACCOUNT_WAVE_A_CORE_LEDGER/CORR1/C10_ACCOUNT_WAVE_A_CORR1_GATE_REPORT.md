# C10 — ACCOUNT_WAVE_A_CORR1_GATE_REPORT

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001` · **supersedes parent file `26`**
Wave A — Core Ledger & Closing · 2026-09-04

---

## 1. Executive summary

### What was learned

The reference core ledger is **arithmetically consistent and not self-proving**. Its correctness is a
property of the code paths that wrote it, not of the data it holds. Three of seven required proof
equations fail as stated, one is a tautology, and **fifteen distinct "balanced but wrong" cases** were
identified — of which **thirteen are undetectable by the equation set**.

Beneath that sit two structural absences that explain most individual findings: there is **no
accounting-event identity distinct from the journal entry**, and **no general provenance carrier**.
Between them they account for duplicate exposure, the collapse of "correct the event" into "edit the
entry", lost migration lineage, and the impossibility of asking what a posting originally referred to.

### What changed from the previous understanding

| | Parent gate | Now |
|---|---|---|
| Fiscal year | claimed absent | exists as a mutable calendar override — **close finding strengthened** |
| Rate types | claimed absent | derived at query time — **becomes a pattern to adopt** |
| Accounting date | re-dated under lock | **system-derived; one path needs no lock at all** |
| Entry balance | assumed enforced | suppressible, **and externally addressable** |
| Missing FX rate | not identified | **converts at par, from the shipped default state, with no detection for invoices and bills** |
| Immutability | two unconditional | two — a claimed third is a ratchet that by default locks protection **off** |

### Major contradictions discovered

`CONTRA-01a`/`01b` partial hash coverage · `CONTRA-05` suppressible balance invariant ·
`CONTRA-06` hash precision collision · `CONTRA-07` hash keyed on storage identity ·
`CONTRA-08` par FX conversion · `CONTRA-09` unbounded reconciliation ·
`CONTRA-11` unsegregated override · `CONTRA-12` derived accounting date ·
`CONTRA-13` caller-owned posted freeze · `CONTRA-14` deletion protection defaults off, permanently.

### Major architectural consequences

1. Separate the **accounting event** from the entry that represents it.
2. Enforce invariants at **storage level**; never as a request parameter.
3. Correction is **additive, always**.
4. Store measurement **once per date**; derive valuation bases.
5. Provenance travels **with the fact**, permanently.
6. Tamper-evidence keys on **business identity**, so it survives migration.

### Unresolved unknowns

Four material items (`FX-08`, `SB-05`, `FX-07`, `B-05`), two of them **cross-tenant integrity**.
Seven Thai statutory items, all `HOLD`, all routed to `WAVE-D TAX`.

---

## 2. Coverage

Percentages are given only where a denominator and an evidence baseline exist.

| Measure | Value | Denominator |
|---|---|---|
| Function coverage — semantically covered | **67.1%** (104 of 155) | the enumerated Wave A scope A–H |
| Evidence coverage | **95.5%** (148 of 155) | as above; the 7 without are findings of absence, each reported with its search scope |
| Reviewer claims verified in whole or material part | **81.5%** (22 of 27) | fresh L12 claims |
| Contradiction resolution | **100%** (16 of 16) resolved or explicitly bounded | the contradiction register |
| Vetoes resolved | **2 of 2** | neither invalidates the model |
| Negatives rescoped | **9** over-scoped negatives corrected | 38 absolute phrasings scanned |
| Unknown count | **31** open items | `C13` §6 plus the gap register |

No progress percentage is offered for anything without an enumerable denominator.

---

## 3. Core findings

| Model | Position |
|---|---|
| **Ledger semantic** | Seven facts; four immutable. Entry = representation **and** sole durable record of an event |
| **Accounting event** | **No identity exists.** Root cause of four downstream findings |
| **COA identity** | Identity is the record, not the code; codes are per-company. **Destroyed by a merge that bypasses the ORM's own guards** |
| **Journal** | A numbering and control domain. Numbering derived from data, not a counter; uniqueness only for posted entries |
| **Reconciliation** | Record + derived state + **emitted accounting event**. Unbounded against the item it settles |
| **Close** | A date, not an object. No closing entry, no closer, no basis. Month 12 identical to any month — **corroborates the Boss baseline** |
| **FX** | Storage one measurement per date; valuation bases derived — **a good pattern**. Undermined by a par fallback reachable from the shipped state |
| **Immutability** | Two things unconditional: a hashed entry and the hard lock's forward-only movement. Everything else is configuration |
| **SaaS boundary** | **No tenant concept.** Outermost boundary is the company group, and in places the **database** |

---

## 4. Decision register — summary

| Class | Count | Examples |
|---|---|---|
| `ADAPT` | 14 | transaction currency always explicit; pairwise matching with three amounts; hard-lock preconditions; single-record subledger; measurement stored once |
| `EXTEND` | 12 | storage-level invariants; full hash coverage keyed on business identity; event identity and provenance; tax point; closed period as a record; template-vs-tenant distinction |
| `REJECT` | 8 | par FX conversion; silent re-dating; numbering-driven period attribution; destructive un-posting; account merge; deletion of a posted fact; caller-suppressible controls; database-wide configuration |
| `UNKNOWN` | 6 | retained earnings treatment; closed-period record; reopening authority; late-document policy; hard-lock cascade; write-off policy |

**No `ADAPT` or `EXTEND` was classified because the reference implements it.** Every one carries a
business, financial or control reason.

---

## 5. Answers to the twenty required questions

Condensed; full text in the parent gate report as corrected by `C02`–`C13`.

1–4 Canonical event: **no such identity exists in the reference** — SMEsPlus must create it. A posted
financial fact is `state = posted`, but immutability is configuration. Amounts, account, counterparty,
currency, period and identity **must** become immutable. Corrections **must** be additive.
5–7 Source document → entry has no general carrier. The entry is the **representation** and, in
practice, the only durable record. The item is the **atomic financial fact**, its balance canonical.
8–9 Reconciliation is record + derived state + emitted event. Partial: residual falls, item stays
open, ageing moves to the latest matched date, **nothing bounds further matches**.
10–12 A lock controls **a range of accounting dates**, and **re-dates rather than rejects**.
Reopening requires no distinct authority and leaves no artefact. Month and year close are procedurally
identical.
13–14 Retained earnings: **`UNKNOWN`** — no reference implementation exists either way; Boss decision
`CL-02`. Opening balances have **no provenance carrier**.
15–16 Company boundary is enforced for journals, entries and liquidity accounts; **tenant boundary
does not exist**, and some structures are database-wide. The standard-versus-tenant template
distinction **has no reference answer** and must be invented.
17 Account identity survives code and name change by design — **and is destroyed by merge**.
18 Realisation is caused by an **event**; revaluation by a **date**. A revaluation mechanism exists in
the reporting module.
19 **They cannot be proven consistent today** — see `C12`. Proposed three-part readiness criterion.
20 A duplicate-**reference** warning exists for sale and purchase documents; it does not block, does
not cover machine-generated entries, and no completeness control was found.

---

## 6. Gate recommendation

> # `RECOMMEND HOLD`

**This is a recommendation only. Boss is the sole Final Approver.**

### Scope of the hold — four named items, not the body of work

| # | Item | Class | Why it blocks |
|---|---|---|---|
| `SB-05` | A null-company exchange rate may re-measure **another tenant's** postings | `PARTIALLY VERIFIED` | Cross-tenant data integrity. Constitution principle 13 designates tenant-isolation failures as candidate `Tolerance = 0`. This cannot be left open through a gate |
| `FX-08` | Branch-level rates invisible to a root-scoped resolver — a tenant believes rates are loaded while conversion uses par | `PARTIALLY VERIFIED` | Combines with `SF-01`, the Wave's most severe finding, and is cheap to close |
| `FX-07` | The revaluation mechanism may inherit the par fallback | `NOT PROVEN` | The compensating control for `SF-01` may itself be contaminated |
| `B-05` | An approval engine may exist and be skipped under privilege elevation | `NOT PROVEN` | Would change the maker-checker conclusion and interacts with `C09` |

Each is closable by a short, targeted search. None requires new access.

### Why `HOLD` and not `CONDITIONAL PASS`

Two of the four concern **cross-tenant integrity**, which this project treats as `Tolerance = 0`
territory. A conditional pass would carry an unverified cross-tenant integrity question forward into
design. That is the one class of item this programme's own constitution says must not pass.

### Why `HOLD` and not `FAIL`

The semantic model **survived two independent adversarial rounds without a single substantive
contradiction**. No veto invalidated it. 22 of 27 fresh reviewer claims were verified and folded in.
The research is materially complete and, on the evidence, deeper than the Asset benchmark it was
required to match. The four open items sharpen severities and close scopes; **none would change a
decision in the transfer register.**

### What the hold is not

It is **not** a judgement that the work is unsound, and **not** a request to redo it. Everything
except the four named items is ready for the Boss Final Research Gate.

---

## 7. Governance findings for Boss attention

1. **Over-scoped negatives are this programme's recurring defect.** Nine were found across the Wave —
   and **three were authored by CORR1 itself, after it wrote the standard prohibiting them.** The
   defect is not ignorance of the rule.
2. **Only independent review has ever caught them.** Twice, in two rounds. `DR-NC-05` should be
   operated as a **named, separately-tasked audit step**, not as an expectation on authors.
3. **Positive and negative findings should be weighted differently at gates.** Positives that survive
   re-verification are the stronger class; negatives are the weaker and should be re-scoped before
   reliance.
4. **Five `Tolerance = 0` candidates are proposed** — `T0-01` entry balance, `T0-02` posting without
   a measurement, `T0-03` deletion or rewrite of a posted fact, `T0-04` tenant isolation,
   `T0-05` over-reconciliation. Only Boss may designate.

---

## 8. Terminal state

> ## `ACCOUNT WAVE A — HOLD, WITH EXACT EVIDENCE`
>
> Four named items block; all are `PARTIALLY VERIFIED` or `NOT PROVEN`, and two concern cross-tenant
> integrity. The remainder of Wave A is **ready for the Boss Final Research Gate**.

**Not declared:** final approved · final freeze · Wave A closed · any gate movement · any
implementation authorisation. **Wave B has not started.**
