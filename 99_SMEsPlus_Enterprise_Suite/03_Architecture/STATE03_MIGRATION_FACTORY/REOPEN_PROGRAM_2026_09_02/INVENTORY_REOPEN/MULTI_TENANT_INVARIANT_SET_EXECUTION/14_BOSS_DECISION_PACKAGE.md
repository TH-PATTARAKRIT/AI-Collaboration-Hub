# [SMEPLUS-26-09-04-INV-MT-INVARIANT-SET-001]
# 14 — Boss Decision Package

Project: `SMEsPlus ENTERPRISE SUITE`
STATE: `STATE03 — Architecture`
Jira: `ERPPLUS-139`
Execution Branch: `design/inventory-multitenant-invariant-set-2026-09-04-001`
Control Level: `/L9999.9999`
Boss: `Sole Final Approver`
Status: `READY FOR BOSS DECISION — INVENTORY MULTI-TENANT INVARIANT SET DESIGN ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. What Boss Authorized, And What This Answers

Boss authorized the Inventory-side multi-tenant invariant set — `RISK-U03` / `GAP-FS-10`, rank 1 of the AAS+ / PMO review — for **design and specification only**.

**Answer: the invariant set has been authored. The gap is not closed, and it was never going to be closed by a design session.**

The artifact that `RISK-U03` records as non-existent now exists: 50 invariants, 9 families, 35 context subjects, 41 functions, 9 handoff contract fields, 30 proof scenarios and 24 registered attacks. What it is not is a built capability, and the difference is the whole content of this package.

---

## 2. The Three Things Boss Should Read First

### 2.1 The result on the numbers is unchanged, and that is the honest headline

| Measure | Before | After |
|---|---:|---:|
| L9 isolation proofs achieved | **0 of 8** | **0 of 8** |
| Boss-approved cross-proof scenarios declarable verified | **0 of 22** | **0 of 22** |
| Material Inventory-to-Accounting handoffs contract-compliant | **0 of 10** | **0 of 10** |
| Joint decisions ready | **0 of 12** | **0 of 12** |
| Prior items closed | — | **0** |

What did change is one thing, and it is stated in the narrowest terms the evidence supports:

> **Handoff element 10 moves from *unsuppliable in principle* to *specified, not built, not verified*.**

Nothing follows from that for any scenario yet. A specification is not evidence, and the Boss-approved contract requires elements to be *known, traceable and evidence-backed*. This is why `AAS-V-01` vetoes any document recording element 10 as supplied.

What also changed, and is worth more than it may look: **all eight L9 proofs become definable for the first time**, with 30 named adversarial scenarios, 27 of which become executable the moment an implementation exists. Before this session there was no proposition to test. The reason `0 of 8` had stood across rounds was not that the tests failed — it is that there was nothing to test.

### 2.2 Designing rank 1 surfaced three decisions only Boss can take

This is the substantive new information in the package. Rank 1 was ranked first because it *depended on nothing*. That was true of the design, and the design was completed without a single upstream input. But attempting it revealed that the **built capability** depends on three decisions that were not visible before:

| Decision | The choice | Why it cannot wait until build |
|---|---|---|
| `MTI-D-01` | Does a product's definitional identity live at tenant level with company-level attachment, or is the master company-owned? | It determines whether a Thai SME group maintains one catalogue or several, and whether inter-company transfer has a natural correlation. Both options are set out with their costs at `03` §4.2 |
| `MTI-D-02` | Is authorization company-only, warehouse-level, or finer? Carried from `RISK-U01` / `U-01` | It determines how many axes the authorization context has. Segregation of duties is **undesignable** until it is ruled. All three shapes are specified so the ruling can be taken on its merits |
| `MTI-D-03` | What may a tenant change, and what stays platform-owned? Carried from `GAP-MD-14` | The mechanism is specified; the boundary is a product-scope choice |

**The context spine is immutable by design once built** — `MTI-06` makes it so deliberately, because a company that can be reassigned re-interprets every movement it ever held. That is why `AAS-V-02` vetoes implementation start before these three are ruled: this is the part of a system that is hardest to change afterwards.

### 2.3 One design position was taken, and it is disclosed rather than buried

`MTI-11` places definitional product identity at tenant level with company-level attachment. **That is a decision with a real trade-off and it belongs to Boss.** The authorization required product and variant visibility to be defined, so a position was taken; it is recorded as `MTI-D-01`, both options are stated with their costs, and every invariant and matrix row that depends on it is marked `CONDITIONAL` rather than settled.

The session's own adversarial challenge upheld this attack (`12` §2, attack 4). It is recorded here because a package that hid it would be worth less than one that names it.

---

## 3. Boss Decision List

Ranked by leverage per unit of Boss effort. Full reasoning at `13` §3.

| # | Decision | Lane | Boss Action Required | If Deferred |
|---:|---|---|---|---|
| **1** | **Rule on `MTI-D-01`** — product master scope | D | One ruling. Options prepared with costs | The invariant set cannot be finalised; six matrix rows and one register entry stay conditional |
| **2** | **Rule on `MTI-D-02`** — authorization granularity (`U-01`) | D | One ruling. All three shapes specified | `L9-03` stays unprovable; segregation of duties stays undesignable |
| **3** | **Rule on `MTI-D-03`** — tenant-changeable boundary (`GAP-MD-14`) | D | One ruling | `L9-04` stays partial; template governance stays undefined |
| **4** | **Commission the privileged-bypass path audit** | A | Commission. **No prior ruling needed** | `MTI-18` stays unverifiable and the isolation claim stays permanently qualified. Started once, never finished |
| **5** | **Rule on `C-02`, then commission the movement attempt identity** | D → A | Rule, then commission | Unchanged from the review's rank 2, with new evidence: context conformance would report **no breach** on a duplicated replay (`09` §3.2) |
| **6** | **Commission the provenance reference** (`GAP-FS-08`) | A | Commission | Unchanged from the review's rank 3, with one addition: `MTI-42` prohibits the wrong migration act but cannot evidence the right one |
| **7** | **Route `MTI-D-06` and the `MTI-F-05` compensating control to the Thai panel** | C | Route, with `SME-Q-03` and `SME-Q-02`. **Fill the panel first** | Two more design questions stay unvalidated at no extra coordination cost if routed together |
| **8** | **Rule on `MTI-D-04`** — whether a sanctioned cross-company read exists | D | One ruling, including "no" | Not deciding is not neutral. The need gets met by export, which is the worst outcome |
| **9** | **Rule on `MTI-D-05`** — PDPA and tenant erasure scope; route to Legal | D | Ruling plus routing | `GAP-MD-29` has **zero coverage anywhere**. Tenant offboarding has no defined boundary |
| **10** | **Commission `L13-MT-01`** with rank 1's implementation, not after it | A | Scope confirmation | Retrofitting authority carriage across a deferral boundary is materially harder than building it in |
| **11** | **All remaining review recommendations, unchanged** | — | As previously tabled | `U-07`, Thai validation, the two reachable leads, `C-05`, the two scope rulings, the seven Inventory-owned items, register hygiene, the residual clean-room re-audit. **None is discharged by this session** |

**This package supplies evidence for each. It decides none of them.**

---

## 4. What Can Proceed Safely After This Package

### 4.1 Can proceed now

| Work | Basis | Why it is safe |
|---|---|---|
| The three shape rulings at decisions 1–3 | Lane D | Decisions, not investigations. Prepared with options and costs |
| The privileged-bypass path audit | Lane A | Needs no ruling; the access was demonstrated by earlier rounds |
| Routing the two new Thai questions with the two already routed | Lane C | Routing is not answering |
| Quantity-side cutover reconciliation, certified **per company** | Lane A | `R4-F-25` extended at `09` §6.1. Still the one item that creates available work rather than blocking it |
| The seven Inventory-owned obligations at `17` §7 | Lane A | Unchanged. Items 1 and 2 remain the highest-leverage |

### 4.2 Cannot proceed

| Work | Why |
|---|---|
| Implementation against this invariant set | `AAS-V-02`. Three shape decisions unruled |
| Recording element 10 as supplied anywhere | `AAS-V-01` |
| Any cross-company valuation view | `AAS-V-03`; `JT-01` **NOT DECIDABLE** |
| Any Team B or Team C activity | Not authorized, in any package in this chain |
| Source code, database or API implementation | Not authorized |
| Freezing Inventory v2.0 | 0 of 12 Joint decisions ready; 3 NOT DECIDABLE |
| Convening the Joint 22-Scenario Cross-Proof | Still not convenable; `0 of 22` unchanged |
| Any downstream reliance on `C-05`-affected material, this package included | Containment ruling outstanding; exposure confirmed live by the review |
| Merge to the canonical branch | Prohibited without Boss authorization. Not performed, not requested |

---

## 5. Verdicts Carried To Boss

| Body | Verdict |
|---|---|
| **AAS+ adversarial challenge** | **`HOLD` — DESIGN SPECIFIED, NOT PROVEN.** 4 of 9 tracks `HOLD`, 5 `CONTINUE_WITH_NOTES`, **0 `FAIL / FROZEN`**. Twelve attacks made on this session's own work: 5 failed, 4 partially succeeded, 2 succeeded, 1 upheld and disclosed |
| **AAS+ vetoes** | **3 issued** — `AAS-V-01` element 10 wording, `AAS-V-02` implementation start, `AAS-V-03` cross-company valuation content. All three are on reliance and sequencing, none on design content |
| **PMO** | `NO GATE IN SCOPE IS READY OTHER THAN BOSS DECISION AND THE BOSS RULINGS THIS PACKAGE PREPARES` |
| **`RISK-U03` / `GAP-FS-10`** | **REMAINS OPEN.** The specification exists; the capability does not |
| **`R4-F-06`, `R4-F-09`, `R4-F-22`** | **All three remain open.** The required divergence is specified for each; closure needs implementation and independent verification |
| **`R4-F-16`** | **Stands.** Element 10's status changes; the finding does not |
| **Accounting COGS dependency** | **`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`** — not lifted, no trespass found |
| **Thai validation** | **`HOLD`** — 0 of 78. Nothing in this package is validated. Two new questions routed |
| **`C-05` / `U-07`** | **Both remain governance blockers.** This package inherits both locks |
| **Clean-room, Layer 1** | Held on this session's own scan: zero vendor tokens, zero code, zero schema, one reference behaviour adopted and disclosed as a positive transfer |

---

## 6. Design Readiness Versus Development Readiness

The authorization requires this distinction to be explicit. It is the single most important line in the package.

| Dimension | Design / specification | Development |
|---|---|---|
| Does the artifact exist? | **Yes** | No |
| Is it complete? | **Conditional** on `MTI-D-01`, `-D-02`, `-D-03` | No |
| Is it validated by a Thai user? | **No** — 0 of 78 | No |
| Is it verified? | **No.** No implementation exists to verify | No |
| Are the acceptance criteria stated? | **Yes** — 30 proof scenarios | — |
| Can any isolation property be proven? | **No.** A proof needs a proposition, an implementation and a test. This session supplies one of three | No |
| Is a build authorized? | **No** — `AAS-V-02` in force | **No** |

`READY FOR BOSS DECISION — INVENTORY MULTI-TENANT INVARIANT SET DESIGN ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 7. Non-Authorization Lock

This package does not declare, and no member of AAS+ or PMO is empowered to declare: `PASS`, `APPROVED`, `CLOSED`, `FINAL SOLUTION ACCEPTED`, `READY FOR DEVELOPMENT`, `READY FOR PRODUCTION`, `TEAM B AUTHORIZED`, `TEAM C AUTHORIZED`, merge approval, or release authorization.

**Prior evidence is preserved. Items closed by this session: 0. All prior identifiers carried unchanged.**

---

## 8. Final Status

`READY FOR BOSS DECISION — INVENTORY MULTI-TENANT INVARIANT SET DESIGN ONLY — NOT DEVELOPMENT FINAL GATE`

Applying additionally to every valuation-related section:

`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
