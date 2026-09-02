# 19 — Security, Permission and Audit Trail Register

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-07 OUTPUT — CONTROL REQUIREMENTS PER MENU — NOT APPROVED DESIGN`
Clean-room boundary: the reopen Council guardrail is applied verbatim in spirit: closing permission gaps by importing the reference system's access-group taxonomy or rule structure would cross the Reference-Only line. This register states control *requirements* in business terms only.

Standing facts (reopen `09`, `02` items 6, 38): company-level isolation enforced at application layer across stock-bearing records, no database backstop (`SAAS-03`), privileged-bypass audit never performed; warehouse-level authorization unknown (`U-01`); operation-level role segregation unitemized; done-move history append-only (positive); global unaudited backdate bypass (`G-2`); PDPA research absent; interface authentication architecture not yet existing.

---

## 1. Permission Axes (candidate)

| Axis | Values | Status in evidence |
|---|---|---|
| Tenant / company | one company per record | ORM-layer proven; DB backstop absent |
| Warehouse | user ↔ warehouses allowed | `UNKNOWN` (`U-01`) |
| Operation type / action | receive, deliver, transfer, count, adjust-approve, scrap-request, scrap-approve, unlock-period, configure | unitemized |
| Data visibility | cost visibility (accountant/owner only), vendor prices | not studied |

---

## 2. Register by Menu

| Menu ID | Roles (candidate) | Segregation of duties | Destructive / fraud-prone actions | Audit trail required | Recovery / concurrency | Status |
|---|---|---|---|---|---|---|
| OP-01 Replenishment | จัดซื้อ confirm; admin rules | Proposal confirm ≠ PO approval | Mass auto-creation of drafts | Run id, who confirmed, quantities edited | Duplicate proposals under retry (`C-02`) | PARTIAL |
| OP-02 Adjustments | คลัง count; หัวหน้าคลัง approve; บัญชี view; auditor witness | Counter ≠ approver; threshold → second approver | Absorbing interim moves into count; backdating; large silent deltas | Count session, counters, differences, reason, approver, timestamps; immutable after apply | Concurrent count vs receiving; conflict policy (four options) | PARTIAL (`GAP-MD-02/03`) |
| OP-03 Transfers | คลัง validate; หัวหน้าคลัง override | Validator ≠ order approver | Over-receipt/over-delivery; validate wrong lot; cancel chain | Every state change with user/time; done immutable | Reservation race (`C-04`); duplicate validation (`C-02`) | PARTIAL |
| OP-04 Scrap | คลัง request; หัวหน้าคลัง approve; บัญชี/ภาษี view | Requester ≠ approver; statutory witness | Scrapping sellable stock to hide theft | Reason, evidence, approver, lot, cost | — | PARTIAL (`GAP-MD-04`) |
| OP-05 Landed costs | บัญชี | Accounting approval | Allocation to closed period | Allocation record | — | PARTIAL |
| OP-06 Scheduler | admin trigger | Cannot create done moves | Double run | Run log (start, end, counts, errors) | Idempotent runs | COVERED |
| PR-01 Products | จัดซื้อ/เจ้าของ create; บัญชี cost | Type/cost change approval | Kind change with stock; delete with history | Field-level change log for type, UoM, category, cost | — | COVERED |
| PR-02 Variants | as PR-01 | — | Delete stocked variant | Change log | — | PARTIAL |
| PR-03 Lots/Serials | คลัง create on receipt; QA edit | Lot immutable after first move | Serial reuse | Lot history | Serial uniqueness under concurrency | PARTIAL (`GAP-MD-11`) |
| RP-01..06 Reports | by role; cost visibility restricted | — | Export of full stock/cost data (PDPA if customer data on delivery docs) | Export log | — | COVERED |
| CF-01 Settings | admin only | Owner acknowledgement for structural switches | Turning off features with dependent data; enabling global bypass | Before/after per switch, user, time | — | COVERED (`GAP-MD-14`) |
| CF-02/03 Warehouses, Locations | admin | — | Archive location with stock | Change log | — | COVERED (`U-01`) |
| CF-04/05 Routes, Rules | admin (advanced) | Preview + confirm | Silent regeneration of flows | Version history | — | COVERED |
| CF-06 Operation types | admin | Role assignment per type is the SoD unit | Changing default locations mid-operation | Change log | — | PARTIAL (`GAP-MD-22`) |
| CF-07/08 Storage, Putaway | หัวหน้าคลัง | — | — | Rule change log | — | PARTIAL |
| CF-09 Categories | บัญชี + admin | Policy change approval with effective date | Category move altering valuation | Policy history | — | PARTIAL (Joint) |
| CF-10..14 Attributes, Packagings, Reorder, Barcode, UoM | admin / จัดซื้อ | Base unit immutable | Retroactive factor edit | Version history | — | COVERED |

---

## 3. Period and Backdate Control (cross-menu)

| Requirement | Benchmark position (Layer 1) | SMEsPlus candidate |
|---|---|---|
| Movement date cannot fall in a closed period | Document-level guard via accounting bridge only; adjustments may bypass; global unaudited toggle | Native Inventory period guard on every movement; exception = user + reason + expiry + record; hard lock never exceptable |
| Who may grant exceptions | Admin toggle | บัญชี role with audit; never warehouse staff |
| Sequencing with Accounting close | Mechanisms never call each other (`G-1`) | Joint Session design |

---

## 4. Privacy (PDPA) note

Inventory documents carry customer names/addresses on delivery notes and vendor data on receipts. PDPA research is absent from the whole chain (reopen `09`). Candidate: scope PDPA review jointly with Account/Legal before any production design; minimise personal data on warehouse-facing screens. Status `HOLD / EVIDENCE REQUIRED` (`GAP-MD-29`).

---

## 5. Gaps and Gate Impact

| Gap ID | Item | Owner | Gate impact |
|---|---|---|---|
| U-01 | Warehouse-level authorization | Track 07; Boss scope ruling | Team B precondition |
| GAP-MD-22 | Operation-level SoD matrix and Thai role names | Track 07, 02 / S1 | Team B precondition |
| GAP-MD-03 | Native period guard and audited exception model | Track 06, 07; Joint | Blocks Joint Backbone publication |
| GAP-MD-29 | PDPA scope for Inventory documents | Track 07; Account/Legal | Pre-production |
| SAAS-03 | DB-layer tenant backstop; bypass audit | Track 05, 07 | Team B precondition |
| C-04 | Reservation locking verification | Track 07 / Team A | Bounded verification |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
