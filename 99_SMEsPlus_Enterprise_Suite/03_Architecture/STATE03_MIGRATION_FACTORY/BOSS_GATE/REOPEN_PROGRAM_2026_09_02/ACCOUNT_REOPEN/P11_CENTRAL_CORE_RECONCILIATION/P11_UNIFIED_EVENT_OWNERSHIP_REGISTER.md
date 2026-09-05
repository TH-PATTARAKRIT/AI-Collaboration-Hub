# P11 — UNIFIED EVENT OWNERSHIP REGISTER

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room
Model 4 of 15. Tests the programme's absolute invariant, event by event.

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. The invariant under test

> `ONE BUSINESS FACT → ONE CANONICAL EVENT → ONE CANONICAL OWNER → ONE ACCOUNTING EFFECT PATH.`
>
> `Consumer/reference modules must not recreate economic effect.`

Four clauses. P11 tests each **separately**, because the evidence shows they fail in different places
and a single pass/fail per event would hide that.

| Clause | Test |
|---|---|
| `C1` one canonical event | Is there exactly one event object for the business fact? |
| `C2` one canonical owner | Is there exactly one process accountable for it? |
| `C3` one accounting effect path | Can the fact reach the ledger by only one route? |
| `C4` no consumer recreation | Can a module that only *reads* this fact produce an economic effect from it? |

---

## 2. The result, stated before the table

> ## `C1` fails for **every** business fact in the register — 44 of 44.
>
> Not sometimes. Always, and for one reason: **there is no accounting-event object** (`UAE-29`,
> `GAP-B02`). Where the event and its representation are the same record, "one canonical event" is
> not a property the system can have or lack — it is a property it cannot express.
>
> `C2` fails for **9 of 44**. `C3` fails for **9 of 44** business facts (11 table rows, 2 of which are
> mechanisms, not members of the 44). `C4` fails for **1 of 44** business facts (3 table rows).
> *Corrected in place `2026-09-05` per `X1-F06`, `X4-F04`, `X1-F05`; the earlier figures were 8 / 11 / 3.*
>
> **`C1`'s universal failure is the finding.** `C2`, `C3` and `C4` are, without exception,
> consequences of it. Closing `UAE-29` is the only move that changes the shape of this table; every
> other remedy treats a symptom.

---

## 3. Ownership register — `C2`, `C3`, `C4` by event

Only the rows that fail at least one of `C2`, `C3`, `C4` are tabulated. The remaining **31** rows satisfy
`C2`–`C4` **and fail `C1` with all the others**; they are listed in §5.

| Event | Owner asserted | `C2` | `C3` | `C4` | Why it fails |
|---|---|---|---|---|---|
| `UBE-06` price difference | **none** | **FAIL** | FAIL | pass | `JT-02` open on price-difference account scope. No process is accountable, and two candidate routes exist (`P01` at bill, Inventory at revaluation) |
| `UBE-08` landed cost | **none** | **FAIL** | **FAIL** | pass | `JT-08` open, **Audit VETO retained**; three incompatible reference behaviours, one a documented failure mode |
| `UBE-11` cost released on delivery | Inventory emits | pass | **FAIL** | pass | `JT-04` `NOT DECIDABLE`. Dispatch and invoice are two different accounting-effect paths for the same fact and the choice is unmade |
| `UBE-16` return cost basis | Inventory emits | pass | **FAIL** | pass | `JT-05` `NOT DECIDABLE`. Original-cost and current-cost bases are two paths |
| `UBE-19` machine time | `P03` | pass | **FAIL** | pass | The cost is computed **twice on two bases** — valuation/ledger at completion, analytic recomputed on every duration change — and **nothing reconciles them** (`SL-13` `08` §5) |
| `UBE-22` production scrap | `P03`+Inventory | **FAIL** | **FAIL** | pass | Loss classification has **no safe default documented**; salvage has no reference concept at all (`R4-F-03`) |
| `UBE-24` absorption variance | **none** | **FAIL** | **FAIL** | pass | No variance mechanism exists in 797 modules (`link 18`) |
| `UBE-27` depreciation absorbed | **contested** | **FAIL** | **FAIL** | pass | `P04` owns the asset; `P03` owns the conversion cost; **`BLK-07` `HOLD` decides which rate basis, and no rule assigns the ownership** |
| `UBE-31` employee expense | `P05` | **FAIL** | — | pass | Producer contract `UNKNOWN — EVIDENCE REQUIRED`; ownership cannot be asserted over an unspecified contract |
| `UBE-36` FX difference on settlement | **the ledger** | **FAIL** | pass | pass | Emitted by reconciliation, not requested. `P06` triggers it, `P08` carries it, **no process owns it**. Account selection `UNK` |
| `UBE-38` cash-basis tax | **the ledger** | **FAIL** | **FAIL** | pass | Emitted by reconciliation; **dated today when its natural period is locked**, so the effect path depends on lock state at run time |
| `UBE-43` analytic attribution | `P09` | pass | pass | **FAIL** | See §4 |
| `UBE-44` deferred release | `P10` | **FAIL** | — | pass | Producer contract `UNKNOWN — EVIDENCE REQUIRED` |
| `UAE-09` classification merge | governance | pass | **FAIL** | **FAIL** | A configuration act **retargets posted items across every process and writes no tracking**. It is an economic effect produced by a maintenance function |
| `UAE-05` re-dating on document-date change | none | **FAIL** | **FAIL** | **FAIL** | A clerical edit in a producing process silently changes period attribution **with no lock configured**. The editor is not the owner of period attribution, and the effect is economic |

