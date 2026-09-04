# [SMEPLUS-26-09-05-INV-MTI-CONTROLLED-REMEDIATION-001]
# 09 — Negative Access Test Specification — Theme 12

Control Level: `/L9999.9999`
Topology Scope: `SHARED SaaS POOL`
Status: `SPECIFICATION COMPLETE — 52 REJECTION CELLS + 8 SUBSTITUTION TESTS = 60 NEGATIVE CASES — 0 EXECUTABLE — 0 EXECUTED`

---

## 1. Theme 12 Is A Form, Not A Section

The authorization records theme 12 as *"Structural — every criterion is a **rejection that must occur**"*. That is correct and it is why theme 12 has no requirement block of its own at `08`: **it is the form every other theme's acceptance criteria are written in.**

This file is the specification of that form. It states what a negative access test is, what counts as passing it, what counts as failing it, and — the part that is easiest to get wrong — **what counts as passing it for the wrong reason.**

> **The expected result is a refusal. A successful operation is a failed proof. An empty result is neither, and is usually the defect.**

---

## 2. The Seven Structural Rules

`N-01` .. `N-03` are carried unchanged from the consolidation's `07` §8. `N-04` .. `N-07` are added by this session and each names its source.

| # | Rule | Why | Source |
|---:|---|---|---|
| `N-01` | **A negative result must be produced by refusal, not by an empty result set.** An empty list derived from a wider query is a filtered leak, not isolation | The wider set was evaluated. Row counts, aggregates, pagination totals and timing all carry information about it | Carried. `RC-P-19`, `MTI-24` |
| `N-02` | **Every refusal is recorded.** A refusal that leaves no trace cannot be distinguished from an attempt that never happened | Without the record, a negative test cannot be shown to have exercised anything | Carried. `MTI-38`, `RC-P-29` |
| `N-03` | **A refusal must not itself disclose.** The refusal text, code, timing and shape must be identical whether the target exists in another context or does not exist at all | **The rule most likely to be violated by a correct implementation**, because a system that correctly refuses cross-context access will naturally produce a different message from one that finds nothing | Carried. `MTI-27`, `RC-P-07` |
| **`N-04`** | **A refusal is an act and emits an event carrying the `CTX` attempted, the `AUTH` found insufficient, and which axis failed.** The event is scoped to the **target's** context, not the attempting actor's | Reconciles `N-02` with `N-03`. If the refusal event were readable by the attempting actor, the event itself would disclose the target's existence — and `N-02` would defeat `N-03` | New. `R-06` at `04` §3; `CF-P-08` |
| **`N-05`** | **Each axis is tested independently and in isolation.** A test that removes two grants at once cannot show which axis refused, and a system enforcing only company would pass it | Four axes means four independent refusals, not one composite one. `MTI-D-02` rules 2 and 3 exist precisely because the composite case hides the individual ones | New. `MTI-D-02` rules 2, 3, 4; `CF-I-01` |
| **`N-06`** | **The negative test set is derived from the *implemented* enumeration, never from a ruling's illustration.** `MTI-D-02` §5's eight operation types are explicitly *"including, but not limited to"* | A test suite built from an illustration proves the illustration | New, extending `RC-P-14`'s published note. `CF-I-05`, `CF-D-02` |
| **`N-07`** | **A refusal must not be reachable by retry, by a second path, or by a privileged path.** Passing on one path is a per-path result, never a completeness result | `L9-01`'s acceptance criterion requires the path enumeration to be **certified complete**, and the bypass-path audit was started and never completed | New, restating the published blocker as a test rule. `MTI-18`, `RC-P-08` |

### 2.1 `N-04` resolves a tension that `N-02` and `N-03` create together

`N-02` requires every refusal to be recorded. `N-03` requires a refusal to disclose nothing. Taken naively the two conflict: a record of *"actor X was refused access to record Y in Company B"* is itself a disclosure of Y's existence to anyone who can read the record.

`N-04` resolves it by scoping: **the refusal event lives in the target's context**, where the target's own company can see it and the attempting actor cannot. The attempting actor receives an indistinguishable refusal and learns nothing; the target's company gains an auditable record of an attempt against it.

**This is a design consequence of applying both carried rules at once, and it is stated rather than left for an implementer to discover.**

---

## 3. The Rejection Matrix — 52 Cells

Four `AUTH` axes × the thirteen enforcement surfaces of the consolidated control model (`04` §5).

**Each cell is one negative case.** `REFUSE` means the act does not execute and `N-01` .. `N-04` all hold. **`0 of 52` are executable today**, because no implementation exists.

