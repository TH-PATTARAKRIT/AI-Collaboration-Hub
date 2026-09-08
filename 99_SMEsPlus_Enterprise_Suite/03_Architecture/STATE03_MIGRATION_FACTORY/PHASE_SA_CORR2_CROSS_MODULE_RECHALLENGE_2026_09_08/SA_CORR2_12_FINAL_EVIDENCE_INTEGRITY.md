# SA_CORR2_12 — FINAL EVIDENCE INTEGRITY
## CP-SA-C2-95 — FINAL EVIDENCE POINTER INTEGRITY VERIFIED

Session: `[SMEPLUS-26-09-08-PHASE-SA-CORR2-XMOD-001]`
Governing law: master prompt §15.

---

## 1. Checks executed, with their results

Every check below was **run**, not described. Where a check found nothing, its positive control is
reported so that the zero is a measured absence rather than a broken instrument.

| # | Master-prompt §15 requirement | Instrument | Result |
|---|---|---|---|
| 1 | Every material claim has evidence | Each status change traced to a verbatim quotation with the owning package's own status tag | **Met** — see §2 for the two exceptions, which are labelled as determinations rather than findings |
| 2 | Every evidence pointer resolves | `git cat-file -t` on every backticked hex token in the package | **14 of 14 resolve** — 11 commits, 3 blobs. **§1.1** |
| 3 | No referenced file is empty or corrupt | Corpus extraction coverage assertion | **3,789 requested / 3,789 written / 0 missing / 0 zero-byte** |
| 4 | Counts are reproducible | Every load-bearing count re-run under a second unit or a second command shape | **Met, with two published failures — §3** |
| 5 | Branch and commit citations are correct | `git rev-parse --verify` per citation | **All resolve** |
| 6 | Stale false positives removed or clearly superseded | `K2-01`…`K2-15` applied by population to the parent registers | **15 applied; §4 verifies each landed** |
| 7 | No unsupported `PASS` remains | Verdict-shaped sweep over this package | **0 affirmative `PASS` verdicts in any CORR2 file.** Positive control: the pattern returns 269 paths corpus-wide, so it fires |
| 8 | No unsupported compliance claim remains | Standards sweep over this package | **0.** The one corpus-wide claim is *reported*, never asserted (`SA_CORR2_07` §3) |
| 9 | Every open `HOLD` has an exact owner and reason | `SA_CORR2_13` §5 | **Met** |
| 10 | Every Boss decision request is genuinely Boss-authority only | Tested item by item against the ruling that reserves it | **Met — and two candidate items were *removed* from the Boss list on this test; §5** |

### 1.1 Evidence-pointer resolution, in full

```
SHA citations in the CORR2 package: 14
  commits (11): cd26c2da…, f0548a20, e280611a, be5d1595, fa57d10f, e47f0f2f,
                a11c9e7b, 36c62ab3, 4c469f8e, 296b495, d9e845e
  blobs   (3):  25a98a50 (8,994 B) · 34e698ab (16,287 B) · 4deacf0f (15,128 B)
  UNRESOLVED: 0
```

**The three blob citations are load-bearing and are verified by size**, because `SA_CORR2_09` §1's
finding *is* the size difference: the version `SA09` read is the 8,994-byte one, the only one of the
three lacking the section that closes the gap it reported. The published byte counts match the
objects exactly.

**A defect in this check's own first run, published.** The first pass tested every hex token with
`git cat-file -t` and flagged three as `NOT-A-COMMIT`. They are **blobs**, cited correctly as blobs.
The instrument assumed every pointer is a commit. **An integrity check that mistakes a correct
citation for a broken one is as damaging as one that misses a broken pointer**, and it would have
produced three false corrections. Corrected to resolve by actual object type.

---

## 2. Claims in this package that are determinations, not findings — labelled

Master prompt §15's first requirement is that every material claim has evidence. Two classes of
statement in this package are **not** evidenced and must not be read as if they were:

| Statement class | Where | Status |
|---|---|---|
| **Nature DNA determinations** `ND-09`, `ND-10`, `ND-11`, `ND-12` | `SA_CORR2_01` §4.4, §5.1; `SA_CORR2_03` §3.1; `SA_CORR2_11` §5 | **SMEsPlus design positions with independent rationale.** Each states what SMEsPlus will do and why. **None is a finding about the evidence**, and none is Boss-approved |
| **The four decisions `C2-D-01`…`C2-D-04`** | `SA_CORR2_02` §6 | **Questions, not answers.** Each names its authority |

