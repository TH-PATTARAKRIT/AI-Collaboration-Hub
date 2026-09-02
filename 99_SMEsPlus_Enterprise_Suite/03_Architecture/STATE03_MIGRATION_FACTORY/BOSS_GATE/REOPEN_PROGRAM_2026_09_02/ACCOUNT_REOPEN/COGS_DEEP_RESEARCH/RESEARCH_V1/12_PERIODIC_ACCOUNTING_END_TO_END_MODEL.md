# 12 — Periodic Accounting End-to-End Model

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `EVIDENCE COMPLETE — PERIODIC LIFECYCLE (LAYER A) — LAYER B THAI HOLD — CP-05 SUPPORT`

---

## 1. Purpose and Scope

This file builds the full Periodic (Continental-heritage / "at closing") accounting lifecycle required by governing-prompt §8.1:

`Opening Inventory -> Purchases / Vendor Bills -> Physical Receipts -> Sales -> Deliveries -> Customer Invoices -> Physical Closing Stock -> Stock Closing Entry -> COGS / Stock Variation -> Financial Statements`

It answers, in order, the ten §8.1 research questions from Layer A (reference ERP observed documentation behavior) only. Layer B (Thai statutory) is marked `HOLD / EVIDENCE REQUIRED` throughout — Thai authoritative research is file `24`'s job, not this file's. Layer C (SMEsPlus candidate semantics) is stated only as non-binding candidate language, never as final account codes or journal structure, per the governing prompt's hard rule.

The reference ERP is used strictly as a learning/benchmark source (clean-room §3). No vendor/product name, ORM identifier, table name, or source-code token appears below; the system is referred to only as "the reference ERP."

---

## 2. Evidence Layer Discipline

| Layer | Content in this file |
|---|---|
| Layer A | Reference ERP official documentation, versions 13.0–19.0, describing Periodic ("at closing") valuation behavior. |
| Layer B | Thai statutory position on periodic/physical inventory systems, cost recognition timing, and cut-off. `HOLD / EVIDENCE REQUIRED` in every section below — routed to file `24`. |
| Layer C | SMEsPlus candidate business-meaning language only. No account code, no journal line, no posting rule is prescribed here. |

A material cross-version evidence tension was found during this pass (§8) and is flagged, not resolved, per the "no manufactured certainty" rule.

---

## 3. Terminology Note (Layer A)

Reference ERP documentation (version 19.0) states the valuation-method selector is now framed as "Periodic (at closing)" vs. "Perpetual (at invoicing)," replacing an older "Automatic" / "Manual" labelling pair used in earlier major versions, and that the older Continental/Anglo-Saxon accounting-standard labels are used interchangeably with Periodic/Perpetual in current documentation, with Continental describing an approach that "records the cost of goods as an expense when the vendor bill is posted... regardless of when the goods are sold," and Anglo-Saxon describing an approach that expenses "cost of goods sold... when the customer invoice is posted."
— *Reference ERP official documentation — Inventory Valuation / Valuation Cheat Sheet, version 19.0, retrieved 2026-09-02.* Fact Status: `VERIFIED` (direct quoted documentation text).

Candidate note (Layer C, non-binding): SMEsPlus should not silently equate "Periodic" with "Continental-standard COGS timing" — the reference ERP's own document treats the valuation-*update-cadence* axis (periodic vs perpetual posting) and the *expense-recognition-trigger* axis (vendor-bill-posting vs customer-invoice-posting) as related but analytically separate ideas that happen to correlate in its default configuration. SMEsPlus must decide both axes explicitly rather than inherit the correlation. `HOLD — JT-03 / JT-04.`

---

## 4. Stage-by-Stage Lifecycle (Layer A, Periodic)

### 4.1 Opening Inventory

**Reference Observation.** Opening inventory value is a starting balance-sheet figure; under Periodic valuation the reference ERP does not maintain a continuously-updated financial inventory balance between closings — the documented behavior is that "inventory valuation is updated only when generating entries during the stock closing process," while physical movements continue to be tracked in the warehouse-side stock report independently of the financial ledger.
— *Reference ERP official documentation — Inventory Valuation, version 19.0, retrieved 2026-09-02.* Fact Status: `VERIFIED`.

