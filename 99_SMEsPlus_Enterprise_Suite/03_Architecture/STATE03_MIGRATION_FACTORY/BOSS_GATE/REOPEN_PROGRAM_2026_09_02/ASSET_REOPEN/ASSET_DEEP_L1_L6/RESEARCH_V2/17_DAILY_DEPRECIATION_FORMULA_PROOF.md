# 17 — DAILY DEPRECIATION FORMULA PROOF
**LAYER 2 — AUDIT QUARANTINE**

This deliverable answers the question Expert 3 raised at Level 2 and that the
governing prompt raises at §59 and §78: **is the project's custom Thai daily
method reproducible by standard configuration, or is it a lost capability?**

## 1. Method note — read before using any number here

Everything in §3–§5 is `EV-SIM`: a line-by-line Python transcription of the two
algorithms from primary source, executed side by side. It is **not** a runtime
execution of either system. It is classified **`SUPPORTED INTERPRETATION`**.

What *is* `FACT VERIFIED` is the **algebra** — the formulas in §2, which are read
directly from source and do not depend on the simulation.

Assumption stated: fiscal year = calendar year. Not verified per company.

## 2. The two formulas, from source

### 2.1 Custom Thai method (legacy v14 line, project-authored)

The custom module overrides only the per-period amount. The **standard v14 board
loop wraps it**, and that wrapper is where the first-period proration happens.
Reading the two together — which the previous analysis of this module did not do —
the effective algorithm is:

```
first_of_month   = first day of the month containing the first depreciation date
lifetime_days    = (first_of_month + N months) − first_of_month        # real calendar days
amount_per_day   = depreciable_base ÷ lifetime_days

period_amount    = min( amount_per_day × calendar days in that month , residual )

if prorata and this is period 1:
        prorata_factor = (days in month − day-of-month + 1) ÷ days in month
        period_amount  = round(period_amount × prorata_factor)

if this is the last period:
        period_amount  = residual
if prorata:
        number of periods = N + 1
```

`FACT VERIFIED` — custom module amount override plus the standard v14 board loop
it runs inside.

**This correction matters.** Read in isolation, the custom override appears to
charge a **full month** in the acquisition month — including days before the asset
was acquired. That would have been a genuine statutory problem under Revenue Code
s.65 bis (2), which requires deduction *in proportion to the period **from the
acquisition***. Read together with its wrapper, the proration is applied and the
apparent problem does not exist. An earlier reading in this session reached the
wrong conclusion by looking at the override alone; the corrected finding is
recorded in `29` as `REV-06`.

### 2.2 Standard v18 *Based on days per period* mode

```
lifetime_days    = (prorata_date + N months) − prorata_date            # real calendar days
days(a,b)        = (b − a).days + 1                                    # inclusive

period_amount    = round( base × days(start, period_end)   ÷ lifetime_days )
                 − round( base × days(start, period_start−1) ÷ lifetime_days )
```

`FACT VERIFIED` — v18 board methods.

### 2.3 Are they the same formula?

Structurally, no. The custom method is **per-period independent**
(`per_day × days_in_month`, each period computed alone). The standard method is
**cumulative-difference** (§16 §1). They are different algorithms.

The question is whether they produce the same numbers.

## 3. Direct numerical comparison — `EV-SIM`

Asset 1,200,000.00 · 60 monthly periods · straight line · no salvage.

| Acquisition | Custom Thai lines | Standard-daily lines | Custom first line | Standard first line | Max per-period difference | FY-1 cumulative difference |
|---|---|---|---|---|---|---|
| 2026-01-01 (month start) | 60 | 60 | 20,372.40 | 20,372.40 | **0.03** | **0.01** |
| 2026-01-15 (mid-month) | 61 | 61 | 11,171.96 | 11,171.96 | **0.03** | **0.01** |
| 2026-02-20 (short month) | 61 | 61 | 5,914.57 | 5,914.57 | **0.03** | **0.01** |
| 2026-04-30 (month end) | 61 | 61 | 657.17 | 657.17 | **0.03** | **0.01** |

## 4. Finding

