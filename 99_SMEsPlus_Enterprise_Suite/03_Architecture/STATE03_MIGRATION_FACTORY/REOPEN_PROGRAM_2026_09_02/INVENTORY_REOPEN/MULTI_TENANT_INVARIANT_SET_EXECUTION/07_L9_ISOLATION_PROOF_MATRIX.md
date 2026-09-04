# [SMEPLUS-26-09-04-INV-MT-INVARIANT-SET-001]
# 07 — L9 Isolation Proof Matrix And Acceptance Criteria

Control Level: `/L9999.9999`
Status: `8 OF 8 L9 PROOFS BECOME DEFINABLE — 0 OF 8 PROVEN — 0 OF 22 CROSS-PROOF SCENARIOS MOVED — DESIGN / SPECIFICATION ONLY`

---

## 1. The Distinction This File Turns On

R4 reports `0 of 8` L9 proofs and gives the reason: *"Without that set, there is nothing against which an isolation property could be proven"* (`10` §1).

A proof requires three things. This session supplies one of them.

| Requirement | Supplied by | Status after this session |
|---|---|---|
| **A proposition** — a stated property precise enough to be violated | This session, at `03` | **Supplied** |
| **An implementation** — a system in which the property could hold or fail | Team B, not authorized | Absent |
| **A test** — an executed attempt to violate it, and its result | A later verification pass, not authorized | Absent |

**Therefore: `0 of 8` proven stands, and stands unchanged.** What changes is that all eight become *definable and testable*, which they were not before. This file states, for each, exactly what would be tested and what result would count.

### 1.1 Proof-state vocabulary

| State | Meaning |
|---|---|
| `DEFINABLE` | Proposition and acceptance criteria complete; nothing upstream blocks definition |
| `DEFINABLE — CONDITIONAL` | Complete in form; scope or content conditioned on a named ruling or input, cited |
| `PARTIALLY DEFINABLE` | The context half is complete; another half is held or absent, cited |
| `PROVEN` | Never used in this file. **No proof is achieved by a design session** |

---

## 2. The Eight Mandated Proofs

### `L9-01` Tenant isolation

| Aspect | Content |
|---|---|
| **Proposition** | No tenant can read or write another tenant's Inventory data under any code path, including privileged, system, background, administrative and migration paths |
| **Invariants** | `MTI-01`, `MTI-02`, `MTI-17`, `MTI-18`, `MTI-20`, `MTI-21`, `MTI-26`, `MTI-27`, `MTI-29`, `MTI-30`, `MTI-47`, `MTI-49` |
| **Proof scenarios** | `MTP-01` .. `MTP-06` — see §3 |
| **Acceptance criterion** | Every enumerated path attempts a cross-tenant read and a cross-tenant write and **fails at `STORE`**, with the failure recorded; and the path enumeration is itself certified complete |
| **What still blocks the proof** | The privileged-bypass path audit **started and never completed** (`L9-01`). Until the enumeration is complete, no completeness claim is possible — only per-path results |
| **State** | **`DEFINABLE`** — definition unblocked; execution requires the audit plus an implementation |

### `L9-02` Company isolation

| Aspect | Content |
|---|---|
| **Proposition** | Within a tenant, one company's stock and value cannot leak into another's — by record, by reference, by derivation, or by disclosure |
| **Invariants** | `MTI-03`, `MTI-04`, `MTI-05`, `MTI-08`, `MTI-12`, `MTI-13`, `MTI-15`, `MTI-19`, `MTI-22`, `MTI-27` |
| **Proof scenarios** | `MTP-07` .. `MTP-14` |
| **Acceptance criterion** | The two named structural mechanisms cease to be expressible: **no location without a company** and **no traceable identity without a company**, both rejected at `STORE`; and every cross-company reference resolves to an `MTI-22` register entry |
| **What still blocks the proof** | Nothing at the definition level. `R4-F-09` and `R4-F-06` remain open findings; closure requires implementation and independent verification |
| **State** | **`DEFINABLE`** — this is the proof the invariant set most directly serves |

### `L9-03` Branch and location isolation

