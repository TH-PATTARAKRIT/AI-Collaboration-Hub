# 31 — MODEL AND FIELD RELATIONSHIP MATRIX
**LAYER 2 — AUDIT QUARANTINE**

Required matrices C and D (§82). Built model-first, not FK-first (§40).

## 1. Models in scope

| Model | Owner | Role | In the asset domain? |
|---|---|---|---|
| Asset | reference product | The sub-ledger record, and its own template, and its own value-increase component | **Core** |
| Asset group | reference product | Reporting grouping, no behaviour | Core |
| Modify wizard | reference product | Transient; five actions | Core |
| Journal entry / journal item | accounting | **Where asset value actually lives** | Core |
| Account | accounting | Configuration + the asset-creation trigger | Core |
| Company | base | Currency, fiscal year, gain/loss accounts | Core |
| Equipment | maintenance | Operational identity | Adjacent — custom link only |
| Maintenance request | maintenance | Operational events, **no money** | Adjacent |
| Work centre | manufacturing | The hourly rate and its analytic | Adjacent |
| Operation (routing line) | manufacturing | **No equipment field** | Adjacent |
| Work order | manufacturing | Cost carrier; **rate snapshotted** | Adjacent |
| Manufacturing order | manufacturing | Absorption point | Adjacent |
| Stock valuation layer | stock accounting | FG cost | Adjacent |
| Analytic line / analytic account | analytic | The one shared dimension | Core |

## 2. Relationship matrix — asset outward

| From | Field kind | To | Cardinality | Owner | Class |
|---|---|---|---|---|---|
| Asset | M2o | Company | N:1, **required** | product | `FV` |
| Asset | related | Currency | via company; **not settable** | product | `FV` |
| Asset | M2o ×3 | Account | N:1 each; **off-balance excluded by domain** | product | `FV` |
| Asset | M2o | Journal | N:1, general only | product | `FV` |
| Asset | M2o | Asset (template) | N:1 | product | `FV` |
| Asset | M2o / O2m | Asset (parent/children) | **self-referencing tree** | product | `FV` |
| Asset | M2o | Asset group | N:1 | product | `FV` |
| Asset | M2m | Journal item (source) | N:N; **immutable once running** | product | `FV` |
| Asset | O2m | Journal entry (depreciation) | 1:N, cascade delete | product | `FV` |
| Asset | JSON | Analytic distribution | 1:N with weights | analytic mixin | `FV` |
| Asset | **M2o** | **Equipment** | **N:1, no inverse, no unique constraint** | **custom** | `FV` |
| Asset | related | Equipment group reference | read-only passthrough | custom | `FV` |
| **Asset** | — | **Product** | **none** | — | `VG` |
| **Asset** | — | **Purchase order / receipt** | **none** | — | `VG` |
| **Asset** | — | **Work centre / operation / order** | **none** | — | `VG` |
| **Asset** | — | **Maintenance request** | **none** | — | `VG` |

## 3. Relationship matrix — the operational side

| From | To | Cardinality | Owner | Class |
|---|---|---|---|---|
| Equipment | Category | N:1 | product | `FV` |
| Equipment | **Work centre** | **N:1** | manufacturing bridge | `FV` |
| Work centre | Equipment | 1:N (inverse) | manufacturing bridge | `FV` |
| Maintenance request | Equipment | N:1 | product | `FV` |
| Maintenance request | Work centre | N:1, computed from the equipment | manufacturing bridge | `FV` |
| Maintenance request | Manufacturing order / work order | N:1 each, **reference only** | manufacturing bridge | `FV` |
| Maintenance request | Calendar leave | N:N — **the capacity effect** | manufacturing bridge | `FV` |
| **Operation** | **Equipment** | **none** | — | **`VG` — the structural gap** |
| Operation | Work centre | N:1, required | product | `FV` |
| Work order | Operation | N:1 | product | `FV` |
| Work order | Work centre | N:1, **rate copied at creation** | product | `FV` |
| Equipment | Product | via the custom stock bridge | custom | `FV` |
| **Equipment** | **Account / analytic / journal** | **none** | — | `VG` |

## 4. Field characteristics — the ones that change behaviour

| Field | Characteristic | Why it matters |
|---|---|---|
| Computation mode | plain stored, **not tracked** | Selects between 30/360 and calendar days. No audit trail — `24` §5 |
| Duration | tracked | Number of **periods**, not months |
| Period length | tracked | Two legal values only |
| Book value | **stored, recursive** | A tree aggregate, not a row property |
| Depreciable value | computed, not stored | Derived from posted entries |
| Not-depreciable value | computed + stored | Excluded from the base |
| Not-depreciable percentage | plain | **The only live rule a template retains** |
| Paused days | stored, `copy=False`, **invisible in the form** | Shifts the entire remaining schedule |
| Already-depreciated-on-import | plain | **Breaks sub-ledger/GL agreement by design** |
| Net gain on sale | stored, **invisible in the form** | Can differ from the posted gain by the residual |
| Analytic distribution | computed + stored, **not tracked** | Copied at entry preparation; changes apply forward only |
| Equipment link | custom M2o, **inert read-only rule** | Editable on running and closed assets |
| Asset lifetime days | computed, **recursive**, invisible | 1800 or 1826 depending on one other field |
