# P04 — DEPRECIATION DATE / DAY CONVENTION

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P04-02`, `BLK-01`. Source basis **series 18**; population
basis **series 16** (`MD-P04-01` §4). **Thai statutory interpretation is not attempted here —
it is P07's.**

---

## 1. Three settings, not two

`prorata_computation_type`, `required=True`, `default='constant_periods'`:

| Value | Label | Behaviour |
|---|---|---|
| `none` | No Prorata | full period charged regardless of in-service date |
| **`constant_periods`** | Constant Periods | **the default** — 30/360 with real-length boundary scaling (§2) |
| `daily_computation` | Based on days per period | real calendar days (§2) |

> **Correction to this package.** `BLK-01` and the L1–L6 inheritance describe **two**
> conventions — *"30/360 default vs calendar"*. There are **three**; `none` is a third,
> and it is not a rounding variant, it is the absence of proration. Recorded as a
> **correction, not a restatement** (`P04-REV-79`).

## 2. The two day-count implementations, verbatim

```
def _get_delta_days(self, start_date, end_date):
    if self.prorata_computation_type == 'daily_computation':
        return (end_date - start_date).days + 1
    else:
        start_date_days_month = end_of(start_date, 'month').day
        start_prorata = (start_date_days_month - start_date.day + 1) / start_date_days_month
        end_prorata   = end_date.day / end_of(end_date, 'month').day
        return sum((start_prorata * 30, end_prorata * 30,
                    (end_date.year - start_date.year) * 360,
                    (end_date.month - start_date.month - 1) * 30))
```

**`DAYS_PER_MONTH = 30`, `DAYS_PER_YEAR = 360`** — module constants.

> **`P04-F-147`. The non-daily branch is not 30/360. It is a hybrid: the two boundary months
> are scaled by their REAL length and then expressed in 30-day units; only the interior is
> synthetic.** A February start is divided by 28 or 29 and multiplied by 30; a 31-day month is
> divided by 31 and multiplied by 30. **The published description *"30/360"* understates the
> precision of the boundary and overstates the uniformity of the whole.** `FACT VERIFIED`,
> series 18.

**Inclusivity differs between the two branches and between two uses of the same idea:**

| Quantity | Expression | Inclusive of both endpoints? |
|---|---|---|
| per-period delta, daily | `(end - start).days + 1` | **yes** |
| asset lifetime, daily | `(prorata_date + N months - prorata_date).days` | **no `+1`** |
| asset lifetime, non-daily | `method_period × method_number × 30` — exactly 1800 for 5 years | n/a, synthetic |

> **Flagged, not asserted as a defect.** A per-period count that includes both endpoints and a
> lifetime that includes one is an off-by-one **candidate**; proving a real over- or
> under-charge requires running the accumulation to the final period, and the final period is
> governed by `_get_depreciation_amount_end_of_lifetime`, which was **not** traced in this run.
> **`UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`, routed as `P04-B-52`** with the exact
> function named. It is bounded and cheap for whoever picks it up; it was not opened here
> because §4 forbids widening and it is not needed to answer `CQ-P04-02`.

## 3. What the deployments actually use

| Identity | Series | Real assets | On `daily_computation` |
|---|---|---:|---|
| `iSMEs` | **v16** | 669 (685 incl. templates) | **683 of 685** |
| `idemo18_uat` | **v18** | 388 | **375 of 388** |
| `iEVING`, `BK12MAY26`, `iTEST02` | v19 | templates only | templates on `constant_periods` |

> **The estate overwhelmingly runs the non-default setting.** Two independent populations, two
> generations, the same shape. **The product default is `constant_periods`; the estate is on
> `daily_computation`.** `FACT VERIFIED`.
>
> **The generation split is stated on the same line as the claim** (`MD-P04-01` §4): the
> *usage* is a v16 and v18 data fact; the *implementation* in §2 is a v18 source fact. No v16
> source exists on this host to confirm the v16 implementation, and this package does not
> assert one.

## 4. Rounding and boundary

`_get_delta_days` returns a **float** in the non-daily branch (`13.548387…` in the module's own
worked example) and an **int** in the daily branch. Rounding to currency happens downstream in
`_compute_board_amount`, which was traced only far enough to establish that it consumes
`days_already_depreciated` and a period day-count. **Per-line rounding policy is not closed** —
it is not required by `CQ-P04-02`, which asks for the day convention, and opening it would
widen the run.

## 5. Statutory question — routed, not answered

Whether Thai tax law requires or permits either convention is **not decided here**. The
estate's own choice (`daily_computation`, both populations) is a **fact about configuration,
not evidence of a legal requirement**. **Routed to P07** with the mechanism stated. This
package's standing position is unchanged: `P04-LAW-A` is an explanatory manual, not the
standard, and the gazetted TAS 16 text remains unretrieved (`P04-B-30`).

## 6. Disposition

> **`CQ-P04-02` — `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** for the implementation and
> the deployed usage, bounded by generation.
> **`BLK-01` remains ANSWERED-NOT-CLOSED**: what the populations use is now measured twice; the
> statutory question that keeps it open is **P07-owned**.
> Two derived items are terminally routed rather than left vague: `P04-B-52` (inclusivity),
> and per-line rounding, declared out of scope for this CQ.
