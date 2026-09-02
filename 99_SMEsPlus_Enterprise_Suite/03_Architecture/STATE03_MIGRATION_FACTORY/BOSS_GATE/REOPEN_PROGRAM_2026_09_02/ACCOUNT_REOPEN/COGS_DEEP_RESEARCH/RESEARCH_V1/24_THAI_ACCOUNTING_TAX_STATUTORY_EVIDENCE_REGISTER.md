# 24 — Thai Accounting, Tax and Statutory Evidence Register

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `EVIDENCE-ONLY — LAYER B THAI ACCOUNTING/TAX/AUDIT PASS — NO DESIGN DECISION, NO PASS/FINAL/APPROVED CLAIMED`

---

## 0. Purpose, Method and Discipline Statement

This file is the Accounting-Tax track evidence pass required by governing prompt §13. It is `Layer B — Thai Accounting / Tax / Statutory / Audit Evidence` only (per prompt §3). It does not merge with `Layer A` (OpenSource reference ERP observation, covered elsewhere in this package) or `Layer C` (SMEsPlus clean-room candidate semantics). No SMEsPlus design decision is made or implied here.

Research method: live web search and direct fetch of primary Thai government/standard-setter sources where reachable, including binary PDF extraction via the Read tool where WebFetch could not parse compressed PDF streams. Every claim below is classified exactly one of:

- `AUTHORITATIVE / VERIFIED` — read directly from, or directly quoted/paraphrased from, primary statutory or standard-setter text (Revenue Code, Revenue Department Order/Notification/Practice-Guideline text, or a Federation of Accounting Professions (TFAC/FAP) standard or official explanatory manual).
- `INTERPRETATION — REVIEW REQUIRED` — found in credible secondary commentary (audit/tax-advisory firm publication, tax-summary aggregator, professional secondary source) but not independently verified against primary text in this pass.
- `NOT FOUND / HOLD` — no authoritative or credible secondary evidence located in this pass.

No secondary-source finding is upgraded to `AUTHORITATIVE` in this file. No citation is invented. Where a primary PDF could be opened and read, its exact clause/section number is quoted; where a primary PDF could not be parsed even after direct download, this is stated explicitly rather than silently substituting a secondary source.

---

## 1. Clean-Room Reconciliation With the Nine Existing TH-HOLD Items

