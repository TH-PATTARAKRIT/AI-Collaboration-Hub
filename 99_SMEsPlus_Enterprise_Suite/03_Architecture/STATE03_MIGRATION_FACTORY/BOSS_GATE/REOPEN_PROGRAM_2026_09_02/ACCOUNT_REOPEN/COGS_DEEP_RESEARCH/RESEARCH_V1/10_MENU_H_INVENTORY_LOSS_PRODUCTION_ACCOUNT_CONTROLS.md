# 10 — MENU H — Inventory Loss / Production / Location Accounting Controls

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `EVIDENCE IN PROGRESS — CP-03 (Menu H) — three-layer evidence, no synthesis to Final Design`

---

## 0. Scope and Convention Binding

This file answers governing prompt §6 Menu H: where supported by the reference ERP version studied, inventory loss/shrinkage account behavior (scrap and its accounting), production/WIP cost account behavior, location-specific accounting controls, and the distinction between COGS and non-COGS inventory reductions **as the reference ERP itself models it** — not as SMEsPlus wishes it modeled. Where a control does not exist as a distinct reference-ERP concept, this file says so explicitly as `NOT PRESENT IN THIS VERSION`.

Inherits `CV-01`–`CV-06`: reference ERP never named by product; citation form `Reference ERP official documentation — <topic>, version <N>, retrieved 2026-09-02`; no vendor code tokens or fenced code blocks; three evidence layers kept separate; no final SMEsPlus design decision made here.

Joint decisions this file feeds (not closes): `JT-09` (work-in-progress recognition timing). Cross-references `TH-HOLD-02` (scrap, per file `01` §3.3/§3.4) and question-fingerprint row `8` (which stock decreases are not COGS) and row `14` (manufacturing RM/WIP/FG/COGS boundary) from file `01` §5.

---

## 1. Layer A — Location Types as the Reference ERP's Structural Control

The reference ERP models "where inventory is" as a typed location graph, and the **type** of a location is itself an accounting control point — not merely a physical/logical grouping. Seven location types are documented across the versions reviewed:

| Location Type | Documented purpose | Accounting relevance |
|---|---|---|
| `Vendor Location` | Origin point for goods purchased from a vendor; items here are not counted as company stock | Boundary of the inbound valuation event (receipt moves stock out of Vendor Location into an Internal Location) |
| `View` | Purely hierarchical/organizational; aggregates child locations; cannot directly hold stock | No accounting relevance — structural only |
| `Internal Location` | Physical storage within the company's warehouses | Stock here is counted in inventory valuation — this is the "Inventory Asset exists" zone |
| `Customer Location` | Destination for sold/delivered products; items here are no longer company stock | Boundary of the outbound valuation event (delivery moves stock out of Internal Location into Customer Location) |
| `Inventory Loss` | Counterpart location used to consume missing items or create stock to account for discrepancies; documented examples are "Inventory adjustment" (stock-count discrepancies) and "Scrap" (damaged goods) | This is the reference ERP's structural mechanism for **non-sale stock reduction** — see §2 |
| `Production` | Virtual location used for the manufacturing process | Raw materials are consumed from an Internal Location into Production; finished goods emerge from Production into an Internal Location — see §4 |
| `Transit Location` | Used when stock is in transit between warehouses (e.g., an inter-warehouse transit location) | Relevant to inter-company/inter-warehouse transfer valuation timing, not directly to loss/production |

`FACT STATUS: VERIFIED` — location type list and stated purposes are corroborated across multiple documentation-derived and cross-checked sources for versions spanning 12.0 through 19.0 with no observed change to the seven-type structure itself in this pass (see §7 for what *did* change).

**Structural finding directly answering the governing-prompt Menu H mandate**: the reference ERP does **not** have a single unified "shrinkage account" field independent of location typing. Instead, accounting behavior for loss is attached to the **Inventory Loss location's configuration** (its Loss Account), not to a global settings field. This is a materially different control shape than a single "Inventory Loss Account" setting under Accounting → Configuration → Settings, and must not be assumed to exist there — it does not, per evidence retrieved.

`NOT PRESENT IN THIS VERSION (all versions reviewed): a single global "Shrinkage Account" or "Inventory Loss Account" field at the company/settings level, distinct from the per-location Loss Account described in §2.`

---

## 2. Inventory Loss / Scrap — Accounting Mechanism

### 2.1 Configuration

