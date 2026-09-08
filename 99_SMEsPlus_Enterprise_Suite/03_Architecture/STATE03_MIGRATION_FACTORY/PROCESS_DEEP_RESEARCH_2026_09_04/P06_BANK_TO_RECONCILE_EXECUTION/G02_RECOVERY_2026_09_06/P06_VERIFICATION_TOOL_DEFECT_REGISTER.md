# P06_VERIFICATION_TOOL_DEFECT_REGISTER.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-INDEPENDENT-FROZEN-SURFACE-RECOVERY-005]`
**Session:** P06 — INDEPENDENT FROZEN-SURFACE CORRECTION RECOVERY (CP-P06R02)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Frozen SHA:** `52127569863455acc06b82a845ef64e106115900`

> Prompt §13 makes this register a precondition for any discharge recommendation: *"verification tools used for completeness are themselves validated."*
>
> **A completeness claim is only as good as the command that measured it.** Every defect below produced a *confident wrong number* — not an error message, not a crash. Each was caught by a **second measurement disagreeing**, never by the instrument noticing its own failure.

---

## 1. The register

| ID | Instrument | Defect | Wrong answer it produced | How it was caught | Direction of error |
|---|---|---|---|---|---|
| **`VER-E-01`** | `git diff -U0 … \| grep -c '^-[^-]'` — counting deleted lines in a diff | **Markdown bullet lines start with `- `, so their diff line begins `--`.** The pattern `^-[^-]` excludes exactly those | **27** deletions, when the true count was **30** | `git diff --numstat` disagreed | **Understated** — would have accused the package of applying fewer corrections than it claimed |
| **`VER-E-02`** | `G="a/*.md"; grep … $G` — globs held in shell variables | **zsh does not glob-expand the contents of a variable.** The command silently searched only the literal directory it could resolve | **65 / 68 / 20 / 70** for blockers / open questions / errors / files, when the true figures were **65 / 75 / 22 / 84** | the file count disagreed with `ls` | **Understated** — two of three subdirectories invisible |
| **`VER-E-03`** | `grep -ohE "REV-E-22, 2026-09-06" …` — counting correction markers | **A grep for a literal marker matches the printed form of the grep itself**, and matches prose that merely names the marker family. It counts *mentions*, not *repairs* | **47 occurrences in 24 files**, read as if it contradicted the published **40 in 20** | per-occurrence classification showed 7 were references, 3 of them the command's own text | **Overstated — and it accused the package.** The published figure was correct |
| **`VER-E-04`** | `grep -on '.\{0,45\}\*\*\*\*.\{0,25\}'` — extracting context around a rendering defect | The regex engine in use rejected the bounded-repetition-over-UTF-8 construction: *"exceeds complexity limits"* | **No output at all** — indistinguishable from "no defects found" had the exit code not been checked | the command errored visibly; **had it returned empty with status 0 it would have read as a clean result** | **Would have understated to zero** |

## 2. What the four have in common

**`VTD-F-01` — Not one of the four announced its own failure.** Three returned a plausible number and one returned nothing. **A silent wrong answer from a counting tool is indistinguishable from a correct one at the point of use** — which is the whole reason a completeness claim needs a second, differently-shaped measurement rather than a more careful reading of the first.

**`VTD-F-02` — The error direction is not stable, and that matters more than the error rate.** `VER-E-01` and `VER-E-02` understated. **`VER-E-03` overstated, and in doing so produced an accusation against the package that a first draft of this round's inventory published as a finding.** An audit instrument biased toward finding fault is not a safe instrument; it is a persuasive one. That draft is corrected in place at `FSI-F-02` and the wrong version is left on the record.

**`VTD-F-03` — Three of the four are the same underlying mistake: the pattern and the population disagree.**
- `VER-E-01`: the pattern could not match part of the population.
- `VER-E-02`: the population was never passed to the pattern.
- `VER-E-03`: the pattern matched things outside the population — **including its own documentation.**