| # | Enforcement surface | Cross **tenant** | Cross **company** | Cross **warehouse**, same company | Cross **operation type**, same warehouse |
|---:|---|:---:|:---:|:---:|:---:|
| 1 | UI — search, selection, confirmation | `REFUSE` | `REFUSE` | `REFUSE` | `REFUSE` |
| 2 | API execution | `REFUSE` | `REFUSE` | `REFUSE` | `REFUSE` |
| 3 | Import | `REFUSE` | `REFUSE` per row | `REFUSE` per row | `REFUSE` per row |
| 4 | Export | `REFUSE` | `REFUSE` unless `XCR-02` | `REFUSE` | `REFUSE` |
| 5 | Scheduler and background execution | `REFUSE` | `REFUSE` | `REFUSE` | `REFUSE` |
| 6 | Report generation | `REFUSE` | `REFUSE` unless `XCR-02` | `REFUSE` | `REFUSE` |
| 7 | Reconciliation views | `REFUSE` | `REFUSE` | `REFUSE` | `REFUSE` |
| 8 | Posting handoff to Accounting | `REFUSE` | `REFUSE` | `REFUSE` | `REFUSE` |
| 9 | Audit trail | `REFUSE` | `REFUSE` | `REFUSE` | `REFUSE` |
| 10 | Valuation views | `REFUSE` | `REFUSE` — **`AAS-V-03`: never permitted by a grant while the COGS Gap stands** | `REFUSE` | `REFUSE` |
| 11 | Replenishment views and scheduler-driven proposals | `REFUSE` | `REFUSE` | `REFUSE` | `REFUSE` |
| 12 | Movement history | `REFUSE` | `REFUSE` unless `XCR-02` | `REFUSE` | `REFUSE` |
| 13 | Landed cost flows | `REFUSE` | `REFUSE` | `REFUSE` | `REFUSE` |

### 3.1 Cell notes that are not uniform

| Cell | Note |
|---|---|
| **Tenant column, all 13** | **No exception exists on any surface.** `MTI-02` and `MTI-25` are absolute: nothing crosses a tenant boundary, including a Cross-Context Report Grant |
| **Company column, surfaces 4, 6, 12** | The only permitted exception is `XCR-02`, which is **`SPECIFIED — CONDITIONAL (MTI-D-04)`** and therefore **not available today**. Until `MTI-D-04` is ruled, these three cells are unconditional refusals in practice |
| **Company column, surface 10** | **Never permitted, grant or no grant.** `AAS-V-03` forbids valuation content on any cross-company view while the COGS Gap stands. `JT-01` **NOT DECIDABLE** |
| **Warehouse column, surfaces 1-13** | `RC-D-01` does **not** affect this column. `MTI-D-02` ruled the warehouse axis; only the **location** axis is unruled |
| **Operation-type column, all 13** | **`N-06` governs the test set.** The set of operation types to iterate is the implemented set, and — under `CF-I-05` — the platform class of each. The class enumeration is `CF-D-02`, **unruled** |
| **Surface 3, import** | Rejection is **per row**, and the rejection is recorded per row. An import that rejects the whole file on one bad row discloses nothing but is a different behaviour and must be specified as such |
| **Surfaces 10 and 13** | **Context carriage is specifiable; every valuation, cost and posting consequence carries `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`.** `JT-08` Audit VETO retained on landed cost |

---

## 4. The Eight Substitution Tests

`CF-I-01` states that no axis substitutes for a wider one. Substitution is a **directed** property and must be tested in both directions on each adjacent pair, which is why there are eight and not four.

| # | Test | Expected |
|---:|---|---|
| `S-01` | An actor with tenant-level authority and no company grant acts in a company | `REFUSE` |
| `S-02` | An actor with a company grant acts in another company of the same tenant | `REFUSE` |
| `S-03` | An actor with company-level authority and **no warehouse grant** acts in a warehouse | **`REFUSE`.** `RC-P-12` — `AUTH` is a subset of a `CTX`, never a superset |
| `S-04` | An actor with a warehouse grant acts in another warehouse of the same company | `REFUSE` |
| `S-05` | An actor with a warehouse grant and **no operation-type grant** performs an operation in that warehouse | `REFUSE` |
| `S-06` | An actor with one operation-type grant performs another operation type in the same warehouse | `REFUSE` |
| `S-07` | An actor with an operation-type grant in one warehouse performs the same operation type in another warehouse | **`REFUSE`.** Operation type does not confer warehouse — `MTI-D-02` rule 4 |
| `S-08` | An actor who **created** a warehouse, operation type, route or rule acts through it without a grant | **`REFUSE`.** `CF-I-04` — defining and acting are separate grants |

`S-01` .. `S-06` are `RC-P-15`'s four directed attempts made explicit and complete. `S-07` and `S-08` are added by this session: `S-07` because `MTI-D-02` rule 4 states a property no published test covers, and `S-08` because `CF-I-04` is new.

