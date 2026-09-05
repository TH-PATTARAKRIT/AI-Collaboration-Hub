# 56 — P05 EXIT CRITERIA V2

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E17`
Supersedes `27`. Every criterion re-derived from its own definition.

| ID | Definition (abridged) | Current evidence | **Status** | Peer dep. | External blocker | P05 can resolve alone? |
|---|---|---|---|---|---|---|
| `EC-01` | Scope bounded; verified denominators | **Materially advanced but NOT bounded.** 8 registries read incl. **two** Odoo 18 databases. But the population claim failed a third time (`RE-29`): 2 archives misread as empty, 1 Odoo 18 `.zip` outside the pattern, and **12 Docker-backed databases including a live Odoo 18 instance** invisible to any filename search. | **NOT SATISFIED — EVIDENCE** | no | container access | partly — `iSMEs182`/`iErpOCC`/`iSCErP` are readable now; the live containers need authorisation |
| `EC-02` | Enumeration converged; material-delta stability | **Not converged.** This round contradicted a Round-2 reclassification of a Round-1 headline finding — the third position on `TZ-01`. Four new research errors. | **NOT SATISFIED — METHOD** | no | no | no — needs two stable passes |
| `EC-03` | Unknowns exhausted, all dispositioned | 18 unknowns dispositioned; **`U-01` CLOSED**. Gating: `U-02b`, `U-03`, `U-09`, `U-16`. | **PARTIAL — EXACT GAP** | P07 (`U-09`) | runtime | partly |
| `EC-04` | Tolerance-zero closed | **1 of 13 closed** (`TZ-01`, by disproof). 12 open. | **NOT SATISFIED — DEPLOYMENT/RUNTIME/PEER** | P01, P08 | runtime | no |
| `EC-05` | Contradictions dispositioned with lineage | 17 research errors + 20 typed contradictions, **all preserved struck-through in place**, none silently rewritten. `TZ-01`'s three successive positions are all on the record. | **SATISFIED — EVIDENCE VERIFIED** | no | no | yes |
| `EC-06` | Negative claims controlled | Every negative carries root + pattern + unit + class. **Two class-E reversals this round were self-declared** (`RE-20`, `RE-21`). No B/C/D upgraded to A. | **SATISFIED — EVIDENCE VERIFIED** | no | no | yes |
| `EC-07` | Two consecutive clean independent passes | **0 of 2.** See `59`. | **NOT SATISFIED — METHOD** | no | no | no |
| `EC-08` | Final knowledge package complete | All mandated artefacts present (66 files). Jira `NOT VERIFIED`. Inherits the gaps above. | **PARTIAL — EXACT GAP** | no | Jira | partly |

## Summary

| Status | Criteria |
|---|---|
| **SATISFIED — EVIDENCE VERIFIED** | `EC-05`, `EC-06` — **2** |
| **PARTIAL — EXACT GAP** | `EC-03`, `EC-08` — **2** |
| **NOT SATISFIED** | `EC-01` (evidence), `EC-02` (method), `EC-04` (deployment/runtime/peer), `EC-07` (method) — **4** |

**Movement against `27`:** `EC-03` improved to `PARTIAL` — the v18 registry hold that blocked it is
closed. `EC-01` **stayed at NOT SATISFIED**: an interim draft of this file had it at `PARTIAL`, which
was withdrawn when Challenge A contradicted the population claim (`RE-29`). `EC-04` gained no closure —
an interim `TZ-01` closure was also withdrawn. `EC-02` and `EC-07` are **further from satisfaction**,
not closer.

**Two of this file's own interim judgements were withdrawn inside the round.** That is recorded rather
than smoothed, and it is the substance of `EC-02`'s `NOT SATISFIED — METHOD`.

Under the Module Exit Rule all eight must be satisfied. **Six are not.**
