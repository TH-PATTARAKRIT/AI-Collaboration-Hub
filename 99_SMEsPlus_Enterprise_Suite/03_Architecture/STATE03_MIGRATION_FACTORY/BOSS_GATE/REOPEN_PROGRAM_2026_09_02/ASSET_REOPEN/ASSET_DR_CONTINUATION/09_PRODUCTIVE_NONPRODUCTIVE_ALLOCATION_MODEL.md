# 09 — PRODUCTIVE / NON-PRODUCTIVE ALLOCATION MODEL (LEVEL 11)

**LAYER 2 — AUDIT QUARANTINE.**
Design content in this document is **DESIGN CANDIDATE** unless marked otherwise.
Nothing here is approved, frozen or authorised for development.

---

## 1. The requirement

`BD-02`: every depreciation period is attributed 100%, split into productive and
non-productive, non-productive classified by cause, nothing carried forward, zero
unexplained balance.

TAS 2 ¶13 (standard text, obtained this session): fixed production overhead is
allocated on the basis of **normal capacity**; the per-unit amount **does not increase**
when production falls or ceases; **unallocated production overhead is recognised as an
expense in the period in which it is incurred**; in abnormally high production the
per-unit amount is reduced so that inventory is not carried above cost.

Both must hold simultaneously. They can.

## 2. Why the obvious model breaks the standard

The obvious reading of `BD-02` is:

```
rate = period depreciation ÷ period productive machine hours     ← WRONG
```

Under this reading 100% is always attributed, because the whole period's depreciation
is divided across whatever hours occurred. It is arithmetically tidy and it is
**non-compliant**: halve the month's hours and the per-hour charge doubles, which is
exactly the outcome TAS 2 ¶13 forbids. In an idle month it is also undefined —
division by zero — and in a very low month it capitalises normal-capacity idleness into
inventory.

**This reading must be rejected explicitly, because it is what a competent engineer
will build if the specification only says "attribute 100%".**

## 3. The model that satisfies both — recommended

Attribute 100% by **classifying** the period's depreciation, not by **spreading** it.

```
rate  =  period depreciation  ÷  NORMAL CAPACITY hours of the machine     ← fixed rate

Productive absorbed      =  actual productive hours × rate      → WIP → FG
Non-productive           =  period depreciation − productive absorbed
                            classified by cause, recognised as period expense
```

The identity closes by construction:

```
Productive absorbed + Non-productive  =  period depreciation      always, exactly
```

**Why this satisfies both requirements:**

| Requirement | How it is met |
|---|---|
| `BD-02` — 100% attributed | Non-productive is the arithmetic remainder. It cannot fail to close |
| `BD-02` — nothing carried forward | The remainder is recognised in its own period |
| `BD-02` — classified by cause | The remainder is decomposed by cause before posting — §4 |
| TAS 2 ¶13 — per-unit does not rise when output falls | The rate's denominator is normal capacity, which does not move with output |
| TAS 2 ¶13 — unallocated is expensed in period | The remainder **is** the unallocated overhead, and it is expensed |
| TAS 2 ¶13 — high output must not carry inventory above cost | See §5 — the one case needing an explicit cap |

**This is the design decision `BLK-07` asks the Boss to confirm.** It is a
recommendation, not an assumption: the alternative in §2 is stated so the choice is
visible.

## 4. Decomposing the remainder by cause

The remainder is not one number; it must arrive at the ledger already classified.

```
Non-productive hours  =  normal capacity hours  −  actual productive hours
```

Each non-productive hour is attributed to a cause from evidence, in this priority:

| Priority | Cause | Evidence source | Treatment |
|---|---|---|---|
| 1 | MAINTENANCE — **planned** | Maintenance request, type *preventive*, with a calendar leave | **Absorbed** — already inside normal capacity, see §6 |
| 2 | MAINTENANCE — **unplanned** | Maintenance request, type *corrective* | Period expense |
| 3 | BREAKDOWN | Time log with an availability-category blocking reason | Period expense |
| 4 | SETUP | Setup/cleanup intervals | **Policy — see below** |
| 5 | STOPPAGE | Time log with a blocking reason not classed above | Period expense |
| 6 | NO_DEMAND | Calendar-available time with no scheduled work order | Period expense |
| 7 | IDLE | Calendar-available time, scheduled but unworked, otherwise unexplained | Period expense |
| 8 | OTHER | Residual — **must be zero or explained** | Period expense, and **reported** |

**OTHER is a control, not a category.** A non-zero OTHER means evidence is missing.
The design should report it every period rather than let it absorb silently, because a
bucket that quietly accepts anything is how a reconciliation stops being one.

