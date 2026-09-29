> Domain: QUALITY_CONTROL_PILOT | Evidence Gap Register

# 22 — UNKNOWN AND GAPS

| ID | Gap | Impact | Status | Route to close |
|---|---|---|---|---|
| GAP-QCP-01 | Whether a Fail result on a Manufacturing-Order-triggered quality check blocks MO completion, or is advisory-only | `QCP-F03`'s C1 open half — a real process-control question (does the system enforce a hold, or only record a failure) | **Resolved (documentation-tier, V2, mixed-evidence disclosed)** — an MO with a pending/incomplete mandatory quality check cannot be finalized (`EV-QCP-03`, official doc); the specific "hides Mark as Done" UI phrasing is blog-sourced (`EV-QCP-04`), not independently re-confirmed against the bare official page. Quality Alerts (`EV-QCP-05`) are a separate notification mechanism, not the blocking mechanism itself; a manual Work-Order "BLOCK" action (`EV-QCP-06`) is a distinct, user-initiated control, not evidenced as an automatic quality-failure trigger | AWT for runtime confirmation only — not blocking |
| GAP-QCP-02 | Whether a failed quality check has any financial/valuation implication (e.g., diverting failed-inspection stock to a distinct location/valuation state) | Structural question — whether this module ever touches Gx7/`M1`'s valuation model at all, or is purely a process/inspection control | **Open — not yet evidenced this pass** | Targeted official-doc pass, or AWT |

## Status summary

```
GAPS OPEN     : 1 (GAP-QCP-02)
RESOLVED      : 1 (GAP-QCP-01, documentation-tier V2, mixed-evidence disclosed)
NON-BLOCKING  : 0 (GAP-QCP-02 not yet triaged for blocking/non-blocking)
```

Same network/egress constraint as every prior Gx/pilot: search-synthesis, not verbatim reads (see `19_PROVENANCE_REGISTER.md`).
