# [SMEPLUS-26-09-04-INV-R4-AAS-PMO-REVIEW-001]
# 09 — Joint Decision Readiness Matrix

Control Level: `/L9999.9999`
Status: `0 OF 12 JOINT DECISIONS READY — 3 FORMALLY NOT DECIDABLE — JOINT CROSS-PROOF NOT CONVENABLE ON ITS OWN TERMS`

---

## 1. What "Ready" Means Here

A Joint decision is **ready** when the Joint session could convene and take it with the inputs that exist today. It is **not decidable** when named inputs are absent and no amount of deliberation supplies them.

R4 records three as formally NOT DECIDABLE. This review tested each against its named missing inputs and confirms the classification.

---

## 2. The Twelve Joint Decisions

| ID | Decision | State | Missing Inputs | Lane | Owner | Ready? | Blocks v2.0 | Blocks DFG |
|---|---|---|---|---|---|---|---|---|
| `JT-01` | Which concept owns valuation policy | **NOT DECIDABLE** | Eight named sub-facts, **two requiring live-instance access** | E | Joint | **No** | **Yes** — `INV-M24` category design | **Yes** |
| `JT-02` | Permitted costing methods and change rules | Open | Blocked by an unresolved contradiction on price-difference account scope | E | Joint | No | Yes | Yes |
| `JT-03` | Continuous vs periodic valuation timing | Open | **No single stable reference pattern exists across versions — imitation is not available** | E | Joint | No | Yes | Yes |
| `JT-04` | COGS recognition timing — dispatch or invoice | **NOT DECIDABLE** | `SME-Q-03`, `TH-NEW-01`, two documentation sub-facts | E + C | Joint + Business SME | **No** | **Yes** — delivery flow | **Yes** |
| `JT-05` | Return cost basis | **NOT DECIDABLE** | `SME-Q-02`, `TH-NEW-02`, live FIFO-return test | E + C | Joint + Business SME | **No** | **Yes** — return flow | **Yes** |
| `JT-06` | Late supplier bill after period close | Open | **No prior-period attribution mechanism exists in the reference ERP at all** — largely original design work | E | Joint | No | Yes | Yes |
| `JT-07` | Period close design and snapshot content | Open | Depends on `JT-01`, `JT-03`, `JT-04` — two of which are NOT DECIDABLE | E | Joint | No | Yes | Yes |
| `JT-08` | Landed-cost eligibility and posting | Open | **Audit VETO concern retained**; three incompatible reference behaviours, one a documented failure mode | E + D | Joint + Audit VETO | No | Yes | Yes |
| `JT-09` | Work-in-progress recognition timing | Open | Conditional on `GAP-FS-19` **Manufacturing scope — a Boss ruling** | E + D | Boss then Joint | No | Yes | Yes |
| `JT-10` | Inter-company transfer treatment | Open — scoping may proceed | Path **never traced end to end** (`GAP-FS-07`) | E | Joint | No | Yes | Yes |
| `JT-11` | Opening-balance certification at cutover | Open | Blocked on `GAP-FS-08` — **the provenance reference, rank 3 of `04` §4** | E + A | Joint + Migration | No | Yes | Yes |
| `JT-12` | Period lock policy and exception granting | Open — mechanism unblocked | Late-cost consequence gated via `JT-06` | E | Joint | No | Yes | Yes |

**0 of 12 ready. 12 of 12 open. 0 closed by any of the three executed COGS packages, by R4, or by this review.**

---

## 3. The Decidability Chain

The three NOT DECIDABLE decisions are not independently stuck. They share a structure worth stating, because it identifies the cheapest unblock.

| Input | Feeds | Then Feeds | Character |
|---|---|---|---|
| `SME-Q-03` (Business SME) | `JT-04` | `JT-07` → period close design | **One routed question.** Cheapest unblock in the set |
| `SME-Q-02` (Business SME) | `JT-05` | return flow design | **One routed question** |
| Eight sub-facts, two needing live-instance access | `JT-01` | `JT-07`, and `GAP-FS-02` / `R4-F-10` category triple ownership | Structurally the hardest |
| Boss scope ruling (`GAP-FS-19`) | `JT-09` | manufacturing proof scenario | **A decision, not an investigation** |

`JT-07` sits downstream of `JT-01`, `JT-03` and `JT-04` — two of which are NOT DECIDABLE — so it cannot be reached until those clear.

| Observation | Consequence |
|---|---|
| `JT-04` and `JT-05` are each blocked by a **single Business SME question** plus supporting facts | These are the **cheapest** unblocks in the entire Joint set — one routed question each, no research |
| `JT-01` needs eight sub-facts, **two requiring live-instance access** | Structurally the hardest, and it gates `JT-07` alongside `JT-04` |
| `JT-07` depends on three decisions, two NOT DECIDABLE | Cannot be reached until upstream clears; scheduling it earlier is wasted effort |
| `JT-09` waits on a **Boss scope ruling**, not on evidence | Cheapest of all — a decision, not an investigation |

**`SME-Q-03` is the single highest-leverage routed question in the programme.** It is named in the COGS evidence as the fastest route to narrowing `JT-04`, no AI may answer it, and `JT-04` is a **fork between two different designs, not two variants of one**. Until it is answered, the delivery flow cannot be designed either way.

---

## 4. Can The Joint Cross-Proof Convene?

**No — and the reason is not the Joint decisions.**

This is the point at which `R4-F-16` and the Joint track intersect, and it is easy to state backwards. Stated correctly:

| Step | Finding |
|---|---|
| Suppose every one of `JT-01` .. `JT-12` were resolved tomorrow | |
| Could the 22-scenario cross-proof then be performed? | **No** |
| Why not? | The Inventory-side multi-tenant invariant set (element 10) still would not exist. Element 10 is **unconditional** in both governing Boss controls. See `04` §3 |
| So what is the actual precondition ordering? | **The three structural capabilities are a precondition to the cross-proof being convenable at all.** The Joint decisions determine *what the answers are*; the structural capabilities determine *whether any answer can be proven* |

**The Joint track and the structural capability track are not competing priorities. They are sequential, and the structural track is first.**

Additionally, the convergence rule forbids the alternative shortcut: Accounting and Inventory Final Solutions **must not be independently frozen and reconciled afterward**. The approved sequence is candidate + candidate → joint 22-scenario cross-proof → delta backflow → re-verification → integrated freeze candidate. There is no compliant path that defers the cross-proof.

And the mandatory joint interface artifact — an `ACCOUNTING_INVENTORY_INTERFACE_CONTRACT_AND_CROSS_PROOF` or equivalent — **does not yet exist**. It is required before integrated final freeze. R4 correctly declined to author it, being a single-domain session. This review likewise does not author it and records it as outstanding.

---

## 5. Joint Readiness Verdict

| Gate | Readiness | Reason |
|---|---|---|
| Any individual Joint decision | **NOT READY — 0 of 12** | Three formally NOT DECIDABLE; the rest open with named blockers |
| Joint 22-Scenario Cross-Proof | **NOT CONVENABLE** | 0 of 22 provable; blocked by structural elements **before** any Joint decision applies |
| Joint interface artifact | **DOES NOT EXIST** | Mandatory before integrated final freeze |
| Joint Backbone publication | **NOT READY** | `RISK-N-A12-01`, valuation policy owner, period guard consequence, `G-5` all open |
| Inventory Final Solution v2.0 | **NOT READY** | `HOLD` in three separate packages; `JT-01`, `JT-04`, `JT-05` NOT DECIDABLE |

**Nothing in this matrix is closed by this review.**

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
