# 00_CARRY_FORWARD_IDENTIFIER_REGISTER.md
# Identifier lineage — what this package owns, and what it inherits

Session `[SMEPLUS-26-09-10-VDR-PREP-003]` · Layer: **LAYER 1 — CLEAN-ROOM.**

An identifier cited here but defined elsewhere is not an orphan; it is **inherited**, and this register
says from where. Without it, the pre-commit identifier check cannot distinguish a broken reference from
a legitimate carry-forward — and the difference matters, because severing lineage is as damaging as
leaving a dangling citation.

## 1. Families this package OWNS and defines

| Family | Meaning | Defined in |
|--------|---------|------------|
| `CH-nn` | challenge findings, adopted | `SMES_CORE_PREP003_CHALLENGE_REPORT.md` |
| `LESA-F-nn` | source-resolution findings | `LESA_PREP003_RESOLUTION_REPORT.md` |
| `P3-F-nn` | process deepening findings | `VDR_PROCESS_DEEPENING_REPORT.md` |
| `C3-F-nn` | configuration deepening findings | `VDR_CONFIGURATION_DEEPENING_REPORT.md` |
| `O3-F-nn` | optional-function deepening findings | `VDR_OPTIONAL_FUNCTION_DEEPENING_REPORT.md` |
| `R3-F-nn` | runtime proof findings | `VDR_RUNTIME_CRITICAL_PROOF_REPORT.md` |
| `PW3-F-nn` | prior-workflow recheck findings | `VDR_PRIOR_WORKFLOW_COMPLETENESS_RECHECK.md` |

**No identifier in a family owned by an earlier package is defined here.** Renaming an inherited
identifier would sever its audit lineage; this package cites them unchanged.

## 2. Identifiers INHERITED and cited, with their defining package

| Identifier | Subject | Defined in | State carried forward |
|------------|---------|-----------|----------------------|
| `CRITICAL-GAP-01` … `-06` | the six open critical gaps | PREP-001 register 09 / PREP-002 `00A` | **all six OPEN** |
| `BOSS-DEC-01` | whether valuation conclusions must be re-derived before supporting a design | PREP-001 register 09 | **OPEN — Boss** |
| **`BOSS-DEC-10`** | **whether the stop-at-one-hop boundary rule is adopted as the universal standard** | PREP-001 register 09 | **OPEN — Boss. The 5,074-item denominator under every number in this package rests on it, and PREP-002 classifies the rule as a PROVISIONAL RESEARCH CONTROL, explicitly not frozen as architecture.** Omitted from the R1 edition of this register (`CH-14`) |
| `BOSS-DEC-12` | whether the functional-ownership eligibility rule becomes universal | PREP-001 register 09 | **OPEN — Boss** |
| `BOSS-DEC-14` | is the quantity axis scoped to the owning module or cross-module | PREP-002 `00A` | **OPEN — Boss** |
| `GOV-01` | the governance certification defect: committing into a package while challengers read it | PREP-001, self-reported | **CLOSED as a defect; standing as a rule** |
| `RC-F-01` | the optional-function zero | PREP-002 `00D` §3 | **RETRACTED** — and its retraction is itself un-propagated (`PW3-F-01`) |
| `RC-F-03` | prior-emphasis refinement | PREP-002 `00D` §3 | **carries the withdrawn zero** (`PW3-F-01`) |
| `RR-F-06` | per-movement valuation in the current generation | PREP-002 `00C` | **RETRACTED** |
| `CORR-F-07` | gating read from two element kinds instead of twelve | PREP-001 self-correction log | closed |
| `CORR-F-37` | a positive control drawn from the searcher's vocabulary | PREP-002 self-correction log | closed; **standing rule** |
| `CORR-F-38` | one ordinal status per row cannot represent independent dimensions | PREP-002 | **repaired by this package** |
| `CORR-F-42` | deployment flag computed as domain-set membership, never queried | PREP-002 self-correction log | closed |

## 3. Numbering gaps in inherited families

The `CORR-F` and `RR-F` families show numbering gaps when swept **within this package**, because this
package cites only the subset of them that bears on its four purposes. The full series is contiguous in
its defining packages. **A gap here is a citation boundary, not a missing record** — and this note
exists so that no reader, and no sweep, has to guess which.
