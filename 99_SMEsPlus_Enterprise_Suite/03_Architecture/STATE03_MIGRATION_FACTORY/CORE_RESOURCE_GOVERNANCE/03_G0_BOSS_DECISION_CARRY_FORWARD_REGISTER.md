# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G0 — Boss Decision Carry-Forward Register

Status: ACTIVE CONTROL REGISTER
Owner: SaaS Team under SMEs Core
Final Approver: Boss only

## Mandatory Carry-Forward Decisions

| ID | Decision | Status in Current Session |
|---|---|---|
| CF-01 | STANDARD = shared-resource multi-tenant Cells | CARRY FORWARD |
| CF-02 | ENTERPRISE = dedicated resource / dedicated tenant environment | CARRY FORWARD |
| CF-03 | No third PRIVATE commercial tier | CARRY FORWARD |
| CF-04 | One product / one Core codebase / many Cells | CARRY FORWARD |
| CF-05 | Tenant != Cell != Server != Database Host | CARRY FORWARD |
| CF-06 | Tenant Count != Capacity | CARRY FORWARD |
| CF-07 | Package size != deployment tier | CARRY FORWARD |
| CF-08 | Organization size is a sizing signal, not sole capacity determinant | CARRY FORWARD |
| CF-09 | Capacity must be measured as an envelope | CARRY FORWARD |
| CF-10 | No Surprise Billing | CARRY FORWARD |
| CF-11 | No Evidence = No Chargeable Overage | CARRY FORWARD |
| CF-12 | Prepaid Before Usage for additional chargeable consumption | CARRY FORWARD |
| CF-13 | 30-Day Notice != 30-Day Credit | CARRY FORWARD |
| CF-14 | No Unsecured Postpaid Overage | CARRY FORWARD |
| CF-15 | Wallet balance does not reset at month end | CARRY FORWARD |
| CF-16 | Historical usage evidence remains auditable/traceable | CARRY FORWARD |
| CF-17 | SMEsPlus defects/inefficiency are not customer usage | CARRY FORWARD |
| CF-18 | Customer logical quota != physical failure boundary | CARRY FORWARD |
| CF-19 | Heavy workloads may require preflight/reservation | CARRY FORWARD |
| CF-20 | STANDARD→ENTERPRISE is a supported normal upgrade path | CARRY FORWARD |
| CF-21 | Tenant identity and business semantics remain stable across mobility | CARRY FORWARD |
| CF-22 | No final package/capacity/pricing/topology freeze without evidence | CARRY FORWARD |
| CF-23 | Boss remains sole Final Approver | CARRY FORWARD |
| CF-24 | Build / Merge / Production not authorized by this session | CARRY FORWARD |

## Interpretation Controls

1. `Projected monthly bill` means projected accrued chargeable consumption / wallet deduction / secured charge estimate. It must not be interpreted as permission for unsecured postpaid debt.
2. `Overage` is valid only when pre-disclosed, measurable, traceable and financially authorized before chargeable consumption where required by the prepaid model.
3. `Protected Mode` must preserve integrity and prioritize restricting optional/high-growth workloads before critical ERP integrity transactions, subject to technical safety.
4. The approximate 1,500–3,500 THB/month Standard direction is a commercial hypothesis/direction only; it is not frozen pricing.
5. No physical host, DB, Cell, CPU or RAM amount is implied by package naming.

## Gate Control

Any later workstream that contradicts CF-01 through CF-24 must stop and produce a material evidence delta plus explicit contradiction disposition before continuing.
