# IV FAST — CHECKPOINT REGISTER

Verifier errors and reruns are recorded, never erased (prompt §11 rule 8).

| CP | Checkpoint | Result | Evidence |
|---|---|---|---|
| `CP-F-01` | Fresh isolated clone made, base `origin/SMEsPlus` @ `b8666f1` | DONE | branch `audit/account-phase-s-fast-iv-2026-09-08-001` |
| `CP-F-02` | §2 immutable handoff verified once — branch head + blob SHA | **SATISFIED** | `00_` §1 |
| `CP-F-03` | §3 frozen authority read back, 40 chars, 7 RC + 2 Boss refs | **9 of 9 MATCH** | `00_` §2 |
| `CP-F-04` | Executor eligibility re-derived per repair/challenge pair | **NOT ELIGIBLE, 6 of 6** | `00_` §3 |
| `CP-F-05` | Lane A input-locality determined (`RC-02`/`03`/`04`) | **repo-only confirmed** | `02_`–`04_` §3 |
| `CP-F-06` | Lane B host inputs verified — root, 4 dumps, toolchain | **all present, SHA-256 match** | `05_` §4–§5 |
| `CP-F-07` | Lane C dependency state recorded with cause | **BLOCKED** | `06_` §2 |
| `CP-F-08` | Moving-head substitution swept, both failure limbs controlled | **6 of 6 HEAD==PIN** | `08_` §1.1 |
| `CP-F-09` | P07 closure impact checked | **unmoved `ee2be30`** | `08_` §1.2 |
| `CP-F-10` | Veto disposition prepared, denominator declared incomplete | **0 discharged** | `09_` |
| `CP-F-11` | Ten closure criteria tested | **4 TRUE / 4 FALSE / 1 PARTIAL / 1 NOT PROVED** | `10_` |
| `CP-F-12` | Terminal state issued | **`IV-CLOSEOUT-B`** | `11_` |

## Verifier errors and reruns this session

| # | Event | Correction |
|---|---|---|
| `VE-01` | First `pg_restore` discovery used zsh globs against `/Library/PostgreSQL/*`, which do not exist on this host; zsh reported *"no matches found"* and **aborted the remaining probes in the same command**, so the `~/Downloads` listing in that invocation returned nothing. **Read alone, that output would have supported a false "inputs absent" conclusion.** | Re-run with `set +e`, `find`-based discovery and explicit per-file tests. Both `pg_restore` versions and all four dumps were then found. Recorded because it is `[[smeplus-negative-result-command-limit-rule]]` exactly: **a shell mechanism, not the subject, produced the negative** |
| `VE-02` | Initial moving-head sweep ran with only one control, exercising the `PIN NOT ON BRANCH` limb. A clean result would have rested on a check whose other failure branch was unproven | Added a second control (`0941161^`) that fires the `head MOVED` limb before the 6-of-6 result was recorded. `08_` §1.1 |

**Neither error changed a published conclusion, and both are published because a control only
reported when it fires is not a control.**
