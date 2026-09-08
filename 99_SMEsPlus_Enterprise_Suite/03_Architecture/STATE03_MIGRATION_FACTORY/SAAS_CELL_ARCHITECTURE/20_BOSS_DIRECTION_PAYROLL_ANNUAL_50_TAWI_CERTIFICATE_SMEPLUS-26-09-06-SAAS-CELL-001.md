# Boss Direction — Payroll Annual 50 Tawi Certificate

Session: `[SMEPLUS-26-09-06-SAAS-CELL-001]`
Jira: `ERPPLUS-151`
Status: BOSS-DIRECTED REQUIREMENT / DETAIL DESIGN PENDING

## Decision

The HR `Payroll & Benefits` capability must include Thai employee withholding-tax certificate support for the annual `50 Tawi` document.

Canonical Thai term:

`หนังสือรับรองการหักภาษี ณ ที่จ่าย ตามมาตรา 50 ทวิ`

Recommended English product label:

`Withholding Tax Certificate (50 Tawi)`

## Placement

`HR -> Payroll & Benefits -> Tax & Social Security -> Withholding Tax Certificate (50 Tawi)`

The certificate is a Payroll tax-output document derived from approved payroll and withholding-tax facts. It must not create a separate or duplicate tax truth.

## Required Data Lineage

`Payroll Periods -> Payroll Runs -> Employee Taxable Income -> Withholding Tax -> Year-to-Date Tax Summary -> 50 Tawi Certificate`

The certificate must remain traceable back to the payroll runs and withholding calculations that produced the annual totals.

## Important Boundary

- Payroll calculates employee income and withholding-tax facts.
- 50 Tawi is an employee tax certificate generated from those approved facts.
- Accounting posting and Finance payment remain separate responsibilities.
- The document must be versioned and reproducible from source payroll facts.
- Reissue/correction must preserve audit history; previously issued evidence must not be silently overwritten.

## Thai Statutory Timing Baseline

For employment income under Section 50(1), the certificate is generally required by 15 February of the following tax year, or within one month when the employee leaves during the tax year. This timing should be treated as a statutory rule subject to controlled legal/tax configuration and current-law verification.

## Proposed Payroll Child Structure Delta

Under `HR-07 Payroll & Benefits`, add:

- `Tax & Social Security`
  - `Employee Withholding Tax`
  - `Year-to-Date Tax Summary`
  - `Withholding Tax Certificate (50 Tawi)`
  - `Certificate Reissue / Correction`

This record does not approve the full Payroll detail design. It records only the Boss-directed inclusion of the 50 Tawi employee annual tax certificate requirement.

Boss remains the sole Final Approver.

No Evidence = No Progress.
Never Skip Gate.
