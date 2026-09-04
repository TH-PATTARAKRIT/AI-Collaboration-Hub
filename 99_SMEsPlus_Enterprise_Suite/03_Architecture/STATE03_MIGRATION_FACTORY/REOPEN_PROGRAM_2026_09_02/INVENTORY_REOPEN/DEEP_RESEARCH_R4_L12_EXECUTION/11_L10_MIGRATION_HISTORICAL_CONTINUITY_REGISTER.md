# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# 11 — L10 Migration / Historical Continuity Register

Level: `L10 — Migration / Historical Continuity`
Scope: `10 mandated continuity areas`
Control Level: `/L9999.9999`
Status: `L10 COMPLETE FOR 10/10 AREAS — PRECONDITION MISSING — DEEP RESEARCH ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. Governing Precondition

Every area in this register depends on one capability that **does not exist**:

**`GAP-FS-08` / `GAP-MD-27` / `CN-36` — the provenance reference.** A mapping from a legacy system key to the SMEsPlus key, carried on every migrated record. Prior evidence records that no such field exists in the reference system and that it must be originated by SMEsPlus. `IV-09` states the invariant: every migrated record carries a provenance reference.

Without it, nothing below can be reconciled, replayed, or defended to an auditor. R4 therefore treats it as the governing precondition rather than as one item among ten, and records it as **Lane A — not COGS-gated**, meaning it can be commissioned now.

Prior evidence separately describes the opening-balance question as *the single highest fabrication-risk point in the whole Inventory scope*, precisely because there is no reference mechanism to copy and an AI executor asked to design one has nothing to anchor to. R4 treats that warning as binding on its own conduct: this register states what must be true, not what a migration would produce.

---

## 2. The Ten Mandated Continuity Areas

### `L10-01` Opening stock

| Aspect | Content |
|---|---|
| Requirement | The quantity position at cutover, per product, location, batch and owner, agreed with the business and the accountant. |
| Mechanism | `CN-33` opening balance; established through the adjustment path (`INV-F-41`). |
| Reference pattern | **None.** No cutover opening-balance mechanism exists to learn from. |
| Blocking items | `JT-11` / `G-5` / `GAP-FS-09` — opening-balance certification. `RC-08` requires **human certification** against the accountant's opening trial balance, once, at cutover. |
| R4 status | `OPEN — DEPENDENCY LOCKED` on the value half; the quantity half is Inventory-owned but blocked on the provenance precondition. |

### `L10-02` Historical movement

| Aspect | Content |
|---|---|
| Requirement | Decide whether movement history migrates, or only an opening position plus history from cutover forward. |
| Mechanism | `HO-25` lineage. |
| Reference pattern | Not applicable — this is a programme decision, not a system behaviour. |
| Blocking items | The decision itself is undecided. `RISK-C02` compounds it: migrated movements without a stable identity cannot be safely replayed if a migration run must be repeated. |
| R4 status | `OPEN — INVENTORY OWNED` as a recommendation, **Boss** as a decision. R4 records the consideration that matters for a Thai SME: the stock card is the document an auditor asks for, and an auditor asking about a period before cutover will not accept "the system starts here" unless the legacy evidence is preserved and reachable. That argues for at least a preserved, queryable legacy history even if it is not migrated as live movement facts. |

### `L10-03` Lot and serial history

| Aspect | Content |
|---|---|
| Requirement | Traceability chains that span the cutover must remain traceable. |
| Mechanism | `CN-17`, `CN-18` with provenance. |
| Reference pattern | None for the migration case. |
| Blocking items | `R4-F-06` — identity scope is (identifier, product, company) with company-less identities possible. A migration that imports legacy batches without resolving the company scope will import the collision surface with them. |
| R4 status | `OPEN — INVENTORY OWNED`. R4 raises this as a specific migration hazard that earlier rounds did not connect to the identity finding. Recorded as `R4-F-23`. For a regulated Thai sector — food, cosmetic, pharmaceutical — a broken chain at cutover is a compliance exposure, and the sector obligations themselves are `TH-HOLD-08`, held. |

### `L10-04` Product identity continuity

| Aspect | Content |
|---|---|
| Requirement | A legacy product resolves to exactly one SMEsPlus product, and the relationship is recorded. |
| Mechanism | Provenance reference; `L8-01` canonical identity. |
| Reference pattern | None. |
| Blocking items | Thai SME masters routinely contain duplicates under Thai and English names and re-used codes for discontinued items. The Boss standard's rule that codes and names are not sufficient identity is at its most consequential here. |
| R4 status | `OPEN`. `GAP-MD-28` — cardinality transform table and orphan quarantine rules — is **open**. R4 records the specific requirement that a many-to-one merge must be recorded as such, so that a later question about a legacy code resolves deterministically. |

### `L10-05` Warehouse and location continuity`

