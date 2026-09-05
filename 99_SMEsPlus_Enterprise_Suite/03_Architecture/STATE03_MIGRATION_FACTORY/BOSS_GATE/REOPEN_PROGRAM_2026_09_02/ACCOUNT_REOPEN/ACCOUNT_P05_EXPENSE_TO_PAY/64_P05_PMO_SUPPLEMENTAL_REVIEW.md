# 64 — P05 PMO SUPPLEMENTAL REVIEW

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E26`
PMO verifies **process**. PMO may not mark READY because effort was extensive.

## 1. The Twenty Verification Points

| # | Point | PMO finding |
|---|---|---|
| 1 | Evidence base reconstructed | **PARTIALLY — and its completeness claim was contradicted.** The search was filesystem-wide and still missed a 10th identity (`.zip`), misread two 100+MB archives as empty, and could not perceive **12 Docker databases including a live Odoo 18 instance** (`RE-29`). |
| 2 | Database denominator known | **NO.** At least 10 file-based identities (8 read) plus 12 container-backed. `EC-01` re-classed `NOT SATISFIED`. |
| 3 | Installed module population verified | **YES** — 7 registries incl. the v18 target (`43`) |
| 4 | Source vs deployed risk separated | **YES, and the separation defeated the author twice** — `44` carries five axes; `U-16` remains open |
| 5 | Headline findings re-ranked | **YES**, then partially **un**-ranked when the ranking evidence failed provenance |
| 6 | P01 live defects routed correctly | **YES** — `49`, narrowed and de-escalated, with the financial effect held at class `C` |
| 7 | P05 did not adjudicate P01 architecture | **YES** after correction — imperatives rewritten as routed questions (`RE-25`) |
| 8 | TX-01 denominator verified | **YES** — **358/358 = 100.00%** on the v18 target, independently reproduced |
| 9 | Screen-vs-CSV divergence verified or held | **VERIFIED** from source + ORM + data on two platforms; rendered artefacts held at class `C` |
| 10 | P07 statutory boundary respected | **YES** — zero statutory assertions found by an adversarial audit; one soft leak and one pre-answer withdrawn |
| 11 | Research errors preserved | **YES** — `RE-07`..`RE-28`, all struck through in place, none deleted |
| 12 | `R-01` lineage preserved | **YES** (`53`) — original, withdrawal, reinstatement, all on the record |
| 13 | Exit criteria recalculated | **YES** (`56`) — 2 satisfied, 3 partial, 3 not satisfied |
| 14 | Tolerance-zero recalculated | **YES** (`58`) — **13 of 13 open**; an interim closure was withdrawn within the round |
| 15 | `EC-07` honestly measured | **YES** (`59`) — **0 of 2**, counter reset a third time, **no self-certification offered** |
| 16 | v18 registry obtained or held | **OBTAINED** — `U-01` residue closed |
| 17 | **No database restore performed** | **CONFIRMED** — `-f` only, `-d` never passed; `60` records the boundary and withdraws the restore ask as unnecessary |
| 18 | No unauthorized write performed | **CONFIRMED** — no code, config, DB, module install, migration, deploy or merge |
| 19 | Vetoes accurately stated | **YES** (`63`) — both strengthened, one new |
| 20 | Checkpoint / auto-resume current | **YES** (`40`, `66`) |

## 2. What This Round Actually Did

| | |
|---|---|
| Closed the principal gating unknown (`U-01` v18 registry) | **yes** |
| Contradicted two prior-round negatives | `RE-20`, `RE-21` |
| Narrowed the P01 severity claim | `RE-22` |
| Published a headline reversal — **and withdrew it inside the same round** | `TZ-01` |
| Downgraded its own new finding unprompted | `PC-01` |
| Tolerance-zero closures | **0** |
| Exit criteria newly satisfied | **0** |

## 3. PMO's Central Observation

> **The round's two most valuable outputs are both discoveries that its own work was wrong.**

The author found a target-platform database nobody had, measured 386 of 387 petty-cash credits landing
correctly, and declared a two-round-old headline finding contradicted. An independent challenge then
established that **all 712 such entries were created on one day by the migration user in a journal
named "COA Migration 2026"** — a population that never exercised the behaviour under test.

The measurement was correct. The counting was correct. It was reproduced exactly. **And it could not
answer the question it was asked.** PMO regards the provenance check — `create_uid`, `create_date`,
journal name, one query — as the single highest-value control this programme has adopted, and notes
that **it has never been in the method-controls table until now**.

**And the second: the evidence base this round was convened to repair was itself declared complete and
was not.** Challenge A found a tenth database in a `.zip`, two 100+MB archives the round had recorded
as empty, and **a live Odoo 18 instance running in Docker** — none reachable by a filename search.
`EC-01` moved **backwards** as a result, from an interim `PARTIAL` to `NOT SATISFIED`.

PMO notes, as a positive process signal, that after Challenge C landed the author applied the same
standard **unprompted** to `PC-01`, a finding it had just published and which the challenge had
explicitly let stand; and that both withdrawn interim judgements (`TZ-01` closure, `EC-01` partial)
were withdrawn **inside the round**, not carried forward.

## 4. Recommendation

> ### PMO RECOMMENDS: **`HOLD`**
>
> P05 must **not** be declared `READY FOR CORE ACCOUNTING RECONCILIATION`.

Process grounds:

1. **Six of eight exit criteria unsatisfied** (`EC-01` now among them, having moved backwards); `EC-02` and `EC-07` are method failures, not evidence gaps.
2. **13 of 13 tolerance-zero boundaries open, zero closed.**
3. **Four of ten handoff elements blocked**, and one moved *backwards* this round.
4. **`EC-07` counter reset a third time.** Three consecutive rounds each discovered a population the
   previous lacked. The evidence base has not stabilised.
5. **`U-16` unresolved** — no source-only finding is demonstrably about deployed code.
6. **The evidence population is still not bounded** (`RE-29`), and **two live Odoo 18 databases sit
   unexamined** for want of connection authorisation (`U-20`).

**PMO's one operational recommendation:** the live `occ-odoo18-db` / `occ-odoo18-webtest` pair is the
shortest path to the live-posting evidence that `TZ-01`, `PC-01`'s cause and `U-16` all require.
Obtaining read authorisation for it would close more of this package than any further file analysis.

**What PMO does endorse for immediate action, independent of P05's gate:**

- **`TX-01`** is reliable and should go to **P07** now (`51`).
- The **P01** routing (`49`) is sound in its corrected, de-escalated form and should go now.
- The **Layer 1 design input** (`17 §6`) is Boss-decidable now; it depends on no reach classification.

**What PMO explicitly does not endorse:** any use of this package's exposure or reach classifications
as settled input, per `AASV-03`.