Source of the nine existing items: `INVENTORY_FINAL_SOLUTION_V1_2026_09_02_EXECUTION` → `.../FINAL_SOLUTION/INVENTORY/V1_0/07_INVENTORY_ACCOUNTING_CONTROL_IMPACT_V1.md`, §6 (read in full before this pass). This file explicitly reconciles against those nine IDs and invents no parallel numbering. Per governing prompt §13, this session advances `TH-HOLD-02`, `TH-HOLD-03`, `TH-HOLD-05`, `TH-HOLD-07` specifically; the other five are carried forward unchanged (out of this session's assigned scope) with a one-line status note only.

| ID | Original statement (verbatim from source file) | This session's disposition |
|---|---|---|
| `TH-HOLD-01` | The required format, columns and title of a Thai statutory stock report, and whether the stock card design satisfies it. | Carried forward unchanged — `HOLD / EVIDENCE REQUIRED`. Not in this session's advance list. Adjacent evidence found (VAT Section 87 stock-report duty, Revenue Department Notification on VAT No. 104 form reference) is logged in §2.7 below as context only, not as closure. |
| `TH-HOLD-02` | The procedure and evidence Thai authorities require before scrapped or destroyed stock is deductible. | **Advanced this session** — see §2.5. Primary-source procedure located and summarized. Remains `HOLD` only on quantitative/threshold sub-questions; see new item `TH-HOLD-COGS-01`. |
| `TH-HOLD-03` | The treatment of import duty and import VAT in landed cost, including whether recoverable input VAT must be excluded. | **Advanced this session** — see §2.6. Primary accounting-standard text located (cost composition clause excludes recoverable tax). Tax-side VAT-recovery mechanics remain `INTERPRETATION — REVIEW REQUIRED`. |
| `TH-HOLD-04` | Whether and how product kind (goods versus service) correlates with withholding-tax applicability. | Carried forward unchanged — `HOLD / EVIDENCE REQUIRED`. Not in this session's advance list; not researched in this pass. |
| `TH-HOLD-05` | Accepted Thai costing norms and whether a chosen costing method is constrained by them. | **Advanced this session** — see §2.2 and §2.9. Primary statutory text (Revenue Code) and primary standard-setter text (TAS 2) both located and materially advance this item. |
| `TH-HOLD-06` | Whether a warehouse must correspond to a registered tax branch, and the consequence of divergence. | Carried forward unchanged — `HOLD / EVIDENCE REQUIRED`. Not in this session's advance list; not researched in this pass. |
| `TH-HOLD-07` | Requirements for a witnessed annual physical count and its documentation. | **Advanced this session** — see §2.8. Auditor-side evidence (TSA 501) and destruction-witness evidence (Order Por.79/2541) both located, but a distinct statutory "witnessed annual physical count" mandate independent of those two contexts was **not** located. Remains partially `HOLD`; reasons stated in §2.8. |
| `TH-HOLD-08` | Sector-specific traceability obligations for food, pharmaceutical and cosmetic goods. | Carried forward unchanged — `HOLD / EVIDENCE REQUIRED`, routed onward to legal per the source file. Not researched in this pass. |
| `TH-HOLD-09` | The link between a delivery document and a tax invoice, and any required document numbering conventions. | Carried forward unchanged — `HOLD / EVIDENCE REQUIRED`. Not in this session's advance list; not researched in this pass. |

---

## 2. Topic-by-Topic Evidence (Governing Prompt §13)

### 2.1 Inventory Cost Composition

**Question:** What does the applicable Thai standard say inventory cost is composed of?

**What was found:** The Federation of Accounting Professions (สภาวิชาชีพบัญชี ในพระบรมราชูปถัมภ์ — TFAC) publishes an official explanatory manual for Thai Accounting Standard No. 2, Inventories ("คู่มืออธิบายมาตรฐานการบัญชี ฉบับที่ 2 เรื่อง สินค้าคงเหลือ", issued 15 May 2020/2563, reflecting TAS 2 revised 2562/2019, itself adapted from IAS 2). Retrieved directly (PDF opened and read page-by-page): the manual states inventory cost ("ต้นทุนของสินค้าคงเหลือ") comprises three elements:

1. **Costs of purchase** ("ต้นทุนในการซื้อ") — purchase price, import duties ("อากรขาเข้า"), other taxes net of amounts the entity will subsequently recover from the taxing authority ("ภาษีอื่น ๆ สุทธิจากจำนวนที่กิจการจะได้รับคืนภายหลังจากหน่วยงานที่มีหน้าที่จัดเก็บภาษี"), transport, handling and other costs directly attributable to the acquisition of finished goods, materials and services — less trade discounts, rebates and similar items.
2. **Costs of conversion** ("ต้นทุนแปลงสภาพ") — direct labor, plus systematically allocated fixed and variable production overheads.
3. **Other costs** ("ต้นทุนอื่น ๆ") — only to the extent incurred in bringing the inventories to their present location and condition.

The manual explicitly lists costs **excluded** from inventory cost and recognized as period expense instead: abnormal amounts of wasted materials, labor or other production costs; storage costs unless necessary in the production process before a further production stage; administrative overheads not contributing to bringing inventories to their present location/condition; and selling costs.

**Source:** Federation of Accounting Professions Thailand (สภาวิชาชีพบัญชี) — คู่มืออธิบายมาตรฐานการบัญชี ฉบับที่ 2 เรื่อง สินค้าคงเหลือ (TAS 2 Explanatory Manual, revised 2562), pp. 3–5, retrieved 2026-09-02 from `acpro-std.tfac.or.th/uploads/files/TAS2-Manual.pdf`.

**Classification:** `AUTHORITATIVE / VERIFIED` (primary standard-setter explanatory text, directly read).

---

### 2.2 Acceptable Cost-Flow Assumptions / Costing Methods

**Question:** What costing methods (cost formulas) are acceptable under the applicable Thai accounting standard, and separately, what does the Revenue Department accept for tax purposes?

**What was found — accounting-standard side:** The same TAS 2 Explanatory Manual states an entity must use the same cost formula for all inventories of similar nature and use, and lists the permitted cost formulas: **specific identification** ("วิธีราคาเจาะจง"), **first-in, first-out / FIFO** ("วิธีเข้าก่อนออกก่อน"), and **weighted average cost** ("วิธีต้นทุนถัวเฉลี่ยถ่วงน้ำหนัก"), with full worked numeric examples for each (Examples 1–4, pp. 5–7). Last-in-first-out (LIFO) is not listed as a permitted formula — consistent with secondary commentary that IAS 2's 2003 revision (carried into TAS 2) removed LIFO as an allowed cost formula. The manual separately lists **costing techniques** used for measurement convenience — the **standard cost method** and the **retail method** — which are distinct from cost formulas and must approximate actual cost. A change from one cost formula to another (e.g., FIFO to weighted average) is explicitly stated to fall under **TAS 8** (Accounting Policies, Changes in Accounting Estimates and Errors) as a change in accounting policy.

**What was found — tax side:** Section 65 bis (6) of the Revenue Code (ประมวลรัษฎากร มาตรา 65 ทวิ (6)) was retrieved directly as a Revenue Department internal-control-register PDF (`rd.go.th/fileadmin/images/image_pramoun/mata65_2.pdf`) and reads, in the operative clause: closing inventory value on the last day of an accounting period must be computed at cost or market price, whichever is lower ("ราคาสินค้าคงเหลือในวันสุดท้ายของรอบระยะเวลาบัญชี ให้คำนวณตามราคาทุนหรือราคาตลาด แล้วแต่อย่างใดจะน้อยกว่า"), and this becomes the opening value carried forward to the next period. The same clause requires that once a method is chosen under accounting principles, it must be used consistently thereafter unless a change is approved by the Director-General of the Revenue Department ("เมื่อได้คำนวณตามหลักเกณฑ์ใดตามวิชาการบัญชี ให้ใช้หลักเกณฑ์นั้นตลอดไป เว้นแต่จะได้รับอนุมัติจากอธิบดีจึงจะเปลี่ยนหลักเกณฑ์ได้"). A separate Revenue Department taxpayer-education slide deck (`rd.go.th/fileadmin/user_upload/spreadsheet/inventory_270160.pdf`, also opened and read directly) confirms, for the purpose of the PND.50 corporate return, that the accepted cost-basis methods for computing closing-inventory tax value are the same three: FIFO ("First in First out"), Specific Identification, and Weighted Average — presented alongside the mandatory cost-or-market comparison per item/category.

**Source:** Federation of Accounting Professions Thailand — TAS 2 Explanatory Manual (as §2.1), pp. 5–7, retrieved 2026-09-02; Revenue Department (กรมสรรพากร) — Revenue Code Section 65 bis (6) internal control register, retrieved 2026-09-02 from `rd.go.th/fileadmin/images/image_pramoun/mata65_2.pdf`; Revenue Department — taxpayer-education slide deck on closing-inventory valuation for PND.50 filing, retrieved 2026-09-02 from `rd.go.th/fileadmin/user_upload/spreadsheet/inventory_270160.pdf`.

**Classification:** `AUTHORITATIVE / VERIFIED` on both the accounting-standard side and the tax side (both primary texts directly read, not secondary summary). This materially advances `TH-HOLD-05`. What remains open is stated in new item `TH-HOLD-COGS-03` (§4).

---

### 2.3 Lower-of-Cost-or-Net-Realisable-Value / Write-Down and Reversal

**Question:** How does the applicable Thai standard require measurement at the lower of cost and net realisable value (NRV), and how must write-down and reversal be treated?

**What was found:** TAS 2 defines net realisable value ("มูลค่าสุทธิที่จะได้รับ") as the estimated selling price in the ordinary course of business less the estimated costs of completion and the estimated costs necessary to make the sale — explicitly distinguished from "fair value" (which reflects a market-participant exit price, per TFRS 13 equivalent). Inventories must be measured at the lower of cost and NRV. The manual states write-down (and any loss) is normally assessed **item by item**, except where items with similar characteristics and use may reasonably be grouped (e.g., items relating to the same product line, produced/marketed in the same geographic area, that cannot practicably be evaluated separately). It explicitly states it is **not appropriate** to write down inventories on the basis of a broad classification, e.g. all finished goods, or all inventories in a particular operating segment. The manual walks through full worked examples (Examples 6.1–6.2, 7.1–7.4, 8.1–8.4, pp. 9–14) including a group-comparison example (write down by item = 1,475; write down by grouped total = 1,485 — different results, illustrating why item-level testing is required) and financial-statement note disclosure examples (a real company's cost/write-down/net table for finished goods, WIP, raw materials, and consumables, across two comparative years).

On reversal, TAS 2 requires a new NRV estimate in each subsequent period; when the circumstances that previously caused a write-down no longer exist, or there is clear evidence of increased NRV due to changed economic circumstances, the amount of the write-down is reversed — but the reversal is capped so the new carrying amount does not exceed the original cost. The manual's worked Example 8.3 shows an entity reversing a prior 300,000-baht write-down in a later period because raw-material scarcity that had depressed NRV resolved.

**Source:** Federation of Accounting Professions Thailand — TAS 2 Explanatory Manual, pp. 8–10 and pp. 13–14, retrieved 2026-09-02.

**Classification:** `AUTHORITATIVE / VERIFIED` (primary standard-setter explanatory text with reproduced worked examples, directly read).

---

### 2.4 Recognition of Inventory Carrying Amount as Expense/COGS When Related Revenue Is Recognized

**Question:** What does the applicable Thai standard state about the core COGS-matching principle — when inventory carrying amount becomes an expense?

**What was found:** The TAS 2 Explanatory Manual contains a dedicated section headed "การรับรู้เป็นค่าใช้จ่าย" (Recognition as an Expense) that states, in substance and close paraphrase of the primary text:

- When inventory is sold, its carrying amount must be recognized as cost of sales in the period in which the related revenue is recognized.
- The amount of any write-down of inventories to NRV, and all losses of inventories, must be recognized as an expense (as part of cost of sales) in the period the write-down or loss occurs.
- The amount of any reversal of a write-down arising from an increase in NRV must be recognized as a reduction in the amount of inventories recognized as an expense (cost of sales) in the period in which the reversal occurs.
- Some inventories may be allocated to other asset accounts (e.g., inventory used as a component of self-constructed property, plant or equipment); such inventory is recognized as an expense over the useful life of that related asset, not at the point of transfer out of inventory.

This is the literal Thai-standard statement of the "not every inventory-value decrease is COGS" principle the governing prompt (§2, §17 Teach-Back Q4) requires this session to prove with evidence — the standard itself draws the same distinction: ordinary cost-of-sales recognition on sale, write-down/loss recognition in the period incurred, reversal as a COGS reduction, and re-allocation to another asset class as depreciation/amortization over that asset's life, are four textually distinct recognition events, not one undifferentiated "inventory decrease".

**Source:** Federation of Accounting Professions Thailand — TAS 2 Explanatory Manual, p. 12 ("การรับรู้เป็นค่าใช้จ่าย" section), retrieved 2026-09-02.

**Classification:** `AUTHORITATIVE / VERIFIED` (primary standard-setter explanatory text, directly read; this is the closest citable statement to the exact TAS 2 recognition paragraph reachable in this pass — see caveat below).

**Caveat (recorded honestly, not smoothed over):** This pass read the TFAC **explanatory manual** for TAS 2, which the manual's own header states "is not part of the financial reporting standards" ("คู่มืออธิบายมาตรฐานการบัญชีนี้ ไม่ถือเป็นส่วนหนึ่งของมาตรฐานการรายงานทางการเงิน"). Two attempts to open the **operative gazetted TAS 2 standard text itself** (`eservice.tfac.or.th/get_file/index.php?file=TAS_2_revised_2568.pdf`) were made; the file downloaded successfully but could not be extracted as readable text in the time available to this pass (WebFetch returned only PDF structural metadata; a follow-up page-range Read of the saved binary was not completed before this file was written). This file therefore classifies the manual's content as `AUTHORITATIVE` because TFAC is the standard-setter and the manual is its own official explanatory publication of TAS 2 — but a reviewer who needs the exact numbered paragraph of the gazetted standard (rather than TFAC's own explanatory restatement of it) should treat that specific gap as open and re-attempt extraction of the gazetted PDF.

---

### 2.5 Abnormal Loss / Scrap / Destroyed Inventory Treatment (advances `TH-HOLD-02`)

**Question:** What procedure and evidence does Thailand require before scrapped, destroyed, or disposed inventory is tax-deductible?

**What was found:** Revenue Department Order No. Por. 79/2541 (คำสั่งกรมสรรพากร ที่ ป.79/2541), dated 3 November 1998 (B.E. 2541), titled "แนวทางปฏิบัติกรณีการทำลายของเสีย สินค้าที่เสื่อมคุณภาพ สินค้าที่มีตำหนิ สินค้าที่หมดสมัยนิยม สินค้าที่หมดอายุ และเศษซาก" (Practice guideline for the case of destroying waste, deteriorated-quality goods, defective goods, out-of-fashion goods, expired goods, and scrap). This is the standing Revenue Department practice guideline binding Revenue Department officers on how corporate income tax and VAT are handled for destroyed inventory. Content located (via direct fetch of the Revenue Department's own published order page, `rd.go.th/3575.html`):

- **Article 2 (normal waste):** Waste within normal/expected process tolerances is absorbed into the cost of the good units produced — no separate deduction or write-off entry is made for it; it is not treated as a discrete tax event.
- **Article 3 (abnormal waste / damaged / obsolete / expired / scrap):** Deductible as a separate expense **only if** proper destruction procedure and documentation are followed and auditor certification is obtained. The required procedure includes: prior management verification that goods meet the applicable damage/obsolescence criteria; for returned goods, retained records of date, quantity, item code, return reason, and signatures of customer and receiving staff; warehouse-staff count and sign-off of items pending destruction, with notice to accounting; and, at the destruction event itself, **witnesses from at least the warehouse, accounting, sales, or internal-audit functions**, who sign as observers (Article 3(3.1)(b) per the order's own numbering as summarized in the retrieved text). An external auditor must be **invited** to witness (mandatory invitation, not mandatory attendance) — where the auditor does not attend, the company may instead provide a written destruction report to the auditor for the auditor's own written certification, to be attached to the financial statements. For perishable goods (food, medicine, chemicals) a Revenue Department officer's attendance is **not required**. For non-perishable/storable goods, a 30-day advance notice to the Revenue Department is required, and the Department may (at its discretion) send an officer to observe.
- **VAT treatment:** where the Article 3(3.2) destruction procedure is properly followed, the company does not owe output VAT on the value of the destroyed raw materials or goods (this specific VAT-waiver point is corroborated by a separate secondary summary of the same order, see below).

A related but distinguishable Revenue Department position (secondary source, PKF Thailand) addresses **selling** (rather than destroying) obsolete/damaged/near-expiry/substandard inventory below market price: no prior Revenue Department approval is required to do so, but the Department retains authority under **Section 65 bis (4)** of the Revenue Code to reassess a sale price that does not reflect a reasonable/market-based value; PKF cites Revenue Department Ruling No. กค.0702/10199 (11 November 2015) as the relevant precedent, and recommends the seller retain inspection reports, internal departmental sign-off (warehouse and accounting as witnesses), and, for promotional/clearance sales, an approved sales plan and post-sale performance review, applied consistently and not selectively to related parties.

**Source:** Revenue Department (กรมสรรพากร) — Order No. Por. 79/2541, "แนวทางปฏิบัติกรณีการทำลายของเสีย สินค้าที่เสื่อมคุณภาพ สินค้าที่มีตำหนิ สินค้าที่หมดสมัยนิยม สินค้าที่หมดอายุ และเศษซาก" (Practice guideline on destruction of waste, deteriorated, defective, out-of-fashion, expired goods and scrap), dated 3 November 1998, retrieved 2026-09-02 from `rd.go.th/3575.html` [`AUTHORITATIVE`]; PKF Thailand — "Tax Implications of Selling Obsolete Goods" (secondary commentary citing Revenue Code s.65 bis(4) and Revenue Department Ruling กค.0702/10199, 11 November 2015), retrieved 2026-09-02 [`INTERPRETATION`].

**Classification:** `AUTHORITATIVE / VERIFIED` for the destruction-procedure/witness/VAT-waiver mechanics of Order Por.79/2541 (fetched directly from the Revenue Department's own order page; content corroborated across two independent search results describing the same order and article numbering). `INTERPRETATION — REVIEW REQUIRED` for the below-market-sale-of-obsolete-goods commentary (PKF Thailand secondary source; the underlying Revenue Department ruling number is cited but the ruling text itself was not independently opened in this pass). This materially advances `TH-HOLD-02`; the residual open sub-question is captured as `TH-HOLD-COGS-01` (§4).

---

### 2.6 Landed Cost / Duty / Recoverable VAT Distinction (advances `TH-HOLD-03`)

**Question:** How should import duty and import VAT be treated in landed cost, and must recoverable input VAT be excluded?

**What was found — accounting-standard side:** As already quoted in §2.1, TAS 2's cost-of-purchase clause explicitly includes import duties in cost, and explicitly nets out from cost "other taxes... net of amounts the entity will subsequently recover from the taxing authority" ("ภาษีอื่น ๆ สุทธิจากจำนวนที่กิจการจะได้รับคืนภายหลังจากหน่วยงานที่มีหน้าที่จัดเก็บภาษี"). Read plainly, this is the general recoverable-tax-exclusion principle that governs how import VAT must be treated when it is recoverable as input VAT: a recoverable tax is not part of inventory cost; a non-recoverable tax (including import duty, which is not a VAT-style recoverable tax) is part of inventory cost.

**What was found — tax-mechanics side:** Thailand applies VAT at a standard rate on imports, assessed on CIF value plus customs duty (and, where applicable, excise and interior tax) as the VAT base. A VAT-registered importer can generally reclaim import VAT as input tax against output VAT, making the VAT itself cost-neutral to the business in ordinary circumstances; import duty itself is not a VAT-recoverable item and is a real landed-cost component. Where BOI (Board of Investment) privileges apply, duty may be reduced or exempted, but import VAT is frequently still payable and then still generally recoverable as input tax subject to the importer's VAT-registered status and the HS code/privilege specifics.

**Source:** Federation of Accounting Professions Thailand — TAS 2 Explanatory Manual, p. 3, cost-of-purchase clause, retrieved 2026-09-02 [`AUTHORITATIVE`, accounting-standard side]; secondary logistics/tax-advisory aggregation (Revenue Department VAT overview at `rd.go.th/english/6043.html`, plus commercial import-duty/landed-cost explainer sources) on the CIF-basis VAT calculation and general input-VAT recoverability mechanics, retrieved 2026-09-02 [`INTERPRETATION`, tax-mechanics side — the general mechanics were not verified against a single consolidated Revenue Department primary text in this pass, though the underlying VAT-input-credit mechanism itself is a widely-documented feature of the VAT Chapter of the Revenue Code, not a novel claim].

**Classification:** `AUTHORITATIVE / VERIFIED` for the accounting-standard principle (recoverable tax excluded from cost; import duty included in cost) — this is the core answer to the "must recoverable input VAT be excluded" question, and it is unambiguous. `INTERPRETATION — REVIEW REQUIRED` for the surrounding VAT-recovery tax mechanics (CIF basis, BOI interaction). This materially advances `TH-HOLD-03`; the residual company-structure question (how landed cost interacts with the entity's own VAT-registration status and any partial-exemption position) is out of scope for this pass and not claimed answered.

---

### 2.7 Period Cut-Off and Physical Stock Evidence — Statutory Report Side (context for `TH-HOLD-01`, not advanced this session)

**What was found (context only, not this session's advance target):** Section 87 of the Revenue Code requires a VAT-registered operator selling goods to maintain a stock/raw-material report ("รายงานสินค้าคงเหลือและวัตถุดิบ"), in a form prescribed by the Revenue Department's Director-General Notification on VAT (No. 104) per secondary summary. Section 87/3 requires registrants to retain tax invoices and supporting documents used to record the input-tax report under s.87(2). Neither the exact statutory form/column layout nor its reconciliation against any SMEsPlus stock-card design was independently verified in this pass; `TH-HOLD-01` is not advanced by this file and remains as originally stated.

**Source:** secondary search-result synthesis referencing Revenue Code ss.87 and 87/3 and Director-General Notification on VAT (No. 104), retrieved 2026-09-02; primary text of ss.87/87/3 and Notification No. 104 not independently opened in this pass.

**Classification:** `NOT FOUND / HOLD` for this pass's purposes (secondary synthesis only, no primary text opened; recorded as context, not as evidence advancing any item).

---

### 2.8 Period Cut-Off and Physical Stock Evidence — Witnessed Annual Count (advances `TH-HOLD-07`)

**Question:** What are the requirements for a witnessed annual physical inventory count and its documentation?

**What was found:** Two distinct, non-overlapping authoritative fragments were located, but no single statutory provision mandating a generic "witnessed annual physical inventory count" independent of those two contexts was found:

1. **Audit-side requirement.** Thai Standard on Auditing 501 (TSA 501, Audit Evidence — Specific Considerations for Selected Items), issued by TFAC, requires the external auditor to attend the observation of the entity's physical inventory count (where inventory is material), to evaluate management's count instructions and procedures, observe the performance of count procedures, inspect the inventory, and perform test counts — except where attendance is impracticable, in which case alternative audit procedures are required. This is an **auditor's** procedural obligation on companies subject to statutory audit (which, per the existing Account-module evidence base, is essentially all Thai limited companies), not a standalone requirement addressed to the company that a count occur on a specific cadence independent of the audit cycle.
2. **Destruction-event witness requirement.** As already found in §2.5, Order Por.79/2541 requires witnesses (warehouse/accounting/sales/audit staff, plus an invited external auditor) specifically at the point of **destroying** damaged/obsolete/expired/scrap goods — not at a general annual stock count of good inventory.

No primary source was located in this pass stating a general Thai statutory requirement that **all** companies conduct a witnessed physical count of good (non-destroyed) inventory on an annual cadence, as a standalone obligation separate from (a) what their auditor requires them to do to obtain an unqualified opinion, and (b) what Section 65 bis (6) implicitly requires as the factual basis for the year-end cost/market comparison (a company cannot apply the cost-or-market rule to a "closing inventory" figure it has not actually counted, but this pass found no provision that spells out count *cadence*, *witness composition*, or *documentation format* as a distinct tax rule).

**Source:** Federation of Accounting Professions Thailand — Thai Standard on Auditing 501, summarized via secondary search synthesis referencing the TFAC-published TSA 501 text, retrieved 2026-09-02 [`INTERPRETATION` — the operative TSA 501 text itself was not independently opened in this pass, only search-engine synthesis of it]; Revenue Department Order Por.79/2541 (as §2.5) [`AUTHORITATIVE` for the destruction-specific witness point only].

**Classification:** `INTERPRETATION — REVIEW REQUIRED` for the audit-observation obligation (TSA 501 text not independently opened); `AUTHORITATIVE / VERIFIED` but narrowly scoped for the destruction-event witness point (does not generalize to ordinary annual counts). The general "witnessed annual physical count" question as originally framed in `TH-HOLD-07` **remains substantially `HOLD`** — this pass narrows the question (there appear to be two distinct witness regimes, not one general one) but does not close it. This is recorded honestly as a partial advance, not a resolution.

---

### 2.9 Tax Inventory Valuation Requirements and Consistency / Change-of-Method Rules (advances `TH-HOLD-05`, second component)

**Question:** What does the Revenue Department require for consistency of costing method, and what is the procedure to change it?

**What was found:** Beyond the cost-or-market rule and consistency requirement already quoted in §2.2 from Revenue Code Section 65 bis (6), the same primary Revenue Department internal-control-register PDF documents the **procedure** for a taxpayer to request a change of inventory-costing method: Revenue Department Practice Guideline No. Mor Kor 4/2546 (แนวทางปฏิบัติกรมสรรพากร ที่ มก.4/2546), dated 1 July 2003 (B.E. 2546), governs requests to change (a) the method/rate for computing depreciation, and separately (b) the method for computing inventory cost, and (c) requests to change the accounting-period year-end date. For an inventory-costing-method change specifically:

- **Requesting party:** the corporate income taxpayer wishing to change its inventory cost-computation method.
- **Approving authority:** the Director-General, delegated to the Area Revenue Office / relevant specialist unit / Regional Revenue Office Director per Revenue Department Order No. Tor.228/2552 (ท.228/2552), dated 20 April 2009 (B.E. 2552).
- **Required documents:** a written request letter; a justification memorandum identifying both the accounting principle currently in use and the one requested; and evidence of board-of-directors or managing-partner approval (meeting minutes or equivalent).
- **Stated legislative rationale (per the register's own analysis column):** the requirement exists so that a company/partnership can adapt its inventory-cost computation to suit its actual business circumstances, while preventing tax-planning abuse; it is characterized in the register as a necessary and proportionate administrative condition, not an undue burden.

**Source:** Revenue Department (กรมสรรพากร) — Revenue Code Section 65 bis (6) internal control register (10. มาตรา 65 ทวิ (6) แห่งประมวลรัษฎากร), citing Revenue Department Practice Guideline Mor Kor 4/2546 (1 July 2003) and Revenue Department Order Tor.228/2552 (20 April 2009), retrieved 2026-09-02 from `rd.go.th/fileadmin/images/image_pramoun/mata65_2.pdf`.

**Classification:** `AUTHORITATIVE / VERIFIED` (primary Revenue Department register text, directly read, naming the specific practice guideline and delegation order by number and date).

---

### 2.10 Financial-Statement Presentation of Inventory / COGS / Gross Profit

**Question:** What does Thai law/standard-setter guidance require for the presentation of Inventory and COGS/gross profit in the financial statements?

**What was found:** The Department of Business Development (DBD), Ministry of Commerce, issues the governing notification "ประกาศกรมพัฒนาธุรกิจการค้า เรื่อง กำหนดรายการย่อที่ต้องมีในงบการเงิน" (Notification specifying the line items required in financial statements) — this is the statutory anchor already identified and Boss-designated as the primary presentation-format source in this program's Account-module track (`COA_G01_THAI_FINANCIAL_STATEMENT_PRESENTATION_SOURCE_R4.md`, §"Boss N-04 route decision"). Search-result synthesis of that DBD notification's income-statement format (this pass did **not** succeed in extracting readable text directly from the DBD PDF itself — both `dbd.go.th/storage/law/0fafe207-f3e1-4173-bca7-47c32219a932.pdf` fetch attempts returned only PDF structural metadata) indicates the required income-statement sequence includes, in order: (1) revenue from sale of goods or rendering of services, and cost of sales or cost of services, presented together; (2) gross profit (loss); (3) other income; (4) selling expenses, administrative expenses, and other expenses. If accurate, this confirms Thai statutory presentation requires COGS to be shown as a distinct deduction from sales revenue to arrive at a labeled gross-profit line — consistent with, and not contradicted by, the TAS 2 recognition principle in §2.4 (cost of sales recognized in the period revenue is recognized).

**This finding must be read together with the existing, unresolved Account-module blocker:** `COA_G01_THAI_FINANCIAL_STATEMENT_PRESENTATION_SOURCE_R4.md` records that the Boss-provided controlled example file (`งบการเงิน 2567.pdf`) could not be opened by that session (`ACCESS_DENIED`, Google Drive file-ID lookup failure), that Source Class F remains `EVIDENCE_MISSING`, and that decision item `N-04` remains `OPEN`. **This file's DBD finding does not close `N-04`** — it is independent secondary synthesis of the same statutory anchor the Account-module track already designated, not a substitute for either the operative DBD notification text or the Boss-provided controlled example. Both remain to be independently opened.

**Source:** Department of Business Development (DBD), Ministry of Commerce — "ประกาศกรมพัฒนาธุรกิจการค้า เรื่อง กำหนดรายการย่อที่ต้องมีในงบการเงิน" (Notification on required financial-statement line items), located at `dbd.go.th/storage/law/0fafe207-f3e1-4173-bca7-47c32219a932.pdf`, content reconstructed from search-engine synthesis rather than direct text extraction, retrieved 2026-09-02.

**Classification:** `INTERPRETATION — REVIEW REQUIRED` (the notification's existence, title, and administering body are confirmed and are consistent across multiple independent search results, but the exact line-item sequence quoted above was not independently verified against directly-extracted primary text in this pass, and must not be treated as `AUTHORITATIVE` until the raw DBD PDF or the Boss-provided controlled example is successfully opened).

---

## 3. Summary Classification Table

| # | Topic | Classification | Advances |
|---|---|---|---|
| 2.1 | Inventory cost composition | `AUTHORITATIVE / VERIFIED` | new evidence base |
| 2.2 | Acceptable costing methods (standard + tax) | `AUTHORITATIVE / VERIFIED` | `TH-HOLD-05` |
| 2.3 | Lower-of-cost-or-NRV, write-down, reversal | `AUTHORITATIVE / VERIFIED` | new evidence base |
| 2.4 | Recognition of carrying amount as COGS | `AUTHORITATIVE / VERIFIED` (with stated manual-vs-gazetted-text caveat) | new evidence base |
| 2.5 | Scrap/destroyed inventory procedure | `AUTHORITATIVE / VERIFIED` (procedure) / `INTERPRETATION` (below-market sale) | `TH-HOLD-02` |
| 2.6 | Landed cost / duty / recoverable VAT | `AUTHORITATIVE / VERIFIED` (accounting principle) / `INTERPRETATION` (VAT mechanics) | `TH-HOLD-03` |
| 2.7 | Statutory stock report (context only) | `NOT FOUND / HOLD` | context for `TH-HOLD-01` (not advanced) |
| 2.8 | Witnessed physical count | `INTERPRETATION` (audit) / `AUTHORITATIVE` narrow (destruction only) | `TH-HOLD-07` (partial) |
| 2.9 | Consistency / change-of-method procedure | `AUTHORITATIVE / VERIFIED` | `TH-HOLD-05` |
| 2.10 | Financial-statement presentation | `INTERPRETATION — REVIEW REQUIRED` | context only — does not close `N-04` |

Tally: **6 `AUTHORITATIVE / VERIFIED`** topic-level findings (2.1, 2.2, 2.3, 2.4, and the procedural cores of 2.5/2.6/2.9 — counted once each at topic level with sub-classifications noted inline), **4 `INTERPRETATION — REVIEW REQUIRED`** components (below-market-sale commentary in 2.5, VAT mechanics in 2.6, audit-observation text in 2.8, DBD presentation sequence in 2.10), **1 explicit `NOT FOUND / HOLD`** (2.7, logged as context, not claimed as an advance).

---

## 4. New COGS-Specific Thai-Hold Items (`TH-HOLD-COGS-*`)

Numbered separately from the original nine per governing-prompt instruction, so no collision occurs. Each is a genuine unresolved question this pass's research surfaced; none is a restatement of an already-open item.

### `TH-HOLD-COGS-01` — Normal vs. abnormal waste threshold

Order Por.79/2541 draws a hard line between "normal" waste (Article 2: absorbed into the cost of good units, no separate deduction, no destruction-witness procedure required) and "abnormal" waste/damage/obsolescence/expiry/scrap (Article 3: separately deductible only via the witnessed destruction procedure). **No quantitative or qualitative threshold for where "normal" ends and "abnormal" begins was located in this pass.** This is material to SMEsPlus because it determines whether a given inventory write-down or shrinkage event should (a) flow automatically into COGS as part of ordinary cost absorption with no extra evidence workflow, or (b) require a distinct scrap/loss workflow with committee sign-off, evidence attachment, and (for storable-goods cases) advance Revenue Department notice. `HOLD / EVIDENCE REQUIRED`.

### `TH-HOLD-COGS-02` — NRV write-down testing granularity vs. category-level account configuration

TAS 2 (§2.3 above) requires NRV write-down testing at the individual-item level or a narrowly-justified similar-item group, and explicitly forbids testing/write-down at a broad classification level (e.g., "all finished goods"). The governing prompt's Menu B/Menu C research track (elsewhere in this package) investigates Product-Category-level and Product-level accounting configuration, including category-level valuation/write-down account assignment. **Whether a category-level (or account-group-level) posting structure for write-downs can coexist with an item-level NRV testing obligation — i.e., whether the account the write-down posts to may be shared across a category while the underlying test and evidence trail must remain item-level — was not researched in this pass.** `HOLD / EVIDENCE REQUIRED`.

### `TH-HOLD-COGS-03` — Scope of the Section 65 bis (6) consistency rule: entity-wide or configurable per product/category?

Every piece of primary evidence located in this pass (the Revenue Code register, the Mor Kor 4/2546 practice guideline, the Tor.228/2552 delegation order) frames the consistency rule and its change-approval procedure at the level of "the taxpayer" (a single corporate entity), not at the level of an individual product or product category. **Whether Revenue Department practice would treat a change to the costing method configured on one Product Category (while other categories remain unchanged) as a "change of method" triggering the same Director-General approval procedure was not found in this pass — no evidence was located either confirming or excluding category-level granularity from the statutory consistency rule.** This is material because the governing prompt's research scope (§11) requires proving category-vs-product costing-method precedence, and this Thai-hold item flags that whatever precedence model SMEsPlus's clean-room candidate eventually proposes, it must independently confirm whether category-level costing-method configurability is itself compatible with Section 65 bis (6) consistency, not just an internal design question. `HOLD / EVIDENCE REQUIRED`.

### `TH-HOLD-COGS-04` — DBD statutory presentation sequence not independently verified; does not close Account-module N-04

As stated in §2.10, this pass's finding on the DBD income-statement line-item sequence (revenue-and-cost-of-sales together, then gross profit, then other income, then operating expenses) is `INTERPRETATION — REVIEW REQUIRED` only — reconstructed from search-engine synthesis, not from directly-extracted primary DBD text, and separately, the Boss-provided controlled example remains inaccessible per the existing Account-module blocker. **This item exists to make explicit and prevent any future reader from treating this file's §2.10 finding as sufficient to close Account-module decision item `N-04` or to reclassify Source Class F away from `EVIDENCE_MISSING`.** Closing `N-04` requires either successful direct extraction of the DBD PDF or Boss resolution of the Google Drive file-access blocker recorded in `COA_G01_PRIMARY_SOURCE_RECOVERY_REGISTER_R4.md`. `HOLD / EVIDENCE REQUIRED`, explicitly cross-referenced to `N-04`.

---

## 5. What This File Does Not Do

This file does not decide any SMEsPlus costing method, account structure, write-down workflow, or presentation format. It does not close `TH-HOLD-01`, `TH-HOLD-04`, `TH-HOLD-06`, `TH-HOLD-08`, or `TH-HOLD-09` (out of this session's assigned advance list; unchanged). It does not close Account-module `N-04`. It does not assert that any Thai statutory rule is settled SMEsPlus design. It does not declare PASS, FINAL, or APPROVED. Every `AUTHORITATIVE / VERIFIED` classification above is traceable to a specific primary document this pass directly opened and read (either via successful WebFetch of the source page, or via direct PDF binary extraction through the Read tool where WebFetch could not parse the compressed stream); every `INTERPRETATION` classification is traceable to a named secondary source; every `NOT FOUND / HOLD` is stated as such rather than filled with a guess.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
