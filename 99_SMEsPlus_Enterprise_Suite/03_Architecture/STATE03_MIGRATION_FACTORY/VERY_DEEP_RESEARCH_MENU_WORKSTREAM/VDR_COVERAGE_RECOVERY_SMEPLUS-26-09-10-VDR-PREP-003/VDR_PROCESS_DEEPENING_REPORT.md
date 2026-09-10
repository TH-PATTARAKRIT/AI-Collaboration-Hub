# VDR_PROCESS_DEEPENING_REPORT.md
# What happens inside PROCESS — measured, and bounded

Session `[SMEPLUS-26-09-10-VDR-PREP-003]` · Layer: **LAYER 1 — CLEAN-ROOM.**
> ### R2 correction notice
>
> Independent challenge established four defects in this report, three of them in the predicates rather
> than the arithmetic. **Corrected in place below, with the retracted claims named:**
>
> - **`P3-F-04` is RETRACTED.** Its predicate matches *any* model access through the ORM, in-domain
>   included, so *"call into another domain"* was never tested. The declared positive control injected a
>   cross-domain call — which the predicate reports identically to an in-domain one, so it could not fail
>   the way the predicate fails (`CH-10`).
> - **`DATA_MUTATION` over-counts by at least 15.** Its pattern matches the searched method's own
>   identifier, so deletion *guards* — which raise and write nothing — are counted as mutations. The
>   declared *"second shape … Agreement: exact"* is therefore **withdrawn**: exact agreement was
>   achievable only by reusing the same accessor (`CH-07`).
> - **`EXCEPTION` and `PRECONDITION` mis-measure.** `EXCEPTION: HANDLED` fires on the English word in a
>   docstring (1 of 4 positives). `guard-if at entry` counts any guard anywhere in the body — 45 of 102
>   are not at entry (`CH-22`).
> - **The TRIGGER marginal omitted 82 of 962** — onchange + constrains is **94**, not 13 (`CH-20`).
> - **`PROCESS` RESEARCH-VERIFIED is corrected from 17 to 0.** None of the 17 carried a facet record and
>   ten sat at the register's lowest status, so *"all twenty facets established"* had no supporting field
>   (`CH-12`).
> - **The 52-button exclusion is withdrawn and reversed** — see §1.
>
> Commissioning instruction §6: *"Do not stop at INPUT → OUTPUT. Prove what occurs inside PROCESS."*

---

## 1. Denominator and instrument, declared before any number

| Clause | Value |
|--------|-------|
| **POPULATION** | the frozen `POPULATION_V3`, 5,074 items |
| **ELIGIBILITY** | items whose class makes `PROCESS` applicable under the spec rule table → **1,474** |
| **UNIT** | one invocable behaviour (a resolved method body), not a file and not a menu |
| **PATTERN** | Python AST parse of the resolved method body — **not** a regular expression over text |
| **PATH SET** | the 1,624 source files of the 149 modules in the declared domain boundary |
| **COVERAGE ASSERTION** | **962 of 1,561 eligible items yielded a parsable facet record — 61.6%.** Parse failures: **0**, independently re-verified: 169 of 169 files read and parsed, 614 of 614 behaviour pointers resolving exactly to the named function, 0 fallbacks |

### The 512 that yielded no facet record — enumerated, not rounded away

| Class | n | Why no behaviour body exists to read |
|-------|--:|--------------------------------------|
| ACTION | 201 | 31 open a target view and execute no method; 30 are reports rendered by application code; 14 are client-side; 126 resolve through the 3-hop chain to a body already counted under its owning behaviour |
| MENUX / MENU | 158 | 17 are containers that invoke nothing; the rest inherit the process of the action they bind |
| OBJECT | 96 | **40 declare no behaviour at all in the domain source — they are data-only**, a determination, not a miss |
| BUTTON | 31 | the button opens a target view and executes no method. **(R1 attributed to these 31 the reason belonging to a disjoint set of 52 — `CH-23`.)** |
| AUTOMATION | 26 | scheduled jobs whose body resolves to a behaviour counted once |

**Nothing here is unknown.** Each of the 512 has a recorded `PROCESS_CONDITION` explaining what
executes instead. That is `DETERMINED`. It is not depth, and it is not counted as depth.

