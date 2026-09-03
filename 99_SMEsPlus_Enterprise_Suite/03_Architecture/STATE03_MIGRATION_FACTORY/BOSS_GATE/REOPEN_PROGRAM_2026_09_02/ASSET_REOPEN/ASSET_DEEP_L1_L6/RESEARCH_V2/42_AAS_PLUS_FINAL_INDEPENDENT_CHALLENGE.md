# 42 — AAS+ FINAL INDEPENDENT CHALLENGE
**LAYER 2 — AUDIT QUARANTINE**

§97. After Level 6, the four experts review the **entire** Asset body again and each
names the ten items the prompt requires. AAS+ then consolidates **without hiding
disagreement**.

---

## EXPERT 1 — LEADER FUNCTIONAL DESIGN

| Prompt item | Answer |
|---|---|
| Most dangerous assumption | That the Boss's Asset and the reference ERP's Asset are the same object. One is a machine that makes concrete; the other is a number that amortises. Six levels have now proved they are different, and the programme still uses one word for both |
| Most weakly supported conclusion | That post-depreciation internal usage is a normal, common case worth designing around. Nobody has counted how many of the 244 open and closed assets are production machines rather than air-conditioners — **and the runtime sample is visibly full of air-conditioners** |
| Most important contradiction | `CTR-02` — a believed-in behaviour that does not execute |
| Most important source gap | `Operation → Equipment` |
| Most important accounting risk | Mid-life method change permitted silently, with no disclosure |
| Most important localisation risk | Deferred to Expert 3 |
| Most important data risk | An unpopulated equipment link that a costing design will key on |
| Most important code risk | Deferred to Expert 4 |
| Most important cross-module risk | That closing the modelling gap does not close the **data** gap — someone has to record which machine ran which job, every time |
| Most important opportunity | That two complete, unbridged truths already exist. The value is in the bridge, and the bridge is small |

---

## EXPERT 2 — LEADERSHIP DATABASE DESIGN

| Prompt item | Answer |
|---|---|
| Most dangerous assumption | That the asset row holds the asset's value. It does not — the entries do, and book value is a recursive tree aggregate |
| Most weakly supported conclusion | Anything drawn from the 280-record population. It is a **mid-migration snapshot**: no templates linked, 35 records with no accounts, provenance unverified |
| Most important contradiction | `CTR-06` — an ORM-only invariant on a bulk-migrated population |
| Most important source gap | No accumulated-depreciation field, so a migration must use the import mechanism, which breaks sub-ledger/GL agreement by design |
| Most important accounting risk | `FAIL-G02` — divergence created deliberately by the import field, detected by nothing |
| Most important localisation risk | Deferred |
| Most important data risk | **`UNR-08`.** I have raised the duplicate-equipment-link exposure at four consecutive levels and it is still uncounted. It is a correctness precondition, not hygiene |
| Most important code risk | Deferred |
| Most important cross-module risk | An unowned cross-domain write with no inverse (`CTR-04`) |
| Most important opportunity | Immutable posted rows plus cumulative-difference arithmetic. Inherit both verbatim; they eliminate two whole classes of defect for free |

---

## EXPERT 3 — LEAD INTEGRATION & LOCALIZATION

| Prompt item | Answer |
|---|---|
| Most dangerous assumption | That "off-balance" is a safe container. It is an account classification inside one product. **How it appears in Thai statutory financial statements was never established**, and the whole management ledger rests on it |
| Most weakly supported conclusion | That the reference chain is reusable. It absorbs at a **standard rate** and computes **no variance**. Feeding it a depreciation-derived rate does not make the output depreciation |
| Most important contradiction | `CTR-01` — a configured method with no verified implementation on the target |
| Most important source gap | **No tax book.** Six tax scenarios, six impossibilities, against statutory rates that are **ceilings** — precisely the condition that generates book/tax differences |
| Most important accounting risk | The compound of the above: the tax position is derived from a single schedule whose day convention nobody has verified |
| Most important localisation risk | `UNR-03` — whether Thai practice permits depreciation absorbed into inventory at all. Raised at Level 4, unanswered at Level 6, and it gates the entire costing design |
| Most important data risk | That 217 assets are running on a convention nobody has checked |
| Most important code risk | Deferred |
| Most important cross-module risk | Link 5 of the cost chain is **conditional on real-time valuation**. For periodic-valued products, machine cost reaches the unit price and never reaches the ledger |
| Most important opportunity | That the daily basis is reproducible by configuration (`17`). The remedy is cheap; only the verification is outstanding |

