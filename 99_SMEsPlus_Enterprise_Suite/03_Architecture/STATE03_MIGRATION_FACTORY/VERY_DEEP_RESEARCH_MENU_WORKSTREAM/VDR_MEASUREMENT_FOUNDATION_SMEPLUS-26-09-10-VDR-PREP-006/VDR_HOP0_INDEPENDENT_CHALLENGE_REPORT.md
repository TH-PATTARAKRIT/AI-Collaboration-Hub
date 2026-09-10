# VDR_HOP0_INDEPENDENT_CHALLENGE_REPORT.md
# "What exists at Hop-0 that the navigator did not enumerate?" — at least 6,104 entities

Session `[SMEPLUS-26-09-10-VDR-PREP-006]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 03.

The challenger did not read the register to validate the register. It rebuilt the domain rule in its own
code, re-derived every count by a second command of a different shape, and swept the host by format.
**20 findings. All adopted.**

---

## 1. The answer, with a number

> **At least 6,104 entities exist at Hop-0 that the enumeration does not carry — every one of them
> inside the navigator's own declared domain — plus 11 generation-19 deployment states the population
> was never built from.**

| # | Component | Count |
|---|-----------|------:|
| **A** | **Entity kinds with no representation at all**, inside the 99 domain modules — buttons 671 · gated view elements 913 · selection values 633 net · compute dependencies 724 · field defaults 483 · client templates 258 · onchange triggers 110 · constraint triggers 84 · **HTTP routes 45** | **3,921** |
| **B** | Entities declared in **non-domain** modules that **target a domain model** — 1,089 views, 182 access lines, 116 window actions, 37 reports, 27 record rules, 24 jobs, 15 server actions | **1,536** |
| **C** | Live access grants on domain models owned by non-domain modules, beyond B | **103** |
| **D** | Registry records on domain models from **custom modules with no source in the declared path set** | **544** |
| | **FLOOR** | **6,104** |

**A floor, not a total.** It excludes four undetermined container volumes, a rule table never extracted,
and whatever the eleven unenumerated live databases contain.

## 2. The anchor rule is one-hop and inbound-only

The anchor set is the **51 models the core module itself declares**. It excludes the valuation-layer,
landed-cost and batch-transfer objects, which belong to adjacent inventory modules — **so the rule is
not transitively closed**, and modules that extend a *domain* model rather than an *anchor* model are
dropped.

**And it follows only edges *into* the anchor, never *out*.** 72 models are extended by a domain module
but declared outside it, pulling in 53 owner modules. The consequence, stated as the challenger did:

> **The product module is not in the inventory domain.** Nor is the unit-of-measure module.

**The domain boundary is an artefact of which models happen to sit in one module's files.**

## 3. Findings that change figures in this package

| Finding | Effect |
|---------|--------|
| **The package publishes a fact and its negation** — the population register said 1,802 prior identities "fall outside the anchor rule"; the reconciliation matrix in the same package says **215** do | **corrected** |
| **"4,148 of 5,074 survive" is not reproducible** — exact identity gives **2,942**, an over-counting bound gives 4,349; 4,148 sits between them under an **undeclared** predicate | **withdrawn; 2,942 is the reproducible floor** |
| **The normaliser fabricates identities.** 26 of 198 domain models carry an underscore inside a segment and cannot round-trip: **37 phantom model identities and 397 phantom field identities are literal rows in the population file** — including one of the anchor's own models counted twice, once real and once phantom | **adopted** |
| **3,590 rows (14.6%) carry a module that does not exist** — `res`, `pos`, `ir`, `report`, `lot` — because the union takes the first dotted segment when the source lookup fails | **adopted** |
| **The headline double-counts 4,227** — 24,553 rows, **20,326 distinct identities** | **corrected** |
| **49.5% is not measuring corroboration.** 836 of the 2,783 runtime-only disagreements are artefacts (765 off-generation + 435 phantom); 1,238 of the 1,850 source-only ones are modules installed on no deployment — not disagreement, a property of the sample. **2,074 of 4,633 disagreements (44.8%) are artefact or non-disagreement; on the residual set agreement is ≈63.9%** | **adopted** |
| **"Logically independent" is false, and the code says so.** The runtime script opens the source script's output on line 25 | **withdrawn** |
| **Generation contamination.** Two of five deployments are 16.0 and 18.0, pooled against a 19.0 source tree. **811 identities are observed only there**, including a model that no longer exists after 16.0 | **adopted** |
| **12 of 14 extracted runtime tables were never opened** — access, menu, constraint, server-action, job, parameter, group, module, movement, company, category and user tables all sat unread. **The rule table was never extracted at all**, and the valuation-layer extract is a file present and empty, which byte-size alone cannot distinguish from a real absence | **adopted** |
| **Because the module table went unread, no deployment's generation was ever established from its own record** | **adopted** |
| **11 generation-19 databases are live in a running container**, reachable by no filesystem search; 4 more paired volumes are undetermined because starting them would be a state change. A further generation-19 state of an included identity, with **486 installed modules against the used snapshot's 453**, sits in a file. **The sweep that chose the five left no output on disk** | **adopted** |

## 4. What the challenger confirmed, having tried hard to break it

- **Every published count reproduces**, re-derived in its own code: 1,433 modules · 12,075 files, 0 parse failures · 51 anchor models · 99 domain modules · 12,092 source entities · 9,170 comparable · 4,537 both · 49.5% · 1,802. **The arithmetic is sound; every defect is a predicate or a boundary.**
- **Its own hypothesis was refuted.** It predicted live records created without an identifier would be invisible to both methods. Measured: **0 menus lack one**, 1 server action, 1 job. **A check that could have found missing surface and did not.**
- **A dead branch loses nothing** — the legacy-constraint form does not exist in this generation, re-tested with a firing positive control.
- **The declared source root is whole** — a single module root, 1,433 manifests.
- **The normaliser fabricates but never silently mismatches** — 0 of the 26 mis-normalised names collide with a real model.

## 5. The challenger's own caught defect, disclosed

A shell-glob failure made four searches return zeros that were **tool failures, not absences**. Re-run
in a second form they gave 724, 110, 84 and 913, matching an independent syntax-tree pass exactly.
**Disclosed rather than published.**

## 6. Verdict

**The Hop-0 population is NOT CERTIFIED**, and this challenge supplies the second and stronger reason.
The first was that two methods corroborate only half of what they find. The second is that **both
methods share a boundary neither can test, and inside that boundary at least 6,104 entities are not
enumerated at all.**
