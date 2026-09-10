# SC-27 — `B-7` INDEPENDENT REVIEW APPOINTMENT AND PROTOCOL PACK

## CP-SA-SC-210 — INDEPENDENT REVIEW PACK READY

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · head consumed `2cfb57eb`
Supersedes `SC-EC07-02` (preserved as lineage; **corrected** at §3)
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **This pack is READY. It is not ACTIVATED.** `EC-05` is open (`SC-25`), so **no reviewer is appointed and
> no pass is opened** — `05_` §4: *"Do NOT appoint a reviewer merely to rediscover a known contradiction."*

---

## 1. What this executor may and may not do — applied, not restated

| MAY (and did) | MUST NOT (and did not) |
|---|---|
| prepare the frozen evidence package — §4 | select its own verifier — **`0` selected** |
| define eligibility criteria — §3 | count itself as independent — **`0` claims** |
| define disqualifiers — §3.2 | count same-session subagents as independent — **`0` subagents used in this session** |
| define reset triggers — §6 | fabricate clean passes — **`EC-07` remains `0 of 2`** |
| define reviewer instructions and prohibitions — §5, §7 | |
| define acceptance/rejection and evidence-verification protocol — §6.2 | |
| prepare the appointment card — §2 | |

---

## 2. The appointment card

> **Appoint a `Q-BOSS-02`-eligible structurally independent challenger to perform the `EC-07` passes over
> the frozen Phase SA baseline Boss designates.**

**One act. No alternatives. Not a decision family. Not counted among the Boss decisions.**

**Preconditions before this act has value** — both Boss-owned, both single-line:
`SC-AUTH-01` (`FG-F-06` collision) and `8C-BOUNDARY-01` (`SC-26` §7).
**Appointing before these are answered buys a pass that `EC-07` cannot count.**

---

## 3. Eligibility — `Q-BOSS-02` at primary text, and the correction it forces

**`SC-F-14`. `SC-EC07-02` §2 stated no candidate was *"named, suggested, or hinted."* True of this
executor's own act — and it omitted that `Q-BOSS-02` already names an eligibility class at Boss's hand.
Withholding that made the card less useful to the only party who can act on it. Corrected here.**

### 3.1 The ten cumulative controls, verbatim from `Q-BOSS-02` §1

> *"A different session alone is insufficient. A different model alone is insufficient."*

| # | Control |
|---:|---|
| 1 | **Model / Agent Separation** — the verifier must not be the same model/agent that authored or executed the work under review |
| 2 | **Appointment Independence** — appointed by Boss or an independent governance authority, **not selected by the correction owner** |
| 3 | **Evidence Isolation** — a separate isolated session against a **frozen** evidence surface and bounded scope |
| 4 | **Read-Only Boundary** — read-only access; **must not edit the owner's artefacts** |
| 5 | **Independent Reproduction** — independently reproduces the relevant tests, counts, predicates and conclusions |
| 6 | **Independent Publication** — publishes its own artefact, branch and immutable commit SHA |
| 7 | **No Owner Mutation** — must not modify peer-owner branches or artefacts |
| 8 | **No Self-Discharge** — must not self-discharge any veto |
| 9 | **No Self-Pass** — must not self-declare `PASS`, gate closure, release, merge or production readiness |
| 10 | **Boss Final Authority** — Boss remains the sole Final Approver |

### 3.2 The named eligibility class — and its scope qualification

`Q-BOSS-02` §2, verbatim:

> - *"**Claude Opus 5**, where it authored or executed the repair being reviewed, is **NOT ELIGIBLE** to
>   perform the corresponding independent challenge for that repair."*
> - *"**ChatGPT GPT-5.6 Sol**, operating in a separate isolated Independent Verification session, may serve
>   as the verifier/challenger **only if** it did not author or execute the repair under review and all
>   controls in Section 1 are satisfied."*
> - *"Eligibility is determined **per repair / challenge pair**. No verifier is presumed independent merely
>   because it is a different session or model."*