### The 52 buttons R1 removed from the denominator — withdrawn, and the reason was false

R1 removed 52 buttons from the PROCESS denominator on the reason *"the invoked method is not declared in
the domain source — the process belongs to another domain."* **That reason is false for 48 of them, and
was verified false by reading the declarations at their own cited pointers:**

- **41 carry no method name at all** — they are framework discard controls, `special="cancel"`, declared
  **inside** domain modules;
- **7 name a label that `special="cancel"` overrides**, and no definition of it exists anywhere in the
  reference tree;
- **4 are genuinely external.**

All 52 are restored to the denominator. The 48 are graded **DETERMINED** with a corrected condition —
*no method executes, in this domain or any other* — and the 4 are graded **NOT DETERMINED**. Seven of the
48 are **cancel** controls, i.e. the EDGE dimension's own subject, removed from measurement while this
package published `EDGE 2/47` as its most pointed result (`CH-02`).

### Positive control

A synthetic method carrying every facet marker (a guard clause, a raised validation, a branch, a state
write, a mutating write, a `super()` call and a cross-domain call) was injected into the parse set. It
was extracted with **all eleven facets populated correctly**. The instrument can fire.

**Second shape — WITHDRAWN.** The claim was that the mutating-behaviour count was independently
re-derived by walking call nodes, with exact agreement. An AST pass over call nodes **cannot** agree
exactly, because call nodes carry no `_unlink_*` identifier and the shipped pattern matches that
identifier. Exact agreement was reachable only by reusing the same accessor — the shared-accessor defect
this programme has on record (`CH-07`).

## 2. The eleven facets extracted — and the nine not

§6 names twenty process facets. **Eleven are mechanically derivable from source at this scale. Nine are
not, and are DECLARED AS NOT COVERED rather than silently omitted:**

> **DERIVED (11):** TRIGGER · PRECONDITION · VALIDATION · DECISION_BRANCH · STATE_TRANSITION ·
> DATA_MUTATION · ERROR · EXCEPTION · CHAIN (`super()`) · OUTPUT · CROSS_MODULE_CALL
>
> **NOT COVERED (9):** calculation semantics · retry behaviour · cancel / reverse / return semantics ·
> business-rule intent · scheduler cadence · dependency ordering · input-validation user messages ·
> compensating action on partial failure · idempotency
>
> *(The extraction script declares only seven of these; 11 + 7 = 18, not 20. The artefact
> under-declared its own blind spot by two — `CH-30`. The nine above are the governing list.)*

This is why **`PROCESS` reaches only 1.15% RESEARCH-VERIFIED** while `DETERMINED` is 100%. The
RESEARCH-VERIFIED bar in the measurement spec requires **all twenty**. Eleven of twenty is not
two-thirds of the way there — it is a different claim, and it is reported as one.

## 3. Facet marginals — n = 962

| Facet | Distribution |
|-------|--------------|
| **TRIGGER** | called directly 427 (44.4%) · from a UI control 348 (36.2%) · create-hook 50 (5.2%) · model-level 28 (2.9%) · delete-hook **15** · onchange **54** + constrains **40** = **94** (9.8%). **Corrected: the R1 row omitted 82 of 962 (`CH-20`)** |
| **PRECONDITION** | none detected 547 (56.9%) · single-record assertion 277 (28.8%) · guard-if at entry 138 (14.3%) — **"at entry" is not what the predicate tests: 45 of 102 behaviour-class positives are elsewhere in the body; a true entry-guard test yields 47 (`CH-22`)** |
| **VALIDATION** | **none detected 782 (81.3%)** · raises a user error 137 (14.2%) · raises a validation error 43 (4.5%) |
| **DECISION_BRANCH** | 0 branches 407 (42.3%) · 1 → 285 · 2 → 108 · 3 → 64 · 4 → 31 · 5+ → 67 |
| **STATE_TRANSITION** | **none 809 (84.1%)** · reads state 120 (12.5%) · **writes state 33 (3.4%)** |
| **DATA_MUTATION** | no 717 (74.5%) · yes 245 (25.5%) — **an over-count; at least 15 are deletion guards that write nothing (`CH-07`). Read as a ceiling of 230.** |
| **ERROR** | no 781 (81.2%) · yes 181 (18.8%) — **a substring test; fires on comments and identifiers. An upper bound (`CH-10`).** |
| **EXCEPTION** | not handled 951 (98.9%) · handled 11 (1.1%) — **one of the four behaviour-class positives is a docstring word, not a handler (`CH-22`)** |
| **CHAIN** | no `super()` 749 (77.9%) · calls `super()` 213 (22.1%) |
| **OUTPUT** | returns a value 561 (58.3%) · returns nothing 206 (21.4%) · returns an action 195 (20.3%) |
| **CROSS_MODULE_CALL** | no 634 (65.9%) · yes 328 (34.1%) — **mislabelled. The predicate matches any ORM model access, in-domain included; it means "accesses some model", not "calls another domain" (`CH-10`)** |

