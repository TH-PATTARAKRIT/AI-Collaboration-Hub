# 12 — Replenishment / Reordering / Scheduler Map

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-05 OUTPUT — REPLENISHMENT PLANNING REFERENCE — NOT APPROVED DESIGN`
Clean-room boundary: replenishment is explained as business logic (demand, forecast, minimum, maximum, lead time, proposal, approval), which is the required transformation. No vendor scheduler architecture, rule engine, or job design is described or proposed.

Menus covered: MENU-OP-01 Replenishment, MENU-CF-12 Reordering Rules, MENU-OP-06 Run Scheduler.

---

## 1. Business Problem

Thai SMEs lose sales when stock runs out and lose cash when stock piles up. Replenishment answers, per product per warehouse: **when should we order (or make, or transfer) more, and how much?** The benchmark provides three cooperating pieces: a rule per product/location (min/max or forecast-based), a planning view that lists what should be ordered now, and a background job that periodically recomputes forecasts and creates proposed documents.

---

## 2. Reordering Rules — จุดสั่งซื้อ (MENU-CF-12)

| Aspect | Content |
|---|---|
| Purpose | State the policy: "keep between X and Y of this product at this location, sourced via this route". |
| Input | Product (variant), warehouse/location, minimum, maximum (or reorder quantity multiple), lead-time horizon (visibility days), preferred route (buy / manufacture / transfer from WH-A), trigger mode (automatic proposal vs manual review only), supplier and price list (Purchase-owned). |
| Process | Forecast = on hand + incoming (confirmed receipts/production) − outgoing (confirmed deliveries/consumption) within the horizon. If forecast < minimum, proposed quantity = maximum − forecast (rounded to multiple). |
| Output | Proposal line in the replenishment view; or, in automatic mode, a draft purchase/manufacturing/transfer request. |
| Control / Accounting impact | None on stock truth until the resulting document is done. Purchasing commitment control belongs to Purchase (approval limits). |
| Thai SME reading | "ถ้าสินค้าเหลือต่ำกว่า 20 ให้เติมจนถึง 100". |
| Candidate rules | Rule per product per warehouse; minimum/maximum in base UoM shown also in purchase UoM; automatic creation only with explicit tenant opt-in; every proposal carries an explanation (forecast components). |

---

## 3. Replenishment — เติมสินค้า / แผนเติมสินค้า (MENU-OP-01)

| Aspect | Content |
|---|---|
| Purpose | One screen where purchasing sees everything that needs replenishing, adjusts quantities, and confirms. |
| Input | Reorder rules, current forecasts, manually added products, optional snoozed lines. |
| Process | User reviews proposals → edits quantity/vendor/route → "สั่งเลย" (order now) creates the source document (PO / MO / transfer) → line disappears when the document is confirmed. Manual replenishment = human decides; automatic planning = system creates drafts on schedule. |
| Output | Purchase order (Purchase domain), manufacturing order (MFG), inter-warehouse transfer (Inventory). |
| Handoff | Inventory emits demand facts; Purchase owns the PO, price, vendor approval; MFG owns the MO. |
| Control / Accounting impact | No valuation until receipt. Control: who may confirm proposals; budget limits (Purchase). |
| Thai SME reading | Two tabs: "สินค้าใกล้หมด" (what needs ordering) and "แผนเติมสินค้า" (system proposals awaiting decision). |
| Evidence | Dispatch mechanism (demand → buy/manufacture/transfer) proven at reference level (reopen `02` item 24); replenishment as a *user process* never mapped before this session. Idempotency under concurrent retry `PARTIALLY SUPPORTED, not proven` (`C-02`). |

### Mandatory Process Questions

| # | Answer |
|---|---|
| 1 Business problem | Avoid stock-outs and over-stock with a repeatable rule instead of memory. |
| 2 Users | จัดซื้อ, เจ้าของ, หัวหน้าคลัง; ฝ่ายผลิตวางแผน (if MFG). |
| 3 Starting event | Scheduled forecast run; manual "check now"; sales order confirmation pushing forecast below minimum. |
| 4 Master data first | Products, warehouses, routes/templates, reorder rules, vendors (Purchase). |
| 5 Manual vs automated | Manual: review/edit/confirm. Automated: forecast computation, proposal creation, optional draft document creation. |
| 6 Quantity state change | None directly; creates planned incoming quantity when document is confirmed. |
| 7 Valuation handoff | None until receipt; purchase price is a Purchase/Accounting fact. |
| 8 Approval / SoD | Proposal confirm ≠ PO approval; automatic draft creation must be logged and cannot self-approve. |
| 9 What goes wrong | Duplicate proposals after retry; forecast ignores unconfirmed sales; min/max set in wrong UoM; rules on archived products; vendor lead time missing. |
| 10 Migration data | Reorder rules (min/max/route) as business policy; open proposals not migrated (regenerate). |
| 11 Thai name | เติมสินค้า / แผนเติมสินค้า. |
| 12 Must not copy | Benchmark scheduler/procurement architecture, rule-object model, job naming. |

---

## 4. Run Scheduler — ประมวลผลแผนสต็อก (MENU-OP-06)

| Aspect | Content |
|---|---|
| Purpose | Trigger, on demand, the background planning that normally runs on a timer: recompute forecasts, evaluate reorder rules, create proposals/drafts, reserve stock for ready documents, and cascade route chains. |
| Input | None from the user beyond "run now"; system reads all rules and pending demands. |
| Process | Deterministic batch: for each company → warehouse → rule: compute forecast, compare to minimum, create/adjust proposals; process pending demand chains; attempt reservations. |
| Output | New/updated proposals and draft documents; reservation state changes; run log. |
| Control / Accounting impact | No valuation. Control: must be idempotent (running twice must not double-propose); must be explainable; must be auditable (run id, start/end, counts, errors). |
| Thai SME reading | Not a user menu. Administrator sees "การประมวลผลอัตโนมัติ: ครั้งล่าสุด 02/09/2569 06:00 สำเร็จ (สร้างข้อเสนอ 12 รายการ)". |
| AI/automation boundary (Track 09) | The scheduler is deterministic control; AI may explain or flag anomalies (e.g. proposal 10× normal) but must not alter quantities or create stock facts. Benchmark evidence: reopen `11_AI_CONTROL` lists generalized anomaly-escalation threshold and deterministic replay protection as preconditions. |
| Evidence | Reopen `02` item 24, `11_AI_CONTROL`; menu-level: `PROCESS BENCHMARK` knowledge. |

---

## 5. Replenishment Handoff Map

```text
Sales order confirmed  ──demand──▶  forecast ↓  ──rule──▶  proposal ──user confirms──▶  PO (Purchase)  ──receipt──▶ Inventory on-hand ↑
Manufacturing need     ──demand──▶  forecast ↓  ──rule──▶  proposal ──user confirms──▶  MO (MFG)       ──production──▶ Inventory on-hand ↑
Branch warehouse low   ──rule──▶  proposal ──user confirms──▶  Transfer WH-A→WH-B (Inventory) ──receipt at B──▶ on-hand ↑ at B
```

Ownership: Inventory owns forecast facts and proposals; Purchase owns PO/vendor/price; MFG owns MO; Accounting receives nothing until receipt/production valuation.

---

## 6. Gaps Carried

| Gap ID | Item | Owner | Gate impact |
|---|---|---|---|
| GAP-MD-01 | Replenishment user process (review/confirm/snooze/explain) never studied at source; Thai purchasing practice input absent | Track 02, 05 / S5 | Team B precondition (conditional feature) |
| GAP-MD-21 | Scheduler/route idempotency under concurrent retry | Track 04, 09 / S3, S5 | Boss decision `C-02` |
| GAP-MD-23 | Forecast definition (which demands count) and Thai lead-time practice | Track 02 / S5 | Team B precondition |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
