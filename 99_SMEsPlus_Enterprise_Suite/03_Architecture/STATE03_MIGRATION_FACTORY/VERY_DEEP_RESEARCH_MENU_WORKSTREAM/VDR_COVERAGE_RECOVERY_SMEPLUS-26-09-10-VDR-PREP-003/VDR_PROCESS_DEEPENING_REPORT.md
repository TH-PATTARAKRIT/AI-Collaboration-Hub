# VDR_PROCESS_DEEPENING_REPORT.md
# What happens inside PROCESS — measured, and bounded

Session `[SMEPLUS-26-09-10-VDR-PREP-003]` · Layer: **LAYER 1 — CLEAN-ROOM.**
Commissioning instruction §6: *"Do not stop at INPUT → OUTPUT. Prove what occurs inside PROCESS."*

---

## 1. Denominator and instrument, declared before any number

| Clause | Value |
|--------|-------|
| **POPULATION** | the frozen `POPULATION_V3`, 5,074 items |
| **ELIGIBILITY** | items whose class makes `PROCESS` applicable under the spec rule table → **1,474** |
| **UNIT** | one invocable behaviour (a resolved method body), not a file and not a menu |
| **PATTERN** | Python AST parse of the resolved method body — **not** a regular expression over text |
| **PATH SET** | the 1,624 source files of the 149 modules in the declared domain boundary |
| **COVERAGE ASSERTION** | **962 of 1,474 eligible items yielded a parsable facet record — 65.3%.** Parse failures: **0** |

### The 512 that yielded no facet record — enumerated, not rounded away

| Class | n | Why no behaviour body exists to read |
|-------|--:|--------------------------------------|
| ACTION | 201 | 31 open a target view and execute no method; 30 are reports rendered by application code; 14 are client-side; 126 resolve through the 3-hop chain to a body already counted under its owning behaviour |
| MENUX / MENU | 158 | 17 are containers that invoke nothing; the rest inherit the process of the action they bind |
| OBJECT | 96 | **40 declare no behaviour at all in the domain source — they are data-only**, a determination, not a miss |
| BUTTON | 31 | the invoked method is not declared inside the 149-module boundary (it belongs to another domain) |
| AUTOMATION | 26 | scheduled jobs whose body resolves to a behaviour counted once |

**Nothing here is unknown.** Each of the 512 has a recorded `PROCESS_CONDITION` explaining what
executes instead. That is `DETERMINED`. It is not depth, and it is not counted as depth.

### Positive control

A synthetic method carrying every facet marker (a guard clause, a raised validation, a branch, a state
write, a mutating write, a `super()` call and a cross-domain call) was injected into the parse set. It
was extracted with **all eleven facets populated correctly**. The instrument can fire.

**Second shape**: the mutating-behaviour count was independently re-derived by walking assignment and
`write()`/`create()` call nodes in a separate pass. Agreement: exact.

## 2. The eleven facets extracted — and the nine not

§6 names twenty process facets. **Eleven are mechanically derivable from source at this scale. Nine are
not, and are DECLARED AS NOT COVERED rather than silently omitted:**

> **DERIVED (11):** TRIGGER · PRECONDITION · VALIDATION · DECISION_BRANCH · STATE_TRANSITION ·
> DATA_MUTATION · ERROR · EXCEPTION · CHAIN (`super()`) · OUTPUT · CROSS_MODULE_CALL
>
> **NOT COVERED (9):** calculation semantics · retry behaviour · cancel / reverse / return semantics ·
> business-rule intent · scheduler cadence · dependency ordering · input-validation user messages ·
> compensating action on partial failure · idempotency

This is why **`PROCESS` reaches only 1.15% RESEARCH-VERIFIED** while `DETERMINED` is 100%. The
RESEARCH-VERIFIED bar in the measurement spec requires **all twenty**. Eleven of twenty is not
two-thirds of the way there — it is a different claim, and it is reported as one.

## 3. Facet marginals — n = 962

| Facet | Distribution |
|-------|--------------|
| **TRIGGER** | called directly 427 (44.4%) · from a UI control 348 (36.2%) · create-hook 50 (5.2%) · model-level 28 (2.9%) · delete-hook 14 (1.5%) · onchange/constrains 13 |
| **PRECONDITION** | **none detected 547 (56.9%)** · single-record assertion 277 (28.8%) · guard-if at entry 138 (14.3%) |
| **VALIDATION** | **none detected 782 (81.3%)** · raises a user error 137 (14.2%) · raises a validation error 43 (4.5%) |
| **DECISION_BRANCH** | 0 branches 407 (42.3%) · 1 → 285 · 2 → 108 · 3 → 64 · 4 → 31 · 5+ → 67 |
| **STATE_TRANSITION** | **none 809 (84.1%)** · reads state 120 (12.5%) · **writes state 33 (3.4%)** |
| **DATA_MUTATION** | no 717 (74.5%) · **yes 245 (25.5%)** |
| **ERROR** | no 781 (81.2%) · yes 181 (18.8%) |
| **EXCEPTION** | **not handled 951 (98.9%)** · handled **11 (1.1%)** |
| **CHAIN** | no `super()` 749 (77.9%) · calls `super()` 213 (22.1%) |
| **OUTPUT** | returns a value 561 (58.3%) · returns nothing 206 (21.4%) · returns an action 195 (20.3%) |
| **CROSS_MODULE_CALL** | no 634 (65.9%) · **yes 328 (34.1%)** |

## 4. What the marginals say — four findings

### `P3-F-01` — Exception handling is effectively absent. 951 of 962 behaviours (98.9%) handle no exception.
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

### `P3-F-04` — 328 of 962 behaviours (34.1%) call into another domain at runtime.
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
- **`PROCESS` is 1.15% RESEARCH-VERIFIED (17 of 1,474)** — 10 objects and 7 menus, the only items where
  all twenty facets are established from an end-to-end trace. That number is the honest one.
