# P10 — DOMAIN ENGINE BOUNDARY RECHECK

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D18`. **No technical code reuse is forced or implied.**

---

## 1. The Distinction Preserved

> Shared **semantics** may exist while each domain engine retains its own **objects, lifecycles, posting patterns and business rules.**

Shared semantics means agreeing what a thing *means*. It does not mean one implementation, one module, or one class hierarchy. Where this document says an element is common, it means the **meaning** is common.

## 2. The Four Domains

| | **Asset depreciation** | **Deferred revenue** | **Deferred expense** | **Accrual** |
|---|---|---|---|---|
| **Object** | An asset — a balance-sheet item with a carrying amount, a residual value and a disposal event | None. Two dates on a journal item | None. Same, direction reversed | None. A transient wizard invocation |
| **Lifecycle** | draft → running → paused → revalued → disposed/closed | none — the source document's lifecycle stands in for it | same | none — created and gone |
| **Posting pattern** | contra-asset accumulation against an expense | liability unwinding into income | asset unwinding into expense | reversing estimate, both legs created together |
| **Business rules** | useful life, prorata, residual, impairment absent, disposal gain/loss | service window, eligibility by account type and direction | same | delivered-not-invoiced position, re-measured at cut-off |
| **Termination** | on **value** — runs until the carrying amount is consumed | on **count** — the window fixes the periods | same | none — a point |
| **Real deployed population** | **669 assets, in one database only**; three of four hold templates only | **zero entries, everywhere** | **zero entries, everywhere** | not enumerated — class `C` |

## 3. What Is Genuinely Common — and at what level

| Element | Common? | At what level | Evidence |
|---------|---------|---------------|----------|
| Allocation convention | **Yes, semantically** | The *meaning* of 30/360 and actual-days is identical across domains. The reference product implements it twice with different normalisation | `FACT VERIFIED` |
| Attribution construction | **Yes** | Two domains independently produce the same shape | `FACT VERIFIED` |
| Correction outcomes — stands / re-derived / catch-up | **Partly** | The three outcomes are common; **which one applies is domain-specific**, and in-flight modification differs by lifecycle rather than by algebra | `SUPPORTED INTERPRETATION` |
| Recognition period as distinct from posting date | **Yes** | Every domain needs it; none has it | `FACT VERIFIED` |
| Termination condition | **NO** | Value versus count. Not reconcilable, and must not be | `FACT VERIFIED` |
| Object and lifecycle | **NO** | Four different objects, four different lifecycles | `FACT VERIFIED` |
| Posting pattern | **NO** | Four different patterns | `FACT VERIFIED` |
| Residue policy | **NO** | Absorb-at-end, force-into-last-period, plug-to-control-account, and refuse — four assertions about who owns a difference | `FACT VERIFIED` |

## 4. The Boundary

**Domain engines keep:** the object · the lifecycle · the posting pattern · the business rules · **the termination condition** · **the residue policy**.

**Semantics may be shared for:** the allocation convention's meaning · the attribution construction rule · the three correction outcomes · the separation of recognition period from posting date.

**The termination condition and the residue policy are the two the recheck confirms must stay domain-owned.** Both were candidates for sharing; both are assertions about accounting, not about arithmetic.

## 5. Deferred Revenue and Deferred Expense Are One Domain

They are the same mechanism with a direction switch, and the reference product implements them as one code path. **They are not two domains and must not be counted as two engines.** Their *settings* are independent per direction, which is a configuration surface, not a domain boundary — and it is the source of the asymmetric-margin risk recorded earlier.

## 6. The Boss's Standing Warning, Re-Applied

> *Never assume asset depreciation and deferred recognition share an implementation merely because both use schedules.*

Honoured, and its converse honoured too. The domains differ on object, lifecycle, posting pattern, termination and residue — **five axes** — and share the meaning of allocation, attribution and correction outcome — **three**. Neither *"they are the same"* nor *"they are wholly different"* is supportable.

## 7. Status

**`DESIGN CANDIDATE`.** Not architecture. Not frozen. Implementation blocked by `AASP-VETO-01`.
