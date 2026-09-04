# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# 18 — Thai User Validation Checklist

Control Level: `/L9999.9999`
Status: `CHECKLIST PREPARED — ZERO ITEMS VALIDATED — ALL THAI CONTENT REMAINS CANDIDATE / UNVALIDATED`

---

## 1. Standing Position

**No Thai user has validated any label, flow, reason code, document name or report title in any round of this programme.** This is `GAP-FS-11`, severity `BLOCKING for user-facing design`, owner **Boss to commission**. `GAP-MD-30` records that the Thai business-reality review panel's named membership has never been filled, and prior evidence describes the gap as structural and unremedied since the founding control document of 2026-08-30.

R4 does not change this. R4 wrote extensively about Thai SME operating reality across `02_L1_DOMAIN_UNDERSTANDING_REGISTER.md` and elsewhere, and the AAS+ challenge (`13` §2, Track 02) returned a `HOLD` for exactly this reason: **that content is plausible and unverified, and plausibility is the failure mode an AI executor is most prone to.**

This file therefore does two things. It converts everything requiring Thai validation into a checklist a real Thai panel can work through. And it states plainly that the checklist is empty of results.

Every Thai string in this package carries `CANDIDATE / UNVALIDATED — THAI USER REVIEW REQUIRED`. Every Thai statutory assertion is `HOLD / EVIDENCE REQUIRED` and belongs to the Accounting-Tax track, not to Inventory and not to this checklist.

---

## 2. Who Must Validate

| Panel role | Why needed | Items they own |
|---|---|---|
| Thai warehouse storekeeper or supervisor | Operational vocabulary and workflow realism | Menu names, operation flow, count practice, reason codes, packaging language |
| Thai SME owner or manager | Whether the module answers the questions they actually ask | Report and analytics content, replenishment behaviour, scrap authorisation expectations |
| Thai accountant, internal or external | Whether the outputs are usable as accounting evidence | Stock card, valuation report, adjustment and scrap registers, document naming |
| Thai auditor | Whether the evidence would be accepted | Audit trail, count witness practice, document numbering expectations |

Prior evidence names filling this membership as a Boss action. R4 restates it as decision 3 in `13` §8.

---

## 3. Section A — Menu Naming (29 items)

Every menu name in `17_THAI_MENU_AND_REPORT_NAMING_REGISTER.md` (`TH-01` .. `TH-29`) requires validation. The checklist question for each is the same: *would a Thai storekeeper, owner or accountant say this word for this thing?*

| Status | Count |
|---|---:|
| Menu names requiring validation | 29 |
| Menu names validated | **0** |

### 3.1 Specific naming conflicts requiring a decision, not just a check

| ID | Conflict | Why it matters |
|---|---|---|
| `N-1` | The umbrella `รายการเคลื่อนย้ายสินค้า` hides `รับเข้า` / `จ่ายออก` / `โอนย้ายภายใน` | Staff think in three separate acts; the proposed resolution is an umbrella for search plus three first-level entries |
| `N-2` | `คลัง` (warehouse) versus `สาขา` (Thai tax branch) | A warehouse must **never** be default-labelled `สาขา`. This is an identity distinction, not only a naming one. `TH-HOLD-06`, `GAP-MD-15` |
| `N-3` | Valuation must state its policy | Header must carry `ตามนโยบายต้นทุน: มาตรฐาน / ถัวเฉลี่ย / FIFO` and the as-of date `ณ วันที่` |
| `N-4` | Consumable must be `วัสดุสิ้นเปลือง` | Not a literal rendering of "used up" |
| `N-5` | Statutory report name `รายงานสินค้าและวัตถุดิบ` | `HOLD / EVIDENCE REQUIRED` — must not be used as a label until the Accounting-Tax track confirms it (`TH-HOLD-01`) |
| `R4-N-6` | **New in R4.** Thai candidate strings diverge between three prior registers for `INV-M03`, `INV-M07`, `INV-M12`, `INV-M26`, `INV-M27` | The naming register is the designated authority, but the divergence is unresolved and must be settled by the panel, not by an executor |

---

## 4. Section B — Report Naming (14 items)

`TH-R01` .. `TH-R14` all require validation. Two carry statutory holds that are **not** for this panel: `TH-R03` (statutory stock report format, `TH-HOLD-01`) and `TH-R08` (scrap and destruction register, `TH-HOLD-02`) route to the Accounting-Tax track for the statutory aspect, while their *usability* aspect stays here.

| Status | Count |
|---|---:|
| Report names requiring validation | 14 |
| Report names validated | **0** |

---

## 5. Section C — Operating-Reality Assertions Made By R4

R4 asserted the following about Thai SME behaviour. **Each is an assumption until a Thai user confirms it.** They are listed explicitly so that none of them can be mistaken for research.

