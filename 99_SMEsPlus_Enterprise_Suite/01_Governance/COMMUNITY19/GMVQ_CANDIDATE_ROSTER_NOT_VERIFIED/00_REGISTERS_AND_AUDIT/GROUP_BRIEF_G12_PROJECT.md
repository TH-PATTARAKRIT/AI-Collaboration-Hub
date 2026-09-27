# GROUP BRIEF — G12 PROJECT (Wave 3, 20 modules)

Subject matter: project-management concepts (tasks, milestones, timesheets, project profitability)
and every seam where project links to another business domain (HR, MRP, purchase, sale, stock,
accounting, communication, portal).

## Modules and arity
- Foundation (low/no bridge arity — full 48+ MVQ expected easily): `project`, `hr_timesheet`,
  `hr_timesheet_attendance`, `portal_rating`, `project_todo`, `project_sms`,
  `project_mail_plugin`, `project_hr_skills`.
- 2-way bridges (seam = the two named domains only): `project_hr_expense`, `project_purchase`,
  `project_sale_expense`, `project_stock`, `project_purchase_stock` (treat as 2-way: project+
  purchase-fulfilled-by-stock, not 3 independent domains), `project_timesheet_holidays`.
- 3-way+ bridges — HIGH ARITY-EXHAUSTION RISK, apply the seam-only test strictly, do not force 48:
  `project_mrp` (2-way, project+manufacturing), `project_mrp_account` (3-way: project+mrp+account),
  `project_mrp_sale` (3-way: project+mrp+sale), `project_mrp_stock_landed_costs` (4-way: project+
  mrp+stock+landed-cost valuation), `project_stock_account` (3-way), `project_stock_landed_costs`
  (3-way).

## Bridge Module Rule reminder (from 00_CONTROL/GMVQ_BRIDGE_MODULE_RULE_V1.00.md)
For any module named A_B(_C…): ask only at the seam. Test: "if this capability were removed and
the parts used entirely apart, would the question still make sense?" YES -> cut it, it belongs to
a lower-arity sibling or a foundation module. A 3-4 way bridge genuinely may not reach 48 distinct
seam questions — if exhaustive search falls short, write an ARITY EXHAUSTION STATEMENT (do not
pad) and report the shortfall to GMVQ control desk for a Boss decision, same pattern as B-03
(G08 sale_project_stock_account / sale_purchase_project).

## Known duplicate-risk pairs (do not noun-swap the same question across these)
- `project_mrp_account` vs `project_stock_account` vs `sale_project_stock_account` (G08, already
  authored) — the "project+X+account" pattern must ask a DIFFERENT seam question per module, tied
  to what X actually contributes (manufacturing cost vs. stock valuation vs. sale-order linkage).
- `project_mrp_sale` vs `sale_project` family (G08) — do not re-ask G08's questions from the
  project side; ask what project-side information changes because of the mrp+sale combination.
- `project_stock_landed_costs` vs `project_mrp_stock_landed_costs` — the seam differs by whether
  manufacturing is in the loop; keep questions distinct to that difference only.

## Clean room
Generic business concepts only. No vendor names, technical field names, or the module's own
metadata identifiers inside HYPOTHESIS / WHY_IT_MATTERS / DISCONFIRMING_OBSERVATION /
PRECONDITIONS. No reference source reading.
