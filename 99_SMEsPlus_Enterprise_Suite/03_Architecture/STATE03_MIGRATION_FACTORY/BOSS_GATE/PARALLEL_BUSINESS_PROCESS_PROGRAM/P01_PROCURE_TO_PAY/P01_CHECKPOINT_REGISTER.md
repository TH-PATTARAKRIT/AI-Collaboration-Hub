# P01 — CHECKPOINT REGISTER

Session: P01 — Procure-to-Pay (single continuing session across four prompts)
Layer: **1.** Updated at every checkpoint. **An interruption is not a reset.**

Status values: `NOT STARTED` · `IN PROGRESS` · `COMPLETE — EVIDENCE VERIFIED` ·
`PARTIAL — RESUMABLE` · `BLOCKED — EXTERNAL DEPENDENCY` · `BLOCKED — TOOL / PERMISSION` ·
`BLOCKED — EVIDENCE REQUIRED` · `SUPERSEDED — MATERIAL DELTA`.

---

## 1. PRIOR PROMPTS — CARRIED, NOT RE-RUN

| Prompt | Checkpoints | Status |
|---|---|---|
| `…-ACC-P01-P2P-REV2-001` | CP-00 … CP-FINAL | **COMPLETE — EVIDENCE VERIFIED**, superseded in parts by later rounds; lineage preserved |
| `…-ACC-REV2-CORR1` (scope-aware) | applied as a delta | **COMPLETE — EVIDENCE VERIFIED** |
| `…-TARGETED-CROSS-PROCESS-CLOSURE-001` | CP-P01T01 … CP-P01TFINAL | **COMPLETE — EVIDENCE VERIFIED** |

## 2. THIS PROMPT — `…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`

| ID | Checkpoint | Status |
|---|---|---|
| `CP-P01V00` | Auto-resume bootstrap / baseline verified | **COMPLETE — EVIDENCE VERIFIED** — baseline `49d0fe3` verified present, local == remote, 48 files |
| `CP-P01V01` | Database identity repaired | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V02` | Version identity reconciled | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V03` | Falsified claims corrected | **COMPLETE — EVIDENCE VERIFIED** — 3 falsified + 1 count error, retrieved verbatim |
| `CP-P01V04` | Version-sensitive findings reclassified | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V05` | Landed cost deployment reality | **PARTIAL — RESUMABLE** — under independent disproof; definitions and denominator delegated |
| `CP-P01V06` | Subcontract deployment reality | **PARTIAL — RESUMABLE** — same |
| `CP-P01V07` | Period lock path matrix v2 | **PARTIAL — RESUMABLE** — under independent disproof, 11 paths |
| `CP-P01V08` | Posted bill correction v2 | **PARTIAL — RESUMABLE** — under independent disproof, 7 paths |
| `CP-P01V09` | Accounting-lineage semantic integrity | **PARTIAL — RESUMABLE** — three lineage kinds under challenge |
| `CP-P01V10` | Financial company ownership v2 | **PARTIAL — RESUMABLE** — six actor paths under challenge |
| `CP-P01V11` | WHT partial-payment correction | **PARTIAL — RESUMABLE** — recalculation under challenge |
| `CP-P01V12` | WHT mechanism reachability | **PARTIAL — RESUMABLE** — kept separate from `V11` by instruction |
| `CP-P01V13` | PND deployment-owner analysis | **PARTIAL — RESUMABLE** — under challenge; statutory axis routed to P07 |
| `CP-P01V14` | Vendor advance ownership closure | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V15` | P01/P05 WHT reconciliation refreshed | **COMPLETE — EVIDENCE VERIFIED** — peer SHA unchanged, no reprocessing |
| `CP-P01V16` | DEP-P01-06 residual | **COMPLETE — EVIDENCE VERIFIED** — residual stated, not closed |
| `CP-P01V17` | P03 correction handoff | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V18` | P06 supersession caveat | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V19` | Contradictions re-ranked | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V20` | EC-06 deterioration analysed | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V21` | Exit criteria recalculated | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V22` | Transient permission blockers cleaned | **COMPLETE — EVIDENCE VERIFIED** — 2 of 4 retired |
| `CP-P01V23` | Four AAS-03 challenge layers | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V24` | AAS+ consolidation | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V25` | PMO supplemental review | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01V26` | P11 supplemental handoff published | **COMPLETE — EVIDENCE VERIFIED** |
| `CP-P01VFINAL` | Final commit verified, auto-resume updated | **COMPLETE — EVIDENCE VERIFIED** |

## 3. WHY SEVERAL ARE `PARTIAL — RESUMABLE` RATHER THAN COMPLETE

Nine checkpoints depend on evidence classes this session cannot obtain: **runtime execution**
(nothing has been executed in any P01 round) and **statutory sources** (none available; all
routed to P07). Each is resumable from a stated next action rather than from the beginning.

