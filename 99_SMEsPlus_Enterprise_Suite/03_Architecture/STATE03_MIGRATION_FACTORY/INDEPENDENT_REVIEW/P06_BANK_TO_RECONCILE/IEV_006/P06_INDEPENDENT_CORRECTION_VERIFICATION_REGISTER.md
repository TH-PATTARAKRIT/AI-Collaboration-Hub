# P06_INDEPENDENT_CORRECTION_VERIFICATION_REGISTER.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-INDEPENDENT-EXTERNAL-CORRECTION-VERIFICATION-006]` · prompt commit `51763d8`
**Track:** INDEPENDENT EXTERNAL VERIFICATION · branch `audit/p06-independent-verifier-2026-09-06-001`
**Frozen audit surface:** `1b018c104001eb4683166518a6161a8cd8ab5cee` · tree `04f90a80…` · 87 files · digest `09c54632…`
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 0. INDEPENDENCE — THE PROMPT'S OWN PRECONDITION IS NOT MET

Prompt §1: *"**THIS PROMPT MUST NOT BE EXECUTED BY THE SAME P06 CORRECTION ACTOR / OLD P06 SESSION THAT AUTHORED THE REPAIRS.** The verifier must begin from a fresh independent session/context."*

**That precondition is not satisfied. The context executing this prompt is the context that authored the 21 `REV-E-23` repairs under audit.** It was directed to proceed and has proceeded, and the conflict is recorded here first because everything below inherits it.

**What was nonetheless achieved, and is real:**
- a **fresh clone** on a separate branch, never the research branch;
- a **frozen tree** proved by SHA, extracted and verified byte-identical 87 of 87;
- populations derived from `git ls-tree`, **never from the author's tally**;
- **four AAS-03 challengers in genuinely separate contexts**, which never saw the authoring, never saw each other, and were given only the frozen path and their own remit.

**What is not achieved:** the same model family; the executor wrote the challengers' briefs and adjudicates their output; and the executor is the author of the repairs it is grading.

> ### Consequence, stated before any finding: **`AASP-VETO-07 — PRESERVED`, and the §9 discharge recommendation is unavailable to this verifier on the prompt's own terms, independently of what the evidence shows.**

**And the evidence does not support discharge either.** What follows would preserve the veto even from a properly independent party.

## 1. Method

Prompt §5 Stages A–E. Instruments, controls and blind spots: `P06_VERIFICATION_INSTRUMENT_CONTROL_REGISTER.md`. Populations: `P06_CLAIM_CLASS_POPULATION_REGISTER.md`. Every challenger claim was **re-executed against the frozen tree before adoption**; two were refuted.

**`IEV-I-01` — this verifier's own first instrument failed and its positive control caught it.** Nine claim-class sweeps held their glob list in a shell variable; zsh does not expand those. The control returned **0 occurrences of `P06` across an 87-file P06 package** and all nine classes returned zero. **Without the control this audit would have certified nine clean classes on nine fabricated zeros.** That is `VER-E-02` — a defect the audited package documents — committed by its auditor, at the first attempt.

## 2. Repair-integrity register (Stage D)

`Repair ID | Claim Class | Original Location | Current Location(s) | Denominator | Independent Method | Result | Downstream Propagation | Disposition`