| # | Assertion | Where used | Consequence if wrong |
|---:|---|---|---|
| 1 | Backdating is routine, not exceptional — goods move before anyone types | `INV-M03`, `R4-F-08`, `R4-F-20`, `L6-13` | The two-date requirement and the history-ordering requirement would be over-engineered |
| 2 | Counting is done on paper first and typed later, so count date and entry date genuinely differ | `INV-M02`, `INV-F-03` | The separate count session concept would be unnecessary |
| 3 | Someone senior is expected to be named as accepting a stock difference | `L7-03` | Approval control could be lighter |
| 4 | Scrap is commercially and tax sensitive; owners want to know who authorised a write-off | `L7-04` | Approval control could be lighter |
| 5 | Salvage sale of scrapped goods genuinely happens | `L6-07`, `INV-F-13` | The salvage origination work would be unnecessary |
| 6 | Duty and clearing invoices arrive weeks after goods, often after some are sold | `INV-M05`, `L6-14` | The landed-cost-after-sale case would be less critical |
| 7 | Most Thai SMEs do not run formal planning; replenishment is a shortage worklist | `INV-M01` | The menu design would be wrong in shape |
| 8 | Reordering rules are set once and never maintained | `INV-M27` | Staleness visibility would be unnecessary |
| 9 | Staff speak in packaging terms — "three boxes" — not base units | `INV-M26` | Packaging prominence would be over-weighted |
| 10 | Businesses buy in one unit and sell in another, constantly | `INV-M29`, `L6-09` | The rounding-direction finding would be less material |
| 11 | Product masters contain duplicates under Thai and English names, and re-used codes | `L10-04` | Migration identity rules could be simpler |
| 12 | Location naming must match what staff say out loud; deep hierarchies are abandoned | `INV-M11`, `INV-M18` | Location design could be deeper |
| 13 | A micro-SME may have two staff in total, making strict segregation impossible | `R4-F-21`, `L7-09` | The compensating-control path would be unnecessary |
| 14 | The external accountant is often the ultimate arbiter and needs line-by-line reconcilability | `INV-M14` | Valuation reporting could be less granular |
| 15 | Consignment stock is informally treated as "ours" | `L5-07` | The ownership dimension could be deprioritised |
| 16 | Expiry management, not recall, is the real driver of batch tracking | `INV-M09` | Traceability emphasis would be misplaced |
| 17 | Multi-step routes are abandoned by SMEs; one-step in and out is the norm | `INV-M19` | Route simplification would be unnecessary |
| 18 | A wrong put-away suggestion is worse than no suggestion | `INV-F-32` | Override prominence could be reduced |

**18 operating-reality assertions. 0 validated.**

R4 records these as a numbered list precisely because burying them in prose would let them harden into accepted fact across future rounds. Any one of them being wrong changes a design conclusion.

---

## 6. Section D — Policy Questions Requiring Thai Business Input

These are not naming questions. They are business policy choices that no executor may make.

| ID | Question | Register |
|---|---|---|
| `GAP-FS-16` / `GAP-MD-06` | Over-receipt tolerance: what threshold, and who approves beyond it | `INV-F-09` |
| `GAP-FS-17` / `GAP-MD-02` | Which count-freeze policy can a Thai SME actually operate, and what is the approval model | `INV-F-04`, `L7-03` |
| `GAP-FS-18` | How granular must segregation of duties be per document type | `L7-09` |
| `GAP-FS-22` | Reservation default: reserve on confirmation, or reserve on picking | `INV-F-06` |
| `RISK-U02` / `U-02` | Is a distinct damaged-goods state needed before scrap | `L7-04` — recorded in prior evidence as *"simply never asked"* |
| `GAP-FS-13` / `GAP-MD-25` | Which management measures do Thai SME owners actually want | `INV-M15` |
| `GAP-FS-15` | Is a point-of-sale channel in scope, and is stock issue real-time or batch | Scope |
| `GAP-FS-21` | Are the five internal location role names right for Thai warehouses | `INV-M18` |
| `R4-Q-01` | **New in R4.** What reason taxonomy should adjustments and scrap use | `L7-08` — this taxonomy is what keeps non-sale reductions distinguishable from sales, so it is not cosmetic |
| `R4-Q-02` | **New in R4.** Are `INV-M12` and `INV-M13` comprehensible as two menus, or should they be one view with a state filter | `INV-M13` |
| `R4-Q-03` | **New in R4.** Which structured barcode formats are actually in use by Thai suppliers | `INV-M28`, `R4-F-12` |

---

## 7. Section E — Items That Are NOT For This Panel

Recorded to prevent scope confusion. These are Thai **statutory** matters and route to the Accounting-Tax track, not to a user panel.

`TH-HOLD-01` statutory stock report format · `TH-HOLD-02` scrap destruction procedure and deductibility · `TH-HOLD-03` import duty and VAT in landed cost · `TH-HOLD-04` withholding-tax correlation with product kind · `TH-HOLD-05` accepted Thai costing norms · `TH-HOLD-06` warehouse versus registered tax branch · `TH-HOLD-07` witnessed annual physical count requirements · `TH-HOLD-08` sector traceability obligations · `TH-HOLD-09` delivery document to tax invoice linkage and numbering.

All nine remain `HOLD / EVIDENCE REQUIRED`. **R4 makes no Thai statutory claim anywhere in this package.**

---

## 8. Validation Scorecard

| Section | Items | Validated |
|---|---:|---:|
| A — Menu naming | 29 + 6 conflicts | **0** |
| B — Report naming | 14 | **0** |
| C — Operating-reality assertions | 18 | **0** |
| D — Policy questions | 11 | **0** |
| E — Statutory (not this panel) | 9 | Routed, all held |
| **Total requiring Thai validation** | **78** | **0** |

---

## 9. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
