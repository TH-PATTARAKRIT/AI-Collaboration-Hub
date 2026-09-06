# E05 — L1–L8 BOUNDED CORRECTION EVIDENCE (LAYER 2 — AUDIT QUARANTINE)

**Session:** `SMEPLUS-26-09-06-P09-P2A-L1-L8-FINAL-BOUNDED-CORRECTION-005`
**Classification:** LAYER 2 — AUDIT QUARANTINE. Boss / PMO / AI-Audit only.
**Prohibition:** nothing here may be transcribed into Layer 1. Layer 1 cites `EV-P09-5nn`.
**Frozen baseline:** `92de8a1` · declared root unchanged.

---

## 0. DECLARED BEFORE ANY RESULT

| Element | K-2 | K-3 |
|---|---|---|
| **unit** | the file | the file |
| **denominator** | files reaching a P09 **table** by raw SQL | files **referencing** a P09 **model** without declaring or inheriting it |
| **source root** | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/addons` — **unchanged, not widened** | same |
| **inclusion rule** | SQL context keyword (`FROM/JOIN/INTO/UPDATE/TABLE/EXISTS`) + one of ten P09 table names | a P09 model string literal surviving an **AST** declaration strip |
| **exclusion rule** | files inside the K-1 population reported separately | same |
| **blind spots** | non-source carriers; dynamically built table names | non-source carriers; dynamically built model names |
| **generation vs deployment** | source generation **18.0 Enterprise**; **no deployment status inferred anywhere** | same |
| **ownership unit** | **file**, never module | same |

---

## 1. EV-P09-500 — L-1: THE NAMESPACE DEFECT AND ITS REPAIR

**Defect, exactly:**

```
PLAN = ("budget.", "account.report.budget")          # MODEL namespace, dotted
values passed in the K-2 branch                      # TABLE namespace, underscored
"account_report_budget".startswith("account.report.budget") -> False   (all inputs)
```

**Repair:** two disjoint predicates, one per namespace.

```
PLANNING_TABLES = {budget_line, budget_analytic, budget_report,
                   account_report_budget, account_report_budget_item}   # K-2
