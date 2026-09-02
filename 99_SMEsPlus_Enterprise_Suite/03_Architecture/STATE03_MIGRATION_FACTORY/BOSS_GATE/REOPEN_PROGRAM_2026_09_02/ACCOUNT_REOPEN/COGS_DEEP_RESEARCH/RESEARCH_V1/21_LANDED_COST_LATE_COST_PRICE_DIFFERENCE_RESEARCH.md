# 21 — Landed Cost, Late Cost, and Price Difference Research

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `EVIDENCE COLLECTION — CP-08` — Layer A observed and cross-checked against multiple reference-version documentation sources and reference-community discussion; several items remain `CONFLICTING` or `HOLD / EVIDENCE REQUIRED` rather than resolved.

---

## 1. Purpose and Scope

This file is the Accounting-side companion to the Inventory-side landed cost design already fixed in Inventory Final Solution v1.0 (`08_INVENTORY_VALUATION_LANDED_ANALYTIC_COST_V1.md`, rules `LC-01`–`LC-07`). That design is **not re-opened here**. This file's job, per governing prompt §12 and §10 items 9/10/11, is to prove, from Layer A reference-ERP evidence, **which account absorbs a landed cost or price-difference amount, when, and under what documented mechanism** — i.e., the financial-recognition side of a fact Inventory has already committed to emitting.

