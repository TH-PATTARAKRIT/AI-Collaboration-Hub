# VDR_PENDING_MEASUREMENT_REPAIRS_REGISTER.md
# The exact nine repairs — retrieved, not invented, and not executed

Session `[SMEPLUS-26-09-10-VDR-SUSPEND-001]` · Layer: **LAYER 1 — CLEAN-ROOM.**

**Source of record:** `VDR_MEASUREMENT_FOUNDATION_SMEPLUS-26-09-10-VDR-PREP-006/`
`PMO_PREP006_FINAL_VERIFICATION_REPORT.md` **§5**, at commit **`361ee541`**. The nine below are that
list, in that order, normalised only for tabulation. **Nothing was added, merged or replaced.**

**Status of every repair: PENDING FUTURE EXECUTION.** None was executed during this suspension.

---

## `REP-01` — the anti-self-reference control must be able to fail

| Field | Content |
|-------|---------|
| **Original finding** | *"`WRITTEN_FIELDS` derived by static analysis of the whole pipeline, with a negative control the test must reject."* |
| **Affected instrument** | the harness's anti-self-reference test — **and, through it, all seven instruments** |
| **Affected dimension** | every dimension: no coverage may be certified while the control that polices grading cannot fail |
| **Evidence pointer** | `…PREP-006/VDR_ANTI_SELF_REFERENCE_VALIDATION_REPORT.md` §1–§3; the instrument module (`WRITTEN_FIELDS`) and the harness, both in `…/MACHINE_REGISTERS/` |
| **Criticality** | **CRITICAL** — this is the round's headline finding |
| **Current status** | **PENDING FUTURE EXECUTION** |
| **Required future action** | derive the written-field set by static analysis of every script in the measurement pipeline; add a deliberately self-referential instrument the test **must reject** |
| **Dependency** | none — it is the entry point |
| **Source** | PMO PREP-006 §5.1; SMEs Core F-01, F-02 |
| **Resume priority** | **1** |

## `REP-02` — every fixture asserted against every instrument

| Field | Content |
|-------|---------|
| **Original finding** | *"Every fixture asserted against every instrument."* |
| **Affected instrument** | the fixture harness |
| **Affected dimension** | the credibility of every instrument-derived figure |
| **Evidence pointer** | `…PREP-006/VDR_MEASUREMENT_ADVERSARIAL_FIXTURE_REGISTER.md` §4; the harness and the three preserved fixture-result files in `…/MACHINE_REGISTERS/` |
| **Criticality** | **CRITICAL** — 168 verdicts computed, **24 compared (14.3%)**, 144 discarded unchecked |
| **Current status** | **PENDING FUTURE EXECUTION** |
| **Required future action** | assert all 168 cells; publish the full matrix; **"24 of 24" may not be cited as evidence of instrument correctness until this is done** |
| **Dependency** | none |
| **Source** | PMO PREP-006 §5.2; SMEs Core F-04, F-14 |
| **Resume priority** | **2** |

## `REP-03` — the five rejected instruments rebuilt or withdrawn

| Field | Content |
|-------|---------|
| **Original finding** | *"The five rejected instruments rebuilt or withdrawn."* |
| **Affected instruments** | **INS-03** (100.00% redundant with a column the pipeline wrote) · **INS-04** (single-valued on 24,553 of 24,553; declares 7 inputs, reads 1) · **INS-05** (46–48% false negatives, up to 40.8% false positives, 81.8% of firings on non-code identities) · **INS-06** (single-valued on 24,553 of 24,553) · **INS-07** (4,227 false duplicates) |
| **Affected dimensions** | four-way classification · exclusion legitimacy · **Edge/Reversal** · contradiction detection · duplicate detection |
| **Evidence pointer** | `…PREP-006/SMES_CORE_MEASUREMENT_INSTRUMENT_CHALLENGE.md` §1–§2; `VDR_MEASUREMENT_INSTRUMENT_REGISTER.md` |
| **Criticality** | **CRITICAL** |
| **Current status** | **PENDING FUTURE EXECUTION** — all five remain **REJECTED**; none may produce official coverage |
| **Required future action** | rebuild each on evidence its verdict actually rests on — in particular INS-05 on the method **body**, not the identifier — and publish its error rates alongside it; or withdraw it |
| **Dependency** | `REP-01`, `REP-02` |
| **Source** | PMO PREP-006 §5.3; SMEs Core F-03, F-13, F-14, F-15, F-16, F-17, F-18 |
| **Resume priority** | **3** |

