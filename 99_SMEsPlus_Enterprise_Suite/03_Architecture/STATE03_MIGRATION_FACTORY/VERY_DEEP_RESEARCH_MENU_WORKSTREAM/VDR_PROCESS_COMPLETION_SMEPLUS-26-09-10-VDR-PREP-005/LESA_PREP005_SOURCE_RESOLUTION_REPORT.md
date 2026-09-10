# LESA_PREP005_SOURCE_RESOLUTION_REPORT.md
# Source Learning Navigator — the sixteen questions, answered per function

Session `[SMEPLUS-26-09-10-VDR-PREP-005]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 12.

---

## 1. §4's sixteen questions, and where each is now answered

| Question | Answered by | Coverage |
|----------|------------|---------:|
| WHAT the function is | the population register | 5,074 |
| WHERE it exists | the evidence pointer, resolved to file and line | **2,729 of 5,074**; 186 have prose, not a path |
| WHO owns it | the primary-owner derivation over 1,433 dependency graphs | 96 of 96 objects |
| HOW it is entered | `PROCESS-01` | **1,337** |
| WHAT triggers it | `PROCESS-01` + `PROCESS-11` + `PROCESS-12` | 1,337 |
| WHAT configuration controls it | the gate census — **per gate, not per function** | 42 gates |
| WHAT optional feature changes it | the subject census — **per subject, not per element** | 39 subjects |
| WHAT model/data it touches | `PROCESS-09` + `PROCESS-10` | 1,337 |
| WHAT state transitions occur | `PROCESS-07` | 1,337 |
| WHAT automation affects it | `PROCESS-11`, joined to five deployments' job and server-action records | 1,337 |
| WHAT security controls it | the access census — **and its standard does not fit three classes** | see §3 |
| WHAT cross-module handoffs exist | `PROCESS-13` + `PROCESS-14` | 1,337 |
| WHAT accounting consequences exist | the valuation re-derivation | the movement population |
| WHAT inventory consequences exist | the optional-function safety matrix | 25 modules, 14 switches |
| WHAT happens on failure/cancel/reverse/return | `PROCESS-15` … `PROCESS-19` | **1,337 — established for the first time** |
| WHAT evidence proves each conclusion | every figure carries its instrument and its control | — |

## 2. `LESA5-F-01` — the failing control, caught before publication

The cancel and reverse facets first returned **0 of 614**. A control drawn from the corpus was run
against the predicate:

```
'action_cancel' -> matched: False      the underscore IS a word character,
'button_cancel' -> matched: False      so \bcancel\b can never fire
```

**The predicate could not return the other answer.** Rebuilt on identifier tokens, the same controls
pass and the facets return **43 cancel paths and 23 reverse/return paths**.

> This is the fourth appearance of this defect class in the programme and **the first time it was caught
> by the producer before publication rather than by a challenger afterwards.** The difference is that
> the control was drawn from the corpus rather than written from expectation.

## 3. `LESA5-F-02` — a measurement standard that does not fit its own population

The security dimension asks *"which access grants and record rules govern this item?"* For a **field**
or a **view** that is the right question. For an **access rule**, a **record rule** or a **group** it is
backwards — those objects *are* the grants and rules.

Consequence: the 270 items of the Security Critical Area score **0 of 270 on their own dimension**, and
the area sits at 9.7%, the lowest of the fifteen. **This is a defect in the measurement, not a property
of the domain**, and it explains a number that would otherwise look like a research failure.

**The repair is a class-appropriate standard**: for a security object, the question is *what does it
grant, to whom, over what* — a different question with the same evidence already extracted.

## 4. `LESA5-F-03` — the automation join, and an 81% false-positive rate

Matching a behaviour's **method name** against deployment automation records gave 180 items. Requiring
the item's **model and method in the same record** gave **34**.

**The name-only shape over-counted by 81.1%.** Generic method names appear in records belonging to
entirely different models. The 34 is the figure of record; the 145 name-only matches are recorded as
*not counted*, with their reason, rather than dropped.

## 5. `LESA5-F-04` — 15 scheduled jobs resolved from source, 11 from runtime, none left unknown

Of 26 scheduled jobs, **11 were resolved through a three-table join** on real deployments — cadence,
active state and body — and the remaining **15 from their source declaration**, every one with a code
body. **Runtime-unreachable is not a licence to leave a process unknown**, and none was left as one.

## 6. Items LESA could not resolve, with the exact limitation

| Item | Limitation | What settles it |
|------|-----------|-----------------|
| 88 buttons, 89 actions and menus, 7 menus | the invoked body lies outside the declared boundary | extend the boundary, or accept the limit and record it — **not both** |
| 26 scheduled jobs at facet level | bodies located; the facet model has not been run over them | one pass, bounded |
| Configuration per function | established per gate | join the gate consequence to each governed element's process — **now possible** |
| Optional function per element | established per subject | as above |
| Whether any module deactivation has fired | source semantics only | module-state history + a column-existence check |
| 704 relational field sites (8.7%) | target supplied dynamically | a loaded-registry dump |

**Every one is a bounded measurement with a named instrument. None is a Boss question, and none is
recorded as one.**
