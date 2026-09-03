# 07 — Solution Path Register

One row per non-closed unknown (57 rows: 59 total minus the 2 already resolved as negative finding/scope condition — `CGS-U14`, `CGS-U49` — which are excluded here, consistent with file `05`). Columns: `UNKNOWN_ID`, `Problem`, `Root Cause` (code from file `06`), `Required Evidence`, `Evidence Owner`, `Resolution Action`, `Decision Owner`, `Dependency`, `Estimated Gate Impact`, `Can Parallelize?`, `Next Prompt Required?`, `Status`.

Grouped by Priority (from file `03`) for readability; every ID from the 57-item open population appears exactly once.

## P0 Items (18)

| UNKNOWN_ID | Problem (short) | RC | Required Evidence | Evidence Owner | Resolution Action | Decision Owner | Dependency | Gate Impact | Parallelize? | Next Prompt? | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CGS-U01 | No stable reference recognition-timing pattern | RC-01 | None will close this — it's a ruling, not a fact | n/a | Boss ruling informed by file 08 | Boss | none | JT-04 | No | Yes — Boss ruling prompt | HOLD |
| CGS-U06 | Expense Account field mode-polymorphic | RC-03 | Field-level re-fetch across modes | Docs/Research owner | Targeted re-fetch pass | n/a (fact-finding) | none | JT-01 | Yes | Yes — re-fetch prompt | HOLD |
| CGS-U07 | Re-class behavior on category change undocumented | RC-05 | Live-instance test | Research owner (blocked, no live instance) | Schedule live-instance walkthrough | n/a | Live-instance access | JT-01 | Yes (with CGS-U08) | Yes | HOLD |
| CGS-U08 | Effect on existing stock on ownership change undocumented | RC-05 | Live-instance test | Research owner (blocked) | Same walkthrough as CGS-U07 | n/a | Live-instance access | JT-01 | Yes (with CGS-U07) | Yes | HOLD |
| CGS-U09 | Journal-level fallback existence unconfirmed | RC-05 | Official-source confirmation | Docs/Research owner | Targeted re-fetch / official FAQ search | n/a | none | JT-01 | Yes | Yes | HOLD |
| CGS-U11 | Fiscal Position override scope undocumented | RC-05 | Direct re-fetch | Docs/Research owner | Targeted re-fetch pass | n/a | none | JT-01 | Yes | Yes | HOLD |
| CGS-U12 | Current-version field mapping incomplete | RC-02 | Direct re-fetch (2 prior failures) | Docs/Research owner | Third re-fetch attempt, different retrieval method | n/a | none | JT-01 | Yes | Yes | HOLD |
| CGS-U13 | Company-exclusivity of accounting package unconfirmed | RC-05 | Re-fetch or live-instance | Research owner | Re-fetch first, live-instance if inconclusive | n/a | none | JT-01 | Yes | Yes | HOLD |
| CGS-U16 | No SMEsPlus late-cost attribution rule | RC-08 | None — design decision | n/a | Boss ruling | Boss | none | JT-06 design | No | Yes | HOLD |
| CGS-U20 | Invoicing-policy/timing-trigger interaction undocumented | RC-01 | Direct re-fetch | Docs/Research owner | Targeted re-fetch pass | n/a | none | JT-04 | Yes | Yes | HOLD |
| CGS-U22 | No safe default for unconfigured loss account | RC-08 | None — design decision | n/a | Boss ruling | Boss | none | Control gate | No | Yes | HOLD |
| CGS-U25 | Periodic accrual-visibility mechanism undocumented | RC-05 | Direct re-fetch | Docs/Research owner | Targeted re-fetch pass | n/a | none | JT-06 | Yes | Yes | HOLD |
| CGS-U31 | Matching-principle risk on invoice-before-delivery | RC-01 | Re-fetch + SME-Q-03 answer | Docs owner + Business SME | Re-fetch, route SME-Q-03 | Business SME (fact), Boss (control) | SME-Q-03 | JT-04 | Partial | Yes | HOLD |
| CGS-U32 | AVCO/credit-note discrepancy; FIFO sub-case weak | RC-05/RC-06 | Live-instance FIFO test; stronger primary source | Research owner (blocked) | Live-instance walkthrough | Boss (for the AVCO control gap itself) | Live-instance access | JT-05 | No (needs live instance) | Yes | HOLD |
| CGS-U33 | Return docs silent on cost basis | RC-06 | None beyond current ceiling without live instance | n/a | Carry forward | n/a | Same as CGS-U32 | JT-05 | No | Yes | HOLD |
| CGS-U34 | Landed-cost residual posting contradicts across sources | RC-04 | None — contradiction, not fact gap | n/a | Present both readings to Boss | Boss | none | JT-08 | No | Yes | HOLD |
| CGS-U36 | Documented control-break case, no journal entry generated | RC-06 | None — Boss must design a control | n/a | Boss ruling with Audit VETO flag retained | Boss | none | JT-08, Audit VETO | No | Yes | HOLD |
| CGS-U42 | Category company-scoping unconfirmed | RC-05 | Official-source confirmation or live-instance test | Research owner | Re-fetch, escalate to live-instance if inconclusive | n/a | none | JT-01 | Yes | Yes | HOLD |

