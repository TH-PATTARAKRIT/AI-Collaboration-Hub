# 04 — BOSS DECISION INCORPORATION

**LAYER 2 — AUDIT QUARANTINE.**

Purpose: record exactly what each Boss decision changes in the architecture, what it
does **not** decide, and where evidence agrees with it, is silent on it, or pulls
against it. A decision that is merely restated has not been incorporated.

---

## `BD-01` — Continuous internal equipment usage accumulation

> Internal equipment usage accumulation may be lower than, equal to, or higher than
> residual book value. No cap. No automatic cut-off. No reduction of residual book
> value from internal usage allocation. Usage may continue while the equipment
> remains operationally eligible for production use. It is a management/control
> allocation concept and must not silently alter statutory depreciation, asset book
> value, financial-statement carrying amount or accumulated depreciation unless
> separately authorised by a valid accounting event.

### What it decides

1. The accumulator is **unbounded in amount**. The bound is a **state**, not a number:
   operational eligibility for production use.
2. The management ledger is a **separate truth** from the financial sub-ledger. It
   reads from it; it never writes back.

### What the evidence says

| Point | Evidence | Class |
|---|---|---|
| The financial residual is excluded from depreciation and protected for the whole running life | Baseline `18`, re-confirmed | `FACT VERIFIED` |
| Nothing in the reference product implements, constrains or even represents a post-depreciation usage accumulator | Exhaustive negative across 797 modules | `FACT VERIFIED` (workspace-bounded) |
| Nothing in TAS 2 or TAS 16 constrains a memorandum accumulator | Standard texts obtained this session | `FACT VERIFIED` — by silence, and silence is the correct reading here: neither standard addresses management accounting |
| Off-balance amounts have no statutory presentation surface | `03` `BLK-04` | `FACT VERIFIED` |
| The platform structurally forbids an entry that mixes off-balance and on-balance lines | `05` §7 | `FACT VERIFIED` |

### Incorporated as

- `19` §6 defines the internal-usage ledger as a **closed off-balance double-entry
  ledger** with no line ever touching an on-balance account. The last two evidence
  rows make this enforceable structurally rather than by policy, which is the
  precedent the baseline recommended following.
- `10` defines the rate base, the effective date, the correction path and the
  disposal path.

### What `BD-01` does **not** decide, and this session does not invent

1. **The rate base.** `BD-01` says the accumulator is unbounded; it does not say what
   accrues into it per day. The baseline's candidate — residual ÷ original lifetime
   days — is carried as a **DESIGN CANDIDATE** in `10` §3, with two alternatives and
   their consequences, for Boss selection.
2. **What happens on re-entry.** A fully depreciated asset can be made depreciable
   again by a capital improvement. `BD-01` is silent. `10` §7 proposes a rule and
   marks it a candidate.
3. **What happens at disposal.** The financial residual does not survive disposal as
   an identifiable amount. `10` §6 proposes closing the accumulator at disposal with
   a terminal memorandum entry, and marks it a candidate.

### Tension found — one, and it is mild

`BD-01` says usage "must not silently alter" statutory figures. The word doing the
work is **silently**. The evidence supports a stronger form and SMEsPlus should adopt
it: the management ledger must not alter statutory figures **at all**, silently or
otherwise, because the platform makes the stronger form free. Recorded in `17` as
`CTR-C-01` at Low severity — it strengthens the decision rather than opposing it.

---

## `BD-02` — 100% depreciation attribution

> Every depreciation period must be attributed 100%. No depreciation amount may
> remain permanently unclassified. Productive depreciation flows Operation →
> Manufacturing Order → WIP → Finished Goods → subsequent cost recognition.
> Non-productive depreciation is assigned by cause: MAINTENANCE, BREAKDOWN, IDLE,
> NO_DEMAND, SETUP, STOPPAGE, OTHER. Unclassified depreciation is not carried forward.

### What it decides

1. A **reconciliation identity** that every period must satisfy:
   `Total period depreciation = Productive allocation + Non-productive allocation`,
   with zero unexplained balance.
2. Non-productive depreciation is **classified**, not pooled.
3. Nothing rolls forward.

### What the evidence says

| Point | Evidence | Class |
|---|---|---|
| Unallocated production overhead is recognised as an expense in the period incurred | TAS 2 ¶13, standard text | `FACT VERIFIED` — the standard and `BD-02` reach the same destination independently |
| Fixed overhead allocated per unit must not increase when production falls or ceases | TAS 2 ¶13 | `FACT VERIFIED` — **constrains how the productive half is computed**; see `BLK-07` |
| Normal capacity already absorbs capacity lost to **planned** maintenance | TAS 2 ¶13 | `FACT VERIFIED` — **splits the MAINTENANCE cause**; see `BLK-08` |
| The reference product has a structured downtime taxonomy at work-centre level, keyed to time logs | `07` §4 | `FACT VERIFIED` — and it is **reusable**: its four categories map onto the Boss's seven causes |
| The reference product has **no** normal-capacity, absorption-variance or over/under-absorption mechanism anywhere in 797 modules | Exhaustive search | `FACT VERIFIED` (negative) |
| The reference product's machine cost is `actual logged hours × rate` — a variable-overhead treatment applied to a fixed cost | `08` §4 | `FACT VERIFIED` |

