# 16 — COGS 32-Scenario Evidence Register

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`

Status: EVIDENCE REGISTER ONLY — no scenario below is PASS/FINAL/APPROVED; all Layer C entries are CANDIDATE or JOINT/HOLD pending Boss and Joint review.

---

## 0. Register Conventions (read before use)

**Evidence layering** (mandatory, never merged):
- **Layer A** — Reference ERP official documentation, observed behavior only. Cited as: `Reference ERP official documentation — <topic>, version <N>, retrieved 2026-09-02`. The reference system is a learning/benchmark source only; nothing here is copied source code, ORM/schema, or method/field identifiers, and nothing here is assumed correct for Thailand or assumed to be the required SMEsPlus design.
- **Layer B** — Thai statutory/tax/audit evidence. This file does not carry primary Thai statutory citations; Thai authoritative evidence is owned by file `24_THAI_ACCOUNTING_TAX_STATUTORY_EVIDENCE_REGISTER.md`. Every scenario below marks Layer B as `HOLD / EVIDENCE REQUIRED — SEE FILE 24` unless a point is self-evidently a pure mechanical/timing question with no statutory content.
- **Layer C** — SMEsPlus candidate semantics. Always marked `CANDIDATE` (directional only, not binding) or `JOINT/HOLD` (an open Joint Team decision controls). Never a final answer.

**Foundational rule carried through every scenario:** *Inventory emits facts; Accounting decides postings.* A quantity or cost movement observed in the reference system's stock ledger is a **fact candidate**, not an automatic accounting instruction. Not every inventory-value decrease is COGS — scrap, loss, write-down, adjustment, internal transfer, and correction must each be separately proven before being classified as Cost of Goods Sold versus another financial classification (loss, expense, contra-asset, or no P&L effect at all).

**Open Joint decisions referenced** (JT-01 through JT-12, per governing prompt — none resolved by this file):
- JT-01 valuation policy ownership
- JT-02 costing methods
- JT-03 continuous/periodic timing
- JT-04 COGS recognition timing
- JT-05 return cost basis
- JT-06 late supplier bill
- JT-07 period close design
- JT-08 landed-cost eligibility
- JT-09 WIP timing
- JT-10 inter-company transfer
- JT-11 opening-balance certification
- JT-12 period lock policy

**"Periodic" and "Perpetual" as used below** follow the reference system's own documented split: Periodic (also documented as manual/at-closing valuation) posts inventory and cost-of-sale journal entries only when an accountant runs a stock-closing/valuation entry, with physical stock movement tracked separately in a stock ledger that is not, by itself, synchronized to the general ledger. Perpetual (also documented as automated/real-time valuation) posts a valuation-account entry at each qualifying stock movement and/or invoice event, so the general ledger and the stock ledger move together continuously. Evidence: `Reference ERP official documentation — Inventory Valuation (Periodic vs Perpetual configuration), version 18.0/19.0, retrieved 2026-09-02`. A material **version delta** is recorded once here and re-flagged wherever it changes a scenario's answer: in the oldest documented architecture the perpetual mode posts a journal entry at the moment of each individual stock movement; in the newest documented architecture (major version 19) the perpetual mode was re-architected to post its valuation-account impact through an automated closing process anchored at the invoice/bill level rather than at each discrete movement, explicitly to address performance and general-ledger-clarity concerns. SMEsPlus must not silently carry either interpretation forward — see `02_REFERENCE_VERSION_BEHAVIOR_DELTA_REGISTER.md` for the full delta record; this file only re-flags it where it is scenario-material (Scenarios 2, 3, 12, 13, 30).

**Field evidence sheet format is not repeated per scenario in this file** — that format lives in files 04/05/06. This file is scenario-outcome-oriented per governing-prompt §10 and §7's instruction that no material cell be left blank; each scenario entry below states Periodic outcome, Perpetual outcome, evidence, JT/HOLD cross-references, and a "why this is/isn't COGS" note.

---

## SCENARIO 1 — Opening inventory with known quantity and value

**Periodic treatment.** The reference system's periodic/manual mode does not itself certify an opening balance; it depends entirely on a physical count and an accountant-entered opening inventory value, since the stock ledger and the general ledger are not continuously reconciled in this mode. The opening value becomes the first term in the documented periodic identity (`Opening Inventory + Net Purchases − Closing Inventory = Cost of Goods Sold`, tested at Reconciliation Identity level in file 27) only if the counted quantity and the costing-method-derived value are both evidenced. Evidence: `Reference ERP official documentation — Inventory Valuation (Periodic/Manual configuration), version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-11 (opening-balance certification — unresolved), JT-01 (valuation policy ownership).

**Perpetual treatment.** In automated/perpetual mode, an opening balance must be loaded as a dated valuation-account entry with an offsetting equity or suspense line, because every subsequent movement layer is computed relative to whatever quantity/cost basis is already on record; an unevidenced or wrong opening layer propagates into every later average-cost or FIFO-layer computation for that product. Evidence: same citation as above, `Automatic Inventory Valuation`, version 18.0, retrieved 2026-09-02.
JT cross-refs: JT-11, JT-02 (costing method — average/FIFO layer seeding).

**Why this is/isn't COGS.** Opening inventory itself is never COGS — it is a balance-sheet asset carrying amount. It only becomes COGS-relevant as an input term once it is released against a later sale. Layer B: HOLD / EVIDENCE REQUIRED — SEE FILE 24 (opening stock certification and physical count evidentiary requirements under Thai practice). Layer C: JOINT/HOLD — JT-11 is explicitly unresolved; SMEsPlus must not assume any opening-balance-loading mechanism is safe without an explicit migration/certification control (see also Scenario 31).

---

## SCENARIO 2 — Purchase receipt before vendor bill

**Periodic treatment.** A physical receipt with no bill has no accounting entry at all in periodic/manual mode — the reference documentation is explicit that "goods reception and outgoing shipments have no direct impact in the accounting" under this mode; the receipt exists only in the physical stock ledger until the accountant's closing entry captures whatever is physically on hand. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0/19.0, retrieved 2026-09-02`.
JT cross-refs: JT-03 (continuous/periodic timing), JT-07 (period close design — the received-not-billed quantity must be captured in the physical count feeding the close).

