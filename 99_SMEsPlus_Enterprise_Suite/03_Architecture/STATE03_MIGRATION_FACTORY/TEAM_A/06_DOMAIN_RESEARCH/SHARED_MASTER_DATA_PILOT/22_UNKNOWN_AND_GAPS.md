> Domain: SHARED_MASTER_DATA_PILOT | Evidence Gap Register

# 22 — UNKNOWN AND GAPS

| ID | Gap | Impact | Status | Route to close |
|---|---|---|---|---|
| GAP-SMD-01 | Whether a child address record shares its parent Company's tax-ID/legal identity, or is an independent Party for tax/legal purposes | `SMD-F01` — material if SMEsPlus needs one legal-entity identity across multiple ship-to/bill-to addresses (Thailand branch-address relevance, flagged not yet evidenced) | **Non-blocking** | Documentation or runtime pass |
| GAP-SMD-02 | Whether Track Inventory / costing method is set at Product Template level (shared across variants) or can differ per Variant | `SMD-F02` — directly material to Gx8's own `RTG-F01` scope (Product Type × Track Inventory); if variants can diverge, Gx8's finding needs a variant-level qualifier it does not currently have | **Resolved by reference (2026-09-29)** — `GROUP_01_SALES_INVENTORY_PURCHASE/01_SHARED_MASTER_DEPENDENCY_MAP.md` `PRD-09`/`PRD-10` (source-code tier, `stock/models/product.py`): `is_storable` is defined at **Template level**, forced `False` whenever `type != 'consu'` — not per-Variant. Not independently re-derived by this session; Carry-forward reference | Closed by reference — no further action needed unless the referenced track's own finding is itself re-audited and changes |
| GAP-SMD-03 | Rounding behavior when a UoM Ratio produces a non-integer result for a discrete-count (non-divisible) UoM | `SMD-F03` — a real precision/financial-control question (e.g., a 3-unit-per-box UoM converted to a fractional box count) | **Resolved by reference (2026-09-29)** — same track's `UOM-07`: `round()`/`compare()`/`is_zero()` all use **one shared "Product Unit" decimal-precision record**, applied uniformly regardless of what a given UoM measures. Carry-forward reference, not independently re-derived | Closed by reference |
| GAP-SMD-05 | **New, disclosed tension** (found via the same-day scope-collision reference check, not resolved): this pilot's own WebSearch-sourced official Odoo 19 documentation (`EV-SMD-03`) describes UoM grouping in terms of a **"Category"**; the source-code+DB evidence from `GROUP_01_SALES_INVENTORY_PURCHASE` (`UOM-01`, `UOM-09`, `UOM-20`) shows the actual dumped codebase has **no `uom.category` model and no `category_id` column** — grouping is instead achieved via a self-referential `relative_uom_id`/`parent_path` hierarchy, with a custom SMEsPlus module (`UOM-14`) re-deriving "same conversion family" precisely *because* no category table exists. **Not resolved either way** — could be a documentation-vs.-actual-deployment version/customization tension (same shape as `GAP-MFG-01`'s Odoo-version tension), or the public docs' "Category" may simply be UI-level vocabulary for what the schema implements structurally differently. Disclosed, not silently reconciled | `SMD-F03` — a genuine terminology/implementation discrepancy between this pilot's own evidence source and a higher-tier, differently-sourced reference | **Open — disclosed tension** | Would require reading the actual public Odoo 19 `uom.uom` source directly (this session has no source access) or asking the other track's own session to re-confirm against a newer schema snapshot |
| GAP-SMD-04 | Exact interaction between a Group's model-level access and a (Multi-Company) Record Rule's row-level filtering when both apply to the same model | `SMD-F04` — a real access-control-adjacent question, structurally similar to Gx9's own `GAP-MCT-01`/`GAP-MCT-02` | **Resolved (documentation-tier, V2, 2026-09-29)** — `EV-SMD-05`: model-level Group access and record-level rules are distinct, composable layers; global (no-group) rules AND-combine as a hard floor, group-carrying rules OR-combine among themselves; Multi-Company rules are typically global, so they apply unconditionally on top of any Group grant — a Group can never bypass a global Multi-Company rule | AWT for runtime confirmation only — not blocking |

## Status summary

```
GAPS OPEN                : 2 (GAP-SMD-01, 05)
RESOLVED BY REFERENCE     : 2 (GAP-SMD-02, GAP-SMD-03 — Carry-forward from GROUP_01_SALES_INVENTORY_PURCHASE, not independently re-derived)
RESOLVED (this pilot's own documentation-tier evidence) : 1 (GAP-SMD-04)
NON-BLOCKING             : 1 (GAP-SMD-01)
DISCLOSED TENSION        : 1 (GAP-SMD-05 — documentation vs. actual-deployment discrepancy, not resolved either way)
```

Same network/egress constraint as every prior Gx/pilot: search-synthesis, not verbatim reads (see `19_PROVENANCE_REGISTER.md`).
