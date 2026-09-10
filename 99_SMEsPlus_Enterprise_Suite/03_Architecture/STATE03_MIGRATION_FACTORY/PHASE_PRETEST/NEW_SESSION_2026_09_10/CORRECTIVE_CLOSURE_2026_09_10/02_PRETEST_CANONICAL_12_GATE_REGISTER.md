# 02 — PRE-TEST CANONICAL 12-GATE REGISTER

# `STATUS = HOLD — CANONICAL SET NOT PROVABLE`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-CORRECTIVE-CLOSURE-001]`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **§5 hard requirement: EXACTLY `12` canonical members explicitly enumerated, or `STATUS = HOLD`.**
> **§5 prohibition: *"Do not invent missing gate membership."* — OBEYED.**

---

## 1. `CC-F-02` — §5 addresses TWO different denominators, and both are `12`

**Before any re-derivation, the instruction itself has to be disambiguated, because conflating these two
would be the exact unit-conflation defect this package has recorded four times.**

| | **Denominator α — BOUNDARIES** | **Denominator β — GATED SCENARIOS** |
|---|---|---|
| What it counts | cross-module **handoff boundaries** | **scenarios** whose test is blocked by a Boss election |
| Value | **`12`** | **`12`** |
| Authority | **`SC-BD-02`** (`XMC-D-02` = extend to all boundaries) | `SA_CORR5_10` `PT` column |
| Fields §5 asks for | *Gate Name · Membership Authority · Entry/Exit Criteria* → **α-shaped** | — |
| §5's cited finding | — | ***`PT10-F-01`*, *"10 WRITABLE / 12 GATED"*** → **β** |
| `PT-16` §11 item | **`B4`** | **`B5`** |

> **§5 names α's fields and β's evidence. They are different populations with different units and they
> are not interchangeable.** **Both are answered below, separately. Neither is reported as the other.**

---

## 2. Denominator α — the `12` boundaries: **NOT PROVABLE**

### 2.1 What authority says

| Source | Says | Enumerates? |
|---|---|---|
| **`SC-BD-02`** §2 | *"not twelve bespoke contracts"* · *"the boundary denominator moves **1 → 12**"* | **NO** |
| **`SC-BD-02`** §7 | *"the denominator is **fixed at 12 boundaries, declared as a set**"* | **NO** |
| **`SC-SMT-09`** (`SC-03`) | *"**1 boundary contracted today → 12** on the recommendation"* | **NO** |
| `SC-01` | *"twelve"* × **4** | **NO** |
| `SC-06` / `SC-10` | *"twelve"* × **1** each | **NO** |

### 2.2 The measurement

**INSTRUMENT:** count of `Asset →` / `Asset ->` (a member appearing in no other context) inside each
authority record. **POSITIVE CONTROL:** `XMC-D-02` in `SC-01` → **`3`** (the instrument reaches these files).

| File | boundary-member occurrences | *"twelve"* |
|---|---:|---:|
| `SC-BD-02_F4_BOSS_RULING.md` | **`0`** | ✓ |
| `SC-01_FINAL_DECISION_SCRUB_REGISTER.md` | **`0`** | `4` |
| `SC-06_BOSS_FINAL_GATE_DELTA_PACK.md` | **`0`** | `1` |
| `SC-10_BOSS_FINAL_GATE_DELTA_PACK_V2.md` | **`0`** | `1` |
| Any `SC-*` continuation record | **`0`** | — |
| Any Pre-Test artefact | **`0`** | — |

> **The Boss-decision chain says *"twelve"* six times and enumerates zero members.**

### 2.3 Where an enumeration DOES exist — and why none of it is authority

| Source | n | Why it cannot serve |
|---|---:|---|
| **CORR3 master prompt §11** | **`12`** | **A PROMPT, not evidence** — and prefixed ***"At minimum test:"***. **A floor is not a denominator.** The token `12` never appears in §11 |
| `SA_CORR3_08` §1.2 | `11` named + `1` in-scope | **A register citing the prompt.** It reports *"the twelve handoff classes master prompt §11 mandates"* — it does not declare them |
| `XMC-H-01`…`XMC-H-18` | **`18`** | the register actually **tested**, *"each exactly once"* — **a different number** |
| CORR4 prompt §4.3 · `SA_CORR4_02` §5 | **`10`** | **different membership** — adds `Purchase → Inventory`, collapses AR/AP/Payment/Bank, **drops `Close →`** |

### 2.4 Determination

> # `HOLD — CANONICAL SET NOT PROVABLE`
>
> **`3` mutually inconsistent enumerations exist (`12` / `18` / `10`), the only 12-member list is in a
> prompt its own author marked *"at minimum"*, and the Boss ruling that fixes the number never declares
> the membership.**
>
> **This register does NOT enumerate a 12-set.** Doing so would mean **transcribing a prompt's floor into
> a Boss-ruled closed denominator** — an authority act SMEs Core does not hold, and the precise thing §5
> forbids.

**Reference candidate list, carried as `PT11-P-01` and NOT adopted here:** Sales→Inventory ·
Sales→Manufacturing · Sales→Purchase · Manufacturing→Inventory · **Inventory→Accounting** · Sales→AR ·
Purchase→AP · Payment→Bank · Asset→Accounting · Expense→Accounting · Tax→reporting · Close→subledgers.

