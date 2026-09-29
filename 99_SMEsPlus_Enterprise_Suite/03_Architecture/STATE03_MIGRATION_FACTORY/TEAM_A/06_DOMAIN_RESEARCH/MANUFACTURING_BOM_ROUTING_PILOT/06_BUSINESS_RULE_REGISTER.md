> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Business Rule Register | Documentation-Tier (WebSearch synthesis — direct WebFetch to odoo.com blocked in this container, same constraint as every prior Deep Study unit)

# 06 — BUSINESS RULE REGISTER

### BRP-F01 — BOM Type selection (Manufacture / Kit / Subcontracting)

- **WHAT**: A Bill of Materials has a `BoM Type` field with exactly three values: **Manufacture this product** (the product is built in-house from the listed components via a Manufacturing Order), **Kit** (the product is a set of unassembled components bundled for sale, not built via an MO), **Subcontracting** (production of the components/product is outsourced to one or more named subcontractors).
- **WHY**: One product master can have fundamentally different production models depending on business context (built in-house vs. bundled vs. outsourced); the BoM Type is the single switch that tells the system which model applies.
- **BUSINESS RULE**: The three types are mutually exclusive per BoM — a BoM is one type, not a blend. Subcontracting additionally requires naming one or more subcontractors in a dedicated field once selected.
- **STATE**: BoM created → Type selected → downstream behavior (MO creation eligibility, component listing requirement, valuation model) branches by type.
- **DATA CONCEPT**: The BoM record itself is the single source of the routing decision — not a separate configuration elsewhere.
- **CONTROL**: Selecting Subcontracting requires the Subcontracting feature to be enabled first (Manufacturing → Configuration → Settings); selecting Kit requires no separate feature toggle documented this round.
- **DEPENDENCY**: Feeds `BRP-F02` (Kit) and `BRP-F03` (Subcontracting) directly — this function is the router, those are its two non-default branches. Also feeds Gx7's `MFG-F01`/`MFG-F02` (the "Manufacture this product" branch is exactly Gx7's scope).
- **EVENT**: "BoM Type set" — a configuration event, not a transactional one.
- **RISK**: Choosing the wrong type is a structural error, not a cost-detail error — e.g., modeling a bundled-for-sale product as "Manufacture this product" would create unnecessary Manufacturing Orders and WIP postings for something that should just pass component value through directly.
- **UNKNOWN**: Whether the BoM Type can be changed after the BoM is already in use by open Manufacturing/Sales Orders, or whether it locks — `SOURCE/RUNTIME VERIFICATION REQUIRED`.

### BRP-F02 — Kit BOM (components-only, no Manufacturing Order)

- **WHAT**: A Kit BoM lists components under the Components tab; no Operations/routing configuration is needed or expected, since a Kit does not go through a Manufacturing Order — it is a sales-side bundling of components sold together as one product line.
- **WHY**: Some products are sold as a set (e.g., a furniture item shipped as separately-boxed parts) without ever being "manufactured" as a distinct value-adding event — a Kit BoM lets one sales line explode into multiple stock-moved components at delivery, without an MO in between.
- **BUSINESS RULE**: **"Kit Value Does Not Change"** — the documented rule is explicit that the stock's value is the same whether or not the kit product itself is tracked; a Kit is not an independent valuation object, it's a bundling label over its components' own values.
- **STATE**: Sales order line for the kit product → delivery → the component stock moves execute directly (no separate MO state machine in between).
- **DATA CONCEPT**: The kit "product" is a sellable identity, not a stock-valued entity in its own right — value lives entirely at the component level.
- **CONTROL**: No manufacturing operations configuration is necessary for a pure sell-only kit (per documentation: "if the kit is solely being used as a sellable product, then only components need to be added").
- **DEPENDENCY**: Distinct from `BRP-F01`'s "Manufacture" branch and from Gx7's MFG-F01/F02 (no WIP account, no consumption-to-WIP posting) — a Kit is the one BoM type Gx7's valuation-timing rule does not apply to, because there is no manufacturing financial event at all.
- **EVENT**: "Kit delivered" → component-level stock moves only; no kit-level financial posting.
- **RISK**: Low for valuation (value simply passes through); the real risk is process — treating a Kit as manufactured would introduce unneeded MO/WIP machinery for something that structurally has none.
- **UNKNOWN**: Whether a Kit can *also* have manufacturing operations configured (a hybrid case, for e.g. light assembly before shipping) and if so how valuation then behaves — the documentation this round distinguishes "sell-only" Kits but does not fully characterize a manufactured-Kit hybrid — `SOURCE/RUNTIME VERIFICATION REQUIRED`.

