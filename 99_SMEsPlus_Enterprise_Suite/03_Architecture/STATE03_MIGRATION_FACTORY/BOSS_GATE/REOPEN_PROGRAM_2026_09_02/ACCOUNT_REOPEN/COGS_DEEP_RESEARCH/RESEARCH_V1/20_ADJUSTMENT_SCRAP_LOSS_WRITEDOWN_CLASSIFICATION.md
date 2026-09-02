# 20 — Adjustment / Scrap / Loss / Write-Down Classification

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `EVIDENCE COLLECTION — CP-08 SCENARIOS 21, 22, 23, 24 — CENTRAL CLASSIFICATION QUESTION, MATERIAL HOLD ON SCENARIO 24`

---

## 1. Scope and the Central Question

Governing-prompt §2 states the rule this file exists to evidence: **"Not every reduction in Inventory Value is COGS."** This file addresses §10 scenarios 21 (inventory adjustment gain), 22 (inventory adjustment loss), 23 (scrap/damage/shrinkage), and 24 (NRV/write-down/impairment), and builds the decision table required by this session's task brief.

Same three-layer evidence discipline as file `19`: `Layer A` (reference ERP observed documentation, called "the reference ERP" throughout), `Layer B` (Thai statutory evidence — this file flags relevance but does not carry primary Thai research; that is file `24`'s track), `Layer C` (SMEsPlus candidate semantics, downstream only). Citations: `Reference ERP official documentation — <topic>, version <N>, retrieved 2026-09-02`.

No journal entry, account code, or cost figure proposed for SMEsPlus in this file. Where evidence is thin, this file states `HOLD / EVIDENCE REQUIRED`, per governing-prompt §22.

---

## 2. Master Decision Table

| Event | Is it COGS? | Is it a separate loss/adjustment classification? | Is it neither? | Why (evidence-backed) |
|---|---|---|---|---|
| Sale delivered/invoiced to a customer (baseline, for contrast only) | **Yes** | No | No | This is the canonical cost-release event; inventory value is released against revenue recognition. Not this file's primary scenario, included only as the classification anchor. |
| Inventory adjustment — counted quantity **higher** than on-hand (gain) | **No** | **Yes — a distinct valuation adjustment, not COGS** | No | The reference ERP's documented Inventory Adjustments mechanism (On Hand Quantity / Counted Quantity / Difference / Accounting Date) reconciles the database to a physical count; it is not a sale, has no revenue counterpart, and the documented automated-valuation account pairing for a quantity increase runs through the stock input/valuation side, not through the delivery/output side that feeds cost-of-goods accounts. See §3. |
| Inventory adjustment — counted quantity **lower** than on-hand (loss) | **No (not automatically)** | **Yes — a distinct loss/adjustment classification, unless the business elects to route it through an Inventory Loss location with a Loss Account that lands in the P&L expense section, which is still documented as a distinct "loss" line, not a COGS line** | No | Same mechanism as the gain case, mirrored. The reference ERP's documented account pairing for a quantity decrease runs through the stock output/valuation side to whatever account is configured on the loss/adjustment location — documented as a "Loss Account," a P&L expense concept, but a different concept from Cost of Goods Sold. See §4. |
| Scrap (declared damaged/defective, moved to a scrap operation) | **No** | **Yes — explicitly documented as a distinct "Inventory Loss" classification with its own Loss Account, separate from Cost of Goods Sold** | No | The reference ERP's official documentation is explicit: scrapped goods reach the Profit & Loss report only through a dedicated Inventory Loss location type with an assigned Loss Account, reported as its own line under Expenses, not blended into the Cost of Goods Sold figure. See §5. |
| Shrinkage discovered only at physical count (no scrap document created) | **No** | **Yes, folded into the Inventory Adjustment (loss) classification of this table, unless and until a scrap document is separately created** | No | The reference ERP has no separate documented "shrinkage" concept distinct from Inventory Adjustment; undocumented/uninvestigated shrinkage is, on the evidence, mechanically indistinguishable from any other counted-quantity loss until a business process (e.g., a scrap declaration) reclassifies it. See §4/§5. |
| NRV write-down / impairment (value held, quantity unchanged, unit cost reduced to reflect lower recoverable value) | **No** | **UNKNOWN / NOT PRESENT IN THIS VERSION as a named, dedicated feature** | **Possibly — falls outside any feature this file could locate** | No official documentation page reviewed in this session names, defines, or walks through an NRV/write-down/impairment workflow as a labeled feature. The closest located mechanism (a manual "Product Revaluation" action that changes a unit cost) is a generic valuation-correction tool, not a policy-driven lower-of-cost-or-NRV feature. See §6. This is independently a live Thai/IAS-2-family requirement regardless of reference-ERP feature presence — flagged, not resolved, per §7. |
| Manufacturing raw-material consumption into WIP (for classification contrast only) | **No** | **Yes — a distinct WIP/production cost concept, not COGS at the consumption moment** | No | Out of this file's assigned scope (file `22` owns this); listed only to keep the decision table internally consistent with governing-prompt §2's list of non-COGS reductions. Not independently evidenced in this file. |
| Inter-company/warehouse transfer (for classification contrast only) | **No** | **Yes/No depending on policy — a location or ownership movement, not a cost-release event** | Possibly | Out of this file's assigned scope (file `25` owns this); listed only for decision-table completeness. Not independently evidenced in this file. |

**Reading the table**: every non-sale inventory-value decrease this file evidenced (adjustment loss, scrap, shrinkage) is documented by the reference ERP as landing in a **P&L expense classification that is structurally distinct from Cost of Goods Sold** — a different account, a different location-type concept, and in the scrap case an explicitly different reporting line. The reference ERP does not use one generic "inventory expense" bucket for both cost of sales and loss/adjustment; it keeps them apart by design. That design choice is Layer A evidence, not an SMEsPlus decision — SMEsPlus must independently decide (Joint session, not this file) whether to preserve, tighten, or diverge from that separation, and must do so under Thai evidence (file `24`), not by copying the reference behavior.

---

## 3. Archetype — Inventory Adjustment Gain (Scenario 21)

### REFERENCE OBSERVATION
The Inventory Adjustments screen (Inventory → Operations → Inventory Adjustments) presents each product/location line with an "On Hand" quantity (system-recorded) and a "Counted" quantity (entered by the user, blank by default), with "Difference" computed automatically. An "Accounting Date" field controls which accounting period the resulting entry lands in. Clicking "Apply" (or "Apply All") commits the count; a reference/reason can be recorded. Where Counted exceeds On Hand, the difference is a positive adjustment. Under automated/perpetual valuation, this is documented as generating a journal entry; the accounting-formula documentation (valuation cheat sheet) identifies the accounts involved in adjustments generically as the product category's Stock Account paired with a Stock Variation concept, plus an optional, recommended-for-Anglo-Saxon-accounting "Inventory Adjustment" account tied to the Inventory Loss location.

### ACCOUNTING MEANING
A quantity gain increases the recorded inventory asset with no corresponding revenue or vendor payable — it is a correction of the books to match a verified physical reality, not a transaction with an external party. Recognizing it as anything other than a valuation adjustment (e.g., as negative COGS) would misstate gross margin for a period in which no sale occurred.

### THAI RULE STATUS
HOLD — see file `24`. The Thai statutory/audit expectation for documented physical-count evidence supporting a positive adjustment (count sheets, approval signatures, reconciliation to a stock card) is a Thai audit-practice question this file has no authority to confirm.

### SMEPLUS CANDIDATE / HOLD
`CANDIDATE`: SMEsPlus should classify a counted-quantity gain as a distinct "Inventory Adjustment — Gain" fact, never as negative COGS, and require it to carry a reference/reason and an accounting-date field consistent with the reference ERP's own documented shape (not copied as design, evidenced as a pattern worth testing against Thai requirement in a Joint session). Precise account classification is explicitly out of scope for this research session.

---

## 4. Archetype — Inventory Adjustment Loss (Scenario 22)

### REFERENCE OBSERVATION
Mechanically identical to §3, mirrored: Counted below On Hand produces a negative Difference. The documented account pairing for the value decrease flows the opposite direction from a gain — out of the Stock Valuation account — with the offsetting side landing on whichever account is configured. The scrap-accounting documentation (§5) describes a specific, named "Inventory Loss" location type with a Loss Account as the mechanism to make such reductions visible in the Profit and Loss report under Expenses; the general Inventory Adjustments documentation reviewed in this file does not itself force use of that location type — a plain adjustment can in principle be posted without routing through a named loss location, depending on configuration, though this file did not locate an explicit statement of what the default offset account is when no Inventory Loss location is configured.

### ACCOUNTING MEANING
A quantity loss reduces the inventory asset with no sale and no revenue counterpart. Whether it is visible as its own labeled expense line (via a configured Loss Account) or falls into a less specific account is a configuration outcome, not a change in its underlying nature: it remains a loss/adjustment, never a cost of goods actually sold to a customer.

### THAI RULE STATUS
HOLD — see file `24`. This is the scenario explicitly flagged by governing-prompt §13 as touching "abnormal loss / scrap / destroyed inventory treatment" — Thai Revenue Department practice on deductibility of inventory losses (documentation requirements, destruction witnessing, write-off approval) is a live statutory concern this file surfaces but does not resolve. Treated as `HOLD`, not silently passed over.

### SMEPLUS CANDIDATE / HOLD
`CANDIDATE` for the classification shape (loss is not COGS); `HOLD` for deductibility/documentation treatment (Thai-side). SMEsPlus should require every counted-quantity loss fact to carry enough evidence (reference, reason, accounting date, approver where material) to support a later Thai-deductibility determination, without this file prejudging what that determination is.

### Gap Explicitly Flagged
`HOLD / EVIDENCE REQUIRED`: this file did not locate an official documentation statement of the default account used for an inventory-adjustment loss when no Inventory Loss location/Loss Account is explicitly configured. This is a materially relevant configuration-default gap and should not be assumed to default to a Cost of Goods Sold account without further evidence.

---

## 5. Archetype — Scrap / Damage / Shrinkage (Scenario 23)

### REFERENCE OBSERVATION
The reference ERP documents scrap as a distinct operation from a plain inventory adjustment, reachable from a receipt, a delivery order, or an internal transfer, or as a standalone scrap operation. To make scrapped value appear in the Profit and Loss report, the documented configuration path is: (1) enable Storage Locations in Inventory settings; (2) on the relevant Product Category, set a Costing Method (FIFO or AVCO) and Inventory Valuation = "Perpetual (at invoicing)" (terminology as observed in the 19.0-line documentation for this setting; see file `02`/`03` version-delta register for the exact label across versions) so real-time entries are generated; (3) create or edit a Location with Location Type = "Inventory Loss" and assign a Loss Account (the documentation's own worked example names an account "600001 Scrapped Goods" as illustration only — not an SMEsPlus candidate code); (4) scrap the product to that location. The resulting entry is documented as visible in Accounting → Reporting → Profit and Loss, under the Expense category, as its own line distinct from Cost of Goods Sold, viewable via a General Ledger drill-down.

### ACCOUNTING MEANING
This is the clearest, most explicit evidence in this file's scope that the reference ERP structurally separates "cost released because a sale happened" from "cost released because inventory was destroyed/damaged/scrapped." The mechanism is not just an account-naming convention — it is a distinct location-type concept (Inventory Loss) with its own reporting line, requiring deliberate configuration (a business must set it up; it is not automatic without configuration). Where a business does not configure a distinct Inventory Loss location, this file's evidence does not establish what happens to the scrapped value's classification by default — see the gap flagged below.

### THAI RULE STATUS
HOLD — see file `24`. Directly relevant to governing-prompt §13's "abnormal loss / scrap / destroyed inventory treatment" investigation point. Thai deductibility of scrapped/destroyed inventory typically has documentary and procedural preconditions (this file does not have authoritative Thai evidence to state what they are); flagged as a required Layer B input before any SMEsPlus scrap-classification candidate can move past `CANDIDATE` status.

### SMEPLUS CANDIDATE / HOLD
`CANDIDATE`: SMEsPlus should preserve the structural separation observed here — scrap is its own fact type, distinct from both a sale-driven cost release and a generic counted-quantity adjustment, carrying enough reference/reason/evidence to support a Thai deductibility review. This candidate does not extend to copying the reference ERP's configuration mechanics (location types, specific account codes) — those are implementation details explicitly out of scope for this research session (governing-prompt §12: "do not prescribe final SMEsPlus account codes or journal structure").

### Gap Explicitly Flagged
`HOLD / EVIDENCE REQUIRED`: the reference ERP's documentation is written as an opt-in configuration recipe ("if scrapped products need to be recorded in the Profit and Loss accounting report..."), which implies that without this configuration, scrap value may not surface distinctly in the P&L at all, or may fall back to some other account. This file did not locate a documented statement of that fallback behavior. This is material: it means "scrap is automatically not-COGS" is **not** a safe unconditional reading of the reference ERP — it is conditional on configuration the business must deliberately set up.

---

## 6. Archetype — NRV / Write-Down / Impairment (Scenario 24)

### REFERENCE OBSERVATION
`NOT PRESENT IN THIS VERSION` (as a named, dedicated, documented feature), evidenced as follows:

- No official documentation page located in this session's search (across the 13.0–19.0 version range and the dedicated inventory-valuation, scrap, and adjustment documentation trees) uses the terms "net realizable value," "write-down," or "impairment" as a labeled inventory feature.
- The one located mechanism with any resemblance is a documented "Product Revaluation" action, described as recalculating a product's inventory valuation "by increasing or decreasing the unit price of each product." This is a generic manual cost-correction tool (adjusts a unit cost figure directly), not a policy-driven lower-of-cost-or-market/NRV comparison, not tied to any documented obsolescence/damage/market-decline trigger, and not documented as distinguishing a "write-down" from any other cost correction (e.g., correcting a data-entry error would use the same mechanism).
- Third-party commentary located during this session's search (a vendor-marketing blog post, not official documentation) asserted that the reference ERP's costing-method flexibility "supports" IAS 2 lower-of-cost-and-NRV compliance. This claim is **not corroborated by any official documentation page** reviewed in this session and is explicitly **not treated as evidence** here, consistent with governing-prompt §13's instruction not to treat commentary as authority. It is recorded only to show it was found and discounted, not relied upon.

`Fact Status: HOLD / EVIDENCE REQUIRED` on feature presence, with reasonably high confidence (multiple targeted searches across the relevant documentation trees, no hits) that no dedicated feature exists as of the versions reviewed — but this file cannot certify a negative with full certainty across every documentation page in every version 13.0–19.0, and does not claim to.

### ACCOUNTING MEANING
If confirmed absent, this means: any lower-of-cost-or-NRV write-down performed by a reference-ERP-based business today is necessarily performed **outside** the costing-method/valuation-account mechanism this file has otherwise evidenced — most plausibly via the generic Product Revaluation (manual unit-cost) action, or via a manual journal entry outside the inventory module entirely, neither of which carries a documented, purpose-built audit trail for "this was a write-down, triggered by this NRV assessment, on this date, approved by this person." That audit-trail gap is itself a material accounting-control finding, independent of whether SMEsPlus ultimately needs the feature.

### THAI RULE STATUS
HOLD — see file `24`, but flagged here with elevated priority per this file's task brief: **lower-of-cost-and-net-realizable-value measurement is a real IAS-2-family and Thai Financial Reporting Standard requirement, and this file's evidence indicates it is independent of whatever the reference ERP's UI does or does not provide.** In other words, the absence of a reference-ERP feature does not remove or reduce the Thai/IFRS-for-SME-family requirement — it only means SMEsPlus cannot learn how to implement NRV write-down by studying the reference ERP's UI, and must instead derive it primarily from Thai/IAS-2-family authoritative evidence (file `24`'s track) with no reference-ERP UI pattern to lean on.

### SMEPLUS CANDIDATE / HOLD
`HOLD`. This file explicitly declines to propose any SMEsPlus NRV/write-down mechanism, consistent with governing-prompt §9's instruction to research "whether the reference ERP has any documented NRV/write-down feature at all" and, having found none, to say so rather than invent one. The only candidate this file will assert is a classification-boundary candidate, not a mechanism candidate: **if and when an NRV write-down is performed, its value decrease should be classified the same way scrap and adjustment losses are classified in this file's decision table — a distinct, non-COGS, P&L-visible loss/adjustment category — not blended into Cost of Goods Sold.** This is asserted on the strength of §2–§5's consistent evidence pattern (every other non-sale inventory decrease this file evidenced is kept structurally separate from COGS), extended by analogy to write-down, not on any direct reference-ERP write-down evidence (since none exists to cite).

---

## 7. Why Scenario 24 Cannot Be Silently Skipped

Per this file's task brief and governing-prompt §13, the correct handling of an absent reference-ERP feature is not to drop the scenario but to make the absence itself a recorded, evidenced fact and to flag the independent statutory requirement:

- `Reference-ERP feature presence`: `NOT PRESENT IN THIS VERSION` (§6).
- `Statutory/accounting requirement independent of the reference ERP`: real and unresolved — routed to file `24` as a named, high-priority HOLD item, not merged into this file's Layer C candidates as if it were a UI question. This file explicitly is **not** the place NRV/write-down gets resolved; it is the place its absence from Layer A evidence gets proven and its Layer B urgency gets flagged.
- `Downstream risk if ignored`: if SMEsPlus later needs NRV write-down (very likely, given Thai/IAS-2-family exposure) and no reference-ERP pattern exists to study, the SMEsPlus design work here is **original design work, not adaptation work** — this has schedule and review-depth implications for whichever team eventually owns this (flagged for file `34`, Next Controlled Action and Owner Matrix, not decided here).

---

## 8. Version Delta Register (Adjustment/Scrap/Write-Down Scope)

| Observation | Version(s) | Delta | Evidence |
|---|---|---|---|
| Inventory Adjustments field set (On Hand / Counted / Difference / Accounting Date) | 15.3 through 19.0 pages reviewed | No material delta observed in field shape across this range | `Reference ERP official documentation — Inventory adjustments, versions 16.0–19.0, retrieved 2026-09-02` |
| Scrap-to-P&L configuration recipe (Storage Locations → Product Category costing/valuation → Inventory Loss location + Loss Account) | 13.0 through 19.0 pages reviewed | No material delta observed in the overall recipe shape; exact valuation-mode label observed as "Perpetual (at invoicing)" in the 19.0-line page reviewed — whether this exact label existed identically in earlier versions was not independently re-verified page-by-page in this file and is `PROVISIONAL` | `Reference ERP official documentation — Scrap Products / Scrap inventory / Account for scrapped goods, versions 13.0, 15.0, 18.0, 19.0, retrieved 2026-09-02` |
| NRV/write-down as a named feature | 13.0 through 19.0 (searched) | No delta — consistently absent across every version searched, to the extent this file's search reached | Absence evidence per §6; not a positive citation |

---

## 9. Fact Status Summary

| Archetype | Fact Status |
|---|---|
| Master decision table (§2) | CANDIDATE, built from VERIFIED mechanism evidence per archetype below; Thai-side confirmation HOLD throughout |
| Inventory adjustment gain (§3) | VERIFIED (mechanism) / CANDIDATE (SMEsPlus classification) |
| Inventory adjustment loss (§4) | VERIFIED (mechanism) / CANDIDATE (classification) / HOLD (default-account gap, Thai deductibility) |
| Scrap/damage/shrinkage (§5) | VERIFIED (mechanism, opt-in configuration) / CANDIDATE (classification) / HOLD (fallback-without-configuration gap, Thai deductibility) |
| NRV/write-down/impairment (§6) | `NOT PRESENT IN THIS VERSION` (feature) — HOLD (statutory requirement, routed to file 24) |

---

## 10. What This File Does Not Do

This file does not resolve Thai deductibility of any loss/scrap/write-down scenario (file `24`'s track). It does not propose an SMEsPlus account code, location-type design, or journal structure. It does not certify with absolute certainty that no NRV/write-down feature exists anywhere in the reference ERP's full version history — it reports a consistent absence across the documentation surfaces searched and treats that as `HOLD`, not as a proven negative. It does not decide manufacturing WIP or inter-company transfer classification (rows included in §2's table only for internal consistency, owned by files `22` and `25` respectively). It does not declare Scenario 24 closed.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
