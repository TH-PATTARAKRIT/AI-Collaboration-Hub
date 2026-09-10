# 00_CARRY_FORWARD_IDENTIFIER_REGISTER.md
# Identifier lineage — owned, inherited, and the open decisions

Session `[SMEPLUS-26-09-10-VDR-PREP-004]` · Layer: **LAYER 1 — CLEAN-ROOM.**

## 1. Families this package OWNS

| Family | Meaning | Defined in |
|--------|---------|-----------|
| `R4-F-nn` | runtime observation findings | `VDR_RUNTIME_OBSERVATION_REPORT.md` |
| `CF4-F-nn` | configuration OFF/ON findings | `VDR_CONFIGURATION_OFF_ON_PROOF_MATRIX.md` |
| `OD4-F-nn` | optional activation/deactivation findings | `VDR_OPTIONAL_FUNCTION_ACTIVATION_DEACTIVATION_MATRIX.md` |
| `PR4-F-nn` | prior-research revalidation findings | `VDR_PRIOR_RESEARCH_REVALIDATION_REPORT.md` |
| `LESA4-F-nn` | source-navigation resolutions | `LESA_PREP004_RESOLUTION_REPORT.md` |
| `FE-nn` | false-exclusion entries | `VDR_FALSE_EXCLUSION_CORRECTION_REGISTER.md` |
| `EV-nn` | evidence-admission entries | `VDR_CONTROLLED_EVIDENCE_ADMISSION_REGISTER.md` |
| `PMO4-nn` | PMO findings | `PMO_PREP004_CERTIFICATION_REPORT.md` |
| `P4-Rn` | register correction rules | the build script in the machine registers |

## 2. Inherited and cited

| Identifier | Subject | Defined in | State carried forward |
|------------|---------|-----------|----------------------|
| `CRITICAL-GAP-01` … `-06` | the six critical gaps | PREP-001 / PREP-002 | **2 CLOSED, 4 HOLD** |
| `CH-01` … `CH-32` | PREP-003 challenge findings | PREP-003 | all dispositioned; `CH-17` **CLOSED this round** |
| `PW3-F-01` … `-03` | prior-workflow defects in PREP-002 | PREP-003 | open against a frozen artefact; corrections published forward |
| `GOV-01` | committing into a package during review | PREP-001 | **RECURRED in PREP-003** (`PMO4-01`); a stronger round-close control is adopted here |
| `CORR-F-37` | a positive control drawn from the searcher's vocabulary | PREP-002 | **recurred twice this round**, in the register itself (`LESA4-F-10`) and in an instrument caught mid-flight |
| `RR-F-06` | per-movement valuation | PREP-002 | retraction **CONFIRMED**; the *explanation* offered for it is **contradicted** (`PR4-F-02`) |
| `BOSS-DEC-01` | re-derive valuation conclusions | PREP-001 | **WITHDRAWN — answered by measurement** |
| `BOSS-DEC-10` | stop-at-one-hop as universal standard | PREP-001 | **REMOVED from the Boss list**; team half measured (`LESA4-F-05`), Boss half not yet decidable |
| `BOSS-DEC-12` · `BOSS-DEC-14` | ownership eligibility · quantity-axis scope | PREP-001 / PREP-002 | **OPEN — not proposed this round**, because neither has had its team half measured |

## 3. Numbering gaps

`CH-`, `PW3-F-` and `CORR-F-` show gaps when swept within this package, because it cites only the
subset bearing on its workstreams. **A gap here is a citation boundary, not a missing record.**