### BRP-F03 — Subcontracting BOM (outsourced production)

- **WHAT**: A Subcontracting BoM names one or more subcontractors instead of listing components in the ordinary Components tab (documentation: "there is no need to list any components in the Components tab of the BoM" for this type). Physical raw materials are sent to a **Subcontracting Location**, which is configured as an **Internal Location** type (not a Customer/external location), even though it represents the subcontractor's own premises.
- **WHY**: The business needs to outsource physical production while retaining financial and stock ownership of the materials until the subcontractor's finished output actually returns — treating the subcontractor's site as an internal location is the mechanism that achieves this.
- **BUSINESS RULE**: **"Sending raw materials to your subcontractors does not impact the inventory valuation, as the components are still valued as part of your stock."** This is the single most important, non-obvious rule in this pilot — the physical location changes (materials leave your warehouse) but the financial/valuation ownership does not, because the destination is modeled as internal, not external.
- **STATE**: Components at home warehouse → transferred to Subcontracting Location (internal move, no valuation change) → subcontractor produces → finished good returns to home warehouse (the point at which the produced-good side of the transaction is realized).
- **DATA CONCEPT**: The Subcontracting Location is a distinct location record, typed Internal, scoped to a specific subcontractor (or shared) — a location-type control, not a partner-type control, is what preserves valuation continuity.
- **CONTROL**: Requires the Subcontracting feature enabled (Manufacturing → Configuration → Settings) before the BoM Type option becomes selectable.
- **DEPENDENCY**: Interacts with Gx7's WIP/valuation model at the point the subcontractor's output returns — that return event is the analog of Gx7's "production completion" for this BoM type, though the mechanics of costing the subcontractor's own labor/fee were not evidenced this round (see UNKNOWN).
- **EVENT**: "Components sent to subcontracting location" (no valuation change) → "Subcontracted product received" (valuation event, mechanics not yet evidenced).
- **RISK**: **C1, financial-control-adjacent** — if the Subcontracting Location were ever misconfigured as an external/Customer-type location, it would incorrectly remove the components from stock valuation on transfer, understating inventory value and misstating the balance sheet during the outsourced-production window. This is exactly the kind of configuration-dependent financial-control risk this Deep Study exists to surface.
- **UNKNOWN**: How the subcontractor's own fee/labor cost is captured and valued into the returned product (a vendor bill against a subcontracting-fee product, a landed-cost-style addition, or something else) — not evidenced this round; **`TARGETED VALIDATION NEEDED`**, official-doc pass focused specifically on subcontracting cost capture, or AWT.

> **RESOLUTION UPDATE (2026-09-29, same day, further search)**: `GAP-BRP-03` closed at documentation-tier (V2). The vendor price set on the subcontracted product represents what is paid to the subcontractor for parts and service time; product cost = component cost + that service/fee figure. **Once the vendor bill is posted, the Finished Goods Valuation Account is debited** — capturing the subcontracting fee into the finished product's valuation at vendor-bill-posting time. This is consistent with (an additional data point for, not a further self-confirmation of) the already-flagged, Boss-designated `Material Finding — Independently Unverified` valuation-timing reconciliation (post at financial-transaction/vendor-bill time) — recorded here as disclosed corroborating evidence only, per the same discipline applied to `MFG-F05`. Source: `EV-BRP-08` (mixed official-doc/partner-blog synthesis this round — see Provenance Register).

### BRP-F04 — Work Center configuration (Cost per hour, Allowed Employees)

