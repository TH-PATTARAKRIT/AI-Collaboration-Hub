# 11 — Operation Types and Stock Flow Map

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-05 OUTPUT — OPERATION TYPE AND MOVEMENT-STATE REFERENCE — NOT APPROVED DESIGN`
Clean-room boundary: the movement lifecycle below is written as business states in Thai user language. The benchmark's state machine, document model, and benchmark document-type vocabulary are explicitly **not** adopted (reopen `05_IBPV` §7 names this vocabulary as a transcription risk for Team B).

Menus covered: MENU-CF-06 Operations Types; feeds MENU-OP-03 Transfers, MENU-RP-03/04 Moves History and Stock Moves.

---

## 1. Operation Type — ประเภทรายการคลัง (MENU-CF-06)

| Aspect | Content |
|---|---|
| Purpose | Define each kind of stock document a warehouse issues, with its own number series, default from/to locations, allowed actions, and responsible role. |
| Input | Name (Thai), warehouse, direction (inbound / outbound / internal / manufacturing), number prefix and sequence, default source and destination location, return counterpart type, reservation policy (reserve on confirm / manual / at scheduled date), whether lots must be pre-assigned, whether new lots may be created here, print templates. |
| Process | Created automatically per warehouse for the three basic types; extra types added for QC, packing, putaway, manufacturing, returns. Every transfer document belongs to exactly one operation type. |
| Output | Document series per type (e.g. RC-2026-00001); dashboard counts per type (to do / late / waiting). |
| Control / Accounting impact | Direction decides whether the document crosses the company boundary (inbound from vendor / outbound to customer) and therefore triggers valuation and accounting handoff. Permissions per type are the natural segregation-of-duties unit (unitemized in prior evidence, reopen `02` item 38). Benchmark caveat: operation "kind" is a string literal in the source, a migration-coupling risk (reopen `02` item 14). |
| Thai SME reading | ใบรับสินค้า (RC), ใบจ่ายสินค้า/ใบส่งของ (DO), ใบโอนย้ายภายใน (TR), ใบรับคืน (RT), ใบเบิกผลิต (MI), ใบรับสินค้าสำเร็จรูป (MO-IN). |

Candidate SMEsPlus operation-type set (per warehouse):

| Type ID | Thai document name | Direction | From → To | Valuation event | Default role |
|---|---|---|---|---|---|
| OT-RC | ใบรับสินค้า | Inbound | ผู้ขาย → คลัง (or รับเข้า) | Receipt valuation | คลัง (receiver) |
| OT-DO | ใบจ่ายสินค้า / ใบส่งของ | Outbound | คลัง → ลูกค้า | COGS / issue valuation | คลัง (picker/shipper) |
| OT-TR | ใบโอนย้ายภายใน | Internal | คลัง → คลัง/ตำแหน่ง | None (same company) | คลัง |
| OT-RTC | ใบรับคืนจากลูกค้า | Inbound | ลูกค้า → คลัง | Return valuation (cost basis is `C-03` conflicting) | คลัง + ฝ่ายขาย |
| OT-RTV | ใบส่งคืนผู้ขาย | Outbound | คลัง → ผู้ขาย | Reverse receipt valuation | คลัง + จัดซื้อ |
| OT-QC | ใบตรวจคุณภาพ | Internal | รับเข้า → ตรวจคุณภาพ → คลัง | None | QC |
| OT-PA | ใบจัดเก็บเข้าที่ | Internal | รับเข้า → ตำแหน่ง | None | คลัง |
| OT-PK | ใบหยิบ / ใบแพ็ก | Internal | คลัง → รอจัดส่ง | None | คลัง |
| OT-MI / OT-MOUT | ใบเบิกผลิต / ใบรับผลิต | Manufacturing | คลัง → การผลิต → คลัง | Consumption / production valuation (Accounting interface; WIP gap `FIN-DELTA-01`) | ฝ่ายผลิต |
| OT-ADJ | รายการปรับปรุงยอด | Exception | ปรับปรุง ↔ คลัง | Adjustment valuation | หัวหน้าคลัง (approver) |
| OT-SCR | รายการตัดสินค้าเสีย | Exception | คลัง → สินค้าเสีย | Scrap valuation | หัวหน้าคลัง + บัญชี |

OT-ADJ and OT-SCR are listed as exception types so that permissions and reports treat them distinctly; whether they are "operation types" in SMEsPlus design is a Team B decision.

---

## 2. Movement Lifecycle — Business States (candidate, Thai)

```text
ร่าง (draft)  ->  รอสินค้า (waiting: upstream not done / not available)
             ->  จองแล้ว (reserved: stock allocated, not yet moved)
             ->  พร้อมดำเนินการ (ready)
             ->  เสร็จสิ้น (done: physical fact recorded, immutable)
             ->  ยกเลิก (cancelled: before done only)
