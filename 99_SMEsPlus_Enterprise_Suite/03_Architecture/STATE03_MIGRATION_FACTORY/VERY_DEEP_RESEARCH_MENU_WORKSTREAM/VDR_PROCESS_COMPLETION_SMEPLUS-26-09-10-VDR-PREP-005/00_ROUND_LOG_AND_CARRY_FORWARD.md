# 00_ROUND_LOG_AND_CARRY_FORWARD.md
# Round log, identifier lineage, and what this package supersedes

Session `[SMEPLUS-26-09-10-VDR-PREP-005]` · Layer: **LAYER 1 — CLEAN-ROOM.**

## 1. The PREP-004 challenge round — opened, held, and closed by an explicit close

| Event | Value |
|-------|-------|
| Baseline challenged | `75b00dc1` |
| **Round OPENED (UTC)** | **2026-09-10T14:57:04Z** |
| Challengers | 2, disjoint mandates: grade legitimacy · missing surface and false exclusion |
| Commits into that package path while open | **0** — verified |
| **Round CLOSED** | on the explicit recorded close, **not** by inferring that reports had stopped arriving |
| Findings | 32 · adopted 30 |

**`GOV-01` did not recur.** The protocol adopted after it recurred in PREP-003 was: *the round closes by
a recorded close, never by inference.* It was followed.

## 2. What this package supersedes

**PREP-004 baseline `75b00dc1` is INVALIDATED as a baseline** and is **not edited**. Its corrections are
carried forward here, including **two retractions of its own conclusions** and the **withdrawal of both
its Critical Gap closures**. The frozen artefact stands as audit lineage.

## 3. Families this package owns

| Family | Defined in |
|--------|-----------|
| `PC5-F-nn` | `VDR_PROCESS_20_FACET_COMPLETION_MATRIX.md` |
| `CC5-F-nn` | `VDR_CONFIGURATION_CONSEQUENCE_MATRIX.md` |
| `OS5-F-nn` | `VDR_OPTIONAL_FUNCTION_SAFETY_MATRIX.md` |
| `FW5-F-nn` | `VDR_SOURCE_RUNTIME_CONFIG_OPTIONAL_RECONCILIATION.md` |
| `RF-A` … `RF-E` | `VDR_PREP004_FINDING_RESOLUTION_REGISTER.md` |
| `LESA5-F-nn` | `LESA_PREP005_SOURCE_RESOLUTION_REPORT.md` |
| `CH5-nn` | `SMES_CORE_PREP005_CHALLENGE_REPORT.md` |
| `PMO5-nn` | `PMO_PREP005_VERIFICATION_REPORT.md` |

## 4. Inherited, and their state

| Identifier | State carried forward |
|------------|----------------------|
| `CRITICAL-GAP-01` … `-06` | **6 of 6 OPEN.** Both PREP-004 closures withdrawn |
| `PR4-F-02` | **RETRACTED** — the configuration was read off a company-dependent property set for one company of 44 |
| `PR4-F-03` | **CORRECTED** — the control could not fire; a fourth route exists |
| `PR4-F-01` | **VALID** — every movement count reproduces to the digit under independent re-derivation |
| `PR4-F-05` | **CORRECTED** — its configuration column is inverted for two of three current-generation deployments; the generation discrimination it establishes stands |
| `RF-A` … `RF-E` | 2 CLOSED, 3 HOLD, each naming a bounded measurement |
| `BOSS-DEC-01` | **withdrawn** — answered by measurement in PREP-004 |
| `BOSS-DEC-10` | **removed from the Boss list**; the team half is measured, and the hop-0 finding shows the boundary question was mis-framed |
| `BOSS-DEC-12`, `BOSS-DEC-14` | **OPEN — not proposed**, because neither has had its team half measured |
| `GOV-01` | recurred in PREP-003; **did not recur in PREP-004 or PREP-005** |
| `CORR-F-37` *(a control drawn from the searcher's vocabulary)* | **recurred and was caught before publication** — the word-boundary defect in the cancel and reverse predicates |

## 5. The standing rule this round adds

> **A dimension is RESEARCH-VERIFIED only when an instrument outside the register established it for
> that item, and that instrument has a control that can fail in the configuration it is measured in.**

Both halves were earned this round: the first by six dimensions graded on the register's own columns,
the second by a positive control that measured the same negative twice.