> **Scope qualification, stated because it matters and is easy to miss.** §2 opens *"For the current
> `P06` / `P08` / `P09` / `P11` correction programme."* **Whether its named eligibility extends to Phase SA
> is itself a scope question.** **§1's ten controls carry no such limitation and are general.**
>
> **Consequence: this executor — Claude Opus 5, author of artefacts in the baseline — is `NOT ELIGIBLE`,
> on Boss's own words, under either scope reading.** That is not a self-assessment; it is a citation.

### 3.3 Disqualifying conditions

- any party that authored, corrected, challenged or published any artefact in the frozen baseline;
- **either executor of this session** — both are disqualified, and both authored baseline artefacts;
- the `[SMEPLUS-26-09-09-PHASE-SA-AUTHORITY-RESOLUTION-001]` **AR track** — it is a **peer**, and its
  cross-examination of this session is classified `PEER CROSS-EXAMINATION`, explicitly not assurance;
- any party selected by, or on the recommendation of, the above;
- **any subagent, persona or debate agent of this session** — same model, same session, same corpus.

---

## 4. The frozen evidence baseline

> **Prepared at `2cfb57eb`. The branch is live and has moved eight times during this session, so the
> baseline MUST be re-frozen at the commit Boss designates at appointment time, and the reviewer must be
> told which commit is the subject. A baseline that moves during a pass is an evidence-integrity failure
> under `EC-07` and resets the count.**

**In scope:** the continuation directory's top-level artefacts at the designated commit —
`SC-00`…`SC-21`, `SC-22`…`SC-31`, `SC-ADDENDUM-A`, `SC-BD-01`…`SC-BD-10`, `SC-CONTRA-01`, `SC-AUTH-01`,
the governance records and the five prompts, plus `PACKAGE_MANIFEST_SHA256.txt`.

**Out of scope:** `PARALLEL_EXECUTION_SUPERSEDED_2026_09_10/` (12 files) — **not canonical, not citable as
`SC-nn`; reviewable as lineage only, and no finding may rest on it.**

**Upstream primary sources the reviewer must reach independently** — *rebuild the frame, do not inherit it;
the findings that mattered in this programme were found by refusing to inherit:*
the Boss rulings (`BD-ACC-01`/`02`/`03A`/`03B`, Phase S closure, `Q-BOSS-02`, `BD-02`, `BD-04`,
`MTI-D-01/02/03`) · the 16-element handoff-contract approval · **`SMEPLUS-DR-EXIT-8C-001` on
`origin/SMEsPlus`** · `SA_CORR3_03`, `SA_CORR3_07`, `SA_CORR3_08` · `SA_CORR4_01`, `SA_CORR4_03` · `SA10` ·
`08_JT04`, `09_JT05` · `03_INVENTORY_FUNCTIONAL_DESIGN_V1` · the `P01`/`P02` deployed-evidence packages ·
the AR branch at head **`822cb327`**.

---

## 5. Where the reviewer should attack first

**Named by the audited party against its own work.**

| # | Target | Why |
|---:|---|---|
| **1** | **`SC-26` §3 — the `phase` × 1 vs `state` × 22 finding** | It is this round's most consequential claim **and it weakens the instruction this executor operates under.** Attack the token counts and the §4/§11 reading |
| 2 | **`EC-04`'s `0 of 3`** and the `PATH-1` rejection | If a lawful minimum harness exists that `RC-V-01` does not bar, the deadlock is smaller than claimed |
| 3 | **`C2-D-02`'s closure** — the one SMEs Core closure that removed a Boss item | Its reversal lever is published; test whether it should have been pulled |
| 4 | **The `23` count and `F5 = 6`** | Three parties converged; **convergence between parties who read each other is not independence** |
| 5 | **`E2E-04`** — a re-grade attempted, withdrawn, and deliberately not reinstated | The specification bearing on it was written by the audited party |
| 6 | **`EC-06`** — the end-to-end negative-claim sweep **deliberately not run** by SMEs Core | The audited party's own uninspected surface |
| 7 | **`XMC-F-03`'s zero-length-chain weakness** | Published, unanswered; the `F3` recommendation rests on it |
| 8 | **`SC-24`'s refusal to disposition the collision** | Test whether an explicit supersession exists that this executor's search missed |

