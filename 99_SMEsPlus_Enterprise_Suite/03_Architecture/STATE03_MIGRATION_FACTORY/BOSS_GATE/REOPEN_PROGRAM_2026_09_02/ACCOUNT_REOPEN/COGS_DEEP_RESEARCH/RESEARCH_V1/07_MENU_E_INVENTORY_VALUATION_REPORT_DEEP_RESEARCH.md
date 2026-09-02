# 07 — Menu E: Inventory Valuation Report Deep Research

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `EVIDENCE IN PROGRESS — CP-03 (Menu E) — Layer A populated, Layer B pointer only, Layer C candidate-only`

---

## 1. Scope

This file answers governing-prompt §6 Menu E: `Inventory -> Reporting -> Inventory Valuation`. It proves, from reference-ERP official documentation only, the quantity/value relationship, the effect of costing method on the report, the opening/inbound/outbound/adjustment/landed/manufacturing/closing value-movement story, as-of-date behavior, drill-down/provenance, reconciliation to Accounting, difference/variance reporting, negative/zero-cost exceptions, and version delta across versions 13.0–19.0. It does not decide SMEsPlus report design. All Layer C content is candidate-only or HOLD.

Feeds open Joint decisions: `JT-01` (policy ownership — the report's dependency on category-level costing/valuation settings), `JT-03` (continuous vs periodic timing — how the report's "closing" values are produced), `JT-06` (late supplier bill / negative-inventory compensation, §9), `JT-07` (period close design, cross-referenced to file `08`).

---

## 2. Layer A — Reference ERP Observed Behavior

### 2.1 Menu path and version delta (navigation)

| Version | Observed menu path (report) | Observed menu path (config) | Fact Status | Evidence |
|---|---|---|---|
| 13.0 | `Inventory -> Reporting -> Inventory Valuation` | `Inventory -> Configuration -> Product Categories` | VERIFIED | Reference ERP official documentation — Using the inventory valuation, version 13.0, retrieved 2026-09-02 |
| 14.0 | `Inventory -> Reporting -> Inventory Valuation` (indexed; page title parallel to 13.0) | `Inventory -> Configuration -> Product Categories` | VERIFIED (config) / PROVISIONAL (report page not independently re-fetched this session, title indexed only) | Reference ERP official documentation — Inventory valuation configuration, version 14.0, retrieved 2026-09-02 |
| 15.0 | `Inventory -> Reporting -> Inventory Valuation` (title indexed) | Not independently fetched this session | PROVISIONAL — title indexed in the documentation index only, content not fetched | Reference ERP official documentation — Using inventory valuation, version 15.0, retrieved 2026-09-02 (index entry only) |
| 16.0 | `Inventory -> Reporting -> Valuation` (dashboard) — this version's documentation set carries **two parallel URL trees** for the same subject: an older `inventory/management/reporting/...` tree and a newer `inventory/product_management/inventory_valuation/...` tree | `Inventory -> Configuration -> Product Categories` | VERIFIED (config, new tree) / PROVISIONAL (old tree content not independently re-fetched this session) | Reference ERP official documentation — Inventory valuation configuration, version 16.0, retrieved 2026-09-02 |
| 17.0 | `Inventory -> Reporting -> Valuation` (dashboard); documentation still resolves under both the old `management/reporting` path and a new `warehouses_storage/inventory_valuation` / `product_management/inventory_valuation` path depending on sub-page | `Inventory -> Configuration -> Product Categories` | VERIFIED (config) / PROVISIONAL (exact report-page path pending single authoritative fetch — two indexed titles observed, not reconciled) | Reference ERP official documentation — Automatic inventory valuation, version 17.0, retrieved 2026-09-02 |
| 18.0 | `Inventory -> Reporting -> Valuation` (Stock Valuation dashboard; the "Valuation" reporting menu entry requires Developer Mode to be visible) | `Inventory -> Configuration -> Product Categories` (category-level) plus `Accounting -> Configuration -> Settings` (Stock Valuation section, global Automatic Accounting toggle) | VERIFIED | Reference ERP official documentation — Using inventory valuation, version 18.0, retrieved 2026-09-02; Reference ERP official documentation — Automatic inventory valuation, version 18.0, retrieved 2026-09-02 |
| 19.0 | `Inventory -> Reporting -> Valuation` (title indexed; direct content fetch of this specific page returned no retrievable body text this session — see §11 gap) | `Inventory -> Configuration -> Product Categories`; global cadence/account settings at `Accounting -> Configuration -> Settings -> Inventory Valuation` | PROVISIONAL (report page body not captured this session) / VERIFIED (config and closing-entry content, via the Accounting-side "Inventory valuation" documentation page) | Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02; Reference ERP official documentation — Valuation cheat sheet, version 19.0, retrieved 2026-09-02 |

