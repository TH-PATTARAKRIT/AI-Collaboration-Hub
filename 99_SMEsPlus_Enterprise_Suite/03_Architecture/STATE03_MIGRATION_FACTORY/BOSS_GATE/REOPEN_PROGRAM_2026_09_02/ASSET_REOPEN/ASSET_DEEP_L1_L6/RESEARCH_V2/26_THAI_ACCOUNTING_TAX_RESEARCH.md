# 26 — THAI ACCOUNTING AND TAX RESEARCH
**LAYER 2 — AUDIT QUARANTINE**

§77 and §78. Researched independently of the reference system, from primary Thai
sources, and kept strictly separate from what the software does.

**Governing clean-room rule:** statutory Thai claims are `HOLD / EVIDENCE REQUIRED`
and route to the Accounting-Tax track. This deliverable **does not** issue Thai
accounting advice. It records what primary text says and what it does not say.

## 1. The four things that must never be merged

| # | Layer | Authority |
|---|---|---|
| A | What the reference ERP does | Its source code — Levels 1–6 |
| B | What Thai **accounting** requires | TFAC / TAS |
| C | What Thai **tax** requires | Revenue Code + Royal Decrees |
| D | What SMEsPlus should target | Boss decision |

Almost every confusion in this domain comes from treating A as if it were B or C.

## 2. Thai tax — primary text obtained

### 2.1 Revenue Code, Section 65 bis (2)

> *"Depreciation and depletion of assets shall be deductible under the rules,
> procedures, conditions and rates specified by a Royal Decree."*
>
> *"The depreciation and depletion of assets shall be deductible **in proportion to
> the period from the acquisition** of such assets."*

Source: Thai Revenue Department, official English text of the Revenue Code.
`FACT VERIFIED`

**What this establishes:** pro-rating from the acquisition date is **statutory**.
It is not a convention, a practice, or a software behaviour.

**What it does not establish:** the *unit* of that proportion.

### 2.2 Royal Decree No. 145 (B.E. 2527 / 1984), Section 4

> *"ให้คำนวณหักตามระยะเวลาที่ได้ทรัพย์สินนั้นมาในแต่ละรอบระยะเวลาบัญชี ในกรณีที่รอบระยะเวลาใดไม่เต็มสิบสองเดือนให้เฉลี่ยตามส่วนสำหรับรอบระยะเวลาบัญชีนั้น"*
>
> — computed according to the **period** during which the asset was held in each
> accounting period; where an accounting period is **less than twelve months**,
> apportioned accordingly for that period.

Maximum rates by class, as published:

| Asset class | Maximum rate |
|---|---|
| Durable/permanent buildings | 5% |
| Temporary buildings | 100% |
| Natural-resource extraction rights | 5% |
| Leasehold, renewable term | 10% |
| Leasehold, fixed term | 100 ÷ years |
| Goodwill, patents, trademarks — indefinite | 10% |
| Goodwill, patents, trademarks — definite term | 100 ÷ years |
| **All other depreciable assets** | **20%** |

Section 5 additionally caps passenger-vehicle depreciation at 1,000,000 baht of
cost, except for vehicle-rental businesses.

Issued 15 January B.E. 2527, published in the Royal Thai Government Gazette.
`FACT VERIFIED`

### 2.3 Rates are ceilings, not schedules

Corroborated by secondary professional guidance: where an entity's own accounting
rate is **lower** than the statutory maximum, the deduction is allowed only at the
entity's own rate. Straight line is the most common basis, and other generally
accepted bases are permitted.

`FACT VERIFIED` (that they are maxima) · secondary corroboration for the practice

**This is why the absence of a tax book matters** (`12` §7). Ceilings plus an
entity-chosen accounting life is exactly the condition that generates a book/tax
difference, and a system with one schedule cannot represent it.

## 3. The daily-basis question — adjudicated

The Boss's assertion is that Thai depreciation is computed on a **daily** basis:
total calendar days including leap years, a per-day amount, and each period charged
by its actual applicable days.