**`VTD-F-04` — The controls that worked were all cross-measurements, never self-checks.** `numstat` vs `grep`; `ls` vs a glob; per-occurrence classification vs a total. **No positive control would have caught `VER-E-03`**, because the pattern *did* fire correctly on real repairs — it also fired on prose. A positive control proves a pattern can match; it says nothing about whether it matches only what you meant.

## 3. Validation applied to every count published this round

Per §13, each completeness figure carries the measurement that validates it.

| Figure | Primary measurement | Independent cross-measurement | Agree? |
|---|---|---|---|
| 30 round-5 markers / 15 files | `grep -ohE`/`-lE` over three roots | `git diff --numstat 18035d9 da98786` → 30 deletions, matching per file | **YES** |
| **40 repairs / 20 files** | 47 marker occurrences − 7 classified references | per-file recomputation after classification | **YES** |
| 84 files | `ls *.md <2 subdirs>/*.md \| wc -l` | per-file SHA-256 list length | **YES** |
| ~~65 `P06-B-*`~~ **SUPERSEDED — see `VTD-C-01` below** | ~~`grep -oh … \| sort -u \| wc -l` over three roots~~ | ~~max id = 65 and contiguous~~ | ~~**YES**~~ **WITHDRAWN 2026-09-08** |
| **67 `P06-B-*`** — current authority, see §3.1 | `grep -ohE 'P06-B-[0-9]+' … \| sort -u \| wc -l` | independent Python parse: 67 distinct, `1…67`, `set(range(1,68))` difference empty | **YES** |
| Claim-class residuals | grep by semantic assertion, multiple patterns per class | independent verifier pass, separate context | see the claim-class register |

## 3.1 `VTD-C-01` — the `P06-B-*` validation row, corrected and re-executed

**Raised by:** `RC-04` (`04_RC04_P06_SOURCE_CHALLENGE.md`, verifier ChatGPT GPT-5.6 Sol) against frozen surface `b5f5a211763568a4212d08954c835412f7728a0a`.
**Executed by:** P06 owner, 2026-09-08, one-prompt final closure.

**The defect.** §3 carried a live validation row certifying **65** distinct `P06-B-*` identifiers with `contiguous = YES`, while the *same file* raises `P06-B-66` and `P06-B-67` nine lines below it (§4, `VER-E-05`). **A validation row marked YES certified a figure the file it lives in already superseded.** The row is not withdrawn because 65 was wrongly measured — 65 was correct on the tree it was run against. It is withdrawn because it was left **current-tense** after the population moved, which is the one thing a validation control must never do.

### The four denominator clauses, declared

| Clause | Declaration |
|---|---|
| **POPULATION** | every distinct `P06-B-*` blocker identifier **raised anywhere in the P06 package**, closed or open — closure of a finding does not remove it from the population (`46_`:126) |
| **PATTERN** | ERE `P06-B-[0-9]+` / Python `\bP06-B-(\d+)\b`. **Requires the hyphen and at least one digit**, which excludes the adjacent `P06-B2R` family (54 occurrences) that a bare `P06-B` prefix would swallow |
| **PATH SET** | all `*.md` under `…/P06_BANK_TO_RECONCILE_EXECUTION/`, **recursive** — 89 files: root **70**, `G02_CLOSURE_2026_09_06` **12**, `G02_VERIFICATION_2026_09_06` **2**, `G02_RECOVERY_2026_09_06` **3**, `G02_OWNER_CORRECTION_2026_09_07` **2** |
| **UNIT** | **distinct identifier token**, not occurrence, not file, not open blocker |

**Path-set sensitivity, measured rather than assumed** — the figure does not depend on which of the three candidate path sets is used:

