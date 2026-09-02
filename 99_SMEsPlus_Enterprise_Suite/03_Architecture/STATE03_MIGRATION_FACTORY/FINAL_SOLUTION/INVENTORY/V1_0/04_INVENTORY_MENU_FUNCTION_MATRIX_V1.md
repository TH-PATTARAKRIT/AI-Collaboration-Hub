# 04 — Inventory Menu / Function Matrix v1.0 (29 Menus)

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V1-001` | Jira: `ERPPLUS-139`
Status: `SMEsPlus-OWNED MENU DESIGN — ALL 29 COVERED — NOT APPROVED UI, NOT APPROVED SCHEMA`
Clean-room: Layer 1. Every block below is SMEsPlus-owned design intent, not a description of any reference ERP's menu. No vendor name, code, model, field, method, schema or markup appears.

**Reading rule.** Every one of the 29 functions is written under exactly five headings: **Purpose / Input / Process / Output / Accounting-Control Impact**. Each block also carries its Thai SME classification, its candidate Thai name, and its evidence status. Every Thai name in this file is `UNVALIDATED - THAI USER REVIEW REQUIRED`. Blocks whose underlying evidence is thin carry an explicit SMEsPlus design hypothesis and are labelled `UNVALIDATED - THAI USER REVIEW REQUIRED` in full; none is left blank.

Classification vocabulary: `MANDATORY` = every stock-keeping Thai SME needs it from day one; `CONDITIONAL` = platform capability always present, tenant visibility switchable; `SYSTEM FUNCTION` = required behaviour with no end-user menu.

---

## A. OPERATIONS

### A1. Replenishment — `MENU-OP-01`
Thai candidate: **เติมสินค้า / แผนเติมสินค้า** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `CONDITIONAL` (core for trading and manufacturing; hidden for micro-retail)

**Purpose.** Decide what to buy, make or move *before* stock runs out, from stated rules rather than from a person's memory.

**Input.** Reorder rules (minimum, maximum, source template, planning horizon) per product and place; the forecast position built from on-hand plus confirmed incoming minus confirmed outgoing; manual additions a buyer types in; supplier lead times.

**Process.** The planning run computes the shortfall for every active rule; each shortfall becomes a proposal carrying its own explanation ("below minimum of 50, forecast 12 on 15 Sep"); a buyer reviews, edits quantity or supplier, and confirms; confirmation hands the proposal to the owning domain, which creates the purchase order, manufacturing order or internal transfer. Rejected proposals are recorded with a reason, not silently discarded.

**Output.** A prioritised proposal list; the source documents created on confirmation; one explanation per proposal; a rejection record for what was declined.

**Accounting-Control Impact.** None until goods are received — a proposal changes no quantity and no value. Controls: confirming a proposal is *not* purchase-order approval and must not stand in for it; automatically generated drafts can never self-approve; every planning run is logged; duplicate proposals from a retried run are prevented by the demand identity rule (`C-02`, Boss decision).

---

### A2. Inventory Adjustments — `MENU-OP-02`
Thai candidate: **ปรับปรุงยอดสต็อก** (count sub-flow: **นับสต็อก**) `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `MANDATORY`

**Purpose.** Make the system quantity equal the physical quantity, with an approved and documented reason — the only sanctioned route by which a stock number changes without a physical movement of goods.

**Input.** A count session (scope, date, counters, freeze policy) or a direct correction request; counted quantities per product, place and lot; a mandatory reason code; supporting evidence; the approver's decision.

**Process.** Plan the count and choose its scope → apply the freeze policy for the counted area → count, on paper or by scan → compare counted against system → recount every discrepancy above the recount threshold → submit for approval with reasons → on approval, apply each difference as a movement between the counted place and the adjustment counterpart → publish the adjustment register entry.

**Output.** Corrected on-hand; a count sheet with counter, date and signature; an adjustment register showing quantity delta, reason, approver and value; a valuation delta fact for Accounting.

**Accounting-Control Impact.** Quantity delta valued at cost becomes an inventory gain or loss fact that Accounting posts; Inventory does not choose the account. Controls: counter ≠ approver; reason code mandatory; value threshold escalation; period guard refuses a backdated adjustment into a closed period except through a recorded exception; applied adjustments are immutable and reversed rather than edited. Open: which of several freeze policies Thai SMEs can actually operate is `UNVALIDATED - THAI USER REVIEW REQUIRED`; the year-end witnessed-count requirement is `HOLD / EVIDENCE REQUIRED` and routed to the Accounting-Tax track.

---

### A3. Transfers — `MENU-OP-03`
Thai candidates: **รับสินค้าเข้า / จ่ายสินค้าออก / โอนย้ายภายใน**, umbrella **รายการเคลื่อนย้ายสินค้า** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `MANDATORY`

