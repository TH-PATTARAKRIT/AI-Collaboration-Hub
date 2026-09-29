> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Carry-forward / Re-audit Matrix

# BASELINE CARRY-FORWARD

| Existing Asset | Status | Reasoning |
|---|---|---|
| Gx7 `MANUFACTURING_VALUATION_PILOT` (`MFG-F01`/`F02`/`F04`) | **Reusable — this pilot extends, does not repeat it** | Gx7 already covers the "Manufacture this product" BoM-type branch's posting timing; this pilot studies the routing/type layer feeding it, not the same ground twice. |
| Gx6 valuation-timing resolution (`PCO-F03`) | **Reusable — inherited, not re-derived** | Still `Material Finding — Independently Unverified` per Boss ruling; this pilot does not add a further self-confirmation of it. |
| `STATE03_ENTERPRISE_MODULE_LEARNING_PRIORITY_MATRIX.md` Wave 5 | **Reusable** | Names Manufacturing/MRP and BOM/Production Master as candidate capabilities; this pilot is the first controlled pass at them. |

No prior Team A research exists for BOM Type/Kit/Subcontracting/Work Center/Routing specifically — this is genuinely new ground, not a re-audit of an existing branch (unlike Inventory Core Backbone's lineage).
