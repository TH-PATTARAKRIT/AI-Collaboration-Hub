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
| 65 `P06-B-*` | `grep -oh … \| sort -u \| wc -l` over three roots | max id = 65 and contiguous | **YES** |
| Claim-class residuals | grep by semantic assertion, multiple patterns per class | independent verifier pass, separate context | see the claim-class register |

## 4. Standing rule this round adds

> **A counting command must be stated with its population, and validated by a second command of a different shape.**
> A positive control is necessary and **not sufficient** — it proves the pattern can fire, not that it fires only on the population.
> **A grep for a literal token will match its own documentation.** Any register that prints its own measurement command has thereby changed the thing it measures.

Recorded as **`P06-B-66`** (INFORMATIONAL) in `40_` **Appendix C**, together with **`P06-B-67`** (HIGH — the population is a floor).

> **`VER-E-05`, self-caught.** When first written, this line cited `P06-B-66` as *"recorded in `40_` Appendix C"* — **and no Appendix C existed.** The identifier was an orphan for the length of one Stage-3 sweep, cited in exactly one file and defined in none. It was caught by the authoritative recount returning **66** distinct `P06-B-*` ids when the standing authority said 65 — *a count disagreeing with a register, again*, and the fifth instrument-level catch of this round. **Appendix C was then written.** The lesson is the package's own standing rule, committed by the round enforcing it: **an identifier is not raised until the register that owns it defines it.**
