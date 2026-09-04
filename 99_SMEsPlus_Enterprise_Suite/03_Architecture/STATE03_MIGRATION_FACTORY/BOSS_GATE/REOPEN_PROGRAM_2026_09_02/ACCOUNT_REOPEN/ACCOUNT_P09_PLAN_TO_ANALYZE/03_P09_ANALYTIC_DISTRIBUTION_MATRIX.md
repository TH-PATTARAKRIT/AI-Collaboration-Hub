# P09_ANALYTIC_DISTRIBUTION_MATRIX

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Process:** P09 Plan-to-Analyze
**Layer:** 1 — clean-room. Evidence identifiers resolve in the Layer 2 quarantine.

---

## 1. DENOMINATOR DECLARATION FOR THIS MATRIX

Per the project denominator rule, the four components are declared before the matrix, and none was chosen by the author of the claims the matrix bounds.

- **POPULATION:** every persisted object that can hold an analytic allocation. Selected by the allocation-mixin pattern, not by a hand-written list.
- **PATTERN:** the allocation-mixin inheritance expression, plus three cross-checking patterns (allocation field name, management-record model name, single-value dimension field name). Declared false-negative mode: an object that carries a dimension by a plain relational field rather than by the mixin is **not** selected — and this mode **materialised** (the budget line, row 12 below).
- **PATH SET:** both reference roots. The pattern returns zero in the second root; that is a measured exclusion, not an assumption.
- **UNIT:** one persisted object type. Not one field, not one call site.

**Correction of record:** a first draft of the producer scope in this session used an author-chosen list of 13 module names. An independently tasked reader refused it and returned a 57-module union, narrowed to a 9-module true producer set — **5 producers were missing from the author's list** (COR-P09-01). The matrix below uses the measured populations only.

## 2. MATRIX A — ALLOCATION CARRIERS (who can hold an allocation)

Population: 11 selected by the mixin pattern, plus 1 found by the declared false-negative mode.

| # | Carrier | Kind | Is it a financial row? | Can it be grouped by allocation in reporting? | Owning scope (proposed) |
|---|---|---|---|---|---|
| 1 | ledger row (journal item) | financial | **yes** | yes | COMPANY |
| 2 | bank-reconciliation working row | transient UI | no | no | COMPANY |
| 3 | reconciliation rule | **master data / rule** | no | no | TENANT |
| 4 | sales order line | commercial document | no | no | COMPANY |
| 5 | purchase order line | commercial document | no | **yes** | COMPANY |
| 6 | purchase requisition line | commercial document | no | no | COMPANY |
| 7 | expense | commercial document | no | **yes** | COMPANY |
| 8 | expense split working record | transient wizard | no | no | COMPANY |
| 9 | fixed asset | asset master record | no | **yes** | COMPANY |
| 10 | work centre | **manufacturing master data** | no | no | TENANT or COMPANY — undetermined, see §5 |
| 11 | allocation rule | **rule; the allocation is its payload** | no | no | TENANT |
| 12 | budget line | budget detail | no | n/a — uses a different shape | TENANT or COMPANY |

**Reading of Matrix A:**

- **Only 1 of 12 carriers is a financial row.** The allocation is overwhelmingly a *pre-financial* or *non-financial* annotation that travels toward the ledger. This supports the determination that allocation **annotates** rather than posts (`P09_FINANCIAL_VS_MANAGEMENT_BOUNDARY` M1).
- **3 of 12 are master data or rules** (rows 3, 10, 11). A master-data record carrying an allocation means the allocation is a *default*, not a fact — yet it is stored in the same shape as a fact. Row 11 is the sharpest: the rule's payload is itself an allocation, so a rule and a fact are the same structure.
- **Only 4 of 12 can be grouped by allocation in the reporting layer** (EV-P09-019). Seven carriers hold an allocation that the reporting path cannot aggregate. Whether an alternative path exists for those seven was **not searched** — class C.
- **Row 12 uses an incompatible shape** (EV-P09-020): the budget line carries one relational field per axis rather than an allocation payload, and the bridge between the two shapes is a **stored derived copy** of the allocation on one commercial document — a second source of truth for the same assignment.

**DM-01.** SMEsPlus shall express allocation in **one** shape across every carrier. Two shapes with a derived bridge is a reconciliation liability with no offsetting benefit.

