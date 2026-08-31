> GROUP A — Sales + Inventory + Purchase Integrated Backbone | EXPERT IBPV — Formal Re-Verification RV-011

# 15 — BOSS DECISION AND DEPENDENCY INPUT REGISTER

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-011-D15`

Single consolidated register of every decision or input this session requires from Boss, Accounting, or PMO to
advance the lifecycle. This session decides none of the items below — each row states only what is needed, from
whom.

| # | Item | Decision/input needed | From whom | Blocking scope |
|---|---|---|---|---|
| 1 | Sales-side cancellation-gate symmetry (A1) | (a) require symmetric gate, or (b) accept disclosed-risk asymmetry — plus the three interface facts listed in `CORRECTIVE_CORR_010/34`§A1 | Boss + Accounting/AR-AP domain owner | Sales-side cancellation-gate design only |
| 2 | Legacy approval internal workflow evidence (A2) | (a) commission source acquisition, or (b) accept vendor-neutral shape as final | Boss/PMO | Internal-logic implementation for Sequential Level-Based Approval only |
| 3 | Three deferred policy defaults (A3) | Set each default value, or explicitly rule "no default" | Boss/business | Not before Development starts broadly |
| 4 | TEAM A evidence branch-lineage gap (C4) | Merge cited TEAM A evidence files into canonical lineage | PMO | Non-blocking — design substance independently verified sound regardless |
| 5 | Governance-evidence cross-branch lineage gap (C5, new this session) | Re-sync GROUP A working lineage from canonical, or merge canonical governance stream into it | PMO/repository governance | Non-blocking — content independently verified consistent with actual Boss authorization |
| 6 | Overall RV-011 acceptance | Accept this session's independent verification conclusion (Deliverable 13/14) as the basis for the next lifecycle decision | Boss | Gates whether/when Boss next authorizes Team C planning, subject to items 1–2 remaining resolved separately |

## Explicit Non-Decisions by This Session

Consistent with the governing prompt's scope limits (§2), this session did not: resolve Accounting/AR-AP facts
for GROUP A; infer unavailable legacy approval internals; set Boss/business policy defaults; redesign
Multi-Approve; convert any carry-forward unknown into a fact; or authorize Team C or Development. Every row above
reflects that discipline — each states a question or a required input, never an answer this session supplied on
Boss's, Accounting's, or PMO's behalf.
