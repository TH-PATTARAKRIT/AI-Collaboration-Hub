# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# 02 — L1 Domain Understanding Register

Level: `L1 — Domain Understanding`
Scope: `29 of 29 Inventory menus`
Control Level: `/L9999.9999`
Status: `L1 COMPLETE FOR 29/29 MENUS — DEEP RESEARCH ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. Method

For each of the 29 menus in the Boss-approved R4 scope this register states, as required by the L1-L12 standard:

1. Business purpose.
2. Primary user role.
3. Thai SME operating reality.
4. Input and output business facts.
5. Relationship to Sale, Purchase, Manufacturing, Accounting, Approval, Document and Reporting.

Menu IDs `INV-M01` .. `INV-M29` follow the Boss register order in `14_INVENTORY_R4_MENU_EVIDENCE_INTAKE_L1_L12.md` and are stable identifiers for the rest of this package.

Thai SME operating reality is written from the SMEsPlus target-customer profile: a Thai small or medium enterprise, commonly single-company or two-company, with one to three physical storage sites, a small warehouse team, an accountant who is often part-time or external, and a strong practical preference for paper evidence and for a person being accountable for each stock difference.

Every Thai term appearing anywhere in this package is `CANDIDATE / UNVALIDATED`. Every Thai statutory assertion is `HOLD / EVIDENCE REQUIRED` and belongs to the Accounting-Tax track, not to Inventory.

---

## 1A. Menu Identifier Crosswalk — Lineage Preservation

R4 uses `INV-M01` .. `INV-M29` because the Boss R4 scope register in source 2 is ordered and unnumbered, and R4 needs a stable ordinal key. The Menu Deep Challenge package already carries its own menu identifiers. **Both are authoritative and neither supersedes the other.** Every register in this package can be read against either.

| R4 ID | Menu | Menu Deep Challenge ID | Concept-model object | Thai naming register ID |
|---|---|---|---|---|
| `INV-M01` | Replenishment | `MENU-OP-01` | `CN-21` / `OBJ-21` | `TH-01` |
| `INV-M02` | Inventory Adjustments | `MENU-OP-02` | `CN-27`, `CN-28` / `OBJ-27`, `OBJ-28` | `TH-02` |
| `INV-M03` | Transfers | `MENU-OP-03` | `CN-24`, `CN-25` / `OBJ-24`, `OBJ-25` | `TH-03` |
| `INV-M04` | Scrap | `MENU-OP-04` | `CN-29` / `OBJ-29` | `TH-04` |
| `INV-M05` | Landed Costs | `MENU-OP-05` | `CN-30` / `OBJ-30` | `TH-05` |
| `INV-M06` | Run Scheduler | `MENU-OP-06` | `CN-35` / `OBJ-35` | `TH-06` |
| `INV-M07` | Products | `MENU-PR-01` | `CN-11`, `CN-13` / `OBJ-11`, `OBJ-13` | `TH-07` |
| `INV-M08` | Product Variants | `MENU-PR-02` | `CN-12` / `OBJ-12` | `TH-08` |
| `INV-M09` | Lots/Serial Numbers | `MENU-PR-03` | `CN-17`, `CN-18` / `OBJ-17`, `OBJ-18` | `TH-09` |
| `INV-M10` | Stock | `MENU-RP-01` | `CN-26` / `OBJ-26` | `TH-10` |
| `INV-M11` | Locations (Reporting) | `MENU-RP-02` | `CN-26` by place | `TH-11` |
| `INV-M12` | Moves History | `MENU-RP-03` | `CN-25` / `OBJ-25` | `TH-12` |
| `INV-M13` | Stock Moves | `MENU-RP-04` | `CN-25` all states | `TH-13` |
| `INV-M14` | Valuation | `MENU-RP-05` | `CN-31`, `CN-32` / `OBJ-31`, `OBJ-32` | `TH-14` |
| `INV-M15` | Warehouse Analysis | `MENU-RP-06` | derived | `TH-15` |
| `INV-M16` | Settings | `MENU-CF-01` | `CN-34` / `OBJ-34` | `TH-16` |
| `INV-M17` | Warehouses | `MENU-CF-02` | `CN-02` / `OBJ-02` | `TH-17` |
| `INV-M18` | Locations (Configuration) | `MENU-CF-03` | `CN-03` / `OBJ-03` | `TH-18` |
| `INV-M19` | Routes | `MENU-CF-04` | `CN-05` / `OBJ-05` | `TH-19` |
| `INV-M20` | Rules | `MENU-CF-05` | `CN-05` / `OBJ-05` | `TH-20` |
| `INV-M21` | Operation Types | `MENU-CF-06` | `CN-04` / `OBJ-04` | `TH-21` |
| `INV-M22` | Storage Categories | `MENU-CF-07` | `CN-06` / `OBJ-06` | `TH-22` |
| `INV-M23` | Putaway Rules | `MENU-CF-08` | `CN-07` / `OBJ-07` | `TH-23` |
| `INV-M24` | Product Categories | `MENU-CF-09` | `CN-08`, `CN-09` / `OBJ-08`, `OBJ-09` | `TH-24` |
| `INV-M25` | Attributes | `MENU-CF-10` | `CN-10` / `OBJ-10` | `TH-25` |
| `INV-M26` | Product Packagings | `MENU-CF-11` | `CN-15` / `OBJ-15` | `TH-26` |
| `INV-M27` | Reordering Rules | `MENU-CF-12` | `CN-20` / `OBJ-20` | `TH-27` |
| `INV-M28` | Barcode Nomenclatures | `MENU-CF-13` | `CN-16` / `OBJ-16` | `TH-28` |
| `INV-M29` | UoM Categories | `MENU-CF-14` | `CN-14` / `OBJ-14` | `TH-29` |

Note on scope ordering: the Boss R4 register lists `Product Categories` under Configuration at position 24, whereas the Menu Deep Challenge ordered it as `MENU-CF-09`. The menu set is identical; only the ordinal differs. R4 follows the Boss R4 register order.

Thai naming note carried forward: the Thai candidate strings differ slightly between the coverage register, the impact matrix and the naming register for `INV-M03`, `INV-M07`, `INV-M12`, `INV-M26` and `INV-M27`. The Thai naming register (`17_THAI_MENU_AND_REPORT_NAMING_REGISTER.md`) is the designated authority for naming. R4 does not resolve the divergence; it is recorded in `18_THAI_USER_VALIDATION_CHECKLIST.md` as an item requiring Thai user validation.

---

## 2. Group A — Operations

### `INV-M01` Replenishment

| Dimension | Content |
|---|---|
| Business purpose | Show the shortfall position across products and locations and let a user convert a shortfall into a supply action (buy, make, or transfer) without leaving the stock context. |
| Primary user role | Inventory planner or, in a small Thai SME, the owner/manager acting as planner. |
| Thai SME operating reality | Most Thai SMEs do not run formal MRP. Buying is triggered by a person noticing a shelf is low, or by a supplier's visit cycle. The realistic use of this menu is as a *daily shortage worklist*, not as an automated planning engine. A design that assumes disciplined min/max maintenance across thousands of items will not be used. |
| Input business facts | Product identity; location; on-hand quantity; forecast quantity; incoming and outgoing commitments; reordering rule parameters where one exists; supply route preference; lead time. |
| Output business facts | A proposed supply quantity per product/location, and, on confirmation, a supply document request handed to Purchase, Manufacturing, or an internal transfer. |
| Sale | Consumes Sale demand as a reduction of forecast availability. |
| Purchase | Emits a purchase requirement. This is a *request*, not a purchase commitment; Purchase owns the commitment. |
| Manufacturing | Emits a production requirement where the supply route is "make". |
| Accounting | No direct accounting effect. A proposal is not a financial event. |
| Approval | Approval belongs to the downstream document (purchase order, production order), not to the proposal. |
| Document | Produces a traceable proposal record that must survive as evidence of *why* a supply action was raised. |
| Reporting | Feeds shortage and service-level reporting. |

### `INV-M02` Inventory Adjustments

| Dimension | Content |
|---|---|
| Business purpose | Record a counted physical quantity and reconcile it against the recorded quantity, producing a controlled correction with a reason. |
| Primary user role | Warehouse staff count; a supervisor or accountant approves the difference. |
| Thai SME operating reality | Physical counting is real and frequent in Thai SMEs, usually as an annual or semi-annual full count plus ad-hoc spot counts when a discrepancy is noticed. The count is often done on paper first and typed in afterwards, so the *count date* and the *entry date* genuinely differ and both matter. Someone senior is expected to be named as the person who accepted the difference. |
| Input business facts | Product; location; lot/serial where tracked; counted quantity; count date; counter identity; reason for difference. |
| Output business facts | A quantity correction, a valuation consequence, a named reason, and an audit record of who counted and who accepted. |
| Sale | An adjustment can invalidate an existing reservation and must not silently break a customer commitment. |
| Purchase | An adjustment absorbing an unrecorded receipt masks a purchase process failure; the two must be distinguishable. |
| Manufacturing | Absorbs unrecorded consumption or yield loss; must be distinguishable from genuine count error. |
| Accounting | Direct valuation and control effect. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Approval | Mandatory. An unapproved quantity correction is the single largest stock-integrity exposure in this module. |
| Document | Count sheet, variance evidence, and approver identity must be attachable. |
| Reporting | Feeds count variance reporting and shrinkage analysis. |

### `INV-M03` Transfers

| Dimension | Content |
|---|---|
| Business purpose | Execute the movement of goods — incoming receipt, outgoing delivery, and internal movement — as a controlled operation with a lifecycle. |
| Primary user role | Warehouse operator; supervisor for exception handling. |
| Thai SME operating reality | This is the menu Thai SME warehouse staff actually live in. It must work with a printed document, must tolerate partial execution, and must tolerate the goods physically moving before anyone types anything. Backdating is not an edge case in a Thai SME; it is normal Monday-morning behaviour. |
| Input business facts | Operation type; source and destination location; product; demanded quantity; done quantity; lot/serial; package; scheduled date; effective date; source document reference. |
| Output business facts | A quantity movement between two locations, a state transition, optionally a remaining-quantity follow-up (backorder), and — where the movement crosses the valuation boundary — a valuation event. |
| Sale | Delivery execution against a sales commitment; drives revenue-recognition dependency. |
| Purchase | Receipt execution against a purchase commitment; drives supplier-liability dependency. |
| Manufacturing | Component issue to production and finished-goods return from production. |
| Accounting | Receipt and delivery are the two primary financial handoff triggers. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Approval | Normally none per transfer; control is exercised through operation type configuration and location rights. |
| Document | Delivery note, receipt note, and packing evidence. In Thailand a delivered-goods document is routinely expected to travel with the goods. |
| Reporting | Primary feed for movement history and operational throughput reporting. |

### `INV-M04` Scrap

| Dimension | Content |
|---|---|
| Business purpose | Remove goods from usable stock because they are damaged, expired, or otherwise unusable, with a stated reason. |
| Primary user role | Warehouse supervisor; often requires owner sign-off in a Thai SME because it is a direct loss. |
| Thai SME operating reality | Scrap is commercially sensitive and tax-sensitive in Thailand. Owners want to know who authorised a write-off. Some scrapped goods still have a resale or salvage value (returnable packaging, metal, recoverable parts) and Thai SMEs do sell that. Physical destruction evidence is frequently required for tax treatment. |
| Input business facts | Product; quantity; unit of measure; lot/serial; source location; scrap destination; reason; date; authorising person. |
| Output business facts | A quantity reduction to a non-usable location, a loss recognition dependency, and a reason-coded audit record. |
| Sale | May cause a reserved quantity to become unavailable and break a customer promise. |
| Purchase | May trigger a supplier claim where the loss is a supplier-quality failure. |
| Manufacturing | Production scrap and yield loss route here or through consumption, and the two must not be conflated. |
| Accounting | Loss recognition, and salvage recognition where salvage exists. `DEPENDENCY: ACCOUNTING COGS GAP`. Thai destruction-evidence tax treatment is `HOLD / EVIDENCE REQUIRED` and belongs to the Accounting-Tax track. |
| Approval | Mandatory. Scrap without approval is an unmonitored write-off channel. |
| Document | Scrap authorisation, photographic or witness evidence, and destruction evidence where claimed. |
| Reporting | Feeds loss, shrinkage, and quality reporting. |

### `INV-M05` Landed Costs

| Dimension | Content |
|---|---|
| Business purpose | Attach additional acquisition costs — freight, insurance, duty, clearing, handling — to the goods they relate to, so that inventory value reflects true landed cost rather than invoice price alone. |
| Primary user role | Accountant or import/purchasing officer. |
| Thai SME operating reality | Highly material for Thai importers, which are a large part of the SMEsPlus target market. Duty and clearing invoices arrive *weeks after* the goods, frequently in a later accounting period, and frequently after some of the goods have already been sold. This is the normal case, not the exception. |
| Input business facts | The cost amount; the cost type; the allocation basis (equal, by quantity, by weight, by volume, by current cost value); the target receipt or production order; the cost date; the supplier bill reference. |
| Output business facts | An allocation of additional cost across the affected goods, an adjustment to inventory value for goods still on hand, and an expense consequence for goods already gone. |
| Sale | Where goods are already sold, the landed cost cannot be capitalised and must fall to cost of sale. |
| Purchase | Source of the cost documents. |
| Manufacturing | Can attach to production orders as well as receipts. |
| Accounting | Direct and material. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Approval | Required — it changes inventory carrying value. |
| Document | Freight, duty, and clearing invoices must be attachable as the evidence for the allocation. |
| Reporting | Feeds true-cost and margin reporting. |

### `INV-M06` Run Scheduler

| Dimension | Content |
|---|---|
| Business purpose | Execute the automated replenishment computation on demand rather than waiting for its normal schedule. |
| Primary user role | Administrator or planner. |
| Thai SME operating reality | Rarely understood by SME staff. Its practical risk is that a user presses it repeatedly when nothing appears to happen, or presses it while a colleague is manually creating the same purchase order. A design that does not make the run visible and idempotent will produce duplicate ordering. |
| Input business facts | The set of active reordering rules; current stock and forecast positions; the current supply pipeline. |
| Output business facts | Supply proposals or supply documents, plus a run record. |
| Sale | Indirect — consumes demand. |
| Purchase | Can create purchase requirements automatically. |
| Manufacturing | Can create production requirements automatically. |
| Accounting | None directly. |
| Approval | The run itself is unapproved; the documents it creates carry their own approval. This is a control asymmetry that must be designed for deliberately. |
| Document | A run log is required as evidence of what the automation did and when. |
| Reporting | Feeds automation-behaviour and duplicate-supply monitoring. |

---

## 3. Group B — Products

### `INV-M07` Products

| Dimension | Content |
|---|---|
| Business purpose | Define the item master: what a thing is, how it is measured, how it is costed, whether it is stock-controlled, and how it is traced. |
| Primary user role | Master-data owner; in a Thai SME usually the owner or a senior admin. |
| Thai SME operating reality | Product masters in Thai SMEs are frequently created ad hoc by whoever needs to raise a document, producing duplicates under Thai and English names and inconsistent units. Bilingual naming is not optional — staff search in Thai, documents may be issued in either language. |
| Input business facts | Identity and code; description; Thai and English naming; stock-control classification (stock-controlled, consumable, service); default unit of measure; purchase unit of measure; traceability policy; product category; costing category assignment; barcode. |
| Output business facts | The controlling master record that determines whether *any* stock or valuation behaviour occurs at all. |
| Sale | Sellable identity, sales unit, sales description. |
| Purchase | Purchasable identity, purchase unit, supplier references. |
| Manufacturing | Component and finished-goods identity. |
| Accounting | The classification decision here determines whether an item is inventory-valued at all. `DEPENDENCY: ACCOUNTING COGS GAP` for the costing-category consequence. |
| Approval | Master-data change approval required for classification, unit of measure, traceability, and costing category. |
| Document | Product specification and supplier documentation attachment. |
| Reporting | Dimension for every inventory report. |

### `INV-M08` Product Variants

| Dimension | Content |
|---|---|
| Business purpose | Represent the sellable and stockable variations of one product concept — size, colour, grade — without duplicating the product master. |
| Primary user role | Master-data owner; merchandiser. |
| Thai SME operating reality | Thai SMEs in garment, footwear, food packaging and building materials genuinely need variants. Many others do not and are actively harmed by being forced into a variant model they do not understand. The design must let a business ignore variants entirely. |
| Input business facts | Attribute values selected; per-variant code and barcode; per-variant cost where applicable. |
| Output business facts | The concrete stock-carrying identity. Stock, valuation, and traceability all attach to the variant, not to the product concept. |
| Sale | Variant is the sold identity. |
| Purchase | Variant is the purchased identity. |
| Manufacturing | Variant is the produced and consumed identity. |
| Accounting | Valuation attaches at variant level. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Approval | Attribute-structure change is a high-impact master-data change and needs approval. |
| Document | Inherits product documentation. |
| Reporting | Required reporting dimension; reports that aggregate to product concept and reports that need variant detail are both real needs. |

### `INV-M09` Lots/Serial Numbers

| Dimension | Content |
|---|---|
| Business purpose | Carry the traceable identity of a specific batch or a specific unit through receipt, storage, movement, and delivery. |
| Primary user role | Warehouse operator records; quality or compliance officer queries. |
| Thai SME operating reality | Mandatory in Thai food, cosmetics, pharmaceutical and agricultural supply chains, and increasingly demanded by large Thai buyers of their SME suppliers. Expiry-date management is often the real driver rather than recall capability. Suppliers frequently reuse batch codes, so batch identity is not globally unique in practice. |
| Input business facts | Lot or serial identifier; product; expiry and best-before dates; supplier batch reference; company context. |
| Output business facts | An unbroken forward and backward traceability chain, and expiry-driven availability constraints. |
| Sale | Determines which units may be delivered and supports recall of what was shipped to whom. |
| Purchase | Records what was received from which supplier batch. |
| Manufacturing | Links component batches to output batches — the genealogy that makes recall possible. |
| Accounting | Where valuation is tracked per batch, batch identity becomes a valuation key. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Approval | Change or merge of an existing lot identity must be approved; it rewrites traceability history. |
| Document | Certificates of analysis, supplier batch documents, expiry evidence. |
| Reporting | Traceability, expiry, and recall reporting. |

---

## 4. Group C — Reporting

### `INV-M10` Stock

| Dimension | Content |
|---|---|
| Business purpose | State the current stock position by product and location — on hand, reserved, available, incoming, outgoing, forecast. |
| Primary user role | Everyone: sales checking availability, warehouse checking location, owner checking exposure. |
| Thai SME operating reality | This is the most-used screen in the module and the one most likely to be disbelieved. If "available" does not match what a person can see on the shelf, the whole system loses credibility. The distinction between *on hand* and *available* must be visible and explainable in Thai to a non-technical user. |
| Input business facts | Movement history and current balances; reservation state; open commitments. |
| Output business facts | The stock position, decomposed into its six meanings. |
| Sale | Availability promise. |
| Purchase | Coverage position. |
| Manufacturing | Component availability. |
| Accounting | Quantity side of the stock-to-ledger reconciliation. `DEPENDENCY: ACCOUNTING COGS GAP` for the value side. |
| Approval | Read-only. |
| Document | Stock position evidence for audit and for lending. |
| Reporting | Core reconciliation surface. |

### `INV-M11` Locations (Reporting)

| Dimension | Content |
|---|---|
| Business purpose | State the stock position from the location perspective — what is physically where. |
| Primary user role | Warehouse staff performing picking, counting, and put-away. |
| Thai SME operating reality | Thai SME warehouses are often organised by informal spatial habit rather than by a formal location scheme. Location reporting is only useful if the location naming matches what staff say out loud. Over-engineering location depth is a common failure. |
| Input business facts | Balances by location, including non-physical locations. |
| Output business facts | Physical findability and the location-level reconciliation view. |
| Sale | Picking support. |
| Purchase | Put-away confirmation. |
| Manufacturing | Component staging visibility. |
| Accounting | Distinguishing valued from non-valued locations is what makes internal transfer financially neutral. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Approval | Read-only. |
| Document | Count sheets by location. |
| Reporting | Location-level reconciliation. |

### `INV-M12` Moves History

| Dimension | Content |
|---|---|
| Business purpose | Provide the completed movement record — what moved, when, from where, to where, under which document. |
| Primary user role | Supervisor, auditor, accountant. |
| Thai SME operating reality | This is the menu that answers "who took it and when", which is the question a Thai SME owner actually asks. Its evidential value depends entirely on it being immutable. |
| Input business facts | Completed movements with their source document, dates, quantities, and traceability identities. |
| Output business facts | The audit trail of physical stock truth. |
| Sale | What was actually delivered. |
| Purchase | What was actually received. |
| Manufacturing | What was actually consumed and produced. |
| Accounting | The quantity-side evidence behind every valuation event. `DEPENDENCY: ACCOUNTING COGS GAP` for the value side. |
| Approval | Read-only and must be immutable. |
| Document | Primary evidence source. |
| Reporting | Backbone of every movement report. |

### `INV-M13` Stock Moves

| Dimension | Content |
|---|---|
| Business purpose | Provide the operational, line-level movement view including movements not yet completed — planned, reserved, partially executed. |
| Primary user role | Planner and supervisor. |
| Thai SME operating reality | Distinguishing "will move" from "has moved" is the single most common source of misunderstanding for SME users. Having two menus in this area — `INV-M12` and `INV-M13` — is only defensible if the difference between them is explicit and expressible in Thai. If it is not, the two must be reconsidered as one view with a state filter. |
| Input business facts | Movement lines in all states, with demanded and done quantities. |
| Output business facts | The forward-looking movement pipeline. |
| Sale | Open delivery pipeline. |
| Purchase | Open receipt pipeline. |
| Manufacturing | Open consumption and output pipeline. |
| Accounting | Pending financial-effect visibility. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Approval | Read-only. |
| Document | Operational worklists. |
| Reporting | Pipeline and ageing reporting. |

### `INV-M14` Valuation

| Dimension | Content |
|---|---|
| Business purpose | State the value of stock and the history of value-changing events. |
| Primary user role | Accountant and owner. |
| Thai SME operating reality | The number here is the number that has to agree with the financial statements and with what an external accountant or auditor expects. In Thai SMEs the external accountant is often the ultimate arbiter and will not accept a value they cannot reconcile line by line. |
| Input business facts | Valuation events: receipt, delivery, adjustment, scrap, landed cost, cost-method change, retroactive cost correction. |
| Output business facts | Stock value by product, category, and location, and the event history that produced it. |
| Sale | Cost of goods delivered. |
| Purchase | Acquisition value. |
| Manufacturing | Component consumption value and output value. |
| Accounting | This is the Inventory-to-Accounting boundary itself. `DEPENDENCY: ACCOUNTING COGS GAP` — **all conclusions here are locked**. |
| Approval | Read-only, but the policies it reflects require approval. |
| Document | Valuation evidence for audit. |
| Reporting | Stock-to-ledger reconciliation. |

### `INV-M15` Warehouse Analysis

| Dimension | Content |
|---|---|
| Business purpose | Provide analytical views of warehouse performance — throughput, ageing, turnover, service level, exception volume. |
| Primary user role | Owner and operations manager. |
| Thai SME operating reality | Analytics is the first thing switched off if the underlying data is not trusted. Its real value in a Thai SME is narrow and concrete: slow-moving stock, expiring stock, and cash tied up in stock. |
| Input business facts | Movement history, stock position, valuation, and time. |
| Output business facts | Analytical measures used for management decisions rather than for statutory reporting. |
| Sale | Service-level and fulfilment analysis. |
| Purchase | Supplier performance and coverage analysis. |
| Manufacturing | Consumption and availability analysis. |
| Accounting | Working-capital and obsolescence analysis. `DEPENDENCY: ACCOUNTING COGS GAP` for any value-based measure. |
| Approval | Read-only. |
| Document | Management reporting. |
| Reporting | Analytical layer; must be reconcilable to the operational layer or it will be distrusted. |

---

## 5. Group D — Configuration

### `INV-M16` Settings

| Dimension | Content |
|---|---|
| Business purpose | Switch on or off the structural capabilities of the module — multi-location, multi-step operations, batch and serial tracking, packages, unit-of-measure handling, landed costs, storage categories, put-away. |
| Primary user role | Administrator, at implementation time. |
| Thai SME operating reality | A Thai SME will typically run with almost everything switched off. The design must be genuinely usable in its simplest configuration and must not silently degrade when a capability is turned on later, after data already exists. Turning traceability on for a product that already has stock is the classic damaging case. |
| Input business facts | Capability flags, per company. |
| Output business facts | The available behaviour of every other menu in the module. |
| Sale / Purchase / Manufacturing | Determines the shape of their stock interaction. |
| Accounting | Determines whether valuation is even produced. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Approval | Mandatory, and change here must be treated as a controlled change with a before/after record. |
| Document | Configuration decision record. |
| Reporting | Determines which reports mean anything. |

### `INV-M17` Warehouses

| Dimension | Content |
|---|---|
| Business purpose | Define a physical or logical site that owns stock, and the operational structure that goes with it. |
| Primary user role | Administrator. |
| Thai SME operating reality | Typically one to three sites: a shop, a store room, and possibly a second branch. Thai SMEs frequently treat a consignment or customer-site stock as "ours" informally, which is exactly the case that needs an explicit ownership answer. |
| Input business facts | Warehouse identity and code; address; company; operational step configuration. |
| Output business facts | The operational and reporting boundary for stock. |
| Sale | Source of supply for delivery. |
| Purchase | Destination for receipt. |
| Manufacturing | Production site. |
| Accounting | Warehouse-to-company mapping is a hard requirement for company isolation. `DEPENDENCY: ACCOUNTING COGS GAP` for warehouse-level valuation separation. |
| Approval | Structural change requires approval. |
| Document | Site registration and address evidence. |
| Reporting | Primary reporting dimension. |

### `INV-M18` Locations (Configuration)

| Dimension | Content |
|---|---|
| Business purpose | Define the location hierarchy and the *kind* of each location — internal, supplier, customer, transit, production, loss, scrap — which is what determines whether crossing it is a valuation event. |
| Primary user role | Administrator. |
| Thai SME operating reality | Staff think in terms of "the front shop", "the back room", "upstairs". The design must accommodate shallow, human location naming while still carrying the location-kind semantics that valuation depends on. The semantics must not be exposed as a technical concept the user must understand. |
| Input business facts | Location identity; parent; kind; company; storage constraints; counting cycle. |
| Output business facts | The structure that determines findability, and the internal/external boundary that determines financial effect. |
| Sale | Delivery destination semantics. |
| Purchase | Receipt source semantics. |
| Manufacturing | Production input and output semantics. |
| Accounting | The location kind is the mechanism by which an internal transfer is financially neutral and a delivery is not. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Approval | Mandatory — changing a location's kind retrospectively changes the meaning of history. |
| Document | Location layout and naming record. |
| Reporting | Location reporting dimension. |

### `INV-M19` Routes

| Dimension | Content |
|---|---|
| Business purpose | Define the multi-step supply and delivery paths goods follow — one-step, two-step, three-step receipt and delivery, cross-warehouse resupply, drop-ship. |
| Primary user role | Administrator or process designer. |
| Thai SME operating reality | Almost always one-step in and one-step out. Multi-step exists in Thai SMEs mainly where quality inspection or a customs bonded step is genuinely required. Complexity here is the most common cause of an SME abandoning stock control. |
| Input business facts | Route identity; applicability (product, category, warehouse); ordered steps. |
| Output business facts | The generated chain of operations for a given demand. |
| Sale | Determines delivery path shape. |
| Purchase | Determines receipt path shape. |
| Manufacturing | Determines component supply path. |
| Accounting | Additional intermediate steps create additional intermediate positions that must remain financially neutral. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Approval | Mandatory — a route change silently changes how future operations are generated. |
| Document | Process design record. |
| Reporting | Explains why operations look the way they do. |

### `INV-M20` Rules

| Dimension | Content |
|---|---|
| Business purpose | Define the individual supply rule that fires within a route — pull from, push to, buy, manufacture — with its source, destination, operation type and lead time. |
| Primary user role | Administrator. |
| Thai SME operating reality | Effectively invisible to SME users and almost never maintained by them. It is nonetheless where most unexplained system behaviour originates, which makes its diagnosability a first-class requirement. |
| Input business facts | Action type; source and destination location; operation type; supply method; delay. |
| Output business facts | The concrete decision that produced a given proposed or generated operation. |
| Sale | Generates delivery steps. |
| Purchase | Generates purchase requirements. |
| Manufacturing | Generates production requirements. |
| Accounting | Wrong destination configuration can route goods across a valuation boundary unintentionally. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Approval | Mandatory, with an explicit before/after record. |
| Document | Rule change record. |
| Reporting | Required for explainability: every generated operation must be traceable back to the rule that created it. |

### `INV-M21` Operation Types

| Dimension | Content |
|---|---|
| Business purpose | Define a class of stock operation — receipt, delivery, internal transfer, return, manufacturing operation — with its default locations, numbering, and behavioural options. |
| Primary user role | Administrator. |
| Thai SME operating reality | This is where document numbering is set, and document numbering is a compliance-relevant and culturally significant matter in Thailand. Numbering continuity and non-reuse are expected by accountants and auditors. |
| Input business facts | Operation class; default source and destination; numbering sequence; behavioural options such as backorder handling and traceability capture. |
| Output business facts | The behavioural template every transfer inherits. |
| Sale | Delivery operation behaviour. |
| Purchase | Receipt operation behaviour. |
| Manufacturing | Production operation behaviour. |
| Accounting | Default locations set here determine the financial character of every operation of that class. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Approval | Mandatory. Numbering-sequence change is a high-risk controlled change. |
| Document | Numbering and control record. |
| Reporting | Operation classification dimension. |

### `INV-M22` Storage Categories

| Dimension | Content |
|---|---|
| Business purpose | Define capacity and compatibility constraints for storage — what may be stored where, and how much. |
| Primary user role | Warehouse manager. |
| Thai SME operating reality | Genuinely relevant for cold-chain, chemical, and food businesses where mixing is unsafe or unlawful. Irrelevant for most others and must be fully optional. |
| Input business facts | Category identity; capacity by product or package; mixing constraints. |
| Output business facts | Constraint input to put-away decisions. |
| Sale / Purchase | Indirect. |
| Manufacturing | Constrains staging. |
| Accounting | None directly. |
| Approval | Change approval where the constraint is safety- or compliance-driven. |
| Document | Storage compliance evidence. Thai regulatory storage requirements are `HOLD / EVIDENCE REQUIRED`. |
| Reporting | Capacity utilisation. |

### `INV-M23` Putaway Rules

| Dimension | Content |
|---|---|
| Business purpose | Decide automatically where received goods should be placed. |
| Primary user role | Warehouse manager configures; operator experiences the result. |
| Thai SME operating reality | Useful only where the location scheme is disciplined enough to be trusted. In most Thai SMEs a suggested location that is wrong is worse than no suggestion, so the operator must always be able to override, and the override must be recorded. |
| Input business facts | Product or category; incoming context; target location; storage category constraints. |
| Output business facts | A suggested destination location. |
| Sale | Indirect via findability. |
| Purchase | Applies at receipt. |
| Manufacturing | Applies at production output. |
| Accounting | Must not move goods across a valuation boundary. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Approval | Configuration change approval. |
| Document | Put-away policy record. |
| Reporting | Override-rate reporting is a genuine quality signal. |

### `INV-M24` Product Categories

| Dimension | Content |
|---|---|
| Business purpose | Group products for reporting, for default behaviour, and — critically — for costing and account determination. |
| Primary user role | Master-data owner and accountant jointly. |
| Thai SME operating reality | Categories are usually created for reporting convenience by non-accountants, without realising they also drive costing and account mapping. This mismatch of intent is a known and repeated source of valuation error. |
| Input business facts | Category identity; parent; costing method assignment; valuation mode assignment; account determination. |
| Output business facts | The costing and account behaviour of every product in the category. |
| Sale | Sales reporting dimension. |
| Purchase | Purchase reporting dimension. |
| Manufacturing | Cost grouping. |
| Accounting | This is the primary carrier of costing policy for Inventory. `DEPENDENCY: ACCOUNTING COGS GAP` — **conclusions locked**. |
| Approval | Mandatory and high-risk: changing a category's costing method changes the costing of every product in it. |
| Document | Costing policy decision record. |
| Reporting | Principal grouping dimension. |

### `INV-M25` Attributes

| Dimension | Content |
|---|---|
| Business purpose | Define the characteristics from which product variants are generated. |
| Primary user role | Master-data owner. |
| Thai SME operating reality | Meaningful in garment, footwear and food-packaging businesses. Attribute values are frequently maintained bilingually and inconsistently, producing near-duplicate values that fragment stock. |
| Input business facts | Attribute identity; value list; display and variant-creation behaviour. |
| Output business facts | The variant matrix. |
| Sale | Selection dimension. |
| Purchase | Ordering dimension. |
| Manufacturing | Specification dimension. |
| Accounting | Indirect via variant valuation. |
| Approval | Mandatory — changing an attribute after variants carry stock is destructive. |
| Document | Specification record. |
| Reporting | Analysis dimension. |

### `INV-M26` Product Packagings

| Dimension | Content |
|---|---|
| Business purpose | Define standard grouped quantities — box, carton, pallet — for buying, selling, and handling. |
| Primary user role | Master-data owner; warehouse. |
| Thai SME operating reality | Thai SMEs habitually buy in one packaging and sell in another, and staff speak in packaging terms ("three boxes") rather than base units. Getting this wrong produces quantity errors that look like theft. |
| Input business facts | Packaging identity; contained quantity in base unit; barcode. |
| Output business facts | Quantity translation between how people speak and how stock is held. |
| Sale | Selling packaging. |
| Purchase | Buying packaging. |
| Manufacturing | Output packaging. |
| Accounting | Quantity errors here become valuation errors. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Approval | Change approval — changing contained quantity retrospectively corrupts historical interpretation. |
| Document | Packaging specification. |
| Reporting | Packaging-level reporting. |

### `INV-M27` Reordering Rules

| Dimension | Content |
|---|---|
| Business purpose | Hold the per-product, per-location replenishment parameters — minimum, maximum, order multiple, route, lead time — that drive automatic replenishment. |
| Primary user role | Planner or owner. |
| Thai SME operating reality | Rules are set once at implementation and then not maintained as the business changes, so they drift out of reality and start producing wrong proposals. The design must make staleness visible rather than assume maintenance. |
| Input business facts | Product; location; minimum; maximum; multiple; route; trigger mode; suspension period. |
| Output business facts | The automatic supply proposal quantity. |
| Sale | Should reflect demand pattern. |
| Purchase | Drives purchase requirements. |
| Manufacturing | Drives production requirements. |
| Accounting | Indirect — drives working capital. |
| Approval | Approval appropriate for parameters with material purchasing consequence. |
| Document | Planning parameter record. |
| Reporting | Coverage and staleness reporting. |

### `INV-M28` Barcode Nomenclatures

| Dimension | Content |
|---|---|
| Business purpose | Define how scanned barcodes are interpreted, including structured barcodes that embed quantity, weight, batch, or expiry. |
| Primary user role | Administrator. |
| Thai SME operating reality | Very relevant for Thai food and fresh-produce businesses using weight-embedded barcodes, and for those receiving international structured barcodes from suppliers. Misinterpretation silently produces wrong quantities, which is more dangerous than an outright scan failure. |
| Input business facts | Nomenclature identity; rule patterns; encoding meaning. |
| Output business facts | The interpreted product, quantity, batch, or expiry from a scan. |
| Sale | Point-of-sale and delivery scanning. |
| Purchase | Receipt scanning. |
| Manufacturing | Component scanning. |
| Accounting | A misread quantity becomes a valuation error. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Approval | Change approval — it alters interpretation of all future scans. |
| Document | Barcode standard record. |
| Reporting | Scan-error reporting. |

### `INV-M29` UoM Categories

| Dimension | Content |
|---|---|
| Business purpose | Group units of measure that are mutually convertible and define the conversion relationships within the group. |
| Primary user role | Administrator, at implementation. |
| Thai SME operating reality | Thai SMEs use a genuine mix of metric, imperial-derived trade units, and local trade units, and they buy in one and sell in another. Conversion is therefore constant, and repeated conversion is where quantity credibility is lost. |
| Input business facts | Category identity; member units; reference unit; conversion factors; rounding precision. |
| Output business facts | The conversion behaviour applied on every document that mixes units. |
| Sale | Selling unit conversion. |
| Purchase | Buying unit conversion. |
| Manufacturing | Recipe unit conversion. |
| Accounting | Conversion rounding directly changes valued quantity. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Approval | Mandatory and high-risk — changing a factor or precision retrospectively changes the meaning of existing records. |
| Document | Unit standard record. |
| Reporting | All quantity reporting depends on it. |

---

## 6. L1 Coverage Result

| Measure | Result |
|---|---|
| Menus in Boss-approved scope | 29 |
| Menus given full L1 treatment | 29 |
| Menus deferred or marked HOLD at L1 | 0 |
| Menus with an Accounting COGS dependency flag raised at L1 | 19 |
| Menus with a Thai statutory `HOLD / EVIDENCE REQUIRED` flag raised at L1 | 3 (`INV-M04`, `INV-M22`, and the numbering aspect of `INV-M21`) |

L1 is complete for 29 of 29 menus. No menu required a HOLD at this level, because L1 asks what the business means, and business meaning was determinable for every menu from the Boss scope register, the v1.0 baseline, and the Thai SME operating profile.

---

## 7. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
