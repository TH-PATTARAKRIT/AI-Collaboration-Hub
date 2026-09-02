# 22 — Manufacturing: Raw Material → WIP → Finished Goods → COGS Research

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `EVIDENCE COLLECTION — CP-08` — Layer A observed from reference-ERP official documentation (manufacturing/inventory valuation) and official-forum evidence; scope status explicitly unresolved at programme level (see §2).

---

## 1. Purpose and Scope

This file proves, from Layer A reference-ERP evidence, where a manufacturing/production module's documentation draws the raw-material (RM) → work-in-progress (WIP) → finished-goods (FG) → COGS boundary, and what the reference system documents for standard-cost variance treatment in manufacturing. It directly answers governing prompt §10 scenarios `#27` (RM consumption), `#28` (WIP → FG), and `#29` (FG → COGS), and feeds `JT-09` (WIP recognition timing — Joint, not closed here).

This file does **not** decide whether Manufacturing is in SMEsPlus v1.0 scope. That is `GAP-FS-19` (below).

---

## 2. Manufacturing Scope Note — `GAP-FS-19` (Read Before Anything Else in This File)

Inventory Final Solution v1.0's risk/gap register records, verbatim in substance:

> `GAP-FS-19` — Whether Manufacturing is in SMEsPlus v1.0 scope, which determines whether the manufacturing handoffs are live or deferred. Classified `MATERIAL — programme scope`. Owner: `Boss`.

That same package's cross-module handoff register carries a manufacturing valuation handoff row (`HX-20`) explicitly tied to `JT-09` (work-in-progress recognition timing) as a Joint, unresolved item — present in the handoff vocabulary but not designed as a committed feature.

**This file's status given that gap**: this session was directed to research the manufacturing cost-flow boundary regardless, so that if/when the Boss decides `GAP-FS-19` in favor of including Manufacturing in v1.0 (or in a defined later phase), the Accounting side has already exhausted the material unknowns rather than starting cold. **Nothing in this file should be read as asserting Manufacturing is in scope.** Every archetype below is written as evidence-in-reserve, explicitly conditional on a future, separate Boss decision on `GAP-FS-19`. If that decision is "not in v1.0 scope," this file's content becomes forward-looking reference material for a later phase, not a current design.

---

## 3. Layer A — What "Manufacturing" Means in the Reference System's Documentation

The reference ERP documents a dedicated Manufacturing application built on: a Bill of Materials (BOM) describing components and quantities per finished unit; a Manufacturing Order (MO) instantiated against a BOM; Work Orders/work centers for operation-level costing; and a **Production** virtual location that inbound components move into and finished goods move out of. Source: Reference ERP official documentation — Manufacturing order costs, versions 17.0 and 19.0, retrieved 2026-09-02.

**Eligibility gate for automatic journal entries (material precondition)**: reference-forum evidence, corroborated across two independent threads, states that manufacturing accounting entries are generated **only** when the component/finished-good product categories use automated/real-time (in 19.0-era terminology, "Perpetual") inventory valuation with Stock Input, Stock Output, Stock Valuation, and a Production-location cost account all configured. Without automated valuation, the reference system tracks quantity movement but produces no journal entries at all for the manufacturing flow. Source: reference-community forum discussion on manufacturing accounting entries in the current major reference version, retrieved 2026-09-02; reference-community forum discussion, "Manufacturing - accounting full work flow", retrieved 2026-09-02.

**Layer C candidate note:** this eligibility gate is structurally the same shape as the landed-cost eligibility gate in file `21` §3.1 — a costing/valuation-mode precondition determines whether a financial fact is even produced. This reinforces the general principle already implicit in the Inventory-side design (`Inventory emits facts; Accounting decides postings`) that **the presence of a posted fact is itself conditional on configuration**, and Accounting cannot assume a manufacturing event always yields a journal entry to consume.

---

## 4. Layer A — The RM → WIP → FG Boundary, Two Distinct Documented Mechanisms

This session found **two structurally different, version-separated mechanisms** in the reference documentation for how RM-to-WIP-to-FG value flows through accounts. Both are recorded because conflating them would misrepresent the version-delta reality the governing prompt requires to be proven, not assumed away (§5, "no silent carry-forward").