**Accounting Meaning.** Opening inventory is a certified prior-period closing balance carried forward as the current period's starting Inventory Asset figure. Under Periodic, that figure is not disturbed by transaction volume during the period — it moves only at the next close.

**Thai Rule Status.** `HOLD / EVIDENCE REQUIRED` — Thai requirements for opening-balance certification, physical count evidence, and consistency of opening figure with the prior period's closing tax filing are not independently verified in this file; routed to file `24`.

**SMEPLUS Candidate / Hold.** Candidate language only: an "opening inventory fact" concept, distinct from any transactional fact, certified at cutover and at each period roll-forward. No account code proposed. `HOLD — JT-11 / migration file 26.`

### 4.2 Purchases / Vendor Bills

**Reference Observation.** Under Periodic, a Vendor Bill posts an ordinary expense-by-nature entry (a purchase expense account is used) rather than directly capitalizing the amount into a perpetual Inventory Asset account at the moment of posting. The stock-value effect of purchases is not separately recognized transaction-by-transaction; it is folded into the period's aggregate purchase expense until the close.
— *Reference ERP official documentation — Inventory Valuation, version 19.0, retrieved 2026-09-02*, corroborated by *Reference ERP official documentation — Automatic Inventory Valuation, version 17.0/18.0 (title/description confirmed via documentation index), retrieved 2026-09-02.* Fact Status: `PROVISIONAL` — the higher-level statement (purchase cost hits an expense account, not a perpetual asset account, under Periodic) is well supported by the version-19.0 documentation text; the exact debit/credit account pairing was not independently confirmed against raw page markup in this pass and should not be treated as a verified journal structure.

**Accounting Meaning.** This is the "purchase cost first expensed" answer for Periodic: **the vendor bill is where cost first lands financially**, as an expense-by-nature charge, not as an asset capitalization event. Capitalization into the Inventory Asset balance, if any, is a period-end phenomenon (§4.7), not a per-bill phenomenon.

**Thai Rule Status.** `HOLD / EVIDENCE REQUIRED` — whether Thai practice/tax rules require purchase cost to be visibly routed through a "purchases" expense-by-nature account before period-end reclassification (a common periodic/physical-inventory pattern in many jurisdictions) is not yet independently verified against Thai authoritative sources. Routed to file `24`.

**SMEPLUS Candidate / Hold.** Candidate language only: a "purchase cost acquisition fact," carrying vendor, quantity, unit cost, currency, and reference, distinct from any later capitalization decision. `HOLD — JT-01 / JT-06.`

### 4.3 Physical Receipts

**Reference Observation.** Physical receipt into the warehouse is tracked as a quantity movement on the inventory side regardless of valuation method; under Periodic that movement does not, by itself, trigger a financial journal entry — the financial side stays silent until the vendor bill (which is expense-by-nature, §4.2) and, later, the close.
— *Reference ERP official documentation — Inventory Valuation, version 19.0, retrieved 2026-09-02.* Fact Status: `PROVISIONAL` — inferred from the documented "movements are tracked physically... but not automatically synchronized with financial records" statement; the absence of a receipt-level journal entry under Periodic was not confirmed by a dedicated receipt-posting-example page in this pass.

**Accounting Meaning.** Under Periodic, physical receipt is a **Stock Truth event only** at the moment it happens. It becomes financially relevant later, at close, when the physical count and the aggregate purchase expense are reconciled (§4.7–§4.9). This is consistent with the foundational rule that Inventory emits facts and Accounting decides postings — under Periodic, Accounting's posting decision for a receipt is deliberately deferred, not skipped.

**Thai Rule Status.** `HOLD / EVIDENCE REQUIRED`.

**SMEPLUS Candidate / Hold.** Candidate language only: a "receipt quantity fact," time-stamped, referencing the purchase order/vendor and location, held by Inventory and made available to Accounting for period-end reconciliation use — not posted individually under a Periodic policy. `HOLD.`

### 4.4 Sales

