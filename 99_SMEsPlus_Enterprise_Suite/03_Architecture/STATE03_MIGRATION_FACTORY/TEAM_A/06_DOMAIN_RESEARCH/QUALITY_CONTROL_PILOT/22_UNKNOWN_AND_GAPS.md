> Domain: QUALITY_CONTROL_PILOT | Evidence Gap Register

# 22 — UNKNOWN AND GAPS

| ID | Gap | Impact | Status | Route to close |
|---|---|---|---|---|
| GAP-QCP-01 | Whether a Fail result on a Manufacturing-Order-triggered quality check blocks MO completion, or is advisory-only | `QCP-F03`'s C1 open half — a real process-control question (does the system enforce a hold, or only record a failure) | **Open — not yet evidenced this pass** | Targeted official-doc pass on Quality Alerts / MO-blocking behavior, or AWT |
| GAP-QCP-02 | Whether a failed quality check has any financial/valuation implication (e.g., diverting failed-inspection stock to a distinct location/valuation state) | Structural question — whether this module ever touches Gx7/`M1`'s valuation model at all, or is purely a process/inspection control | **Open — not yet evidenced this pass** | Targeted official-doc pass, or AWT |

## Status summary

```
GAPS OPEN     : 2
RESOLVED      : 0
NON-BLOCKING  : 0 (both are the pilot's own open questions this early in research — not yet triaged for blocking/non-blocking)
```

Same network/egress constraint as every prior Gx/pilot: search-synthesis, not verbatim reads (see `19_PROVENANCE_REGISTER.md`).
