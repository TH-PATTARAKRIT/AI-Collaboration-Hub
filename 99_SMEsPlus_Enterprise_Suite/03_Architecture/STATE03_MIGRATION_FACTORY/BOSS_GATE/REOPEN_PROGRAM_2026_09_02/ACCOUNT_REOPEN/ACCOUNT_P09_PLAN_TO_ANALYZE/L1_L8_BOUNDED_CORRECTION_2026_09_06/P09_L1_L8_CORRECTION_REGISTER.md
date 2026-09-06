# P09_L1_L8_CORRECTION_REGISTER

**Prompt:** `SMEPLUS-26-09-06-P09-P2A-L1-L8-FINAL-BOUNDED-CORRECTION-005` · **PHASE S** · **AI EOS = OFF**
**Layer:** 1 — clean-room. Evidence in `LAYER2_AUDIT_QUARANTINE/E05`; instruments under `INSTRUMENTS/`.

> ## ⚠ CORRECTED AFTER FOUR INDEPENDENT CHALLENGES
> **35 findings; all re-verified before adoption.** The first publication of this register asserted corrections it had not applied, and published a classifier acceptance the shipped instrument contradicted. **Both are now fixed at the artefacts that carry them, not asserted in prose.** Full record: `P09_AAS03_L1_L8_CHALLENGE_RECORD`.

---

## 0. BASELINE FREEZE AND THE AUTHORITATIVE L-LIST

| Step | Result |
|---|---|
| local HEAD at read | `54cf8b9`; **after the fast-forward, `92de8a1` — the value the freeze actually holds** *(corrected: the first publication recorded only the pre-merge value)* |
| authoritative remote | `92de8a1` — **delta classified before proceeding**: one commit adding only the prompt file, no P09 artefact touched, zero local divergence |
| working tree | **clean** |
| frozen at | **`92de8a1`** |

**§4 compliance — the L-items were taken from the package, not from the prompt's summary.** `L-1`…`L-8` are defined in **`FINAL_BOUNDED_COMPLETION_2026_09_06/P09_CHECKPOINT_REGISTER.md` §3** and repeated identically in that round's `P09_AUTO_RESUME_STATE.md`. Both copies were compared and are **identical**. They are reproduced verbatim in §1 below.

**Nothing was invented, renamed or broadened.** The governing prompt's §5.D lists examples — a `BD-01` wording correction and a generation-basis correction among them — and states that they *"do not expand the authoritative L-list."* **Neither appears in the package's `L-1`…`L-8`, so neither was executed.** `BD-01` remains flagged, untouched and undecided.

---

## 1. THE EIGHT ITEMS, VERBATIM, WITH DISPOSITION

| # | Verbatim definition | Disposition |
|---|---|---|
| **L-1** | *"re-run K-2's materiality with a **table-name** predicate **and its own positive control**; republish the corrected classification"* | **COMPLETE** |
| **L-2** | *"give **K-2 and K-3 control tables** of their own — every filter carries its own controls, not only the headline instrument"* | **COMPLETE ON THE THIRD SPECIFICATION.** The negative control was written three times: v1 tested a property the instrument never claims; v2 drew its witness from the set defined by the property, so it could not fail; **v3 selects the witness independently and asserts only what the strip claims.** All controls are now **inside the instrument that computes the residue** |
| **L-3** | *"restate the `K-1` control row *"declare and inherit"* so it expresses the set-difference rule it actually implements"* | **COMPLETE** |
| **L-4** | *"assess the **160 unassessed K-3 files** against non-planning completeness claims, or state the exclusion's authority"* | **ASSESSMENT COMPLETE; THE AUTHORITY LIMB DOES NOT CLOSE.** Population corrected to **159**. The stated authority was **falsified by the package's own register** — see §5 |
| **L-5** | *"state what the **6 test files** assert before excluding them"* | **COMPLETE — and the exclusion is now qualified** |
| **L-6** | *"reconcile the **two `CO-02b` rows** across two files to one row, one status"* | **COMPLETE** |
| **L-7** | *"give `CH-09`'s withdrawn text a **locator**, name the **successor identifiers** for `CO-01` / `CO-02a`, and **enumerate inbound citations**"* | **COMPLETE — and the locator search returned a finding of its own** |
| **L-8** | *"re-run K-3's declaration-stripping on an **AST** basis in the published artefact (already verified clean by challenge; the published instrument is still line-based)"* | **COMPLETE** |

