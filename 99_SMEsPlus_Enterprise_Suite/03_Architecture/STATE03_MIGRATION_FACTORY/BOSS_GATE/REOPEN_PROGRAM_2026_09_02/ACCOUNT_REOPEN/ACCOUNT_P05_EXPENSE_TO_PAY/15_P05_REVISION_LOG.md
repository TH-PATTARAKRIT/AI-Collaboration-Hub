# 15 — P05 RESEARCH ERROR AND REVISION LOG

`LAYER 2 — AUDIT QUARANTINE`
This log records every hypothesis this session **got wrong and corrected**, and every revision forced
by governance. Per `ER-AASR-1`, this file and `11`, `16 §4`, `21` govern over any summary table
elsewhere in the package.

## 1. Self-Corrected Research Errors

| ID | Erroneous hypothesis | How it was caught | Correct finding | Impact if it had shipped |
|---|---|---|---|---|
| `RE-01` | *"Thai WHT is silently skipped when a payment is registered from a vendor bill, because the WHT branch requires `active_model == 'account.move.line'`."* | Traced the actual call chain instead of assuming the button's context. `account/models/account_move.py:5153-5161` routes `action_register_payment` → `action_force_register_payment` → `self.line_ids.action_register_payment()`, and `account_move_line.py:1112-1119` sets `active_model='account.move.line'`. | **CONTRADICTED.** The WHT branch does run. Recorded as `P05-F-29`, class **E**. | A false statutory-compliance defect would have been reported to Boss. |
| `RE-02` | *"`account.withholding.tax` has no ACL and no company rule."* | Read the manifest's `data` list and then the files it names, rather than inferring from a `find` that had been scoped to `models/` and `wizard/`. `security/ir.model.access.csv:2` and `security/security.xml:2-4` both exist. | **CONTRADICTED.** `P05-F-30`, class **E**. | A false security finding. |
| `RE-03` | *"A single expense report can mix `own_account` and `company_account` lines, because the sheet's `payment_mode` is a related field over a One2many and takes line 0."* | Read on past the field definition to the constraints. `hr_expense_sheet.py:422-427` `_check_payment_mode` blocks it, and `hr_expense.py:539-541` re-raises it from the line side, so **both** directions are guarded. | **CONTRADICTED.** `P05-F-31`, class **E**. | A false integrity finding, and it would have masked the real finding (`EX-03`: cardinality, not mixing). |
| `RE-04` | *"`hr_expense_petty_cash` registers its `_check_petty_cash_amount` constraint twice, because `account_move.py` and `account_invoice.py` both define it."* | Read `models/__init__.py`. Only `account_move` is imported; `account_invoice.py` is never loaded, and `views/account_invoice_views.xml` is not in the manifest. | **REVISED.** Not a duplicate-constraint defect; it is **orphaned code** (`P05-F-04`). The two files also differ materially (one uses `sudo()`, one does not; one clears `line_ids`, one does not), so the orphan is a divergent fork, not a copy. | A wrong defect class, and the real one (dead code carrying a different security posture) would have been missed. |
| `RE-05` | *"`advance.expense.clear.wizard` is a dead button — the model does not exist."* | Grepped the whole custom tree for the model name instead of only the two files whose names suggested it. It is defined at `wizard/advance_request_reconcile.py:53`, viewed at `wizard/advance_request_reconcile_view.xml:22`, and ACL'd at `security/ir.model.access.csv:6`. | **WITHDRAWN.** The wizard exists and is wired. | A false dead-code claim. |
| `RE-06` | Zero-count negatives for `petty cash`, `cash advance`, `corporate card` etc. across the reference tree. | The first run used unquoted `--include=*.py`, which **zsh expanded as a glob** and silently changed the command. Every count returned 0, including for tokens that are in fact abundant. Re-ran with quoted patterns. | **CORRECTED.** `petty[ _-]?cash` → 21 files in `CUSTOM`, 31 in `LEGACY14`. The corrected run is what located `hr_expense_petty_cash` and `scgl_advance_expense_request` — **the two modules that carry most of P05**. | Catastrophic. The package would have concluded that petty cash, employee advances and Thai WHT do not exist in this system, and would have declared six of eight expense classes "absent" when three of them are implemented in custom code. |

