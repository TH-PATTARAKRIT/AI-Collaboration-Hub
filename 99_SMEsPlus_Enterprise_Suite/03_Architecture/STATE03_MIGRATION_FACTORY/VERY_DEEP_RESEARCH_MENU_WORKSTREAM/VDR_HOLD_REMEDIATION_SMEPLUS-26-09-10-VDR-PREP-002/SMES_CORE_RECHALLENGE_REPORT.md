# SMES_CORE_RECHALLENGE_REPORT.md
# R3 — Clean Independent Re-Challenge: result and disposition

Session `[SMEPLUS-26-09-10-VDR-PREP-002]` · Layer: **LAYER 1 — CLEAN-ROOM.**

---

## 1. Round identity and freeze compliance — the control that failed last time

| Item | Value |
|------|-------|
| Round | **R3 — clean independent re-challenge** |
| **Frozen SHA** | **`1d6238a5574ae8a07e1c7679be024cdeacc84940`** |
| Working tree over the package at freeze | **clean — 0 modified, 0 untracked** |
| Reviewers | **2, independent**, each given the frozen SHA, the primary evidence roots and its own scratch space; each instructed to write its own instruments and not reuse the producer's |
| **Commits to the package path during the round** | **0** — `git log <SHA>..HEAD -- <package path>` returns empty |
| **Uncommitted changes during the round** | **0** |
| **Diff against the frozen SHA at round close** | **0** |
| **ROUND VALIDITY** | **CLEAN** |

**One reviewer ran this test independently and reported the same result**, noting correctly that while
`HEAD` equals the frozen SHA the range is empty by construction and the test acquires force only when
re-run after a later commit. **It has now been re-run after later commits; it still returns empty for
the round window.**

**The producer found ten of its own defects while the round was open — including two that falsify
published claims — and applied none of them until the round closed.** They were held in a file outside
the package path. That is the rule `GOV-01` broke, obeyed.

## 2. Volume

| Reviewer | Surface | Findings |
|---|---|---|
| **R3-A** | functional ownership, runtime reachability, the valuation claim, the newer dumps, inference strength | **16** |
| **R3-B** | prior-research reconciliation, delta research, coverage arithmetic, governance, integrity | **20** |
| **Producer self-review during the freeze window** | evidence base, census, identity object | **10** |
| | | **46** |

## 3. The two retractions

### R-1 — `RC-F-01` — the optional-function zero (**CRITICAL RETRACTION**)

Published: *"Zero occurrences across 5,193 lines… none of that surface exists in the prior research at
all."* **False.** The prior corpus calls the dimension a **capability switch** and devotes a function
and a menu study to it, rated configuration risk HIGH, with a named open gap.

**The measurement searched for this session's vocabulary, and its positive control was drawn from the
same wrong vocabulary — so the control could not fire, and its silence was read as confirmation.**

Withdrawn with it: `GAP-INV-19`, the `COMPLETE = 0` headline, and the stated delta on 29 `PARTIAL`
menus. **The decision not to re-research those menus is better justified than published, not worse.**

### R-2 — `RR-F-06` — the valuation chain (**CRITICAL RETRACTION**)

Published: *"it is not merely renamed — it is not being written"*, as the primary input to
`BOSS-DEC-01`. **False, in two independent ways.**

1. **The wrong object was identified as the replacement.** Per-movement valuation exists in series 19,
   relocated **onto the movement row**. Measured on a transacted series-19 deployment:
   **100% of 3,680 completed movements carry a value.** The columns were in the movement extract this
   package itself committed, and were not read.
2. **No state basis and no configuration control.** A movement is valued when it completes; the
   deployment the claim was measured on had **zero completed movements**. The accounting-link half is
   governed by **periodic vs real-time valuation** — every located series-19 deployment runs periodic,
   under which no movement creates an accounting entry in any generation.

**What survives, at `MATERIAL` weight:** an append-only ledger with its own row identity became
**mutable columns on the transaction row**, and the accounting linkage is **unobservable** in the
target generation. `CRITICAL-GAP-01` is re-stated at that weight.

