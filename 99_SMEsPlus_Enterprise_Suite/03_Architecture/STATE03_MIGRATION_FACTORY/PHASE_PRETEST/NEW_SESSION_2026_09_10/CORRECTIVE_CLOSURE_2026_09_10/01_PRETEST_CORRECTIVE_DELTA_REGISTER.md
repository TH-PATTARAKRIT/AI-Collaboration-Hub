# 01 — PRE-TEST CORRECTIVE DELTA REGISTER

## `CHECKPOINT A — CANONICAL INPUTS + SUPERSESSION NORMALIZED`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]`
Corrective round: `[SMEPLUS-26-09-10-PHASE-PRETEST-CORRECTIVE-CLOSURE-001]`
Branch: `architecture/account-phase-pretest-new-session-2026-09-10-001` · head consumed `38d668aa`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **Continuation, not a new session. `0` Phase SA restarts. `0` evidence discarded. `0` artefacts overwritten.**
> **Corrections are published as superseding evidence; originals remain Audit Lineage.**

---

## 1. Canonical state at intake — verified, not assumed

| Check | Result |
|---|---|
| Local head vs `origin` | **`38d668aa` = `38d668aa`** — `0` drift |
| Writer-collision sweep | **`1` of `193`** branches carries a `PHASE_PRETEST` path — the canonical one |
| Package manifest | **`22 of 22 OK`** |
| Boss single-writer confirmation | **`PT-17`**, branch pinned by name |

**`0` stop conditions (§22) triggered at intake.**

---

## 2. Delta register

**`Material Delta?` = did evidence dated AFTER the claim change what the claim asserts?**

