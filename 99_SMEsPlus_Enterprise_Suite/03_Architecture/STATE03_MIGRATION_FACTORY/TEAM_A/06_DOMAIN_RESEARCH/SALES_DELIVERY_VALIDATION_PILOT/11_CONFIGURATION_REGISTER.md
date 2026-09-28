> Domain: SALES_DELIVERY_VALIDATION_PILOT (Gx2) | Configuration Profile (Boss order §4.E) | Documentation-Tier

# 11 — CONFIGURATION REGISTER

Per Boss's order §4.E, four distinct states are tracked separately for every configuration-dependent behavior: **function exists** (documented) / **function configured** (a specific setting is named) / **function runtime reachable** (would require an environment) / **function verified end-to-end** (would require AWT). Source/documentation presence is not runtime proof.

| Configuration surface | Function exists | Function configured | Function runtime reachable | Function verified end-to-end |
|---|---|---|---|---|
| Multi-Step Routes (delivery routing) | Documented | Named (toggle, Inventory → Configuration → Settings) | `UNAVAILABLE` — no environment | `UNAVAILABLE` |
| Invoicing Policy (ordered vs. delivered quantities) | Documented | Named (per-product setting, Sales → Products → Invoicing Policy) | `UNAVAILABLE` | `UNAVAILABLE` |
| Perpetual (at invoicing) valuation + Stock Variation account | Documented | Named (per Product Category) | `UNAVAILABLE` | `UNAVAILABLE` — **this is exactly the GAP-SDV-01 contradiction; "configured" here means the documentation names the setting, not that its timing behavior is confirmed** |
| Reverse Transfer (pre-invoice return) | Documented | No separate toggle found — appears to be a standard Inventory app capability, not a settings flag | `UNAVAILABLE` | `UNAVAILABLE` |
| Credit Note (post-invoice return) | Documented | Standard Accounting app capability | `UNAVAILABLE` | `UNAVAILABLE` |

## Environment fingerprint (Golden Trace §8 fields) — status

Identical to Gx1's `11_CONFIGURATION_REGISTER.md` §B: release/build, installed modules, company/role/fixture, reset procedure — all `UNAVAILABLE`, no reachable environment in this container.
