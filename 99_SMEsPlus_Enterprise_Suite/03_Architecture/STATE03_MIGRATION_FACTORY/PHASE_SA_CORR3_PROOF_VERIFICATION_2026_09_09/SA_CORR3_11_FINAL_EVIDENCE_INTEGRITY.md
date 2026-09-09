# SA_CORR3_11 — FINAL EVIDENCE INTEGRITY
## CP-SA-C3-95 — FINAL EVIDENCE INTEGRITY VERIFIED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR3-PROOF-001]` · Frame: **`CORR3-FRAME`**
Boss: **SOLE FINAL APPROVER**

---

## 1. The eleven checks master prompt §17 requires, each executed

| # | Requirement | Method | Result |
|---:|---|---|---|
| 1 | **Every material claim has evidence** | Every finding row in all 14 artifacts carries an evidence pointer — blob SHA, repo path, or a named commit | **SATISFIED.** Spot-verified on 12 load-bearing claims, listed at §2 |
| 2 | **Every pointer resolves** | Every backticked hex token of 7–40 chars across the package resolved with `git cat-file -t` | **56 distinct tokens · 11 commits · 45 blobs · `0` UNRESOLVED** |
| 3 | **No cited evidence file is empty or corrupt** | Extraction coverage on the frame that produced every citation | **3,900 requested / 3,900 written / 0 missing / 0 zero-byte** |
| 4 | **Every count is reproducible** | Each headline count re-run in a **second command shape**; disagreements published, not reconciled silently | **SATISFIED.** §3 lists the reproductions and the **four disagreements published** |
| 5 | **22-scenario status is reproducible** | §3.1 table re-counted by row and by identifier enumeration, two shapes | **22 rows · scenarios 1…22 each exactly once · `0 VERIFIED / 0 N/A / 22 HOLD` · 0+0+22 = 22** ✓ |
| 6 | **Invariant status is reproducible** | Denominator re-derived on two shapes with the one-token discriminator printed before counting | **58 · `0 PROVEN / 0 N/A / 0 SUPERSEDED / 58 HOLD` · 0 left as merely `SPECIFIED`** ✓ |
| 7 | **False positives removed or superseded** | Every inherited claim re-tested before use; falsifications recorded as findings, not silent deletions | **4 CORR2 Boss-facing items falsified · 3 executor returns corrected on intake · 6 of 9 executors corrected themselves before publishing.** §4 |
| 8 | **No unsupported compliance claim remains** | Pattern `ISO 27001\|ISO 9001\|SOC 2\|GDPR` over all 14 CORR3 files, every hit read | **`0` unqualified claims.** Every hit is a quotation of the prohibition, a pattern literal, or a classification row. The one live claim in the repository is **corrected** (`C3-G-01`) |
| 9 | **No misleading `PASS` / `CERTIFIED` wording remains** | Word-bounded sweep, every occurrence read individually | **40 `PASS` occurrences — every one a quotation of another package's verdict or of a constitution clause. `0` affirmative verdict-shaped `PASS` issued by any CORR3 file** (verdict-shaped pattern with the standard exclusion list returns empty). **2 `CERTIFIED` — a pattern literal and a classification row; neither is a claim** |
| 10 | **All material unresolved gaps have an exact proof gap, an owner and a next action** | Every `HOLD` traced to its artifact's proof-gap table | **SATISFIED.** §5 consolidates them |
| 11 | **No Boss question remains that SMEs Core could research or prove itself** | The §18 qualification test applied to every candidate, all seven questions | **SATISFIED.** `SA_CORR3_00` §5. Two items CORR2 marked *"research can close: yes"* were **executed rather than carried** |

---

## 2. The twelve load-bearing claims re-verified by the orchestrator against primary text

Executor returns were **not adopted on the executor's word**. These were re-run independently:

| # | Claim | Re-verification | Result |
|---:|---|---|---|
| 1 | Element 10 is unconditional; element 15 equally so | The 16 elements extracted from the contract blob; qualifiers counted | **CONFIRMED — 6 qualified, 10 unqualified; element 10 the only one carrying `mandatory`; element 15 carries no qualifier** |
| 2 | The 16-element contract is scoped to one boundary | Title + all scope clauses read | **CONFIRMED — four clauses, all *"Inventory → Accounting"*** |
| 3 | Phase SA never read the 31-row handoff register | `10_INVENTORY_CROSS_MODULE_HANDOFF`, `07_…CONTROL_IMPACT`, `HX-` over the active package | **CONFIRMED — 0, 0, 0**, control `03_INVENTORY_FUNCTIONAL_DESIGN_V1` = 1 |
| 4 | Phase SA never read the target Accounting Core baseline | 7 patterns over the active package | **CONFIRMED — 0 each; control `BD-ACC-01` = 28.** Baseline exists as 14 files |
| 5 | The invariant set was never read against 4 standing rulings | Per-blob token count over the 35 isolation blobs | **CONFIRMED — `BD-ACC-01/02/03`, `GB-08` all 0; control `MTI-D-01` = 26** |
| 6 | `BLK-06` is closed by a Boss decision | Blocker register read | **CONFIRMED — `CLOSED — BOSS DECISION`, closed by `BD-02`** |
| 7 | `BLK-08` exists and is maintenance-specific with a recommendation | Decision register read | **CONFIRMED — verbatim, recommendation `Split`** |
| 8 | `SA_CORR2_05`'s checkpoint contradicts its own corrected table | Lines 69 / 232 read | **CONFIRMED — `14+3+1=18` vs `13 of 18 … 4 …`.** Independently reproduced by **three** executors |
| 9 | The Quality object exists | 4 patterns re-run | **CONFIRMED — `quality check` = 10 / 16; `QualityCheck` = 5, of which two are Layer-1 clean-room blueprints** |
| 10 | The four database archives exist on the host | Directory listing | **CONFIRMED — all four, with the exact names and dates reported** |
| 11 | `Q-BOSS-02` is APPROVED, not open | Ruling read at its own commit | **CONFIRMED — `APPROVED — STRUCTURAL INDEPENDENCE AUTHORITY DEFINED`, ten controls, `2930723`** |
| 12 | Phase SA entry authority is valid | Commit times of the two conflicting records compared | **CONFIRMED — the Boss act is 11 h 25 m later, and later than the gate it cites** |