> **`RE-06` is the most important entry in this log.** It is a direct instance of the project's
> standing rule that *an enumeration is bounded by its pattern, not only by its path* — and the failure
> mode was not a wrong path but a **silently mutated command**. Method consequence, adopted for the
> remainder of this session and recommended project-wide: **a zero result is never accepted without
> re-running the same query in a second form.** Every zero count in `21` was re-run.

## 2. Governance-Forced Revisions

| ID | Trigger | Revision |
|---|---|---|
| `GR-01` | `SMEPLUS-26-09-04-ACC-REV2-CORR1` — Scope-Aware Constitution Correction, received mid-execution | **No reset, no restart, no evidence discarded.** Added `22_P05_SCOPE_OWNERSHIP_MATRIX.md`. Revalidated the four findings that rested on a blanket "Tenant+Company mandatory everywhere" assumption: `R-01` (withdrawn as a scope defect), `R-02` (upheld, re-derived from the object's own financial semantics), `R-03` (**new finding `SC-01`** — the reference is *over*-constrained, the opposite of the original reading), `R-04` (upheld, re-derived). `R-05` confirmed unaffected. `R-06` lists the findings that carry no scope assumption and are preserved verbatim. |
| `GR-02` | Same correction, §7 | `PEER DEPENDENCY OPEN` recorded for P01/P02/P03 rather than blocking. Session continued. |
| `GR-03` | Same correction, §10 | Terminal wording constrained to `READY FOR CORE ACCOUNTING RECONCILIATION`; `PASS`, `FINAL FREEZE`, `MERGED`, `IMPLEMENTATION AUTHORIZED` are prohibited without Boss decision. Verified mechanically — see `18 §5`. |

> `GR-01` note: the correction did not merely soften a rule, it **inverted one finding's direction**.
> `R-03` was originally logged as compliant *because* it was company-scoped. Under scope-aware analysis
> the same fact is a defect, because statutory reference data is being duplicated per company. A
> blanket rule had been hiding an over-constraint.

## 3. Method Controls Applied This Session

| Control | Applied? | Evidence |
|---|---|---|
| Read the adversarial/correction section of a source before its summary (`ER-AASR-1`) | Yes | Governance files were read for their operative clauses; `00 §Reading Order Rule` propagates the rule to readers of this package |
| Declare POPULATION + PATTERN + PATH SET + UNIT for every enumeration | Yes | `01 §1.1`, `13 §3`, `21` |
| Never upgrade a class B/C/D negative to class A | Yes | `21`; `NC-04`, `NC-05`, `NC-08`..`NC-12` all held at B or C |
| Independent review inside the enumeration phase, disjoint assignments, at least one adversarial | Yes | Four AAS-03 experts, disjoint scopes, all four briefed to **disprove** rather than confirm, and all four told to report errors in the brief itself |
| Mechanical scan for prohibited verdict wording | Yes | `18 §5` |
| Prove the executor of every declared control | Yes | This is how `C-01` was found: the guard exists, is readable, looks correct, and does not contain the fields it names |

## 4. Revision History

| Rev | Change |
|---|---|
| `r1` | Initial trace of `hr_expense`; findings `P05-F-19..F-28` |
| `r2` | Custom addon set located after `RE-06` correction; scope of the session materially widened |
| `r3` | Advance, petty cash and WHT chains traced; `P05-F-01..F-18` |
| `r4` | `RE-01`..`RE-05` self-disproofs recorded before any external review |
| `r5` | Four AAS-03 challenges dispatched with disjoint scopes |
| `r6` | `CORR1` applied — `22` added, `R-01`..`R-06` revalidated, `02`/`04` patched with pointers |
| `r7` | Challenge verdicts consolidated into `16`, `11`, `21`; AAS+ and PMO issued |
