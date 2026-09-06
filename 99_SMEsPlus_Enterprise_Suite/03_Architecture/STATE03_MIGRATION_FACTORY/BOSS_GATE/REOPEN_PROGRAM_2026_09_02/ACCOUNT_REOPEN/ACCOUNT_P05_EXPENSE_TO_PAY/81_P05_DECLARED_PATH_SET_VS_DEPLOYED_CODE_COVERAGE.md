# 81 — P05 DECLARED PATH SET vs DEPLOYED CODE COVERAGE

`LAYER 2 — AUDIT QUARANTINE` · target `idemo18_uat` · read-only

**Origin.** AAS-03 **Expert 4** disclosed that, while testing whether `MD-01`'s declared path set was
self-consistent, one directory listing of the **parent** of the declared custom root surfaced a
sibling family of same-vendor custom modules. Expert 4 correctly reported this as *"the declared
three-root boundary was not tested against its own immediate neighborhood"* and left `MD-01`'s
conclusion unchanged. **This file executes the test Expert 4 named.**

The project's own denominator rule requires **POPULATION + PATTERN + PATH SET + UNIT**, none
author-chosen. Files `13` and `68` declared a PATH SET. **They never intersected it with the
deployed module list.** That intersection is the test, and it had never been run.

## 1. The Test

| Element | Value |
|---|---|
| **POPULATION** | every row of `ir_module_module` on `idemo18_uat` with `state = 'installed'` |
| **UNIT** | one installed module |
| **PATH SET (as declared)** | `ENT18` = the Odoo 18 distribution `odoo/addons`; `CUSTOM` = `.../EXTRA MODULE/smeplus-custom/addons` |
| **PATTERN** | module `name` present as a directory immediately under either declared root |
| **DIRECTION** | deployed → declared. The reverse direction (declared modules never deployed) was already covered by `44`/`45`. |

## 2. Result

```
installed modules total                                        : 361
installed AND present in the declared PATH SET                 : 191
installed AND ABSENT from the declared PATH SET                : 170   (47.1%)
```

> **`PS-01` FACT VERIFIED — class A within `ir_module_module` on `idemo18_uat`.**
> **170 of 361 installed modules — 47.1% of the deployment — were never inside the path set this
> package read from.** `MD-01` (`scgl_signature_hr_expense` has no source) was reported as a single
> named exception. It is one row of a 170-row population that was never enumerated.

## 3. The P05-Material Subset

Filtering the 170 to modules that inherit `hr.expense` or `hr.expense.sheet` — the only filter this
file is entitled to apply:

| Installed module | Declared root? | Inherits | Read before now? |
|---|---|---|---|
| `hr_expense_extract` | **absent** | `hr.expense`, `hr.expense.sheet` | **no** |
| `hr_expense_predict_product` | **absent** | `hr.expense` | **no** |
| `documents_hr_expense` | **absent** | `hr.expense` | **no** |
| `scgl_signature_hr_expense` | **absent** | `hr.expense.sheet` form only (per registry) | **no** — this is `MD-01` |

> **`PS-02` FACT VERIFIED.** Three modules that inherit the P05 core models were **installed on the
> evidenced deployment and outside the path set every P05 round read from.** They are not exotic:
> they ship with the platform generation the deployment runs.

**Where the missing roots actually are.** A second Odoo 18 addons tree exists on this host at
`.../Odoo18/t8master/addons` and carries all three. It was never declared. **This is not a new
search** — it is the named locator for the three modules `PS-02` identified, and nothing beyond
those three was read from it.

## 4. Impact on the Published State Finding — Bounded Read

`PSC-01` and `CQ-P05-03` turn on exactly two methods. Of the three unread modules, **one overrides
both of them**:

| Module | Overrides | Gate |
|---|---|---|
| `hr_expense_extract` | `_do_approve` · `action_sheet_move_post` · `action_register_payment` · `_unlink_except_posted_or_paid` | every override is gated on `_is_expense_sample()`; the non-sample branch delegates upward |

> **`PS-03` FACT VERIFIED.** For a sheet whose lines are flagged as samples, `action_sheet_move_post`
> **sets the sheet posted and, on the business-funded route, paid — and creates no accounting entry
> at all.** Approval likewise writes the approval fields and returns before entry creation.
> A **complete expense-to-pay lifecycle terminating in `paid` with no ledger record** is reachable in
> installed code.

### Is it live?

The route was measured, not assumed:

```
hr_expense.sample distribution : {NULL: 989, 'f': 4, 't': 0}
sheets with no accounting entry            : 267
  of which composed of sample expenses     : 0
```

> **`PS-04` — LATENT, NOT LIVE. Class A negative** within `hr_expense` on `idemo18_uat`
> (population 993, pattern `sample = 't'`, unit one expense row).
> **No sample-flagged expense exists on this deployment, so the bypass has not fired here.**
> It does **not** explain `PC-01`. The prior explanation of the 267 stands unchanged.

**What did not change.** `PS-04` closes the reachability question; it does not soften `PS-03`. The
distinction this programme adopted after the latent/live lesson applies here in the author's own
favour and is therefore stated at its weakest: **installed, reachable by construction, not observed
firing.**

### The residue `PS-04` leaves behind

```
sheets with no accounting entry : 267
  state = done, payment_state = paid  : 222
  state = approve / submit / draft / cancel : 45
```

> **222 sheets are marked settled and paid with no accounting entry of any kind.** That is `PC-01`,
> unchanged and now with one candidate cause eliminated rather than assumed.

## 5. What This File Does Not Claim

- It does **not** claim the other 167 modules are irrelevant. They were **not examined**. Their
  disposition is `C — NOT SEARCHED`, and widening to them is outside this phase.
- It does **not** claim `hr_expense_predict_product` or `documents_hr_expense` are inert. Only their
  `_inherit` declarations were read. Their behaviour is `C — NOT SEARCHED`.
- It does **not** withdraw `MD-01`. `scgl_signature_hr_expense` remains absent from every root
  searched, including the newly named one. `MD-01`'s **finding** survives; `MD-01`'s **framing** as a
  lone exception does not.
- It does **not** claim the deployment's running code matches any root read. That remains `U-16`,
  class **D**, and `PS-01` makes it worse rather than better.

## 6. Disposition

| Item | Before | After |
|---|---|---|
| Declared PATH SET completeness | asserted, never tested | **tested — 47.1% of installed code outside it** |
| `MD-01` | one named module with no source | **one row of an unenumerated 170** |
| `PSC-01` evidence base | two roots | **two roots, with a third holding an installed override of both governed methods** |
| `EC-01` (evidence population bounded) | NOT SATISFIED | **NOT SATISFIED — and now for a measured reason, not an estimated one** |
