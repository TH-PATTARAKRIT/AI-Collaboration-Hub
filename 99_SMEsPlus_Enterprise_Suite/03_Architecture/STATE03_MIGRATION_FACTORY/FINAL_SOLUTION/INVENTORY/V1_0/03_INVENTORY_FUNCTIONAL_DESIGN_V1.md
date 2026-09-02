# 03 — Inventory Functional Design v1.0

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V1-001` | Jira: `ERPPLUS-139`
Status: `SMEsPlus-OWNED FUNCTIONAL DESIGN — CANDIDATE FOR BOSS FINAL GATE — NOT APPROVED, NOT IMPLEMENTABLE AS WRITTEN`
Clean-room: Layer 1. Reference systems appear only as "the reference ERP" / "the benchmark". No source code, model, field, method, schema, markup, menu definition or file citation.

---

## 1. Purpose of the Inventory Module

The Inventory module answers five questions for a Thai SME, at any moment and for any past date:

1. **What do we have?** — quantity on hand, per product, per place, per lot.
2. **What can we promise?** — available quantity after reservations.
3. **Where did it come from and where did it go?** — the movement history behind every number.
4. **What is it worth?** — the value of stock under a stated costing policy, reconcilable to the general ledger.
5. **Who did it and who approved it?** — the control record behind every exception.

Everything else in the module exists to serve one of those five.

---

## 2. Design Principles

| # | Principle | Consequence |
|---|---|---|
| P-01 | **One physical event, one movement fact.** | No duplicate counting; every document line resolves to exactly one done movement. |
| P-02 | **Movement facts are immutable once done.** | Errors are corrected by a new, reversing movement with its own reason and approver, never by editing or deleting a past record. |
| P-03 | **On-hand is derived, never edited.** | There is no screen anywhere in SMEsPlus that lets a user type a new on-hand number directly. The only way to change stock is a movement, and adjustments are movements with a reason and an approver. |
| P-04 | **The internal / non-internal boundary is what creates accounting.** | Moving stock between two internal places is free of accounting effect; crossing to a supplier, customer, loss, adjustment counterpart or production counterpart emits a valuation fact. |
| P-05 | **Complexity is opt-in.** | Lots, expiry, multi-location, packaging, variants, landed cost, multi-step flows, storage capacity, barcode parsing all default to off. A single-warehouse trading SME must never see them. |
| P-06 | **Every automatic action must be explainable and repeatable.** | Any system-generated proposal, reservation or routing decision carries a plain-language explanation record and a stable identity so a retry cannot duplicate it. |
| P-07 | **Inventory emits facts; Accounting decides postings.** | Inventory never writes a journal entry and never chooses an account. It emits a valuation fact with quantity, cost basis, date, reason and reference; Accounting owns what happens next. |
| P-08 | **Thai business language first.** | Screens, documents and reports use the words Thai warehouse staff and Thai accountants already use, never a transliteration of a benchmark term. All such names are currently `UNVALIDATED - THAI USER REVIEW REQUIRED`. |
| P-09 | **Every record is tenant- and company-scoped.** | Isolation is a data-layer guarantee with a post-write audit, not an application-layer convention. |
| P-10 | **Every migrated record carries its origin.** | A provenance reference from the legacy source to the SMEsPlus record is mandatory and must be designed as a first-class migration component, because no such mapping exists today. |

---

## 3. Functional Scope and Boundaries

### 3.1 In scope for Inventory v1.0

- Warehouse, location, route-template, flow-rule and operation-type configuration.
- Product master, variants, attributes, packaging, unit-of-measure groups and conversion governance.
- Lot and serial identity, expiry, and traceability queries.
- Receipt, delivery, internal movement, return, scrap, adjustment and physical count processes.
- Replenishment rules, planning proposals, and the background planning run.
- Barcode format definition and scan resolution.
- Emission of valuation facts, landed-cost allocation facts, adjustment and scrap facts.
- Stock, location, movement-history, movement-fact, valuation and warehouse-analysis reporting.
- Migration intake of master data, opening balances and movement history.

### 3.2 Explicitly out of scope for Inventory (owned elsewhere)

| Out of scope | Owner | Why |
|---|---|---|
| Journal entries, account selection, posting rules | Accounting | Inventory emits facts only (P-07). |
| Costing method and valuation-timing policy decision | Joint Accounting ↔ Inventory | Undecided; see file 08 and `GAP-FS-01`. |
| Period lock date and backdating exception grants | Accounting | Inventory enforces the lock it is given, and requires a native guard of its own that does not depend on an accounting bridge. |
| Purchase order, sales order and manufacturing order lifecycles | Purchase / Sales / Manufacturing | Inventory receives intent and returns movement facts. |
| Vendor pricing, 3-way match, customer invoicing | Purchase / Sales | Inventory supplies received and delivered quantities. |
| Thai statutory report formats, deductibility of scrap, import duty and VAT treatment, withholding-tax mechanics | Accounting-Tax track | `HOLD / EVIDENCE REQUIRED` — this session has no legal evidence source. |
| Tenant provisioning and subscription tiering | SaaS Foundation | Inventory consumes the feature-switch set. |
| Screen design, component architecture, and any code | Not yet authorized | Design evidence only. |

### 3.3 Boundary cases decided in this design

| Case | Decision | Rationale |
|---|---|---|
| Is a warehouse the same as a Thai tax branch (สาขา)? | **No.** Branch is a separate, explicit attribute of a warehouse and is never assumed. | A prior precision note warns these are routinely conflated; the tax consequence of getting it wrong is real. `UNVALIDATED - THAI USER REVIEW REQUIRED` for how Thai SMEs expect to see it presented. |
| Is a packaging the same as a unit of measure? | **No.** A unit of measure is *how it is counted*; a packaging is *how it arrives*. Packagings convert to the base unit at document entry and never become a second stock unit. | Prevents double conversion, the most common source of quantity error. |
| Does a service product hold stock? | **No.** Product kind (stockable / consumable / service) determines whether stock truth applies at all, and changing kind after stock exists is a controlled, approved action. | The derivation must be stated as a business rule the user can read, not as an internal flag combination. |
| Can on-hand go negative? | **Displayed, flagged, and policy-controlled** — never silently clamped and never silently allowed. Available quantity may show zero; true on-hand shows the negative and raises an exception. | Hidden negatives destroy the conservation check that makes stock truth auditable. |
| Who guards the closed period for stock movements? | **Inventory guards it natively**, using the lock date Accounting supplies, rather than relying on a downstream accounting bridge to reject the movement. | A movement recorded into a closed period is a stock-truth defect before it is an accounting defect. |

---

## 4. Thai SME Warehouse and Stock Operating Model

**Tier assumption (candidate, `UNVALIDATED - THAI USER REVIEW REQUIRED`).** The design assumes three operating tiers, and every capability below is assigned to the tier where it first becomes visible.

| Tier | Typical business | Visible Inventory capability |
|---|---|---|
| T0 — micro | Single shop, single store room, owner counts stock personally | Products, receipt, delivery, on-hand report, physical count and adjustment |
| T1 — growing | One or two warehouses, staff doing receiving and picking, some tracked goods | Adds internal transfer, locations, lots/expiry where relevant, reorder points, stock card, scrap register |
| T2 — established | Multi-site, imports, variants, bins, barcode scanning, formal audit | Adds routes, putaway, storage capacity, landed cost, packaging, variants, valuation reconciliation, warehouse analytics |

**Operating rhythm assumed (candidate, `UNVALIDATED - THAI USER REVIEW REQUIRED`).** Daily receiving and dispatch against orders; weekly review of near-empty items; monthly or quarterly cycle counting; an annual full count witnessed for the auditor; month-end valuation handed to the accountant; scrap handled as an approved exception, not a routine.

---

## 5. Warehouse, Location, Route and Rule Design

**Inherited clean-room constraint — preserved.** The location role set below is **benchmark-derived and unvalidated**. It is described in prose, deliberately *not* as a vendor-style parent-code/child-name path notation, and which of these roles Thai SME warehouses actually use — and under what names — is `UNKNOWN / EVIDENCE REQUIRED` pending Thai field input. It is carried for structural learning only and is **not** a business requirement established by this document. This restates, and does not weaken, the corrected wording on the authoritative containment branch.

### 5.1 Location roles (candidate, benchmark-derived, unvalidated)

| Role | Thai label (candidate) | Business meaning | When it exists |
|---|---|---|---|
| Main stock | คลังสินค้า | Where on-hand stock lives; optionally subdivided into zones, shelves or a cold-storage area | Always |
| Receiving holding area | รับเข้า (รอตรวจ/รอเก็บ) | Goods rest here after arrival, before inspection or put-away | Only in a two- or three-step receipt process |
| Quality-check area | ตรวจคุณภาพ | Goods await inspection | Only in a three-step receipt process |
| Shipping staging area | รอจัดส่ง | Goods await dispatch | Only in a two- or three-step delivery process |
| Packing area | แพ็กสินค้า | Goods are packed before staging or dispatch | Only in a three-step delivery process |

All Thai labels: `UNVALIDATED - THAI USER REVIEW REQUIRED`.

### 5.2 Non-physical counterpart places

Movements always have two ends. Where one end is outside the company's stock, SMEsPlus uses a named counterpart that never holds real stock: supplier (ผู้ขาย), customer (ลูกค้า), loss or scrap (สินค้าเสีย/สูญหาย), adjustment counterpart (ปรับปรุงยอด), production counterpart (การผลิต) where manufacturing applies, and in-transit (ระหว่างขนส่ง) for movement between warehouses or companies. All Thai labels: `UNVALIDATED - THAI USER REVIEW REQUIRED`.

### 5.3 Structural rules

| Rule | Control consequence |
|---|---|
| Only internal locations hold company stock | Valuation sums internal locations only |
| Every movement has exactly one source and one destination | Enables the conservation check: sum of movements in, minus sum of movements out, equals on-hand |
| Crossing the internal / non-internal boundary emits a valuation fact | The single trigger for the Accounting handoff |
| Grouping nodes hold nothing | Reporting roll-up only |
| A location belongs to exactly one warehouse and one company | Tenant isolation; cross-company movement must pass through transit, and that end-to-end path has never been traced (`GAP-FS-07`) |
| A location may be archived only when empty | Prevents orphaned stock |

### 5.4 Flow templates, not rules

Thai SME users never see "routes" or "rules". They choose a named template per warehouse — a one-step, two-step or three-step receipt; a one-step, two-step or three-step delivery; resupply from another warehouse; buy-on-reorder-point; make-or-buy on demand; direct shipment from supplier to customer; and manufacture — and the system resolves the movement chain from that choice. Raw rule editing is an advanced, audited administrator action.

Three governing rules apply to templates:

1. **Versioned, not regenerated.** Changing a warehouse's template must not rewrite flows already planned; it applies to new demand from an explicit effective date. The benchmark regenerates its flow graph on write; SMEsPlus versions instead.
2. **Deterministic and explainable.** Every resolution produces a plain-language explanation record the user can read.
3. **Idempotent.** A demand identity — source document line, template, and attempt — must be unique, so a retry cannot create a second movement chain. Carried finding `C-02`: whether this is gate-blocking is Boss's decision.

---

## 6. Product Master, Variant, Attribute and Packaging Structure

| Element | Design |
|---|---|
| Product | One identity per traded item: code, Thai and English names, kind, category, base unit, tracking mode, optional expiry policy, optional barcode, tax defaults supplied by Accounting. |
| Product kind | Three business labels — สินค้าคงคลัง (stockable), วัสดุสิ้นเปลือง (consumable), บริการ (service), all `UNVALIDATED - THAI USER REVIEW REQUIRED`. The derivation must be a stated business rule; the benchmark's two-axis internal gate must not be copied as a literal structure, and the tie-break when the two axes disagree is an open item (`GAP-FS-04`). |
| Variant | Where a model has options, stock is counted per variant, not per model. Variant identity is the combination of stable attribute-*value codes*, so renaming a value's display text never breaks identity or history. |
| Attribute | An axis of variation with stable value codes. Display names are free to change; codes are not. |
| Packaging | A named pack size over the base unit ("ลัง 12 ชิ้น"), used for entry and barcode resolution only. Conversion to base unit happens once, at entry. |
| Unit of measure | Units belong to a convertible group with a single base unit. Factors are versioned and effective-dated; a factor change never restates historical quantities. Rounding behaviour is explicit and visible, never an invisible default. |

---

## 7. Traceability, Expiry and Quality

- **Tracking mode** is a per-product choice: none, by lot, or by serial. It is switched on only where the business needs it.
- **Lot identity** is product plus lot value within a company, and becomes immutable after its first movement. **Serial identity** is product plus serial value within a company and must be unique — enforced at the data layer, not detected after the fact.
- **Expiry** is captured at receipt for products with an expiry policy. The issue proposal is oldest-expiry-first where expiry is tracked, oldest-received-first otherwise, and the user may override with a reason.
- **Quality holds** are a location state, not a product state: goods awaiting or failing inspection sit in a quality-check or quarantine place and are therefore visible in on-hand but excluded from available. Whether a distinct damaged-goods state is needed is an open item carried from the evidence chain (`RISK-U02`).
- **Recall** must be answerable in both directions: from a lot to every customer who received it, and from a customer complaint back to the receipt and supplier.

---

## 8. Control Model

| Control | Design |
|---|---|
| Separation of duties | The person who counts is not the person who approves the adjustment; the person who validates a receipt is not the person who approved the order; the person who requests a scrap is not the person who approves it. |
| Reason codes | Mandatory on every adjustment and every scrap, from a controlled list, with free text as a supplement and never a substitute. |
| Value thresholds | Adjustments and scraps above a configurable value escalate to a higher approver. |
| Period guard | Movements dated into a closed period are refused natively by Inventory, with a recorded exception path that names the grantor, the reason and an expiry. |
| Immutability | Done movements cannot be edited or deleted, only reversed. |
| Audit trail | Actor, timestamp, before/after and approval chain on every exception; feature-switch changes are themselves audited. |
| Authorization by place | Whether a user's rights can be scoped to a warehouse or location is an open item carried from the evidence chain (`RISK-U01`). |

---

## 9. Non-Functional Requirements Stated as Business Requirements

| Requirement | Business statement |
|---|---|
| Data isolation | A user of one company can never read or write another company's stock, and this must be guaranteed below the application layer with a post-write audit that proves it. |
| Idempotency | Any operation that can be retried — a planning run, an integration call, a migration replay — carries a stable identity so the retry produces no second effect. |
| Reproducibility | Any report as of a past date must produce the same figures every time it is run. |
| Export integrity | Every report that an accountant or auditor relies on must have its export path acceptance-tested; a prior benchmark lesson records a reconciliation export that was defective in practice. |
| Explainability | Any automatic decision the user did not make personally must be accompanied by a readable reason. |

---

## 10. What This Design Deliberately Did Not Carry Forward

| Not carried | Why |
|---|---|
| Any reference-ERP source code, model, field, method, schema or markup | Clean-room rule; Layer 1 output. |
| The benchmark's document-type vocabulary and internal operation-kind coupling | SMEsPlus names its own Thai document types. |
| The benchmark's flow-rule engine architecture and background-job architecture | Business behaviour was learned; architecture was not. |
| The benchmark's specific location node set as a requirement | Preserved as benchmark-derived and unvalidated (§5). |
| Application-layer-only uniqueness for serials | SMEsPlus requires data-layer enforcement. |
| Silent regeneration of configuration on write | SMEsPlus versions configuration instead. |
| Any prescriptive claim that SMEsPlus "must" do what the reference does | This is precisely the language defect the carried `C-05` finding identified; every statement here is justified as a Thai SME business need or marked unvalidated. |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
