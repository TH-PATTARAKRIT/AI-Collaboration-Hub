# 05 — P03 DOUBLE-COUNTING ATTACK

**LAYER 2 — AUDIT QUARANTINE.**

**This is the core result of the session.**

Canonical principle under test:

> **ONE ECONOMIC COST → ONE COST INJECTION PATH INTO WIP.**

Method: the attack is run as a set of falsifiable simulations. Each states an input, the
code path, the arithmetic, and the output. Each is then classified. One hypothesis was
raised, tested and **discarded** — it is kept in §9 because a discarded attack is
evidence too.

---

## 1. Findings, ranked

| ID | Finding | Class | Severity |
|---|---|---|---|
| `DC-01` | Machine cost is charged on the **raw sum of overlapping time logs**, so one machine-hour becomes N machine-hours when N people work it | `FACT VERIFIED` — **CONTRADICTED design** | **Critical** |
| `DC-02` | Machine and labour rates are applied to the same interval with no control on what the machine rate contains | `FACT VERIFIED` | High |
| `DC-03` | `extra_cost` is capitalised and never relieved (non-subcontract) | `FACT VERIFIED` | High |
| `DC-04` | Standard-cost + real-time products relieve labour that was never capitalised | `FACT VERIFIED` | High |
| `DC-05` | Analytic and financial cost use different durations **and** different cost content | `FACT VERIFIED` | High |
| `DC-06` | The posted rate ignores the work-order rate snapshot that every report honours | `FACT VERIFIED` | Medium-High |
| `DC-07` | Labour absorption defaults to crediting the **finished product's expense (COGS) account** | `FACT VERIFIED` | **Critical** |
| `DC-08` | Zero-time work orders silently inject **expected** cost as actual | `FACT VERIFIED` | High |
| `DC-09` | The labour entry takes today's date, not the MO's | `FACT VERIFIED` | Medium-High |
| `DC-10` | Employee analytic cost is inert unless an unrelated Project module is installed | `FACT VERIFIED` | Medium |
| `DC-11` | `_post_labour` resolves company-dependent accounts in the **user's** company, not the MO's | `FACT VERIFIED` | **Critical — tenant isolation** |
| `DC-12` | Employee cost is converted at the currency rate **twice** in the cost-structure report | `FACT VERIFIED` | Medium — reporting only |
| `DC-13` | Unbuild releases finished goods at the **first** valuation layer's unit cost | `FACT VERIFIED` | Medium |
| `DC-14` | **The identical value is distributed twice into the analytic ledger** — work-centre distribution and project distribution, no guard, no plan-collision check | `FACT VERIFIED` (mechanism) | **High** |
| `DC-15` | The labour relief entry writes an entry marker onto every time log and **never reads it as a guard** — no idempotence marker exists | `FACT VERIFIED` (absence) | Medium |

`DC-14` and `DC-15` were raised by **P04 — Acquire-to-Retire** and independently verified
from primary source before adoption. Full verification record, including where P03 rates
`DC-14` **higher** than P04 does: `25` §3.

## 2. `DC-01` — one machine-hour, N injections · **the headline**

### The two duration bases

| Function | Duration basis | Cited |
|---|---|---|
| `_compute_duration` — base | `sum(order.time_ids.mapped('duration'))` — **raw sum** | `mrp/models/mrp_workorder.py:321-329` |
| `_compute_duration` — with the work-order module installed | `wo.get_duration()` → `_intervals_duration` — **overlap-merged** | `mrp_workorder/models/mrp_workorder.py:757-767`, `:811`, `:828-836` |
| **`_cal_cost` — the function that posts money** | `sum(wo.time_ids.mapped('duration'))` — **raw sum, in both modules** | `mrp/models/mrp_workorder.py:582-587` |

The work-order module exists precisely to de-duplicate overlapping employee intervals —
`_intervals_duration` is written for that purpose and `_compute_duration` is overridden to
use it. **`_cal_cost` was not.**

### Simulation

Two operators, one machine, one work order. Both log 09:00–10:00. Work-centre rate 500/h.

| Quantity | Value | Path |
|---|---|---|
| Overlap-merged duration | 60 min | `get_duration()` → what the user sees |
| Raw sum of time logs | 120 min | `sum(time_ids.duration)` |
| **Machine cost posted into WIP** | **120 ÷ 60 × 500 = 1,000** | `_cal_cost`, `mrp/models/mrp_workorder.py:587` |
| Machine cost the business incurred | 500 | one machine, one hour |
| Machine cost the work order **displays** | 500 | `duration` = 60 min |

**One economic cost. Two injections. The screen shows one; the ledger carries two.**

**Scope of the inflation — AAS-03 `C-01`.** The *employee* half of `_cal_cost` is
correct here: two people did work two hours, and two labour-hours is the right answer.
**The inflation is confined to the machine component**, which is charged on a head-count-
dependent base for a resource that has no head count. Read the finding as *machine cost
scales with operators*, not as *all conversion cost doubles*.