**Purpose.** Record every physical movement of goods exactly once, against the document that caused it. This is the single source of stock truth in SMEsPlus.

**Input.** Purchase order lines, sales order lines, manufacturing order lines, internal transfer requests, return requests; the physical goods themselves; lot or serial values where tracked; the operator's confirmed quantities.

**Process.** A document is created from the source order (or manually) → stock is reserved according to the reservation policy → the operator receives or picks, scanning or entering lots where tracked → partial fulfilment triggers an explicit backorder decision rather than a silent one → the operator validates → immutable movement facts are emitted → downstream domains are notified. Returns run the same path in the opposite direction with an explicit return reason. Cancellation before validation releases reservations and cancels the chain; the symmetry of cancellation between the sales and purchase sides is a carried conflict (`C-01`).

**Output.** A validated receipt, delivery, internal transfer or return document; updated on-hand per place; movement facts; backorder documents where quantities were short; lot history entries.

**Accounting-Control Impact.** A receipt brings stock across the ownership boundary and emits a receipt valuation fact; a delivery emits a cost-of-goods-sold fact; a return emits a reversing fact whose cost basis is a carried conflict (`C-03`); an internal transfer emits nothing. Controls: the validator must differ from the order approver; the period guard applies to the movement date; over-receipt beyond tolerance requires approval, and the tolerance policy itself is an open item; a validated document cannot be re-validated (duplicate protection); goods left in transit must be visible and aged. The timing of cost-of-goods-sold recognition — at delivery or at invoice — is a Joint Accounting ↔ Inventory decision, not settled here.

---

### A4. Scrap — `MENU-OP-04`
Thai candidate: **ตัดสินค้าชำรุด/สูญเสีย** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `MANDATORY`

**Purpose.** Remove stock that can no longer be sold or used, with approval, a reason, and an auditable loss record — so that the books stop carrying value that no longer exists.

**Input.** A scrap request naming product, lot or serial, quantity, place, reason (damaged / expired / lost / disposed under procedure), supporting evidence such as photographs or an inspection note, and the approver.

**Process.** Damage, expiry or loss is identified → a request is raised → approval is obtained, escalating by value, and where a formal destruction procedure applies a witness is recorded → the goods move from their internal place to the loss counterpart → physical disposal is recorded → the scrap register entry is published with its evidence pack.

**Output.** Reduced on-hand and reduced lot balance; a scrap register entry; a loss valuation fact; a destruction evidence pack where one was required.

**Accounting-Control Impact.** Quantity valued at cost becomes a loss fact for Accounting to post. Controls: requester ≠ approver; reason mandatory; value escalation; witness for formal destruction; period guard. **The deductibility of scrapped stock for Thai tax purposes, and the procedure and evidence a Thai authority requires for destruction, are `HOLD / EVIDENCE REQUIRED` and routed to the Accounting-Tax track.** This session makes no statutory claim. Open: whether a distinct damaged-goods holding state is needed before scrap, or whether a quarantine location suffices, is carried as `RISK-U02`.

---

### A5. Landed Costs — `MENU-OP-05`
Thai candidate: **ต้นทุนสินค้าเพิ่มเติม / ต้นทุนนำเข้า** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `CONDITIONAL` (mandatory for importers; hidden for domestic-only SMEs)
Evidence status: thin in the prior chain — the block below is this session's SMEsPlus design hypothesis, `UNVALIDATED - THAI USER REVIEW REQUIRED`.

**Purpose.** Add freight, duty, insurance, broker and handling charges to the cost of the goods they relate to, so that margin and stock value reflect what the goods actually cost to land in the warehouse.

**Input.** Additional-cost bills supplied by Accounting with their cost types; the target receipt documents; the allocation basis (by value, by quantity, by weight, by volume, or explicitly per line); the effective date.

**Process.** Select the receipts the cost relates to → enter cost lines by type and amount → choose an allocation basis per cost line → the system computes the allocation per receipt line and shows it for review → the user validates → the cost basis of the affected receipt lines is increased and a value-change fact is emitted. Where the goods have already been sold, the design requires the system to say so explicitly and route the residual to Accounting rather than silently adjusting a cost basis that no longer has stock behind it.

**Output.** An allocation statement showing base amount, basis, and the amount landed on each receipt line; the adjusted cost basis; a value-change fact per affected line.

**Accounting-Control Impact.** Value-only — no quantity moves. Accounting posts the value change and owns the account mapping for each cost type. Which products are eligible (for example, whether a standard-cost product may receive landed cost at all) and how the posting is structured are **Joint Accounting ↔ Inventory decisions and are not settled here**. Controls: Accounting approval; period guard; a receipt line may not be double-allocated for the same cost bill. **Thai import duty and import VAT treatment is `HOLD / EVIDENCE REQUIRED`, routed to the Accounting-Tax track** — in particular whether recoverable input VAT must be excluded from landed cost is a statutory question this session does not answer.