**Perpetual treatment.** This is the scenario most affected by the version delta. In the earlier documented architecture, receipt posts a debit to a receiving/interim (stock-input-type) asset account against a payable-clearing account at the moment of physical receipt, ahead of any bill. In the newest documented architecture (major version 19), the perpetual valuation impact is instead anchored to the automated closing/invoice-level process, so the accounting-visible effect of a receipt with no bill may not appear as a discrete journal entry until the closing process runs, even though the underlying quantity/cost fact is recorded immediately in the stock ledger. Evidence: `Reference ERP official documentation — Automatic Inventory Valuation, version 18.0, retrieved 2026-09-02` and `Reference ERP official documentation — Valuation Cheat Sheet (Perpetual/US accounting), version 19.0, retrieved 2026-09-02`.
JT cross-refs: JT-03, JT-06 (late supplier bill — same mechanical family as an unbilled receipt).

**Why this is/isn't COGS.** Never COGS by itself — a receipt only ever creates or increases an inventory-asset-side fact; no revenue event has occurred. Layer C: CANDIDATE — SMEsPlus should treat "received, unbilled" as an inventory-asset fact with an offsetting interim/clearing liability candidate, not as an expense, in both modes; final account classification is JOINT/HOLD pending JT-03/JT-06.

---

## SCENARIO 3 — Vendor bill before receipt

**Periodic treatment.** Under periodic/manual valuation the vendor bill is a payable-recognition and (depending on configured expense-account resolution) potential direct expense event, independent of physical receipt, because periodic mode does not gate the bill on stock movement; the physical receipt, when it later occurs, has no direct accounting entry of its own (per Scenario 2) and is instead absorbed into the next closing count. Evidence: `Reference ERP official documentation — Vendor Bills and Inventory Valuation interaction, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-03, JT-04 (COGS recognition timing — this is where a premature expense booking risk is most visible).

**Perpetual treatment.** A bill posted ahead of a matching receipt is documented as creating a valuation/clearing mismatch that the system carries until the receipt occurs, since the automated valuation account expects a receipt-side entry to clear against; in the pre-19 real-time-at-movement architecture this produces a visible interim-account imbalance until receipt, while in the 19.x invoice-anchored architecture the bill itself may be closer to the trigger point, making the receipt the lagging event instead. Evidence: same citation family as Scenario 2, plus `Reference ERP official documentation — Automatic Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-03, JT-06.

**Why this is/isn't COGS.** Not COGS in either mode at the bill-only moment — a vendor bill is a purchase/payable and inventory-capitalization event, not a cost-of-sale event; no sale has occurred. Layer C: CANDIDATE, mismatch/clearing treatment; final resolution JOINT/HOLD under JT-03/JT-06.

---

## SCENARIO 4 — Receipt and bill in the same period

**Periodic treatment.** No mid-period accounting distinction exists in periodic mode regardless of receipt/bill sequencing within the period — both are absorbed into the same period-end physical count and single closing entry. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-03.

**Perpetual treatment.** Documented as the clean case: receipt and bill both post within the same fiscal period, so any interim/clearing account opened by the earlier of the two events is closed by the later one before period close, leaving no cross-period clearing balance. Evidence: `Reference ERP official documentation — Valuation Cheat Sheet, version 19.0, retrieved 2026-09-02`.
JT cross-refs: JT-03, JT-07.

**Why this is/isn't COGS.** Not COGS — purely a purchase/capitalization pairing; COGS only arises later at the qualifying sale event. Layer C: CANDIDATE — this is the reference baseline case that should require no special SMEsPlus handling once JT-03/JT-04 are resolved.

---

## SCENARIO 5 — Receipt in period N, bill in period N+1

**Periodic treatment.** The physical receipt in period N is captured only through the period-N closing count (if evidence of receipt exists); the bill posted in N+1 is a period-N+1 payable event. Because periodic valuation does not tie the bill to the specific receipt event mechanically, the documentation implies a manual matching burden falls on the accountant to avoid either omitting the cost from period N's closing value or double-counting it in N+1. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-06 (late supplier bill), JT-07 (period close design), JT-12 (period lock policy).

**Perpetual treatment.** This is the documented purpose of the interim/clearing (stock-input-type) account architecture: the period-N receipt posts against the interim account, leaving an open balance that is understood to represent "received, not yet billed"; the period-N+1 bill clears it. The cross-period carry of that interim balance is exactly what a period-close/lock control must be able to explain. Evidence: `Reference ERP official documentation — Automatic Inventory Valuation (interim accounts), version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-06, JT-07, JT-12.

**Why this is/isn't COGS.** Not COGS in either period at either event — both are purchase-side/capitalization facts. Layer B: HOLD / EVIDENCE REQUIRED — SEE FILE 24 (Thai cut-off evidentiary requirement for goods received before period-end but billed after). Layer C: JOINT/HOLD — an explicit accrual candidate exists here (goods-received-not-invoiced) but SMEsPlus's specific accrual account and reversal mechanism are not decided by this research.

---

## SCENARIO 6 — Vendor bill price differs from receipt/valuation basis

**Periodic treatment.** Because periodic mode does not carry a per-receipt valuation layer forward in real time, a price difference mainly manifests as a difference between the closing count's carried value (from whatever cost basis was used at count time) and the amount actually paid; the documentation does not describe an automatic price-difference account operating in periodic mode — this is a manual reconciliation point for the accountant. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-02 (costing method), JT-06.

**Perpetual treatment.** The reference documentation names a dedicated Price Difference account, used specifically under standard-cost-type configurations to capture the variance between the standard cost already used to value the receipt and the actual vendor-billed price; under average-cost or FIFO-type configurations the documented behavior instead adjusts the running average or creates a new cost layer rather than routing the variance to a separate account. Evidence: `Reference ERP official documentation — Inventory Valuation Configuration (Price Difference Account), version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-02, JT-06.

**Why this is/isn't COGS.** Generally not COGS at the moment the variance is captured — it is a valuation/capitalization correction. It becomes COGS-relevant only indirectly, once the corrected cost basis flows through to a later sale. Layer C: CANDIDATE — a price-difference concept is plausible for SMEsPlus, but which costing methods it applies to, and whether it ever routes to a P&L variance account instead of capitalizing, is JOINT/HOLD under JT-02.

---

## SCENARIO 7 — Purchase return before bill

**Periodic treatment.** A return before any bill exists is a pure physical reversal in periodic mode — it is captured in the next closing count as a quantity/value reduction with no independent journal entry of its own, mirroring Scenario 2's "no bill, no entry" logic. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-05 (return cost basis).