### Incorporated as

- `09` defines the productive/non-productive model and proves the identity closes.
- `09` §3 states the **one reading** under which `BD-02` and TAS 2 ¶13 are both
  satisfied, and shows that the obvious alternative reading breaches the standard.
- `07` §4 proposes reusing the platform's downtime taxonomy rather than inventing a
  parallel one — the Boss's seven causes and the platform's four categories are
  mapped, not merged.

### What `BD-02` does **not** decide

1. **The denominator of the productive rate.** `BLK-07`. This is the single most
   consequential open item created by this session.
2. **Whether MAINTENANCE splits into planned and unplanned.** `BLK-08`.
3. **The account to which each non-productive cause posts.** `12` §5 proposes a
   mapping; account selection is a chart-of-accounts decision, not a research finding.

### Tension found — one, and it is real

`BD-02` says "no depreciation amount may remain permanently unclassified" and
"do not automatically carry unclassified depreciation forward". Both are consistent
with TAS 2. But **a naïve implementation of 100% attribution is not**: if a period's
whole depreciation is divided across that period's actual productive hours, then in a
month of low output the per-unit charge rises, which TAS 2 ¶13 expressly forbids.

**`BD-02` is compliant under the normal-capacity reading and non-compliant under the
actual-hours reading.** The Boss's instruction does not choose between them. `09` §3
recommends the normal-capacity reading and states why. This is the item that most
needs a Boss decision at the Final Gate.

---

## `BD-03` — Work centre principle

> The work centre is not simply a generic averaging bucket for all machinery cost.
> The routing/operation/equipment relationship must preserve actual operational
> meaning. Determine the strongest defensible model without blindly copying a
> reference ERP implementation.

### What the evidence says

`BD-03` is **structurally vindicated and the reference model structurally cannot
satisfy it.** Three facts, each verified from primary source this session:

1. The operation object references a work centre and **nothing else**. It has no
   equipment field.
2. Equipment references a work centre, **many-to-one**. A work centre with three
   machines cannot say which one ran.
3. The cost function is `logged duration × work-centre hourly rate`. The rate is a
   single scalar per work centre that merges the cost pool and the allocation basis.

Together these mean the reference model answers "how much machine cost" and is
*incapable* of answering "which machine" — not by omission but by construction.

### Incorporated as

`19` §3 adopts the four-role separation the prompt asked to be challenged rather than
assumed. It is adopted **because** the challenge was run and the alternative failed:
`07` §6 sets out the case for keeping the work centre as the cost bucket and why the
evidence defeats it.

---

## `BD-04` — Allocation driver

> Machine hour, work-centre hour, production quantity are the controlled candidates.
> A customer/configuration context selects ONE primary allocation method unless
> evidence demonstrates a justified multi-driver model. Do not create arbitrary
> combinations.

### What the evidence says

The evidence **does** demonstrate a justified two-driver model, and the justification
is statutory rather than a matter of taste. TAS 2 ¶13 prescribes different treatment
for two classes of cost that the reference product merges into one rate:

- **Fixed** production overhead — including depreciation — allocated on **normal capacity**.
- **Variable** production overhead — allocated on the **actual** use of the facilities.

A single driver cannot be correct for both. `11` therefore proposes **one primary
driver per cost class**, not per customer, which is a narrower and more defensible
departure from `BD-04` than a free combination — and it is exactly the "justified
multi-driver model" the decision reserves for.

`11` presents the full matrix and does **not** declare a universal winner across
contexts, per the prompt's instruction.

---

## Summary of incorporation

| Decision | Incorporated | Evidence agrees | Evidence extends it | Open sub-decision |
|---|---|---|---|---|
| `BD-01` | Fully | Yes | Yes — enforce structurally, not by policy | Rate base; re-entry; disposal |
| `BD-02` | Fully | Yes, on destination | Yes — and constrains the method | `BLK-07`, `BLK-08` |
| `BD-03` | Fully | Yes, strongly | Yes — the reference model *cannot* comply | None |
| `BD-04` | With one declared departure | Partly | Yes — statute requires two drivers | Confirmation of the departure |

**No Boss assertion was found to be wrong about the business.** The two extensions
above arise from statutory text that was not available when the decisions were taken.