| Element | Status |
|---|---|
| Pro-rating from acquisition is required | **`FACT VERIFIED`** — s.65 bis (2) |
| Apportionment for part periods is required | **`FACT VERIFIED`** — RD 145 s.4 |
| The apportionment unit is specifically the **day** | **`SUPPORTED INTERPRETATION`** |
| 365/366 with real month lengths | **`SUPPORTED INTERPRETATION`** |

**Why not FACT VERIFIED:** the primary texts retrieved use *ระยะเวลา* / *period* and
*เฉลี่ยตามส่วน* / *apportion in proportion*. Neither uses *จำนวนวัน* / *number of
days*. A monthly apportionment is also "in proportion to the period".

**Why SUPPORTED and not merely asserted:** three independent lines of evidence
converge on the daily unit —

1. Thai professional and ERP-vendor practice guidance publishes the formula as
   `depreciation per day = (cost − accumulated − salvage) ÷ remaining life in days`,
   then `× days in the month`;
2. the project's own vendor **built a custom module implementing exactly that**,
   which is behavioural evidence of what the market expects;
3. it is the more conservative reading of "in proportion to the period from
   acquisition" — a daily apportionment satisfies a monthly requirement, but not
   the reverse.

**Classification: `SUPPORTED INTERPRETATION`. Routed to the Accounting-Tax track as
`HOLD / EVIDENCE REQUIRED`** for confirmation against a Revenue Department ruling
or departmental instruction. `UNR-01`.

This is an **upgrade** on the prior session, which reached the same classification
from secondary sources only; the statutory pro-ration requirement itself is now
`FACT VERIFIED` from primary text.

## 4. Thai accounting standards

TFAC-adopted standards on property, plant and equipment require depreciation over
useful life, a reviewed residual value, and component depreciation where components
have different useful lives.

Against the reference system:

| Requirement | Reference system |
|---|---|
| Depreciate over useful life | Yes |
| Residual value, reviewed | Held; **review is manual**, no prompt |
| Useful life reviewed at least annually | **No mechanism** |
| Component depreciation | **`VERIFIED GAP`** — value increases become children, but an original asset cannot be decomposed |
| Revaluation model with a revaluation surplus | **`VERIFIED GAP`** — `02` §3 item 13 |
| Impairment | **`VERIFIED GAP`** |

`SUPPORTED INTERPRETATION` for the standards' content — this session did not obtain
the TFAC primary texts. **`HOLD / EVIDENCE REQUIRED`.** `UNR-20`.

## 5. What this means for the custom Thai module

`17` establishes that the project's custom Thai method and the reference product's
standard calendar-day mode are **numerically equivalent within rounding**.

So the compliance question is **not** "can we reproduce the Thai method". It is
**"is the right computation mode selected on the 217 running assets"** — `UNR-02`.

And the consequence of getting it wrong is quantified in `16` §3.4: monthly amounts
diverge by up to 8%, while the **annual** total stays within 0.05%. An annual tax
computation will not reveal the error. Only a monthly review will.

## 6. Thai questions this session could not answer

| ID | Question | Why it matters |
|---|---|---|
| `UNR-01` | Is the apportionment unit legally the day? | Determines the compliance status of the 30/360 default |
| `UNR-03` | Does Thai practice permit depreciation to be absorbed into inventory value, and on what basis? | **Precondition for the entire SMEsPlus costing design** |
| `UNR-20` | TFAC primary text on PPE | Component depreciation and revaluation gaps |
| `UNR-21` | Does Thai tax law permit suspending depreciation on an owned asset (the pause function)? | `06` §3.4 |
| `UNR-22` | Statutory standing of the 1-baht residual convention | `18` §7 |
| `UNR-23` | How off-balance-type accounts are treated in Thai statutory financial statements | **Precondition for the management ledger** |

`UNR-03` and `UNR-23` are the two that gate the Boss's design, and neither is
answerable from software evidence. Both are Accounting-Tax track items.

## 7. Sources

See `28_SOURCE_LINK_REGISTER.md`.
