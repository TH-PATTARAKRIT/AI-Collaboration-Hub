# U112 — Product Variant Explosion: Neutral Knowledge Layer
## Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

This layer explains the variant explosion mechanism using plain language only.
No identifiers, no technical tokens, no code keywords.

---

### N-U112-01: The Attribute Model
A product attribute is a named property (for example "Color" or "Size") that a product can have. Attributes are ordered by a sequence number, which controls the display order when a buyer configures a product.

### N-U112-02: The Variant Creation Mode Field
Every attribute carries a setting that decides how the system should handle the creation of concrete product records when this attribute is applied to a product. This setting has three possible choices and defaults to the first option, which creates all combinations immediately.

### N-U112-03: Immediate Creation Mode
When an attribute is set to immediate mode, the system generates all possible product combinations as soon as any value for that attribute is assigned to a product. No further user action is required.

### N-U112-04: On-Demand Creation Mode
When an attribute is set to on-demand mode, no product combination records are created in advance. A concrete product record is only created the first time a customer or salesperson selects that exact combination on a sales order.

### N-U112-05: Never-Create Mode
When an attribute is set to never-create mode, no separate product records are ever created for the combinations of that attribute. The chosen value travels with the sales order line itself rather than being stored as a distinct product record. This is useful for options that vary per order but do not require separate stock tracking.

### N-U112-06: Locked Mode After Use
Once an attribute has been assigned to at least one product, its creation mode cannot be changed. Attempting to change it will produce a warning listing the affected products and block the operation.

### N-U112-07: Multi-Checkbox Restriction
A display format that shows attribute values as a group of checkboxes (allowing multiple selections simultaneously) is only permitted when the attribute uses the never-create mode. This rule is enforced at the database level, not only by the application logic.

### N-U112-08: The Attribute Line
The attribute line is an intermediate record that sits between a product and one of its attributes. It holds the specific set of values that have been selected for that attribute on that particular product. Think of it as the row in a configuration table that says "this product uses this attribute with these possible values."

### N-U112-09: Automatic Sync After Adding a Line
When a new attribute line is added to a product, the system automatically aligns all the intermediate value records and then triggers variant generation, unless a context flag has been set to postpone those actions.

### N-U112-10: Automatic Sync After Editing a Line
Editing the values on an attribute line (for example, adding or removing a color option) likewise triggers the same alignment and variant regeneration, unless the same context flag suppresses it.

### N-U112-11: Cleanup After Removing a Line
Deleting an attribute line causes the system to immediately remove any resulting surplus variants from the product, in addition to cleaning up the intermediate value records.

### N-U112-12: The Template Attribute Value
For each value selected on an attribute line, a dedicated materialised record is created. This record acts as the bridge between the general attribute definition and the specific product, and is the building block that gets combined into variant records.

### N-U112-13: Extra Price on Each Value
Every materialised value record stores an extra price amount. When a variant that includes this value is sold, this amount is added on top of the product's base sale price.

### N-U112-14: Non-Standard Active Flag
These materialised value records use their own active indicator rather than the standard ORM active field. This design allows the records to remain visible in certain views even when they are deactivated, without being subject to the framework's default invisible-when-inactive filter.

### N-U112-15: Seeding Extra Price from Attribute Value
When a new materialised value record is created for an attribute line, its extra price is pre-filled from a default extra price stored on the underlying attribute value definition. This allows a product designer to set a global price suggestion at the attribute level.

### N-U112-16: Exclusion Rules Trigger Rebuild
When a rule is added or changed that declares two attribute values incompatible with each other, the system immediately rebuilds all variant combinations for the affected product. This ensures that newly excluded combinations are removed and previously impossible combinations that become valid are created.

### N-U112-17: Cascade Removal on Value Deletion
Removing a materialised value record first attempts to remove or archive every product variant that currently uses that value, before the value record itself is deleted.

### N-U112-18: The Central Variant Generation Method
There is a single entry-point method responsible for creating, activating, and deactivating all product variants for a given set of product templates. It is called after template creation, after attribute lines are modified, or when a template is reactivated. Its job is to reconcile the actual variant records in the database against the set of combinations that should currently exist.

### N-U112-19: Filtering Out Never-Create Attributes
At the start of variant generation, all attribute lines that use the never-create mode are removed from consideration. Those attributes contribute no dimension to the combination space.

### N-U112-20: Skipping Pre-Generation for On-Demand Attributes
If any remaining attribute line uses the on-demand mode, the system skips generating new variants entirely. It only checks whether existing variants have become invalid and should be deactivated.

### N-U112-21: Cartesian Product Computation
When all remaining attributes use the immediate mode, the system computes all possible combinations as the mathematical Cartesian product of the selected values across each attribute line. An iterator is used instead of building the full list in memory, avoiding exhaustion of resources when the combination count is large.

### N-U112-22: Safety Cap on Variant Count
A system configuration parameter sets a maximum number of variants that can be pre-generated from a single product. The default limit is one thousand. If a product's configuration would produce more combinations than this limit, the operation is blocked and the user is informed.

### N-U112-23: Respecting Template Active State
Before reactivating archived variants, the system checks that the parent product template is itself active. Variants whose template is archived are not reactivated even if their combination would otherwise be valid.

### N-U112-24: Removal of Obsolete Variants
After creating new variants, variants that no longer correspond to any valid combination are removed. The removal process tries deletion first, falling back to archiving when foreign-key constraints in other parts of the system prevent full deletion.

