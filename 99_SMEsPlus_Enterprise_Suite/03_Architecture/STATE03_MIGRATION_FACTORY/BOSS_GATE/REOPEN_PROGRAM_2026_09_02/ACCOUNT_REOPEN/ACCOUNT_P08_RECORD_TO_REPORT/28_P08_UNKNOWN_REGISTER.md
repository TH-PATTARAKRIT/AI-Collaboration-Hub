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

---

# CLOSURE DELTA — unknowns opened, discharged, or re-classified

| ID | Item | Class | Movement |
|---|---|---|---|
| `P08-U-02` | Whether the custom access-override module is installed anywhere | — | **DISCHARGED.** Absent or uninstalled in 3 of 3 |
| `P08-U-04` | Whether the residual-drift path manifests at runtime | — | **DISCHARGED.** 0 residual drift across 100,580 settled lines |
| `P08-U-10` | The custom addon set was largely unreviewed | — | **PARTIALLY DISCHARGED** by the sweep; **re-opened wider** as `P08-U-18` |
| `P08-U-13` | The lock-free re-dating path a peer reported | — | **DISCHARGED — CONFIRMED.** `46` §6 |
| `P08-U-14` | Three core-accounting instances handed over by a peer | `C NOT YET SEARCHED` | **NEW** |
| `P08-U-15` | Whether a tax-specific settlement mechanism exists under an unsearched name | `C NOT YET SEARCHED` | **NEW** |
| `P08-U-16` | Whether the remaining peer published under different branch naming | `C NOT YET SEARCHED` | **NEW** |
| `P08-U-17` | The hierarchy-wide lock traversal, peer-supplied and not re-derived | `B` for P08 | **NEW** |
| `P08-U-18` | **32 modules installed in a deployed database exist in neither searched source tree** — among them two touching ledger numbering, one writing the rate master, and one able to carry arbitrary models and server-side automation | **GATING — re-classified from `C NOT YET SEARCHED`** | **NEW, and the most consequential open item in the package.** The constitution forbids carrying a current-scope blocker as an unsearched class. Two of these sit directly under class-A claims and one is the residual route the context attack left open |
| `P08-U-19` | A statutory register query with **no company predicate**, in a module installed on two 44-company databases, recorded in the package's own quarantine and carried into no Layer-1 file | `FACT VERIFIED`, **unincorporated** | **NEW** |
| `P08-U-20` | Whether the second, vendor-supplied statutory reporting stack behaves as the custom one does | `C NOT YET SEARCHED` | **NEW.** The sweep examined one of two stacks and generalised |
| `P08-U-21` | What produced the 5,622 **backward** accounting-date divergences; the studied mechanism can only move a date forward | `UNRESOLVED — EVIDENCE REQUIRED` | **NEW** |
| `P08-U-22` | A fourth deployed database declared unreadable by one tool and not retried with another | `C NOT YET SEARCHED` | **NEW.** A fourth database is a fourth version premise |
| `P08-U-23` | Two further custom source trees on the host, outside the declared path set | `C NOT YET SEARCHED` | **NEW** |