## P1 Items (16) — Register-Level Treatment

| UNKNOWN_ID | Problem (short) | RC | Required Evidence | Evidence Owner | Resolution Action | Decision Owner | Dependency | Gate Impact | Parallelize? | Next Prompt? | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CGS-U02 | Terminology/ownership-model shift across versions | RC-01 | Re-fetch | Docs owner | Re-fetch pass | n/a | none | JT-03 | Yes | Yes | HOLD |
| CGS-U03 | Price Difference Account scope conflict | RC-04 | Primary-page direct quote, current version | Docs owner | Re-fetch; see file 12 | n/a | none | JT-02 | Yes | Yes | HOLD |
| CGS-U04 | Menu A field set rests on reconstruction | RC-02 | Direct-fetch retry | Docs owner | Retry with alternate method | n/a | none | JT-02/03 (19.0-pinned designs) | Yes | Yes | HOLD |
| CGS-U05 | Category-level labels persist to 19.0? | RC-05 | Live-instance | Research owner (blocked) | Live-instance test | n/a | Live-instance access | JT-01 (secondary) | Yes | Yes | HOLD |
| CGS-U15 | Closing mechanism ambiguity (routine vs. migration) | RC-01 | Re-read source heading structure | Docs owner | Targeted re-read/re-fetch | n/a | none | JT-07 scoping | Yes | Yes | HOLD |
| CGS-U23 | Location-level override generalization unconfirmed | RC-05 | Additional case study | Research owner | Re-fetch additional scenarios | n/a | none | JT-01 (secondary) | Yes | Yes | HOLD |
| CGS-U24 | Third precedence axis (location) needed? | RC-08 | None — design decision | n/a | Boss ruling | Boss | CGS-U23 | JT-01 (secondary) | No | Yes | HOLD |
| CGS-U30 | Bill-before-receipt weakest-evidenced sub-case | RC-05 | Live-instance or re-fetch | Research owner | Re-fetch first | n/a | none | JT-04 (secondary) | Yes | Yes | HOLD |
| CGS-U35 | Standard-Price landed-cost eligibility unconfirmed | RC-05 | Worked-example search | Docs owner | Re-fetch | n/a | none | JT-08 (secondary) | Yes | Yes | HOLD |
| CGS-U39 | NRV/write-down absent as reference feature | RC-07 | None — original design; Thai evidence only | n/a | Original design work + TAS 2 review | Boss/Design owner | TH-HOLD-COGS-02 | JT-09 (design) | Partial | Yes | HOLD |
| CGS-U40 | Inventory guard insufficient for Accounting close | RC-08 | None — design decision | n/a | Boss ruling | Boss | none | JT-06/07 | No | Yes | HOLD |
| CGS-U43 | Shared category could force costing method cross-company | RC-08 (dependent) | Resolution of CGS-U42 first | n/a | Resolve CGS-U42, then design | Boss | CGS-U42 | JT-01 (multi-company) | No | Yes | HOLD |
| CGS-U45 | Accounting-side duplicate-posting risk; GAP-FS-08 missing | RC-08 | None — design decision, artifact must be created first | n/a | Create GAP-FS-08, then Boss ruling | Boss | GAP-FS-08 creation | Migration gate | No | Yes | HOLD |
| CGS-U48 | Naive Periodic COGS identity absorbs scrap/shrinkage | RC-08 | None — depends on SMEsPlus capture granularity (design) | n/a | Boss ruling | Boss | none | JT-06 | No | Yes | HOLD |
| CGS-U50 | Cost Release classification rule set undefined | RC-08 | None — design decision | n/a | Boss ruling | Boss | none | JT-01/06 | No | Yes | HOLD |
| TH-HOLD-COGS-03 | Sec. 65 bis(6) entity vs. category-level binding unconfirmed | RC-09 | Primary statutory research | Thai statutory track owner | Thai-track research pass | n/a (fact-finding), Boss for design consequence | none | JT-02 | Yes | Yes | HOLD |

