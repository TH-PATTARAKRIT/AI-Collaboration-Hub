# P08_INDEPENDENT_CORRECTION_VERIFICATION_REGISTER

Prompt `[SMEPLUS-26-09-06-P08-R2R-INDEPENDENT-EXTERNAL-CORRECTION-VERIFICATION-003]` · prompt commit `f9099c0`
**Frozen audit surface: `00ccd663d55d72830c8e0db46e4cc1aa345d0af1`** — proven below, not assumed.
Verification branch: `audit/p08-independent-verifier-2026-09-06-001`. **The source branch was not modified.**

---

## 0. INDEPENDENCE — stated before any finding, because the Boss must weigh it

`AAS+-PS-VETO-01` C-6 requires *an independent pass over this round's corrections*, on the rule that **a party that made material errors and authored their repairs cannot certify them.**

**This verifier satisfies that rule in some respects and not in others, and says so rather than claiming clean independence.**

| Independence dimension | Status |
|---|---|
| Fresh session, fresh context, **fresh clone** | **YES** — a new clone was taken; no working state from the audited session was inherited |
| Read the package **only at the frozen SHA**, as evidence under audit | **YES** |
| **Re-derived from primary evidence** rather than from the package's tables | **YES** — including re-extraction from the original database dumps rather than the audited party's intermediate extracts |
| Four fresh challengers, reporting before seeing each other | **YES** |
| **A different actor from the one that authored the repairs** | **NO — and this is the limitation.** The verifying agent is the same model, and within this execution retains knowledge of having authored the corrections under audit |

> **`IVR-IND-01`. The structural independence C-6 demands is NOT fully met.** What is met is procedural independence: fresh context, frozen surface, primary re-derivation, adversarial challenge, and a standing instruction to treat the package as untrusted. **Whether that is sufficient to discharge C-6 is a Boss decision, not a verifier decision, and this register does not treat C-6 as discharged.**

## 1. Stage A — the frozen surface, proven

| Check | Result |
|---|---|
| Frozen SHA resolves | `00ccd66` — *"P08 Phase-S: challenge record, AAS+ consolidation, PMO review, resume state"*, 2026-09-06T13:27:33+07:00 |
| Frozen SHA **is** the tip of the source branch | **YES** — `origin/research/account-p08-record-to-report-2026-09-04-001` = `00ccd663d55d72830c8e0db46e4cc1aa345d0af1` |
| Audit branch's copy of the package is byte-identical to the frozen SHA | **YES** — `git diff 00ccd66 HEAD -- <package>` is empty |
| Package size at the frozen SHA | **72 artefacts** (`.md`), of which **67** are numbered Layer-1 files |

## 2. Stage A — the correction population, enumerated not assumed

**ENUMERATION.** POPULATION: all 72 `.md` artefacts at `00ccd66`. PATTERN: regex `P08-CONTRA-\d+` over the full text of each. PATH SET: the frozen package directory. UNIT: **one distinct correction id**. POSITIVE CONTROL: the contradiction register alone yields 43 ids, so the extractor reads. FAILURE CONTROL: a fabricated id returns zero matches.

| | Count |
|---|---|
| Distinct correction ids in the package | **74** |
| Ids attributable to the round under audit (`-43` … `-74`) | **32** |
| Ids with a definition-bearing statement somewhere | **32 of 32** |
| **Ids present in the contradiction register `17`** | **43 of 74** |
| **Ids ABSENT from the register that is supposed to enumerate them** | **31**, of which **26 are from the round under audit** |

### `IVR-F-01` · MATERIAL · The correction register does not enumerate the corrections, and points at a table that does not contain them

Register `17` carries a **single catch-all row**: *"`P08-CONTRA-48` … `-74` — **27 further contradictions** … Full table in `61` §2."*

**Verified: `61` contains 12 distinct correction ids and its §2 table has 10 rows.** The promised full table does not exist. **15 of the 27 ids the row names are enumerated in no table anywhere.**

**This is the defect the same round recorded as `P08-CONTRA-45` (an identifier defined but missing from its register) and `P08-CONTRA-47` (families with no roll-up) — repeated, in the same commit, on the correction family itself.**