**Counts: `C2` FAIL = 8 distinct business facts** (`UBE-06`, `UBE-08`, `UBE-22`, `UBE-24`, `UBE-27`,
`UBE-31`, `UBE-36`, `UBE-38`, `UBE-44` — and `UAE-05` which is not a business fact but a mechanism;
the business-fact count is **9**, corrected here rather than carried). `C3` FAIL = **11**.
`C4` FAIL = **3**.

> **Correction made inside this file rather than propagated.** The §2 headline was drafted as
> "`C2` fails for 8 of 44"; the enumeration in §3 returns **9** business facts. The headline figure
> is wrong and the table is right. This is recorded as `P11-E-01` in
> `P11_RESEARCH_ERROR_AND_REVISION_LOG.md` and is **not** an inherited error — it is this session's
> own, caught by re-deriving the count from the table rather than restating it.
> The corrected line is: **`C2` fails for 9 of 44.**

---

## 4. `C4` — the three consumer-recreation failures

`C4` is the clause most likely to be assumed satisfied, because every domain package asserts its own
ownership boundary correctly. It fails three times, and each failure is invisible from inside a single
domain.

### `C4-01` — Analytic attribution recreates economic effect on correction

`P09` is a **read-only** consumer: budget consumes the ledger, it does not produce entries, and
analytic attribution is *derived from the item's distribution*. But analytic **lines** are derived and
destructible: they are deleted on un-post and regenerated on repost (`SL-01` `06` §3). Regeneration is
an economic effect — the management-accounting subledger after a correction is not the one before it,
and the difference is not recorded anywhere. A consumer's subledger is being **rewritten by a
producer's correction**, with no event and no trace.

`P11-DERIVED, SUPPORTED INTERPRETATION.` Severity: material for `P09`, and it is the reason `P09`'s
apparently safe read-only posture does not make it safe.

### `C4-02` — Classification merge rewrites posted history

`AE-20`: posted items are retargeted, accounts are **deleted by direct statement past the ORM's own
guards**, and **no tracking is written**. A chart-maintenance function — a configuration act, not an
accounting act — produces an economic effect across every process's history. There is no record of any
kind afterwards.

`FACT VERIFIED` at `SL-01` `07` `AE-20` / `EV-004` / `COR-08`, within that package's undeclared root
boundary.

### `C4-03` — Report definitions can be created and shared cross-company

`MCU-04`, `CLOSED — VERIFIED DEFECT`: `account.report` has no company dimension, is targeted by no
record rule in any of 6 roots, and carries full create/write/unlink for the accounting-manager role;
its sibling in the same security file **is** company-scoped. `FC-A1` amplifies: the bound server action
creates a menu, and the menu model has no company field and no record rule either.

This is `C4` failing at the **reporting** layer: a consumer that should only read produces a durable,
cross-company artefact. It is also `T0-04` tenant isolation, which remains `UNRESOLVED`.

---

## 5. Events SATISFYING `C2`, `C3` and `C4`

`UBE-01`…`UBE-05`, `UBE-07`, `UBE-09`, `UBE-10`, `UBE-12`…`UBE-15`, `UBE-17`, `UBE-18`, `UBE-20`,
`UBE-21`, `UBE-23`, `UBE-25`, `UBE-26`, `UBE-28`…`UBE-30`, `UBE-32`…`UBE-35`, `UBE-37`, `UBE-39`…`UBE-42`.

**All of them fail `C1`.** Listing them as "passing" without that sentence would be the exact reporting
defect this programme has corrected four times (`GB-06`): a headline table that contradicts the
disposition beneath it.

---

## 6. Ownership positions P11 asserts

Offered as `DESIGN CANDIDATE`, each traceable to evidence, none decided.

| id | Position | Basis |
|---|---|---|
| `OWN-01` | **Every accounting event has exactly one owning process, named on the event object.** Where the ledger emits an event itself, the ledger is the owner and must be named as such — not left implicit | `UBE-36`, `UBE-38` have no owner today |
| `OWN-02` | **A process that emits an accounting event is a producer for that event, regardless of its primary role.** Reconciliation (`P06`) is a producer. Chart maintenance is a producer. Reporting must not be | `UAE-01`…`UAE-03`, `C4-02`, `C4-03` |
| `OWN-03` | **Period attribution is owned by `P08` alone.** No producing process, and no clerical edit inside one, may move an accounting date | `UAE-04`, `UAE-05` |
| `OWN-04` | **A derived subledger may not be destroyed by a correction in another domain.** Analytic intent survives; analytic lines are rebuilt from it and the rebuild is itself an event | `C4-01` |
| `OWN-05` | **Conversion-cost ownership must be assigned before `BLK-07` is decided, not after.** The rate-basis decision presumes an owner and there is none | `UBE-27` |
| `OWN-06` | **Where two processes both compute the same cost, exactly one is the fact and the other is a report of it** — and the system must be able to prove they agree | `UBE-19`, `SL-13` `08` §5 |