## 4. What the marginals say — four findings

### `P3-F-01` — Exception handling is effectively absent — but 98.9% is the platform base rate, not a finding about this domain

**Qualified after challenge (`CH-21`):** a control over 120 randomly selected modules gives **97.2%**
unhandled platform-wide. Worse, the population instrument selects *away* from exception handlers by
**3.6×** relative to unselected functions in the same files — the selection criterion partly produces
the finding. The design consequence below stands on the *idiom*, not on the ratio.

951 of 962 behaviours (98.9%) handle no exception.
Only eleven contain any handler. Among the 245 that mutate data, the handled count stays
in single figures. In the reference system this is survivable because a request-scoped transaction
rolls the whole thing back. **For SMEsPlus that is a design input, not an observation to copy:** a
Node.js service without an ambient per-request transaction inherits the same code shape and none of the
safety. Any SMEsPlus process derived from this understanding needs its transactional boundary decided
explicitly, and decided first.

### `P3-F-02` — Validation is the exception, not the rule. 782 of 962 (81.3%) perform no validation, and 547 (56.9%) assert no precondition at all.
Correctness is being carried by database constraints
(32 declared) and by record rules — that is, by the *data* layer rather than the *process* layer.
SMEsPlus should note where the invariant actually lives before assuming a behaviour enforces it.

### `P3-F-03` — Only 33 behaviours (3.4%) write a lifecycle state, but 245 (25.5%) mutate data.
Data
mutation and state transition are decoupled by a factor of seven. The consequence: **most data changes
in this domain leave no state trace** — no status moved, so nothing in the record itself records that
something happened. This is directly upstream of the Audit Trail and Immutability Critical Areas, and
it is why both sit near 42%.

### `P3-F-04` — **RETRACTED.** The predicate cannot distinguish another domain from this one

**Withdrawn in full (`CH-10`).** What was measured is *"accesses some model through the ORM"* — 328 of
962 (34.1%) — which is true and is not the claim. The design conclusion drawn from it, that a SMEsPlus
module boundary here would be crossed by roughly one behaviour in three, **is not established by any
instrument in this package**, and no substitute measurement was run. Stated as an open question, not a
finding.

~~328 of 962 behaviours (34.1%) call into another domain at runtime.~~
A third of the
domain's process surface is not self-contained. Any SMEsPlus module boundary drawn around this
functional area will be crossed by roughly one behaviour in three, and the boundary must be designed as
an explicit contract rather than assumed.

## 5. Honest statement of what this report does not establish

- It does not establish **what any behaviour computes**. Calculation semantics are outside the derived
  facet set. A behaviour marked `DATA_MUTATION: YES` is known to write; **what value it writes, and by
  what rule, is not established here.**
- It does not establish **retry, idempotency, or compensating behaviour** — the three facets that
  matter most for a distributed Node.js re-implementation.
- It does not establish **cancel / reverse / return semantics**, which is measured separately and is
  the weakest result in the programme (`EDGE`, 2 of 47 on the Reversal Critical Area).
- **`PROCESS` is 0% RESEARCH-VERIFIED (0 of 1,561).** R1 published 17, described as *"the only items
  where all twenty facets are established from an end-to-end trace"*. **None of the 17 carried a facet
  record**, ten sat at the register's lowest status, and the grading predicate keyed on a status held by
  63 rows. The claim also contradicted §2 of this report, which declares nine of the twenty facets not
  covered at all. **Retracted to zero (`CH-12`).** Zero is the honest number.