## `REP-04` — a runtime-native domain module set

| Field | Content |
|-------|---------|
| **Original finding** | *"A runtime-native domain module set, so the two methods are independent in population as well as observation."* |
| **Affected instrument** | the two Hop-0 discovery methods and their union |
| **Affected dimension** | **the Hop-0 population itself, and every coverage figure computed on it** |
| **Evidence pointer** | `…PREP-006/VDR_HOP0_CANONICAL_POPULATION_REGISTER.md` §4; the runtime discovery script in `…/MACHINE_REGISTERS/`, line 25 |
| **Criticality** | **CRITICAL** — perturbing the shared module set moved the runtime output by **74.6%**; the agreement rate has **zero power** against an error in it |
| **Current status** | **PENDING FUTURE EXECUTION** |
| **Required future action** | derive the domain module set from the deployments' own module table, which is present on all five and was not used; re-run both methods; recompute the agreement |
| **Dependency** | none |
| **Source** | PMO PREP-006 §5.4; SMEs Core F-07, G-09 |
| **Resume priority** | **4** |

## `REP-05` — a declared version basis, off-generation deployments as their own stratum

| Field | Content |
|-------|---------|
| **Original finding** | *"A declared version basis, and off-generation deployments handled as their own stratum."* |
| **Affected instrument** | the Hop-0 union; every cross-deployment figure |
| **Affected dimensions** | Runtime Reachability · Runtime Observation · the corroboration rate |
| **Evidence pointer** | `…PREP-006/VDR_HOP0_CANONICAL_POPULATION_REGISTER.md` §6 version-basis note; `SMES_CORE_MEASUREMENT_INSTRUMENT_CHALLENGE.md` §2 |
| **Criticality** | **HIGH** — two of five deployments are generations 16.0 and 18.0, pooled against a 19.0 source tree; **765 comparable rows** exist only there and were scored as disagreement. Corroboration: **49.5% mixed · 53.9% constant basis** |
| **Current status** | **PENDING FUTURE EXECUTION** |
| **Required future action** | carry a generation dimension in the population, the agreement rate and the register; stratify |
| **Dependency** | `REP-04` |
| **Source** | PMO PREP-006 §5.5; SMEs Core F-19, G-10 |
| **Resume priority** | **5** |

## `REP-06` — the identity normaliser fixed

| Field | Content |
|-------|---------|
| **Original finding** | *"The normaliser fixed — 435 fabricated entities removed, 48 real matches restored."* |
| **Affected instrument** | the union script's runtime-identity normaliser |
| **Affected dimension** | the Hop-0 population and the corroboration rate |
| **Criticality** | **HIGH** — **37 phantom model identities and 397 phantom field identities are literal rows in the population file**, including one anchor model counted twice, once real and once phantom; and the constraint namespace is an unfixed guaranteed-zero join (46 source-only, 41 runtime-only, **0 both**) left inside the comparable denominator |
| **Evidence pointer** | `…PREP-006/VDR_HOP0_INDEPENDENT_CHALLENGE_REPORT.md` §3; the union script and `HOP0_POPULATION.csv` in `…/MACHINE_REGISTERS/` |
| **Current status** | **PENDING FUTURE EXECUTION** |
| **Required future action** | replace the unconditional underscore-to-dot substitution with an invertible map built from the real model list; extend it to the constraint namespace; remove the 435 fabricated rows; restore the 48 dropped matches |
| **Dependency** | none |
| **Source** | PMO PREP-006 §5.6; SMEs Core F-08, F-09, G-11 |
| **Resume priority** | **6** |

## `REP-07` — the 6,104-entity floor enumerated