| Aspect | Content |
|---|---|
| Requirement | Legacy storage structure maps to SMEsPlus warehouses and locations without changing the meaning of historical movements. |
| Mechanism | `L8-03`, `L8-04`. |
| Reference pattern | None. |
| Blocking items | `R4-F-09` — optional company assignment on locations. A migration is exactly the moment when a company-less location would be created in bulk. |
| R4 status | `OPEN — INVENTORY OWNED`. The location **kind** must be assigned deliberately at migration, because it determines the financial meaning of every movement that crossed the location (`L5-08`). A migration that assigns kinds by name-matching will silently mis-state financial history. Recorded as `R4-F-24`. |

### `L10-06` Valuation continuity

| Aspect | Content |
|---|---|
| Requirement | Value at cutover, and the ability to answer a valuation question dated before cutover. |
| Mechanism | `CN-31` valuation facts; `CN-33` opening balance. |
| Reference pattern | None. |
| Blocking items | **`DEPENDENCY: ACCOUNTING COGS GAP`** — `JT-01` (policy owner) NOT DECIDABLE, `JT-02` (methods and change rules) open. A cost layer cannot be migrated without knowing what policy it was produced under and what policy it will be read under. The evidence adds that a costing-method change does not retroactively rebase existing value, confirmed only in one direction, so a migration that lands stock under a different method than it left is in the unconfirmed direction. |
| R4 status | `OPEN — DEPENDENCY LOCKED`. This is the area where R4 is most constrained and it does not speculate. |

### `L10-07` Cutover reconciliation

| Aspect | Content |
|---|---|
| Requirement | Prove that what arrived equals what left, in quantity and in value, before go-live is accepted. |
| Mechanism | `RC-08`; a reconciliation report with named certification. |
| Reference pattern | None. |
| Blocking items | Provenance precondition; `JT-11` / `G-5`. |
| R4 status | `OPEN — DEPENDENCY LOCKED` on value, `OPEN — INVENTORY OWNED` on quantity. R4 records that quantity reconciliation is achievable independently and should not wait for the value half — the two can be certified separately and the quantity certificate is useful on its own. |

### `L10-08` Migration exception treatment

| Aspect | Content |
|---|---|
| Requirement | Records that cannot be migrated cleanly are quarantined, visible, and dispositioned — never silently dropped or silently defaulted. |
| Mechanism | Orphan quarantine (`GAP-MD-28`). |
| Reference pattern | Prior evidence records a reject-table pair present in the reference schema with **zero rows** — the structure exists, the practice does not. |
| R4 status | `OPEN — INVENTORY OWNED`. R4 records the requirement that a quarantined record must be *counted* in the cutover reconciliation as an explicit exception, not omitted from it. A reconciliation that balances because the difficult records were excluded is not a reconciliation. |

### `L10-09` Legacy reference quarantine

| Aspect | Content |
|---|---|
| Requirement | Legacy identifiers and structures are preserved for lookup but must not become live SMEsPlus semantics. |
| Mechanism | Provenance reference as a one-way map; legacy values readable, never authoritative. |
| Reference pattern | None. |
| R4 status | `OPEN`. This is also a clean-room concern: legacy structures carried forward as design, rather than as data, would breach the Layer 1 boundary. R4 records that the provenance reference must be a **data** mapping and never a design inheritance. |

### `L10-10` Evidence lineage

| Aspect | Content |
|---|---|
| Requirement | Every migration decision, transform and exception is recorded and reachable after go-live. |
| Mechanism | Migration batch identity — handoff element 14 — plus a decision record. |
| Reference pattern | None. |
| Blocking items | The batch identity **does not exist** (`GAP-FS-08`). |
| R4 status | `OPEN`. Handoff element 14 is unsuppliable, which is one of the three failures behind `R4-F-16`. |

---

## 3. Migration-Specific Findings Raised By R4

| ID | Finding | Severity |
|---|---|---|
| `R4-F-23` | Migrating legacy batch identities without resolving company scope imports the cross-company collision surface in bulk | MATERIAL |
| `R4-F-24` | Assigning location kinds by name-matching at migration silently mis-states the financial meaning of historical movements | MATERIAL |
| `R4-F-25` | Quantity cutover reconciliation is achievable independently of value cutover reconciliation and should not be deferred behind it | MATERIAL — opportunity, not defect |

`R4-F-25` is recorded deliberately as an opportunity. Almost everything in this register is blocked. The quantity half of cutover reconciliation is not blocked by the Accounting COGS Gap and can be specified and certified on its own, which materially de-risks go-live without requiring any Joint decision.

---

## 4. L10 Coverage Result

| Measure | Result |
|---|---:|
| Mandated continuity areas | 10 |
| Given full L10 treatment | 10 |
| Areas with **no reference pattern to learn from** | 9 of 10 |
| Areas blocked by the missing provenance reference | 10 of 10 |
| Areas additionally dependency-locked on the Accounting COGS Gap | 3 — `L10-01` (value half), `L10-06`, `L10-07` (value half) |
| Areas actionable now, in whole or part | 4 — `L10-04`, `L10-05`, `L10-08`, and the quantity half of `L10-07` |
| Areas closed by this session | **0** |

That nine of ten areas have no reference pattern is the defining characteristic of migration in this programme: it is almost entirely origination. That is also why prior evidence names it the highest fabrication-risk area, and why R4 has confined itself to stating requirements rather than proposing a design.

---

## 5. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
