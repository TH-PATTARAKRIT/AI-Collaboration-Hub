# AI01 — P09_ANALYTIC_INTEGRITY_BASELINE_RECONCILIATION

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Continuation prompt:** `SMEPLUS-26-09-04-ACC-P09-ANALYTIC-ECONOMIC-INTEGRITY-001`
**Execution type:** TARGETED CONTINUATION — NO RESET. Prior P09 evidence, amendments, `CORR1`, `HOLD-AS-01`, `DIS-09`, contradictions and AAS-03 challenges are **preserved as prior evidence and audit lineage**.
**Layer:** 1 — clean-room.

---

## 1. WHAT THIS CONTINUATION IS FOR

The base P09 package established a mechanism. This continuation must prove or disprove an **economic** claim about it:

> **An analytic record existing is not equivalent to an economic management allocation being correct.**

The base package already carries the mechanism. What it did **not** carry is: the algebra stated as algebra; the eligibility rule that decides which rows participate; a systematic sweep across event types; a database or runtime population; or a statement of what each management surface actually displays. Those are the deltas.

## 2. AUTHORITATIVE BASELINE — READ FROM THE REPOSITORY, NOT FROM THE PROMPT

Read at commit `9a3bded` on `research/account-p09-plan-to-analyze-2026-09-04-001`. Every ID below was located in its own file and its current wording confirmed; **the prompt's summary was not relied on.**

| ID | Where it lives now | Current status | Delta this continuation must add |
|---|---|---|---|
| **E19** | `08` row 39 | asset depreciation with an allocation: written to **both** rows, amount is the negated signed balance × share, records are mirror images and **net to zero**. Class A, corrected post-publication | state it as algebra; prove it is unconditional, not configuration-dependent; establish what each report surface shows |
| **E20** | `08` row 40 | asset with **no** allocation: key deliberately omitted, each row computes its own from its own account, so a balanced pair can carry two different allocations → non-zero unbalanced residue. Mechanism A, outcome D | unchanged in substance; folded into the eligibility matrix |
| **E21** | `08` row 41 | mandatory-axis validation does not fire on programmatic posts — opt-in by context **and** restricted to product-type rows. Row-type gate A; call-site enumeration **B from P09's position** | unchanged; the call-site enumeration remains P04's and is **not** upgraded here |
| **EA-06** | `08` line 49 | an allocation shall be applied only to rows carrying the economic effect; symmetric allocation of a balanced pair attributes nothing by arithmetic | now supported by a formal proof rather than an observation |
| **EA-07** | `08` line 51 | where rows are allocated independently, the result shall be verified against the intended attribution | unchanged |
| **CN-20** | `11` row 34 | the mechanism that exists to attribute a cost is arithmetically guaranteed to attribute nothing | unchanged; severity re-assessed after the surface analysis |
| **CN-21** | `11` row 35 | the no-allocation fallback can attribute the two legs to different cost objects | unchanged |
| **EC-56 … EC-59** | `10` rows 90–93 | symmetric pair nets to zero; no-allocation residue; validation gates; a record that attributes nothing is not identifiable as such | EC-59 is strengthened: the surfaces **disagree with each other**, which is worse than "not identifiable" |
| **`14` §R9** | revision log | the incoming P04 correction and its verification | this continuation is logged as §R10 |
| **`HOLD-AS-01` / `DIS-09`** | `11` §C and §B | the cross-track contradiction with a prior Asset package's costing-veto premise | **preserved, not settled here** — see AI11 §5 |
| **`P04-PD-04` / MA-11** | `20` §B | accepted peer dependency; obligation-carrying object must share the scope of the fact it governs | re-tested in AI09 |

**Reconciliation result: the baseline is intact and internally consistent. Nothing in it is withdrawn by this continuation.** Every change below is an addition or a sharpening.

## 3. WHAT WAS ALREADY PROVEN VERSUS WHAT IS NEW

| Question | Base package | This continuation |
|---|---|---|
| do two analytic records get created? | yes — class A | unchanged |
| do they net to zero? | yes — class A, asserted from three read locations | **proved as algebra**, and shown to be unconditional for the both-legs case |
| which rows are eligible at all? | not stated | **AI03** — eligibility is by *assignment*, not by account type or row type |
| is depreciation unique in this? | **declared unsearched** (`NS-12`, `DEP-P09-12`) | **AI07** — systematic event sweep |
| what does a management report show? | not stated | **AI08** — surfaces disagree with each other |
| is there deployed data? | none used; package explicitly not executed | **AI05 / AI06** |
| does double counting coexist with zeroing? | three double-count mechanisms found, none linked to zeroing | **AI11** — both failure classes tested together |

## 4. PRESERVED LINEAGE

Commit lineage carried forward unbroken: `88f52cd` (base) → `16f884f` (P09 package) → `0d792d9` (SHA record) → `9a3bded` (P04 amendment) → this continuation. No file from the base package is deleted; the base documents are **updated in place** where a finding changes, and every change is logged in the revision log.

## 5. CHECKPOINT

**CP-AI01 — CURRENT P09 BASELINE RECONCILED.** Auto-continue.
