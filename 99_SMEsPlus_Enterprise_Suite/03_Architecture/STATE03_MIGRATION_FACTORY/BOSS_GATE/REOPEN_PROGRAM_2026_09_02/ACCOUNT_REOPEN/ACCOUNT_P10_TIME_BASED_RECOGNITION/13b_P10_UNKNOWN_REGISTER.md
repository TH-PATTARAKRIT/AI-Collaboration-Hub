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

## Unknowns Added by the Cross-Process Reconciliation

| # | Unknown | Disposition | Gating? | Justification |
|---|---------|-------------|---------|---------------|
| `P10-U-19` | What is the authoritative `P01`–`P11` process taxonomy? | `BOSS DECISION REQUIRED` — `P11` `D-2` already names it | **NON-GATING for P10's findings, GATING for any cross-process routing** | `P11-F-04`: the taxonomy does not exist in the canonical repository. P10 mis-routed its entire dependency register because of this (`P10-R-09`) |
| `P10-U-20` | Does any entry in the deployed archives carry a date inconsistent with its own schedule? | `ROUTED` — a query over the readable archives, not yet run | **NON-GATING** but it is the cheapest remaining evidence that would show whether the re-dating has actually occurred in the estate | Obtainable today with tooling already used this session |
| `P10-U-21` | Do P10's scope determinations agree with `P04`'s and `P08`'s? | `ROUTED TO P11`, which owns cross-process scope reconciliation | NON-GATING for P10 | **Class `C` — NOT COMPARED.** The peer scope matrices were not read line by line; the extraction agents commissioned for it did not complete |
| `P10-U-22` | Does the accounting-event object, once authored under `D-5`, accommodate the anchor taxonomy in `27` §2? | `ROUTED` — cannot be tested before the object exists | **GATING for `P10-D-01`** | `P10-D-01` is now sequenced behind `D-5` |

Revised summary: **22 material unknowns, all dispositioned, none unclassified. Gating: 9.**


## Corrections and Additions From the Fresh Challenge Round

| # | Unknown | Disposition | Change |
|---|---------|-------------|--------|
| `P10-U-16` | What does the fourth deployed archive contain? | **CLOSED** | It opens with a tool already installed. Contents read: deferral structures present, transfer model absent, **four lock dates set**, one company, 12 asset schedules, zero deferral entries |
| `P10-U-20` | Has any deployed entry been re-dated? | **PARTIALLY CLOSED, and the routing was wrong** | The decisive column had already been extracted by P10's own script and never read (`34` `W-34`). Three archives carry no lock, so the lock path cannot have fired there. The fourth carries locks and its entry dates have **not** been queried — that part remains open |
| `P10-U-01`, `P10-U-02` | Executing reproduction of the two company-boundary defects | **RE-CLASSED** | The premise "this session has no runtime access" was **never tested**; tooling and initialised data directories are present. `C — NOT ATTEMPTED` |
| `P10-U-23` | *new* — the second, **lock-free** re-dating path a peer records, triggered by a document-date change | `PEER DEPENDENCY OPEN`, routed to `P08` and the raising peer | **GATING for the completeness of `P10-D-02`.** Every option in `28` is framed around the lock; a ruling scoped to the lock path would leave this path untouched |
| `P10-U-24` | *new* — is the lock-exception route available on the older estate line? | `ROUTED` | The object is absent from that line's schema, so Option E may be unavailable on part of the estate |
| `P10-U-25` | *new* — what does the deployed estate's own installed-module manifest bound? | `ROUTED` | An artefact on the host carries the authoritative installed-module list, which would reduce a surface currently routed as `C — NOT SEARCHED` to a named, countable set |

Revised summary: **28 material unknowns. 1 closed, 1 partially closed, 3 re-classed, 5 added. Gating: 10.**
