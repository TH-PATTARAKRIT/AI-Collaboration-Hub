# 16 — DEPRECIATION ENGINE FORENSIC
**LAYER 2 — AUDIT QUARANTINE**

Primary source: reference ERP v18 Enterprise asset model, board-computation
section (≈200 lines across six methods). Every formula below is transcribed from
that source, not from documentation.

## 1. The engine's actual shape

The engine is **not** "amount per period × number of periods". It is a
**cumulative-difference** engine:

> For each period, compute what *total* depreciation the asset **should have
> reached** by the end of that period, and post the difference against what it has
> already reached.

```
amount_this_period =
      round( base × days_from_start_to_period_end   ÷ lifetime_days )
    − round( base × days_from_start_to_period_start ÷ lifetime_days )
```

This single design decision has three consequences that matter more than the
formula itself:

1. **Rounding cannot drift.** Each period re-anchors on the cumulative total, so
   a half-satang error in period 7 does not propagate to period 8. Verified
   numerically in `40`: every scenario tested sums to the depreciable base **to
   the exact cent**, with no final-line plug.
2. **There is no "amount per period" to look up.** Any SMEsPlus design that stores
   a per-period depreciation rate is storing a derived number, not the mechanism.
3. **The last line is not special.** It is not a balancing figure. It falls out of
   the same formula, and is then *capped* at the residual by two independent
   guards (see §5).

`FACT VERIFIED`

## 2. The three depreciation methods

| Method | Per-period amount | Notes |
|---|---|---|
| **Straight line** | The cumulative-difference formula above, on `original − salvage` | Default |
| **Declining** | Depreciate down to `residual_at_year_start × (1 − factor × elapsed_days ÷ days_in_fiscal_year)`, then take the larger of that and a linear comparison | Rebases at each **fiscal year** boundary, not at each period |
| **Declining then straight line** | Same as declining, but the linear comparator is the true straight-line amount, so the schedule automatically switches to straight-line at the crossover | The switch is **not** a configured date. It is `max(degressive, linear)` evaluated every period |

The switching condition asked for by §23.3 is therefore: **the method switches on
the first period where the straight-line amount exceeds the declining amount**,
which the code achieves without ever detecting the switch explicitly.

`FACT VERIFIED`

## 3. The three prorata computation modes — the critical field

This is the single most consequential field on the asset. It selects between two
**incompatible day arithmetics**, both implemented in one helper.

### 3.1 Mode: *Constant Periods* (the product default)

A **30/360** convention.

```
days_between(start, end) =
      30 × (days remaining in start month ÷ length of start month)
    + 30 × (day-of-month of end ÷ length of end month)
    + 360 × (year difference)
    + 30  × (month difference − 1)
```

`lifetime_days = periods × months_per_period × 30`

**Every month is 30 days. Every year is 360 days. February and January are
identical. Leap years do not exist.** A 60-month asset has a lifetime of exactly
1800 days regardless of when it starts.

### 3.2 Mode: *Based on days per period*

A **true calendar** convention.

```
days_between(start, end) = (end − start).days + 1        # inclusive both ends
lifetime_days = (prorata_date + N months) − prorata_date  # real calendar days
```

A 60-month asset starting 2026-01-15 has a lifetime of **1826** days — 1825 plus
the 2028 leap day.

### 3.3 Mode: *No Prorata*

Not a third arithmetic. It uses the 30/360 arithmetic and additionally forces the
prorata date back to **the first day of the fiscal year** containing the
acquisition. A machine bought in November depreciates as though bought in January.

`FACT VERIFIED` — all three, from the mode-switching helper and the lifetime
computation.

### 3.4 What the difference is worth

Asset 1,200,000.00 · 60 months · straight line · acquired 2026-01-01
(`EV-SIM`, reproduced in `40` T01–T04):

| Period | Calendar days | *Based on days* | *Constant periods* | Difference |
|---|---|---|---|---|
| Jan 2026 | 31 | 20,372.40 | 20,000.00 | +372.40 (+1.86%) |
| **Feb 2026** | **28** | **18,400.87** | **20,000.00** | **−1,599.13 (−8.00%)** |
| Apr 2026 | 30 | 19,715.23 | 20,000.00 | −284.77 (−1.42%) |
| **Feb 2028** | **29** | **19,058.05** | **20,000.00** | **−941.95 (−4.71%)** |
| **FY2026 total** | | **239,868.57** | **240,000.00** | **−131.43 (−0.05%)** |

**Read that table carefully, because it contains the most practically important
finding in this deliverable.**

The **annual** difference is negligible — 0.05%. Anyone checking the choice against
a year-end tax computation would see nothing wrong.

The **monthly** difference is not negligible — up to **8% in February**.

