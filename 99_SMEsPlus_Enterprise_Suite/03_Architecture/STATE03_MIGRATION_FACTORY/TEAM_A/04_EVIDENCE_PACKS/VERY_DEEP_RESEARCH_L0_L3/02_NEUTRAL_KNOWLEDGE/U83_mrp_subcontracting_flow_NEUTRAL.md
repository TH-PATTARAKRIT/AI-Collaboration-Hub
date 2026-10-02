# U83 Neutral Knowledge — MRP Subcontracting Flow
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U83-001 | A subcontracting Bill of Materials carries a dedicated multi-partner field that identifies which suppliers are authorised to perform the subcontracting work for that product configuration. |
| NR-U83-002 | The Bill of Materials type field is extended by the subcontracting module to include a subcontracting option; removing that option archives the BOM and reverts the type to normal. |
| NR-U83-003 | The system searches for a matching subcontracting BOM by filtering on the authorised subcontractor list; if no subcontractor is specified the search returns nothing. |
| NR-U83-004 | Manufacturing Orders for subcontracted products are triggered at the point when the corresponding receipt stock move is confirmed — that is, when the purchase order is confirmed and a receipt is generated. |
| NR-U83-005 | Only receipt moves originating from a supplier location and going to a non-supplier destination are considered as subcontract candidates when checking for a matching subcontracting BOM. |
| NR-U83-006 | When a subcontracting BOM is found, the receipt move is flagged as a subcontract move and its source location is updated to the subcontractor's virtual location. |
| NR-U83-007 | After move confirmation, a separate internal routine creates and immediately confirms the linked Manufacturing Orders, one per distinct picking, grouped by company. |
| NR-U83-008 | Manufacturing Orders are created in bulk per company in a single database write, then immediately confirmed within the same transaction as the purchase order confirmation. |
| NR-U83-009 | After creation, Manufacturing Orders are immediately confirmed so procurement rules can generate component replenishments automatically. |
| NR-U83-010 | Following MO confirmation, components are reserved against the subcontractor's virtual location via a stock assignment call on the newly created MOs. |
| NR-U83-011 | The Manufacturing Order uses the subcontractor's per-partner virtual location as both the source and destination for components; it falls back to the company-level subcontracting location if no per-partner location is set. |
| NR-U83-012 | Each company has a dedicated internal virtual location for subcontracting that serves as the default home for components and finished goods pending subcontractor handling. |
| NR-U83-013 | Each supplier partner can have a company-dependent virtual location assigned specifically for subcontracting; this overrides the company-level default. |
| NR-U83-014 | A stock location is considered a subcontracting location when it is a child of the company's dedicated subcontracting virtual location. |
| NR-U83-015 | Each warehouse has a flag (enabled by default) that controls whether automatic component resupply pickings are generated towards the subcontractor. |
| NR-U83-016 | The component resupply route is defined as a pull rule from main warehouse stock to the subcontracting virtual location, using an internal transfer operation type dedicated to subcontractor resupply. |
| NR-U83-017 | Two dedicated operation types are created per warehouse: one for Manufacturing Orders of type subcontracting (sequence SBC) and one for internal component resupply transfers (sequence RES). |
| NR-U83-018 | The warehouse stores references to the resupply route, the MTO pull rule, and the MTS pull rule for subcontractor component replenishment. |
| NR-U83-019 | Receipt validation is the trigger for automatic Manufacturing Order completion; the override runs after the standard done action. |
| NR-U83-020 | On receipt validation, all subcontract Manufacturing Orders linked to the validated picking are collected. |
| NR-U83-021 | Each linked subcontract Manufacturing Order is marked as done by calling the standard mark-done button action, effectively closing the MO automatically on receipt. |
| NR-U83-022 | The dates on all raw and finished moves of the subcontract MO are backdated to one second before the earliest receipt move line date, keeping traceability reports consistent. |
| NR-U83-023 | A Manufacturing Order locates its corresponding subcontract receipt move by following its finished product move's destination moves and filtering for the subcontract flag. |
| NR-U83-024 | The subcontractor identity on the Manufacturing Order is populated from the commercial partner of the receipt picking partner at MO creation time. |
| NR-U83-025 | A picking is considered a subcontract receipt when its operation type is incoming and at least one of its moves is flagged as a subcontract move. |
| NR-U83-026 | The accounting extension overrides the price calculation on the Manufacturing Order to compute an extra cost representing the subcontractor's service fee. |
| NR-U83-027 | The billed portion of the subcontractor fee is derived by reading the value already posted in account journal entries linked to the receipt move. |
| NR-U83-028 | Any quantity not yet billed is valued using the purchase order unit price; both billed and unbilled portions are combined into the total extra cost. |
| NR-U83-029 | The subcontractor extra cost per finished unit equals the sum of billed value and PO value for unbilled quantity, divided by total received quantity. |
| NR-U83-030 | When computing journal entry values for the finished goods move of a subcontract MO, the extra cost is subtracted to prevent double-counting because the subcontractor bill posts it separately. |
| NR-U83-031 | The extra-cost deduction from the finished goods journal entry applies only when the product uses average or FIFO costing; standard cost follows a different reconciliation path. |
| NR-U83-032 | The purchase module extension adds a counter on the purchase order showing how many component resupply pickings were generated from that order. |
| NR-U83-033 | The list of component resupply pickings for a purchase order is derived by navigating from the PO lines through their subcontract receipt moves to the linked Manufacturing Orders, then to those MOs' pickings. |
| NR-U83-034 | On a component resupply picking, the originating purchase order is found by navigating through the picking's stock references to the subcontract receipt moves and then to their purchase line's order. |
| NR-U83-035 | When a subcontract MO is confirmed, the purchase module extension injects the originating purchase order into the confirmation context so that responsible parties can be notified. |
| NR-U83-036 | For standard-cost products, when a vendor bill is received for a subcontracted purchase, the cost of the raw components consumed in the linked Manufacturing Order is added to the price-unit variance to fully reconcile the payable. |
| NR-U83-037 | Subcontracting lead time is the maximum of the vendor lead time and the sum of the manufacturing lead time plus days-to-prepare the MO, with the days-to-purchase added on top of both paths. |
| NR-U83-038 | The dropshipping-subcontracting extension enables a flow where components are shipped directly from a vendor to the subcontractor; the purchase order for those components is addressed to the subcontractor when the destination is a subcontracting virtual location. |
| NR-U83-039 | For a dropship-subcontract purchase order, the delivery address is automatically set to the subcontractor partner derived from the destination subcontracting location. |
| NR-U83-040 | When searching for an existing purchase order to aggregate a dropship-subcontract procurement, the system additionally filters by the subcontractor delivery address to avoid merging orders for different subcontractors. |
| NR-U83-041 | Component resupply moves linked to a subcontract MO via the resupply-on-order route carry the subcontractor as the partner, ensuring the internal transfer is addressed to the correct subcontractor. |
| NR-U83-042 | When computing a subcontracting BOM's cost price, the selected supplier's price (converted to company currency) is added on top of the component material cost. |
| NR-U83-043 | The subcontract Manufacturing Order is assigned the warehouse's subcontracting operation type (not the receipt operation type), giving it the SBC sequence code and MRP operation category. |
| NR-U83-044 | When marking a subcontract MO as done, consumption checks are skipped because the subcontractor has physically consumed the components outside the company's direct control. |
| NR-U83-045 | Subcontract receipt moves bypass warehouse reservation because the goods originate from the subcontractor's virtual location, not from internal warehouse stock. |
