# P09_FINAL_BOUNDED_COMPLETION_REGISTER

**Prompt:** `SMEPLUS-26-09-06-P09-P2A-FINAL-BOUNDED-COMPLETION-004` · **PHASE S** · **AI EOS = OFF**
**Layer:** 1 — clean-room. Evidence identifiers resolve in Layer 2 (`E04`); the instruments themselves are stored under `LAYER2_AUDIT_QUARANTINE/INSTRUMENTS/`.

> ## ⚠ CORRECTED AFTER FOUR INDEPENDENT CHANGED-SURFACE CHALLENGES
> **31 findings; all re-verified against source before adoption.** Two conclusions of this round were **contradicted** — one against P09 and one **in P09's favour**. Corrections are inline; superseded wording is retained. Full record: `P09_AAS03_FINAL_CHALLENGE_RECORD`.

---

## 0. BASELINE FREEZE — EXECUTED BEFORE ANY EDIT

| Step | Result |
|---|---|
| local HEAD recorded | `b7bf546` |
| authoritative remote read | `a10c5ad` — **not equal** |
| **delta classified before proceeding** | remote ahead by **exactly one commit adding only this prompt file**; **no P09 artefact touched; zero local divergence** — a safe fast-forward, not a divergence |
| working tree | **clean** |
| package frozen at | **`a10c5ad`** — 121 files |
| **manifest integrity at freeze** | 120 rows over 121 files, **0 checksum mismatches**. *(Corrected: the one uncovered file is the manifest itself, which cannot checksum itself. The exclusion is now named rather than left to inference.)* |
| prior settled findings and negative controls | **preserved unchanged** |

---

## 1. THE EIGHT ACTIONS — DISPOSITION

| # | Action | Disposition |
|---|---|---|
| **K-1** | re-publish the population from a controlled instrument | **COMPLETE — instrument ACCEPTED, headline reproduced, three sub-counts corrected** |
| **K-2** | raw-SQL bounded scan | **THE SCAN RAN; ITS MATERIALITY RESULT IS WITHDRAWN.** The file and module counts stand. The *"materiality is zero"* finding was produced by a predicate that **cannot fire** and is **withdrawn**; corrected value is **1 of 12** |
| **K-3** | relational-reference bounded pass | **COMPLETE — floors corrected upward; material residue is 4 non-test files, 3 already published** |
| **K-4** | re-state `CI-05b` at the report-cell unit | **COMPLETE** |
| **K-5** | `CO-02b` row + `CH-09` tombstone | **COMPLETE — withdrawn text preserved, not overwritten** |
| **K-6** | `CH-06` disposed per component | **COMPLETE — four components, four separate dispositions, no compression** |
| **K-7** | establish the generation basis | **CONTRADICTED — CORRECTED, AND CLOSED IN P09'S FAVOUR.** Generation **IS** establishable in-root: **series 18.0, Enterprise edition.** The deployment rungs remain held |
| **K-8** | reconcile the plan-line field count | **COMPLETE — resolved AGAINST the author's own figure** |

**CORRECTED TALLY AFTER CHALLENGE: six closed, one closed in P09's favour after being wrongly held, one materially defective.**

| | |
|---|---|
| closed and survived challenge | `K-1`, `K-3`, `K-4` *(with one mechanism sentence narrowed)*, `K-5` *(with three defects)*, `K-6` *(with one component regressed)*, `K-8` *(with two rows still mis-united)* |
| **closed in P09's favour after being wrongly held** | **`K-7`** — a challenger found the in-root marker the author's probe set missed |
| **materially defective** | **`K-2`** — its materiality result is an artefact |

---

## 2. K-1 — THE POPULATION, REPRODUCED RATHER THAN CARRIED FORWARD

The instrument was rebuilt from scratch by parsing each file's **syntax tree** rather than matching text. That removes all three prior defect classes *by construction* — a keyword argument cannot collide with a class-body assignment; list position and line breaks are irrelevant to a parsed list; and ownership is evaluated per class body.

**Coverage: 13,515 source files parsed, 0 unparseable. Unit, explicit: the file.**

**Nine controls, eight positive and one negative — all hold, including the three defect classes and the multi-line case that shipped last round.** Only then was the count treated as evidence.

