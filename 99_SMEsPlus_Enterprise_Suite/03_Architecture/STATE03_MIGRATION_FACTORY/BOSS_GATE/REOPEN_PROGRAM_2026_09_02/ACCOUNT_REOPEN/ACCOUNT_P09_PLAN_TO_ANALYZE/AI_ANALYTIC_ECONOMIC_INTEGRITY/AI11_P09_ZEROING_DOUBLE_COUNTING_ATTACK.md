# AI11 — P09_ZEROING_DOUBLE_COUNTING_ATTACK

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · continuation `…ANALYTIC-ECONOMIC-INTEGRITY-001`
**Layer:** 1 — clean-room.

Two opposite failure classes are tested **together**, because the directive requires it and because — as this document establishes — they interact.

---

## 1. CLASS A — ZEROING: A VALID ECONOMIC COST EXISTS AND THE ATTRIBUTION CANCELS

| ID | Mechanism | Status |
|---|---|---|
| **Z-01** | asset depreciation allocates both legs of a balanced pair; net attribution zero, gross double | **FACT VERIFIED**, unconditional (`AI02` Corollary 1, `AI04`) |
| **Z-02** | the deferred-expense and deferred-revenue variants of the same mechanism share the two-row, both-legs shape | **FACT VERIFIED** for the shape; per-variant confirmation in `AI07` |
| **Z-03** | any future event type that assigns one allocation to a whole entry inherits the same arithmetic | **SUPPORTED INTERPRETATION** — a property of the algebra, not of a specific event |
| **Z-04** | a management record whose net contribution is nil is indistinguishable from a meaningful one | **FACT VERIFIED** (`EC-59`) |

**Detection difficulty.** Zeroing is invisible to every control the reference pattern has: the ledger balances, the entry is balanced, both management records exist and are individually well-formed, the allocation totals 100 %, the company is consistent, and the axis is valid. **Nothing is malformed. The defect is only visible in the sum.**

## 2. CLASS B — DOUBLE COUNTING: ONE ECONOMIC COST ATTRIBUTED THROUGH SEVERAL MECHANISMS

Carried forward from the base package and re-stated here as one register:

| ID | Mechanism | Status |
|---|---|---|
| **D-01** | one work-order duration change produces a work-centre-rate record **and** an employee-rate record, both tagged the same, aggregated by a profitability section that does not distinguish them | mechanism **FACT VERIFIED**; firing is configuration-dependent — **UNRESOLVED, DATA REQUIRED** |
| **D-02** | two budget lines with overlapping windows and complementary blank axis columns each count the **full** amount of the same management record, because a blank axis column is a wildcard | mechanism **FACT VERIFIED**; firing is configuration-dependent |
| **D-03** | the project-to-asset bridge **counts** assets whose allocation mentions a project's axis value, so an asset split across two projects is counted under both — a count, not a partition | reported by P04, **not re-verified by P09** — class **B from P09's position** |
| **D-04** | gross analytic movement is double the economic cost for every symmetric pair — a *presentational* double count on any surface that reports gross | **FACT VERIFIED** (`AI02` Corollary 2) |

## 3. THE INTERACTION — THE FINDING THIS DOCUMENT EXISTS TO PRODUCE

The directive asks specifically about asset depreciation across four mechanisms: financial depreciation, analytic allocation, equipment allocation, and manufacturing/WIP cost injection.

**Financial depreciation** posts the cost to the ledger — correct, and undisturbed by anything here.

**Analytic allocation** attributes it to the cost centre — and nets to **zero** (Z-01).

**Manufacturing cost injection** attributes machine time to the cost centre through the **work centre's hourly cost rate**, as a management record with no journal entry at all.

A machine-hour rate is, in ordinary cost-accounting practice, built to recover the machine's ownership cost — depreciation included. Where that is how the rate was set, the cost centre receives:

```
  from depreciation :   +X  and  −X   →   0
  from machine hours:   the rate × hours, which already contains the depreciation
  ─────────────────────────────────────────────────────────────────────────────
  net on the cost centre:  approximately one depreciation charge
```

**The two defects partially cancel.** A cost centre can show approximately the right total while both contributing mechanisms are wrong: the one designed to attribute depreciation contributes nothing, and the one designed to attribute machine time silently carries the depreciation instead.

**Classification: `SUPPORTED INTERPRETATION`.** The two mechanisms are FACT VERIFIED individually. Whether a given deployment's hourly rate includes depreciation is a **configuration and costing-policy fact**, not a source fact, and it is not decidable from code. Recorded as **`UNRESOLVED — EVIDENCE REQUIRED`** for any specific deployment, and handed to P03.

**Why it matters more than either defect alone.** A plausible-looking total is the strongest possible barrier to discovering either fault. An organisation reconciling its cost centres would find nothing wrong. This is the single most important reason the zeroing defect must not be reported to Boss as "a number is missing" — **the number may well be present, sourced from the wrong mechanism, with no traceability from the cost centre back to the asset.**

## 4. THE ATTACK MATRIX REQUIRED BY THE DIRECTIVE

| Attack | Result | Class |
|---|---|---|
| **record exists but effect = zero** | **CONFIRMED** — asset depreciation, unconditionally | FACT VERIFIED |
| **double analytic allocation** | **CONFIRMED** — the same allocation applied to two rows of one event | FACT VERIFIED |
| **sign cancellation** | **CONFIRMED** — the negated-balance convention guarantees it for a balanced pair | FACT VERIFIED |
| **symmetric debit/credit cancellation** | **CONFIRMED** — this is the same finding, stated at entry level | FACT VERIFIED |
| **wrong account-type attribution** | **CONFIRMED** — a balance-sheet row produces a cost attribution; there is no account-type test on the creation path | FACT VERIFIED |
| **wrong line eligibility** | **CONFIRMED** — eligibility is by assignment only; see `AI03` | FACT VERIFIED |
| **wrong company attribution** | **NOT REACHED BY THIS DEFECT** — a symmetric pair is always within one company (`AI09` §4). The separate company findings in the base package stand unchanged and are independent | not applicable here |
| **duplicate cost object attribution** | **CONFIRMED as mechanism** in three places (D-01, D-02, D-03); firing is configuration-dependent | mechanism verified, firing unresolved |

## 5. WHAT WOULD DISPROVE THE ZEROING CONCLUSION

Stated in advance, so the challenge phase has a target it can actually hit:

1. an account-type or row-type filter on the **creation** path that excludes balance-sheet rows — would make the corollary vacuous for depreciation;
2. a different sign convention for balance-sheet rows — would break the mirror-image property;
3. an entry structure where the two rows do **not** both receive the allocation;
4. a consumer that treats the analytic ledger as balanced by design and never reports its net as a cost — would make the zero correct rather than defective;
5. real deployed data showing non-zero net cost-centre balances traceable to depreciation.

Points 1–3 are settled negatively in `AI02` and `AI03`. Point 4 is **partly true and is why the intent question is routed as a design decision** (`AI04` §4). Point 5 is the subject of `AI05`.

## 6. CHECKPOINT

**CP-AI11 — ZEROING / DOUBLE-COUNTING ATTACK COMPLETED.** Both classes confirmed; their interaction identified as a masking effect and routed to P03 as unresolved. Auto-continue.