Directly answers scenarios:
- `#6` Vendor bill price differs from receipt/valuation basis
- `#7` / `#8` Purchase return before/after bill (touched, not exhausted — full treatment is file `19`'s scope)
- `#9` Landed cost before any sale
- `#10` Landed cost after partial sale
- `#11` Landed cost after full sale

Cross-references: `JT-08` (landed-cost eligibility and posting structure — Joint, not closed here), `LC-01`–`LC-07` (Inventory-side rules this file must not contradict), `TH-HOLD-03` (recoverable input VAT capitalization — Thai-HOLD, owned by file `24`).

---

## 2. Layer Discipline Statement

Per governing prompt §3, three layers are kept separate throughout this file:

- **Layer A** — Reference ERP observed/documented behavior (the reference ERP's public official documentation and its official-forum evidence, cited `Reference ERP official documentation — <topic>, version <N>, retrieved 2026-09-02`, versions checked: 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0).
- **Layer B** — Thai accounting/tax/statutory evidence. Not independently researched in this file; every Thai-facing statement below is `HOLD`, routed to file `24`.
- **Layer C** — SMEsPlus clean-room candidate semantics, derived only where Layer A is clear and does not require a Layer B answer to state.

No conclusion below merges Layer A observation with a Thai statutory claim.

---

## 3. Layer A — Landed Cost Mechanism as Documented

### 3.1 Configuration and eligibility (Menu A/B cross-reference)

| Item | Observed behavior | Evidence |
|---|---|---|
| Activation | A "Landed Costs" toggle exists under the Inventory settings' Valuation section; enabling it exposes a Default Journal field for landed-cost-generated entries. | Reference ERP official documentation — Landed costs, version 19.0, retrieved 2026-09-02 |
| Landed cost "product" | Must be a Service-type product with a "Is a Landed Cost" flag set on its Purchase tab, and a split method (Equal / By Quantity / By Current Cost / By Weight / By Volume). | Reference ERP official documentation — Landed costs, version 19.0, retrieved 2026-09-02 |
| **Costing-method eligibility gate** | The receiving Product Category must use **AVCO or FIFO** costing. Reference-community sources are consistent that Standard Price products are **not** the documented target of the Landed Costs feature — Standard Price divergences from bill price are instead handled through the separate Price Difference Account mechanism (§4). | Reference ERP official documentation — Landed costs, version 19.0, retrieved 2026-09-02; corroborated by reference-community forum discussion, "v16 Landed cost best practice", retrieved 2026-09-02 |
| Trigger | A landed-cost product line is added to a vendor bill against an already-received purchase order; the system marks it as a landed cost line, distinct from ordinary bill lines. | Reference ERP official documentation — Landed costs, version 19.0, retrieved 2026-09-02 |

**Layer C candidate note:** this eligibility gate is directionally consistent with `LC-06`/`JT-08` (eligibility is Joint, unresolved) but adds a concrete Layer A data point the Joint session should weigh: the reference system does not appear to define a documented Standard-Price landed-cost path at all — it routes that case through a structurally different mechanism (price difference / variance), not through landed cost allocation. This is evidence for the Joint session, not a SMEsPlus decision.

### 3.2 The Valuation Adjustments statement (maps to `LC-02`)

Once a landed cost record is created against a vendor bill line, the reference system presents a **Valuation Adjustments** tab with three documented columns before validation:

| Column | Observed meaning |
|---|---|
| Original Value | The receipt/PO-derived value already carried for the line |
| Additional Landed Cost | The apportioned landed-cost amount per the chosen split method |
| New Value | The sum — the resulting post-allocation value |

Source: Reference ERP official documentation — Landed costs, version 19.0, retrieved 2026-09-02.

**Layer C candidate note:** this three-column statement is structurally the same shape already fixed by `LC-02` (base amount, basis, resulting amount, shown before validation). No contradiction found. This is corroborating Layer A evidence for a rule Inventory already committed to — it does not extend or re-derive it.

### 3.3 Journal entries on validation — REFERENCE OBSERVATION / ACCOUNTING MEANING / THAI RULE STATUS / SMEPLUS CANDIDATE

**Archetype: Landed cost allocation (stock still on hand, full quantity)**

- `REFERENCE OBSERVATION`: Clicking Validate on the landed cost record posts a journal entry in the configured Default Journal. The entry increases the Stock Valuation account for the receiving product(s) and reduces/clears the landed-cost vendor-bill-linked amount, split per the chosen apportionment basis across the affected receipt lines. Each validation is independently viewable in Accounting → Journal Entries. Source: Reference ERP official documentation — Landed costs, version 19.0, retrieved 2026-09-02.
- `ACCOUNTING MEANING`: A capitalizable acquisition cost (freight, duty, insurance, handling) not known at original receipt time is added to the cost basis of inventory still recognized as an asset, consistent with the general principle that landed-cost elements are includable in inventory cost when incurred to bring inventory to its present location and condition and stock is still on hand to absorb them.
- `THAI RULE STATUS`: `HOLD` — file `24` owns the authoritative Thai evidence for which landed-cost elements (freight, duty, non-recoverable tax) are includible in inventory cost versus expensed directly.
- `SMEPLUS CANDIDATE / HOLD`: Candidate directional agreement with `LC-01`/`LC-02` (single allocation, shown arithmetic before validation). No SMEsPlus account codes or journal structure asserted, per governing prompt §12.

**Archetype: Landed cost after partial sale**

- `REFERENCE OBSERVATION`: Reference-community evidence (not confirmed in the primary documentation text retrieved) describes the reference system's Standard/AVCO landed-cost entry, when applied after part of the receipt quantity has already left stock, as splitting into multiple journal lines: a first pair that would capitalize the full additional cost to inventory, a second pair that reverses the portion attributable to the already-sold quantity out of inventory, and a third pair that reclassifies that reversed portion to a cost-of-goods-sold-type account — leaving the correct residual debit in inventory and the correct residual credit/expense recognition against goods no longer on hand. Source: reference-community forum discussion, "How do Landed Costs work if products are sold in the mean time?", retrieved 2026-09-02. **This mechanism is not independently confirmed against the primary documentation pages retrieved in this session; it is treated as `PROVISIONAL`, not `VERIFIED`.**
- `ACCOUNTING MEANING`: The residual cost attributable to units no longer in inventory cannot be capitalized (there is no asset left to attach it to) and must be expensed through the period's cost-of-goods-sold-type recognition instead, split proportionally between the quantity still on hand and the quantity already released.
- `THAI RULE STATUS`: `HOLD`.
- `SMEPLUS CANDIDATE / HOLD`: This is direct, if provisional, Layer A corroboration of `LC-03` ("where the goods have already been sold, the system says so explicitly and routes the residual to Accounting; it never silently adjusts a cost basis with no stock behind it"). The reference mechanism's multi-line split (inventory portion vs. expensed portion) is offered as one worked precedent for how a system can implement `LC-03` without inventing a phantom cost basis — not as the SMEsPlus target design, which remains `HOLD` pending `JT-08`.

**Archetype: Landed cost after full sale**

- `REFERENCE OBSERVATION`: Where the entire receipt quantity has already been sold before the landed-cost bill/allocation is processed, reference-community evidence states the full additional cost "will be booked to COGS instead" of inventory, because there is no remaining stock to capitalize it against. A separate, more recent reference-community note (attributed to behavior from version 19.0 forward) states that this case now requires a **manually generated entry** for products sold prior to the landed cost being applied, and recommends routing the unallocated amount through a dedicated **Landed Cost Clearing account** for month-end reconciliation rather than posting it automatically straight to a cost-of-goods-sold account. Source: reference-community forum discussion, "How do Landed Costs work if products are sold in the mean time?", retrieved 2026-09-02. **`CONFLICTING`: the "auto-books to COGS" description and the "19.0+ needs a manual entry via a clearing account" description are not the same mechanism and were not reconciled against the primary version-19.0 documentation page in this session — both are retained as reported, neither is asserted as the current documented behavior without further evidence.**
- `ACCOUNTING MEANING`: Once no inventory asset remains behind a cost element, that cost element cannot be an asset — it must be an expense of the period in which the cost becomes known (a cost-of-goods-sold-type or clearing-account expense), never a stock-value increase with nothing behind it.
- `THAI RULE STATUS`: `HOLD`.
- `SMEPLUS CANDIDATE / HOLD`: Strong Layer A corroboration for `LC-03`'s "never silently adjusts a cost basis with no stock behind it" clause specifically. The open question this raises for the Joint session (`JT-08`) is **whether the residual should post automatically to a COGS-type account, or whether it should land in an intermediate clearing/suspense account requiring an approval step before final classification** — the reference evidence itself is split on this point across versions/sources, so SMEsPlus should not assume either answer. `HOLD / EVIDENCE REQUIRED` for the posting mechanism; `LC-03`'s behavioral principle (residual routed to Accounting, not silently absorbed into a phantom cost basis) is the only piece treated as reasonably corroborated.

### 3.4 Late supplier bill after period close

- `REFERENCE OBSERVATION`: The retrieved documentation and forum evidence describe the landed-cost bill/vendor-bill flow as date-driven (posted as of the bill/landed-cost validation date) with no explicit, version-specific statement found in this session's research describing a hard block on posting a landed cost against a prior, closed accounting period. No page retrieved in this session documents an override/back-dating control specific to landed costs. `NOT FOUND / HOLD`.
- `ACCOUNTING MEANING`: In the absence of a documented period-lock interaction specific to landed costs, the general accounting-period-lock mechanism (where it exists in the reference system) would be expected to govern whether a late-dated landed cost entry can post into a closed period at all, or must be re-dated into the current open period — but this session did not independently verify that general period-lock behavior's interaction with landed cost specifically.
- `THAI RULE STATUS`: `HOLD` — file `24`'s scope (period cut-off and physical stock evidence).
- `SMEPLUS CANDIDATE / HOLD`: No contradiction of `LC-05` ("allocation is subject to the period guard") found, but no independent Layer A confirmation of the mechanism either. `HOLD / EVIDENCE REQUIRED`. Flagged for a follow-up targeted research pass (file `08`/`23` territory) rather than resolved here.

---

## 4. Layer A — Price Difference Account Under Standard Price Costing

### 4.1 What the account is documented to capture

| Item | Observed behavior | Evidence |
|---|---|---|
| Field location | A "Price Difference Account" field is configured on the Product Category (visible when Standard Price costing applies), with documented help text to the effect of "used to value price difference between purchase price and accounting cost." | Reference ERP official documentation — Automatic inventory valuation, version 18.0, retrieved 2026-09-02; reference-community forum discussion on purchase-price-variance account setup, retrieved 2026-09-02 |
| Trigger | When a vendor bill's invoiced unit price differs from the product's fixed Standard Price, the reference system books the receipt/interim clearing at standard cost and routes the delta (invoice price − standard cost) to this account at bill-validation time. | Reference ERP official documentation — Automatic inventory valuation, version 18.0, retrieved 2026-09-02 |
| Account type | Reference-community evidence describes this account as configured as an Expense-type account in worked examples, though the primary documentation text retrieved does not state a mandatory account type. `PROVISIONAL`, not `VERIFIED`, on account type. | reference-community forum discussion on purchase-price-variance account setup, retrieved 2026-09-02 |
| Worked mechanics | Example pattern repeatedly observed across sources: Inventory/interim account debited/credited at standard cost; Accounts Payable credited at actual invoiced cost; the Price Difference Account absorbs the arithmetic difference so the entry balances without disturbing the standard-cost figure carried in stock. | Reference ERP official documentation — Automatic inventory valuation, version 18.0, retrieved 2026-09-02 |

### 4.2 REFERENCE OBSERVATION / ACCOUNTING MEANING / THAI RULE STATUS / SMEPLUS CANDIDATE

**Archetype: Purchase price variance under Standard Price**

- `REFERENCE OBSERVATION`: A vendor bill priced above or below the product's fixed standard cost posts the arithmetic difference to the category-level Price Difference Account at bill-validation time; the stock valuation figure itself is not disturbed — it remains at standard cost. Source: Reference ERP official documentation — Automatic inventory valuation, version 18.0, retrieved 2026-09-02.
- `ACCOUNTING MEANING`: This is a **variance recognition**, not a cost-basis edit — it is the accounting expression of `LC-04` ("where a product's policy uses a fixed planned cost, applying landed cost must be handled as a variance question, not as a cost-basis edit... otherwise the standard is no longer a standard"). The reference system's Price Difference Account is one documented implementation pattern of exactly the principle Inventory already fixed as `LC-04`, applied to ordinary purchase-price variance rather than to landed cost specifically — but the underlying accounting logic (a fixed planned cost must not silently move) is the same.
- `THAI RULE STATUS`: `HOLD` — no authoritative Thai source checked in this file for standard-costing variance presentation; routed to file `24`.
- `SMEPLUS CANDIDATE / HOLD`: Strong corroboration of `LC-04`'s stated principle from an independent reference mechanism. Whether SMEsPlus adopts a category-level variance account, a different account granularity, or a different variance-clearing cadence remains `HOLD` — this file records the *principle* as corroborated, not any specific account structure.

**Archetype: Standard-Price landed cost — the eligibility gap**

- `REFERENCE OBSERVATION`: Because the documented Landed Costs feature's eligibility is gated to AVCO/FIFO product categories (§3.1), a Standard-Price product's late freight/duty bill does not appear to flow through the Valuation Adjustments mechanism at all in the primary documentation retrieved — it would instead surface as an ordinary vendor-bill line, itself subject to the Price Difference Account logic if it is priced against a PO/standard expectation, or as a plain expense if it is not tied to a receipt line at all. `NOT FOUND / HOLD` — no page retrieved in this session explicitly walks through a worked example of applying a landed-cost-shaped bill (freight/duty/insurance) to a Standard-Price product.
- `ACCOUNTING MEANING`: If confirmed, this would mean the reference system treats "landed cost" and "purchase price variance" as two structurally separate mechanisms that are not documented to compose for Standard-Price products — a material gap for any Thai SME importer using standard costing with freight/duty bills that arrive separately from the goods invoice.
- `THAI RULE STATUS`: `HOLD`.
- `SMEPLUS CANDIDATE / HOLD`: `HOLD / EVIDENCE REQUIRED`, and flagged as a **material open question for `JT-08`**: SMEsPlus's landed-cost eligibility decision must explicitly decide whether Standard-Price products can receive landed cost at all, and if so, whether it is treated as a cost-basis capitalization (contradicting `LC-04`'s "not a cost-basis edit" principle for standard-cost policies) or purely as a variance (consistent with `LC-04`, but then the "landed cost" language becomes potentially misleading for a standard-cost product). This is not resolved by reference evidence and must not be assumed either way.

### 4.3 A second, later-version account observed — "Variation Account" (version 19.0)

- `REFERENCE OBSERVATION`: Reference-community forum evidence for version 19.0 distinguishes a **Variation Account** ("new in [version] 19") from the category-level Price Difference Account, describing a worked example where a $100 purchase posts to an Expense account and a $10 standard-cost difference posts to the Variation account, with an explicit statement that "you use one or the other, never both at the same time." This was not independently corroborated against the primary version-19.0 product-category documentation page in this session. `CONFLICTING / PROVISIONAL` — retained as reported, not verified as current documented behavior, and not reconciled with the "Price Difference Account" terminology used elsewhere in the same version's documentation set.
- `ACCOUNTING MEANING`: If accurate, this would be a second, version-specific variance-capture mechanism layered onto (or replacing, in some configurations) the long-standing Price Difference Account, which would itself be a material version-delta fact.
- `THAI RULE STATUS`: `HOLD`.
- `SMEPLUS CANDIDATE / HOLD`: `HOLD / EVIDENCE REQUIRED`. Recorded here only so a future targeted pass does not silently miss this thread; not treated as settled Layer A fact given the internal source conflict.

---

## 5. Purchase Return Interaction (Scenario 7/8 — Touched Only)

- `REFERENCE OBSERVATION`: No page retrieved in this session's targeted research for this file documents a specific landed-cost-return or price-difference-return worked example. General reference-system return handling (a reversing stock move against the original receipt) is described elsewhere in the reference ERP's documentation set but was not the target of this file's research pass. `NOT FOUND / HOLD` for the landed-cost/price-difference-specific return interaction.
- `ACCOUNTING MEANING`: Not derivable without evidence.
- `THAI RULE STATUS`: `HOLD`.
- `SMEPLUS CANDIDATE / HOLD`: `HOLD / EVIDENCE REQUIRED`. Full purchase-return cost-basis treatment (including whether an already-applied landed cost or price difference travels with a return) is explicitly assigned to file `19` (Return/Reversal Original Cost Linkage) per the governing prompt's file list; this file records only that the landed-cost/price-difference angle of a return was not exhausted here and must be picked up there, not silently dropped.

---

## 6. Reconciliation Identity Challenge (governing prompt §14, scoped to this file)

`Inventory Value = Opening + Capitalizable Cost Added − Cost Released ± Approved Valuation Adjustments`

- **Candidate application to landed cost before sale**: "Capitalizable Cost Added" includes the landed-cost allocation amount, in full, when stock is still on hand — `CANDIDATE`, evidence-supported (§3.3).
- **Candidate application to landed cost after partial/full sale**: the identity only holds if the portion attributable to already-released stock is excluded from "Capitalizable Cost Added" and instead recognized directly as an expense/COGS-type item in the period — `CANDIDATE`, provisionally evidence-supported (§3.3), but the exact posting mechanism for the excluded portion remains `HOLD` per §3.3's `CONFLICTING` note.
- **Candidate application to Standard Price variance**: purchase-price variance under Standard Price is explicitly *not* part of "Capitalizable Cost Added" under this identity — it bypasses the inventory value roll-forward entirely and posts to a variance account instead, which is the accounting expression of why `LC-04` treats it as a variance question rather than a cost-basis edit — `CANDIDATE`, evidence-supported (§4.2).

No identity above is declared `VERIFIED`; all remain `CANDIDATE` pending Joint review, consistent with governing prompt §14's requirement that these identities be tested, not assumed.

---

## 7. Version Delta Register Entries (this file's scope only)

| Delta ID | Observation | Versions | Status |
|---|---|---|---|
| `VD-LC-01` | Landed Costs feature present with substantially the same Valuation Adjustments statement (Original/Additional/New Value) from version 14.0 through 19.0; menu path relocates within the Inventory app's settings/valuation hierarchy across versions but the mechanism is stable. | 14.0–19.0 | `VERIFIED` (menu path relocation), `PROVISIONAL` (mechanism stability — not independently re-verified page-by-page for every intermediate version in this session) |
| `VD-LC-02` | A version-19.0-attributed source reports a new manual-entry requirement plus a "Landed Cost Clearing account" recommendation for goods sold before landed cost is applied, differing from the older "auto-books to COGS" description found for earlier versions. | 19.0 vs. pre-19.0 | `CONFLICTING` — not reconciled against primary documentation text; see §3.3 |
| `VD-LC-03` | Reference-community evidence describes a version-19.0 "Variation Account" as distinct from the long-standing Price Difference Account. | 19.0 | `CONFLICTING / PROVISIONAL` — see §4.3 |
| `VD-LC-04` | The reference system's valuation-timing terminology itself changed from "Automated (real-time)" / "Manual" (pre-19.0 framing) to "Perpetual (at invoicing)" / "Periodic (at closing)" (19.0 framing), and the documented trigger point for Perpetual valuation is reported to have moved from "posts at each stock movement" (pre-19.0) to "posts at the invoice/bill level" (19.0). This does not change this file's landed-cost/price-difference conclusions directly, but it changes the timing context in which a late bill or landed cost arrives relative to when Inventory Value was already updated, and is material to `JT-04`/`JT-06`. Flagged here for the files that own that boundary (`12`, `13`, `18`). | 19.0 vs. pre-19.0 | `PROVISIONAL` — reported by secondary sources, not independently confirmed against primary documentation text in this session |

---

## 8. Section 15 (9 Veto) Pre-Flags Relevant to This File

Not a full Veto run (owned by file `28`), but flagged here so file `28` does not have to re-derive it:

- **Financial/Accounting/Tax VETO pre-flag**: §4.2's "Standard-Price landed cost eligibility gap" and §3.3's `CONFLICTING` posting-mechanism finding for full-sale landed cost are both material enough to block a Joint `JT-08` decision until independently re-verified against primary documentation, not secondary/forum sources alone.
- **AI Control/Human Oversight VETO pre-flag**: no journal entry, account code, or cost figure was invented anywhere in this file; every numeric example ($100/$10, "half sold") is quoted from the cited source as an illustrative worked example, not asserted as a SMEsPlus figure.
- **Clean-Room/IP/Provenance VETO pre-flag**: no vendor/product name, code token, table/field identifier, or fenced code block appears in this file, consistent with the clean-room rules; all citations use the `CV-02` neutral citation form.

---

## 9. Summary Table — SMEsPlus Candidate / HOLD Status

| # | Item | Status |
|---|---|---|
| 1 | Landed-cost allocation before any sale capitalizes fully to inventory | `CANDIDATE` (Layer A corroborated) |
| 2 | Landed-cost residual for already-sold stock must not silently create a phantom cost basis (`LC-03`) | `CANDIDATE` (Layer A corroborated, principle only) |
| 3 | Exact posting mechanism for the sold-stock residual (direct-to-COGS vs. clearing account) | `HOLD / EVIDENCE REQUIRED` — sources conflict |
| 4 | Standard-Price purchase-price variance is a variance, not a cost-basis edit (`LC-04`) | `CANDIDATE` (Layer A corroborated) |
| 5 | Whether Standard-Price products can receive landed cost at all, and how | `HOLD / EVIDENCE REQUIRED` — material open question for `JT-08` |
| 6 | Existence/behavior of a distinct "Variation Account" alongside Price Difference Account | `HOLD / EVIDENCE REQUIRED` — internally conflicting sources |
| 7 | Late-bill period-lock interaction specific to landed cost | `NOT FOUND / HOLD` |
| 8 | Purchase-return interaction with landed cost/price difference | `NOT FOUND / HOLD` — deferred to file `19` |
| 9 | Recoverable input VAT within landed cost | `HOLD` — `TH-HOLD-03`, file `24` owns |

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
