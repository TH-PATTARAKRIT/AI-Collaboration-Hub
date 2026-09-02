# 15 — Landed Cost / Valuation / Accounting Handoff Map

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-05 / CP-07 OUTPUT — VALUATION AND ACCOUNTING-INTERFACE REFERENCE — NOT APPROVED DESIGN, NOT AN ACCOUNTING RULING`
Clean-room boundary: valuation learning is taken only from Layer 1 clean-room summaries (CORR-007B files `08`/`09` rewritten at commit `9996072a`) and reopen `08_FINANCIAL`. `C-05` remains Boss-visible: no Layer 2 material was opened by this session. Accounting boundary discipline: every item is classified with the CP-07 taxonomy; Inventory closes nothing that belongs to Accounting.

Menus covered: MENU-OP-05 Landed Costs, MENU-RP-05 Valuation, MENU-CF-09 Product Categories (valuation policy).

---

## 1. Ownership Statement (carry-forward, unchanged)

| Domain | Owns | Emits / receives |
|---|---|---|
| Inventory (Stock Truth) | Quantities, movements, lots, locations, cost-basis *references* per movement, adjustment/scrap deltas, landed-cost allocation *facts* | Emits valuation facts |
| Accounting (Financial Truth) | Valuation policy decision (timing, method), accounts, journal design, period close, GL reconciliation, retained earnings, tax | Receives facts; decides postings |
| Joint (Session 3) | `N-A12-01` in full, `G-1`, `G-2`, `G-5`, `G-6`, posting-architecture fork, return cost basis (`C-03`), Product Category redesign | — |

Standing status: `N-A12-01 = HIGH FUNCTIONAL DESIGN GAP — REOPENED`; `Account + Inventory Backbone Reference Baseline = HOLD` (CORR-007B, reconfirmed by reopen `08`, `14`, `20`). This session does not change it.

---

## 2. Valuation — มูลค่าสินค้าคงเหลือ (MENU-RP-05) as a process

| Aspect | Content |
|---|---|
| Purpose | Tell the accountant and owner what the stock on hand is worth, by product/category/location, as of a date, under the company's costing policy, and reconcile it to the GL. |
| Input | Done movements with quantities; cost basis per movement (purchase cost, landed cost, production cost, adjustment cost); costing method per category (standard / average / FIFO); valuation timing (periodic vs perpetual). |
| Process | Perpetual: each valued movement produces a value change that Accounting posts immediately (or receives as an event). Periodic: value is computed at period close from quantities and cost, and a closing entry trues up GL. Both are policy choices; the benchmark separates them by a single per-movement gate (Layer 1 summary). |
| Output | Valuation report as of date; valuation change facts; period-close valuation summary (opening value, receipts value, issues value, adjustments, closing value). |
| Control / Accounting impact | Highest. Reconciliation of valuation report to GL inventory account is the audit test. Benchmark: the one reconciliation report's export is a stub (`G-7`); no year-end retained-earnings entry exists in the reference (`G-6`) — Thai practice expects one; a late vendor bill silently changes a closed period's recomputed value (`FIN-DELTA-04`). |
| Thai reading | มูลค่าสินค้าคงเหลือ ณ วันที่ … ตามนโยบายต้นทุน (ถัวเฉลี่ย / FIFO / มาตรฐาน); กระทบยอดกับบัญชีสินค้าคงเหลือ. |
| Classification | `ACCOUNTING_INTERFACE_REQUIREMENT` for the facts; `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` for method/timing/close design; `PENDING_ACCOUNT_SESSION` for Thai costing norm (`TH-INV-03` → `COA-G06`). |

### 2.1 Valuation facts Inventory must be able to emit (candidate minimum)

| Fact | Per | Notes |
|---|---|---|
| Opening quantity and value | product × location × period | From prior close or certified cutover (`G-5`) |
| Receipt quantity and cost basis | movement | Cost basis reference: PO price / vendor bill / landed cost allocation |
| Issue quantity and cost (per method) | movement | Method computed by valuation engine (owner TBD Joint) |
| Adjustment / scrap quantity and cost | movement | With reason |
| Production consumption / output cost | movement | WIP handling is a gap (`FIN-DELTA-01`) |
| Landed cost allocation | receipt line | See §3 |
| Closing quantity and value | product × location × period | Must equal opening + in − out ± adjustments |
| Valuation method and policy version used | period | For audit |

---

## 3. Landed Costs — ต้นทุนสินค้าเพิ่มเติม (MENU-OP-05)

| Aspect | Content |
|---|---|
| Purpose | Add freight, insurance, customs duty, brokerage, and other acquisition costs to the value of received goods so that stock value and COGS reflect true cost. |
| Input | Landed-cost document: vendor bill(s) for the extra costs (Accounting), the receipts to which they apply, allocation method (by quantity / by weight / by volume / by value / equal), cost type → account mapping (Accounting-owned). |
| Process | Select receipts → enter cost lines → compute allocation per receipt line → review → validate: each receipt line's cost basis increases by its share; valuation facts emitted. |
| Output | Allocation statement per receipt line (TH-R13); adjusted cost basis; accounting facts. |
| Control / Accounting impact | Benchmark (Layer 1, reopen `08`): allocation allowed only for average/FIFO-costed products (standard cost raises an error); allocation methods by quantity/weight/volume/equal; landed-cost postings are protected by the accounting lock date; the periodic/standard-cost path is present but disabled in source ("never read" — reopen `15` §D). Thai importers commonly incur duty + VAT at import; VAT is not a cost (input tax) — statutory claim `HOLD`. |
| Thai reading | ค่าขนส่ง, ค่าประกัน, อากรขาเข้า, ค่าชิปปิ้ง ปันส่วนเข้าต้นทุนสินค้าตามจำนวน/น้ำหนัก/ปริมาตร/มูลค่า. |
| Classification | `ACCOUNTING_INTERFACE_REQUIREMENT` (allocation facts); `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` (which costing methods allow landed cost; posting design); `PENDING_ACCOUNT_SESSION` (import VAT/duty treatment). |
| Evidence status | `HOLD / EVIDENCE REQUIRED` for full allocation mechanism (`GAP-MD-05`); business process above is `PROCESS BENCHMARK` knowledge plus reopen `08` facts. |

### 3.1 Mandatory Process Questions — Landed Costs

| # | Answer |
|---|---|
| 1 Business problem | Imported goods cost more than the supplier invoice; margins are wrong without it. |
| 2 Users | จัดซื้อ/นำเข้า, บัญชี; คลัง only supplies receipts. |
| 3 Starting event | Freight/duty/broker bill arrives after (or before) receipt. |
| 4 Master data first | Landed cost types with account mapping (Accounting), receipts validated, costing method per category. |
| 5 Manual vs automated | Manual: select receipts, choose method, review. Automated: allocation math, cost basis update, fact emission. |
| 6 Quantity state change | None. |
| 7 Valuation handoff | Value-only change per receipt line → Accounting posting per policy. |
| 8 Approval / SoD | Accounting approval; cannot post into closed period. |
| 9 What goes wrong | Allocating to already-sold goods (COGS restatement); allocating VAT; double allocation; standard-cost products; currency. |
| 10 Migration data | Historical landed-cost allocations as cost history (Accounting) — not re-created. |
| 11 Thai name | ต้นทุนสินค้าเพิ่มเติม / ต้นทุนนำเข้า. |
| 12 Must not copy | Benchmark restriction set as a design rule; account-field vocabulary. |

---

## 4. Product Category Valuation Policy — หมวดหมู่สินค้าและนโยบายต้นทุน (MENU-CF-09)

Layer 1 learning (CORR-007B file `09`, rewritten): Product Category can own valuation timing and costing method with a company default fallback. Four candidate policy owners for SMEsPlus (company / category / product / native policy object); six inheritance questions (override rules, multi-company behaviour, category change, historical valuation on policy change); a six-row timing × method matrix that Team B must complete. Only 3 of 3,980 real categories in the studied dataset carried an override (reopen `12`), so most tenants effectively use a company default — a usability fact for Thai SMEs.

Classification: `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` (both Track 05 and Track 09 recommend one joint Category design pass; dual ownership with putaway/routing is a design smell — reopen `07_IESA`, `14`).

---

## 5. Accounting Handoff Matrix (Inventory → Accounting facts)

| Event | Inventory fact emitted | Accounting decision | CP-07 classification | Standing evidence |
|---|---|---|---|---|
| Receipt validated | qty, cost basis ref, date, product, category, location | Post to inventory asset / clearing per timing policy | `ACCOUNTING_INTERFACE_REQUIREMENT` | Reopen `02` item 12 |
| Vendor bill posted after receipt | (Accounting event) price difference vs receipt cost basis | Price variance handling; late bill in closed period rule (`FIN-DELTA-04`) | `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` | Reopen `08` |
| Delivery validated | qty, cost per method, date | COGS timing (delivery vs invoice) — `FIN-DELTA-03` | `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` | Reopen `08` |
| Customer return | qty, cost basis (original vs recomputed — `C-03`) | Reverse COGS | `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` | Reopen `13` C-03 |
| Vendor return | qty, original receipt cost | Reverse receipt / credit note link | `ACCOUNTING_INTERFACE_REQUIREMENT` | — |
| Adjustment applied | delta qty, cost, reason | Inventory gain/loss account; period | `ACCOUNTING_INTERFACE_REQUIREMENT` | Reopen `02` item 19 |
| Scrap validated | qty, cost, reason, lot | Loss account; tax-deductibility evidence (`GAP-MD-04`) | `ACCOUNTING_INTERFACE_REQUIREMENT` + `PENDING_ACCOUNT_SESSION` (statutory) | — |
| Landed cost validated | allocation per receipt line | Posting; method eligibility | `ACCOUNTING_INTERFACE_REQUIREMENT` + Joint | Reopen `08` `FIN-DELTA-02` |
| Internal transfer | none (same company) | none | `INVENTORY_OWNED_STOCK_FACT` | Reopen `02` item 14 |
| Inter-company transfer | sale/purchase pair facts | Inter-company invoicing | `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` | Reopen `02` item 33 |
| Manufacturing consumption / output | component cost out, finished cost in; WIP timing | WIP account; close automation (`FIN-DELTA-01`) | `ACCOUNTING_INTERFACE_REQUIREMENT` + Joint | Reopen `02` item 29 |
| Period close | closing qty/value per product; reconciliation to GL | Closing entry; lock date sequencing (`G-1`); retained earnings (`G-6`) | `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` | CORR-007B; Reopen `20` |
| Migration cutover | certified opening qty/value (`G-5`) | Opening trial balance cross-proof | `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` | Reopen `11`, `13` U-04 |
| Posting architecture | (design) direct journal write vs neutral event emission | Accounting-owned posting service | `PENDING_ACCOUNT_INVENTORY_JOINT_SESSION` | Reopen `07` `INV-FP-09` |
| Thai costing norm (which methods, presentation) | — | `TH-INV-03` | `PENDING_ACCOUNT_SESSION` (`COA-G06`) | Reopen `14`, `20` |
| Thai WHT on services vs goods | product kind fact | `GRPA-M18-D`, WHT design | `PENDING_ACCOUNT_SESSION` | Reopen `12` §8 |

---

## 6. What This Session Did Not Close (explicit)

- COA / account mapping for stock, variance, COGS, loss.
- Journal entry design and posting-architecture fork.
- Valuation timing/method policy owner.
- Period close sequencing, lock-date exception model, retained earnings entry.
- Return cost basis conflict (`C-03`).
- Thai statutory treatment of scrap destruction, import duty/VAT, costing method presentation.
- `C-05` independent clean-room re-audit (not performed; remains Boss-visible control).

---

## 7. Gaps Carried

| Gap ID | Item | Owner | Gate impact |
|---|---|---|---|
| GAP-MD-05 | Landed-cost allocation mechanism completeness (periodic/standard path) | Track 06 / S6 | Team B precondition (conditional feature) |
| GAP-MD-13 | Valuation policy owner and Category redesign; `N-A12-01` closure | Joint Session; Boss | **Blocks Joint Backbone publication** |
| GAP-MD-24 | Import duty / VAT cost treatment for Thai importers (statutory) | Accounting-Tax track | `HOLD / EVIDENCE REQUIRED` |
| C-03 | Return cost basis | Track 01 / Boss | Bounded verification |
| C-05 | Independent clean-room re-audit of CORR-007B 08/09 | Boss / Track 08 | Precondition for any Team B reliance |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
