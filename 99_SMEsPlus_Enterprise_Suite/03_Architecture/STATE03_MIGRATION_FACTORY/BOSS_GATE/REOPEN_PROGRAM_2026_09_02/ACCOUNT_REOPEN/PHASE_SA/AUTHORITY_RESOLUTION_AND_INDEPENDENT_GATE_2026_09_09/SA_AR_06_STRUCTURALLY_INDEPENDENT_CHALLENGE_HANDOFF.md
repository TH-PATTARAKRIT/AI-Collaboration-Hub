# SA_AR_06 — STRUCTURALLY INDEPENDENT CHALLENGE HANDOFF

## CP-SA-AR-60 — INDEPENDENT CHALLENGE PACKAGE READY

**This package is executable by a reviewer who trusts none of this session's conclusions.**
It is **not** an independent pass. It is what an independent pass would need.

---

## 1. THE CLAIM THIS PACKAGE MAKES ABOUT ITSELF

| | |
|---|---|
| Structurally independent Phase SA review | **NONE — not appointed, not performed, not claimed** |
| Internal adversarial self-challenge | **performed** — `SA_AR_09`, and 19 findings in the parent round |
| `EC-07` clean independent passes | **0 of 2** |
| Fabricated assurance anywhere in the package | **none** |

**Same-model agents, internal personas, parallel subagents and self-challenge are
`INTERNAL ADVERSARIAL SELF-CHALLENGE`.** They are not `STRUCTURALLY INDEPENDENT ASSURANCE`, and this
package never counts them as such. The programme's own record puts the ratio at roughly **3 self-caught
to 29 externally caught** on one comparable package.

---

## 2. ELIGIBILITY — READ THIS BEFORE APPOINTING

`Q-BOSS-02` §2, verbatim: **"Claude Opus 5, where it authored or executed the repair being reviewed, is
`NOT ELIGIBLE` to perform the corresponding independent challenge for that repair."**

**This entire package was authored and executed by Claude Opus 5.** It is therefore ineligible to
challenge itself, and no part of this session may be represented as satisfying `EC-07`.

**"Eligibility is determined per repair / challenge pair. No verifier is presumed independent merely
because it is a different session or model."**

---

## 3. THE TEN CONTROLS THE REVIEWER OPERATES UNDER

Reproduced from `BOSS_DECISION_PHASE_S_Q_BOSS_02_2026_09_07.md` §1, read at source:

| # | Control |
|---:|---|
| 1 | **Model / Agent Separation** — not the model that authored the work under review |
| 2 | **Appointment Independence** — appointed by Boss or an independent governance authority, **never selected by the correction owner** |
| 3 | **Evidence Isolation** — a separate isolated session against a **frozen** evidence surface and bounded scope |
| 4 | **Read-Only Boundary** — read-only on owner evidence; must not edit the owner's artefacts |
| 5 | **Independent Reproduction** — independently reproduces the tests, counts, predicates and conclusions |
| 6 | **Independent Publication** — publishes its own artefact, branch and immutable commit SHA |
| 7 | **No Owner Mutation** — must not modify peer-owner branches |
| 8 | **No Self-Discharge** — must not discharge any veto |
| 9 | **No Self-Pass** — must not declare `PASS`, gate closure, release, merge or production readiness |
| 10 | **Boss Final Authority** — Boss remains the sole Final Approver |

> **Control 2 is why `B-7` is a Boss act and not a task this session can perform.** A session choosing
> its own challenger has produced no independence, however good the challenger.

---

## 4. THE FROZEN EVIDENCE SURFACE

| Layer | Commit | Content |
|---|---|---|
| **This package** | *(recorded in the resume state at publication)* | `SA_AR_00`…`SA_AR_11` + manifest |
| **Parent Final Boss Gate** | **`9d5bc2db`** | 13 files + manifest, verified 13/13 |
| **CORR5** | **`379fd073`** | 22 files, manifest 21/21 |
| **CORR4** | **`60752e2d`** | pre-gate closure |
| **CORR3** | **`604398c3`** | the proof round — `SA_CORR3_02`, `_03`, `_07`, `_08`, `_12` |
| **Mainline** | **`3f5d915a`** | post-merge default branch |
| **`Q-BOSS-02`** | **`2930723f`** | the independence ruling |
| **Exit constitution** | on `origin/SMEsPlus` | `SMEPLUS_VERY_DEEP_RESEARCH_8_CRITERIA_UNIVERSAL_EXIT_CONSTITUTION.md` |

**Nothing in this list may move while a pass is running.** The parent round recorded the opposite
failure — a freeze that cited three files which did not yet exist (`CHF-15`).

---

## 5. WHAT TO ATTACK — TWELVE FALSIFICATION CLASSES, WITH THE ENTRY POINT FOR EACH

