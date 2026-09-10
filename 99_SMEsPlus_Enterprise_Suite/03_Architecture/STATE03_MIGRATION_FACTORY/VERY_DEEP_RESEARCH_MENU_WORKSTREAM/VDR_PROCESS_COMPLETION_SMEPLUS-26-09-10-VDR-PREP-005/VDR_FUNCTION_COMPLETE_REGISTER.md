# VDR_FUNCTION_COMPLETE_REGISTER.md
# Function Complete — 0 of 5,074, and the arithmetic that says why

Session `[SMEPLUS-26-09-10-VDR-PREP-005]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 07.

---

## 1. The rule, applied without exception

§13: a function is complete only when **every** applicable dimension is verified — process,
configuration, optional function, source presence, runtime reachability, data/model, security,
cross-module, edge/reversal, audit/traceability. If any applicable dimension is unverified, blocked,
contradicted or unmeasured-critical, **Function Complete = NO**.

## 2. Result

| | |
|---|---|
| Applicable population | **5,074** |
| Applicable dimension cells | **30,759** |
| **FUNCTION COMPLETE** | **0 = 0.00%** |
| Determined-complete | 4,715 = 92.92% |
| Research-verified cells | **6,756 = 21.96%** |

Verified-dimension distribution: **2 dims → 2,595 items · 1 dim → 1,566 · 0 dims → 913. No item exceeds
two.**

## 3. Per dimension

| Dimension | Applicable | Determined | Det % | **Research-verified** | **RV %** | Instrument |
|-----------|-----------:|-----------:|------:|----------------------:|---------:|-----------|
| **PROCESS** | 1,510 | 1,337 | 88.54% | **1,337** | **88.54%** | **20-facet AST model + deployment job registry** |
| SOURCE | 5,074 | 4,888 | 96.33% | **2,729** | **53.78%** | pointer resolved to file and line against the declared tree |
| RUNTIME | 5,074 | 5,074 | 100.00% | **2,690** | **53.02%** | the deployment's own element registry |
| CONFIGURATION | 4,058 | 4,058 | 100.00% | 0 | **0.00%** | *retracted — see §4* |
| OPTIONAL_FUNCTION | 4,046 | 4,046 | 100.00% | 0 | **0.00%** | *retracted* |
| DATA_MODEL | 2,863 | 2,863 | 100.00% | 0 | **0.00%** | *retracted* |
| SECURITY | 4,058 | 4,058 | 100.00% | 0 | **0.00%** | *retracted* |
| CROSS_MODULE | 2,909 | 2,909 | 100.00% | 0 | **0.00%** | *retracted* |
| EDGE | 1,167 | 1,167 | 100.00% | 0 | **0.00%** | *retracted* |
| **ALL CELLS** | **30,759** | **30,400** | **98.83%** | **6,756** | **21.96%** | |

## 4. Why six dimensions returned to zero

An independent challenger tested each grade as a pure function of the register's own columns and found
**zero exceptions in 5,074 rows**:

```
CROSS_MODULE   non-empty(condition)      == RESEARCH_VERIFIED : 2909/2909, exceptions 0
DATA_MODEL     non-empty(condition)      == RESEARCH_VERIFIED : 2863/2863, exceptions 0
SECURITY       startswith("OBJECT-LEVEL:") == RESEARCH_VERIFIED : exceptions 0 of 4058
EDGE           startswith(one of 5 prefixes) == RESEARCH_VERIFIED : exceptions 0 of 1167
```

**Not one of these consulted an artefact outside the register.** Worse, in one case the grading script
**wrote** the qualifying string onto three rows and **tested for it thirteen lines later in the same
loop** — the script manufactured the evidence it then graded.

**All six are retracted. The rule adopted:** *research-verified requires an instrument outside the
register, with a control that can fail.*

**Cost of the retraction: 13,586 verified cells → 6,756. Published coverage 44.01% → 21.96%.**

## 5. Why PROCESS — the round's objective — did not produce a single complete function

`PROCESS` rose from an ungraded 0.00% to a measured **88.54%**, and **no item became function-complete**,
because process was never the only missing dimension. Every process-applicable item also carries
configuration, optional-function, data, security, cross-module or edge — and all six are now honestly at
zero.

**The blocker moved rather than cleared.** Before this round the blocker was that process was ungraded.
Now the blocker is that six dimensions have no instrument.

## 6. What each retracted dimension needs

| Dimension | The instrument it needs |
|-----------|------------------------|
| CONFIGURATION | the per-gate nine-axis consequence joined to each governed element's own behaviour — **now possible for the first time, because process has an instrument** |
| OPTIONAL_FUNCTION | the per-subject activation/deactivation result joined to each element |
| SECURITY | **a class-appropriate standard.** The current one asks what governs an item; for an access rule, a record rule or a group that question is backwards, which is why the Security Critical Area scores 0 of 270 on its own dimension |
| DATA_MODEL | the field registry already extracted, joined per item |
| CROSS_MODULE | the relation graph already built for the boundary measurement, per item |
| EDGE | the process facets 18 and 19 — **which now exist**: 43 cancel paths and 23 reverse paths measured |

**Four of the six can be built from artefacts this round already produced.** That is the honest next
step, and it is named rather than estimated.
