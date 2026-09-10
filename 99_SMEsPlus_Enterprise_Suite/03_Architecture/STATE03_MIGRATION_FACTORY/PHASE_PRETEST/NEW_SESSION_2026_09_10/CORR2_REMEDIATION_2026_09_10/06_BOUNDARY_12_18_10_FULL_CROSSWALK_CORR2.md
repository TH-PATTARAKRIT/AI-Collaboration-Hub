# 06 — BOUNDARY `12 ↔ 18 ↔ 10` FULL CROSSWALK · `CORR2`

# `DERIVED · 9 of 10 · 11 of 12 · CORE-07 DISCHARGED AS A MAPPING`

## `CHECKPOINT G`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Baseline: `c91d5840` · Boss: **SOLE FINAL APPROVER**

> **`CORE-07` is executed here as a structural mapping.** A structural crosswalk requires no scope act.
> **Only choosing which granularity is canonical for counting is a scope act, and that is not done here.**

---

## 1. THE THREE POPULATIONS — each read at its own primary source

### The declared `12` — read at the Boss declaration, not at a summary

`22_` §1, **`B4′`**, verbatim: *"DECLARE the proposed 12 explicitly named boundaries as the canonical
Boss-declared closed denominator. **This is a NEW Boss authority declaration; it is NOT treated as
inherited authority from `PT11-P-01`.**"*

```
1  Sales→Inventory              5  Inventory→Accounting        9  Asset→Accounting
2  Sales→Manufacturing          6  Sales→AR/Accounting        10  Expense→Accounting
3  Sales→Purchase (dropship)    7  Purchase→AP/Accounting     11  Tax→Accounting/reporting
4  Manufacturing→Inventory      8  Payment→Bank/Accounting    12  Close→required subledgers
```

**Why declaration was required at all** — `02_` §2 measured the prior state: the chain says *"twelve"*
`6` times and **enumerates `0`**; the only `12`-list was a **prompt floor** marked *"At minimum test:"*.
**A floor is not a denominator.** `B4′` closed the floor into a denominator.

### The `18` — `SA_CORR3_08` L213–230, enumerated in full

```
$ grep -oE 'XMC-H-[0-9]{2}' SA_CORR3_08 | sort -u | wc -l      ->  18
$ sed -n '608p'  "| **Total** | XMC-H-01…XMC-H-18, each exactly once | 18 |"
```

`-01` Sales→Inventory · `-02` Sales→Manufacturing · `-03` Sales→Purchase · `-04` Manufacturing→Inventory ·
`-05` Inventory→Accounting · `-06` Sales→AR/Accounting · `-07` **Purchase→AP/Accounting** ·
`-08` Payment→Bank/Accounting · `-09` Asset→Accounting · `-10` Expense→Accounting ·
`-11` Tax→Accounting/reporting · `-12` Close→all subledgers · `-13` Inventory→Sales and Purchase ·
`-14` Quality→Inventory · `-15` Quality hold→Accounting · `-16` Internal transfer→Accounting ·
`-17` Service/Project performance→Accounting · `-18` Migration/replay→Inventory and Accounting

### The `10` — `SA_CORR4_02` §5, enumerated in full

`1` Sales→Inventory · `2` Sales→Manufacturing · `3` Sales→Purchase/dropship · **`4` Purchase→Inventory** ·
`5` Inventory→Accounting · `6` Manufacturing→Inventory→Accounting · `7` AR/AP→Payment/Bank→Accounting ·
`8` Asset→Accounting · `9` Expense→Accounting · `10` Tax-related handoffs

**Tally at primary source: `2 CONTRACT-SUFFICIENT` (`5`, `10`) · `8 CONTRACT-GAP` · `0` `N/A`.**
`SA_CORR4_02` §5 states its own limit: *"**`CONTRACT-SUFFICIENT` … does not mean built, proven, verified
or compliant.** **`0 of 10`** material handoffs are contract-compliant."*

---

## 2. LEG A — `12 ↔ 18` · **EXACT `1 : 1` ON THE FIRST TWELVE**

| Class | Declared label | `XMC-H` | Label at `SA_CORR3_08` | Match |
|---:|---|---|---|:---:|
| `1` | Sales→Inventory | `-01` | Sales → Inventory | **✓** |
| `2` | Sales→Manufacturing | `-02` | Sales → Manufacturing | **✓** |
| `3` | Sales→Purchase (dropship) | `-03` | Sales → Purchase (dropship/MTO) | **✓** |
| `4` | Manufacturing→Inventory | `-04` | Manufacturing → Inventory | **✓** |
| `5` | Inventory→Accounting | `-05` | Inventory → Accounting | **✓** |
| `6` | Sales→AR/Accounting | `-06` | Sales → AR / Accounting | **✓** |
| `7` | Purchase→AP/Accounting | `-07` | Purchase → AP / Accounting | **✓** |
| `8` | Payment→Bank/Accounting | `-08` | Payment → Bank / Accounting | **✓** |
| `9` | Asset→Accounting | `-09` | Asset → Accounting | **✓** |
| `10` | Expense→Accounting | `-10` | Expense → Accounting | **✓** |
| `11` | Tax→Accounting/reporting | `-11` | Tax → Accounting / reporting | **✓** |
| `12` | Close→required subledgers | `-12` | Close → all subledgers | **✓** |