| # | Item | Current claim | Original evidence | Superseding evidence | Current authority | Material delta? | Action | Owner | Verification method | Closure evidence | Final status |
|---:|---|---|---|---|---|:--:|---|---|---|---|---|
| **D-01** | `PT10-F-01` — readiness split | `10 WRITABLE / 12 GATED` | `SA_CORR5_10` **2026-09-09** | `SC-BD-05`/`-07`/`-02`/`-08` **2026-09-10** | Boss rulings | **YES** | **RE-DERIVE** | SMEs Core, **Boss-directed §5** | per-cell gating-decision status | **`02_`** | **RE-DERIVED — `19/2/1`, §3** |
| **D-02** | `PT04-F-01` — boundary set | `12` "declared as a set" | `SC-BD-02` §7 | none found | Boss | **NO** | enumerate or `HOLD` | Boss/PMO | corpus search + control | **`02_`** | **`HOLD — CANONICAL SET NOT PROVABLE`** |
| **D-03** | `PT02-F-02` — element 15 design | **WITHDRAWN** | `SA_CORR4_07` §3 | **`SA_CORR5_01`** | CORR5 adjudication | **YES** (already applied) | preserve as lineage | — | pointer-following | `PT-02` §5.1 | **DISPROVED — PRESERVED** |
| **D-04** | `PT05-F-01` — rule sets | attribution corrected | `SA_CORR3_08` §4.1 | **`06_` prompt's FIVE** | governing prompt | **YES** (already applied) | preserve corrected form | — | prompt re-read | `PT-05` header + `PT-13` §4 | **CORRECTED — PRESERVED** |
| **D-05** | `PT07-F-01` — veto count | `6` in force, membership unestablished | `SC-04` | `SC-19`, `SA_CORR3_03` | AAS+/Boss | **NO** | classify A/B/C | AAS+ / Boss | register membership test | **`07_`** | **`C` — count is `7`, §7** |
| **D-06** | `PT09-F-01` — `RT-E15` → exit criteria | `PTX-01`…`-11` constituted | `SC-BD-09` §8.1 | none | Boss direction | **NO** | reconcile 1:1, no bulk | SMEs Core | mapping + duplicate test | **`08_`** | **RECONCILED, undischarged** |
| **D-07** | `PT04-F-03` — missing consumers | `4` outputs, no consumer | `SA03`, `XMC-H-09` | none | — | **NO** | classify A/B/C/D | SMEs Core | 4-way classification | **`03_`** | **`03_`** |
| **D-08** | `PT09-F-02` — composition | unspecified | `X-11`, `JT-05`, `PT-S-06` | `SC-BD-05` rules `JT-05` | Boss | **YES — partial** | decompose per transition | SMEs Core | node-by-node | **`04_`** | **`04_`** |
| **D-09** | `PT05-F-03` — flow enumeration | short by ≥1 | `XMC-F-14` | none | — | **NO** | reconcile population | SMEs Core | denominator derivation | **`05_`** | **`05_`** |
| **D-10** | `X-18` — classification tie-break | undefined; `BD-ACC-01` silent for services | `SA_CORR3_06` | none | — | **NO** | define or route | Boss | precedence test | **`06_`** | **`06_`** |
| **D-11** | `EC-04` `0/3` | unchanged | `SC-58` | none | `8C-CLARIFICATION-01` cl.3 | **NO** | re-test per sub-item | AAS+/Boss | per-boundary | **`09_`** | **`0/3` — CONFIRMED** |
| **D-12** | `EC-07` `0/2` | unchanged | `SC-58` §3 | `SC-BD-10` approves the **act** | Boss | **NO** — appointment ≠ pass | re-test | Boss | pass count | **`09_`** | **`0/2` — CONFIRMED** |
| **D-13** | `E2E-04` `NOT TRAVERSABLE` | unchanged | `SA15` v2 | `SC-BD-02` §8.3/§8.4 | Boss | **YES — partial** | build traversal chain | SMEs Core | node-by-node | **`10_`** | **`10_`** |
| **D-14** | `0 of 48` verified | unchanged | `PT-12` | none | — | **NO** | itemise + verify | SMEs Core | per-item | **`11_`** | **`11_`** |
| **D-15** | `CP-PT-14` NOT DECLARED | unchanged | `PT-14` | `PT-17` reinforces reviewer status | Boss | **NO** | disposition | Boss | authority test | **`12_`** | **`12_`** |
| **D-16** | `PT15-D-01` — title fidelity | `7` headers fixed | `PT-15` §2 | — | — | **NO** | verify still fixed | SMEs Core | header sweep | **`15_`** | **VERIFIED HELD** |
| **D-17** | B-7 baseline drift | re-frozen `22/22` | `PT-15` §5 | this round edits again | — | **YES** | re-freeze at `CHECKPOINT F` | SMEs Core | manifest | **`14_`** | **`14_`** |
| **D-18** | `PT00-F-03` — single writer | **CLOSED** | `PT-00` §9.2 | **Boss confirmation** | Boss | **YES** (applied) | preserve | — | sweep | `PT-17` | **CLOSED** |

**`18` delta items · `7` carry a material delta · `0` findings deleted · `0` originals overwritten.**

---

## 3. `D-01` — the re-derivation, executed

**Per-cell test: is the decision that gates this cell RULED as of `2026-09-10`?**

| Cell | Rows | Gating decision | Ruled? | Authority |
|---|---|---|:--:|---|
| `AC` | `1`,`2`,`3`,`4`,`5`,`6` | **`JT-04`** | **YES** | `SC-BD-05` — `2 of 2` |
| `AC` | `8`,`9` | **`JT-05`** | **YES** | `SC-BD-05` |
| `AC` | `16`,`17` | **`B-6`** = `BLK-07`/`-08` restatement · **veto limb 2** · `POH-D-01`/`-02`/`-06` | **NO** | `POH-D-06` ruled; **`POH-D-01` open · `POH-D-02` withheld · limb 2 outstanding** |
| `AU` | `10` | **`XD1-P1`** — named in `F2` | **YES** | `SC-BD-07` — `3 of 3` |
| **`AU`** | **`5`** | **over-receipt tolerance default (`B4`)** | **NOT ESTABLISHED** | **§3.1** |
| `OUT` | `18` | `XMC-D-02` · `XMC-D-01` | **YES** | `SC-BD-02` · `SC-BD-08` |

