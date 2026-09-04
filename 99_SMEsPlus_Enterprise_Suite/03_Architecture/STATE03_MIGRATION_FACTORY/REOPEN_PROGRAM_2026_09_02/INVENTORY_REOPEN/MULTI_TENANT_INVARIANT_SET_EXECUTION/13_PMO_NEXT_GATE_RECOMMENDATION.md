# [SMEPLUS-26-09-04-INV-MT-INVARIANT-SET-001]
# 13 — PMO Next Gate Recommendation

Control Level: `/L9999.9999`
Status: `PMO REVIEW COMPLETE — RECOMMENDATION ONLY — NO GATE DECLARED READY OTHER THAN BOSS DECISION — NOT DEVELOPMENT FINAL GATE`

---

## 1. Scope

PMO assesses whether this design package is usable as a controlled input, and recommends the next controlled actions. **PMO recommends. Boss decides.** PMO approves nothing and authorizes no team.

This recommendation **supersedes nothing** in `11_PMO_NEXT_CONTROLLED_ACTION_RECOMMENDATION.md` from the AAS+ / PMO review. Ranks 2 through 12 of that recommendation stand unchanged. This file reports what happened to rank 1 and re-sequences only what rank 1's completion affects.

---

## 2. What Happened To Rank 1

| Rank 1 as commissioned | Result |
|---|---|
| *"Commission the Inventory-side multi-tenant invariant set. `RISK-U03` / `GAP-FS-10`. Lane A. Requires no Boss ruling to begin, and no upstream input."* | **The design and specification half is executed.** The invariant set exists. `RISK-U03` remains open, because the item is the capability and not the specification of it |

**The distinction PMO asks Boss to hold on to.** Rank 1 was ranked first because it *depended on nothing and unblocked the most*. The first half of that is now confirmed by execution: the design required no Boss ruling and no upstream input, and it was completed. The second half was always about the built capability, not the design — and the design has surfaced **three decisions that the built capability does depend on**, which were not visible before the design was attempted.

That is a normal and useful outcome of a design pass, and it is why `AAS-V-02` vetoes implementation start before those three are ruled.

---

## 3. Ranked Recommendations

Ordered by leverage per unit of Boss effort. Each names what it unblocks and what happens if deferred.

### Rank 1 — Rule on the three shape decisions: `MTI-D-01`, `MTI-D-02`, `MTI-D-03`

**Lane D. Boss only. Three rulings, no investigation, and they gate everything downstream of the invariant set.**

These are the cheapest high-value actions available, and they are cheap for the same reason `U-07` and `GAP-FS-19` were: they are decisions, not research.

| Decision | What Boss is choosing | Prepared? |
|---|---|---|
| `MTI-D-01` | Product master scope — tenant-level definitional identity with company attachment, or a company-owned master | **Yes** — both options set out with their costs at `03` §4.2, with a stated recommendation |
| `MTI-D-02` | Authorization granularity — company-only, warehouse-level, or finer. Carried from `RISK-U01` / `U-01` | **Yes** — all three shapes specified at `04` §7 so the ruling can be taken on its merits |
| `MTI-D-03` | Shared-template versus tenant-owned boundary — what a tenant may change. Carried from `GAP-MD-14` | Partially — the mechanism is specified; the boundary content is a product-scope choice |

**Unblocks:** finalisation of the invariant set · `L9-03` and the boundary half of `L9-04` · the `AUTH` shape · segregation of duties becoming designable at all (`L7-09`) · lifting `AAS-V-02`.

**If deferred:** the invariant set stays conditional, implementation stays vetoed, and the context spine — which `MTI-06` makes immutable by design — risks being built in a shape that cannot be changed afterwards.

### Rank 2 — Commission the privileged-bypass path audit

`L9-01`. **Lane A. No ruling needed. Started once and never finished.**

`MTI-18` states the property that no unaudited privileged bypass exists. **It is unverifiable until the path set is enumerated**, and no amount of further design changes that. This is the single largest gap between the specification and any claim about it.

**Unblocks:** `L9-01`'s completeness claim · `MTP-03` · the `EP-W` coverage assertion at `05` · the credibility of `MTI-17`, which is the invariant the whole set rests on.

**If deferred:** `L9-01` can produce per-path results and never a completeness result, and the isolation claim stays qualified permanently.

### Rank 3 — Rule on `C-02`, then commission the movement attempt identity

**Unchanged from the review's rank 2.** `RISK-C02` / `IV-06`. Lane D for the ruling, Lane A for the build.

**Promoted in urgency by this session's evidence, not in rank.** The design makes the interaction concrete: `MTI-41` specifies replay determinism for context, and `09` §3.2 establishes that a replay in a system without an attempt identity produces duplicates whose context is individually correct and collectively wrong — which the `MTI-19` conformance control would report as **no breach**. The two capabilities are more entangled than either register previously showed.

**Unblocks:** handoff element 15 · scenario 22 · six enforcement points at `05` · `MTA-12`.

### Rank 4 — Commission the migration and replay provenance reference

**Unchanged from the review's rank 3.** `GAP-FS-08` / `CN-36`. Lane A.

This session adds one argument for not deferring it further: `MTI-42` prohibits inferring context at migration, and `MTA-21` records that **the prohibition can be stated but the correct act cannot be evidenced** without the provenance reference. A migration that assigns context correctly and cannot prove it afterwards is not auditable, and the opening balance is named in prior evidence as the highest fabrication-risk point in the whole Inventory scope.

### Rank 5 — Route `MTI-D-06` and the `MTI-F-05` compensating control to the Thai panel, with `SME-Q-03` and `SME-Q-02`

