# 06 — REMEDIATION CHECKPOINT REGISTER

**Session** `[SMEPLUS-26-09-07-ACC-PHASE-S-REMEDIATION-002]`

| CP | Item | Status | Evidence |
|---|---|---|---|
| `CP-R-01` | Pre-flight: remote state, six frozen refs re-verified | **COMPLETE** | all six `HEAD == ASSERTED`; `00_` §3 |
| `CP-R-02` | Stale asserted SHA classified | **COMPLETE** | `09128a9` → `2e2b8de`, ancestor, **governance-only, non-material to evidence**; `00_` §4 |
| `CP-R-03` | Pre-freeze record published | **COMPLETE — ORDERING DEVIATION DECLARED** | verification done before mutation; **publication after**. Declared in `00_` §1 rather than concealed |
| `CP-R-04` | `CO-F-01` instrument + wrapper enumeration | **COMPLETE** | 4 candidates over a declared population; **1** consumes a pin table; a `git grep \b` tool failure caught and reported |
| `CP-R-05` | `CO-F-01` defect reproduced | **COMPLETE** | pin changed → **byte-identical** output |
| `CP-R-06` | Pin-honouring repair | **COMPLETE — UNVERIFIED** | `9d4ecdc`; 6 fail-closed classes + 2 positive controls; **2 invalid controls discarded and rebuilt, both recorded** |
| `CP-R-07` | Determinism | **COMPLETE** | two clean runs, byte-identical |
| `CP-R-08` | Old vs repaired by **member identity** | **COMPLETE** | 214 vs 214, **different sets**, one out / one in |
| `CP-R-09` | Affected claims re-stated, bounded | **COMPLETE — UNVERIFIED** | `D1` 56 · `D2` 48 · `D1∩D2` 19; `P11-E-47` verification sentence withdrawn |
| `CP-R-10` | `CO-F-02` receipt correction | **COMPLETE — UNVERIFIED** | both negatives struck; notification read at `c7cfd8a`; 5-pattern sweep, 0 further |
| `CP-R-11` | `RC-05` evidence sweep | **COMPLETE** | 4 dumps located; **`P08-RC05-PREP-C` NOT raised**; `~/Library` declared unswept |
| `CP-R-12` | `RC-05` instrument + controls published | **COMPLETE — NOT CERTIFIED** | `e368d11`; prediction hashed **before** first run |
| `CP-R-13` | `P08-U-22` retried | **COMPLETE** | readable under `pg_restore` 18.6; **population is 4 databases, not 3** |
| `CP-R-14` | `RC-01`…`RC-06` packaging verified | **COMPLETE** | `04_`; one provenance note on `RC-01`, no peer mutation |
| `CP-R-15` | Out-of-remit defect registered | **COMPLETE** | **`P11-E-49`** — manifest coverage assertion carried forward and false |
| `CP-R-16` | Pre-commit sweep, disjoint units | **COMPLETE** | identifier · file · table-row · hash · prohibited-wording; a heuristic false-positive class identified and stated |
| **`RC-01` … `RC-06`** | **execution** | **NOT RUN — NOT THIS SESSION'S TO RUN** | `XRD-009`; awaiting the appointed independent verifier |

## Not done, and deliberately so

| | |
|---|---|
| Any `RC` executed or certified | **NO** |
| Any veto discharged | **NO** — `AAS+-PS-VETO-01` `C-6`, `AAS+-VETO-04` both stand |
| Any domain Boss decision answered | **NO** — the 51 remain open |
| Any peer package mutated | **NO** |
| Any frozen ref rewritten | **NO** |
| Phase S declared closed | **NO** |
| P11 terminal state changed | **NO** — `TERMINAL B` |
| `~/Library` swept | **NO** — declared exclusion |
| `P11-E-49`'s shape swept across other packages | **NO** — outside the remit; **flagged as a lead** |
