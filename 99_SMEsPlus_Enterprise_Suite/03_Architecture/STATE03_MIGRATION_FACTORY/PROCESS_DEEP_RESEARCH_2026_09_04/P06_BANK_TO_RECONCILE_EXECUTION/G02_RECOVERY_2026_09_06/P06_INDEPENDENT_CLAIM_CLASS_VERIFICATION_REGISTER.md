# P06_INDEPENDENT_CLAIM_CLASS_VERIFICATION_REGISTER.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-INDEPENDENT-FROZEN-SURFACE-RECOVERY-005]`
**Session:** P06 — INDEPENDENT FROZEN-SURFACE CORRECTION RECOVERY (CP-P06R03)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Frozen SHA:** `52127569863455acc06b82a845ef64e106115900`

> **Stage 1 — published before any Stage-2 edit, per prompt §8.**
> Two passes were run over the frozen surface: an **executor pass** and an **independent verifier pass** given only the SHA, the three file roots, the nine claim classes as semantic assertions, and three known instrument hazards — **no counts, no registers, no narrative.**
> **Per §9, no challenger claim is adopted on the challenger's authority.** Every one was re-executed against the files. **Two did not reproduce and are refuted below.**

---

## 1. Independence — assessed, not asserted

| What the verifier pass establishes | What it does not |
|---|---|
| It never saw the executor's scoping, so it **cannot inherit the executor's scoping bias** — the defect that governed rounds 5 and 6 | Same underlying model family |
| Its population came from the files, not from a tally | **The executor authored its brief**, and therefore chose which nine classes are in scope |
| A disagreement between the two passes is informative, and there were many | **The executor adjudicates its output** |

### `INDEPENDENCE NOT PROVABLE — AASP-VETO-07 CANNOT BE DISCHARGED`

Reported verbatim per prompt §5. **Partial separation was achieved and it was productive** — the verifier found nine defects that two prior rounds *and the executor's own Stage-1 pass* had missed. **That is evidence the separation was real. It is not evidence that it was sufficient.**

## 2. The frozen surface was written to during the audit — disclosed

The verifier reported, unprompted, that an untracked directory appeared mid-audit and that it excluded it: `G02_RECOVERY_2026_09_06/`.

**It was right to flag it, and the cause is this session.** That directory is the executor's own Stage-0/Stage-1 record. **The executor declared a surface "frozen" and then wrote into the package root while the audit was running.** No claim file was touched — `git status` showed **0 modified files** throughout Stage 1 — but the *directory tree* the verifier was auditing changed under it, and a naive recursive enumeration would have returned 49/25 instead of 47/24.

**Recorded as `REC-E-01`.** The lesson is exact: **a freeze is a property of the tree, not of the files you promised not to edit.** Stage-1 records belong outside the audited root, or the audit must be told about them in advance.

## 3. Claim-class register

Columns per §12. **CURRENT** = the package asserts it as true now. **HISTORICAL** = a quotation, revision row, before/after table, challenge record or supersession note — correct to leave.