### 3.1 `CC-F-01` — a family ruled `3 of 3` whose `3` members are never named

**`SC-BD-07` rules `F2` `3 of 3`, and its member list reads *"three members, **incl.** `XD1-P1`"*.**
**The other two are never enumerated in the ruling, in `SC-11`, or in any `SC-*` record.**

The over-receipt tolerance default is `B4`, *"bundle with `B3`/`TV6-BOSS-01`"* — and `SA17` §2d maps
`F2` to **rows 5 and 10**, which is consistent with `B4` being an `F2` member. **Consistent is not
established.**

> **This is `PT04-F-01`'s defect shape at a second site: a denominator ruled by NUMBER whose MEMBERSHIP is
> never declared.** `12` boundaries and now `3` `F2` members. **Row 5's `AU` cell is therefore recorded
> `NOT ESTABLISHED`, not assumed ruled** — assuming it would be inventing membership, which §5 forbids.

### 3.2 Re-derived result

| Class | Rows | n |
|---|---|---:|
| **`WRITABLE` (gating decisions all ruled)** | `1`,`2`,`3`,`4`,`6`,`8`,`9`,`10`,`18` **+ the `10` already writable** (`7`,`11`,`12`,`13`,`14`,`15`,`19`,`20`,`21`,`22`) | **`19`** |
| **`GATED` (genuinely still gated)** | `16`, `17` | **`2`** |
| **`NOT ESTABLISHED`** | `5` | **`1`** |
| Total | | **`22`** ✔ |

**`10 WRITABLE / 12 GATED` → `19 WRITABLE / 2 GATED / 1 NOT ESTABLISHED`, freshly derived.**

### 3.3 The qualification that must travel with it

> **`WRITABLE` means only *a test case can be written*.** A ruling fixes the **meaning**; the scenario's
> **expected values** must still be taken from the ruling text (e.g. `JT-04` = recognition at the physical
> movement; `JT-05` = original cost). **`0 of 22` remain runtime-verified. The re-derivation moves
> writability, not proof.**

---

## 4. Supersession chain — resolved before reliance

| Claim | Latest artefact ON THAT CLAIM | Superseded |
|---|---|---|
| Element 15 design | **`SA_CORR5_01`** | `SA_CORR4_07` §3 |
| E2E scenario grades | **`SA15_…FINAL_CONTROLLED_V2`** | CORR5-controlled, historical |
| Pre-Test handoff | **`SA17_…FINAL_CONTROLLED_V2`** | CORR5-controlled, historical |
| `FG-F-06` | **`SC-AUTH-02` = Reading C** (`SC-51`) | `SC-BD-01` (B), `SC-CONTRA-01` (A) |
| `BN-nn` status | **`SA_CORR2_03` §4** — `1/17/0` | `SA05` §3 — *"must not be quoted"* |
| Convergence rules | **`SA_CORR3_08` §4.1** (tested) | `SC-45` §2 restatement |
| Decision population | **`SC-11` §2** — `16 of 23` | `26`/`25` headlines |

---

## 5. Checkpoint

> ## `CHECKPOINT A — CANONICAL INPUTS + SUPERSESSION NORMALIZED`
>
> **`0` drift · `1 of 193` branches · manifest `22/22` · `18` delta items, `7` material ·
> **`D-01` RE-DERIVED: `10/12` → `19 WRITABLE / 2 GATED / 1 NOT ESTABLISHED`** ·
> **`CC-F-01` — a second denominator ruled by number with unnamed membership (`F2` `3 of 3`), so row 5 is
> recorded NOT ESTABLISHED rather than assumed** · `7` supersession chains resolved · `0` originals
> overwritten.**