**Material finding — documentation reorganization is itself evidence, not noise.** Between roughly version 16.0 and 18.0, the reference documentation set moved this topic from an `inventory/management/reporting/` tree to an `inventory/product_management/inventory_valuation/` (and, for the report specifically, `inventory/warehouses_storage/...`) tree, and the Accounting-side closing narrative moved to a dedicated `finance/accounting/get_started/inventory_valuation.html` page that did not exist in the same form in 13.0–16.0 indexes searched this session. This is treated as `VERSION DELTA — CONFIRMED (documentation structure)`, not yet confirmed as a menu-label change inside the live product for every version (that would require a UI screenshot pass, which is out of scope for this Deep Research file and flagged in §11).

### 2.2 Quantity/value relationship

The dashboard/report is described consistently (18.0 evidence, most detailed capture) as showing, per product (and per grouping dimension the user selects): **Date**, **Quantity**, **Unit Value**, **Total Value**, and a **Reference** to the originating warehouse operation. The identity proven in the documentation is:

`Total Value = Quantity x Unit Value`

Both sides move together on every recorded valuation layer/line: a receipt increases quantity and (depending on costing method) may change unit value; an outbound movement decreases quantity at whatever unit value the costing method assigns to the release. No version's documentation describes a case where Total Value can be edited independently of a Quantity x Unit Value line without going through a labeled revaluation mechanism (§9).

Fact Status: `VERIFIED` (13.0, 18.0). `PROVISIONAL` for exact column set in 19.0 pending direct page re-fetch.

### 2.3 Cost-method effect on the report

| Costing method | Effect on Unit Value shown in the report | Fact Status | Evidence |
|---|---|---|---|
| Standard Price | Unit Value is the manually defined standard cost on the product record; it does not move with actual purchase price. A change to the standard cost field generates its own record in the valuation report (a revaluation line), separate from ordinary receipt/issue lines. | VERIFIED | Reference ERP official documentation — Using inventory valuation, version 18.0, retrieved 2026-09-02 |
| Average Cost (AVCO) | Unit Value is a running weighted average = total inventory value / total quantity on hand; it recalculates on each qualifying inbound movement and, per the documentation, explicitly **does not** change on outbound movements. | VERIFIED | Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02 (avg-price section) |
| FIFO | Unit Value on outbound movements is drawn from the oldest still-open inbound cost layer(s) until exhausted, then the next-oldest layer; inbound movements are valued at the actual received cost. | VERIFIED | Reference ERP official documentation — Automatic inventory valuation, version 18.0, retrieved 2026-09-02 |

Costing method is set at product-category level (Menu B territory) and is a report **input**, not a report control — the report does not offer an independent costing override; it reflects whatever method the category (or product override) resolves to. This dependency is why Menu E cannot be evidenced in isolation from Menu B/C; this file treats that boundary as already owned by files `04`/`05` and does not re-litigate it.

### 2.4 Value-movement categories (opening / inbound / outbound / adjustment / landed / manufacturing / closing)

