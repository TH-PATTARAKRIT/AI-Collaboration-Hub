# SA_AR_10 — FINAL EVIDENCE INTEGRITY

## CP-SA-AR-95 — FINAL EVIDENCE INTEGRITY: CHECKS EXECUTED

**Content freeze is at this file.** The manifest is generated after it and after `SA_AR_11`, over every
file in the package directory, and is not regenerated afterwards. The publication commit is recorded in
the commit message and the resume state, never inside a hashed artefact, so no hash can go stale.

---

## 1. THE ELEVEN CHECKS MASTER PROMPT §11 REQUIRES

| # | Check | Result |
|---:|---|---|
| 1 | Every cited path resolves | **all resolve** — each read via `git show <ref>:<path>` on the branch that owns it |
| 2 | Every SHA is correct | **11 of 11** — §2, with a positive **and** a negative control |
| 3 | Every material count reproduces | **§3** — each re-derived on a second command shape |
| 4 | PR #63 merge state correctly represented | **`MERGED`**, merge commit `3f5d915a` is the head of `SMEsPlus`, re-measured at freeze |
| 5 | No unsupported compliance claim reintroduced | **0** — the package makes no compliance claim; it reports the retraction |
| 6 | No unsupported `PASS` / `CERTIFIED` wording | **0 affirmative verdicts** — §4, every hit listed in full |
| 7 | No vendor-copying tokens | **0** — one pattern hit, the English word *"product."*, refuted at `SA_AR_09` §5 |
| 8 | No hidden SMEs Core / PMO / document-owner material work | **0 / 0 / 0** — `SA_AR_08` |
| 9 | Decision counts equal the decision-family contents | **24 = 2+3+2+2+6+4+4+1** ✓, and `24 + 1 relocated + 5 acts = 30` ✓ |
| 10 | Veto counts equal the veto register | **6 rows, 6 distinct identifiers** ✓ |
| 11 | Category 3 count equals the Pre-Test qualification register | **0 = 0** ✓ |

---

## 2. CITED OBJECTS

Checked with a known-good (`3f5d915a` → `commit`) **and** a known-bad (`deadbeef` → correctly
unresolved), because the first run of this check put `git` outside the repository and reported all
eleven as broken (`AR-I-02`).

| Id | Type | What |
|---|---|---|
| `3f5d915a` | commit | **the PR #63 merge — current head of `SMEsPlus`** |
| `dafc0ff0` | commit | the retraction patch, head of PR #63 |
| `28de295d` | commit | mainline before the merge |
| `e6d2be32` | commit | this session's prompt, and this control branch's start point |
| `9d5bc2db` | commit | parent Final Boss Gate publication |
| `379fd073` · `60752e2d` · `604398c3` | commits | CORR5, CORR4, CORR3 |
| `2930723f` | commit | Boss decision `Q-BOSS-02` |
| `827b5906` | blob | **the corrected** file now authoritative on mainline |
| `111bfc41` | blob | the uncorrected claim — **retained in history, no longer served** |

**11 of 11 resolve. 0 unresolved.**

---

## 3. EVERY MATERIAL COUNT, AND THE SECOND SHAPE THAT CONFIRMS IT

| Figure | Result | First shape | Second shape |
|---|---:|---|---|
| Remote branches | **189** | `git branch -r` | `for-each-ref` with `grep -vx origin`, and `ls-remote --heads` — **three agree** |
| Compliance split | **182 / 7 / 0** | per-branch `git show \| grep RETRACTED` | sums to the branch population ✓ |
| Mainline delta | **2 commits, 1 file** | `git log 28de295d..` | `git diff --name-only` |
| Parent package | **13 files, 13/13 `OK`** | `shasum -c` | file count vs manifest lines |
| Surviving decisions | **24** | row-by-row decomposition | family membership sum |
| Population | **30** | decomposition | `24 + 1 + 5` |
| Identifier census | **23** | membership-row extraction | **deliberately ≠ 24** — `AR-C-01` |
| Vetoes | **6** | register rows | distinct identifiers |
| `SA15` classes | **2 / 15 / 1 = 18** | class column of 18 rows | summary table, **and** identifier enumeration showing `E2E-01`…`-18` each exactly once |
| Category 3 | **0** | obligation table | scenario tables |
| Test A coverage | **189 of 189 refs** | explicit counter | positive control fires on 3 ruling files |