| Measure | Result | Against the prior round |
|---|---|---|
| population | **52 files / 29 modules** | **reproduced** |
| **owning** | **10 files / 3 modules** | **reproduced — unchanged through three instruments and two challenge rounds** |
| extending | **42 files / 27 modules** | module count **corrected** (was 26) |
| allocation-mixin extenders | **11** | **corrected** (was 10) |
| plan-column-mixin extenders | **4** | **corrected** (was 1) |

**The headline held; three sub-counts did not.** The prior figures came from a line-regex, and the mixin counts were understated because those inheritances sit inside lists — the same defect family, one layer down.

---

## 3. K-2 — THE RAW-SQL BLIND SPOT IS REAL, MEASURED, AND IMMATERIAL

| Measure | Result |
|---|---|
| files reaching a P09 table by raw SQL | 15 |
| **outside the population** | **12** — reproduced exactly |
| modules involved | **10** — **corrected**; the prior "3" counted modules *entirely absent*, not modules involved |
| modules entirely absent from the population | 3 — reproduced |

> ~~**Of the 12 files outside the population, ZERO touch a planning model.**~~ → **CORRECTED: ONE of the 12 does.**
>
> **The zero was an artefact.** The classifier tested **dotted model prefixes** against **underscored table names**; no table name could ever match, so the predicate returned zero **on every possible input**. The file it missed — the report-engine file — reaches **both** second-family tables by raw SQL, and it is the same file this register names in §4 as a K-3 material residue and documents in §6 as `CO-02b`'s mechanism. **The round published a fact and its negation in three places and closed K-2 on the half that was never measured.**

**`FC-01` IS WITHDRAWN.** Its reasoning — *a blind spot can be populated and still be immaterial to the claims it was raised against* — remains a sound distinction in principle, and the substantive exposure is already published under `CO-02b`. **But the evidence offered for it does not exist, so the finding cannot stand.**

**`FC-06` (replaces it) — K-1 carried nine controls; K-2 and K-3 carried none, and the defect landed exactly there.** Controls must travel with every filter in a round, not only with the instrument the round was named after.

---

## 4. K-3 — THE REFERENCE BLIND SPOT, MEASURED AND ENUMERATED

| Measure | Result |
|---|---|
| files referencing a P09 model without declaring or inheriting it | 193 |
| **outside the population** | **170 files / 52 modules** — **corrected upward** from 164 / 51 |
| **touching a planning model** | **10** |
| of those, **test files** | **6** |
| **non-test, material** | **4** |

Of the four: **three are already published findings** — the elevated inward read from the commitment carrier, the reverse relation from the account master, and the report engine's consumption point. **One is new and minor**: a project-side reference to the plan line, carrying no new mechanism.

**`FC-02` — NARROWED AFTER CHALLENGE.** The **planning** residue is enumerable and enumerated: four non-test files. **It is not *the* completeness residue.** Of the 170 files outside the population, only the **10** touching a planning model were assessed; **160 were assessed against nothing** and bear on P09's non-planning completeness claims. Stated as *"the completeness residue"*, it over-closed by 160 files.

**And the six test files were set aside with no stated basis.** *"Test file"* was used as a materiality criterion; two of the six concern the committed/achieved and theoretical behaviour P09's own handoffs turn on. **A test can be the only written statement of an inter-domain contract.** `exclusion needs authority` — the set-aside is recorded as unjustified pending a statement of what those tests assert.

---

## 5. K-4 — `CI-05b` RESTATED AT THE REPORT-CELL UNIT

**Superseded wording (retained):** *"the account-keyed intended amount — intent for one specific account on a single date."*

**Restated:**

> **`CI-05b` — a report-cell budget entry.** The input is a **`(value, account, window)` triple entered in a report cell.** The consuming report decomposes the window into one stored row per month. **The increment applied is a delta share** — computed once for the whole window against the sum of rows already present, then divided across months — **but the stored row's amount is a running accumulation**, not a delta against anything.

*(Corrected after challenge: the earlier wording called the stored amount a delta. The conclusion it protects is unchanged and in fact stronger — **no stored row corresponds to any user-entered value at all.**)*