```

Rules (business level, candidate):

| Rule | Meaning | Evidence |
|---|---|---|
| Only "done" changes on-hand | Planned/reserved quantities are not stock truth | Reopen `02` items 7–11 |
| Reservation reduces "available", not "on hand" | Three quantities: on hand, reserved, available | Reopen `02` items 8–10 |
| Done movements are append-only | No un-done; correction is a reverse movement with reason | Reopen `02` item 38 (append-only confirmed as positive control) |
| Partial completion creates a backorder (remaining planned quantity) or is explicitly closed short | User must choose: สร้างใบค้างส่ง / ปิดยอดที่เหลือ | Reopen `02` item 15 (representation heterogeneity is an open design item) |
| Cancellation after done is impossible; before done it releases reservations and, if driven by a sales/purchase cancellation, cascades along the chain | Cascade symmetry for purchase side is `C-01` conflicting | Reopen `13` C-01 |
| Over-receipt / over-delivery has no ceiling in the benchmark | SMEsPlus must decide a tolerance policy (`GAP-MD-06`) | Reopen `02` item 28; `05_IBPV` §10 item 1 |
| Backdating a done movement into a closed period is blocked only at document level via the accounting bridge; adjustments may bypass | SMEsPlus should own a native period guard | Reopen `02` item 31; `05_IBPV` §10 item 7 |

---

## 3. Stock Quantity Facts per Movement (what the fact ledger must carry)

| Fact | Required | Why |
|---|---|---|
| Document + line identity, operation type | Yes | Audit trail, numbering |
| Product / variant, lot/serial, package | Yes | Identity |
| From location, to location | Yes | Conservation |
| Planned quantity, done quantity, UoM entered, base quantity | Yes | Partial/backorder logic; UoM audit |
| Scheduled date, done date (effective date) | Yes | Period cut-off |
| Source document (SO / PO / MO / count / scrap / manual) | Yes | Handoff traceability |
| Reservation link | Yes | Availability |
| Cost basis reference (for valuation handoff) | Yes (as reference, not value ownership) | Accounting interface |
| User who created / confirmed / validated; reason code for exceptions | Yes | SoD, audit |
| Idempotency key (source line + attempt) | Yes (SMEsPlus original) | Replay safety (`C-02`) |

---

## 4. Segregation of Duties Matrix (candidate; unknown in prior evidence)

| Action | คลัง (staff) | หัวหน้าคลัง | จัดซื้อ | ฝ่ายขาย | บัญชี | ผู้ดูแลระบบ |
|---|---|---|---|---|---|---|
| Create receipt from PO | ✔ | ✔ | (view) | – | – | – |
| Validate receipt (done) | ✔ | ✔ | – | – | – | – |
| Create delivery from SO | ✔ | ✔ | – | (view) | – | – |
| Validate delivery | ✔ | ✔ | – | – | – | – |
| Internal transfer | ✔ | ✔ | – | – | – | – |
| Start count | ✔ | ✔ | – | – | – | – |
| Approve adjustment | – | ✔ | – | – | (view) | – |
| Scrap request / approve | ✔ / – | – / ✔ | – | – | (view) | – |
| Unlock backdate / period exception | – | – | – | – | ✔ (with reason, expiry) | ✔ |
| Edit operation type / warehouse setup | – | – | – | – | – | ✔ |

This matrix is a candidate for real Thai user validation (TBRAC gap) and Track 07 ruling; it is not evidence.

---

## 5. Gaps Carried

| Gap ID | Item | Owner | Gate impact |
|---|---|---|---|
| GAP-MD-06 | Over-receipt / over-delivery tolerance policy brief (parity with count-freeze brief) | Track 03 / S1 | Team B precondition |
| GAP-MD-07 | Partial/backorder representation and return sub-flows as one Thai user flow | Track 03 / S1 | Team B precondition |
| GAP-MD-22 | Operation-type-level SoD and Thai document numbering standards | Track 07, 02 / S1, S8 | Team B precondition |
| C-01 | Purchase-side cancellation cascade re-trace | Track 01 / Team A | Bounded verification |
| C-02 | Idempotency severity/ownership | Boss | Boss decision |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