| Movement category | How it appears on the report (Layer A) | Fact Status | Evidence |
|---|---|---|---|
| Opening | No dedicated "opening balance" line type is documented; opening value is simply whatever quantity/value existed as of the earliest date in scope when the as-of-date filter (§5) is applied. Migration/cutover opening balances are governed separately (file `26` scope, `JT-11`/`G-5`), not by a report feature. | PROVISIONAL — report-level "opening" is inferred from as-of-date behavior, not a named report row/section in any fetched page | Reference ERP official documentation — Using inventory valuation, version 18.0, retrieved 2026-09-02 |
| Inbound (receipt) | A line per qualifying stock move, valued per the costing method (§2.3), with a Reference pointing to the receiving operation. | VERIFIED | Reference ERP official documentation — Using inventory valuation, version 18.0, retrieved 2026-09-02 |
| Outbound (delivery/issue) | Symmetric line, negative quantity/value effect, Reference to the outgoing operation. | VERIFIED | same as above |
| Adjustment | A manual "Product Revaluation" action, reachable after grouping the dashboard by product, lets a user increase or decrease unit price with a documented reason; this generates its own valuation line distinct from a transactional receipt/issue line. | VERIFIED | Reference ERP official documentation — Using inventory valuation, version 18.0, retrieved 2026-09-02 |
| Landed cost | Documented as capable of being added to a purchase and affecting the product's unit cost; the report reflects the resulting unit-value change, but the precise line-item mechanics (whether landed cost posts as its own report line or is absorbed into the receipt line it is allocated to) were not resolved to VERIFIED depth this session. | PROVISIONAL / HOLD on line-level mechanics | Reference ERP official documentation — Using inventory valuation, version 18.0, retrieved 2026-09-02 |
| Manufacturing | Documented as impacting valuation "when materials are consumed and finished goods are produced"; a dedicated "Cost of Production" account exists at the Accounting-settings level (Menu F territory, §7 of file `08`) that bridges the valuation account with production expense. The report-level line mechanics for WIP vs finished-goods valuation were not independently confirmed this session. | PROVISIONAL / HOLD | Reference ERP official documentation — Using inventory valuation, version 18.0, retrieved 2026-09-02; Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02 |
| Closing | Under the Periodic model, the report is the documented **basis** for the closing journal entry (file `08`, §Stock Closing Entry) — the report does not itself post the closing entry; it is read by the accountant (or a scheduled/triggered action) to determine what the closing entry should be. Under Perpetual, there is no separate "closing" value-movement category on the report; ordinary transactional lines already carry the running valuation. | VERIFIED (Periodic role) / VERIFIED (Perpetual — no separate closing category) | Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02 |

### 2.5 As-of-date behavior

A control described as **"Inventory At Date"** (13.0/14.0 wording) and **"Valuation At Date"** (18.0 wording — a further terminology delta, `VERSION DELTA — CONFIRMED (label)`) opens a dialog that reconstructs, for any past date selected, the same quantity/unit-value/total-value picture as of that date, by replaying stock moves and on-hand stock up to that date. This is documented across 13.0 and 18.0 consistently in function even though the exact button label differs.

Fact Status: `VERIFIED` (function); `VERIFIED` (label differs by version — see table above).

### 2.6 Drill-down / provenance to source documents

The **Reference** column carries the originating warehouse-operation identifier. An arrow/icon control on that column opens the underlying stock-move detail (quantity, on-hand stock, and the move itself), which is the documented drill-down path from a valuation line back to its originating transaction. No version's documentation describes a drill-down that reaches further upstream than the stock move (e.g., directly into the vendor bill or customer invoice line) from the valuation report itself; that link, where it exists, runs through the accounting journal entry (§2.7), not through this report.

Fact Status: `VERIFIED` (move-level drill-down). `HOLD` (whether any version links the report row directly to the source vendor bill/customer invoice line without an intermediate step) — not resolved this session.

### 2.7 Reconciliation to Accounting

Under Automated/Perpetual valuation, each qualifying valuation layer generates a corresponding journal entry in the Accounting app, posted to the Valuation (Stock) account and, depending on transaction type, an interim Stock Input/Output or COGS/Variation account (file `06`/`08` account-type detail). The documentation states that viewing this linkage requires **access rights on the accounting module** — i.e., the reconciliation view is access-gated separately from ordinary inventory-report access, which is a control-relevant fact for the SMEsPlus role model (Layer C candidate flag in §10).

The reconciliation identity implied (not stated as a single formula in any one fetched page, so classified `CANDIDATE`, not `VERIFIED`, at the identity level) is:

`Inventory Valuation report closing Total Value (as of a date) <-> Accounting Valuation (Stock) account balance (as of the same date) + any explained reconciling items (in-transit landed cost not yet allocated, timing differences under Perpetual for received-not-billed / delivered-not-invoiced captured in the Variation account, manual revaluations not yet posted)`

