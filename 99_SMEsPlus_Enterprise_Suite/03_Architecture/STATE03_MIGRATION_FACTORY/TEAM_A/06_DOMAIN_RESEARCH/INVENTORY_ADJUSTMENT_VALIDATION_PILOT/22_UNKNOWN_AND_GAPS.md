> Domain: INVENTORY_ADJUSTMENT_VALIDATION_PILOT (Gx4) | Evidence Gap Register

# 22 — UNKNOWN AND GAPS (Gx4)

| ID | Gap | Impact | Status | Route to close |
|---|---|---|---|---|
| GAP-IAV-01 | **Evidence Conflict, third data point.** This Gx's documentation states inventory-adjustment postings are immediate and unconditional; Gx1/Gx2 found valuation-mode-dependent (and, in Gx2's case, invoice-timing-dependent) postings for receipts/deliveries. Not yet determined whether these are three genuinely different mechanisms (plausible) or a documentation inconsistency (also plausible). | Affects any design assumption about a single, uniform "when does a stock event hit the GL" rule across the whole Inventory↔Accounting interface | **Evidence Conflict — cross-Gx, same lineage as `GAP-SDV-01`** | AWT — this is now a 3-part test: receipt, delivery, and adjustment, run in the same environment session for direct comparability |
| GAP-IAV-02 | No documented reversal/undo mechanism for an applied inventory adjustment | Cannot state whether IAV-F06 works like Reverse Transfer/Credit Note or is simply "make another adjustment" | **Targeted Validation Needed** | Documentation search focused specifically on "correcting" or "undoing" an applied count, or runtime evidence |
| GAP-IAV-03 | No documentation evidence on authority/role controls for applying adjustments or scrapping goods | Control Applicability Matrix records Authority as `Unknown` | **Non-blocking** | Documentation or runtime pass |
| GAP-IAV-04 | No documentation evidence on multi-company/tenant scoping | Control Applicability Matrix records Tenant/Company Scope as `Unknown` | **Non-blocking** | Documentation or runtime pass |
| GAP-IAV-05 | Whether single-line Apply captures a reason the same way Apply All does | IAV-F02 UNKNOWN field | **Non-blocking** | Documentation or runtime pass |
| GAP-IAV-06 | Same network/egress constraint as all prior Gx | Search-synthesis, not verbatim reads | **Non-blocking** | Same as prior Gx |

## Status summary

```
GAPS OPEN                    : 6
EVIDENCE CONFLICT (cross-Gx) : 1 (GAP-IAV-01)
TARGETED VALIDATION          : 1 (GAP-IAV-02)
NON-BLOCKING                 : 4 (GAP-IAV-03, 04, 05, 06)
```