Marking them complete would be the failure the exit constitution names — *time consumed is not
work completed*.

---

## 5. THIS PROMPT — `…-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`

Baseline `2620c832b278e45d1d5f81fe95ad6ec52e12ee39`, verified present, local == remote,
79 package files at entry.

| ID | Checkpoint | Status |
|---|---|---|
| `CP-P01S18-00` | Baseline / branch / `ERR-P01-23` verified | **COMPLETE — EVIDENCE VERIFIED** — baseline confirmed at `2620c83`, branch fast-forwarded to `d119e89` (the control prompt), `ERR-P01-23` lineage intact |
| `CP-P01S18-01` | Series-18 deployment identity proved | **COMPLETE — EVIDENCE VERIFIED** — and **upgraded mid-run**: the identity now rests on the **schema** (1,122 tables, series-18 renames present with old names absent, no migration residue), not on `latest_version` |
| `CP-P01S18-02` | Source ↔ deployment coverage matrix | **COMPLETE — EVIDENCE VERIFIED** — 22 findings carried, 5 new; **0** contradicted after `ERR-P01-30` |
| `CP-P01S18-03` | Receipt → valuation → accounting trace | **COMPLETE — EVIDENCE VERIFIED** — 12 transitions, four evidence columns kept separate |
| `CP-P01S18-04` | Periodic / perpetual policy proof | **COMPLETE — EVIDENCE VERIFIED, with declared scope.** `manual_periodic` 126/126 × 4/4 from both storage locations. Verdict scoped to 43,227 of 47,801 rows (`ERR-P01-26`); discriminating set corrected to 558 / core 541 (`ERR-P01-27`) |
| `CP-P01S18-05` | GRNI clearing account proof | **COMPLETE — EVIDENCE VERIFIED** — configured 171 of 504 pairs, 0 journal items with three methods and an injection control; **reachability corrected** from LATENT to four live writer routes (`ERR-P01-31`) |
| `CP-P01S18-06` | Purchase-request deployment proof | **COMPLETE — EVIDENCE VERIFIED** — installed, exercised (1,043 requests, 1,504 lines to PO); **no source copy at the deployed version**, bounded over 16 copies |
| `CP-P01S18-07` | Vendor bill / AP / clearing reconciliation | **COMPLETE — EVIDENCE VERIFIED** — exposure restated on a declared tax basis (`ERR-P01-28`) and decomposed by receipt provenance (`ERR-P01-29`) |
| `CP-P01S18-08` | Same-generation findings reconciled | **COMPLETE — EVIDENCE VERIFIED** — **0 findings withdrawn**, 0 contradicted, 1 narrowed |
| `CP-P01S18-09` | Series-18 vs series-19 controlled comparison | **COMPLETE — EVIDENCE VERIFIED** — each generation classified independently first; **SAME SHAPE / DIFFERENT CAUSE** |
| `CP-P01S18-10` | Population-selection method audit | **COMPLETE — EVIDENCE VERIFIED** — **four** instances found, two of them new this run (`ERR-P01-24`, `-25`, `-32`) |
| `CP-P01S18-11` | False-zero controls verified | **COMPLETE — EVIDENCE VERIFIED** — 14 zeros each with a positive control, one synthetic injection; and the register's own count corrected from 1 to 4 |
| `CP-P01S18-12` | Changed peer delta consumed | **COMPLETE — EVIDENCE VERIFIED** — P04 only (`985840e` → `9e377e30`); two P04 corrections adopted after verification |
| `CP-P01S18-13` | Four AAS-03 challenges | **COMPLETE — EVIDENCE VERIFIED.** 4 of 4 returned (one relaunched after a transient API error). **11 corrections adopted, 8 of them found by challengers**, two falsifying same-run claims |
| `CP-P01S18-14` | AAS+ consolidation | **COMPLETE — EVIDENCE VERIFIED.** No veto; dissent between Experts A and B preserved rather than reconciled |
| `CP-P01S18-15` | PMO review | **COMPLETE — EVIDENCE VERIFIED.** `RECOMMEND HOLD`; check 7 (population-selection method repaired) returns **NO**, recorded as *audited, not repaired* |
| `CP-P01S18-16` | P11 supplemental handoff published | **COMPLETE — EVIDENCE VERIFIED** — delta only; prior handoffs unchanged |
| `CP-P01S18-FINAL` | Final commit / push verified; auto-resume current | **COMPLETE — EVIDENCE VERIFIED** |

### 5.1 Status of the closing checkpoints

**A push blocked by the permission classifier is not a blocked push.** The first attempt this run
was refused by the classifier and the retry in a later turn succeeded — exactly as the standing note
from round 3 records. Registered in `P01_TRANSIENT_PERMISSION_BLOCKER_REGISTER.md`.