| # | Claim Class | File | Loc | C/H | Prior wording | Verified current wording | Evidence | Result | Downstream impact | Disposition |
|---|---|---|---|---|---|---|---|---|---|---|
| `R-01` | 2 peer publication | `13_` | :103 | **CURRENT** | — | *"**8 of 9** — P01 absent"* | `git ls-remote --heads origin` → `research/account-p01-…` exists at `b820b29` | **STALE — false assertion about a remote** | Evidence manifest; `13_` carries **zero** correction markers — rounds 5 and 6 never opened it | **REPAIR** |
| `R-02` | 9 population | `13_` | :94 | **CURRENT** | — | *"Blocker population \| `grep -oh 'P06-B-…' *.md \| sort -u \| wc -l` \| **58**"* | that exact command in that exact scope returns **65** | **STALE — printed command disagrees with printed result** | manifest integrity table | **REPAIR** |
| `R-03` | 2 peer publication | `18_` | :169 | **CURRENT** | — | *"`P06-B-03` peers unread \| **CLOSED** — 7 of 9 read; P01 and P08 re-raised"* | `48_`:96 says *"**DISCHARGED to 8 of 9** — P08 published this round"*; `53_` read P08 in round 3 | **STALE, and it is in the P11-bound pack** | **Refutes `VER-F-08`/`PROP-F-04`, which certified `18_` as carrying zero stale statements** | **REPAIR** |
| `R-04` | 9 population | `18_` | :214 | **CURRENT** | — | *"with **55 blockers** (7 closed, 48 open)"* | executed: **65** | **STALE — in the P11-bound pack** | as `R-03` | **REPAIR** |
| `R-05` | 9 population | `70_` | :108 | **CURRENT** | — | *"with **58 blockers** (7 closed, severity-ranked)"* | executed: **65** | **STALE — in the P11 supplemental handoff** | `70_` was certified clean in round 6 | **REPAIR** |
| `R-06` | 4 `is_matched` | `01_` | :115 | **CURRENT** | — | *"Branch B (`:450`): … `is_matched = True` **unconditionally**"* | `account_payment.py:447-449`: `True` **only if** `journal_id.default_account_id in liquidity_lines.account_id` | **DEFECTIVE — contradicts `01_`:122 seven lines below**, which round 6 corrected to *"by configuration alone"* | The round-6 repair fixed the summary line and left the branch narrative **in the same file** | **REPAIR** |
| `R-07` | 5 eighth door | `35_` | :97, :99 | **CURRENT** | — | *"**PH-F-05 — P05 supplies an eighth ingestion/settlement door P06 did not count.**"* | `62_`:42 names *"`35_` PH-F-05"* **by name** as the original that was corrected | **STALE — the named original was never edited** | Peer handoff matrix | **REPAIR** |
| `R-08` | 5 eighth door | `36_` | :58 | **CURRENT** | — | *"The eighth settlement path (`SR-04`…)"* | `55_` SDD-F-01/02: it is P05's path 5 of 7 | **STALE** | Dependency register | **REPAIR** |
| `R-09` | 8 generation gap | `40_` | :69 | **CURRENT** | — | *"The only deployment evidence available is from **Odoo 19** … a material fraction of this package is scoped to a superseded line."* | `51_` overturns it; `18_`:184 and `46_`:74 carry the narrowing | **STALE — and this is the PRIMARY `B-44` blocker row** | Blocker register | **REPAIR** |
| `R-10` | 8 generation gap | `42_` | :53 | **CURRENT** | — | same, unqualified | same | **STALE** | Veto recheck | **REPAIR** |
| `R-11` | 8 generation gap | `24_` | :42 | **CURRENT** | — | *"**the single most consequential fact in this file**"*, unqualified | same | **STALE** | invisible to the declared pattern `only deployment evidence` | **REPAIR** |
| `R-12` | 3 evidence base | `56_` | :68, :70, :78 | **CURRENT** | — | *"filtered tree, 3 declared modules"* · *"filtered-tree-bounded"* · *"the filtered-build risk"* | `REV-E-16`: relocation, not filtering | **STALE terminology on live scope qualifiers** | The file that *produced* the correction still labels its own scope column with the superseded term | **REPAIR** |
| `R-13` | 9 population | `46_` | :124 | **CURRENT** | *(round-6 wording)* | *"re-executed … → **63**, ids `B-01`…`B-63`"* | that command returns **65**; `B-64`/`B-65` are defined at `40_`:234-235, inside its own glob | **DEFECTIVE — on a line round 6 edited**; the same sentence separately says "65" | Severity register | **REPAIR** |
| `R-14` | — tally | `34_` | :51 | **CURRENT** | *(round-6 wording)* | *"10 SETTLED · 4 CONTESTED · 3 UNOWNED · 3 OPEN · 1 HOLD"* — sums to **21** | the table has **20** `F-` rows | **DEFECTIVE — on a line round 6 edited.** Two different columns summed into one tally | Ownership register (P11-bound) | **REPAIR** |
| `R-15` | 5 eighth door | `34_` | :57 vs :81 | **CURRENT** | — | *"A **fifth** settlement door"* (`CPO2-F-02`) vs *"an **8th** path emits none"* (same finding id) | `55_`:66 withdraws "eighth" | **INTERNAL CONTRADICTION, one file, one finding id** | Ownership register | **REPAIR** |
| `R-16` | 4 `is_matched` | `52_`, `62_` | :55, :35 | **CURRENT** | — | *"two set `True` **unconditionally** with no statement (`:444`, `:450`)"* | correct at **site** granularity; `:450` is configuration-gated at **branch** granularity | **NARROWED — not false; unit undeclared**, as `25_`:67 was until round 6 declared it | — | **REPAIR (unit note only)** |

## 4. Challenger claims that DID NOT reproduce — refuted, per §9