**Boss decision required (`B4`):** adopt this `12` as the declared set · or declare a different set ·
or rule that the denominator is `18` (`XMC-H`) or `10` (`SA_CORR4_02`).

**Blocked until then:** the per-boundary **applicability declaration** (`SC-11` §6 obligation `5`, owner
SMEs Core) — *"a boundary may propose; it may not declare"* — **cannot be written against a set that does
not exist.**

---

## 3. Denominator β — the gated scenarios: **RE-DERIVED**

**Freshly proven per `01_` §3. `10 WRITABLE / 12 GATED` is NOT carried forward.**

| # | Gate ID | Canonical gate name | Declared membership authority | Latest Boss ruling | Latest evidence SHA | State | Open dependencies | Contradictions | Disposition |
|---:|---|---|---|---|---|---|---|---|---|
| β1 | `X-01` | Stockable purchase receipt → handoff | Boss 22-scenario baseline `a1fc7cd6` | **`JT-04` RULED** | `89ba9c7d` | **WRITABLE** | el.`12` bridge not item-matched | — | expected values from `SC-BD-05` |
| β2 | `X-02` | Vendor bill, receipt timing variation | " | **`JT-04` RULED** | `89ba9c7d` | **WRITABLE** | no prior-period attribution mechanism | — | " |
| β3 | `X-03` | Stockable sales delivery → cost handoff | " | **`JT-04` RULED** | `89ba9c7d` | **WRITABLE** | `BP-02` selectability | — | " |
| β4 | `X-04` | Customer invoice, delivery timing variation | " | **`JT-04` RULED** | `89ba9c7d` | **WRITABLE** | — | — | " |
| **β5** | **`X-05`** | **Partial receipt** | " | `JT-04` **RULED**; **over-receipt tolerance default (`B4`) NOT ESTABLISHED** | `89ba9c7d` | **`NOT ESTABLISHED`** | **`F2` ruled `3 of 3` with members unnamed — `CC-F-01`** | **§3.1** | **HOLD** |
| β6 | `X-06` | Partial delivery | " | **`JT-04` RULED** | `89ba9c7d` | **WRITABLE** | `H-05` draft-invoice deletability | — | " |
| β7 | `X-08` | Purchase return | " | **`JT-05` RULED = original cost** | `89ba9c7d` | **WRITABLE** | return basis `PENDING` | — | " |
| β8 | `X-09` | Sales return | " | **`JT-05` RULED** | `89ba9c7d` | **WRITABLE** | `Average`-costing residual → Boss | — | " |
| β9 | `X-10` | Cancellation before physical execution | " | **`XD1-P1` RULED = `BLOCK`** | `SC-BD-07` | **WRITABLE** | `C-01`, `C2-F-01` | — | `M-1`…`M-6` as assertions |
| **β10** | **`X-16`** | **Manufacturing RM → WIP → FG** | " | **`B-6` PARTLY** — `POH-D-06` ruled only | `SC-BD-06` | **`GATED`** | **`POH-D-01` open · `POH-D-02` withheld · veto limb 2 outstanding** | — | **HOLD** |
| **β11** | **`X-17`** | **Manufacturing reversal / scrap / variance** | " | **`B-6` PARTLY** | `SC-BD-06` | **`GATED`** | same | — | **HOLD** |
| β12 | `X-18` | Stockable vs consumable vs service routing | " | **`XMC-D-02` + `XMC-D-01` RULED** | `SC-BD-02`/`-08` | **WRITABLE** | **tie-break undefined — `06_`** | — | routing ruled; classification open |

**The `10` rows already `WRITABLE` at `SA_CORR5_10` are unchanged:** `X-07`, `X-11`, `X-12`, `X-13`,
`X-14`, `X-15`, `X-19`, `X-20`, `X-21`, `X-22`.

### 3.1 Result

| Class | n | Members |
|---|---:|---|
| **`WRITABLE`** | **`19`** | the `10` pre-existing + β1,β2,β3,β4,β6,β7,β8,β9,β12 |
| **`GATED`** | **`2`** | `X-16`, `X-17` |
| **`NOT ESTABLISHED`** | **`1`** | `X-05` |
| Total | **`22`** ✔ | |

> **`10 WRITABLE / 12 GATED` → `19 / 2 / 1`.** **`0 of 22` remain runtime-verified — this moves
> writability, not proof.** Expected values must be taken from the ruling text, not assumed.

---

## 4. Checkpoint

> ## `CHECKPOINT B (part 1) — GATE DENOMINATORS RECONCILED`
>
> **Denominator α (boundaries): `HOLD — CANONICAL SET NOT PROVABLE`. `0` members enumerated by authority,
> `3` inconsistent lists (`12`/`18`/`10`), the only `12` is a prompt floor. **No set invented.** Boss item `B4`** ·
> **Denominator β (gated scenarios): RE-DERIVED `19 / 2 / 1` from per-cell ruling status** ·
> **`CC-F-01` — `F2` ruled `3 of 3` with members unnamed, so `X-05` is `NOT ESTABLISHED`, not assumed** ·
> **`CC-F-02` — §5 addressed two different `12`s; both answered, neither reported as the other.**

