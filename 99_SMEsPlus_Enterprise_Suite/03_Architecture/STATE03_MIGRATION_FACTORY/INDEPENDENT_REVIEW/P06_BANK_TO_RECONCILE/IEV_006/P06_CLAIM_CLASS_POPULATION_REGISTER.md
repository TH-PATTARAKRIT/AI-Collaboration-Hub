# P06_CLAIM_CLASS_POPULATION_REGISTER.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-INDEPENDENT-EXTERNAL-CORRECTION-VERIFICATION-006]` · prompt commit `51763d8`
**Track:** INDEPENDENT EXTERNAL VERIFICATION · branch `audit/p06-independent-verifier-2026-09-06-001`
**Frozen audit surface:** `1b018c104001eb4683166518a6161a8cd8ab5cee`
**Classification:** LAYER 2 — AUDIT QUARANTINE

> **Prompt §5 Stage A: *"Do not use the author's tally as the denominator."*** Every population below is derived from the frozen tree.

---

## 1. Frozen surface, proved

| Step | Result |
|---|---|
| `git cat-file -t 1b018c1` | `commit` |
| Subject | *"post-publication record — published SHA d1e66f5, authoritative remote verified"* |
| Tree SHA | `04f90a801eb24f51f3e6738ca50dba310ecd95b7` |
| `.md` files under the package root, **enumerated from the tree** | **87** — root **70** · `G02_CLOSURE_2026_09_06` **12** · `G02_VERIFICATION_2026_09_06` **2** · `G02_RECOVERY_2026_09_06` **3** |
| Extraction integrity | **87 of 87 byte-identical** to `git show` per file. Digest `09c54632d5ebfbff687f8bcb29562169c7bf194fc9d8faed31735df8c19eadff` |

## 2. The repair population — three independent methods

| Method | Occurrences | Files |
|---|---|---|
| `M1` `git grep -o/-l` against the frozen commit | **26** | **19** |
| `M2` per-file `git show \| /usr/bin/grep -oE` (different binary, different code path) | **26** | **19** |
| `M3` markers on **added diff lines** only, `git diff -U0 5212756 1b018c1` | **26** | **19** |
| `M4` **marker-independent**: deleted lines per file, `git diff --numstat 5212756 1b018c1` | **24 replaced statements** | 21 modified + 3 added files |

**Classification of the 26 occurrences** — per the package's own documented `VER-E-03`, a literal-marker grep also matches prose and printed commands:

| Kind | Count | Evidence |
|---|---|---|
| **REPAIR** — attached to a changed statement | **24** | agrees with `M4`'s 24 replaced statements |
| **REFERENCE** — not a repair | **2** | `G02_CLOSURE_2026_09_06/P06_AUTO_RESUME_STATE.md:172` is a printed `grep` command; `G02_VERIFICATION_2026_09_06/P06_CORRECTION_PROPAGATION_MATRIX.md:96` is **the sentence stating the count itself** |

**`CCP-F-01` — The corrected surface is 24 changed statements, and the package's own decomposition reconciles to it exactly.**
`G02_VERIFICATION_2026_09_06/P06_CORRECTION_PROPAGATION_MATRIX.md:96` reads: *"**Executed: 21 repairs across 14 files** … **plus 3 supersession/snapshot markers**."* **21 + 3 = 24.** Independent measurement: **24.** **The package's arithmetic is correct.**

**`CCP-F-02` — But five of the six statements of that figure omit the second component, and one of them is the successor's instruction.**

| Location | Wording | Complete? |
|---|---|---|
| `G02_VERIFICATION.../P06_CORRECTION_PROPAGATION_MATRIX.md:96` | 21 repairs / 14 files **plus 3 supersession/snapshot markers** | **YES** |
| `G02_CLOSURE.../P06_AUTO_RESUME_STATE.md:157` | *"21 repairs across 14 files"* | no |
| **`G02_CLOSURE.../P06_AUTO_RESUME_STATE.md:170` — NEXT EXACT ACTION** | *"over the **21 `REV-E-23` repairs across 14 files**"* | **no — and this is the instruction to the next verifier** |
| `G02_CLOSURE.../P06_CHECKPOINT_REGISTER.md:108` | *"21 repairs / 14 files"* | no |
| `G02_CLOSURE.../P06_EVIDENCE_MANIFEST_G02.md:154` | *"REV-E-23 repairs -> 21 in 14 files"* | no |
| `G02_RECOVERY.../P06_INDEPENDENT_CLAIM_CLASS_VERIFICATION_REGISTER.md:94` | *"the 21 … repairs. Scope: the 14 files changed this round"* | no |

