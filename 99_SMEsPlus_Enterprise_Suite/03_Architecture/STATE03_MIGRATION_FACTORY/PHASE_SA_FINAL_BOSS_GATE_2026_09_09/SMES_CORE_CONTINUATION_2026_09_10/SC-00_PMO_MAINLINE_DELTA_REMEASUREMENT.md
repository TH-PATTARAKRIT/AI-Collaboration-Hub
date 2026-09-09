# SC-00 — PMO MAINLINE DELTA RE-MEASUREMENT

## CP-SA-SC-00 — MAINLINE DELTA RE-MEASURED

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Continuation head at entry: `33537d36c7b962fd3674860001568f84f8a1aa38`
Parent Final Boss Gate package: `9d5bc2db4a6b62c4cd01a04388b5bad23e6f5306`
Boss: **SOLE FINAL APPROVER**

---

## 1. Result, stated first

> # `PMO MAINLINE ACT COMPLETE — CATEGORY 3 GOVERNANCE GAP CLOSED`

**Re-measured, not inherited.** PR #63 is `MERGED`. The merge commit named in the continuation prompt
resolves and is an ancestor of the current default branch. The default branch now serves the **corrected**
blob, and an unauthenticated public fetch returns it by **hash identity**, not by inference.

**The parent pack's own conversion condition is met.** `SA_FINAL_04` §6 stated: *"The moment PR #63
merges, Category 3 falls to `0` and this file's result converts with no other change."* That conditional
is now discharged on evidence, and §5 of this file tests the *"with no other change"* half rather than
assuming it.

**This closes the one act. It does not open the Phase SA gate**, which turns on the 26 Boss decisions,
the 6 vetoes and the independence question — all re-worked at `SC-01`…`SC-05` of this continuation.

---

## 2. The six things master prompt §3 requires, answered exactly

| # | Required statement | **Measured result** |
|---:|---|---|
| **1** | Current default-branch SHA | **`a20db7a36e39b12d0b14e94e1667780424cdfa43`** — `SMEsPlus`, confirmed the default by `gh api repos/… --jq .default_branch` |
| **2** | PR #63 state and merge SHA | **`MERGED`** · merge commit **`3f5d915a2dc14f8121c4292e863f08b743992101`** · `merged_at 2026-09-09T15:44:43Z` · merged by `scglegacy` · head `dafc0ff057a0b0f222234059034598cec1a7a847` · base `SMEsPlus` · 1 file, `+22 / −6` |
| **3** | Is the prior unqualified compliance claim still live? | **NO.** Default-branch blob at the path = **`827b59068d8fdafa4d72acbcb42913b3bbdb3b97`** — the corrected blob. Unauthenticated `curl` returns **`HTTP 200`, 7,724 bytes**, and the returned body **hashes to `827b5906…`**. Heading line 215 reads *"Standards Alignment — design targets, not compliance or certification claims"*; the string *"Standards Compliance"* survives at **exactly one** line (218) and **inside the retraction note**, which is the corrected text's intended behaviour |
| **4** | Is the former Category-3 PMO mainline blocker CLOSED, OPEN or CHANGED? | **`CLOSED`.** The `SA_FINAL_00` §6 completion test is reproduced verbatim and both of its expectations are met. **`CATEGORY 3 MATERIAL GAP COUNT: 1 → 0`** |
| **5** | Evidence commands / paths | §3 below — every command and its output |
| **6** | New material delta introduced by the merge? | **By the merge itself: none** beyond the intended one-file correction. **After the merge: 17 commits / 16 files**, all `ERPPLUS-152` `CORE_RESOURCE_GOVERNANCE` `G1`–`G3`, with **0 bearing** on any Phase SA decision, veto or constitution identifier — measured with an instrument proven live (§5) |

---

## 3. Evidence — commands and outputs

