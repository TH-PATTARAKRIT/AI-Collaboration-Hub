# SC-ADDENDUM-A — MATERIAL FINDINGS FROM A PARALLEL EXECUTION

> **SUBORDINATE TO THE CONTROLLING PACKAGE.** The controlling package is `SC-08` / `SC-09` / `SC-10` as
> named by `03_SMEPLUS_PHASE_SA_BOSS_FINAL_DECISION_GATE_PROMPT.md` §1. **This addendum adds two findings;
> it changes no count, reopens no family, and claims no controlling status.**

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`
Branch: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001` · consumed head `6d08bcc5`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

---

## 0. Why this file exists

A second execution of `02_PHASE_SA_CANONICAL_TWO_TRACK_CONSOLIDATION_NEXT_PROMPT.md` ran in parallel and
**converged independently on every controlling fact** — `23` decisions, `F5 = 6`, `5` acts, `6` vetoes with
`0` discharged, Category 3 `0`, `0` independent passes, `FG-F-06` reserved to Boss, no targeted research
required. Its package is quarantined at `PARALLEL_EXECUTION_SUPERSEDED_2026_09_10/` and **is not canonical.**

**It surfaced two things the controlling package does not carry.** Measured: `POH-F-06`, *"issuer and
Boss"*, *"limb 2"* and *"would not lift the veto"* return **`0` hits** across `SC-08`, `SC-09` and `SC-10`;
`822cb327`, `d7ab8e53` and `SA_AR_R2_03/04` likewise return **`0`**.

**Both bear on rulings Boss is about to make. Withholding them would make Boss the first detector.**

---

## 1. `SC-ADD-01` — `F5`'s `POH-D-06` is NOT a Boss-only act, and ruling it does NOT lift the veto

**Primary source: `SA_CORR3_03_PRODUCTION_OVERHEAD_PROOF.md`, read directly on the CORR3 branch.**

`POH-F-06`, verbatim:

> *"The standing veto has **two limbs** … Limb 1 (`BLK-07`) is the decision. **Limb 2 — prove exactly one
> mechanism carries machine cost into product cost — is an SMEs Core proof obligation**, it is undischarged,
> and its own reviewer records that the limb *"tests for uniqueness where the answer is zero"*, so it cannot
> be discharged in either direction as written. **Restating a veto limb is reserved to the veto's issuer and
> Boss. Deciding `BLK-07` alone would not lift the veto.**"*

And `POH-D-06`'s own decision cell extends its restatement request to limb 2:

> *"**`BLK-07` and `BLK-08`: confirm, or restate** … This document requests a restatement; it does not
> perform one. **Same for veto limb 2**"*

### Two consequences for the `F5` ruling

| # | Consequence | Why it matters at the moment of ruling |
|---|---|---|
| **1** | **`POH-D-06` requires the veto's issuer (AAS+) as well as Boss.** *"Restating a veto limb is reserved to the veto's **issuer and Boss**."* | **Boss ruling `POH-D-06` alone does not complete the restatement it requests.** A dependent issuer act follows, and it is currently unnamed anywhere in the controlling package |
| **2** | **Ruling `F5` does not discharge the standing manufacturing veto.** *"**Deciding `BLK-07` alone would not lift the veto.**"* | A reader of the `F5` card could reasonably assume that resolving the blocker resolves the veto. **It does not** |

**Neither consequence changes the count.** `F5` remains **6** decisions. **`POH-D-06` remains a Boss item.**
What changes is **what Boss's ruling on it accomplishes**, and what must follow it.

### Relationship to `AR-F-01`

The peer track's `AR-F-01` reached `F5 = 6` on the ground that *"veto limb 2 is `POH-G-03`, an SMEs Core
design gap, not a Boss decision, and is removed from the decision population entirely."*

> **The number is right and is adopted. The ground is imprecise.** `POH-G-03` is the **gap statement** about
> limb 2, and limb 2's **discharge** is indeed an SMEs Core proof obligation — the peer is correct there.
> But limb 2's **restatement** is *"reserved to the veto's issuer and Boss"* and is **bundled inside
> `POH-D-06`**. **It is absorbed, not excluded.**
>
> **`F5 = 6` survives on a stronger and independent ground:** `POH-F-16` states it outright — *"**The Boss
> residue is six items**, five of them small"* — and §11 enumerates them as `POH-D-01`…`POH-D-06`.

---

## 2. `SC-ADD-02` — the AR branch advanced two commits past the cited baseline

**The AR branch head is `822cb327`, not `b1f07939`.** Two commits were published after the baseline the
prompts cite, and **neither is referenced in the controlling package**:

| Commit | Time | File | Why it matters |
|---|---|---|---|
| **`d7ab8e53`** | 2026-09-10 01:11 | `SA_AR_R2_03_BOSS_RULING_BOSS_ROUTE_01.md` | **The peer's own record of the `BOSS-ROUTE-01` ruling**, in the peer's words — an **independent corroboration** of the ruling the controlling package acts on, and the peer's self-declared terminal state `CLOSED — ROUTED` |
| **`822cb327`** | 2026-09-10 01:15 | `SA_AR_R2_04_SC_INTAKE_CONFORMANCE_CHECK.md` | **A peer conformance check on this session's own intake**, measured at `2139088b`. It found `AR-F-02` **materially unconsumed at that commit** and recommended the exact correction later applied at `c4949ec6` |

**Neither changes a count or a decision.** `SA_AR_R2_04`'s finding was already satisfied by `c4949ec6`
before that check was written, and its `AR-F-01` item it explicitly declined to raise as a defect.

**Recorded because a cited baseline is a floor, not a ceiling** — and because `SA_AR_R2_03` is the only
peer-authored record of the routing ruling, which is worth having in the lineage.

### One point of divergence, stated plainly

`SA_AR_R2_04` §3 concluded **no correction was needed** on `AR-F-01`, holding that the `26`-based and
`24`-based units were each declared and each defensible.

> **The parallel execution declined that.** `8` for `F5` is reachable only by slicing one governance act
> into subjects **and** counting a third subject the source excludes from the decision population — **a
> membership error on top of a unit choice, not an alternative unit.**
>
> **The controlling package and the parallel execution both use `F5 = 6`, so this divergence changes
> nothing in front of Boss.** It is recorded so the *reason* the count is 6 is on the strongest ground
> available, which is `POH-F-16`'s own sentence.

---

## 3. What this addendum does NOT do

1. **It does not change the canonical count.** `23` decisions, `F5 = 6`, `5` acts — unchanged.
2. **It does not reopen a family.** `F5` is not re-derived; only the consequence of ruling it is stated.
3. **It does not answer `FG-F-06`.**
4. **It does not discharge, re-word or narrow any veto** — and `SC-ADD-01` is precisely a statement that a
   veto is **not** lifted by a ruling that might be read as lifting it.
5. **It does not claim controlling status**, and it is deliberately named outside the `SC-nn` series so it
   cannot be mistaken for one, and so it does not collide with `SC-11` / `SC-12` as the `03_` prompt
   reserves them.
6. **It modifies no peer artefact and no controlling artefact.**

---

## 4. Disposition requested

| Finding | Requested handling |
|---|---|
| **`SC-ADD-01`** | **Carry onto the `F5` card before Boss rules it.** Two lines: `POH-D-06` needs AAS+ concurrence as well as Boss; and ruling `BLK-07` does not lift the standing veto |
| **`SC-ADD-02`** | Add `d7ab8e53` and `822cb327` to the AR lineage index. **No count or decision changes** |

---

No Evidence = No Progress. Never Skip Gate. Boss must not be the first detector.
Boss remains the sole Final Approver.