### `IVR-F-02` · MATERIAL · Four incompatible totals are published for one population, and the veto condition inherits the ambiguity

| Where | Statement | Implied |
|---|---|---|
| `61` §5 | *"Material corrections adopted **20** (`-48` … `-74`, excluding the five reviewer errors)"* | 20 |
| `60` | *"Defects caught only by challenge **20** — `P08-CONTRA-48` … `-74`"* | 20 over a 27-id range |
| `17` | *"**27 further contradictions**"* | 27 |
| `62` §5 | *"**Twenty of the twenty-five** corrections came from challenge"* | 25 |
| `63` | *"Corrections applied **25**"* | 25 |
| **Enumerated by this verifier** | ids `-43` … `-74` | **32** |

**Two defects, not one.**

1. **No published total is derived by enumeration**, in a package whose own standing rule is *totals are unverified claims — enumerate, never assert*.
2. **The subtraction that produces "20" is a unit error.** The "five reviewer errors" are *reviewer-claim adjustments* recorded in `61` §3; they are **not** members of the `-48`…`-74` id population. Subtracting one unit from another is the conflation the package records as a standing lesson.

**And it reaches the veto.** `62` C-6 gates the terminal state on *"an independent pass over the **20** corrections"*; `63` §5 states the same condition as *"the **25** corrections"*. **The condition that decides the terminal state does not have a determinate population.** A verifier cannot certify completeness against an undetermined denominator, and this verifier does not.

## 3. Stage D — corrections applied by appending, with the standing tables left contradicting them

**This is the round's dominant residual defect class. Four instances, each verified.**

### `IVR-F-03` · MATERIAL · The domain-purity register still publishes its superseded result and its superseded disposition

`55` §5 (appended) establishes the audit covered **22 of 64** artefacts, that **12 further artefacts match its own pattern unaudited**, that **five more contaminations** (`K-1`…`K-5`) and **five over-routings** exist, and that a **twelfth** adjacent domain was missing.

**§4 — the standing table a reader takes as the result — was never updated.** At the frozen SHA it still reads:

| `55` §4, unchanged | Verifier's corrected value |
|---|---|
| Artefacts audited **22** | 22 **of 64** |
| Contaminated and re-scoped **2** | **at least 7** (2 + `K-1`…`K-5`) |
| Adjacent domains with a declared boundary **11** | **12** |
| **Disposition: `DOMAIN PURITY PRESERVED`** | **the exact conclusion §5.1 says cannot be drawn** |

### `IVR-F-04` · MATERIAL · The Candidate pack updated the count it thought of and left the count its own correction invalidated

`54` §5 publishes **CANDIDATE INPUT 11**. `54` §6.2, appended, names **eight further input classes** and states in terms: *"`P08-CONTRA-60`. The Candidate INPUT inventory is a floor, not a census."*

The **HANDOFF** count in the same table **was** updated (12 → 14). **The INPUT count, which the correction actually invalidated, was not.**

### `IVR-F-05` · MATERIAL · The closure register's per-question dispositions contradict its own corrected summary

`53` `CQ-P08-12`, corrected, publishes **"Named `UNRESOLVED` items: 1"**.

The per-question disposition lines, uncorrected, still claim:

| Question | Disposition line still says | Fact |
|---|---|---|
| `CQ-P08-03` | *"with one named `UNRESOLVED`"* | its `UNRESOLVED` was **closed adversely** by `-62` |
| `CQ-P08-04` | *"with two named `UNRESOLVED`"* | one was narrowed to an exclusion by `-49`/`-50` |
| `CQ-P08-07` | *"one `UNRESOLVED`"* | **closed** by `-51` |
| `CQ-P08-08` | *"one named `UNRESOLVED`"* | **closed** by `-74` |

**Five claimed against a corrected summary of one, and three of the four sections contain the very correction that closed the item they still claim.**

### `IVR-F-06` · MATERIAL · The output-boundary artefact's disposition still names a closed unresolved

