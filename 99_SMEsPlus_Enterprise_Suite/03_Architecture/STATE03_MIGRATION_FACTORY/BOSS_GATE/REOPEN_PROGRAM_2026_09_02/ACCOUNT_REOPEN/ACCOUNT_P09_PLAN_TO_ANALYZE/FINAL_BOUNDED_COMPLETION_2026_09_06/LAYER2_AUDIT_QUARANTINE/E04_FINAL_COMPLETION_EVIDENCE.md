# E04 — FINAL BOUNDED COMPLETION EVIDENCE (LAYER 2 — AUDIT QUARANTINE)

**Session:** `SMEPLUS-26-09-06-P09-P2A-FINAL-BOUNDED-COMPLETION-004`
**Classification:** LAYER 2 — AUDIT QUARANTINE. Boss / PMO / AI-Audit only.
**Prohibition:** nothing here may be transcribed into Layer 1. Layer 1 cites `EV-P09-4nn`.
**Frozen baseline:** `a10c5ad` · package 121 files · manifest 120 rows · **0 checksum mismatches at freeze**

---

## 0. DECLARED ROOT — UNCHANGED

`S1 = /Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/addons`. **No new root. No estate, volume or cloud sweep.**

---

## 1. EV-P09-400 — K-1: THE INSTRUMENT, REBUILT AND CONTROLLED

**Not copied forward.** The population was re-derived from scratch by a **Python AST parse**, which removes all three prior defect classes by construction:

| Prior defect | Removed how |
|---|---|
| `D1` — `comodel_name=` read as a declaration | a keyword argument is a different AST node from a class-body assignment; it cannot collide |
| `D2` — declare-and-inherit read as ownership | ownership rule applied per class body: `_name` minus `_inherit` |
| `D3` — list position / multi-line | list elements are parsed, not matched; position and line breaks are irrelevant |

**Coverage:** `13,515` source files parsed. **Unparseable: 0.**
**UNIT, explicit: the FILE**, counted once regardless of how many P09 models it touches.
Script: `scratchpad/k1.py`; machine-readable output `scratchpad/k1_population.json`.

### 1.1 Controls — the instrument was not treated as evidence until all passed

| Control | Type | Expected | Result |
|---|---|---|---|
| plan header file | positive | OWNS | **HOLDS** |
| fact-table declaring file | positive | OWNS | **HOLDS** |
| second planning family | positive | OWNS | **HOLDS** |
| non-first list position × 3 | positive | EXTENDS | **HOLDS** |
| **multi-line list** | positive | EXTENDS | **HOLDS** |
| declare **and** inherit | positive | must classify as EXTENDS | **HOLDS** |
| **`comodel_name`-only reference** | **negative** | must be **absent** | **HOLDS** |

> **INSTRUMENT: ACCEPTED.**

### 1.2 Result

| Measure | K-1 (accepted instrument) | Prior round | Status |
|---|---|---|---|
| population | **52 files / 29 modules** | 52 / 29 | **REPRODUCED** |
| owning | **10 files / 3 modules** | 10 / 3 | **REPRODUCED** |
| extending | **42 files / 27 modules** | 42 / **26** | **module count CORRECTED** |
| fact-table extenders | **17** | 17 | reproduced |
| allocation-mixin extenders | **11** | **10** | **CORRECTED** |
| plan-column-mixin extenders | **4** | **1** | **CORRECTED** |
| dimension value / obligation rule | 8 / 7 | 8 / 7 | reproduced |

**The headline reproduced; three sub-counts did not.** The prior figures were produced by a line-regex; the mixin counts were understated because those inheritances sit in lists.

---

## 2. EV-P09-401 — K-2: RAW-SQL BOUNDED PASS

Pattern: `(FROM|JOIN|INTO|UPDATE|TABLE|EXISTS)\s+["']?<P09 table>` over the declared root, ten P09 table names.

| Measure | K-2 | Prior floor | Status |
|---|---|---|---|
| files hit | 15 | — | — |
| **outside the population** | **12 files** | 12 files | **REPRODUCED** |
| modules involved | **10** | **3** | **CORRECTED — the prior "3" counted modules *entirely absent*, not modules involved. A unit conflation in the prior round's own figure** |
| modules entirely absent from the population | **3** | 3 | reproduced |

The three entirely-absent modules are a cash-basis reporting module, a timesheet-attendance module and a timesheet-holidays module.

### 2.1 Materiality — the decisive result