- **WHAT**: A Work Center record defines where Manufacturing work orders are physically processed, with at minimum a name, a **Cost per hour** (the operating expense rate of that work center), and an **Allowed Employees** field (if blank, all employees may work there).
- **WHY**: Manufacturing cost is not just component cost — labor/operations time must be priced, and different physical stations (a CNC machine vs. a manual assembly bench) plausibly cost different amounts per hour; Work Centers are the unit that carries that rate.
- **BUSINESS RULE**: Specifying a Work Center is **required** when a work order is defined in a BoM's Operations tab — a routing step cannot exist without a named Work Center to attach its cost rate to.
- **STATE**: Work Center created → Cost per hour set → referenced by one or more BoM Operations (`BRP-F05`) → consumed at MO execution time as an input to `MFG-F04` (Gx7's MO cost computation).
- **DATA CONCEPT**: The Work Center is a shared, reusable configuration object — one Work Center can be referenced by many BoMs/operations, so a rate change retroactively affects the cost model of every operation that cites it (for future, not-yet-costed MOs).
- **CONTROL**: `Allowed Employees` is an authorization-adjacent control (who may log time/execute a work order at that station), separate from the cost-rate control.
- **DEPENDENCY**: Direct input to Gx7's `MFG-F04` (MO cost computation) — this pilot supplies the *rate*, Gx7 already covers *how* that rate combines with component cost into the final MO cost figure.
- **EVENT**: "Work order processed at Work Center" — a time/capacity event, not itself a financial-posting event (the financial effect is realized later, through MFG-F04's computed cost feeding MFG-F01/F02's postings).
- **RISK**: Misconfigured or stale Cost per hour silently misvalues every future MO through that Work Center — a slow-to-notice, cumulative risk rather than a single transactional error.
- **UNKNOWN**: Whether Cost per hour supports time-based variation (e.g., shift differentials, overtime rates) or is a single flat figure — not evidenced this round; `SOURCE/RUNTIME VERIFICATION REQUIRED`, non-blocking (not C1 on its own).

### BRP-F05 — Routing Operations / Work Orders (per-BOM operation steps)

- **WHAT**: Routing is defined through **Operations** entries directly on a BoM (not a separate "Routing" master record in the documentation surfaced this round) — each Operation names a step, the Work Center where it happens, and an expected duration in minutes.
- **WHY**: A single BoM often requires more than one production step (e.g., cut → assemble → finish); Operations sequence those steps and attach each to the Work Center that will price it.
- **BUSINESS RULE**: Enabling "Work Orders" (Manufacturing → Configuration → Settings) is a prerequisite before Operations/routing become available on a BoM at all — without it, a BoM presumably behaves as a single undifferentiated production step (not independently confirmed this round; see UNKNOWN).
- **STATE**: Work Orders feature enabled → BoM Operations tab populated (step name + Work Center + expected duration) → at MO execution, each Operation becomes a trackable Work Order instance.
- **DATA CONCEPT**: An Operation is BoM-scoped (belongs to one BoM's routing), while a Work Center (`BRP-F04`) is a shared, cross-BoM resource — the same one-to-many relationship pattern as most master-data/transaction-line designs.
- **CONTROL**: Expected duration is a planning input (capacity/scheduling), not itself a hard constraint documented this round — whether actual time is validated against expected duration was not evidenced.
- **DEPENDENCY**: Multiplies with `BRP-F04`'s Cost per hour to produce the operations-cost component of Gx7's `MFG-F04`; also the scheduling/capacity layer the Learning Priority Matrix's Wave 5 groups under "Manufacturing/MRP."
- **EVENT**: "Work Order started/completed" per Operation — time-tracking events feeding cost, distinct from Gx7's stock-valuation posting events.
- **RISK**: An under- or over-estimated expected duration misprices the operations-cost component of every MO using that routing, compounding with any `BRP-F04` rate error.
- **UNKNOWN**: Behavior of a BoM with Work Orders *disabled* (does routing/operations simply not exist, or is there a simpler single-step cost model?) and whether actual-vs-expected duration variance is tracked/reported — both `SOURCE/RUNTIME VERIFICATION REQUIRED`, non-blocking.