**Reference Observation.** Symmetrically to purchases, under Periodic a Customer Invoice posts revenue and (where used) a receivable; the reference ERP's documentation of the Periodic pattern does not describe a per-invoice COGS entry — cost recognition is deferred to the close, consistent with the "expense recognized when generating entries during the stock closing process" statement.
— *Reference ERP official documentation — Inventory Valuation, version 19.0, retrieved 2026-09-02.* Fact Status: `PROVISIONAL`.

**Accounting Meaning.** Revenue recognition (on invoice) and cost recognition (deferred to close) are **decoupled in time** under Periodic. This is a structurally different pattern from Perpetual, where the two are documented as being pulled closer together (file `13`).

**Thai Rule Status.** `HOLD / EVIDENCE REQUIRED` — Thai revenue-recognition timing rules for goods (point of delivery vs. point of invoice) are a Layer B question independent of costing-side timing; not resolved here.

**SMEPLUS Candidate / Hold.** `HOLD.`

### 4.5 Deliveries

**Reference Observation.** As with receipts, physical delivery out of the warehouse is a quantity movement tracked on the inventory side; under Periodic it does not, by itself, generate a financial entry. No per-delivery COGS posting is described for the Periodic pattern.
— *Reference ERP official documentation — Inventory Valuation, version 19.0, retrieved 2026-09-02.* Fact Status: `PROVISIONAL` (same basis as §4.3).

**Accounting Meaning.** Under Periodic, delivery is a **Stock Truth event only**, exactly like receipt. Neither event is individually an accounting trigger; both feed the period-end reconciliation instead.

**Thai Rule Status.** `HOLD / EVIDENCE REQUIRED`.

**SMEPLUS Candidate / Hold.** Candidate language only: a "delivery quantity fact," symmetrical to the receipt quantity fact. `HOLD.`

### 4.6 Customer Invoices

Covered jointly with §4.4 (Sales) above — the reference ERP documentation does not describe these as financially distinct events under Periodic in the material reviewed. Fact Status: `PROVISIONAL`.

### 4.7 Physical Closing Stock

