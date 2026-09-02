# 13 — Inventory Adjustment and Scrap Control Map

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-05 OUTPUT — EXCEPTION PROCESS REFERENCE (COUNT, ADJUSTMENT, SCRAP) — NOT APPROVED DESIGN`
Clean-room boundary: process and control learning only. The benchmark's count-conflict mechanism is described in business terms as established by the reopen package (`N-A7-01`, `CORR-007B`); no wizard, model, or method is named or proposed.

Menus covered: MENU-OP-02 Inventory Adjustments (including physical count), MENU-OP-04 Scrap.

---

## 1. Inventory Adjustments — ปรับปรุงยอดสต็อก (MENU-OP-02)

### 1.1 Two sub-processes Thai users actually run

| Sub-process | Thai name | Trigger | Who |
|---|---|---|---|
| A. Physical count (cycle or full) | นับสต็อก / ตรวจนับสินค้า | Scheduled cycle count; year-end count with auditor witness; suspicion of discrepancy | คลัง counts; หัวหน้าคลัง reviews; บัญชี/ผู้สอบบัญชี witnesses at year-end |
| B. Direct adjustment | ปรับปรุงยอดสต็อก | Known error (wrong receipt qty, breakage found, theft, migration opening balance) | หัวหน้าคลัง requests; approver approves |

### 1.2 Process A — Physical Count (candidate reference)

```text
1. Plan count      : choose scope (warehouse / location / category / product / lot), date, counters       -> count sheet (ใบตรวจนับ) generated with system quantity hidden or shown (policy)
2. Freeze policy   : decide whether movements in scope are blocked, warned, or allowed during count      -> policy record (see 1.4)
3. Count           : counters enter counted quantity (paper -> keyed, or mobile/scan)                    -> counted lines with counter identity and time
4. Compare         : system computes difference = counted - system at count time                          -> difference list; large differences flagged by threshold
5. Recount         : disputed lines recounted by a second person                                          -> second count recorded
6. Approve         : approver reviews differences with reason codes                                       -> approved adjustment set
7. Apply           : approved differences become movements (adjustment location <-> stock location), effective date = count date -> on-hand corrected; valuation delta emitted
8. Close & archive : count closed; sheet, counters, approver, differences retained                        -> audit pack
```

Benchmark evidence (business level): the reference detects when stock moved between "count entered" and "count applied" and asks the user to choose which quantity to keep; it does **not** hard-freeze movements. The freeze policy is a design choice with four named options (hard freeze / soft warning as-is / location-session lock / manager exception) and remains a Team B decision (`N-A7-01`, `INV-FP-08`, reopen `05_IBPV`, `09_SECURITY`). Any user permitted to apply a count can absorb an intervening movement into the adjustment without privileged sign-off (reopen `09` §3) — a control weakness SMEsPlus must not inherit by default.

### 1.3 Process B — Direct Adjustment

```text
1. Request : user selects product/location/lot, enters new quantity or delta, reason code (mandatory), attaches evidence (photo, memo)
2. Review  : approver checks; threshold rules (value or % of on-hand) may require second approver or Accounting acknowledgement
3. Apply   : movement adjustment <-> stock, effective date within open period only (period guard)
4. Report  : adjustment register (ทะเบียนการปรับปรุง) updated; valuation delta emitted to Accounting
```

### 1.4 Controls required (candidate)

| Control | Why | Evidence / status |
|---|---|---|
| Mandatory reason code (นับผิด / เสียหาย / สูญหาย / รับผิด / ยอดยกมา / อื่น ๆ) | Audit and tax review | Reopen `04_TBRAC` (no Thai count practice evidence) — `HOLD` on Thai reason taxonomy |
| Approval by a role other than the counter | Segregation of duties | Reopen `02` item 38: operation-level SoD unitemized (`U-01`-adjacent) |
| Freeze/conflict policy explicit per tenant | Prevent silent absorption of interim moves | `N-A7-01` design options; Team B decision |
| Period guard: adjustments cannot be dated into a closed period; exceptions need user, reason, expiry | Benchmark: adjustments may bypass document-level lock check; global bypass toggle unaudited (`G-2`, `G-3`) | Reopen `02` item 31; `09_SECURITY`; Joint Session item |
| Value-threshold escalation | Large adjustments are fraud-prone | Candidate; no evidence |
| Adjustment register report | Auditor and management visibility | Report TH-R07 |
| Immutable after apply; correction = new adjustment | Append-only movement history | Reopen `02` item 38 (positive control confirmed) |

### 1.5 Mandatory Process Questions

| # | Answer |
|---|---|
| 1 Business problem | Keep the system quantity equal to the physical quantity, with an auditable reason for every difference. |
| 2 Users | คลัง, หัวหน้าคลัง, บัญชี, ผู้สอบบัญชี (witness at year-end). |
| 3 Starting event | Count schedule, discovered discrepancy, year-end audit, migration opening balance. |
| 4 Master data first | Products, locations, lots; reason codes; approval roles. |
| 5 Manual vs automated | Manual: counting, reason, approval. Automated: difference calculation, threshold flags, movement creation. |
| 6 Quantity state change | On-hand changes by the approved difference; reservations may be affected. |
| 7 Valuation handoff | Adjustment delta × unit cost (per costing policy) → Accounting as inventory gain/loss fact; Accounting decides account and period. |
| 8 Approval / SoD | Counter ≠ approver; large deltas escalate; year-end count witnessed. |
| 9 What goes wrong | Counting during receiving; counting in wrong UoM; applying stale counts; backdating; adjustments used to hide theft; opening-balance adjustments with no source. |
| 10 Migration data | Historical adjustments as movements with reason and approver; opening balance as a certified adjustment at cutover (`G-5`: no reference mechanism exists — human certification required). |
| 11 Thai name | ปรับปรุงยอดสต็อก (with นับสต็อก as sub-flow). |
| 12 Must not copy | Benchmark's conflict wizard flow, soft-only default, global bypass toggle. |

---

## 2. Scrap — ตัดสินค้าชำรุด/สูญเสีย (MENU-OP-04)

### 2.1 Process (candidate reference)

```text
1. Identify   : damaged / expired / lost / obsolete item found (at receiving, in stock, at return, in production)
2. Request    : scrap document: product, lot/serial, qty, from location, reason (ชำรุด / หมดอายุ / สูญหาย / ล้าสมัย / ทำลายตามระเบียบ), photo/evidence, optional source document (receipt, return, MO)
3. Approve    : หัวหน้าคลัง approves; above threshold บัญชี acknowledges; for tax-deductible destruction, statutory witness step (see 2.3)
4. Execute    : movement stock -> loss location (สินค้าเสีย); lot/serial history updated; on-hand reduced
5. Dispose    : physical disposal / return to vendor / sale as scrap (Sales domain) recorded as follow-up
6. Report     : scrap register (ทะเบียนตัดสินค้าเสีย); valuation delta emitted to Accounting as loss fact
```

Benchmark evidence: a dedicated scrap document exists routing stock to a loss location; a generic return flow exists; **no distinct "damaged goods" exception category** exists anywhere in nine rounds (`U-02`, reopen `13`). Whether SMEsPlus needs a damaged-goods state separate from scrap (for example "hold for vendor claim" before scrapping) is an open Thai-practice question.

### 2.2 Distinctions Thai users need

| Situation | Not scrap | Scrap |
|---|---|---|
| Damaged at receiving, vendor will replace | ส่งคืนผู้ขาย (return to vendor) | — |
| Damaged in stock, claimable | Hold in "รอเคลม" location (candidate) | Scrap after claim decision |
| Expired | — | Scrap with reason หมดอายุ; lot recorded |
| Lost / theft | Adjustment with reason สูญหาย (police report attachment) or scrap — policy choice | — |
| Obsolete but sellable | Sell at discount (Sales) | — |
| Destruction for tax deduction | — | Scrap with statutory destruction evidence |

### 2.3 Thai statutory dimension (claim held, evidence required)

Thai practice commonly requires documented destruction procedures (witness, notice, inspection report) for inventory write-offs to be tax-deductible and for VAT treatment. **This session does not assert the legal rule.** Per Council 06 rule, statutory claims require authoritative evidence: `HOLD / EVIDENCE REQUIRED` (`GAP-MD-04`), owner Track 06 / Accounting-Tax track. Inventory's job is to emit the facts a destruction report needs: product, lot, qty, cost, date, reason, witnesses, approver, photos.

### 2.4 Controls required (candidate)

| Control | Status |
|---|---|
| Reason code mandatory; photo/evidence attachment | Candidate |
| Approval by role above requester; value threshold escalation | Candidate; SoD unknown in evidence |
| Lot/serial recorded on scrap line (recall, warranty) | Carry-forward from lot facts |
| Scrap register report with cost | Report TH-R08 |
| Scrap location cannot be a source for deliveries | Candidate (loss location is a sink) |
| Period guard as for adjustments | Joint Session item (`G-2`/`G-3`) |

### 2.5 Mandatory Process Questions

| # | Answer |
|---|---|
| 1 Business problem | Remove unusable stock from the books with an approved reason and an accounting loss fact. |
| 2 Users | คลัง, หัวหน้าคลัง, QA, บัญชี, ภาษี (destruction evidence). |
| 3 Starting event | Damage/expiry/loss discovered; QC rejection; return inspection. |
| 4 Master data first | Loss location, reason codes, approval roles, lot tracking where applicable. |
| 5 Manual vs automated | Manual: request, evidence, approval. Automated: movement, valuation delta, expiry watch list feeding candidates. |
| 6 Quantity state change | On-hand reduced; lot balance reduced; reservations released if any. |
| 7 Valuation handoff | Qty × cost (per policy) → Accounting as inventory loss; account/period is Accounting's. |
| 8 Approval / SoD | Requester ≠ approver; statutory witness for destruction. |
| 9 What goes wrong | Scrap used to hide theft; scrapping sellable goods; wrong lot; missing destruction evidence causing non-deductibility; scrap dated into closed period. |
| 10 Migration data | Historical scrap movements with reason; loss-location balances should be zero at cutover. |
| 11 Thai name | ตัดสินค้าชำรุด/สูญเสีย. |
| 12 Must not copy | Benchmark scrap document shape; loss-location naming; absence of damaged-goods state as a design default. |

---

## 3. Gaps Carried

| Gap ID | Item | Owner | Gate impact |
|---|---|---|---|
| GAP-MD-02 | Count freeze / conflict policy selection; approval and reason taxonomy for Thai counts; year-end witnessed count flow | Track 03, 02 / S1; Team B | Team B precondition |
| GAP-MD-03 | Adjustment period guard independent of Accounting bridge; audited exception model (`G-2`/`G-3`) | Track 06, 07 / S6; Joint Session | Blocks Joint Backbone publication |
| GAP-MD-04 | Thai statutory destruction evidence rule for scrap deductibility | Track 06 / Accounting-Tax | `HOLD / EVIDENCE REQUIRED` |
| U-02 | Damaged-goods state distinct from scrap | Track 02, 03 / S1 | Team B precondition |
| G-5 | Opening-balance adjustment at cutover — no reference mechanism; human certification required | Joint Session; Track 09 | Blocks migration authorization |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