| Path set | Files | Distinct `P06-B-*` |
|---|---:|---:|
| root `*.md` only (the command printed at `13_`:94) | 70 | **67** |
| the three frozen roots declared in `P06_FROZEN_SURFACE_INVENTORY.md` §2 | 84 | **67** |
| recursive, whole package (this row's declaration) | 89 | **67** |

### Two independent instrument shapes

```
SHAPE A — shell, stream-oriented, set by text
  find . -name '*.md' -type f -print0 \
    | xargs -0 grep -ohE 'P06-B-[0-9]+' | sort -u | wc -l
  → 67          max id (numeric sort of the same stream) → 67

SHAPE B — Python, per-file, set of integers, contiguity by set difference
  ids = { int(m) for f in walk('*.md') for m in re.findall(r'\bP06-B-(\d+)\b', read(f)) }
  → len(ids) = 67 ; min = 1 ; max = 67
  → sorted(set(range(1, max+1)) - ids) = []      # missing: NONE
  → ids == set(range(1,68))                      # contiguous: True
```

The two shapes share no code path: A compares **strings** produced by a stream filter, B compares **integers** produced by a parser against a constructed range. They agree on the total, on the maximum, and on contiguity.

### §3.2 Controls — each able to fail

A positive control proves the pattern can fire. It cannot expose a **missing** identifier, so a deletion control is run as well.

| Control | Mutation | Expected | Observed | Verdict |
|---|---|---|---|---|
| **Negative** | none; search impossible id `P06-B-⟨9999⟩` (written with bracket digits here — see `VER-E-07`) | 0 | **0** | pattern does not fire on an absent id |
| **Positive / injection** | append a synthetic `P06-B-⟨68⟩` to one file in a scratch copy | 67 → 68, max 68 | **A: 68 · B: 68, max 68** | **a NEW identifier is detected by both shapes** |
| **Deletion** | rewrite every `P06-B-33` to `P06-X-33` in a scratch copy | 67 → 66, missing `[33]`, contiguous False | **A: 66 · B: 66, missing `[33]`, contiguous False** | **a MISSING identifier is detected, and contiguity flips** |
| **Family boundary** | `grep -ohE 'P06-B[^-]'` over the live tree | the `P06-B2R` family must be visible and excluded | **54 `P06-B2` occurrences, 0 counted** | the pattern is not over-wide |

**The deletion control is the one the superseded row never had.** The 65 row's cross-check was *"max id = 65 and contiguous"* — both computed from the same set the total came from. **A check derived from the measurement cannot contradict it**; that is why the row could stay YES while the population moved underneath it.

### §3.3 The enumeration, not the total

Per the prompt: the population is published, not only its cardinality.

```
P06-B-01 P06-B-02 P06-B-03 P06-B-04 P06-B-05 P06-B-06 P06-B-07 P06-B-08
P06-B-09 P06-B-10 P06-B-11 P06-B-12 P06-B-13 P06-B-14 P06-B-15 P06-B-16
P06-B-17 P06-B-18 P06-B-19 P06-B-20 P06-B-21 P06-B-22 P06-B-23 P06-B-24
P06-B-25 P06-B-26 P06-B-27 P06-B-28 P06-B-29 P06-B-30 P06-B-31 P06-B-32
P06-B-33 P06-B-34 P06-B-35 P06-B-36 P06-B-37 P06-B-38 P06-B-39 P06-B-40
P06-B-41 P06-B-42 P06-B-43 P06-B-44 P06-B-45 P06-B-46 P06-B-47 P06-B-48
P06-B-49 P06-B-50 P06-B-51 P06-B-52 P06-B-53 P06-B-54 P06-B-55 P06-B-56
P06-B-57 P06-B-58 P06-B-59 P06-B-60 P06-B-61 P06-B-62 P06-B-63 P06-B-64
P06-B-65 P06-B-66 P06-B-67
```
**67 identifiers · `P06-B-01`…`P06-B-67` · contiguous · no gaps · carried in 73 of the 89 files.**

### §3.4 `Q-P06-03` / `Q-P06-04` reconciliation — re-checked, not re-researched

Prompt item 7. Every companion figure from the same correction round re-executed at this commit:

| Figure | Command | Now | Prior published | Reconciles? |
|---|---|---|---|---|
| blockers | shapes A and B above | **67** | 67 | **yes** |
| vetoes | `grep -ohE 'AASP-VETO-[0-9]+' … \| sort -u` | `AASP-VETO-01…07` = **7** | 7 | **yes** |
| author errors | distinct `REV-E-*` = **23**, of which **21** carry a definition line | **21** | 21 | **yes** — unit is *author error*, not identifier |
| host archive | `…/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons_archive` present and readable at this run | **present** | population 961 dirs | **yes** — the evidence base is still at rest and reachable |
| open items | see `VER-E-06` below | **68 root-only / 75 package-scope** | **both published, neither scoped** | **NO — repaired below** |

`Q-P06-04`'s restatement of `FTB-F-07` is untouched. `P06-B-34` / `P06-B-35` remain **flagged, not disposed**. **No `Q-P06-03` / `Q-P06-04` research was reopened.**

---

## 3.5 `VER-E-06` — self-caught while validating `VTD-C-01`: two live totals for one concept, separated only by an undeclared path set

**The fifth instrument defect, and the first found by the correction round for a different figure.** While running the path-set sensitivity table above for `P06-B-*`, the same three path sets were run for the `P06-OQ-*` open-item family. They do **not** agree:

```
grep -ohE 'P06-OQ-[0-9]+' *.md                                   | sort -u | wc -l → 68   (root only, 70 files)
grep -ohE 'P06-OQ-[0-9]+' *.md G02_CLOSURE…/*.md G02_VERIFICATION…/*.md | sort -u | wc -l → 75   (three frozen roots, 84 files)
find . -name '*.md' -print0 | xargs -0 grep -ohE 'P06-OQ-[0-9]+'  | sort -u | wc -l → 75   (recursive, 89 files)
```

The seven identifiers that exist only outside the package root, enumerated:

| Identifier | Carried in |
|---|---|
| `P06-OQ-120` | `G02_CLOSURE_2026_09_06/P06_DOMAIN_PURITY_AND_BOUNDARY_REGISTER.md`, `…/P06_P10_MATERIAL_DELTA_REGISTER.md` |
| `P06-OQ-121` | `G02_CLOSURE_2026_09_06/P06_DOMAIN_PURITY_AND_BOUNDARY_REGISTER.md`, `…/P06_P10_MATERIAL_DELTA_REGISTER.md` |
| `P06-OQ-122` | `G02_CLOSURE_2026_09_06/P06_CANDIDATE_INPUT_PROCESS_OUTPUT_HANDOFF_PACK.md` |
| `P06-OQ-123` | `G02_CLOSURE_2026_09_06/P06_AUTO_RESUME_STATE.md`, `…/P06_CONTRADICTION_AND_REVISION_SUPPLEMENT.md`, `…/P06_PMO_TERMINAL_REVIEW.md`, `…/P06_SOURCE_LINK_AND_EVIDENCE_SUPPLEMENT.md` |
| `P06-OQ-125` | `G02_CLOSURE_2026_09_06/P06_AUTO_RESUME_STATE.md`, `…/P06_PMO_TERMINAL_REVIEW.md`, `…/P06_SOURCE_LINK_AND_EVIDENCE_SUPPLEMENT.md` |
| `P06-OQ-126` | `G02_CLOSURE_2026_09_06/P06_AAS_PLUS_CONSOLIDATION.md`, `…/P06_PMO_TERMINAL_REVIEW.md` |
| `P06-OQ-127` | `G02_CLOSURE_2026_09_06/P06_AAS_PLUS_CONSOLIDATION.md`, `…/P06_PMO_TERMINAL_REVIEW.md` |

**Both figures were live, current-tense, in the same package, at the same commit:**
- `13_P06_EVIDENCE_MANIFEST.md`:95 — *"Open-item population … **68**"*;
- `18_P06_CORE_RECON_HANDOFF_PACK.md`:214 — *"**67 blockers and 75 open items** at the current frozen surface"*.

**Neither is a miscount. Both are correct for the path set they were run over, and neither stated one.** `RC-04` independently reproduced 68 and did not reach 75, because it inherited the narrower published command — **an undeclared path set propagates to the verifier as silently as it propagates to the reader.**

**This is the same defect class as `VTD-C-01`,** so it is repaired in the same loop rather than queued: *a count carrier that does not state its path set*. **Unlike `VTD-C-01` it is not a stale figure — it is two simultaneously-true figures with no way for a reader to tell them apart.**

**Repair applied** (values unchanged; the scope is what was missing):
- `13_`:95 now reads **68 — root-only path set, 70 files**, with the package-scope figure named beside it;
- `18_`:214 now reads **75 — three frozen roots, 84 files**, with the root-only figure named beside it;
- `P06-OQ-*` is **not contiguous** (`max id = 128`, 75 distinct) and is therefore **not** subject to the contiguity control that governs `P06-B-*`. Stating that prevents the next reader from importing a check that does not apply.

> **`VTD-F-05`, the rule this adds.** A count that is stable across path sets and a count that is not are **indistinguishable in a published total.** `P06-B-*` returns 67 under all three path sets; `P06-OQ-*` returns 68 or 75 depending on one. **Only running the sensitivity table tells you which kind of number you are holding** — and it must be run for every family, not for the one currently under challenge.

---

## 3.6 `VER-E-07` — the register inflated the population it was correcting, in the act of correcting it

**Self-caught, 2026-09-08, between writing §3.2 and re-running §3.1.**

The control table in §3.2 was first written with the synthetic identifiers spelled in full — the injected one and the impossible one. Re-running SHAPE A over the package immediately afterwards returned:

```
find . -name '*.md' -print0 | xargs -0 grep -ohE 'P06-B-[0-9]+' | sort -u | wc -l
  → 69                       # not 67
  → tail of numeric sort: 67, 68, 9999
```

**The two highest "identifiers" in the P06 package were the two that this register had just invented to test the instrument.** The count corrected from 65 to 67 by this very section was, for the length of one edit, 69 — **and both new members were text written by the correction.**

This is **`VER-E-03` recurring inside the round that documents `VER-E-03`.** That entry's rule — *"a grep for a literal token matches its own documentation"* — was written, published, restated as a standing rule in §4, and then **violated by the next section of the same file.** It was caught only because §3.1's re-run was executed after the edit rather than before it.

**Repair:** every synthetic identifier in §3.2 is now written with bracketed digits, which the declared pattern cannot match because it requires a digit immediately after the final hyphen. The real in-range identifiers (`P06-B-33`, `P06-B-66`, `P06-B-67`) are left spelled in full — they are members of the population and belong in it.

> **`VTD-F-06`.** A control that mutates a scratch copy still contaminates the live population **through the prose that describes it.** The mutation was correctly isolated to a temporary tree; **the description was not.** An instrument whose population is *text* has no safe way to name a token it wants to exclude — it can only refuse to spell it.
>
> **Knowing the rule is not applying it.** The gap between §4 and §3.2 in this file is nine lines of prose and one working session.

---

## 4. Standing rule this round adds

> **A counting command must be stated with its population, and validated by a second command of a different shape.**
> A positive control is necessary and **not sufficient** — it proves the pattern can fire, not that it fires only on the population.
> **A grep for a literal token will match its own documentation.** Any register that prints its own measurement command has thereby changed the thing it measures.

Recorded as **`P06-B-66`** (INFORMATIONAL) in `40_` **Appendix C**, together with **`P06-B-67`** (HIGH — the population is a floor).

> **`VER-E-05`, self-caught.** When first written, this line cited `P06-B-66` as *"recorded in `40_` Appendix C"* — **and no Appendix C existed.** The identifier was an orphan for the length of one Stage-3 sweep, cited in exactly one file and defined in none. It was caught by the authoritative recount returning **66** distinct `P06-B-*` ids when the standing authority said 65 — *a count disagreeing with a register, again*, and the fifth instrument-level catch of this round. **Appendix C was then written.** The lesson is the package's own standing rule, committed by the round enforcing it: **an identifier is not raised until the register that owns it defines it.**