`57`'s standing disposition reads *"with one named `UNRESOLVED` (the deployed reporting module)"*. That item was **closed as `P08-CONTRA-74`, a fabricated blocker**, in the same round — and the correction sits in the same file.

> **`IVR-M-01`. A correction appended below a standing table does not correct the standing table.** The round's own method register carries this lesson; the round then produced four instances of it in six artefacts. **A reader taking each artefact's summary at face value receives the pre-correction package.**

## 4. Stage B — veto lifting conditions, verified independently

**No condition is discharged automatically. Only evidence-supported conditions are marked satisfied.**

| Condition | Verifier finding | Status |
|---|---|---|
| **C-1** predicates published in executable form beside each result | Deferred to the reproducibility challenge; the package itself does not claim it | **NOT SATISFIED** |
| **C-2** three-way reachability status on every control | The package **states the requirement** in `56` §2 prose; **no artefact publishes a three-column status table** | **NOT SATISFIED** |
| **C-3** version marker on every row, verified to a published pass rate | **Re-derived at the frozen SHA: 52 of 307 table rows carry a marker — 16.9%.** `57` carries **0 of 26**. The package's own figure (47 of 299) was measured before its final edits and is itself stale | **NOT SATISFIED** |
| **C-4** purity audit re-run over all 64 artefacts with a pattern the author did not derive | **Never re-run.** `55` records the failure and leaves §4 asserting the old result — `IVR-F-03` | **NOT SATISFIED** |
| **C-5** the 19.0 source line read | **Confirmed present on the host** (`/…/SMEsPlus19/SOURCE_CODE /addons_enterprise`, 1,428 modules). **Not read by P08** | **NOT SATISFIED** |
| **C-6** an independent pass over the corrections | Performed procedurally by this verifier; **structural independence not met** (`IVR-IND-01`); **and the condition's own population is indeterminate** (`IVR-F-02`) | **NOT DISCHARGEABLE AS WRITTEN** |

**`AAS+-VETO-01`** (inherited, 2 conditions) — **both remain undischarged**; C-1 above is one of them.
**Four expert vetoes from the audited round** — no lifting condition is evidenced as met.

## 5. What the verifier confirms in the package's favour

Stated because a verification that reports only defects is as misleading as one that reports none.

- **The frozen surface is exactly what it claims to be.** SHA proven, tip proven, package byte-identical on the audit branch.
- **Every correction id in the round has a definition-bearing statement.** None is a bare assertion.
- **The superseded wording is quoted rather than silently replaced** wherever a correction was applied in place — the package's claim to that effect holds on inspection.
- **The round's self-reported failures are real and were not softened.** `55` §5, `53` `CQ-P08-12` and `63` state the package's own defects in stronger terms than a defensive author would.
- **`P08-U-18` was not narrowed by assertion**, and the package refused to claim search authority it did not have.

## 6. Verifier disposition on the correction surface

| Claim class | Verifier disposition |
|---|---|
| Correction enumeration and totals | **MATERIAL DEFECT — `IVR-F-01`, `IVR-F-02`** |
| Standing tables vs applied corrections | **MATERIAL DEFECT — `IVR-F-03` … `-06`** |
| Veto lifting conditions | **0 of 6 satisfied; C-6 not dischargeable as written** |
| Independence | **PROCEDURAL ONLY — `IVR-IND-01`, Boss decision** |
| Substantive claim classes 1–9 of the mandate | see the challenge record and the claim-class register |

---

## 7. A live uncorrected error, and how it survived

### `IVR-F-08` · **MATERIAL — the most consequential finding of this verification**

The frozen package states, in **two** artefacts:

> *"**38 posted entries have every line zero in both frames** — posted, final, and with no financial effect."* — `53`, marked `FACT VERIFIED`
> *"**38 posted entries have every line zero in both frames** … **CONFIRMED.** The reviewer counted 36; the author counts 38 on its own zero test."* — `48`

**Independently re-derived by this verifier, from the deployed extract, in exact Decimal arithmetic:**

| Predicate | Posted entries |
|---|---|
| every line zero in the **reporting frame** (debit + credit) | **38** |
| every line zero in **both frames** (reporting **and** transaction amount) | **36** |

