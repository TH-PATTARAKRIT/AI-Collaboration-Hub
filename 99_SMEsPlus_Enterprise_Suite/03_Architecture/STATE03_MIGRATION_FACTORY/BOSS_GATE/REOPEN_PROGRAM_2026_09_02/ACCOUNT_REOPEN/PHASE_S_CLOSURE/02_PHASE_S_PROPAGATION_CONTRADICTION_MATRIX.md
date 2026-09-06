# 02_PHASE_S_PROPAGATION_CONTRADICTION_MATRIX

**Session** `[SMEPLUS-26-09-06-ACC-P06-P08-P09-P11-PHASE-S-CLOSURE-001]` · branch `audit/account-phase-s-closure-2026-09-06-001`

## Disposition: CONSUMED BY REFERENCE — NOT RE-AUTHORED

| | |
|---|---|
| **Authoritative artefacts** | `03_CROSS_PXX_HANDOFF_AND_PROPAGATION_MATRIX.md` and `04_VERIFIER_AUTHORED_DEFECT_SEPARATION_REGISTER.md` |
| **Branch** | `audit/account-xrecon-2026-09-06-001` |
| **Commit SHA** | `32912109d37117aae1e91cb612c36c67c9be70a4` |
| **Paths** | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/ACCOUNT_XRECON_2026_09_06/03_CROSS_PXX_HANDOFF_AND_PROPAGATION_MATRIX.md` · `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/ACCOUNT_XRECON_2026_09_06/04_VERIFIER_AUTHORED_DEFECT_SEPARATION_REGISTER.md` |

Rationale for consumption rather than re-authoring is stated in `01_` and applies identically.

## Live propagation edges carried into the correction queue

**Index of edges the parent session established. No new propagation claim is made here.**

| Edge | From | To | Status | Queue coupling |
|---|---|---|---|---|
| **`XRD-011`** — *"3 at 1e-7"* | **P08** `58_`:13 | **P11** `F-02`:15, `CI-01`:124, dispositions `:106` | **LIVE — P11 does not yet know** | `Q-P08-01` **must notify** → `Q-P11-04` |
| **`XRD-006`** — `HO-` namespace | **P08** `25_`/`54_`/`58_`; **P06** `HO-01`…`HO-06` | **P11** citations incl. `:148` | **LIVE** — `HO-nn` does not resolve to one producer | `Q-P08-02` + `Q-P11-02`, **must not cross** |
| **`XRD-005`** — stale peer SHA pins | **P11** live outbound registers | P06 / P08 / P09 | **LIVE** — 3 peers pinned at CORR2 heads | `Q-P11-01` |
| **`XRD-008`** — superseded P09 reading | **P11** `B-38` | **P09** @ `92de8a1` | **LIVE** — P09's L1–L8 limb superseded at `4778792` | `Q-P11-03` |
| **`XRD-003`** — wrong count families | **P06** `18_`, `70_` | **P11** | **LIVE in the handoffs**; measured **not** to have crossed into P11's substance | `Q-P06-03` + downstream notification |
| **P07 edge** | P11 `B-36`, `B-39` | **P07** `ee2be30` | **NEVER OPENED across three rounds** | **routed, not queued** — see `05_` criterion 8 |

## Contradictions standing, unresolved

| # | Contradiction | Both sides live? |
|---|---|---|
| 1 | **P06 IEV publishes 18/15/3-of-4 and 25/2/19/4-of-4** | **YES** — in the same commit `b423eff`. Independently re-confirmed here |
| 2 | **P06 instrument register `:45` says 65 and `:54` contradicts it** | **YES** — measured truth is 67 |
| 3 | **P08 `25_` and `54_` publish different sets under identical `HO-` ids** | **YES** |
| 4 | **P08 IEV `:317` cites requirements 2 and 4; `:339` says requirement 2 is unaffected** | **YES** — the FX repair carries no valid number |
| 5 | **`Q-BOSS-01` names two different questions on two branches** | **YES** — raised by this session as `PF-03`, `00_` §5.1 |

## Measured negatives — each against a positive control

**Carried forward from the parent session because a negative is a claim.** Not re-derived here; no owner
reference moved, so each remains current.

| Negative | Control |
|---|---|
| P06's wrong counts did **not** cross into P11's substance | positive control present |
| P08's 19 and P11's 19 Boss decisions are **distinct families** | enumerated separately, **never netted** |
| The 13-vs-14 handoff row conflict is **two populations, not a defect** | enumerated |

**No package may be declared clean while any edge above is LIVE.** Six are.
