> Domain: QUALITY_CONTROL_PILOT | Evidence Annex Index

# 19 — PROVENANCE REGISTER

Retrieved via `WebSearch` (search-engine-mediated; direct fetch blocked, same constraint as every prior Deep Study unit) on **2026-09-29**.

| Evidence ID | URL | Tier | Used for |
|---|---|---|---|
| EV-QCP-01 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/quality/quality_management/quality_control_points.html` | Official documentation | `QCP-F01` (QCP configuration: Operation, Product/Category, Quantity scoping) |
| EV-QCP-02 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/quality/quality_management/quality_checks.html` | Official documentation | `QCP-F02` (check types: Pass/Fail, Measure, Picture), `QCP-F03` (Manufacturing-Order trigger, Work Order Operation scoping) |
| EV-QCP-03 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/quality/quality_check_types/pass_fail_check.html` | Official documentation | `GAP-QCP-01` closure: an MO with pending/incomplete quality checks cannot be finalized — a validation error is raised |
| EV-QCP-04 | `https://www.infintor.com/quality-control-inspection-in-odoo-manufacturing/` (blog, UI-behavior specific: "hides Mark as Done" when a mandatory QC fails) | **Blog — UI-level detail not independently re-confirmed against the bare official page's own wording** | `GAP-QCP-01` (corroborating detail, disclosed as sub-official tier, not the sole basis for closure) |
| EV-QCP-05 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/quality/quality_management/quality_alerts.html` | Official documentation | `GAP-QCP-01` scope note: Quality Alerts are a distinct notification mechanism (to quality teams), not itself the MO-blocking mechanism |
| EV-QCP-06 | `https://www.odoo.com/forum/help-1/how-to-block-work-orders-from-continuing-if-there-is-a-quality-alert-130928` | Community forum | `GAP-QCP-01` scope note: a separate, manually-triggered "BLOCK" action exists on Work Orders (Shop Floor), distinct from an automatic quality-check-failure block — user-initiated, not evidenced as automatic |

## Clean-room boundary

Same as all prior Gx/pilots — evidence annex only, not to be copied verbatim into a future Clean-Room Neutral Pack. No Odoo source code, schema, or ORM identifier was read or recorded this round — documentation-tier only.
