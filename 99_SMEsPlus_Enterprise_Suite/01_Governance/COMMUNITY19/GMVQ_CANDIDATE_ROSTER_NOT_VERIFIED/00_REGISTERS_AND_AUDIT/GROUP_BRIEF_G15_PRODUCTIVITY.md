# GROUP BRIEF — G15 PRODUCTIVITY / SPREADSHEET (Wave 4, 11 modules)

Subject matter: collaborative dashboards/spreadsheets and every seam where a spreadsheet dashboard
draws live data from another business domain.

## Modules and arity
- Foundation (full 48+ MVQ expected): `board` (kanban/planning board), `spreadsheet`,
  `spreadsheet_dashboard` (the base dashboard-of-dashboards capability).
- 2-way bridges (seam = spreadsheet_dashboard + the one named domain):
  `spreadsheet_dashboard_account`, `spreadsheet_dashboard_hr_expense`,
  `spreadsheet_dashboard_hr_timesheet`, `spreadsheet_dashboard_im_livechat`,
  `spreadsheet_dashboard_sale`, `spreadsheet_dashboard_stock_account` (treat stock_account as one
  combined accounting-of-stock domain, not 3 parties).
- 3-way — HIGH ARITY-EXHAUSTION RISK: `spreadsheet_dashboard_event_sale` (dashboard+event+sale),
  `spreadsheet_dashboard_sale_timesheet` (dashboard+sale+timesheet).

## Bridge Module Rule reminder
Same seam-only test as G12. A dashboard bridge module's questions must be about what breaks or
becomes uncertain ONLY when live dashboard reporting is layered on top of the source domain data
(staleness, permission leakage through aggregation, real-time vs. batch mismatch, cross-record
rollup exposing data the viewer should not see) — not a restatement of the source domain's own
questions (those belong to `sale`, `hr_expense`, `stock_account` etc. in their own groups).

## Known duplicate-risk pairs
- `spreadsheet_dashboard_sale` vs `spreadsheet_dashboard_sale_timesheet` — the timesheet variant
  must ask specifically about time-based rollup exposure, not repeat the sale-dashboard's own
  questions.
- `spreadsheet_dashboard_stock_account` vs G12's `project_stock_account` — different seam entirely
  (reporting-layer exposure vs. project-linkage); do not cross-pollinate question text.

## Clean room
Same rule as all groups — generic business concepts only, no vendor/technical identifiers, no
reference source reading.