> ~~**Of the 12 files outside the population, ZERO touch a planning model.** Every one reaches only the analytic fact table.~~
>
> ### **WITHDRAWN AND SUPERSEDED — the corrected value is 1 of 12.**
> The predicate that produced this zero compared **dotted model prefixes** with **underscored table names** and could not fire on any input. One of the twelve — the report-engine file — reaches **both** second-family planning tables by raw SQL. Corrected under `L-1`; see `L1_L8_BOUNDED_CORRECTION_2026_09_06`.

~~**K-2 therefore closes without disturbing any planning completeness or absence claim.**~~ **WITHDRAWN with the zero above.** The raw-SQL blind spot is real, populated, and measured at **1 of 12**.

---

## 3. EV-P09-402 — K-3: RELATIONAL-REFERENCE BOUNDED PASS

Pattern: any P09 model named as a string literal, **after stripping declaration and inheritance lines** so the pass measures *reference* only.

| Measure | K-3 | Prior floor | Status |
|---|---|---|---|
| files hit | 193 | — | — |
| **outside the population** | **170 files / 52 modules** | 164 / 51 | **CORRECTED upward** |

### 3.1 Materiality

**10 of the 170 touch a planning model. Six are test files.** The four non-test files:

| File | Planning model referenced | Already in the package? |
|---|---|---|
| the commitment-carrier file | the plan line | **YES** — this is the `sudo()` inward read already recorded |
| the account master file | the second family's item | **YES** — the reverse relation already recorded |
| the report engine file | the second planning family | **YES** — the consumption point already recorded |
| a project-side plan file | the plan line | **NEW — minor**; a producer-side reference, no new mechanism |

> **The material residue of K-3 is four non-test files, three of which are already published findings, and one new and minor.**

---

## 4. EV-P09-403 — K-8: THE PLAN-LINE FIELD COUNT, RECONCILED

Two counts were in conflict: **17** (author) and **16** (challenger).

**Resolved from the frozen evidence — the challenger is right.**

A line-anchored pattern matching *any* indentation returns 17. Restricting to **exactly four-space indentation — the class body** — returns **16**. The seventeenth match is at eight-space indentation **inside a method**: a local variable assigned from a date helper, not a field.

| File | class-body fields |
|---|---|
| plan line | **16** *(was published as 17)* |
| plan header | 10 ✓ |
| second family | 8 ✓ |
| fact table | 13 ✓ |
| dimension value | 13 ✓ |

**Only the plan-line row was wrong.** Cause: a unit error — *any indented assignment* was counted where *class-body field declaration* was meant.

---

## 5. EV-P09-404 — K-7: THE GENERATION BASIS CANNOT BE ESTABLISHED

Tested inside the declared root:

| Probe | Result |
|---|---|
| manifest version string, analytic module | `'1.1'` — **carries no series**, not a generation discriminator |
| manifest version string, plan module | **none** |
| manifest version string, reporting module | **none** |
| release marker governing the root | **none** — the only one found governs a *sibling* server tree, not this root |
| modules in the root carrying no version string at all | **94 of the first 400 sampled** |

> **The generation of the declared root is NOT ESTABLISHABLE from the declared root.**

### 5.1 The evidence chain, stated exactly

`source present` — **YES, this is all P09 has.**
`installed` — **NOT ESTABLISHED.** No module list from any deployment is in evidence for this root.
`configured` — **NOT ESTABLISHED.**
`exercised` — **NOT ESTABLISHED.** Nothing was executed in any round.
`economically correct` — **NOT ESTABLISHED.**

**No deployment status is inferred from source presence anywhere in this package.** Every P09 claim derived from this root is a **source-presence claim**, and every version-dependent claim inherits this hold.

---

## 6. REPRODUCIBILITY LOCATORS

| Item | Locator |
|---|---|
| K-1 instrument and controls | `scratchpad/k1.py` — root, seeds, ownership rule and all nine controls inline |
| K-1 machine-readable population | `scratchpad/k1_population.json` — every file with its owned and extended model lists |
| K-2 / K-3 passes | `scratchpad/k2k3.py`; output `scratchpad/k2k3.json` |
| K-8 reconciliation | four-space-anchored field grep over the five owning model files |
| K-7 probes | manifest version strings of the three owning modules; release-marker search over the root |

**Any verifier can repeat every count above from the frozen package and the declared root.**

---

