# 27 — P05 EXIT CRITERIA REGISTER

`LAYER 2 — AUDIT QUARANTINE`
Against `SMEPLUS-DR-EXIT-8C-001`. Each criterion carries exactly one disposition from the permitted
set: `SATISFIED — EVIDENCE VERIFIED` · `NOT SATISFIED — EVIDENCE GAP` · `NOT SATISFIED — PEER
DEPENDENCY` · `NOT SATISFIED — RUNTIME REQUIRED` · `NOT SATISFIED — STATUTORY EVIDENCE REQUIRED` ·
`NOT SATISFIED — CONTRADICTION` · `NOT APPLICABLE — EVIDENCE VERIFIED`.

**No criterion is bypassed to reach a READY status.**

## `EC-01` — Scope Bounded

| | |
|---|---|
| **Disposition** | **NOT SATISFIED — EVIDENCE GAP** |
| Movement this continuation | Substantial. The module population moved from *no evidence* to six real `ir_module_module` registries at class **A** within them (`24`). Source path set, patterns and units are declared and reproducible (`21 §1`). |
| Why still not satisfied | The **deployed** universe for the **v18 target** remains `UNBOUNDED / NOT YET ENUMERABLE`. No Odoo 18 database carrying the P05 surface exists in the evidence; the only v18 database found is a 41-module sandbox with the claim engine uninstalled. Held class **D**, not upgraded (`24 §4`). |
| Exact evidence that would close it | A dump or `ir_module_module` export of `smesplus_th`, or of any Odoo 18 database carrying the P05 custom modules. |
| Additional caveat found by review | The six registries are a **convenience sample** — the dumps that happened to exist on this host — not an enumerated population of deployments. That bound is stated in `24 §4`. |

## `EC-02` — Enumeration Converged

| | |
|---|---|
| **Disposition** | **NOT SATISFIED — CONTRADICTION** |
| Why | Convergence requires material-delta stability. This continuation produced the opposite: it discovered an entire evidence class the package had asserted did not exist (`39 RE-07`), and then **two of the three findings it published from that new evidence were contradicted by the single independent review that completed** (`39 RE-10`, `RE-11`) — one of them inverted. A round that publishes, then withdraws, its own headline empirical findings has not converged. |
| Not merely a gap | This is recorded as `CONTRADICTION` rather than `EVIDENCE GAP` deliberately: the defect is not missing evidence but unstable conclusions drawn from evidence in hand. |
| Exact evidence that would close it | Two consecutive independent passes producing no new material population and no new finding class — see `EC-07`. |

## `EC-03` — Unknown Exhausted

| | |
|---|---|
| **Disposition** | **NOT SATISFIED — EVIDENCE GAP** |
| Movement | `U-01` and `U-02` both moved from blanket unknowns to **partially resolved with precisely named residues**; `U-04` closed outright. Every unknown carries a permitted disposition (`35`). |
| Why still not satisfied | Gating unknowns remain: `U-01` (v18 target module state), `U-02b` (runtime execution), `U-03` (force-cancel and cross-currency outcomes, class **D**), `U-08` (`SO-01`, `SO-03`), `U-09` (statutory). None is routed forward to conceal it; each names the evidence that would close it. |

## `EC-04` — Tolerance-Zero Closed

| | |
|---|---|
| **Disposition** | **NOT SATISFIED — EVIDENCE GAP** |
| Count | **13 boundaries, 0 closed.** Seven `LIVE` in an evidenced deployment, six `LATENT` (`26 §4`). |
| Position taken | Deployment evidence changes a boundary's **reach**, never its **status**. No boundary was closed on the grounds that a module is currently uninstalled (`26 §2`). |
| Ownership | `TZ-08` is P08's; `TZ-11` (down-payment leg) and `TZ-12` are **P01's**. P05 cannot close another process's boundary. |

## `EC-05` — Contradiction Resolution Complete