---

## EXPERT 4 — LEAD CODE & UI ARCHITECT

| Prompt item | Answer |
|---|---|
| Most dangerous assumption | **That the code in this workspace is the code running on the UAT.** `UNR-04` and `UNR-05` have been open since Level 1 and cap every negative finding in this package |
| Most weakly supported conclusion | Every statement of the form "X does not exist". Each is bounded by *"in the source trees available in this workspace"* |
| Most important contradiction | `CTR-02`, as a **class**: three constructs in one small custom module do nothing, and **none raises an error** |
| Most important source gap | No audit tracking on the fields that decide money — computation mode, method, accounts, analytic |
| Most important accounting risk | The computation mode can be changed with **no trace whatsoever** |
| Most important localisation risk | Deferred |
| Most important data risk | Fields that change money and are invisible in the form — paused days, stored gain |
| Most important code risk | **Silent inertness.** Code present, reviewed, believed, and doing nothing. There is no reason to think this module is unique |
| Most important cross-module risk | Rate snapshotting on work orders, which will silently defeat a monthly-derived rate |
| Most important opportunity | The reference engine is genuinely well built. Adopt its semantics; do not copy its implementation; and **never assume a custom extension executes without checking the initialiser** |

---

## AAS+ CONSOLIDATION — FINAL

### Where all four converge

1. **The reference engine is sound and worth learning from.** Sixteen adversarial
   attacks on the arithmetic, fifteen held, none arithmetic-related.
2. **Every remaining risk sits outside the engine** — in configuration, custom code,
   cross-module boundaries, migration, and unanswered statutory questions.
3. **The two truths are complete and unbridged**, and the bridge is the SMEsPlus
   proposition.
4. **Nothing the Boss asserted was wrong about the business.** Two assertions
   carried an implicit technical assumption the evidence does not support.

### Where they do not converge, preserved

| ID | Disagreement | Status |
|---|---|---|
| `D1-01` | Capitalisation: `ABSENT` or `PARTIAL` | Open |
| `D1-02` | Revaluation: boundary or `PARTIAL` | Open |
| `D2-02` | Retire the term "Depreciation Board"? | Open |
| `D3-01` | Severity of the unguarded confirm path | Open — the test is specified |
| `D4-01` | Is maintenance costing a genuine differentiator? | Open |
| `D5-01` | May internal usage accumulate without bound? | **Escalated to the Boss** |
| `D5-02` | Where machine identity should live | Open architecture decision |
| `D6-01` | Should the Level 6 scoreboard be reported? | Recorded; Expert 4's objection stands |

**Eight open disagreements. None suppressed. None averaged.**

### The four experts' single most important disagreement about priority

- **Expert 1** would spend the next effort on **counting what the population
  actually is** — how many assets are production machines.
- **Expert 2** would spend it on **`UNR-08`**, the duplicate-link count.
- **Expert 3** would spend it on **`UNR-03`**, Thai admissibility of absorption.
- **Expert 4** would spend it on **`UNR-04`/`UNR-05`**, establishing what is actually
  deployed.

AAS+ does not adjudicate this. All four are cheap; three of the four are the same
UAT session. **Expert 3's is the only one that is not, and it is also the only one
that can invalidate the design rather than adjust it.**

### AAS+ recommendations

1. **Run one UAT evidence session.** Nine open items close in it, including the
   highest-priority blocker `UNR-02`.
2. **Route `UNR-03` and `UNR-23` to the Accounting-Tax track now**, in parallel.
   They gate the design and neither is answerable from software.
3. **Bring `UNR-B3` to the Boss as a policy question**, framed as Expert 2 framed
   it: an accumulator without a terminating rule.
4. **Repair the Asset↔Equipment link before designing anything that keys on it.**
5. **Do not treat any negative finding in this package as final** until `UNR-04` is
   closed.

### AAS+ final position

The Asset domain is now **understood** to primary-source depth at every level the
prompt required. What remains open is not understanding — it is **verification of
the deployed system** and **authority rulings on Thai treatment**.

This package does not issue PASS, APPROVE or FREEZE, and no expert opinion in it
constitutes one.
