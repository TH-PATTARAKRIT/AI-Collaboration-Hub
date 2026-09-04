# 18 — THAI ACCOUNTING / STATUTORY REGISTER (LEVEL 20)

**LAYER 2 — AUDIT QUARANTINE.**

Per §5 Level 20, every statement is separated into one of five classes and none is
promoted beyond its evidence. **Any statutory conclusion without authoritative evidence
is HOLD.**

Classes: **THAI STATUTORY REQUIREMENT** · **ACCOUNTING STANDARD INTERPRETATION** ·
**COMMON ERP PRACTICE** · **SMEsPLUS DESIGN POLICY** · **MANAGEMENT ACCOUNTING POLICY**

---

## 1. Sources used

| ID | Source | Authority | Obtained |
|---|---|---|---|
| `LAW-01` | Revenue Code s.65 bis (2) | Revenue Department, primary statute | `LIN-02`, carried |
| `LAW-02` | Royal Decree No. 145, s.4–5 | Revenue Department, primary statute | `LIN-02`, carried |
| `LAW-03` | PwC Worldwide Tax Summaries — Thailand | Professional secondary | `LIN-02`, carried |
| `LAW-04` | Thai ERP vendor guidance on daily depreciation | Practice secondary | `LIN-02`, carried |
| **`TAS-02`** | **มาตรฐานการบัญชี ฉบับที่ 2 *สินค้าคงเหลือ***, per ประกาศสภาวิชาชีพบัญชี ที่ 34/2562 — **the standard text** | **TFAC, primary standard** | **This session** |
| **`TAS-16M`** | **คู่มืออธิบายมาตรฐานการบัญชี ฉบับที่ 16** — TFAC's official explanatory manual, published 27 ก.พ. 2563 | **TFAC, standard-setter publication.** The manual states on every page that it is *not part of* the standard | **This session** |
| **`DBD-01`** | **ประกาศกรมพัฒนาธุรกิจการค้า — รายการย่อที่ต้องมีในงบการเงิน, แบบ 2 (บริษัทจำกัด)** | **Department of Business Development, primary regulation** | **This session** |

`LAW-05` in the baseline — TFAC primary text on property, plant and equipment — is
**partially discharged**: `TAS-16M` is the standard-setter's own manual on that standard,
not the standard text. The standard text itself (ประกาศ 32/2565) was located but could
not be retrieved by this session's network path. Where a conclusion rests on `TAS-16M`
alone it is classified **ACCOUNTING STANDARD INTERPRETATION**, never STATUTORY.

## 2. Depreciation absorbed into inventory — resolved

**Class: ACCOUNTING STANDARD REQUIREMENT (TFRS), from the standard text.**

`TAS-02` ¶12 (translated; Thai wording quoted in `03` `BLK-03`):

> The conversion cost of inventories comprises costs directly related to the units
> produced, such as direct labour, together with a systematic allocation of fixed and
> variable production overheads incurred in converting materials into finished goods.
> **Fixed production overheads are the indirect costs of production that remain
> relatively constant regardless of production volume, such as the depreciation and
> maintenance of factory buildings, factory equipment and right-of-use assets used in
> the production process, and the costs of factory management and administration.**

`TAS-16M` corroborates from the asset side: depreciation is recognised in profit or loss
**except where it must be included in the carrying amount of another asset**.

**Conclusion.** Absorbing the depreciation of production equipment into inventory is not
merely permitted under Thai accounting standards — **it is required**. `BLK-03` closes.

**What this does not settle.** Whether the Revenue Department accepts the same figure
for **tax** purposes, and what timing difference arises, is a separate question. It is
`UNR-C-01` in `22` §5 at Medium severity and is **not** blocking, because the accounting
treatment is mandatory regardless of the tax outcome. **This session makes no tax claim
about inventory absorption.**

## 3. Fixed overhead allocation — the binding constraint

**Class: ACCOUNTING STANDARD REQUIREMENT (TFRS), from the standard text.**

`TAS-02` ¶13, four requirements:

| # | Requirement | Design consequence |
|---|---|---|
| 1 | Fixed production overhead is allocated **on the basis of normal capacity** of the production facilities. Normal capacity is the production expected on average over several periods or seasons under normal circumstances, **taking into account capacity lost to planned maintenance**. The actual level may be used if close to normal capacity | The rate denominator is normal capacity — `09` §3, `11` §5. Planned maintenance is **inside** it — `09` §6 |
| 2 | The fixed amount allocated to each unit **shall not increase** when production falls or ceases | The naïve 100%-attribution reading is forbidden — `09` §2 |
| 3 | **Unallocated production overhead is recognised as an expense in the period in which it is incurred** | The non-productive remainder is period expense — `09` §7 |
| 4 | In abnormally high production the per-unit fixed amount is **reduced**, so inventory is not carried above cost | Absorption is capped at the period's depreciation — `09` §5 |

**This is the most consequential evidence obtained by this session.** Requirement 1
mandates a mechanism that **does not exist anywhere in the 797-module reference product**
(`07` §7). Requirement 3 independently reaches the same destination as `BD-02`.
Requirements 2 and 4 constrain the arithmetic in ways the Boss's instruction does not
address, which is why `BLK-07` and `BLK-08` exist.