### 4.1 Mechanism 1 — Production-location cost account (documented across versions, no dedicated "WIP journal entry" feature)

- `REFERENCE OBSERVATION`: A virtual **Production** location carries a configurable "Cost of Production" account (documented as configurable per-location under Inventory Valuation settings, distinct from the general Inventory Loss/Variation account). When a component is consumed into a manufacturing order, value moves out of the raw-material Stock Valuation account and into this Production-location account; when the manufacturing order completes, value moves out of the Production-location account and into the finished-good Stock Valuation account, clearing the Production-location balance automatically at MO close. Source: Reference ERP official documentation — Inventory valuation configuration, version 15.0, retrieved 2026-09-02; corroborated by reference-community forum discussion on work-in-progress valuation, retrieved 2026-09-02.
- `ACCOUNTING MEANING`: This is a **single-step, automatic** value transfer mechanism — the "WIP" state exists only as a balance sitting in the Production-location account between the moment components are consumed and the moment the MO is marked done. There is no separate, dated, manually-controlled WIP journal entry in this mechanism; the Production-location account is itself the WIP proxy, and it is expected to net to zero once every open MO using it completes.
- `THAI RULE STATUS`: `HOLD` — file `24` owns whether Thai practice requires WIP to be a distinct, dated balance-sheet line versus a transient clearing account.
- `SMEPLUS CANDIDATE / HOLD`: `HOLD / EVIDENCE REQUIRED`, pending `GAP-FS-19` and `JT-09`. Recorded as one documented pattern: WIP-as-transient-clearing-balance, cleared automatically on completion, with no independent approval step.
- **Documented limitation** (material to `JT-09`): reference-community evidence for versions up to and including 15.0 states this mechanism only supports what it calls "PLANNED WIP" (a Bill-of-Materials-structure-and-cost report) and "ACTUAL WIP" (a Manufacturing Order Cost Analysis report) as **reporting views**, not as a progressively-updated balance-sheet WIP account during a long-running order — the accounting entry itself is described as landing in a single step at consumption/completion, not incrementally as operations progress. Real-time, progressive WIP tracking during a long manufacturing run is explicitly described as requiring customization beyond the documented base feature. Source: reference-community forum discussion on work-in-progress valuation, retrieved 2026-09-02, version context 14.0–15.0.

### 4.2 Mechanism 2 — Dedicated, manually-posted WIP journal entry feature (version 19.0 only, in evidence retrieved)

- `REFERENCE OBSERVATION`: Version 19.0's documentation describes a distinct, opt-in feature: a manufacturing order can have a "Post WIP Accounting Entry" action invoked manually, which posts a dated journal entry debiting a dedicated **WIP Account** (documented default label "Work in Progress") and a **WIP Overhead Account** (documented default label "Cost of Production") against consumed-component and incurred work-order cost, specifically to represent the value of a manufacturing order that is still open at a reporting cut-off. The documentation distinguishes "MO Cost" (planned, BOM-derived) from "Real Cost" (actual, incurred-to-date). This WIP entry is explicitly temporary: the documentation states it must be manually reversed once the order completes, and schedules an automatic reversal for the following day by default (adjustable). Source: Reference ERP official documentation — Work-in-progress costs, version 19.0, retrieved 2026-09-02; corroborated by reference-community forum discussion on manufacturing accounting entries in the current major reference version, retrieved 2026-09-02.
- `ACCOUNTING MEANING`: This is a **deliberate, dated, reversing accrual** — the accounting purpose is specifically to state the value of unfinished production truthfully as of a period cut-off (e.g., month-end) for a manufacturing order that spans the cut-off, then to undo that accrual once it is no longer needed (either because the order completed and its actual cost flowed through the ordinary consumption/completion mechanism, or because a new cut-off requires a fresh WIP snapshot). This is conceptually a period-end accrual/reversal discipline, not a permanent account balance.
- `THAI RULE STATUS`: `HOLD`.
- `SMEPLUS CANDIDATE / HOLD`: `HOLD / EVIDENCE REQUIRED`, pending `GAP-FS-19` and `JT-09`. Recorded as a second, materially different documented pattern: WIP-as-deliberate-period-end-accrual, manually triggered and manually/automatically reversed, distinct from Mechanism 1's always-on transient clearing balance.
- **Documentation gap found**: the primary version-19.0 documentation page retrieved does **not** explicitly state whether Mechanism 2 (manual WIP accrual) and Mechanism 1 (Production-location automatic clearing) operate simultaneously on the same manufacturing order, replace each other, or are mutually exclusive configuration choices. `NOT FOUND / HOLD` — flagged as a material follow-up question, not resolved by inference.