---

## 2. L-1 — K-2 MATERIALITY, RE-RUN AND REPUBLISHED

**Declared before the result:** unit = the file · denominator = files reaching a P09 **table** by raw SQL, outside the K-1 population · root = the already-declared root, unchanged · inclusion = SQL context keyword + P09 table name · blind spots = non-source carriers, dynamically built table names.

The defect was a **namespace mismatch**: dotted *model* prefixes tested against underscored *table* names. The repaired predicate keeps the two namespaces explicitly separate.

> ### **Corrected result: 1 of 12, not 0 — reproduced independently, and by three challengers.**
>
> **And the correction is now applied at the text that carried the error.** The superseded zero in the prior round's Layer 2 evidence is struck and marked withdrawn in place; it is no longer live anywhere.

| Measure | Result |
|---|---|
| outside the K-1 population | **12** files |
| **touching a planning table** | **1** — the report-engine file, reaching both second-family tables |
| touching only the fact table | **11** |

**`FC-01` remains WITHDRAWN.** The corrected classification is published here and supersedes the zero.

**The fact/negation collision is now removed from current statements.** The package previously asserted *"ZERO touch a planning model"* while, in the same round, naming that same file as a `K-3` residue and documenting its mechanism as `CO-02b`. **The current statement is 1 of 12 everywhere — and that is now true rather than asserted.** The first publication of this register claimed it while editing nothing outside its own directory, so the zero stayed live at its own location. It has now been **struck in place**, and the superseded wording is retained beside the correction.

---

## 3. L-2 — CONTROL TABLES FOR K-2 *AND* K-3

The prior round armoured `K-1` with nine controls and gave `K-2` and `K-3` none. Both now carry their own.

### 3.1 K-2 control table — **CLASSIFIER ACCEPTED**

| Control | Type | Result |
|---|---|---|
| a known planning-SQL file classifies as planning | positive | **HOLDS** |
| a known fact-table-only file classifies as **not** planning | negative | **HOLDS** |
| the fact table alone is not "planning" | negative | **HOLDS** |
| **the predicate fires on the exact table name that broke it** | positive | **HOLDS** |

### 3.2 K-3 control table — **THREE SPECIFICATIONS, AND THE HISTORY IS THE FINDING**

The first K-3 negative control asserted *"a file's own declaration is not counted as a reference"* and **FAILED**.

**Diagnosed rather than patched.** The witness chosen declares the plan header *and legitimately references it elsewhere* — the self-referencing revision links. **The control asserted something the instrument never claims.** The control was wrong; the instrument was not.

**v2 — also wrong, and for a subtler reason.** It asserted *"the declaration statement must not survive"* but drew its witness from the set **defined by that property** ("files with matches before the strip and none after"). **A control whose witness is selected by the property it tests cannot fail.** A challenger caught it; the "29 witnesses" figure was true by construction, not measured.

**v3 — the specification now shipped.** The witness is selected **independently** — the first owning file in the K-1 population, chosen by *declaration* — and the assertion is the only thing the strip actually claims: **the declaration statement's text is removed from the source.** A file may legitimately reference its own declared model; that is not a defect, and v1 wrongly treated it as one.

| Control | Type | Result |
|---|---|---|
| **declaration STATEMENTS removed from the source** *(witness selected independently)* | negative | **HOLDS** |
| a pure reference survives the strip | positive | **HOLDS** |
| a declare-and-reference file keeps its reference and loses its declaration | failure | **HOLDS — now asserted, not narrated** *(the prior publication graded this row by hand; the instrument computed no predicate for it)* |

