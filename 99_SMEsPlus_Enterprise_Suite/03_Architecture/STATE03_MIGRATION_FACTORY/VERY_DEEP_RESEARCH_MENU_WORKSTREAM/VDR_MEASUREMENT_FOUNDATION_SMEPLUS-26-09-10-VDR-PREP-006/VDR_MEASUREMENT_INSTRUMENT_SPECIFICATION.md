# VDR_MEASUREMENT_INSTRUMENT_SPECIFICATION.md
# What a measurement must state before it may produce a number

Session `[SMEPLUS-26-09-10-VDR-PREP-006]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 05.

---

## 1. The rule this specification exists to enforce

> **Research output must not be used as its own grading oracle.**

A previous round graded six of nine dimensions by a string test over columns the same process had
written — zero exceptions in 5,074 rows — and in one case the script wrote the qualifying string and
tested for it thirteen lines later in the same loop. **That is the failure this specification prevents,
structurally rather than by intention.**

## 2. The five stages every measurement must keep distinct

| Stage | Definition | May it use the previous stage's output? |
|-------|-----------|----------------------------------------|
| **OBSERVATION** | a fact read from an artefact outside the measurement — a file, a registry record | — |
| **DERIVATION** | a fact computed from observations by a published rule | yes |
| **CLASSIFICATION** | placing a derived fact into a declared category | yes |
| **GRADING** | assigning a coverage verdict to a classification | yes |
| **VERIFICATION** | an independent party reproducing the grade from the observations | **it must not use any stage's output — it re-derives from the observation** |

**A stage may never be skipped, and no stage may read a field that a later stage writes.**

## 3. The eighteen clauses every dimension must declare

1. Measurement name · 2. Purpose · 3. Unit · 4. Population eligibility · 5. Numerator ·
6. Denominator · 7. Inclusion rule · 8. Exclusion rule · 9. N/A rule · 10. Required evidence ·
11. Allowed evidence classes · 12. Verification status required · 13. Criticality rule ·
14. Failure rule · 15. Contradiction rule · 16. Recalculation rule · 17. Versioning rule ·
18. Reproducibility procedure.

## 4. Rules that bind every dimension without exception

| Rule | Statement |
|------|-----------|
| **Evidence externality** | the numerator must rest on an artefact **outside the register**. A field written by the measurement process is never evidence |
| **Falsifiability** | every grade must have a value it can take that means *not verified*, and that value must **occur** in the register. A grade with no observed negative is not a test |
| **Control liveness** | every published negative must carry a positive control that **can fire in the configuration it is measured in.** A control that measures the same negative twice is not a control |
| **N/A discipline** | `N/A` is assigned only by a published class rule. **Unknown, disabled, hidden, optional and configuration-dependent are never `N/A`** |
| **Exclusion traceability** | an item may leave a denominator only by a registered exclusion carrying ids, reason, evidence, reviewer and status. **An item may never simply disappear** |
| **Denominator stability** | once measurement begins the denominator is frozen. A change forces a new population version, full recalculation, and preservation of the prior calculation |
| **No compensation** | each dimension is judged against its own floor. A strong dimension never offsets a weak one |
| **No self-certification** | the author of an instrument may not be its sole validator |

## 5. The sixteen dimensions, and their declared shape

| Dimension | Unit | Numerator | Denominator | Required evidence |
|-----------|------|-----------|-------------|-------------------|
| Source Presence | entity | pointer resolves to file **and** line in the declared root | entities with source applicable | the file, read |
| Runtime Reachability | entity | the declaring module is installed on ≥1 deployment | entities with runtime applicable | the installed-module table |
| Runtime Observation | entity | the entity's **own** registry record found, joined on its own identity | entities for which such a record can exist | the deployment registry |
| Configuration Reachability | entity | its gate condition determined | entities with configuration applicable | the gate census |
| Optional Function Reachability | entity | its activation route determined | entities with optional applicable | the dependency graph |
| Process | (entity, facet) | all 20 facets VERIFIED or class-N/A | process-applicable entities | the parsed body |
| Configuration | entity | OFF-vs-ON consequence proven **for that entity** | configuration-applicable entities | source + a deployment where the state differs |
| Optional Function | entity | activation **and** deactivation proven for that entity | optional-applicable entities | source + uninstall path |
| Function Complete | entity | every applicable dimension verified | applicable population | all of the above |
| Object/Data | entity | its declared type, attributes, relations and constraints | data-applicable entities | the field registry |
| Cross-Module | entity | its boundary-crossing relations enumerated | relational entities | the relation graph |
| Hidden Automation | entity | job or server action joined on **model and method** | process-applicable entities | the deployment job registry |
| Security | entity | **class-appropriate**: for a governed object, what governs it; **for a governing object, what it grants** | security-applicable entities | the access and rule registries |
| Tenant/Company | entity | its isolation scope determined | scoped entities | record rules + company records |
| Edge/Reversal | entity | cancel and reverse path established, absence included | lifecycle entities | the parsed body |
| Audit/Traceability | entity | its state-change trace established | mutating entities | the parsed body + registry |
| Critical Area | (entity, dimension) | every applicable cell verified | the area's mapped entities | all of the above |

## 6. Thresholds

| | |
|---|---|
| **Every applicable dimension** | **≥ 96%** — a per-dimension floor, never an average |
| **Every Critical Area** | **100%** |
| **Any uncertified instrument** | the dimension it measures produces **no official coverage** |

## 7. What this specification forbids outright

- A grade computed from a field the measurement wrote.
- A classification used as proof of itself.
- A denominator that changes because the instrument changed.
- An excluded item that disappears without a traceable reason.
- A percentage published from an instrument that has not passed independent validation.