## 7. EV-P09-405 — CORRECTIONS FORCED BY THE FOUR CHANGED-SURFACE CHALLENGES

All four experts challenged this round. **Every finding below was re-verified against source by the author before adoption.**

### 7.1 K-2's MATERIALITY RESULT IS AN ARTEFACT — THE PREDICATE CANNOT FIRE

Three of four experts found this independently. The K-2 classifier tests **dotted model prefixes** (`budget.`, `account.report.budget`) against **underscored table names** (`budget_line`, `account_report_budget`). No table name can ever match:

```
"account_report_budget".startswith("account.report.budget")  ->  False   (every case)
```

**The predicate returns 0 on every possible input.** Re-run with a table-name predicate over the frozen output: **1 of the 12, not 0** — `account_reports/models/account_report.py`, reaching **both** second-family tables by raw SQL from outside the population.

**The contradiction was visible in this round's own printed output**, which listed that file two lines above the sentence reporting zero — and in §4, which names the same file as a K-3 material residue, and in `CO-02b`, which documents its mechanism.

> **`FC-01` IS WITHDRAWN.** The substantive conclusion may survive — the exposure is already published under `CO-02b` — but **the evidence offered for it does not.**
>
> **Root cause: K-1 carried nine controls; K-2 and K-3 carried none.** The defect landed exactly where the controls stopped. This is the programme's own *prove-the-filter-can-fire* rule, broken one action to the right of where it was being enforced.

### 7.2 K-7's HEADLINE IS CONTRADICTED — GENERATION *IS* ESTABLISHABLE, IN-ROOT

Two in-root markers the K-7 probe set never tested:

| Marker | Declared root | Comparison root |
|---|---|---|
| `i18n/*.pot` → `Project-Id-Version: Odoo Server …` — analytic module | **`18.0`** | `19.0` |
| same — plan module | **`18.0+e`** | `19.0+e` |
| same — reporting module | **`18.0+e`** | `19.0+e` |
| series distribution across the root | **391 × `18.0+e`, 311 × `18.0`**, max **18.0** | 19.0 |
| `web_enterprise/version.py` — **inside the declared root** | patches the release to the **enterprise** edition | — |

**The marker discriminates the two roots cleanly.** The claim that *"the only release marker found governs a sibling tree"* is false: this one is in-root.

> ### **CORRECTED: the declared root's generation IS established — series 18.0, Enterprise edition.**
> **This is a discharge in P09's favour, and it was found by a challenger, not by the author.**

**What does NOT change:** the remaining rungs. `installed`, `configured`, `exercised`, `economically correct` are still **NOT ESTABLISHED** — a `.pot` header establishes the **source generation**, never a deployment. The three version-dependent claims are now anchored to *source generation 18.0 Enterprise*, and remain unanchored as to deployment.

Additionally, the K-7 sample **does not reproduce**: *"94 of the first 400"* re-executes as **83**, and the sampling basis was never declared. The **full population is 216 of 1,273** manifests carrying no version string — obtainable in one pass, and stronger than the sample. **A sample was published where a population was available.**

### 7.3 `CH-06.d` IS A REGRESSION AGAINST THIS PACKAGE'S OWN EVIDENCE

`CH-06.d` published: *"the **consumption carrier's** figures are plain floats with no currency field."*

Source, at the consumption carrier:
```
2111  CREATE TEMPORARY TABLE ... account_report_budget_temp_aml () inherits (account_move_line) ...
2114  ALTER TABLE account_report_budget_temp_aml ALTER COLUMN currency_id DROP NOT NULL;
```

**The carrier declares `currency_id` (by inheritance), its NOT-NULL constraint is deliberately dropped, and NULL is written into it.** That is materially different from — and more dangerous than — an absent field: a currency-aware consumer reads a **NULL currency** rather than failing to find the column.

**P09 recorded this correctly one round ago** (`N-1`: *"NOT-NULL dropped on currency, move, journal and display type"*). This round regressed against its own published evidence by conflating two carriers: the **storage row** genuinely has no currency field; the **consumption carrier** does.

### 7.4 `CH-06.b` UNDERSTATES — THE SECOND FAMILY IS NOT SCOPED AT ALL

Adopted from challenge, verified: the item's `budget_id` is required with cascade to a header whose `company_id` is required, so **company is deterministically recoverable one level up** — *reader-defaulted at creation, then stored*. "Reader-derived, not stored" would let a counterparty conclude it is unrecoverable.