### Why this is a design contradiction, not a preference

The same module that introduces overlapping time logs also introduces the function that
merges them, and applies it to the displayed duration. The costing function reads the
un-merged sum from a **different module's** implementation. Both behaviours are
deliberate in isolation; together they contradict.

`CONTRADICTED`. Recorded in `16_P03_CONTRADICTION_REGISTER.md` as `CTR-P03-01`.

### Scale

The multiplier is the number of concurrently logged operators. It is unbounded, it applies
to every MO that uses multi-operator work orders, and it inflates **inventory**, not just
an expense — so it survives into the balance sheet and then into COGS.

## 3. `DC-07` — labour absorption credits COGS by default

```
account = wo.workcenter_id.expense_account_id or product_accounts['expense']
```
`mrp_account/models/mrp_production.py:81`

`expense_account_id` on the work centre is optional and has no default
(`mrp_account/models/mrp_workcenter.py:12-13`). When it is unset — the out-of-the-box
state — the fallback is `product_accounts['expense']`, **the finished product's expense
account, i.e. its cost-of-goods-sold account**.

### Simulation

MO produces 100 units. Work-centre cost 10,000. Nothing sold this period.

| Account | Effect |
|---|---|
| Production Cost | Dr 10,000 |
| **COGS of the finished product** | **Cr 10,000** |

COGS is credited 10,000 in a period in which nothing was sold. Gross margin is overstated
by 10,000 until the goods sell, and the two errors only cancel if the whole batch sells in
the same period.

**The help text on the field states the intent plainly** — *"If not set, it is the expense
account of the final product that will be used instead"* — so the behaviour is documented.
It is nonetheless a defect in the SMEsPlus sense: a **silent default that produces a wrong
period result**, in the same family as the silent 1:1 FX fallback recorded in
`smeplus-account-wave-a-core-findings`.

**Failure mode — AAS+ `AASP-01`.** This is a **period-attribution** failure, not a
permanent overstatement. The two errors cancel once the batch sells. Where production and
sale fall in one period the ledger ends correct. Severity remains Critical because
`PROJECT_CONSTITUTION.md` principle 13 assigns severity on the failure mode rather than on
its expected frequency — but the finding must not be read as a permanent loss of value.

`FACT VERIFIED`. SMEsPlus requirement: absorption credits must be explicit and mandatory;
no absorption may fall back to a COGS account.

## 4. `DC-11` — company-dependent accounts resolved in the wrong company

Within one function, `mrp_account/models/mrp_production.py:72-106`:

| Line | Code | Company context |
|---|---|---|
| `:74` | `mo.with_company(mo.company_id).product_id.valuation` | **MO's company — correct** |
| `:77` | `mo.product_id.product_tmpl_id.get_product_accounts()` | **no `with_company` — the acting user's company** |
| `:90` | `mo.move_finished_ids[0]._get_src_account(product_accounts)` | consumes the mis-resolved data |

`property_stock_account_production_cost_id` is declared `company_dependent=True`
(`mrp_account/models/product.py:124-128`). `stock_journal` and `expense` are likewise
company-dependent properties.

**The guard is present on line 74 and absent three lines later.** A user whose active
company differs from the MO's company posts the labour entry to **the wrong company's
accounts and the wrong company's journal**, while the `check_company` constraints on the
individual fields pass, because each account is internally consistent — just for the wrong
company.

`FACT VERIFIED`. This is a cross-company leakage class finding and is routed to the
Inventory multi-tenant invariant set for conformance
(`origin/ruling/inventory-mti-*`), as `DEP-05`.

## 5. `DC-08` — expected cost injected as actual

`mrp/models/mrp_production.py`, inside `_post_inventory`:

```
for workorder in order.workorder_ids:
    if workorder.state not in ('done', 'cancel'):
        workorder.duration_expected = workorder._get_duration_expected()
    if workorder.duration == 0.0:
        workorder.duration = workorder.duration_expected
```

An MO completed without any time tracking has its duration **set equal to the expected
duration**, and `_cal_price` then capitalises that as actual cost.

**Consequences:**
1. An "actual cost" product silently becomes standard-costed for its conversion cost.
2. The variance is structurally zero, so no report can reveal it.
3. There is no evidence anywhere in the record that no work was measured.

**Classification — corrected by AAS-03 `C-04`.** The *outcome* — a zero-duration work
order ends up costed at its expected duration — is `FACT VERIFIED`: it follows from
`_cal_price` reading `_cal_cost`, both read in full. The *mechanism* by which the forced
write propagates into the time logs runs through `_set_duration`, whose body **was not
read in this session**; that step is `SUPPORTED INTERPRETATION`. Severity is unchanged;
the classification is corrected rather than left overstated.

