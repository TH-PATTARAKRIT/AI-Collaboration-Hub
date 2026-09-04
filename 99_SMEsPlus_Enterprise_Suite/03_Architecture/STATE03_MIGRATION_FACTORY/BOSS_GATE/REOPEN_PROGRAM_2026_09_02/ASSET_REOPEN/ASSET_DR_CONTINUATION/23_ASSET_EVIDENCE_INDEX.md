# 23 — EVIDENCE INDEX

**LAYER 2 — AUDIT QUARANTINE.** Mandatory under §7. Every significant conclusion's
evidence, with the fields §7 requires.

---

## 1. Evidence obtained by **this** session

| Evidence ID | Source | Type | Locator | Date | Observed fact | Interpretation | Confidence | Class | Affects | Gate impact |
|---|---|---|---|---|---|---|---|---|---|---|
| `E-C-01` | Reference ERP v18 Enterprise, build `18.0+e.20250608` | Primary source code | `mrp/models/mrp_routing.py` L17–59 | 2026-09-04 | The operation model's only resource reference is the work centre | Machine identity is absent from routing | High | `FACT VERIFIED` | `07`, `19` §3 | Confirms `BD-03` |
| `E-C-02` | Same | Primary source code | `mrp_maintenance/models/mrp_maintenance.py` | 2026-09-04 | Equipment→work centre is Many2one; maintenance blocks capacity via calendar leaves; requests link to production and work orders | N:1, with an unused traceability hook | High | `FACT VERIFIED` | `06`, `07` | — |
| `E-C-03` | Same | Primary source code | `maintenance/models/maintenance.py` | 2026-09-04 | Requests carry no monetary field; requests carry a preventive/corrective type; equipment carries an inert `cost` float | The planned/unplanned axis exists; the cost field is a second source of truth | High | `FACT VERIFIED` | `06` §4, `09` §6 | **Supplies `BLK-08`'s data** |
| `E-C-04` | Same | Primary source code | `mrp/models/mrp_workcenter.py` — productivity, loss and loss-type models | 2026-09-04 | A downtime taxonomy of named causes in four categories, with optional work-order reference and calendar-aware duration | A reusable structure for `BD-02` | High | `FACT VERIFIED` | `07` §4, `19` §4 | Reduces build scope |
| `E-C-05` | Same | Primary source code | `account/models/account_move_line.py` `_check_off_balance` | 2026-09-04 | An entry mixing off-balance and on-balance accounts is refused | Platform-wide structural firewall | High | `FACT VERIFIED` | `05` §7, `10` §5 | **Makes `BD-01` enforceable** |
| `E-C-06` | Same | Primary source code | `mrp_account/models/mrp_workcenter.py` `expense_account_id` | 2026-09-04 | No domain excludes off-balance accounts | Selectable, not postable | Medium-High | `FACT VERIFIED` (absence) | `05` §8, `CTR-C-05` | Design ruling |
| `E-C-07` | Same | Primary source code | `mrp/models/mrp_workorder.py` `_cal_cost` L576–588; rate written at L~662, L~715 | 2026-09-04 | Cost uses the **live** work-centre rate; the snapshot is written at completion and read only by reporting helpers | The snapshot does not protect valuation or the ledger | High | `FACT VERIFIED` | `08` §5, `C-01`, `C-02` | **Corrects the baseline** |
| `E-C-08` | Same | Primary source code | `mrp_account/models/mrp_production.py` `_cal_price`, `_post_labour` | 2026-09-04 | FG absorption only for FIFO/average; the labour entry only under real-time valuation; the entry is dated **today** | Two conditionals and a period defect | High | `FACT VERIFIED` | `08` §3, `13` `T-02`, `CTR-C-07`, `CTR-C-09` | Design rulings |
| `E-C-09` | Same | Exhaustive search | All 797 modules — `normal_capacity`, `absorption_variance`, `under_absor`, `over_absor`, `overhead_absor`; `variance` in `mrp_account`/`stock_account` | 2026-09-04 | **Zero hits** | No normal-capacity or variance mechanism exists | High | `FACT VERIFIED` (negative, workspace-bounded) | `07` §7, `19` §10 | **Adds build step 3** |
| `E-C-10` | Same | Primary source code | `account_asset/models/account_asset.py` L15–16, L50–80, L273–281 | 2026-09-04 | `DAYS_PER_MONTH = 30`; three prorata modes, default `constant_periods`; `none` backdates to fiscal-year start | 30/360 is the default; `none` is not pro-ration | High | `FACT VERIFIED` | `05` §3 | Confirms `BLK-01`'s stakes |
| `E-C-11` | Same | Security data | `account_asset/security/*.xml`, `maintenance/security/*.xml`, `mrp/security/*.xml` | 2026-09-04 | Assets visible to child companies via `parent_of`; equipment, work centres, BoMs and operations visible when company is empty; work orders and time logs strict | Two leakage vectors and one disclosure | High | `FACT VERIFIED` | `14` | **SaaS FAIL in `20`** |
| `E-C-12` | Same | Product master | `product/models/product_template.py`; `stock/models/product.py` | 2026-09-04 | `type` ∈ goods/service/combo; storability is a **separate** boolean | The taxonomy is two-dimensional | High | `FACT VERIFIED` | `12` §2 | Corrects an assumption |
| `E-C-13` | Custom module `equipment_sequence` v18.0.1.6 | Primary source code | `__init__.py`, `models/__init__.py`, `models/account_asset.py`, `wizard/asset_modify.py` | 2026-09-04 | `wizard` unimported; three model files unimported; `validate()` claims the machine; no uniqueness constraint; a soft selection-domain guard; nothing ever unclaims | Three of four behaviours inert, plus a one-way ratchet | High | `FACT VERIFIED` | `06` §5, `16` §3, `CTR-02`, `CTR-04` | Most actionable defect |
| `E-C-14` | Platform core of the same build | Primary source code | `odoo/fields.py`, `odoo/models.py`, `odoo/api.py` L419–512 | 2026-09-04 | `states` absent from the field engine; `name_get` absent from the base model; `@api.model create` still shimmed | Two custom constructs are dead metadata; the third works | High | `FACT VERIFIED` | `16` §3 | **Turns inference into proof** |
| **`E-L-01`** | **TFAC — มาตรฐานการบัญชี ฉบับที่ 2, per ประกาศ 34/2562** | **Primary standard text** | ¶12–13 | 2026-09-04 | Fixed production overhead includes the depreciation of production equipment and enters conversion cost; allocation on **normal capacity**; per-unit not increased when output falls; **unallocated expensed in period**; capped in high-output periods | Absorption required; the denominator constrained | High | `FACT VERIFIED` | `18` §2–3, `09`, `11`, `12` | **Closes `BLK-03`; raises `BLK-07`, `BLK-08`** |
| **`E-L-02`** | **TFAC — คู่มืออธิบาย TAS 16, 27 ก.พ. 2563** | **Standard-setter publication** (not the standard) | Depreciation section | 2026-09-04 | Component depreciation required where significant; life and residual reviewed at least annually; depreciation to P&L **except** where included in another asset's carrying amount | Corroborates `E-L-01` from the asset side | Medium-High | `ACCOUNTING STANDARD INTERPRETATION` | `18` §4 | Structural requirements |
| **`E-L-03`** | **DBD — ประกาศ กำหนดรายการย่อ, แบบ 2 (บริษัทจำกัด)** | **Primary regulation** | Prescribed statements | 2026-09-04 | **No** off-balance, memorandum or นอกงบดุล line item in any prescribed statement | No statutory presentation surface | High | `FACT VERIFIED` (negative) | `18` §5, `10` §5 | **Closes `BLK-04`** |
| `E-D-01` | Derived | Analytic re-derivation | Independent recomputation of the day-convention scenarios | 2026-09-04 | 20,372.40 / 18,400.87 / 19,058.05 / 239,868.57 on 1,200,000 over 1,826 days | The baseline's figures reproduce to the satang | High as arithmetic | `FACT VERIFIED` (arithmetic) / underlying engine transcription remains `SOURCE-SUPPORTED INTERPRETATION` | `08` §2 | Confirms the 8% February exposure |