**CONTROL:** the two predicates return different values, so the test discriminates. **POPULATION:** 169,143 posted entries, all carrying lines. **UNIT:** one posted entry.

> **The claim is CONTRADICTED. 38 is the reporting-frame-only count. The sentence says "in both frames", and the both-frames count is 36. The number answers a different question than the sentence asks.**

**How it survived is the finding.** The package records that a challenger reported **36** and that the author **preferred its own 38**, then marked the row **`CONFIRMED`**. **The discrepancy was closed by preferring an instrument, not by testing which predicate matched the claim's own wording.** Neither party's number was wrong as a measurement; the author's number was attached to the wrong sentence.

**The correct figure appears nowhere in the frozen package.** A challenge finding that was received, recorded, and adjudicated was then **lost**, and the erroneous form was published twice — once as `FACT VERIFIED`.

> **`IVR-M-03`. When two parties disagree on a count, the resolution is to test which predicate matches the claim's wording — not to prefer an instrument.** The audited round diagnosed predicate error as its own dominant failure mode across four artefacts, and then committed it in the act of adjudicating a challenger who had it right.

### `IVR-F-07` · MATERIAL · "Not one arithmetic error was found" does not survive the package's own record

`61` §1, `50` and `62` §5 each state that four independent re-derivations found **no arithmetic error**, and `51` uses it as the ground for not escalating beyond hold.

**Contradicted on the package's own text and on re-derivation:**

| | |
|---|---|
| A settlement population published as **63,779** and corrected in `53` to **63,782** | an arithmetic correction, applied |
| An asymmetry published as **175×** in `46`, derived from **rounded** percentages; the underlying counts give **182×** | an arithmetic imprecision, **still live** |
| **`IVR-F-08` above** | a numeric claim, **still live and wrong**, in two artefacts |

**The headline is CONTRADICTED**, and it is load-bearing: it is the sentence the package uses to argue that only its interpretation layer failed. **Its measurement layer failed too — less often, and at least once in a way that is still published.**

---

## 8. The period-absence repair — verified false inside the set it retreated to

### `IVR-F-09` · **MATERIAL — this defeats `P08-CONTRA-68`**

The audited round re-scoped *"there is no accounting-period object"* to *"…in the declared 18.0 root set"*. **Independently verified: the re-scoped form is false inside that set, and it is refuted twice.**

| Evidence, read directly in the declared 18.0 tree | |
|---|---|
| A **persisted fiscal-year model** — `name`, `date_from`, `date_to`, `company_id`, **all `required=True`**, plus an `@api.constrains` forbidding overlapping years | present in the accountant module of the declared root set |
| A **period resolver** returning `{date_from, date_to}` for any date | present in **core accounting** — i.e. **not** an enterprise-only object — and overridden in the accountant module to search the fiscal-year records first |
| Company-level fiscal-year boundary fields, **`required=True`**, defaulted to 31 / 12 | present in core accounting |

**And it is refuted on the deployment.** Re-derived across all three databases: **89 of 89 companies carry a populated fiscal-year boundary, every one of them `('31','12')`.** A period definition is supplied on every deployed company with no configuration act.

**`58` §2 row 4 hands P11 *"a period to reconcile within — absent"*. That is wrong on the merits for the consumer, not merely out of scope.**

### `IVR-F-10` · **MATERIAL — a previously-applied correction was regressed**

**This is the most serious finding of the audit.** The package **already contained the correct wording, installed by an earlier independent review**, and the Phase-S round re-published the sentence that review had removed.

| Artefact | Text at the frozen SHA |
|---|---|
| `01A` `RS-A-02` | *"**No period object carrying state, closure, or a link to an entry exists.** (Re-worded after independent review. **The draft published the unqualified sentence 'no accounting-period entity exists', which its own close model contradicts**: a named, dated, owned fiscal-year entity **does** exist…)"* |
| `09` `PC-04` | *"**No period object carrying state, closure, or a link to an entry exists.** A named, dated, owned fiscal-year entity **does** exist in 13 of the 22 roots **including the target root** — it simply carries none of those things."* |
| `29` | *"Re-worded after review — **the pattern never supported the broader sentence the draft published.**"* |
| Layer-2 `E00` | the instrument was a **model-name census** on two period name forms — which cannot speak to a fiscal-year object under a different name |

