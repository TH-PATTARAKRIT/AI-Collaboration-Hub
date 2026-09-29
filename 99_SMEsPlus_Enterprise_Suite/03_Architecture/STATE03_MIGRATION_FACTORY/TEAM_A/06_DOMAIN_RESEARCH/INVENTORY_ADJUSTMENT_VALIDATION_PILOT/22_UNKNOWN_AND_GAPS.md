> Domain: INVENTORY_ADJUSTMENT_VALIDATION_PILOT (Gx4) | Evidence Gap Register

# 22 — UNKNOWN AND GAPS (Gx4)

| ID | Gap | Impact | Status | Route to close |
|---|---|---|---|---|
| GAP-IAV-01 | **RESOLVED 2026-09-28 (Gx6), documentation-tier.** Was: third data point on the cross-Gx valuation-timing conflict. Gx6 clarified: adjustments post immediately because they have **no future vendor bill/customer invoice to defer to** — the adjustment application *is* the financial transaction in that case, consistent with (not contradicting) the "posts at financial-transaction-time" rule found for receipts/deliveries. See `../PERIOD_CUTOFF_VALIDATION_PILOT/06_BUSINESS_RULE_REGISTER.md` PCO-F03/01_EXECUTIVE_RESEARCH_SUMMARY.md. **STATUS DOWNGRADE (2026-09-29, Boss ruling): this resolution is `Material Finding — Independently Unverified`, not Canonical Architecture Truth — it was reconciled by the same session that raised the original conflict, not an independent reviewer. Routed to `CHATGPT_AUDIT`; see `00_Architecture_Governance/STATE03_VALUATION_TIMING_CROSS_GX_CONTRADICTION_MATRIX.md`.** | No longer an open contradiction; the "uniform rule" is: post at financial-transaction time, whatever that transaction is for the given event type. | **Material Finding — Independently Unverified** (was: Resolved, documentation-tier, high confidence) | AWT (shared capstone session) for final runtime confirmation; independent audit via `CHATGPT_AUDIT` |
| GAP-IAV-02 | No documented reversal/undo mechanism for an applied inventory adjustment | Cannot state whether IAV-F06 works like Reverse Transfer/Credit Note or is simply "make another adjustment" | **Targeted Validation Needed** | Documentation search focused specifically on "correcting" or "undoing" an applied count, or runtime evidence |
| GAP-IAV-03 | No documentation evidence on authority/role controls for applying adjustments or scrapping goods | Control Applicability Matrix records Authority as `Unknown` | **Non-blocking** | Documentation or runtime pass |
| GAP-IAV-04 | No documentation evidence on multi-company/tenant scoping | Control Applicability Matrix records Tenant/Company Scope as `Unknown` | **Non-blocking** | Documentation or runtime pass |
| GAP-IAV-05 | Whether single-line Apply captures a reason the same way Apply All does | IAV-F02 UNKNOWN field | **Non-blocking** | Documentation or runtime pass |
| GAP-IAV-06 | Same network/egress constraint as all prior Gx | Search-synthesis, not verbatim reads | **Non-blocking** | Same as prior Gx |

## Status summary

```
GAPS OPEN                    : 6
RESOLVED (2026-09-28, Gx6)   : 1 (GAP-IAV-01, was Evidence Conflict)
TARGETED VALIDATION          : 1 (GAP-IAV-02)
NON-BLOCKING                 : 4 (GAP-IAV-03, 04, 05, 06)
```