**A successor obeying the NEXT EXACT ACTION verifies 21 of 24 changed statements and never opens `21_`, `41_` or `P06_SOURCE_LINK_AND_EVIDENCE_SUPPLEMENT.md`.** The three omitted are precisely the round's final bounded loop, applied *after* the census was taken. **This is the stale-count defect (`REV-E-08`) in its fourth recurrence — and this time it is embedded in the handoff of the audit itself.**

**`CCP-F-03` — The successor's published command is also wrong, independently.**
`P06_AUTO_RESUME_STATE.md:172` prints:
```
grep -rnE "REV-E-23, 2026-09-06" *.md G02_CLOSURE_2026_09_06/*.md G02_RECOVERY_2026_09_06/*.md
```
Executed verbatim on the frozen tree it returns **25 occurrences / 18 files**, not 26 / 19. It **includes `G02_RECOVERY_2026_09_06/`, which contains zero matches, and omits `G02_VERIFICATION_2026_09_06/`, which contains one.** The command searches an empty directory and skips a populated one. *This is the excluded-directory defect the same package documents; the round fixed it in its measurements and left it in its instruction.*

## 3. Claim-class raw populations, widened patterns

**DENOMINATOR: all 87 frozen files, all four directories, every sweep.**
**POSITIVE CONTROL: token `P06` → 2,422 occurrences across 87 of 87 files. NEGATIVE CONTROL: impossible token → 0 files.**

| # | Claim class | Widened pattern | Hits | Files |
|---|---|---|---|---|
| C1 | `X-08` / `D-08` / `PD-08` closure | `X-08\|D-08\|PD-08` | 81 | 21 |
| C2 | peer publication status | `unpublished\|not published\|NOT PUBLISHED\|absent from origin\|P01 absent\|cannot be read` | 89 | 25 |
| C3 | evidence base filtered vs relocated | `filtered[ -](distribution\|build\|tree)` | 58 | 21 |
| C4 | `is_matched` branches/sites | `top-level branch\|assignment site` | 33 | 10 |
| C5 | settlement-path ordinal | `(eighth\|8th\|fifth\|5th) (settlement\|ingestion)?[ -]?(door\|path)` | 48 | 16 |
| C6 | `res.config.settings` ACL breadth | `broad default ACL\|broad ACL` | 9 | 6 |
| C7 | `ir.sequence` re-issuable | `re-issuable\|reissuable` | 9 | 6 |
| C8 | generation gap | `only (available )?deployment evidence` | 16 | 8 |
| C9 | blocker population totals | `[0-9]+ blockers\|[Bb]locker population` | 34 | 14 |

**These are raw hits, not current statements.** Classification is in `P06_INDEPENDENT_CORRECTION_VERIFICATION_REGISTER.md`.

## 4. `IEV-I-01` — this verifier's own instrument failed, and the control caught it

The nine sweeps above were first run with the glob list held in a shell variable:
```
ALL="*.md G02_CLOSURE_2026_09_06/*.md …"
/usr/bin/grep -rhoE "$pattern" $ALL
```
**zsh does not expand globs held in a variable.** The **positive control returned 0 occurrences of `P06`** — impossible on a 87-file P06 package — and **all nine claim classes returned 0 hits.**

**Without the positive control this audit would have reported nine clean classes on nine zeros produced by its own broken instrument, and recommended discharging `AASP-VETO-07`.**

**This is `VER-E-02` — a defect the audited package documents — committed by the auditor auditing it.** Recorded, not concealed. Re-run with literal globs, the controls fire correctly and the populations above are the corrected figures.

## 5. Blind statement

- **The nine classes are inherited from the audited package.** A claim class P06 never named is invisible to this audit too. The population of *classes* is not independently established, and cannot be by this method.
- **Widened patterns reduce the paraphrase blind spot; they do not close it.** Three consecutive P06 rounds were each defeated by a variant their patterns could not match, and this audit found its own instrument defeated on the first attempt.
