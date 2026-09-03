# 04 — P0 Gate Blocker Register

The 18 P0 items from file `03`, grouped by the gate they block, with the specific evidence that would clear each.

## Gate: `JT-04` (COGS Recognition Timing)

| ID | Blocking reason | Evidence that clears it | Owner |
|---|---|---|---|
| `CGS-U01` | No single reference recognition-timing behavior to imitate | Not clearable by more reading — requires Boss ruling (see file `08`) | Boss |
| `CGS-U20` | Invoicing-policy/trigger-table interaction undocumented | Direct re-fetch of invoicing-policy documentation pages | Research/Docs owner |
| `CGS-U31` | Matching-principle risk on invoice-before-delivery unresolved | Same re-fetch pass, plus Business SME answer to `SME-Q-03` | Research owner + Business SME |

## Gate: `JT-05` (Return Cost Basis)

| ID | Blocking reason | Evidence that clears it | Owner |
|---|---|---|---|
| `CGS-U32` | Vendor-admitted AVCO/credit-note discrepancy; FIFO sub-case community-only | Live reference-instance FIFO-return test, or a stronger primary source | Research owner (needs live-instance access this session lacks) |
| `CGS-U33` | Reference return documentation silent on cost basis | Already assembled from secondary source; no further ceiling to raise without live instance | n/a — ceiling reached |

## Gate: `JT-01` (Valuation Policy Owner)

| ID | Blocking reason | Evidence that clears it | Owner |
|---|---|---|---|
| `CGS-U06` | Expense Account field is mode-polymorphic | Direct field-level re-fetch across modes | Research/Docs owner |
| `CGS-U07` | Re-class behavior on category change undocumented | Live-instance test | Research owner (blocked, no live instance) |
| `CGS-U08` | Effect on existing stock undocumented | Live-instance test | Research owner (blocked) |
| `CGS-U09` | Fallback-layer existence unconfirmed | Community claim needs official-source confirmation | Research/Docs owner |
| `CGS-U11` | Fiscal Position override scope undocumented | Direct re-fetch | Research/Docs owner |
| `CGS-U12` | Current-version field mapping incomplete | Direct re-fetch (two prior attempts failed) | Research/Docs owner |
| `CGS-U13` | Company-exclusivity of accounting package unconfirmed | Direct re-fetch or live-instance test | Research owner |
| `CGS-U42` | Category company-scoping unconfirmed against official docs | Official-source confirmation or live-instance test | Research owner (partially blocked) |

## Gate: Boss Account Ruling / Control Design (not a specific `JT`, but a hard gate)

| ID | Blocking reason | Evidence that clears it | Owner |
|---|---|---|---|
| `CGS-U16` | Late-arriving cost has no SMEsPlus-specific attribution rule | Design decision, not a fact — routed to Boss | Boss |
| `CGS-U22` | Unconfigured loss has no safe default account | Design decision — routed to Boss | Boss |
| `CGS-U25` | Periodic accrual-visibility mechanism undocumented; blocks `JT-06` design | Direct re-fetch pass | Research/Docs owner |
| `CGS-U34` | Landed-cost residual posting contradicts across sources | Contradiction, not closable by reading; routed to Boss with both readings presented | Boss |
| `CGS-U36` | Documented control-break case (no journal entry generated) | Same — Boss must decide SMEsPlus's own control, not adopt a reference failure mode | Boss |

## Summary

All 18 P0 items are accounted for; none is silently dropped from this register. Of the 18: **8** are clearable by a bounded documentation re-fetch this session did not have tool access to perform (no live web-fetch capability confirmed working this session — see file `01` §2), **2** require a live reference-instance walkthrough (unavailable), and **8** are not fact gaps at all — they require a Boss ruling and cannot be closed by any amount of further reading. This 8/2/8 split is itself new organizing work product of this session; no P0 item was closed.
