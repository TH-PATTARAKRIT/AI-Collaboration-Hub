# 25 — PEER EVIDENCE INTEGRATION: P04 ACQUIRE-TO-RETIRE

**LAYER 2 — AUDIT QUARANTINE.**

Inbound peer evidence from **P04 — Acquire-to-Retire**
(`research/account-p04-acquire-to-retire-2026-09-04-001`, file `06`), received after this
package was pushed at `812cc5c`.

**Method.** Every P04 claim that touches P03's domain was **independently re-verified from
primary source before adoption.** Nothing was adopted on assertion. Where P04 corrects
P03, P03 is corrected. Where P03 was already right, that is stated plainly rather than
inflated. Where P04 and P03 genuinely diverge, the divergence is preserved for P11.

---

## 1. Verification results

| # | P04 claim | Verified? | Effect on P03 |
|---|---|---|---|
| 1 | Nine monetisation paths, not two | **Method accepted** | **P03's "two" declared no unit — corrected, §2** |
| 2 | Real GL mismatch under standard costing | **Confirmed** | Sharpens `DC-04`, §4 |
| 3a | Extra unit cost never relieved | **Already `DC-03`** | Independent confirmation |
| 3b | Help text describes the wrong residue | **Confirmed from source** | **New — sharpens `DC-03`, §4** |
| 3c | M4/M5 post the identical amount twice into the analytic ledger | **Confirmed from source** | **New finding `DC-14`, §3** |
| 3d | Analytic ledger and GL disagree on the same work order | **Already `DC-05`** | Independent confirmation |
| 3e | Labour relief entry has no idempotence marker | **Confirmed from source** | **New finding `DC-15`, §3** |
| 4 | The operation has no equipment field | **Consistent** with `04` §2 and Asset `07` §2 | Third independent confirmation |
| 5 | The analytic route for depreciation **nets to zero** | **Confirmed from source** | **Strengthens `CC-07`, §5** |
| 6 | Scope narrowing; `P04-B-35` assigned to P03 | **Accepted, with one divergence** | **§6 — includes P03's first downgrade under CORR1** |

## 2. The denominator correction — P04's most useful contribution

`01` §3 asserted *"everything in the chain reduces to exactly two writers."* P04 counts
nine, and **states honestly that the counts are not comparable because the prior count
declared no unit.** That is precisely right, and the failure is P03's.

`smeplus-denominator-completeness-rule` requires **POPULATION + PATTERN + PATH SET + UNIT**,
none author-chosen. `02` §1's register declared its unit ("independent writers that put
this element into inventory value"). **`01` §3 did not, and is the weaker statement.**

**Correction, applied.** `01` §3 now declares:

> **UNIT: one writer that changes the carrying value of inventory.**
> Under that unit the count is two — `_cal_price` and `_post_labour`.
> Under P04's disjunctive unit — own rate field OR own driver quantity OR own destination
> ledger — the count is nine, and the analytic and planning paths that P03 correctly
> excluded from *inventory value* are correctly included in *monetisation*.

**Both counts are right under their own declared unit. Neither supersedes the other.**
What survives every unit, and is the sentence that matters: **the same hour is monetised
more than twice, and at least two of those paths do not reconcile.**

P04's `M5` is the weakest of the nine on P04's own account — a second call, not a second
computation. **P03's verification finds M5 stronger than P04 claims**: see §3.

## 3. Two new findings adopted

### `DC-14` — the same value distributed twice into the analytic ledger

`project_mrp_account/models/mrp_workorder.py:9-14` overrides
`_create_or_update_analytic_entry_for_record(value, hours)`:

```
super()._create_or_update_analytic_entry_for_record(value, hours)   # → work-centre distribution
project = self.production_id.project_id
mo_analytic_line_vals = …_perform_analytic_distribution(
    project._get_analytic_distribution(), value, hours, self.mo_analytic_account_line_ids, self)
```

**The identical `value` and `hours` are distributed twice** — once over the work centre's
distribution, once over the project's — with **no guard and no plan-collision check.**

**P03 rates this higher than P04 does.** P04 calls it "a second call, not a second
computation". That is true of the *arithmetic* and irrelevant to the *ledger*: two calls
that each create analytic lines for the same value produce two sets of analytic lines. Where
both distributions resolve to the same analytic account — an ordinary single-plan SME
configuration — the analytic ledger carries the work-centre cost twice.

`FACT VERIFIED` (mechanism). Incidence is a configuration question: `UNR-P03-05`.
Conditional on `project_mrp_account` being installed and the order carrying a project —
the same conditional-availability class as `DC-10`.

### `DC-15` — the labour relief entry has no idempotence marker

`mrp_account/models/mrp_production.py:106` writes the resulting entry's line onto every
contributing time log:

```
workorders[line.account_id].time_ids.write({'account_move_line_id': line.id})
```

**Enumeration.** POPULATION: the manufacturing and manufacturing-accounting modules.
PATTERN: identifier `account_move_line_id`. UNIT: one occurrence.
Result — 4 occurrences: one field declaration, one write, **two reads, both in tests.**

