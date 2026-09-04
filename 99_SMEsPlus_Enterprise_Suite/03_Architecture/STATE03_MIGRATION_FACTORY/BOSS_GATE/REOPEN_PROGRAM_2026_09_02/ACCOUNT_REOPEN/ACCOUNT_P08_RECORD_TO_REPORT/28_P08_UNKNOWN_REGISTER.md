# P08_UNKNOWN_REGISTER

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`

Every unknown carries the mandated disposition vocabulary: `GATING` · `NON-GATING` · `ROUTED TO LATER WAVE/PROCESS` · `OUT OF SCOPE WITH EVIDENCE` · `BOSS DECISION REQUIRED`. An earlier draft classified these by closing condition only and omitted the vocabulary; that is corrected here.

| ID | Unknown | Class | Disposition | What closes it |
|---|---|---|---|---|
| `P08-U-01` | End-to-end reachability of the suppression parameters from an external caller | `SUPPORTED INTERPRETATION` | **GATING** — it moves `P08-T0-01` from defect to exploitable | one executed call |
| `P08-U-02` | Whether the custom access-check override module is installed in any deployment | `C` | **GATING** — it decides whether `P08-T0-08` is live | the deployed module registry |
| `P08-U-03` | Which copy of the project custom addon set is deployed | `D` | **GATING** — every custom-layer finding is conditional on it | deployment configuration |
| `P08-U-04` | Whether the residual-drift path manifests at runtime | `SUPPORTED INTERPRETATION` | NON-GATING | one database query |
| `P08-U-05` | Whether a classification change bypasses the residual routines | `D` | NON-GATING | runtime trial |
| `P08-U-06` | The statement-snapshot hook on an inverted date range | `SUPPORTED INTERPRETATION` | NON-GATING | runtime trial |
| `P08-U-07` | Whether the two rate-type shortcut sets produce a wrong figure | `D` | NON-GATING | runtime trial |
| `P08-U-08` | Which of the 22 roots the deployed system runs | `D` | **GATING** — it bounds every behavioural conclusion | `P08-BD-05`, a programme declaration |
| `P08-U-09` | The archive file inside the custom addon set, listed but not content-searched | `C` | NON-GATING | extract and sweep |
| `P08-U-10` | The custom modules not reviewed for isolation behaviour — **20 of the 21 that touch the ledger** | `C` | **GATING** — the one module examined produced a total access bypass; the sample rate is 1 of 1 | a bounded sweep |
| `P08-U-11` | Thai statutory requirements bearing on statement format, retention and the accounting date | `HOLD / EVIDENCE REQUIRED` | **ROUTED** — Accounting-Tax track, and P07 | authoritative evidence |
| `P08-U-12` | Whether any mechanism reconciles a genuine subsidiary store to the ledger | `C` | **GATING** — it is the object of `KRN-INV-06` | a bounded search |
| `P08-U-13` | The **~19 class-`A` claims scoped to one root of 22 and not re-run** | `C` pending re-run | **GATING** — this is the unclosed half of the root-set defect | re-run each pattern across the declared root set, or downgrade |
| `P08-U-14` | The **43 files that extend the ledger entry object** and may alter any semantic in this package | `C` | **GATING** — every posting, manual-GL and close finding is stated against the base implementation only | enumerate and diff each override |
| `P08-U-15` | The schema, trigger and migration-script surface, which no pattern run by this session can see | `C` | NON-GATING but named — candidate files exist in 7 roots and were not opened | open them |
| `P08-U-16` | Whether the accounting-event class list is complete as a class list, not merely in its cells | `C` | NON-GATING | a structural sweep beyond the accounting dependency closure |
| `P08-U-17` | The 102 accounting models collapsed out of the scope matrix by an unreproducible rule | `C` | **GATING** for the matrix's completeness claim | list the 131, map each to a matrix row, read the residue |

**17 unknowns. 8 GATING. 1 ROUTED. 8 NON-GATING. 0 out of scope with evidence.**

No `GATING` unknown is routed forward to hide it: `P08-U-13`, `P08-U-14` and `P08-U-17` all belong to this session's own scope and are named as this session's residuals, not passed to a later one.
