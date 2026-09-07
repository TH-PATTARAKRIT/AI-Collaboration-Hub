# IV CHECKPOINT REGISTER

Session: `SMEPLUS-26-09-07-ACC-PHASE-S-INDEPENDENT-RC-VERIFY-001`
Branch: `audit/account-phase-s-iv-rc-2026-09-07-001` · base `2e2b8dec555454435a462420b6abe5cfde9e7139`
Date: 2026-09-07

| CP | Checkpoint | State | Evidence |
|---|---|---|---|
| `IV-CP-00` | Isolated verification session opened; fresh clone; no reuse of any owner working tree | DONE | Clone at `ACCOUNT_PHASE_S_IV_RC_2026_09_07_EXECUTION/repo`, `git fetch +refs/heads/*:refs/remotes/origin/*` |
| `IV-CP-01` | Governing instruments read at immutable SHA (Boss ruling, remediation prompt, verification prompt) | DONE | `00_...` §1 |
| `IV-CP-02` | Hard precondition tested — `REMEDIATION-A` published? | **FAILED — NOT PUBLISHED** | `00_...` §2, checks P-1…P-4, each with a positive control |
| `IV-CP-03` | Required handoff artefact `04_RC01_RC06_VERIFIER_HANDOFF_MATRIX.md` present? | **FAILED — 0 occurrences across all remote branches** | `00_...` §2 CHECK P-2 |
| `IV-CP-04` | Remediation Workstreams A / B / C artefacts present? | **FAILED — 0 of 8 required outputs, no remediation branch** | `00_...` §2 CHECK P-2, P-3 |
| `IV-CP-05` | Structural independence of verifier identity established? | **FAILED — BOSS DECISION REQUIRED** | `00_...` §3 |
| `IV-CP-06` | `RC-01` executed | NOT STARTED — blocked by `IV-CP-02`, `IV-CP-05` | `01_11_IV_OUTPUTS_NOT_PRODUCED.md` |
| `IV-CP-07` | `RC-05` executed | NOT STARTED — blocked additionally by absent P08 reproducibility package | `01_11_...` |
| `IV-CP-08` | `RC-02` executed | NOT STARTED — blocked additionally by absent `CO-F-01` repair | `01_11_...` |
| `IV-CP-09` | `RC-06` executed | NOT STARTED — blocked additionally by absent `CO-F-02` repair and by `RC-05` | `01_11_...` |
| `IV-CP-10` | `RC-03` executed | NOT STARTED — blocked by `IV-CP-02`, `IV-CP-05` | `01_11_...` |
| `IV-CP-11` | `RC-04` executed | NOT STARTED — blocked by `IV-CP-02`, `IV-CP-05` | `01_11_...` |
| `IV-CP-12` | Post-RC cross-package verification | NOT STARTED — prompt §6 requires six terminal RC results; 0 exist | `01_11_...` |
| `IV-CP-13` | Veto disposition recommendation | NOT STARTED — no verified evidence generated; no Veto touched | `01_11_...` |
| `IV-CP-14` | Phase S closure criteria independently tested | NOT STARTED — prompt §8 bars documentary-only marking | `01_11_...` |
| `IV-CP-15` | Owner branches unmutated | HELD | Only write in this session is branch `audit/account-phase-s-iv-rc-2026-09-07-001`; all reads at `2e2b8de` |
| `IV-CP-16` | Terminal state published | DONE | `IV-PRECONDITION-HOLD` + `IV-INDEPENDENCE-HOLD`, `00_...` |

## VERIFIER ERRORS AND RERUNS (prompt §4.H)

| # | Error | Correction | Retained |
|---|---|---|---|
| `IV-E-01` | First filename sweep used an over-wide pattern (`HANDOFF_MATRIX\|RC01_RC06\|REMEDIATION`), returning 68 KB dominated by unrelated `*_REMEDIATION_*` Boss-gate files from 2026-09-02. The result was not wrong, but it could not discriminate. | Re-run narrowed to `HANDOFF_MATRIX\|RC01_RC06\|RC_01.*RC_06`, and separately as an exact per-filename count with a positive control. Both re-runs are the published evidence. | The over-wide run is disclosed here and not erased. |
| `IV-E-02` | The per-filename counting loop initially carried a stray `head -0` fragment which emitted `head: illegal line count -- 0` to stderr on each iteration. The counts themselves came from `grep -c` and were unaffected; the positive control (`05_PHASE_S_CLOSURE_CRITERIA_REGISTER` → 4) confirms the loop returned non-zero where a file exists. | Disclosed rather than silently re-run, so the published zeros are read against a known-noisy but demonstrably firing instrument. | Yes. |
| `IV-E-03` | Pre-commit table-integrity sweep (unit: table row, counting raw `|` characters) flagged one row of this file as malformed at 9 pipes against an expected 5. | **Re-checked against the GFM specification, not against the sweep's own assumption.** The four extra pipes are `\|` escapes inside code spans in the `IV-E-01` row; GFM resolves cell boundaries after escape processing, so the row is well-formed at 4 columns. The sweep produced a **false positive**: its predicate counts raw pipes, but the unit it claims to measure is cell boundaries. | Disclosed. The sweep is retained — a predicate that over-reports is safe here, one that under-reports would not be — but its known false-positive class is recorded so a successor does not read a future 9-pipe flag as a defect without checking for escapes. |

## CONTROLS APPLIED

| Control | Where | Result |
|---|---|---|
| Positive control on content grep | `REMEDIATION-A` search | `IV-PRECONDITION-HOLD` token → 1 hit; grep fires |
| Positive control on filename loop | 8-file absence sweep | `05_PHASE_S_CLOSURE_CRITERIA_REGISTER` → 4 hits; loop fires |
| Discriminating control | `HANDOFF_MATRIX` pattern class | 19 hits across P05/P06/P09/Inventory; the pattern matches real artefacts, so the RC matrix is the absent member |
| Second-shape confirmation | 4 disjoint check shapes (content grep, tree enumeration, ref enumeration, commit timeline) | All four converge on the same conclusion |
| No moving-head reliance | Branch cut from `2e2b8de`, not from `origin/<branch>` | Held |

No RC result state was issued. No Veto discharged. No Phase S criterion marked TRUE.
