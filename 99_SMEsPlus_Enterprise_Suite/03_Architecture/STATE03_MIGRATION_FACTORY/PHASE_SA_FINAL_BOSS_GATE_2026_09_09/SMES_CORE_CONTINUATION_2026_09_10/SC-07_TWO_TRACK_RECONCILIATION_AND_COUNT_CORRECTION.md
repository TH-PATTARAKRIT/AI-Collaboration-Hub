# SC-07 — TWO-TRACK RECONCILIATION AND COUNT CORRECTION

## POST-PUBLICATION CORRECTION TO `SC-01`, `SC-04`, `SC-06`

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`
Branch: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Published at: `2139088b` · corrected in this commit
**Beyond the master prompt's required output list**, published because §2 requires supersession and
contradiction lineage to be preserved, and because a peer track's corrections would otherwise be lost.
Boss: **SOLE FINAL APPROVER**

---

## 1. Result

> # `TWO LIVE BOSS INSTRUCTIONS GOVERN THE SAME F1–F8 POPULATION. BOTH ARE COHERENT. THEY ARE JOINTLY INCONSISTENT ON ONE NUMBER AND ONE GROUND. THIS SESSION ADOPTS THE PEER'S TWO CORRECTIONS AFTER VERIFYING BOTH AT PRIMARY SOURCE — AND DOES NOT CHOOSE THE ROUTE.`

| | |
|---|---|
| **Corrections adopted** | **2** — `AR-F-01` (the count) and `AR-F-02` (an `8C-001` Reading A ground) |
| **Verified independently at primary source before adopting** | **2 of 2** — neither is inherited on the peer's say-so |
| **Boss decision population** | **`26` → `24` corrected → `23` after this session's one closure** |
| **Reading A grounds for `8C-001`** | **3 clauses and NO Phase SA precedent** (was: 5 clauses and a precedent) |
| **`BOSS-ROUTE-01` — which track Boss reads** | **OPEN. NOT DECIDED HERE.** |
| **Peer package withdrawn or overwritten** | **0.** Nothing on the peer's branch is touched |

---

## 2. The two tracks

| | **AR track** | **SC track — this one** |
|---|---|---|
| Instruction | `[SMEPLUS-26-09-09-PHASE-SA-AUTHORITY-RESOLUTION-001]`, prompt `e6d2be32` | `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`, `34a46d9b`/`cdcf53c9`/`33537d36` |
| Branch | `architecture/phase-sa-authority-resolution-and-independent-gate-2026-09-09-001` | `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001` |
| Published | **R1 `afe664c6`** (Terminal A, 24 decisions, 5 acts) · **R2 `b1f07939`** (Terminal B — HOLD) | `2139088b` (Terminal A), corrected by this commit |
| Parent named | `9d5bc2db` | `9d5bc2db` |

**Both verified to exist and resolve:** `afe664c6`, `b1f07939`, `e6d2be32`, `b8666f14` all resolve.
**This branch forks at `b8666f14` and does NOT contain `afe664c6`** — confirmed by
`git merge-base --is-ancestor`, which returns false. **So this session derived from a baseline that did
not carry the peer's corrections, exactly as the peer predicted.**

### 2.1 The peer was right about what this session would do, and about what it would fix

`b1f07939` records that the SC instruction gates escalation on three items the AR package had not
performed — **§5's `F3` bounded re-read, §7's SMT dispositions, and the §4 scrub** — and states that this
work *"is authorized to the other track on the other branch under `SC-*` identifiers, and was NOT performed
here — never scope a write wider than the read."*

> **All three are now performed.** `SC-01` (scrub), `SC-02` (`F3` bounded re-read), `SC-03` (SMT
> dispositions, 8 of 8 families). **The conditions that placed the AR package in Terminal B are discharged
> by this package's existence** — but **only the AR track may say so about its own terminal state**, and
> this file does not say it for them. **It is reported to them, not applied to them.**

**Neither track committed an error in sequencing.** The AR round 1 predates the SC instruction by 1h19m;
the SC instruction postdates the AR publication and does not cite it. **Both are correct on their own
inputs.** What follows is not a fault in either — it is what happens when two instructions fork.

---

## 3. `AR-F-01` — ADOPTED. The Boss decision population is 24, not 26

### 3.1 The peer's claim

