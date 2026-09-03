# 07 — Depreciation Engine Forensic

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `EVIDENCE COLLECTION`

---

## 1. Scope

Per governing brief research object 05: daily vs. monthly vs. annual calculation, prorata, first/last period, month-length and leap-year handling, rounding, partial periods, mid-life modification/pause/disposal, residual treatment.

## 2. Classification Table

| Mechanic | Reference-ERP evidence | Classification |
|---|---|---|
| Depreciation is period-based (a schedule of discrete entries, not a continuous daily accrual, by default) | Documented: a "Depreciation Board" of planned entries is generated, one per period (interval controlled by the asset model/duration setting — commonly monthly or annual in worked examples). | `FACT VERIFIED` |
| Prorata computation exists as a configurable option, including a days-based option | Documented: "Based on days per period" is a named computation-method option, alongside "No Prorata" and "Constant Periods." | `FACT VERIFIED` (existence) |
| Exact day-count convention (actual/365, actual/actual, 30/360) for "Based on days per period" | Not located in any documentation page retrieved this session. | `UNRESOLVED / EVIDENCE REQUIRED` |
| First-period prorata (partial first entry from acquisition date rather than period start) | Documented as the explicit purpose of "Prorata Temporis": the first depreciation entry runs from the purchase date instead of January 1 / fiscal-year start. | `FACT VERIFIED` |
| Last-period prorata / disposal-date partial entry | Not directly quoted in this session's retrieval. Plausible by symmetry with first-period prorata but not confirmed. | `UNRESOLVED / EVIDENCE REQUIRED` |
| Month-length handling (28/29/30/31-day months under a days-based method) | Not located. If the days-based option truly counts actual calendar days, unequal month lengths would mechanically produce unequal period depreciation amounts — this is a logical implication of the documented feature's name, not itself directly evidenced with a worked example. | `SUPPORTED INTERPRETATION` |
| Leap-year handling | Not located at all. | `UNRESOLVED / EVIDENCE REQUIRED` |
| Rounding rule | Not located. | `UNRESOLVED / EVIDENCE REQUIRED` |
| Mid-life modification ("Modify Depreciation" action) | Documented: opens a form to set new depreciation values; a value decrease posts a new journal entry for the decrease and recalculates all future unposted entries on the Depreciation Board; a value increase is handled analogously per the same documented action. | `FACT VERIFIED` |
| Pause | Not directly confirmed as a distinct documented state/action separate from Modify. Plausible via a state field (draft/running/close, per file `02`) but the specific "pause and later resume, with depreciation correctly skipping the paused interval" behavior was not found described in the pages retrieved. | `UNRESOLVED / EVIDENCE REQUIRED` |
| Disposal mid-life | Documented generally: an asset can be disposed of, generating a gain/loss entry against remaining book value (see file `09` for the residual/disposal mechanics in detail). Exact interaction with a not-yet-posted partial-period entry at disposal date was not independently confirmed. | `SUPPORTED INTERPRETATION` (existence of disposal handling) / `UNRESOLVED / EVIDENCE REQUIRED` (exact partial-period-at-disposal mechanics) |
| Residual/not-depreciable value treatment during the schedule | Documented: excluded from the Depreciable Value base entirely (Depreciable Value = Original Value − Not Depreciable Value), so it is structurally never depreciated at any point in the schedule, not just "left over at the end." | `FACT VERIFIED` — see also file `09` |

## 3. Daily vs. Monthly vs. Annual — Direct Answer

The reference ERP is **not exclusively daily, monthly, or annual** — it is documented as a configurable engine where the *period interval* (how often a depreciation entry is generated — commonly monthly or annual in the worked examples reviewed) is a separate configuration axis from the *prorata computation method* (whether a partial first/last period is computed using actual days or a simplified constant-period convention). This two-axis structure is itself a material finding directly relevant to the Boss's Thai daily-depreciation assertion (file `08`): "monthly depreciation may differ by days in month" is only mechanically true if a days-based prorata method is actually selected — a No-Prorata or Constant-Periods configuration would not produce day-length-driven variance even though the underlying reference-ERP engine is capable of it.

## 4. Fact Status Summary

| Mechanic | Fact Status |
|---|---|
| Depreciation-method mechanics (§2 rows 1-3 of file `03`) | `FACT VERIFIED` |
| Prorata options exist, including days-based | `FACT VERIFIED` |
| Exact day-count convention, leap-year, rounding | `UNRESOLVED / EVIDENCE REQUIRED` |
| First-period prorata | `FACT VERIFIED` |
| Last-period/disposal prorata, pause behavior | `UNRESOLVED / EVIDENCE REQUIRED` |
| Mid-life modification | `FACT VERIFIED` |
| Residual exclusion from depreciable base | `FACT VERIFIED` |

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