PLANNING_MODELS_PREFIX = ("budget.", "account.report.budget")           # K-3
```

**Result — reproduced independently of the prior round's output:**

| Measure | Value |
|---|---|
| files reaching a P09 table by raw SQL, outside the population | **12** |
| **touching a planning table** | **1** — `account_reports/models/account_report.py` → `account_report_budget`, `account_report_budget_item` |
| touching only `account_analytic_line` | **11** |

---

## 2. EV-P09-501 — L-2: CONTROL TABLES

### 2.1 K-2 — ACCEPTED

| Control | Witness | Result |
|---|---|---|
| positive — planning-SQL file classifies planning | `account_reports/models/account_report.py` | **HOLDS** |
| negative — fact-only file classifies not-planning | `hr_timesheet/models/hr_employee.py` | **HOLDS** |
| negative — `account_analytic_line` alone is not planning | literal | **HOLDS** |
| positive — predicate fires on `account_report_budget` | literal (the string that broke it) | **HOLDS** |

### 2.2 K-3 — ONE CONTROL FAILED FIRST

**First attempt, negative control:** *"a file's own declaration is not counted as a reference"*, witness `account_budget/models/budget_analytic.py` → **FAILED**.

**Diagnosis, not a patch.** That file declares the plan header at line 10 **and legitimately references it** at lines 17, 22 (`comodel_name='budget.analytic'`, the revision links) and 86 (markup). The declaration **was** stripped; the surviving hits are real references. **The control asserted a property the instrument never claims.**

**v2 — also defective, caught by challenge.** It drew its witness from `pure`, the set **defined by the property under test** ("matches before the strip, none after"), then re-tested that membership. **A control whose witness is selected by the property it tests cannot fail.** The "29 witnesses" figure was true by construction, not measured. It also lived in a **second script that computes no residue**, while the residue producer still carried and gated on v1 and shipped `"k3_controls_ok": false`.

**v3 — shipped.** Witness selected **independently**: the first owning file of the K-1 population, chosen by *declaration*. Assertion: **the declaration statement's text is removed from the source.** A file may legitimately reference its own declared model — v1 wrongly treated that as a defect.

| Control | Witness | Result |
|---|---|---|
| negative — **declaration STATEMENTS removed from the source** | `account_budget/models/budget_analytic.py` (2 statements), selected independently | **HOLDS** |
| positive — a pure reference survives | `account_budget/models/purchase_order_line.py` | **HOLDS** |
| failure — a declare+reference file keeps its reference and loses its declaration | same | **HOLDS — now ASSERTED**; the prior publication graded this row by hand while the script computed no predicate |

**All three now run inside the residue-producing instrument**, which prints `K-3 CLASSIFIER: ACCEPTED` and stores `"k3_controls_ok": true`.

---

## 3. EV-P09-502 — L-8: AST STRIP

Declaration lines are removed by walking the syntax tree and blanking every line span of a `_name` / `_inherit` / `_inherits` assignment — multi-line by construction.

| Measure | AST | Line-based |
|---|---|---|
| unparseable | **0** | — |
| outside population | **169 / 52** | **169 / 52** *(both executed; was 170 before the eligibility fix)* |
| planning | **10** | **10** |
| tests / non-test | **6 / 4** | 6 / 4 |

**Identical, and both columns EXECUTED** — the earlier publication hard-coded the right-hand column. Construction safety is **narrowed**: annotated / augmented / tuple- and attribute-target declarations are unhandled, enumerated over the root, and **measured at zero on P09 models**.

---

## 4. EV-P09-503 — L-4: THE 160

| Model referenced | Files |
|---|---|
| `account.analytic.line` | 100 |
| `account.analytic.account` | 72 |
| `account.analytic.plan` | 57 |
| `account.analytic.distribution.model` | 11 |
| `account.analytic.applicability` | 9 |

**No planning model.** Population corrected **160 → 159** (one entered on a dotted field path, not a model); outside-population **170 → 169**. Assessed against every current non-planning P09 claim: none of ownership or extension is disturbed. **BUT the exclusion authority is WITHDRAWN — the prior round publishes 193 and 170/52 over the reference relation, so the reversal condition has already fired.**

---

## 5. EV-P09-504 — L-5: THE SIX TESTS

| File | Classes | Test methods |
|---|---|---|
| `account_budget/tests/common.py` | `TestAccountBudgetCommon` | **0** — fixture |
| `account_budget/tests/test_account_budget.py` | `TestAccountBudget` | 2 |
| `account_budget/tests/test_commited_achieved_amount.py` | `TestCommittedAchievedAmount` | **10** — incl. `test_budget_multi_currency`, unposted-bill, discount/included-tax, multiple bills per order |
| `account_budget/tests/test_theoreticalamount.py` | `TestTheoreticalAmount` | 2 |
| `account_reports/tests/test_budget.py` | `TestBudgetReport` | **9** — incl. comparison period, date filters, **`test_report_budget_edit_items`** |
| `project_account_budget/tests/test_project.py` | `TestProject` | 2 |

**Two bear on live handoffs:** the multi-currency case on `CH-06`'s currency component; the edit-items case on `CI-05b`'s report-cell unit.

---

## 6. EV-P09-505 — L-7: THE LOCATOR SEARCH

| Probe | Result |
|---|---|
| `CH-09` row today | already corrected |
| `CH-09` row at its **first commit** (`99b0d52`) | **already corrected** — edited in place before ever being committed |
| the distinctive phrases elsewhere in the package | ~~absent~~ → **FALSE NEGATIVE.** The Phase S challenge record carries *"three outputs are terminal, cross no boundary, need no contract"* — **nearer verbatim than the paraphrase named below**, and the same file is counted as a citation two sections later. A fact and its negation, corrected |
| nearest attested source | **the Phase S challenge record's near-verbatim line**, committed at `99b0d52`; the I/P/O pack's paraphrase is second-nearest |

**No committed original exists** — the row was corrected in place before its first commit. The tombstone's *"preserved verbatim"* is corrected to **"reconstructed from the near-verbatim attested line"**, which is a **stronger** basis than first recorded.

**Citations: 21 occurrences across 11 files over a declared path set including the shared program root — four lie OUTSIDE the P09 package.** ~~P11 has published no branch~~ — **FALSE; P11 has published a branch at CORR3 and consumes P09 artefacts by name.** What holds on measurement: **no peer package cites the `CH-09` identifier.**

---

## 7. REPRODUCIBILITY

| Item | Locator |
|---|---|
| L-1 / L-2 (K-2) / L-8 | `INSTRUMENTS/L1_L2_L8.py`, output `INSTRUMENTS/L_results.json` |
| L-2 (K-3 re-specified control) | `INSTRUMENTS/L2_k3_control.py` |
| L-4 / L-5 | `INSTRUMENTS/L4_L5.py` |

**All are inside the package, read package-relative paths, and are checksummed in `INSTRUMENTS_MANIFEST_SHA256.md`.** The first publication asserted this while the producer still read its denominator from a session scratchpad and no checksum existed — **the defect was repeated and is now actually fixed.**

---

## 8. BLIND SPOTS, RESTATED

| # | Blind spot | Class |
|---|---|---|
| 1 | non-source carriers (views, data, client-side) | **C — not searched** |
| 2 | dynamically built table or model names | **C — not searched** |
| 3 | roots outside the declared one | **B — boundary declared, not chased** |
| 4 | deployment rungs — installed / configured / exercised | **held; source generation established, deployment not inferred** |