SMEsPlus requirement: a cost with no measurement must be **either**
refused **or** recorded as an explicitly flagged estimate. It must never be
indistinguishable from a measured cost.

## 6. `DC-05` — three different numbers for one cost

| Consumer | Duration | Content | Cited |
|---|---|---|---|
| **Ledger** | raw sum | machine + employee | `mrp/models/mrp_workorder.py:582-587`; `mrp_workorder/models/mrp_workorder.py:854-858` |
| **Analytic** | `wo.duration` — merged when the work-order module is installed | **machine only** | `mrp_account/models/mrp_workorder.py:45-47` |
| **Report** | per time log | machine + employee, employee at rate² | `mrp_workorder_hr_account/report/mrp_cost_structure.py:61,78-83` |

The analytic amount is `-hours × wo.workcenter_id.costs_hour` with `hours = wo.duration / 60`.
It therefore differs from the ledger in **both** factors at once. Analytic accounting can
never be reconciled to the general ledger for manufacturing cost. `FACT VERIFIED`.

## 7. `DC-10` — the inert employee analytic field

**Enumeration.** POPULATION: all `*.py` in the declared source root.
PATTERN: identifier `employee_analytic_account_line_ids`. UNIT: one occurrence.
Result — 9 occurrences, 3 files:

| File | Role |
|---|---|
| `mrp_workorder_hr_account/models/mrp_workorder.py:18` | declares the field |
| `mrp_workorder_hr_account/models/mrp_workorder.py:25` | unlinks it on cancel |
| `project_mrp_workorder_account/models/mrp_workcenter_productivity.py:40` | **the only writer** |
| `project_mrp_workorder_account/tests/…` | tests |

The module that declares the field never populates it. The only writer lives in a
**Project** bridge module. Without that module, employee analytic cost is never recorded
and the field is inert.

Class: **conditional dead code** — the same class as the partly-dead custom asset-equipment
link recorded in `smeplus-asset-deep-l1-l6-findings`. `FACT VERIFIED`.

## 8. `DC-12` and `DC-13` — the two narrower ones

**`DC-12`** — `mrp_workorder_hr_account/report/mrp_cost_structure.py:43-44`:
```
cost = employee_cost * currency_rate
empl_cost_by_product[product].append([..., duration / 60.0, cost * currency_rate])
```
The rate is applied on both lines, then `:47` computes `l[-1] * l[-2]` — cost × hours.
The **duration factor is correct**; the error is precisely that the currency rate is
applied twice, so the reported employee cost is out by a factor of the rate
(AAS-03 `C-05`). In a single-currency company the rate is 1 and the defect is invisible.
Reporting only; does not reach the ledger. `FACT VERIFIED`.

**`DC-13`** — `mrp_account/models/stock_move.py:49-51`: on unbuild, the released unit cost
is taken from `…stock_valuation_layer_ids.filtered(…)[0].unit_cost` — the **first** layer
for that product on the MO. Where the finished goods were produced across more than one
layer, the unbuild releases a cost that belongs to a different layer. `FACT VERIFIED`.

## 9. An attack that was raised and discarded

Recorded because a discarded hypothesis is evidence, and because
`smeplus-deep-research-negative-claim-standard` requires it.

**Hypothesis.** `mrp_account/models/stock_move.py:23-24` extends
`_ignore_automatic_valuation()` to return true for any move carrying a raw-material
production link. Raw-material scrap moves carry that link
(`mrp/models/stock_scrap.py:47-48`). If that flag suppressed GL posting, scrapped material
would never reach the ledger — a severe finding.

**Test.** The single call site was read:
`stock_account/models/stock_move.py:573`. It sits inside the **analytic** line
preparation, selecting which source the analytic amount is drawn from. It has **no effect
on general-ledger posting**.

**Result: hypothesis false. Discarded.** Scrap is valued and posted by the generic
inventory-loss path. The real scrap finding is different and narrower, and is in
`11_P03_SCRAP_REWORK_MATRIX.md`.

## 10. Verdict against the canonical principle

| Principle | Holds? |
|---|---|
| ONE BUSINESS FACT → ONE EVENT OWNER | **Yes** — the work order owns conversion cost unambiguously |
| ONE EVENT OWNER → ONE ACCOUNTING EFFECT | **No** — `DC-03`, `DC-04`, `DC-07` produce residues and mis-directed effects |
| **ONE ECONOMIC COST → ONE COST INJECTION PATH INTO WIP** | **No — `DC-01` breaches it directly and unboundedly** |

**The reference product's manufacturing cost model does not satisfy the canonical
principle.** SMEsPlus must not inherit its cost-injection structure. That is a statement
about the reference product, not an approval of any replacement: no replacement design is
authorised by this session.