The distinction matters because `SA12-F-01` records that the Nature DNA obligation which fails
silently is *"what did we deliberately not inherit"* — and a determination presented among findings
reads as inherited fact.

---

## 3. Reproducibility — including the two counts this package could not reproduce and the two of its own that failed

### 3.1 Reproduced

| Count | Second instrument | Agreement |
|---|---|---|
| Population 183 branches | three command shapes (`for-each-ref` minus alias; `ls-remote --heads`; `packed-refs`) | **all three = 183** |
| Corpus 3,789 text blobs | coverage assertion + content positive controls (`BD-ACC-01` 34, `clean.room` 1,219) + negative control 0 | **consistent** |
| `\bcancel` under Order-to-Cash = 23 | four units — paths, blobs, branch-path pairs, any path named `P02` | **all four = 23** |
| The ISO/SOC/GDPR claim on every branch | per-branch `git rev-parse '<branch>:<path>'` over all 183 | **183 present, 183 byte-identical, 0 absent** |
| Handoff contract 16 elements | primary approval text vs two secondary renderings | **element names agree exactly**; element 14's conditional and element 10's non-conditional both confirmed verbatim |

### 3.2 Not reproduced, and said so

| Count | Why |
|---|---|
| `SA11` §9.2's *"`SOX` — 175 hits inside one binary document"* | This corpus extracts only `.md`/`.txt`/`.csv`. The path set contains 19 `.pdf`, 6 `.zip`, 4 `.docx` and 1 `.jpg` that were never extracted. **Neither reproduced nor refuted**, and the reason is published rather than the figure dropped |
| The nine CORR1 findings with no disposition row (`N-05`) | The adversarial pass's own output is not in the repository. **Unrecoverable from evidence**, recorded as an open lineage item rather than silently closed |

### 3.3 `C2-F-29` — two of this package's own check-claims were false, and a mechanical sweep caught both

| Claim, as first written | Test | Result |
|---|---|---|
| *"every identifier `AR-01`…`AR-29` appears exactly once in §2"* | regex enumeration of the table's first column | **24 distinct, not 29** — six rows had been compressed into `AR-01…AR-06` and three into `AR-07…AR-09` |
| *"every identifier `BN-01`…`BN-18` appears exactly once above"* | same | **6 distinct, not 18** — seventeen were written `BN-01, 02, 03, …`, which a checker reads as one identifier and sixteen bare numbers |

Both claims **read true to a human and failed their own stated check.** Both are the defect class
this package convicts `SA20` of at `N-05` — an assurance sentence that cannot be verified by the
method it names — **committed by the author, inside the line asserting correctness.**

Corrected: rows written out in full, both claims re-verified mechanically, both now enumerate
`18/18`, `29/29`, `18/18`, `16/16`.

> **A check line is a claim. It is the one claim in a register that readers never test, because
> testing it is the register's own job.**

---

## 4. Corrections applied by population — each verified in the target text

| # | Target | Verification executed | Result |
|---|---|---|---|
| `K2-01` | resume state `SA00-F-03` | count of the falsified sentence outside a struck/quoted context | 1 → **0** |
| `K2-02` | `SA15` header | header figure vs §4 table | 6 → **4**, and the identifiers are now carried in the header |
| `K2-03` | `SA13` §6 | the falsified self-assessment | present → **struck, with the falsifying finding in its place** |
| `K2-04` | `SA19` §16 + `SA20` status | both now state their unit | **applied** |
| `K2-05` | `SA20` §2.1 | `24 files` → `23 unique paths (U2)` | **applied**, reproducible under four units |
| `K2-06` | `SA20` §2.2 | `12 occurrences in [a file]` → `12 unique paths across [a programme]` | **applied** |
| `K2-07` | `SA20` §6 | the universal *"every negative was re-tested"* | **withdrawn**, exception named |
| `K2-08` | seven registers | the `SA20` §4 accepted-open set | **7 of 7 dispositioned** — `SA_CORR2_08` §3 |
| `K2-09` | `SA04` §2 | *"two independent measurements"* and *"every route with an Accounting endpoint"* | **both withdrawn** |
| `K2-10` | `SA13` §4.2 | *"the design position is closed"* vs `SA14`'s `XD-06 OPEN` | **reconciled** |
| `K2-11` | `SA12` §4 | *"Four"* vs the eight then extant | **corrected to eight, extended to eleven** |
| `K2-12` | `SA11` §5 | heading and sentence asserting the absence §7.5 narrows | **corrected in place** |
| `K2-13` | `SA13` §3 | `SA13-F-01` re-framed per `C2-F-22` | **applied, with the Boss ruling quoted in place** |
| `K2-14` | `SA15` §6 | `SA15-F-02` qualified per `N-15` | **applied** |
| `K2-15` | `SA_CORR2_03`, `SA_CORR2_07` | clean-room scrub, with the count delta measured | **applied; 3 → 0** |