---

### A6. Run Scheduler — `MENU-OP-06`
Thai candidate: **ประมวลผลแผนสต็อก** (admin status view: **สถานะการประมวลผลอัตโนมัติ**) `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `SYSTEM FUNCTION` — not an end-user menu; required as a background function with an administrator-visible run log

**Purpose.** Make planning happen reliably without anyone remembering to trigger it: refresh forecasts, generate replenishment proposals, resolve reservations, and extend movement chains.

**Input.** All active reorder rules, all pending demand, all flow templates, the tenant's planning calendar.

**Process.** A deterministic batch runs per company and warehouse on a schedule, and may also be triggered manually by an administrator. Each run records what it examined, what it created, what it skipped and why, and any error. Re-running the same window must not duplicate anything already created.

**Output.** Replenishment proposals and draft documents; reservation state changes; a run log with counts, durations and errors.

**Accounting-Control Impact.** None — the run never changes on-hand and never emits a valuation fact. Controls: the run is idempotent by demand identity; it can never create a *done* movement, only planned work; every run is logged, including runs that produced nothing; silent failure is itself an alertable condition; any anomaly detection is advisory only and may never take an action on its own. Carried: `C-02` idempotency severity is a Boss decision.

---

## B. PRODUCTS

### B1. Products — `MENU-PR-01`
Thai candidate: **สินค้า / ข้อมูลสินค้า** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `MANDATORY`

**Purpose.** Hold one agreed identity per item the business trades, so that purchasing, selling, warehousing and accounting all mean the same thing by the same name.

**Input.** Thai and English names; internal code; barcode; product kind (สินค้าคงคลัง / วัสดุสิ้นเปลือง / บริการ, all unvalidated); category; base unit and unit group; tracking mode; expiry policy; reorder defaults; tax defaults supplied by Accounting; supplier references; legacy identifiers at migration.

**Process.** Create the product → generate variants where the model has options → set stock, tracking and costing-relevant policies → activate. Changes to kind, base unit or category after stock exists are controlled, approved and logged. Products are archived, never deleted, and archiving is refused while stock or open documents exist.

**Output.** The product master consumed by every other domain; a variant grid where applicable; a full change history.

**Accounting-Control Impact.** Product kind determines whether stock truth and valuation apply at all; category is the current candidate owner of valuation policy; tax defaults are Accounting-owned and Inventory only carries them. Controls: duplicate-code and duplicate-barcode prevention; kind change with existing stock requires approval and a stated treatment for the existing balance; every cost-relevant field change is logged. Open: the tie-break rule when the kind derivation is ambiguous (`GAP-FS-04`); the correlation between product kind and Thai withholding-tax applicability is `HOLD / EVIDENCE REQUIRED`, routed to the Accounting-Tax track.

---

### B2. Product Variants — `MENU-PR-02`
Thai candidate: **สินค้าย่อย / ตัวเลือกสินค้า** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `CONDITIONAL` (apparel, footwear, cosmetics, spare parts)
Evidence status: no dedicated variant evidence exists in the prior chain — the block below is this session's SMEsPlus design hypothesis, `UNVALIDATED - THAI USER REVIEW REQUIRED`.

**Purpose.** Let a business manage one model while counting, costing and selling stock per option — colour, size, capacity — without creating an unmanageable list of unrelated products.

**Input.** The parent product, the attributes that vary it, the values in play, and the generation mode (all combinations, or a selected subset).

**Process.** Selected combinations generate variants; each variant receives its own code and barcode; unused combinations may be pruned before activation; new values added later extend the grid without disturbing existing variant identity.

**Output.** A variant grid; stock, cost and availability per variant; a variant-to-legacy-identifier map at migration.

**Accounting-Control Impact.** Stock truth and valuation are held at variant level, not at model level; reporting rolls up to the model. Controls: variant identity is the combination of stable attribute-*value codes*, so a renamed display label never breaks history; a variant holding stock or history cannot be deleted, only archived; combinatorial explosion is guarded by requiring explicit generation rather than defaulting to every combination.

---

### B3. Lots / Serial Numbers — `MENU-PR-03`
Thai candidate: **เลขล็อต / เลขซีเรียล** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `CONDITIONAL` as a menu, `MANDATORY` as platform capability (food, pharmaceutical, cosmetics, electronics, warranty goods)

**Purpose.** Know which specific batch or unit is where, so that a recall can be executed, an expiry can be enforced, and a warranty claim can be verified.

**Input.** The product's tracking mode; lot or serial values captured at receipt or production; expiry and manufacture dates where the product has an expiry policy; supplier batch references.

**Process.** Values are assigned or scanned on receipt → on issue the system proposes oldest-expiry-first where expiry is tracked and oldest-received-first otherwise, with an override that requires a reason → every movement records the lot or serial → traceability queries run in both directions, from batch to customers and from customer back to supplier.

**Output.** A lot and serial master; per-lot balances; movement history per lot; an expiry watch list; a recall query result set.

**Accounting-Control Impact.** No direct valuation effect in the general case; where costing is tracked per lot, the lot becomes the cost carrier. Controls: serial uniqueness per product per company must be enforced at the data layer rather than detected afterwards; a lot value becomes immutable after its first movement; shipping an expired lot is blocked unless explicitly overridden with a reason and an approver. Open: the depth of the expiry workflow (alert horizons, automatic blocking, disposal linkage) was never studied and is `UNVALIDATED - THAI USER REVIEW REQUIRED`. Sector-specific Thai traceability obligations for food and pharmaceutical goods are `HOLD / EVIDENCE REQUIRED`, routed to the Accounting-Tax track for onward legal routing.

---

## C. REPORTING

### C1. Stock — `MENU-RP-01`
Thai candidate: **ยอดสินค้าคงเหลือ** (คงเหลือจริง / จองแล้ว / พร้อมใช้) `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `MANDATORY`