---

## 3. Counts reproduced, and the disagreements published

**Every headline count in this package was run in a second command shape.** Four disagreements were found
and **all four are published in the artifacts rather than reconciled silently**:

| Disagreement | Cause | Disposition |
|---|---|---|
| Corpus set difference **2,859** vs arithmetic **79** | **`git diff --raw` abbreviates blob SHAs to 8 chars while `ls-tree` gives 40** — the union deduplicated across incompatible key widths | **Instrument corrected.** Caught because a set operation disagreed with its own subtraction, not by inspection |
| Asset↔object relation count **4** vs **3** | **The unit differed, not the population** — 3 relations expressed as 4 foreign-key rows | **Published as `MNT-F-16`**, not reconciled |
| `XD1-05` denominator **41** vs **38** | The executor counted files it did not then search | **Corrected on intake (`XD1-C1`).** Result unchanged — still 0 against a control of 28 |
| Over-absorption treatments **1** vs **2** | A narrow alternation missed a hit | **Published as `POH-C-07`.** *"A count validated only against its own pattern is not validated"* |

**Frame controls, re-fired at close:** positive `BD-ACC-01` **55**, `clean.room` (-i) **1,266**; negative
`qxvz7481_no_such_token` **0**; injection control **0 → 1 → 0**. All as declared.

---

## 4. False positives and superseded claims — removed by correction, never by deletion

| Inherited claim | Disposition |
|---|---|
| *"The Quality object does not exist — 0 blobs, two command shapes"* | **FALSIFIED.** `quality check` returns 10 |
| *"`PHASE-S/Q-BOSS-02` — raised and unanswered"* | **FALSIFIED.** APPROVED 2026-09-07 |
| *"No amount of research resolves an ambiguity in a ruling"* (`C2-D-03`) | **FALSIFIED.** 12 of 16 cases resolve by quoting the ruling |
| *"Price determination `INPUT-EVIDENCE-INSUFFICIENT`"* | **EVIDENCE-REJECTED.** The negative's authority was a vocabulary count |
| *"The deterministic identity is owned by neither"* | **CORRECTED.** `BD-ACC-01` names three owners explicitly |
| *"Publishing the contract closes `H-01`, `H-02`, `H-03`, element 15, `JCP-03`, `AR-26`"* | **FALSIFIED — it closes none**, and does not bear on `H-02` at all |
| *"It is element 10, unconditionally, on every scenario"* | **NARROWED.** Sufficient, not necessary; `(b)` = 0 of 22 |
| *"Maintenance cost never becomes an accounting fact at all"* | **OVER-WIDE.** Falsified on 2 of 5 cost-origin classes |
| *"Seven of eight overhead elements"* | **Denominator author-chosen and superseded**; union = 9 |
| *"SMEsPlus control: none yet"* (TAS 2 ¶12 row) | **CONTRADICTED.** Four design candidates exist, unadopted |

**`C3-E-01` — the pattern across all ten.** Every one of these was a **negative** produced by a party whose
**positive control fired**. In no case was the reasoning wrong. **In three cases the instrument's blind spot
and the evidence base were the same set** — a spaced pattern that could not reach run-together identifiers; a
clean-room scrub that removed the very tokens the pattern needed; a diff-based clause that could not reach an
inherited blob.

> **The transferable control, and it is this round's most useful output: a positive control must be chosen to
> sit inside the blind spot the pattern is suspected of having, not merely inside the corpus. A control drawn
> from the same vocabulary as the failing pattern will fire and prove nothing.**

---

## 5. Material unresolved gaps — each with exact gap, owner and next action

