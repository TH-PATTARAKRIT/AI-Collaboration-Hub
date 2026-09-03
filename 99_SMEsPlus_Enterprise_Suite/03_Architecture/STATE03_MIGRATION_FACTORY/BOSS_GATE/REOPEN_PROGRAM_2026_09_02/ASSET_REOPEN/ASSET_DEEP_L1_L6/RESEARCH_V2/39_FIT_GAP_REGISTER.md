# 39 — FIT / GAP REGISTER
**LAYER 2 — AUDIT QUARANTINE**

§84. Each reference capability classified `ADOPT SEMANTICS` · `ADAPT` · `EXTEND` ·
`REJECT` · `UNKNOWN`. **Never `COPY IMPLEMENTATION`.**

## 1. Semantics worth adopting

| # | Capability | Why | Class |
|---|---|---|---|
| 1 | **The schedule *is* the journal entries** | Removes an entire class of sub-ledger/GL reconciliation problem at zero cost | `ADOPT SEMANTICS` |
| 2 | **Posted entries are immutable; every change is catch-up + reverse-future + rebuild-forward** | Audit-grade by construction. The single best property of the reference design | `ADOPT SEMANTICS` |
| 3 | **Cumulative-difference amount computation** | Rounding cannot drift; no balancing plug is ever needed. Verified across every tested scenario | `ADOPT SEMANTICS` |
| 4 | **Value is a derivation, not a column** | Prevents the whole class of "the register does not tie" defects | `ADOPT SEMANTICS` |
| 5 | **State is read-only; every transition is a guarded method** | Thirteen guards depend on it | `ADOPT SEMANTICS` |
| 6 | **The board invariant** — a running asset's last line must leave zero | The strongest single guarantee in the engine | `ADOPT SEMANTICS`, but **enforce it at the data layer too** (`CTR-06`) |
| 7 | **Cancellation's audit message** — every reversed entry listed with date, reference and value, plus the net effect on both accounts | Exemplary. Copy the behaviour, not the code | `ADOPT SEMANTICS` |
| 8 | **Off-balance accounts structurally excluded from asset accounts** | Enforces the Boss's own boundary by construction rather than policy | `ADOPT SEMANTICS` |
| 9 | Account-driven automatic asset creation from supplier invoices | A sound trigger model | `ADOPT SEMANTICS` |
| 10 | Balance-weighted analytic inheritance from the source document | Correct default behaviour | `ADOPT SEMANTICS` |

## 2. Adapt

| # | Capability | Required adaptation | Class |
|---|---|---|---|
| 11 | Three depreciation methods | Keep. **Add the Thai calendar-day basis as an explicit, first-class, per-company default** rather than one of three prorata options | `ADAPT` |
| 12 | The prorata computation mode | **Rename and re-present it.** The current label gives no hint that one option ignores the calendar (`UI-03`) | `ADAPT` |
| 13 | *Duration* + *period length* | **Re-present as one unambiguous concept.** "Duration 60" meaning 60 years is a user trap (`UI-01`) | `ADAPT` |
| 14 | Asset Model as a template | **Decide: template or policy.** If template, add a divergence report. If policy, make it govern | `ADAPT` |
| 15 | Confirm posting the whole life | Keep, but **make it explicit to the user** and reconcile with period-close design | `ADAPT` |
| 16 | Upward revaluation creating a child asset | Semantically defensible. **Ensure the equipment association and cost pool follow the tree** — today the child does not inherit the link | `ADAPT` |
| 17 | The one wizard driving five actions | **Separate them.** Five accounting events behind one control is a training and permission risk (`UI-06`) | `ADAPT` |
| 18 | Analytic copied at posting | Keep the model. **Add the divergence report the reference product lacks** | `ADAPT` |
| 19 | The production cost chain, links 2–6 | Reuse the absorption machinery. **Fix the four inherited defects** in `36` §4 | `ADAPT` |

## 3. Extend