Fact Status: `CANDIDATE` (identity) / `VERIFIED` (that a journal-entry-level linkage and an access-rights gate exist).

### 2.8 Difference / variance reporting

The report documentation names a **"Stock Variation"** section/grouping that surfaces the gap between what the report's transactional lines say inventory is worth and what has actually been posted to Accounting for received-not-billed and delivered-not-invoiced timing gaps under Perpetual valuation. Under Periodic valuation, the analogous gap is not a report feature at all — it is closed manually at the closing-entry step (file `08`). No named "variance report" separate from this Stock Variation grouping and the closing-entry mechanism was found in Layer A evidence this session.

Fact Status: `VERIFIED` (Stock Variation grouping exists and is named) / `HOLD` (whether it is a distinct sub-report vs. a filter/group-by view of the same dashboard — not resolved to line-level certainty this session).

### 2.9 Negative / zero-cost exceptions

This is the most concrete Layer A finding in this file. When stock is shipped without sufficient valued quantity on hand (a negative-inventory condition), the documentation describes the reference ERP creating a **valuation-layer compensation mechanism**: the outbound movement is valued at an estimated price (because no real cost layer exists yet to draw from), and the system explicitly labels the resulting entry as a **revaluation of the negative-inventory outbound movement**. When a later receipt arrives, the reference ERP uses that receipt's real cost to "compensate" the earlier estimated-price layer:

- If the later real price equals the earlier estimate, no new layer is created; the original layer is simply marked compensated.
- If the later real price differs, a compensating valuation line is created to true up the estimate to the real cost.

This is documented specifically under the Average Cost (AVCO) method; FIFO and Standard Price behavior under negative inventory was not independently confirmed to the same depth this session (`HOLD`). A zero-cost exception (e.g., a product with no cost basis at all — Standard Price never set, or a first-ever FIFO issue with no prior receipt) was not directly documented in any fetched page; this is recorded as `HOLD / EVIDENCE REQUIRED`, not assumed to behave the same as the negative-inventory case.

Fact Status: `VERIFIED` (negative-inventory AVCO compensation mechanism) / `HOLD` (FIFO/Standard negative-cost behavior; true zero-cost-basis behavior).

---

## 3. Field Evidence Sheet (governing-prompt §7 format)

