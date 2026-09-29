> Domain: SHARED_MASTER_DATA_PILOT | Business Rule Register | `SMD-F04` at this pilot's own documentation-tier (WebSearch synthesis); `SMD-F01`–`F03` are Carry-forward summaries only — full detail lives in `GROUP_01_SALES_INVENTORY_PURCHASE/01_SHARED_MASTER_DEPENDENCY_MAP.md` (source-code+DB tier, a separate authorized track, cited by reference)

# 06 — BUSINESS RULE REGISTER

### SMD-F01 — Party/Contact model (Carry-forward summary only)

Full business-rule detail is not re-derived here — see `GROUP_01_SALES_INVENTORY_PURCHASE/01_SHARED_MASTER_DEPENDENCY_MAP.md` §02 (`PTY-01`–`PTY-22`), source-code+DB tier. Summary for this register's own continuity: one `res.partner` model serves every party role (customer/vendor/contact/company); `type` (contact/invoice/delivery/other) plus `parent_id`/`child_ids` gives one Company record many typed sub-addresses; `commercial_partner_id` groups them under one billing entity. **Open in the referenced track, not this pilot**: several DB columns (`brand_id`, `parent_company_id`, `store_type_id`, etc.) have no corresponding source — flagged there as `EVIDENCE_MISSING`, not resolved by this pilot.

### SMD-F02 — Product Template/Variant (Carry-forward summary only)

See `01_SHARED_MASTER_DEPENDENCY_MAP.md` §"PRODUCT" (`PRD-01`–`PRD-18`) and §"CATEGORY" (`CAT-*`). Summary: `product.template`/`product.product` template-variant split confirmed at DB level (`product_product` has no `company_id`/`uom_id`/`categ_id` — those live on the template only). `is_storable` ("Track Inventory") is Template-level, forced `False` for non-`consu` types (`PRD-09`/`10`) — this is the reference answer to this pilot's own `GAP-SMD-02`, now resolved by reference.

### SMD-F03 — UoM Category and Conversion (Carry-forward summary, with a disclosed tension)

See `01_SHARED_MASTER_DEPENDENCY_MAP.md` §"UOM" (`UOM-01`–`UOM-20`). Summary: conversion is `qty * self.factor / to_unit.factor` (`UOM-08`), same-family grouping enforced via `parent_path`/`relative_uom_id` recursion (`UOM-09`), **not** a separate `uom.category` model — this actual codebase has no `category_id` column (`UOM-20`). Rounding uses one shared "Product Unit" decimal-precision record for every UoM (`UOM-07`) — resolves this pilot's own `GAP-SMD-03` by reference. **Disclosed, unresolved tension**: this pilot's own official-documentation source (`EV-SMD-03`) describes UoM grouping via "Category" — see `GAP-SMD-05`.

### SMD-F04 — Access Rights / Groups (Role boundary) — this pilot's own primary contribution

- **WHAT**: Access to a model's records is granted through membership in one or more **Groups** (`res.groups`). Each Group carries a set of model-level CRUD permissions (create/read/update/delete per model). A user's effective access is the **union** (additive) of every Group they belong to — there is no subtractive/deny mechanism at this layer. A **Role** is documented as a predefined bundle of Groups presented to an administrator as one named unit, not a separate permission primitive of its own.
- **WHY**: Different job functions (a warehouse clerk vs. an accountant vs. an administrator) need different subsets of an ERP's very large model surface exposed to them; Groups let an administrator grant a coherent bundle of app-level access without hand-picking individual model permissions per user.
- **BUSINESS RULE**: If no Group a user belongs to grants an access right for a given model+operation, the operation is denied — access is opt-in only, never a default-allow with exceptions. Multiple Group memberships never reduce access; they only add to it.
- **STATE**: User created → assigned to one or more Groups (directly, or via a Role bundle) → effective permission set is the union of all assigned Groups' rights → recomputed whenever group membership changes.
- **DATA CONCEPT**: `res.groups` is a first-class record (name + category), independent of any specific model it grants access to — the model-to-group binding lives in a separate access-control-list layer, not on the Group record itself.
- **CONTROL**: This is a **model-level** (coarse-grained) control only — it answers "can this user touch this model at all, for this operation," not "which specific rows." Row-level filtering is a separate, distinct mechanism (Record Rules) not researched this pass.
- **DEPENDENCY**: Directly adjacent to `MULTICOMPANY_ISOLATION_PILOT`'s (`Gx9`) `MCT-F01` (Company-level data isolation) — Company scoping and Group-based model access are two independent axes that can both apply to the same model simultaneously; their interaction is this function's own open Unknown (`GAP-SMD-04`).
- **EVENT**: "Group membership changed" — an administrative event, not a business-transaction event; takes effect on the user's next access check, not retroactively re-evaluated against past actions.
- **RISK**: **C1, access-control-significant** — because access is purely additive, an administrator who over-grants a Group (e.g., adding a user to a broad "Administration" group to solve one narrow access need) creates a standing over-permission that no other Group membership can narrow back down; the only fix is removing the over-broad Group itself.
- **UNKNOWN → RESOLVED (2026-09-29, same-day WebSearch follow-on, `EV-SMD-05`)**: Model-level access (Groups) and record-level rules (including Multi-Company rules) are two distinct, composable layers, not one merged mechanism. Record rules with no group attached ("global rules") combine with **AND** and act as a hard floor — a failure there is absolute, regardless of Group membership; record rules that do carry a group combine with **OR** among themselves. Multi-company rules are typically implemented as **global** rules (no group), so in practice they apply as an unconditional filter layered on top of whatever a Group's model-level grant already allows — a Group can never bypass a global Multi-Company rule. See `GAP-SMD-04` for the full closure record.

## Clean-Room boundary

`SMD-F04` above is this pilot's own WebSearch-documentation-tier (V2) finding, Odoo-19-reference only — not SMEsPlus target IAM/RBAC design. `SMD-F01`–`F03` are Carry-forward citations to a separately-authorized, source-tier track — not re-derived, not copied verbatim beyond the evidence-ID references above, and not to be read as this pilot's own primary evidence.