**Perpetual treatment.** The documentation describes automatic accounting-entry generation when shipments are returned to a supplier, reversing the interim/valuation entries created at receipt; since no bill yet exists, the reversal unwinds only the receipt-side interim entry, not any payable. Evidence: `Reference ERP official documentation — Automatic Inventory Valuation (returns), version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-05.

**Why this is/isn't COGS.** Not COGS — a purchase return before billing is a pure reversal of a capitalization event, never a cost-of-sale event. Layer C: CANDIDATE, straightforward reversal; JT-05 still governs the general return-cost-basis principle for SMEsPlus even in this simplest case.

---

## SCENARIO 8 — Purchase return after bill

**Periodic treatment.** In periodic mode the return again shows up only through the next physical count; the already-posted bill's payable side must be corrected separately (a debit note or bill reversal), which the documentation treats as an ordinary vendor-credit accounting event distinct from the physical stock reduction. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-05.

**Perpetual treatment.** The documented behavior reverses the valuation-account entry using the same cost basis the original receipt was valued at (not a re-derived current cost), consistent with the general average-cost principle that outbound movements — including outbound returns to a supplier — use the existing cost basis rather than triggering a recalculation; the payable side is separately corrected via a vendor credit. Evidence: `Reference ERP official documentation — Average Price on Returned Goods, version 19.0, retrieved 2026-09-02`; `Reference ERP official documentation — Automatic Inventory Valuation (returns), version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-05, JT-02.

**Why this is/isn't COGS.** Not COGS — reversal of a capitalized purchase, never a cost-of-sale event, regardless of billing sequence. Layer C: CANDIDATE that "return reverses at original cost basis, not current/re-derived cost" is the right default principle to carry into SMEsPlus; formal adoption is JOINT/HOLD under JT-05.

---

## SCENARIO 9 — Landed cost before any sale

**Periodic treatment.** Periodic mode has no documented mechanism-of-record for landed-cost integration mid-period; the additional cost is expected to be folded into whichever cost basis feeds the next closing entry, meaning it is only visible in the general ledger once that closing entry is posted. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation and Landed Costs interaction, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-08 (landed-cost eligibility).

**Perpetual treatment.** The documented landed-cost function validates a dedicated landed-cost document against a designated journal, and — when none of the affected quantity has yet moved out — increases the valuation-account carrying amount of the still-on-hand stock directly, with the offset posted to the landed-cost source (a vendor bill line or a manually entered cost). This is the clean, fully capitalizable case. Evidence: `Reference ERP official documentation — Landed Costs, version 18.0/19.0, retrieved 2026-09-02`.
JT cross-refs: JT-08.

**Why this is/isn't COGS.** Not COGS — landed cost added before any sale is pure inventory capitalization, raising the asset carrying amount; no cost has been released against revenue. Layer C: CANDIDATE — full capitalization when 100% of the affected quantity is still on hand is the least-contested landed-cost case; scope/eligibility of which cost types may be capitalized (freight vs. insurance vs. recoverable duty/VAT) is JOINT/HOLD under JT-08 and flagged to Thai evidence (Layer B: HOLD / EVIDENCE REQUIRED — SEE FILE 24, recoverable-VAT/duty distinction).

---

## SCENARIO 10 — Landed cost after partial sale

**Periodic treatment.** Not separately documented as a distinct periodic mechanism; because periodic mode has no persistent per-unit cost layer between closes, a landed cost arriving mid-period is, per the same logic as Scenario 9, simply absorbed into whatever value feeds the next closing entry — meaning the split between "still on hand" and "already sold" portions is not distinguished by the periodic mechanism itself, only by the physical count.
Evidence: inferred directly from `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`; no periodic-specific landed-cost split procedure is separately documented — marked PROVISIONAL.
JT cross-refs: JT-08, JT-04.

**Perpetual treatment.** The documented behavior is materially important and directly on point for governing-prompt §10 item 10: when a landed cost is validated after part of the affected quantity has already been delivered/sold, the reference system splits the additional cost proportionally — the portion attributable to remaining on-hand quantity is capitalized to the valuation account, and the portion attributable to the already-sold quantity is routed to the expense/cost-of-revenue side rather than to inventory, because that portion cannot be capitalized into stock that no longer exists on the balance sheet. Evidence: `Reference ERP official documentation — Landed Costs, version 18.0/19.0, retrieved 2026-09-02`; corroborating community/forum discussion of the mechanism was reviewed only as secondary evidence, not treated as authoritative.
JT cross-refs: JT-08, JT-04 (this is a direct COGS-timing interaction).

**Why this is/isn't COGS.** Split scenario: the on-hand-quantity portion is not COGS (capitalized to asset); the already-sold-quantity portion is a genuine late-arriving COGS adjustment, because the additional cost relates to goods whose revenue has already been recognized. Layer C: JOINT/HOLD — proportional split is a plausible candidate principle, but SMEsPlus's specific allocation formula, which account absorbs the sold-portion adjustment, and the prior-period-vs-current-period presentation are all unresolved (JT-08, JT-04, JT-07).

---

## SCENARIO 11 — Landed cost after full sale

**Periodic treatment.** Same PROVISIONAL basis as Scenario 10 — no distinct periodic mechanism is documented; the full amount would only surface through the next closing entry's implied variance, since there is no remaining on-hand quantity to absorb it into.
JT cross-refs: JT-08, JT-04.

**Perpetual treatment.** This is a documented and, per reviewed community evidence, an area of observed version-delta instability. Where 100% of the affected quantity has already been delivered and invoiced (zero remaining quantity), the entire landed-cost amount cannot be capitalized to stock and must route to an expense/cost account instead. However, the exact destination account is reported to differ by version: one documented major-version behavior routes the full amount to the cost-of-goods-sold account (preserving accurate product costing and gross margin), while another reports it remaining in the original freight/expense account rather than moving to cost-of-goods-sold; a further reported issue notes at least one version failing to generate the accounting entry at all for this specific zero-remaining-quantity case, which would itself be a control break (valuation moves without a corresponding journal entry). Evidence: `Reference ERP official documentation — Landed Costs, version 18.0/19.0, retrieved 2026-09-02`; version-behavior-difference and known-issue points drawn from reviewed community/forum and issue-tracker discussion are secondary evidence only, not treated as authoritative documentation, and are flagged for independent verification before any SMEsPlus candidate is finalized.
JT cross-refs: JT-08, JT-04, and Audit VETO (evidence-chain integrity — a valuation change with no journal entry is a material control concern regardless of Thai statutory status).

