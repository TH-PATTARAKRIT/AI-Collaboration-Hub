# 06 — Inventory Object / Data Concept Model v1.0

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V1-001` | Jira: `ERPPLUS-139`
Status: `CONCEPTUAL BUSINESS MODEL — NOT A DATABASE SCHEMA, NOT APPROVED DESIGN`
Clean-room: Layer 1. **These are business concepts — what a Thai SME must be able to name, count and prove — not tables, not entities, not fields.** No reference-ERP model, field, method, schema, index or markup is described, proposed or implied. Identity statements are candidate business requirements for a future data-design track, not design decisions.

---

## 1. Concept Register

| ID | Business concept | Thai candidate (all `UNVALIDATED - THAI USER REVIEW REQUIRED`) | Who creates it | Who reads it | Candidate business identity | Owning domain |
|---|---|---|---|---|---|---|
| `CN-01` | Company / tenant context | บริษัท | Platform | Everything | tenant + company | SaaS Foundation |
| `CN-02` | Warehouse | คลังสินค้า | CF-02 | Everything | company + code | Inventory |
| `CN-03` | Storage place | ตำแหน่งจัดเก็บ | CF-03, CF-02 defaults | Operations, Reporting | warehouse + place path + role | Inventory |
| `CN-04` | Document type | ประเภทรายการคลัง | CF-06 | OP-02, OP-03, OP-04 | warehouse + code | Inventory |
| `CN-05` | Flow template | เส้นทางการไหลของสินค้า | CF-04, CF-05 | OP-01, OP-03 | company + template + version | Inventory |
| `CN-06` | Storage category | ประเภทพื้นที่จัดเก็บ | CF-07 | CF-08 | company + code | Inventory |
| `CN-07` | Put-away rule | กฎจัดเก็บสินค้าเข้าที่ | CF-08 | OP-03 | company + key + priority | Inventory |
| `CN-08` | Product category | หมวดหมู่สินค้า | CF-09 | PR-01, RP-05 | company + path | Inventory (tree) / **Joint (policy)** |
| `CN-09` | Valuation policy | นโยบายต้นทุน | CF-09 (candidate owner) | RP-05, OP-05 | policy + version + effective date | **Joint Accounting ↔ Inventory** |
| `CN-10` | Attribute and value | คุณลักษณะสินค้า | CF-10 | PR-02 | stable value code | Inventory / Sales |
| `CN-11` | Product | สินค้า | PR-01 | Everything | company + code, plus legacy reference | Inventory |
| `CN-12` | Product variant | สินค้าย่อย | PR-02 | Everything | product + attribute-value codes | Inventory |
| `CN-13` | Product kind | ประเภทสินค้า | PR-01 | Operations, RP-05 | derived, with a stated business rule | Inventory (fact) / Accounting (tax use) |
| `CN-14` | Unit group and unit | หน่วยนับ | CF-14 | Everything | group + unit code + factor version | Inventory |
| `CN-15` | Packaging | หน่วยบรรจุ | CF-11 | OP-03 | product + pack code | Inventory |
| `CN-16` | Barcode format | รูปแบบบาร์โค้ด | CF-13 | OP-02, OP-03 | company + format name + priority | Inventory |
| `CN-17` | Lot | ล็อต | PR-03, OP-03 | RP-03, OP-04 | company + product + lot value | Inventory |
| `CN-18` | Serial | ซีเรียล | PR-03, OP-03 | RP-03 | company + product + serial value, unique | Inventory |
| `CN-19` | Handling unit | หีบห่อ | OP-03 when enabled | RP-02 | handling-unit code, with a history snapshot | Inventory |
| `CN-20` | Reorder rule | จุดสั่งซื้อ | CF-12 | OP-01, OP-06 | product + place | Inventory |
| `CN-21` | Replenishment proposal | ข้อเสนอเติมสินค้า | OP-01, OP-06 | OP-01 | rule + planning-run identity | Inventory |
| `CN-22` | Demand | ความต้องการ | Sales / Purchase / Manufacturing | OP-01, OP-03 | source line + attempt identity | Source domain |
| `CN-23` | Reservation | การจอง | OP-03, OP-06 | RP-01 | movement + place balance | Inventory |
| `CN-24` | Stock document | ใบรับ / ใบจ่าย / ใบโอน / ใบคืน | OP-03 | Reporting | document type + number | Inventory |
| `CN-25` | Movement fact | รายการเคลื่อนไหว | OP-02, OP-03, OP-04, Manufacturing | RP-03, RP-04, RP-05 | document line + attempt identity; **immutable** | Inventory |
| `CN-26` | Place balance | ยอดคงเหลือ | Derived from `CN-25` | RP-01, RP-02 | product × place × lot × handling unit × owner | Inventory |
| `CN-27` | Count session | ใบตรวจนับ | OP-02 | Reporting | session identity | Inventory |
| `CN-28` | Adjustment | รายการปรับปรุงยอด | OP-02 | RP-03, control reports | number + reason + approver | Inventory (fact) / Accounting (posting) |
| `CN-29` | Scrap | รายการตัดสินค้าเสีย | OP-04 | control reports | number + reason + approver | Inventory (fact) / Accounting (posting) |
| `CN-30` | Landed cost allocation | การปันส่วนต้นทุนเพิ่ม | OP-05 | RP-05 | cost document + receipt line | Inventory (fact) / Accounting (posting) |
| `CN-31` | Valuation fact | รายการมูลค่า | OP-02, OP-03, OP-04, OP-05, Manufacturing | RP-05 | movement + policy version | Inventory emits / **Accounting owns posting** |
| `CN-32` | Period close snapshot | ยอดปิดงวด | RP-05 (Joint) | RP-05 | company + period | **Joint** |
| `CN-33` | Opening balance at cutover | ยอดยกมา | Migration + OP-02 | RP-05 | company + cutover date + certification | **Joint** |
| `CN-34` | Feature switch set | การตั้งค่า | CF-01 | Everything | company + version | Inventory / SaaS |
| `CN-35` | Planning run log | บันทึกการประมวลผล | OP-06 | Administrator | run identity | Inventory |
| `CN-36` | Provenance reference | รหัสอ้างอิงระบบเดิม | Migration | Everything | source system + source key → SMEsPlus key | Migration — **does not exist today and must be originated** |

---

## 2. Concept Relationships (business statements, not a schema)

| Statement | Consequence |
|---|---|
| A movement fact always names exactly one source place and one destination place. | Conservation is checkable; every quantity has a provenance. |
| A place balance is a consequence of movement facts, never an independently editable figure. | There is no screen anywhere that sets on-hand directly. |
| A stock document groups movement facts; the document may be cancelled while planned, but a done fact is never removed. | Correction is by reversal. |
| A product may have variants; where variants exist, stock and value are held at variant level and roll up for reporting. | Reporting hierarchy is separate from stock identity. |
| A lot or serial qualifies a movement fact; it does not replace the product on it. | Traceability is an attribute of the movement, not a parallel stock ledger. |
| A packaging converts to the base unit at entry and never becomes a second stock unit. | Only one truthful quantity exists. |
| A valuation policy is versioned and effective-dated; a valuation fact records which version produced it. | Historical valuations remain explainable after a policy change. |
| Every concept above is scoped to exactly one company. | Cross-company movement is two facts in two companies, connected by a transit concept. |
| Every migrated instance of any concept carries a provenance reference. | Replay, reconciliation and audit are possible after cutover. |

---

## 3. Candidate Invariants

These are business rules the future data design must guarantee. They are stated as requirements with an owner, not as implementation decisions.

| ID | Invariant | Why it matters | Owner |
|---|---|---|---|
| `IV-01` | On-hand per place equals the sum of done movements in, minus the sum of done movements out. | The conservation check; without it no stock figure is provable. | Inventory |
| `IV-02` | On-hand may go negative only where the tenant has explicitly allowed it; where it does, it is displayed and flagged, never hidden. | Hidden negatives silently destroy the audit trail. | Inventory |
| `IV-03` | Exactly one balance exists per product, place, lot, handling unit and owner combination. | Prevents duplicate balances that merge inconsistently after the fact. | Inventory |
| `IV-04` | A serial value is unique per product per company, guaranteed at the data layer. | Reactive detection after a duplicate has already shipped is not a control. | Inventory |
| `IV-05` | A done movement fact is immutable; corrections are new reversing facts. | The basis of the audit trail. | Inventory |
| `IV-06` | Every movement carries a stable identity that makes retries safe. | Without it, a retried planning run, integration call or migration replay duplicates stock and value. **Carried as `C-02`; severity is Boss's decision.** | Boss |
| `IV-07` | A movement's date must fall in an open period, unless it passes a recorded exception naming grantor, reason and expiry. | Prevents silent restatement of closed figures. | Inventory + Accounting |
| `IV-08` | Every record belongs to exactly one company, guaranteed below the application layer, with a post-write audit. | Multi-tenant isolation cannot rest on application convention. **Carried as `U-03`.** | SaaS Foundation / Boss |
| `IV-09` | Every migrated record carries a provenance reference to its source. | Nothing can be reconciled or replayed without it; no such mapping exists today. | Migration |
| `IV-10` | A valuation as of a date is reproducible and, after close, agrees with the general ledger. | This is the acceptance test for the whole accounting interface. | **Joint** |
| `IV-11` | A unit factor change never alters a historical quantity; rounding behaviour is explicit and visible. | Retroactive conversion silently restates history. | Inventory |
| `IV-12` | Changing a product's kind while stock exists is an approved action with a stated treatment for the existing balance. | Prevents stock stranded on an item that no longer holds stock. | Inventory |
| `IV-13` | A lot value becomes immutable after its first movement. | Otherwise traceability history is rewritable. | Inventory |
| `IV-14` | Attribute value codes are immutable once used by a variant. | Renaming a display label must never break variant identity or history. | Inventory |
| `IV-15` | Configuration is versioned with effective dates, never regenerated in place. | An explicit departure from the benchmark's regeneration behaviour, which silently rewrote existing configuration. | Inventory |

---

## 4. Concept-Level Impact Summary

| Concept group | Stock truth | Valuation | Accounting handoff | Tax / statutory | Migration | Multi-company |
|---|---|---|---|---|---|---|
| Structure (`CN-02`, `CN-03`, `CN-06`) | Yes (where) | Boundary only | Boundary only | Branch question — `HOLD` | Yes | Yes |
| Master data (`CN-11`–`CN-16`) | Yes (identity) | Yes (policy inheritance, conversion) | Conditional | Product-kind correlation — `HOLD` | Yes | Yes |
| Traceability (`CN-17`–`CN-19`) | Yes | No (unless cost is lot-carried) | No | Sector obligations — `HOLD` | Yes | Yes |
| Planning (`CN-20`–`CN-23`, `CN-35`) | No | No | No | No | Policy only | Yes |
| Transactions (`CN-24`, `CN-25`, `CN-28`–`CN-30`) | Yes | Yes | Yes | Scrap and import — `HOLD` | Yes | Yes |
| Derived positions (`CN-26`, `CN-31`–`CN-33`) | Derived | Yes | Yes | Stock report and valuation — `HOLD` | Yes | Yes |
| Governance (`CN-34`, `CN-36`) | Structural | Conditional | Conditional | No | Yes | Yes |

---

## 5. Concept-Level Open Items

| ID | Concept | Open question | Owner |
|---|---|---|---|
| `GAP-FS-01` | `CN-08`, `CN-09`, `CN-32` | Which concept owns valuation policy, and how is the period close designed? | Joint Accounting ↔ Inventory |
| `GAP-FS-02` | `CN-08` | Product category is a candidate owner of both valuation policy and put-away behaviour; is that dual role acceptable, or must they be separated? | Joint |
| `GAP-FS-03` | `CN-12`, `CN-10` | Variant identity when an attribute set changes after variants already hold stock. | Data design track |
| `GAP-FS-04` | `CN-13` | The tie-break rule when the product-kind derivation is ambiguous. | Inventory |
| `GAP-FS-05` | `CN-19` | Whether handling units are migrated live, as history, or both. | Migration |
| `GAP-FS-06` | `CN-25` | Whether movement idempotency (`IV-06`) is gate-blocking. **Carried as `C-02`.** | Boss |
| `GAP-FS-08` | `CN-36` | The provenance reference does not exist and must be designed from scratch. | Migration |
| `GAP-FS-09` | `CN-33` | Certification of the opening quantity and value against the accountant's opening trial balance. **Carried as `G-5`.** | Joint |
| `GAP-FS-10` | `CN-01` | The Inventory-side multi-tenant invariant set. **Carried as `U-03`.** | Boss |

---

## 6. What This File Is Not

It is not a database design. It names no table, no column, no key structure, no index and no constraint syntax. It proposes no technology. It is the vocabulary a future data-design track would start from, and every identity statement in it is a candidate requiring validation.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
