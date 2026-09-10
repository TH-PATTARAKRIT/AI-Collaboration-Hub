# 03 — OUTPUT → CONSUMER RECONCILIATION

## `XMC-H × SA03 RECONCILED — 4-WAY CLASSIFICATION COMPLETE`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-CORRECTIVE-CLOSURE-001]` · Boss: **SOLE FINAL APPROVER**

> **§6: no unclassified output may pass Pre-Test. Every material output = `A CONSUMED` · `B TERMINAL BY
> DESIGN` · `C EXPLICITLY EXCLUDED` · `D ORPHAN / GAP`.**

---

## 1. The reconciliation `PT04-F-03` said had never been done

**Two registers describe the same subject and were never joined:**

| Register | Unit | Missing-consumer count |
|---|---|---:|
| `XMC-H-01`…`XMC-H-18` (`SA_CORR3_08` §2.5) | cross-module **handoff** | **`1`** — `XMC-H-09` |
| `SA03_OUTPUT_CONSUMER_REGISTER` | **output** | **`3`** + `1` input with no producer |
| **Union** | mixed | **`4` outputs, `1` orphan input** |

**`SC-45` §2 reports *"`XMC-H-09` … the one recorded missing consumer."* That is exact within the `XMC-H`
register and is READ as the total. The union is `4`.**

---

## 2. The four outputs — classified from primary text, one class each

| # | Output | Producer | Consumer | Evidence | **Class** | Ground |
|---:|---|---|---|---|---|---|
| **1** | **Sub-location resolution** | Inventory | none | `SA03` line 54: *"Inventory-internal only … **by design**"*; `SA03` §6: *"**Legitimately internal.** Recorded so the register's zero is a **determination, not an omission**"* | **`B` TERMINAL BY DESIGN** | the source itself classifies it |
| **2** | **Commercial-terms freeze flag** (freezes 8 named line fields) | Sales | none | `SA03` §6: *"a control that changes nothing outside its own module is **either an internal-only concern or an unwired control. SMEsPlus must decide which**; it must not carry it forward unexamined"* | **`D` ORPHAN / GAP** | **the source expressly refuses to classify it.** A binary the register declines to resolve is a gap, not a terminal output |
| **3** | **Remaining-supply record** (partial fulfilment) | Inventory | **none** — *"neither Sales nor Purchase read it"* | `SA03` line 51: *"recorded by Group A as **a genuine non-consumption, not silence**"*; §6: *"commercial *'how much is still coming'* is therefore **re-derived rather than read**"* | **`D` ORPHAN / GAP** | **a fact is produced and the consumer re-derives it independently.** Two sources of one truth is the `E2E-18` defect shape |
| **4** | **`XMC-H-09` Asset → Equipment** | Asset | **none** — *"the Equipment consumer has **no evidenced route**"* | `SA_CORR3_08` §2.5: *"Capitalization evidenced; **derecognition `PARTIAL`**"* | **`D` ORPHAN / GAP** | fails `P5`: *a missing consumer is a defect* |
| — | **Customer-invoice lifecycle state** *(input, not output)* | **none — *"Nobody →"*** | Sales/AR | `SA03` §6 | **`D` ORPHAN / GAP** *(inverted direction)* | a required input with no producer |

### 2.1 Result

| Class | n |
|---|---:|
| `A` CONSUMED | `0` *(of the disputed set; the consumed population is the rest of both registers)* |
| **`B` TERMINAL BY DESIGN** | **`1`** — sub-location resolution |
| `C` EXPLICITLY EXCLUDED | **`0`** |
| **`D` ORPHAN / GAP** | **`3` outputs + `1` orphan input = `4`** |
| **Unclassified** | **`0`** ✔ |

---

## 3. `CC-F-03` — `1` of the `4` is closable now, and `3` are not

| Item | Closable by SMEs Core? | Why |
|---|---|---|
| Sub-location resolution | **CLOSED** — `B` | the register already determined it; this round only recorded the class |
| Commercial-terms freeze flag | **NO** | *"SMEsPlus must decide which"* — internal-only **or** unwired control. **It is a design determination, and `PT-16` §1 counts it among the semantics Functional Design would otherwise invent** |
| Remaining-supply record | **NO** | either Sales/Purchase gain a read, or the re-derivation is ratified as correct. **A determination, not a documentation act** |
| `XMC-H-09` Asset → Equipment | **NO** | the Equipment consumer route **does not exist**; originating it is design |
| Customer-invoice lifecycle state | **NO** | a producer must be assigned |

> **`PT-16` §1 item 2 counted *"4 outputs have no consumer."* After classification the accurate statement
> is: **`1` is terminal by design and closes; `3` outputs plus `1` orphan input remain genuine gaps.**
> **The blocker shrinks from `4` to `4`-with-`1`-closed — it does not disappear.**

---

## 4. Checkpoint

> **`XMC-H` × `SA03` reconciled for the first time — the union is `4`, not the `1` the summary carries ·
> `0` unclassified outputs · `1` closed as `TERMINAL BY DESIGN` on the source's own determination ·
> `3` outputs + `1` orphan input remain `D ORPHAN / GAP`, **each requiring a design determination SMEs
> Core may not make in Pre-Test**.**