**Why this is/isn't COGS.** COGS in principle (the cost relates entirely to goods whose revenue is already recognized), but the reference system's own documented/reported behavior for *which account* receives it is inconsistent across versions and, in at least one reported case, may not post at all. Layer C: HOLD — this is flagged as a material open item, not a candidate; SMEsPlus must not silently inherit either observed behavior. See also `30_COGS_MATERIAL_UNKNOWN_CONFLICT_REGISTER.md`.

---

## SCENARIO 12 — Customer delivery before invoice

**Periodic treatment.** No entry at delivery; the delivery is a physical stock ledger event only, captured (as a reduction) in the next closing count and blended into the periodic COGS-by-difference calculation, not traced to the individual delivery. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-03, JT-04.

**Perpetual treatment.** Version-delta-material, mirroring Scenario 2. In the earlier documented real-time-at-movement architecture, delivery ahead of invoicing posts a valuation-account credit against an interim (stock-output-type) account immediately at the delivery event, with cost-of-goods-sold recognized at that same moment under the documented Anglo-Saxon/US perpetual configuration. In the newest documented architecture (major version 19), the valuation-account impact is instead anchored to the invoice-level automated closing process, meaning the accounting-visible cost-of-goods-sold entry may not appear until invoicing/closing even though the physical delivery and its stock-ledger fact are immediate. Evidence: `Reference ERP official documentation — Valuation Cheat Sheet, version 19.0, retrieved 2026-09-02`; `Reference ERP official documentation — Automatic Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-03, JT-04 (this is the single most direct evidence point for the COGS-recognition-timing Joint decision).

**Why this is/isn't COGS.** This is exactly the scenario the reference system's own documentation uses to demonstrate that inventory-value decrease and COGS recognition are not automatically the same moment — under the older architecture they coincide at delivery; under the newest documented architecture they can diverge, with the inventory-ledger fact preceding the accounting-recognized cost by design. Layer C: HOLD — this is the central unresolved question for JT-04 and must not be pre-decided by this file.

---

## SCENARIO 13 — Customer invoice before delivery

**Periodic treatment.** The invoice is a revenue-recognition/receivable event independent of physical delivery in periodic mode; no inventory-side entry occurs until the next closing count captures whatever quantity actually moved. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-03, JT-04.

**Perpetual treatment.** Under the invoice-anchored newest documented architecture, an invoice issued ahead of delivery is a materially different case than under the older delivery-anchored architecture: if the valuation/COGS impact is tied to invoicing, an invoice-before-delivery sequence risks recognizing cost of goods sold before the goods have physically left the warehouse, which is a timing risk the older delivery-anchored architecture did not have (it recognized COGS at physical delivery regardless of invoice timing). Evidence: `Reference ERP official documentation — Valuation Cheat Sheet, version 19.0, retrieved 2026-09-02`.
JT cross-refs: JT-04 (highest materiality — revenue/cost matching risk), JT-03.

**Why this is/isn't COGS.** Should not be COGS until the goods actually leave inventory, regardless of invoice timing — the underlying principle (cost follows the physical/economic transfer, not merely the paper event) is a standard matching-principle question, not something this file can resolve from reference-system behavior alone. Layer B: HOLD / EVIDENCE REQUIRED — SEE FILE 24 (Thai revenue/expense-matching requirement for invoice-before-delivery sequencing). Layer C: HOLD — flagged as a material open item for JT-04; the version delta itself is evidence that SMEsPlus cannot assume invoice timing is a safe COGS trigger without an explicit decision.

---

## SCENARIO 14 — Delivery and invoice same period

**Periodic treatment.** No distinction from Scenario 4's purchase-side analog — both events are absorbed into the same period-end closing count and single closing entry regardless of internal sequencing. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-03.

**Perpetual treatment.** The clean baseline case under either documented architecture: whichever event anchors the valuation/COGS entry (delivery under the older architecture, invoicing under the newest), the other event occurs in the same period, so no cross-period interim balance survives to a close. Evidence: `Reference ERP official documentation — Valuation Cheat Sheet, version 19.0, retrieved 2026-09-02`.
JT cross-refs: JT-03, JT-04.

**Why this is/isn't COGS.** COGS, cleanly, once the anchoring event (whichever JT-04 selects) has occurred — this is the reference baseline with no timing ambiguity. Layer C: CANDIDATE as the reference baseline; still contingent on JT-04's resolution of which event anchors recognition.

---

## SCENARIO 15 — Partial delivery

**Periodic treatment.** Periodic mode has no per-delivery cost tracking; a partial delivery is simply a partial physical-quantity reduction absorbed into the closing count like any other movement — the documentation draws no distinction between full and partial delivery in this mode. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-03.

**Perpetual treatment.** Documented as valuing and posting the delivered quantity's cost only, leaving the undelivered/backordered balance on hand and unaffected; under the average-cost method the documented recompute formula operates on inbound quantity only, so a partial outbound delivery consumes the current average cost per unit for exactly the quantity that moved, without altering the average for the remainder. Evidence: `Reference ERP official documentation — Automatic Inventory Valuation, version 18.0, retrieved 2026-09-02`; `Reference ERP official documentation — Average Price on Returned Goods (average-cost recompute formula), version 19.0, retrieved 2026-09-02`.
JT cross-refs: JT-04, JT-02.

**Why this is/isn't COGS.** COGS only for the quantity actually delivered (subject to JT-04's anchoring-event answer); the undelivered remainder is not COGS and stays an inventory asset. Layer C: CANDIDATE — quantity-proportional recognition is the expected default; final anchoring event is JOINT/HOLD under JT-04.

---

## SCENARIO 16 — Backorder

**Periodic treatment.** Same logic as Scenario 15 — periodic mode does not distinguish a backorder from any other partial movement; only the physical closing count matters. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-03.

**Perpetual treatment.** A backorder is documented as a separate, linked delivery document for the undelivered balance; each partial delivery document (the initial partial and the eventual backorder completion) independently triggers its own valuation/COGS-anchoring event under whichever architecture is in force, at whatever quantity actually ships on that document. Evidence: `Reference ERP official documentation — Automatic Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-04.