### 4.3 Version Delta — `VD-MFG-01`

| Delta ID | Observation | Versions | Status |
|---|---|---|---|
| `VD-MFG-01` | Mechanism 1 (Production-location automatic clearing account acting as the WIP proxy) is the only documented mechanism found for versions up to 18.0. Mechanism 2 (dedicated manual WIP Account / WIP Overhead Account journal-entry feature with scheduled reversal) is documented only for version 19.0 in the evidence retrieved. Whether Mechanism 2 is genuinely new in 19.0, or whether it existed earlier under different documentation coverage that this session's searches did not surface, is **not conclusively established** — this session found no 19.0 documentation page stating "this is new," and found no pre-19.0 documentation page describing an equivalent manually-posted, reversing WIP entry with dedicated named accounts. Treated as `PROVISIONAL — LIKELY VERSION-INTRODUCED`, not `VERIFIED — CONFIRMED NEW`. | pre-19.0 vs. 19.0 | `PROVISIONAL` |

**Do not silently carry forward** (per governing prompt §5): a SMEsPlus design built only from Mechanism 1 (the older, always-on clearing pattern) would miss the newer accrual/reversal discipline; a design built only from Mechanism 2 would wrongly assume every version has a dedicated, manually-triggered WIP entry with scheduled reversal. Both must be weighed once `GAP-FS-19` is decided.

---

## 5. RM → WIP → FG → COGS: Full Archetype Chain

### 5.1 Raw-material consumption (Scenario #27)