| Challenger claim | Re-check | Verdict |
|---|---|---|
| **B5** — *"`34_`:88 F-16 row reads UNOWNED/SETTLED, contradicting `34_`:101"* | **F-16 is at `34_`:44, not `:88`.** Line 88 is a different row ("Bank event identity"). `34_`:44 reads `UNOWNED` and `:101` says *"accepted into P11's matrix but with no owning process yet"* | **REFUTED — the cited lines are wrong and the contradiction does not exist.** A manufactured finding |
| **Class 3** — *"`41_`:35, :101, :113 are stale CURRENT statements"* | `41_` is the round-3 AAS-03 **challenge record**. `:35` *"Amendment applied"* and `:113` a numbered amendments table are records of what was amended then; `:101` is that challenge's findings table | **REFUTED — HISTORICAL.** Correct to leave |

**`ICC-F-01` — Two of sixteen challenger findings were wrong, and one of them was wrong in the direction of accusing the package.** This is the second time this round an audit instrument has produced a false positive (`VER-E-03` was the first). **§9's requirement to re-check before adopting is not ceremony: adopting the verifier wholesale would have published a fabricated contradiction about `F-16`.**

## 5. Findings

**`ICC-F-02` — Every confirmed survivor was invisible to the pattern the package declared for its class.** Not one is a reasoning failure:

| Class | Declared pattern | What it cannot see |
|---|---|---|
| 3 | `filtered distribution\|filtered build\|filtered tree` | **the hyphenated form** — `filtered-build`, `filtered-tree` (9 lines) |
| 5 | `eighth settlement door\|eighth door` | **the ordinal variants** — *"eighth ingestion/settlement door"*, *"eighth settlement path"*, *"an 8th path"*, *"a fifth settlement door"* |
| 2 | `unpublished\|not published` | **the paraphrase** — *"P01 absent"* |
| 8 | `only deployment evidence` | **the synonym** — *"the only available deployment evidence"* (`24_`:42) |
| 9 | `population at G02 close` | **the header** — *"Blocker population"*, *"with 55 blockers"* |

**Round 6 diagnosed phrase-scoping as the governing defect (`PROP-F-02`) and then committed it in nine more places.** That is the third consecutive round to commit the defect it had just named.