**And the real exposure is larger than the one published:** the second family has **no record rule at all** — the first family ships company record rules on both its models; the second ships none — and the item's account reference carries **no company check and no constraint** binding it to the header's company. `CH-06.b` should read **unconstrained**, not merely reader-derived.

### 7.5 THE K-8 TABLE STILL MIXES UNITS — IN THE SECTION WHOSE PURPOSE WAS UNIT CONFLATION

Two experts, independently. Verified by AST at the **model** unit:

| Published row | Published | At the model unit |
|---|---|---|
| plan line | 16 | **16 — correct** |
| plan header | 10 | 10 — correct |
| dimension value | 13 | 13 — correct |
| **fact table** | **13** | **11** + 2 belonging to a **separate mixin model** declared in the same file |
| **second family** | **8** | **4 + 4 — two independent models** |

*"Only the plan-line row was wrong"* is **itself wrong**. Two rows remain stated at the **file** unit under **model** labels.

### 7.6 FURTHER ADOPTED FINDINGS

| # | Finding | Status |
|---|---|---|
| **a** | `FC-02`'s *"the completeness residue is four files"* over-closes: only the **10 planning-touching** files were assessed; **160 remain unassessed** against non-planning claims | **NARROWED** |
| **b** | *"6 are test files"* is used as a materiality criterion **with no stated basis**; two of them are about the committed/achieved and theoretical behaviour P09's own handoffs turn on | **NARROWED — exclusion needs authority** |
| **c** | `CO-02b` is presented as **"(added)"**; it was already published last round. Its **status field changed** without editing the earlier row — **two rows, two statuses, two files** | **CONTRADICTED** |
| **d** | The `CH-09` tombstone **reverses** last round's *"deleted, not renumbered"* **without acknowledging the reversal**, gives no locator for the "verbatim" text, and assigns **no successor identifier** to the two outputs whose terminality it withdraws | **CONTRADICTED** |
| **e** | The withdrawal **creates outbound obligations** where a consumer was told none existed, with **no enumeration of who cited `CH-09`** | **MISSING EVIDENCE** |
| **f** | K-1's control row *"declare and inherit → must classify as EXTENDS"* is **mis-stated**; under it the plan line and plan header would be excluded from owning. The set-difference rule is right; the **control wording is not** | **CONTRADICTED** |
| **g** | **K-2 and K-3 carry no controls at all**, and K-3's declaration-stripping is **line-based** — the very construct the AST rebuild existed to remove. *(One expert re-ran K-3 with an AST strip: 0 of the 170 are false positives, so K-3 survives its own worst construction.)* | **MISSING EVIDENCE** |
| **h** | `FC-05`'s universal *"no deployment status is inferred anywhere"* is **violated twice in its own document** — *"already shipped"* and *"estate-wide reach"* | **NARROWED** |
| **i** | Reproducibility locators point into a **session-scoped temporary directory**, not the frozen package; the instruments are **not durably available** | **CONTRADICTED** |
| **j** | §0 records **121 files / 120 manifest rows** without naming the excluded file | **NARROWED — non-material** |

### 7.7 WHAT SURVIVED, INDEPENDENTLY REPRODUCED

| Item | Status |
|---|---|
| **K-1 population 52 / 29; owning 10 / 3; extending 42 / 27** | **reproduced exactly by two experts, one from a scratch-built AST instrument** |
| per-model extension counts 17 / 11 / 8 / 7 / 4 | reproduced exactly, including both corrected mixin counts |
| **13,515 files parsed, 0 unparseable** | reproduced |
| **the seed set** | tested independently against **all 2,050** model strings in the root — **13 in-seed cover every declared analytic/budget model; no gap** |
| the ownership rule | holds in every case, including the three declare-and-inherit files |
| **K-3: 170 / 52 outside, 10 planning, 6 tests, 4 non-test** | reproduced (one expert 169 — both floors, same residue) |
| **K-8 plan line = 16**, the 17th a method-local | reproduced by AST, not only by indentation |
| `K-4`'s unit correction and `FC-03` | *"the strongest item in the package"*; no smuggled model-level claim found |
| residual AST blind spots (`Dict`, `AnnAssign`, augmented/conditional/dynamic declarations) | enumerated and **measured at zero occurrences on P09 models** — immunity is real but **untested by the controls** |
| localization | **no statutory claim, no Thai claim, nothing to place on HOLD** — verified by full grep |