| ID | Class | Original | Current | Denominator | Method | Result | Downstream | Disposition |
|---|---|---|---|---|---|---|---|---|
| `R23-01` | is_matched qualifier | `01_`:115 *"unconditionally"* | `01_`:115 | 4 branches / 5 sites, source-verified | re-executed `account_payment.py:436-452` | **CORRECT in substance** — `:450` is gated at `:447` | — | **VERIFIED**, with two defects **on the same line** — see `IEV-D-06`, `IEV-D-07` |
| `R23-02/03` | population; peer status | `13_`:94 *"58"*; `13_`:103 *"P01 absent"* | same | all 87 files | ran both printed commands | `:103` **CORRECT**; **`:94` WRONG — 65 published, 67 measured** | evidence manifest | **DEFECT — `IEV-D-01`** |
| `R23-04/05` | peers read; population | `18_`:169; `18_`:214 | same | — | `git ls-remote`; id count | `:169` **CORRECT**; **`:214` publishes 65/three vetoes/— into the P11 pack** | **P11** | **DEFECT — `IEV-D-01`, `IEV-D-02`** |
| `R23-06` | population (round-local) | `21_`:42 | same | — | read | **CORRECT** — the right instrument for the defect | — | **VERIFIED** |
| `R23-07` | generation gap | `24_`:42 | same | — | read against `51_` | **CORRECT** | — | **VERIFIED** |
| `R23-08/09/10` | tally; ordinal ×2 | `34_`:51, `:57`, `:81` | same | 20 `F-` rows | counted Disposition column: 10/4/2/3/1 = 20 | `:51` **EXACT**; `:57`/`:81` correct **but `:57` claims two ordinals where three exist** | **P11** | **DEFECT — `IEV-D-04`** |
| `R23-11/12` | eighth door | `35_`:97, `:99` | same | — | read against `55_` | **CORRECT** | all peers | **VERIFIED** |
| `R23-13` | eighth door | `36_`:58 | same | — | read | **CORRECT** | all peers | **VERIFIED** |
| `R23-14` | generation gap | `40_`:69 | same | — | read against `51_` | **CORRECT**, but the retired half survives at `18_`:188 | **P11** | **DEFECT — `IEV-D-05`** |
| `R23-15` | supersession pointer | `41_`:6 (inserted) | same | 5 cited lines | resolved each cite | **DEFECT — all five cites wrong by exactly 3; the insertion shifted the file it points into** | — | **DEFECT — `IEV-D-03`** |
| `R23-16` | generation gap | `42_`:53 | same | — | read | **CORRECT** | — | **VERIFIED** |
| `R23-17` | population | `46_`:124 | same | its own printed command | executed it | **WRONG — states 65, returns 67**, on the line that states the rule about stale printed results | severity register | **DEFECT — `IEV-D-01`** |
| `R23-18` | unit declaration | `52_`:55 | same | — | read | **CORRECT** | — | **VERIFIED** |
| `R23-19/20/21` | evidence base | `56_`:68, `:70`, `:78` | same | 6-row table | read | **CORRECT as written** — but **5 of the 6 rows of the same table are unrepaired** | — | **DEFECT — `IEV-D-08`** |
| `R23-22` | unit declaration | `62_`:35 | same | — | read | **CORRECT** | — | **VERIFIED** |
| `R23-23` | population | `70_`:108 | same | — | id counts | **WRONG on three figures in one sentence: 65 (67), "four active vetoes" (7), "16 author errors" (23)** | **P11** | **DEFECT — `IEV-D-01`, `IEV-D-02`** |
| `R23-24` | snapshot marker | `SOURCE_LINK…`:151 | same | — | read | **CORRECT** | — | **VERIFIED** |

**14 of 24 repairs verify clean. 10 carry or expose a defect.**

## 3. Material defects — every one re-executed by this verifier

