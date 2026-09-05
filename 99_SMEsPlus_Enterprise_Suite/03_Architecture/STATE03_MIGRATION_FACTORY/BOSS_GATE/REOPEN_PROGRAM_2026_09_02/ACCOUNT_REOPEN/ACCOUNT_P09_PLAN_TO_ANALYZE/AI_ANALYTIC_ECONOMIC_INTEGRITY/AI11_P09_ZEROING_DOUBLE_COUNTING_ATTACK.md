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

## 3. THE INTERACTION — **OVER-CLAIMED IN THE FIRST DRAFT, RE-BASED HERE**

> **An independent reviewer challenged this section and was right to.** The first draft's licensing premise was: *"A machine-hour rate is, in ordinary cost-accounting practice, built to recover the machine's ownership cost — depreciation included."* That is a **general cost-accounting proposition asserted without citation**, imported from outside the evidence base, doing load-bearing work for the package's most quotable paragraph. It is the secondary-source defect class, and it is stated plainly here rather than defended.

**What the source actually shows**, verified by the reviewer with declared positive controls:

- the hourly rate is a **bare scalar** with a one-line description and **no components, no build-up, and no link to any asset or equipment record**;
- across the manufacturing modules — 222 non-test files — the terms for depreciation, amortisation, residual and ownership return **two hits, both meaning by-products**, and the asset model returns **zero**. Positive controls on the same patterns fired in the asset module (431 and 18);
- the reference itself names the cost derived from that rate **three incompatible ways** in three different modules: "machine cost", "Labour", and "Overhead".

**The depreciation-specific form of the masking interaction is therefore NOT SOURCE-SUPPORTED, and is withdrawn.**

### 3.1 The re-based finding — stronger, and source-supported

What the source **does** establish needs no costing-policy premise:

> **The hourly rate is an undifferentiated scalar with no declared composition and no provenance.** Whatever a user folded into it — depreciation, insurance, rent, utilities, maintenance — is attributed to the cost centre with **no traceability back to its origin**. Change tracking records value *changes*, not composition.

Depreciation is one instance of a general untraceability. **Classification: `FACT VERIFIED`** — an improvement on the withdrawn version's `SUPPORTED INTERPRETATION`.

### 3.2 The routing class was also wrong

The first draft routed the firing condition to P03 as `UNRESOLVED — EVIDENCE REQUIRED`, implying deployment data could settle it. **It cannot.** No query can answer *"does this number include depreciation?"* about a scalar with no components and no derivation trail. As routed, P03 was set up to return a zero result that would be misread as a negative finding.

**Corrected class: `NOT DECIDABLE FROM SYSTEM EVIDENCE — COSTING-POLICY DETERMINATION REQUIRED`.** The evidence needed is a policy document or an interview, not data.

### 3.3 The double-count pair was also mis-named

The reviewer contradicted `D-01` as characterised: the machine rate and the labour rate are **complementary in the product's own model and are added**, so their two records are not two attributions of one cost. **The genuine same-rate duplication is elsewhere**: one bridge module creates a second management record with the **same value and same hours** as the work-centre record, against a different allocation. Where the two allocations name the same axis value, the machine cost is attributed **twice**, and one profitability section sums both.

**`D-01` as written: CONTRADICTED. The mechanism it claims: CONFIRMED at a different location.** Firing remains configuration-dependent.

### 3.4 Why this section still matters

A plausible-looking cost-centre total remains the strongest barrier to discovering any of these faults. That observation survives the correction. What does **not** survive is the specific claim that depreciation is the thing hiding inside the rate.

## 4. THE ATTACK MATRIX REQUIRED BY THE DIRECTIVE

| Attack | Result | Class |
|---|---|---|
| **record exists but effect = zero** | **CONFIRMED** — asset depreciation, unconditionally | FACT VERIFIED |
| **double analytic allocation** | **CONFIRMED** — the same allocation applied to two rows of one event | FACT VERIFIED |
| **sign cancellation** | **CONFIRMED** — the negated-balance convention guarantees it for a balanced pair | FACT VERIFIED |
| **symmetric debit/credit cancellation** | **CONFIRMED** — this is the same finding, stated at entry level | FACT VERIFIED |
| **wrong account-type attribution** | **CONFIRMED** — a balance-sheet row produces a cost attribution; there is no account-type test on the creation path | FACT VERIFIED |
| **wrong line eligibility** | **CONFIRMED** — eligibility is by assignment only; see `AI03` | FACT VERIFIED |
| **wrong company attribution** | **ROW RE-OPENED BY CHALLENGE.** The first draft closed it on the strength of a bare universal. A reviewer found an untested path: when an entry is mirrored into a second company, the mirror **keeps exactly the company-less (shared, tenant-level) axis values** and drops the company-scoped ones — so one economic event produces, on **one shared axis value**, two records in **two different companies with opposite signs**, which partially cancel on any tenant-level view. Mechanism **CONFIRMED**; firing requires intercompany rules plus a shared axis value; magnitude **UNRESOLVED** | **re-opened** |
| **duplicate cost object attribution** | **CONFIRMED as mechanism**, but **D-01 was mis-named** — see §3.3. The genuine same-rate duplication is in a bridge module, not in the machine/labour pair | mechanism verified at a corrected location |

## 5. WHAT WOULD DISPROVE THE ZEROING CONCLUSION

Stated in advance, so the challenge phase has a target it can actually hit:

1. an account-type or row-type filter on the **creation** path that excludes balance-sheet rows — would make the corollary vacuous for depreciation;
2. a different sign convention for balance-sheet rows — would break the mirror-image property;
3. an entry structure where the two rows do **not** both receive the allocation;
4. a consumer that treats the analytic ledger as balanced by design and never reports its net as a cost — would make the zero correct rather than defective;
5. real deployed data showing non-zero net cost-centre balances traceable to depreciation.

Points 1–3 are settled negatively in `AI02` and `AI03`. **Point 4 is now settled: the product's declared intent is a margin ledger, not a balanced subledger** (`AI04` §4, corrected) — so the zero is a departure from stated intent, not a design feature. **Point 5 is settled positively and against the first draft: deployed data shows the defect firing at 98.57 % annihilation** (`AI05` §3).

**A sixth route, supplied by challenge:** the record's `category` field could in principle separate the mechanisms. It does not — the field is consumed only as a search grouping and a profitability section split, and **no cost-centre balance surface filters on it**. Recorded so the route is closed rather than unexamined.

## 6. CHECKPOINT

**CP-AI11 — ZEROING / DOUBLE-COUNTING ATTACK COMPLETED.** Both classes confirmed; their interaction identified as a masking effect and routed to P03 as unresolved. Auto-continue.