## 2. Evidence carried from `LIN-02` at its original class and date

| Evidence | Original class | Date | Carried because |
|---|---|---|---|
| Runtime read-out of the UAT — population, states, account triples, absent model links | `FACT VERIFIED` | 2026-08-26 | The UAT was unreachable this session; not refreshed, not extrapolated |
| Asset Model export | `FACT VERIFIED` (content) / provenance `UNRESOLVED` | 2026-08-27 | Unchanged; provenance is part of `Q-01` |
| Asset Actual Mapping handoff | `FACT VERIFIED` (as a project record) | 2026-08-26 | Unchanged |
| Revenue Code s.65 bis (2); Royal Decree 145 s.4–5 | `FACT VERIFIED` | 2026-09-04 | Not contradicted by the new standards evidence |
| Equivalence of the custom Thai method and the calendar mode, within 0.03 baht | `SOURCE-SUPPORTED INTERPRETATION` | 2026-09-04 | Rests on the engine transcription; re-running it would not raise its class |
| The full Levels 1–6 mechanism corpus, 46 deliverables | Various | 2026-09-04 | Re-tested per `02` §2; four mechanism corrections issued |

## 3. Evidence **not** obtained, and the consequence

| Not obtained | Consequence | Recovery |
|---|---|---|
| Any runtime or database read | `BLK-01`, `BLK-02` held; six further questions open | `22` §4 — under ten minutes |
| The installed-module list of the running system | **Caps every negative finding in this and the previous package** | `Q-04` |
| TAS 16 standard text | Three conclusions rest on TFAC's manual and are down-classified accordingly | One retrieval |
| A Revenue Department ruling on the pro-ration unit | `HOLD-01` — non-blocking | Accounting-Tax track |
| Independent review by a human or a separate agent | The AAS+ audit is a self-challenge | Declared, not concealed |

## 4. Evidence standard observed

No conclusion in this package uses "seems", "probably" or "likely" as closure. Every
negative finding states that it is bounded by the source available in this workspace.
Every derived number states that it is derived. Every statutory statement carries the
class of its source and no more — and where TFAC's own manual disclaims being part of
the standard, the conclusions resting on it are labelled interpretation, not requirement.
