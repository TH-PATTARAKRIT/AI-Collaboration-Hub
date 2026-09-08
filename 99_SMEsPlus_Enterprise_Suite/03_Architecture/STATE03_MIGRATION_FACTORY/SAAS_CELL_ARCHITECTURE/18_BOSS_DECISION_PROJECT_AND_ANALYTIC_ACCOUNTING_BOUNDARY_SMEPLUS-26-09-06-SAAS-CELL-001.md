# BOSS DECISION — Project and Analytic Accounting Boundary

Session: SMEPLUS-26-09-06-SAAS-CELL-001
Date: 2026-09-08
Status: APPROVED DIRECTION / DETAIL DESIGN PENDING
Boss: Sole Final Approver

## 1. Approved Principle

Project and Analytic Accounting are separate responsibilities.

- `Project` = operational management of work, milestones, resources, tasks and delivery progress.
- `Analytic Accounting` = financial dimensional analysis describing where / why / for whom accounting facts belong.

Project does not own financial source facts. Financial truth remains with source domains such as Accounting, Invoicing, Finance, Purchase and Inventory.

## 2. Accounting Menu Direction

```text
Accounting
├── Invoicing
├── General Ledger
├── Finance
└── Analytic Accounting
    ├── Dimensions
    ├── Allocation Rules
    ├── Budgets
    └── Analytic Reports
```

Candidate analytic dimensions include:

- Department
- Project
- Cost Center
- Branch
- Product Line
- Customer
- Sales Channel
- Business Unit

## 3. Project Menu Direction

```text
Project
├── Projects
├── Tasks
├── Milestones
├── Planning
├── Resources
├── Timesheets
├── Billing Status
├── Risks & Issues
└── Reports
```

## 4. Key Boundary

A company that only needs to identify which department / cost center owns a transaction does not need to open the Project module.

Example:

```text
Expense 100,000
GL = Repair Expense
Department = Production
```

A true project may use several dimensions at the same time:

```text
Vendor Bill 500,000
GL Account  = Subcontract Cost
Project     = PJ-2026-001
Department  = Engineering
Cost Center = CC-ENG-01
Branch      = Bangkok
```

## 5. Reporting Principle

`GL tells WHAT the accounting item is.`

`Analytic Dimension tells WHERE / WHY / FOR WHOM it belongs.`

Reports may include:

- P&L by Project
- P&L by Department
- P&L by Cost Center
- P&L by Branch
- Project Margin
- Department Expense

The same source transaction may be analyzed by multiple dimensions without GL proliferation.

## 6. Source-of-Truth Relationship

```text
Project
├── Tasks
├── Milestones
├── Planning
├── Resources
└── Operational Progress
         │
         ↓
      Project ID
         │
         ↓
Accounting
└── Analytic Accounting
    ├── Project Dimension
    ├── Department Dimension
    ├── Cost Center Dimension
    └── Other Dimensions
```

Financial values shown in Project dashboards are derived from source facts, for example:

- Contract Value / Billed / Invoice Status -> Invoicing / Sales source facts
- Recognized Revenue -> Accounting
- Collected Cash -> Finance
- Material Cost -> Inventory
- External Cost -> Purchase
- Labor Cost -> Timesheet / Workforce integration

Project dashboards must not create duplicate financial truth.

## 7. Constitutional Summary

`Project = manage work.`

`Analytic Accounting = manage financial dimensions.`

Do not force every analytic dimension to become a Project. Do not force every Project to carry full financial analysis.

No Evidence = No Progress.
Boss remains sole Final Approver.