The Boss's design routes depreciation into **monthly** production cost. Under the
default mode, February's machine cost is overstated by 8% and January's is
understated by 1.9%, every year, forever — and it will never show up in an annual
reconciliation. For a concrete producer whose February volumes differ from
January's, that is a real distortion of unit cost.

**This alone justifies making the computation mode an explicit, deliberate
SMEsPlus decision rather than an inherited default.**

## 4. Duration semantics — §23.4 answered

`method_number` is **the number of periods**, not months and not years. Period
length comes from a *separate* field with two legal values (1 or 12 months).

- `method_number = 60`, period = 1 → 60 monthly periods = 5 years
- `method_number = 60`, period = 12 → 60 **yearly** periods = 60 years

The field is labelled *Duration* in the UI. See `04` §4 `UI-01`.

The asset's last day is `prorata_date + (periods × months) − 1 day`, shifted
forward by any accumulated pause days.

`FACT VERIFIED`

## 5. Period boundaries, and why 60 months gives 61 lines — §23.6

A period ends at:
- the **end of the month** containing its start, for monthly assets;
- capped by the **fiscal year end** in all cases.

The loop runs while `residual ≠ 0` **and** `period_start < final_period_end`.

Therefore, for an asset acquired mid-month with a 60-month duration:

```
partial first period (acquisition date → end of that month)
+ 59 full months
+ partial final period (1st of the last month → the asset's last day)
= 61 lines
```

Reproduced exactly (`40` T06). 1,200,000 / 60 months / acquired 2026-01-15:

| | *Constant periods* | *Based on days* |
|---|---|---|
| Lines | **61** | **61** |
| First (15–31 Jan) | 10,967.74 | 11,171.96 |
| Last (Jan 2031) | 9,032.26 | 9,200.44 |
| **First + last** | **20,000.00** | **20,372.40** |
| A full period | 20,000.00 | 20,372.40 (31-day month) |
| Total | 1,200,000.00 | 1,200,000.00 |

**§23.7 reconciliation holds exactly.** Partial first + partial final = one full
period, to the cent, in both modes. There is no rounding residue to explain.

An asset acquired on the **first** of a month produces exactly 60 lines. The 61st
line is caused by mid-month acquisition, not by an off-by-one defect.

`FACT VERIFIED` (source) + `SUPPORTED INTERPRETATION` (the numbers, from `EV-SIM`)

## 6. Rounding — §23.8

Four separate mechanisms, in order:

1. **Currency rounding** on the cumulative amount and again on the difference.
2. **Residual cap:** `amount = min(computed, residual, key=abs)` — the period can
   never take more than is left.
3. **End-of-lifetime override:** if the residual is smaller than the computed
   amount, *or* if cumulative days have reached the asset's lifetime, the amount
   becomes **exactly the residual**. This is what closes the board to zero.
4. **Sign clamp:** positive assets can never post a negative period and vice versa.

**There is no unexplained rounding delta anywhere in the tested scenarios.** The
requirement in §23.8 is met by construction, not by a balancing entry.

`FACT VERIFIED`

## 7. Depreciable base — §24 answered precisely

| Term | Definition in source | Stored? |
|---|---|---|
| Original Value | Σ source bill line balances (÷ integer quantity if split) + non-deductible tax | Yes |
| Not Depreciable (salvage) Value | User-set, or `original × model percentage` | Yes |
| **Depreciable base** | `original − salvage` | No — computed |
| Depreciable Value (residual) | `original − salvage − imported − Σ posted depreciation` | No — computed |
| Accumulated depreciation | `Σ posted depreciation` (from the entries) | Not on the asset at all |
| **Book Value** | `residual + salvage + Σ children book values`, **minus salvage again once closed** | Yes, recursive |
| Gross increase value | Σ children original values | No |

Two traps for SMEsPlus, both confirmed from source:

- **Accumulated depreciation is not a field.** It exists only as a sum over posted
  entries. A migration that carries an "accumulated depreciation" number has
  nowhere to put it except the dedicated *already depreciated on import* field,
  which reduces the board **without producing any journal entry**.
- **Book value is recursive.** For a revalued asset it aggregates a tree.

`FACT VERIFIED`

## 8. What the engine does NOT do

| Absent capability | Confirmed by |
|---|---|
| Units-of-production / activity-based depreciation | Method selection has three values, none activity-based |
| Any second (tax) schedule | One board, one set of entries |
| Component depreciation | Value increases become children; original components cannot be split |
| Impairment | No such event |
| Depreciation holiday other than manual pause | — |
| Group / composite depreciation | The asset group field carries no behaviour |
| Mid-life change of computation mode with historical restatement | See `24` — history is **never** restated |

`VERIFIED GAP` for each.