| Field | Menu Path | Field Label | Purpose | Values/Options | Default | Visibility | Scope | Inherits From | Override Precedence | Transaction Consumer | Periodic Behavior | Perpetual Behavior | Account Type Impact | Financial Statement Impact | Change Impact | Version Delta | Evidence | Fact Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Date | Inventory -> Reporting -> Valuation | `Date` | Timestamp of the valuation-layer event | Any date | Move/event date | Always | Company | N/A | N/A | Every receipt/issue/adjustment/revaluation | Same column, but under Periodic most lines pre-close carry no accounting posting yet | Same column, and each line is expected to have a matching journal entry | N/A (report field) | None directly; underlies BS/P&L via the linked journal entry | N/A | Present 13.0–18.0 consistently; 19.0 not independently re-confirmed | Reference ERP official documentation — Using inventory valuation, v18.0, retrieved 2026-09-02 | VERIFIED |
| Quantity | same | `Quantity` | Units on hand / moved | Numeric, signed by direction | 0 | Always | Company/product | N/A | N/A | Every stock move | Physical tracking continues even though financial posting waits for closing | Physical and financial move together | N/A | None directly | N/A | Stable across versions | same | VERIFIED |
| Unit Value | same | `Unit Value` | Per-unit cost per the resolved costing method | Numeric currency | Costing-method dependent | Always | Product/category-resolved | Product Category costing method (Menu B) | Product-level cost override where the reference ERP supports one (Menu C boundary, not re-litigated here) | Every valued line | Same computation; only the posting timing differs | Same computation; posting is close to real time | N/A | None directly; drives Total Value | Changing costing method does not retroactively rewrite historical Unit Value lines per evidence found — `HOLD` on exact retroactivity rule | Terminology/label stable; underlying method options stable 13.0–19.0 | Reference ERP official documentation — Automatic inventory valuation, v18.0, retrieved 2026-09-02 | VERIFIED (existence) / HOLD (retroactivity) |
| Total Value | same | `Total Value` | Quantity x Unit Value | Numeric currency | 0 | Always | Company/product | Derived | N/A | Every valued line | Aggregates to the closing-entry basis | Aggregates to the running Valuation account balance | Asset (via Valuation account) | Balance Sheet | N/A | Stable | same | VERIFIED |
| Reference | same | `Reference` | Points to the originating operation for drill-down | Operation identifier | N/A | Always | Company | N/A | N/A | Every valued line | Same | Same | N/A | None directly | N/A | Stable | Reference ERP official documentation — Using inventory valuation, v18.0/v13.0, retrieved 2026-09-02 | VERIFIED |
| Valuation At Date / Inventory At Date | same (dashboard toolbar) | `Valuation At Date` (18.0) / `Inventory At Date` (13.0/14.0) | Reconstruct the report as of a past date | Date picker | Today | Always | Company | N/A | N/A | Read-only reconstruction, no posting | Same | Same | N/A | Supports BS/P&L cutoff analysis | N/A | Label changed between early (13.0/14.0) and later (18.0) versions; exact version of the label change not pinpointed this session | Reference ERP official documentation — Using the inventory valuation, v13.0; Using inventory valuation, v18.0, retrieved 2026-09-02 | VERIFIED (function) / PROVISIONAL (exact version of label change) |
| Product Revaluation (manual adjustment) | same, grouped by product | `Revaluation` action | Manually correct unit price with a documented reason | Increase/decrease + reason | N/A | Conditional — requires grouping by product first | Product | N/A | N/A | Adjustment event only | Generates a closing-relevant delta the accountant must reconcile at close | Generates an immediate valuation-layer and (if Automated) a journal entry | Asset adjustment; contra typically an expense/adjustment account (exact account not confirmed this session — `HOLD`) | Balance Sheet + P&L (via contra account) | Future-only; no evidence of retroactive rewrite | Present at least from 18.0 evidence; earlier-version presence/wording not independently confirmed | Reference ERP official documentation — Using inventory valuation, v18.0, retrieved 2026-09-02 | VERIFIED (18.0) / HOLD (contra account identity; earlier-version presence) |
| Stock Variation (grouping/section) | Report grouping; also named in the Accounting-side closing documentation | `Stock Variation` | Surfaces received-not-billed / delivered-not-invoiced and Periodic-close timing gaps | N/A | N/A | Conditional on valuation model | Company | N/A | N/A | Close / reconciliation event | Central to the Periodic closing entry | Present as a smaller, ongoing true-up mechanism | Expense (Continental) or current-asset/expense (Anglo-Saxon Perpetual) — see file `08` | P&L or Balance Sheet depending on accounting standard | N/A | Terminology consistent 17.0–19.0 evidence; 13.0–16.0 not independently confirmed | Reference ERP official documentation — Inventory valuation, v19.0, retrieved 2026-09-02 | VERIFIED (17.0–19.0) / HOLD (13.0–16.0) |
| Negative-inventory revaluation (compensation entry) | Generated automatically, surfaces on the same dashboard | Entry labeled as a revaluation of the negative-inventory outbound movement | Correct an outbound line valued at an estimate because no real cost layer existed | Automatic | N/A | Conditional — only when negative stock occurs under AVCO | Product | N/A | N/A | The compensating receipt | Same mechanism; Periodic close would still need to true this up in the closing entry if unresolved by close date | Confirmed under Perpetual/AVCO | Asset (Valuation account) correction | Balance Sheet, and P&L to the extent COGS was already recognized at the estimated price | Retroactively corrects the earlier estimated line's effect once a real cost is known | Documented for 19.0; not independently confirmed for 13.0–18.0 | Reference ERP official documentation — Inventory valuation, v19.0, retrieved 2026-09-02 | VERIFIED (19.0, AVCO) / HOLD (other versions/methods) |

---

## 4. Layer B — Thai Accounting/Tax/Statutory Evidence