- `REFERENCE OBSERVATION`: When components are consumed against a manufacturing order (under Mechanism 1, at the moment of the consumption stock move; under Mechanism 2, additionally reflected in a manually-posted interim entry before completion), the documented entry pattern is: debit the WIP/Production account, credit the raw-material Stock Valuation account, for the quantity and cost of components actually consumed (not merely planned). Source: reference-community forum discussion, "Inventory Accounting: Manufacturing", retrieved 2026-09-02; reference-community forum discussion, "Manufacturing - accounting full work flow", retrieved 2026-09-02.
- `ACCOUNTING MEANING`: This is a **reclassification within inventory-type value**, not an expense recognition and not COGS. Raw material asset value is not destroyed by consumption into production — it is relocated to a different asset-side bucket (WIP) representing partially-transformed inventory. This is direct evidence for the governing prompt's foundational statement that "not every reduction in Inventory Value is COGS" (§2, §8.1) — RM consumption into production is exactly such a non-COGS reduction.
- `THAI RULE STATUS`: `HOLD` — file `24` owns whether Thai practice requires component consumption to be valued at actual issue cost per the product's costing policy (FIFO/AVCO/Standard) with no additional adjustment, or whether absorption of production overhead into WIP has specific Thai presentation requirements.
- `SMEPLUS CANDIDATE / HOLD`: `HOLD`, pending `GAP-FS-19`/`JT-09`. Directional note only: whatever SMEsPlus decides, the RM-to-WIP step should be modeled as an asset reclassification (Inventory Cost Released "OR another explicitly approved financial classification," per governing prompt §14's Cost Release identity — here, the "another classification" is WIP, not COGS).

### 5.2 WIP → Finished goods (Scenario #28)

- `REFERENCE OBSERVATION`: On marking a manufacturing order complete/done, the documented entry pattern reverses the WIP/Production debit into the finished-good's Stock Valuation account: debit Finished Goods Stock Valuation, credit WIP/Production account, for the accumulated cost of components consumed plus (where work-center/operation costing is configured) labor/overhead cost incurred. One reference-forum answer states explicitly that "there is no separate journal entry for 'return to inventory'" — it is folded into the completion valuation step itself, not a distinct manual action, under Mechanism 1. Source: reference-community forum discussion, "Manufacturing - accounting full work flow", retrieved 2026-09-02.
- `ACCOUNTING MEANING`: A second asset-to-asset reclassification — WIP value becomes finished-goods inventory value. Still not COGS. The finished-good's resulting unit cost is documented as a **rolling average of every completed MO's actual cost** for that product (not a single MO's cost carried in isolation), meaning the finished-goods cost figure that eventually flows to COGS on sale already embeds whatever actual-vs-planned divergence occurred during production, smoothed across completed orders.
- `THAI RULE STATUS`: `HOLD`.
- `SMEPLUS CANDIDATE / HOLD`: `HOLD`, pending `GAP-FS-19`/`JT-09`. Material open question flagged for the Joint session: **should a SMEsPlus finished-good's cost be a rolling average across completed orders (reference pattern), or should each completed order preserve its own discrete cost layer** (relevant if SMEsPlus's inventory-side costing policy is FIFO/specific-identification rather than average)? The reference pattern's rolling-average behavior is evidence, not a SMEsPlus requirement — costing-method choice for manufactured goods is itself unresolved (`JT-02` territory, this file only surfaces the manufacturing-specific angle of it).

### 5.3 Finished goods → COGS on sale (Scenario #29)

- `REFERENCE OBSERVATION`: No manufacturing-specific documentation page retrieved in this session describes a distinct COGS-recognition mechanism for manufactured finished goods — the sale of a manufactured product is documented to follow the same delivery/invoice-driven COGS recognition already governing any other stock item under the applicable Periodic/Perpetual policy (owned by files `12`/`13`/`18`, not re-derived here).
- `ACCOUNTING MEANING`: This is the point at which manufactured inventory value finally converts from an asset-side classification (finished-goods Stock Valuation) to an expense-side classification (COGS) — the same "Cost Release → COGS or another approved classification" identity as any purchased product, with the only manufacturing-specific difference being *how the FG cost figure itself was built* (§5.1–5.2), not *when or how it is released to COGS*.
- `THAI RULE STATUS`: `HOLD`.
- `SMEPLUS CANDIDATE / HOLD`: No new candidate asserted here — this file explicitly defers to files `13`/`18` for the recognition-timing rule itself, and records only that manufacturing does not appear (per evidence retrieved) to introduce a second, parallel COGS-timing rule of its own.

---

## 6. Standard-Cost Variance Treatment in Manufacturing

- `REFERENCE OBSERVATION`: The reference documentation distinguishes **"MO Cost"** (the estimated cost to complete an order, computed from the Bill of Materials' planned component quantities and planned operation durations) from **"Real Cost"** (the actual cost, updated as real component consumption and real operation durations are recorded, finalized at MO completion). The documentation states these two figures are tracked and can diverge when actual usage exceeds or falls short of the BoM's planned figures. Source: Reference ERP official documentation — Manufacturing order costs, versions 17.0 and 19.0, retrieved 2026-09-02.
- `ACCOUNTING MEANING — MATERIAL GAP FOUND`: The retrieved documentation describes MO Cost vs. Real Cost as a **reporting/analysis distinction** (surfaced through a Production Analysis report and the MO's own cost fields), not as a **posted variance account** comparable to the Price Difference Account mechanism found for purchase-price variance under Standard Price costing (file `21` §4.1). No documentation page or forum thread retrieved in this session describes a dedicated "manufacturing standard cost variance" account, or an automatic posting that isolates a favorable/unfavorable production variance the way purchase-price variance is isolated. `NOT FOUND / HOLD` — this is a genuine absence of evidence, not an inferred "the reference system does not do this."
- `THAI RULE STATUS`: `HOLD` — routed to file `24`. Thai cost-accounting practice for standard-cost manufacturers (materials/labor/overhead variance recognition and presentation) is a Layer B question this file cannot answer from Layer A evidence alone.
- `SMEPLUS CANDIDATE / HOLD`: `HOLD / EVIDENCE REQUIRED`. This is flagged as the **single most material open item in this file**: if SMEsPlus ever supports Standard Cost as a manufacturing costing policy (contingent on `GAP-FS-19` first deciding Manufacturing is in scope, and `JT-02` deciding Standard Cost is a permitted method), the reference system's evidence trail does not hand SMEsPlus a ready-made variance-posting pattern for production the way it does for purchasing (file `21` §4.1). A production standard-cost variance mechanism, if required, would need to be independently designed and justified against Thai evidence, not adapted from an observed reference pattern — because no such reference pattern was found. `LC-04`'s principle ("a fixed planned cost is a variance question, not a cost-basis edit") should be read as extending to manufacturing by the same logic that already applies to purchasing, but this file found no reference-system implementation to point to as precedent for *how*.

---

## 7. Reconciliation Identity Challenge (governing prompt §14, scoped to this file)

`Inventory Value = Opening + Capitalizable Cost Added − Cost Released ± Approved Valuation Adjustments`

- **Candidate application to manufacturing**: "Capitalizable Cost Added" for a finished good includes consumed raw-material cost plus (where configured) work-center/operation cost, accumulated through the WIP stage before reaching finished-goods valuation — `CANDIDATE`, evidence-supported (§5.1–5.2).
- **Candidate application of "Cost Released"**: RM consumption is a reclassification (RM → WIP), not a release to COGS; WIP completion is a further reclassification (WIP → FG), not a release to COGS; only the eventual sale of the finished good is a release event under this identity — `CANDIDATE`, evidence-supported, and directly reinforces governing prompt §2's "not every reduction in Inventory Value is COGS" for the manufacturing case specifically.
- **Unresolved**: whether a period-end WIP accrual (Mechanism 2, §4.2) should be modeled as part of "Inventory Value" at all under this identity, or as a separate, off-balance-identity memo figure that reverses before the next period's roll-forward — `HOLD`, not decided by evidence retrieved.

---

## 8. Section 15 (9 Veto) Pre-Flags Relevant to This File

Not a full Veto run (owned by file `28`), flagged here for that file:

- **Financial/Accounting/Tax VETO pre-flag**: §6's "no documented production standard-cost variance posting mechanism" finding is material and should block any future assumption that a reference-adapted variance pattern exists for manufacturing the way one exists for purchasing.
- **Audit VETO pre-flag**: §4.3's `VD-MFG-01` version-delta finding is `PROVISIONAL`, not `VERIFIED` — a future audit pass should re-confirm whether Mechanism 2 is genuinely 19.0-introduced before any version-specific SMEsPlus design decision leans on that fact.
- **AI Control/Human Oversight VETO pre-flag**: no journal entry, account code, or cost figure was invented in this file; the "MO Cost"/"Real Cost" and default account labels ("Work in Progress", "Cost of Production") are quoted from the cited source as reference-system defaults, not proposed as SMEsPlus account names.
- **Clean-Room/IP/Provenance VETO pre-flag**: no vendor/product name, code token, or fenced code block appears in this file, consistent with clean-room rules.

---

## 9. Summary Table — SMEsPlus Candidate / HOLD Status

| # | Item | Status |
|---|---|---|
| 1 | Manufacturing scope for SMEsPlus v1.0 | `HOLD` — `GAP-FS-19`, Boss decision, not this session's to make |
| 2 | RM consumption is asset reclassification (RM→WIP), not COGS | `CANDIDATE` (Layer A corroborated) |
| 3 | WIP completion is asset reclassification (WIP→FG), not COGS | `CANDIDATE` (Layer A corroborated) |
| 4 | FG→COGS on sale follows the same timing rule as any other stock item | `CANDIDATE` (no manufacturing-specific override found) |
| 5 | Two structurally different WIP mechanisms exist across reference versions | `PROVISIONAL` — `VD-MFG-01`, needs independent re-confirmation |
| 6 | Whether the two WIP mechanisms coexist or are mutually exclusive | `NOT FOUND / HOLD` |
| 7 | Manufactured finished-goods cost is a rolling average across completed orders (reference pattern) | `PROVISIONAL` — corroborated but not cross-checked against every version |
| 8 | Production/manufacturing standard-cost variance posting mechanism | `NOT FOUND / HOLD` — **most material open item in this file** |
| 9 | Thai cost-accounting requirements for manufacturing (absorption costing, variance presentation) | `HOLD` — file `24` owns |

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