**Reference Observation.** The Periodic pattern depends on a physical stock count (or a system-derived closing quantity/value) being established at period end; the documentation frames the Periodic/"at closing" method around a "stock closing process" during which entries are generated based on the physical inventory of the company, with "warehouse employees tak[ing] the time to count the stock."
— *Reference ERP official documentation — Inventory Valuation, version 19.0, retrieved 2026-09-02.* Fact Status: `VERIFIED` (direct quoted documentation description of the closing process's physical-count dependency).

**Accounting Meaning.** This is the direct answer to "how is closing inventory value determined": **under Periodic, closing inventory value is an input to the close, not an output continuously derived from transactions.** It is established by counting (or an equivalent closing valuation exercise) and then used to derive the period's expense.

**Thai Rule Status.** `HOLD / EVIDENCE REQUIRED` — Thai requirements for physical count evidence, count documentation retention, and count-to-book reconciliation tolerance are not independently verified here. Routed to file `24`.

**SMEPLUS Candidate / Hold.** Candidate language only: a "certified closing stock fact" (quantity and value, dated, with count-evidence reference) as a distinct fact type from ordinary transactional facts. `HOLD — JT-07.`

### 4.8 Stock Closing Entry

**Reference Observation.** Documentation identifies two accounts specific to the Periodic close: a **Valuation Account**, described as recording "the inventory value listed as a current asset on the balance sheet," and a **Variation Account**, described as tracking "inventory variations for the period covered by the stock closing process." The Periodic Valuation cadence itself is configurable as Manual, Daily, or Monthly. Version-19.0 material further describes a "guided closing interface" assisting the closing process and states that valuation data is stored differently (directly on stock-movement records rather than in separate valuation-layer records) than in prior major versions, removing a prior constraint against back-dating closing-relevant transfers.
— *Reference ERP official documentation — Inventory Valuation / Valuation Cheat Sheet, version 19.0, retrieved 2026-09-02*; version-19-specific architecture change corroborated by a secondary (non-official, community-sourced) technical summary, treated here as **secondary evidence only, not authoritative**: *secondary source — "New era of stock valuation" summary, non-official, retrieved 2026-09-02, used only to corroborate the direction of the version-19 change, not as a standalone fact source.* Fact Status: `VERIFIED` for the Valuation/Variation account role descriptions (direct documentation quotes); `PROVISIONAL` for the "guided closing interface" and back-dating claims (corroborated by secondary source only).

**Accounting Meaning.** This is the direct answer to "is there a stock variation calculation": **yes — the Variation Account is the documented mechanism by which the difference between what was expensed-by-nature during the period (§4.2) and what physical closing stock (§4.7) actually shows is captured and moved.** The close is where Stock Truth (physical count) and Financial Truth (accumulated purchase-expense-by-nature ledger) are reconciled into a single Inventory Asset figure and a single period expense figure.

**Thai Rule Status.** `HOLD / EVIDENCE REQUIRED` — Thai requirements for closing-entry timing, approval, and audit-trail retention are not independently verified. Routed to file `24`.

**SMEPLUS Candidate / Hold.** Candidate language only, no account code: a "closing valuation-adjustment fact," produced once per closing cycle, referencing the certified closing stock fact (§4.7) and the accumulated purchase-expense total for the period, with an explicit approver and cadence. `HOLD — JT-07.`

### 4.9 COGS / Stock Variation

**Reference Observation.** The documentation frames the Variation Account as the vehicle by which the period's net inventory movement is expressed financially at close — i.e., COGS under Periodic is not itself a per-transaction figure but a **derived period result**: the change in inventory value implied by (opening value + net purchase expense − closing value), with the Variation Account absorbing that movement.
— *Reference ERP official documentation — Valuation Cheat Sheet, version 19.0, retrieved 2026-09-02.* Fact Status: `PROVISIONAL` — the general "COGS is a derived period residual under Periodic" characterization is a reasonable and widely corroborated reading of the documented Variation Account role, but the reference ERP's documentation reviewed here does not use the literal words "COGS equals opening plus purchases minus closing" as a stated formula; this exact identity is challenged, not assumed, in file `27`.

**Accounting Meaning.** This is the direct answer to "how is COGS derived/presented" under Periodic: it is **presented as a period P&L residual**, computed at close, not as an accumulation of individually-tagged COGS journal lines per sale. This is the classic periodic-inventory-system pattern (opening + net purchases − closing = cost of goods sold), which the reference ERP's Variation Account mechanism operationalizes without necessarily labelling the resulting P&L line "COGS" verbatim in every configuration — some configurations may present it as a "cost of goods" or "inventory variation" line. This distinction between the *mechanism* (Variation Account movement) and the *label* (whatever the P&L caption is configured to say) matters for SMEsPlus and must not be collapsed.

**Thai Rule Status.** `HOLD / EVIDENCE REQUIRED` — whether Thai statutory P&L presentation requires a discrete "Cost of Sales"/"Cost of Goods Sold" line distinct from a generic "inventory variation" line is a Layer B question. Routed to file `24`.

**SMEPLUS Candidate / Hold.** Candidate language only: "COGS-equivalent period result" as a P&L-facing label distinct from the underlying "closing valuation-adjustment fact" (§4.8) that produces it. No account code, no journal structure prescribed. `HOLD — JT-04 (recognition-timing decision also needs to state whether Periodic's deferred/derived COGS timing is acceptable for any SMEsPlus configuration, or whether Perpetual is mandated instead).`

### 4.10 Financial Statements

**Reference Observation.** The Valuation Account is documented as feeding the Balance Sheet ("current asset"); the Variation Account is documented as the period-covering mechanism that, in effect, reaches the P&L. No further statement-level detail (e.g., specific P&L caption text) was independently confirmed in this pass.
— *Reference ERP official documentation — Valuation Cheat Sheet, version 19.0, retrieved 2026-09-02.* Fact Status: `VERIFIED` for the Balance Sheet/current-asset characterization; `HOLD` for P&L caption specifics.

**Accounting Meaning.** Under Periodic, the Balance Sheet Inventory Asset figure only changes at each close (§4.7–§4.8); intra-period, it is a stale/carried-forward number by design, not a real-time figure. The P&L cost-of-goods figure is a period result, not a transaction trail.

**Thai Rule Status.** `HOLD / EVIDENCE REQUIRED`.

**SMEPLUS Candidate / Hold.** `HOLD.`

---

## 5. Explicit Answers to the §8.1 Research Questions

| # | Question | Layer A Answer (Periodic) | Fact Status |
|---|---|---|---|
| 1 | When is purchase cost first expensed or capitalized? | First **expensed** (by nature) at vendor-bill posting (§4.2); **not** capitalized to a perpetual Inventory Asset account transaction-by-transaction. Any capitalization effect is realized only through the closing entry (§4.8), as a derived adjustment, not a per-bill entry. | `PROVISIONAL` |
| 2 | Is Inventory Asset updated transaction-by-transaction or at close? | At close only. Documentation is explicit: "inventory valuation is updated only when generating entries during the stock closing process." | `VERIFIED` |
| 3 | How is closing inventory value determined? | By a physical stock count (or equivalent closing valuation exercise) at period end — an **input** to the close, consistent with documented warehouse-count dependency. | `VERIFIED` |
| 4 | How is stock variation calculated? | Via the documented **Variation Account**, which absorbs the difference between the period's accumulated purchase-expense-by-nature total and the certified closing stock value. Exact formula wording not found verbatim in the material reviewed — treated as a corroborated pattern, not a confirmed literal documentation statement. | `PROVISIONAL` |
| 5 | How is COGS derived/presented? | As a **period residual** produced by the closing entry (opening value + period purchase expense − closing value, in substance), routed through the Variation Account mechanism; exact P&L caption not confirmed. | `PROVISIONAL` |
| 6 | Receipt exists with no bill — what happens? | Under Periodic, the receipt is a Stock-Truth-only quantity movement (§4.3); with no vendor bill posted, no purchase expense has been recognized for that unit at all until a bill eventually posts. The physical closing count (§4.7) will still include the received-but-unbilled quantity, meaning the closing count can show more stock than the accumulated purchase-expense ledger would suggest, absorbed at close via the Variation Account. **No dedicated "goods received, not invoiced" accrual account was confirmed as part of the Periodic pattern in the material reviewed** — that accrual/interim-account mechanism is documented for the Perpetual pattern (file `13`, file `17`), not confirmed for Periodic. `HOLD — this asymmetry (accrual account documented for Perpetual, not confirmed for Periodic) is itself a material open question for JT-06.` | `HOLD` |
| 7 | Bill exists with no receipt — what happens? | The vendor bill still posts its expense-by-nature entry (§4.2) regardless of physical receipt status, per the documented decoupling of the financial (bill-driven) and physical (receipt-driven) sides under Periodic. If the physical count at close does not reflect the goods (because they were never actually received), the closing entry's Variation Account will absorb that gap as part of the period's derived result — i.e., **the discrepancy is not separately flagged as an exception under Periodic; it is silently folded into the period variation figure** unless a separate control catches it. This is flagged as a control-risk observation, not a confirmed system behavior beyond the documented close mechanics. | `PROVISIONAL` |
| 8 | How are returns handled before/after closing? | Not independently confirmed for the Periodic pattern in the material reviewed in this pass. Return handling detail (cost-basis linkage) is documented primarily in Perpetual/Anglo-Saxon material reviewed for file `17`/`19`. Under Periodic, a return before closing should, by the same logic as §4.2/§4.3, simply reduce the period's accumulated purchase-expense or sales-revenue figures and be absorbed at the next close; a return after closing (i.e., against a prior, already-closed period) raises a prior-period-adjustment question not confirmed here. | `HOLD` |
| 9 | How are write-down, loss, scrap, adjustment distinguished from ordinary COGS? | Not confirmed for the Periodic pattern specifically in the material reviewed here. The reference ERP documentation for Perpetual describes dedicated location-scoped accounts (Inventory Loss Account, Cost of Production Account) distinct from ordinary COGS; whether an equivalent distinction is preserved (vs. collapsed into the single Variation Account) under Periodic is **not confirmed** and is a material open question — full treatment deferred to file `20`. | `HOLD` |
| 10 | How does close reconcile physical Stock Truth to Financial Truth? | The Stock Closing Entry (§4.8) is precisely the documented reconciliation mechanism: it takes the certified physical closing count/value (Stock Truth) and the accumulated financial purchase/sales-expense ledger (Financial Truth-so-far) and produces the Variation Account movement that makes the two consistent for the period. This reconciliation is periodic and batched by design — it is not a continuous reconciliation. | `VERIFIED` (mechanism existence); `PROVISIONAL` (full mechanics) |

---

## 6. Receipt-With-No-Bill / Bill-With-No-Receipt — Consolidated Finding

This deserves consolidation beyond the table row above because it is a recurring §10 scenario driver (scenarios 2, 3, 5) and a named Joint decision input (`JT-06`).

Under the Periodic pattern as documented:
- The **financial** side of the lifecycle is driven by the **vendor bill** (expense-by-nature) and the **customer invoice** (revenue), not by physical receipt/delivery events.
- The **physical** side is driven by receipt/delivery quantity movements, tracked independently.
- The two sides are **only reconciled at close**, via the physical count and the Variation Account.
- This means a receipt-with-no-bill and a bill-with-no-receipt are **not distinguished as separate exception types** by the Periodic mechanism itself — both simply flow into whatever the period's purchase-expense ledger and physical count happen to show, and the Variation Account absorbs whatever net difference results.
- **Material gap:** the documented Perpetual pattern uses named interim/accrual accounts (documented for that pattern; see file `17`) to make an un-invoiced receipt visible as a distinct balance. No equivalent named accrual account was confirmed for Periodic in the material reviewed in this pass. Whether the reference ERP's Periodic pattern has *any* dedicated visibility mechanism for "physically received, not yet billed" as a standing balance (versus only discovering the gap once per period at close) is `HOLD / EVIDENCE REQUIRED` and should be added to file `02`'s version-delta register and file `27`'s reconciliation-identity challenge.

---

## 7. Version Delta Directly Relevant to This File

| Version window | Observed state | Evidence | Fact Status |
|---|---|---|---|
| Documentation index confirms presence of an inventory-valuation-configuration page across versions 13.0 through 19.0 (URLs independently located for 13.0, 14.0, 15.0, 16.0/saas-16.4, 17.0, 18.0, 19.0). | Periodic/Perpetual (or the older Manual/Automatic naming) has been a documented, present concept across this entire version window; it is not a recently-introduced feature. | *Reference ERP official documentation index — search-result confirmation of page existence per version, retrieved 2026-09-02.* | `PROVISIONAL` — existence confirmed by indexed page titles; full field-level content of every one of the 13.0–18.0 pages was not individually fetched and diffed in this pass. Full cross-version diff is file `02`'s scope. |
| Pre-19.0 vs 19.0 | Terminology renamed from "Automatic"/"Manual" toward "Perpetual (at invoicing)"/"Periodic (at closing)." Version-19.0 material also describes a storage-architecture change (valuation data moved from separate valuation-layer records onto stock-movement records directly) and a new "guided closing interface." | *Reference ERP official documentation — Inventory Valuation, version 19.0, retrieved 2026-09-02* (terminology); secondary non-official technical summary (architecture-change corroboration only), retrieved 2026-09-02. | `VERIFIED` (terminology); `PROVISIONAL` (architecture-change detail, secondary-sourced). |
| Pre-19.0 vs 19.0 — Perpetual trigger (flagged tension, not resolved) | One search-derived summary states pre-19.0 Perpetual/Automatic valuation posts real-time entries "whenever stock enters or leaves" (i.e., triggered by the physical stock move). A separate search-derived summary states that "since [version] 19, the Perpetual method impacts the stock valuation account at the invoice level," implying version 19.0 shifted the Perpetual trigger toward invoice-posting rather than stock-move-posting. **These two characterizations describe different triggers for the same "Perpetual" label and were not reconciled against a single authoritative page in this pass.** | Both are search-engine-generated summaries of reference-ERP-domain content, not independently confirmed against a single fetched official page for each version. | `CONFLICTING — HOLD.` This is the single most material open item this file surfaces; see §9. |

---

## 8. Material Open Item — Perpetual Trigger Definition Instability Across Versions

Flagged here (and echoed in file `13` and file `02`) because it directly affects `JT-03` (continuous vs. periodic timing) and `JT-04` (COGS recognition event — dispatch vs. invoice):

If the reference ERP's own Perpetual/"real-time" valuation trigger changed across its major versions — from "stock movement" (receipt/delivery) to "invoice posting" — then **"Perpetual" is not a single stable reference pattern that SMEsPlus can benchmark against without pinning an exact version.** This is exactly the kind of "version drift must be proven, not assumed away" risk the governing prompt anticipates (§5, hard rules). It must not be silently resolved by picking whichever version's behavior is convenient; it requires a dedicated fetch-and-diff pass against the actual documentation pages for at least two bracketing versions (e.g., 17.0 and 19.0) before file `02` and file `13` can close this point. Recorded here as `HOLD / EVIDENCE REQUIRED — MATERIAL — VERSION DELTA UNRESOLVED.`

---

## 9. Reconciliation Identity — Preliminary Challenge (Periodic)

Per governing-prompt §14, the candidate identity `Opening Inventory + Net Purchases / Capitalizable Costs − Closing Inventory = COGS` is **directionally consistent** with the documented Periodic Variation Account mechanism (§4.8–§4.9) but is classified here as `CANDIDATE`, not `VERIFIED`, because:
- the exact treatment of received-but-unbilled and billed-but-unreceived quantities inside that formula is unconfirmed (§6);
- the exact treatment of returns, write-downs, scrap, and adjustments inside vs. outside that formula is unconfirmed (§5, rows 8–9);
- the reference ERP's own documentation was not found, in the material reviewed, to state the formula in those literal terms.

Full identity testing is file `27`'s scope; this file only supplies the Periodic-side evidence feeding that test.

---

## 10. Cross-Reference to Open Joint Decisions

| Joint ID | Relevance in this file |
|---|---|
| `JT-01` | Valuation-policy ownership — this file shows Periodic's mechanism depends on a category/company-level valuation-method setting, but does not itself resolve who owns that setting in SMEsPlus. `HOLD`. |
| `JT-02` | Costing-method interaction with Periodic timing is noted (§3, §5 row 4) but full costing-method-by-costing-method proof is file `15`'s scope. |
| `JT-03` | Directly fed by this entire file — Periodic is one full side of the continuous-vs-periodic decision. Not closed here. |
| `JT-04` | Directly fed by §4.9/§4.10 — under Periodic, COGS timing is "at close," structurally different from any per-invoice trigger. Not closed here. |
| `JT-06` | Directly fed by §6 — late-bill / receipt-without-bill behavior under Periodic is materially thinner evidence than under Perpetual; flagged `HOLD`. |
| `JT-07` | Directly fed by §4.7–§4.8 — period close design. This file supplies the Periodic close's documented shape (physical count input, Valuation/Variation accounts, configurable cadence) as a candidate input, not a decision. |

---

## 11. Material HOLD Summary (This File)

1. `HOLD` — Whether Periodic has any dedicated "received, not billed" or "billed, not received" accrual visibility mechanism, or only discovers the gap at close (§6). **Most material item for downstream Joint work.**
2. `HOLD` — Return handling before/after closing under Periodic specifically (§5 row 8).
3. `HOLD` — Distinction between ordinary COGS/variation and write-down/loss/scrap/adjustment under Periodic specifically (§5 row 9).
4. `HOLD` — Exact literal formula wording (or absence thereof) for COGS-as-residual in reference documentation (§9).
5. `HOLD / CONFLICTING` — Perpetual trigger definition stability across versions, which indirectly bears on how "Periodic" is defined by contrast (§8). **Single most material open item in this file — see §8.**
6. `HOLD` — All Layer B (Thai) rows throughout §4–§5; routed to file `24`.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
