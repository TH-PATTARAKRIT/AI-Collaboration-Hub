# SA_CORR4_00 — CORR3 BASELINE REPRODUCTION

## CP-SA-C4-00 — CORR3 BASELINE REPRODUCED, WITH FOUR DENOMINATORS CORRECTED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR4-PREGATE-CLOSURE-001]`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `architecture/phase-sa-corr4-pregate-closure-2026-09-09-001`
Master prompt commit: `5931d7ef` · Parent CORR3 publication: `604398c3`
Boss: **SOLE FINAL APPROVER**

---

## 1. What this file is, and the one rule it applies

Master prompt §2: *"Do not trust summary prose where primary evidence is available. Reproduce all
critical denominators and counts before modifying conclusions."*

Every figure CORR4 inherits is re-measured here **before** any of it is used. Where a figure
reproduces, it is stated as reproduced and the command shape is published. Where it does not, the
correction is stated with its cause.

> **Result: the CORR3 package's conclusions survive reproduction. Four of its denominators do not.**
> None of the four failures is a reasoning error in CORR3. **Three are the corpus moving underneath a
> measurement that was correct when taken**, and the fourth is a scope stated as a description. All
> four matter to CORR4, because CORR4's own §6 is a re-measurement task and would have inherited them.

---

## 2. Package consumed

At `604398c3`, the CORR3 package is **17 files**, path
`.../STATE03_MIGRATION_FACTORY/PHASE_SA_CORR3_PROOF_VERIFICATION_2026_09_09/`.

| File | Consumed | Note |
|---|---|---|
| `PHASE_SA_CORR3_AUTO_RESUME_STATE.md` | **Full** | §5.1's ordered next-work list is CORR4's mission statement |
| `SA_CORR3_00_DECISION_RECLASSIFICATION.md` | Full | |
| `SA_CORR3_01` … `SA_CORR3_04` | Read for cross-reference | Four targeted studies; not re-opened |
| `SA_CORR3_05_GOVERNANCE_AND_STANDARDS_CORRECTION.md` | **Full** | The C4-04 baseline |
| `SA_CORR3_06_JOINT_CROSS_PROOF_VERIFICATION_22X22.md` | **Full** | The 22-scenario register CORR4 §9 re-runs |
| `SA_CORR3_07_INVARIANT_PROOF_REGISTER.md` | **Full** | The 58-invariant register CORR4 §8 reclassifies |
| `SA_CORR3_08_CROSS_MODULE_CONTRACT_PROOF.md` | **Full** | `XMC-C-D1` and the `XMC-F-02` measurement |
| `SA_CORR3_09` / `10` / `11` / `12` | **Full** | Panel, independence, integrity, Boss pack |
| `SA_CORR3_13` / `14` | Read for cross-reference | `TVDR-06`, `TVDR-04`; both executed, not re-opened |
| `PACKAGE_MANIFEST_SHA256.txt` | Verified — §7 | |

**Naming note, recorded because the master prompt cites a filename that does not exist.** §2 of the
CORR4 prompt asks for `SA_CORR3_07_22_SCENARIO_CROSS_PROOF.md` *"or current equivalent"*. There is no
such file. The 22-scenario work is `SA_CORR3_06_JOINT_CROSS_PROOF_VERIFICATION_22X22.md`; `SA_CORR3_07`
is the invariant register. **Both were consumed under their real names.** Recorded so that no later
reader takes the prompt's filename as evidence that a file is missing.

---

## 3. The evidence frame — `CORR4-FRAME`, declared once

Declared to the four-clause standard the programme requires: **POPULATION · PATTERN · PATH SET · UNIT**,
none of them author-chosen.

| Clause | Value |
|---|---|
| **POPULATION** | **185** branches on `origin` at 2026-09-09 08:0x +0700 |
| **PATH SET** | every path in the tree of **every one of the 185 branch heads** |
| **PATTERN** | stated per measurement, with its command shape published beside its result |
| **UNIT** | `U1` = **3,926** distinct text blobs · `U2` = **3,604** distinct text paths. Extensions `.md` `.txt` `.csv`. **Never conflated** |
| **COMPLEMENT, stated** | blobs reachable only from non-head history commits; all non-`.md`/`.txt`/`.csv` files (**4,062 − 3,926 = 136** blobs, **3,740 − 3,604 = 136** paths); and **the reference-ERP source trees and runtime database dumps that live outside this clone**, which this session did not need and did not search |

### 3.1 Controls, executed