A location must have its Location Type set to `Inventory Loss` to serve this role. For a location dedicated to scrap specifically, the documentation additionally requires marking it as a scrap location (a distinct checkbox/flag beyond the base `Inventory Loss` type in at least one version reviewed — 19.0 documentation describes "Is a Scrap Location?" as a required affirmative setting alongside `Location Type = Inventory Loss`) and assigning a **Loss Account** in that location's Accounting Information section.

`FACT STATUS: VERIFIED.` Reference ERP official documentation — Scrap inventory; Account for scrapped goods, version 19.0, retrieved 2026-09-02.

### 2.2 Posting mechanism

When a scrap operation moves stock into the Inventory Loss location: the account **debited** is the Loss Account configured on that Inventory Loss location (documented example label: "Scrapped Goods"); the account **credited** is the product's inventory asset (Stock Valuation) account, i.e. the same asset account structure established in file `09` for ordinary stock moves. This produces a direct expense recognition, reducing both physical quantity and asset value in a single event.

`FACT STATUS: VERIFIED.` Reference ERP official documentation — Account for scrapped goods, version 19.0, retrieved 2026-09-02.

### 2.3 Dependency on valuation method

This automatic posting is explicitly conditioned on **Automated/Perpetual** inventory valuation being active: *"real-time journal entries are created in the Accounting app whenever stock enters or leaves the company's warehouse"* under Perpetual, which is what makes the scrap event immediately financial-statement-visible. Under **Manual/Periodic** valuation, the documentation for this specific page does not describe an automatic entry; consistent with file `09`'s Periodic mechanics (value affected only at bill-posting/closing, not at physical movement), a scrap event under Periodic would not itself generate a journal entry — the loss would only surface indirectly at the next stock-closing as part of the computed stock variation, with no dedicated "scrap" line separable from ordinary usage/COGS at that point unless a manual closing adjustment specifically isolates it.

`FACT STATUS: VERIFIED` for the Perpetual/Automated behavior (directly quoted); `PROVISIONAL` for the Periodic/Manual inference — this is derived from file `09`'s established Periodic mechanics by direct logical extension, not from an independently retrieved Periodic-specific scrap worked example. Flagged for direct verification before being treated as settled.

### 2.4 Scrap vs COGS — explicit distinction as modeled

The reference documentation itself draws the distinction the governing prompt asks for: scrapped goods represent **inventory losses** (damage, spoilage, obsolescence) and are documented to appear as a **separate line item in the Profit & Loss report**, distinct from COGS, which reflects normal product sales. This is a structural, not merely presentational, distinction in the reference ERP: it flows from routing the debit to the Inventory-Loss-location's Loss Account rather than to the Expense/COGS account resolved from the Product/Category (file `05`). The reference ERP therefore models "COGS vs non-COGS inventory reduction" as a **function of which typed location the stock move terminates in**, not as a manually-tagged classification on an otherwise-identical transaction.

`FACT STATUS: VERIFIED.` Reference ERP official documentation — Account for scrapped goods, version 19.0, retrieved 2026-09-02. This is a materially important structural finding for the governing-prompt's absolute domain boundary ("not every inventory-value decrease is COGS") — the reference ERP independently arrives at the same principle via its location-type architecture, which is corroborating Layer A evidence for that boundary, not proof that SMEsPlus must adopt the same location-typing mechanism.

---

## 3. Other Non-COGS Reductions Modeled the Same Way