---

## 4. VERDICT-WORD SWEEP, EVERY HIT LISTED

```
grep -n -w PASS|CERTIFIED|COMPLIANT|APPROVED  over SA_AR_00..SA_AR_09
```

**11 hits, all read in context, 0 affirmative verdicts:**

| Where | What it is |
|---|---|
| `SA_AR_01`:45 | **the sweep's own negation** — *"No affirmative `PASS` / `CERTIFIED` / `COMPLIANT` verdict is issued"* |
| `SA_AR_04`:157, 287, 290 | the **Boss-approved handoff contract §4** quoted — *"forbids `PASS / VERIFIED` where duplicate effects cannot be prevented"* |
| `SA_AR_05`:22, 61 | the constitution's **status field** (`BOSS APPROVED`) and **§4 quoted verbatim** (`EC-01 PASS`…) |
| `SA_AR_06`:53, 98, 135, 136 | `Q-BOSS-02` control 9 (**No Self-Pass**), the `EC-07` clean-pass *definition*, and two prohibitions |

**Affirmative-verdict headers:** four checkpoint headings contain `VERIFIED`. **All four are the master
prompt's own mandated checkpoint names, and each matches its file's actual result.** Every file carries
*Boss remains the sole Final Approver*; `SA_AR_00` carries *Checkpoint completion is NOT Boss approval*.
Refuted as a finding at `SA_AR_09` §5, with the distinction from the parent round's `CHF-09` stated.

---

## 5. WORDING VETOES — CLASSIFIED, NOT ZEROED

| Prohibition | Pattern | Hits | Classification |
|---|---|---:|---|
| `CF-V-01` | `(element 10\|HF-CTX-11).{0,80}(supplied\|available\|satisfied\|suppliable)` | 4 | 2 state the prohibition, 2 quote the pattern. **0 breaches** |
| `CF-V-02` | `CF-I-0[68].{0,120}reduc` | 2 | 1 states the prohibition, 1 quotes the pattern. **0 breaches** |

**A raw zero is not claimed and would be false.** The parent round claimed one and was wrong.

---

## 6. IDENTIFIER FAMILIES

**Owned by this session and contiguous:** `AR-F-01`, `AR-F-02` · `AR-C-01`…`AR-C-04` ·
`AR-I-01`, `AR-I-02`. **No gaps, no collision** with `CHF-*`/`FG-F-*` (the parent's), `CHA`/`CHB`/`CHC`/
`CHD` (CORR5's), or `POH-*`/`CF-*`/`RC-*`/`MTI-*` (peer families, declared not defined here).

---

## 7. HISTORICAL PRESERVATION

- The parent Final Boss Gate package at `9d5bc2db` is **untouched** — this package lives on a different
  branch and a different path, and nothing on the parent branch was written.
- The pre-merge blob `111bfc41` and the pre-merge tree `28de295d` both still resolve. **The retraction
  preserved history rather than rewriting it.**
- `SA15`/`SA17` now stand in **three generations** — historical, CORR5-controlled, final-controlled v2 —
  none overwritten.

---

## 8. WHAT INTEGRITY VERIFICATION CANNOT ESTABLISH

1. **That the conclusions are right.** `AR-F-01` — a wrong headline count carried through three rounds
   — **would have passed every check above** in each of those rounds. It hashes and tallies exactly like
   sound work.
2. **That the four repairs are sound.** No second party reviewed them.
3. **That this round is independent.** It is not, and `SA_AR_06` §2 records that this session's own
   model is ineligible to challenge it.
4. **That the mainline figures hold tomorrow.** They are true as at this freeze and must be
   re-measured, never inherited.

## 9. Checkpoint

> ## `CP-SA-AR-95 — FINAL EVIDENCE INTEGRITY: CHECKS EXECUTED (CONCLUSIONS NOT THEREBY VERIFIED)`
> **11 of 11 §11 checks · 11 of 11 objects resolve with positive and negative controls · every material
> count re-derived on a second shape · 0 vendor tokens · 0 affirmative verdicts across 11 listed hits ·
> 0 wording-veto breaches, classified not zeroed · 2 instrument failures published · 3 artefact
> generations preserved.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