> **K-3 CLASSIFIER: ACCEPTED — on the third specification, inside the residue-producing instrument.**
>
> **The first publication of this section was wrong in a way that mattered more than the control itself.** The re-specified control lived in a *second* script that computes **no residue**, while the instrument that produced every K-3 number still carried the superseded control, still gated on it, and shipped a stored verdict of **`false`**. Three challengers found it independently: **the classifier published as accepted was not the classifier that produced the numbers.**
>
> **Fixed by merging the control into the producer and re-running**, not by asserting it. Every figure below is from that run.

---

## 4. L-3 — THE K-1 CONTROL ROW, RESTATED

**Superseded wording (retained):** *"declare **and** inherit | positive | must classify as EXTENDS | HOLDS."*

**Defect:** taken literally, any file declaring a P09 model while inheriting *anything* would be excluded from ownership — which would eject the plan line and the plan header, the population's own headline models, from the owning set. The rule the instrument implements is a **per-model set difference**, not a per-file test.

**Restated:**

> **Control — the set-difference rule.** For each class body, ownership is `_name` **minus** the models that same class inherits. A file that declares model *X* while inheriting model *Y* **owns X and extends Y**. A file that declares *X* **and inherits X** owns nothing and extends *X* — the in-place extension case.
> **Witness:** a file declaring the plan line while inheriting the plan-column mixin → **owns the plan line, extends the mixin.** **HOLDS.**

**No count changes.** The rule was always implemented correctly; only its published description was wrong.

---

## 5. L-4 — THE 160, ASSESSED *AND* THE EXCLUSION'S AUTHORITY STATED

**Both limbs of the item were executed, not one.**

**Assessed.** Population corrected from 160 to **159**: one file entered solely on the string `account.analytic.account.id` — **a dotted field path, not a model**. The inclusion rule now requires a literal to be a model **actually declared in the root**, and the K-3 outside-population count falls from 170 to **169**.

The 159 reference the analytic dimension only:

| Model referenced | Files |
|---|---|
| the fact table | 100 |
| the dimension value | 72 |
| the axis | 57 |
| the assignment rule | 11 |
| the obligation rule | 9 |

**Tested against every current non-planning P09 claim:**

| Claim | Can a *reference* disturb it? |
|---|---|
| ownership — 10 files / 3 modules | **No.** Ownership is declaration; reference is disjoint from it |
| extension counts — 17 / 11 / 8 / 7 / 4 | **No.** These count inheritance, a different relation |
| population — 52 files / 29 modules | **No.** The population is *defined* as declare-or-inherit; the exclusion is the population's stated rule, not an oversight |
| "the dimension is written into across the estate" | **No — they corroborate it.** A breadth claim cannot be contradicted by more breadth |
| the six absence claims | **No.** Every one is a *planning* concept; these files are outside that subject by measurement |

**Exclusion authority, now stated rather than assumed:**

> ~~**The 160 are excluded because no current P09 claim is stated over the "references a P09 model" relation.**~~
>
> ### **WITHDRAWN — FALSIFIED BY THE PACKAGE'S OWN REGISTER.**
> Two challengers showed the reversal condition **has already fired**. The prior round publishes, un-withdrawn, *"files referencing a P09 model without declaring or inheriting it — 193"* and *"outside the population — 170 files / 52 modules"*, and **this round re-publishes the same relation**. Those are current P09 claims stated over exactly that relation, so **the 159 sit inside a live published denominator** and the exclusion is **not authorised as written**.
>
> **`L-4`'s assessment limb closes; its authority limb does not.** The honest position: the 159 are *assessed* and disturb no ownership or extension count — but they are **not excludable**, because P09 itself publishes measurements over the relation they belong to.

---

## 6. L-5 — WHAT THE SIX TEST FILES ASSERT

Stated **before** exclusion, per *exclusion needs authority*.

| Test file | What it asserts |
|---|---|
| plan-module common fixture | shared setup; **no test methods** — a fixture, not an assertion |
| plan-module main test | **2 methods** — plan behaviour and the split wizard |
| **committed/achieved test** | **10 methods** — revenue and expense committed/achieved amounts; **an unposted bill on an order**; discount and included tax; **multi-currency**; multiple bills from one order. Docstring: *the committed amount stays correct while an order has an unposted bill; the amount should not be 0* |
| **theoretical-amount test** | **2 methods** — the theoretical amount and its aggregates |
| **second-family report test** | **9 methods** — single and multiple budgets, **comparison period**, date filters, **editing budget items** |
| project-side test | **2 methods** — retrieving budget items |

