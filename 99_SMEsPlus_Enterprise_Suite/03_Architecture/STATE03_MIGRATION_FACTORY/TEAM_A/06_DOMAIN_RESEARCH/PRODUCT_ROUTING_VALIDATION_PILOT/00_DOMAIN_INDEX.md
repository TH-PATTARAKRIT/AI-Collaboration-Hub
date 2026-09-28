> Domain: PRODUCT_ROUTING_VALIDATION_PILOT (Gx8) | Team A (Maker) | Documentation-Only | Boss sole Final Approver

# 00 — DOMAIN INDEX

Gx8 of the continuous STATE03 Deep Study run. Backbone Roadmap Lane C scenario 8: *"Stockable vs Consumable vs Service routing proof."* This directly tests the Backbone Roadmap's own stated rule: `Consumable / Service != Inventory-managed stock fact.`

## Material finding — the three-way model itself has changed in Odoo 19

The classic Storable/Consumable/Service three-way product-type split is **not** how Odoo 19 actually models it: the product form has a **Product Type** field (Goods or Service) plus a separate **Track Inventory** checkbox — a Goods product is "storable" only if Track Inventory is on; a Goods product with Track Inventory off is the old "Consumable." This is two orthogonal fields, not three peer categories — see `06_BUSINESS_RULE_REGISTER.md` `RTG-F01`.

Also finds a clean, specific accounting rule that confirms and refines the whole cross-Gx valuation-timing thread: **consumables expense at vendor-bill (purchase) time; storable goods expense at customer-invoice (sale) time (COGS)** — this is a textbook Anglo-Saxon accounting distinction, not a new one, but this is the first Gx to state it this precisely.

Same taxonomy as prior Gx.
