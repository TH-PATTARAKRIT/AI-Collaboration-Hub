# P11 — UNIFIED TAX ARCHITECTURE

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Model 8 of 15 · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**
> **Every statutory claim below is either carried from a package that cited authoritative Thai
> evidence, or marked `HOLD — STATUTORY EVIDENCE REQUIRED`. P11 makes no statutory claim of its own.**

---

## 1. Statutory positions that are closed, with their authority

| Position | Authority | Status | Consequence |
|---|---|---|---|
| Fixed production overhead — **expressly including depreciation and maintenance of factory buildings, factory equipment and right-of-use assets used in production** — forms part of the conversion cost of inventories | **TAS 2 ¶12**, standard text per **ประกาศสภาวิชาชีพบัญชี ที่ 34/2562**; corroborated from the asset side by TFAC's TAS 16 manual | **`CLOSED — EVIDENCE VERIFIED`** (`BLK-03`) | Absorption is **required**, not permitted |
| Unallocated production overhead is recognised as an **expense in the period incurred**; the per-unit allocation **shall not increase** when production falls or ceases | **TAS 2 ¶13** | **`CLOSED — EVIDENCE VERIFIED`** | `CVP-02`; the actual-hours rate basis is `REJECTED` |
| Prescribed statement line items for a private limited company contain **no off-balance / memorandum / *นอกงบดุล* item** — exhaustive text search of all four prescribed statements | **ประกาศกรมพัฒนาธุรกิจการค้า, แบบ 2** | **`CLOSED — EVIDENCE VERIFIED`** (`BLK-04`) | Off-balance amounts have **no statutory presentation surface** |

## 2. Held statutory items — no AI may close these

| id | Item | Status |
|---|---|---|
| `TX-H01` | Whether Thai **tax** accepts depreciation absorbed into inventory, and the resulting timing difference | `HOLD — STATUTORY EVIDENCE REQUIRED` (`UNR-C-01`) |
| `TX-H02` | How a **standard-costed** product complies with TAS 2 | `HOLD` — Medium-High (`UNR-C-03`, `CTR-C-09`) |
| `TX-H03` | Bookkeeping standing of a memorandum ledger under the Accounting Act | `HOLD` — Low (`UNR-C-04`) |
| `TX-H04` | Withholding tax mechanics, certificate obligations, and the `WHT`/`GRPA` items carried from Account Batch A | `HOLD — STATUTORY EVIDENCE REQUIRED` |
| `TX-H05` | Thai period-attribution consequence of generated tax entries landing in the **current** period when their own period is locked | `HOLD / EVIDENCE REQUIRED` (`XM-02`) — **assessed by the Accounting-Tax track, not here** |
| `TX-H06` | `TH-HOLD-01` statutory **format** of stock cards and registers; `TH-HOLD-02` scrap/destruction evidence | `HOLD` |
| `TX-H07` | `TH-NEW-01` (COGS recognition timing) and `TH-NEW-02` (return cost basis) | `HOLD` — these gate `JT-04` and `JT-05` |

## 3. Tax as a cross-process problem

| id | Finding | Cross-process consequence |
|---|---|---|
| `TX-01` | **Cash-basis tax is emitted by reconciliation, not by the tax engine**, and is **dated today when its natural period is locked** | `P06` acts → `P07`'s return content changes → `P08`'s comparatives change. **It can cross a fiscal year.** Owner: none |
| `TX-02` | **Posting a tax return sets the tax lock date automatically** | A `P07` act sets a `P08` governance state. Reset-to-draft is restricted where carryover exists |
| `TX-03` | **Tax items are outside hash coverage** | The tax subledger is *of record, unprotected*. Assurance over the tax return does not extend to its detail |
| `TX-04` | **`DC-07`** — accrual tax on the document plus cash-basis tax on settlement, with the unmatch reversal not stated | Candidate **double tax recognition**. `UNRESOLVED — EVIDENCE REQUIRED` |
| `TX-05` | Statutory tax **reference** (rates, codes) is `PLATFORM`-scoped; tax **configuration** is `TENANT` or `COMPANY` and is **`HOLD — SCOPE EVIDENCE REQUIRED`** | Under `SMEPLUS-26-09-04-ACC-REV2-CORR1`, `P07` is the process that benefits most from the correction: statutory reference no longer needs an artificial tenant dimension |

## 4. Positions

| id | Position | Basis |
|---|---|---|
| `TXP-01` | **A tax recognition event is owned by `P07`, even when another process's action triggers it.** `P06` may not silently own a tax fact | `TX-01`, `OWN-02` |
| `TXP-02` | **A generated tax entry whose natural period is closed is denied, not re-dated.** Re-dating across a fiscal year is a statutory question, not a convenience | `TX-01`, `XM-02` |
| `TXP-03` | **Tax items are inside integrity coverage** | `TX-03` |
| `TXP-04` | **Statutory reference data is `PLATFORM`-scoped, versioned and effective-dated; tenant tax configuration is a separate object** | `TX-05`, `SCP-03` |
| `TXP-05` | **No statutory position is adopted without an authoritative citation.** The three closed positions in §1 carry theirs; the seven in §2 do not and remain held | project rule |
