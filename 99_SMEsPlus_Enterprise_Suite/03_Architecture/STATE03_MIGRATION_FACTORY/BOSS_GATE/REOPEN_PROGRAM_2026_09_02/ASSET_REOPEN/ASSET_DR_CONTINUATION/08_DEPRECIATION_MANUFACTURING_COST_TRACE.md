# 08 — DEPRECIATION → MANUFACTURING COST TRACE (LEVEL 11)

**LAYER 2 — AUDIT QUARANTINE.**

End-to-end trace: asset depreciation → equipment → production usage → operation →
manufacturing order → work in progress → finished goods, with every link classified as
**exists and works**, **exists and is wrong for our purpose**, or **absent**.

---

## 1. The chain, link by link

| # | Link | Status | Evidence |
|---|---|---|---|
| 1 | Vendor bill → asset | **Works** | Account-flag driven creation |
| 2 | Asset → depreciation entry | **Works, and well** | The schedule *is* the entries |
| 3 | Depreciation entry → expense account | **Works** | Two lines, accumulated depreciation and expense |
| 4 | Depreciation entry → analytic tag | **Works** | Copied from the asset at entry creation |
| 5 | Depreciation → **machine cost pool** | **ABSENT** | No cost pool object exists |
| 6 | Machine → work centre | Works | Many-to-one reference |
| 7 | Machine → **operation** | **ABSENT** | The operation has no equipment field |
| 8 | Depreciation → **hourly rate** | **ABSENT** | The rate is typed by a person |
| 9 | Work centre rate → work order cost | **Works** | `logged duration ÷ 60 × rate` |
| 10 | Time logs → work order duration | **Works** | Summed from logs |
| 11 | Time log → **machine** | **ABSENT** | Logs name a work centre |
| 12 | Work order cost → finished-goods unit price | **Works, conditionally** | See §3 — **only for FIFO and average costing** |
| 13 | Finished-goods price → stock valuation layer | Works | Standard valuation |
| 14 | Work-order cost → ledger entry | **Works** | A "labour" entry at order completion |
| 15 | Ledger entry ↔ time log | **Works** | Each log is stamped with its ledger line |
| 16 | Work-centre cost → analytic line | **Works, on a different basis** | See §5 — a second, divergent figure |
| 17 | Finished goods → cost of sales | Works | Standard |
| 18 | Absorbed vs actual **variance** | **ABSENT** | No such mechanism in 797 modules |
| 19 | **Normal capacity** | **ABSENT** | Does not exist |

**Ten of nineteen links exist and work.** The gaps are concentrated at the **front**
of the chain — 5, 7, 8, 11 — and at the **statutory control** end — 18, 19.

This is the finding that most changes the size of the work, and it is good news: the
absorption machinery from the rate onward is complete and reusable. What must be built
is the derivation of the rate, the machine dimension, and the compliance controls.

## 2. When depreciation becomes a monthly figure — arithmetic re-derived

Independently re-computed this session, not carried from the baseline. Asset value
1,200,000 THB, five years, straight line, acquired 1 January.

Lifetime in real calendar days: **1,826** (the span includes one leap day).

| Period | Days | Real-calendar basis | 30/360 basis | Difference |
|---|---|---|---|---|
| January (31 days) | 31 | **20,372.40** | 20,000.00 | +1.86% |
| **February (28 days)** | 28 | **18,400.87** | 20,000.00 | **−8.00%** |
| February 2028 (29 days) | 29 | **19,058.05** | 20,000.00 | −4.71% |
| **Full first year** | 365 | **239,868.57** | 240,000.00 | **−0.05%** |

The baseline's figures reproduce to the satang. `FACT VERIFIED` as arithmetic; the
transcription of the engine that produces them remains `SOURCE-SUPPORTED
INTERPRETATION` and should be confirmed against one real asset before migration.

**Why this belongs in a manufacturing-cost document.** Because the design routes
depreciation into **monthly** product cost, an 8% February error is an 8% error in
February's machine cost, every year, permanently — and the annual reconciliation that
would normally catch a systematic error differs by 0.05% and will never catch it.

## 3. When depreciation becomes manufacturing cost — the two moments

There are two, they are different, and the difference matters.

**Moment A — finished-goods valuation.** At manufacturing order completion, the sum of
work-order costs is added to the finished move's unit price, which flows into the stock
valuation layer.

> **Conditional, and the condition is not small.** This happens only where the product's
> cost method is FIFO or average. Under **standard costing, work-centre cost never
> enters the finished-goods value at all.** A design that assumes machine cost reaches
> inventory will be silently wrong for every standard-costed product.

**Moment B — the ledger.** After inventory is posted, a separate "labour" entry is
created: the work-centre expense account is credited and the stock-side account debited.

> **Conditional too.** This happens only where the product's valuation is real-time
> (perpetual). Under periodic valuation, no such entry exists.