## 4. Findings accepted, by class

| Class | Count | Examples |
|---|---:|---|
| **Retractions of published findings** | 2 | `RC-F-01`, `RR-F-06` |
| **Withdrawn columns / untested claims** | 3 | the ownership deployment flag (10 rows never tested); `DR-F-08`'s zero-field object; `GAP-INV-09B` |
| **Numeric corrections** | 11 | 32→29 mapped · 14→17 containers · 1→3 outdated · 63→59 and 755→677 verified · 6→5 identities · 0.72→0.92 · 11→10 and 18→17 groups · 12→11 cluster · 5→6 optional-dependent · 8→11 triggering objects |
| **Instrument corrections** | 7 | `CORR-F-36` … `CORR-F-43` |
| **Strengthened findings** | 4 | `DR-F-04` (identity object measured in data) · `RR-F-01` (live on a transacted deployment) · the deployment count 2→5 · three generations |
| **Confirmed sound** | **29** | see §6 |

## 5. Findings the producer corrected in the reviewers' favour, and against

**Adopted after verification against source in every case.** Two reviewer statements were themselves
refined:

| Reviewer claim | Producer verification |
|---|---|
| the delivery carrier object has 228 fields | **264 across 24 modules** on independent recount — the defect is larger than reported |
| a transacted deployment carries stock in the target generation | **confirmed**, and the producer had independently found the same artefact during the freeze window and held it |

## 6. What survived independent attack

Both reviewers wrote their own instruments and reproduced these:

- **The primary-owner derivation — 96 of 96 objects, 0 disagreements.** All 11 multi-declarer objects
  resolve to the obviously-correct definer. The alphabetical-ordering defect the producer recorded
  (`CORR-F-31`) was confirmed as exactly right.
- **Ownership class counts** 60 / 13 / 10 / 7 / 5 / 1 with 0 unresolved; the point-of-sale cluster's
  **34 of 149 modules owning exactly 1 object**, including the caveat that 13 of the 34 are
  localisation modules.
- **Deployment profile** — every module, menu, generation and cron figure, reproduced to the digit and
  in one case to the second.
- **Zero absent-while-installed**, extended by a reviewer from 186 to **1,557 menu and 345 action
  observations** — still zero. *(One counter-example was then found at field level — `RR-F-09`.)*
- **`RR-F-01`, `RR-F-02`, `RR-F-03`** — the suppression parameter's absence, the scheduler's and the
  valuation job's execution, all confirmed with positive controls.
- **The series-16 valuation figures** — 74,982 rows, 98.0%, 77.2% — exact.
- **`DR-F-09`**, attacked directly and held: a menu whose action targets **no data object at all**.
- **Package integrity** — manifest 55/55 with 0 mismatches, 0 broken table rows, 0 junk, and
  **0 vendor tokens in any Layer-1 file** under a token list wider than the producer's own.
- **Governance discipline** — no self-awarded PASS; no Boss-reserved question settled; all four Boss
  decisions carried as OPEN with evidence attached.

## 7. Disposition

| Class | Count |
|---|---:|
| `PASS` — challenged, no defect | 29 |
| `CONTRADICTION` — resolved by correction | 16 |
| `GAP` — accepted, recorded with an owner | 6 |
| `CRITICAL GAP` | 1 new (`CRITICAL-GAP-06`) |
| Retractions | 2 |

**Round disposition: `CLEAN` as to process — `HOLD` as to content.**

The freeze held, the reviewers were independent, their findings were verified before adoption, and
every correction was applied to the register text rather than to a revision log. **Two CRITICAL
findings did not survive, and the register that produced them could not have contradicted one of
them.** That is the round working.

## 8. What this round did not do

- **It did not re-challenge the corrected package.** These corrections have been verified by the
  producer against source. That is a screen, not a certification. **A further independent round is
  required and is not performed here.**
- **It did not re-certify the prior `VDR-PREP-001-CORR1` package**, which remains uncertified under
  `GOV-01`. `BOSS-DEC-13` remains open.