**DM-02.** A default allocation held on master data shall be a distinct object type from an actual allocation held on a transaction. They shall not share a storage shape.

## 3. MATRIX B — ALLOCATION RULE SELECTION

The reference pattern pre-fills an allocation from a rule set. Selection semantics:

| Selector | Empty value means | Evidence |
|---|---|---|
| partner | matches every partner | EV-P09-021 |
| partner category | matches every category | EV-P09-021 |
| company | matches every company | EV-P09-021 |
| account prefix | matches every account | EV-P09-115 |
| product | matches every product | EV-P09-115 |
| product category | matches every category | EV-P09-115 |

**Every selector treats empty as a wildcard.** A rule with all selectors empty matches every transaction in the database.

**Precedence:** declared order first, then **newest record first**; each matching rule contributes only for axes not yet contributed; a rule spanning two axes is skipped entirely if either axis is already filled (EV-P09-022, EV-P09-023).

| Property | Assessment |
|---|---|
| deterministic given a fixed rule set? | yes |
| deterministic given the same *business configuration* entered in a different order? | **no** — creation order breaks ties |
| explainable per row? | **not found in scope** — no record of which rule produced an allocation |
| can two rules disagree? | yes; the later-ordered rule's value wins by dictionary union |

**DM-03.** Rule precedence shall be a declared total order that is a property of the configuration, never of creation order.
**DM-04.** Every pre-filled allocation shall record which rule produced it. Without it, an allocation cannot be explained, re-derived, or corrected at the rule level.
**DM-05.** A rule whose selectors are all empty shall be prohibited, or shall require an explicit "applies to all" declaration.

## 4. MATRIX C — ALLOCATION INTEGRITY

| Property | Reference pattern | Class | SMEsPlus requirement |
|---|---|---|---|
| totals to 100 % | **two independent gates, both of which must be passed for the check to run at all**: the caller must opt in by execution context, **and** the row must be of product display type. Entries with no product-type rows — depreciation among them — are skipped even when the flag is set. No model or storage constraint. | A within the analytic module; the row-type gate verified separately after publication | **DM-06** enforce at the storage layer for every axis **and every row type**; not defeatable by a caller flag or a row-type filter |
| referential integrity to the dimension value | **none** — ids live inside a schemaless payload; dangling references are an expected state and are filtered on read | A | **DM-07** allocation shall be relationally integral |
| scope consistency with the carrier | enforced on the one privileged axis only; structurally unattachable to the payload | A / B | **DM-08** enforce uniformly at the storage layer for every axis |
| residual when under-allocated | none; the remainder is unrepresented | A | **DM-09** named visible residual |
| zero splits | dropped silently, still counted in the total | A | **DM-10** record or adjust; never silent |
| audit of change | **none** on a posted row — not tracked, not hashed, not lock-protected | A on three independent lists | **DM-11** every allocation change is an append-only audited event |

## 5. UNDETERMINED — ROUTED, NOT ASSUMED

**DM-U-01 — Scope of the work-centre carrier (Matrix A row 10).** A work centre carrying a default allocation is master data whose costs are attributable to a legal entity. Whether the object is TENANT-scoped with a company qualifier, or COMPANY-scoped outright, cannot be determined from the analytic evidence alone; it depends on the manufacturing domain's own scope determination.
**Status: `HOLD — SCOPE EVIDENCE REQUIRED` · `PEER DEPENDENCY OPEN — P03 Manufacture-to-Cost, P11 scope reconciliation`.** P09 does not adjudicate it and does not stop for it.

**DM-U-02 — Scope of the budget object (Matrix A row 12).** See `P09_BUDGET_CONTROL_MODEL` §6. Determined *per budget* rather than per model; the record must declare it.

**DM-U-03 — Alternative reporting aggregation for the 7 non-groupable carriers.** Class **C — not searched.** Recorded so that it is not later restated as an absence.

**DM-U-04 — The full set of posting paths that bypass obligation enforcement.** Enumerated by the P04 process and reported to P09. **P09 verified the row-type gate directly from source but did not re-enumerate the call sites**, so this is class **B from P09's position** and is not restated here as a P09 class-A finding.

## 6. TERMINAL STATE

**MATRIX ISSUED AND AMENDED AFTER PUBLICATION. DM-01 … DM-11 ARE PROPOSALS. DM-U-01 … DM-U-04 ARE OPEN. NO GATE MOVED.**