**`12 / 12` map, label by label. The declared set is exactly `XMC-H-01`…`-12`.** Independently derived
here; it corroborates Round 1's `T3` rather than inheriting it.

### The `6` outside

| `XMC-H` | Flow | Disposition | Gap-carrying? |
|---|---|---|:---:|
| `-13` | Inventory → Sales and Purchase | `HOLD — EXACT GAP` | **YES** |
| `-14` | Quality → Inventory | `HOLD — EXACT GAP` (*"MATCH on routing; **GAP on the object**"*) | **YES** |
| `-15` | Quality hold → Accounting | `NOT APPLICABLE — EVIDENCE-BACKED` | **conditional — see §4** |
| `-16` | Internal transfer → Accounting | `NOT APPLICABLE — EVIDENCE-BACKED` | **conditional — see §4** |
| `-17` | Service / Project performance → Accounting | `HOLD — EXACT GAP` | **YES** |
| `-18` | Migration / replay → Inventory and Accounting | `HOLD — EXACT GAP`; *"`14` and `15` `NOT SUPPLIABLE`"* | **YES** |

**`4` gap-carrying `XMC-H` rows outside the declared `12`** — the package's published figure, **and it is
correct within the `XMC-H` population.**

---

## 3. LEG B — `12 ↔ 10` · **THE LEG THE PACKAGE DECLINED · DERIVED HERE**

`05_` §4 declined it: *"Mapping them requires a determination about which granularity governs — **a scope
act, not a transcription**."*

**That is true of the *counting* question and not of the *structural* question.** A structural crosswalk
asks *which class does this row touch*. It does not ask *which granularity is canonical*.
**The refusal was right in direction and over-wide in scope.**

| Contract row | Flow | Reaches class | Reaches `XMC-H` | Note |
|---:|---|---|---|---|
| `1` | Sales → Inventory | **`1`** | `-01` | — |
| `2` | Sales → Manufacturing | **`2`** | `-02` | — |
| `3` | Sales → Purchase / dropship | **`3`** | `-03` | — |
| **`4`** | **Purchase → Inventory** | **`NONE`** | **`NONE`** | **§5** |
| `5` | Inventory → Accounting | **`5`** | `-05` | the only row `CONTRACT-SUFFICIENT` with both halves published |
| `6` | Manufacturing → Inventory → Accounting | **`4` and `5`** | `-04`, `-05` | **one row spans two classes** |
| `7` | AR/AP → Payment/Bank → Accounting | **`6`, `7` and `8`** | `-06`, `-07`, `-08` | **one row spans three classes** |
| `8` | Asset → Accounting | **`9`** | `-09` | — |
| `9` | Expense → Accounting | **`10`** | `-10` | — |
| `10` | Tax-related handoffs | **`11`** | `-11` | `CONTRACT-SUFFICIENT` for context; `HOLD` on every statutory element |
| — | — | **class `12` reached by NO row** | `-12` | **§6** |

```
contract rows mapping to ≥1 declared class   9 / 10  = 90.0 %
declared classes reached by ≥1 contract row 11 / 12  = 91.7 %
rows spanning >1 class                       2  (rows 6 and 7)
class:row correspondence                     NOT 1:1 in either direction
```

> **`CORE-07` — the `12 ↔ 18 ↔ 10` mapping — is DISCHARGED as a mapping act.** What remains is not a
> mapping; it is `BOSS-CORR1-01`, an amendment question reserved to `B4′`'s issuer.

---

## 4. THE `N/A` PAIR — `§24` applied

`SA_CORR3_08` §2.6, verbatim: *"**`XMC-H-16` — the `N/A` is evidence-backed and its protection is not.**
… A configuration change that breaks transfer neutrality **silently converts two `NOT APPLICABLE —
EVIDENCE-BACKED` rows into ungoverned postings.** The `N/A` is correct today and is **not durable** —
and **that belongs in the row, not a footnote**."*

```
$ grep -ciE 'durab|configuration change|silently convert'  RECOVERY/05_  ->  0
$ grep -ciE 'durab|configuration change|silently convert'  RECOVERY/10_  ->  0
$ POSITIVE CONTROL — same shape on 28_                                   ->  3   (it fires)
```

**`§24` requires every `N/A` to carry a named item, authority, business reason, phase reason, scope
reason and evidence. These two carry all six *and* a published defeating condition — which the recovery's
canonical registers drop.**

| `N/A` | Supported? | Durable? | `§24` disposition |
|---|---|---|---|
| `XMC-H-15` | **YES** — evidence-backed, reason stated | **NO** — configuration-defeasible | **CONDITIONAL — counts as `UNRESOLVED`, not removed from the denominator** |
| `XMC-H-16` | **YES** | **NO** | **CONDITIONAL — same** |

> **Consequence: *"`4` gap-carrying handoffs outside the declared set"* is a FLOOR, not a count.**
> Under a configuration that breaks transfer neutrality it is **`6`**.