**Why this is/isn't COGS.** COGS only accrues as each backorder increment actually ships — the original order's un-shipped balance is never COGS until it, too, physically moves (and, under JT-04, until its anchoring event occurs). Layer C: CANDIDATE, consistent with Scenario 15; no new principle beyond partial-delivery quantity-proportionality.

---

## SCENARIO 17 — Customer return in same period

**Periodic treatment.** A same-period return nets against the same period's closing count — the documentation implies the physical increase from the return is simply part of the same physical stock-on-hand figure counted at close, with no separate journal entry required in this mode. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-05.

**Perpetual treatment.** The documented mechanism reverses the COGS/valuation entry using the original cost basis at which the goods were sold, not a newly computed current cost — explicitly stated for average-cost valuation as "the average cost does not change" on outbound movements, including reversing inbound movements such as a customer return, precisely to avoid inconsistency between the physical stock ledger and the average-cost calculation. Evidence: `Reference ERP official documentation — Average Price on Returned Goods, version 19.0, retrieved 2026-09-02`.
JT cross-refs: JT-05 (this is the primary evidence source for the Joint return-cost-basis decision).

**Why this is/isn't COGS.** A COGS reversal (contra-COGS), not a new inventory-value-decrease event — the documented principle is that a return reverses the original cost-of-sale entry at its original cost basis. Layer C: CANDIDATE that "reverse at original cost basis" is the correct default principle for SMEsPlus; formal adoption remains JOINT/HOLD under JT-05.

---

## SCENARIO 18 — Customer return in later period

**Periodic treatment.** Because periodic mode has no persistent per-sale cost layer, a return in a later period is documented (by absence of any contrary mechanism) as simply increasing that later period's physical count and thus that period's COGS-by-difference — there is no traceable link back to the original sale's cost in this mode, only to the current period's overall inventory movement. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-05, JT-12 (period lock policy — is the prior period allowed to be touched, or does the return land entirely in the current period).

**Perpetual treatment.** Same original-cost-basis reversal mechanism as Scenario 17, but now crossing a period boundary; because the reversal references the original sale's cost layer directly rather than recomputing a current value, it is mechanically able to reverse into a locked/closed prior period's figures unless a period-lock control specifically prevents posting into a closed period, in which case the documented alternative is to post the reversal in the current open period referencing the original transaction. Evidence: `Reference ERP official documentation — Average Price on Returned Goods, version 19.0, retrieved 2026-09-02`.
JT cross-refs: JT-05, JT-12.

**Why this is/isn't COGS.** A COGS reversal tied to the original sale, regardless of which period it lands in — the substantive question is not whether it is COGS-related (it is) but which period absorbs the reversal. Layer B: HOLD / EVIDENCE REQUIRED — SEE FILE 24 (Thai treatment of prior-period revenue/cost reversals and any restatement-versus-current-period rule). Layer C: JOINT/HOLD under JT-05 and JT-12 jointly — period-lock interaction with return reversal is an open control question, not a reference-system-settled one.

---

## SCENARIO 19 — Cancellation before physical movement

**Periodic treatment.** No accounting entry exists to cancel in periodic mode if no physical movement has yet occurred — this is a non-event for the periodic mechanism by definition, since periodic valuation only reacts to physical counts. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: none material — no JT is engaged because no fact was ever emitted.

**Perpetual treatment.** Likewise a non-event for the valuation account in perpetual mode if the cancellation occurs strictly before the qualifying stock movement (receipt or delivery) — any earlier commercial document (a purchase order or sales order) that is cancelled before it produces a stock movement has no valuation-account trace to reverse. Evidence: `Reference ERP official documentation — Automatic Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: none material.

**Why this is/isn't COGS.** Never COGS, and never even an inventory-value fact — nothing physical or financial occurred. Layer C: CANDIDATE — the only SMEsPlus-relevant point is a control one (cancellation-before-movement should be provably a no-financial-effect event, auditable as such), not a valuation question.

---

## SCENARIO 20 — Correction/reversal after physical movement

**Periodic treatment.** A correction after physical movement in periodic mode is again absorbed into the next closing count's physical figure — the documentation does not describe a discrete "correction" transaction type distinct from any other adjustment to the counted quantity/value in this mode. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-07.

**Perpetual treatment.** Once a stock movement has posted its valuation entry, a correction is documented as requiring an explicit reversing/adjusting transaction referencing the original movement (not a silent edit to the posted entry), consistent with the general audit-trail principle that a posted valuation-account entry is not directly mutated. Evidence: `Reference ERP official documentation — Automatic Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-04, and Audit VETO (no silent mutation of a posted valuation fact).

**Why this is/isn't COGS.** Depends entirely on what is being corrected — a correction to a sale-related movement is a COGS correction; a correction to a purchase-related movement is an inventory-capitalization correction; a correction to a non-sale movement (adjustment, transfer) is neither. This scenario is a mechanism (how corrections post), not itself a COGS-classification answer. Layer C: CANDIDATE — reference-style "reverse-and-repost, never mutate" is a sound audit principle to carry forward; specific SMEsPlus correction workflow is out of this research's scope (see Contract C in file 31).

---

## SCENARIO 21 — Inventory adjustment gain

**Periodic treatment.** A counted quantity higher than the book quantity simply raises the closing count's value, which in the documented periodic COGS-by-difference formula (`Opening + Purchases − Closing = COGS`) mechanically *reduces* the derived COGS figure for the period — the documentation does not describe an adjustment-gain figure being separately visible from the COGS number in this mode; it is blended into it unless the accountant manually isolates it. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-01 (valuation policy ownership — who classifies an adjustment).

