# 20 — Clean-Room Process Transformation Register

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-08 OUTPUT — CLEAN-ROOM TRANSFORMATION EVIDENCE — NOT A CLEAN-ROOM AUDIT PASS`
Governing rules: Clean Room Learning Directive v2.0 (Policy A); execution prompt §2 hard prohibitions; CORR-007B Layer model and Layer 2 quarantine rules (`9996072a`); Council 08 invariant `Reference ERP behavior = Evidence / Learning Input, not target architecture by default`.

---

## 1. Transformation Chain Applied to Every Menu

`Benchmark Menu -> Business Meaning -> Thai User Language -> SMEsPlus Candidate Process Reference -> Evidence / Gap / Gate Impact`

| Menu ID | Benchmark menu | Business meaning extracted | Thai user language (17) | SMEsPlus candidate (map) | What was deliberately NOT carried |
|---|---|---|---|---|---|
| OP-01 | Replenishment | Order-before-stock-out planning with explainable proposals | เติมสินค้า / แผนเติมสินค้า | 12 | Scheduler/procurement architecture; rule object model |
| OP-02 | Inventory Adjustments | Count + approval + reason + period control | ปรับปรุงยอดสต็อก / นับสต็อก | 13 | Conflict wizard flow; soft-only default; global bypass |
| OP-03 | Transfers | One movement fact model behind three Thai documents | รับเข้า / จ่ายออก / โอนย้าย | 11, 14 | State machine, benchmark document-type vocabulary, return wizard shape |
| OP-04 | Scrap | Reasoned, approved removal with loss fact and destruction evidence | ตัดสินค้าชำรุด/สูญเสีย | 13 | Scrap document model; loss-location naming |
| OP-05 | Landed Costs | Acquisition-cost allocation as accounting interface | ต้นทุนสินค้าเพิ่มเติม | 15 | Eligibility restriction as design rule; account vocabulary |
| OP-06 | Run Scheduler | Deterministic, auditable background planning | ประมวลผลแผนสต็อก (admin) | 12 | Job/cron design |
| PR-01 | Products | Single identity; three Thai kinds over a documented two-axis derivation | สินค้า | 09 | Two-axis gate as schema; type labels |
| PR-02 | Product Variants | SKU per option with stable identity | สินค้าย่อย | 09 | Variant model |
| PR-03 | Lots/Serial Numbers | Recall/expiry/warranty traceability | เลขล็อต / เลขซีเรียล | 09 | Lot model; app-layer uniqueness |
| RP-01..06 | Reports | Four audience classes; reproducibility; export tested | 17 §3 | 16 | Report layouts, queries, models |
| CF-01 | Settings | Business-question switches with guards and audit | ตั้งค่าระบบคลังสินค้า | 08 | Settings structure; regeneration-on-write |
| CF-02 | Warehouses | Physical site ≠ tax branch; versioned flow policy | คลังสินค้า | 08, 10 | Regeneration behaviour |
| CF-03 | Locations | Controlled place types; boundary crossing = valuation | ตำแหน่งจัดเก็บ | 08, 10 | Location model |
| CF-04/05 | Routes / Rules | Thai flow templates hiding rules | เส้นทาง / กฎการไหลของสินค้า | 10 | Route/rule engine, vocabulary |
| CF-06 | Operations Types | Thai document kinds with numbering and SoD | ประเภทรายการคลัง | 11 | Benchmark document-type vocabulary; string-literal kind coupling |
| CF-07/08 | Storage Categories / Putaway | Capacity classes; explainable storage rules | ประเภทพื้นที่จัดเก็บ / กฎจัดเก็บ | 08 | Rule models; category coupling |
| CF-09 | Product Categories | Grouping; valuation policy owner *candidate* (Layer 1 only) | หมวดหมู่สินค้าและนโยบายต้นทุน | 08, 15 | Category model; account fields; dual ownership |
| CF-10/11/13 | Attributes / Packagings / Barcode | Stable codes; pack over base unit; Thai barcode formats | 17 | 08, 09 | Models |
| CF-12 | Reordering Rules | จุดสั่งซื้อ min/max policy | จุดสั่งซื้อ | 12 | Reorder-rule model |
| CF-14 | UoM Categories | Thai unit groups, versioned factors, explicit rounding | กลุ่มหน่วยนับ | 08, 09 | Unit tree model |

---

## 2. Prohibition Compliance Statement (execution prompt §2)

| # | Prohibition | Compliance | Evidence |
|---|---|---|---|
| 1 | No source code copied | Complied — no code opened or reproduced | Session read only Layer 1 markdown and governance files |
| 2 | No ORM models copied | Complied | No model names used as SMEsPlus objects (03 uses business objects) |
| 3 | No database schema copied | Complied | 03 §3 states invariants as requirements, not DDL |
| 4 | No method/field/file-path/implementation architecture copied | Complied with one caveat: the reopen deliverables cite `file:line -- method` (A17 style) and the extraction passes quoted those citations back to the executor; **none** were transcribed into this package's 29 files (mechanical scan in §4) | §4 scan |
| 5 | No menu names as final SMEsPlus names | Complied — all Thai names marked candidate, `UNVALIDATED` | 17 |
| 6 | No claim SMEsPlus must follow benchmark | Complied — every "must" in this package is a candidate requirement or a governance rule, never "as the reference does" | All maps |
| 7 | No quarantined source-level evidence exposed to Team B/C/Dev | Complied — Layer 2 not opened; pre-remediation CORR-007B `08`/`09` not opened | 01 §3 |
| 8 | No benchmark behaviour treated as approved design | Complied — status vocabulary never exceeds `COVERED / PARTIAL / HOLD`; no PASS | 25 |

---

## 3. Layer 2 Quarantine Handling

| Question | Answer |
|---|---|
| Was source-level inspection unavoidable? | No. Menu-level business meaning was reconstructed from Layer 1 reopen findings plus general ERP process knowledge (`PROCESS BENCHMARK`). |
| Was any Layer 2 item touched? | Only a directory-level open of the V2.0 module/view export CSV to confirm the inventory module family exists; no view/menu XML content was read or recorded. Classified as boundary contact, not use. |
| Were the extraction passes' `file:line` citations retained? | They exist in the session transcript and in the reopen deliverables (Layer 1 audit documents). They were **not** copied into any of the 29 files here. |
| Would a Team B reader of this package see any vendor identifier? | Residual vendor-adjacent tokens remaining after the scan are limited to project finding IDs (for example `N-A12-01`, `SAAS-04`) and the generic words "benchmark document-type vocabulary" / "string-literal kind coupling" used to *name what must not be copied*; no identifier is usable as a schema or code hint. |

---

## 4. Mechanical Clean-Room Scan of This Package

A mechanical sweep of the 29 output files was run before publication for: fenced code blocks containing programming syntax; tokens matching vendor model naming patterns (`stock.`, `product.`, `ir.`, `res.`, `account.move`, `.py`, `_action_`, `sudo`, `quant`, `orderpoint`, `picking`); and prescriptive phrases ("must use the model present in source", "as Odoo does"). Result is recorded in `28_SESSION_CLOSURE_...md` §5 together with any remediation applied. The scan is a mechanical control, not a substitute for the independent Clean-Room Re-Audit required by `C-05`.

---

## 5. `C-05` Position (unchanged)

| Item | Status |
|---|---|
| CORR-007B files `08`/`09` current branch surface | Remediated (`9996072a`) |
| Independent Clean-Room Re-Audit | **Not performed** (this session is not that audit) |
| Reliance by this package on `08`/`09` | Layer 1 text of `09` only; `08` not opened |
| Team B/C reliance | Not authorized |
| Boss visibility | Preserved in 24, 25 |

---

## 6. Forward Clean-Room Risks Named (carry-forward from reopen `04`, `05`, `07`, `10`, `11`)

| Risk | Where it would bite | Control candidate |
|---|---|---|
| Default-by-absence: benchmark behaviour becomes design because no Thai evidence competes | Count policy, backdate governance, product kinds, branch fields | Real-user validation before Team B; explicit decision records |
| Bundle-by-inheritance: Product Category owning both valuation and putaway | Category design | One joint Category design pass |
| Vocabulary transcription: state machine, document-type names, model names in Team B schema | Team B kickoff | Re-apply clean-room checklist to lifecycle documents; this package's Thai templates as the vocabulary source |
| AI migration agent reproducing source structures under "necessary business fact" | Migration Factory | Extend quarantine discipline to migration code; human design review |
| Account vocabulary transliteration into Thai CoA | Accounting design | Independent Thai CoA definition (TFRS for NPAEs) |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
