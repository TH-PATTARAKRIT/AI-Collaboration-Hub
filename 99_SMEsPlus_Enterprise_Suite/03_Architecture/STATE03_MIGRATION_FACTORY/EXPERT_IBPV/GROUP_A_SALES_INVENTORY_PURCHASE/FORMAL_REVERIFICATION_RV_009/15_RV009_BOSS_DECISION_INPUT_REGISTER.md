# 15 — RV-009 Boss Decision Input Register

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-009-D15`
Project: SMEsPlus ENTERPRISE SUITE · STATE03 — Architecture · GROUP A — Sales + Inventory + Purchase
Session: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-009`

Per the governing prompt: this register does **not** ask Boss to re-approve an already-controlled project invariant (the existence of Multi-Tenant SaaS is not re-opened anywhere in this session — see Deliverable 08). Only genuinely unresolved items appear below.

## Items Needing Boss Policy/Risk Decision

1. **Sales-side cancellation-gate symmetry** (Deliverable 14 §3 Item 1) — unchanged since FV-006. Requires Accounting Core/AR-AP domain input alongside Boss's decision.
2. **Legacy approval internal-logic evidence gap** (Deliverable 14 §3 Item 2) — unchanged, pre-existing carry-forward from the original Boss Evidence Gate. Requires Boss/PMO decision on evidence-acquisition vs. formal acceptance of the vendor-neutral shape.
3. **Race-condition findings `FV006-EVT-004`/`FV006-EVT-005` disposition** (Deliverable 14 §3 Item 3) — new to this session: decide whether TEAM B designs a resolution now or these are accepted as a scoped, tracked, deferred risk before Team C reaches the Sales-side event-driven fulfillment path.
4. **Three deferred policy defaults** (canonical Invoiced Quantity definition; Over-Fulfillment/Over-Billing default; Sales Confirmation Gate default) — unchanged, reconfirmed safe to defer; set whenever convenient before the specific computation/flow each feeds is considered feature-complete.

## Items Needing Input From Another Team/Domain

- Accounting Core / AR-AP domain owner input on Item 1 above (the underlying fact the Sales-side gate would depend on is outside GROUP A's authority to define unilaterally).

## Items Needing TEAM B Rework

- Eight light documentation/precision defects (Deliverable 14 §4, items 1–7 plus the PMO items 8–9) — none is a business-policy choice; all are independently verified as TEAM-B-fixable without new evidence or a Boss ruling. Recommended as a single light follow-up pass, not urgent before Team C starts on unaffected areas.

## Items Safe to Carry Forward Without Action Now

- Pre-existing `FV006-SAAS-002` evidence-citation gap (Deliverable 11 C5) — non-blocking, low priority, unchanged by CORR-008.
- Cross-Company Handoff (`FV006-SAAS-004`) and the Thai-SME-structure-mapping question — both independently confirmed still correctly labeled `CONTROLLED ASSUMPTION / REQUIRES FUTURE VERIFICATION`, unchanged, not newly discovered (Deliverable 08).

## Items Already Independently Verified Closed

- Denied-approval wind-down path (structural level) — Deliverable 03 RV9-01.
- Retry/idempotency contract — Deliverable 03 RV9-02.
- Downstream-failure compensation mechanism (structural level) — Deliverable 03 RV9-03.
- Sequential-approval wording clarification (structural level) — Deliverable 03 RV9-04.
- Self-approval mechanism gap — Deliverable 03 RV9-05 (**VERIFIED**, no conditions).
- Event-transport classification rule (structural level, excluding the ordering-clause defect tied to Item 3 above) — Deliverable 03 RV9-06.
- Lot/serial and package ownership (structural level) — Deliverable 03 RV9-07.
- Shared-master archival rule (structural level) — Deliverable 03 RV9-08.
- SaaS/Tenant mandate-vs-structure reconciliation — Deliverable 03 RV9-09.
- Corrected package integrity (SHA-256 manifest, ancestry, cross-team isolation) — Deliverable 02, unconditional **PASS**.