**Purpose.** Answer, at a glance, what the business physically has, what is already promised, and what can still be sold.

**Input.** Done movement facts; reservations; confirmed incoming and outgoing quantities.

**Process.** Aggregate done movements per product (and per variant, lot, place as requested); subtract reservations to give available; show the forecast position separately from the physical position.

**Output.** Four clearly separated quantities — on hand, reserved, available, forecast — per product, filterable by warehouse, category and tracking attribute; drill-through to the movements behind any number.

**Accounting-Control Impact.** None directly — the report reads, it never writes. Controls: the conservation check (movements in minus movements out equals on-hand) must hold and must be visible; negative on-hand is displayed and flagged, never hidden; forecast quantities must never be presented in the same column as physical stock, because that is how a business ships goods it does not have.

---

### C2. Locations — `MENU-RP-02`
Thai candidate: **สินค้าคงเหลือตามตำแหน่งจัดเก็บ** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `CONDITIONAL` (multi-location or bin-managed warehouses)

**Purpose.** Tell a warehouse worker where a specific item physically is, and tell a supervisor what is sitting in a given place.

**Input.** On-hand per place, per lot, per handling unit; the place hierarchy; storage capacity data where defined.

**Process.** Present two symmetrical views — place-first ("what is in this shelf") and product-first ("where is this item") — with empty-place and over-capacity highlighting.

**Output.** Place contents; item locations; empty places; capacity utilisation.

**Accounting-Control Impact.** None. Controls: visibility should be scopeable by warehouse so that a branch cannot browse another branch's stock — whether SMEsPlus supports place-level authorisation is an open carried item (`RISK-U01`). Stock found in a grouping node or a non-physical counterpart place is a data defect and must be surfaced as an exception, not displayed as ordinary stock.

---

### C3. Moves History — `MENU-RP-03`
Thai candidate: **ประวัติการเคลื่อนไหวสินค้า / สต็อกการ์ด** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `MANDATORY`

**Purpose.** Give one product's complete running ledger — opening balance, every movement in and out, closing balance — as the primary artefact an accountant or auditor uses to prove a stock figure.

**Input.** The certified opening balance; every done movement line with date, document, counterparty, quantity and running balance; the as-of date requested.

**Process.** Order chronologically, compute the running balance, and reproduce the position as of any past date. Re-running the same as-of date must always yield identical figures.

**Output.** A per-product stock card, on screen and as a file export, with document references that drill through to the source.

**Accounting-Control Impact.** The stock card is the bridge between stock truth and the accountant's working papers. Controls: append-only history; guaranteed as-of reproducibility; the export path must be acceptance-tested, because a prior benchmark lesson records a reconciliation export that was defective in practice. **The Thai statutory stock-report format — its required columns, its title, and whether this artefact satisfies it — is `HOLD / EVIDENCE REQUIRED` and routed to the Accounting-Tax track.** The alternate statutory-sounding Thai name is not claimed by this session.

---

### C4. Stock Moves — `MENU-RP-04`
Thai candidate: **รายการเคลื่อนไหวสินค้า** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `MANDATORY` as the audit fact ledger, `CONDITIONAL` as an end-user menu

**Purpose.** Expose the raw movement facts themselves, for investigation, reconciliation, and as the replay base for migration.

**Input.** Every movement line, planned and done, with its full attribute set.

**Process.** Filter and sort by product, place, document, date, actor, state; export the filtered set.

**Output.** A fact-level list showing state, document, quantity, unit, lot, source and destination place, dates and actor.

**Accounting-Control Impact.** None directly; this is the evidence layer beneath every other report. Controls: planned and done facts must be visually and structurally distinct, because treating planned as done is a classic misreading; facts are immutable; every fact carries the identity that makes migration replay safe (`C-02`).

---

