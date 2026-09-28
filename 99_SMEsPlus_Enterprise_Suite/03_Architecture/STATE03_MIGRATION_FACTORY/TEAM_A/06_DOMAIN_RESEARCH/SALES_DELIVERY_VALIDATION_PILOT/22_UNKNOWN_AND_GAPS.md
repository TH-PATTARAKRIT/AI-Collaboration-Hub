> Domain: SALES_DELIVERY_VALIDATION_PILOT (Gx2) | Evidence Gap Register | Gaps recorded as Evidence Gap / Evidence Conflict, not Fail

# 22 — UNKNOWN AND GAPS (Gx2)

| ID | Gap | Impact | Status | Route to close |
|---|---|---|---|---|
| GAP-SDV-01 | **Evidence Conflict.** Two genuine Odoo 19 documentation sources disagree on when perpetual valuation posts a journal entry: at physical movement (the claim Gx1's `GRV-F04` recorded) vs. at invoice time via a Stock Variation buffer account (this Gx's finding, EV-SDV-04). | Directly affects the C1 valuation-timing claim in **both** Gx1 and Gx2; must not be relied on in either direction for any downstream design discussion. | **Evidence Conflict — highest-priority open item across Gx1+Gx2** | AWT (this pilot's `AWT_BACKLOG.md` and Gx1's, both updated) is the only way to resolve this; a further documentation pass could also help (e.g. checking whether the "invoice-timing" pages are describing a *specific* valuation sub-mode not covered by the generic page Gx1 used) but is unlikely to fully resolve it alone |
| GAP-SDV-02 | Delivery-side backorder documentation reads as more automatic than Gx1's purchase-side, action-gated backorder description; not confirmed whether this is a real mechanical difference or documentation-emphasis difference | Cannot yet state with confidence that GRV-F03 and SDV-F03 are mechanically identical | **Targeted Validation Needed** | Direct page comparison once network access allows, or runtime confirmation |
| GAP-SDV-03 | No documentation evidence gathered on multi-company/tenant scoping for delivery, invoicing-policy enforcement, or credit notes | Control Applicability Matrix records Company/Data Scope as `Unknown` | **Non-blocking** | Targeted documentation pass, or runtime observation |
| GAP-SDV-04 | No documentation evidence on audit trail/event emission for delivery validation, return, or credit-note issuance | Control Applicability Matrix records Audit/Event as `Unknown` | **Non-blocking** | Documentation or runtime pass |
| GAP-SDV-05 | Credit Note amount derivation (automatic vs. manual) not evidenced | SDV-F07 UNKNOWN field | **Non-blocking** | Documentation or runtime pass |
| GAP-SDV-06 | Same network/egress constraint as Gx1 (`GAP-GRV-08`) — all citations are search-synthesis, not verbatim reads | Slightly lower confidence tier on every claim | **Non-blocking** (disclosed in `19_PROVENANCE_REGISTER.md`) | Same as Gx1 |

## Cross-Gx action taken

`GAP-SDV-01` was pushed back into Gx1: `../GOODS_RECEIPT_VALIDATION_PILOT/AWT_BACKLOG.md` GRV-F04 entry was updated with a cross-reference (not a rewrite of GRV-F04's original documentation-tier finding, which stands as recorded — only the AWT plan was extended to also test this contradiction). This is the Material Delta mechanism working as intended: a later Gx's research improved an earlier Gx's open question without discarding it.

## Status summary

```
GAPS OPEN                 : 6
EVIDENCE CONFLICT (shared with Gx1) : 1 (GAP-SDV-01)
TARGETED VALIDATION       : 1 (GAP-SDV-02)
NON-BLOCKING              : 4 (GAP-SDV-03, 04, 05, 06)
```
