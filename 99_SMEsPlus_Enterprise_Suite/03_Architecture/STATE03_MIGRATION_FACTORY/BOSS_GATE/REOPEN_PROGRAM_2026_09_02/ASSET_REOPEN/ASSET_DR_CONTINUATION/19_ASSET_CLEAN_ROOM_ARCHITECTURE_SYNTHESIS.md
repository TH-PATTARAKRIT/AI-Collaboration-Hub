# 19 — CLEAN-ROOM ARCHITECTURE SYNTHESIS (LEVEL 21)

**Written clean-room.** No reference-system model, field or file name appears in this
document. Every entity below is a **DESIGN CANDIDATE**. Nothing here is approved,
frozen, or authorised for development.

---

## 1. The four truths

The design rests on keeping four kinds of fact apart, because every serious failure mode
found in this research is a collapse between two of them.

| # | Truth | Question it answers | Authority |
|---|---|---|---|
| 1 | **Financial** | What did we pay, what is it worth now, what did we charge to profit? | TFRS, Revenue Code |
| 2 | **Operational** | Which physical machine exists, where is it, what state is it in, what did it do? | The business |
| 3 | **Costing** | How much of the financial truth attaches to which output? | TAS 2, and Boss policy within it |
| 4 | **Management** | What is this machine still contributing after its accounting life? | Boss policy alone |

Truth 3 reads from 1 and 2 and writes to the statutory ledger. Truth 4 reads from 1 and
2 and writes **only** to the management ledger. **Truth 4 never writes to truth 1.**

## 2. Asset domain

| Entity | Purpose | Notes |
|---|---|---|
| **Asset** | The capitalised financial record | Company **mandatory**. Value **derived**, never stored |
| **Asset component** | A depreciable part of an asset with its own life | **Required by the standard** (`18` §4). New — no precedent in the reference product |
| **Asset class** | Carries behaviour: statutory rate ceiling, default life, default method, and **production / non-production** | The reference product's equivalent carries **no** behaviour. This is a deliberate departure |
| **Depreciation schedule entry** | One period's charge | **Is** the ledger entry. Never a parallel table |
| **Asset event** | Acquisition, confirmation, pause, resume, re-evaluation, disposal, correction | Each a guarded transition, each recorded |

**Rules adopted, each traceable to a finding:**

1. Book value, accumulated depreciation and residual are **derivations**, never columns.
2. A posted entry is never edited. Catch up, reverse the future, rebuild forward.
3. Each period is computed from the **cumulative** total, so rounding cannot drift.
4. **The day convention is an explicit, recorded, per-asset decision** — never an
   inherited default, and never silently changed. Changing it is an event.
5. **The mode that backdates depreciation to the fiscal-year opening is not offered.**
   It produces a figure the Revenue Code does not permit (`05` §3).
6. Life and residual are **reviewed annually** and the review is recorded — required by
   the standard, and reused as the cadence for two other controls.
7. **Production / non-production is a first-class attribute of the asset class**, and it
   is the gate into the costing model (`12` §4).

## 3. Operational domain

| Entity | Purpose | Notes |
|---|---|---|
| **Machine** | The physical production resource | Company **mandatory**. **No monetary field of any kind** — a deliberate omission (`06` §4) |
| **Machine ↔ asset link** | Binds financial to operational | **Unique**, **same-company**, **bidirectional**, and **mandatory** for any machine in costing scope |
| **Machine assignment** | A **dated** record of machine-to-resource-group membership | Never a field. History is required, because cost attribution depends on it |
| **Resource group** | Scheduling, calendar, capacity, alternatives | What the reference product calls a work centre. **Demoted from cost bucket to resource group** |
| **Machine state** | commissioned · available · running · maintenance · breakdown · standby · disposed | Seven states. The reference product has an archive flag and a scrap date |
| **Site / plant** | Between company and resource group | New (`14` §7). Deferrable |
| **Usage-rights record** | Dated permission for another company to use a machine, with a charge basis | Replaces the accidental "leave the company empty" mechanism (`14` §4) |

**The cardinality rules, which are the heart of `BD-03`:**

- One asset **may** have many machines — required, because component depreciation and
  multi-station machines both need it.
- One machine has **exactly one** owning asset — enforced by constraint, not convention.
- One resource group has **many** machines.
- **An operation names a machine, not only a resource group.** Where a resource group
  holds exactly one machine, the machine defaults; where it holds several, it is
  required. This is the single structural change that makes per-machine costing possible.

## 4. Measurement

| Entity | Purpose |
|---|---|
| **Usage event** | An interval of machine time: machine, resource group, optional production order, optional operation, start, end, duration, and a **cause** |
| **Cause** | A named, extensible reason belonging to one of a small fixed set of **categories** |
| **Category** | productive · availability · performance · quality |
| **Normal capacity record** | A **dated** figure per machine per period, net of planned maintenance |

**Rules:**

1. A usage event with **no** production order is valid — that is how idleness is
   recorded.
2. Non-productive duration is measured against the **working calendar**, so non-working
   time never becomes downtime.
3. Causes are **data, not an enumeration in code.** The Boss's seven are seeded values;
   the costing engine switches on the **category**. An eighth cause must never require a
   code change.
4. **Planned and unplanned maintenance are different causes with opposite treatments**
   (`09` §6).
5. A usage event with **no machine identity** is recorded as **unattributed and
   reported**. It **never** falls back to a group average (`15` `EC-15`).

## 5. Costing