**Every correction was verified in the target file text, not in a disposition column.** That is the
discipline `SA_CORR2_00` §1 exists to enforce, applied to this package's own corrections.

---

## 5. Boss-authority test — two candidates removed

Master prompt §15 requires that every Boss decision request be genuinely Boss-authority only, and
§16 forbids presenting routine operational corrections as Boss decisions. Each candidate was tested:

| Candidate | Test | Outcome |
|---|---|---|
| The secondary TAS overclaim in a revalidation register | Is it a governance act, or a wording fix? | **REMOVED from the Boss list** — routed to PMO (`SA_CORR2_07` §5) |
| Two of three `APPROVED`-by-a-non-Boss-body candidates | Are they attributed to Boss in their own headers? | **REMOVED** — two are attributed; one PMO item remains (`SA_CORR2_08` §7) |
| `XD-06` publish the `BD-ACC-01` contract | Does a ruling already assign it? | **NOT a Boss decision** — `BD-ACC-01` already assigns ownership. SMEs Core design obligation |
| `C2-D-01`, `C2-D-02` | Is there a ruling that settles them? | **No** — but they are design positions first. **SMEs Core → Boss confirm**, not raw Boss questions |
| `C2-D-03` kit vs component Product Category | Is it an ambiguity *inside* a Boss ruling? | **YES — genuinely Boss.** `BD-ACC-03A/03B` are Boss rulings and neither resolves a kit spanning categories |

---

## 6. Clean-room integrity of this package

| Sweep | Unit | Result |
|---|---|---|
| Vendor/reference technical tokens, declared ∪ derived | occurrence per file | **0 across all 12 CORR2 files** — after `K2-15` removed 3 |
| Baseline comparison, per file, against the parent package | occurrence delta | parent **0**, CORR2 **0**; **no file rose above its baseline** |
| Prohibited verdict wording | line | **0 affirmative `PASS`**; the pattern fires elsewhere (269 paths) |
| Identifier consistency | identifier | every cited `C2-F`, `C2-I`, `C2-D`, `K2`, `N`, `JCP`, `ND` identifier has a definition in this package or a cited external register. **0 orphans** |
| `ND` numbering collision with the parent's `ND-01`…`ND-08` | identifier | **none** — CORR2 adds `ND-09`…`ND-12` |

**Three leaks were found and removed** (`K2-15`), all in text that was **correct**: a third-party
module's technical name quoted for precision, and two reference object names inside a *published
search pattern*. The second is the harder case — reproducibility argues for publishing the pattern
and the clean-room rule forbids the tokens in it. **Resolved by publishing the clean pattern and the
measured effect of removing them** (−20 on the subject, −70 on the control), so nothing is hidden and
nothing leaks.

---

## 7. What remains unverified, stated rather than omitted

- **No proof obligation moved.** `0 of 22` cross-proof scenarios, `0 of 8` isolation proofs,
  `0 of 13` enforcement surfaces, `0 of 52` negative access tests. This package reconciles and
  determines; it proves nothing.
- **The nine undispositioned CORR1 findings (`N-05`) cannot be recovered** from repository evidence.
- **The `SOX` binary figure is neither reproduced nor refuted** (§3.2).
- **No independent assurance exists** (`SA_CORR2_11`), and the frame defect `C2-I-02` shows what an
  internal challenge inside the author's own corpus structurally cannot find.

---

`CP-SA-C2-95 — FINAL EVIDENCE POINTER INTEGRITY VERIFIED (execution status).`

Checkpoint completion is **not** Boss approval.

Boss remains the sole Final Approver. No Evidence = No Progress. Never Skip Gate.