| ID | Defect | Evidence | Material |
|---|---|---|---|
| **`IEV-D-01`** | **The corrected blocker count is wrong: 65 published, 67 measured — at every declared scope.** Root-only `*.md` → **67**; `*.md G02_CLOSURE/*.md` → **67**; all 87 → **67**; ids contiguous `B-01`…`B-67`. `B-66`/`B-67` are defined at `40_`:269-270, **inside both printed commands' own glob, created by the same round**. The standing authority (`AUTO_RESUME`:147) says **67** and disagrees with four of its own repairs | `13_`:94 · `46_`:124 · `18_`:214 · `70_`:108 | **YES** |
| **`IEV-D-02`** | **Two outbound sign-offs carry stale figures beside the corrected one, in the same sentence.** `18_`:214 *"three vetoes"* and `70_`:108 *"four active vetoes"* — **seven exist** (`AASP-VETO-01`…`07`). `70_`:108 *"16 recorded author errors"* — **23 exist**. The repair fixed one number and left two | `18_`:214 · `70_`:108 | **YES** |
| **`IEV-D-03`** | **The `41_` supersession pointer sends readers to five wrong lines.** It cites `:23`, `:33`, `:35`, `:101`, `:113`; the content is at `:26`, `:36`, `:38`, `:104`, `:116` — off by exactly 3, because **inserting the 3-line pointer shifted the file it points into.** `:35` is a blank line; `:113` is a table separator. Its stated purpose was *"so a reader cannot mistake a record for a current claim"* | `41_`:6 | **YES** |
| **`IEV-D-04`** | **`34_`:57's correction claims the file gave the finding "two different ordinals"; it gives three.** `34_`:32 (`F-04`) is untouched: *"CONTESTED, **four entry points** … P05 confirms **a fifth path** with no payment object at all"* — an ordinal read against a population of payment-intent entry points, which `SR-04` cannot join because it produces no payment object. **The unit conflation `REV-E-12` withdrew, re-committed against a second denominator** | `34_`:32 vs `:57` | **YES** |
| **`IEV-D-05`** | **`18_`:188 retains the exact half of `B-44` that `40_`:69 declares retired** — *"If the target has moved to 19, a material fraction of this package is scoped to a superseded line."* Four lines below `18_`:184, which carries the narrowing. REV-E-23 opened `18_` twice and did not reach `:188` | `18_`:188 | **YES** |
| **`IEV-D-06`** | **`01_`:122 cites `:437` as the circular assignment site; it is `:438`.** `:437` is `pay.is_reconciled = False`. The same file gets it right at `:109` and `:114`. The off-by-one survived `REV-E-21`, `REV-E-22` **and** `REV-E-23` while that paragraph was edited three times | `01_`:122 | **YES** |
| **`IEV-D-07`** | **`01_`:122 says two branches are `True` "by configuration alone"; its own appended correction says one.** Branch 3 (`:444`) is gated by **zero amount**, not configuration; only branch 4 (`:450`) is configuration-gated. A zero-amount test is not a configuration. And `R23-01`'s insertion at `:115` orphaned the sentence tail — *"With no bank statement in existence**."* is now subjectless with an unclosed emphasis | `01_`:115, `:122` | **YES** |
| **`IEV-D-08`** | **The retired "filtered" reading survives in 13 CURRENT statements across 7 files, under variants no declared pattern could match.** `filtered subset` (`51_`:21) · `filtered to the Thai deployment` (`12_`:154, `38_`:58, `51_`:22) · `filtered checkout` (`38_`:57) · `filtered 791-addon tree` (`56_`:62,64,65,66,67 — **five rows of the six-row table whose sixth row `:68` was repaired**) · `filtered-evidence-base` (`18_`:208, `66_`:42) · and **`56_`:53, the mandated permitted form for every future negative**: *"NO DEFINITION FOUND IN THE FILTERED 791-ADDON v18 TREE…"* | 7 files | **YES** |
| **`IEV-D-09`** | **`51_` publishes the retired reading in three places, carries no correction marker at all, and rests `B-55` on a denominator that inverts.** `:22` cites *"791 versus 1422"* as proof of filtering — but on the corrected denominator the v18 population is **1752**, *larger* than v19's 1422. **The comparison does not prove what it is cited for**, and `51_` is the authority every `B-44` narrowing cites | `51_`:21, `:22`, `:93` | **YES** |
| **`IEV-D-10`** | **`36_`:42-43 gates four items on "P08's absence" and prescribes "One publication closes the chain."** P08 was published and read in round 3; the same file corrects the premise at `:13`, `:33`, `:61`. The remedy is also wrong — `34_`:51 establishes the rows stay open *"because no ruling exists, not because no package exists"*. The pattern `unpublished\|not published` cannot match the noun **"absence"** | `36_`:42-43 | **YES** |
| **`IEV-D-11`** | **`40_`:17 and `:35` still say "7 of 9 peers read" and "P01 and P08 remain"**, while `:79` and `:126` of the same file were corrected under `REV-E-22`. Expressed as an ordinal count, invisible to a phrase-scoped sweep | `40_`:17, `:35` | **YES** |
| **`IEV-D-12`** | **`34_`:44 asserts a peer *accepted* a P06 row, and cites P06's own sentence as the evidence.** *"P11 intakes it as a new scope-mismatch row: 'Reconciliation must be journal-scoped, not account-scoped'"* / *"**SETTLED — accepted into P11's matrix**"*. That quotation occurs exactly twice in the frozen tree: `09_`:80, where it is **P06's own consequence**, and here. Meanwhile `35_`:158 calls the same rows *"net-new"* to P11's matrix and `37_`:60 says they *"will land"* in it. **This is the only place in the package where P06 records a peer acceptance, and it is the shape `AASP-VETO-06` exists to forbid** | `34_`:44 | **YES** |
| **`IEV-D-13`** | **`P06_AAS_PLUS_CONSOLIDATION.md`:50 states `HO-03`/`HO-04` *"are labelled so"* [WRITTEN, NOT DELIVERED]. They are not.** The handoff pack contains exactly **one** line matching `WRITTEN\|DELIVER\|deliver`, and it is `:187` — *"`HO-04` → P10 — the `X-08` answer, **re-delivered**"*. `HO-03` carries no delivery label at all. **Two governance statements certify this "verified by grep"** (`CHECKPOINT`:73, `PROPAGATION_MATRIX`:128) **for a string that is not in the artefact** | handoff pack `:187` | **YES** |
| **`IEV-D-14`** | **`18_`:7 and `:212` publish completion language on the outbound pack** — *"READY FOR CORE ACCOUNTING RECONCILIATION"*, *"TARGETED BLOCKER CLOSURE COMPLETED"* — while the terminal state at the same commit is **`INDEPENDENT VERIFICATION NOT PROVABLE — EVIDENCE INTEGRITY HOLD`** under seven vetoes. REV-E-23 edited `:214`, two lines below `:212` | `18_`:7, `:212` | **YES** |
| **`IEV-D-15`** | **`37_` reconciles against "seven" peer scope matrices while enumerating eight, and P08 is in neither figure.** P08 was read and carries scope determinations P06 itself quotes (`53_`:72). `SCR-F-03`'s *"no counterpart row in **any** peer scope matrix"* rests on a path set with an undeclared exclusion — and it feeds `34_`:44, `35_`:158 and `36_`:30 | `37_`:5, `:11`, `:52` | **YES** |
| **`IEV-D-16`** | **`12_`, designated *"the controlling denominator document"*, says "Branches read (7)", lists eight, and omits P08 entirely.** `13_`:103 says *"8 of 9 READ stands"*. **The manifest and the controlling denominator document disagree on the peer read set**, and every P08 citation rests on a source the denominator document does not declare | `12_`:133 | **YES** |
| **`IEV-D-17`** | **`52_`:86 claims *"An independent sweep of all nine peer branches"*** while `38_`:92 (`OQ-128`) records that **P01 has never been consumed** and `OQ-124` that consuming it is out of bounds. No command, denominator or path set is published for the sweep | `52_`:86 | **YES** |
| **`IEV-D-18`** | **`09_`:13 and `:98` still state *"P06 is a terminal process"* / *"P06 owns nothing else"***, the framing P06 formally withdrew on P11's evidence (`34_`:15-19, `35_`:34-42). `34_`:5 scopes its supersession to the *status column* only, by design — so the narrative of the ownership file of record is untouched, and `09_` is indexed in the outbound pack at `18_`:123 | `09_`:13, `:98` | **YES** |

