# [SMEPLUS-26-09-04-INV-MT-INVARIANT-SET-001]
# 08 — Failure, Edge Case And Leakage Attack Register

Levels: `L6 — contradiction, failure, edge case` and `L12 — adversarial audit challenge`
Control Level: `/L9999.9999`
Status: `24 ATTACKS REGISTERED — 8 DEFENDED IN DESIGN — 16 CARRY RESIDUAL RISK — 0 ITEMS CLOSED`

---

## 1. Method

An invariant set is worth what an attacker cannot do to it. Each entry below is an attempt to produce a cross-context effect, written as a concrete operational sequence rather than a category. Each records:

- the **mechanism** — how it would actually happen in ordinary operation, not in a contrived case;
- the **evidence basis** — where in the published evidence chain the mechanism is recorded, or `ORIGINATED` where this session raises it;
- the **defence** — which invariant refuses it, and at which layer;
- the **residual risk** — what survives the defence, stated without softening.

`RESIDUAL: NONE IN DESIGN` never means safe. It means no residual risk survives *at the design level*, and every one of them survives at the implementation level until built and verified.

---

## 2. Attacks On The Context Spine

| ID | Attack | Mechanism | Evidence | Defence | Residual |
|---|---|---|---|---|---|
| `MTA-01` | **Company-less location created in bulk** | An administrator reconfigures a warehouse; the platform re-derives operation types, locations and routes; the re-derived locations carry no company | `L2-OBS` via `R4-F-09`; `SAAS-04` | `MTI-04` (no null context) + `MTI-08` (anchor is the warehouse) + `MTI-35` (never regenerate in place) | `RESIDUAL: NONE IN DESIGN`. Implementation and verification outstanding; `R4-F-09` open |
| `MTA-02` | **Company-less traceable identity at receipt** | A goods receipt creates a batch identity for a product whose company scope was not resolved | `L2-OBS` via `R4-F-06` | `MTI-12` + `MTI-04` + `EP-W` at `INV-F-19` | `RESIDUAL: NONE IN DESIGN`. `R4-F-06` open |
| `MTA-03` | **Location re-parented across companies** | A location is moved under a warehouse belonging to a different company to "tidy the structure" | `ORIGINATED` — follows from `MTI-08` being an anchor | `MTI-08` + `MTI-06` + `MTI-40` | `RESIDUAL: NONE IN DESIGN` |
| `MTA-04` | **Warehouse company reassigned after movements exist** | A group restructures and moves a warehouse between companies | `L8-03` — *"moving a warehouse between companies re-interprets every movement it ever held"* | `MTI-06` — prohibited; the only path is an evidenced migration act | **`RESIDUAL: MATERIAL`.** The migration path itself needs the provenance reference (`GAP-FS-08`, rank 3), which does not exist. A real business need currently has no compliant path |
| `MTA-05` | **Context defaulted from a session fallback** | A background or import path finds no company and falls back to "the first" or "the default" company | `L9-01` — application-layer enforcement, unfinished bypass audit | `MTI-20` (fail closed) + `MTI-17` (`STORE`) | **`RESIDUAL: MATERIAL`.** Unverifiable until the privileged-path audit is completed |

---

## 3. Attacks Through Derivation And Reporting

| ID | Attack | Mechanism | Evidence | Defence | Residual |
|---|---|---|---|---|---|
| `MTA-06` | **Correct rows, wrong sum** | Every stored row carries the right company; a derived on-hand or forecast aggregates across two of them. `P-03` makes the most-used numbers derived by design | `R4-F-22` | `MTI-23` + `MTI-24` + `EP-A` on all reporting functions | `RESIDUAL: NONE IN DESIGN`. `R4-F-22` open |
| `MTA-07` | **Negative position masks the discrepancy** | A cross-context aggregation error nets against a genuinely negative on-hand, which the display clamps at zero, so the error is invisible on screen | `R4-F-07` + `R4-F-22` combined — `ORIGINATED` as a combination | `MTI-23` + the display-contract decision at `R4-F-07` | **`RESIDUAL: MATERIAL`.** The display contract is an open Inventory decision (`R4-F-07`), outside this authorization |
| `MTA-08` | **Uniqueness feedback discloses another company's data** | A user enters a batch, product code, barcode or document number already used in another company and the system says so | `ORIGINATED` — created by `MTI-12`'s per-company uniqueness | `MTI-27` (absence must not leak existence) | `RESIDUAL: NONE IN DESIGN`. New finding `MTI-F-03` |
| `MTA-09` | **Export as the leak surface** | A report is scoped correctly on screen, then exported; the file leaves the system, is not re-scoped on arrival, and is shared | `ORIGINATED`; `INV-F-25` | `MTI-28` (scope is part of report identity) + `EP-Q` `EP-A` `EP-E` at `INV-F-25` | **`RESIDUAL: MATERIAL`.** Nothing in the system controls the file after export. This is a governance and labelling obligation, not a technical one |
| `MTA-10` | **Barcode nomenclature as a cross-context lookup** | A tenant-level structured nomenclature resolves a scanned value to an identity outside the caller's context | `R4-F-12`; `MTI-11`/entry 16 at `04` §4 | `MTI-26` — resolution always occurs within the caller's `CTX` | **`RESIDUAL: MATERIAL`.** A misparse producing a *plausible wrong quantity* is `R4-F-12`, unaddressed by any context invariant, and real Thai formats are unevidenced (`R4-Q-03`) |
| `MTA-11` | **Cross-Context Report Grant used as a general back door** | A grant intended for one consolidated report becomes the standing mechanism through which everything is read | `ORIGINATED` — created by `MTI-25` itself | `MTI-25` — named, scoped, time-bounded, logged per use, never crosses a tenant; and `AAS-V-03` refuses valuation content | **`RESIDUAL: MATERIAL`.** Every grant mechanism degrades toward permanence. Requires a governance review cadence that is not designed here (`MTI-D-04`) |

