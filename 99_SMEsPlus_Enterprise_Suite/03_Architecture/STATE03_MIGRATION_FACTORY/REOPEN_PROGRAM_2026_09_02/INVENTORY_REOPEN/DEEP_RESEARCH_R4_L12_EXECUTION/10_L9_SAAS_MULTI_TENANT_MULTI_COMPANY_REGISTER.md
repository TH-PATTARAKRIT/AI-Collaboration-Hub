# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# 10 — L9 SaaS / Multi-Tenant / Multi-Company Register

Level: `L9 — SaaS / Multi-Tenant / Multi-Company`
Control Level: `/L9999.9999`
Status: `L9 COMPLETE FOR 8/8 MANDATED PROOFS — 0 OF 8 PROVEN — DEEP RESEARCH ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. Headline Position

The L9 requirement is to **prove** eight isolation properties. R4 proves none of them, and says so plainly rather than describing intent as evidence.

The reason is a single, previously recorded, still-unresolved fact:

**`RISK-U03` / `GAP-FS-10` / `U-03` — the Inventory-side multi-tenant invariant set does not exist.** There is a cross-gate SaaS invariant set defined elsewhere in the programme; whether and how it extends to Inventory has never been established. Without that set, there is nothing against which an isolation property could be proven.

R4's contribution at L9 is therefore not a proof. It is three things: it confirms the gap is still open; it supplies two new first-hand structural findings that make the gap more concrete than it was; and it states precisely what would have to exist for each of the eight proofs to be attemptable.

Severity **BLOCKING for any build**. Owner **Boss / SaaS Foundation**. **Lane A — not COGS-gated**, so this is actionable now and is blocked only by not having been commissioned.

---

## 2. Two New Structural Findings

### `R4-F-09` — Location company assignment is optional

`L2-OBS`: a storage location's company assignment is optional in the reference pattern. Company-scoped behaviour is guarded so that it applies only where a company is present, which means a location with no company falls outside company scoping entirely.

Why it matters: `L5-08` — the neutrality of internal movement — and handoff element 9 (`WHICH Warehouse / Location`) both assume a location carries company context. A company-less location breaks both assumptions structurally, not through misconfiguration.

### `R4-F-06` — Traceable identities may be company-less

`L2-OBS`: batch and serial uniqueness is scoped to (identifier, product, company), and records with no company are possible. The reference implementation handles this with a **reactive cross-company duplicate check** — it detects collisions between company-less and company-scoped identities after the fact rather than preventing the condition.

Why it matters: a reactive check is a report, not an isolation guarantee. Handoff element 8 (`WHICH Product / Lot / Serial`) and the entire traceability semantic (`L5-06`) rest on identity uniqueness.

These two findings are structural rather than configurational. They cannot be closed by configuring the system correctly; they require a design decision that company assignment is mandatory, enforced below the application layer.

---

## 3. The Eight Mandated Proofs

### `L9-01` Tenant isolation

| Aspect | Content |
|---|---|
| What must be proven | No tenant can read or write another tenant's stock data under any code path. |
| What exists | Prior evidence records company scoping enforced at the application layer across the core stock concepts, with **no database-layer backstop**, and an audit of privileged bypass paths that was started and **never completed**. |
| What is missing | The invariant set itself (`RISK-U03`); the completed bypass-path audit; any database-layer enforcement. |
| R4 status | **NOT PROVEN.** `IV-08` — one company per record, guaranteed below the application layer, with post-write audit — is the target invariant and it is a design requirement, not an observed property. |

### `L9-02` Company isolation

| Aspect | Content |
|---|---|
| What must be proven | Within a tenant, one company's stock and value cannot leak into another's. |
| What exists | Route-to-rule company consistency **is** genuinely enforced (`L2-OBS`) — a real strength. Location barcode uniqueness is scoped per company. |
| What is missing | Mandatory company assignment on locations (`R4-F-09`) and on traceable identities (`R4-F-06`). |
| R4 status | **NOT PROVEN**, and R4 has now identified two specific structural mechanisms by which it could fail. This is more than earlier rounds had. |

### `L9-03` Branch and location isolation

| Aspect | Content |
|---|---|
| What must be proven | Within a company, rights and visibility can be confined to a warehouse or a storage place where the business requires it. |
| What exists | Nothing established. |
| What is missing | `RISK-U01` / `U-01` — whether user rights can be scoped to a warehouse or storage place — is recorded in prior evidence as *"not merely undesigned — unevidenced either way."* |
| R4 status | **NOT PROVEN and not researched.** R4 flags a Thai-specific consequence: a warehouse is **not** a Thai tax branch (`TH-HOLD-06`, `GAP-MD-15`), so branch isolation for tax purposes and warehouse isolation for operational purposes are two different requirements that must not be conflated by a single mechanism. |

### `L9-04` Shared template versus tenant-owned customization boundary

| Aspect | Content |
|---|---|
| What must be proven | What a tenant may change, what is provisioned from a shared template, and what happens to tenant changes when the template changes. |
| What exists | Nothing decided. `L2-OBS` confirms the underlying hazard: reconfiguring a warehouse causes its operation types, locations and routes to be **re-derived**. |
| What is missing | The boundary itself; `GAP-MD-14` (`SAAS-04` — provisioning-template regeneration risk, switch-off guards, versioning) is **open**. |
| R4 status | **NOT PROVEN.** `IV-15` — configuration versioned with effective dates, never regenerated in place — is the required divergence from the reference behaviour, and R4 confirms the reference behaviour is regeneration. |

### `L9-05` No cross-tenant stock visibility

| Aspect | Content |
|---|---|
| What must be proven | No report, search, aggregate or automated process surfaces another tenant's quantities. |
| What exists | Application-layer scoping. Prior evidence records inherited grouping scope as a specific concern. |
| What is missing | Proof across *derived* surfaces. Balances, forecasts and analytics are computed, and a computation can aggregate across a boundary even where the underlying records are scoped correctly. |
| R4 status | **NOT PROVEN.** R4 adds a requirement earlier rounds did not state explicitly: isolation must be proven on the **derived** surfaces (`INV-M10`, `INV-M11`, `INV-M14`, `INV-M15`), not only on stored records, because `P-03` makes the most-used numbers in the module derived by design. Recorded as `R4-F-22`. |

### `L9-06` No cross-company cost leakage

| Aspect | Content |
|---|---|
| What must be proven | A costing policy, a cost layer or a valuation event belonging to one company cannot influence another's value. |
| What exists | `L2-OBS`: costing method and valuation mode are **company-scoped properties** of the product category — meaning one shared category can legitimately cost differently per company. That is the correct shape. |
| What is missing | Proof that the cost layers themselves, and the retroactive compensation pass that consumes them (`L6-13`), respect the company boundary in every path. |
| R4 status | **NOT PROVEN — and `DEPENDENCY: ACCOUNTING COGS GAP`.** `JT-10` (inter-company transfer treatment) is open, and `GAP-FS-07` — the cross-company transfer path has **never been traced end to end** — remains unresolved. `GAP-MD-20` carried. |

### `L9-07` No hard-coded Thailand-only logic in the SaaS core

| Aspect | Content |
|---|---|
| What must be proven | Thai-specific behaviour lives in a localization layer, not in the core. |
| What exists | The v1.0 design principle `P-08` — Thai business language first — governs *labels*, which is a presentation concern and correctly separable. |
| What is missing | An explicit inventory of which Thai requirements are presentational, which are behavioural, and which are statutory. |
| R4 status | **NOT PROVEN, but low risk and R4 can say why.** Every Thai-specific item in this package is either a naming candidate (presentational, all `UNVALIDATED`) or a statutory `HOLD` routed to the Accounting-Tax track (`TH-HOLD-01` .. `TH-HOLD-09`). **No Thai statutory rule has been admitted into Inventory core logic by any round, including this one.** That is a genuine and deliberate clean-room and architecture strength, and R4 records it as such rather than letting it pass unnoticed. |

### `L9-08` Controlled localization extension points

| Aspect | Content |
|---|---|
| What must be proven | Named, versioned extension points exist where a localization may attach, and nothing else may. |
| What exists | The routing discipline exists — statutory items are consistently routed out of Inventory to the Accounting-Tax track. |
| What is missing | The extension points themselves. Routing an item to another track is a governance act; it is not an architectural extension point. |
| R4 status | **NOT PROVEN.** R4 records the distinction explicitly because it is easy to mistake the governance discipline for architectural readiness. They are different things and only the first exists. |

---

## 4. What Would Make These Proofs Attemptable

R4 states this concretely so the Boss decision has a defined scope rather than an open-ended one.

| Prerequisite | Serves | Lane |
|---|---|---|
| Author the Inventory-side multi-tenant invariant set (`RISK-U03`) | `L9-01`, `L9-02`, `L9-05` | A — not COGS-gated |
| Make company assignment mandatory on locations and traceable identities, enforced below the application layer (`R4-F-09`, `R4-F-06`, `IV-04`, `IV-08`) | `L9-02`, `L9-05` | A |
| Complete the privileged-bypass path audit that was started and never finished | `L9-01` | A |
| Boss scope ruling on warehouse-level and operation-level authorization (`U-01`) | `L9-03` | A — Boss decision |
| Decide the shared-template versus tenant-owned boundary and adopt versioning over regeneration (`IV-15`, `GAP-MD-14`) | `L9-04` | A |
| Trace the cross-company transfer path end to end (`GAP-FS-07`, `GAP-MD-20`) | `L9-06` | B, with a C dependency for the valuation half |
| Inventory the Thai requirements by kind — presentational, behavioural, statutory | `L9-07`, `L9-08` | A |
| Define and version the localization extension points | `L9-08` | A |

**Seven of the eight prerequisites are Lane A.** None of them is blocked by the Accounting COGS Gap. This mirrors the finding at `05` §4 and reinforces it: the isolation work is not waiting on Accounting, it is waiting on commissioning.

---

## 5. L9 Coverage Result

| Measure | Result |
|---|---:|
| Mandated proofs | 8 |
| Given full L9 treatment | 8 |
| **Proofs achieved** | **0** |
| Proofs blocked by a missing invariant set | 5 |
| Proofs blocked by never having been researched | 2 |
| Proofs dependency-locked on the Accounting COGS Gap | 1 (`L9-06`, in part) |
| New structural findings raised by R4 | 3 — `R4-F-06`, `R4-F-09`, `R4-F-22` |
| Items closed by this session | **0** |

R4 does not present zero proofs as a failure of this session. The eight proofs were never achievable at L9 without the invariant set, and the invariant set has been an open Boss item since before this session was authorized. What R4 adds is that the gap is now **specific**: two named structural mechanisms, one named unfinished audit, and an eight-item prerequisite list with lanes attached.

---

## 6. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