**The exclusion is now QUALIFIED, not withdrawn.** These tests are **not runtime behaviour and not a deployment**, so they cannot settle any completeness or absence claim — that is the ground for excluding them from the residue. **But they are the reference pattern's own written statement of the committed/achieved and theoretical contracts**, and two of them bear directly on live P09 handoffs: the **multi-currency** case touches `CH-06`'s currency component, and **editing budget items** touches `CI-05b`'s report-cell unit.

> **`LC-01` — the six tests are excluded from the evidence residue as non-runtime, and simultaneously recorded as corroborating a live handoff requirement.** Both statements are true; the earlier round asserted only the first, with no basis given.

---

## 7. L-6 — THE TWO `CO-02b` ROWS, RECONCILED TO ONE

Two rows existed with two statuses in two files. **Reconciled to a single authoritative row:**

> ### `CO-02b` — CANDIDATE HANDOFF (authoritative row)
>
> | Field | Value |
> |---|---|
> | what leaves P09 | the account-keyed plan comparison |
> | consumer candidate | the financial-reporting surface |
> | mechanism | consumed as a percent-comparison column via a temporary table substituted for the ledger-row table |
> | P09's position | **P09 RECOMMENDS AGAINST** — a second instance of the mechanism `AAS+-VETO-02` stands against |
> | **provenance** | **first published in the targeted-correction round; status changed in the final-completion round.** It was **never "added" twice** |
> | status | **`CANDIDATE HANDOFF — CONTESTED BY ITS OWN AUTHOR`** |
>
> **This row supersedes both earlier rows.** The earlier ones remain readable in their files as revision lineage and are marked superseded by this register.

**One word is corrected on the evidence:** the earlier row called the mechanism *"already shipped"*. **That is a deployment-status claim and is withdrawn**; the supportable statement is *"present in the source of the declared root, at source generation 18.0 Enterprise."*

---

## 8. L-7 — `CH-09`: LOCATOR, SUCCESSORS, CITATIONS

### 8.1 The locator — and it returned a finding

**Searched for the original of the text the tombstone published as "verbatim". It does not exist in any committed artefact.**

| Probe | Result |
|---|---|
| the `CH-09` row in the Phase S handoff register **today** | already the **corrected** wording |
| the same row **at its first commit** | **already corrected** — the row was edited **in place before it was ever committed** |
| the distinctive phrases anywhere else in the package | **absent** |
| nearest attested source | a **paraphrase** in the Phase S I/P/O pack: *"three of five outputs are terminal — they end with management and cross no boundary"* |

> **`LC-02` — the tombstone's "preserved verbatim" claim is CORRECTED to "reconstructed".** No committed original exists, because the row was corrected in place before its first commit — **the superseded wording was never preserved at its own location.**
>
> **Locator, stated honestly:** original location `PHASE_S_DOMAIN_PURE_CLOSURE_2026_09_06/P09_CANDIDATE_HANDOFF_REGISTER.md` row `CH-09` — **overwritten in place, no committed original**. Attested paraphrase: that round's I/P/O pack, output-side finding. **Attested reason for withdrawal:** that round's challenge record, finding 13.

### 8.2 Successor identifiers — named

| Withdrawn from `CH-09` | Successor | Status |
|---|---|---|
| management attribution by dimension value | **`CO-01`** | **`CANDIDATE HANDOFF`** — crosses to reconciliation with a required sign convention; value varies with the reading company and rate date |
| dimensional plan consumption | **`CO-02a`** | **`CANDIDATE HANDOFF`** — same grounds |
| the over-plan signal | **`CO-03`** | **terminal for the plan-line instance only** |

**The two crossings now have owning rows.** Previously they had none.

### 8.3 Inbound citations — enumerated

