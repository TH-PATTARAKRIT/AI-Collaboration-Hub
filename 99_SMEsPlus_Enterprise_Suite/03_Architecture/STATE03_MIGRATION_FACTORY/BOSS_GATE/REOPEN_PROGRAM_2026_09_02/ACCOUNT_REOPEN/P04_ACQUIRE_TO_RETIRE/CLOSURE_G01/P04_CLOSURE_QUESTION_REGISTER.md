# P04 — CLOSURE QUESTION REGISTER (G01)

**LAYER 2 — AUDIT QUARANTINE.** Prompt §7 / §15. One terminal disposition each. No `OPEN`.

**Source basis: series 18 reference tree + `18.0.x` custom addons. Runtime basis: per identity,
series named. The v16 deployment's source is unobtainable on this host (`MD-P04-01`).**

---

| CQ | Subject | Terminal disposition | Where |
|---|---|---|---|
| **CQ-P04-01** | Asset Model → Asset policy inheritance | **FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE** *(headline disproved by own disproof pass and reissued narrower)* | `P04_ASSET_MODEL_INHERITANCE_TRACE.md` |
| **CQ-P04-02** | Depreciation date / day convention | **FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE** (implementation + deployed usage). Statutory limb **CROSS-PROCESS OWNER — P07** | `P04_DEPRECIATION_DAY_CONVENTION_CLOSURE.md` |
| **CQ-P04-03** | Asset ↔ Equipment relationship | **FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE** | `P04_ASSET_EQUIPMENT_RELATIONSHIP_TRACE.md` |
| **CQ-P04-04** | Equipment without Asset | **FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE** | `P04_NON_ASSET_EQUIPMENT_BOUNDARY.md` |
| **CQ-P04-05** | Active-period depreciation attribution | **BOSS DECISION REQUIRED — DECISION PACKAGE READY** (`BLK-07`, `P04-BD-05`); factual half FACT VERIFIED | `P04_ACTIVE_DEPRECIATION_ATTRIBUTION_MATRIX.md` |
| **CQ-P04-06** | Post-depreciation internal usage | **BOSS DECISION REQUIRED — DECISION PACKAGE READY**; factual half FACT VERIFIED, one route closed by `P04-F-154` | `P04_POST_DEPRECIATION_INTERNAL_USAGE_MODEL.md` |
| **CQ-P04-07** | Operation → specific Equipment | **FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE**; design question **BOSS DECISION REQUIRED** | `P04_OPERATION_EQUIPMENT_CAUSALITY_INTERFACE.md` |
| **CQ-P04-08** | Maintenance / non-productive cause | **FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE** (negative, denominator declared); repair-expense limb **CROSS-PROCESS OWNER — P05** | `P04_MAINTENANCE_NONPRODUCTIVE_CAUSE_MATRIX.md` |
| **CQ-P04-09** | Analytic bridge | **FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE** | `P04_ANALYTIC_BRIDGE_TRACE.md` |
| **CQ-P04-10** | Disposal / derecognition / residual | **FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE** | `P04_DISPOSAL_DERECOGNITION_TRACE.md` |
| **CQ-P04-11** | Scope / multi-company / access | **FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE**, one asymmetry routed as `P04-B-54` | `P04_SCOPE_OWNERSHIP_MATRIX.md` |
| **CQ-P04-12** | Evidence integrity / terminality | **FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE** for the version-basis test; residual source gap **UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE** (`P04-B-51`) | `P04_DEPLOYED_CODE_IDENTITY_DELTA.md`, `P04_CHECKPOINT_REGISTER_G01.md` |

## Derived subquestions — each terminally dispositioned

| ID | Subquestion | Disposition |
|---|---|---|
| `P04-B-51` | A series-16 addons tree for the v16 deployment | **UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE.** Not repairable by searching; P03 enumerated with a 28×-firing control |
| `P04-B-52` | Day-count inclusivity: per-period `+1` vs lifetime without it | **UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE** here; function named, bounded, not opened (would widen) |
| `P04-B-53` | Runtime count: equipment referenced by >1 asset; expensed-and-capitalised overlap | **UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE** in a source-scoped run; registered |
| `P04-B-54` | `ir.rule` company restriction on `maintenance.equipment` | **UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE**; stated as a question, not a hole |
| `P04-B-55` | Any deployed custom module creating assets programmatically with `model_id` | **UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE**; decides whether `P04-F-145` is latent or live |
| — | Per-line rounding policy of the depreciation board | **OUT OF SCOPE — ROUTED WITH EVIDENCE.** Not required by `CQ-P04-02`; opening it widens the run |
| — | UI reachability of `name_asset`; degraded label from removed `name_get` | **OUT OF SCOPE — Class E.** Cannot change an accounting conclusion |

## Inherited blockers — status unchanged by this run

| ID | Status |
|---|---|
| `BLK-01` day convention | **ANSWERED-NOT-CLOSED** — measured twice; statutory limb P07-owned |
| `BLK-07` allocation denominator | **BOSS DECISION REQUIRED** — untouched; P03 routed it back here |
| `P04-BD-05`…`P04-BD-09` | **BOSS DECISION REQUIRED** — recommendations on file, none approved |
| `P04-B-47`, `P04-B-48` | unchanged — one execution and one archive recovery, both Boss-gated |

> **0 of 4 inherited blockers closed by this run.** **Seven** new blockers registered,
> `P04-B-49` through `P04-B-55`, each with a named owner or dependency and none left vague.

## Findings issued in this closure

Definition rows, so every identifier resolves under the standing sweep without widening a
check to accommodate the prose that introduced it.

| ID | Finding | CQ |
|----|---------|----|
| `P04-F-145` | Model policy is an action **three call sites** perform, not a property of the record; `create()` applies nothing. **First form withdrawn** after its own disproof | 01 |
| `P04-F-146` | **Ten snapshot fields and one live field** on the same object — the not-depreciable percentage tracks the model for life, the other ten do not | 01 |
| `P04-F-147` | The non-daily branch is **not 30/360** — boundary months are scaled by their real length; only the interior is synthetic | 02 |
| `P04-F-148` | `equipment_sequence` **installs only because the breaking file is never imported** — 3 of 8 model files unregistered. *Source present ≠ registered* | 03 |
| `P04-F-149` | The equipment link is repointable at any time and the `eqp → tass` transition **has no reverse anywhere** — 4 writes one way, 0 back | 03 |
| `P04-F-150` | Operational equipment is created by **validating a goods receipt**; nothing in that path touches asset accounting | 04 |
| `P04-F-151` | Expense-then-capitalise is **unprevented by construction**; frequency **not measured** (`P04-B-53`) | 04 |
| `P04-F-152` | Maintenance cost is a **statistical float** — zero references to `account.move` or `account.analytic` in the whole module | 04, 08 |
| `P04-F-153` | The analytic distribution is written to **every line** of the depreciation entry → nets to zero; draft moves only | 09 |
| `P04-F-154` | **`account.asset` cannot post off-balance** — all three account fields exclude the type by domain. Closes one route to a Boss policy input | 09, 06 |
| `P04-F-155` | **Two fiscal-lock behaviours in one module** — disposal raises, account re-assignment silently skips | 10 |
| `P04-F-156` | Company scope is **asymmetric** between `model_id` and `name_asset`; stated as a question (`P04-B-54`), not a hole | 11 |
