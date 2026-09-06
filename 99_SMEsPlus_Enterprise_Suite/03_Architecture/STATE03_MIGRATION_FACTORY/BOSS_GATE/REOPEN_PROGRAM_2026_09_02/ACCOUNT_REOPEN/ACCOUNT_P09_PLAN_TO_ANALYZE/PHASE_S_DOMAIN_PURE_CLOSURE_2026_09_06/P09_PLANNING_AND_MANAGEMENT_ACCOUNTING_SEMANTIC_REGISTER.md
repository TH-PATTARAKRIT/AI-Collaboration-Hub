# P09_PLANNING_AND_MANAGEMENT_ACCOUNTING_SEMANTIC_REGISTER

**Prompt:** `SMEPLUS-26-09-06-P09-P2A-DOMAIN-PURE-BOUNDED-CLOSURE-002` · **Phase S** · **AI EOS NOT ACTIVE**
**Layer:** 1 — clean-room. **Answers `CQ-P09-02`.**

---

> ## ⚠ CORRECTED AFTER INDEPENDENT CHALLENGE
> Statements in this file were **contradicted by the AAS-03 challenges and re-verified against source by the author before adoption.** Corrections are marked inline; superseded wording is retained. The full list is in `P09_AAS03_INDEPENDENT_CHALLENGE_RECORD`.

---

## 1. THE HEADLINE

> **~~Six~~ SEVEN of the planning concepts named are not present in the module set searched.**
> *(Corrected: the sentence said six and the list that follows it carries seven. An author-chosen denominator contradicted by its own adjacent sentence.)*
> What exists is a **budget**, its **revision**, and a **consumption ratio**. There is no forecast, no scenario, no version axis, no target, no baseline, no simulation — **and no variance.**

**AND THE BOUNDARY IS WEAKER THAN THIS FILE FIRST CLAIMED.** The positive control fires at 315 — but **all 315 hits fall in two of the four modules**, and one of the other two has a twelve-line model file that could not have produced a hit under any pattern (EV-P09-208 §9.6). **The control was a population-level control presented as an artefact-level one** — the author's own `NC-13`, written one round earlier and not applied.

**Further:** a module named for one of the absent concepts sits in the same root, joined to the management fact table, carrying a *stored* intent/achieved/ratio triple — and the name-based selector **structurally could not select it** (EV-P09-208 §9.7). The negatives remain true within their declared boundary; **the boundary was drawn by an instrument blind to the concept it tested.**

**Consequence for SMEsPlus:** the prompt's own vocabulary is *wider than the reference pattern's*. Planning semantics that a management-accounting process would normally be expected to inherit have **no precedent to inherit from**, and must be authored — exactly as the cost object and the financial-event identity must be.

---

## 2. THE TERM-BY-TERM DETERMINATION

| Concept | Present? | What it actually means here | Class |
|---|---|---|---|
| **plan** | **yes** | the axis structure and the intended-amount header; the word carries **two unrelated senses** in one surface — see §3 | `FACT VERIFIED — P09` |
| **budget** | **yes** | a header + lines, an intended amount per dimension and free-form window | `FACT VERIFIED — P09` |
| **revision** | **yes** | a parent/child link between a superseded plan and its successor | `FACT VERIFIED — P09` |
| **period** | **partial** | a free-form `date_from` / `date_to` window — **there is no fiscal-period object** | `FACT VERIFIED — P09` (absence class B) |
| **dimension** | **yes** | an axis, materialised as physical schema rather than data | `FACT VERIFIED — P09` |
| **measure** | **yes — three in one generation, two in the other** | intended amount, achieved amount, and a committed amount **that exists in only one of the two generations examined** — see §8 | `FACT VERIFIED — P09`, generation-bounded |
| **state** | **yes** | `draft` → `confirmed` → `revised` → `done` | `FACT VERIFIED — P09` |
| **forecast** | **NO** | zero occurrences, zero declarations | `NOT FOUND IN SCOPE` — class B |
| **scenario** | **NO** | zero | `NOT FOUND IN SCOPE` — class B |
| **target** | **NO** | zero | `NOT FOUND IN SCOPE` — class B |
| **baseline** | **NO** | zero | `NOT FOUND IN SCOPE` — class B |
| **simulation** | **NO** | zero | `NOT FOUND IN SCOPE` — class B |
| **variance** | **NO** | zero, in **three independent forms** — see `…ACTUAL_PLAN_VARIANCE_EVIDENCE_REGISTER` | `NOT FOUND IN SCOPE` — class B |
| **version** | **NO, as a planning axis** | the only matches are a module manifest string and two unrelated uses. Revision is a **lineage**, not a version dimension — §4 | `NOT FOUND IN SCOPE` — class B |

