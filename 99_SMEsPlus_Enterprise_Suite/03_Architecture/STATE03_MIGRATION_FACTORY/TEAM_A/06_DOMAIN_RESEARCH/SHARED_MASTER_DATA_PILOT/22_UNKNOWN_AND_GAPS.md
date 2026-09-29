> Domain: SHARED_MASTER_DATA_PILOT | Evidence Gap Register

# 22 — UNKNOWN AND GAPS

| ID | Gap | Impact | Status | Route to close |
|---|---|---|---|---|
| GAP-SMD-01 | Whether a child address record shares its parent Company's tax-ID/legal identity, or is an independent Party for tax/legal purposes | `SMD-F01` — material if SMEsPlus needs one legal-entity identity across multiple ship-to/bill-to addresses (Thailand branch-address relevance, flagged not yet evidenced) | **Non-blocking** | Documentation or runtime pass |
| GAP-SMD-02 | Whether Track Inventory / costing method is set at Product Template level (shared across variants) or can differ per Variant | `SMD-F02` — directly material to Gx8's own `RTG-F01` scope (Product Type × Track Inventory); if variants can diverge, Gx8's finding needs a variant-level qualifier it does not currently have | **Targeted Validation Needed** — feeds back into an existing Gx8 finding, not just this pilot | Official-doc pass focused on variant-level cost/valuation fields, or AWT |
| GAP-SMD-03 | Rounding behavior when a UoM Ratio produces a non-integer result for a discrete-count (non-divisible) UoM | `SMD-F03` — a real precision/financial-control question (e.g., a 3-unit-per-box UoM converted to a fractional box count) | **Non-blocking** | Documentation or runtime pass |
| GAP-SMD-04 | Exact interaction between a Group's model-level access and a (Multi-Company) Record Rule's row-level filtering when both apply to the same model | `SMD-F04` — a real access-control-adjacent question, structurally similar to Gx9's own `GAP-MCT-01`/`GAP-MCT-02` | **Non-blocking** (this pass) — candidate for a joint follow-up with `MULTICOMPANY_ISOLATION_PILOT` | Documentation or runtime pass, cross-referenced with Gx9 |

## Status summary

```
GAPS OPEN                : 4
RESOLVED                 : 0
TARGETED VALIDATION      : 1 (GAP-SMD-02 — feeds back into Gx8's RTG-F01)
NON-BLOCKING             : 3 (GAP-SMD-01, 03, 04)
```

Same network/egress constraint as every prior Gx/pilot: search-synthesis, not verbatim reads (see `19_PROVENANCE_REGISTER.md`).
