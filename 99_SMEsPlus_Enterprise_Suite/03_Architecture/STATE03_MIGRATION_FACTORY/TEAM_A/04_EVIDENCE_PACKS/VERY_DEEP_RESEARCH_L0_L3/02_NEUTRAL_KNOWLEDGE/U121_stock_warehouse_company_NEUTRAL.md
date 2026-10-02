# U121 — Warehouse-Company Binding and Inventory Isolation
## Plain Business Language Summary
## Date: 2026-10-02
## Gap ID: GAP-003
## Function IDs: MCT-F05, INV-F01

---

## How Warehouses Bind to Companies

Every warehouse in Odoo belongs to exactly one legal entity (company). This binding is set at the moment the warehouse is created and cannot be changed afterwards — any attempt to reassign a warehouse to a different company is blocked with an error. The warehouse automatically inherits its name and short code from the company if none are provided.

When a warehouse is created, all of its physical storage areas (the main stock area, input zone, quality control area, output area, and packing zone) are automatically assigned to the same company as the warehouse. This means the entire physical structure of a warehouse is anchored to one legal entity.

The system also enforces uniqueness: no two warehouses in the same company can share the same name or the same short code. This ensures that operation references (like receipt or delivery numbers) are unambiguous within each company.

---

## How Record Rules Prevent Cross-Company Inventory Access

Odoo enforces a set of built-in security filters that restrict what each user can see based on the companies they are currently logged into. These filters (called record rules) apply to every inventory object and are always active:

- **Warehouses**: users only see warehouses belonging to their active company or companies.
- **Transfers and Transfer Lines**: users only see stock transfers stamped with their active company. Transfer company is automatically set from the operation type and cannot be manually changed.
- **Stock Movements**: every movement of goods is stamped with a company; users only see movements for their active companies.
- **Inventory Positions (Quants)**: the physical stock held at a location inherits the location's company. Users only see stock positions in locations belonging to their active companies.
- **Locations**: a location either belongs to a specific company (in which case it is hidden from other companies) or belongs to no company, in which case it is visible to everyone as a shared virtual location (for example, the global Vendors and Customers virtual locations).
- **Lots and Serial Numbers, Packages, Putaway Rules, Reordering Rules, Stock Rules, Routes, Storage Categories**: all of these objects are similarly filtered by company.
- **Scrap Operations**: fully isolated to a single company with no shared-company fallback.

The security rules are defined at installation and are marked as non-updatable, meaning they cannot be accidentally overwritten during a module upgrade.

---

## Transit Locations for Inter-Company and Inter-Warehouse Goods Movement

Two kinds of transit locations exist in Community edition:

1. **Per-company internal transit location**: when a company is first created, a dedicated transit storage area is automatically created and attached to that company. This location is initially hidden (inactive). It becomes relevant when two warehouses within the same company want to replenish stock from each other — goods pass through this transit area as an intermediate stop, so no accounting entry is generated between the two sites.

2. **Global inter-company transit location**: a single shared transit location with no company affiliation exists in the system. It is also initially hidden and is activated the moment a second company is added to the database. It serves as the logical handoff point when goods are intended to cross from one legal entity's possession to another's. However, in Community edition, the automated creation of matching purchase and sales orders between companies (the full inter-company trade flow) requires the Enterprise inter-company rules module, which is not part of the Community source. Community provides the transit location infrastructure but not the automated order generation.

When the system classifies a stock movement as incoming or outgoing, transit locations with no company are treated the same way as supplier or customer virtual locations — they signal that goods are crossing a company boundary.

---

## Quant (Inventory Position) Company Isolation

A quant records how much of a given product exists at a specific location, lot, and package. Its company is not stored independently — it is automatically derived from the company of its storage location. This means there is no way to place company A's stock into company B's location, because the quant's company is always exactly whatever company owns that location. If a location has no company (a shared virtual location), then the quant likewise has no company.

---

## Operation Types and Their Role in Company Binding

Each warehouse operation type (receiving, delivering, internal transfer) also carries a company, set at creation and immutable thereafter. Since a transfer's company is derived from its operation type, choosing the wrong operation type cannot silently switch a transfer to the wrong legal entity — the operation type itself is the single source of truth for company assignment on a transfer.

---

## Summary for GAP-003 Assessment

Warehouse-to-company binding is enforced by required fields, immutability guards, and database uniqueness constraints. Inventory isolation across companies is enforced by 14 record-rule filters covering every stock model. Transit infrastructure for intra-company and inter-company goods movement is present in Community. The gap between Community and Enterprise lies in automated inter-company order generation, which is an Enterprise-only feature; Community only provides the transit location plumbing.
