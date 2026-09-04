# ACCOUNT WAVE A — FINAL NEGATIVE-CLAIM COMPLIANCE SCAN

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-FC-001` · Layer 1 clean-room
Standard: `DR-NC-01` — **`NO EVIDENCE FOUND` ≠ `FUNCTION DOES NOT EXIST`.**
Scan script: `LAYER2_FC_EVIDENCE/fcscan.sh` — re-runnable, deterministic.

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. Classes

| Class | Meaning |
|---|---|
| `A` | **VERIFIED ABSENCE** — complete enumeration over a declared pattern **and a declared path set**; every member tested |
| `B` | Searched, not answerable from source |
| `C` | **NOT YET SEARCHED** — boundary declared |
| `D` | Residual — a bounded remainder of a closed search |
| `E` | **NO EVIDENCE FOUND** — reported as absence. **Prohibited as a conclusion** |

---

## 2. Machine scan — executed

```
FINAL_CLOSURE            files=6    lines=1170
METHOD_CONVERGENCE_CLOSURE  files=20   lines=4329
METHOD_CONVERGENCE          files=15   lines=2507
```

| Unbounded-negative token | `FC` | `MCC` |
|---|---|---|
| `does not exist` | 1 | 10 |
| `there is no` | 5 | 10 |
| `no rule` | 2 | 1 |
| `no constraint` | 0 | 3 |
| `no such` | 0 | 4 |
| `nowhere` | 0 | 4 |
| `impossible` | 0 | 2 |

| Bounding token | `FC` | `MCC` |
|---|---|---|
| `declared pattern` | 8 | 20 |
| `path set` | 16 | 57 |
| `bounded` | 20 | 100 |
| `NOT YET SEARCHED` | 2 | 4 |
| `outside the bound` | **1** | **0** |
| `NEGATIVE-CLAIM` notice | 4 | 6 |

**Density check.** `FC` carries **8 unbounded-negative tokens in 1,170 lines** against **46 bounding
tokens** — a ratio of **5.8 bounding statements per unbounded negative**. `MCC`: 34 against 191, ratio
**5.6**. **The control is being applied at a consistent and adequate density in both packages.**

---

## 3. Prohibited-wording scan — `CLEAN`

Every occurrence in `FC` of a verdict token was read individually:

| Token | Hits | Every hit is |
|---|---|---|
| ` PASS` | 11 | `passes` (plural), *"`CONDITIONAL PASS` **is unavailable**"*, *"a conditional pass … **is a `PASS` with a different label**"* — **all prohibitions or grammar; no verdict** |
| `APPROVED` | 1 | *"**Not declared:** … final approved …"* — a **non**-declaration |
| `FINAL APPROVAL` | 1 | *"**No AI may declare** Final Approval"* — a prohibition |
| `CERTIFIED` | 0 | — |

> **No `PASS`, approval or certification is declared anywhere in this package.**

---

## 4. Every negative claim made by THIS round, classified

| # | Claim | Class | Bound stated |
|---|---|---|---|
| 1 | No `_inherit = 'account.report'` extension declares a `company_id` | **`A`** | 6 roots of 22 — §10 of the `MCU-04` file |
| 2 | No record rule targets `account.report` anywhere | **`A`** | 6 roots of 22 — **explicitly restated as `MCU-22`, class `C`, for the other 16** |
| 3 | No Python `ir.rule` creation names `account.report` | **`A`** | 6 roots |
| 4 | `ir.ui.menu` has no company field and no record rule | **`A`** | ODOO19 root; base model + XML rules |
| 5 | `sum_currency` does not exist in v18 | **`A`** | the complete v18 package, all extensions |
| 6 | The v19 ORM-core aggregator applies no record rule | **`A`** | **Not a search result — a property of the constructed SQL, read directly.** Strongest class of negative available |
| 7 | `Δ1` is absent from 17 of 22 roots | **`A`** | exact-string test, all 22 roots enumerated |
| 8 | 22 reference core roots exist | **`A` over its pattern; NOT a total** | **Stated: a root omitting or relocating `addons/base/models/res_currency.py` is not discovered** |

**Class `E` claims made by this round: `0`.**

---

## 5. `MC-05` — final status: `NOT MET`, and the reason has changed

The parent reason was: *"58.1% of the package has never had the negative-claim control applied"*
(`MCU-12`). `MCC_F` addressed that over the corrected file manifest.

**The reason is now different, and it is structural:**

> ### Every class `A — VERIFIED ABSENCE` in the programme's history is bounded to **at most one
> reference core root of the 22 that exist**, and **not one of them says so.**

A class `A` claim asserts *complete enumeration over a declared pattern and a declared path set*. The
patterns were declared. **The path sets were declared at tree level inside an undeclared root.** Under
`DR-NC-01`'s own definition, a claim whose path set is not fully declared is **not class `A`** — it is
class `A` **relative to an undeclared scope**, which is class `E` wearing class `A`'s label.

**This applies to this round's own claims too**, and §4 states their bound for exactly that reason.
**`FC` is the first package in the programme to quantify the bound rather than assert the class.**

---

## 6. Backlog — carried, not cleared

`MCU-17`'s standing backlog is **unchanged by this round**, which does not edit parent artefacts
(`DR-NC-06`):

| Item | Count | Status |
|---|---|---|
| Contradicted affirmative claims still live in canonical registers, original wording | **7** | **UNCLEARED** |
| Orphan unknown ids with no row | **5** | **UNCLEARED** |
| Unregistered balanced-but-wrong cases | **2** | **UNCLEARED** |
| **`MCC_00` §1 ↔ §2 arithmetic contradiction** | **1** | **NEW — `FC-F1`** |
| `MCC_L` *"prompt NOT COMMITTED"* contradiction | **1** | **NEW — `FC-F5`** |
| Parent findings/corrections not consumed by the AAS+ sibling (`V-SYS-2`) | **≥2 sources** | **NEW, independent** |

**Backlog grew from 14 items to ≥18.** The channel exists; **nothing is draining it.**

---

## 7. Compliance verdict

| Dimension | Verdict |
|---|---|
| This round's own negative claims | **COMPLIANT** — 0 class `E`; every claim bounded; bounds quantified |
| Prohibited verdict wording | **CLEAN** — 0 |
| Control density | **ADEQUATE** — 5.8 bounding statements per unbounded negative |
| **`MC-05` programme-wide** | **`NOT MET`** — every historical class `A` is scoped to ≤1 of 22 roots and none declares it |
| Correction backlog | **NOT CLEARED, and growing** |

> **Cost to move `MC-05` to `MET`: declare the root set once, then re-scope the existing class `A`
> claims to it. The patterns are already written. No new research.**
