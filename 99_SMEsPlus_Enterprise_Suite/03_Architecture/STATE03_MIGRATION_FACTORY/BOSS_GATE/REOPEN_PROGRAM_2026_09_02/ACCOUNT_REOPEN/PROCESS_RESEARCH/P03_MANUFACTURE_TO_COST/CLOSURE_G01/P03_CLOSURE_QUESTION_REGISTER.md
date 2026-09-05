# P03 CLOSURE QUESTION REGISTER — G01 BOUNDED-DEEP CLOSURE

**LAYER 2 — AUDIT QUARANTINE.** Prompt `SMEPLUS-26-09-06-G01-P03-M2C-BOUNDED-DEEP-CLOSURE-002`.
Every CQ ends as **exactly one** terminal disposition. No `OPEN`, no `TBD`.

---

## 1. Terminal dispositions

| CQ | Subject | **Terminal disposition** | File |
|---|---|---|---|
| **CQ-P03-01** | P01 purchase/revaluation delta entering manufacturing | **FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE** — it reaches manufacturing only as a changed unit cost, with **no lineage marker of any kind** | `P03_PRICE_DIFFERENCE_TO_MFG_TRACE.md` |
| **CQ-P03-02** | Stock valuation-layer filter chain | **FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE** — 3 participants in series 16 (P01) and 18 (P03); **0 manufacturing participants in either**; restructured by 19 | `P03_STOCK_VALUATION_LAYER_FILTER_CHAIN.md` |
| **CQ-P03-03** | RM → WIP → Semi/FG → COGS propagation | **FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE** — propagates at consumption; **no lineage**; unbuild does **not** reverse the same economic effect | `P03_RM_WIP_FG_COGS_CAUSAL_TRACE.md` |
| **CQ-P03-04** | `P03R-F-01` subsidiary vs GL divergence | **EXTERNAL / CROSS-PROCESS OWNER — HANDOFF PUBLISHED** — origin **P01-owned**; amplification and blast radius **P03-owned, FACT VERIFIED**; sane-GL mechanism **UNRESOLVED** | `P03_VALUATION_GL_DIVERGENCE_CLOSURE.md` |
| **CQ-P03-05** | Fixed-overhead injection boundary | **FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE** for the **measured** claim; the **source** claim is bounded to series 18/19 (`CC-04`) | `P03_FIXED_OVERHEAD_INJECTION_MATRIX.md` |
| **CQ-P03-06** | Operation → Equipment → Cost causality | **FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE** — Operation→WorkCentre proven; Operation→Equipment **proven absent**; no equipment cost enters MO/WIP/FG in 4 deployments | `P03_EQUIPMENT_OPERATION_COST_CAUSALITY.md` |
| **CQ-P03-07** | Work-centre rate / valuation-policy reachability | **FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE** — cause is **configuration separation**, denominator 4 databases, one a 32-line test system | `P03_WORKCENTER_VALUATION_REACHABILITY.md` |
| **CQ-P03-08** | Scope ownership | **FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE**; analytic-plan row **EXTERNAL (P09)**; `SCOPE-Q-02` **UNRESOLVED** | `P03_SCOPE_OWNERSHIP_MATRIX.md` |
| **CQ-P03-09** | Cross-process ownership and handoff | **EXTERNAL / CROSS-PROCESS OWNER — HANDOFF PUBLISHED** — P08, P11, Asset, Inventory | `P03_TO_P08_HANDOFF.md`, `P03_TO_P11_HANDOFF.md` |
| **CQ-P03-10** | Evidence integrity / terminality | **CONTRADICTED — CORRECTED AND CLOSED FOR CURRENT EVIDENCE** — `MD-01`: P03 read series 18 for four rounds against a series-16 deployment. Corrected, bounded, and the source-basis gap declared **UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE** | `P03_DEPLOYED_CODE_IDENTITY_DELTA.md` |

**10 of 10 terminally dispositioned.** Counted from the table: 6 `FACT VERIFIED`,
2 `EXTERNAL / HANDOFF PUBLISHED`, 1 `CONTRADICTED — CORRECTED`, 1 `FACT VERIFIED` with an
internal `EXTERNAL` row. *(CQ-05 and CQ-08 each carry a named sub-item at a different
disposition; both are stated in their own rows.)*

## 2. Derived subquestions — terminal disposition

| ID | Subquestion | Disposition |
|---|---|---|
| `MD-01` | P03's source basis vs the deployment | **UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE.** No series-16 tree in a fully enumerated path set with a working positive control |
| `MD-02` | How much does the mismatch damage the findings? | **FACT VERIFIED** — per-finding classification in `P03_DEPLOYED_CODE_IDENTITY_DELTA.md` §3 |
| `MD-03` | Does manufacturing participate in the filter chain? | **FACT VERIFIED — NO**, in both available series |
| `MD-04` | Undeclared volume `/Volumes/iMac` | **FACT VERIFIED** — real omission, **material effect nil** |
| `MD-05` | Manifest `'version'` as a discriminator | **CONTRADICTED** — every manifest reads `1.0`; instrument failed and is reported as failed |
| `MD-06` | P01's series-16 root does not resolve here | **OUT OF SCOPE — ROUTED WITH EVIDENCE** to P01 |
| P01's kit question, part 1 | Is the "manual" correction a defined procedure? | **FACT VERIFIED — NO.** A two-line docstring; no procedure, wizard, report, flag or reconciliation surface |
| P01's kit question, part 2 | Does the kit price difference reach RM/WIP/FG? | **UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE.** No kit has ever been purchased; cannot be constructed read-only |
| `DEP-06` | Series-18 FIFO/average bill-difference path | **UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE** — no deployment exercises it (P01 concurs) |
| `SCOPE-02` | Work-centre rate on a nullable company | **BOSS/P11 — mechanism FACT VERIFIED, incidence 0 of 60, severity High→Medium, OPEN for P11** |
| `UNR-P03-10` | Which deployment is the migration target? | **BOSS DECISION REQUIRED — DECISION PACKAGE READY** |
| `UNR-P03-18` | Company-dependent valuation fallback not read from `ir_default` | **UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE** — E4/E3 dissent, preserved |

## 3. What changed status during this closure

| Item | Was | Now |
|---|---|---|
| `P03R-F-01` ownership | P03 investigating as amplifier; P01 had routed it to P03 as **owner** | **P01 withdrew the routing.** Origin P01-owned; **both sessions independently reached the same attribution** |
| `P03R-F-01` origin mechanism | P03's "vendor receipt/bill revaluation" | **Named to the function by P01** — and marked **inherited, not verified** (`CC-01`) |
| Source basis of the whole package | assumed series 18 | **series 16 deployment, series 18 source** — `MD-01` |
| Fixed-overhead conclusion | one claim | **two claims** with different evidence bases (`CC-04`) |
| Series-19 filter chain | "removed" | **restructured** (`CC-02`) |
| Chain corroboration | "independent" | **pattern-bounded**, two trees one probe (`CC-03`) |