### C5. Valuation — `MENU-RP-05`
Thai candidate: **มูลค่าสินค้าคงเหลือ ณ วันที่** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `MANDATORY`

**Purpose.** State the value of stock as of a date under an explicitly named costing policy, and reconcile that value to the general ledger.

**Input.** Quantities as of the date; the cost basis per costing method; the effective policy version; the corresponding general-ledger balance supplied by Accounting.

**Process.** Compute value per product and category as of the date → show the period's movement of value (opening, receipts, issues, adjustments, scrap, landed cost, closing) → compare to the ledger and present the reconciling items line by line.

**Output.** A valuation report whose header names the costing policy and the version used; a reconciliation statement; a file export.

**Accounting-Control Impact.** This is the core accounting interface of the whole module. Inventory computes and presents; **Accounting owns the policy, the posting and the close**. Controls: the policy in force must be printed on the report, or an accountant will misread it; the figure must be reproducible as of any date; the export must be acceptance-tested; a late supplier bill arriving after a closed period must follow an explicit rule rather than silently restating a closed figure. **Blocking:** the ownership of valuation policy and the design of the period close are unresolved Joint items and this report cannot be finalised until they are settled. Carried: `C-03` (return cost basis), `C-05` (evidence-chain containment), and the reopened close-design finding.

---

### C6. Warehouse Analysis — `MENU-RP-06`
Thai candidate: **วิเคราะห์คลังสินค้า** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `CONDITIONAL` (management dashboard)
Evidence status: never studied in any prior round — the block below is this session's SMEsPlus design hypothesis, `UNVALIDATED - THAI USER REVIEW REQUIRED`.

**Purpose.** Show the owner and the warehouse manager how well the warehouse is running and how much cash is tied up in it.

**Input.** Planned versus actual dates on receipts and deliveries; movement volumes; stock ages; values; adjustment and scrap history.

**Process.** Compute a small, stable set of indicators over a chosen period and compare against the previous period.

**Output.** On-time receipt and dispatch percentage; open backorders and their age; stock ageing bands; turnover and days of stock; dead-stock list; adjustment and scrap trend by reason; capacity utilisation where storage capacity is configured.

**Accounting-Control Impact.** None — these are management indicators. Controls: the dashboard must be visibly labelled as management information and must never be presented as an accounting or statutory figure; every indicator must state its formula and its period, so that two people reading it reach the same conclusion.

---

## D. CONFIGURATION — WAREHOUSE

### D1. Settings — `MENU-CF-01`
Thai candidate: **ตั้งค่าระบบคลังสินค้า** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `MANDATORY`

**Purpose.** Let each company switch on only the Inventory capabilities it actually needs, so a small trader is never shown a large distributor's screens.

**Input.** Administrator choices expressed as business questions — do you track batches or serial numbers? do you store goods in more than one place? do you sell by pack? do you import? do you scan barcodes? do you inspect goods before putting them away? what is your reservation policy?

**Process.** Each switch reveals or hides menus, fields and reports, and some switches create the default records the capability needs. Switching a capability *off* while dependent data exists is refused, with an explanation of what is blocking it.

**Output.** The company's effective feature set, versioned and dated.

**Accounting-Control Impact.** Switches that affect valuation, costing or the period guard are accounting-interface changes and require Accounting acknowledgement, not just administrator action. Controls: every switch change is audited with actor, time and previous value; turning a capability on must never silently regenerate or overwrite existing configuration — SMEsPlus versions configuration rather than regenerating it, which is an explicit departure from the benchmark's behaviour.

---

### D2. Warehouses — `MENU-CF-02`
Thai candidate: **คลังสินค้า** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `MANDATORY`

**Purpose.** Represent a physical site where goods are received, kept and dispatched.

**Input.** Name, code, address, owning company, the receipt and delivery step policy (one, two or three steps), and — separately and explicitly — whether this site corresponds to a registered tax branch.

**Process.** Creating a warehouse creates its default places, its default document types and its default flow template selection. Changing the step policy takes effect from an explicit date for new demand only and never rewrites flows already planned.

**Output.** The warehouse structure and its generated defaults.

**Accounting-Control Impact.** Valuation is normally company-wide rather than per warehouse; if a tenant needs value per site, that is an accounting-interface question, not an Inventory setting. Controls: the warehouse code is a migration key and must be stable; **a warehouse must never be silently equated with a Thai tax branch (สาขา)** — branch is an explicit attribute, and the tax consequences of conflating them are `HOLD / EVIDENCE REQUIRED`, routed to the Accounting-Tax track; step-policy changes are audited.

---

### D3. Locations — `MENU-CF-03`
Thai candidate: **ตำแหน่งจัดเก็บ** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `MANDATORY` for system defaults, `CONDITIONAL` for user-managed bins

**Purpose.** Define every place stock can sit, physical or logical, so that every movement has a real source and a real destination.

