# 16 — Thai Tax Review

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `EVIDENCE COLLECTION — HOLD-HEAVY BY DESIGN`

---

## 1. Scope

Independent Thai Revenue Department / Revenue Code review for asset-related tax treatment: depreciation ceilings, method-change restrictions, disposal/gain treatment, and any documentation-requirement pattern relevant to the Asset domain. This file is deliberately conservative — anything not backed by an authoritative primary source is `HOLD`.

## 2. Findings

| Item | Evidence | Classification |
|---|---|---|
| Statutory basis for tax depreciation | Revenue Code, deductibility of depreciation/depletion governed "under the rules, procedures, conditions and rates specified by a Royal Decree" — general structure confirmed by secondary sourcing (a legal-library summary of Revenue Code Sections 65–76) referencing this decree mechanism; the decree's precise number was not independently confirmed against a primary gazette source in this session (see file `08` §3 on the "145" naming discrepancy). | `SUPPORTED INTERPRETATION` (mechanism) / `HOLD` (exact decree number) |
| Maximum depreciation rates by category | Buildings (permanent) 5% p.a.; plant and equipment 20% p.a.; computer hardware/software 33.33% p.a.; leased assets 100%/lease-term p.a. — directly retrieved from a Thai tax-advisory firm's public summary page. | `SUPPORTED INTERPRETATION` (a professional secondary source, not the primary gazetted decree text itself) |
| Method/rate consistency requirement | The same secondary source states that once a depreciation rate and method are adopted for an asset category, they cannot be changed without Revenue Department approval. | `SUPPORTED INTERPRETATION` |
| Proration principle | Depreciation/depletion "deductible in proportion to the period from the acquisition of such assets" — a proration-by-time principle confirmed by secondary sourcing; the exact computational convention (daily/monthly, day-count basis) is the specific open question addressed in depth in file `08`. | `SUPPORTED INTERPRETATION` (principle) / `HOLD` (exact convention) |
| Loss/scrap/destruction deductibility documentation requirements for a disposed or written-off asset | Not researched in this session — out of this file's completed scope, flagged for follow-up. Note: the sibling COGS Deep Research package independently flagged an analogous inventory-side gap (Revenue Department Order Por.79/2541 threshold for normal vs. abnormal loss) which may have a parallel, not-yet-researched analogue for fixed-asset disposal/write-off; this is a hypothesis for future research, not a finding of this file. | `UNRESOLVED / EVIDENCE REQUIRED` |
| Gain/loss on disposal — tax treatment | Not independently researched against a primary Revenue Department source in this session. General expectation (unverified here) is that a disposal gain is assessable income and a disposal loss may be deductible, consistent with ordinary capital-allowance recapture logic in many jurisdictions, but this file does not assert this as confirmed Thai-specific fact. | `HOLD / EVIDENCE REQUIRED` |
| Accounting depreciation vs. tax depreciation reconciliation requirement | The secondary source notes accounting depreciation rates lower than the tax maximum must still be used for tax purposes (i.e., tax deduction cannot exceed the lower of the Royal-Decree cap or the company's own accounting rate) — a materially important asymmetry: a company cannot simply claim the statutory maximum if its own books use a slower rate. | `SUPPORTED INTERPRETATION` |

## 3. What This File Explicitly Declines to Assert

This file does not assert the Royal Decree's exact number, does not assert an exact day-count convention (routed to file `08`), does not assert disposal-related deductibility documentation requirements, and does not assert gain-on-disposal tax treatment — all `HOLD / EVIDENCE REQUIRED` pending primary-source retrieval (Revenue Department website direct text, the gazetted Royal Decree itself, or a Revenue Department ruling/order).

## 4. Materiality

These `HOLD` items are material to SMEsPlus because a Thai-market ERP's asset module will be expected to compute a tax-book depreciation figure alongside the accounting-book figure for corporate income tax filing purposes — getting the rate ceiling, the proration convention, and the disposal treatment wrong has direct tax-compliance consequences. This file does not attempt to close that gap by inference; it names it and routes it to file `24`.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