| Guard against generalisation | Statement |
|---|---|
| unit | the **report cell**. Not the stored row, not the model, not the module, not the domain |
| the stored row's single date | a **derived monthly bucket**, not the period the user expressed |
| the stored row's amount | a **delta share**, so no single row means "the intended amount" |
| direction | written **by the consuming report**, not supplied to it |

**`FC-03` — a report-cell fact is not a model fact.** The earlier wording promoted a cell-level input to a model-level object, which is the unit error this whole correction line exists to eliminate.

---

## 6. K-5 — `CO-02b` ADDED, `CH-09` TOMBSTONED

**`CO-02b` — CANDIDATE HANDOFF. ~~(added)~~ → STATUS CHANGED, NOT ADDED.**

*(Corrected: `CO-02b` was already published in the previous round. This round changed its **status field** to contested while presenting it as a creation, and did not edit the earlier row — leaving **two rows with two statuses in two files**, the very defect this package had already recorded against itself.)*

> ## ⚠ THIS ROW IS SUPERSEDED — `P09-C2`, 2026-09-08
>
> **The authoritative `CO-02b` row is the one published at `L1_L8_BOUNDED_CORRECTION_2026_09_06/P09_L1_L8_CORRECTION_REGISTER.md` §7.** The row below is **revision lineage. It is not current and must not be cited as current.**
>
> **Why this marking exists.** The L-6 correction asserted that *"the earlier ones remain readable in their files as revision lineage and are marked superseded by this register."* **They were not marked.** `RC-01` (`RC01-F2`) found this row still live, still present-tense, at the frozen surface. **A register that says a row elsewhere is superseded has not superseded it — only an edit at the carrying file does that.**
>
> **The deployment wording below is WITHDRAWN.** *"already shipped"* is a **deployment-status claim** and P09 has no deployment evidence for it. The supportable statement is: **present in the source of the declared root, at source generation 18.0 Enterprise.** Source presence is not deployment.

| Field | Value *(SUPERSEDED — lineage only)* |
|---|---|
| what leaves P09 | the **account-keyed plan comparison** |
| consumer candidate | the financial-reporting surface |
| mechanism | ~~consumed as~~ **present in the source of the declared root as** a percent-comparison column via a **temporary table substituted for the ledger row table** **[`P09-C2` — present-tense consumption withdrawn]** |
| P09's position | **P09 RECOMMENDS AGAINST** — this is a **second instance** of the mechanism `AAS+-VETO-02` already stands against, and it is ~~**already shipped**, not proposed~~ **[`P09-C2`, 2026-09-08 — WITHDRAWN. Deployment status is not evidenced; read as "present in the source of the declared root, source generation 18.0 Enterprise".]** |
| status | ~~`CANDIDATE HANDOFF — CONTESTED BY ITS OWN AUTHOR`~~ **SUPERSEDED BY THE `L1_L8` §7 AUTHORITATIVE ROW** — which carries the same status text, so the *status* did not change; **what changed is which row is current** |

**`CH-09` — TOMBSTONE. Withdrawn, not deleted.**

> ### ⚠ THIS TOMBSTONE IS SUPERSEDED — `P09-C5`, 2026-09-08
>
> **The current authority is `L1_L8_BOUNDED_CORRECTION_2026_09_06/P09_L1_L8_CORRECTION_REGISTER.md` §8**, which carries the locator, the successors and the citation enumeration. The tombstone below is retained as lineage, with two of its own statements corrected in place:
>
> 1. **"preserved verbatim" is FALSE and is corrected to "RECONSTRUCTED".** `LC-02` searched for the original and found none: the `CH-09` row was **overwritten in place before it was ever committed**, so no committed original exists to have preserved. **A tombstone whose text cannot be checked against an original is a reconstruction, and calling it verbatim is a stronger claim than the record supports.**
> 2. **the `MISSING EVIDENCE` disposition on the citation enumeration is DISCHARGED** — §8.3 delivers it: **21 occurrences across 11 files**, over a declared path set that includes the shared program root, **four of them outside the P09 package**, with a disambiguation rule separating the bare token from the prefixed `ACC-R-` / `INV-R-` / `JNT-R-` families.
>
> **Why this marking exists at all.** Both corrections were published in a later register and **neither was applied here**. `RC-01` found the same pattern at `CO-02b` and `CH-09`; it is the package's recurring shape — **a correction recorded in a revision log is not a correction to the text that carries the claim.**

