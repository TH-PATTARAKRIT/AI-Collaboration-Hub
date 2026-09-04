# 11 — ALLOCATION DRIVER DECISION MATRIX (LEVEL 13)

**LAYER 2 — AUDIT QUARANTINE.** Content is **DESIGN CANDIDATE**.

Per the prompt: no universal winner is declared unless the evidence supports one. It
supports one on a narrower question than the prompt asks — see §5.

---

## 1. Candidates evaluated

The three controlled candidates from `BD-04`, plus one that the evidence forced onto
the list.

| ID | Driver | Definition |
|---|---|---|
| `D1` | **Machine hour** | Hours a **specific machine** ran, at machine grain |
| `D2` | **Work-centre hour** | Hours a **work centre** ran, machines undifferentiated |
| `D3` | **Production quantity** | Units produced |
| `D4` | **Normal-capacity machine hour** | Machine hours, with the **rate denominator fixed at normal capacity** rather than actual hours |

`D4` is not a fourth basis of measurement — it is `D1` with the statutorily required
denominator. It is listed separately because the distinction between "what we measure"
and "what we divide by" is exactly the distinction the reference product loses (`07` §6),
and keeping them separate is the point.

## 2. The matrix

Scored against the thirteen criteria the prompt requires.

| Criterion | `D1` Machine hour | `D2` Work-centre hour | `D3` Production quantity | `D4` Normal-capacity machine hour |
|---|---|---|---|---|
| **Business meaning** | The job carries the machines it used | The job carries the department average | The job carries a share by volume | As `D1`, with idleness correctly excluded from product cost |
| **Accounting suitability (TAS 2 ¶13)** | **Non-compliant for fixed overhead** if the denominator is actual hours | Non-compliant, same reason | Non-compliant, same reason, and worse — quantity varies with output by definition | **Compliant** |
| **Manufacturing suitability** | High | Medium | Low where products differ in machine intensity | High |
| **Data required** | Machine identity on the operation; time logs at machine grain | Already captured | Already captured | As `D1`, plus a normal-capacity figure per machine |
| **Measurement reliability** | Depends on operator capture; high where a work centre holds one machine | High — already automatic | High | As `D1` |
| **Implementation complexity** | **High** — two absent links must be built | **None** — it is what exists | Low | **High** — as `D1` plus the capacity register |
| **Manipulation exposure** | Moderate — misreported machine identity shifts cost between jobs | Low — nothing to misreport | Low | Moderate, **plus a new one**: normal capacity is a management estimate, and lowering it inflates absorbed cost and inventory. This is the classic overhead-absorption abuse |
| **Auditability** | Good — each allocation traces to a machine, a period and logs | Poor for the question asked — the average cannot be decomposed | Good arithmetically, weak causally | **Best** — the reconciliation in `09` §8 closes to zero and exposes the estimate |
| **Missing-data behaviour** | **Dangerous** — a log with no machine is silently unallocated. Needs an explicit rule | Cannot occur | Cannot occur | As `D1` |
| **Multi-order behaviour** | Correct — hours split naturally | Correct | Correct | Correct |
| **Multi-equipment behaviour** | **Correct — this is the reason to choose it** | **Fails — the whole point of `BD-03`** | Fails, differently | Correct |
| **Downtime behaviour** | Downtime carries no hours, so no cost attaches — but nothing classifies it | Same | Downtime invisible | **Correct** — downtime becomes the classified remainder (`09` §4) |
| **Period-close behaviour** | Rate moves monthly; orders spanning month end are ambiguous (`13` §3) | Same | Same | Same, but the rate is **stabler** because the denominator does not move with output |

## 3. What the evidence decides, and what it does not

**Decided by evidence:**

1. `D2` is **eliminated for the fixed component**. Not on preference — it structurally
   cannot answer "which machine", which is `BD-03`'s requirement, and the elimination
   survived a serious challenge in `07` §3.
2. Any driver with an **actual-output denominator** is eliminated for the **fixed**
   component, by TAS 2 ¶13. That removes `D1`-as-usually-implemented and `D3` from that
   role.
3. `D4` is therefore the **only compliant driver for depreciation**. This is a genuine
   universal result within its scope, and it is worth being clear that it comes from
   statute, not from analysis preference.

**Not decided by evidence:**

- The driver for **variable** overhead. TAS 2 ¶13 requires variable overhead to be
  allocated on the **actual use** of the production facilities, which admits `D1`, `D2`
  or `D3` depending on what the cost actually varies with. Electricity varies with
  machine hours; consumable packaging varies with quantity. **This is where `BD-04`'s
  per-context selection belongs**, and where a universal winner would be wrong.

## 4. The declared departure from `BD-04`

`BD-04` says one primary allocation method is selected per customer/configuration
context, unless evidence demonstrates a justified multi-driver model.

**The evidence demonstrates one, and the justification is statutory.** TAS 2 ¶13
prescribes *different* bases for two classes of cost:

| Cost class | Required basis | Driver |
|---|---|---|
| **Fixed** production overhead, including machine depreciation | **Normal capacity** of the production facilities | `D4` — fixed |
| **Variable** production overhead | **Actual use** of the production facilities | `D1`, `D2` or `D3` — configurable |

A single driver cannot serve both. The departure is therefore **one driver per cost
class**, with configurability retained **within** the variable class — which is narrower
than a free combination and does not create the arbitrary combinations `BD-04` forbids.

**Boss confirmation of this departure is requested at the Final Gate.**

## 5. Recommendation

| Cost class | Driver | Status |
|---|---|---|
| Machine depreciation and other fixed production overhead | **`D4` — normal-capacity machine hour** | Recommended; statutorily required |
| Variable production overhead | Configurable among `D1`/`D2`/`D3` per cost element | Recommended; per-context, per `BD-04` |
| Where a work centre holds exactly one machine | `D4` with the machine defaulted from the work centre | Recommended — removes the capture burden where there is no ambiguity |
| Where machine identity is genuinely uncapturable | **Do not silently fall back to `D2`.** Record the allocation as unattributed and report it | Recommended — a silent fallback would reintroduce the averaging `BD-03` rejects, invisibly |

## 6. The new risk this introduces, stated plainly

Choosing `D4` creates a control problem the other drivers do not have: **normal capacity
is a management estimate that directly determines how much cost is capitalised into
inventory.** Lower it and more cost is absorbed into stock and less hits the period.
That is the standard overhead-absorption abuse, and it is the reason TAS 2 ¶13 exists
in the form it does.

Three controls, all cheap, all recommended:

1. Normal capacity is a **dated, attributed record** — never an editable field.
2. It is **reviewed annually**, alongside the useful-life and residual review TAS 16
   already mandates. No new governance ceremony is created.
3. The reconciliation in `09` §8 **reports the absorption ratio** every period. A
   machine absorbing consistently more or less than its depreciation is visible
   immediately, which is the entire point of computing the remainder rather than
   spreading it.