---

## 5. `CORR2-XW-01` — MATERIAL · `Purchase → Inventory`

**The single most fundamental inventory inflow in an ERP — goods receipt against a purchase order — is
in neither the declared `12` nor the tested `18`.**

**Negative proved in three command shapes, with a firing positive control:**

```
shape 1  XMC-H rows matching 'Purchase.*→.*Inventory'                        -> 0
shape 2  all 18 flow labels printed and read individually                    -> absent
shape 3  XMC-H rows with a Purchase origin  -> XMC-H-07 "Purchase → AP / Accounting"  (different target)
POSITIVE CONTROL  shape 1 on 'Sales → Inventory'                             -> 1   (it fires)
CONFIRMATION      the Boss declaration text at 22_ §1 read directly          -> no such class
```

**It is not undocumented — it is `HX-04`** (*"Purchase → Inventory · Expected receipt: product, quantity,
expected date, supplier, price reference"*). `SA_CORR4_02` §5 classifies it **`CONTRACT-GAP`**: *"none
authored by the emitter. `HX-04` is **Inventory's receiving-side row**."*

**The defect is a counting-unit defect, and it must be named precisely:**

| Statement | True? |
|---|---|
| *"`4` gap-carrying handoffs outside the declared boundary set"* | **TRUE — within the `XMC-H` population** |
| the same sentence **declares** that population bound | **FALSE — it does not** |
| gap-carrying flows outside the declared set, **union of both registers** | **`5`** |
| that `5` is a ceiling | **FALSE — §4 makes it a floor of `5`, up to `7`** |

> **`CORE-07` is a Boss-declared precondition to any `B4′` amendment and is scoped to `4`.**
> **This session does NOT amend the denominator.** Evidence only, carried to `13_`.

---

## 6. `CORR2-XW-02` — MATERIAL · declared class `12` is covered by no contract row

**Class `12` (Close → required subledgers/control sources) is reached by none of the `10` contract rows.**
Its `XMC-H` counterpart `-12` is `HOLD — EXACT GAP` on a finding that is structural rather than
incidental: *"**There is no accounting-period object**, and the accounting date is *'silently movable past
a lock'*."*

**Consequence:** `SC-11` §6 #5's per-boundary applicability declaration **can name class `12` as a target
and cannot say which handoff rows cover it, because none do.** `28_` §4 records this as `STILL BLOCKED`
on `BOSS-CORR1-01`. **The crosswalk now supplies the missing measurement behind that block.**

**`CORR2-XW-03` — MODERATE.** `05_` publishes the crosswalk as complete for the legs it derived while
`22_` §1.1 records `CORE-04` as open on the whole `12 ↔ 18 ↔ 10`. **The un-derived leg was the one
carrying both material findings.** This is a second unresolved contradiction for exit condition `16`.

---

## 7. COVERAGE — measured per dimension

| Measure | Denominator | Named membership | Numerator | Coverage | Floor | Verdict |
|---|---:|---|---:|---:|---:|---|
| Declared classes reached by a contract row | `12` | `22_` §1 ✔ | `11` | **`91.7 %`** | `96 %` | **HOLD** |
| Contract rows reaching a declared class | `10` | `SA_CORR4_02` §5 ✔ | `9` | **`90.0 %`** | `96 %` | **HOLD** |
| `XMC-H` rows inside the declared set | `18` | `SA_CORR3_08` ✔ | `12` | **`66.7 %`** | — | measurement |
| `XMC-H` applicable rows contract-sufficient | `16` (`18 − 2` `N/A`) | ✔ | **`0`** | **`0 %`** | `96 %` | **HOLD** |
| Contract rows `CONTRACT-SUFFICIENT` | `10` | ✔ | `2` | **`20.0 %`** | `96 %` | **HOLD** |
| Contract rows **contract-compliant** | `10` | ✔ | **`0`** | **`0 %`** | `96 %` | **HOLD** — stated by `SA_CORR4_02` itself |
| `N/A` rows carrying their defeating condition | `2` | ✔ | **`0`** | **`0 %`** | `100 %` (`ZT-04`) | **HOLD** |

**Every dimension is below its floor. `CORE-07` discharged; `0` denominators amended.**

---

## 8. CHECKPOINT

> ## `CHECKPOINT G — 12 ↔ 18 ↔ 10 COMPLETED`
>
> **`12 ↔ 18` exact `1 : 1`** on `-01`…`-12`, verified label by label at the Boss text ·
> **`12 ↔ 10` DERIVED — `9 of 10` · `11 of 12`**, `2` rows spanning multiple classes ·
> **`CORE-07` DISCHARGED as a mapping act** · `2` MATERIAL findings —
> **`Purchase → Inventory` outside both registers** · **declared class `12` uncovered** ·
> *"`4` outside"* re-characterised as **a floor of `5` under a declared union population, up to `7`** ·
> `3` command shapes and `2` firing positive controls on the decisive negative ·
> **`0` denominators amended — `BOSS-CORR1-01` carries the amendment question.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the sole Final Approver.**