Path under test throughout: `99_SMEsPlus_Enterprise_Suite/16_Learning_Analysis/01_SYSTEM_OVERVIEW.md`
Corrected blob `827b59068d8fdafa4d72acbcb42913b3bbdb3b97` · uncorrected blob `111bfc41f6e6253ab69a522c35edfc034fd06e1d`

| # | Command | Output |
|---:|---|---|
| `E1` | `git ls-remote origin refs/heads/SMEsPlus` | `a20db7a36e39b12d0b14e94e1667780424cdfa43` |
| `E2` | `gh api repos/TH-PATTARAKRIT/AI-Collaboration-Hub --jq '.default_branch'` | `SMEsPlus` |
| `E3` | `gh pr view 63 --json state,mergedAt,mergedBy,mergeCommit,baseRefName,headRefOid,files` | `state: MERGED` · `mergedAt: 2026-09-09T15:44:43Z` · `mergeCommit.oid: 3f5d915a…` · `baseRefName: SMEsPlus` · 1 file `+22/−6` |
| `E4` | `gh api repos/…/pulls/63 --jq '{state,merged,merge_commit_sha,changed_files}'` — **second command shape** | `state: closed` · `merged: true` · `merge_commit_sha: 3f5d915a…` · `changed_files: 1` — **agrees with `E3`** |
| `E5` | `git rev-parse origin/SMEsPlus` | `a20db7a3…` |
| **`E6`** | `git rev-parse -q --verify 'origin/SMEsPlus:…/01_SYSTEM_OVERVIEW.md'` | **`827b59068d8fdafa4d72acbcb42913b3bbdb3b97`** — matches the expected corrected blob |
| `E7` | `git merge-base --is-ancestor 3f5d915a… origin/SMEsPlus` | **exit 0** — the merge commit is on the default branch |
| `E8` | `git rev-list --count 3f5d915a…..origin/SMEsPlus` | **17** commits after the merge |
| **`E9`** | `curl -s …/SMEsPlus/…/01_SYSTEM_OVERVIEW.md?cb=<ts>` then `git hash-object` | **`HTTP 200`**, 7,724 bytes, body hashes to **`827b5906…`** · `grep -c 'Standards Alignment'` = **1** · `grep -n 'Standards Compliance'` = **line 218 only**, inside the retraction note |
| `E10`/`E11` | `git diff --name-only 3f5d915a…..origin/SMEsPlus` | **16 unique paths**, all `…/CORE_RESOURCE_GOVERNANCE/`; **0** matching `PHASE_SA|16_Learning_Analysis|ACCOUNT` |
| `E12` | per-branch `git rev-parse -q --verify "$b:$P"` over every remote head | **190 / 8 corrected / 182 uncorrected / 0 absent / 0 other**; sum `190` ✓ |
| `E13` | per-branch `git ls-tree "$b" -- "$P"` — **second command shape** | 190 rows: **182 + 8** — **agrees with `E12`** |
| `E14` | which heads carry the corrected blob | `origin/SMEsPlus` · the four `phase-sa-*` correction branches · `phase-sa-final-boss-gate-readiness` · **this continuation branch** · `governance/compliance-retraction-mainline` = **8** |
| `E15b` | validated identifier sweep over the 16 new mainline files (§5) | **0 hits** |
| `E17b` | same pattern over the parent pack — **positive control** | **14 files, 36 of 36 identifiers fire** |
| `E19`/`E20` | `ERPPLUS-152` gate progress | latest published gate `G3` → *"READY FOR G4"*; **`G6` Metering/Wallet Gate not reached** |

### 3.1 The population split, and why the constant is not a stall

| Measure | `SA_FINAL_00` §3 (parent) | **This session** | Movement |
|---|---:|---:|---|
| Remote-branch population | 188 | **190** | +2 new heads |
| Carrying the **corrected** blob | 5 | **8** | +3 |
| Carrying the **uncorrected** blob | 183 | **182** | **−1** |
| Absent | 0 | **0** | — |