**Lane C. No AI may answer any of them.**

The review's rank 4 and rank 5 already require the panel to be constituted and two questions routed. This session adds two more that ride at no additional coordination cost:

- `MTI-D-06` — may a handling unit ever carry two companies' goods, and if not, what concept replaces the practice (`MTA-20`)?
- The `MTI-F-05` compensating control — how does segregation of duties degrade when the only other authorised person is in another company (`MTA-16`, `R4-F-21`)?

**Filling the panel membership remains the precondition and has never been done.**

### Rank 6 — Rule on `MTI-D-04`: whether a sanctioned cross-company read exists

**Lane D. Boss only. An authorisation question before it is a design question.**

`L13-MT-03` sets out why this cannot be left implicit: an isolation design with no sanctioned door produces an unsanctioned one, and `MTA-09` records that the unsanctioned one is export. Ruling that no such grant exists is a perfectly good ruling; leaving it unruled is not.

### Rank 7 — Rule on `MTI-D-05` and route the PDPA scope to Legal

**Lane D then Legal.** `GAP-MD-29` has **zero coverage anywhere in the evidence chain**. `MTI-49` is specified in shape and empty in content, and `MTA-24` is `BLOCKING`. No AI may supply a legal scope.

### Rank 8 — Commission the two L13 items that belong inside rank 1's build

`L13-MT-01` deferred-execution context, and the `MTI-19` conformance control as a first-class deliverable rather than an afterthought.

**Both are small and both are inside the invariant set's own scope.** `L13-MT-01` should be commissioned **with** the implementation, not after it, because retrofitting authority carriage across a deferral boundary is materially harder than building it in.

### Rank 9 — All remaining review recommendations, unchanged

Ranks 3, 4, 6, 7, 8, 9, 10, 11 and 12 of `11_PMO_NEXT_CONTROLLED_ACTION_RECOMMENDATION.md` stand exactly as written: `U-07`, Thai validation, the two reachable leads, `GAP-FS-08`, `C-05`, the two scope rulings, the seven Inventory-owned non-blocked items, register hygiene, and the residual clean-room re-audit. **Nothing in this session supersedes any of them and nothing in this session discharges any of them.**

---

## 4. What PMO Recommends Against

| Action | Why Not |
|---|---|
| **Recording element 10 as supplied** | `AAS-V-01`. It is `specified, not built, not verified`. Recording it as supplied would make ten handoffs appear compliant when zero are |
| **Starting implementation now** | `AAS-V-02`. Three shape decisions are unruled, and the context spine is immutable by design once built |
| **Treating `RISK-U03` as closed** | The item is the capability. **Items closed by this session: 0** |
| **Re-commissioning the invariant set as further research** | It is not a research gap. What remains is three rulings, one audit, and an implementation |
| **Convening the Joint 22-Scenario Cross-Proof** | Still not convenable. `0 of 22` unchanged; elements 14 and 15 still absent; elements 4 and 7 still held |
| **Bundling ranks 2, 3 and 4 above into one commission** | The same error the review corrected at `04` §4. They have different owners, different gating and different reach |
| **Reading `MTI-14` as resolving `R4-F-11`** | It resolves the cross-company half only. Stated four times in the package for this reason |
| **Relying on this package while `C-05` stands** | The containment ruling is outstanding and the exposure was confirmed live by the review. This package inherits that lock |
| **Deferring `MTI-D-04` by not deciding it** | Not deciding is not neutral. The need is met informally by export, which is the worst available outcome |

---

## 5. Gate Readiness

| Gate | Readiness | Reason |
|---|---|---|
| Boss decision on this package | **READY FOR BOSS DECISION** | This package |
| The three shape rulings | **READY FOR BOSS RULING** | Options prepared with costs at `03` §4.2 and `04` §7 |
| Inventory multi-tenant invariant set — design | **SPECIFIED, CONDITIONAL** | Conditional on the three shape rulings |
| Inventory multi-tenant invariant set — capability | **NOT READY** | Not built, not verified. `RISK-U03` open |
| `L9` isolation proofs | **NOT READY — 0 of 8** | Definable, not proven |
| Inventory Final Solution v2.0 | **NOT READY** | 0 of 12 Joint decisions ready; 3 NOT DECIDABLE; 0 of 22 provable |
| Accounting × Inventory Joint Cross-Proof | **NOT CONVENABLE** | Structural preconditions still absent |
| Joint interface artifact | **DOES NOT EXIST** | Mandatory before integrated final freeze; not authored here |
| Team B build readiness | **NOT AUTHORIZED** | Out of scope; `AAS-V-02` in force |
| Team C development | **NOT AUTHORIZED** | Out of scope |
| Merge to canonical branch | **NOT PERFORMED, NOT REQUESTED** | Prohibited without Boss authorization |
| Production or release | **NOT AUTHORIZED** | Out of scope |

**No gate is ready other than Boss decision on this package and the three Boss rulings it prepares.**

---

## 6. PMO Verdict

`NO GATE IN SCOPE IS READY OTHER THAN BOSS DECISION AND THE BOSS RULINGS THIS PACKAGE PREPARES.`

This package is assessed **usable as a controlled input** to Inventory Final Solution v2.0 preparation, subject to the three vetoes at `12` §5, the three shape rulings at rank 1, and every hold carried at `11`.

PMO declares no PASS, no approval, no Team B authorization, no Team C authorization, no development readiness, no merge, no release and no production readiness, and is not empowered to.

**Items closed by this session: 0.**

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
