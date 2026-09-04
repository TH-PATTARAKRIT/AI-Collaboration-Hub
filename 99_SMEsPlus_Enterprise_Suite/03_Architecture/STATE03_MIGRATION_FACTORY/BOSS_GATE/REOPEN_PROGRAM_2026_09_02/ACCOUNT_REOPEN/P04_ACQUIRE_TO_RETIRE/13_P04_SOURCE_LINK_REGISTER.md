# 13 — P04 SOURCE LINK REGISTER

Layer: **2 — audit quarantine**.

Every source relied on, with the pattern and path set that produced it.
Per the clean-room rule, reference-ERP file paths and line ranges are Layer 2
evidence and are cited by **module and behaviour**, not by transcribed code.

---

## 1. Primary source code

| ID | Root | Scope of use |
|----|------|--------------|
| `EV-CODE` | Reference ERP v18 Enterprise source tree, build `20250608` | The asset module (model, accounting-document extension, modify wizard, security, views, tests); the accounting core (posting routine, lock-date handling, analytic-line creation, product account resolution); procurement; inventory and inventory accounting; manufacturing and manufacturing accounting; work-order and work-order-human-resources; project bridges; expense; loans; deferred recognition; reporting |
| `EV-CUST` | Project custom addon set, v18 line | The equipment-sequence module (full import-chain read); the equipment-product-stock module; the advance-expense-request module |
| `EV-LEG` | Legacy v14 source tree | Not read this session. Prior findings imported |

### 1.1 Declared populations, executed this session

| Population | Count | Method |
|------------|-------|--------|
| Entries in the reference addons root | **797** | directory listing |
| Directories in the reference addons root | **791** | type-filtered find |
| **Installable modules** (directories carrying a manifest) | **790** | manifest search |
| Entries in the custom addons root | **68** | directory listing |
| **Directories** in the custom addons root | **65** | type-filtered find |
| Reference modules referencing the asset model in Python | **3** | `grep -rlE "['\"]account\.asset" --include='*.py'` |
| Custom modules referencing the asset model in code or manifest | **2** | `grep -rlI -E "account\.asset|account_asset" --exclude-dir=i18n` (three further hits are documentation files — false positives) |
| Reference modules **instantiating** an asset record | **1** | creation-site sweep |

### 1.2 Declared negative patterns

Each returned **zero hits under the stated path set** and is reported as
*"not found under &lt;path set&gt; using &lt;pattern&gt;"*, never as non-existence.

| Pattern | Path set | Meaning of the negative |
|---------|----------|------------------------|
| `scrap` (case-insensitive) | the asset module | no scrap event |
| `impair` (case-insensitive) | the asset module | no impairment concept |
| `transfer` (case-insensitive) | the asset module | no transfer capability |
| `partial` (as a code path) | the asset module | no partial disposal |
| `ir.cron` | the asset module | no scheduled action of its own |
| `account.asset` | procurement, inventory, inventory-accounting modules | no purchase- or receipt-driven asset creation |
| `asset` (case-insensitive) | manufacturing, manufacturing-accounting, work-order modules | no manufacturing-to-asset route |
| `equipment` | manufacturing and work-order model packages | no operation-to-equipment reference |
| `original_value` \| `capitaliz` | the loans module | no borrowing-cost capitalization |
| `account.asset` \| `account_asset` | reporting modules | no asset-specific close or report-driven recomputation |

## 2. Runtime and project evidence

| ID | Artefact | Date | Bound — stated at every point of use |
|----|----------|------|--------------------------------------|
| `EV-RT` | ORM read-out against the UAT database | 2026-08-26 | The population query was **unbounded** (limit 10 000, returned 280) and is a population statement. The **external-identifier query was restricted to a hand-picked list of 26 identifiers** and is **not** a population statement. The field list is **12 fields** and **omits the source-journal-item link** |
| `EV-HND` | Asset Actual Mapping execution handoff | 2026-08-26 | Project record: 16 controlled models, state counts, traceability rules |

## 3. Prior audited evidence

| ID | Package | Branch | Research commit |
|----|---------|--------|-----------------|
| `EV-P1` | Asset function deep research | `audit/asset-function-deep-research-2026-09-03-001` | `57cdb99` |
| `EV-P2` | Asset deep research L1–L6 (**controlled baseline**) | `research/asset-deep-l1-l6-2026-09-04-001` | `6c7512e` |
| `EV-P3` | Asset DR continuation L7→Final | `research/asset-deep-continuation-2026-09-04-001` | `a852b6e` |

## 4. Statutory and standard-setter sources

### 4.1 Imported from prior packages, not re-retrieved