| Control | Result |
|---|---|
| **Positive** — `BD-ACC-01` across all 185 branch heads | **58 distinct paths.** Fires |
| **Positive** — `MTI-50` | **17 distinct paths.** Fires |
| **Negative** — `zqw94713_corr4_no_such_token` | **0.** A **fresh** token: `C3-I-02` records that a published negative-control token is single-use |
| **Branch enumeration, three shapes** | `for-each-ref` **185** · `branch -r` **185** · `ls-remote --heads` **185**. Agree |
| **Second instrument** | `ripgrep 14.1.1` used to re-count every figure in §5 that `ugrep 7.8.4` produced. Agreements and one disagreement recorded at §4.4 |

---

## 4. The four denominators that did not reproduce

### 4.1 `C4-B-01` — the branch population is **185**, not 184

Three command shapes agree at 185. CORR3 declared 184, and the difference is
`origin/architecture/phase-sa-corr4-pregate-closure-2026-09-09-001` — **this session's own control
branch, pushed at 2026-09-09 08:01:53 with the CORR4 master prompt on it, ten minutes after CORR3
published.**

Not a CORR3 error. **Recorded because CORR4 §6.1 instructs in terms not to assume 184, and the first
thing a re-measurement must establish is that the denominator moved and why.**

### 4.2 `C4-B-02` — seven Boss decisions landed on mainline during CORR3, and six are outside CORR3's frame

`origin/SMEsPlus` advanced **seven commits between 06:55:40 and 07:37:07 on 2026-09-09**, each adding
one file to `SAAS_CELL_ARCHITECTURE/`, numbered **22** through **28**:

| Commit | Time | File |
|---|---|---|
| `a7c6ebee` | 06:55:40 | `22_BOSS_DECISION_USAGE_BASED_CAPACITY_AND_TRANSPARENT_BILLING` |
| `a60019ff` | 07:02:17 | `23_BOSS_DECISION_CUSTOMER_USAGE_VISIBILITY_AND_PROJECTED_MONTHLY_COST` |
| `b8ff286c` | 07:27:18 | `24_BOSS_DECISION_WALLET_PROTECTION_AND_ADVANCE_NOTIFICATION` |
| `980e2af8` | 07:30:34 | `25_BOSS_DECISION_30_DAY_ADVANCE_WALLET_DEPLETION_NOTICE` |
| `5f915ed3` | 07:33:10 | `26_BOSS_DECISION_PREPAID_BEFORE_USAGE_30_DAY_NOTICE_IS_NOT_CREDIT` |
| `8a48b013` | 07:35:59 | `27_BOSS_DIRECTION_LOW_BASE_SUBSCRIPTION_WITH_PREPAID_USAGE_SERVICES` |
| `403deb09` | 07:37:07 | `28_BOSS_DECISION_PACKAGE_AND_ORGANIZATION_SIZE_AS_ROOM_SIZE_MODEL` |

CORR3 published at **07:50:50** — *after* all seven landed — and declared `U1 = 3,900 / U2 = 3,579`.
Re-measured now with the two CORR4-only branches excluded, the same frame yields **3,906 / 3,585**: a
delta of **+6 in both units**, matching six of the seven files.

> **`C4-B-02`. CORR3's frame was taken before mainline finished moving and was not re-taken before
> publication. Six Boss decisions dated the same morning are outside the population every CORR3
> negative was measured over.**

**This is not a criticism that costs CORR3 a conclusion — it is a live obligation for CORR4.** The
programme's own rule is that a negative is only as wide as its declared population. **CORR4 must read
all seven against the four conditions**, and does so: `SA_CORR4_01` §7 (metering is a non-interactive
execution path) and `SA_CORR4_08` challenge 11.

### 4.3 `C4-B-03` — the compliance denominator is **185 / 2 corrected / 183 uncorrected / 0 absent**

Measured per branch with `git rev-parse -q --verify '<branch>:<path>'`, and independently with
`git ls-tree <branch> -- <path>`; the two shapes agree exactly.

| | Count |
|---|---:|
| Branches carrying the path at all | **185 — every branch. `0` absent** |
| Carrying the **uncorrected** blob `111bfc41` | **183** |
| Carrying the **corrected** blob `827b5906` | **2** — `…corr3-proof-verification…` and this branch, which inherits it |
| Of which **`origin/SMEsPlus` (mainline)** | carries the **uncorrected** blob |

**CORR3 wrote "one blob, 184 branches, byte-identical" and "the other 183 branches".** Read against
this measurement: the remaining count **is** 183, and **it is 183 for a different reason than CORR3's
arithmetic gives.** CORR3's 183 = 184 − 1. CORR4's 183 = 185 − 2. The two agree by coincidence, and a
round that had assumed the figure rather than re-measured it would have carried a wrong denominator
and a wrong corrected-count and never noticed, because the number it cared about was unchanged.