**Input.** Name, Thai label, parent, place role (internal stock, grouping, supplier counterpart, customer counterpart, loss, adjustment counterpart, production counterpart, transit), owning warehouse, and optional storage category.

**Process.** Maintain the place hierarchy. System-created counterpart places cannot be deleted. A place may be archived only when it holds no stock.

**Output.** The place hierarchy and on-hand per place.

**Accounting-Control Impact.** The internal / non-internal boundary defined here is what triggers every valuation fact in the module — this menu is therefore an accounting-relevant configuration, not a cosmetic one. Controls: place roles are a closed, controlled list; stock discovered in a grouping node is an exception; place-scoped authorisation is an open carried item (`RISK-U01`). The five internal role names above are **benchmark-derived and unvalidated**, described in prose and not as any path notation, exactly as the authoritative containment branch requires.

---

### D4. Routes — `MENU-CF-04`
Thai candidate: **เส้นทางการไหลของสินค้า**, presented to users as named templates such as **รับสินค้า 1 ขั้นตอน** / **รับ-ตรวจ-เก็บ** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `CONDITIONAL`

**Purpose.** Turn a demand into the right chain of movements without the user having to think about it.

**Input.** The template chosen per warehouse, optionally overridden per category or product; the warehouse's step policy; the effective date of the choice.

**Process.** When demand appears, the system resolves the applicable template and generates the planned movement chain, writing an explanation of why that template applied.

**Output.** Planned movement chains; purchase or manufacturing requests where the template ends at a supply boundary; one explanation record per resolution.

**Accounting-Control Impact.** None directly; the chain's endpoints determine where valuation facts later arise. Controls: resolution must be deterministic — the same input always selects the same template; the resolution must be explainable in one readable sentence; templates are versioned with effective dates rather than regenerated; a retried resolution must not create a second chain (`C-02`).

---

### D5. Rules — `MENU-CF-05`
Thai candidate: **กฎการไหลของสินค้า** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `CONDITIONAL`, hidden behind templates

**Purpose.** Define a single step inside a flow template — where goods move from, where they move to, which document type carries them, and how the step is supplied.

**Input.** The step's source place, destination place, document type, supply behaviour (take from stock, buy, manufacture, or push onward), and lead time.

**Process.** Steps chain to form the template's movement path. Editing a step directly is an advanced administrator action available only when advanced mode is on, and every edit is audited.

**Output.** The steps that make up each template, and the planned movements they generate.

**Accounting-Control Impact.** None directly. Controls: Thai SME users must never need to see or edit this menu — if a common Thai flow can only be achieved by hand-editing steps, that is a design defect in the template set, not a task for the customer; every direct edit is logged with the reason for departing from the template.

---

### D6. Operation Types — `MENU-CF-06`
Thai candidate: **ประเภทรายการคลัง** (ใบรับสินค้า / ใบจ่ายสินค้า / ใบโอน / ใบคืน) `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `MANDATORY`

**Purpose.** Define the kinds of stock document the business uses, each with its own numbering, its own defaults, and its own approval rights.

**Input.** Name, warehouse, direction (in, out, internal), document number series and prefix, default source and destination places, matching return type, and reservation behaviour.

**Process.** Default types are created with each warehouse; additional types are added where the business genuinely distinguishes them. Each type carries its own number series that must never be shared or reused.

**Output.** Document types, their number series, and the per-type work queues staff actually operate from.

**Accounting-Control Impact.** Direction determines whether the document's movements cross the ownership boundary and therefore whether they emit valuation facts. Controls: the document type is the unit of separation of duties — rights are granted per type, and how granular Thai SMEs need this to be is `UNVALIDATED - THAI USER REVIEW REQUIRED`; number series must be gapless and auditable; changing default places on a type must not affect documents already created. Thai document-numbering conventions are a candidate design here, not an established requirement.

---

### D7. Storage Categories — `MENU-CF-07`
Thai candidate: **ประเภทพื้นที่จัดเก็บ** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `CONDITIONAL` (capacity- or condition-constrained warehouses)
Evidence status: never studied in any prior round — the block below is this session's SMEsPlus design hypothesis, `UNVALIDATED - THAI USER REVIEW REQUIRED`.

**Purpose.** Describe what a storage place can physically hold — how much, and under what conditions — so that put-away suggestions are realistic.

**Input.** Capacity limits (by weight, volume or handling-unit count), allowed product categories or conditions (chilled, frozen, dry, hazardous), and mixing rules (may different products or different lots share this place?).

**Process.** Categories are defined and assigned to places; put-away consults them when suggesting a destination; violations are flagged.

**Output.** Capacity-aware put-away suggestions; over-capacity and condition-violation exception lists.

**Accounting-Control Impact.** None. Controls: constraints are **advisory by default** — a full storage place must never block a physical receipt, because the goods have already arrived and the system's job is to record reality, not to argue with it. Blocking behaviour, if any tenant wants it, must be an explicit opt-in.

---

### D8. Putaway Rules — `MENU-CF-08`
Thai candidate: **กฎจัดเก็บสินค้าเข้าที่** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `CONDITIONAL` (bin-managed warehouses)
Evidence status: never studied in any prior round — the block below is this session's SMEsPlus design hypothesis, `UNVALIDATED - THAI USER REVIEW REQUIRED`.

**Purpose.** Answer the warehouse worker's question at the receiving dock: "this has arrived — where do I put it?"

**Input.** A matching key (product, category, packaging, or storage condition), a destination place or storage category, and a priority.

**Process.** On receipt, the most specific matching rule wins; capacity and condition constraints filter the result; the system suggests a destination and shows why it chose it; the worker may override, and the override is recorded.

**Output.** A suggested destination place per received line, with its explanation.

**Accounting-Control Impact.** None — put-away moves stock between internal places only. Controls: the suggestion must be explainable; it must never override a destination the worker explicitly chose; conflicting rules of equal priority must be detected at configuration time, not silently resolved at run time. Open: product category is being considered as the owner of both valuation policy and put-away behaviour, and that dual ownership is a Joint design question (`GAP-FS-02`).

---

## E. CONFIGURATION — PRODUCT

### E1. Product Categories — `MENU-CF-09`
Thai candidate: **หมวดหมู่สินค้า** (if it owns costing policy: **หมวดหมู่สินค้าและนโยบายต้นทุน**) `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `MANDATORY`

