# SC-EC07-02 — `B-7` APPOINTMENT CARD AND `EC-07` INDEPENDENT-PASS PROTOCOL

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`
Branch: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001` · **frozen baseline `e113258f`**
Prepared under: `03_…BOSS_FINAL_DECISION_GATE_PROMPT.md` §3, on `SC-CONTRA-01` (`FG-F-06 = READING A`)
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **This card requests an appointment. It does not make one.** `Q-BOSS-02` control 2 forbids a session
> selecting its own challenger, and gate prompt §8 forbids self-appointment and forbids claiming structural
> independence from internal challenge. **No candidate is named, suggested, or hinted at anywhere in this
> file.**

---

## 1. What is being asked of Boss

> **Appoint a `Q-BOSS-02`-eligible structurally independent challenger to perform the `EC-07` passes over
> the frozen Phase SA baseline `e113258f`.**

**One act. No alternatives. It is not a decision family and is not counted among the 23.**

---

## 2. Structural-independence eligibility controls

**`Q-BOSS-02` defines independence as ten cumulative controls. Its two operative sentences, verbatim:**
*"A different session alone is insufficient. A different model alone is insufficient."*

**The two that bind this appointment most tightly:**

| Control | Requirement |
|---|---|
| **Control 2** | **The correction/execution owner may not select its own verifier.** This is why the card names no candidate |
| **Cumulative rule** | Neither a fresh session nor a different model is sufficient alone. **Both, plus the remaining controls, are required** |

**Disqualifying conditions — stated so an appointment is not made that fails on inspection:**

- any party that authored, corrected, challenged or published any artefact in the frozen baseline;
- either executor of `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`;
- the `[SMEPLUS-26-09-09-PHASE-SA-AUTHORITY-RESOLUTION-001]` (AR) track — **it is a peer, not an
  independent reviewer**, and its own cross-examination of this session is classified
  `PEER CROSS-EXAMINATION`, explicitly not assurance;
- any party selected by, or on the recommendation of, the above.

> **The AR track's exclusion is deliberate and is the strictest call in this card.** Its work was
> genuinely productive against this session — it corrected a published count and removed a ground from
> Boss's ledger. **Productivity is not independence.** Admitting it as the `EC-07` reviewer would satisfy
> the appearance and fail the standard.

---

## 3. The exact frozen evidence baseline

> **Baseline commit AT PREPARATION: `e113258f4e3565030b417ceed01264a337aa20f0`**
>
> ⚠ **THE BRANCH IS LIVE AND HAS MOVED SINCE.** At `89ba9c7d` the Reading B path added `SC-BD-02`…`SC-BD-10`,
> `SC-11` and `SC-12`. **The baseline MUST be re-frozen at the commit Boss designates at appointment time**,
> and the reviewer must be told which commit is the subject. **A baseline that moves during a pass is an
> evidence-integrity failure under `EC-07` and resets the count.**
> Path: `…/PHASE_SA_FINAL_BOSS_GATE_2026_09_09/SMES_CORE_CONTINUATION_2026_09_10/`
> **20 blobs in scope + 12 quarantined (out of scope, §3.2).**

| Blob (12) | File |
|---|---|
| `1b0d80956534` | `SC-00_PMO_MAINLINE_DELTA_REMEASUREMENT.md` |
| `c0022be7e0ea` | `SC-01_FINAL_DECISION_SCRUB_REGISTER.md` |
| `f24e537cbe00` | `SC-02_F3_DROPSHIP_BOUNDED_VERIFICATION.md` |
| `309c400adb51` | `SC-03_SMT_FIRST_LINE_CHALLENGE_REGISTER.md` |
| `7fc8247cdae9` | `SC-04_VETO_AUTHORITY_HANDOFF_REGISTER.md` |
| `4effc0479b97` | `SC-05_PRETEST_ENTRY_REQUALIFICATION.md` |
| `da2f633ff73d` | `SC-06_BOSS_FINAL_GATE_DELTA_PACK.md` |
| `070471ed4cb0` | `SC-07_TWO_TRACK_RECONCILIATION_AND_COUNT_CORRECTION.md` |
| `19a207c509ad` | `SC-08_BOSS_ROUTE_RESOLUTION_AND_AR_INTAKE.md` |
| `1399974fd6b8` | `SC-09_FG_F06_FINAL_SCOPE_RECHECK.md` |
| `ebb6fef71185` | `SC-10_BOSS_FINAL_GATE_DELTA_PACK_V2.md` |
| `f6d31d24562a` | `SC-ADDENDUM-A_PARALLEL_EXECUTION_MATERIAL_FINDINGS.md` |
| `7996b7074c37` | `SC-BD-01_FG_F06_BOSS_RULING.md` |
| `29519fbe85a0` · `d988a811b754` · `47db72a3a878` · `d7b13ab8ba35` · `e83cc4461985` | governance records and the four prompts |
| `5e8b6902defd` · `6f57efd45d49` | auto-resume state · manifest |
| **this commit** | `SC-CONTRA-01`, `SC-EC07-01`, `SC-EC07-02` |

