> Domain: MULTICOMPANY_ISOLATION_PILOT (Gx9) | Team A (Maker) | Documentation-Only | Boss sole Final Approver

# 00 — DOMAIN INDEX

Gx9 of the continuous STATE03 Deep Study run. Backbone Roadmap Lane C scenario 9: *"Multi-company / Tenant isolation at Inventory-to-Accounting handoff."*

## Material finding — warehouse-level access is not a native single toggle

A warehouse is bound to exactly one company (required field), and users are bound to companies — that much is native and structural. But restricting a specific *user within an allowed company* to a specific *warehouse* is documented as requiring **manually configured record rules and access groups** (one group per warehouse), not a built-in per-user warehouse-assignment field. See `06_BUSINESS_RULE_REGISTER.md` `MCT-F05`.

Same taxonomy as prior Gx.