**The marker is written and never read as a guard.** `_post_labour` has no check for an
existing entry; its only guards are the valuation mode and a zero-amount test.

`FACT VERIFIED` — the absence of the guard. **Whether a second post is reachable is
`UNRESOLVED`** (`UNR-P03-06`): `_post_labour` is called only for orders reaching the done
state, and a second transition is not obviously reachable from the code read. P04 states
the same limitation. Neither session claims more than the code shows.

## 4. Two findings sharpened

### `DC-03` — the documentation states the inverse of the behaviour

Verified at `mrp_account/models/product.py:126-128`. The production-account field's help
text reads:

> *"If there are any workcenter/employee costs, this value will remain on the account once
> the production is completed."*

**Work-centre and employee costs are exactly what `_post_labour` clears.** The residue that
genuinely remains — the manually entered extra unit cost — is not mentioned.

The documentation therefore describes as permanent the one residue that is relieved, and
omits the one that is not. A reader following the help text would look for the balance in
the wrong place. `FACT VERIFIED`. P04's catch; P03 confirms.

### `DC-04` — naming the content of the standard

`03` §4 established the mismatch. P04 supplies what the standard *contains*, which P03 had
traced but not connected: `_compute_bom_price`
(`mrp_account/models/product.py:87-94`) builds the standard from
**planned** duration × `_total_cost_per_hour`, which is the work-centre rate plus, where
the employee bridge is installed, the employee rate × ratio
(`mrp_workorder_hr_account/models/mrp_routing.py:10-11`).

So the mismatch is sharper than `03` §4 stated:

> **Standard overhead on *planned* duration is credited to the production account; actual
> overhead on *actual* duration is debited to it. The difference is stranded, with no
> variance account and no report line pointing at it.**

This is the mechanism behind `10` §4's unnamed residue, now fully named. Both sessions
independently reach Asset `UNR-C-03`; **neither closes it — it is Asset-owned.**

## 5. `CC-07` strengthened — the believed depreciation route nets to zero

`02` §1 recorded "no path" for equipment depreciation. P04 explains why the route most
people assume exists does not, and P03 verified it:

`account_asset/models/account_move.py:297-299` sets `analytic_distribution` on **both**
lines of the depreciation entry. The two lines are equal and opposite, so the analytic
amounts are `+x` and `−x`. **The analytic dimension nets to zero and cannot accumulate a
depreciation cost pool.**

`FACT VERIFIED`. This converts `CC-07` from *no path found* to *the one candidate path is
structurally incapable of carrying the cost* — a materially stronger statement, and one
that survives `DEP-04`, because it does not depend on which modules are installed.

## 6. Scope — `P04-B-35` accepted, and P03's first downgrade under CORR1

### The item assigned to P03

**`P04-B-35` / `P04-PD-01`** — the work centre carries a rate that lands in inventory
valuation, so it creates a financial effect, so CORR1 question 7 (*which company owns that
financial effect?*) must be answerable. On a company-optional work centre it is not.
**Missing required scope = DENY.**

**Accepted and registered** as P03's `SCOPE-02`, High. It is the same defect `18` §4 states
as `R-15`, now carrying P04's identifier and its closing evidence: **one runtime count of
work centres with no company.** Added to `14` as `DEP-13`.

### The downgrade

`18` §3 gave a single row *"Machine / equipment — `COMPANY`"*. **P04 is right that this
conflates two objects.**

| Object | P03's original | Corrected | Reason |
|---|---|---|---|
| Machine / **equipment register** | `COMPANY` | **`TENANT`, company-optional correct** | The register creates no financial effect of its own. Under CORR1, requiring company context here is over-constrained |
| The **asset** behind it | `COMPANY` | `COMPANY` — unchanged | Depreciation is a company-scoped financial effect |
| The **work-centre rate** | `COMPANY` | `COMPANY` — unchanged, now reinforced | `SCOPE-02` |

**This is the first genuine downgrade P03 has recorded under CORR1**, and it matters. `22`
§3 previously showed two findings strengthened, one new, and **zero downgrades** — a
pattern that is evidence of a correction being applied selectively rather than honestly.
The correction is not a device for making findings worse. Recorded as `REV-S-05`.

### The one divergence preserved for P11

P04 treats the equipment register as `TENANT`. P03 accepts that for the register. **P03
does not extend it to the asset**, and P04's message does not ask it to. Should a later
reconciliation read P04's narrowing as covering assets too, **P03 dissents**: an asset
whose depreciation is a company-scoped financial effect cannot itself be tenant-scoped.
Recorded for `DEP-11` (P11), not resolved here.

## 7. Effect on the standing AAS+ veto

`20` §5 upheld `AASP-VETO-01`. P04 reports that the veto's second limb — proving that
**exactly one** mechanism carries machine cost into product cost — is now **wider**: the
proof must be discharged against a declared population of **nine**, not two.

**P03 accepts this without qualification.** It is the correct consequence of §2, and it
makes the veto harder to discharge, not easier. `20` §5 is amended accordingly.

**No prior blocker is closed by this integration. No gate is closed. Nothing is merged.**