**Perpetual treatment.** The documented mechanism for a positive inventory adjustment posts a valuation-account debit against a dedicated inventory-adjustment/variance-type account, not against cost of goods sold — the reference system treats a count-driven adjustment as its own transaction type distinct from a sale. Evidence: `Reference ERP official documentation — Automatic Inventory Valuation (inventory adjustments), version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-01.

**Why this is/isn't COGS.** Not COGS. This is the governing-prompt's own headline example: an inventory-value *increase* from a count adjustment is unambiguously not a sale-driven cost release, and the reference system's perpetual mode structurally keeps it out of the cost-of-goods-sold account by routing it to a distinct adjustment/variance account. The periodic mode's blending of this figure into a single derived COGS number is precisely the kind of "not every inventory-value change is COGS" contamination risk the governing prompt warns against. Layer C: CANDIDATE — SMEsPlus should structurally separate adjustment gains from COGS even where a periodic-style derived figure is also produced, to avoid a distorted gross-margin figure; final treatment JOINT/HOLD under JT-01.

---

## SCENARIO 22 — Inventory adjustment loss

**Periodic treatment.** Mirror of Scenario 21 — a counted quantity lower than book quantity lowers the closing value and mechanically *increases* the derived periodic COGS-by-difference figure, again blending a non-sale event into the COGS number unless manually isolated. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-01.

**Perpetual treatment.** The documented mechanism posts a valuation-account credit against the same inventory-adjustment/variance-type account used for gains (mirror-image entry), not against cost of goods sold. Evidence: `Reference ERP official documentation — Automatic Inventory Valuation (inventory adjustments), version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-01.

**Why this is/isn't COGS.** Not COGS, for the same structural reason as Scenario 21 — an unexplained count shortfall is a loss/variance event, not evidence that a sale occurred. Conflating it with COGS would overstate cost of goods sold and understate a distinct loss line, misrepresenting gross margin. Layer C: CANDIDATE — same separation principle as Scenario 21; JOINT/HOLD under JT-01 for the specific SMEsPlus account and threshold/approval control around adjustment losses.

---

## SCENARIO 23 — Scrap / damage / shrinkage

**Periodic treatment.** Not separately distinguishable from Scenario 22 in periodic mode's own mechanism — the documentation does not describe a dedicated scrap/damage transaction type in periodic valuation; a scrapped unit simply is not present at the next physical count and is blended into the same derived-COGS shortfall as any other unexplained loss unless the accountant maintains a separate scrap log outside the valuation mechanism itself. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-01.

**Perpetual treatment.** The reference system documents a dedicated scrap transaction type that removes quantity from a normal storage location and posts its valuation-account impact against a scrap/loss-type expense account (the documentation groups this with the same production/loss account family used for other non-sale consumption) — again structurally distinct from cost of goods sold. Evidence: `Reference ERP official documentation — Automatic Inventory Valuation (scrap), version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-01, JT-09 (WIP timing — scrap arising from a manufacturing order specifically).

**Why this is/isn't COGS.** Not COGS — scrap/damage/shrinkage is an operational loss, not a cost-of-sale event; no revenue was recognized. This is the second headline example the governing prompt names explicitly. Layer B: HOLD / EVIDENCE REQUIRED — SEE FILE 24 (Thai treatment and any deductibility conditions for destroyed/damaged inventory, and evidentiary requirements — e.g., witnessed destruction — for a loss claim). Layer C: CANDIDATE that scrap must be structurally isolated from COGS in SMEsPlus; final account and control (approval, evidence retention) JOINT/HOLD under JT-01.

---

## SCENARIO 24 — NRV / write-down or impairment treatment

**Periodic treatment.** Not documented as a mechanism-native feature of periodic valuation itself — a write-down to net realizable value is an accounting judgment applied on top of whatever quantity/cost the periodic mechanism produces, not something the periodic closing entry computes on its own. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02` (absence of a native write-down mechanism, PROVISIONAL — not exhaustively verified across all documented versions).
JT cross-refs: JT-01.

**Perpetual treatment.** The reference documentation does not describe a native "lower of cost or net realizable value" automated feature either; a valuation write-down, where used, is documented as an inventory revaluation transaction posting a valuation-account adjustment against a loss/write-down-type account, functioning mechanically like Scenario 22's adjustment loss but carrying different accounting *meaning* (a recognized decline in value versus an unexplained count shortfall). Evidence: `Reference ERP official documentation — Inventory Valuation Configuration (manual revaluation), version 18.0, retrieved 2026-09-02` — PROVISIONAL, mechanism-only, not a policy statement.
JT cross-refs: JT-01.

**Why this is/isn't COGS.** Not COGS under most authoritative frameworks — a write-down to net realizable value is typically presented as a separate loss/impairment line (or, under some frameworks, folded into cost of sales presentation but still conceptually distinct from a sale-driven cost release); the reference system provides no authoritative guidance on this because it is a statutory/framework question, not a system-mechanism question. Layer B: HOLD / EVIDENCE REQUIRED — SEE FILE 24 (Thai statutory NRV/write-down requirement, reversal permissibility, and presentation — this is explicitly named in the governing prompt as a Thai-evidence-owned point). Layer C: HOLD — no SMEsPlus candidate is offered here pending Layer B; this is one of the more statute-sensitive scenarios in the register.

---

## SCENARIO 25 — Internal warehouse transfer, same company

**Periodic treatment.** A same-company internal transfer between locations, if both locations are within the same valuation/company scope, produces no book-value change under periodic mode's own logic — total company-wide quantity and value are unchanged; only location-level physical records move. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: none material at company level; potentially JT-10 only if the two locations sit under different accounting/company scopes internally (see Scenario 26 boundary).