---

## 5. What Counts As A Failed Proof

Stated as a closed list, because the most likely outcome of a negative test suite is a system that passes it for the wrong reason.

| # | Observed | Verdict | Why |
|---:|---|---|---|
| 1 | The act succeeds | **FAILED** | The obvious case, and the least common |
| 2 | The act returns an **empty result** rather than refusing | **FAILED** | `N-01`. The wider set was evaluated. This is the most common real defect |
| 3 | The act refuses, and the refusal **differs** in text, code, shape or timing from a not-found refusal | **FAILED** | `N-03`. The refusal is the disclosure |
| 4 | The act refuses and **nothing is recorded** | **FAILED** | `N-02`. Unfalsifiable — indistinguishable from an attempt that never reached the system |
| 5 | The act refuses and the refusal event is **readable by the attempting actor** | **FAILED** | `N-04`. The event discloses what the refusal concealed |
| 6 | The act refuses on the first attempt and succeeds on **retry, a second path, or a privileged path** | **FAILED** | `N-07` |
| 7 | Two axes were removed together and the act refused | **INCONCLUSIVE, recorded as FAILED** | `N-05`. Cannot distinguish four-axis enforcement from company-only enforcement |
| 8 | The suite passes over the **eight illustrated** operation types and no others | **INCONCLUSIVE, recorded as FAILED** | `N-06`. The illustration is not the enumeration |
| 9 | The suite passes on every path the tester knew about | **PER-PATH RESULT, never a completeness result** | `N-07`, `RC-P-08`. **This is the standing condition, not a hypothetical** |
| 10 | The act refuses **correctly** on every cell and every substitution test | **The negative half holds, within the paths tested.** It is not a proof of isolation, and it says nothing about `CTX` conformance, duplicate freedom or authorization conformance, which are independent properties | `08` §9.1 |

---

## 6. What Cannot Be Negatively Tested Today

Recorded because a negative test specification that lists only what it covers implies it covers everything.

| Item | Why not | Register |
|---|---|---|
| That **no path** exists which merges products by attribute similarity | The path set is not enumerated. Any suite tests the paths it knows; `L9-01`'s criterion requires the enumeration to be **certified complete** | `RC-P-08` **`NOT DEFINABLE`**; privileged-bypass audit |
| That a **mapping** asserts correspondence without merging identity | The object does not exist | `RC-P-20`, `RC-P-21` **`NOT DEFINABLE`**; `RC-F-03` |
| That a requirement is correctly classified pool-safe or Private-Company-required | No criteria exist | `RC-P-45` **`NOT DEFINABLE`**; `RC-D-03` |
| That the Private Company topology refuses what the pool refuses | No invariants are written for it | `RC-P-46`, `RC-P-48` **`NOT DEFINABLE`**; `RC-F-07`, `CF-I-08` |
| That a **retry** is distinguishable from a second genuine act | No idempotency identity exists | `RISK-C02`; `RC-P-25` partial, `RC-P-31` not exercisable |
| That a **platform-level** segregation rule refuses correctly | The rule cannot be expressed over a tenant-defined label | `CF-F-04`; `RC-P-16` doubly conditional; `CF-D-02` unruled |
| That an **authorization conformance breach** is detected | The control does not exist | `CF-F-05`; `CF-I-03`, `CF-P-06` |
| That any refusal behaves as a **Thai user** expects | Nothing is validated | `GAP-FS-11`, **`0 of 78`** |
| That any **valuation** view refuses correctly in content | **`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`** | `AAS-V-03`; `JT-01` **NOT DECIDABLE** |

---

## 7. Specification Result

| Measure | Result |
|---|---:|
| Enforcement surfaces | **13** |
| `AUTH` axes | **4** |
| Rejection cells | **52** |
| Substitution tests | **8** |
| **Total negative cases specified** | **60** |
| Structural rules | **7** — `N-01` .. `N-07`, of which **4 carried, 3 new** |
| Failure modes enumerated | **10**, of which **8 are ways to pass for the wrong reason** |
| Cells with a permitted exception | **3** — surfaces 4, 6, 12 in the company column, and only under `XCR-02`, which is **not available** |
| Cells where no exception exists under any grant | **49**, plus surface 10's company cell under `AAS-V-03` |
| **Negative cases executable today** | **0** |
| **Negative cases executed** | **0** |
| Cases that would be **inconclusive even after implementation** | **the whole operation-type column until `CF-D-02` is ruled, and every case until the path set is enumerated** |

**`0 of 60`. No implementation exists, and a completeness claim over any of it additionally requires the privileged-bypass path enumeration, which was started once and never completed.**

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