### 3.1 Upstream primary sources the reviewer must reach independently

**The reviewer must rebuild the evidence frame rather than inherit it.** The programme's record is that the
findings that mattered were found by **refusing to inherit**.

Boss rulings (`BD-ACC-01`/`02`/`03A`/`03B`, Phase S closure) · the 16-element handoff-contract approval ·
`SMEPLUS-DR-EXIT-8C-001` on `origin/SMEsPlus` · `SA_CORR3_03` (`POH-*`) · `SA_CORR3_07` · `SA_CORR3_08`
(`XMC-*`) · `SA_CORR4_01`, `SA_CORR4_03` (`CF-I-03`) · `SA10` · `08_JT04` / `09_JT05` ·
`03_INVENTORY_FUNCTIONAL_DESIGN_V1` · the `P01` / `P02` deployed-evidence packages · the AR branch at
head **`822cb327`** — *not* the cited `b1f07939`.

### 3.2 Explicitly OUT of the review scope

`PARALLEL_EXECUTION_SUPERSEDED_2026_09_10/` (12 files) — **not canonical, not to be cited as `SC-nn`**.
Reviewable only as lineage, and **no finding may rest on it**.

---

## 4. Where the reviewer should attack first

**Named by the executing party against its own work, because a reviewer who has to find the soft spots
unaided spends the first pass locating what the author already knows.**

| # | Target | Why |
|---|---|---|
| 1 | **`EC-04`** — `0 of 3` tolerance-zero boundaries evidence-closed, and the circularity at `SC-EC07-01` §3.1 | If the circularity is real, **no number of clean passes opens this gate** |
| 2 | **`C2-D-02`'s closure** — the one SMEs Core closure that removes an item from the Boss list | Its reversal lever is published; **test whether it should have been pulled** |
| 3 | **`F5`'s `POH-D-06`** — `SC-ADD-01` says ruling it needs AAS+ too and does not lift the veto | Verify at `SA_CORR3_03` primary text; it is **absent from the controlling package** |
| 4 | **`E2E-04`** — a re-grade attempted, withdrawn under challenge, and **deliberately not reinstated** | The specification bearing on it was written by the audited party |
| 5 | **`EC-06`** — the end-to-end negative-claim sweep **deliberately not run** by SMEs Core | It is the audited party's own uninspected surface |
| 6 | **The `23` count and `F5 = 6`** | Two derivations converged; **convergence between two parties who read each other is not independence** |
| 7 | **`XMC-F-03`'s zero-length-chain weakness** — published, unanswered | The `F3` recommendation rests on it |

---

## 5. The two-consecutive-clean-pass requirement

**`EC-07`, verbatim:** *"at least two consecutive fresh independent passes must complete without any of the
following: new material population · new material finding class · new gating unknown · reopened
tolerance-zero issue · new Gate-changing contradiction · evidence-integrity failure. **Reviewer findings
must themselves be independently verified before acceptance.**"*