*"The parent pack's headline 26 counted `F5` by **identifier** while `F5`'s own card said 'eight
identifiers, six decisions'. At primary source `POH-D-06` is one governance act with **two** subjects
(`BLK-07`, `BLK-08`), and 'veto limb 2' is `POH-G-03`, an SMEs Core design gap that was never a Boss
decision. 30 candidates → **24** decisions in the same 8 families."*

### 3.2 Verified here, at primary source, before adopting

**Instrument:** `SA_CORR3_03_PRODUCTION_OVERHEAD_PROOF.md` on
`origin/architecture/phase-sa-corr3-proof-verification-2026-09-09-001`, read directly.

| Check | Primary text | Result |
|---|---|---|
| How many subjects does `POH-D-06` name? | *"`POH-D-06` \| **`BLK-07` and `BLK-08`: confirm, or restate** \| **Governance act.** … **This document requests a restatement; it does not perform one.** Same for veto limb 2"* | **TWO.** *"Same for veto limb 2"* is an **appended sentence**, not a third subject of the decision cell |
| What is *"veto limb 2"*? | §11: *"…`POH-G-03`'s mutual exclusion **built** and its detection report **specified**; and `POH-D-01`, `POH-D-02`, `POH-D-06` **returned by Boss**"* | **`POH-G-03` is a `POH-G-*` design/build gap, listed apart from the Boss returns. It was never a Boss decision** |
| Does the source state the residue directly? | **`POH-F-16`: *"The Boss residue is six items, five of them small."*** | **Stated outright. `F5` = 6** |

> **`AR-F-01` is CONFIRMED on independent evidence.** The verification did not rely on the peer's file; it
> read the same primary source and found a sentence — `POH-F-16` — that states the answer in words.

### 3.3 What this session got wrong, and the shape of the error

**This register's first draft used `F5` = 6 and was right.** It was then **overridden to `F5` = 8 to match
the parent's headline**, with the unit declared and the parent's internal inconsistency explicitly noted.

> **`SC-F-06`. Declaring the unit is not the same as resolving it correctly.** `SC-01` §1.0 observed that
> *"the two readings are both in the parent and they differ"* and then **resolved the conflict toward the
> summary instead of toward the source.** That is the programme's own *secondary-source* defect class,
> committed in the act of guarding against a *different* defect class — and the guarding was itself
> published as a finding (`SC-F-02`), which made the wrong resolution look controlled.
>
> **A declared unit inherits the authority of whatever it points at.** Pointing it at a headline gives a
> rigorous-looking derivation of a defective number.

### 3.4 Corrected arithmetic

| Family | Corrected |
|---|---:|
| `F1` | 2 |
| `F2` | 3 |
| `F3` | **1** (conditional) |
| `F4` | 2 |
| `F5` | **6** |
| `F6` | 4 |
| `F7` | 4 |
| `F8` | 1 |
| **Total** | **23** |

**Corrected parent population `24` → `23` after this session's one closure (`C2-D-02`).**
`2+3+1+2+6+4+4+1 = 23`, summed from the rows.

---

## 4. `AR-F-02` — ADOPTED. Reading A loses its only Phase SA precedent

### 4.1 The peer's claim

*"The single Phase SA citation of `SMEPLUS-DR-EXIT-8C-001` applies **§9** (`PROVISIONAL / NON-CANONICAL`),
not §4 or `EC-07` — which narrows the case for Reading A that the parent round built on it."*

### 4.2 Verified here, at primary source

| Check | Primary text | Result |
|---|---|---|
| What does `SA_CORR3_07` actually say? | §2.5: *"…**6 in force, 0 discharged.** **Under the 8-Criteria Exit Constitution the whole conformance package is `PROVISIONAL / NON-CANONICAL`.**"* | It applies a **grading**, not an exit rule |
| Which clause produces `PROVISIONAL / NON-CANONICAL`? | Constitution **§9 — AAS+ / Design Handoff Rule**: *"AAS+ may explore designs in parallel only as `PROVISIONAL / NON-CANONICAL` while parent Very Deep Research is not yet complete."* | **§9. Not §4. Not `EC-07`** |

> **`AR-F-02` is CONFIRMED.** §9 governs **AAS+ parallel design exploration**. A §9 grading says **nothing**
> about whether §4's Module Exit Rule or `EC-07`'s two-clean-independent-passes requirement binds Phase SA's
> gate. **The parent pack offered this citation as a Reading A ground; it is not one, and it is withdrawn
> from `SC-04` §6.3 and `SC-06` §4.**

