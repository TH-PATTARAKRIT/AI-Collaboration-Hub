# P09_ACTUAL_PLAN_VARIANCE_EVIDENCE_REGISTER

**Prompt:** `SMEPLUS-26-09-06-P09-P2A-DOMAIN-PURE-BOUNDED-CLOSURE-002` · **Phase S** · **AI EOS NOT ACTIVE**
**Layer:** 1 — clean-room. **Answers `CQ-P09-05`.**

---

> ## ⚠ CORRECTED AFTER INDEPENDENT CHALLENGE
> Statements in this file were **contradicted by the AAS-03 challenges and re-verified against source by the author before adoption.** Corrections are marked inline; superseded wording is retained. The full list is in `P09_AAS03_INDEPENDENT_CHALLENGE_RECORD`.

---

## 1. THE FINDING, AND IT INVERTS THE QUESTION ASKED

The prompt asks *how variance is defined, calculated, attributed, grouped, dated and scoped.*

> **There is no variance. Not "variance is computed oddly" — the quantity does not exist in the P09-owned surface.**

Plan-versus-actual is expressed entirely as **ratios of consumption** and one **boolean**. At no point is a difference between intended and actual computed, stored or displayed as a quantity (EV-P09-202, EV-P09-203).

**Restating the question as P09 can answer it:** *what does this surface say about the relationship between intent and outcome?* It says **how much of the intention has been used up**, and **whether that exceeds 100 %**. It never says **by how much**.

---

## 2. THE NEGATIVE, ESTABLISHED TO THE PROGRAMME'S OWN STANDARD

A zero from one query form is not admissible here. Three independent forms were run.

| Form | Method | Result |
|---|---|---|
| **1 — the word** | `variance` across the P09-owned modules | **0** |
| **2 — the concept by other names** | `difference`, `delta`, `gap`, `remaining`, `deviation`, `over_amount`, `under_amount`, `vs_`, `shortfall`, `surplus` | **0** (one `remaining` match, inspected, unrelated) |
| **3 — the arithmetic** | any subtraction between the intended amount and the achieved amount, in either operand order | **0** |
| **positive control** | `budget` | **315 — the search fires** |

**Class B.** Boundary: four modules, one declared root, the source-file population, unit = declaration. **Not restatable as "no variance exists in the system".**

Form 3 is the one that matters. Forms 1 and 2 test vocabulary; **form 3 tests whether the computation happens under any name at all**.

> **CAVEAT ADOPTED AFTER CHALLENGE — AND IT STRIKES THE GROUND THIS FINDING STOOD ON.**
> Form 3 is the form that elevates this from a vocabulary result to a behavioural one, and it is the **weakest evidence in the round**:
> - its command was **described, never published** — a reader cannot re-run it;
> - it carried **no positive control of its own**. The 315 control is a *word-frequency* control and cannot demonstrate that a *subtraction-shaped* pattern can fire. A genuine control was available in the surface and was not used;
> - its population was source files only, while the Layer 1 claim covered *"computed, stored **or displayed**"* — **the view layer, where the comparison is actually rendered, was never tested.**
>
> **The disposition is reduced accordingly.** This is the author's own `declared-pattern-not-run` defect: publish the command and its output, not the pattern.

---

## 3. WHAT IS COMPUTED INSTEAD

| Quantity | Form | What it can answer | What it cannot |
|---|---|---|---|
| achieved amount | money | how much was recorded | — |
| **achieved percentage** | ratio | how much of the plan is consumed | **by how much it is over** |
| committed amount / percentage | money, ratio | how much is promised | whether promise and outcome are the same thing |
| theoretical amount / percentage | money, ratio | how much *should* be consumed by now, pro-rata on calendar days | anything about the business |
| **over-plan boolean** | flag | that a threshold was crossed | by how much, when, or by what |