**Purpose.** Group products for reporting, and — as the current leading candidate — carry the valuation policy that products inherit.

**Input.** The category tree; the removal or issue strategy; the valuation timing and costing method if this object owns them; the account mapping supplied by Accounting.

**Process.** Products inherit the effective policy from their category. A policy change is an approved, effective-dated action, never an immediate silent restatement; moving a product between categories with different policies is treated as a policy change on that product and requires the same approval.

**Output.** The effective valuation policy per product; the reporting hierarchy.

**Accounting-Control Impact.** The highest accounting impact of any configuration menu in Inventory. **Whether category is in fact the right owner of valuation policy — as against product, warehouse, or a standalone versioned policy object — is an open Joint Accounting ↔ Inventory decision and is not settled here** (`GAP-FS-01`). Controls: policy changes require approval, an effective date, and a recorded reason; a category move that would silently change how a product is valued must be refused and re-raised as a policy change. Carried: this menu sits directly on top of the evidence chain that produced the `C-05` finding; this package uses only remediated Layer 1 learning and reproduces none of the quarantined material. Thai costing-norm expectations are `HOLD / EVIDENCE REQUIRED`, routed to the Accounting-Tax track.

---

### E2. Attributes — `MENU-CF-10`
Thai candidate: **คุณลักษณะสินค้า** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `CONDITIONAL` (pairs with variants)
Evidence status: no dedicated evidence in the prior chain — this session's SMEsPlus design hypothesis, `UNVALIDATED - THAI USER REVIEW REQUIRED`.

**Purpose.** Define the axes along which a model varies — colour, size, capacity, material — and the permitted values on each axis.

**Input.** Attribute name, its display type, and its list of values, each with a stable code and a display label in Thai and English.

**Process.** Attributes are assigned to a product; the selected values determine which variants can exist. Values may be added at any time; a value in use may be renamed for display but its code is permanent.

**Output.** The attribute and value catalogue that drives the variant grid.

**Accounting-Control Impact.** None directly; attribute-value codes are the backbone of variant identity and therefore of variant-level stock and valuation. Controls: value codes are immutable once used; a value in use cannot be deleted; renaming a display label must never alter historical variant identity.

---

### E3. Product Packagings — `MENU-CF-11`
Thai candidate: **หน่วยบรรจุ / แพ็กสินค้า** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `CONDITIONAL` (wholesale, distribution, fast-moving consumer goods)
Evidence status: the prior chain recorded that the studied benchmark had no distinct packaging concept; the block below is this session's SMEsPlus design hypothesis, `UNVALIDATED - THAI USER REVIEW REQUIRED`.

**Purpose.** Let staff enter and scan goods in the packs they physically handle — a carton, a case, a pallet — while stock is always counted in the base unit.

**Input.** Product, pack name in Thai, quantity of base units per pack, and the pack's own barcode.

**Process.** When a pack barcode is scanned or a pack quantity is entered, the system converts once to base units and records the movement in base units, while displaying what was actually handled.

**Output.** Documents that show both the pack handled and the base quantity recorded; base-unit stock.

**Accounting-Control Impact.** None directly, but a conversion error here becomes a quantity error and therefore a value error. Controls: a packaging is explicitly **not** a unit of measure — packaging is how goods arrive, unit of measure is how goods are counted, and the system must never allow the same conversion to be applied twice; changing a pack's contained quantity is effective-dated and never restates history.

