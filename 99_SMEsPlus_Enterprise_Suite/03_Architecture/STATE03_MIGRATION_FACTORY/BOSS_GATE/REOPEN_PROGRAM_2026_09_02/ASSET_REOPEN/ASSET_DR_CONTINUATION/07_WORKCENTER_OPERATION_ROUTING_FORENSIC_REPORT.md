# 07 — WORK CENTRE / OPERATION / ROUTING FORENSIC REPORT (LEVEL 10)

**LAYER 2 — AUDIT QUARANTINE.**

The prompt requires the hypothesis *"Work Centre = Cost Bucket"* to be **challenged**,
and the four-role alternative to be adopted only if it survives challenge. Both are
done here, in that order, and the challenge is run seriously rather than for form.

---

## 1. What each object actually is, from source

| Object | What it is | Key evidence |
|---|---|---|
| **Work centre** | A *resource* with a working calendar, a default capacity, setup and cleanup times, a time-efficiency factor, an OEE target, a list of alternative work centres, per-product capacities, and **one hourly cost scalar** | It inherits a calendar resource; the rate is a single float |
| **Routing / Operation** | A step on a bill of materials: a name, a **work centre**, a sequence, a duration model, a worksheet, and dependencies on other operations | Full field list read; **no equipment reference exists** |
| **Work order** | The execution of one operation for one manufacturing order: a work centre, a state, an expected duration, an actual duration, a set of time logs, and a rate field written at completion | Field list and completion path read |
| **Time log** | The atom of evidence: a work centre, an **optional** work order, an optional user, a **blocking reason**, a category, a start, an end, and a duration | Model read in full |
| **Blocking reason** | A named cause, tied to one of four **effectiveness categories**: availability, performance, quality, productive | Model and selection read |

## 2. What actually proves a machine was used — the question the prompt asks

| Claim to be proven | Proof available in the reference product | Grain |
|---|---|---|
| A work order ran | Yes — the work order and its state | Work order |
| For how long | Yes — the sum of its time logs' durations | Work order |
| Started and ended when | Yes — each log carries a start and end timestamp | Log |
| **On which machine** | **No.** The log names a *work centre*, never a machine | — |
| How much was produced | Yes — quantity produced on the work order | Work order |
| Setup time | Partly — setup and cleanup times exist as work-centre and per-product parameters, and setup can be a blocking reason, but setup is not separately timed by default | Mixed |
| Downtime, and why | **Yes** — a time log with a blocking reason and a category | Work centre |
| Interrupted by maintenance | Indirectly — maintenance blocks the calendar; the interruption is a *leave*, not a log | Work centre |
| Material consumption | Yes — through stock moves | Order |

**The decisive row is the third.** Every measurement in the product resolves to a work
centre. The machine dimension does not exist anywhere in the measurement chain — not
on the operation, not on the work order, not on the time log.

## 3. The challenge: could *Work Centre = Cost Bucket* be right after all?

Stated at its strongest, the case **for** keeping the work centre as the cost bucket:

1. It is where the reference product already puts the rate, and the entire absorption
   machinery downstream already works from it.
2. If a work centre contains machines of similar cost and similar throughput, averaging
   across them is an acceptable approximation — and cost accounting is full of
   defensible approximations.
3. It requires no new data capture. Machine-grain capture requires operators to record
   which machine they used, which is a real operational burden with a real error rate.
4. TAS 2 ¶13 requires allocation on **normal capacity of the production facilities** —
   a phrase that reads naturally at facility, not machine, grain.

That case is coherent, and point 4 is the strongest thing anyone has said for it.

### Why it fails

**It fails on the business requirement, not on the accounting.** `BD-03` and the Boss's
toll-gate concern are that a job should carry the cost of the machines it *actually
used*. Averaging is precisely the operation that destroys that information, and it
destroys it irreversibly — no downstream report can recover which machine ran from an
average that has already been struck.

The failure is sharpest where the money is largest. A work centre holding one
twenty-million-baht CNC machine and two three-hundred-thousand-baht manual stations
charges every job the same rate. A job that ran entirely on a manual station is charged
for the CNC. That is not an approximation of the truth; it is a different answer.

Point 4 does not rescue it either: normal capacity governs the **denominator** of the
fixed-overhead rate. It says nothing about the grain at which the **numerator** — the
cost pool — is assembled. A per-machine pool with a per-machine normal capacity is
fully compliant, and more informative.

**Ruling: the hypothesis is rejected on evidence.** Not because the four-role model is
more fashionable, but because the cost bucket model cannot answer the question the
business asked, and the four-role model can.

### What survives from the challenge, and must be kept

Two things, and they are not concessions:

1. **Machine-grain capture is a real operational cost.** `19` §3 therefore makes the
   machine dimension **required on the operation** but permits a work centre holding
   exactly one machine to default it. Most SME work centres hold one machine. The
   burden falls only where the ambiguity is real.