| | |
|---|---|
| **Disposition** | **SATISFIED — EVIDENCE VERIFIED** |
| Basis | Every material contradiction is dispositioned with traceable evidence and lineage. Original round: 20 typed contradictions, 6 author self-corrections, **0 remaining as unresolved differences of opinion** (`11 §5`). Continuation: 4 further contradictions (`RE-10`..`RE-13`), all resolved by author re-verification of the reviewer's counter-evidence, all recorded with the original claim preserved and struck through rather than deleted. |
| Note | This is the one criterion the continuation strengthened rather than weakened — because the corrections were *taken*, verified, and propagated downstream rather than argued with. |

## `EC-06` — Negative Claim Controlled

| | |
|---|---|
| **Disposition** | **SATISFIED — EVIDENCE VERIFIED, with one standing defect disclosed** |
| Basis | 33 negative claims each carrying PATH SET, PATTERN, UNIT and a class letter; 6 contradicted claims recorded as class **E**; 4 held at class **D** and not upgraded (`21`). No `B`/`C`/`D` was converted to `A` anywhere in the package. |
| Disclosed defect | A negative was contradicted by a root inside the package's own declared path set **twice** — `21 NC-E-05` and, in this continuation, `39 RE-12`. The classification discipline held both times (both are recorded as class `E`); the *enumeration* discipline did not. Disclosed rather than absorbed. |

## `EC-07` — Two Consecutive Clean Independent Passes

| | |
|---|---|
| **Disposition** | **NOT SATISFIED — EVIDENCE GAP** |
| Counter | **0 of 2.** See `29` for the measurement against the quoted definition. |
| Structural reason | Pass 1 (original four challenges) was not clean — new material population, 60 new findings, 7 new tolerance-zero boundaries. Even a perfectly clean pass 2 therefore gives `dirty → clean` = **one** clean pass. |
| Pass 2 outcome | Also not clean, and by a wide margin: it raised a new material population, an evidence-integrity failure (`RE-07`), and **contradicted two findings this continuation had itself published**. |
| Coverage shortfall | Pass 2 was additionally **incomplete**: only one of four commissioned challenges returned on the first attempt; three terminated on a session rate limit and were re-dispatched. See `36 §1`. |
| Blocker classification | **INTERNAL.** Not waiting on an external party. |

## `EC-08` — Final Knowledge Package Complete

| | |
|---|---|
| **Disposition** | **NOT SATISFIED — EVIDENCE GAP** (structurally complete, substantively incomplete) |
| Present | Domain semantic model, function coverage, source-of-truth register, event/state model, cross-module dependency map, control matrix, failure/edge-case register, unknown register, contradiction register, negative-claim register, evidence manifest with SHA-256, Boss decision register, clean-room design input, scope ownership matrix, gate report, repository/branch/commit lineage. |
| Missing | Jira lineage — **`NOT SUPPLIED`**, recorded rather than fabricated (`18 §2`, `38`). |
| Inherited gaps | The package inherits every gap above; a complete package cannot rest on an unbounded scope and an unconverged enumeration. |

## Summary

| Criterion | Disposition |
|---|---|
| `EC-01` Scope Bounded | NOT SATISFIED — EVIDENCE GAP |
| `EC-02` Enumeration Converged | **NOT SATISFIED — CONTRADICTION** |
| `EC-03` Unknown Exhausted | NOT SATISFIED — EVIDENCE GAP |
| `EC-04` Tolerance-Zero Closed | NOT SATISFIED — EVIDENCE GAP |
| `EC-05` Contradiction Resolution | **SATISFIED — EVIDENCE VERIFIED** |
| `EC-06` Negative Claim Controlled | **SATISFIED — EVIDENCE VERIFIED** |
| `EC-07` Two Clean Passes | NOT SATISFIED — EVIDENCE GAP |
| `EC-08` Package Complete | NOT SATISFIED — EVIDENCE GAP |

**2 of 8 satisfied — unchanged in count from the prior package, but not unchanged in substance.**
`EC-02` moved from "cannot be demonstrated for lack of runtime evidence" to "actively contradicted by
its own published findings", which is a worse position honestly arrived at. `EC-01` and `EC-03` moved
materially closer to closure with named residues. `EC-05` and `EC-06` held under a review that
specifically attacked them.

Under `§4 Module Exit Rule`, all eight must be satisfied before the module may be presented to Boss
for a Final Exit Decision. **Six are not.**