> **GENERATION BOUND, added after the generation control (EV-P09-206, EV-P09-207).** The table above describes the generation actually read. In the other generation examined, **the committed amount and committed percentage do not exist as fields**: the report emits a hardcoded zero and defers the measure to a separate, optional module. **There are two figures there, not three.** This register's statements about the committed figure are therefore bounded to the generation that carries it, and the earlier "three figures on three time bases" finding is **bounded, not withdrawn**.

**AV-01 — A ratio is not a variance. ~~The quantity a manager acts on is the one that is absent.~~ NARROWED AFTER CHALLENGE.**

A ratio loses sign, magnitude and direction the moment the denominator changes. But the final sentence was **overstated and is withdrawn**: the plan amount and the achieved amount are rendered **together**, six times each, on list, form and pivot, with a decoration predicate comparing them (EV-P09-208 §9.8). A reader has the magnitude.

**What survives, and is defensible:** there is no **computed, stored, signed, tolerance-bearing, aggregable** variance. That is a narrower claim than published and it is the one the evidence supports.

**AV-02 — The threshold is fixed at exactly 100 % and is not a policy.** There is no tolerance, no band, no materiality. A plan consumed at 100.01 % and one at 300 % are the same boolean.

---

## 4. THE ATTRIBUTION, DATING, GROUPING AND SCOPING OF THE COMPARISON

Answered for the comparison that *does* exist.

| Property | Behaviour | Assessment |
|---|---|---|
| **attributed** by | exact dimension-value equality, per axis | no hierarchy roll-up at this join |
| **dated** by | the actual's own date against a free-form window | **no fiscal-period object**; three time bases across the three figures |
| **grouped** by | dimension value and account **type** | a plan cannot be stated against an account *set* — only a whole type |
| **scoped** by | the plan's company field, where empty matches **every** company | ownership and availability conflated in one nullable field |
| **stored?** | **no figure is stored** | the comparison is not reproducible on a later date |

**AV-03 — The comparison is not reproducible, so it cannot be audited.** Its inputs are mutable — an allocation on a posted, locked, hash-chained entry can be changed with no trace — and every figure is recomputed on read. **A closed period's plan consumption can change silently after the fact.** This is the base package's composite finding, restated at the comparison level, and this round found nothing that contradicts it.

---

## 5. WHAT P09 REQUIRES, STATED AS MEANING ONLY

`CANDIDATE PROCESS SEMANTIC` — not a design.

| # | Requirement | Why the evidence forces it |
|---|---|---|
| **AV-R1** | plan-versus-actual shall produce a **signed difference quantity**, not only a ratio | AV-01 |
| **AV-R2** | the comparison shall declare **one time basis** and convert to it visibly | three bases today |
| **AV-R3** | every figure shall state which truth it measures — ledger, management, or operational | achieved mixes T2 and T3 |
| **AV-R4** | a figure presented for a closed period shall be **stored, dated and re-derivable** | AV-03 |
| **AV-R5** | the over-plan condition shall be a **declared policy with a tolerance**, not a fixed equality | AV-02 |
| **AV-R6** | the comparison shall be **bidirectionally traversable** — from a figure to its contributing records, and back | four of eight trace links are absent |

**None of AV-R1…R6 is authorised by this document.** They are candidate meanings for Boss decision.

---

## 6. DISPOSITIONS

| ID | Disposition |
|---|---|
| the variance absence | **REDUCED AFTER CHALLENGE** → `UNRESOLVED — SPECIFIC P09 EVIDENCE UNAVAILABLE`. The narrow form — *no computed, stored, signed, tolerance-bearing, aggregable variance field* — is `SUPPORTED INTERPRETATION — P09`. The published form is **withdrawn** |
| `AV-01`, `AV-02`, `AV-03` | `FACT VERIFIED — CLOSED FOR CURRENT P09 EVIDENCE` |
| `AV-R1` … `AV-R6` | `BOSS DECISION REQUIRED — DECISION PACKAGE READY` |
| whether variance exists outside the bounded module set | `UNRESOLVED — SPECIFIC P09 EVIDENCE UNAVAILABLE` |
