# P01 — CHECKPOINT REGISTER

Session: P01 — Procure-to-Pay (single continuing session across four prompts)
Layer: **1.** Updated at every checkpoint. **An interruption is not a reset.**

Status values: `NOT STARTED` · `IN PROGRESS` · `COMPLETE — EVIDENCE VERIFIED` ·
`PARTIAL — RESUMABLE` · `BLOCKED — EXTERNAL DEPENDENCY` · `BLOCKED — TOOL / PERMISSION` ·
`BLOCKED — EVIDENCE REQUIRED` · `SUPERSEDED — MATERIAL DELTA`.

---

## 1. PRIOR PROMPTS — CARRIED, NOT RE-RUN

| Prompt | Checkpoints | Status |
|---|---|---|
| `…-ACC-P01-P2P-REV2-001` | CP-00 … CP-FINAL | **COMPLETE — EVIDENCE VERIFIED**, superseded in parts by later rounds; lineage preserved |
| `…-ACC-REV2-CORR1` (scope-aware) | applied as a delta | **COMPLETE — EVIDENCE VERIFIED** |
| `…-TARGETED-CROSS-PROCESS-CLOSURE-001` | CP-P01T01 … CP-P01TFINAL | **COMPLETE — EVIDENCE VERIFIED** |

## 2. THIS PROMPT — `…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`

| ID | Checkpoint | Status |
|---|---|---|
| `CP-P01V00` | Auto-resume bootstrap / baseline verified | **COMPLETE — EVIDENCE VERIFIED** — baseline `49d0fe3` verified present, local == remote, 48 files |
| `CP-P01V01` | Database identity repaired | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V02` | Version identity reconciled | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V03` | Falsified claims corrected | **COMPLETE — EVIDENCE VERIFIED** — 3 falsified + 1 count error, retrieved verbatim |
| `CP-P01V04` | Version-sensitive findings reclassified | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V05` | Landed cost deployment reality | **PARTIAL — RESUMABLE** — under independent disproof; definitions and denominator delegated |
| `CP-P01V06` | Subcontract deployment reality | **PARTIAL — RESUMABLE** — same |
| `CP-P01V07` | Period lock path matrix v2 | **PARTIAL — RESUMABLE** — under independent disproof, 11 paths |
| `CP-P01V08` | Posted bill correction v2 | **PARTIAL — RESUMABLE** — under independent disproof, 7 paths |
| `CP-P01V09` | Accounting-lineage semantic integrity | **PARTIAL — RESUMABLE** — three lineage kinds under challenge |
| `CP-P01V10` | Financial company ownership v2 | **PARTIAL — RESUMABLE** — six actor paths under challenge |
| `CP-P01V11` | WHT partial-payment correction | **PARTIAL — RESUMABLE** — recalculation under challenge |
| `CP-P01V12` | WHT mechanism reachability | **PARTIAL — RESUMABLE** — kept separate from `V11` by instruction |
| `CP-P01V13` | PND deployment-owner analysis | **PARTIAL — RESUMABLE** — under challenge; statutory axis routed to P07 |
| `CP-P01V14` | Vendor advance ownership closure | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V15` | P01/P05 WHT reconciliation refreshed | **COMPLETE — EVIDENCE VERIFIED** — peer SHA unchanged, no reprocessing |
| `CP-P01V16` | DEP-P01-06 residual | **COMPLETE — EVIDENCE VERIFIED** — residual stated, not closed |
| `CP-P01V17` | P03 correction handoff | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V18` | P06 supersession caveat | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V19` | Contradictions re-ranked | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V20` | EC-06 deterioration analysed | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V21` | Exit criteria recalculated | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V22` | Transient permission blockers cleaned | **COMPLETE — EVIDENCE VERIFIED** — 2 of 4 retired |
| `CP-P01V23` | Four AAS-03 challenge layers | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V24` | AAS+ consolidation | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V25` | PMO supplemental review | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V26` | P11 supplemental handoff published | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01VFINAL` | Final commit verified, auto-resume updated | **COMPLETE — EVIDENCE VERIFIED** |

## 3. WHY SEVERAL ARE `PARTIAL — RESUMABLE` RATHER THAN COMPLETE

Nine checkpoints depend on evidence classes this session cannot obtain: **runtime execution**
(nothing has been executed in any P01 round) and **statutory sources** (none available; all
routed to P07). Each is resumable from a stated next action rather than from the beginning.

Marking them complete would be the failure the exit constitution names — *time consumed is not
work completed*.
