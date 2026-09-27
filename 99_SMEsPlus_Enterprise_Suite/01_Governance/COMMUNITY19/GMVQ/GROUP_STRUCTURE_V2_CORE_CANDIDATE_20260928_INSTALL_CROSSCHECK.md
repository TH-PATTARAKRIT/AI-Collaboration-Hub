# Candidate Roster — Installed-Status Cross-Check (2026-09-28)

**STATUS: SUPPLEMENTARY EVIDENCE ONLY — DOES NOT CONFIRM GROUP MEMBERSHIP.**

This note cross-checks every "candidate lead" module named (but explicitly **not** credited
as roster membership) in `GROUP_STRUCTURE_V2_CORE_CANDIDATE_20260928.tsv` and its README
against a Boss-provided `ir.module.module` export (`Module_ir.module.module_7.xlsx`, 683
total module rows, 270 marked `Installed`). This confirms only that a given technical module
**exists and is installed on the exported instance** — it says nothing about which SMEsPlus
governance group (G01–G16) that module belongs to, because the export has no group/category
column of any kind. Per the Boss's own instruction, this is used strictly as supplementary
cross-check evidence, not as roster-group confirmation.

**Source instance:** not independently confirmed by MASTER from the file itself (no instance
URL/database name embedded in the export); Boss should confirm which instance this was
exported from if that provenance matters later.

## Cross-check results

| Group (candidate lead, NOT credited membership) | Module | Install status in export |
|---|---|---|
| G02 IDENTITY_ACCESS | `auth_password_policy` | Installed |
| G02 IDENTITY_ACCESS | `auth_oauth` | Installed |
| G02 IDENTITY_ACCESS | `auth_totp` | Installed |
| G02 IDENTITY_ACCESS | `auth_passkey` | Installed |
| G02 IDENTITY_ACCESS | `auth_ldap` | Installed |
| G03 MASTER_DATA (already CONFIRMED anchors) | `product`, `uom`, `analytic` | Installed |
| G05 INVENTORY (already CONFIRMED anchor) | `stock` | Installed |
| G06 MANUFACTURING (already CONFIRMED anchor) | `mrp` | Installed |
| G07 PURCHASE (already CONFIRMED anchor) | `purchase` | Installed |
| G08 SALES (already CONFIRMED anchor) | `sale` | Installed |
| G09 CRM (already CONFIRMED anchor) | `crm` | Installed |
| G11 EVENTS (all 8, DERIVED) | `event`, `event_booth`, `event_booth_sale`, `event_crm`, `event_crm_sale`, `event_product`, `event_sale`, `event_sms` | Installed (all 8) |
| G12 PROJECT_SERVICES (anchor + bridge leads) | `project` (CONFIRMED anchor), `hr_timesheet`, `sale_project`, `sale_timesheet` (uncredited bridge leads) | Installed (all 4) |
| G13 PEOPLE (uncredited leads) | `hr`, `hr_attendance`, `hr_holidays`, `hr_expense`, `hr_recruitment` | Installed (all 5) |
| G14 COLLABORATION (uncredited secondary trace) | `mail`, `calendar` | Installed (both) |
| G16 TECHNICAL_INTEGRATION (uncredited secondary trace) | `auth_oauth` | Installed |
| G16 TECHNICAL_INTEGRATION (governed BLOCKED-TECHNICAL, not asserted as the delta row) | `cloud_storage_google` | **Not Installed** |

## What this changes

**Nothing in the TSV's `source_confidence` column.** Every GAP row in
`GROUP_STRUCTURE_V2_CORE_CANDIDATE_20260928.tsv` remains GAP. Every already-CONFIRMED/DERIVED
row remains at its existing confidence level — installed-status is not a substitute for an
explicit module-to-group pairing in a controlled roster document, and this file does not
create one. The one negative result (`cloud_storage_google` not installed) is also purely
supplementary: it neither confirms nor rules out that module as G16's unresolved 20→19 delta
row, since install status on one instance is not evidence of SMEsPlus group ownership either
way.

## What would actually resolve a GAP row

Only an explicit module ↔ group pairing in a controlled source (the recovered
`GROUP_STRUCTURE_V2_CORE.tsv` bytes, or an equivalent Boss-issued roster document) can move a
row from GAP/DERIVED to CONFIRMED. This cross-check exists so the Boss has installed-status
context available alongside the candidate roster — not to shortcut that requirement.