2. **The work centre remains necessary.** It is the scheduling resource, the calendar
   owner, the capacity constraint and the alternatives group. Dissolving it would break
   scheduling. The work centre is not deleted; it is **demoted from cost bucket to
   resource group**.

## 4. The downtime taxonomy — an asset the baseline did not surface

The reference product already carries a structured downtime model:

- Every interval of a work centre's time may be recorded as a **time log**.
- A log may carry a **blocking reason** — a named, user-extensible cause.
- Every reason belongs to one of four **effectiveness categories**: availability,
  performance, quality, productive.
- A log's work-order reference is **optional**, so an interval with **no production at
  all** is recordable. Idle time is expressible.
- Duration is computed against the work centre's **working calendar** for
  non-productive categories, and against wall-clock for productive ones — so a
  weekend does not silently become downtime.

This is the mechanism `BD-02` needs, and it already exists. It carries **no cost**, which
is the gap — not the absence of structure.

### Mapping the Boss's causes onto it

| `BD-02` cause | Category | Source of the record |
|---|---|---|
| MAINTENANCE — **planned** | availability | Maintenance request, type *preventive* → calendar leave |
| MAINTENANCE — **unplanned** (`BLK-08` split) | availability | Maintenance request, type *corrective* |
| BREAKDOWN | availability | Blocking reason on a time log |
| IDLE | availability | Calendar time with no log and no leave |
| NO_DEMAND | availability | Calendar time with no scheduled work order |
| SETUP | productive or performance — a design choice, see below | Setup time, or a blocking reason |
| STOPPAGE | availability or performance | Blocking reason |
| OTHER | any | Blocking reason |

**Two mapping decisions are not derivable from evidence and are marked as candidates
in `09` §4:** whether SETUP is productive (absorbed) or not, and whether IDLE and
NO_DEMAND are one cause or two. Both are policy.

**The general ruling is derivable, and it is this:** SMEsPlus should **reuse this
taxonomy's shape** — extensible named causes, each classified into a small fixed set of
categories — rather than hard-coding the Boss's seven values as an enumeration. The
Boss's seven become the seeded data; the categories become the thing the costing engine
switches on. Hard-coding the seven would require a code change the first time a customer
needs an eighth.

## 5. What is measured against what — the capacity picture

| Concept | Where it lives | Notes |
|---|---|---|
| Working calendar | The work centre's resource | Defines available time |
| Leaves | Calendar leaves | Maintenance writes these |
| Default capacity | Work centre | Units producible in parallel |
| Per-product capacity | A separate capacity record | Overrides the default per product |
| Time efficiency | The work centre's resource | Scales expected duration |
| OEE | Computed | **Over the last month, from time logs, not stored** |
| **Normal capacity** | **Nowhere** | Does not exist — see §7 |

## 6. The rate: one scalar doing two jobs

The work centre's hourly cost is a single number, and every consumer multiplies it by a
duration. That number is simultaneously:

- the **cost pool** — what the resource costs to run, and
- the **allocation basis** — the rate at which cost attaches to output.

Merging them is why the reference model cannot answer "which machine": once the pool is
expressed as a rate per work-centre hour, machine identity is already gone.

**This is also why the model cannot comply with TAS 2 ¶13.** A single rate cannot be
simultaneously a normal-capacity rate for the fixed component and an actual-usage rate
for the variable component. See `12` §3.

## 7. The exhaustive negative that matters most

A search of the entire 797-module reference product for any normal-capacity,
absorption-variance, or over/under-absorption mechanism returns **nothing**. Not in the
manufacturing modules, not in the manufacturing-accounting bridge, not in stock
valuation, not anywhere.

`FACT VERIFIED` (negative), bounded by the workspace as every negative in this package is.

**Consequence.** The product computes an absorbed amount and never computes what it
should have been. There is no variance because there is no standard to vary from. Since
TAS 2 ¶13 requires the normal-capacity basis and requires the unallocated remainder to
be expensed, **the reference product cannot produce a compliant fixed-overhead
allocation at all**, and no configuration of it can. This is not a gap SMEsPlus should
fill by extension; it is a mechanism SMEsPlus must own.

## 8. Level 10 conclusions

1. Work centre, operation, work order and time log are all real, well-built objects.
   **None of them carries a machine.**
2. The measurement chain is complete and trustworthy at **work-centre grain** and
   silent at **machine grain**.
3. *Work Centre = Cost Bucket* was challenged at its strongest and **fails on the
   business requirement**; the work centre survives as a **resource group**.
4. A reusable, well-shaped **downtime taxonomy already exists** and carries no cost.
   `BD-02` should adopt its shape rather than a fixed enumeration.
5. The single hourly rate **merges the cost pool with the allocation basis**, which is
   both why machine identity is lost and why the statutory split cannot be expressed.
6. **Normal capacity does not exist anywhere in the product.** This is the largest
   single mechanism SMEsPlus must build.
