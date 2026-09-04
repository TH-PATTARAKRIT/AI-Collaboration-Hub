# [SMEPLUS-26-09-04-INV-MT-INVARIANT-SET-001]
# 12 — AAS+ Adversarial Challenge And Verdict

Level: `L12 — adversarial audit challenge and veto`, with `L13+` escalation at §6
Reviewer: `AAS+ — AI Audit SMEsPlus`
Control Level: `/L9999.9999`
Status: `CHALLENGE COMPLETE — CONTROLLING VERDICT: HOLD / DESIGN SPECIFIED, NOT PROVEN — 3 VETOES ISSUED — NO PASS DECLARED`

---

## 1. Standing Rules And Inherited Conditionality

AAS+ may not declare Gate PASS, Boss approval, Team B or Team C authorization, development readiness, merge, release or production. Boss is the sole Final Approver.

**Charter conditionality carried, not resolved.** `U-07` records two competing 9 Veto Council charters, both claiming Boss approval. R4 disclosed the conditionality; the AAS+ / PMO review inherited it; **this session inherits it again**. If Boss rules that the other charter governs, this verdict's structure must be re-run.

**Reliance conditionality carried, not resolved.** The `C-05` containment ruling is outstanding and the review confirmed the exposure live in a fresh clone. Downstream reliance on Inventory evidence — **including this package** — remains locked until Boss rules.

This challenge is adversarial toward its own session first. Confirming one's own design is worth nothing.

---

## 2. Attacks Made On This Session's Own Work

| # | Attack | Outcome |
|---:|---|---|
| 1 | **"This restates the problem as fifty bullet points and calls it a design."** | **Failed.** Each invariant carries an owner, an enforcement layer, a status, and — via `07` — an acceptance criterion expressed as an attempt that must be rejected. Thirty proof scenarios are named. A restatement cannot be violated; these can |
| 2 | **"`STORE`-level enforcement is unimplementable without a schema, and schema is out of scope — so the central invariant is unfalsifiable."** | **Partially succeeded.** `MTI-17` names an obligation whose satisfiability in a chosen technology this session cannot test. Recorded as `MTI-CH-01`. The obligation is still correct — prior evidence records application-layer-only enforcement with no backstop as the actual condition — but **whether it is achievable is a Team B question that is not approached here**, and the package must not be read as having answered it |
| 3 | **"`R4-F-06` and `R4-F-09` have been closed by fiat."** | **Failed.** Both are recorded as open in `03` §3.1, `04` §2.1, `08` and `11` §5. Items closed by this session: **0**. What is supplied is the required divergence, which is what R4 said was missing, not a verification that it holds |
| 4 | **"`MTI-11` takes a product-scope decision that belongs to Boss."** | **Succeeded.** The position is a genuine decision with a material trade-off. It is recorded as decision blocker `MTI-D-01`, both options are set out with their costs, and the invariant's status is `SPECIFIED — CONDITIONAL`. **The attack is upheld and the remedy is the blocker, not the removal of the position** — the authorization requires product visibility to be defined |
| 5 | **"The Cross-Context Report Grant reintroduces the hole you just closed."** | **Partially succeeded.** It is a deliberate hole. Mitigations: never crosses a tenant; named, scoped, time-bounded and logged per use; no valuation content while the COGS Gap stands (`AAS-V-03`). Residual recorded at `MTA-11`: **every grant mechanism degrades toward permanence**, and no review cadence is designed here. `MTI-D-04` |
| 6 | **"Nothing here moves `0 of 22`, so nothing was unblocked."** | **Failed as stated, upheld in substance.** `0 of 22` is unchanged and is stated as unchanged in four separate files. What changed is element 10's status from *unsuppliable in principle* to *specified, not built, not verified*. That is a real change and a small one, and the package says so rather than presenting it as progress it is not |
| 7 | **"`MTI-14` is presented as fixing the reordering rule conflict."** | **Failed.** `03` §4.4, `04` row 13, `05` §6 and `MTA-14` each state explicitly that `R4-F-11`'s within-company overlap is untouched. The point is made four times because it is the most likely misreading in the package |
| 8 | **"The owner dimension is a new axis introduced without authority."** | **Failed.** It is carried from `L5-07` and from the v1.0 concept model, which already places an owner dimension on the balance. This session states the prohibition on conflating it with company and decides **no** ownership policy; `GAP-MD-09` stays open |
| 9 | **"Fifty invariants is padding — a smaller set would say the same."** | **Failed, with a note.** Families A and C are the load-bearing core; the rest are the anchors and surfaces without which the core is not attachable to anything. `05` demonstrates the attachment across 41 functions. **Note recorded as `MTI-CH-02`:** the set has not been minimised, and a later pass may find genuine redundancy. It has been made complete, which was the more important property here |
| 10 | **"The 30 proof scenarios cannot be run, so they are decoration."** | **Partially succeeded.** 27 of 30 become executable once an implementation exists. **Three cannot be run even then** — `MTP-28`, `MTP-29`, `MTP-30` — and each names its upstream blocker. Recorded as `MTI-CH-03` |
| 11 | **"Context conformance is being sold as isolation."** | **Failed — and the package pre-empts it.** `09` §3.2 states that context conformance and duplicate freedom are independent properties, that neither implies the other, and that this package supplies only the first |
| 12 | **"No Thai validation, so the user-facing half is unfounded."** | **Upheld, and disclosed.** Nothing in this package is Thai-validated. `GAP-FS-11` records 0 of 78 validated, unremedied since 2026-08-30. Two items here depend directly on Thai input — `MTI-D-06` and the `MTI-F-05` compensating control — and both are routed, not answered |

