# VDR_PROCESS_20_FACET_COMPLETION_MATRIX.md
# The PROCESS dimension, instrumented — 0.00% to 88.54%

Session `[SMEPLUS-26-09-10-VDR-PREP-005]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoints 01–02.

---

## 1. Why this dimension was at zero, and what changed

PREP-004 reported `PROCESS 0.00%` and named it the programme's single blocking dimension. An
independent challenger then established something sharper: **no published script graded PROCESS at
all.** The zero was not a measurement — it was an ungraded column reported as a coverage result.

**This round builds the instrument.** All twenty facets are derived from the **abstract syntax tree** of
the resolved method body, never from a substring of its text. Every predicate a challenger falsified in
PREP-003 or PREP-004 is rebuilt on nodes rather than characters, and each rebuild is named at its facet.

## 2. Denominator, instrument and controls

| Clause | Value |
|--------|-------|
| **POPULATION** | the frozen population, items for which `PROCESS` is applicable → **1,510** (after the container correction, §7) |
| **UNIT** | one *(item, facet)* cell — **30,200 cells** |
| **PATTERN** | Python AST parse of the resolved body; the object registry of five deployments for the automation facet |
| **PATH SET** | the declared source root, plus five deployment extracts |
| **COVERAGE ASSERTION** | behaviours: **614 of 614 resolved, 614 exact, 0 fallback, 0 unresolved, 0 read failures, 0 parse failures** |

### The control that changed the result before it was published

The cancel and reverse facets first returned **0 of 614** — a clean, plausible zero. A positive control
drawn from the corpus was run against it:

```
control 'action_cancel'  -> cancel matched: False      <-- the predicate could not fire
control 'button_cancel'  -> cancel matched: False
```

**The predicate used a word boundary, and in an identifier like `action_cancel` the underscore *is* a
word character**, so `\bcancel\b` can never match. Rebuilt to match underscore-separated identifier
tokens, the same controls pass and the facets return **43 cancel paths and 23 reverse paths**.

> A zero that survives its own control is a result. This one did not survive it, and it was caught
> **before publication** rather than by a challenger afterwards. That is the whole point of the control.

### The second control, on the automation facet

Automation was first resolved by matching a behaviour's **method name** against the deployments'
scheduled-job and server-action records. That gave 180 items. Requiring the item's **model *and* method
to occur in the same record** gives **34**.

```
matched by method name alone        : 180   <- over-counts
matched by model AND method         :  34   <- the figure of record
false-positive rate of the name-only shape : 81.1%
```

**A name-only join over-counted by four-fifths.** Generic names — `create`, `button_validate` — appear
in records belonging to other models entirely.

## 3. Result

| | |
|---|---|
| PROCESS-applicable items | **1,510** |
| **PROCESS-COMPLETE — all twenty facets VERIFIED or NOT_APPLICABLE** | **1,337 = 88.54%** |
| Items with at least one facet unresolved | **173** |
| Facet cells: VERIFIED | 26,326 |
| Facet cells: NOT_APPLICABLE *(by class, declared)* | 559 |
| Facet cells: UNVERIFIED | 3,315 |

By class: behaviours **614 of 614** · objects **96 of 96** · buttons 343 of 431 · actions 154 of 201 ·
extension menus 92 of 134 · menus 38 of 45 · scheduled jobs 0 of 26 *(see §6)*.

## 4. The twenty facets, measured over 614 parsed behaviours

| Facet | Distribution |
|-------|--------------|
| **01 Entry Point** | called directly 69.5% · decorated 30.5% |
| **02 Preconditions** | **none detected 70.5%** · single-record assertion 21.8% · entry guard 7.7% |
| **03 Input Validation** | **none detected 80.5%** · raises a user error 12.9% · raises a validation error 6.5% |
| **04 Business Rules** | **none detected 80.3%** · conditional refusal 13.2% · declared constraint + refusal 6.5% |
| **05 Decision Branches** | 0 branches 38.1% · 1 → 30.8% · 2 → 14.5% · 3+ → 16.6% |
| **06 Calculation Logic** | **no calculation 87.9%**; of those that calculate, most carry **no rounding control** |
| **07 State Transition** | none 84.0% · reads state 13.4% · **writes state 2.6%** |
| **08 Internal Actions** | no self-call 46.3% · one 38.6% · two or more 15.1% |
| **09 Data Read** | **no explicit read 62.4%** · filtered 10.9% · browse 6.8% |
| **10 Data Write** | **no write 69.2%** · via write 11.4% · via create 9.4% |
| **11 Automation** | no automation reference 70.0% · **invoked by a job or server action 5.5%** · name-only match rejected 23.6% |
| **12 Scheduler** | not a scheduled entry point 99.2% |
| **13 Cross-Module Trigger** | **no boundary trigger 95.0%** |
| **14 Cross-Module Consumption** | **in-domain only 67.1%** · one external model 14.0% |
| **15 Error Handling** | **not handled 99.5%** — 3 behaviours of 614 carry a handler |
| **16 Failure Path** | **no explicit failure path 80.0%** |
| **17 Retry / Recovery** | **none 99.2%** — 3 carry transaction control, 2 are named as retry paths |
| **18 Cancel** | no cancel path 93.0% · **is a cancel path 4.6%** |
| **19 Reverse / Return** | no reverse path 96.3% · **is a reverse/return path 2.8%** |
| **20 Output / Handoff** | returns a value 55.5% · returns nothing 22.1% · returns an action 17.6% |

## 5. Findings

### `PC5-F-01` — the domain calculates almost nowhere, and where it does it usually does not round
**87.9% of behaviours perform no arithmetic at all.** Of the 74 that do, the majority carry **no
rounding or float-comparison helper**. In a domain whose subject is quantity and value, arithmetic
without an explicit rounding decision is the shape that produces cent-level drift. **For SMEsPlus this
is a design rule, not an observation: every quantity or value computation needs its rounding decided at
the point of computation, not inherited from a default.**

### `PC5-F-02` — error handling, retry and recovery are effectively absent, and now measured as three separate facts
`99.5%` handle no exception · `99.2%` have no retry or recovery path · `80.0%` have no explicit failure
path. PREP-003 reported the first of these and a challenger correctly showed it was close to the
platform base rate. **The three together are a different claim**: this domain has neither handlers, nor
recovery, nor — in four cases in five — any declared refusal at all. Correctness is carried by the
database and by an ambient transaction. **A Node.js re-implementation inherits the code shape and none
of the ambient safety.**

### `PC5-F-03` — 2.6% write a lifecycle state; 30.8% mutate data
A behaviour that writes data without moving a state leaves no trace in the record that anything
happened. The ratio is roughly **twelve to one**. This is upstream of the Audit Trail and Immutability
Critical Areas, and it is why both sit where they do.

### `PC5-F-04` — cancel and reverse exist, and they are rare and concentrated
**43 cancel paths and 23 reverse/return paths** across 614 behaviours. The Reversal Critical Area covers
47 items; the domain's actual reverse surface is of that order. Both figures existed only because a
failing control was caught — under the first predicate both were zero.

### `PC5-F-05` — one behaviour in three reaches outside its own domain, and now the count means what it says
**32.9% access at least one external model**; 5.0% touch a declared boundary object. PREP-003 published
34.1% for a predicate that matched *any* model access including in-domain, and a challenger required its
retraction. **The instrument now separates in-domain from external by comparing against the declared
owned-model set**, so the number is about domain boundaries rather than about ORM usage.

## 6. What is NOT complete, and why — stated as a limitation, never as a determination

| Set | n | Why |
|-----|--:|-----|
| Buttons whose invoked method is outside the boundary | 88 | the body is not in the declared path set |
| Actions and extension menus whose target could not be resolved | 89 | multi-hop resolution beyond the declared boundary |
| Menus | 7 | as above |
| **Scheduled jobs** | **26** | their process is the server action they run. **11 were resolved by a three-table join through five deployments** — cadence, active state and body — and **15 more from their source declaration**, but the facet model has not yet been applied to those bodies. **This is the clearest remaining work in the dimension and it is bounded** |

**173 items, 11.46%.** Each names its own limitation. None is recorded as `NOT APPLICABLE`, and none is
sent upward as a question.

## 7. The container correction, applied at the population level this time

An independent challenger established that the container rule, which PREP-004 applied to 17 nodes, was
keyed on a marker emitted only for one of the two menu classes. **By the package's own published
definition — a grouping node that binds no action — the population is 54, not 17.**

```
class=MENU   binds no action : 17   had the rule
class=MENUX  binds no action : 37   did NOT have the rule
total by the published definition : 54
```

**All 54 now carry it.** Applicable cells: 30,870 → **30,759**.

> This is the third round in which this family stated a correction rule and applied it only where a
> reviewer pointed. It was corrected at 3 of 17, then found wrong at 17 of 54. **The rule now keys on
> the property, not on the class the marker happened to be written for.**