**`ICC-F-03` — Three of the fourteen survivors sit on lines round 6 itself edited** (`R-13`, `R-14`, and `R-06`'s file). **A repaired line is not a repaired file, and a repaired file is not a repaired claim.**

**`ICC-F-04` — The population is a floor, not a population, and this is the finding that decides terminality.** Round 6 published *"53 current statements"* as the denominator of the correction surface. That figure was derived from the same phrase-scoped patterns it criticised. **Three consecutive passes each found new members of classes previously declared COMPLETE.** No pass has yet produced a population that a later pass did not enlarge. **§13 condition 3 — *"no material stale/incorrect current claim survives"* — is therefore not establishable by this method**, independently of how many repairs are applied.

**`ICC-F-05` — Two claim classes reproduce cleanly and should be recorded as such.** Class 6 (`res.config.settings` ACL — re-verified against `base/security/ir.model.access.csv:129`) and class 7 (`ir.sequence` re-issuable) have **one CURRENT statement each, both correct**. Class 1 (`X-08`) has **11 CURRENT statements, all consistent, none claiming closure** — the `X-08` family is the one surface both prior rounds got completely right.

**`ICC-F-06` — `REV-E-19` was never applied as an inline marker anywhere.** The round-5 family is `REV-E-18`/`20`/`21` only; `REV-E-19` (the undeclared third reference tree) exists as narrative in 7 places. **Not a defect** — it was an evidence-base note, not a statement correction — but the marker family is 3, not 4, and any count keyed on 4 ids is keyed on a set with an empty member.

**`ICC-F-07` — The `****` rendering repair is the one self-reported repair claim that fully reproduces.** Two occurrences remain, both inside backtick code spans in the verification register quoting the defect it describes. **Zero unrepaired instances.**

---

## 6. Stage 3 — AAS-03 challenge on the CHANGED SURFACES ONLY (§9)

Run after the 21 `REV-E-23` repairs. Scope: the 14 files changed this round, and nothing else.

### Expert 1 — Leader Functional Design
**SUPPORTED.** The `X-08` family (11 CURRENT statements) is the one surface three rounds have got entirely right; it needed no repair and got none. `R-06`'s repair resolves a contradiction *inside one file seven lines apart* and now states both units.
**CONTRADICTED.** Nothing in the changed set.
**NARROWED.** `R-04`/`R-05` rewrite handover sentences that were **true when written**. Marking them time-bounded is right, but the package now contains handover statements from four rounds with four different totals; a reader still has to know which round they are in.
**MISSING EVIDENCE.** None.
**EXACT CLAIM/FILE.** `18_`:214, `70_`:108.
**MATERIAL? NO** — the repairs are sound; the residual is a structural property of a multi-round package.

### Expert 2 — Leadership Database Design
**SUPPORTED.** `R-14` is now derived from the Disposition column by mechanical count (20 rows: 10/4/2/3/1), not from narrative. `R-02`/`R-13` replace printed results that disagreed with their own printed commands.
**CONTRADICTED.** Nothing.
**NARROWED.** `R-13`'s repair states that *"a printed command and a printed result date differently"* — true, and it means **every register in this package that prints a command with a result carries a latent future defect.** Four such pairs exist.
**MISSING EVIDENCE.** No one has enumerated the command/result pairs.
**EXACT CLAIM/FILE.** `13_`:94, `46_`:124, `G02_CLOSURE/P06_EVIDENCE_MANIFEST_G02.md`:63-73.
**MATERIAL? NO for this round; YES as a standing hazard** — routed, not executed.

### Expert 3 — Lead Integration & Localization
**SUPPORTED.** All six outbound artefacts measure zero stale current statements after repair. `13_`:103, a **false factual assertion about a git remote**, is gone.
**CONTRADICTED.** **`VER-F-08`/`PROP-F-04` of the prior round, which certified `18_` clean.** It was not, and the certification was scoped to what the round already knew.
**NARROWED.** Publication status is corrected everywhere; **intake is not performed anywhere.** Nine peer packages are published; P06 has consumed eight and never P01. The outbound wording is now true and the inbound gap is unchanged.
**MISSING EVIDENCE.** None in scope. Consuming P01 is forbidden here.
**EXACT CLAIM/FILE.** `18_`:169, `13_`:103, `P06-OQ-124`, `P06-OQ-128`.
**MATERIAL? NO after repair** — but the certification failure it exposes is why `AASP-VETO-07` stands.

### Expert 4 — Lead Code & UI Architect
**SUPPORTED.** `R-06` re-executes against `account_payment.py:447-449` exactly: `True` **only if** `journal_id.default_account_id in liquidity_lines.account_id`. `25_`:60-67 is the model the rest of the package should follow — **guard column and assignment column side by side, so both units are visible in one row and neither can be misquoted.**
**CONTRADICTED.** **`VER-E-05`, in this round's own output.** `P06-B-66` was cited in the tool-defect register while `40_` had no Appendix C — an orphan identifier created by the round enforcing the orphan-identifier rule. Caught only because the authoritative recount returned 66 against a standing authority of 65.
**NARROWED.** `REC-E-01`: the executor declared the surface frozen and then wrote its own Stage-1 records into the audited root. No claim file was touched, but the verifier had to detect and exclude the directory itself.
**MISSING EVIDENCE.** None.
**EXACT CLAIM/FILE.** `G02_RECOVERY_2026_09_06/P06_VERIFICATION_TOOL_DEFECT_REGISTER.md`:54; `40_` Appendix C.
**MATERIAL? YES, and both are self-caught and repaired** — recorded because a round that hid its own two defects would not be worth reading.

### Dissent preserved
Experts 1 and 3 hold the changed surface is sound and the residual risk is structural. **Expert 2 holds that every printed command/result pair is a latent defect and none has been enumerated. Expert 4 holds that a round which produced two of its own defects (`VER-E-05`, `REC-E-01`) has not demonstrated the discipline it is certifying.** No expert recommends discharging `AASP-VETO-07`.

## 7. §13 decision test, applied

| Condition | Met? |
|---|---|
| Frozen population reproduced independently | **YES** — 30/15 and 40/20 both reproduce; the frozen SHA was mismatched and classified first |
| All current hits in affected claim classes audited | **YES** for the nine declared classes, under widened patterns |
| **No material stale/incorrect current claim survives** | **NOT ESTABLISHABLE.** Three consecutive passes each enlarged a population previously declared complete. `ICC-F-04` / `P06-B-67` |
| Correction propagation internally consistent | **YES after repair** — measured, all nine classes |
| Changed surfaces survive fresh challenge | **PARTIALLY** — two self-caught defects (`VER-E-05`, `REC-E-01`) |
| Verification tools themselves validated | **YES, and five defects were found in them** (`VER-E-01`…`05`) |
| **Independence actually demonstrable** | **NO** — §1 |

### `AASP-VETO-07 — NOT DISCHARGED`
Two conditions fail outright. **Discharge is not recommended, and it is not close.**