| ID | Source | Class |
|----|--------|-------|
| `LAW-01` | ประมวลรัษฎากร มาตรา 65 ทวิ (2) | primary statute |
| `LAW-02` | พระราชกฤษฎีกา ฉบับที่ 145 (พ.ศ. 2527) มาตรา 4–5 | primary statute |
| `TAS-02` | มาตรฐานการบัญชี ฉบับที่ 2 *สินค้าคงเหลือ*, ประกาศสภาวิชาชีพบัญชี ที่ 34/2562 — ¶12 and ¶13 | standard text, TFAC |
| `DBD-01` | ประกาศกรมพัฒนาธุรกิจการค้า — รายการย่อที่ต้องมีในงบการเงิน, แบบ 2 | primary regulation |

### 4.2 Retrieved by this session

| ID | Source | Retrieved | Class | Used for |
|----|--------|-----------|-------|----------|
| `P04-LAW-A` | **คู่มืออธิบายมาตรฐานการบัญชี ฉบับที่ 16** เรื่อง ที่ดิน อาคารและอุปกรณ์ — สภาวิชาชีพบัญชี ในพระบรมราชูปถัมภ์, เผยแพร่ **27 กุมภาพันธ์ 2563**. Retrieved as a document and text-extracted locally | this session | **TFAC explanatory manual — states on every page that it is NOT part of the financial reporting standards** | Derecognition criteria; gain/loss determination; forms of disposal; disposal date and control; revaluation surplus to retained earnings; impairment referred to TAS 36; third-party compensation; separate-events rule; depreciation cessation; the fully-depreciated exception; units-of-production zero charge; annual review of life and residual; revenue-based depreciation not appropriate |
| `P04-LAW-B` | **คำสั่งกรมสรรพากร ที่ ป. 79/2541** (3 พฤศจิกายน 2541) — แนวทางปฏิบัติ กรณีการทำลายของเสีย สินค้าที่เสื่อมคุณภาพ สินค้าที่มีตำหนิ สินค้าที่หมดสมัยนิยม สินค้าที่หมดอายุ และเศษซาก | this session | **Revenue Department instruction — primary** | Scope (**goods, inventory, scrap — not fixed assets**); approval; witnesses; auditor as witness and written certification |
| `P04-LAW-C` | **คำสั่งกรมสรรพากร ที่ ป. 84/2542** (13 พฤษภาคม 2542) — same subject; revokes and replaces clause 3.2 of the above | this session | Revenue Department instruction — primary | The **30-day advance notice** before the destruction date; officials may attend; exemption where destruction is already under official supervision |
| `P04-LAW-D` | **ข้อหารือกรมสรรพากร เลขที่ กค 0811/09658** (14 กันยายน 2542) | this session | Revenue Department ruling — persuasive, **not** a general instruction | Destruction of **damaged fixed assets**: remaining book value deductible where destruction is **proved** and the **auditor certifies** it; not prohibited by มาตรา 65 ตรี (13); allowed **without prior notice** on those facts |
| `P04-LAW-F` | **ประมวลรัษฎากร มาตรา 77/1 (8) และ (9)** — the VAT definitions of *"ขาย"* and *"สินค้า"* | this session | **Primary statute** | A fixed asset is goods; its transfer is a sale **with or without consideration**; deeming provisions for non-business use, goods missing from the record, and goods remaining on cessation. `07` §5.5 |
| `P04-LAW-E` | **คำสั่งกรมสรรพากร ที่ ป. 36/2536** (15 พฤศจิกายน 2536) — การขายสินค้าตามสัญญาให้เช่าซื้อหรือสัญญาซื้อขายผ่อนชำระ | this session | Revenue Department instruction — primary | **Hire-purchase / instalment acquisition**: a tax invoice on **each instalment due date**; VAT per instalment, not on the whole contract at inception |

### 4.3 Statutory classification discipline applied

- `P04-LAW-A` is an **explanatory manual**, not the standard. Every finding drawn
  from it is classified **ACCOUNTING STANDARD INTERPRETATION**, never
  **THAI STATUTORY REQUIREMENT**. The gazetted TAS 16 text remains unretrieved —
  registered `P04-B-30`, continuing the prior package's hold.
- `P04-LAW-D` is a **single ruling on specific facts**. It is persuasive, not
  general. The question it does not settle — whether the 30-day regime of
  `P04-LAW-C` reaches fixed assets — is registered `P04-B-24` as
  **HOLD / EVIDENCE REQUIRED** and routed to the Accounting-Tax track, **not**
  answered by inference.
- A search-result summary encountered during retrieval asserted a 30-day notice
  requirement for fixed-asset write-off. Reading `P04-LAW-D` in full **did not
  support** that assertion. The summary was discarded and the source text used.
  Recorded in `18_P04_REVISION_LOG.md` as `P04-REV-07`.
