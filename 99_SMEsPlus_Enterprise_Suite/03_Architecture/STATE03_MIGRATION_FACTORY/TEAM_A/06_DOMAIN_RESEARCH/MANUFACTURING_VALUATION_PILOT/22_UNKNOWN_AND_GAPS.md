> Domain: MANUFACTURING_VALUATION_PILOT (Gx7) | Evidence Gap Register

# 22 — UNKNOWN AND GAPS (Gx7)

| ID | Gap | Impact | Status | Route to close |
|---|---|---|---|---|
| GAP-MFG-01 | **PARTIALLY RESOLVED 2026-09-29, V1 (community/blog tier, not official docs).** The forum thread (opened this round) and a secondary Odoo-partner blog source disagree on Odoo *version*: the thread describes pre-19 behavior (a "Revaluation of WH/MO/XXX" entry once negative-inventory-consumed material is later received); the blog states Odoo 19 changed this so raw-material cost is only booked at vendor-bill time, with no automatic revaluation entry. **Disclosed as an open version tension, not resolved either way** — see `06_BUSINESS_RULE_REGISTER.md` MFG-F05. If the Odoo-19 reading is correct, this is additional (not independently verified) evidence for the same already-flagged valuation-timing Material Finding, not a new item. | Criticality remains C1 (provisional); still no official-documentation-tier source | **Targeted Validation Needed — official Odoo 19 doc page or AWT still required** | Official Odoo 19 documentation search (not blog/forum) on MRP negative-stock revaluation, or AWT runtime confirmation |
| GAP-MFG-02 | Production Account misconfiguration behavior (blocked/defaulted/silent) not evidenced | `MFG-F01` UNKNOWN field | **Non-blocking** | Documentation or runtime pass |
| GAP-MFG-03 | Partial-completion finished-good valuation not evidenced | `MFG-F02` UNKNOWN field | **Non-blocking** | Documentation or runtime pass |
| GAP-MFG-04 | Work-center cost-rate mechanics not evidenced | `MFG-F04` UNKNOWN field | **Non-blocking** | Documentation or runtime pass |
| GAP-MFG-05 | Whether MFG-F03's interim entry reversal is automatic on MO completion | `MFG-F03` UNKNOWN field | **Non-blocking** | Documentation or runtime pass |
| GAP-MFG-06 | Same network/egress constraint as all prior Gx | Search-synthesis, not verbatim reads | **Non-blocking** | Same as prior Gx |

## Status summary

```
GAPS OPEN              : 6
TARGETED VALIDATION    : 1 (GAP-MFG-01, partially resolved 2026-09-29 to V1 — version tension disclosed, official-doc/AWT confirmation still required)
NON-BLOCKING           : 5 (GAP-MFG-02..06)
```