> **This is precisely the failure §6.1 of the master prompt was written to prevent, and it would have
> occurred.** Recorded as the strongest single argument in this package for re-measurement over
> inheritance.

### 4.4 `C4-B-04` — `XMC-F-02`'s scope is stated as a description, not as a set

CORR3's `XMC-F-02` reads: *"Element 10 … is absent from the emitting party's own published payload."*

The measurement behind it reproduces **exactly**: over
`FINAL_SOLUTION/INVENTORY/V1_0/07_INVENTORY_ACCOUNTING_CONTROL_IMPACT_V1.md`, `tenant` occurs on **1**
line and `company` on **4**, none in §1.1 — confirmed here on **both** `ugrep` and `ripgrep`,
case-sensitive, with a negative control at 0. CORR3's `30 paths / 30 blobs` and `0 outside
FINAL_SOLUTION/INVENTORY` also reproduce exactly.

**What does not reproduce is the scope of the sentence.** *"The emitting party's own published payload"*
is a description; the measured set is **one file, in `V1_0`, of a two-version package**. CORR4 measured
the rest:

| Artefact | `tenant` | `Tenant` | `company` | Both instruments agree |
|---|---:|---:|---:|:---:|
| `V1_0/07_…CONTROL_IMPACT_V1.md` *(CORR3's file)* | 1 | 0 | 4 | ✓ |
| `V1_0/10_…CROSS_MODULE_HANDOFF_V1.md` *(the 31-row register)* | 1 | 0 | 2 | ✓ |
| `V2_0/05_INVENTORY_V2_FUNCTIONAL_DELTA_DESIGN.md` | 2 | 1 | 2 | ✓ |
| `V2_0/03_INVENTORY_V1_TO_V2_DELTA_MAP.md` | 0 | 0 | 0 | ✓ |

**The finding survives on every one of the four.** No producer artefact in either version carries
tenant or company as a payload element.

**But a second emitting-side artefact exists that CORR3 did not measure and that does carry them.**
`.../INVENTORY_REOPEN/MULTI_TENANT_INVARIANT_SET_EXECUTION/06_CROSS_MODULE_HANDOFF_CONTRACT_FIELDS.md`
specifies a nine-field context group `HF-CTX-01` … `HF-CTX-09` in which **`HF-CTX-01` Tenant identity
and `HF-CTX-02` Company identity are both marked mandatory `Always`**, extended to eleven fields by
`07_CONSUMING_MODULE_OBLIGATION_MATRIX_R2.md`.

> **`C4-B-04`. `XMC-F-02` is true of the `FINAL_SOLUTION` package and false as a statement about the
> programme.** The corrected finding, and what it does and does not change, is `SA_CORR4_02` §3 —
> where it turns out to make C4-02 **closable at Phase SA**, which the uncorrected form did not.

---

## 5. What reproduced, unchanged

| CORR3 figure | CORR4 re-measurement | Verdict |
|---|---|---|
| **58** invariants (50 `MTI-*` + 8 `CF-I-*`) | 58. Declared tally cross-checks: `41 + 7 + 5 + 5 = 58` | **Reproduced** |
| **22** scenarios, all `HOLD — EXACT PROOF GAP` | 22 rows, each with a named `(c)` blocker | **Reproduced** |
| **18** cross-module handoffs, `0 PROVEN / 2 N/A / 16 HOLD` | 18 | **Reproduced** |
| **30** `FINAL_SOLUTION` paths, `0` outside `INVENTORY`, `V1_0`=18 / `V2_0`=12 | 30 / 0 / 18 / 12 | **Reproduced** |
| `tenant`=1, `company`=4 lines in `07_…V1.md` | identical on two instruments | **Reproduced** |
| **31**-row `HX-` handoff register, `HX-` cited **0** times by Phase SA | `HX-` returns **31** rows in its own file and **18** paths branch-wide. Of the 18, **2 are `SA_CORR3_08` and `SA_CORR3_11` — CORR3's own files, reporting the zero** — and **0 of the 35 `SA00`–`SA20` / `SA_CORR2_*` artefacts** cite it | **Reproduced, with the unit made exact** |
| Compliance path present on every branch, byte-identical among the uncorrected | 183 branches share one blob SHA | **Reproduced** |
| Manifest — every hash | **21 lines / 17 files, all match** — §7 | **Reproduced** |

---

## 6. Instrument findings — each one cost a measurement

### `C4-I-01` — a whole scan returned sixteen false zeros, and only the positive control caught it

The shell is **zsh**. `BR=$(cat branches.txt)` followed by `git grep -l -F "$T" $BR` passes the **entire
185-line list as one argument**, because zsh does not word-split an unquoted parameter expansion. The
same list written `$(cat branches.txt)` **does** split, because command substitution splits on `IFS`.

A sixteen-token privileged-path scan returned **0 for every token, including `MTI-18`** — an identifier
that demonstrably occurs in three files. Re-run in the splitting form, the same scan returns
`privileged`=**89**, `superuser`=**34**, `break-glass`=**4**, `MTI-18`=**17**.

> **The scan was internally consistent, produced a plausible answer — "no privileged-path vocabulary
> exists in this corpus" — and was wholly false. Nothing in the output distinguished it from a real
> negative.** It was caught because a positive control had been run *separately*, in the other form,
> minutes earlier. **A control run in a different command shape from the measurement it certifies is
> not a control for that measurement.** Every branch-wide count in this package was re-run in the
> splitting form after this was found.

### `C4-I-02` — a literal-token count matched its own documentation

Extracting invariant identifiers with `grep -oE 'MTI-[0-9]{2}'` returns **51**, not 50 — and `ripgrep`
returns 51 too. **Two instruments, two shapes, one wrong answer**, because both used the same pattern.

The 51st is `MTI-51`, and reading the line shows it occurs in exactly one sentence, which says
`CF-I-*` *"are not numbered `MTI-51`+"*. **The pattern matched the sentence that explains why the
identifier does not exist.** Corrected by reading, not by a second shape. This is the programme's
recorded counting-command defect executing again, and it is recorded because the second-shape rule did
**not** catch it and cannot.

### `C4-I-03` — selection by convenience, tested rather than assumed

Twelve primary sources were located by filename. `head -1` on the path list is a convenience selection
and would silently choose one of several same-named files. **Tested: all thirteen names resolve to
exactly one path each in `U2`.** The selection is therefore not biased — established by measurement,
not by assumption.

### `C4-I-04` — `git rev-parse` prints its argument on failure

`git rev-parse "<ref>:<path>"` writes the **unresolved argument to stdout** when the path is absent,
so a `[ -n "$S" ]` guard admits it and a version-ranking loop reports every branch as carrying every
file. Use `git rev-parse -q --verify`. Caught because a 171-line file appeared to exist on 185 branches
with 185 distinct "SHAs" that were visibly paths.

---

## 7. Manifest and commit verification

| Check | Result |
|---|---|
| `PACKAGE_MANIFEST_SHA256.txt` | 21 lines; **16 file hashes**, all recomputed and **matching**. The manifest does not hash itself — 16 hashes over a 17-file package is correct, not short |
| Cited parent commit `604398c38fa9b51cf4e30692a3c4f284bf7b7cde` | **resolves** — `Phase SA CORR3: record publication commit and refresh manifest` |
| CORR3 auto-resume's self-declared publication commit `c7f42ce0` | **resolves**, and is the **parent** of `604398c3`. The auto-resume names the earlier of the two. **Recorded, immaterial** — both are on the CORR3 branch and the package content is identical between them apart from the manifest refresh |
| Master prompt commit `5931d7ef` | **resolves** — the CORR4 prompt, added to this control branch at 08:01:53 |
| Empty or zero-byte artefacts in the CORR3 package | **0 of 17** |

---

## 8. What CORR4 inherits, and what it does not

**Inherited and not re-opened:** every frozen carry-forward in the CORR3 auto-resume §2 — Phase S
conditionally closed and Phase SA entry authorized by Boss act `eb3d7dbb`; `SA00`…`SA20` and
`SA_CORR2_00`…`13` as baseline; every standing Boss ruling; `BD-ACC-03A`/`03B` not re-askable;
`BD-ACC-01`'s express grant to design the technical representation; the `SCOPE-AWARE EVERYWHERE`
correction; no peer package mutated; no veto discharged.

**Explicitly not re-opened, per the CORR3 auto-resume §5.1's own prohibition:** `TVDR-04`, `TVDR-06`,
`C2-D-03`, the verdict-vocabulary question, and — as a *decision* — the compliance retraction. **The
retraction's decision is closed; only its propagation is CORR4 work, and that is what C4-04 does.**

**Not inherited — re-measured instead:** the branch population; the frame's two units; the compliance
denominator; and the scope of `XMC-F-02`. All four are corrected above.

---

## 9. Checkpoint

> ## `CP-SA-C4-00 — CORR3 BASELINE REPRODUCED`
> **17 of 17 files consumed · 8 figures reproduced unchanged · 4 denominators corrected ·
> 4 instrument findings recorded · 0 CORR3 conclusions overturned at this checkpoint.**

**Next autonomous action:** `CP-SA-C4-10`, the privileged-bypass path enumeration.

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