**Both moments are at order completion, not when the machine ran.** A machine that ran
in January inside an order that completes in February contributes to **February's**
valuation and **February's** ledger entry. `13` §3 takes this up.

## 4. Does actual machine use drive the cost? — and the statutory answer

**In the reference product: yes, entirely.** The cost is logged duration × rate. No
production, no logged time, no cost. Scheduled availability contributes nothing.

**Under TAS 2 ¶13, that is correct for variable overhead and wrong for fixed overhead.**

The standard requires that fixed production overhead — which expressly includes the
depreciation of factory equipment — be allocated on the basis of **normal capacity**,
and states that the amount allocated per unit **shall not increase when production
falls or ceases**. Allocating a fixed monthly depreciation across that month's actual
hours does exactly what is forbidden: halve the hours and the per-hour charge doubles.

So the reference mechanism applies a **variable-overhead treatment to a fixed cost**.
It is not merely imprecise; for the depreciation component it does not comply.

**This is the single most consequential finding of the session for the design**, and it
is what raises `BLK-07`.

## 5. The two cost figures that can disagree

The product computes work-centre cost **twice**, on two different bases:

| Figure | Basis | Rate used | When |
|---|---|---|---|
| Valuation and ledger | Sum of time-log durations | **The work centre's rate at that instant** | Once, at order completion |
| Analytic line | Work-order duration | **The work centre's rate at that instant** | **Recomputed every time duration changes** |

Both read the live rate — **neither reads the rate field stored on the work order**.
That field is written at completion and is consumed only by expected/current-cost
reporting helpers. This corrects the baseline (`02` §4, `C-01`/`C-02`).

**The divergence.** The analytic figure is recomputed as time is logged; the valuation
figure is struck once at completion. If the work centre's rate changes between the last
time log and completion, the two figures disagree — and nothing reconciles them.

For a design that intends to derive the rate **monthly** from depreciation, the rate
will change every month by construction. Any order spanning a month end will produce
two different machine costs for the same work. `13` §3 specifies the rule.

## 6. What the chain does with each Boss scenario

| Scenario | Reference-product behaviour | Compliant with TAS 2 ¶13? |
|---|---|---|
| Machine runs normally | Cost = actual hours × rate → WIP → FG | Only if the rate is a normal-capacity rate |
| Machine idle all month | **Zero cost allocated. Depreciation sits in the expense account** | Accidentally yes — the standard also expenses it. But by omission, not design, and unclassified |
| Machine under maintenance all month | Same as idle. The calendar is blocked; no logs; no cost | Planned maintenance should be **inside** the rate (`BLK-08`); it is not |
| Breakdown mid-production | The interruption may be logged with a reason; the log carries **no cost** | Should be expensed and classified; it is neither |
| No demand all month | Same as idle | As above |
| Setup | Setup and cleanup times inflate expected duration; whether they are logged productively depends on configuration | Policy question (`09` §4) |
| Partial-month usage | Handled naturally — hours are hours | Yes |
| Two products share one machine | Each order carries its own hours × rate | Yes for variable; the fixed part is still misallocated |
| Two orders share one machine | Same | Same |
| **Two machines in one work centre** | **Indistinguishable.** Both charged at the work centre's average | **No — and this is `BD-03`'s point** |

## 7. The 100% attribution identity — does it hold today?

`BD-02` requires, for every period:

```
Total period depreciation  =  Productive allocation  +  Non-productive allocation
```

**In the reference product this identity is not computed, not enforced, and not
reportable.** There is no object that holds a period's total machine depreciation, no
object that holds the productive allocation, and no non-productive concept at all. The
depreciation lands in an expense account; the absorbed labour amount lands in a
different entry derived from an unrelated typed rate. **The two numbers have no
arithmetic relationship whatsoever.**

That is worth stating bluntly, because it is easy to assume the reference product does
something approximately right that merely needs refining. It does not. It runs two
independent mechanisms that happen to concern the same machines.

`09` specifies the model that makes the identity hold.

## 8. Level 11 conclusions

1. The chain is **ten of nineteen links complete**, with the gaps at the front and at
   the statutory-control end.
2. Depreciation becomes a monthly figure through a **day convention** whose default is
   wrong by 8% in February and right within 0.05% annually.
3. Machine cost enters finished goods at **order completion**, and **only under FIFO or
   average costing**; it reaches the ledger **only under real-time valuation**.
4. The product's allocation basis is **actual hours**, which is a **variable-overhead**
   treatment applied to a **fixed** cost, and does not comply with TAS 2 ¶13.
5. Two divergent machine-cost figures exist; the rate snapshot that appears to protect
   them **is not read by either**.
6. The 100% attribution identity **has no representation at all** in the reference
   product and must be built as a first-class reconciliation.