> **The project's custom Thai daily method and the reference product's standard
> *Based on days per period* mode are numerically equivalent to within currency
> rounding — a maximum of 0.03 THB in any single period and 0.01 THB cumulative,
> on a 1.2 million baht asset, across month-start, mid-month, short-month and
> month-end acquisitions.**

Both derive a per-day rate from the **real calendar length of the asset's life**
(1826 days for a 5-year asset spanning one leap day, not 1800), and both charge
each period by its **real calendar length** (28 / 29 / 30 / 31).

`SUPPORTED INTERPRETATION` — from `EV-SIM`. It should be confirmed by running one
real asset both ways on the UAT before any migration decision relies on it.

## 5. What this changes

This reverses the risk assessment carried into this deliverable from Level 2.

| | Before this proof | After this proof |
|---|---|---|
| Nature of the risk | A compliance capability was built in v14 and **lost** in the v18 migration | The capability is **reproducible by one configuration field**; the risk is that the field was not set |
| Severity | High — regression, needs redevelopment | **Medium — configuration verification** |
| Action | Port or rebuild a custom module | Check one field on 217 assets; correct it if wrong |
| Cost if unaddressed | Same either way: wrong monthly amounts | Same either way |

**The exposure is unchanged. The remedy is far cheaper than it appeared.**

And the cost of getting it wrong is quantified in `16` §3.4: if those assets were
migrated on the product **default** (*constant periods*, 30/360) instead, every
February is overstated by **8%** and every 31-day month understated by **1.9%**,
while the annual total stays within 0.05% — so **an annual reconciliation will not
detect it**. Only a monthly review will.

That is why `UNR-02` is the highest-priority open item in this session.

## 6. Boss assertion §78, adjudicated

The Boss's stated Source-Learning hypothesis was:

> 1. determine the duration; 2. determine start/prorata treatment; 3. determine
> total calendar days including leap year; 4. derive depreciation per day;
> 5. period depreciation = daily amount × actual applicable days.

**Against the custom Thai method: `CONFIRMED AGAIN`.** All five steps are exactly
what the code does.

**Against the standard *Based on days per period* mode: `CONFIRMED AGAIN`.** Same
five steps, reached by different arithmetic, same result.

**Against the reference product's default configuration: `CONTRADICTED`.** The
default is 30/360, in which step 3 is false (no leap year, no real months) and
step 5 is false (every period is 30 days).

The Boss's description of the *mechanism* is correct. What is not correct — and
this is the substance of `BA-01` in `38` — is the implicit assumption that the
mechanism is what the system does **by default**. It is one of three options, and
it is not the one selected out of the box.

## 7. Thai statutory position

See `26`. In summary:

- Pro-rating from acquisition is **statutory** — Revenue Code s.65 bis (2).
  `FACT VERIFIED`
- Royal Decree 145 s.4 requires computation according to the period the asset was
  held, pro-rated for part periods, and sets **maximum** rates by class.
  `FACT VERIFIED`
- That the pro-ration **unit** must be the *day* rather than the month is **not**
  stated in the primary text retrieved, which says *period* (`ระยะเวลา`). It is
  standard Thai practice and it is what both daily implementations do, but it is
  classified **`SUPPORTED INTERPRETATION`** and routed to the Accounting-Tax track
  as `HOLD / EVIDENCE REQUIRED`.

One point of fairness to the 30/360 default, established by working the
arithmetic rather than assuming: **it does prorate the acquisition month
correctly in proportion.** An asset acquired on the 15th of a 31-day month is
charged `17/31` of a period in both modes. The 30/360 mode is not "wrong about
the acquisition date".

Where it deviates is afterwards, in two places:

1. every **full** period is 1/60th of the base regardless of whether the month has
   28 or 31 days — the 8% February effect in `16` §3.4; and
2. the **lifetime** is 1800 notional days rather than the 1826 real days the asset
   actually lives, so the per-day rate itself is ~1.4% high.

Whether either deviation breaches "in proportion to the period from acquisition"
under s.65 bis (2) is an accounting/tax authority question, not a code question.
It is marked **`HOLD / EVIDENCE REQUIRED`** and routed to the Accounting-Tax
track. This package does not adjudicate it.
