# P10 — PERIOD RECOGNITION MATRIX

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1

How each mechanism answers: *which period does this amount belong to, and how much of it?*

---

## 1. Period Grid

| Mechanism | Grid | Configurable | Anchored to | Evidence |
|-----------|------|--------------|-------------|----------|
| Deferral | calendar months, cut at month end | **no** | calendar, not fiscal year | `E-P10-007` |
| Accrual | single point, operator-chosen | n/a | operator's cut-off date | `E-P10-024` |
| Depreciation | months or years | yes | fiscal year for the "none" prorata mode | `E-P10-029`, `E-P10-031` |
| Loan amortisation | schedule line dates, forced to month end for posting | no | the contractual schedule | `E-P10-033` |
| Recurring | fixed interval from the origin entry | monthly/quarterly/yearly | the origin entry's date | `E-P10-039` |

Two grids are calendar-anchored and one is fiscal-year-anchored. **No mechanism derives its grid from the owning company's fiscal calendar for the purpose of allocation** — the fiscal calendar enters only the depreciation prorata start rule. For a company whose fiscal year is not the calendar year, the deferral grid and the fiscal grid do not coincide, and the deferral report's period columns are calendar periods.

## 2. Allocation Rules

| Rule | Where available | Day arithmetic | Notes |
|------|-----------------|----------------|-------|
| Actual days | Deferral (`day`), Depreciation (`daily_computation`) | true calendar, leap years honoured | Two separate implementations (`E-P10-006`, `E-P10-031`) |
| 30/360 | Deferral (`month`), Depreciation (`constant_periods`) | last calendar day of a month normalised to day 30 | Two separate implementations with different normalisation code |
| Full month | Deferral (`full_months`) only | both ends snapped to the first of the month | No depreciation equivalent |
| Contractual | Loan only | amounts supplied, not derived | Uploaded or computed externally |
| None | Accrual, Recurring | n/a | |

The prior Asset round established that under the 30/360 convention **monthly amounts differ by up to 8% in February while annual totals agree within 0.05%**. That result transfers directly to the deferral mechanism, which uses the same convention: **an incorrect allocation setting is invisible to annual reconciliation and visible only in monthly reporting.** Cited as prior evidence, not re-derived.

## 3. Boundary Behaviour

| Case | Deferral | Depreciation | Loan | Accrual |
|------|----------|--------------|------|---------|
| First partial period | pro-rated from the start date | pro-rated per prorata mode | contractual | n/a |
| Last partial period | pro-rated, **plus all rounding residue** (`E-P10-009`) | end-of-life adjustment | contractual | n/a |
| Window shorter than one period | one period; if it falls in the source document's own month, **no entries at all** are produced (`E-P10-007`) | at least one period | contractual | n/a |
| Window ends exactly at a period end | clean | clean | clean | n/a |
| Window expressed as start → same-day-next-year | 12 + 1/30 periods; uneven amounts; advisory warning only (`E-P10-015`) | n/a | n/a | n/a |

## 4. Recognition Period vs Posting Date — the separation that does not exist

| Mechanism | Period the amount belongs to | Date the entry carries | Can they differ? | Is the difference recorded? |
|-----------|------------------------------|------------------------|------------------|------------------------------|
| Deferral | the month segment | the same month end — **unless re-dated by the lock check** | **yes** (`P10-F-05`) | **no** |
| Depreciation | the board period | the period end | yes, same mechanism | no |
| Loan | the schedule line | month end of the line date | yes, same mechanism | no |
| Accrual | the cut-off instant | the cut-off date | yes, same mechanism | no |
| Recurring | the interval | the computed date | yes | no |

**This row is the matrix's central finding.** Every mechanism examined conflates the accounting period an amount belongs to with the date the entry happens to carry, and every one of them inherits a shared posting layer that will silently change the second (`E-P10-036`, `E-P10-037`) without any means of preserving the first. In an SMEsPlus kernel these must be two fields, and their divergence must be a reportable quantity.

## 5. Duplicate-Recognition Exposure per Period

Consolidating the independent challenge (`15_P10_AAS03_CHALLENGE.md`):

| Mechanism | Duplicate control | Strength | Independent challenge result |
|-----------|-------------------|----------|------------------------------|
| Deferral — grouped path | date-and-state proxy key on the source document (`E-P10-022`), plus a cumulative self-correcting model | partial | **Defeated twice**: by a deferral entry left in draft with a past date, and by an un-keyed result cache shared across report types and periods |
| Deferral — validation path | none needed at generation; guarded by source-document state | adequate for its own path | Not defeated; the exposure arises on the *other* path |
| Accrual | **none of any kind** | none | Confirmed: repeat execution reproduces identical entries |
| Depreciation | posted entries are never rewritten; only draft board entries are replaced | strong | Not defeated for the recompute path; the pause/resume/dispose paths were **not searched** — class `C` |
| Loan | none inside the confirmation path | none | Defeated three ways: re-entrant confirmation, a reset path that orphans posted entries, and an off-by-one in the skip rule |
| Recurring | origin chain | weak | Not attacked in this round |

## 6. Lost-Recognition Exposure per Period

| Path | Effect | Class |
|------|--------|-------|
| A recurring template carrying a deferred cost | the schedule is dropped on every copy; the whole amount is recognised in the posting period | `VERIFIED FACT` |
| A scheduled entry that fails to post once during the automatic run | it is flagged unchecked and thereafter excluded from its own automatic posting, permanently | `VERIFIED FACT` |
| A posted depreciation entry reset to draft | the residual is restored and the amount is re-spread over the remaining life; the period's charge vanishes from that period | `VERIFIED FACT` for the code path, `INFERENCE` for the net amount |
| A recognition entry re-dated by the lock check | the amount lands in a later period; the intended period is never recognised | `VERIFIED FACT` |

## 7. What SMEsPlus Must Specify

1. Whether the recognition grid is the **fiscal** calendar of the owning company or the civil calendar. (Currently: civil, unconditionally.)
2. Whether daily recognition must be supported as a **grid**, not merely as a weighting. (Currently: not available.)
3. Where rounding residue belongs. (Currently: the last period, unconditionally.)
4. Whether a recognition period, once determined, may ever be changed by a posting constraint. (Currently: yes, silently.)
5. Whether an allocation convention is a PLATFORM definition, a TENANT default or a COMPANY binding value — all three, in the shape given in `10b_P10_SCOPE_OWNERSHIP_MATRIX.md`.