`182 + 8 = 190` ✓ on **two independent command shapes**. The parent predicted exactly this: *"On
completion the uncorrected count falls **183 → 182**."* **It did.** The `−1` is `origin/SMEsPlus` itself
crossing from the uncorrected class to the corrected one; the `+3` corrected is that crossing plus the two
new heads. The remaining **182** are the historical execution branches CORR4 classified as audit lineage to
be preserved (`C4-04-F-07`) — unchanged, and correctly so.

---

## 4. What the merge did *not* change

Stated because a closure is the moment a reader is most likely to over-read it.

| | |
|---|---|
| Phase SA Boss decisions | **26, unchanged** — the merge rules none of them |
| Vetoes in force | **6, unchanged; 0 discharged** — a PMO act cannot discharge an AAS+ veto |
| Independence status | **unchanged** — no structurally independent Phase SA review has been appointed or performed |
| `SMEPLUS-DR-EXIT-8C-001` scope question (`FG-F-06`) | **unchanged and still undetermined** |
| Scenarios verified | **0 of 22** — unchanged and unchangeable at Phase SA |
| `NOT TRAVERSABLE` E2E scenarios | **1** (`E2E-04`), unchanged |
| `GAP-KC-01` — folder-level disposition of `16_Learning_Analysis` | **still open, still PMO-owned.** Correcting the claim does not dispose of the folder, and this file does not treat it as closed |
| The ~935 unread paths of CORR4's 1,061-path broad compliance population | **unchanged** — the one-file class still rests on instruments B, C and D, not on the broad sweep |

---

## 5. Testing the *"with no other change"* half — the 17 post-merge commits

The parent's conversion clause asserts nothing else changed. **An assertion about a live branch is a claim,
not a fact**, so it was measured rather than accepted.

**Population:** the 17 commits between `3f5d915a…` and `a20db7a3…`, touching **16 unique paths**, all under
`…/STATE03_MIGRATION_FACTORY/CORE_RESOURCE_GOVERNANCE/` — `ERPPLUS-152`'s `G1` terminology/invariant, `G2`
package-to-entitlement and `G3` storage/database gates, each with its draft, specialist review, independent
challenge, freeze candidate and gate disposition.

**Path-level exclusion is not sufficient authority** to declare no bearing — a peer session can rule on a
Phase SA item from a file whose path says nothing about Phase SA. So the 16 files were searched at **content
level** for every Phase SA decision, veto and constitution identifier:

`JT-04` `JT-05` `XD1-P1` `TV6-BOSS-01` `TV6-BOSS-02` `XMC-D-01` `XMC-D-02` `C2-D-01` `C2-D-02`
`POH-D-01…06` `MTI-D-04` `RC-D-01…04` `CF-D-01` `CF-D-02` `C-02` `BLK-07` `BLK-08`
`AAS-V-01/02/03` `CF-V-01` `CF-V-02` `RC-V-01` `BD-ACC-01/02/03A/03B` `SMEPLUS-DR-EXIT-8C-001`

**Result: `0` hits.** Additionally `Phase SA` as plain language: `0`.

### 5.1 `SC-F-01` — the first instrument was dead, and a positive control is the only reason this is known

**A negative result was produced by a pattern that could not fire.** The first sweep used
`grep -E '(^|[^A-Za-z0-9-])C-02([^0-9]|$)'` and returned `0`. Run against a file **known** to contain
`` `C-02` `` — `SA_FINAL_03`, where `C-02` is `F8`'s decision ID — it also returned **`0`**.

Cause: **BSD `grep -E` on this host does not match a `(^|…)` alternation group in this position.** The same
expression without the `^` alternative returns `3`. The dead pattern's silence was **indistinguishable from
a true zero**, and it was pointed at a load-bearing negative claim — *"the new mainline work does not touch
Phase SA"* — which, if wrong, would have been inherited into every downstream file of this continuation.