**18 material defects, every one re-executed by this verifier against the frozen tree.**

## 4. Challenger claims REFUTED (§5 — re-checked before adoption)

| Claim | Re-check | Verdict |
|---|---|---|
| E1 `F8` — *"`34_`:40/:99 use 'delivered' contrary to `AASP-VETO-06`"* | Both read *"The answer is **delivered; the dependency is NOT closed**"* and *"**delivered, not accepted**"* — each qualified in the same clause | **NARROWED, not material.** The unqualified instances are `35_`:148 and the `HO-04` heading, which are carried separately |
| E4 — *"`VER-E-04` does not reproduce; the regex returns 4 hits with EXIT=0"* | **ADOPTED, and it corrects this verifier's own register.** `VER-E-04` as documented is not reproducible under `/usr/bin/grep`; the package's entry should name the tool and version. This verifier's instrument register is amended accordingly | **ADOPTED against myself** |

## 5. What verifies clean — recorded because an audit that reports only failures is not an audit

- **The source layer is sound.** `is_matched` structure (4 branches / 5 sites), every v18 and v19 line number sampled, the `account_move` SQL quotation, and all eight enumerative version counts re-execute exactly. Two of three re-tested cross-version rows are byte-identical across generations.
- **The `X-08` family is clean** — 11 current statements across 7 files, all reading *answered by P06, closure is P10's, still `OPEN — PEER EVIDENCE` at `1fea562`*. **No survivor asserts closure.** Three rounds got this surface entirely right.
- **`34_`:51's tally is exact** — independently counted: 10 SETTLED · 4 CONTESTED · 2 UNOWNED · 3 OPEN · 1 HOLD = 20 rows.
- **The repair arithmetic reconciles.** *"21 repairs … plus 3 supersession/snapshot markers"* = 24; measured 24.
- **`P06-OQ-*` = 75 and `REV-E-*` = 23 both reproduce** against the standing authority.
- **Every §6 protected item is preserved**: `P06-B-08` `BOSS DECISION REQUIRED`, `P06-B-09` statutory, `P06-OQ-98` `HOLD`, `X-08` peer-owned, `AASP-VETO-07` nowhere discharged. Every apparent exception was inspected individually and is a quotation or a *"must not assume"* warning.
- **Time-bounded negatives are correct as written and must not be swept**: `12_`:84, `12_`:134, `11_`:85, `09_`:34-35, `53_`:15.
- **Zero real broken-emphasis instances.** All four `****` are quotations inside code spans.
