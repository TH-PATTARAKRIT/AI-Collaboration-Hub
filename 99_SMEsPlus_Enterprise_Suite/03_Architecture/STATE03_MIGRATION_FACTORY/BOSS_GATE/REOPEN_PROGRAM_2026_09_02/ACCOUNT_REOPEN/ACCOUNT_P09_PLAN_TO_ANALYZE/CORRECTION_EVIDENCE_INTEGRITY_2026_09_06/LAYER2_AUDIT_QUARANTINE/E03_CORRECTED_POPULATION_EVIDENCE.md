# E03 — CORRECTED POPULATION EVIDENCE (LAYER 2 — AUDIT QUARANTINE)

**Session:** `SMEPLUS-26-09-06-P09-P2A-EVIDENCE-INTEGRITY-TARGETED-CORRECTION-003`
**Classification:** LAYER 2 — AUDIT QUARANTINE. Boss / PMO / AI-Audit only.
**Prohibition:** no path, model name, field name or method name here may be transcribed into Layer 1. Layer 1 cites `EV-P09-3nn`.

---

## 0. DECLARED ROOT — UNCHANGED, NOT WIDENED

| Root | Path | Manifests |
|---|---|---|
| **S1** | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/addons` | 1,273 (top-level) |

**No new root was introduced.** `S2` (`ODOO19/addons`) is retained only as the generation-comparison root. The base package's unresolved `R1` (790 manifests) remains `UNRESOLVED` and was **not** chased — chasing it would require the estate sweep this prompt forbids.

---

## 1. EV-P09-300 — THE CORRECTED SELECTOR

**Superseded selector:** module name pattern `*budget*` / `*analytic*` at depth 1 → 4 modules.

**Corrected selector — by MODEL, at file granularity:**

```
grep -rlE "_(name|inherit|inherits) *= *\[?['\"](SEED)['\"]" S1 --include="*.py"
SEED = account\.analytic\.[a-z.]+ | analytic\.mixin | analytic\.plan\.fields\.mixin
     | budget\.[a-z.]+ | account\.report\.budget[a-z.]*