| Aspect | Content |
|---|---|
| **Proposition** | Within a company, rights and visibility can be confined to a warehouse or a storage place where the business requires it |
| **Invariants** | `MTI-07`, `MTI-08`, `MTI-21`, `MTI-26`; and the `AUTH` shape at `04` §7 |
| **Proof scenarios** | `MTP-15`, `MTP-16` |
| **Acceptance criterion** | Depends on the ruling. Under a company-only ruling the proof is **vacuous** and should be recorded as such rather than as failed. Under a warehouse- or location-level ruling, an actor scoped to one warehouse can neither read nor write in another within the same company |
| **What still blocks the proof** | `RISK-U01` / `U-01` — recorded as *"not merely undesigned — unevidenced either way"*. A **Boss scope ruling**, not an investigation. Separately, a Thai tax branch is not a warehouse (`TH-HOLD-06`) and the two must not be carried by one mechanism |
| **State** | **`DEFINABLE — CONDITIONAL (`MTI-D-02` / `U-01`)`** — both branches specified so the ruling can be taken on its merits |

### `L9-04` Shared template versus tenant-owned customization boundary

| Aspect | Content |
|---|---|
| **Proposition** | What a tenant may change, what is provisioned from a shared template, and what happens to tenant changes when the template changes, are all stated — and a template change never mutates instantiated tenant configuration |
| **Invariants** | `MTI-34`, `MTI-35`, `MTI-36`, `MTI-37`, `MTI-47` |
| **Proof scenarios** | `MTP-17` .. `MTP-19` |
| **Acceptance criterion** | Two halves, and they separate cleanly. **Mechanism half:** a template version is changed and no instantiated tenant record changes; a warehouse is reconfigured and no derived record is recreated without its company. **Boundary half:** the enumeration of what a tenant may change is published and complete |
| **What still blocks the proof** | The **boundary half only**. `GAP-MD-14` / `SAAS-04` is open and is a product-scope decision (`MTI-D-03`). The mechanism half is unblocked |
| **State** | **`PARTIALLY DEFINABLE`** — mechanism `DEFINABLE`, boundary content conditional |

### `L9-05` No cross-tenant stock visibility

| Aspect | Content |
|---|---|
| **Proposition** | No report, search, aggregate, export or automated process surfaces another tenant's quantities — **including on derived surfaces** |
| **Invariants** | `MTI-21`, `MTI-23`, `MTI-24`, `MTI-25`, `MTI-26`, `MTI-27`, `MTI-28` |
| **Proof scenarios** | `MTP-20` .. `MTP-26` |
| **Acceptance criterion** | The derived surfaces named at `R4-F-22` — `INV-M10`, `INV-M11`, `INV-M14`, `INV-M15` — are each exercised for cross-boundary aggregation and each fails to produce one; **and** the negative disclosure channels (uniqueness feedback, autocomplete, barcode resolution, error text) disclose nothing |
| **What still blocks the proof** | Nothing at the definition level. `R4-F-22` is served directly by Family D |
| **State** | **`DEFINABLE`** — and this is the proof whose definition changed most, since no prior round stated the derived-surface requirement |

### `L9-06` No cross-company cost leakage

