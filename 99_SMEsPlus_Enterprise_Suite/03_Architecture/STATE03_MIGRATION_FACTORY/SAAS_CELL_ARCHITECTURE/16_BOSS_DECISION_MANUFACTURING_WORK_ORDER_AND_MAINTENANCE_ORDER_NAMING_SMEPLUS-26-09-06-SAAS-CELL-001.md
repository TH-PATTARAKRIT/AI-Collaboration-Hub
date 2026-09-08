# BOSS DECISION — MANUFACTURING WORK ORDER AND MAINTENANCE ORDER NAMING

Session: SMEPLUS-26-09-06-SAAS-CELL-001
Date: 2026-09-08
Status: APPROVED DIRECTION / DETAIL DESIGN PENDING
Boss: Sole Final Approver

## 1. APPROVED NAMING BOUNDARY

The term `Work Orders` is reserved for Manufacturing execution.

Manufacturing navigation:
- Manufacturing Orders
- Work Orders
- Work Centers
- Operations
- Production Reports

Thai localization direction:
- คำสั่งผลิต
- ใบสั่งงานผลิต
- ศูนย์งาน
- ขั้นตอนการผลิต
- รายงานการผลิต

Maintenance does NOT reuse the generic `Work Orders` label.

Maintenance navigation:
- Maintenance Requests
- Maintenance Orders
- Preventive Maintenance
- Corrective Maintenance
- Maintenance Plans
- Downtime
- Reports

Thai localization direction:
- แจ้งซ่อม
- ใบงานซ่อมบำรุง
- บำรุงรักษาเชิงป้องกัน
- ซ่อมบำรุงแก้ไข
- แผนซ่อมบำรุง
- เวลาหยุดเครื่อง
- รายงาน

## 2. SEMANTIC RULE

Manufacturing `Work Order` = production work to be executed for an Operation / Work Center.

Maintenance `Maintenance Order` = maintenance work to be executed against Equipment.

Approved rule:

> The same user-facing name should not be reused across different domains when it creates a material risk of user misinterpretation.

## 3. CROSS-DOMAIN RELATIONSHIP

Canonical relationship:

Manufacturing Work Order
-> Equipment Breakdown
-> Maintenance Request
-> Maintenance Order
-> Repair / Maintenance Completion
-> Equipment Available
-> Manufacturing Work Order Continues

The two domains remain connected, but their operational responsibilities and terminology remain distinct.

## 4. GOVERNANCE

- English remains the Canonical Product Language and default UI language.
- Thai remains controlled semantic localization.
- This decision supersedes any prior Maintenance candidate using the generic `Work Orders` label.
- No Team C / production authorization is created by this record.
- No Evidence = No Progress.
- Boss remains sole Final Approver.