---

### E4. Reordering Rules — `MENU-CF-12`
Thai candidate: **จุดสั่งซื้อ / ยอดต่ำสุด-สูงสุด** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `CONDITIONAL` (pairs with replenishment)

**Purpose.** Record, per product and place, the stock level at which the business wants to reorder and the level it wants to reorder up to.

**Input.** Minimum, maximum, the unit those figures are expressed in, the supply template, the planning horizon, lead time, and whether the rule triggers automatically or only proposes for review.

**Process.** Each planning run compares the forecast position against the minimum and proposes a quantity that restores the maximum, rounded to the supplier's pack or multiple where one is defined.

**Output.** Replenishment proposals with their explanations.

**Accounting-Control Impact.** None. Controls: the unit of the minimum and maximum must be shown explicitly, because a minimum expressed in cartons and read as pieces is a costly and common error; rules on archived products are surfaced and disabled rather than silently ignored; automation is opt-in per rule.

---

### E5. Barcode Nomenclatures — `MENU-CF-13`
Thai candidate: **รูปแบบบาร์โค้ด** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `CONDITIONAL` (barcode-enabled operations)
Evidence status: never studied in any prior round — this session's SMEsPlus design hypothesis, `UNVALIDATED - THAI USER REVIEW REQUIRED`.

**Purpose.** Teach the system how to read the barcodes a business actually uses, so a scan resolves to the right product, pack, batch or quantity.

**Input.** Named formats with their patterns and what each pattern means — a retail article code, an internally assigned code, a weight-embedded code, a batch-carrying label, a pack label.

**Process.** A scan is matched against the formats in priority order; the first match determines what was scanned and what it resolves to; an unmatched scan is refused with a readable message rather than guessed at.

**Output.** A resolved scan — product, variant, pack, batch, quantity — ready for the document being worked on.

**Accounting-Control Impact.** None directly; a mis-parsed scan becomes a wrong movement, which becomes a wrong quantity and a wrong value. Controls: overlapping patterns must be detected when the format is saved, not when a worker is standing at the dock; every unmatched scan is logged so the format set can be corrected. Whether Thai SMEs predominantly use a standard retail article format, an internal format, or both is `UNVALIDATED - THAI USER REVIEW REQUIRED`.

---

## F. CONFIGURATION — UNITS

### F1. UoM Categories — `MENU-CF-14`
Thai candidate: **กลุ่มหน่วยนับ / หน่วยนับและอัตราแปลง** `UNVALIDATED - THAI USER REVIEW REQUIRED` · Classification: `MANDATORY`

**Purpose.** Let a business buy in one unit, count in another and sell in a third — ชิ้น, โหล, กล่อง, ลัง, กิโลกรัม — while the system holds a single truthful quantity underneath.

**Input.** The unit group, its single base unit, each member unit with its conversion factor, the factor's effective date and version, and the explicit rounding behaviour.

**Process.** Every entered quantity is converted to the base unit at the point of entry and stored in the base unit. Conversion never happens twice on the same figure. A factor change creates a new version effective from a date and never restates history.

**Output.** Base-unit stock; documents that display the unit the user actually worked in.

**Accounting-Control Impact.** Conversion and rounding directly determine quantity and therefore value; a rounding rule applied invisibly is an unrecorded valuation decision. Controls: the base unit of a group is immutable once stock exists; factors are versioned and effective-dated; rounding is stated on screen ("1 โหล = 12 ชิ้น"); units may only be converted within their own group. Thai unit conventions are a candidate list and are `UNVALIDATED - THAI USER REVIEW REQUIRED`.

---

## G. Coverage Roll-Up

| Group | Menus | Count |
|---|---|---:|
| Operations | OP-01 … OP-06 | 6 |
| Products | PR-01 … PR-03 | 3 |
| Reporting | RP-01 … RP-06 | 6 |
| Configuration — Warehouse | CF-01 … CF-08 | 8 |
| Configuration — Product | CF-09 … CF-13 | 5 |
| Configuration — Units | CF-14 | 1 |
| **Total** | | **29** |

| Check | Result |
|---|---|
| All 29 covered | Yes |
| All five mandatory headings present in every block | Yes |
| Any block blank | No |
| Blocks written as an explicit unvalidated SMEsPlus hypothesis due to thin evidence | 8 — OP-05, PR-02, RP-06, CF-07, CF-08, CF-10, CF-11, CF-13 |
| Blocks carrying a statutory `HOLD / EVIDENCE REQUIRED` routed to the Accounting-Tax track | 7 — OP-04, OP-05, PR-01, PR-03, RP-03, CF-02, CF-09 |
| Blocks with an explicit Accounting-Control Impact statement | 29 of 29 |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