---

## 4. Attacks Through Execution And Scheduling

| ID | Attack | Mechanism | Evidence | Defence | Residual |
|---|---|---|---|---|---|
| `MTA-12` | **Overlapping runs producing duplicate supply** | A user presses run while a scheduled run is in progress; nothing prevents overlap and nothing identifies what a run produced | `L6-10`; `GAP-MD-21` | `MTI-29` + `MTI-31` supply scoping and mutual exclusion **within** a context | **`RESIDUAL: BLOCKING`.** The idempotency identity is `RISK-C02`, rank 2, **not in this authorization**. Duplicate detection remains impossible |
| `MTA-13` | **Deferred run executes under lapsed authority** | A job is scheduled, the scheduling user's access to that company is revoked, the job fires later | `ORIGINATED` — L1-L12 addresses synchronous boundaries only | `MTI-30` — authority carried; lapse prevents execution and is recorded | `RESIDUAL: NONE IN DESIGN`. Escalated to L13 — see `12` §6 |
| `MTA-14` | **Nested reordering rules raising supply twice** | Two rules cover the same product, one at a parent location and one at a child; both are active; the shortfall walk covers both | `R4-F-11` | `MTI-14` closes **only** the cross-company half | **`RESIDUAL: MATERIAL`.** Within-company overlap is untouched. `R4-F-11`, Lane A, outside this authorization. Explicitly restated so `MTI-14` is not misread as closing it |
| `MTA-15` | **Put-away override across companies** | A picker overrides a suggested destination and selects a location in another company from a picker list | `ORIGINATED`; `INV-F-32` | `MTI-08` + `EP-Q` on the picker + `EP-W` on the write + `EP-E` on the override | `RESIDUAL: NONE IN DESIGN` |
| `MTA-16` | **Approval routed to an approver in another company** | The only available second person with authority sits in another company of the same group — the ordinary situation in a small Thai group | `R4-F-21`; `L7-09` | `MTI-45` / `06` §6 — the context boundary wins; segregation degrades to a compensating control | **`RESIDUAL: MATERIAL`.** The compensating control needs Thai user input (Lane C) and does not exist. New finding `MTI-F-05` |

---

## 5. Attacks Through Master Data And Configuration

| ID | Attack | Mechanism | Evidence | Defence | Residual |
|---|---|---|---|---|---|
| `MTA-17` | **A tenant-level master change hits every company at once** | A unit conversion factor, an attribute set, or a stock-control classification is changed for one company's need and applies tenant-wide | `INV-F-17`, `INV-F-18`, `INV-F-37`; `GAP-FS-03` | `MTI-36` (versioned, non-retroactive) + `MTI-40` (evented, approved) + `IV-11` | **`RESIDUAL: MATERIAL`.** This is the cost of `MTI-D-01` option A and it is why the decision is a Boss item |
| `MTA-18` | **Category costing facet changed across companies in one act** | The product category owns reporting, put-away **and** costing facets; one edit touches all three, and costing is company-scoped | `R4-F-10`; `GAP-FS-02` | `MTI-11` (costing facet company-scoped) + `EP-G` at `INV-F-33` | **`RESIDUAL: BLOCKING`.** The facet split is `GAP-FS-02`, precondition-blocked on `JT-01`, which is **NOT DECIDABLE** |
| `MTA-19` | **Template regeneration silently reverts a tenant's configuration** | A platform template is updated and instantiated tenant configuration is re-derived from it | `L2-OBS`; `SAAS-04`; `GAP-MD-14` | `MTI-35` (copy at provisioning, never propagate) + `MTI-36` | `RESIDUAL: NONE IN DESIGN` for the mechanism; the **boundary content** is `MTI-D-03`, open |
| `MTA-20` | **Handling unit carrying two companies' goods** | A shipment is consolidated into one box for carrier efficiency | `ORIGINATED`; `CN-19`; `GAP-FS-05` | `MTI-13` — prohibited | **`RESIDUAL: MATERIAL`.** The prohibition may conflict with a genuine logistics practice. If a Thai SME group consolidates physically, the model needs a separate consolidation concept. Routed to the Thai panel |