**Also from ¶13:** variable production overhead is allocated **on the actual use of the
production facilities** — the basis for the two-driver departure in `11` §4.

## 4. Depreciation and pro-ration — carried, unchanged

| Statement | Class | Basis |
|---|---|---|
| Depreciation must be deducted in proportion to the period from acquisition | **THAI STATUTORY REQUIREMENT** | `LAW-01`, `LAW-02` |
| Rates by asset class are **maximums**, not required schedules | **THAI STATUTORY REQUIREMENT** | `LAW-02` |
| Part accounting periods are apportioned | **THAI STATUTORY REQUIREMENT** | `LAW-02` |
| The apportionment unit is specifically the **day** | **COMMON ERP PRACTICE** — **not** proven statute | `LAW-04` secondary only. Primary text says *period* (`ระยะเวลา`), not *days*. **HOLD** |
| Useful life and residual must be reviewed **at least at each financial year end**; changes are accounting-estimate changes under TAS 8 | **ACCOUNTING STANDARD INTERPRETATION** | `TAS-16M` |
| **Component depreciation is required** where a component's cost is significant relative to the whole | **ACCOUNTING STANDARD INTERPRETATION** | `TAS-16M`, with a worked machine example |
| Depreciation goes to profit or loss **except** where it must be included in another asset's carrying amount | **ACCOUNTING STANDARD INTERPRETATION** | `TAS-16M` |

### Two consequences the reference product cannot meet

1. **Component depreciation.** `TAS-16M` illustrates it with a production machine split
   into frame, circuitry, mould and belt, each with its own life. The reference product
   has **no component concept** and its asset↔machine link is single-valued, so it can
   express neither the accounting split nor the operational one (`06` §2). SMEsPlus must
   support a **parent asset with depreciable components** and must decide how components
   aggregate into one machine cost pool. **Not blocking; structural.**
2. **Annual review of life and residual.** No review mechanism exists. `10` §4 and
   `11` §6 reuse this mandatory review as the natural cadence for the internal-usage rate
   and for normal capacity — one control, three purposes.

## 5. Off-balance accounts in the statutory statements — resolved

**Class: THAI REGULATORY FACT.**

`DBD-01` prescribes the required line items for a private limited company. Exhaustive
text search of the prescribed statement of financial position, statement of
comprehensive income, statement of changes in equity and cash-flow statement returns
**no** off-balance-sheet, memorandum or *นอกงบดุล* line item of any kind.

**Conclusion.** Amounts in accounts of that class have **no presentation surface** in the
Thai statutory financial statements. The management ledger cannot appear in them.
`BLK-04` closes.

**Stated precisely, because the distinction matters.** This is a fact about
**presentation**. It is not affirmative authorisation for the **bookkeeping**, and it
does not follow that any memorandum ledger is lawful merely because it is unprintable.
Whether the Accounting Act constrains a memorandum ledger is `UNR-C-04` in `22` §5 at
Low severity. **The blocker as asked is answered; the narrower question is declared
rather than quietly absorbed.**

## 6. Items still on HOLD

| ID | Item | Class sought | Why HOLD |
|---|---|---|---|
| `HOLD-01` | Is the Thai pro-ration unit legally the **day**? | Statutory | Primary text says *period*. A Revenue Department ruling would settle it. **Not blocking** — the daily basis is the conservative choice either way |
| `HOLD-02` | Does Thai **tax** accept depreciation absorbed into inventory, and on what timing? | Statutory | Not researched. Accounting treatment is mandatory regardless. **Not blocking** |
| `HOLD-03` | TAS 16 **standard text** (as opposed to TFAC's manual) | Standard | Located; not retrievable by this session's network path. Affects only the classification of §4's last three rows |
| `HOLD-04` | Statutory standing of the **one-baht residual** convention | Statutory | Carried from the baseline. **Now matters more**, because `10` §3 shows a token residual makes one internal-usage rate base useless |
| `HOLD-05` | Does Thai tax permit **suspending** depreciation on an owned asset? | Statutory | Carried. Bears on the pause function |
| `HOLD-06` | Bookkeeping standing of a memorandum ledger under the Accounting Act | Statutory | New — `UNR-C-04`. **Not blocking** |

**No item in this register is closed by inference, by analogy to IFRS, or by
professional-secondary sources alone.**

## 7. The statutory picture in one paragraph

Thai tax law requires depreciation to be pro-rated from acquisition and caps the rate by
asset class, leaving the life to the entity's own judgement. Thai accounting standards
require the depreciation of production equipment to be **absorbed into inventory** as a
fixed production overhead, allocated on **normal capacity**, with anything unallocated
**expensed in the period**, and require both **component depreciation** and an **annual
review** of life and residual. The statutory financial statements prescribed by the
Department of Business Development have **no line** in which an off-balance amount could
appear. Taken together: the SMEsPlus costing proposition is not merely permitted — it is
closer to what the standards already require than the reference product is, and the two
places the design must be most careful are the **allocation denominator** and the
**boundary between the two ledgers**.