### Two policy questions, marked as candidates, not decided here

1. **Is SETUP productive?** Setup is real machine time attributable to a specific job.
   Treating it as productive attaches it to the job that caused it; treating it as
   non-productive spreads it. **Candidate: productive**, on the grounds that it is
   caused by, and traceable to, a job — but this is a Boss call.
2. **Are IDLE and NO_DEMAND one cause or two?** They differ in management meaning —
   no demand is a sales problem, idle is a scheduling problem — and not at all in
   accounting treatment. **Candidate: keep both**, because the management distinction
   is the reason the Boss listed them separately.

## 5. The abnormally-high-production case

TAS 2 ¶13 requires that in periods of abnormally high production the per-unit fixed
overhead be **reduced**, so inventory is not carried above cost.

With a normal-capacity denominator, actual hours can exceed normal capacity. Then:

```
Productive absorbed  =  actual hours × rate   >   period depreciation
```

and the remainder goes **negative** — the machine would absorb more depreciation than
exists. The identity still closes arithmetically, but a negative non-productive amount
is a credit to expense, which is over-absorption.

**Ruling — DESIGN CANDIDATE:** cap productive absorption at the period's depreciation.
Absorbed cost may never exceed the cost that exists. When the cap binds, the effective
per-unit rate falls, which is precisely what the standard requires, and the event is
**reported** because a bound cap means normal capacity is set too low.

## 6. Planned maintenance — why it is absorbed, not expensed

TAS 2 ¶13 defines normal capacity *"โดยคำนึงถึงกำลังการผลิตที่สูญเสียอันเกิดจากการ
บำรุงรักษาตามแผนที่วางไว้"* — taking into account capacity lost to **planned**
maintenance.

Planned downtime is therefore already **subtracted from the denominator** when normal
capacity is set. The rate is correspondingly higher, and planned-maintenance
depreciation is recovered through every productive hour. Expensing it *as well* would
charge it twice.

So the correct treatment is: **planned maintenance reduces normal capacity; it does not
generate a non-productive charge.** Unplanned maintenance and breakdown do the reverse:
they do not reduce the denominator, and they do generate a charge.

**This is `BLK-08`.** The Boss's list treats MAINTENANCE as one cause; the standard
requires two, with opposite treatments. Getting it wrong misstates inventory and period
expense in opposite directions simultaneously.

The data to make the split **already exists** — the maintenance request's
preventive/corrective type (`06` §4). No new capture is required.

## 7. Where each amount lands

| Amount | Destination | Statutory basis |
|---|---|---|
| Productive absorbed | WIP → finished goods → cost of sales | TAS 2 ¶12 — conversion cost |
| Unplanned maintenance, breakdown, stoppage, idle, no demand | **Period expense**, classified by cause | TAS 2 ¶13 — unallocated overhead |
| Planned maintenance | Absorbed through the rate | TAS 2 ¶13 — inside normal capacity |
| Depreciation of **non-production** assets | Period expense, outside this model entirely | TAS 16 |

The last row is a boundary that must be drawn before any of this runs: **only the
depreciation of assets used in the production process enters this model.** Office
equipment, vehicles and buildings not used in production go straight to expense. The
reference product has no such classification — the asset grouping object carries no
behaviour (`05` §2, row 3) — so SMEsPlus must add one.

## 8. Reconciliation report — mandatory, not optional

Every period, per machine, the design must be able to produce:

| Line | Source |
|---|---|
| Period depreciation | Asset sub-ledger |
| Normal capacity hours | Machine configuration, dated |
| Actual productive hours | Time logs at machine grain |
| Rate | Derived |
| Productive absorbed | Derived |
| Non-productive by cause, 8 lines | Derived + evidence |
| **Difference** | **Must be exactly zero** |

If this report cannot be produced for a machine, that machine's costing is not
trustworthy for that period, and the design should say so rather than publish a number.

## 9. What is not decided here

| Item | Status |
|---|---|
| The normal-capacity reading itself | **`BLK-07`** — Boss confirmation |
| Splitting MAINTENANCE planned/unplanned | **`BLK-08`** — Boss confirmation |
| Whether SETUP is productive | Candidate — Boss |
| IDLE and NO_DEMAND as one cause or two | Candidate — Boss |
| Who sets normal capacity, and how often it is reviewed | Candidate — `13` §6 proposes annually with the useful-life review TAS 16 already requires |
| The expense accounts for each cause | Chart-of-accounts decision, not research |