**The qualifier that made the claim true — *carrying state, closure, or a link to an entry* — was dropped.** Phase S then "corrected" the resulting falsehood by **narrowing the root set** instead of **restoring the qualifier**, which is why the narrowed form is still false.

> **`IVR-M-04`. A correction can be regressed by a later round that never reads the register recording it.** The package now carries **both** forms of one claim: the qualified, true form in `01A`, `09` and `29`, and the unqualified, false form in `33`, `45`, `46`, `52`, `53`, `57` and `58`. **The false form is the one on the outbound artefacts.**

## 9. Structural defects in the outbound pack

### `IVR-F-11` · MATERIAL · A malformed outbound row to P11

**Re-derived by cell count.** `54` §4's header declares **8** cells. Thirteen of fourteen rows carry 8. **`HO-02` — *"What P11 must reconcile, and what the ledger cannot supply for it"* — carries 7.** The Scope column is lost and every value after it shifts by one. It is an outbound row to P11.

### `IVR-F-12` · MATERIAL · The PMO compliance statement is false for two of four tables

`63` §1 certifies `54` as *"11 / 10 / 9 / 14 **with all ten mandated columns**"*. **Re-derived header cell counts:**

| Table | Header cells | Mandated |
|---|---|---|
| CANDIDATE INPUT | **10** | 10 ✓ |
| PROCESS | **9** | 10 ✗ |
| CANDIDATE OUTPUT | **10** | 10 ✓ |
| **CANDIDATE HANDOFF** | **8** | 10 ✗ |

**The certification fails for two of four tables, including the outbound one — and the item counts it certifies (11/10/9/14) are themselves the counts `IVR-F-04` shows to be stale.**

---

## 10. Findings adopted from the four challenges, each re-derived by the verifier

| ID | Finding | Verifier's own check |
|---|---|---|
| `IVR-F-15` | **The capability denominator reads the wrong column, and its predicate is falsified.** `7 / 75` rests on a per-company code-override map; account-to-company scoping lives in a separate relation table **neither party extracted** | **Extracted it from the original dump.** One 19.0 database alone shows **11 companies holding accounts, not 3**. And a **posted entry's company appears in no charted set under either instrument** — so the capability set does not contain the history set. **The one-line control `history ⊆ capability` was never run** |
| `IVR-F-16` | **A figure with no referent shipped to P11.** `58` §1 publishes *"at 1e-7 the answer is 3"* | **Re-derived in exact Decimal: 0 unbalanced at 0.005, 1e-4, 1e-7 and exact equality**, on both computed and stored balance. The package names its own float instrument as the cause in the same sentence and ships the number anyway |
| `IVR-F-17` | **A token count published as an existence status.** `56` §2 states the retention control has *"ZERO occurrences in the declared 18.0 source tree"* and is **UNREACHABLE** | **Verified: it exists in that tree under a different name, in 52 files** — and the package's **own Layer-2 quarantine cites it at two line numbers**, while an **earlier round already recorded it as present**. The newer name was searched against the older tree |
| — | The withdrawn *"every non-sale document"* wording | **Enumerated: live in six further locations**, including the outbound handoff to three peers and the previously published handoff pack |
| — | **Extract integrity** | **Discharged.** A challenger re-extracted all 21 tables from the original dumps: **byte-identical, 21 of 21**, once a restore-tool nonce line is excluded. The provisional caveat in §2 of the instrument register is lifted for those tables |
| — | The fourth, unread database | **Explained, not excluded.** Its archive format is newer than the restore tool on this host — **a cheap, liftable blocker**, not an unbounded search |

**And one method result that changes how the denominator round should be read:** across **six** defensible eligibility predicates the numerator is **0 in every one**. **Two rounds of denominator correction could not have changed any conclusion** — while the denominator itself is unstable, swinging from 75 to 34 journals on one added posting precondition, with no sensitivity note published.