**Five attacks failed outright. Four partially succeeded. Two succeeded. One was upheld and disclosed.** The three that landed hardest — `MTI-CH-01`, `MTI-D-01`, `MTA-11` — are all cases where a design session reached the edge of its authority, which is the correct place for a design session to be stopped.

---

## 3. Verdict By Challenge Track

| Track | Question | Verdict |
|---|---|---|
| **T1 — Mandate discharge** | Was the Inventory-side multi-tenant invariant set authored? | **CONTINUE_WITH_NOTES.** 50 invariants, 9 families, 35 context subjects, 41 functions, 9 handoff fields, 30 proof scenarios, 24 attacks. The artifact `RISK-U03` records as non-existent now exists as a specification |
| **T2 — Scope discipline** | Did the session stay inside design and specification? | **CONTINUE_WITH_NOTES.** No code, no schema, no migration, no API, no UI. One position taken that is a Boss decision, and it is recorded as a blocker rather than asserted — `MTI-D-01` |
| **T3 — Proof honesty** | Is the difference between specified and proven maintained? | **CONTINUE_WITH_NOTES.** Stated at `02` §4, `03` §2.3, `07` §1, `09` §3 and `10` §5. The word *proven* is not applied to anything in this package |
| **T4 — Cross-proof impact** | Is the effect on the 22 scenarios stated without overstatement? | **CONTINUE_WITH_NOTES.** `0 of 22` stated as unchanged in `02`, `06`, `07` and `10` |
| **T5 — Dependency honesty** | Are ranks 2 and 3 kept out, rather than designed around? | **CONTINUE_WITH_NOTES.** Both are named as absent at every point they are needed, and no substitute is offered |
| **T6 — Accounting COGS boundary** | Was any valuation conclusion trespassed? | **HOLD / EVIDENCE REQUIRED.** No trespass found. Nine matrix rows, five invariants and four reconciliation identities carry `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`. The dependency is **not lifted** |
| **T7 — Thai and business reality** | Is any Thai claim made? | **HOLD.** No Thai statutory claim of any kind. No label validated. `TH-HOLD-06` respected — a warehouse is never equated with a tax branch. 0 of 78 validated, unchanged |
| **T8 — Clean-room** | Is the Layer 1 boundary held? | **HOLD.** Self-scan result at §4. `C-05` reliance lock inherited and **not** discharged |
| **T9 — Authority boundary** | Did the session take a decision belonging to Boss? | **HOLD.** One position taken and disclosed as `MTI-D-01`. Five further decisions identified and **routed, not taken**. `SME-Q-02` and `SME-Q-03` untouched. `C-02` severity **not** classified |

**Distribution: 4 `HOLD`, 5 `CONTINUE_WITH_NOTES`, 0 `FAIL / FROZEN`.** Reconciled to the conservative label.

