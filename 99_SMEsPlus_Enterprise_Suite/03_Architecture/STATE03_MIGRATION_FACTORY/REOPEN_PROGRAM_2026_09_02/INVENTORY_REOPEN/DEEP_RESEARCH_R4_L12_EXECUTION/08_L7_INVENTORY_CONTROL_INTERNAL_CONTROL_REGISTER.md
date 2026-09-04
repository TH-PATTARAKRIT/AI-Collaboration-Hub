# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# 08 — L7 Inventory Control / Internal Control Register

Level: `L7 — Control / Internal Control, adapted to Inventory`
Control Level: `/L9999.9999`
Status: `L7 COMPLETE FOR 10/10 MANDATED CONTROLS — 7 HAVE NO REFERENCE PATTERN — DEEP RESEARCH ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. Headline Finding

R4's L7 work produces one finding that outweighs the individual control entries and is stated first because it changes the shape of the Inventory design scope.

**`R4-F-15`. The OpenSource reference ERP supplies almost no approval infrastructure for the changes that most affect stock integrity.** Twelve controlled changes were identified at L4 §2.5. A usable reference pattern exists for at most one and a half of them. The two highest-exposure operations in the module — inventory adjustment and scrap — both have a two-state lifecycle with **no approval state, no rejection path, and no reviewer field** (`L2-OBS`, findings `R4-F-02` and `R4-F-04`).

The consequence is that internal control in SMEsPlus Inventory is **predominantly original design work, not transfer work.** Earlier rounds recorded individual control gaps; none stated the aggregate. Severity **MATERIAL**, trending **BLOCKING for build**, owner Inventory with Boss scope confirmation required.

This is a positive finding for the clean-room position — there is little here to inherit and therefore little contamination risk — and a negative finding for schedule and scope, which is why it belongs in the Boss package.

---

## 2. The Ten Mandated Controls

### `L7-01` Stock integrity control

| Aspect | Content |
|---|---|
| Control objective | Recorded quantity equals physical quantity, and the record cannot be altered except through a controlled movement. |
| Mechanism | `P-03` — on-hand is derived from movement facts and never edited directly. `IV-01` — on hand equals total in minus total out. `RC-01` — conservation checked continuously with an alarm on breach. |
| Reference pattern | Partially present. Prior evidence records four stock-truth invariants with **no database-level enforcement**, application-layer only. `L2-OBS` confirms no uniqueness constraint exists on the balance identity, so duplicate balance records for the same product/location/batch combination are structurally possible and are reconciled after the fact rather than prevented. |
| R4 status | `OPEN`. `IV-03` (exactly one balance per product, place, batch, handling unit and owner) is confirmed as a required divergence. `N-A13-01` — a manual-override path onto the available-quantity concept, noted twice across nine rounds and **never read** — remains an unfollowed lead and R4 does not close it. |
| Gate impact | Precondition for any build. |

### `L7-02` Movement approval control

| Aspect | Content |
|---|---|
| Control objective | Movements occur only under proper authority. |
| Mechanism | Control is exercised through operation type configuration and location rights rather than per-movement approval — which is correct, since per-movement approval would make the module unusable in a warehouse. |
| Reference pattern | Present in the sense that rights exist; absent in the sense that they are not scoped the way a business needs. |
| R4 status | `OPEN`. `RISK-U01` / `U-01` — whether user rights can be scoped to a warehouse or a storage place — is recorded in prior evidence as *"not merely undesigned — unevidenced either way"*, and R4 does not resolve it. Operation-level segregation (receive, deliver, transfer, adjust, scrap, count as distinct rights) is likewise an open unknown. |
| Gate impact | Team B precondition; Boss scope ruling named as required. |

### `L7-03` Adjustment approval control

| Aspect | Content |
|---|---|
| Control objective | No quantity correction takes effect without an accountable approver who is not the counter. |
| Mechanism | `INV-F-04` — count, then a separate approval, then application, with reason, approver identity, and both dates recorded. |
| Reference pattern | **None usable.** `R4-F-02`: the count is an attribute of the balance rather than a document with a lifecycle, and there is no approval state. |
| R4 status | `NO REFERENCE PATTERN — ORIGINAL DESIGN`. `GAP-MD-02` (count freeze and approval policy unselected) and `GAP-FS-17` (which count-freeze policy a Thai SME can actually operate) both **open** and both requiring Thai user input. |
| Gate impact | This is the largest single stock-integrity exposure in the module. |

### `L7-04` Scrap approval control

| Aspect | Content |
|---|---|
| Control objective | No write-off occurs without named authority, since it is a direct and irreversible loss. |
| Mechanism | Request, approve, execute, with reason, authoriser, and evidence attachment. |
| Reference pattern | **None.** `R4-F-04`: two states only, draft and done. |
| R4 status | `NO REFERENCE PATTERN — ORIGINAL DESIGN`. Compounded by `L5-09`: scrap, count loss, shrinkage and salvage can collapse into one undifferentiated number, so even a well-controlled scrap can be misclassified afterwards. `RISK-U02` / `U-02` — whether a distinct damaged-goods state is needed before scrap — is recorded as *"simply never asked"* and remains open. |
| Gate impact | Direct financial-loss channel; Thai deductibility evidence `TH-HOLD-02` separately held. |

### `L7-05` Location control

| Aspect | Content |
|---|---|
| Control objective | Goods can only be moved to locations that are valid for them, and the location structure cannot be changed in ways that silently re-interpret history. |
| Mechanism | Location kind determines financial character (`P-04`); storage categories constrain what may be stored where; kind changes require approval and versioning (`INV-F-28`). |
| Reference pattern | Structure present. `L2-OBS`: a location's company assignment is **optional** (`R4-F-09`), and location barcode uniqueness is scoped per company. |
| R4 status | `OPEN`. The optional company assignment is the structural mechanism for cross-company visibility and is carried to L9. |
| Gate impact | Underpins `L5-08`, the module's most load-bearing semantic. |

### `L7-06` Route and rule change control

| Aspect | Content |
|---|---|
| Control objective | Changes to automated supply behaviour are approved, versioned, and explainable. |
| Mechanism | Approval with before/after record; `IV-15` — configuration versioned with effective dates, never regenerated in place; `P-06` — every automatic action explainable and repeatable. |
| Reference pattern | Company consistency between a route and its rules **is** genuinely enforced (`L2-OBS`) and is worth transferring. Nothing else is. `L2-OBS` also confirms that changing a warehouse's step configuration causes its operation types, locations and routes to be **re-derived** — the `SAAS-04` regeneration risk — which is the opposite of versioning. |
| R4 status | `OPEN`. `GAP-MD-14` open. R4 records the explainability requirement as mandatory: a generated operation must name the rule that produced it, or a Thai SME cannot self-diagnose and the module becomes permanently support-dependent. |
| Gate impact | Team B precondition. |

### `L7-07` Lot and serial integrity control

| Aspect | Content |
|---|---|
| Control objective | A traceable identity is unique, immutable in its meaning, and its history cannot be silently rewritten. |
| Mechanism | `IV-04` uniqueness enforced below the application layer; `IV-13` batch value immutable after first movement; amendment and merge (`INV-F-20`) as approved operations. |
| Reference pattern | Present but insufficiently scoped. `R4-F-06`: uniqueness is (identifier, product, company) with company-less identities permitted; the reference implementation performs a reactive cross-company duplicate check rather than preventing the condition. |
| R4 status | `OPEN`. `GAP-MD-11` carried. R4 upgrades the evidence basis from an inference to a first-hand observation. |
| Gate impact | Recall capability depends on it; regulated Thai sectors depend on recall (`TH-HOLD-08`, held). |

### `L7-08` Count variance control

| Aspect | Content |
|---|---|
| Control objective | Differences found at counting are explained, classified, approved, and analysable over time. |
| Mechanism | Mandatory reason taxonomy; approver distinct from counter; adjustment register (`TH-R07`); variance trend reporting. |
| Reference pattern | A reason-tag structure exists for scrap; the reason is not mandatory anywhere and no approval gate exists. |
| R4 status | `OPEN`. The reason taxonomy itself — what the categories should be for a Thai SME — is unvalidated (`GAP-FS-11`, `GAP-MD-30`). R4 records the Inventory-owned, **non-COGS-gated** obligation from `05` §5 identity 4: **every non-sale stock reduction must carry a classification that distinguishes it from a sale**, or the periodic cost-of-sales computation silently mislabels it. This is the clearest instance in the whole package of a control requirement that Inventory can act on now without waiting for the Joint track. |
| Gate impact | Directly affects the reliability of the Accounting side. |

### `L7-09` Segregation of duties

| Aspect | Content |
|---|---|
| Control objective | The person who counts is not the person who approves; the person who requests a scrap is not the person who authorises it; the person who configures is not the person who transacts. |
| Mechanism | Role separation enforced by the system, not by convention. |
| Reference pattern | Prior evidence records that a group-by-group breakdown of access rights was never performed and is named as requiring *"a dedicated future source-research pass"*. |
| R4 status | `OPEN`. `GAP-FS-18` — how granular segregation needs to be per document type — requires Thai user and security input and is unresolved. R4 adds the realistic constraint that must shape the answer: **a Thai micro-SME may have two staff in total.** A segregation model that cannot degrade gracefully to a two-person business will be bypassed rather than followed, and a bypassed control is worse than an honest compensating control. R4 recommends the design carry an explicit, recorded compensating-control path for businesses too small to segregate, rather than a rule everyone breaks. Recorded as `R4-F-21`. |
| Gate impact | Team B precondition; Boss scope ruling required. |

### `L7-10` Audit trail requirement

| Aspect | Content |
|---|---|
| Control objective | Every material act leaves an inspectable, immutable record of who did what, when, to what, and why. |
| Mechanism | `P-02` / `IV-05` — done movement facts immutable, corrections by reversing facts. `INV-F-40` — reversal linked to original. |
| Reference pattern | Append-only completed-movement history is confirmed present in prior evidence — a genuine strength. Audit-trail *coverage* across the core stock-truth concepts is recorded as an open unknown. |
| R4 status | `OPEN` on coverage, `CONFIRMED` on the movement history itself. R4 adds two coverage requirements derived from this session's findings: configuration changes must be audited as first-class events (`INV-F-26` .. `INV-F-37` are all controlled changes with no reference audit pattern), and the granting of a period exception must produce a permanent record with grantor, reason and expiry (`IV-07`) — the v1.0 position that a global unaudited bypass is unacceptable is treated as fixed. |
| Gate impact | Precondition for any Thai statutory or audit reliance. |

---

## 3. Control Coverage Summary

| Control | Reference pattern available | R4 disposition |
|---|---|---|
| `L7-01` Stock integrity | Partial, application-layer only | OPEN |
| `L7-02` Movement approval | Partial, wrongly scoped | OPEN |
| `L7-03` Adjustment approval | **None** | ORIGINAL DESIGN |
| `L7-04` Scrap approval | **None** | ORIGINAL DESIGN |
| `L7-05` Location control | Partial, company assignment optional | OPEN |
| `L7-06` Route and rule change | Partial — one transferable strength | OPEN |
| `L7-07` Batch and serial integrity | Partial, insufficiently scoped | OPEN |
| `L7-08` Count variance | **None** | ORIGINAL DESIGN |
| `L7-09` Segregation of duties | **None evidenced** | ORIGINAL DESIGN |
| `L7-10` Audit trail | Partial — movement history is a genuine strength | OPEN on coverage |

Controls with no usable reference pattern: **4 of 10 outright**, and a further **3 of 10** where what exists is scoped in a way SMEsPlus must not inherit. Controls closed by this session: **0**.

---

## 4. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