> **Withdrawn text, ~~preserved verbatim~~ → RECONSTRUCTED (`P09-C5`, 2026-09-08 — no committed original exists; see `LC-02`):** *"the three terminal management outputs — attribution, plan consumption, over-plan signal | no one — they terminate with management | correctly terminal; they cross no boundary and need no contract."*
>
> **Reason for withdrawal:** the row conflated *who consumes a figure* with *what boundary the figure crosses*. Two of the three outputs are carried to a peer with a required sign convention, and their value varies with the reading user's company and the reading day's rate. **Terminality survives only for the plan-line over-plan signal.**
>
> **Status: WITHDRAWN.**
>
> **Three defects in this tombstone, adopted from challenge:**
> 1. it **reverses** the previous round's *"`CH-09` is deleted, not renumbered"* **without acknowledging the reversal** — two contradictory dispositions were live simultaneously. Tombstoning is the better practice; the silent reversal is not;
> 2. *"preserved verbatim"* carries **no locator** — a reader cannot check the text against its original;
> 3. it withdraws terminality from two outputs and assigns them **no successor identifier**, so two boundary crossings are left with no owning row. **`CO-01` and `CO-02a` are those crossings** and are hereby named as their own rows pending a successor identifier.
>
> **And the withdrawal creates outbound obligations where a consumer was told none existed, with no enumeration of who cited `CH-09`.** ~~`MISSING EVIDENCE` — a citation enumeration is required.~~ → **DISCHARGED (`P09-C5`, 2026-09-08): the enumeration is published at `L1_L8` §8.3 — 21 occurrences / 11 files / 4 outside the package.**

---

## 7. K-6 — `CH-06` DISPOSED PER COMPONENT

The prior single requirement — *"sign convention, scope, rate source and rate date"* — compressed a mixed result. Decomposed:

| # | Component | Disposition |
|---|---|---|
| **CH-06.a** | **sign convention** | `SUPPORTED` — management amounts carry the opposite sign to the ledger; the requirement stands as written |
| **CH-06.b** | **scope** | `NARROWED — AND ITSELF CORRECTED.` The amount-bearing row carries no company field, **but its parent link is required with cascade to a header whose company is required**, so company is **deterministically recoverable one level up** — reader-*defaulted at creation*, then stored. ~~*"reader-derived, not stored"*~~ would wrongly imply it is unrecoverable. **The real exposure is larger than published:** the second family ships **no record rule at all** (the first family ships company rules on both its models), and its account reference carries **no company check and no constraint** binding it to the header. Correct word: **unconstrained** |
| **CH-06.c** | **rate source and rate date** | `CONTRADICTED as a single pair` — the consumption row set mixes bases: one component divides by the **order's stored rate**, another is the management amount, a third is the plan amount. **Required per component, not per figure** |
| **CH-06.d** | **currency basis of the carrier** | **`CONTRADICTED — CORRECTED. This was a REGRESSION against this package's own evidence.`** The **consumption carrier declares `currency_id`** by inheritance, has its **NOT-NULL constraint deliberately dropped**, and is **populated with NULL** — materially different from, and more dangerous than, an absent field: a currency-aware consumer reads a **NULL currency** rather than failing to find the column. P09 recorded this correctly one round ago as `N-1`. Two carriers were conflated: the **storage row** genuinely has no currency field; the **consumption carrier** does. The component axis is right and genuinely distinct from (c); **the fact published under it was wrong** |

**`FC-04` — a mixed result must not be compressed into one requirement.** `CH-06` as published was satisfiable by a counterparty while still shipping an unreconcilable number.

---

## 8. K-7 — THE GENERATION BASIS: NAMED EVIDENCE HOLD

| Probe | Result |
|---|---|
| manifest version, analytic module | carries **no series** — not a discriminator |
| manifest version, plan module | **none** |
| manifest version, reporting module | **none** |
| release marker governing the declared root | **none** — the only one found governs a **sibling** tree |
| modules with no version string at all | ~~94 of the first 400 sampled~~ → **the sample does not reproduce (83), and its basis was never declared. Full population: 216 of 1,273** — one pass, and stronger than the sample. **A sample was published where a population was available** |