| Rule | Applied here |
|---|---|
| **Two, and consecutive** | A clean pass followed by a non-clean pass followed by a clean pass is **`1`**, not `2` |
| **Fresh** | Each pass rebuilds the frame from §3.1, not from the prior pass's notes |
| **Findings verified before acceptance** | *"`Independent Review != Truth. Verified Evidence = Truth Basis.`"* A reviewer finding is verified at primary source **before** it is accepted — and a **disproof** is verified too. The programme's record includes an independent review committing its own bounded-enumeration false negative |

### 5.1 What resets the count — the six triggers, made testable

| Trigger | Test |
|---|---|
| new material **population** | a denominator changes, or one not previously declared is required |
| new material **finding class** | a defect of a kind not already in the registers |
| new **gating unknown** | an unknown that blocks the gate and carries no disposition |
| **reopened tolerance-zero** issue | any of the 3 boundaries changes state, or a 4th is identified |
| new **Gate-changing contradiction** | a contradiction that changes what the gate may do |
| **evidence-integrity failure** | a manifest mismatch, an unresolvable citation, or a claim whose instrument cannot be shown to fire |

**On any trigger: correct → re-verify → restart the consecutive count**, per Boss's instruction.

> ### `SC-EC-02` — a reset trigger is already live, before pass 1
> **`EC-05` is open on a Gate-changing contradiction between `SC-BD-01` and `SC-CONTRA-01`** (`SC-EC07-01` §4).
> **Any pass run while it stands is non-clean by `EC-07`'s own list.** **Commissioning the reviewer before
> Boss dispositions it spends a cycle to rediscover a known defect and returns the count to `0`.**
>
> **SMEs Core therefore does not open the sequence, and says so rather than opening it and reporting a
> failed pass.**

---

## 6. What the reviewer may NOT do

| Prohibition | Ground |
|---|---|
| Redesign, or mutate any SMEs Core owner artefact | The reviewer audits the frozen baseline; **changing it destroys the thing being audited** and breaks pass-to-pass comparability |
| Rule any of the 23 decisions, or `FG-F-06` | Boss authority |
| Discharge, re-word or narrow any veto | Issuer's act, ratified by Boss. **6 in force / 0 discharged** |
| Declare Phase SA closed, or any `PASS` | Boss authority |
| Select or influence the second reviewer, if a different party performs pass 2 | Control 2 applies to the reviewer as it does to the executor |
| Inherit the executing party's evidence frame | §3.1 |
| Treat the quarantined package as canonical | §3.2 |

**Corrections arising from findings are made by the artefact's owner, then re-verified — the reviewer
reports, the owner repairs, and the count restarts.**

---

## 7. Terminal state after appointment

| Step | Terminal |
|---|---|
| Boss appoints | `EC-07 SEQUENCE OPEN — PASS 1 COMMISSIONED` |
| Pass 1 clean | `EC-07 1 OF 2` |
| Pass 1 non-clean | findings verified → owner corrects → re-verify → **count restarts at `0`** |
| Pass 2 clean, consecutive | **`EC-07 SATISFIED — 2 OF 2`** |
| After `EC-07` satisfied | **`EC-04`, `EC-05` and `EC-08`'s two absences remain open** (`SC-EC07-01`). **The gate is not thereby open** |
| All eight satisfied | Return to Boss for the `F1`–`F8` rulings — **`READY FOR BOSS F1–F8 RULING UNDER A SATISFIED GATE`** |

> **`EC-07` satisfied is not Phase SA exit.** `EC-04` and `EC-05` fail independently and are not addressed
> by any number of clean passes.

---

## 8. Checkpoint

> ## `B-7 APPOINTMENT CARD PREPARED — APPOINTMENT NOT MADE`
> **Baseline frozen at `e113258f`, 20 blobs in scope, 12 quarantined out of scope · eligibility controls
> stated with four disqualifying conditions, **including the peer AR track** · **no candidate named,
> suggested or hinted** · 7 attack targets named by the audited party against itself · the six reset
> triggers made testable · **`SC-EC-02`: a reset trigger is already live before pass 1**, so the sequence
> is not opened · reviewer prohibitions stated · terminal ladder published · `EC-07` satisfied ≠ gate open.**

No Evidence = No Progress. Never Skip Gate. A party cannot be structurally independent of itself.
Boss remains the sole Final Approver.
