# 13 — P04 SOURCE LINK REGISTER

Layer: **2 — audit quarantine**.

Every source relied on, with the pattern and path set that produced it.
Per the clean-room rule, reference-ERP file paths and line ranges are Layer 2
evidence and are cited by **module and behaviour**, not by transcribed code.

---

## 1. Primary source code

| ID | Root | Scope of use |
|----|------|--------------|
| `EV-CODE` | **RE-DERIVATION WARNING** (`P04-F-110`): every root below contains spaces and all evidence here was executed in **`zsh`**, which does not word-split unquoted expansions. Under **`bash`** an unquoted search over these roots returns **0 matches on files that exist** — quote every path or state the shell. Reference ERP v18 Enterprise source tree, build `20250608` — **PATH NOT DECLARED WHEN WRITTEN, and the build string does not identify the tree**: two directories on this host carry build `20250608` and hold **793** and **1753** manifests (`P04-F-93`). **27 of 361 modules installed in the v18 deployment are in neither this root nor the custom set** | The asset module (model, accounting-document extension, modify wizard, security, views, tests); the accounting core (posting routine, lock-date handling, analytic-line creation, product account resolution); procurement; inventory and inventory accounting; manufacturing and manufacturing accounting; work-order and work-order-human-resources; project bridges; expense; loans; deferred recognition; reporting |
| `EV-CUST` | Project custom addon set, v18 line — **65 directories at `Odoo18/EXTRA MODULE/smeplus-custom/addons`, of which only 28 are installed in the v18 deployment; 37 are not.** One deployed module, `scgl_date_range_auto_period`, sits **one directory above this root** (`P04-F-94`) | The equipment-sequence module (full import-chain read); the equipment-product-stock module; the advance-expense-request module |
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
| Custom modules referencing the asset model in code or manifest | **2** | `grep -rlI -E "account\.asset\|account_asset" --exclude-dir=i18n` (three further hits are documentation files — false positives) |
| Reference modules **instantiating** an asset record | **1** | creation-site sweep |

### 1.2 Declared negative patterns

*Re-audited at `01` §6A.22 (`P04-F-121`) against the four boundaries this session
moved — signature set, path set, source scope, generation basis. **Nine of the ten
are protected**: no module outside the declared source scope declares on the model
they concern. **One is exposed** — *no operation-to-equipment reference* — because
`equipment_fleet` declares on `maintenance.equipment` from outside both declared
roots, with no source on this host. Protection is a **floor**: `ir_model_data` sees
XML-id declarations only, so a module could override a method and declare nothing.*

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
| `EV-DB` | **Database archives — 39 artefacts on this host** (27 `PGDMP`, 12 zip-with-`dump.sql`), census completed over `/Volumes` + `$HOME`, size ≥1 MB, two signatures, 0 via the `/Volumes/iMac` symlink (`P04-F-126`) — **zip signature: a member named `dump.sql`; the discriminator that actually separates a backup from source is `dump.sql` at the archive root with `manifest.json` beside it (`P04-F-129`)**. **Two narrowings were undeclared and are now measured** (`P04-F-127`): `2>/dev/null` dropped **141** unreadable directories of 1,070,459 traversed, all macOS privacy containers; and the gzip branch read 200 bytes for one string, so a gzipped `PGDMP` archive would have been missed — **all 72 gzip archives ≥1 MB re-tested with a firing control, none is a database**. **8 identities keyed and read; the rest un-keyed — a file count is not an identity count in either direction**, keyed on `database.uuid`: `45a8e08e` 2026-07-11 (v1.14), `1f6338ae` 2026-07-23 (v1.14), `f4a44cce` 2026-03-30 (**zip**), `66d1b52a` 2026-08-03 ×2 (v1.14 **and zip**), `a1430edc` 2026-07-14 + 2026-06-14 (**v1.16**). **Two formats, not one** — a `PGDMP`-only scan misses the zips (`P04-F-86`) | read this session | **Database evidence**, added after this package's declared *"no database access was attempted"* was tested and found false (`18` `P04-REV-21`). Four sat in one download directory and **one inside the SMEsPlus working tree**, which the first search missed (`P04-REV-24`). **The two v1.16 archives are rejected by the host's default client (16.15)** and require `postgresql@18`; a reader with only the default client reproduces **three of five** (`P04-REV-23`)  **THIS CENSUS IS SUPERSEDED AND IS A LOWER BOUND** (`18` `P04-REV-37`). It was taken over a path set — `~/Downloads` and the SMEsPlus tree — that was **author-chosen and never declared**. A census over a **declared** path set (`/Volumes` + `$HOME`, size bound >=1 MB stated, three signatures content-tested) has already returned **`idemo18_uat`** at `~/OCC_BACKUP/` — **v18, 388 real assets, the database two blockers were held open on** (`P04-F-90`) — plus a name-matched candidate set including further copies of `a1430edc`, `iEVING` 2026-03-31, `BK12MAY26` 2026-06-23, `iMSCG` ×2, `pankhamhom` ×2, `iErpOCC`, `iSCErP` and seven `OCC_Odoo18_Simulation_Lab` snapshots, **none of which is counted here because none has yet been uuid-keyed and content-verified**. Confirmed floor: **>=12 artefacts, >=8 snapshots, >=6 identities.** No count in this package is stated over the host until that census completes; every database-derived finding remains bounded to the identity named in it. |
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
| `LAW-01` | ประมวลรัษฎากร มาตรา 65 ทวิ (2) | primary statute — **inherited (P3); not this session's `P04-LAW-A`…`H`** |
| `LAW-02` | พระราชกฤษฎีกา ฉบับที่ 145 (พ.ศ. 2527) มาตรา 4–5 | primary statute — **inherited (P3)** |
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
| `P04-LAW-H` | **ประกาศอธิบดีกรมสรรพากร เกี่ยวกับภาษีมูลค่าเพิ่ม (ฉบับที่ 2)**, 25 ธ.ค. 2534, in force 1 ม.ค. 2535 — the self-supply safe harbour | **retrieved by P07**, taken in as peer-published | **Primary — Director-General announcement.** Not independently retrieved by P04; P07 quoted the operative text and P04 relies on that quotation | The harbour is conditioned on use **in a VAT-liable business** and covers **use, not transfer** — so donation and scrapping fall outside it. Carries an unresolved limb question P07 declines to settle by inference. `07` §5.5.1 |
| `P04-LAW-G` | **ประมวลรัษฎากร มาตรา 87** — the value-added-tax reporting obligations | this session, after P07 challenge | **Primary statute** | s.87(3) requires the goods-and-raw-materials report **only of registrants carrying on a business of selling goods**, and names nothing about fixed assets. This is what anchors sub-paragraph (จ) of the deemed-sale definition and what takes it out of reach of a fixed asset. `07` §5.2.1 |
| `TAS-16M` | **The same document as `P04-LAW-A`**, cited under a second label in `07` §§5.1–5.3 — *Source `TAS-16M`: คู่มืออธิบายมาตรฐานการบัญชี ฉบับที่ 16*. **One source, two names, one register row until now** | this session | **Duplicate label, not a duplicate source.** Same class as `P04-LAW-A`: TFAC explanatory manual, **not** part of the standards; every finding drawn from it stays ACCOUNTING STANDARD INTERPRETATION | Registered here so the label resolves. Found at `P04-F-143` by deriving which families carry definitions instead of reading the declared list. Consolidation onto one label is `P04-B-50` |
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