> ### ~~**NOT ESTABLISHABLE**~~ → **CORRECTED: THE GENERATION IS ESTABLISHED — SERIES 18.0, ENTERPRISE EDITION.**
>
> A challenger found two markers **inside the declared root** that the author's probe set never tested: the translation-catalogue headers, which stamp the server series on every module (**18.0 / 18.0+e** here against **19.0 / 19.0+e** in the comparison root — the marker **discriminates the two roots cleanly**), and an **in-root** edition patch establishing the Enterprise edition. The claim that *"the only release marker found governs a sibling tree"* is **false**.
>
> **This is a discharge in P09's favour, found by a challenger and not by the author.**

**The chain, stated exactly and not inferred:**

| Rung | Status |
|---|---|
| **source present** | **YES — this is all P09 has** |
| installed | **NOT ESTABLISHED** |
| configured | **NOT ESTABLISHED** |
| exercised | **NOT ESTABLISHED** — nothing has been executed in any P09 round |
| economically correct | **NOT ESTABLISHED** |

**`FC-05` — CORRECTED AND NARROWED.** The **source generation is established: 18.0 Enterprise.** The remaining rungs are **not**, and a translation header establishes a *source generation*, never a deployment. Every claim derived from this root is a **source-generation-18.0-Enterprise claim**, and the three version-dependent claims are now anchored on that footing while remaining unanchored as to deployment.

**`FC-05` was also violated twice inside its own document** — *"already shipped"* in §6 and *"estate-wide reach"* in §3 are both deployment/estate words sitting under a hold that records `installed — NOT ESTABLISHED`. Both are **withdrawn**; the supportable wording is *"present in the source of the declared root."*

**Still held:** `installed` / `configured` / `exercised` / `economically correct` — closing these needs a deployment's installed-module list, which this prompt forbids acquiring. `UNRESOLVED — SPECIFIC EVIDENCE / AUTHORIZATION REQUIRED`.

---

## 9. K-8 — THE FIELD COUNT, RESOLVED AGAINST THE AUTHOR

Two counts conflicted: **17** (author) and **16** (challenger).

**The challenger is right.** A pattern matching *any* indented assignment returns 17. Anchored to the **class body** it returns **16**. The seventeenth is a **method-local variable** assigned from a date helper — not a field.

| Model file | class-body fields |
|---|---|
| **plan line** | **16** — *published as 17; corrected* |
| plan header | **10** ✓ |
| dimension value | **13** ✓ |
| **fact table** | ~~13~~ → **11**, plus 2 belonging to a **separate mixin model** declared in the same file |
| **second family** | ~~8~~ → **4 + 4 — two independent models**, not one |

~~**Only the plan-line row was wrong**~~ → **CORRECTED AFTER CHALLENGE: three rows were wrong.**

The plan-line row was wrong at the *indentation* unit and is now right. **Two further rows were stated at the FILE unit under MODEL labels** — the fact-table row folded in a separate mixin model declared in the same file, and the second-family row summed two independent models. **The same unit conflation, inside the section whose entire purpose was to eliminate it.**

The original cause stands: *any indented assignment* counted where *class-body field declaration* was meant. **No count was invented; the discrepancy was resolved from the frozen evidence.**

---

## 10. DOMAIN PURITY — NOT RE-OPENED

`PRESERVED at file granularity`, carried forward unchanged. **K-1…K-8 produced no documented material contradiction against it**, so it was not re-opened as a broad question, per §7 of the governing prompt.

Paths that entered another domain during K-2 / K-3 were **stopped at the boundary**; the minimum interface facts retained are those already published, plus the one new minor project-side reference.

**One challenger contested the blanket wording, and the contest is adopted in part.** This package does state implementation detail of a reporting surface — the temp-table substitution and the second family's row-splitting arithmetic. **That is not smuggled adjacent-domain research: the file declaring the second planning family is classified P09-OWNED by K-1**, so reading it is reading P09's own surface. But the sentence *"no adjacent-domain internal was researched"* is too broad for a package that annexes a file inside a reporting module. **Corrected wording: no internal of a domain P09 does not own was researched; the reporting-module file P09 owns was read as P09's own.**