### 4.3 Reading A's grounds, after both narrowings

| Ground | Status |
|---|---|
| §2.3 *every STATE before advancement* | **Not engaged** — Phase SA sits inside `STATE03` (`SC-V-01`, this session) |
| §5 State Exit Rule | **Not engaged** — operates at State level (`SC-V-01`, this session) |
| **`SA_CORR3_07` precedent** | **WITHDRAWN** — it applies §9 (`AR-F-02`, peer, verified here) |
| §2.4 *Cross-Module and Whole-System State Integration Review* | **Live and contested** |
| §4 *"next controlled phase"* | **Live and contested** |
| §6 `/L99999.99999` depth label carried by every Phase SA prompt | **Live and contested** |

> **Reading A is materially weaker than the parent pack presented it: three contested clauses and no
> precedent.** **This does not make Reading B correct**, and this session still offers **no preference** —
> two independent tracks have now each narrowed Reading A, and *"only Boss may state what a Boss ruling
> covers"* is unaffected by how strong either reading looks.
>
> **And the direction is noted: both narrowings favour the reading that opens the gate.** That is the
> standing bias, which is exactly why neither track adopted the conclusion the narrowings point toward.

---

## 5. `BOSS-ROUTE-01` — open, and not decided here

> **Two Boss-authored instructions govern the same `F1`–`F8` population. Only Boss may say which package he
> reads, or whether he reads both.**

| Option | What it means |
|---|---|
| **SC** | Boss reads this package. The AR package's `AR-F-01`/`AR-F-02` are already consumed into it by this file |
| **AR** | Boss reads `afe664c6` + `b1f07939`. Its Terminal B conditions are discharged by this package's `SC-01`/`SC-02`/`SC-03`, which the AR track would need to record itself |
| **BOTH** | The packages are **complementary on the merits**: AR corrected the count and the constitutional ground; SC performed the scrub, the `F3` re-read and the SMT challenge. **No finding of either contradicts a finding of the other** — the only inconsistency was the count, and it is now resolved in the peer's favour |

**This session picks none of the three.** Choosing a route between two Boss instructions is a governance
act, and an executing party choosing the branch it authored is the self-interested-classification failure
the programme has recorded.

**Nothing on the peer's branch is modified, withdrawn or overwritten by this session** — a write is never
scoped wider than the read.

---

## 6. Effect on this package's terminal state

**None.** `TERMINAL A — READY FOR BOSS PHASE SA FINAL DECISION` stands, on its four tested conditions:
SMEs Core authority exhausted · SMT challenge complete · team-owned material gaps closed or bounded
(`CATEGORY 3 = 0`) · the pack contains only Boss-owned decisions and acts.

**What changed is the size of the list (`25 → 23`) and the strength of one Reading A ground — not what is
owed, by whom, or whether the team finished its work.**

**And `BOSS-ROUTE-01` is now visible in the pack**, which it was not before this file. **A route question
Boss cannot see is a worse outcome than one he can**, and surfacing it is the reason this file exists.

---

## 7. Findings

| ID | Finding | Disposition |
|---|---|---|
| **`SC-F-06`** | This session resolved a declared count unit **toward the parent's headline instead of toward primary source**, producing a rigorous-looking derivation of a defective number. Its own first draft had it right | **Corrected.** `SC-01`, `SC-06` patched; arithmetic re-summed from rows |
| **`SC-F-07`** | This session **did not detect the parallel AR track** during execution. It derived from `9d5bc2db` as its instruction named, and never swept for branch commits postdating that parent | **Recorded.** Prevention control at §8 |

## 8. Prevention control

> **Before executing a re-issued instruction, sweep for Boss-authored commits that postdate the parent it
> names** — `git log --all --remotes --since=<parent date>` — **and check whether the instruction's own
> subject population is already the subject of a published package.**
>
> **This session's instruction named `9d5bc2db` as parent and a published package over the same population
> existed one branch away.** Neither the master prompt nor the resume state mentioned it, and **nothing in a
> single-branch execution can surface it.** The peer track found this session by exactly that sweep; this
> session did not run it, and found the peer only afterwards.
>
> **Proposed for SMEs Core adoption. Not proposed as a project-wide rule** — that would be a governance act
> outside this session's authority.

---

No Evidence = No Progress. Never Skip Gate. Verify before adopting a peer's finding.
SMEs Core does not choose between two Boss instructions. Boss remains the sole Final Approver.