### N-U112-25: Guard Against Leaving No Variants
After removing obsolete variants, the system verifies that the product template itself still exists. If removing surplus variants caused the entire template to be deleted (because no variant remained), a user error is raised to alert the user.

### N-U112-26: Variant Inherits From Template
The product variant record is a sub-record of the product template via a delegation inheritance mechanism. Fields defined on the template are directly accessible on the variant without storing them separately, because the variant holds a mandatory reference to its parent template.

### N-U112-27: Combination Encoded as Related Values
Each variant record carries a set of references to materialised attribute value records. This set precisely encodes the attribute combination that defines the variant.

### N-U112-28: Index Key for Combination Lookup
The set of materialised value references is also stored as a sorted comma-separated string of identifiers in a separate indexed field. This string serves as a fast lookup key, allowing the system to find the variant for a given combination without scanning the join table.

### N-U112-29: Uniqueness Enforced at Database Level
A partial index at the database level ensures that no two active variants for the same product template share the same combination-index string. Archived variants are excluded from this constraint, which allows the same combination to exist as both an active and an archived record.

### N-U112-30: Variant Extra Price as Sum
The total extra price shown on a variant record is computed as the arithmetic sum of the extra prices from all the materialised value records in its combination. This sum is recalculated whenever any individual extra price changes.

### N-U112-31: Selling Price Formula
The selling price of a variant is the product template's base list price plus the variant's total extra price. This computed value is the price shown to customers.

### N-U112-32: Inverse Price Setting
When the selling price is edited directly on a variant, the system back-calculates the base list price by subtracting the total extra price from the entered value and stores the result on the template.

### N-U112-33: Combination Index Stays Current
The combination-index string is recomputed automatically whenever the set of attribute values on a variant changes, keeping the lookup index consistent with the actual combination.

### N-U112-34: Resilient Removal Strategy
The removal-or-archive method used for obsolete variants is designed to be resilient. It first tries to remove all records in one batch. If that fails due to constraints, it splits the batch in half and retries each half recursively. If a single record still cannot be removed, it is archived instead.

### N-U112-35: Automatic Variant Creation on New Product
Whenever a new product template is saved, the variant generation method is called automatically. The caller can suppress this by passing a context flag.

### N-U112-36: Conditional Rebuild on Edit
Editing a product template triggers variant regeneration only if the attribute configuration (the set of attribute lines) is among the changed fields, or if the template is being reactivated and currently has no variants.

### N-U112-37: Archiving Cascades to Variants
When a product template is archived, all of its variants are archived in the same operation, keeping the dataset consistent.

### N-U112-38: Context-Injected Extra Price for Template Price Computation
When computing a sale price for a product template in the context of a specific combination, the sum of attribute extra prices for that combination is passed through the request context as a tuple and added to the base list price during computation.

### N-U112-39: Detecting On-Demand Mode on a Template
A product template is considered to have at least one on-demand attribute if any of its valid attribute lines references an attribute that uses the on-demand creation mode.

### N-U112-40: Complete Combination Possibility Check
A combination is deemed possible only when all of the following conditions are true: it conforms to the template's attribute configuration, the corresponding variant exists and is active (for non-on-demand products), no own exclusion rule blocks it, and no exclusion rule from a parent product blocks it.

### N-U112-41: Archived Variant Blocks Combination
For products in on-demand mode, an archived variant for a given combination makes that combination impossible to select. For products in immediate mode, the combination is also impossible if the variant does not exist at all or is archived.

### N-U112-42: No-Variant Attributes Excluded from Physical Record
When a variant is created on demand from a combination that includes never-create attribute values, those never-create values are not stored on the physical variant record. They exist only on the order line.

### N-U112-43: Combination Filter Logic
The combination filter validates candidates by checking three things: the count of non-multi-checkbox attribute values matches the template's configuration, the attribute lines referenced by the combination match the lines on the template, and no exclusion rule connects two values that are both present in the combination.

### N-U112-44: Default Extra Price on the Global Value
The global attribute value definition carries a default extra price field that is used to seed the extra price on new template-specific value records whenever that value is added to a product.

### N-U112-45: Free-Text Custom Values
A flag on the global attribute value definition allows customers to enter free-text input for that value. When this flag is set, the attribute line is treated as configurable even when only one value is defined.

### N-U112-46: Variant Preparation Before Creation
Before each new variant record is inserted into the database, a preparation step assembles the creation dictionary, including the parent template reference, the set of attribute value references, and the active state mirroring the template.

### N-U112-47: Archived Variants Included in Rebuild
During variant generation, previously archived variants are included in the set of candidates so that a combination that was previously archived and then re-enabled can be restored to active rather than creating a duplicate record.

### N-U112-48: Single-Value Lines Handled Without Regeneration
When an attribute line has exactly one active value, adding or updating it does not trigger a full Cartesian product regeneration. Instead, that single value is written directly onto all existing variants, preserving their configuration.

### N-U112-49: Template Attribute Value Synchronisation
The synchronisation method reconciles the set of intermediate value records against the currently selected values on the attribute line. It removes records for values that have been deselected, restores records for values that were archived but re-selected, and creates records for newly added values.

### N-U112-50: Variant Possibility Delegated to Template
When checking whether a specific existing variant is valid (for example when filtering a product configurator), the variant delegates the decision entirely to its parent template's combination-possibility method, passing its own stored attribute values.
