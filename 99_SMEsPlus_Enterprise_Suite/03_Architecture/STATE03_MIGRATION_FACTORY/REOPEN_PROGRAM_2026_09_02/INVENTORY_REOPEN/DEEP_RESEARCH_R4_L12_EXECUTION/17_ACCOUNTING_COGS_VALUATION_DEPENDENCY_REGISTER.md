# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# 17 — Accounting COGS / Valuation Dependency Register

Control Level: `/L9999.9999`
Status: `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`

---

## 1. Purpose

The Boss ruling authorising Inventory v2.0 preparation requires that, before any valuation-related section can be closed or upgraded, the executor holds a **direct evidence link and commit SHA for the Accounting COGS Gap package**. This register discharges that requirement: it states what evidence exists, at which commits, what its own terminal state is, and what consequently remains locked.

The dependency was traced through its full chain rather than assumed from any single branch.

---

## 2. Evidence Chain — Verified This Session

| Package | Branch | HEAD commit | Deliverables | Terminal state |
|---|---|---|---|---|
| COGS Deep Research (`ERPPLUS-142`) | `audit/cogs-deep-research-2026-09-02-001` | `a959327938cc1168c93e1e4a89bd1dcf846871c5` | 37 files | `HOLD / EVIDENCE REQUIRED — COGS MATERIAL UNKNOWN NOT EXHAUSTED` |
| COGS Fact Verification | `research/cogs-fact-verification-2026-09-03-001` | `178cd06f7e9923bb3f876e17664f4833e534833c` | 20 files | `PARTIAL FACT BASELINE — TARGETED EVIDENCE REQUIRED` |
| COGS Targeted Resolution | `research/cogs-targeted-resolution-2026-09-03-001` | `8a90f60b629eea2c1d34b39eb08123f0c16acd97` | 25 files | `PARTIAL RESOLUTION — CONTROLLED DECISIONS REQUIRED` |
| COGS Joint Closure | `audit/cogs-joint-closure-2026-09-03-001` | `13219268caa67a8e9bd32a062a346edc958e78ab` | **4 files — governance container only** | `HOLD — DEPENDENCY EVIDENCE PACKAGE BEING RESTORED` |

### 2.1 Joint Closure — confirmed content-empty for closure deliverables

The Joint Closure branch exists on origin and contains four governance-container files: a session control record, baseline pointers, a resume-blocker register, and a Boss execution authorization. **It contains no joint decision closure document, no joint cross-proof, and no closure verdict.** Its own session control file states that it does not assert Joint Closure is complete and that it only restores the branch-level governance container. A prior package independently corroborates this.

**Consequence: no Joint closure exists to rely upon.** Any downstream claim that the Joint track has closed anything is unsupported.

---

## 3. Correction To A Standing Inventory Risk

The Inventory v2.0 package recorded `RISK-COGS-01`, severity `BLOCKING`, stating that the COGS Deep Research session had **not been executed** and that *"no commit, branch or archived record exists for any of its 37 mandatory deliverables."*

**That statement is now factually superseded.** The package exists at commit `a959327938cc1168c93e1e4a89bd1dcf846871c5` with 37 deliverables, and its own terminal state is a `HOLD`.

R4 records this as correction `R4-D-01`. The correction **does not lift the dependency** — the executed package closes none of the twelve Joint decisions and its terminal state is a hold, not a completion. What changes is the *reason* Inventory is blocked: it is no longer "the research has not been done", it is "the research was done and concluded that the decisions still cannot be closed."

This distinction matters for the Boss decision, because the remedy is different. Commissioning the research again would achieve nothing; the named missing inputs are business-SME input, Thai statutory confirmation, and live reference-instance access.

---

## 4. The Twelve Joint Decisions

All twelve remain **open**. Zero were closed by any of the three executed packages.

| ID | Decision | Status | Inventory area it blocks |
|---|---|---|---|
| `JT-01` | Which concept owns valuation policy | **NOT DECIDABLE** — eight named sub-facts missing, two requiring live-instance access | `INV-M24` category design, `INV-M14` valuation, `GAP-FS-02` |
| `JT-02` | Permitted costing methods and change rules | Open — blocked by an unresolved contradiction on price-difference account scope | Costing-method-to-account mapping; `L6-17` |
| `JT-03` | Continuous versus periodic valuation timing | Open — the reference ERP has **no single stable pattern across versions**, so imitation is not available | Fact emission timing, `INV-F-07` |
| `JT-04` | COGS recognition timing — dispatch or invoice | **NOT DECIDABLE** — `SME-Q-03`, `TH-NEW-01`, two documentation sub-facts | `INV-F-07` delivery flow, `L6-03`, `L6-06`, `L11-02` |
| `JT-05` | Return cost basis | **NOT DECIDABLE** — `SME-Q-02`, `TH-NEW-02`, live FIFO-return test | `INV-F-11` return flow, `L6-05`, `L11-04` |
| `JT-06` | Late supplier bill after period close | Open — **no prior-period attribution mechanism exists in the reference ERP at all**; largely original design work | `INV-F-38`, `L6-15`, `L11-01` |
| `JT-07` | Period close design and snapshot content | Open — depends on `JT-01`, `JT-03`, `JT-04` | `INV-F-23`, `L11-08` |
| `JT-08` | Landed-cost eligibility and posting structure | Open — **Audit VETO concern retained**; three incompatible reference behaviours, one a documented failure mode | `INV-F-14`, `L6-14`, `L11-07` |
| `JT-09` | Work-in-progress recognition timing | Open — conditional on `GAP-FS-19` Manufacturing scope | `L11-03` |
| `JT-10` | Inter-company transfer treatment | Open — Lane B, scoping may proceed | `L9-06`, `L11-09`, `GAP-FS-07` |
| `JT-11` | Opening-balance certification at cutover | Open — Lane B, blocked on `GAP-FS-08` | `INV-F-41`, `L10-01`, `L11-10` |
| `JT-12` | Period lock policy and exception granting | Open — Lane B, mechanism unblocked; late-cost consequence gated via `JT-06` | `INV-F-38` |