| Field | Content |
|-------|---------|
| **Original finding** | *"The 6,104-entity floor enumerated — buttons, gated elements, selection values, compute dependencies, defaults, client templates, onchange and constraint triggers, HTTP routes, and the surface non-domain modules aim at domain models."* |
| **Affected instrument** | the source discovery method |
| **Affected dimension** | the Hop-0 population and **every** dimension measured on it |
| **Criticality** | **CRITICAL** — the floor decomposes as **3,921** entity kinds with no representation at all + **1,536** entities declared by non-domain modules targeting domain models + **103** live access grants + **544** registry records from custom modules outside the declared source path set |
| **Evidence pointer** | `…PREP-006/VDR_HOP0_INDEPENDENT_CHALLENGE_REPORT.md` §1 |
| **Current status** | **PENDING FUTURE EXECUTION** |
| **Required future action** | add an emitter per missing kind, including one that reads **inside** view definitions and one that reads controller classes carrying no model name; widen the module scope to modules that target domain models without extending them |
| **Dependency** | `REP-04` |
| **Source** | PMO PREP-006 §5.7; SMEs Core G-01, G-03, G-04, G-16 |
| **Resume priority** | **7** |

## `REP-08` — the twelve unopened runtime tables read

| Field | Content |
|-------|---------|
| **Original finding** | *"The 12 unopened runtime tables read, the rule table extracted, and each deployment's generation established from its own record."* |
| **Affected instrument** | the runtime discovery method |
| **Affected dimensions** | Security · Tenant/Company · Hidden Automation · Runtime Observation |
| **Criticality** | **HIGH** — the access, menu, constraint, server-action, job, parameter, group, module, movement, company, category and user tables were all extracted and **never opened**; the **rule table was never extracted at all**; and because the module table went unread, **no deployment's generation was ever established from its own record** |
| **Evidence pointer** | `…PREP-006/VDR_HOP0_INDEPENDENT_CHALLENGE_REPORT.md` §3; `work4/runtime/<deployment>/` |
| **Current status** | **PENDING FUTURE EXECUTION** |
| **Required future action** | read all twelve; extract the rule table; read each generation from its own module record. **Note: a valuation-layer extract exists as a file with no data block on all five — a present-and-empty file, which byte size alone cannot distinguish from a real absence** |
| **Dependency** | none |
| **Source** | PMO PREP-006 §5.8; SMEs Core G-15 |
| **Resume priority** | **8** |

## `REP-09` — the eleven live databases enumerated, or a recorded reason why not

| Field | Content |
|-------|---------|
| **Original finding** | *"The 11 live databases enumerated, or a recorded reason why not."* |
| **Affected instrument** | the evidence-base sweep |
| **Affected dimension** | Runtime Reachability and Runtime Observation, and the provenance of the five-deployment choice |
| **Criticality** | **HIGH** — eleven generation-19 databases are live in a running container, reachable by no filesystem search; four further paired volumes are **UNDETERMINED** because starting them would be a state change; a further generation-19 state of an already-included identity carries **486 installed modules against the used snapshot's 453**; and **the sweep that chose the five left no output on disk**, so that choice has no recorded provenance |
| **Evidence pointer** | `…PREP-006/VDR_HOP0_INDEPENDENT_CHALLENGE_REPORT.md` §3 final rows |
| **Current status** | **PENDING FUTURE EXECUTION** |
| **Required future action** | enumerate them, **or record why not**. **This is the one repair with a governance component**: reading or starting a live system this programme does not own is a state change, and it is on the Boss decision list for that reason — not because the technical question is open |
| **Dependency** | none |
| **Source** | PMO PREP-006 §5.9; SMEs Core G-17 |
| **Resume priority** | **9** |

---

## Roll-up

| | |
|---|---:|
| Repairs recorded | **9** |
| Executed during this suspension | **0** |
| Status of all nine | **PENDING FUTURE EXECUTION** |
| Critical | 4 (`REP-01`, `REP-02`, `REP-03`, `REP-07`) |
| High | 5 |
| Carrying a Boss governance component | 1 (`REP-09`) |

**All nine are measurement work. Not one is a question for the Boss, with the single exception of
`REP-09`'s governance half.**
