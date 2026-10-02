# U170 — Neutral Knowledge: Stock Put-Away Rules
**Unit:** U170 | **Scope:** Warehouse put-away rules and destination location assignment
**Audience:** Non-technical reviewers, migration planners, business analysts

---

## What Are Put-Away Rules?

Put-away rules automate where incoming goods should be stored inside a warehouse. When products arrive at a receiving location (such as a goods-in bay), the system consults the rules and redirects each item to a specific sub-location (a shelf, bin, or aisle) rather than leaving everything at the top-level destination.

---

## How the System Decides Where to Put a Product

When a product arrives, the system:

1. Looks at all rules attached to the arrival location.
2. Filters those rules to the ones that match the incoming product, its category, and the type of packaging if any.
3. Ranks matching rules from most specific to least specific: a rule written for a particular product beats a rule written for its category; a rule tied to a specific package format ranks highest of all.
4. Within the same rank, rules are ordered by a numeric priority field — a smaller number is processed first.
5. The first rule whose target location has enough space (weight capacity, quantity limit, product-mix policy) is used. If no rule passes all checks, the product stays at the original destination.

---

## Rule Components (plain language)

| Component | Meaning |
|-----------|---------|
| Arrival location | The warehouse location where products are first received. Rules are defined here. |
| Storage location | The sub-location where the product should actually be placed. Must be inside the arrival location. |
| Product filter | Optional — apply rule only when this exact product variant arrives. |
| Product category filter | Optional — apply rule when the product belongs to this category (or any parent category). |
| Package type filter | Optional — apply rule only when the package is of a specific physical format. |
| Sequence / Priority | Numeric order for tie-breaking within the same specificity tier. Lower = higher priority. |
| Sub-location mode | Controls whether to use a fixed destination, the last-used location, or the nearest location with matching storage type. |

---

## Storage Categories (Capacity Constraints)

A storage category can be assigned to any warehouse location. It defines:

- **Maximum weight** the location may hold.
- **Product-mix policy**: accept anything / accept only the same product / accept only when empty.
- **Per-product quantity limit**: how many units of a specific product the location may hold.
- **Per-package-format quantity limit**: how many packages of a given type the location may hold.

When a put-away rule points to a location that has a storage category, the system checks all of these constraints before confirming the assignment. If the location would be over-capacity, the system moves to the next candidate.

---

## Package Type Integration

A put-away rule can be restricted to packages of a specific physical format. When the incoming goods arrive in a labeled package, the system first tries to consolidate them with existing packages of the same format in the target sub-locations. If no suitable existing location is found, it finds the first empty location that matches the storage category.

---

## Multi-Company Behaviour

Each put-away rule belongs to exactly one company and cannot be transferred to another company after creation. Locations may optionally be shared across companies (by leaving their company field blank), but the rules themselves remain company-specific.

---

## Sub-Location Modes

| Mode | Behaviour |
|------|-----------|
| Fixed | Product always goes to the specified storage location. |
| Last used | Product goes to wherever this product was most recently stored (based on completed transfers). Falls back to the fixed location if no history exists. |
| Closest location | System scans sub-locations that share the specified storage category and picks the one that can accommodate the product within its weight and quantity limits. |

---

## Bypass

The put-away calculation can be skipped entirely by the system during certain programmatic operations (for example, manual inventory adjustments or certain import flows). In those cases the product goes directly to the transfer's destination without consulting put-away rules.

---

## Migration Relevance

- Put-away rules, storage categories, and the links between locations and categories must all be migrated together.
- Company assignments on rules must be validated against the new company structure.
- Storage category capacity records (per-product and per-package-type quantity limits) are separate child records under each category and must be carried over.
- The `sublocation` mode on each rule must be preserved, as it changes runtime behaviour significantly.
