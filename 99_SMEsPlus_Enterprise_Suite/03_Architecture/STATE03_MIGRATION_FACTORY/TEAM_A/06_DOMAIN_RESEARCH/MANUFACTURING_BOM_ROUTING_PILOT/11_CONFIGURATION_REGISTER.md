> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Configuration Profile

# 11 — CONFIGURATION REGISTER

| Configuration surface | Function exists | Function configured | Function runtime reachable | Function verified end-to-end |
|---|---|---|---|---|
| BoM Type field (Manufacture / Kit / Subcontracting) | Documented | Named (per-BoM field) | `UNAVAILABLE` | `UNAVAILABLE` |
| Subcontracting feature toggle (Manufacturing → Configuration → Settings) | Documented | Named | `UNAVAILABLE` | `UNAVAILABLE` |
| Subcontracting Location (type = Internal) | Documented | Named (Inventory → Configuration → Locations, per subcontractor) | `UNAVAILABLE` | `UNAVAILABLE` |
| Work Orders feature toggle (Manufacturing → Configuration → Settings) | Documented | Named | `UNAVAILABLE` | `UNAVAILABLE` |
| Work Center (Cost per hour, Allowed Employees) | Documented | Named (Manufacturing → Configuration → Work Centers) | `UNAVAILABLE` | `UNAVAILABLE` |
| BoM Operations tab (step, Work Center, expected duration) | Documented | Named (per-BoM tab) | `UNAVAILABLE` | `UNAVAILABLE` |
| Reordering Rule (min/max, automatic/manual) | Documented | Named (Inventory → Operations → Replenishment) | `UNAVAILABLE` | `UNAVAILABLE` |
| Master Production Schedule | Documented | Named (Manufacturing → Planning → Master Production Schedule) | `UNAVAILABLE` | `UNAVAILABLE` |
| By-Products feature toggle + BOM tab | Documented | Named (Manufacturing → Configuration → Settings; per-BoM tab) | `UNAVAILABLE` | `UNAVAILABLE` |
| Sub-assembly BOM reference (multi-level) | Documented | Named (component pointing to another BoM) | `UNAVAILABLE` | `UNAVAILABLE` |

Environment fingerprint: `UNAVAILABLE` — same AWT/runtime constraint as every prior Deep Study unit; documentation-tier only until `BGQ-04` resolves. First-hand verification of this constraint (not just asserted): see `STATE03_CORRECTIVE_CHECKPOINT_RESPONSE.md` §B5.