| # | Gap | Extension | Class |
|---|---|---|---|
| 20 | **Operation → Equipment** | The structural prerequisite for the toll-gate requirement | `EXTEND` |
| 21 | **Asset ↔ Equipment, properly** | Constrained, validated, with an inverse, and behaviours that actually execute | `EXTEND` |
| 22 | **Per-machine cost pool from the sub-ledger** | The core differentiator | `EXTEND` |
| 23 | **Absorption variance** | `GAP-ABS-VAR`. Missing from the reference chain and from the Boss's hypothesis | `EXTEND` |
| 24 | **A tax book** | Six for six impossible today. The largest functional gap for a Thai deployment | `EXTEND` |
| 25 | **A capitalisation / under-construction stage** | Absent. Matters for self-built plant assets | `EXTEND` |
| 26 | **Asset transfer** | Recorded separately from split and merge at Expert 1's insistence (`D3-02`): transfer is commercially common, the other two are rare | `EXTEND` |
| 27 | **Sub-ledger ↔ GL reconciliation** | The reference product needs it too, because of the import field | `EXTEND` |
| 28 | **Maintenance cost capture** | No monetary field exists. Contested as a differentiator (`D4-01`) | `EXTEND` — pending `D4-01` |
| 29 | **A fully-depreciated condition** | Required as the trigger for the internal usage design | `EXTEND` |
| 30 | **Audit tracking on the computation mode, method, accounts and analytic** | Today untracked. A cheap, material control improvement | `EXTEND` |
| 31 | **Disclosure prompt on mid-life method change** | A change in estimate, permitted silently (`D6-02`) | `EXTEND` |
| 32 | **Useful-life and residual review prompt** | Required by the accounting standards, absent from the product | `EXTEND` |
| 33 | **Post-depreciation internal usage ledger** | Entirely original. `DESIGN CANDIDATE` throughout | `EXTEND` |

## 4. Reject

| # | Capability | Why | Class |
|---|---|---|---|
| 34 | The 30/360 convention as a **default** | Distorts monthly amounts by up to 8% and is invisible in annual totals | `REJECT` as default; retain as an option only if a customer requires it |
| 35 | *No prorata* mode (backdating to the fiscal year start) | Incompatible with "in proportion to the period from acquisition" | `REJECT` |
| 36 | The dormant currency-conversion path | Code that appears to support foreign-currency assets and cannot | `REJECT` — either support it properly or omit it |
| 37 | Invisible fields that change money — paused days, stored gain | Audit holes | `REJECT` |
| 38 | Reading the stored gain-on-sale field | It can differ from the posted figure by the residual (`CTR-05`) | `REJECT` |
| 39 | A single hourly rate conflating cost pool and driver | The precise reason the reference model cannot answer "which machine" | `REJECT` |

## 5. Unknown

| # | Item | Blocking evidence |
|---|---|---|
| 40 | Whether Thai practice permits depreciation absorbed into inventory | `UNR-03` |
| 41 | How off-balance accounts appear in Thai statutory statements | `UNR-23` |
| 42 | Whether the daily unit is statutory | `UNR-01` |
| 43 | The correct grain for a per-machine rate | `UNR-24` |
| 44 | Whether maintenance cost is genuinely uncaptured or merely uncaptured in that module | `D4-01` |

## 6. Unresolved expert disagreements carried here

| ID | Item | Status |
|---|---|---|
| `D1-01` | Capitalisation: `ABSENT` or `PARTIAL`? | Open — affects whether item 25 is an extension or a new build |
| `D1-02` | Revaluation: boundary statement or `PARTIAL`? | Open — affects how item 16 is presented |
| `D2-02` | Should "Depreciation Board" survive as a term? | Open — item 1 says the schedule *is* the entries, which supports retiring it |
| `D3-02` | Transfer / split / merge as one gap or three | **Resolved** — transfer separated, item 26 |
| `D4-01` | Maintenance costing as a differentiator | Open — item 28 |
| `D5-01` | Unbounded cumulative internal usage | Escalated to the Boss — `UNR-B3` |
| `D5-02` | Where machine identity should live | Open architecture decision |
| `D6-01` | Whether to report the Level 6 scoreboard | Recorded; Expert 4's objection stands |
