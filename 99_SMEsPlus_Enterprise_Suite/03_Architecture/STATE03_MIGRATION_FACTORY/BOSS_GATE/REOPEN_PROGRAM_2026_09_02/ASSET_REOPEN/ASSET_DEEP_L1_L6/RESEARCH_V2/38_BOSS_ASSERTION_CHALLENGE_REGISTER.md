# 38 — BOSS ASSERTION CHALLENGE REGISTER
**LAYER 2 — AUDIT QUARANTINE**

Required under §75. **Purpose: not to challenge authority, but to prevent business
knowledge from being converted into unverified technical fact** (§4, §75).

Boss assertions are high-value business evidence. They are recorded here with what
independently supports them and what does not.

---

## `BA-01` — "The source system computes depreciation on a daily basis"

**Business meaning:** Thai fixed-asset depreciation should follow actual calendar
days — total days including leap years, a per-day rate, each period charged by its
actual applicable days.

| Perspective | Position |
|---|---|
| **Functional** | The described mechanism is exactly right, step for step, for two of the four implementations found |
| **Database** | The mechanism depends on one field. The lifetime value differs by 26 days between modes on a 5-year asset |
| **Integration / Localisation** | The statutory basis is confirmed for *pro-ration*; the *daily unit* is practice, not retrieved statute |
| **Code / UI** | **The described behaviour is not the default.** It is one of three options, and the default is 30/360 |

**Supporting evidence:** `SRC-01` — the calendar-day mode implements precisely the
five steps described. `SRC-27` — the project's own custom module implements them
too. `EV-SIM-02` — the two are numerically equivalent within 0.03 THB per period.

**Contradicting evidence:** `SRC-01` — the product default is *constant periods*, a
30/360 convention in which the description is false at steps 3 and 5.

**AAS+ position:** **`CONFIRMED AGAIN` as a description of the mechanism.
`CONTRADICTED` as a description of the default configuration.**

**Final classification:** the Boss's model of *how it works* is correct. The
implicit assumption that it is *what the system does out of the box* is not. This
distinction is the practical content of `CTR-01`.

---

## `BA-02` — "Thai accounting/tax requires daily depreciation"

| Perspective | Position |
|---|---|
| **Functional** | Not a functional question |
| **Database** | Not a data question |
| **Integration / Localisation** | Pro-ration from acquisition is **statutory and now verified from primary text**. The **unit** is not stated in that text |
| **Code / UI** | Three independent implementations of the daily unit exist, which is behavioural evidence of market expectation |

**Supporting evidence:** `LAW-01` — Revenue Code s.65 bis (2), *"deductible in
proportion to the period from the acquisition"*. `LAW-02` — Royal Decree 145 s.4,
computation by period held with apportionment for part periods. `LAW-04` — Thai
practice guidance publishing the per-day formula. `SRC-27` — the project's own
vendor built it.

**Contradicting evidence:** none. **Insufficient evidence:** neither primary text
retrieved uses *จำนวนวัน* / *number of days*. A monthly apportionment also satisfies
"in proportion to the period".

**AAS+ position:** **split.**

| Component | Classification |
|---|---|
| Pro-ration from acquisition is required | **`FACT VERIFIED`** |
| Statutory rates are **ceilings**, not schedules | **`FACT VERIFIED`** |
| The apportionment unit is the **day** | **`SUPPORTED INTERPRETATION`** — `HOLD / EVIDENCE REQUIRED`, `UNR-01` |

**Upgrade on the prior session**, which classified the whole assertion as
`SUPPORTED INTERPRETATION` from secondary sources only — `29` `REV-07`.

---

## `BA-03` — "A production job passing through a machine should receive that machine's cost; a job that does not use the machine must not" (the toll-gate concept)

| Perspective | Position |
|---|---|
| **Functional** | Correct as a business requirement, and **not satisfiable on the reference model** |
| **Database** | The model is `Operation → Work Center ← many Equipment`. There is no job-to-machine edge |
| **Integration** | Translated out of the analogy: this is a **traced direct cost** requirement, not an allocation requirement |
| **Code / UI** | Confirmed in two lines of source: the operation model carries a work-centre field and no equipment field |

**Supporting evidence:** `SRC-12`, `SRC-11`.

**Contradicting evidence:** none.

**AAS+ position:** **`CONFIRMED AGAIN`.** The Boss's concern is an accurate reading
of a real structural limitation. `Operation → Equipment` is a `VERIFIED SOURCE GAP`
and a legitimate extension candidate.

**Caution recorded** (Expert 1, `09`): closing the modelling gap does not close the
**data** gap. Someone must record which machine ran which job, every time. That
operational burden is not yet acknowledged in the design.

---

## `BA-04` — "Production allocation configuration belongs to the MRP production equipment context, not to the generic equipment master and not to the Asset Model"

