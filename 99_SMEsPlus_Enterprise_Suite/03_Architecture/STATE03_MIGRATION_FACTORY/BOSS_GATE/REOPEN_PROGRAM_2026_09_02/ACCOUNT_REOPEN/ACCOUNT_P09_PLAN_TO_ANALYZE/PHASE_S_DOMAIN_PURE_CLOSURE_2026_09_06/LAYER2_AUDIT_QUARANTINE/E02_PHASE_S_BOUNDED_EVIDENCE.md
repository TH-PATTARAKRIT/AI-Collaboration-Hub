# E02 — PHASE S BOUNDED EVIDENCE (LAYER 2 — AUDIT QUARANTINE)

**Session:** SMEPLUS-26-09-06-P09-P2A-DOMAIN-PURE-BOUNDED-CLOSURE-002
**Classification:** LAYER 2 — AUDIT QUARANTINE. Boss / PMO / AI-Audit only.
**Prohibition:** no identifier, path, model name or field name in this file may be transcribed into any Layer 1 deliverable. Layer 1 cites `EV-P09-2nn` only.

---

## 0. DECLARED BOUNDED PATH SET

Enumerated, not described. This round did **not** search the estate.

| Root | Path | Modules |
|---|---|---|
| **S1** | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/addons` | 1,273 manifests |

**P09-owned module surface inside S1, selected by name pattern `*budget*` and `*analytic*` at depth 1, then filtered to the P09 domain:**

| Module | Files (`*.py`) | In P09 domain? |
|---|---|---|
| `analytic` | 14 | yes |
| `analytic_enterprise` | 4 | yes |
| `account_budget` | 18 | yes |
| `project_account_budget` | 9 | yes |
| `l10n_be_hr_contract_salary_mobility_budget` | — | **NO — excluded on grounds.** A localisation payroll-benefit module; the token `budget` is a false positive of the name pattern. Excluded by inspection, not by assumption |

**UNIT:** the model declaration and the field declaration — not the word.

---

## 1. EV-P09-200 — MODELS DECLARED IN THE P09-OWNED SURFACE

Command: `grep -rhoE "_name = ['\"][a-z0-9_.]+['\"]" <module> --include="*.py"`

| Module | Models declared |
|---|---|
| `analytic` | `account.analytic.account`, `account.analytic.applicability`, `account.analytic.distribution.model`, `account.analytic.line`, `account.analytic.plan`, `analytic.mixin`, `analytic.plan.fields.mixin` |
| `account_budget` | `budget.analytic`, `budget.line`, `budget.report`, `budget.split.wizard` |
| `analytic_enterprise` | none declared |
| `project_account_budget` | none declared |

Two matches (`complete_name`, `create_date`) are `_name` assignments inside field definitions, not model names. Inspected and excluded.

**Generation note:** the budget surface here is the `budget.analytic` / `budget.line` generation. This is **not** the `crossovered.budget` generation carried by older deployments. Any comparison across generations must state which is meant.

---

## 2. EV-P09-201 — PLANNING-SEMANTIC TERM SWEEP

Population: the four P09-owned modules. Pattern: `\b<term>`, case-insensitive, over `*.py`. Unit: matching line.

| Term | Hits | Disposition |
|---|---|---|
| `budget` | **315** | **POSITIVE CONTROL — the search fires** |
| `plan` | 289 | present |
| `commit` | 77 | present |
| `revision` | 4 | present |
| `version` | 3 | present — 1 is a module-manifest version string, 2 are unrelated |
| **`forecast`** | **0** | NOT FOUND IN SCOPE |
| **`scenario`** | **0** | NOT FOUND IN SCOPE |
| **`target`** | **0** | NOT FOUND IN SCOPE |
| **`variance`** | **0** | NOT FOUND IN SCOPE |
| **`baseline`** | **0** | NOT FOUND IN SCOPE |
| **`simulation`** | **0** | NOT FOUND IN SCOPE |

Second pass, unit = **declaration** (`x = fields.Y(` or `_name = '...x...'`) rather than any occurrence: **zero declarations** for every one of the six absent terms.

**Class B — not found in the declared scope, boundary stated.** The positive control at 315 establishes that the command could have returned a hit. Not class A: the search covers four modules of one root, not the system.

---

## 3. EV-P09-202 — THE VARIANCE NEGATIVE, ESTABLISHED IN THREE INDEPENDENT FORMS

The programme's own standard forbids accepting a zero from one query form.

| Form | Method | Result |
|---|---|---|
| **1** | the word `variance` | 0 |
| **2** | ten synonyms — `difference`, `delta`, `gap`, `remaining`, `deviation`, `over_amount`, `under_amount`, `vs_`, `shortfall`, `surplus` | 0, except `remaining` = 1 (inspected: unrelated) |
| **3** | any arithmetic subtraction between the plan amount and the achieved amount, in either order | **0 — no stored difference is computed anywhere in the surface** |

---

## 4. EV-P09-203 — THE PLAN LINE'S ACTUAL FIELD SET

Command: `grep -rhnoE "^\s+[a-z0-9_]+ = fields\.[A-Za-z]+\(" <account_budget>/models/`

`budget.line` carries: `date_from`, `date_to`, `budget_amount`, `achieved_amount`, `achieved_percentage`, `committed_amount`, `committed_percentage`, `theoritical_amount`, `theoritical_percentage`, `is_above_budget`, `budget_analytic_state`.

`budget.analytic` carries: `name`, `date_from`, `date_to`, `state`, `budget_type`, `is_above_budget`, plus the revision links in §5.

**The comparison vocabulary is three amounts and three percentages of consumption, plus one boolean. There is no difference quantity, signed or unsigned.** (The misspelling `theoritical_` is the field name as shipped; recorded verbatim because a search on the correct spelling returns nothing.)

---

## 5. EV-P09-204 — STATE AND TYPE VOCABULARIES, AND THE REVISION LINK

| Vocabulary | Values |
|---|---|
| plan state | `draft` → `confirmed` (labelled "Open") → `revised` → `done` |
| plan type | `revenue`, `expense`, `both` |

Revision is a **self-referencing pair** on the plan header: a `Revision Of` parent link and a `Revisions` child collection, with a validation raise and a "New revision" action.

**The label and the stored value differ for one state**: the stored value is `confirmed`, the caption reads "Open". Any Layer 1 statement must name the stored value.

---

## 6. EV-P09-205 — THE DECLARED SOURCE ROOT OF THE BASE PACKAGE IS NOT RE-IDENTIFIABLE

The base package declared root `R1` as `<ref-erp>/odoo/addons/` with **790** manifests.

Bounded re-identification attempt, restricted to the reference-ERP tree on the project volume (no estate sweep, no cloud storage):

| Root | Manifests |
|---|---|
| the v18 server root | 636 |
| the v18 addons root (**S1**, used this round) | 1,273 |
| the v18 custom roots | 65 / 57 |
| a v19 root | 1,399 |
| older-generation roots | 127 / 58 |

**No root in the bounded search carries 790 manifests.** Class **B** — not found in the declared bounded scope, boundary stated. **This is expressly NOT a claim that `R1` does not exist**; it is a claim that `R1` cannot be resolved from its own published description within this round's declared path set. The root may lie outside the bounded set, including in locations this round is forbidden to sweep.

**Consequence:** the base package's `R1`-bounded findings are reproducible only by someone who can resolve `R1`. Recorded for `CQ-P09-11` and routed as an evidence item, not as a contradiction of any finding.

---

## 7. EV-P09-206 — GENERATION CONTROL (added after the first draft)

**Why it was run.** The generation of root `S1` is **not established**. Its module manifest string reads `1.1`, which carries no series and is not a discriminator; the only release file found governs a *sibling* root, not `S1`. The model-name set (`budget.analytic` / `budget.line` / `budget.report` / `budget.split.wizard`) is **identical** in `S1` and in an independently-identified later-generation root, so it is not a discriminator either.

**Rather than assert a generation, the identical sweep was run on a second root and the results compared.**

| Root | `budget` | `forecast` | `scenario` | `target` | `variance` | `baseline` | `simulation` |
|---|---|---|---|---|---|---|---|
| **S1** | 315 | 0 | 0 | 0 | 0 | 0 | 0 |
| **S2** — `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/ODOO19/addons` | 395 | 0 | 0 | **1** | 0 | 0 | 0 |

The single `target` hit in `S2` was **inspected, not counted**: it is a user-interface window-action attribute (`'target': 'new'`), not a planning target. **The planning-target absence holds in both.**

State vocabulary — `draft` / `confirmed`("Open") / `revised` / `done` — is **identical in both roots**.

> **Result: the six planning-concept absences and the state vocabulary are INVARIANT across the two generations examined.** Those claims therefore do not depend on resolving `S1`'s generation. Where a claim *does* depend on it, §8 says so.

---

## 8. EV-P09-207 — THE COMMITMENT MEASURE IS GENERATION-SPECIFIC, AND ITS ZERO IS AMBIGUOUS

The generation control surfaced a divergence the author had not looked for.

| Field | `S1` | `S2` |
|---|---|---|
| `committed_amount` (Monetary) | **present** | **absent** |
| `committed_percentage` (Float) | **present** | **absent** |
| `committed` (Float) | present | absent |
| occurrences of `commit` in the plan surface | **77** | **2** |

**FIRST DRAFT SAID "REMOVED". THAT WAS WRONG, AND THE SECOND AND THIRD FORMS CAUGHT IT.**

The two remaining occurrences in `S2` are in the reporting query, and they are decisive:

- `0 AS committed,` — carrying an inline comment naming a **separate purchase-budget module** as the consumer;
- a second branch computing `committed` from the management amount with a sign flip on plan type.

**The commitment measure was not deleted. It was moved out of the core plan surface into a separate, optional module.** In the later generation the core query emits a **literal zero** for committed value unless that module is installed.

**The consequence is the programme's own recurring defect, found inside the P09 surface itself:**

> **A committed figure of zero means either "nothing is committed" or "the module that would tell you is not installed", and the two are indistinguishable on the face of the report.**

`Installed != configured != exercised` applies directly. Second form (nine synonyms: `reserved`, `encumbr`, `obligat`, `pledge`, `ordered_amount`, `open_order`, `po_amount`, `purchase`, …) returns **0** in `S2`, confirming the concept is absent from the core surface under any name — while the hardcoded `0 AS committed` proves it is *expected* to arrive from elsewhere.

**Class A within the two roots read** for the field-presence difference; **class B** for any statement about which module set a given deployment installs.

---

## 9. EV-P09-208 — CORRECTIONS FORCED BY THE AAS-03 CHALLENGES

Every item below was **re-verified against source by the author before adoption**. All are confirmed. Each supersedes the earlier statement in this file; the superseded wording is retained.

### 9.1 The population instrument could not see the surface it enumerated

`EV-P09-200` enumerated models by `_name`. That unit is **structurally blind to extension models** (`_inherit`). Re-run with `_inherit`:

| Module | `EV-P09-200` said | Actually extends |
|---|---|---|
| `analytic_enterprise` | "none declared" | `account.analytic.line` |
| `project_account_budget` | "none declared" | `budget.analytic`, `budget.line`, `project.project`, `project.update` |
| `account_budget` | 4 models | + `account.analytic.account`, **`purchase.order`**, **`purchase.order.line`** |

**A floor was published as an inventory.**

### 9.2 A second budget model family exists in the same root and was never enumerated

`account_reports/models/budget.py` declares **`account.report.budget`** (line 9) and **`account.report.budget.item`** (line 105), the latter carrying `account_id` — **a specific account, not an account type** — plus `amount` and a required `date`. Invisible to a module-name pattern.

**Verified at both line numbers.**

### 9.3 The plan's company field is REQUIRED in this generation

`account_budget/models/budget_analytic.py:53` — `company_id … required=True, default=lambda self: self.env.company`; `budget_line.py:45` stores it `related` on the line.

**This CONTRADICTS** the statement carried in `P09_SCOPE_AND_OWNERSHIP_REGISTER` §2 and `…ACTUAL_PLAN_VARIANCE…` §4 that the plan's company is *"optional; empty matches every company"*. That behaviour belongs to a **different generation** and was carried across without re-verification — the exact cross-generation carry §1 of this file warned against.

### 9.4 `EV-P09-203`'s field census is both over- and under-inclusive

`is_above_budget` occurs **0** times in the header model and 2 times on the line model; the published header set wrongly included it and **omitted `company_id`, `user_id`, `budget_line_ids`** — the omitted `company_id` being precisely the field that falsifies §9.3.

### 9.5 There are THREE over-plan computations, not one

`budget_line.py:46`, `purchase_order_line.py:9`, `purchase_order.py:7`. The purchase-order-line instance is a **prospective, commitment-time** test — `committed + uncommitted > budget`, where uncommitted is derived from un-invoiced quantity.

**Consequence:** the Layer 1 claim that over-plan signalling is *"a displayed boolean that gates nothing"* scoped *"per plan"* is wrong on both count and scope, and **Boss decision `BD-01` is mis-framed**: it offers commitment-time enforcement as a *departure* from the reference position, which already computes exactly that.

### 9.6 The positive control does not fire in half the declared population

| Module | `*.py` files | `budget` hits |
|---|---|---|
| `analytic` | 14 | **0** |
| `analytic_enterprise` | **4 files, one of which is a 12-line model file** | **0** |
| `account_budget` | 18 | 210 |
| `project_account_budget` | 9 | 105 |

All 315 control hits lie in the two budget-**named** modules. **The control demonstrates nothing about the other two**, one of which could not have produced a hit under any pattern.

**This is the author's own `NC-13` — per-artefact positive control — written one round ago and not applied.**

### 9.7 A module named for the concept under test sits in the same root, joined to P09's own fact table

`project_timesheet_forecast/models/project_forecast.py`: `_inherit = 'planning.slot'`; `effective_hours` **stored**; `percentage_hours` ("Progress") **stored**, computed as `effective_hours / allocated_hours * 100`; `timesheet_ids = Many2many('account.analytic.line')`.

**That is an intent / achieved / ratio triple, stored, joined to the management fact table, in a module named `forecast`.** Four `*forecast*` modules exist in the root.

The class-B negatives remain true **within their declared boundary**. What is now established is that **the boundary was drawn by an instrument that cannot see the concept it was asked to test** — the name pattern `*budget*|*analytic*` structurally cannot select a module named `*forecast*`.

### 9.8 The plan and the actual are rendered together

`budget_amount` and `achieved_amount` each appear **6 times** across the plan views, on list, form and pivot, with a decoration predicate comparing them.

**A signed difference is one subtraction of two adjacent, self-summing, simultaneously displayed figures.** The absence claim survives only in its narrow form — *no computed, stored, signed, tolerance-bearing, aggregable variance field* — not in the form published.

### 9.9 Form 3 was described, not published

`EV-P09-202` Form 3 published a description of intent, no command, and **no positive control of its own** — the 315 control is a word-frequency control that cannot show a subtraction-shaped pattern can fire. A genuine control was available and unused (`product_qty - qty_invoiced`, `purchase_order_line.py:50`). Population was `*.py`; the Layer 1 claim said *"computed, stored **or displayed**"*, and the view layer was never in the tested population.

**This is the author's own `declared-pattern-not-run` defect: publish the command and its output, not the pattern.**

---

## 10. EV-P09-209 — SECOND WAVE OF VERIFIED CORRECTIONS

### 10.1 THERE IS A FIFTH PLAN STATE, AND IT CARRIES A DELETION PATH

`budget_analytic.py:30-36` declares **five** values, not four:

`('draft',"Draft") ('confirmed',"Open") ('revised',"Revised") ('done',"Done") ('canceled',"Canceled")`

And `canceled` is not decorative:
- `:74-75` `action_budget_cancel()` sets it;
- `:62-63` `_unlink_except_draft_or_cancel` permits **deletion** of a plan in `draft` **or** `canceled` only.

**Two failures compound here.**
1. `EV-P09-204`, `CQ-P09-07` and the correction register all published **four states**.
2. `EV-P09-206` then asserted the four-state vocabulary **invariant across both generations** — **converting a miscount into a claim of robustness.** A control that re-published the wrong enumeration confirmed the wrong enumeration.

**And the substantive miss is worse than the count:** a *cancelled plan is a deletable plan*. A **destruction path for a management plan** is absent from a register whose entire subject is correction and history.

### 10.2 THE COMMITMENT MEASUREMENT COMPARED TWO DIFFERENT POPULATIONS

`EV-P09-207` reported `commit` occurrences as **77 → 2**. The later root carries a module **`account_budget_purchase`**, which declares `committed_amount` (`budget_line.py:9`) and `committed_percentage` (`:13`) — and it was **not in the population the second half of the comparison was measured over.**

Measured at the same unit on both sides, the later root's plan surface carries **117** occurrences, not 2.

> **The substantive conclusion is CONFIRMED and in fact strengthened** — the measure is carried by a separate, optional module, and the core report emits `0 AS committed` naming that module in a comment. **But the number published to carry it was a mismatched-denominator artefact**, and anyone re-running it at the stated unit gets a different figure.

**This is a denominator error committed inside a control run to catch denominator errors.**

### 10.3 A SECOND LABEL/VALUE DIVERGENCE, IN THE SAME SURFACE

`analytic/models/analytic_plan.py:299-301` — the applicability object's business-domain field stores `'general'` and captions it `'Miscellaneous'`. `EV-P09-204` reported **one** divergence; a systematic scan of every selection declaration in the four modules returns **two**.

### 10.4 THE PACKAGE WAS BEING REWRITTEN WHILE UNDER CHALLENGE

One challenger recorded that `E02` grew from 125 to 174 lines and a Layer 1 register from 111 to 150 lines **between its first and second reads**, and that its findings are stated against the intermediate text.

**This is a genuine process breach and it is the author's.** The programme's rule is that a package is **frozen before review opens**. The additions were the generation control (§7–§8) — good work, wrongly timed. **A challenge conducted against a moving target cannot state what it reviewed**, and one challenger correctly declared that `NOT DECIDABLE` rather than guessing.

### 10.5 SELF-INCONSISTENCY IN THE GENERATION CONTROL'S OWN SUMMARY

`EV-P09-206`'s prose says *"five of the six absences are invariant"* while its own table shows **all six** invariant. Corrected: **all six absences are invariant across the two roots**; the item that diverges (the commitment measure) is **not an absence**.