**Perpetual treatment.** The documented behavior for a same-valuation-scope internal transfer is either no valuation-account entry at all, or a wash entry (debit and credit to the same or equivalent valuation account), because no ownership or expense event has occurred — only physical location changed. Evidence: `Reference ERP official documentation — Automatic Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: none material.

**Why this is/isn't COGS.** Not COGS, and not even a value change — this is the clearest possible "inventory movement without a value or COGS effect" case, useful as a control baseline against which every other scenario's COGS/non-COGS classification should be checked. Layer C: CANDIDATE — no material SMEsPlus decision required beyond confirming location-level tracking does not leak into COGS.

---

## SCENARIO 26 — Inter-company inventory transfer

**Periodic treatment.** Where the two locations belong to different legal companies, periodic mode is documented as requiring the transfer to be modeled as a sale-and-purchase pair (an inter-company sale from Company A and a corresponding purchase by Company B), each side following its own company's periodic closing mechanism independently — the documentation does not describe a "transfer" transaction type that bypasses this at the company-boundary level. Evidence: `Reference ERP official documentation — Inter-company transactions and Inventory Valuation, version 18.0, retrieved 2026-09-02` — PROVISIONAL, general inter-company documentation reviewed rather than a dedicated inter-company-valuation page.
JT cross-refs: JT-10 (inter-company transfer).

**Perpetual treatment.** Each company independently books its own valuation-account entries as though the movement were an ordinary external sale (Company A) and purchase (Company B), meaning Company A's side can produce a cost-of-goods-sold-shaped entry at its own delivery/invoice-anchoring event, and Company B capitalizes the inbound leg at whatever transfer price was used — which is not necessarily Company A's original cost basis. Evidence: same citation as above, PROVISIONAL.
JT cross-refs: JT-10, JT-04 (whether Company A's leg should even be presented as "COGS" in a consolidated view, or eliminated).

**Why this is/isn't COGS.** At the single-company (unconsolidated) level, Company A's outbound leg has the shape of COGS; at a consolidated group level it should not survive as COGS, since no sale to an external party occurred — an elimination is expected. Whether SMEsPlus's inter-company model produces true intercompany-sale documents (as observed) or a distinct non-P&L transfer type is unresolved. Layer C: HOLD — JT-10 is explicitly unresolved per the governing prompt's Joint decision list, and this scenario is the clearest evidence that the reference system's own default (model as a sale) may not be the right SMEsPlus answer without a consolidation/elimination design, which is out of this file's scope.

---

## SCENARIO 27 — Manufacturing raw-material consumption

**Periodic treatment.** Periodic mode is not documented as distinguishing manufacturing consumption from any other outbound movement — raw material leaving stock for a production order is, like a sale or scrap, simply absent from the next closing count, blended into the derived periodic figure unless separately isolated by the accountant. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-09 (WIP timing), JT-01.

**Perpetual treatment.** The documented mechanism, when automated accounting is configured for the relevant categories and a cost-of-production account is set on the production location, posts a valuation-account credit on the raw-material side (reducing raw-material inventory value) against a debit to a work-in-progress-type account, moving value out of raw-material inventory and into WIP — not into cost of goods sold. Evidence: `Reference ERP official documentation — Work-in-Progress Costs, version 19.0, retrieved 2026-09-02`.
JT cross-refs: JT-09.

**Why this is/isn't COGS.** Not COGS — raw-material consumption into production is an asset-to-asset transfer (raw material inventory to WIP inventory), not a cost-of-sale event; no finished good has yet been sold, and in most documented configurations no finished good has even been completed yet. Layer C: CANDIDATE that raw-material consumption must route to WIP, not COGS, in SMEsPlus; the specific WIP account design and whether WIP is tracked at all (versus an immediate RM-to-FG shortcut) is JOINT/HOLD under JT-09.

---

## SCENARIO 28 — Manufacturing WIP to finished goods

**Periodic treatment.** Same absence-of-distinction logic as Scenario 27 — periodic mode has no documented native WIP concept; the transformation from raw material to finished good is invisible between closes and only the final finished-goods quantity/value at the next count matters. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-09.

**Perpetual treatment.** On completion of the manufacturing order, the documented mechanism transfers the accumulated cost from the work-in-progress-type account to the finished-goods valuation account — a debit to finished-goods inventory and a credit clearing the WIP account (net of whatever WIP balance was carried, if optional WIP journal entries were used for a long-running order). Evidence: `Reference ERP official documentation — Work-in-Progress Costs, version 19.0, retrieved 2026-09-02`.
JT cross-refs: JT-09.

**Why this is/isn't COGS.** Not COGS — this is another asset-to-asset transfer (WIP inventory to finished-goods inventory); still no sale has occurred. Layer C: CANDIDATE, same principle as Scenario 27; JOINT/HOLD under JT-09 for SMEsPlus's specific WIP-to-FG mechanics and whether WIP is a required intermediate stage or an optional one (the reference documentation describes WIP journal entries as optional/manual for long-running orders, not mandatory for every manufacturing order).

---

## SCENARIO 29 — Manufacturing finished goods to COGS

**Periodic treatment.** No distinction from an ordinary sale of a purchased product — periodic mode does not differentiate a manufactured finished good from a purchased one once it is in finished-goods stock; its cost simply exits through the same closing-count-driven derived COGS figure as any other sold item. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-04, JT-09.

**Perpetual treatment.** Once a manufactured finished good is delivered/invoiced, it follows the same documented delivery/invoice-anchored valuation mechanism as any other product (Scenario 12/13's mechanism), released from the finished-goods valuation account into cost of goods sold at whichever event the applicable architecture version anchors recognition to. Evidence: `Reference ERP official documentation — Valuation Cheat Sheet, version 19.0, retrieved 2026-09-02`.
JT cross-refs: JT-04, JT-09.

**Why this is/isn't COGS.** COGS, at the same anchoring event and subject to the same JT-04 timing question as a purchased-product sale — the only difference from Scenario 12/13 is that the cost basis being released originated from the manufacturing cost flow (Scenarios 27-28) rather than from a purchase. Layer C: CANDIDATE, contingent on JT-04 and JT-09 both being resolved; the manufacturing cost accumulation (materials, work-center cost, any labor/overhead absorption) must itself be evidence-backed before the released COGS figure can be trusted — this file does not certify any specific cost-accumulation formula.

---

## SCENARIO 30 — Period-end closing/cut-off with unbilled receipts and uninvoiced deliveries

**Periodic treatment.** This is the documented core purpose of the periodic mechanism: the accountant's single closing entry is expected to capture the full physical count regardless of billing/invoicing status, meaning unbilled receipts and uninvoiced deliveries are automatically included in the physical figure (they are physically present or absent, billing-status notwithstanding) — but the *purchase accrual* (goods received, not billed) and *revenue cut-off* (goods delivered, not invoiced) are separate, not-automatically-generated accounting entries that the documentation implies fall to the accountant's manual judgment in this mode. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02`.
JT cross-refs: JT-06, JT-07, JT-12.

**Perpetual treatment.** Materially version-delta-sensitive. Under the older delivery/receipt-anchored architecture, the interim (stock-input/stock-output-type) accounts are documented as exactly the mechanism that carries "received-not-billed" and "delivered-not-invoiced" balances across a period boundary, giving an automatic, traceable accrual balance at any point in time without a manual entry. Under the newest invoice-anchored architecture, because the valuation/COGS impact is tied to the invoice/bill-level automated closing process rather than to the physical movement itself, an uninvoiced delivery or an unbilled receipt may not yet have posted *any* accounting-side valuation impact at period-end, shifting the cut-off risk from "is the interim balance correctly stated" to "has the automated closing process run far enough to capture the period's economic activity at all." Evidence: `Reference ERP official documentation — Automatic Inventory Valuation, version 18.0, retrieved 2026-09-02`; `Reference ERP official documentation — Valuation Cheat Sheet, version 19.0, retrieved 2026-09-02`.
JT cross-refs: JT-06, JT-07, JT-12 — all three simultaneously engaged; this is the single most control-dense scenario in the register.