## P2 Items (14) — Register-Level Treatment, Lighter Detail

| UNKNOWN_ID | Problem (short) | RC | Required Evidence | Evidence Owner | Resolution Action | Decision Owner | Dependency | Gate Impact | Parallelize? | Next Prompt? | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CGS-U17 | Lock Date vs. scheduled Periodic close entry | RC-05 | Re-fetch | Docs owner | Re-fetch pass | n/a | none | none named | Yes | Optional | HOLD |
| CGS-U18 | Negative/zero-cost handling incomplete for FIFO/Standard | RC-05 | Re-fetch | Docs owner | Re-fetch pass | n/a | none | none named | Yes | Optional | HOLD |
| CGS-U21 | Hard block on bill/invoice-before-receipt/delivery unconfirmed | RC-05 | Re-fetch | Docs owner | Re-fetch pass | n/a | none | none named | Yes | Optional | HOLD |
| CGS-U26 | Return handling before/after close under Periodic | RC-05 | Re-fetch (Perpetual-only evidence exists) | Docs owner | Re-fetch pass | n/a | none | JT-05 (secondary) | Yes | Optional | HOLD |
| CGS-U27 | Write-down distinguished from ordinary COGS under Periodic? | RC-05 | Re-fetch | Docs owner | Re-fetch pass | n/a | none | none named | Yes | Optional | HOLD |
| CGS-U29 | Existing-stock conversion mechanics on costing-method change (AVCO/FIFO) | RC-05 | Re-fetch | Docs owner | Re-fetch pass | n/a | none | none named | Yes | Optional | HOLD |
| CGS-U37 | No production standard-cost variance mechanism | RC-07 | None — original design | n/a | Original design work | Design owner/Boss | none | Manufacturing (future) | Yes | Deferred | HOLD |
| CGS-U38 | Two WIP mechanisms — coexist or exclusive? | RC-05 | Re-fetch | Docs owner | Re-fetch pass | n/a | none | Manufacturing (future) | Yes | Deferred | HOLD |
| CGS-U41 | Does the 16-field handoff contract cover unmatched-fact queries? | RC-09 (documentation, not statutory) | Re-read the already-approved contract | Docs owner | Direct contract re-read (no new research) | n/a | none | none named | Yes | Yes — cheap, do first | HOLD |
| CGS-U46 | Initial-stock action: value/cost input and account unconfirmed | RC-05 | Re-fetch | Docs owner | Re-fetch pass | n/a | none | Migration (secondary) | Yes | Optional | HOLD |
| CGS-U47 | No structural duplicate-import block confirmed | RC-05 | Re-fetch | Docs owner | Re-fetch pass | n/a | none | Migration (secondary) | Yes | Optional | HOLD |
| TH-HOLD-COGS-01 | No numeric threshold for normal vs. abnormal waste | RC-09 | Thai statutory research | Thai track owner | Thai-track research pass | n/a | none | none named | Yes | Optional | HOLD |
| TH-HOLD-COGS-02 | Category-level write-down vs. item-level NRV coexistence | RC-09 | Thai statutory research | Thai track owner | Thai-track research pass | n/a | none | CGS-U39 (secondary) | Yes | Optional | HOLD |
| TH-HOLD-COGS-04 | DBD presentation-sequence finding is interpretation-only | RC-09 | Direct primary-text extraction | Thai track owner | Thai-track research pass | n/a | none | none named | Yes | Optional | HOLD |

## P4 Items (9) — Watch/Deferred, No Individual Row Detail Beyond Status

`CGS-U10`, `CGS-U19`, `CGS-U28`, `CGS-U44`, `TH-HOLD-05-residual`, and the carried bundle `TH-HOLD-01/04/06/08/09` — all Status: **HOLD, DEFERRED, WATCH**. No resolution action assigned this session; carried unchanged. Not force-populated with fabricated urgency.

## Two New Items This Session Adds to the Routing Surface (Not New Register IDs — Cross-Referenced Only)

`TH-NEW-01`, `TH-NEW-02` (identified in the Fact Verification session, file `12`) are not separate register IDs — they are sub-questions of `TH-HOLD-COGS-03`/`JT-04` and `CGS-U32`/`JT-05` respectively — and are carried into file `15` of this package rather than duplicated here as new rows.
