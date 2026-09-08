# [SMEPLUS-26-09-06-SAAS-CELL-001]
# Boss Decision — Equipment vs Fixed Asset Boundary

Status: APPROVED DIRECTION / DETAIL DESIGN PENDING
Boss: Sole Final Approver
Date: 2026-09-08
Jira: ERPPLUS-151

## Decision

Boss APPROVED the separation between operational Equipment and accounting Fixed Assets.

### Core distinction

- Equipment = operational object used by the business.
- Fixed Asset = accounting classification/lifecycle for assets that meet the capitalization/accounting criteria.
- Not every Equipment is a Fixed Asset.
- An Equipment item may optionally link to a Fixed Asset record where applicable.

## Candidate navigation direction

### Operations

- Equipment
  - Equipment Register
  - Equipment Category
  - Location
  - Work Center Assignment
  - Maintenance
  - Usage / Meter
  - Calibration
  - Status

### Accounting

- Fixed Assets
  - Asset Register
  - Asset Models
  - Acquisitions
  - Depreciation
  - Transfers
  - Disposals
  - Reports

## Relationship model

Equipment
-> Operational Identity
-> Work Center / Maintenance / Calibration / Usage / Production
-> Optional Fixed Asset Link
-> Depreciation / Book Value / GL / Financial Statements

## Examples

- CNC machine: Equipment = Yes; Fixed Asset = Yes.
- Hand drill expensed at purchase: Equipment = Yes; Fixed Asset = No.
- Rental forklift: Equipment = Yes; Fixed Asset = No; ownership/rental context retained.
- Fully depreciated machine still in use: remains Equipment even when accounting depreciation is complete.

## Governance principle

"Every Fixed Asset may relate to Equipment, but not every Equipment is a Fixed Asset."

Operational lifecycle and accounting lifecycle remain separate responsibilities while preserving traceability between them.

No Team C / production authorization is granted by this decision.
No database topology is frozen.
No Evidence = No Progress.
Never Skip Gate.
