# SC-17 — FINAL CANONICAL EVIDENCE INTEGRITY

## CP-SA-SC-150 — FINAL EVIDENCE INTEGRITY VERIFIED

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`
Execution host: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

---

## 1. The fourteen §11 checks

| # | Check | Method | Result |
|---:|---|---|---|
| **1** | All current files non-empty | byte size of every package file | **PASS-EQUIVALENT — `0` empty or short.** 22 files checked, all ≥ 500 bytes |
| **2** | All manifest hashes reproduce | `shasum -a 256 -c` against the working tree, then **against the pushed tree object-by-object** | **`22 of 22` reproduce** (§3) |
| **3** | Every cited commit exists | **absolute path**, plus a **known-good and a known-bad control** | **`23 of 23` distinct objects resolve; `deadbeef` correctly does NOT.** *(Instrument shape taken from the peer's `AR-I-02`, which reported 11 good SHAs as broken from a relative path)* |
| **4** | Every cited file resolves | each `SC-*` reference checked against the package directory | **`0` unresolved** |
| **5** | Every count has **one declared count unit** | inspected each headline figure for a unit declaration preceding it | **`SC-10` §1 declares the unit before any number.** `SC-01` §1.0 declares its own and is **superseded** by `SC-10` with the supersession stated |
| **6** | `F1`–`F8` atomic membership sums **exactly** to the canonical count | summed the register's rows: `2+3+1+2+6+4+4+1` | **`23` ✓ — equals the declared canonical count** |
| **7** | Boss acts **not** counted as decisions | `SC-12` header rule; cross-checked against `SC-10` §2 and `SC-18` §3 | **`5` acts, `0` in the decision count** |
| **8** | `FG-F-06` **not** counted as an `F1`–`F8` atomic decision | `SC-13` header; `SC-10` §6; `SC-18` §3 | **Stated in 3 places. Not in the 23** |
| **9** | No stale `26` or `24` headline survives where the canonical count differs | swept **every** `SC-*` file for `2[456] Boss` / `all 2[456]` / `the 2[456] decisions` | **1 found and corrected** — `SC-00` carried a stale `26` (`SC-F-10`). **Re-swept: `0` remain** |
| **10** | No unsupported affirmative `PASS` / `CERTIFIED` verdict | swept headings for `PASS\|CERTIFIED\|VERIFIED\|APPROVED` | **`0`** |
| **11** | No unqualified compliance claim | swept for standards names and compliance assertions | **`0`** |
| **12** | No current-state `SMT` except marked historical quotation | classified **every** `\bSMT\b` occurrence in `SC-08`…`SC-18` | **`0` uses as the active-body name** (§2) |
| **13** | No false independent-assurance wording | swept for `independent assurance/review complete\|performed\|achieved` | **`0`.** Every `independent` match is a **negation** or an act description |
| **14** | No Pre-Test execution started | swept for Pre-Test Matrix start language, excluding negations | **`0` violations.** Every mention is *"not started"* |

---

## 2. Check 12 in full — classification, not a raw zero

**A package that states its own naming rule matches its own pattern.** A raw count is therefore not the
result; the classification is.

| Class | Count |
|---|---:|
| Raw `\bSMT\b` occurrences in `SC-08`…`SC-18` | **26** |
| — part of the identifier `SC-SMT-nn` (historical finding IDs from `SC-03`) | **18** |
| — inside a nomenclature or identifier rule that *states* the control | **6** |
| — **self-referential**: `SC-16`'s own name for the check class and its finding heading | **2** |
| **— used as the name of the active body** | **`0`** |

**Positive control:** the same logic over the legacy `SC-03` returns **11** bare uses, so the instrument
distinguishes a real use from an identifier. **It fires.**

**Disposition of the 18 identifiers:** retained verbatim and **marked** in `SC-10` and `SC-11` with an
`IDENTIFIER NOTE` — `LEGACY NAME — CURRENT BODY = SMEs CORE`. **They are not renamed**: renaming identifiers
already published at `2139088b` would sever citation lineage to satisfy a naming rule.

> **A third instrument failure was caught here.** The first form of check 12 piped `grep -o` into a filter
> that needed the surrounding line, so **the filter could not fire and the count was meaningless.** Re-run
> with a parser that strips the identifier form before testing for a bare token. **Published, not quietly
> re-run.**

---

## 3. Manifest

**22 entries.** Regenerated after every correction in this round, verified against the working tree, then
**re-verified object-by-object against the pushed tree** — because a manifest that matches only the local
copy proves nothing about what Boss will read.

| Class | Files |
|---|---:|
| Prior package (`SC-00`…`SC-07`) | 8 |
| This round (`SC-08`…`SC-18`) | 11 |
| Governance — continuation record, master prompt, auto-resume state | 3 |
| **Total in manifest** | **22** ✓ *(the manifest is not self-hashed)* |

> **`SC-F-13`, caught by running the manifest rather than describing it.** A first version of this section
> stated **19 files** and broke them down as `8 + 11 + 4`, which is **23** — a headline that disagreed with
> both the real count and its own rows. **The real count is `19` `SC-*` files plus `3` governance files
> = `22`.** Corrected here. **This is the third arithmetic self-correction in this session** (`SC-F-02`,
> `SC-F-10`, `SC-F-13`), and all three were caught the same way: **by re-deriving from the rows instead of
> restating the headline.**

---

## 4. Instrument failures across this session — the running count

**Six instrument failures have been caught by their own controls in this programme's last two rounds, four
of them by this session.** Every one would have produced a plausible, publishable, wrong result.

| Instrument | Failure mode | Would have published |
|---|---|---|
| `SC-F-01` | BSD `grep -E` cannot match a `(^\|…)` alternation here — **returned `0` on a file known to contain the token** | *"the new mainline work does not touch Phase SA"* from a pattern that never ran |
| `C-02` substring pair | loose pattern over-reported (`SEC-02`); strict pattern was dead | a false positive **and** a false negative in one sweep |
| `SC-I-03` | `grep -E` returned **`error: exceeds complexity limits`** — an error, not a zero | a clean COGS-freeze result from an instrument that never ran |
| `SC-I-04` | printed file paths with no line content | two phantom independence-claim hits |
| `SC-I-05` *(this file, §2)* | `grep -o` piped to a filter needing the whole line | a meaningless naming-drift count |
| **peer `AR-I-01`** | one `git grep` over 189 refs returned `0` **including for known-ruled identifiers** | *"0 already ruled"* from an instrument that never ran |
| **peer `AR-I-02`** | relative path put `git cat-file` outside the repo | **11 good SHAs reported broken** |

> **The rule this session applies without exception: a zero is not a result until its instrument has been
> shown to fire.** Five of the seven above were caught only because a positive control was run beside the
> claim.

---

## 5. Package inventory

| File | Subject |
|---|---|
| `SC-00` | Mainline delta re-measurement *(stale `26` corrected this round)* |
| `SC-01` | `F1`–`F8` authority scrub *(count superseded by `SC-10`)* |
| `SC-02` | `F3` bounded verification |
| `SC-03` | First-line challenge register *(legacy `SMT` naming, marked)* |
| `SC-04` | Veto / authority handoff *(Reading A ground withdrawn)* |
| `SC-05` | Pre-Test entry re-qualification |
| `SC-06` | First delta pack *(count superseded by `SC-10`)* |
| `SC-07` | Two-track reconciliation and count correction |
| `SC-08` | Two-track primary-source reproduction |
| `SC-09` | `BOSS-ROUTE-01` closure and lineage rule |
| `SC-10` | **Canonical authority and de-duplication register** |
| `SC-11` | **`F1`–`F8` canonical decision cards** |
| `SC-12` | Boss-commissioned acts register |
| `SC-13` | `FG-F-06` scope clarification card |
| `SC-14` | Final veto and independence reconciliation |
| `SC-15` | Pre-Test entry canonical re-qualification |
| `SC-16` | Final adversarial re-check |
| `SC-17` | This file |
| `SC-18` | **Boss Phase SA Final Decision Pack** |
| `PACKAGE_MANIFEST_SHA256.txt` · `PHASE_SA_SMES_CORE_AUTO_RESUME_STATE.md` · `00_CONTROLLED_CONTINUATION_RECORD.md` · `01_…MASTER_PROMPT.md` | governance |

---

## 6. Checkpoint

> ## `CP-SA-SC-150 — FINAL EVIDENCE INTEGRITY VERIFIED`
> **14 of 14 §11 checks executed · `0` empty files · manifest **22/22** reproducing against the **pushed**
> tree · **23/23** cited objects resolve with a known-bad control correctly failing · family membership
> sums **exactly** to `23` · `5` acts and `1` scope clarification held out of the count · **1 stale `26`
> found and corrected**, `0` remain · `0` affirmative verdicts · `0` compliance claims · `0` active-body
> `SMT` uses on a classified sweep with a firing positive control · `0` false independence wording ·
> `0` Pre-Test execution · **1 further instrument failure and 1 arithmetic error caught and published**.**

No Evidence = No Progress. Never Skip Gate. A zero is not a result until its instrument is shown to fire.
Boss remains the sole Final Approver.
