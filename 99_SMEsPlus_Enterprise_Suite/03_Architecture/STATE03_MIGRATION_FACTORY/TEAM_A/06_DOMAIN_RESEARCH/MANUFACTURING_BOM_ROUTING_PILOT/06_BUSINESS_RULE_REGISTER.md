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

> **CLASSIFICATION (Boss's "STATE03 Corrective Checkpoint Prompt" §B4, 2026-09-29): `Conditional Reference Finding — requires version, installed-module, location/ownership, costing/valuation configuration, and evidence-pointer scope.`** The valuation-non-impact rule below is conditional on Odoo 19.0 (not independently confirmed for other versions), the Subcontracting feature being enabled, the Subcontracting Location actually being configured as an Internal Location, and the exact pointers in `19_PROVENANCE_REGISTER.md` (`EV-BRP-04`/`05`/`08`). **Not a universal accounting statement; not SMEsPlus target behavior** — Odoo-reference learning input only, per the Master Prompt's Clean-Room boundary. Full detail: `STATE03_CORRECTIVE_CHECKPOINT_RESPONSE.md` §B4.

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

### BRP-F06 — Reordering Rules (min/max automatic replenishment)

> **CLASSIFICATION (per Boss's "STATE03 Population Lineage Correction & Autonomous Continuation" §3, 2026-09-29): `Configuration-scoped reference constraint — Odoo 19.0, Inventory app, Replenishment configuration only. Not a universal business rule; not a target-design decision.`**

- **WHAT**: A Reordering Rule keeps a product's forecasted stock above a minimum threshold without exceeding a maximum, by specifying min/max quantities; when set to automatic, Odoo generates a new supply order (purchase or manufacturing) itself, when set to manual, Odoo instead suggests the order on a replenishment report for a person to confirm.
- **WHY**: Immediate, ongoing replenishment needs a rule-based trigger rather than someone watching stock levels manually.
- **BUSINESS RULE**: Automatic vs. manual is a per-rule setting, not a global one — different products can use different modes.
- **STATE**: Forecasted stock crosses below minimum → (automatic: order generated immediately) or (manual: order surfaced on the replenishment report, awaiting confirmation).
- **DATA CONCEPT**: The rule is a per-product(-location) record — min/max is not a product-master-level field, it is scoped to where replenishment applies.
- **DEPENDENCY**: Directly conflicts with `BRP-F07` (Master Production Schedule) if both are applied to the same product — see BRP-F07's own BUSINESS RULE.
- **EVENT**: "Reordering rule triggered" → supply-order creation or suggestion, not itself a financial posting — the resulting document's own posting timing (already characterized elsewhere in this Deep Study, e.g. Gx1's `GRV` functions for the resulting purchase) applies from there.
- **RISK**: A misconfigured min/max either starves operations (too low) or ties up working capital in excess stock (too high) — a business-tuning risk, not a structural one.
- **UNKNOWN**: Whether automatic mode has any approval/authorization gate before order creation, or is fully unattended — `SOURCE/RUNTIME VERIFICATION REQUIRED`, non-blocking.

### BRP-F07 — Master Production Schedule (long-term manual demand-driven planning)

> **CLASSIFICATION (per Boss's "STATE03 Population Lineage Correction & Autonomous Continuation" §3, 2026-09-29): `Configuration-scoped reference constraint — Odoo 19.0, Manufacturing app, MPS/Planning feature enabled. Not a universal business rule; not a target-design decision.`** The `BRP-F06`/`BRP-F07` mutual-exclusivity warning below is Odoo's own documented guidance for its own feature pair — it is disclosed as reference input for SMEsPlus's own future replenishment/planning design, not adopted or assumed as SMEsPlus's rule.

- **WHAT**: The MPS plans longer-term replenishment against a manually-adjustable demand forecast, intended for products/components with long lead times or seasonal variability — distinct from the immediate, threshold-driven mechanics of `BRP-F06`.
- **WHY**: Some supply decisions need to be made well ahead of an actual stock shortfall (long lead-time components, seasonal demand), which a simple min/max threshold cannot anticipate.
- **BUSINESS RULE**: **Explicit incompatibility with `BRP-F06`** — the documentation states Reordering Rules should not be applied to products already on the MPS, because doing so creates inaccurate forecasts and unnecessary replenishment orders. A product uses one mechanism or the other, not both.
- **STATE**: Forecast entered/adjusted manually → MPS displays planned vs. actual → replenishment is driven by the plan, not an automatic threshold-cross event.
- **DATA CONCEPT**: A planning/forecast record layered over a product, not a transactional document itself.
- **CONTROL**: Manual by nature — the documentation frames MPS as relying on human-adjusted forecasts, not automation.
- **DEPENDENCY**: Mutually exclusive with `BRP-F06` per product; otherwise independent of this pilot's other functions.
- **EVENT**: No automatic event — MPS is a display/planning surface, not itself a trigger.
- **RISK**: Low direct financial/stock risk (no automatic action), but applying it to the wrong product class (short lead-time, stable demand) wastes the planning effort `BRP-F06` would have handled automatically.
- **UNKNOWN**: Whether MPS forecasts feed any other automated process besides guiding a human's own manual order placement — `SOURCE/RUNTIME VERIFICATION REQUIRED`, non-blocking (not C1).

### BRP-F08 — By-Products (secondary output tracked via BOM)

- **WHAT**: A BoM can declare one or more By-Products — additional output products created alongside the primary finished good — once the By-Products setting is enabled; each by-product entry specifies a quantity and, optionally, which routing Operation produces it.
- **WHY**: Some production processes genuinely yield more than one usable output (e.g., a cutting process yielding both a primary piece and a usable offcut); the system needs to track and value both, not just the primary good.
- **BUSINESS RULE**: By-Products requires an explicit feature toggle (Manufacturing → Configuration → Settings) before the By-products tab becomes available on a BoM — same feature-gating pattern as Subcontracting (`BRP-F03`) and Work Orders (`BRP-F05`).
- **STATE**: MO confirmed/completed → primary finished good produced → declared by-product quantities also enter stock, at the Operation named (if any).
- **DATA CONCEPT**: A by-product is a distinct product record with its own stock/valuation identity — it is not a scrap or waste record, it is trackable inventory.
- **DEPENDENCY**: Directly interacts with the overall MO cost figure (`MFG-F04`, Gx7) — if total production cost must now be allocated across primary good *and* by-product(s), this changes what "the" cost of the primary good means.
- **EVENT**: "By-product produced" — a stock-entry event alongside the primary good's own completion event.
- **RISK**: **Material, financial-control-adjacent** — how cost is allocated across primary output and by-product(s) directly affects the recorded unit cost of the main product; an unevidenced allocation method here is exactly the kind of "documented as configured, not confirmed as enforced" gap this Deep Study exists to surface.
- **UNKNOWN**: The precise cost-allocation method between primary product and by-product(s) (proportional value, a fixed by-product valuation with the remainder to the primary good, or something else) — not evidenced this round; **`TARGETED VALIDATION NEEDED`**.

> **CLASSIFICATION (per Boss's "STATE03 Population Lineage Correction & Autonomous Continuation" §3, 2026-09-29): `Conditional / Unknown — requires version, module, and configuration scope; not a universal accounting statement and not SMEsPlus target behavior.`** This finding is Odoo-reference learning input only, per the Master Prompt's Clean-Room boundary — SMEsPlus has not adopted, designed, or committed to any by-product cost-allocation model.

> **PARTIAL EVIDENCE UPDATE (2026-09-29, same day, targeted follow-on search per Boss's instruction to continue documentation/source/configuration analysis on this C1 gap now)**: A candidate default disposition was found — "by default, no material cost is allocated to the by-products manufactured, therefore full production cost is charged to the main finished good" (`EV-BRP-13`, third-party marketplace listing; `EV-BRP-14`, pre-19/V12 community forum, independently corroborating). **This is explicitly not officially confirmed**: the official `mo_costs.html` documentation page (`EV-BRP-11`'s own source, re-queried this round) does not itself state a by-product cost-allocation rule. Actual V remains **V1** (third-party-listing + pre-19-forum corroboration, not official documentation, not Odoo-19-version-confirmed) — **not upgraded to V2**. `GAP-BRP-09` therefore moves from "no candidate found" to "candidate default disclosed, sub-documentation-tier, `Open/Conditional`" — it does **not** move to Resolved.
>
> **Negative-case design (documentation-tier only, no runtime access)**: if this candidate default holds, the negative/edge case worth testing at AWT is — a BoM with a By-Product whose own market value **exceeds** the primary finished good's (e.g., a valuable co-product mislabeled as a "by-product" for BoM-configuration convenience): under a "zero-allocation-to-by-product" default, the primary good's unit cost would be inflated by the *entire* production cost while the more valuable by-product enters stock at zero or unset cost — a real, discoverable financial-misstatement risk if the by-product/co-product distinction is not made deliberately. This scenario is designed now, at documentation-tier, as a target for future AWT runtime confirmation (`BGQ-04`) — not executed, not claimed as observed.

### BRP-F09 — Multi-level BOM (nested sub-assemblies)

- **WHAT**: A BoM's component can itself be a manufactured product with its own BoM (a sub-assembly/semifinished product); Odoo resolves this recursively — confirming a manufacturing order for the top-level product can generate manufacturing or purchase orders for every sub-assembly down the chain.
- **WHY**: Real products are frequently built from sub-assemblies that are themselves built (not just purchased), and the system needs to plan/cost/track that whole chain, not just one level.
- **BUSINESS RULE**: Multilevel BoMs are recommended specifically when a sub-assembly is reused across multiple finished products (build the shared sub-assembly's BoM once, reference it from many parents), rather than duplicating the sub-assembly's structure inside every parent BoM.
- **STATE**: Top-level MO confirmed → system resolves the BOM tree → generates the necessary downstream supply documents (further MOs for manufactured sub-components, purchase orders for purchased ones) at each level.
- **DATA CONCEPT**: A recursive parent-child structure — a BoM's component list can itself point to another BoM, not just to a "flat" purchasable/stockable item.
- **CONTROL**: A BOM Overview / hierarchy view is documented as letting a user expand or collapse sub-assembly levels for inspection.
- **DEPENDENCY**: **Compounds every other function in this pilot at each level** — `BRP-F01`'s type routing, `BRP-F03`'s subcontracting rule, `BRP-F04`/`F05`'s cost/routing inputs, and `BRP-F08`'s by-product allocation can each apply independently at every level of the tree, not just at the top.
- **EVENT**: "Top-level MO confirmed" → cascading document-generation events down the BOM tree.
- **RISK**: Compounding — an error at any single level (wrong BOM type, misconfigured work center, unevidenced by-product allocation) propagates upward into every product that consumes that sub-assembly, not just the immediate parent.
- **UNKNOWN**: Whether cost changes at a lower level automatically re-cost already-completed higher-level MOs, or only affect future ones — not evidenced this round; `SOURCE/RUNTIME VERIFICATION REQUIRED`.