| # | Class | Entry point | The specific thing to try to falsify |
|---:|---|---|---|
| 1 | **Wrong decision count** | `SA_AR_01` §3 | Is `F5` six decisions? Re-derive from `SA_CORR3_03`, not from this pack. **Three rounds have miscounted this family** |
| 2 | **False Boss escalation** | `SA_AR_03` §4 | Take any of the 24 and find a ruling that already settles it. Test A found none across 189 refs — **re-run it with your own instrument and your own positive control** |
| 3 | **Wrong authority owner** | `SA_AR_04` cards | Each card names a quotation and a file. Open the file. **`F8`'s "five independent instruments" was verified at one by this session** |
| 4 | **Suppressed source clause** | `SA_CORR2_02` §3.1 | The `E2E-04` sentence. **This session's predecessor quoted half of it and reversed a scenario grade.** Look for others of the same shape |
| 5 | **Hidden Category 3** | `SA_AR_02` §3 | 13 obligation rows, 12 unchanged. Find one that is a specification gap dressed as a runtime obligation |
| 6 | **Omitted downstream consequence** | `SA_AR_04` module rows | Every card claims per-module effects. Find a module a decision reaches that no card names |
| 7 | **Overconfident recommendation** | `SA_AR_04` | Seven cards recommend; `F3` deliberately does not. Attack the seven — especially `F2`, where one principle is recommended for three separately-evidenced items |
| 8 | **Incorrect independence claim** | `SA_AR_06` §1 | Find any sentence in the package that treats self-challenge as assurance |
| 9 | **Stale mainline reference** | `SA_AR_00` §6 | Every mainline figure is as-at-publication. **Re-measure; do not inherit** |
| 10 | **Evidence-count defect** | every count | **Validate each with a second command of a different shape.** The parent's `NOT TRAVERSABLE` count differs by instrument: whole-file grep returns 2, class-column returns 1 |
| 11 | **Constitution scope** | `SA_AR_05` | Both readings are built here. **Attack the one you find weaker — and note the recommendation is the expensive one, so check whether it is over-corrected** |
| 12 | **Negative-claim control** | anywhere a `0` appears | Every zero in this package should have a positive control. **The first run of Test A returned a false zero and only the control caught it** (`SA_AR_03` §3) |

---

## 6. THE CLEAN-PASS DEFINITION — `EC-07`, VERBATIM

A pass is **clean** only if it completes with **none** of:

- a new material **population**
- a new material **finding class**
- a new **gating unknown**
- a **reopened tolerance-zero** issue
- a new **Gate-changing contradiction**
- an **evidence-integrity failure**

**And: "Reviewer findings must themselves be independently verified before acceptance."**

> **Two consecutive clean passes are required, and `EC-07` may be harder here than it looks.** Every
> Phase SA round to date has produced a new material finding class, including this one (`AR-F-01`,
> `AR-F-02`). **If passes keep finding things, `EC-07` is not reached by running more of them** — Boss
> should say what happens in that case. Flagged at `SA_AR_05` §5 dissent 3.

---

## 7. REQUIRED OUTPUT SCHEMA

The reviewer publishes on its **own** branch, with its own immutable SHA:

```
IV_00_APPOINTMENT_AND_ELIGIBILITY.md     appointing authority; model; the per-pair eligibility test
IV_01_FROZEN_SURFACE_VERIFICATION.md     every SHA in §4 re-resolved; manifests re-verified
IV_02_INDEPENDENT_REPRODUCTION.md        counts/predicates re-derived with the reviewer's own commands
IV_03_FINDINGS.md                        one row per finding, each independently verified before acceptance
IV_04_CLEAN_PASS_DETERMINATION.md        each of the six EC-07 conditions, evidenced
IV_05_STATEMENT_OF_LIMITS.md             what the pass did NOT cover
```

**Findings row:** `id · class (1–12) · claim attacked · file:line · reviewer's own evidence · verdict
CONFIRMED | REFUTED | UNDETERMINED · materiality · verification of the finding itself`.

**Prohibited to the reviewer**, per `Q-BOSS-02` §5 and this programme's standing rules: editing owner
artefacts · discharging a veto · declaring `PASS` or gate closure · merging or releasing · widening
scope · Functional Design · schema/API design · code · **inferring `PASS` from silence or from the
existence of this prompt**.

---

## 8. IF BOSS RULES `FG-F-06 = READING B`

**This package is preserved as optional assurance evidence and is not represented as having been
required.** No artefact may then say Phase SA "needed" an independent pass, and `EC-07` may not be
cited as a Phase SA criterion. **The package remains useful; the obligation does not exist.**

## 9. Checkpoint

> ## `CP-SA-AR-60 — INDEPENDENT CHALLENGE PACKAGE READY`
> **Frozen surface at 8 named commits · 10 `Q-BOSS-02` controls reproduced at source · eligibility
> exclusion stated against this session's own model · 12 falsification classes each with an entry point
> and a named prior defect · `EC-07` clean-pass definition verbatim · output schema fixed · 0
> independence claimed.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
