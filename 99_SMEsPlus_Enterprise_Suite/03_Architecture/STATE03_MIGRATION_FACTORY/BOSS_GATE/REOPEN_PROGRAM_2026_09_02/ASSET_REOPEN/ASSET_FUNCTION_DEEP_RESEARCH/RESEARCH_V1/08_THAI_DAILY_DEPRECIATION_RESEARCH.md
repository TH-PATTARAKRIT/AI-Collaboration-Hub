# 08 — Thai Daily Depreciation Research (Independent Verification of a Boss Assertion)

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `EVIDENCE COLLECTION — BOSS ASSERTION UNDER CHALLENGE, NOT ACCEPTED AS FACT`

---

## 1. The Assertion Under Test

Boss-provided factual claim: "Thai depreciation uses daily calculation, so monthly depreciation may differ by days in month." This file treats that as a hypothesis requiring independent verification, per governing rule #2, and actively looked for evidence both supporting and contradicting it, and for the distinction between Thai **tax** depreciation (Revenue Code) and Thai **accounting** depreciation (TAS 16), which the assertion does not itself distinguish.

## 2. Two Separate Regimes — Do Not Conflate

Thai depreciation exists in (at least) two independently governed regimes, and the assertion must be tested against each separately:

1. **Tax depreciation** under the Revenue Code, specifically the capital-allowance rules set by Royal Decree (the maximum-rate-setting decree is referred to in secondary sourcing as Royal Decree No. 145 issued under the Revenue Code).
2. **Accounting depreciation** under Thai Financial Reporting Standards, specifically TAS 16 (Property, Plant and Equipment), which Thailand has aligned closely with IAS 16.

These can differ: a company may use one depreciation rate/method for statutory books (TAS 16, any systematic and rational method, no day-count mandate located) and a different, capped rate for the tax computation (Revenue Code, Royal Decree 145), reconciling the difference via a tax computation adjustment. This distinction is itself a finding this file surfaces that the Boss's one-line assertion does not make.

## 3. Evidence Found — Tax Side

- A directly retrieved secondary source (Sherrings.com, a Thai tax-advisory firm's public page) confirms: Royal-Decree-set **maximum rates by asset category** (buildings 5% p.a., plant and equipment 20% p.a., computer hardware/software 33.33% p.a., leased assets 100%/lease-term p.a.), and confirms depreciation/depletion "shall be deductible in proportion to the period from the acquisition of such assets" (a proration principle) — but this page did **not** state a daily-vs-monthly computation mechanic explicitly, and did not name Royal Decree 145 as such (it referenced Royal Decrees 620 and 473 by number instead — a naming discrepancy this file flags, not resolves; the "145" number is carried from the Boss's own prompt and from one secondary community source, not independently confirmed against the decree's own gazetted number in this session).
- A secondary, non-authoritative source (a SAP-implementation community forum discussion about Thailand business requirements) explicitly asserts: assets are calculated for tax depreciation on a "Daily" basis, using actual days in the year (365 or 366, i.e., leap-year-aware), consistent with an actual/actual day-count convention. This is the only source located in this session that states day-level granularity explicitly and by name — and it is **not an authoritative government or professional-body source**; it is a practitioner community discussion about ERP configuration.
- The Revenue Code's own primary statutory text (Sections 65–76 generally, and the specific Royal Decree text governing depreciation) was **not independently retrieved and read** in this session. This file did not fetch and read the primary decree text — a material gap.

## 4. Evidence Found — Accounting Side (TAS 16)

- IAS 16 (directly retrieved, and Thailand's TAS 16 is understood to be closely aligned with it, though the Thai-language TAS 16 text itself was not independently retrieved this session) requires depreciation to be calculated by "systematically allocating the depreciable amount... over the asset's useful life," with useful life, residual value, and method reviewed at least annually. No day-count mandate is part of IAS 16's own text as retrieved; IAS 16 leaves the specific period-allocation method (which could be monthly, annual, or day-based) to the reporting entity's judgment, provided it reflects the pattern of economic benefit consumption.
- No TFAC-specific statement mandating daily calculation for **accounting** (as opposed to tax) depreciation was located in this session.

## 5. Classification of the Boss Assertion

| Sub-claim | Classification | Reasoning |
|---|---|---|
| "Thai depreciation uses daily calculation" (as a blanket, unqualified statement) | `SUPPORTED INTERPRETATION`, not `FACT VERIFIED` | Directly asserted only by one non-authoritative secondary (practitioner-forum) source; the authoritative tax-advisory source confirms a *proration-by-period-from-acquisition* principle consistent with, but not identical to, a strict daily mechanic, and does not itself use the word "daily"; the primary Royal Decree text was not independently read |
| "...so monthly depreciation may differ by days in month" | `SUPPORTED INTERPRETATION` | Logically follows *if* the daily-calculation premise is correct, and is independently consistent with the reference ERP's own documented "Based on days per period" prorata option (file `07` §2) existing as a real, implementable pattern — but inherits the same evidentiary gap as the premise it depends on |
| Applicability to statutory **accounting** depreciation (TAS 16) specifically, as opposed to tax depreciation | `UNRESOLVED / EVIDENCE REQUIRED` | No evidence located that TAS 16 itself mandates a daily convention; the Boss's assertion, read literally, does not specify which regime it addresses, and this file will not assume it means both |

## 6. HOLD Statement

Per governing rule #4, this is a statutory Thai claim without a genuinely authoritative primary source independently retrieved and cited with URL and access date in this session. **Classification: `HOLD / EVIDENCE REQUIRED`.** The specific day-count convention (actual/365 vs. actual/366-leap-year-aware vs. actual/actual) needed to actually implement a daily depreciation engine is not confirmed by any source retrieved in this session, authoritative or otherwise, beyond the unauthoritative community-forum assertion. Before SMEsPlus commits engineering effort to a specific daily day-count convention for Thai tax depreciation, the primary Royal Decree text (and, separately, any Revenue Department departmental order or ruling interpreting it) should be directly retrieved and read.

## 7. What Would Resolve This

Direct retrieval and reading of: (a) the Royal Decree issued under the Revenue Code governing depreciation rates and method (confirm its actual number — this file could not confirm "145" against a primary source), (b) any Revenue Department ruling/order on day-count convention, (c) TFAC's own TAS 16 published standard text (Thai language) for any accounting-side day-count guidance. None of these three were completed in this session.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