**Boundary on every class B above:** four modules of one declared root, the source-file population, unit = declaration. Not the system. **None of these may ever be restated as "does not exist".**

---

## 3. THE WORD "PLAN" CARRIES TWO UNRELATED MEANINGS

This is a semantic defect P09 must not inherit, and it is invisible unless the two senses are named:

| Sense | What it is | Scope |
|---|---|---|
| **plan-as-axis** | a *dimension type* — the declaration that "cost centre" is an axis of analysis | TENANT; materialises as schema |
| **plan-as-intent** | a *budget* — an intended amount for a dimension value over a window | TENANT or COMPANY |

They share a word and nothing else: different objects, different lifecycles, different scopes, no relationship. A requirement written as "the plan" is ambiguous between an analysis axis and a spending intention.

**PS-01 — SMEsPlus shall never use one term for the analysis axis and the intended amount.** The programme has already been bitten once by a name carrying two meanings; this one is in the P09 vocabulary itself.

---

## 4. REVISION IS LINEAGE, NOT VERSIONING

The distinction decides whether comparative planning is possible at all.

| Property | Evidenced behaviour | What it means |
|---|---|---|
| structure | a parent link and a child collection on the plan header | a **chain**, not a set of alternatives |
| the predecessor | flips to a `revised` state when the successor is confirmed | only one plan is live at a time |
| can two plans for the same dimension and window coexist as **alternatives**? | **not evidenced** — nothing distinguishes "the other case" from "the superseded case" | **scenario planning is not expressible** |
| is the superseded plan retained? | yes, readable | history survives |
| can the amounts on a confirmed plan still change? | **yes** — the lock is a view attribute, not a server guard | **the revision object is bypassable** |

**PS-02 — A revision chain answers *what did we previously intend?* It cannot answer *what if?*** Those are different objects. SMEsPlus needs both and inherits only the first.

**PS-03 — A revision is only meaningful if the predecessor is immutable.** Today it is not, so the chain records what was *declared*, not necessarily what was *in force*.

---

## 5. THE THREE MEASURES, AND WHAT EACH ONE ACTUALLY MEASURES

| Measure | Source | Time basis | Stored? | Truth class |
|---|---|---|---|---|
| **intended** | the plan itself | the plan window | yes | management intent |
| **achieved** | management records | the **record's own date** | **no** | **T2 + T3 mixed** — includes records with no ledger counterpart |
| **committed** *(one generation only — §8)* | open commitments | the **order date** | **no** | pre-financial |
| **theoretical** | the plan × elapsed calendar days | **calendar** | **no** | arithmetic, not a fact |

*(The table above describes the generation that carries the committed measure. In the other, the row does not exist and the report emits a hardcoded zero — §8.)*

**PS-04 — Only one of the four is stored, and it is the only one that is not a measurement.** Every figure describing *reality* is recomputed at read time from mutable inputs. This is the same defect as the unstored consumption figure recorded in the base package, restated at the semantic level: **the plan is durable and the actuals are ephemeral, which is precisely backwards.**

---

## 6. WHAT P09 OWNS, SEMANTICALLY

