# SC-13 — `FG-F-06` SCOPE CLARIFICATION CARD

## CP-SA-SC-120 — `FG-F-06` CARD EVIDENCE-COMPLETE

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`
Execution host: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **This is a BOSS SCOPE CLARIFICATION. It is NOT one of the 23 atomic Boss decisions, and no evidence
> defines it as one.** It is a question about **what a Boss ruling covers**.

---

## 0. The question

> ## `Does SMEPLUS-DR-EXIT-8C-001 bind the Phase SA exit?`

**The instrument.** `SMEPLUS_VERY_DEEP_RESEARCH_8_CRITERIA_UNIVERSAL_EXIT_CONSTITUTION.md`, read on the
current default branch. Constitution ID `SMEPLUS-DR-EXIT-8C-001` · Status **`BOSS APPROVED / PROJECT-WIDE
MANDATORY`** · Effective `2026-09-04` · Scope **`ALL MODULES / ALL STATES / ALL FUTURE VERY DEEP RESEARCH`**
· Depth baseline `VERY DEEP / L99999.99999`.

**What turns on it — `EC-07`, verbatim:**

> *"Before Final Research Gate, at least two consecutive fresh independent passes must complete without any
> of the following: new material population · new material finding class · new gating unknown · reopened
> tolerance-zero issue · new Gate-changing contradiction · evidence-integrity failure. Reviewer findings
> must themselves be independently verified before acceptance."*

**Phase SA has completed `0` independent passes.**

---

## 1. Reading A — IT BINDS the Phase SA exit

**Surviving primary grounds only. Two previously-offered grounds have been removed (§3).**

| # | Ground | Primary text |
|---|---|---|
| **A-1** | **The widest scope line in the corpus** | **`ALL MODULES / ALL STATES / ALL FUTURE VERY DEEP RESEARCH`**, status **`PROJECT-WIDE MANDATORY`**; §2 closes: *"none of the eight constitutional Exit Criteria may be weakened, removed, bypassed, or treated as optional **without explicit Boss approval**"* |
| **A-2** | **§2 item 4 names what Phase SA structurally is** | *"This Constitution applies to: … **4. Cross-Module and Whole-System State Integration Review.**"* Phase SA's own artefact directories are `PHASE_SA_CROSS_MODULE_ASSURANCE`, `…_CROSS_MODULE_RECHALLENGE`, `…_CROSS_MODULE_CONTRACT_PROOF`; its subject is the 22 joint cross-proof scenarios and the 18 end-to-end flows |
| **A-3** | **§4's trigger is *"next controlled phase"*, not only *"next State"*** | *"No Module may advance to its **next controlled phase** or State unless `EC-01 PASS` … `EC-08 PASS`."* Phase SA → Pre-Test **is** a next controlled phase |
| **A-4** | **The programme already treats this work as Very Deep Research** | The Boss closure artefact: *"the function **returns to targeted Very Deep Research**"* · `SA_CORR3_13`'s own header: **`PHASE SA · CORR3 · TARGETED VERY DEEP RESEARCH — EXECUTED, NOT CARRIED`** · **every Phase SA prompt, including this one, carries `/L99999.99999`**, which is the constitution's own §6 depth baseline and appears nowhere else in the programme's vocabulary *(peer track ground, adopted)* |

**Consequence if Boss chooses A.** **`EC-07` fails on zero passes.** **`B-7` becomes MANDATORY and
gate-blocking**, and **two consecutive clean structurally independent passes become mandatory before
Phase SA exit.** No amount of further SMEs Core work can satisfy `EC-07`. The self-assessment at §5 becomes
live, and `EC-04` and `EC-06` also require attention.

---

## 2. Reading B — IT DOES NOT BIND the Phase SA exit

**Exact primary grounds only. Three of the five are peer-track grounds this session did not have.**

| # | Ground | Primary text |
|---|---|---|
| **B-1** | **Every operative noun is *Module* or *State*, and Phase SA is neither** *(peer ground, adopted)* | §3: *"**A Module or State** may advance…"* · §4 is titled **Module Exit Rule** · §5 **State Exit Rule** · §11's two operative rules read *"NO **MODULE** MAY ADVANCE TO THE NEXT CONTROLLED **STATE**…"* and *"NO **STATE** MAY ADVANCE TO THE NEXT STATE…"*. §4's subject is ***No Module***. The Modules are Account, Inventory, Manufacturing; **Phase SA is a cross-module assurance activity inside `STATE03`** |
| **B-2** | **§2 items 3 and 5 are not engaged** *(this session's ground, `SC-V-01`)* | §2.3 is *"Every **STATE** before advancement to the next STATE"* and §5 is the **State** Exit Rule. **Phase SA sits inside `STATE03`; its exit is to Pre-Test, not to `STATE04`.** Both engage later, at `STATE03 → STATE04` |
| **B-3** | **Designation is Boss's act, and none is recorded** *(peer ground, adopted)* | §2 item 5: *"All future research programmes **designated by Boss** as Very Deep Research."* **Searched: no artefact records Boss designating Phase SA as Very Deep Research.** The nearest hits are a *return* to targeted VDR for a specific function, and one self-labelled CORR3 sub-study — **neither is a Boss designation** |
| **B-4** | **Phase SA has its own gate rules, and they have governed six rounds** *(peer ground, adopted)* | Every Phase SA prompt sets its own terminal conditions, checkpoint ladder, prohibitions and Boss-gate rule. **CORR1 through the Final Boss Gate ran under those rules and none invoked `EC-07`** |
| **B-5** | **The constitution's subject is Very Deep *Research*, and Boss separated the two** | The Boss closure describes Phase SA as *"synthesis; architecture; conceptual/domain design … **and controlled return to Very Deep Research where required**"* — language treating Phase SA as **not itself** Very Deep Research. `EC-07`'s own trigger is *"Before **Final Research Gate**"*; Phase SA's gate is an architecture gate |

**Consequence if Boss chooses B.** The gate stands on `SC-15`'s three categories. **`B-7` blocks nothing —
but it does not disappear:** it remains a required Boss **act** (`SC-12` #1) and SMEs Core still recommends
performing it. **`RC-V-01` independently requires an independent check before any implementation start**,
so an independent-review obligation survives Reading B regardless — it simply attaches to **build**, not to
**Phase SA exit**. Any independent-challenge handoff material is preserved as **optional assurance
evidence** and **must not be represented as having been required**.

---

## 3. Two grounds REMOVED from Reading A — and why

| Removed ground | Why it is removed |
|---|---|
| **The `SA_CORR3_07` precedent** *("a Phase SA round already applied this constitution")* | **`AR-F-02`, verified at primary source by this session.** `SA_CORR3_07` §2.5 grades a package **`PROVISIONAL / NON-CANONICAL`** — and that wording is **§9, the AAS+ / Design Handoff Rule**: *"AAS+ may explore designs in parallel only as `PROVISIONAL / NON-CANONICAL` while parent Very Deep Research is not yet complete."* **Not §4's Module Exit Rule. Not `EC-07`.** **Applying one clause of a constitution is not adopting it as your exit gate.** The fact survives — a Phase SA artefact did reach for this constitution — but **on `EC-07` the precedent is silent** |
| **§2.3 and §5 as Reading A application points** | **`SC-V-01`.** Both operate at **State** level and Phase SA's exit is not a State advancement. **Carried to Reading B as ground `B-2`** |

> **Both removals were made by the executing side against its own preferred direction's opponent — and
> both narrow Reading A, which is the reading that would hold this gate.** Recorded because a card that
> only ever weakens one side is not a card.

---

## 4. The honest balance

| Evidence line | Reading A | Reading B |
|---|---|---|
| Scope line `ALL MODULES / ALL STATES` + `PROJECT-WIDE MANDATORY` | **strongly for** | — |
| §2 item 4 — cross-module state integration review | **strongly for** | — |
| §4 wording *"next controlled phase or State"* | **for** | **against** — the subject is *No Module* |
| §3 / §4 / §5 / §11 operative nouns | — | **strongly for** |
| §2.3 and §5 application points | — | **for** (`SC-V-01`) |
| Boss designation as Very Deep Research | — | **for** — none found |
| `/L99999.99999` on every Phase SA prompt | **for** | — |
| Phase SA's own gate rules, six rounds | — | **for** |
| **The one precedent** | **silent** — it is §9 (`AR-F-02`) | **for**, at clause level |

> **Neither reading is unreasonable and the text does not settle it.** §2 item 4 describes Phase SA's
> activity; §4 and §11 describe a subject Phase SA is not. **That is a scope ambiguity in a Boss-approved
> instrument.**

---

## 5. If Reading A binds — self-assessment against all eight criteria

**Self-assessed. NOT independently verified. Offered so Boss is not choosing blind.**

| Criterion | Assessment | Basis |
|---|---|---|
| `EC-01` Scope Bounded | likely satisfied | every round declares POPULATION / UNIT / PATH SET / PATTERN and its blind spot as the complement |
| `EC-02` Enumeration Converged | likely satisfied | **23** summed from rows against a unit declared before the total |
| `EC-03` Unknown Exhausted | likely satisfied | every open item carries an owner and a class |
| `EC-04` Tolerance-Zero Closed | **UNTESTED — the honest answer** | `CF-I-03` `D3` is `CRITICAL — TOLERANCE ZERO` and is **specified, not proven**. Whether *closed* means specified or proven is **part of this same scope question** |
| `EC-05` Contradiction Resolution Complete | likely satisfied | `G2` is the one live contradiction and it is dispositioned to the `C4-D-02` review |
| `EC-06` Negative Claim Controlled | **improved, not clean** | this session ran positive controls on multiple negatives and **found one instrument dead before believing its zero** (`SC-F-01`). The peer track published **two** of its own (`AR-I-01`, `AR-I-02`). **A criterion that keeps catching its own failures is working; it is not thereby passed** |
| **`EC-07` Two Consecutive Clean Independent Passes** | **FAILS** | **zero independent passes.** **And `EC-07` may be unsatisfiable as written for this phase** — see §6 dissent 3 |
| `EC-08` Final Knowledge Package Complete | likely satisfied | every named artefact class exists with branch, commit and paths |

---

## 6. SMEs Core position

> # `NO AUTHORITY TO SELF-SELECT — BOSS SCOPE CLARIFICATION REQUIRED.`

**No existing Boss ruling settles it.** The governing precedent for this exact class is `CF-D-01`'s:
***"only Boss may state what a Boss ruling covers."***

**And the direction is declared.** Reading B is the reading that lets this gate open — the direction an
executing party is biased toward. **Two independent tracks have now each narrowed Reading A** (`AR-F-02`
removed its precedent; `SC-V-01` removed two of its application points) **and neither adopted the
conclusion those narrowings point toward.** Adopting Reading B here would make that record worthless.

### 6.1 The peer track's recommendation — recorded, attributed, NOT adopted

The AR track offered a **third form**, and it is preserved because Boss may prefer it:

> *"**Reading A on substance, scoped by Boss's own words rather than by inference.** Direct that the eight
> criteria apply to the Phase SA exit **as a Boss instruction**, and that `EC-07`'s two passes be satisfied
> by the `B-7` challenger. This gets the assurance `EC-07` exists to provide without deciding, by
> inference, that a research constitution silently governs every architecture phase in the programme."*

**SMEs Core neither adopts nor rejects it**, under the no-self-selection rule above. It is on the ballot at
§7 as a Boss option.

**The peer's own three dissents against its own recommendation, carried verbatim in substance:**

1. **It is the expensive answer, recommended by the party that would be audited** — a direction the
   record shows is *not* the one an executor is usually biased toward, *"which is itself worth Boss's
   scepticism in the opposite direction."*
2. **Reading B is textually strong on the operative clauses.** A reader who weights operative clauses over
   scope headers reaches B.
3. **`EC-07` may be unsatisfiable as written for this phase.** It requires two consecutive passes with **no
   new material finding class** — and **every Phase SA round so far has produced one**, including the peer's
   (`AR-F-01`, `AR-F-02`) and this one (`SC-F-08`, `SC-F-09`). **Boss should know that adopting `EC-07` may
   mean more than two passes, and should say what happens if passes keep finding things.**

---

## 7. What Boss answers — one line

```
FG-F-06 = READING A                 the constitution binds the Phase SA exit; EC-01..EC-08 apply
FG-F-06 = READING B                 it does not; Phase SA's own gate rules govern
FG-F-06 = READING A BY DIRECTION    the criteria apply because Boss directs it, not by inference
```

| Answer | Immediate effect |
|---|---|
| **A** or **A BY DIRECTION** | **`B-7` becomes gate-blocking.** Phase SA holds until two consecutive clean independent passes complete. **Boss should also state what happens if passes keep producing material findings** (§6 dissent 3) |
| **B** | The gate stands on `SC-15`. **`B-7` remains a recommended act that blocks nothing.** `RC-V-01`'s independent check still bars **implementation start**. Any independent-challenge handoff is preserved as **optional** assurance and **is not represented as required** |

---

## 8. Checkpoint

> ## `CP-SA-SC-120 — FG-F-06 CARD EVIDENCE-COMPLETE`
> **Both readings built from the constitution's own primary text · Reading A: **4** surviving grounds,
> **2 removed** (`AR-F-02`, `SC-V-01`) · Reading B: **5** grounds, **3 of them adopted from the peer
> track** · 9 evidence lines scored either way · 8-criteria self-assessment published with `EC-04`
> UNTESTED and `EC-07` FAILING · peer recommendation recorded, attributed and **not adopted** · peer's
> three dissents carried · **SMEs Core: `NO AUTHORITY TO SELF-SELECT`** · **not counted among the 23**.**

No Evidence = No Progress. Never Skip Gate. Only Boss may state what a Boss ruling covers.
Boss remains the sole Final Approver.
