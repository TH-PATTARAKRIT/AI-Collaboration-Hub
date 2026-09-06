# P06_VERIFICATION_INSTRUMENT_CONTROL_REGISTER.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-INDEPENDENT-EXTERNAL-CORRECTION-VERIFICATION-006]` · prompt commit `51763d8`
**Track:** INDEPENDENT EXTERNAL VERIFICATION · branch `audit/p06-independent-verifier-2026-09-06-001`
**Frozen audit surface:** `1b018c104001eb4683166518a6161a8cd8ab5cee`
**Classification:** LAYER 2 — AUDIT QUARANTINE

> **Prompt §5 Stage C:** *"If the instrument cannot fail, it cannot establish absence/completeness."*
> Every instrument this verifier used for a material negative or completeness claim is listed with its positive control, its failure control, its declared denominator, its blind spot, and — where the result is load-bearing — an independent second method.

---

## 1. Instruments used by this verification

| # | Instrument | Denominator declared before use | Positive control | Failure control | Blind spot | Second method |
|---|---|---|---|---|---|---|
| `I-1` | `git ls-tree -r --name-only <frozen> -- <pkg>` filtered to `.md` | every blob under the package root at the frozen commit; **derived from the tree, not from any declared file list** | token `P06` → **87 of 87 files** | token `ZZQQ_NOT_PRESENT_XX` → **0 files** | cannot see files outside the package root, by design | file count cross-checked against `git diff --name-status` and against the extracted archive |
| `I-2` | `git grep -c/-o -E "REV-E-23, 2026-09-06" <frozen>` | marker **occurrences** across the 87 frozen files | the pattern returns non-zero in 19 files | — | **counts mentions, not repairs** — it matches prose naming the marker and the printed text of the counting command itself | `I-3` and `I-4` |
| `I-3` | per-file `git show <frozen>:<f> \| /usr/bin/grep -oE …` | same | same | same | same as `I-2`; uses a different code path and binary | agrees with `I-2` exactly |
| `I-4` | markers on **added diff lines** only, `git diff -U0 5212756 1b018c1` | markers *introduced by the round under audit* | the diff is non-empty (24 files) | — | cannot distinguish a repair from a prose mention added in the same round | agrees with `I-2`/`I-3` exactly |
| `I-5` | `git diff --numstat 5212756 1b018c1` — **deleted lines** per file | statements **replaced** by the round, entirely independent of any marker | 24 files changed, 21 modified / 3 added | a file with `-0` must be an insertion-only change, and every such file is verified to be one | counts line replacements, not semantic repairs; a two-line replacement of one claim would over-count | cross-checked against the per-occurrence classification |
| `I-6` | `git archive <frozen> \| tar -x` then per-file SHA-256 against `git show` | all 87 files | — | **the control fired: a first extraction with the wrong `--strip-components` produced 17 files and 87 hash mismatches, and was rejected** | none material — the check is exhaustive | — |

**`ICR-F-01` — Instrument `I-6` failed once and was caught by its own control.** A `--strip-components=6` extraction silently produced a 17-file tree. **Had the extraction been used without the hash check, every subsequent "not found" would have been measured over 17 of 87 files** and would have read as a clean result. The control was written before the extraction, not after it failed.

## 2. The package's own five documented tool defects — independently re-checked

The frozen package documents `VER-E-01` … `VER-E-05` in `G02_RECOVERY_2026_09_06/P06_VERIFICATION_TOOL_DEFECT_REGISTER.md`. Each was re-executed on this tree.

| ID | Package's description | Independent re-check |
|---|---|---|
| `VER-E-01` | `grep -c '^-[^-]'` on a diff misses markdown bullets, returning 27 for 30 | **REPRODUCED.** On `git diff -U0 18035d9 da98786`, `'^-[^-]'` returns **27**; `'^-'` minus the `--- a/` headers returns **30**. The defect is real and correctly described |
| `VER-E-02` | globs held in shell variables are not expanded by zsh, so a count silently covers one directory | **REPRODUCED as a property of the shell.** `G="a/*.md"; grep … $G` does not expand under zsh. Directly demonstrable |
| `VER-E-03` | a literal-marker grep matches its own printed documentation | **REPRODUCED, and it is live on this tree.** Of 26 `REV-E-23` occurrences, **2 are not repairs**: `G02_CLOSURE_2026_09_06/P06_AUTO_RESUME_STATE.md:172` is a printed `grep` command, and `G02_VERIFICATION_2026_09_06/P06_CORRECTION_PROPAGATION_MATRIX.md:96` is the sentence *"Executed: 21 repairs across 14 files"* — **the marker sits inside the very claim it falsifies** |
| `VER-E-04` | a bounded-repetition context regex over UTF-8 errors rather than returning results | **DOES NOT REPRODUCE.** Re-executed under `/usr/bin/grep` over all 87 frozen files, the documented regex returns its hits with **exit status 0**. *Amended after AAS-03 Expert 4 challenged this verifier's first, softer wording — adopted against myself.* The construction is not defective; the failure was specific to a grep implementation the register never names. **Per the programme's own negative-about-own-capability rule, `VER-E-04` as written should name the tool, its version and its output.** Routed as a P06 repair item |
| `VER-E-05` | an identifier (`P06-B-66`) cited while its owning register lacked the section | **REPRODUCED as having been repaired.** `40_` Appendix C exists on the frozen tree and defines `P06-B-66` and `P06-B-67`; the citation resolves |

**`ICR-F-02` — Four of the five reproduce. `VER-E-04` does not, and this verifier's first wording of that row was too generous to the package.** It was corrected only because an independent challenger re-executed the regex and got exit 0. *An auditor's charitable reading is itself an instrument, and it failed here in the package's favour.*

**`ICR-F-03` — And this verifier committed `VER-E-02` at its first attempt** (`IEV-I-01`). Of the five defects the package documents, **one was reproduced accidentally, by the auditor, while auditing it.**

## 3. Blind statement — what these instruments cannot establish

- **They cannot establish that the nine claim classes are the complete set of classes.** The class list is inherited from the audited package. A claim class the package never named is invisible to this audit as well.
- **They cannot establish semantic correctness of prose**, only presence, absence, count and agreement between locations.
- **They cannot establish that a "historical record" classification is right** where a statement is genuinely ambiguous between a record and a live claim; those are adjudicated by reading, and reading is not an instrument.
- **A grep for meaning is a proxy.** Widened patterns reduce, but do not eliminate, the paraphrase blind spot that has defeated three consecutive rounds.