## 11. Verifier's overall disposition

**TERMINAL STATE `B` — `P08 INDEPENDENT VERIFICATION FOUND MATERIAL DEFECT — TARGETED REPAIR REQUIRED`.** Full reasoning, the 17 material defects, the veto table and the 10 bounded repair requirements are in `P08_INDEPENDENT_VERIFICATION_TERMINAL_REPORT.md`.

**No veto is discharged. No repair was performed on the source package. The source branch was not modified.**

---

## 12. Late inbound after freeze — handled, verified, and **not** allowed to change the audit

### `IVR-INB-01` — provenance and handling

A challenger from **the audited round** (not from this verification) delivered a late addendum **after** the surface was frozen at `00ccd66` and after this verification closed. It reports two second-form re-executions and one new cross-link.

**Handling, stated before the content, because the discipline matters more than the finding:**

| | |
|---|---|
| Does it change the frozen surface? | **No.** The audit is of `00ccd66`; the surface is unchanged and unmodifiable by this track |
| Does it change the terminal state? | **No.** State `B` rests on 17 material defects, none of which this touches |
| Does it change any veto or lifting condition? | **No** |
| Is it recorded and routed? | **Yes** — as an input to the bounded repair requirements |

**A finding that arrives after a freeze is evidence for the next round, not a silent amendment to the closed one.** It is recorded here in full rather than folded into the audit body.

### `IVR-INB-02` · MATERIAL as a repair input · The FX consequence and the numbering defect describe the same four entries, and the package connects them nowhere

**Re-derived by the verifier.** The four posted entries that constitute **the entire measured consequence of the transaction-currency invariant gap** are:

| Entry | Journal | Journal code | Date | Number prefix matches its own journal? |
|---|---|---|---|---|
| `DEPRE2024010033` | 3 | `MISC` | 2024-01-19 | **no** |
| `DEPRE2025030145` | 3 | `MISC` | 2025-03-26 | **no** |
| `DEPRE2025040116` | 3 | `MISC` | 2025-04-21 | **no** |
| `DEPRE2025040117` | 3 | `MISC` | 2025-04-25 | **no** |

**All four are members of the 4,995-entry mis-prefixed population** that the numbering finding measures — verified by set membership.

**The package routes these to two unrelated places.** The FX row sends the consequence to the platform rate master; the numbering row is a separate process entry whose collision question the round left open. **Neither cites the other**, and the same four rows are the whole evidential basis of one of them.

### `IVR-INB-03` — the verifier's refinement: shared **population**, not a demonstrated shared **mechanism**

The addendum states that whether the overlap is coincidence or common cause is undetermined. **The verifier tested it, and can narrow it one step without over-claiming.**

| | |
|---|---|
| Posted entries | 169,143 |
| Depreciation-numbered posted entries | 21,291 — **12.59%** |
| — of which sit in the general journal (the mis-prefixed ones) | **4,154 — 2.46% of posted** |
| — of which sit in their own journal | 17,137 |
| Depreciation share of the whole mis-prefixed set | **83.2%** |

**Under a random draw, four entries all falling in a 2.46% subpopulation has probability ≈ 4 × 10⁻⁷. The overlap is not chance.**

**But it is explained by a shared population, and that is as far as the evidence goes.** Both defects concentrate in one machine-generated class — depreciation entries routed into the general journal. That is consistent with a single bulk generation run that both mis-numbered its entries and mishandled their foreign-currency legs, **and the verifier does not assert it.** `SUPPORTED INTERPRETATION`; a shared mechanism is **UNRESOLVED — SPECIFIC EVIDENCE REQUIRED**.

**Routed as bounded repair requirement 11** — *see the correction note below; requirements 1–10 are unchanged*: when the FX row and the numbering row are re-issued, each must cite the other and state the shared population, so a consumer is not told that four entries evidence one defect while the same four evidence another.

### `IVR-INB-04` — a second late inbound, and it **narrows** a repair requirement