---

## 6. Pass protocol

**`EC-07`, verbatim:** *"at least two consecutive fresh independent passes must complete without any of the
following: new material population · new material finding class · new gating unknown · reopened
tolerance-zero issue · new Gate-changing contradiction · evidence-integrity failure. **Reviewer findings
must themselves be independently verified before acceptance.**"*

### 6.1 Reset triggers, made testable

| Trigger | Test |
|---|---|
| new material **population** | a denominator changes, or one not previously declared is required |
| new material **finding class** | a defect of a kind not already in the registers |
| new **gating unknown** | an unknown that blocks the gate and carries no disposition |
| **reopened tolerance-zero** | any of the 3 boundaries changes state, or a 4th is identified |
| new **Gate-changing contradiction** | a contradiction that changes what the gate may do |
| **evidence-integrity failure** | a manifest mismatch, an unresolvable citation, a moved baseline, or a claim whose instrument cannot be shown to fire |

**On any trigger: `CORRECT → VERIFY → RE-FREEZE → RESET COUNT TO 0`.**
Two clean passes must be **consecutive**. Clean → non-clean → clean is **`1`**, not `2`.
**No internal adversarial round is pre-counted.** `EC-07` is currently **`0 of 2`**.

### 6.2 Acceptance and evidence verification

> ***"`Independent Review != Truth. Verified Evidence = Truth Basis.`"*** — `EC-07`'s own words.

A reviewer finding is verified at primary source **before** acceptance — **and so is a reviewer
disproof.** This programme's record includes an independent review committing its own bounded-enumeration
false negative. **Corrections are made by the artefact's owner, then re-verified: the reviewer reports, the
owner repairs, the count restarts.**

### 6.3 The `Q-BOSS-02` §4 required flow, adopted

`Owner bounded correction → Freeze corrected surface → Structurally independent challenge → Independent
evidence publication → Veto re-evaluation → Cross-package verification → Closure criteria review`

---

## 7. Reviewer prohibitions

Redesign or mutate any owner artefact (controls 4, 7) · rule any Boss decision or `FG-F-06` · discharge,
re-word or narrow any veto (control 8) · declare `PASS`, gate closure, merge, release or production
readiness (control 9) · select or influence the second reviewer · inherit this executor's evidence frame ·
treat the quarantined package as canonical.

---

## 8. Terminal ladder

| Step | Terminal |
|---|---|
| `EC-05` closed **and** `8C-BOUNDARY-01` answered | **precondition met** |
| Boss appoints | `EC-07 SEQUENCE OPEN — PASS 1 COMMISSIONED` |
| Pass 1 clean | `EC-07 1 OF 2` |
| Pass 1 non-clean | verify → owner corrects → re-verify → re-freeze → **count restarts at `0`** |
| Pass 2 clean, consecutive | **`EC-07 SATISFIED — 2 OF 2`** |
| After that | **`EC-04` and `EC-08`'s two absences remain open.** The gate is **not** thereby open |

> **`EC-07` satisfied is not Phase SA exit.** `EC-04` fails independently and no number of clean passes
> closes it (`SC-26` §6).

---

## 9. Checkpoint

> ## `CP-SA-SC-210 — INDEPENDENT REVIEW PACK READY (NOT ACTIVATED)`
> **Ten `Q-BOSS-02` controls carried verbatim · **the named eligibility class surfaced and this executor
> cited as `NOT ELIGIBLE` on Boss's own words** (`SC-F-14`, correcting `SC-EC07-02`) · 5 disqualifying
> conditions · baseline prepared with a mandatory re-freeze instruction · 8 attack targets, the first of
> which undermines this executor's own governing instruction · reset triggers testable · **`0` reviewers
> appointed, `0` passes opened, `0` independence claimed** · pack **READY, NOT ACTIVATED** pending two
> Boss answers.**

No Evidence = No Progress. Never Skip Gate. A party cannot be structurally independent of itself.
Boss remains the sole Final Approver.