| Perspective | Position |
|---|---|
| **Functional** | Supported — non-production equipment does not need production configuration |
| **Database** | Supported — the asset template governs nothing after creation, and on this deployment governs nothing at all |
| **Integration** | Supported — the reference product already places production cost configuration on the work centre |
| **Code / UI** | Supported, **with one challenge**: the product puts the rate on the work **centre**. A per-machine rate is a new grain and its home is undecided |

**Supporting evidence:** `SRC-01` and `EV-RT-02` — 280 assets, **zero** linked to a
template. `SRC-14` — production cost configuration lives on the work centre.

**AAS+ position:** **`SUPPORTED INTERPRETATION`** — an evidence-consistent design
judgement. This also `CONFIRMS AGAIN` the historical correction recorded in §80 of
the governing prompt.

**Open sub-question:** whether the per-machine grain belongs on the equipment
record, on a new production-equipment mapping, or on the work-centre–equipment pair
— `UNR-24`.

---

## `BA-05` — "When financial depreciation completes, residual book value stays unchanged and internal equipment usage cost continues; internal usage must not reduce financial residual book value"

| Perspective | Position |
|---|---|
| **Functional** | The mechanical premise is verified. **The trigger is not available** — there is no fully-depreciated state |
| **Database** | An unbounded, monotonically increasing accumulator with no terminating rule (Expert 2, `11`) |
| **Integration** | The separation is sound and, on the asset side, **already enforced by the product** — off-balance accounts are forbidden on the asset account triple |
| **Code / UI** | Nothing in the reference system resembles this. Entirely original |

**Supporting evidence:** `SRC-01` — the not-depreciable amount is excluded from the
base and never touched by any depreciation line; the asset stays `open` after
completion with book value equal to the residual. `SRC-04` — off-balance accounts
are excluded from all three asset accounts by field domain.

**Contradicting evidence:** none — but **two boundary conditions the assertion does
not cover:**

1. **On closure the residual is removed from book value** and written out through
   gain/loss. It does not survive disposal as an identifiable amount (`18` §6).
2. **A fully depreciated asset can be made depreciable again** at any time by a
   capital improvement (`F09`). The re-entry case is undefined.

**AAS+ position:**

| Component | Classification |
|---|---|
| Depreciation stops; residual persists while running | **`FACT VERIFIED`** |
| The asset remains a live, usable record | **`FACT VERIFIED`** |
| Internal usage cost continues | **`DESIGN CANDIDATE`** — no precedent found |
| Residual as a permanent reference base | **`DESIGN CANDIDATE`** |
| Cumulative usage may exceed residual without bound | **`DESIGN CANDIDATE`, contested** — `D5-01`, escalated as `UNR-B3` |

---

## `BA-06` — "Off-Balance is an account type; customers may create their own accounts of that type; no cross-entry between off-balance and financial WIP/FG/expense"

| Perspective | Position |
|---|---|
| **Functional** | Consistent |
| **Database** | Consistent |
| **Integration** | **The boundary is stronger than stated** on the asset side — the product enforces it structurally |
| **Code / UI** | Confirmed as an account classification |

**Supporting evidence:** `SRC-04` — all three asset account fields exclude
off-balance accounts by domain.

**AAS+ position:** **`CONFIRMED AGAIN`, and strengthened.** What the Boss asked to be
maintained by policy is, on the asset side, already enforced by the product.

**Two things this does not establish**, and neither should be assumed:

- whether off-balance accounts are permitted in the work-centre or valuation path
  (`UNR-17`);
- **how accounts of that type are treated in Thai statutory financial statements**
  (`UNR-23`). The management-ledger design rests on this and it is untested.

---

## `BA-07` — "Do not hard-code monthly logic; if the source uses day-based depreciation, derive from a daily basis"

**AAS+ position:** **`CONFIRMED AGAIN`, and now demonstrated to be necessary rather
than merely prudent.**

`16` §3.4 shows monthly amounts diverging by **8% in February** between the two
conventions while annual totals agree within 0.05%. A monthly-hard-coded internal
usage rate would carry exactly that error into product cost, invisibly to any
annual check.

This is the assertion best vindicated by this session's evidence.

---

## Summary

| ID | Assertion | Outcome |
|---|---|---|
| `BA-01` | Daily depreciation in the source | Confirmed as mechanism; **contradicted as default** |
| `BA-02` | Thai law requires daily | **Split** — pro-ration `FACT VERIFIED`; daily unit `SUPPORTED INTERPRETATION` |
| `BA-03` | Toll-gate | **Confirmed again** |
| `BA-04` | Allocation config belongs to production context | **Supported interpretation** |
| `BA-05` | Post-depreciation internal usage | **Premise verified; mechanism a design candidate; two boundary conditions uncovered** |
| `BA-06` | Off-balance boundary | **Confirmed again and strengthened** |
| `BA-07` | Daily not monthly basis | **Confirmed again and shown necessary** |

**Nothing the Boss asserted was found to be wrong about the business.** Two
assertions carried an implicit technical assumption that the evidence does not
support: that daily computation is the system's default (`BA-01`), and that the
daily *unit* is statutory rather than practice (`BA-02`).