---

## 5. The Ten Dependency Areas Named In The Boss Prompt

| # | Area | Status | Governing decision |
|---:|---|---|---|
| 1 | COGS at delivery | **LOCKED** | `JT-04` NOT DECIDABLE |
| 2 | Stock input interim | **LOCKED** | Documented as a pre-version-19 pattern only; whether a periodic posture has an equivalent visibility mechanism is a blocking open item |
| 3 | Stock output interim | **LOCKED** | Same open question on the sale side |
| 4 | Periodic versus perpetual behaviour | **LOCKED** | `JT-03`; no stable reference pattern exists to imitate |
| 5 | Standard, average, FIFO cost behaviour | **LOCKED** | `JT-02`. Average-cost return behaviour is documented; FIFO return behaviour is **community-corroborated only, not primary-documented** |
| 6 | Return cost basis | **LOCKED** | `JT-05` NOT DECIDABLE |
| 7 | Scrap and salvage accounting | **LOCKED** | Configuration-dependent with **no safe default documented**; salvage has **no reference concept at all** (`R4-F-03`) |
| 8 | Landed cost allocation and posting | **LOCKED** | `JT-08`, Audit VETO retained |
| 9 | Period close and late movement handling | **LOCKED** | `JT-06`, `JT-07`. Guard *mechanism* is fixed in v1.0 design and not re-litigated; the late-cost *consequence* is locked |
| 10 | Inventory report to GL reconciliation | **LOCKED**, with one non-blocked disclosure requirement | Holds at the closing boundary, not continuously; the report must disclose which posture it measures |

**Ten of ten dependency areas remain locked.** No area is upgraded by this session.

---

## 6. What R4 Contributed Without Trespassing

R4 is permitted to *study* these areas. It contributed the following, each of which is a fact or a consequence rather than a decision:

1. **Costing method is a company-scoped property of the product category** — a fact that makes `JT-01` load-bearing and quantifies its blast radius.
2. **The category owns reporting, put-away and costing simultaneously** (`R4-F-10`) — the structural root of `GAP-FS-02`.
3. **If the original cost basis is chosen for returns, Inventory must carry per-unit original-cost lineage** — a data-model consequence of `JT-05` that must be understood before the decision, not after.
4. **The financial entry date defaults to the processing date, not the physical event date** — which is why handoff elements 3 and 4 genuinely diverge and cannot be collapsed.
5. **Retroactive cost compensation is sequenced by record creation order, not by effective date** (`R4-F-20`) — escalated to `L13-01`; it means back-dated entry can attribute cost to the wrong period.
6. **Scrap has no salvage concept and no approval state** (`R4-F-03`, `R4-F-04`) — dependency area 7 has no reference pattern to adopt.
7. **Weight- and volume-based landed cost allocation distorts silently** when those product attributes are unmaintained (`R4-F-05`).

None of these decides anything. Each narrows what the Joint session must decide, or warns it of a consequence.

---

## 7. Inventory-Owned Work That Is Not Blocked

Recorded here so the dependency lock is not read as a general stop.

1. Every non-sale stock reduction carries a classification distinguishing it from a sale — this is what prevents the periodic cost-of-sales computation from silently mislabelling scrap, shrinkage, write-down and adjustment.
2. Reversal-to-original linkage on every correction.
3. Physical event date and entry date carried as two distinct values.
4. Landed cost allocation statement inspectable **before** validation, stating base, basis, per-line amount, and which goods were on hand versus gone.
5. Quantity-side cutover reconciliation, certifiable independently of the value side (`R4-F-25`).
6. An independent check that internal-to-internal movements net to zero value effect (`R4-F-18`).
7. Movement history with an explicitly stated ordering rule (`R4-F-08`).

---

## 8. Explicit Constraints On This Session

Recorded verbatim in effect, from the packages that impose them:

- Inventory v2.0 finalization is **HOLD** and **NOT READY** in three separate packages.
- No gate in the Targeted Resolution package's scope is ready.
- Merge into the canonical branch is prohibited without Boss authorization.
- **No AI may answer `SME-Q-03` on behalf of the business.** R4 has not attempted to.
- The upstream branches remain authoritative for their own evidence and must not have their findings rewritten. R4 has cited them and rewritten nothing.
- `JT-01`, `JT-04` and `JT-05` specifically block Inventory v2.0 category design, COGS-gap dependency resolution, and return-flow finalization respectively.

---

## 9. Terminal Status Of This Register

`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`

Accounting COGS Gap evidence now **exists** and is cited by branch and commit, so this session was not blocked from studying valuation. It is **not resolved**, so no valuation, COGS, landed-cost, period-close, return-cost-basis, scrap-accounting or Inventory-to-ledger conclusion is finalised by this session.

---

## 10. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