Same provenance and same handling as `IVR-INB-01`: **after the freeze, changes nothing in the audit, changes no veto, changes not the terminal state.** Recorded because **a verifier must record a narrowing as carefully as a widening** — a requirement that shrinks on evidence is as much a finding as one that grows.

**The transaction-currency count of 4 is now confirmed under five independent predicate forms**, three from the challenger and **two written by this verifier**:

| Form | Selects on | Result |
|---|---|---|
| challenger, procedural | per-entry accumulation with a company-currency flag, synthetic-injection control | 4 |
| challenger, set-based A | currency cardinality = 1 and that currency is foreign | 4 |
| challenger, set-based B | no company-currency line exists **and** some currency group does not net | 4 |
| **verifier, form C** | **currency cardinality = 1 and foreign, bucket non-zero** | **4** |
| **verifier, form D** | **no company-currency leg **and** some bucket off** | **4** |

**All five select the same four entries.** Forms C and D are *different conditions* — one keys on how many currencies an entry uses, the other on whether a company-currency counter-leg exists — so their agreement establishes that the four entries are **single-currency *and* counter-leg-free**, not merely one or the other.

**DISCRIMINATING CONTROL, run by the verifier:** entries that **do** carry a company-currency counter-leg alongside a non-netting foreign bucket number **1,847**, and **neither form selects any of them**. The instrument separates the defect population from the exculpated one rather than merely returning a small number.

**Consequence — the repair requirement shrinks.** The published correction's *count* (4) and its *mechanism* (the other 1,847 carry a legitimate company-currency counter-leg) are both **sound**. **The only defect in that row is the cause clause** — *"all from a 1:1 rate fallback"* — which is false for the entry whose five legs sit at an implied rate of ≈35.4 with a 0.04 residue, and imprecise for the other three, whose defect is a foreign-flagged line carrying **no transaction amount** — a missing-amount defect, not a rate fallback.

**Bounded repair requirement 11 is therefore narrowed:** withdraw and replace the **cause clause only**. The count and the exculpation need no rework. **Requirement 2 — the figure with no referent in the outbound handoff — is a different defect, is unaffected, and stands.**


---

## 13. `Q-P08-03` — correction to this register's own cross-reference

Executed 2026-09-07 under Boss authorization `PHASE-S/Q-BOSS-01` (`1bf9b40`), queue item `Q-P08-03` (`3291210`). Pointer-only, `RC-07`: **no fresh challenge required.**

### 13.1 What was wrong

Two lines of this register routed the FX cause-clause repair to *"bounded repair requirements **2 and 4**"* and to *"**requirement 2**"*.

**Neither requirement carries the FX row.** Terminal-report requirement **2** is *"delete the '3 at 1e-7' from the P11 handoff and re-run every balance measurement in exact arithmetic"* — which the same paragraph then says *"is unaffected and stands"*, so it cannot also be the requirement being narrowed. Requirement **4** is the capability denominator. **The FX cause-clause repair was not among the ten numbered requirements at all.**

### 13.2 The correction

**A new requirement 11 is added. Requirements 1–10 are NOT renumbered** — they are cited elsewhere, and the queue row prohibits it.

| # | Bounded repair requirement | Owner |
|---|---|---|
| **11** | **Withdraw the FX cause clause *"all from a 1:1 rate fallback"* and replace it with the per-entry cause:** one entry is a rounding residue of 0.04 across five legs at an implied rate of ≈35.4; the other three carry a foreign-flagged line with **no transaction amount**, which is a missing-amount defect and not a rate fallback. **The count of 4 and its 1,847-row exculpation are sound under five predicate forms and are NOT re-opened.** When re-issued, this row and the entry-numbering row **must cite each other** and state the shared population — all four entries are depreciation-numbered entries in the general journal, and all four are members of the mis-prefixed population | **P08 — source** |

### 13.3 Scope discipline observed

- **The existing ten requirements are unchanged**, in number and in text.
- **The narrowing itself is not re-opened** — it is sound, and the queue row prohibits re-opening it.
- This item required **no fresh challenge** (`RC-07`) and **is complete on execution**.