---

## 4. Clean-Room Position

| Control | Result |
|---|---|
| Vendor product or model identifiers | **0** — this package names no system |
| Vendor technical tokens, field names, method names, file paths, line references | **0** |
| Code fragments or fenced code blocks | **0** |
| Schema, DDL, ORM structure or migration script | **0** |
| Reference-system language used | Only `reference ERP`, `reference pattern`, `reference behaviour`, `reference implementation`, and `L2-OBS` observation citations |
| Reference behaviour **adopted** | One — route-to-rule company consistency (`MTI-10`), recorded as a positive transfer at `03` §4.1 |
| Reference behaviour **diverged from** | Four — optional location company, company-less traceable identity, regeneration in place, reactive duplicate detection |
| Thai candidate strings introduced | **0** |

**No first-hand reference-system inspection was performed by this session.** Every reference-behaviour statement is a citation to R4's published `L2-OBS` observations, and is attributed at the point of use. Layer 2 findings and the audit quarantine were not accessed and are not relied upon beyond what R4 published.

`RISK-CR-02` is **not** further discharged by this session. The residual scope the review defined — Layer 2 findings, quarantine citations, Thai content — is unchanged.

---

## 5. Vetoes Issued

| ID | Veto | Basis |
|---|---|---|
| **`AAS-V-01`** | **VETO on recording handoff element 10 as supplied, satisfied or suppliable on the basis of this package.** Its status is `specified, not built, not verified` and no other wording may be substituted | Contract §3 requires an element to be *known, traceable and evidence-backed*; contract §4 disqualifies an element *unsupported by evidence*. A specification satisfies neither. Any downstream document recording element 10 as supplied would make ten handoffs appear compliant when zero are |
| **`AAS-V-02`** | **VETO on any implementation start against this invariant set before `MTI-D-01`, `MTI-D-02` and `MTI-D-03` are ruled** | Each of the three determines the *shape* of what would be built, not a detail within it. `MTI-D-01` decides where the product master lives; `MTI-D-02` decides how many axes `AUTH` has; `MTI-D-03` decides what a tenant may change. Building before they are ruled means building the wrong thing, and the context spine is the hardest thing in a system to change afterwards — `MTI-06` makes it immutable by design |
| **`AAS-V-03`** | **VETO on any Cross-Context Report Grant carrying valuation content while the Accounting COGS Gap stands** | `L9-06` value half is `HOLD`; `JT-01` is **NOT DECIDABLE**; `GAP-FS-07` records the cross-company path as never traced end to end. A consolidated cross-company **value** view built on an undecided valuation policy would present a number that no domain owns |

**All three vetoes are on reliance and sequencing. None is a veto on the design content**, and none prevents Boss from commissioning the next controlled action.

---

## 6. `L13+` Escalation — Three Levels Opened

Opened where evidence shows complexity that `L1-L12` does not reach. Each carries all six required fields.

### `L13-MT-01` — Deferred and asynchronous execution context

| Field | Content |
|---|---|
| **Trigger** | `MTI-30` and `MTA-13`: a queued or scheduled run executes after the scheduling actor's access has been revoked, the company deactivated, or an `MTI-18` grant expired |
| **Evidence** | `L6-10` records that nothing prevents an overlapping run and there is no run-level mutual exclusion; `L3` enforcement points are synchronous function boundaries with a caller present |
| **Why `L1-L12` is insufficient** | Every enforcement point at `L3` presumes a synchronous caller whose authority can be evaluated at the moment of the act. A deferred run has no such caller. The gap is not in the invariants but in the level at which they are checked |
| **Objective** | Define the carriage, revalidation and expiry semantics of context and authority across a deferral boundary, including what is recorded when a run does not execute |
| **Checkpoint** | The definition is complete when `MTP-04` can be scored without reference to a synchronous session |
| **Impact on Boss decision** | Small in scope, and it lands inside rank 1's own implementation. It should be commissioned **with** rank 1, not after it |

### `L13-MT-02` — Tenant lifecycle, export and erasure

