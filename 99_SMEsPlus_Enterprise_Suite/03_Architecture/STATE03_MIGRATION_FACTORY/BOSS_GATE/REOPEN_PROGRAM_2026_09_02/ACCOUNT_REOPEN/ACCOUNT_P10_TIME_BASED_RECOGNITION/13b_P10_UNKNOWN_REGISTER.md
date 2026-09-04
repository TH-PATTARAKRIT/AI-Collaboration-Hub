# P10 — UNKNOWN REGISTER

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1
Issued under `EC-03`: every material unknown carries a final disposition. **No unclassified gating unknown remains.**

Permitted dispositions: `CLOSED` · `NON-GATING` · `ROUTED TO LATER WAVE/STATE` · `OUT OF SCOPE WITH EVIDENCE` · `BOSS DECISION REQUIRED`.

---

| # | Unknown | Disposition | Gating? | Justification |
|---|---------|-------------|---------|---------------|
| `P10-U-01` | Does the allocation-policy scope defect manifest at runtime as predicted? | `ROUTED` — **executing** reproduction required | **GATING** for the tolerance-zero assessment | The code path is verified; the observable consequence is not. **Partially bounded by deployed evidence (`22`):** all 44 companies in both databases carrying the function hold one identical configuration, so the divergence cannot manifest today and would appear on the first setting change. The defect is intact; the realised exposure is currently nil. |
| `P10-U-02` | Under which chart configuration does the multi-company grouped generation post rather than refuse? | `ROUTED` — **executing** reproduction under both configurations | **GATING** | **Partially closed by deployed evidence (`22`):** both databases have the shareable many-to-many chart shape and **no scalar company column at all**, but only 1 account of 544 in one database and 0 of 544 in the other actually belong to more than one company. On today's data the defect would most likely fail loudly. The safer branch remains an accident of configuration, and one shared account already exists. See `P10-C-02`. |
| `P10-U-03` | Do asset pause, resume, revaluation and disposal produce duplicate recognition? | `ROUTED TO LATER WAVE` — five named methods were listed and not read | **NON-GATING for P10**, gating for the Asset programme | P10's scope is the kernel question; the asset object's own lifecycle belongs to the Asset programme. Recorded as `NC-16`, class `C`. |
| `P10-U-04` | Do localisation modules alter time-based recognition? | `ROUTED` | NON-GATING for the design decision | No localisation module was examined. Recorded as `NC-17`, class `C`. |
| `P10-U-05` | Which of the two same-build reference roots is deployed? | `ROUTED` to the Migration track | NON-GATING for P10 | This package declares its root and bounds every claim to it. |
| `P10-U-06` | Are the deferral window fields editable on a posted document at runtime? | `ROUTED` — reproduction | NON-GATING | The absence of a Python-level guard is verified; the runtime editability is not. `NC-20`, class `D`. |
| `P10-U-07` | Is a shared chart of accounts permitted in SMEsPlus? | `BOSS DECISION REQUIRED` | **GATING** for `P10-S-02`'s severity, not for its existence | Architectural choice, not a research question. `P10-SQ-03`. |
| `P10-U-08` | May a tenant bind an allocation convention across its companies? | `BOSS DECISION REQUIRED` | NON-GATING for the kernel shape | `P10-SQ-01`, decision `P10-D-04`. |
| `P10-U-09` | Does SMEsPlus require daily recognition as a grid, not merely as a weighting? | `BOSS DECISION REQUIRED` | **GATING** for the kernel's period-grid design | Business requirement, not discoverable from the reference product. |
| `P10-U-10` | Must prepaid expense be presented separately from deferred charge under Thai requirements? | `ROUTED TO ACCOUNTING-TAX` (`P07`) | NON-GATING for the kernel; gating for presentation | `HOLD / EVIDENCE REQUIRED`. `P10-C-05`. |
| `P10-U-11` | Does a reversing accrual crossing a tax period create a divergence between the accrual basis of taxable income and of accounting? | `ROUTED TO ACCOUNTING-TAX` (`P07`) | NON-GATING for P10 | `HOLD / EVIDENCE REQUIRED`. `P10-C-06`. |
| `P10-U-12` | Who owns the accrual event — P10, or the order processes? | `BOSS DECISION REQUIRED` | **GATING** for the kernel's boundary | Cannot be settled by evidence; both assignments are coherent. Decision `P10-D-03`. |
| `P10-U-13` | Is the recognition grid the fiscal calendar or the civil calendar? | `BOSS DECISION REQUIRED`, jointly with `P04` | **GATING** | The reference behaviour is civil unconditionally; SMEsPlus has not chosen. |
| `P10-U-14` | May a posting constraint alter a recognition period? | `BOSS DECISION REQUIRED`, jointly with `P04` | **GATING** — this is the kernel's load-bearing element | P10's position is that it may not. See `10` `X-05`. |
| `P10-U-15` | Is the exact count of time-based mechanisms in the reference root knowable with the patterns available? | `OUT OF SCOPE WITH EVIDENCE` | NON-GATING | A floor is sufficient for every use this package makes of it. Asserting a total is prohibited. `NC-01`, class `D`. |

## Summary

| Disposition | Count |
|-------------|-------|
| `BOSS DECISION REQUIRED` | 6 |
| `ROUTED` (runtime, later wave, or Accounting-Tax) | 8 |
| `OUT OF SCOPE WITH EVIDENCE` | 1 |
| `CLOSED` | 0 |
| **Unclassified** | **0** |

**Gating unknowns: 7** (`U-01`, `U-02`, `U-07`, `U-09`, `U-12`, `U-13`, `U-14`). None is routed to a later wave to conceal a blocker belonging to this scope: five are Boss decisions that research cannot resolve, and two require runtime access this session does not have.

## Unknowns Added by the Deployed-Evidence Correlation (`22`)

| # | Unknown | Disposition | Gating? | Justification |
|---|---------|-------------|---------|---------------|
| `P10-U-16` | What time-based recognition mechanisms exist in the fourth deployed archive? | `ROUTED` | NON-GATING | The host's tooling cannot open its archive format. Class `C`, NOT SEARCHED. **Not an absence.** |
| `P10-U-17` | Why is one deployed database on a different product line, with no deferral structure and a periodic-transfer mechanism the others lack? | `ROUTED TO MIGRATION` | **GATING for migration, not for P10 design** | The estate is not uniform. Any migration plan assuming one mechanism set is wrong. `P10-F-37`. |
| `P10-U-18` | Will any company diverge from the single estate-wide configuration, and under whose authority? | `BOSS DECISION REQUIRED` | NON-GATING today, gating the moment it happens | The allocation-policy scope defect is dormant only because all 44 companies are identically configured. |

Revised summary: **18 material unknowns, all dispositioned, none unclassified. Gating: 8.**