**Correction:** the sweep was re-run with `\b…\b`, and the pattern was proven live before its zero was
believed — `36 of 36` identifiers fire across `14` files of the parent pack (`E17b`).

**A first draft of §5 also mis-declared the naive pattern's one hit as bearing.** `grep -E 'C-02'` matched
`SEC-02` in `19_G3_SPECIALIST_REVIEW.md` — a substring of an unrelated finding ID. Both the false positive
and the false negative sat in the same sweep: **the loose pattern over-reported and the strict pattern was
dead.** Only the word-boundary form, validated against a positive control, is sound.

This is the programme's recorded *executed-not-quoted* and *counting-command-validation* class, committed
inside the file whose subject is re-measurement. It is published against this round.

### 5.2 The one relocated Phase SA item, re-checked at its own gate

`SA_FINAL_02` §4.1 relocated the **prepaid-wallet balance-sheet character and tax treatment** to
`ERPPLUS-152`'s `G6` Metering / Wallet Gate. Because that session is the one that moved, its progress was
measured rather than assumed: it has published through **`G3`**, disposition *"READY FOR `G4` COMPUTE /
RUNTIME GATE"*. **`G6` has not been reached and the wallet question is still undecided there.**

**Consequence for Phase SA: none, and the relocation remains correct.** The item is not silently
un-owned — it has an owner, a gate and a not-yet-arrived decision point. It is **not** re-imported into the
Phase SA Boss list.

---

## 6. Delta classification

| Delta | Class | Effect on Phase SA |
|---|---|---|
| PR #63 merged; corrected blob authoritative | **MATERIAL — CLOSING** | Category 3 `1 → 0`; the `SA_FINAL_04` conversion clause discharged |
| 17 commits / 16 files of `ERPPLUS-152` `G1`–`G3` | **NON-MATERIAL to Phase SA** | 0 identifier hits, instrument proven live; no Boss item, veto or scenario moves |
| `ERPPLUS-152` reached `G3`, not `G6` | **NON-MATERIAL — status confirmation** | the relocated wallet item stays relocated and stays open |
| Branch population `188 → 190`, corrected `5 → 8`, uncorrected `183 → 182` | **NON-MATERIAL — expected** | matches the parent's published prediction exactly |
| `SC-F-01` instrument defect | **PROCESS — this round's own** | corrected before publication; no downstream file rests on the dead pattern |

**New Category 3 items introduced by any of the above: `0`.**

---

## 7. Residual

1. **This measurement is time-stamped.** `origin/SMEsPlus` is live and unprotected and moved 17 commits
   between the parent's freeze and this one. Any figure here describing it is true as at this file's
   publication and must be re-measured, not inherited — the same caution the parent recorded, now applying
   to this file.
2. **`GAP-KC-01` is not closed by this.** The folder disposition of `16_Learning_Analysis` remains PMO-owned
   and open; a corrected claim inside a folder is not a decision about the folder.
3. **The 182 uncorrected historical heads are unchanged by design**, not by omission.
4. **Closing the PMO act removes a Category 3 gap; it opens nothing.** Pre-Test entry is re-qualified from
   current evidence at `SC-05`, and this file supplies one input to that recomputation, not its result.

---

## 8. Checkpoint

> ## `CP-SA-SC-00 — MAINLINE DELTA RE-MEASURED`
> **Default branch `a20db7a3` · PR #63 `MERGED` at `3f5d915a` (two command shapes) · corrected blob
> `827b5906` authoritative, public fetch `HTTP 200` hashing to it · the unqualified claim is **not** live ·
> former Category-3 PMO blocker **CLOSED**, count `1 → 0` · population `190 / 8 / 182 / 0` on two shapes,
> matching the parent's prediction · 17 post-merge commits measured at content level with a proven-live
> instrument: **0 bearing** · `ERPPLUS-152` at `G3`, wallet gate `G6` not reached · 1 process finding
> (`SC-F-01`, corrected before publication) · 0 new Category 3 items.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
