> Domain: GOODS_RECEIPT_VALIDATION_PILOT | Pilot Configuration Profile (Master Prompt §8) | Documentation-Tier

# 11 — CONFIGURATION REGISTER / PILOT CONFIGURATION PROFILE

Per Master Prompt §8, a Pilot Configuration Profile must precede AWT. Because no runtime is reachable from this container (see `22_UNKNOWN_AND_GAPS.md`, GAP-GRV-01), this profile records only what is **documented as a configuration surface**, not a confirmed, reproducible environment fingerprint. Fields that require an actual environment are marked `UNAVAILABLE`.

## A. Documented configuration surfaces (from official documentation, this round)

| Configuration surface | Documented effect | Evidence status |
|---|---|---|
| Multi-Step Routes (warehouse feature toggle) | Enables 2-step / 3-step receipt routing (GRV-F01) | `DOCUMENTED` |
| Costing Method (per Product Category): FIFO / AVCO / Standard-equivalent | Determines valuation behavior at receipt (GRV-F04) and eligibility for landed cost (GRV-F05) | `DOCUMENTED` |
| Valuation setting (per Product Category): Automatic (perpetual) vs Manual (periodic) | Determines whether receipt creates an immediate GL entry (GRV-F04) | `DOCUMENTED` |
| Bill Control Policy (Purchase settings): "ordered quantities" vs "received quantities" | Determines when a vendor bill can be drafted (GRV-F06) | `DOCUMENTED` |
| 3-way matching toggle (Purchase → Configuration → Settings → Invoicing) | Only functions when Bill Control Policy = "received quantities" (GRV-F06) | `DOCUMENTED` |

## B. Environment fingerprint fields required by Master Prompt §8 (Golden Trace) — status

| Field | Status |
|---|---|
| Release / build | `UNAVAILABLE` — no instance reachable |
| Installed / extension module matrix | `UNAVAILABLE` |
| Company / role / test fixture | `UNAVAILABLE` |
| Reset procedure | `UNAVAILABLE` — no environment to reset |
| Costing method / valuation / accounting-category configuration **as actually set in a specific test environment** | `UNAVAILABLE` — Section A above records documented *options*, not a confirmed environment setting |
| In-scope/excluded variants (price variance, landed-cost treatment) | Partially documented (landed-cost gating condition, Section A); price-variance handling not evidenced this round |

## Boundary statement

This register does not authorize or imply that any AWT step can proceed. It exists so that, once Boss authorizes an environment, the AWT team has a pre-built list of configuration surfaces to fix/freeze rather than discovering them cold.
