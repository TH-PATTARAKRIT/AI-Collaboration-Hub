# 07 — ACCOUNT WAVE A — NEGATIVE CLAIM CONVERGENCE SCAN

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001` · Layer 1 clean-room · cites `MCE-0NN`
Applies `DR-NC-01` … `DR-NC-06` to the **entire current Wave A canonical package**.

---

## 1. The denominator, stated first

`G06` — the parent scan — declares its scope as *"45 canonical Wave A files"*. Measured against the
package as it actually stands at the gate baseline (`MCE-011`):

| Measure | Value |
|---|---|
| Canonical package files | **64** |
| Canonical package lines | **14,575** |
| Files inside `G06`'s scope | 45 |
| Lines inside `G06`'s scope | 6,113 — **41.9%** |
| **Files never scanned** | **19** |
| **Lines never scanned** | **8,462 — 58.1%** |

The 19 unscanned files are not marginal. They are **every expert review (`X1`–`X4`), every fresh
independent review (`L12A`, `L12B`, `GR1`, `GR2`), the adversarial challenge register (`C1`), both
Layer-2 evidence files (`E00`, `E01`), and the final gate report `G10` itself.**

This is the same defect one level up, and it is `DR-NC-01`'s own subject matter: **`G06` scanned the
files it had in mind, and reported the result as a property of the package.** The scan's scope was
author-derived. Enumeration rule `ER-24` fixes the denominator to the package manifest.

## 2. Scan executed this round

Tokens per the round instruction — `never`, `always`, `cannot`, `does not exist`, `no support`,
`no control`, `no validation`, `impossible` — plus `there is no`, `no such`, `anywhere`.

| Token | `G06` scope (45 files) | **Unscanned (19 files)** |
|---|---|---|
| `cannot` | 68 | **125** |
| `never` | 66 | **105** |
| absolute-absence forms | 50 | **83** (`there is no` 63 · `does not exist` 12 · `no such` 8) |
| `always` | 15 | **9** |
| `anywhere` | not separately reported | **45** |
| `no control` / `no validation` / `impossible` / `no support` | 1 (system-wide phrasing) | **10** |
| **Total raw hits** | **200** | **377** |
| **Package total** | | **577** |

The never-scanned portion carries **1.9×** the raw negative-claim load of the portion that was
triaged.

## 3. Triage of the unscanned set

Full triage of 377 hits was not completed this round. What was completed is a **bounded high-risk
pass** — every hit carrying a universal-scope qualifier, the form `DR-NC-01` exists to catch.

| Category | Count | Treatment |
|---|---|---|
| Universal-scope absence phrases (`anywhere in the tree` / `nowhere in` / `does not exist anywhere`) | **11** | Individually read — §4 |
| Quotation of a claim already rescoped by `G06`/`C04`, or of the rule itself | 6 of the 11 | **Compliant** — lineage, not new claims |
| Reviewer text *challenging* an unbounded claim | majority of the `anywhere` hits | **Compliant** — the reviewers were applying `DR-NC` correctly, which is why they found the breaches |
| **New unbounded factual negatives, authored in unscanned files** | **5** | **Non-compliant — §4** |
| Remaining hits not individually triaged | **~366** | **`NOT YET SEARCHED`** — declared, not estimated |

## 4. New unbounded factual negatives found this round

Authored inside files `G06` never scanned. Each is restated at the scope its evidence supports.

| # | Claim as written | Where | Class | Required rescoping |
|---|---|---|---|---|
| `MCNC-01` | "There is no database-level assertion of balance **anywhere on the entry table**" | expert review | **`A` within scope** | True for the entry table as read; the storage-constraint population is **11 tuples in 6 blocks** (`MCE-002`) and none asserts balance. **Now a bounded verified absence** — rescope to "within the 11 enumerated storage constraints of the Wave A models" |
| `MCNC-02` | "no message post, no message log, and no logger call **anywhere**" on a named path | expert review | **`B`** | Rescope to the named path and the files read. Whole-tree logging was not searched |
| `MCNC-03` | "no maker-checker **anywhere in the core ledger**" carried forward as settled | challenge register | **`E` — already contradicted** | Superseded by `RS-02`: an approval engine exists in another module, can gate the posting action, cannot gate the underlying write, and is skipped under elevated privilege. The unscanned file still carries the un-rescoped form |
| `MCNC-04` | "no failure raised **anywhere on the path**" | expert review | **`A` within scope** | The failure-path population is now bounded at **153** (`MCE-002`); rescope to "none of the 153 enumerated failure paths lies on this path" |
| `MCNC-05` | "the rate used is not stored **anywhere**" | final review | **`B`** | Rescope to the report-options surface read. Persistence elsewhere not searched |

**None of the five changes a decision, a severity, or a gate blocker** — the same result `G06` §8
reported for its seventeen. Two of them (`MCNC-01`, `MCNC-04`) are *strengthened* by this round: the
populations they assert absence over are now bounded, so they convert from "not found" to a verified
absence within a counted scope.

## 5. Required classification of every material negative claim

Per the round instruction, each material negative claim is classified. Position at the end of this
round:

| Class | Count | Notes |
|---|---|---|
| **`VERIFIED ABSENCE`** (within a fully enumerated bounded scope) | **4** | `MCE-004` no record-scoping rule on either reconciliation model, bounded across 797 modules · `MCE-006` the configuration-key class is closed at 5 · `MCNC-01` · `MCNC-04` |
| **`NOT FOUND IN SEARCHED SCOPE`** | **20** | `G06`'s 17 rescoped, plus `MCNC-02`, `MCNC-03`, `MCNC-05` |
| **`NOT YET SEARCHED`** | **~366 raw hits** | the untriaged remainder of the 19 unscanned files |
| **`UNKNOWN`** | see file `06` | |
| **`CONTRADICTED`** | **5** | `G06`'s four class-`E` rescopings, plus `MCNC-03` |

Before this round the package held **zero** claims in class `VERIFIED ABSENCE`. `DR-NC-03` requires
that "not found" is not promoted to "verified absent" without proportional evidence; the effect had
been that *nothing* could ever reach verified absence, because no population was bounded. Bounding
populations is what makes a legitimate absence claim possible at all.

## 6. Rule-by-rule result

| Rule | Result |
|---|---|
| `DR-NC-01` absence within scope ≠ absence system-wide | **NOT ESTABLISHED for the package.** Holds for 41.9% by volume; 5 new breaches found in the remainder |
| `DR-NC-02` every material negative declares its boundary | **NOT ESTABLISHED** — same coverage limit |
| `DR-NC-03` "not found" distinguished from "verified absent" | **IMPROVED** — first 4 claims to reach `VERIFIED ABSENCE`, each over a counted population |
| `DR-NC-04` system-wide claims need system-wide evidence | **SATISFIED where tested** — `MCE-004` is the model: a genuine whole-tree claim backed by a whole-tree search |
| `DR-NC-05` independent review challenges high-impact negatives | **SATISFIED** — and this round confirms review is doing the work: most `anywhere` hits in the unscanned files are reviewers challenging unbounded claims |
| `DR-NC-06` contradicted negatives rescoped with lineage | **SATISFIED** — nothing deleted or silently edited here either |

## 7. Verdict on `MC-05`

> **`MC-05` NEGATIVE CLAIM COMPLIANCE — NOT MET.**

Not because the claims are wrong — most are sound and the control has worked well — but because
**compliance has been demonstrated over 41.9% of the package and asserted over 100% of it.** That is
itself the `DR-NC-01` error, committed by the control that enforces `DR-NC-01`.

**What closes it:** run `ER-24` over the 64-file manifest and triage the ~366 remaining hits. This is
mechanical, cheap, and requires no new research — the same argument `G06` §7 made for making the scan
mandatory, now applied to the scan itself.

## 8. Recommendation carried to the gate report

`G06` §7 recommended the mechanical scan become mandatory pre-gate. This round supports that and adds
one word: the scan must be **manifest-bound**. A scan whose file list is written by hand reproduces
the defect it was built to catch.