| Gap | Exact proof gap | Owner | Next action |
|---|---|---|---|
| **58 invariants, 0 proven** | 57 have runtime truth-makers and are unreachable at Phase SA **by construction, not by effort** | Development / Pre-Test | Build, then prove. **3 of the 11 element-10 gating invariants cannot be closed by building alone** |
| **The privileged-bypass path enumeration** | The path set is **not enumerated**; the audit was started and never finished | SMEs Core | **An evidence act, not a build — the earliest item on the element-10 critical path that could start today** |
| **`CF-I-03` does not exist** | The authorization conformance control that `MTI-43`'s second attestation references | SMEs Core | Design it, or the attestation stays a reference to nothing |
| **22 of 22 `HOLD`** | `VERIFIED` requires an implementation and an executed test; Phase SA may produce neither | Development / Pre-Test | Build and prove. **Discharging element 10 alone moves 0 of 22 → 0 of 22** |
| **`XD-06` contract published but not built** | Specification satisfies *known* and arguably *traceable*, **never *evidence-backed*** | SMEs Core → Pre-Test | Publish (**done, `SA_CORR3_08` §3**), then build, then prove |
| **Element 10 absent from the producing payload** | A **second cause independent of the invariant programme** | SMEs Core | Add tenant + company to the emitted payload — `XMC-C-D1` |
| **`TV6-B-03`** exposure coverage | Whether delivered-not-invoiced is inside the exposure figure | Research | **One query per deployment**, with a never-transacted negative control |
| **`TV6-A-14`(c)** field-level permission | Whether price and discount fields carry a group restriction | Research | **One query per deployment**, two generations |
| **`TV4-G-01`** Quality liveness | **No row count exists anywhere** for the 18 deployed tables | Research | One query |
| **Thai statutory items** | Gazetted primary text **not read in this frame** | Boss / Legal / Tax track | **All held. No statutory claim is made anywhere in this package** |
| **Compliance overclaim propagation** | Corrected on **1 of 184** branches | PMO / repository owner | A mainline act. **Not a Boss decision** |
| **Constitution version drift** | **58 of 184** branches carry v1.0, predating the independent-expert structure | PMO | Recorded, not remediated |

---

## 6. What this register cannot certify, stated plainly

1. **Nothing here is independent.** Every layer is same-model. `Q-BOSS-02` controls 1 and 2 fail decisively.
   **The integrity of this package was checked by the party that produced it.**
2. **`0` proof obligations are discharged.** This round moved **none** of them, and no artifact claims
   otherwise. **What changed is the accuracy of the map, not the state of the territory.**
3. **The frame has a stated complement** — non-head-history blobs and all non-`.md`/`.txt`/`.csv` files. **A
   design artefact abandoned mid-branch, or a specification in a spreadsheet or diagram, is outside everything
   searched in this package**, except where an artifact declared its own wider instrument and said so.
4. **Three of the four falsified negatives were falsified by an *instrument* change.** By symmetry, **this
   package's own negatives are exposed to the same class of defect, and no control here can rule it out** —
   only a differently-vocabularied party can.

---


### 6.1 `C3-E-02` — the pre-commit sweep produced two wrong answers before its third, and the checker was the defect both times

Recorded because it happened **in this register's own closing sweep**, and because a peer executor
independently recorded the same defect class (`TV6-K-03`).

The identifier sweep was run three times and gave three different answers:

| Run | Result | What was actually wrong |
|---:|---|---|
| 1 | **1 orphan** — `C3-E-01` | **The checker.** Its definition-regex required a bolded identifier immediately followed by a closing `**`; the identifier is defined as `**`C3-E-01` — the pattern across all ten.**`, a **legitimate definition form the regex could not see** |
| 2 | **"cited 1"** for every family, including families with six | **The checker again.** A `for id in $cited` loop over an unquoted multi-line variable **does not word-split in this shell**, so the loop ran once with the whole list as a single token |
| 3 | **17 cited · 17 defined · 0 orphans** | Correct. Re-run with `while IFS= read -r`, one identifier per line, and a definition regex covering **all four** legitimate definition forms |

> **The document was clean at run 1. Both failures were in the instrument, in opposite directions: run 1
> produced a false positive, and run 2 would have produced a false *negative* for any family whose
> identifiers were genuinely orphaned — it reported "cited 1 / orphans 0" for a family of six.**
>
> **A checker that cannot see one of its subject's legitimate forms will report a clean document dirty; a
> checker whose loop silently collapses will report a dirty document clean.** This round met both, on the
> same check, ten minutes apart. **The only reason either was caught is that the three runs disagreed** —
> which is the same control that caught the blob-SHA width defect at §3. **Disagreement between shapes is
> doing more work in this programme than any single result.**


## 7. Checkpoint

# `CP-SA-C3-95 — FINAL EVIDENCE INTEGRITY VERIFIED`

`CLOSED (execution status)`. **Checkpoint completion is NOT Boss approval.**

| | |
|---|---|
| §17 checks executed | **11 of 11** |
| Pointers unresolved | **0 of 56** |
| Affirmative `PASS` verdicts issued by this package | **0** |
| Unqualified compliance claims in this package | **0** |
| Clean-room vendor tokens across all 14 artifacts | **0** |
| Counts re-run in a second shape | **all headline counts**; **4 disagreements published** |
| Inherited claims falsified or corrected | **10** |
| Independence claimed | **none** |

Boss remains the sole Final Approver. No Evidence = No Progress. Never Skip Gate.