```

**Result: 49 files across 28 modules.**

### 1.1 Positive controls — all four objects the name selector provably missed

| Control | Result |
|---|---|
| the enterprise analytic extension module | **SEEN** (1 file) |
| the project-budget module | **SEEN** (2 files) |
| the module carrying the second planning family | **SEEN** (2 files) |
| the module named for the concept under test (`forecast`) | **SEEN** (1 file) |

**All four seen. The instrument is accepted.**

---

## 2. EV-P09-301 — TWO DEFECTS FOUND IN MY OWN INSTRUMENT, BOTH BEFORE PUBLICATION

| # | Defect | How it showed | Fix |
|---|---|---|---|
| **D1** | `comodel_name='…'` **ends in `_name`** and matched the declaration pattern | 3 files reported as declaring a P09 model when they only reference one in a relational field | anchor `_name` at a line-leading word boundary. **Negative control now returns 0** |
| **D2** | the `_name` **+** `_inherit`-of-the-same-model pattern is an **in-place extension**, not a declaration | 2 timesheet files reported as *owning* the management fact model | ownership rule: declares `_name` **and does not inherit that same model** |

**Both were caught by inspecting the suspicious rows rather than by accepting the count.** Uncorrected, D1+D2 would have inflated P09 ownership from 3 modules to 5 and mis-assigned the fact model to a timesheet module.

---

## 3. EV-P09-302 — THE CORRECTED OWNERSHIP SPLIT

| Class | Files | Modules |
|---|---|---|
| **P09-OWNED** — declares a P09 model | **10** | **3** |
| **EXTENDS a P09 model** — producers/consumers writing into P09's surface | **39** | **27** |
| total | **49** | 28 |

**Owning modules:** the analytic module, the plan module, and **the financial-reporting module**.

### 3.1 The prior declaration was wrong in BOTH directions

| Prior "P09-owned" (4 modules) | Corrected |
|---|---|
| analytic module | **OWNS** — correct |
| plan module | **OWNS** — correct |
| enterprise analytic extension | **DOES NOT OWN** — it only extends. Wrongly included |
| project-budget module | **DOES NOT OWN** — it only extends. Wrongly included |
| *(absent)* | **financial-reporting module — OWNS a second planning family. Wrongly excluded** |

---

## 4. EV-P09-303 — OWNERSHIP IS A PROPERTY OF THE FILE, PROVEN IN BOTH DIRECTIONS

This is the correction's central evidence fact.

| Case | Module domain | Contains |
|---|---|---|
| the plan module | **P09** | 2 files (`purchase_order.py`, `purchase_order_line.py`) that extend **purchase-domain** models |
| the financial-reporting module | **R2R** — ~30 files extending report/ledger/partner/company models | **1 file** (`models/budget.py`) that **declares a P09 planning family** |

> **A P09 module contains adjacent-domain files, and an adjacent-domain module contains a P09 file.** Module-level ownership cannot express either. **File-level ownership expresses both.**

---

## 5. EV-P09-304 — THE SECOND PLANNING FAMILY, IN FULL

`account_reports/models/budget.py`

| Model | Line | Fields |
|---|---|---|
| `account.report.budget` | 9 | `sequence`, `name` (required), `item_ids`, `company_id` (**required**, defaulted) |
| `account.report.budget.item` | 105 | `budget_id` (required, cascade), **`account_id` → `account.account`, required** (109), `amount` = **`fields.Float`** (110), `date` (**required**, 111) |

Methods: a name constraint, `create`, `_create_or_update_budget_items(value_to_set, account_id, rounding, date_from, date_to)`, `copy_data`, `copy`.

### 5.1 Measured differences from the first planning family

| Property | first family | second family |
|---|---|---|
| stated against | analytic dimension + account **type** filter | **a specific account, required** |
| analytic dimension | plan columns | **NONE — `analytic` occurrences = 0** *(control: `account` = 16, so the search fires)* |
| period | `date_from` / `date_to` window | **a single required `date`** |
| amount type | `Monetary` | **`Float` — no currency field anywhere in the file** |
| state / lifecycle | 5 values | **NONE** |
| revision lineage | parent/child | **NONE** |
| consumption figures | achieved / committed / theoretical | **NONE on the model** |

### 5.2 Minimum interface fact on how it is consumed — R2R internals NOT researched

`account_report.py:788` sets a **percent-comparison** column to the budget; `:1901` builds a budget option list; `:2079`/`:2092` create a **report budget temporary table**.

**Retained fact only:** *the second planning family is consumed as a plan-versus-actual comparison column via a temporary table substituted into the report.* **The report engine was not researched further.**

---

## 6. EV-P09-305 — THE OVER-PLAN COMPUTATIONS, RE-LOCATED AT FILE GRANULARITY

Three computations, as previously found. Their **file ownership** is now precise:

| File | Declares/extends | Class |
|---|---|---|
| `account_budget/models/budget_line.py` | declares the plan line | **P09-OWNED** |
| `account_budget/models/purchase_order_line.py` | extends `purchase.order.line` | **P09-AUTHORED FILE ON AN ADJACENT-DOMAIN CARRIER** |
| `account_budget/models/purchase_order.py` | extends `purchase.order` | **P09-AUTHORED FILE ON AN ADJACENT-DOMAIN CARRIER** |

**Neither purchase file appears in the model-based population**, because neither declares nor extends a P09 model — they attach P09 semantics to a purchase carrier. **This is the boundary case §6 of the prompt describes**, and purchase internals were **not** researched.

---

## 7. DECLARED BLIND SPOTS OF THE CORRECTED INSTRUMENT

Stated, not hidden.

| # | Blind spot | Class |
|---|---|---|
| **B-1** | a model reached only through a **variable-held name** or raw SQL | **C — not searched** |
| **B-2** | P09 semantics attached to an adjacent-domain carrier **without touching a P09 model** — the purchase files are the known instance; there may be others | **C — the instrument cannot see this class by construction** |
| **B-3** | non-Python carriers (views, data files) | **C — not searched**; the prior round's variance negative was already reduced for this reason |
| **B-4** | roots outside `S1` — including the unresolved `R1` | **B — boundary declared, not chased** |

**B-2 is the honest residue:** a model-based selector solves the name-based selector's blind spot and has one of its own. Neither is complete alone. **The pair is what should be run.**

---

## 11. EV-P09-306 — CORRECTIONS FORCED BY THE AAS-03 CHALLENGES

All four experts challenged the corrected population. **Every finding below was re-verified against source by the author before adoption.** All are confirmed.

### 11.1 THE PUBLISHED POPULATION CAME FROM THE **UNFIXED** INSTRUMENT

§2 declared defect **D1** fixed — *"anchor at a line-leading word boundary. Negative control now returns 0."* **The selector published in §1 carries no anchor**, and the published figure of 49 is its output.

| Selector | Files |
|---|---|
| as published in §1 (unanchored) | **49** |
| anchored, as §2 claims was applied | **48** |

The one differing file is admitted **solely** by `comodel_name=` — the exact D1 class. **The negative control does not return 0; it returns 1.**

**The single self-caught defect offered as evidence of instrument discipline was described and not carried into the artefact.**

### 11.2 A FOURTH DEFECT, WHICH SHIPPED — LIST-POSITION DEPENDENCE

The fragment `\[?['\"]SEED['\"]` matches a list only when the P09 model is the **first** element. Four files inherit a P09 model from a non-first position and were silently absent:

| File | Statement |
|---|---|
| `account_asset/models/account_asset.py:21` | `_inherit = ['mail.thread', 'mail.activity.mixin', 'analytic.mixin']` |
| `hr_expense/models/hr_expense.py:14` | `_inherit = ['mail.thread.main.attachment', 'mail.activity.mixin', 'analytic.mixin']` |
| `mrp_account/models/mrp_workcenter.py:9` | `_inherit = ['mrp.workcenter', 'analytic.mixin']` |
| `project/models/project_project.py:22` | a **multi-line** list carrying the plan-column mixin |

The fourth is invisible to any single-line pattern. **`account_asset` is an entire module absent from the declared set.**

### 11.3 THE CORRECTED POPULATION

A multi-line-aware re-derivation over the whole root (independently reproduced by two experts, one by an AST pass over 13,515 files with zero parse errors):

> **52 files / 29 modules.** Ownership: **10 owning files / 3 modules** *(unchanged)*; **42 extending files / 26 modules**.

**The published 49/28 was wrong in both directions at once** — one false positive from an unapplied fix, four false negatives from a regex shape. Both are the defect class this round exists to eliminate, and **neither was self-caught**.

### 11.4 BLIND SPOT **B-2** WAS MISCLASSIFIED — IT IS MEASURABLE, NOT INVISIBLE

§7 classed B-2 *"C — the instrument cannot see this class by construction."* **That is wrong on both the property and the class.**

- The property is not *"never touches a P09 model"* but **"does not declare or inherit one."** B-2's own named instance touches P09 models by relational reference and by `env[…]`.
- Measured on the already-declared root: **187 files reference a P09 model without declaring or inheriting it; 164 of them lie outside the population, across 51 modules.**

**Class corrected: A — measurable, and now measured as a floor of 164 files.** It was declared unsearchable while one bounded command over the declared root reopens it.

### 11.5 THE FORECAST DEMONSTRATION WAS POINTED AT THE WRONG BLIND SPOT

The forecast object is declared in `project_timesheet_forecast/report/timesheet_forecast_report.py` (`_auto = False`) and reaches the management fact table by **raw SQL** (`FROM account_analytic_line A`).

**That is blind spot B-1 (raw SQL), which §7 classed "not searched" — not B-2.** Measured: **15 files reach a P09 table by raw SQL; 12 lie outside the population, in 3 modules absent from it entirely.** B-1 is populated at scale and closable by one grep that was not run.

### 11.6 POSITIVE CONTROL 4 PASSED AT THE WRONG GRANULARITY

Control 4 was satisfied by a **different file** in the forecast module than the one declaring the object. **The instrument is declared file-granular; its acceptance control was evaluated at module granularity.** A control that returns a positive while the object it names is unreachable is not a control on that object. **Control 4 failed, and *"the instrument is accepted"* does not follow.**

### 11.7 COUNTS NOT REPRODUCIBLE

| Published | Measured |
|---|---|
| fact-table extenders **16** | **17** — an off-by-one **inside the author's own population** |
| allocation-mixin extenders **7** | **10** |
| plan-column mixin row | **absent from the matrix; measured 1** |
| the `account` control "16" | a **line** count, reproducible as such; the unit was not stated |
| plan-line fields **17** | **16** by one expert's count — *not adopted*: the author's own figure reproduced for a second expert. **Recorded as unreconciled** |

### 11.8 NEW P09 FACTS THE ROUND UNDER-RETAINED — ALL VERIFIED

| # | Fact | Why it matters |
|---|---|---|
| **N-1** | the second family's rows are shadowed into the report with **`'parent_state': 'posted'`** and the plan amount written into **`balance`**, on a temp table that `inherits (account_move_line)` with NOT-NULL dropped on currency, move, journal and display type | **a SECOND instance of the report-shadowing mechanism `AAS+-VETO-02` already stands against** — plan rows read as posted journal items |
| **N-2** | `account_budget/models/purchase_order_line.py:43` reads the plan line via **`sudo()`** | elevated read **inward** into P09's plan surface from an adjacent-domain document, bypassing record rules including company rules |
| **N-3** | the second family's **amount-bearing row carries no company field** (measured 0); company is stamped from the reader's active company at consumption | company attribution is **reader-derived, not stored** — a cleaner instance of a defect P09 already records |
| **N-4** | the plan-consumption row set mixes rate bases — one component divides by the order's stored rate — on a carrier whose figures are all plain floats with **no currency field** | `CH-06`'s "rate source and rate date" is **not sufficient**; it is needed **per component** |
| **N-5** | the second family has **no unique constraint, no company check**; its name is not unique and `(budget, account, date)` is not unique — duplicates are tolerated by design | identity and cardinality of the second family are **unstated** |

### 11.9 GENERATION DEPENDENCE OF THE NEW CLAIMS

| Item | Later generation |
|---|---|
| the second family's account key | carries an **account-type domain restriction** — so the withdrawn *"type, never a specific account"* claim has live substance there |
| the forecast module | **does not exist** |
| the same selector | returns a **different population** |
| the over-plan purchase-carrier files | live in a **separate module** |

**Every new claim in this round is generation-bounded, and the generation basis remains unestablished.**