**Why this is/isn't COGS.** Mixed — the physical quantity change is a fact regardless of billing status; whether its value has been *recognized* as COGS (or as a purchase accrual/capitalization) at period-end depends entirely on the architecture version and the close-timing policy in force. This scenario is the direct evidentiary basis for why the governing prompt requires an explicit `REFERENCE_VERSION_BEHAVIOR_DELTA_REGISTER` (file 02) and why JT-07 (period close design) cannot be resolved without first resolving JT-04 (COGS recognition timing). Layer C: HOLD — no close-design candidate is offered here; this is flagged directly to file 27 (Reconciliation Identity Register) and file 23 (Period Close/Cutoff Model).

---

## SCENARIO 31 — Migration / opening inventory replay

**Periodic treatment.** Not a reference-system-documented concept at all — migration/replay is a SMEsPlus-specific operational concern, not a feature the reference documentation addresses for either mode. What periodic mode *does* establish, by analogy, is that an opening inventory value is only as trustworthy as the physical count and costing method behind it (Scenario 1), which is directly relevant to any migration cut-over: a migrated opening balance is functionally identical to a period-1 opening count and must meet the same evidentiary bar. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02` (evidentiary-standard analogy only; migration itself is out of reference-system documentation scope).
JT cross-refs: JT-11.

**Perpetual treatment.** Likewise not directly documented; by analogy to Scenario 1's perpetual opening-balance loading, a migrated opening position under perpetual/automated valuation must seed each product's cost-layer/average-cost basis correctly, because every subsequent perpetual computation (average recompute, FIFO layer consumption) depends on that seed being right — an incorrect migrated seed propagates silently into every later transaction's cost. Evidence: `Reference ERP official documentation — Automatic Inventory Valuation, version 18.0, retrieved 2026-09-02` (evidentiary-standard analogy only).
JT cross-refs: JT-11, JT-02.

**Why this is/isn't COGS.** Not COGS at the moment of load — a migrated opening balance is a balance-sheet asset carrying amount, exactly like Scenario 1. It becomes a COGS risk only derivatively: if the migrated seed is wrong, every subsequent COGS computation drawing on it is wrong. Layer B: HOLD / EVIDENCE REQUIRED — SEE FILE 24 (any Thai requirement for migration-cutover physical count/certification). Layer C: JOINT/HOLD under JT-11 — this file establishes only that the evidentiary bar for a migrated opening balance is at least as high as an ordinary period-1 opening count, not any specific SMEsPlus migration mechanism.

---

## SCENARIO 32 — Retry / idempotency / replay with no duplicated COGS or Inventory Value

**Periodic treatment.** Not addressed by reference documentation — periodic mode's single-closing-entry-per-period design has a structural (if untested-by-this-research) idempotency property in that re-running the same physical count and closing calculation for an already-closed period should, if the process is deterministic and the underlying count data unchanged, reproduce the same closing entry rather than a second one; but the documentation does not describe any explicit re-run/replay-safety control, so this is inference from the mechanism's shape, not an observed control. Evidence: `Reference ERP official documentation — Periodic (Manual) Inventory Valuation, version 18.0, retrieved 2026-09-02` — PROVISIONAL, inferred, not directly evidenced.
JT cross-refs: JT-07, JT-12, AI Control/Human Oversight VETO.

**Perpetual treatment.** Not addressed by reference documentation either — the automated posting of a valuation-account entry per qualifying movement or per closing run is not documented with an explicit duplicate-prevention/idempotency guarantee in the material reviewed; each stock movement is understood to post once at the time it is validated, but replay-safety under a retry (e.g., a failed post retried by an external system, or a SaaS integration re-sending the same event) is an integration/control design question the reference documentation does not speak to. Evidence: none found directly on point — marked HOLD, not PROVISIONAL, because no reference-system statement (even an inferable one) was located; this is a genuine documentation gap.
JT cross-refs: AI Control/Human Oversight VETO (directly on point — "no fabricated journal entry," "no fabricated cost," deterministic proof), JT-07, JT-12.

**Why this is/isn't COGS.** Not a COGS-classification question at all — this scenario is a control-integrity question (does replaying an already-processed event create a second, duplicate COGS/inventory-value fact). The reference ERP's public documentation does not provide authoritative evidence either way, so no Layer A finding can be cited beyond structural inference. Layer C: HOLD — this must be an explicit SMEsPlus design control (idempotency key, replay-detection, or equivalent), not something inherited from reference-system behavior, since no reference-system behavior on this point is evidenced. This is flagged as a material gap to `26_MIGRATION_OPENING_COST_REPLAY_IDEMPOTENCY_REGISTER.md` and `30_COGS_MATERIAL_UNKNOWN_CONFLICT_REGISTER.md`.

---

## Register Summary

- Scenarios with a clean, low-ambiguity Layer A finding in both modes: 4, 7, 9, 14, 17, 19, 21, 22, 23, 25 (10 of 32).
- Scenarios carrying a material, version-delta-driven open question (Layer C: HOLD, not CANDIDATE): 2, 3, 11, 12, 13, 30 (6 of 32) — all trace back to the single JT-04/architecture-version delta recorded in file 02.
- Scenarios with no reference-system documentation located at all (Layer C: HOLD on documentation-gap grounds): 32, and partially 26/31 (analogy-only).
- Scenarios explicitly deferred to Thai statutory evidence (Layer B: HOLD / EVIDENCE REQUIRED — SEE FILE 24) as a material, not incidental, dependency: 1, 5, 13, 18, 23, 24, 31.
- No scenario in this register is marked COMPLETE, FINAL, or PASS. Every Layer C entry is CANDIDATE (directional, non-binding) or JOINT/HOLD (an unresolved Joint decision controls). The most materially significant single open item across the register is Scenario 11 (landed cost after full sale), because it combines a version-behavior inconsistency, a reported case of a valuation change posting with no corresponding journal entry, and direct JT-04/JT-08 exposure — it is the clearest evidence in this register that reference-system behavior must not be silently carried into a SMEsPlus design.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