~~**17 citations across 8 files**~~ → **21 occurrences across 11 files. CORRECTED.**

**PATH SET, now declared as a set rather than described:** every `*.md` under `ACCOUNT_REOPEN/`, which includes the P09 package **and the shared program root one level above it**. The first enumeration ran only over the package and reported its own boundary as the world.

| Correction | Detail |
|---|---|
| unit | the first table mixed **identifier** and **phrase** hits while declaring itself identifier-only; two counted rows carry no identifier at all |
| boundary | **four occurrences lie outside the package**, in two shared-root prompt files |
| collision | the bare token collides with three **prefixed** families (`ACC-R-`, `INV-R-`, `JNT-R-`) which are **not** P09 citations; disambiguation rule: a P09 citation is `CH-09` **not preceded by an identifier character** |

Distribution as first published, retained for lineage:

| File | Citations |
|---|---|
| Phase S handoff register | 2 — the row itself and the population correction |
| Phase S I/P/O pack | 1 — the paraphrase |
| Phase S challenge record | 1 |
| targeted-correction I/P/O pack | 1 — *"deleted, not renumbered"* |
| targeted-correction checkpoint + resume state | 2 |
| final-completion register | 5 |
| final-completion checkpoint + resume state | 2 |
| final-completion challenge record + Layer 2 | 3 |

~~**No citation lies outside the P09 package.**~~ **FALSE — four lie outside it**, in the shared program root.

~~**P11 has published no branch.**~~ **FALSE — P11 has published a branch, now at CORR3, and it already consumes P09 artefacts by name**, pinning P09 at `5441f8d`. This was a **peer-state assertion never executed**, and it was the load-bearing half of the exposure conclusion.

> **What survives, and it is narrower than what was published:** across the declared path set, **no peer package cites the `CH-09` identifier** — P11's package returns zero `CH-0x`/`CO-0x` citations on measurement. **So no external consumer closed on the withdrawn terminality.** The broader claim *"no external exposure"* is **withdrawn**; the measured claim replaces it.

---

## 9. L-8 — K-3 STRIPPING ON AN AST BASIS

The published instrument stripped declarations **line by line** — the exact construct the K-1 rebuild existed to remove, one action to the right.

**Re-run with an AST strip that is multi-line aware by construction:**

| Measure | AST strip | Line-based strip |
|---|---|---|
| unparseable files | **0** | — |
| outside the population | **169 files / 52 modules** | **169 / 52** |
| touching a planning model | **10** | **10** |
| test / non-test | **6 / 4** | **6 / 4** |

**Both columns are now EXECUTED.** The first publication printed the line-based column as a **hard-coded literal** — a comparison against a remembered number, not a run. A challenger caught it; the instrument now computes both and compares them.

**The count moved 170 → 169** because the inclusion rule was corrected: a literal counts only if it is a model **actually declared in the root**, which rejects the dotted field path that had been admitted.

> **Identical — and both sides executed.**
>
> **The "by construction" claim is NARROWED on measurement.** The strip handles assignment statements with plain targets; it does not handle annotated, augmented, tuple-target or attribute-target declarations. Those were **enumerated over the whole root and measured at zero occurrences on P09 models**, and a character-range variant of the strip returns identical counts. So the result is safe here — **by a different, now-measured property of this root, not by construction.**

---

## 10. WHAT THIS ROUND DID NOT DO

No new research round. No new root. No widening.

**Purity, stated accurately after challenge.** The earlier sentence claimed *"no adjacent-domain internal researched — at the P09-owned files that carry them."* **The report-engine file is NOT P09-owned** — this round's own measurement places it outside the K-1 population. The supportable statement: **P09 read one adjacent-domain file to the minimum depth needed to classify a K-2 hit and to name the mechanism it carries, and researched no adjacent-domain lifecycle, state machine or internal.** The earlier wording claimed more purity than the work supports. **No Boss decision answered**; `BD-01` untouched. **`AAS+-VETO-04` not discharged by this register** — see its disposition. No Candidate Handoff promoted to a contract. No PHASE SA, PHASE B or PHASE C. **AI EOS = OFF.**