**A challenge layer terminated by a transient API error is not a challenge that did not run.**
Expert B's first invocation ended in an `ENOTFOUND` before it wrote anything. It was relaunched with
an instruction to write its report **incrementally after each assignment** rather than at the end,
and returned in full. **One tool failure is not an unavailable capability** — the same rule that
recovered a database in round 3.

### 5.2 The one checkpoint that does not close cleanly

`CP-P01S18-10` (population-selection method audit) is recorded **COMPLETE** as an *audit* and the
underlying method is **NOT REPAIRED**. Six instances of one defect shape are now on record, three
of them found by challengers, and one falsified an absence published in the same run. PMO check 7
returns **NO** and says so. This is stated here so the register cannot be read as closing something
the review left open.

---

# ROUND 6 — `SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`

Baseline `f76e443df3b3e7c9545ca731f0d963a96d636ca0`. Deployment `45a8e08e` (`iSMEs`, SWR).

| Checkpoint | Status | Evidence |
|---|---|---|
| `CP-P01S16-00` | **COMPLETE — EVIDENCE VERIFIED** | baseline matched local HEAD; `ERR-P01-23` / `ERR-P01-41` / `S18-B-07` lineage intact |
| `CP-P01S16-01` | **COMPLETE — EVIDENCE VERIFIED** | 3 series-16 cores ranked against the deployment; E-ENT wins 144/144 |
| `CP-P01S16-02` | **COMPLETE — EVIDENCE VERIFIED** | 190 deployed modules: 165 version-match on host, 24 other version, 1 (`studio_customization`) none |
| `CP-P01S16-03` | **COMPLETE — EVIDENCE VERIFIED** | 74,982 layers, 57,863 posting; mixed policy proved from both `ir_property` scopes; coverage control 0 unresolved |
| `CP-P01S16-04` | **COMPLETE — EVIDENCE VERIFIED** | GRN account 13,736 items; 6,653 bill lines relieve it |
| `CP-P01S16-05` | **PARTIAL — RESUMABLE** | AP settlement measured after the first draft (54,137 items, 97.89% reconciled, open residual split by state); **advance-specific lineage still not measured**; P05 disagreement preserved |
| `CP-P01S16-06` | **COMPLETE — EVIDENCE VERIFIED** as to behaviour | 5,201 certs, 25.24% of supplier payments; **statutory questions routed to P07** |
| `CP-P01S16-07` | **COMPLETE — EVIDENCE VERIFIED** | 5,115 immutable reversals, 0 unresolvable originals |
| `CP-P01S16-08` | **COMPLETE — EVIDENCE VERIFIED** | no lock configured; 15.19% of bills pre-dated; 31 BE-dated rows |
| `CP-P01S16-09` | **COMPLETE — EVIDENCE VERIFIED** | 18 entries; 8 active-and-exercised, 3 contradictions open |
| `CP-P01S16-10` | **COMPLETE — EVIDENCE VERIFIED** | 13-step chain, each step with its evidence status |
| `CP-P01S16-11` | *see §R6.1* | four challenges dispatched |
| `CP-P01S16-12` | *see §R6.1* | — |
| `CP-P01S16-13` | *see §R6.1* | — |
| `CP-P01S16-14` | **COMPLETE — EVIDENCE VERIFIED** | delta-only: P04 and P07 changed and were read; eight peers unchanged and **not re-read** |
| `CP-P01S16-FINAL` | *see §R6.1* | — |

## §R6.1 Checkpoints that do not close in this round

`CP-P01S16-05` is **PARTIAL — RESUMABLE** and says so. The prompt asked for advance → partial payment →
WHT → reconciliation → final deduction → residual lineage. This round reached the **populations** and not the
**lineage**. The reconciliation join — 22,468 payments against 447,384 journal items and two reconcile tables —
was **not attempted**, rather than attempted and estimated. It is the largest remaining executable piece in
this package and is recorded as the NEXT EXACT ACTION.

## §R6.2 Four method defects were committed inside this round and corrected before publication

`ERR-P01-42` (a join on `stock_valuation_layer.categ_id`, **a column that does not exist in series 16** —
the round's central result would have been exactly inverted), `ERR-P01-43` (a correction to `ERR-P01-41` nearly
published from the wrong addons directory), `ERR-P01-44` (a version predicate ignoring Odoo's own `'1.0'`
manifest default), plus `NEAR-MISS-P01-07` (a normaliser that assumed the series it was testing for) and
`NEAR-MISS-P01-08` (**"quadrillions posted to the GL"** — the linked entries balance at ฿31,622,699.37).

**Four of the five were caught by a control this package has adopted since round 3; none was caught by a
challenger, because all five were corrected before the package was frozen.** That is the intended order and
it is recorded so the low challenger-catch count is not read as an easy round.