---

## 6. Attacks Through Migration, Handoff And Lifecycle

| ID | Attack | Mechanism | Evidence | Defence | Residual |
|---|---|---|---|---|---|
| `MTA-21` | **Bulk migration assigning company by name match** | A legacy warehouse or location list is imported and company is inferred from a name, code or text pattern | `R4-F-23`, `R4-F-24` | `MTI-42` — explicit, evidenced assignment; inference prohibited | **`RESIDUAL: BLOCKING`.** The provenance reference that would make the assignment inspectable afterwards is `GAP-FS-08`, rank 3, and does not exist. `MTI-42` prohibits the bad act but cannot evidence the good one |
| `MTA-22` | **Inter-company transfer modelled as one movement** | The simplest implementation of a group resupply is a single movement from company A's location to company B's | `HO-22`; `GAP-FS-07`; `JT-10` | `MTI-15` + `MTI-44` — two facts, correlated via `XCR-01` | **`RESIDUAL: BLOCKING`.** The path is recorded as **never traced end to end** and its treatment is `JT-10`, open. The structure is specified; the path is not proven to work |
| `MTA-23` | **Consignment stock read as another company's stock** | Owner and company are conflated; supplier-owned goods at our location are treated as belonging to another entity, or third-party goods are valued as a company asset | `L5-07`; `GAP-MD-09` | `MTI-16` + `HF-CTX-09` — owner carried as its own field, conflation prohibited | **`RESIDUAL: MATERIAL`.** What may be valued as whose asset is `GAP-MD-09`, open, with the valuation half held. New finding `MTI-F-02` |
| `MTA-24` | **Tenant erasure removing, or failing to remove, the wrong data** | Offboarding or a data-subject request executes against a boundary nobody defined | `GAP-MD-29` — recorded as having **zero coverage anywhere in the evidence chain** | `MTI-49` — bounded by `CTX` | **`RESIDUAL: BLOCKING`.** The legal scope does not exist, no AI may supply it, and the invariant is specified in shape only. `MTI-D-05` |

---

## 7. Contradictions This Register Does Not Arbitrate

Carried forward unchanged so that a future session does not mistake an unresolved disagreement for a settled position. **This session arbitrates none of them.**

| ID | Conflict | Owner | Position Here |
|---|---|---|---|
| `C-01` / `RISK-C01` | Cancellation-cascade symmetry | Team A / Track 01 | `MTA-*` touches it at `INV-F-10`; not arbitrated |
| `C-02` / `RISK-C02` | Idempotency and replay — gate-blocking or design input | **Boss** | Severity explicitly **not** classified by this session, consistent with R4 and the review both declining |
| `C-04` / `N-CONC-01` | Reservation locking under concurrency | Team A / Track 07 | Reservation context is specified at `MTI-16`; the concurrency question is untouched |
| `N-A13-01` | Unread manual-override path onto available quantity | Team A / Track 07 | If a write path onto a derived value exists, `MTI-23` and `EP-W` would both apply to it. **The lead remains unread and this session did not read it** |
| `C-05` | Clean-room exposure in prior evidence | **Boss** | Containment ruling outstanding; reliance lock inherited and carried. Not touched |
| `U-07` | Two competing 9 Veto Council charters | **Boss** | Inherited conditionality — see `12` §1 |

---

## 8. Register Result

| Measure | Result |
|---|---:|
| Attacks registered | **24** |
| Originated by this session | 8 |
| Carried from published evidence | 16 |
| `RESIDUAL: NONE IN DESIGN` | **8** |
| `RESIDUAL: MATERIAL` | **11** |
| `RESIDUAL: BLOCKING` | **5** — `MTA-12`, `MTA-18`, `MTA-21`, `MTA-22`, `MTA-24` |
| Attacks defeated by an invariant this session originated | 6 — `MTA-03`, `MTA-06`, `MTA-08`, `MTA-13`, `MTA-15`, `MTA-19` |
| Unarbitrated conflicts carried | 6 |
| Items closed | **0** |

**The five `BLOCKING` residuals are the honest measure of this session.** Not one is caused by a defect in the invariant set. Every one sits on a capability outside this authorization: rank 2 (`MTA-12`), a `NOT DECIDABLE` Joint decision (`MTA-18`), rank 3 (`MTA-21`), an untraced path (`MTA-22`), or a legal scope that has never been established (`MTA-24`).

---

## 9. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