`N/A for this file — pointer only.` Thai statutory evidence on inventory measurement, lower-of-cost/NRV, and cut-off evidence requirements belongs to file `24` (`THAI_ACCOUNTING_TAX_STATUTORY_EVIDENCE_REGISTER`), which has not been produced in this session as of this file's writing (only files `00` and `01` exist in `RESEARCH_V1` at the time this file was authored). This file introduces no Thai statutory claim. Any apparent Thai-relevant implication drawn from Layer A above (e.g., cut-off, lower-of-cost-or-NRV) is `HOLD / EVIDENCE REQUIRED` until file `24` independently verifies it against authoritative Thai sources.

---

## 5. Layer C — SMEsPlus Clean-Room Candidate Semantics (CANDIDATE / HOLD only — never final)

These are neutral business-meaning candidates derived from §2–§3, not SMEsPlus design decisions:

1. `CANDIDATE` — An Inventory Valuation reporting surface should expose, at minimum, quantity, unit cost, extended value, and a source-document reference per valuation event, plus an as-of-date reconstruction capability. This mirrors the consistent 13.0–18.0 Layer A pattern. Subject to Inventory-side review (Stock Truth ownership) before adoption.
2. `CANDIDATE` — A "Stock Variation" or equivalent grouping that isolates received-not-billed / delivered-not-invoiced timing gaps is a reasonable reconciliation aid regardless of which valuation-timing model (`JT-03`) SMEsPlus ultimately adopts, because the gap exists structurally whenever physical and financial events are not simultaneous.
3. `HOLD` — Whether SMEsPlus should expose a manual "revaluation" adjustment action directly from a valuation report, versus routing all valuation corrections through a controlled Accounting-approved adjustment workflow, is undecided. The reference ERP's pattern (report-initiated revaluation) is evidence, not a requirement; Thai audit-trail and segregation-of-duties expectations (file `24`, 9-Veto Security/Privacy/Resilience track) must be checked first.
4. `HOLD` — Negative-inventory / zero-cost-basis exception handling is a material control gap in this session's evidence (confirmed only for one costing method, one version). No SMEsPlus candidate is proposed until FIFO and Standard-Price negative-cost behavior, and true zero-cost-basis behavior, are independently verified.
5. `HOLD` — Whether reconciliation-to-Accounting access should be a distinct permission from ordinary inventory-report viewing (as Layer A suggests it is in the reference ERP) is a candidate control point for the SMEsPlus role model, not yet adjudicated.

---

## 6. Reconciliation Identity Status (governing-prompt §14 cross-check)

| Identity | Status here | Note |
|---|---|---|
| `Inventory valuation as-of-date <-> Accounting inventory balance + explained reconciling items` | `CANDIDATE` | See §2.7. Not independently proven as a single documented formula; assembled from separate, individually-verified facts. |
| Quantity identity (`Opening + Inflows - Outflows +/- Adjustments = Closing`) | Not directly tested by report evidence in this file; owned by the Inventory-side quantity truth (file `10`/Inventory package), referenced not re-derived here | `N/A — out of this file's evidence scope` |

---

## 7. Contradictions / Evidence Gaps Found This Session

1. Terminology instability: the reference ERP's own documentation uses "Automated"/"Manual" at the product-category field level and "Perpetual"/"Periodic" at the Accounting-settings level, across overlapping version ranges, without a single page reconciling the two vocabularies. Treated as `CONFLICTING (terminology only, not behavior)` — the underlying behavior described is consistent; only the label pairing needs a live-UI confirmation pass before being used in any SMEsPlus field-mapping document.
2. Direct content fetch of the version 19.0 dedicated report page (`Using inventory valuation`, 19.0) returned no retrievable body text this session (empty page content from the fetch tool). All 19.0 report-level claims in this file are therefore inherited from the 18.0 page plus the 19.0 Accounting-side closing/cheat-sheet pages, and are marked `PROVISIONAL` where the distinction matters. A follow-up direct fetch or archived-snapshot fetch is recommended before this file is treated as version-19.0-complete.
3. Landed-cost and manufacturing line-level report mechanics (§2.4) are `PROVISIONAL/HOLD` — confirmed only at the conceptual "it affects unit value" level, not at the report-row mechanics level.

---

## 8. Checkpoint Status

`CP-03` (Menu A-H coverage) — Menu E portion: Layer A substantially populated with named gaps; Layer B pointer-only (file `24` not yet produced); Layer C candidate/HOLD only. Not a completion claim for CP-03 as a whole, which requires Menus A–D and G–H also closed.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