| Entity | Purpose |
|---|---|
| **Cost pool** | A machine's period cost, from the asset sub-ledger. Fixed and variable held **separately** |
| **Cost driver** | Per cost class: normal-capacity machine hour for fixed; configurable for variable (`11` §5) |
| **Allocation rate** | Derived, **dated**, immutable once struck |
| **Allocation event** | Productive absorption to a production order, or non-productive to a classified expense |
| **Period reconciliation** | Per machine, per period. **Must close to exactly zero** |
| **WIP cost record** | Value of work in progress at period end, by production order |

**Rules:**

1. `Period depreciation = productive absorbed + non-productive classified` — **exactly,
   every period, every machine.** A machine that does not reconcile does not publish a
   cost.
2. The fixed rate's denominator is **normal capacity**, never actual output (`18` §3).
3. Absorption is **capped** at the period's depreciation (`09` §5).
4. Hours are rated at the rate **in force when the hours were logged** — not at
   completion (`13` §3).
5. Cost is attributed to the period **the hours occurred in**, not the period the order
   completed in (`13` `T-01`).
6. **The `OTHER` cause is a control, not a bucket.** A non-zero balance is reported.

### The single-mechanism rule

**Exactly one mechanism may carry machine depreciation into product cost.** The research
found two already live in the reference product — a typed hourly rate, and a management
tag copied onto every depreciation entry — and this design proposes a third. Any two of
them running together double counts silently, and the reconciliation will still close,
because each mechanism reconciles against itself.

The design must therefore **name the authoritative mechanism and prove the others are
off**, as an explicit, tested condition — not as an assumption. This is `CTR-C-08`'s
sibling and, on the evidence, the most likely way this project produces a wrong number
that passes every check.

## 6. Management ledger

| Entity | Purpose |
|---|---|
| **Internal usage rate** | Dated, attributed, prospective only |
| **Internal usage accumulator** | Per machine. **Unbounded** (`BD-01`) |
| **Internal usage allocation event** | Mirrors the costing model, in the management ledger only |
| **Terminal contribution record** | Closes the accumulator at disposal (`10` §6) |

**Rules:**

1. Every management entry is composed **entirely** of off-balance accounts. Enforced
   structurally, on the pattern proven in `05` §7 — not by policy.
2. It begins **only after** statutory depreciation completes, detected from the derived
   residual reaching zero.
3. It is **suspended** while the asset becomes depreciable again (`10` §7).
4. It is **frozen and closed** at disposal.
5. It **never** updates a product cost, a standard cost, or an inventory valuation. This
   is the leak the account-class firewall does not cover (`15` `EC-27`).
6. Corrections are **dated entries**, never restatements.

## 7. Cross-cutting controls

| # | Control | Answers |
|---|---|---|
| 1 | **Three closes** — operational, costing, accounting — with a one-directional dependency | `13` §2 |
| 2 | Costing entries carry the **costing period's** date, and are refused if it is locked | `CTR-C-07` |
| 3 | **Every** posting path is lock-guarded, including asset confirmation | `05` §5 |
| 4 | System-controlled accounts refuse manual journals | `15` `EC-27` |
| 5 | **Sub-ledger to ledger reconciliation exists and is run** | Absent in the reference product |
| 6 | Every account selector on a costing object excludes off-balance accounts | `CTR-C-05` |
| 7 | Every rate, capacity and assignment is a **dated record**, never a mutable field | `CTR-C-06` |
| 8 | Cancellation **reverses**; it never deletes | `CTR-C-08` |
| 9 | No stored value without a consumer | `CTR-C-06` |
| 10 | Conversion cost enters inventory under **every** costing method | `CTR-C-09` |

## 8. Multi-company and tenancy

| # | Rule |
|---|---|
| 1 | **Company is mandatory and non-empty on every costing-relevant record.** No exceptions |
| 2 | Asset visibility is scoped **strictly** to the owning company. No parent traversal |
| 3 | The asset↔machine link is **same-company** and unique |
| 4 | Rates, pools and normal capacity are company-scoped |
| 5 | Cross-company machine use is a **dated usage-rights record with an explicit intercompany charge**. Never an implicit shared pool |
| 6 | **Tenant is not a field.** Tenant isolation lives above the application; a tenant-crossing query must not be **expressible** (`14` §6) |

## 9. What this design deliberately does not copy

Eleven refusals, each with a reason, at `16` §4. The three that most shape the
architecture:

1. **A single rate merging the cost pool with the allocation basis** — the reason the
   reference model cannot answer "which machine", and cannot express the statutory
   fixed/variable split.
2. **Company-optional master data** — safe in a corporate group, a disclosure in a SaaS.
3. **A stored snapshot that nothing reads** — a field that lies about the guarantee it
   provides.

## 10. Implementation order, and why

Unchanged in shape from the baseline's recommendation, with two insertions the new
statutory evidence forces.

| # | Step | Why here |
|---|---|---|
| 1 | **Repair and constrain the asset↔machine link** — unique, same-company, bidirectional, with a working disposal path | Everything keys on it, and today it is optional, duplicable and partly inert |
| 2 | **Give the operation a machine dimension** | Without it the machine-hour basis has no measurement |
| 3 | **Build the normal-capacity register** | **New.** Without it no compliant fixed rate can be struck at all — and no configuration of the reference product supplies one |
| 4 | **Derive the cost pool from the asset sub-ledger**, fixed and variable separately | The rate cannot be split without the pool being split |
| 5 | **Build the period reconciliation**, and make it the gate | `BD-02`'s identity has no representation today; without it nothing detects the double counting in §5 |
| 6 | **Handle timing** — hours-period attribution, WIP valuation, rate-in-force | `13` |
| 7 | Management ledger | Depends on 1–6 and on nothing else |

**Steps 1 and 2 remain unglamorous and remain the entire foundation. Step 3 is new, and
it is not optional.**