Because the mechanism in §2 is location-type-driven rather than transaction-type-driven, **every** Inventory-Loss-routed move shares the same posting shape (debit the location's configured Loss Account, credit Stock Valuation), differentiated only by which specific Inventory Loss location (and therefore which specific Loss Account) the move targets:

| Documented Inventory-Loss sub-case | Location example | Distinguishing feature |
|---|---|---|
| Inventory count discrepancy | "Inventory adjustment" location | Triggered by a physical count correction rather than a deliberate scrap decision; same Loss Account posting mechanism, different loss account may be configured |
| Damaged/obsolete goods | "Scrap" location | Requires the "Is a Scrap Location?" affirmative flag in addition to `Location Type = Inventory Loss` (19.0) |

The reference ERP does not appear, from evidence retrieved, to further subdivide "Inventory Loss" into a formally distinct taxonomy (e.g. a dedicated "write-down"/"impairment"/"abnormal loss" location type separate from generic adjustment/scrap). Any such finer Thai-statutory distinction (write-down vs abnormal loss vs normal shrinkage — see prompt §13) would have to be achieved either by configuring multiple distinct Inventory-Loss-typed locations each with its own Loss Account, or by a downstream manual reclassification — the reference ERP's own structure does not natively express that finer taxonomy as a first-class field.

`NOT PRESENT IN THIS VERSION (all versions reviewed): a distinct location type or field specifically labeled "Write-down," "Impairment," or "Abnormal Loss," separate from the generic Inventory Loss / Scrap / Inventory-adjustment structure described above.`

`FACT STATUS: VERIFIED` for the two documented sub-cases; `VERIFIED (absence)` for the NOT PRESENT finding, based on the location-type list in §1 being consistently seven types across all versions checked with no additional loss-subtype location documented.

---

## 4. Production / Work-in-Progress Accounting

### 4.1 Structural flow

Raw materials are consumed from an Internal Location into the `Production` virtual location when a manufacturing order proceeds; finished goods emerge from `Production` into an Internal Location on completion. This is the same location-typed-move architecture as §1–§3, applied to manufacturing rather than loss.

`FACT STATUS: VERIFIED.` Reference ERP official documentation — Locations; Inventory management, versions 17.0–19.0, retrieved 2026-09-02.

### 4.2 WIP account configuration

Two dedicated accounts are configured under Accounting → Configuration → Settings, Inventory Valuation section, Manufacturing subsection:

- **WIP Account** — tracks the value of work-in-progress goods (documented default label observed: "Work in Progress").
- **WIP Overhead Account** — tracks overhead costs allocated to WIP (documented default label observed: "Cost of Production").

`FACT STATUS: VERIFIED.` Reference ERP official documentation — Work-in-progress costs, version 19.0, retrieved 2026-09-02. Exact numeric GL codes cited in secondary material are **not** treated as authoritative defaults here (chart-of-accounts/localization-dependent) — see `HOLD` note in the field sheet, §6.

### 4.3 Posting trigger — manual, not automatic

Materially important finding: WIP journal entries are **not** created automatically as a byproduct of production activity. They require an explicit user action — posting a "WIP Accounting Entry" from the Manufacturing Order — and reflect costs "at the moment the entry is posted, based on what has already been consumed" (actual component consumption, actual work-center time, vs the Bill-of-Materials-planned figures). The system is documented to automatically schedule a **reversal** of that WIP entry for the next day, and a manual reversal path also exists. The stated purpose is that WIP postings are a **temporary period-spanning snapshot** — they must be returned to an empty/reversed state before being usable again in a subsequent posting cycle.

`FACT STATUS: VERIFIED.` Reference ERP official documentation — Work-in-progress costs, version 19.0, retrieved 2026-09-02.

This is directly relevant to `JT-09` (WIP recognition timing): the reference ERP's own answer is that WIP recognition is **not** a passive byproduct of the physical consumption event — it is a distinct, manually-triggered, auto-reversing accounting act layered on top of the physical Production-location move. A design that assumed WIP value "just appears" from the stock move alone would misrepresent the reference ERP's actual documented behavior.

### 4.4 Value flow to finished goods

The documented flow is: raw-material stock valuation account → WIP account (on consumption, when a WIP entry is posted) → finished-goods valuation account (on completion, coinciding with the WIP entry's scheduled/manual reversal). The retrieved documentation frames this at the outcome level; the precise treatment of labor/overhead absorption variance (planned-vs-actual gap when a WIP entry differs from the eventual finished-goods costing outcome) was not independently retrieved as a worked example in this pass.

`FACT STATUS: VERIFIED` for the outcome-level flow; `HOLD / EVIDENCE REQUIRED` for the labor/overhead variance treatment at completion — not established from evidence retrieved this pass. Routed to file `22` (Manufacturing RM/WIP/FG/COGS research).

### 4.5 WIP vs Periodic/Perpetual axis

The retrieved documentation locates the WIP/WIP-Overhead account fields inside the same Accounting → Configuration → Settings → Inventory Valuation surface used for the Stock Valuation/Variation accounts in file `09`, suggesting WIP is treated as a **manufacturing-specific extension of the same valuation-account framework**, not a wholly separate subsystem. Whether WIP posting availability/behavior differs materially between Continental/Periodic and Anglo-Saxon/Perpetual company configurations was **not independently confirmed** in the excerpts retrieved — the WIP documentation page fetched does not itself branch by accounting mode.

`FACT STATUS: HOLD / EVIDENCE REQUIRED` — WIP behavior under Periodic vs Perpetual configuration specifically is not established from evidence retrieved this pass. Routed to file `22`/`30`.

---

## 5. Location-Specific Accounting Controls — Beyond Loss and Production

### 5.1 Per-location Accounting Information

Both the `Inventory Loss` and (by documented pattern) other typed locations expose an "Accounting Information" configuration section on the location record itself, distinct from the Product-Category-level accounts studied in file `04`. This means the reference ERP supports **location-level** accounting overrides as a third inheritance dimension alongside Category (file `04`) and Product (file `05`) — a dimension the governing prompt's Menu B/C sections do not separately name but which Menu H surfaces directly.

`FACT STATUS: VERIFIED` for the Inventory Loss location case (directly documented); `PROVISIONAL` for generalizing "Accounting Information" as present on every location type — only the Inventory Loss case was independently confirmed with a quoted field in this pass.

### 5.2 Interaction with Category/Product resolution (open question)

The retrieved documentation does not resolve, for a stock move that is **not** loss/production/sale (e.g., a routine internal transfer between two ordinary Internal Locations, or an inter-warehouse Transit move), whether any location-level account ever overrides the Category/Product-resolved account, or whether ordinary Internal-Location-to-Internal-Location moves are simply non-value-affecting by default (most likely, since both ends are within the "counted as stock" boundary) and thus the question is moot for that case specifically. For Inventory-Loss and Production moves specifically, §2–§4 establish that the **location's own configuration**, not the Category/Product Expense account, governs the posting — a distinct precedence rule from the ordinary sale path in file `09`.

`FACT STATUS: VERIFIED` for the Loss/Production-specific precedence rule (location config governs, not Category/Product Expense account); `HOLD` for the general ordinary-internal-transfer case, which is likely non-value-affecting by default but was not independently confirmed with a quoted worked example in this pass.

---

## 6. Menu H Field Evidence Sheet

| Field | Requirement |
|---|---|
| Menu Path | Inventory → Configuration → Locations (location record, Location Type + Accounting Information section); Accounting → Configuration → Settings → Inventory Valuation → Manufacturing subsection (WIP accounts) |
| Field Label | "Location Type" (options: Vendor Location, View, Internal Location, Customer Location, Inventory Loss, Production, Transit Location); "Is a Scrap Location?"; "Loss Account"; "WIP Account"; "WIP Overhead Account" |
| Purpose | Location Type determines whether stock present there counts as company inventory and, for Inventory Loss specifically, routes the value of stock moved there to a configured non-COGS expense account rather than the Category/Product-resolved Expense account |
| Values / Options | Location Type: seven documented values (§1). Loss Account / WIP Account / WIP Overhead Account: any GL account of the appropriate type (Expense-type for Loss Account; documented example "Scrapped Goods"; WIP/WIP Overhead documented example labels "Work in Progress" / "Cost of Production") |
| Default | UNKNOWN for Loss Account (must be explicitly configured per location, no universal default found); WIP Account/WIP Overhead Account documentation cites example default labels, but this session does not treat a specific numeric GL code as an authoritative universal default — chart-of-accounts/localization-dependent |
| Visibility | Loss Account field visible on a location record only once Location Type = Inventory Loss; "Is a Scrap Location?" visible in that same context (19.0); WIP/WIP Overhead accounts visible in Settings regardless of company accounting-mode selection (mode-branching not confirmed — see §4.5) |
| Scope | Location record (Loss Account) = per-location, not per-company-global; WIP/WIP Overhead = company Settings level |
| Inherits From | Not inherited from Product Category or Product — this is an independent, location-keyed configuration axis (§5.1) |
| Override Precedence | For Inventory Loss / Production moves: location configuration wins over Category/Product Expense-account resolution (§2.4, §5.2). This is a distinct precedence path from the ordinary sale/purchase path documented in file `09`. |
| Transaction Consumer | Scrap operation (consumes Loss Account); Inventory adjustment posting to the Inventory-Loss-typed adjustment location (consumes that location's Loss Account); Manufacturing Order "Post WIP Accounting Entry" action (consumes WIP Account / WIP Overhead Account) |
| Periodic Behavior | Scrap/loss: no automatic entry under Manual/Periodic valuation (PROVISIONAL, §2.3); loss surfaces only indirectly in the period-end stock-variation computation, not as a separable scrap line, absent a manual isolating adjustment. WIP: posting mechanism itself (manual entry + scheduled reversal) is documented independent of Periodic/Perpetual company mode (§4.5, HOLD on mode-branching). |
| Perpetual Behavior | Scrap/loss: automatic real-time entry on the scrap move itself (VERIFIED, §2.3). WIP: same manual-entry-plus-reversal mechanism (§4.3); mode-branching not confirmed (§4.5, HOLD). |
| Account Type Impact | Loss Account = Expense (P&L, separate line from COGS per §2.4); WIP Account / WIP Overhead Account = documented as Asset-adjacent "Work in Progress" / cost-of-production concepts sitting inside the same Inventory Valuation settings surface as the Stock Valuation asset accounts in file `09` — precise account-type classification (Asset vs Expense) for WIP specifically was not independently re-confirmed by a quoted type label in this pass |
| Financial Statement Impact | Loss Account: P&L, distinct line from COGS. WIP Account: Balance Sheet during the open WIP window (asset-like presentation implied by "tracks the value of WIP goods"), reversing before the next cycle — HOLD on precise statement classification, see Account Type Impact row. |
| Change Impact | Changing which Loss Account a location points to is prospective only for future moves through that location — no evidence retrieved of retroactive restatement of historical scrap postings. Not independently confirmed with a quoted statement; treated as consistent-by-pattern with file `09`'s general "Change Impact" finding for account reassignment. |
| Version Delta | "Is a Scrap Location?" as an explicit required flag alongside `Location Type = Inventory Loss` is confirmed in 19.0 documentation; whether this flag existed identically in earlier versions (13.0–18.0) or scrap-location behavior was inferred solely from `Location Type = Inventory Loss` without a separate flag in those versions was **not independently re-checked per-version** in this pass | 
| Evidence | See per-section citations, §1–§5 above |
| Fact Status | Mixed — see VERIFIED / PROVISIONAL / HOLD markers embedded in each section above; no blank cells |

---

## 7. Version Delta Register (Menu H specific — feeds file `02`)

| Version boundary | What is confirmed to have changed or requires further check | Evidence |
|---|---|---|
| 13.0–18.0 → 19.0 | "Is a Scrap Location?" documented as an explicit required affirmative setting in 19.0, in addition to `Location Type = Inventory Loss`. Whether earlier versions required this as a separate field or treated `Inventory Loss` type alone (with a naming convention, e.g. a location literally named "Scrap") as sufficient was **not independently re-checked per version** in this pass. | Reference ERP official documentation — Scrap inventory, version 19.0, retrieved 2026-09-02; earlier-version pages not independently re-fetched for this specific field in this pass |
| Across all versions reviewed | The seven-type location model (§1) and the WIP Account/WIP Overhead Account manual-entry-plus-reversal mechanism (§4.2–4.3) show no documented structural change across the versions retrieved in this pass. This should not be read as proof of zero change — only as "no change was found in the excerpts retrieved." | Reference ERP official documentation — Locations; Work-in-progress costs, versions 17.0–19.0, retrieved 2026-09-02 |

`FACT STATUS: PROVISIONAL` on the "Is a Scrap Location?" version-origin question specifically — flagged as an open item rather than asserted as new-in-19.0 without earlier-version confirmation.

---

## 8. Layer B — Thai Accounting / Tax Evidence

Not independently researched in this file. Pointer only: see `24_THAI_ACCOUNTING_TAX_STATUTORY_EVIDENCE_REGISTER.md` for authoritative Thai treatment of abnormal loss / scrap / destroyed-inventory classification, and any statutory documentation-substantiation requirement (e.g. destruction witnessing, tax-authority notification) that a reference-ERP scrap posting alone would not satisfy. This file makes **no** Thai-authority claim, including no claim that the reference ERP's location-type-driven Loss-Account mechanism alone is sufficient evidence for a Thai-deductible loss.

`FACT STATUS: N/A — pointer only, per file `01` §5 routing (Layer B owned by file `24`); cross-reference `TH-HOLD-02` per file `01` §3.4.`

---

## 9. Layer C — SMEsPlus Candidate Semantics (CANDIDATE / HOLD only)

None of the following are final design.

| # | Layer A observation | Neutral business meaning | SMEsPlus candidate status |
|---|---|---|---|
| C-H1 | COGS vs non-COGS reduction is structurally determined by destination-location typing, not by a manual transaction-type tag (§2.4) | "Where stock physically goes determines its financial classification, as a structural property of the movement, not an afterthought classification" | `CANDIDATE` — directly supports the governing-prompt boundary rule ("not every inventory-value decrease is COGS"); the specific location-typing *mechanism* is Layer A implementation detail and is NOT proposed as SMEsPlus's literal architecture — only the underlying principle (destination determines classification) is offered as a candidate business rule |
| C-H2 | WIP recognition is a manual, auto-reversing, period-bounded act layered on the physical Production move, not an automatic byproduct of consumption (§4.3) | "Work-in-progress value is a deliberate accounting snapshot, not a continuous derivative of physical consumption" | `CANDIDATE` — directly feeds `JT-09`; offered as a business-meaning input to that Joint decision, not as a resolution of it |
| C-H3 | No finer statutory-grade loss taxonomy (write-down/impairment/abnormal-loss) exists as a first-class reference-ERP concept (§3) | "A Thai-statutory-grade loss classification, if required, would need to be built as an SMEsPlus-specific extension — it cannot be assumed to already exist in inherited reference behavior" | `HOLD` — explicitly requires Layer B (file 24) input before any candidate can be proposed; flagged, not designed, here |
| C-H4 | Location-level accounting override exists as a third inheritance axis (location, alongside Category and Product) (§5.1) | "Accounting resolution may need to consider more than Category/Product precedence — a movement's destination location can itself carry accounting authority" | `HOLD` — this is a materially new candidate input to the Product-Category-vs-Product precedence matrix (file `11`), which as scoped only covers Category/Product, not location; flagged for file `11` to explicitly acknowledge or explicitly exclude location as a third axis, rather than silently omitting it |

---

## 10. Special Team Notes (abbreviated — full register in file `29`)

- `S1 COGS/Financial Accounting`: confirms Menu H's structural finding (§2.4) as corroborating, not sufficient, evidence for the governing-prompt boundary rule; the reference ERP's mechanism does not by itself prove the boundary is correctly drawn for Thai/SMEsPlus purposes.
- `S3 Product Category & Product Accounting Configuration`: flags C-H4 (location as a third inheritance axis) directly to file `11`'s owning team — this was not anticipated by the Menu B/C-only framing of the precedence matrix as originally scoped.
- `S6 Returns/Adjustment/Scrap/Landed Cost`: primary consumer of §2–§3; notes the Periodic/Manual scrap-visibility gap (§2.3, PROVISIONAL) as needing direct verification before file `20` (Adjustment/Scrap/Loss/Write-down Classification) relies on it.
- `S7 Manufacturing Cost`: primary consumer of §4; flags §4.4 (labor/overhead variance at completion) and §4.5 (Periodic/Perpetual mode-branching for WIP) as the two open items file `22` must resolve or carry forward as HOLD.
- `S8 Thai Accounting/Tax/Audit Reality`: flags C-H3 as a direct question for file `24` — does Thai practice require a loss-classification granularity the reference ERP does not natively provide, and if so what substantiation standard applies.

---

## 11. Open HOLD / EVIDENCE REQUIRED Items From This File

1. Scrap/adjustment posting visibility (or lack thereof) under Manual/Periodic valuation specifically — currently inferred by extension from file `09`, not independently confirmed (§2.3).
2. Generalization of "Accounting Information" location-level override to location types beyond Inventory Loss (§5.1).
3. Precedence behavior for ordinary Internal-Location-to-Internal-Location transfers — most likely non-value-affecting by default, not independently confirmed (§5.2).
4. Labor/overhead absorption variance treatment at WIP-to-finished-goods completion (§4.4) — routed to file `22`.
5. Whether WIP posting/reversal mechanics branch by Periodic vs Perpetual company accounting mode (§4.5) — routed to file `22`/`30`.
6. Precise account-type classification (Asset vs Expense presentation) for the WIP Account specifically (§6, Account Type Impact row).
7. Version-origin of the "Is a Scrap Location?" explicit flag — confirmed for 19.0 only, not re-checked per version 13.0–18.0 (§7).
8. Whether SMEsPlus's Product-Category/Product precedence matrix (file `11`) must be extended to a third, location-keyed axis (C-H4) — flagged, not decided, here.

No item above is resolved by assumption. Each remains `HOLD / EVIDENCE REQUIRED` until independently re-verified.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