| Semantic | Owner |
|---|---|
| what an axis means, and what its values are | **P09** |
| what an allocation instruction means | **P09** |
| what an intended amount means, and its window and state | **P09** |
| what "consumed" means, and on which basis | **P09** |
| what a costed fact *is* | `EXTERNAL DOMAIN BOUNDARY` |
| when a commitment becomes an actual | `EXTERNAL DOMAIN BOUNDARY` |
| what an account type means | `EXTERNAL DOMAIN BOUNDARY` |
| which producers write balanced pairs | `EXTERNAL DOMAIN BOUNDARY` |

---

## 7. GENERATION — THE CLAIMS WERE TESTED RATHER THAN ASSUMED

The generation of the root read is **not established**: the manifest string carries no series, and the model-name set is identical across the two generations examined, so neither is a discriminator.

**Rather than assert a generation, the identical sweep was run against a second, independently-identified root** (EV-P09-206).

| Claim | Invariant across both roots? |
|---|---|
| forecast / scenario / baseline / simulation absent | **yes** |
| variance absent | **yes** |
| planning target absent | **yes** — the one apparent hit was inspected and is a user-interface attribute, not a planning target |
| ~~the four planning states~~ **the state vocabulary** | **NO — CORRECTED.** The vocabulary published was **wrong in both roots**: there are **five** states, and the fifth carries a deletion path. The control re-published the error as invariant (EV-P09-209 §10.1) |
| **the commitment measure** | **NO — see §8** |

**PS-05 — Where a claim is invariant across generations, it does not depend on resolving which generation was read.** ~~Five of the six~~ **All six** absences are invariant *(corrected: the prose contradicted its own table)*. The sixth item is not an absence at all, and is the finding below.

---

## 8. THE COMMITMENT MEASURE IS GENERATION-SPECIFIC, AND ITS ZERO IS AMBIGUOUS

The generation control found a divergence nobody had looked for.

In one generation the plan line carries a **committed amount and a committed percentage**. In the other, **neither field exists** — occurrences of the term fall from 77 to 2.

**The first draft of this register said the measure had been *removed*. That was wrong.** The second and third forms caught it before publication. The two surviving occurrences are in the reporting query, and they settle it: the query emits a literal **zero** for committed value, carrying an inline comment naming a **separate, optional module** as the real source.

> **The commitment measure was not deleted. It moved out of the core plan surface into a module that may or may not be installed.**

**PS-06 — A committed figure of zero means either *nothing is committed* or *the module that would tell you is absent*, and the two are indistinguishable on the face of the report.** `Installed != configured != exercised`, materialising inside P09's own surface rather than in an adjacent domain.

**PS-07 — The "three figures on three time bases" finding is generation-specific.** In the later generation there are **two** figures plus a hardcoded zero. Any P09 statement about the comparison must name the generation it describes. The earlier finding is not withdrawn — it is **bounded**.

---

## 9. DISPOSITIONS

| ID | Item | Disposition |
|---|---|---|
| `PS-01` | one word, two meanings | `BOSS DECISION REQUIRED — DECISION PACKAGE READY` |
| `PS-02` | scenario planning not expressible | `FACT VERIFIED — CLOSED FOR CURRENT P09 EVIDENCE` |
| `PS-03` | revision bypassable | `FACT VERIFIED — CLOSED FOR CURRENT P09 EVIDENCE` |
| `PS-04` | only intent is stored | `FACT VERIFIED — CLOSED FOR CURRENT P09 EVIDENCE` |
| six absent concepts | forecast / scenario / target / baseline / simulation / variance | `UNRESOLVED — SPECIFIC P09 EVIDENCE UNAVAILABLE` outside the bounded set; **no absence claim beyond the declared boundary** |
| `PS-05` | absences invariant across generations | `FACT VERIFIED — CLOSED FOR CURRENT P09 EVIDENCE` |
| `PS-06` | the ambiguous committed zero | `FACT VERIFIED — CLOSED FOR CURRENT P09 EVIDENCE` |
| `PS-07` | the three-figure finding is generation-bounded | `CONTRADICTED — CORRECTED` (bounded, not withdrawn) |
