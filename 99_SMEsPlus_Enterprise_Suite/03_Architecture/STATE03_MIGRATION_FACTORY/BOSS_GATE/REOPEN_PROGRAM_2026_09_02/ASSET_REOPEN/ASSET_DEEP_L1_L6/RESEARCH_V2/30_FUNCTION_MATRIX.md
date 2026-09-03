# 30 — ASSET FUNCTION MATRIX
**LAYER 2 — AUDIT QUARANTINE**

Required matrix A (§82). Every cell carries a classification. **No cell is blank.**

`FV` FACT VERIFIED · `SI` SUPPORTED INTERPRETATION · `DC` DESIGN CANDIDATE ·
`CT` CONTRADICTED · `VG` VERIFIED GAP · `UN` UNRESOLVED

| ID | Function | Exists | Trigger | State effect | GL effect | Analytic | Audit trail | Class |
|---|---|---|---|---|---|---|---|---|
| F01 | Create manually | Yes | user | → draft | none | user | create log | `FV` |
| F02 | Create from vendor bill | Yes | bill posting on a flagged account | → draft/open | none | **inherited from the line** | message on bill and asset | `FV` |
| F03 | Split by line quantity | Yes | account flag | N × draft | none | inherited | as F02 | `FV` |
| F04 | Apply a template | Yes | selecting a model | fields copied | none | default only | none | `FV` |
| F05 | Convert a posted entry | Yes | action on a move | → draft | none | none | none | `FV` |
| F06 | Confirm | Yes | user | draft → open | **whole board posted, incl. future** | per line | tracked parameters | `FV` |
| F07 | Compute board | Yes | confirm / button | — | entries created and posted | per line | none | `FV` |
| F08 | Post depreciation | Yes | automatic | — | Dr expense / Cr accumulated | both lines | chatter per entry | `FV` |
| F09 | Re-evaluate upward | Yes | wizard | **new child asset** | Dr asset / Cr counterpart | copied | tracked + link message | `FV` |
| F10 | Re-evaluate downward | Yes | wizard | — | value-change entry | inherited | tracked | `FV` |
| F11 | Change duration / period | Yes | wizard | — | catch-up + rebuild; **children cascaded** | inherited | tracked | `FV` |
| F12 | Change accounts / journal | Yes | wizard | — | catch-up; **history keeps old accounts** | inherited | **not tracked** | `FV` |
| F13 | Change method | Yes | wizard | — | future only | inherited | **not tracked** | `FV` |
| F14 | Change computation mode | Yes | direct field edit | — | recompute on next board build | inherited | **not tracked** | `FV` |
| F15 | Change residual | Yes | wizard | possible child asset | catch-up + rebuild | inherited | tracked | `FV` |
| F16 | Pause | Yes | wizard | open → paused | catch-up entry posted | inherited | chatter | `FV` |
| F17 | Resume | Yes | button | paused → open | rebuild; **end date extends** | inherited | chatter | `FV` |
| F18 | Dispose | Yes | wizard | → close (with children) | multi-line disposal | on every line | chatter | `FV` |
| F19 | Sell | Yes | wizard + posted invoice | → close | disposal + proceeds | on every line | chatter | `FV` |
| F20 | Cancel | Yes | button | → cancelled | **all posted entries reversed** | reversal inherits | **detailed entry-by-entry log** | `FV` |
| F21 | Reset to draft | Yes | button | → draft | none | — | none | `FV` |
| F22 | Reset to running | Yes | button | close → open | rebuild; **disposal entry left in place** | inherited | none | `FV` |
| F23 | Archive | Yes | checkbox | — | none | — | none | `FV` |
| F24 | Delete | Yes | user | gone | none | — | message on source move | `FV` |
| F25 | Depreciation schedule report | Yes | menu | — | — | — | — | `FV` |
| F26 | Equipment status flip on confirm | **Custom** | F06 | equipment → *To Assets* | none | — | **none, and no inverse** | `FV` |
| F27 | Equipment deactivate on sale | **Intended** | F19 | — | — | — | — | **`CT`** — dead code |
| F28 | Transfer an asset | **No** | — | — | — | — | — | `VG` |
| F29 | Split an existing asset | **No** | — | — | — | — | — | `VG` |
| F30 | Merge assets | **No** | — | — | — | — | — | `VG` |
| F31 | Impairment | **No** | — | — | — | — | — | `VG` |
| F32 | Revaluation surplus (IAS-16 model) | **No** | — | — | — | — | — | `VG` |
| F33 | Component depreciation | **No** | — | — | — | — | — | `VG` |
| F34 | Tax book / second schedule | **No** | — | — | — | — | — | `VG` |
| F35 | Sub-ledger ↔ GL reconciliation | **No** | — | — | — | — | — | `VG` |
| F36 | Foreign-currency asset | **No** | — | — | — | — | — | `VG` |
| F37 | Units-of-production depreciation | **No** | — | — | — | — | — | `VG` |
| F38 | Useful-life review prompt | **No** | — | — | — | — | — | `VG` |
| F39 | Template divergence report | **No** | — | — | — | — | — | `VG` |
| F40 | Analytic divergence report | **No** | — | — | — | — | — | `VG` |
| F41 | Asset → production cost | **No** | — | — | — | — | — | `VG` — `27` |
| F42 | Post-depreciation internal usage | **No** | — | — | — | — | — | `VG` / `DC` |
| F43 | Lock-date guard on confirm and pause | **Unknown** | — | — | — | — | — | **`UN`** — `UNR-09` |

**26 functions verified present · 1 contradicted · 15 verified gaps · 1 unresolved.**