| Aspect | Content |
|---|---|
| **Proposition** | A costing policy, a cost layer or a valuation event belonging to one company cannot influence another's value |
| **Invariants** | `MTI-16`, `MTI-23`, `MTI-24`, `MTI-44`; register entry `XCR-01` |
| **Proof scenarios** | `MTP-27`, `MTP-28` |
| **Acceptance criterion** | **Context half:** every cost layer and every valuation fact resolves to exactly one company, and the retroactive compensation pass matches only within a company. **Value half:** cannot be stated |
| **What still blocks the proof** | The value half. `JT-01` valuation policy owner is **NOT DECIDABLE**; `JT-10` inter-company transfer treatment is open; `GAP-FS-07` records the cross-company transfer path as **never traced end to end**. Additionally `R4-F-20` — retroactive compensation sequenced by record creation order rather than effective date — is a `L13-01` escalation on the value half |
| **State** | **`PARTIALLY DEFINABLE`** — context half `DEFINABLE`; value half `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |

### `L9-07` No hard-coded Thailand-only logic in the SaaS core

| Aspect | Content |
|---|---|
| **Proposition** | Thai-specific behaviour lives in a localization layer, not in the core |
| **Invariants** | `MTI-34`, `MTI-36`; and `MTI-07`'s prohibition on equating a warehouse with a tax branch |
| **Proof scenarios** | `MTP-29` |
| **Acceptance criterion** | An inventory of Thai requirements classified by kind — **presentational**, **behavioural**, **statutory** — exists and is validated, and no item classified behavioural or statutory is implemented in the tenant-neutral core |
| **What still blocks the proof** | The inventory itself does not exist, and its statutory column may not be produced by an AI. `TH-HOLD-01` .. `TH-HOLD-09` are held and route to the Accounting-Tax track; the presentational column requires the Thai user panel (`GAP-FS-11`, 0 of 78 validated) |
| **State** | **`DEFINABLE — CONDITIONAL (Lane C)`.** R4's assessment is carried unchanged: **no Thai statutory rule has been admitted into Inventory core logic by any round, including this one**, which is a genuine architectural strength and is recorded as such rather than assumed |

### `L9-08` Controlled localization extension points

| Aspect | Content |
|---|---|
| **Proposition** | Named, versioned extension points exist where a localization may attach, and nothing else may |
| **Invariants** | `MTI-34`, `MTI-35`, `MTI-36`, `MTI-37` |
| **Proof scenarios** | `MTP-30` |
| **Acceptance criterion** | The extension points are enumerated and versioned; an attempt to attach localization behaviour anywhere else fails; and each attachment resolves to a `CTX` or is tenant-neutral by declaration |
| **What still blocks the proof** | The **set** of extension points depends on `L9-07`'s classification inventory, which does not exist. R4's distinction is carried and not softened: **routing a statutory item to another track is a governance act, not an architectural extension point** |
| **State** | **`DEFINABLE — CONDITIONAL`** on `L9-07` |

---

## 3. Proof Scenarios — `MTP-01` .. `MTP-30`

Each is an adversarial attempt, not a demonstration. The expected result is a **rejection**; a successful operation is a failed proof.

| ID | Serves | Attempt | Expected Result |
|---|---|---|---|
| `MTP-01` | `L9-01` | Read a movement fact of tenant B from a session in tenant A | Rejected at `STORE`; indistinguishable from non-existence |
| `MTP-02` | `L9-01` | Write a balance row in tenant B from a background job bound to tenant A | Rejected at `STORE`; failure recorded |
| `MTP-03` | `L9-01` | Execute an administrative or support path with elevated rights and read across tenants | Rejected, or permitted **only** under a named `MTI-18` grant with a log entry |
| `MTP-04` | `L9-01` | Schedule a run in tenant A, revoke the scheduling authority, let the run fire | Run does not execute; non-execution recorded (`MTI-30`) |
| `MTP-05` | `L9-01` | Export from tenant A and confirm no tenant B row is present in the output | No foreign row; export act evented |
| `MTP-06` | `L9-01` | Provision a new tenant and inspect for inherited operational data | Zero inherited operational rows (`MTI-47`) |
| `MTP-07` | `L9-02` | Create a storage location with no company | **Not expressible** — the location has no warehouse-less form (`MTI-08`) |
| `MTP-08` | `L9-02` | Re-parent a location under a warehouse belonging to another company | Rejected at `STORE` |
| `MTP-09` | `L9-02` | Create a lot or serial identity with no company | Rejected at `STORE` (`MTI-12`) |
| `MTP-10` | `L9-02` | Create the same batch value in two companies | **Permitted** — legitimate distinct identities — and neither is presented, exported or handed off as a bare value |
| `MTP-11` | `L9-02` | Validate a movement whose source and destination resolve to different companies | Rejected (`MTI-15`); the legitimate form is `XCR-01`, two facts |
| `MTP-12` | `L9-02` | Place goods from two companies in one handling unit | Rejected (`MTI-13`) |
| `MTP-13` | `L9-02` | Attach a rule to a route in another company | Rejected — the reference pattern already rejects this; adopted as `MTI-10` |
| `MTP-14` | `L9-02` | Change a warehouse's company after movements exist | Rejected (`MTI-06`); the only path is an evidenced migration act |
| `MTP-15` | `L9-03` | With a warehouse-scoped actor, read a second warehouse in the same company | Under a warehouse-level ruling: rejected. Under a company-only ruling: permitted, and the proof is **vacuous, not failed** |
| `MTP-16` | `L9-03` | Confirm that a tax-branch attribute, if present, is not derived from warehouse | Separate dimension confirmed (`TH-HOLD-06` held) |
| `MTP-17` | `L9-04` | Change a platform template version and inspect instantiated tenant configuration | No instantiated record changes (`MTI-35`) |
| `MTP-18` | `L9-04` | Reconfigure a warehouse and inspect every re-derived record | No record recreated without its company (`MTI-04`, `MTI-35`); prior configuration versions remain resolvable |
| `MTP-19` | `L9-04` | Attempt a tenant edit outside the published tenant-changeable boundary | Rejected — **requires the boundary to be published first (`MTI-D-03`)** |
| `MTP-20` | `L9-05` | Produce a stock position spanning two tenants | Not producible (`MTI-24`) |
| `MTP-21` | `L9-05` | Produce a valuation position spanning two companies without a grant | Not producible; **with** a grant, valuation content is refused while the COGS Gap stands (`AAS-V-03`) |
| `MTP-22` | `L9-05` | Produce warehouse analytics whose measure aggregates across companies | Not producible; the measure states its `CTX` scope (`MTI-28`) |
| `MTP-23` | `L9-05` | Enter a batch value already in use in another company and read the feedback | No disclosure that the value exists elsewhere (`MTI-27`) |
| `MTP-24` | `L9-05` | Resolve a scanned barcode that matches an identity in another context | Resolves nothing (`MTI-26`) |
| `MTP-25` | `L9-05` | Search or autocomplete for a product code held only in another company | Zero results, indistinguishable from non-existence |
| `MTP-26` | `L9-05` | Compare a forecast against its stated `CTX` scope | Scope present and part of the report identity |
| `MTP-27` | `L9-06` | Trace a cost layer's consumption and confirm it never matches a movement in another company | Context half only; **value half held** |
| `MTP-28` | `L9-06` | Execute an inter-company transfer end to end and inspect both sides | **Cannot be executed as a proof** — path never traced end to end (`GAP-FS-07`), treatment `JT-10` open |
| `MTP-29` | `L9-07` | Inspect the classified Thai requirement inventory and confirm no behavioural or statutory item sits in the tenant-neutral core | **Cannot be executed** — the inventory does not exist (Lane C) |
| `MTP-30` | `L9-08` | Attempt to attach localization behaviour outside an enumerated extension point | Rejected — **requires the extension points to be enumerated first**, which depends on `MTP-29` |

---

## 4. L9 Result After This Design

| Measure | Before | After | Change |
|---|---:|---:|---|
| Mandated L9 proofs | 8 | 8 | — |
| Proofs **achieved** | **0** | **0** | **None** |
| Proofs with a stated proposition | 0 | **8** | +8 |
| Proofs `DEFINABLE` unconditionally | 0 | **3** — `L9-01`, `L9-02`, `L9-05` | +3 |
| Proofs `DEFINABLE — CONDITIONAL` | 0 | **3** — `L9-03`, `L9-07`, `L9-08` | +3 |
| Proofs `PARTIALLY DEFINABLE` | 0 | **2** — `L9-04`, `L9-06` | +2 |
| Proof scenarios specified | 0 | **30** | +30 |
| Scenarios executable once an implementation exists | — | **27 of 30** | — |
| Scenarios **not executable even then** | — | **3** — `MTP-28`, `MTP-29`, `MTP-30`, each on a named upstream blocker | — |
| Prior items closed | — | **0** | — |

---

## 5. Cross-Proof Impact On The 22 Boss-Approved Scenarios

The authorization requires this statement explicitly. It is stated conservatively.

### 5.1 The headline

**`0 of 22` stands. No scenario becomes verified, provable, or closer to being declared verified by this session.**

Element 10 was one of three structural elements failing on every material handoff. Its status changes from *unsuppliable in principle* to *specified, not built, not verified*. Under contract §3, an element must be **known, traceable and evidence-backed**; a specification satisfies none of the three on its own.

### 5.2 What does change

| Scenario | Change |
|---|---|
| **15 — Multi-company / tenant boundary** | The only scenario whose subject matter *is* this capability. It moves from **not testable — no proposition exists** to **testable once implemented**, with 30 named proof scenarios. This is the largest single change and it is a change in testability, not in result |
| **All 22** | The element 10 obstruction acquires a defined remedy with acceptance criteria. The obstruction itself is not removed |
| **20, 21, and the certified opening balance** | Unchanged — element 14, rank 3, `GAP-FS-08` |
| **22 — Retry / idempotency / replay** | Unchanged — element 15, rank 2, `RISK-C02`. `MTI-31` narrows the scheduler exposure; it supplies no identity |
| **1–14, 16–19** | Unchanged — elements 4 and 7 held under the COGS Gap in addition to 14 and 15 |

### 5.3 The sequencing statement, restated because it is the point

The review established that the three structural capabilities are a precondition to the cross-proof being convenable at all, and that the Joint track and the structural track are **sequential, with the structural track first** (`09` §4).

This session completes the **design** of the first and highest-reaching of the three. It does not complete the capability. The correct reading is:

> Rank 1 has moved from *not commissioned* to *specified*. It has not moved to *built*, and nothing downstream of it has moved at all.

---

## 6. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