| Field | Content |
|---|---|
| **Trigger** | `MTI-49` and `MTA-24`: offboarding, data export and erasure are isolation acts with no defined boundary |
| **Evidence** | `GAP-MD-29` — PDPA scope for Inventory documents — is recorded as having **zero coverage anywhere in the evidence chain** and remains open |
| **Why `L1-L12` is insufficient** | `L1-L12` treats a steady-state tenant. Provisioning, deactivation, export and erasure are lifecycle transitions in which the boundary itself moves, and no level addresses them |
| **Objective** | Define the context boundary of a tenant lifecycle transition, separately from the legal scope, which only Legal may supply |
| **Checkpoint** | The definition is complete when an export can be asserted to contain exactly one tenant, and an erasure to remove exactly one tenant's data without breaking another's references |
| **Impact on Boss decision** | `MTI-D-05`. Requires a joint routing to Legal and the Account track before the technical half is useful. **No AI may supply the legal scope** |

### `L13-MT-03` — Authorized cross-company traversal for a group

| Field | Content |
|---|---|
| **Trigger** | `MTI-25`, `XCR-02` and `MTA-11`: a Thai SME group owner operating several companies has a legitimate need for a consolidated view, and an isolation design with no sanctioned door produces an unsanctioned one |
| **Evidence** | Boss scenario 15 is *"Multi-company / tenant boundary"*; `JT-10` inter-company transfer is open; `GAP-FS-07` records the cross-company path as never traced end to end; `MTA-09` records export as the leak surface that is used when no sanctioned path exists |
| **Why `L1-L12` is insufficient** | `L9` states isolation as prohibition. It does not address **authorized traversal**, which is a different design problem: prohibition needs a barrier, traversal needs a governed door with a review cadence |
| **Objective** | Define the grant model, its governance cadence, its expiry and revocation behaviour, and the content classes it may and may not carry |
| **Checkpoint** | The definition is complete when a grant can be issued, exercised, logged, reviewed and revoked, and when `MTP-21` can be scored |
| **Impact on Boss decision** | `MTI-D-04`. **This is a Boss authorisation question before it is a design question** — only Boss may sanction a door through an isolation boundary |

**Three levels opened — `L13-MT-01`, `L13-MT-02`, `L13-MT-03`. Six of six required fields on every one. None is a relocation of a carried conflict.**

---

## 7. Controlling AAS+ Verdict

**`HOLD` — DESIGN SPECIFIED, NOT PROVEN.**

Four of nine tracks return `HOLD`. None reached `FAIL / FROZEN`. Reconciled to the conservative label.

| Dimension | Assessment |
|---|---|
| **Mandate discharge** | The invariant set that `RISK-U03` records as non-existent has been authored, with anchors, enforcement layers, acceptance criteria, proof scenarios and an attack register |
| **Design content** | Assessed as internally coherent and attached to every function and surface it must govern. **Not validated, not verified, not minimised** |
| **`RISK-U03` / `GAP-FS-10`** | **REMAINS OPEN.** A specification is not the capability. Closure requires implementation and independent verification |
| **The 8 L9 proofs** | **`0 of 8` unchanged.** 8 of 8 become definable; 30 proof scenarios named; 27 executable once an implementation exists |
| **The 22 cross-proof scenarios** | **`0 of 22` unchanged.** Element 10's status changes; no scenario's does |
| **Accounting COGS dependency** | **`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`.** Not lifted. No trespass found |
| **Thai validation** | **`HOLD`.** 0 of 78. Nothing in this package is validated |
| **`C-05` / `U-07`** | **Both remain governance blockers.** Reliance on this package inherits both locks |
| **Inventory Final Solution v2.0** | **NOT READY.** 0 of 12 Joint decisions ready, 3 NOT DECIDABLE — untouched by this session |
| **Development Final Gate** | **NOT IN SCOPE AND NOT APPROACHED** |

---

## 8. Not Declared

This verdict does not declare, and no member of AAS+ is empowered to declare: `PASS`, `APPROVED`, `CLOSED`, `FINAL SOLUTION ACCEPTED`, `READY FOR DEVELOPMENT`, `READY FOR PRODUCTION`, `TEAM B AUTHORIZED`, `TEAM C AUTHORIZED`, merge approval, or release authorization.

**Items closed by this session: 0. All prior identifiers carried unchanged.**

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
