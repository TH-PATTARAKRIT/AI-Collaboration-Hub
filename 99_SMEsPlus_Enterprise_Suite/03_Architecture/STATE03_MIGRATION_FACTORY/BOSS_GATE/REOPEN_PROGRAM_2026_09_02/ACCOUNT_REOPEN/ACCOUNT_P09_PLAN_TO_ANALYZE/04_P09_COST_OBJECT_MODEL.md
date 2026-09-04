# P09_COST_OBJECT_MODEL

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Process:** P09 Plan-to-Analyze
**Layer:** 1 — clean-room. Evidence identifiers resolve in the Layer 2 quarantine.

---

## 1. THE HEADLINE FINDING

**There is no cost object in the reference pattern.**

There is a dimension value, and there are a dozen modules that each add their own relational field to the management record — task, project, employee, department, manager, parent task, milestone, sales order line, work centre, work-order productivity record, and more. What there is *not* is a first-class object that answers "what accountable thing bears this cost", with an identity, a lifecycle, a scope and a closing state.

The consequence is that **the cost object is whatever the producing module decided to attach**, and no two producers agree. This is the single largest design gap surfaced by P09, alongside the absent accounting-event identity inherited from the Core Ledger study.

## 2. THE COST OBJECTS THAT EXIST IN PRACTICE

| # | De facto cost object | Introduced by | Has its own lifecycle? | Closes? | Reaches the ledger? |
|---|---|---|---|---|---|
| C1 | dimension value (cost centre, branch, generic) | the analytic layer itself | archive flag only | **no** | via allocation |
| C2 | project | project management | yes | yes (project stages) | via its bound dimension value |
| C3 | task | project management | yes | yes | no — dimension only |
| C4 | employee | human resources | yes | no | only through payroll, separately |
| C5 | department | human resources; on the analytic surface **only via a tenant custom extension** | yes | no | no |
| C6 | manufacturing order / work order | manufacturing | yes | yes | partially — see `P09_EVENT_TO_ANALYTIC_MATRIX` |
| C7 | work centre | manufacturing | master data | no | as a default allocation carrier |
| C8 | equipment | maintenance | yes | no | **no path at all** — §4 |
| C9 | sales order line | sales | yes | yes | via invoicing |
| C10 | asset | asset accounting | yes | yes | via depreciation |

**Ten de facto cost objects, one shared record type, no discriminator.** A management record does not say which of C1–C10 it is *about*; it says which fields happen to be populated.

## 3. THE PROJECT CASE — THE ONLY BOUND COST OBJECT

The project is the only cost object the reference pattern binds to the dimension structure, and it does so by privilege rather than by design: **one axis is singled out by a database-global system parameter** and mapped to a fixed column, and the project object binds to that axis (EV-P09-013).

Three properties follow:

1. the privileged axis is named by a parameter that is **global to the whole database**, not to a tenant or a company;
2. the reference pattern's own source states that the parameter cannot be changed safely after it is set without a manual database script (EV-P09-013);
3. every other axis is a runtime-created column and therefore carries none of the platform's relational protections (EV-P09-029).

**CO-01.** SMEsPlus shall not privilege one axis. Every axis shall be structurally identical, and any cost object shall be bindable to any axis by declared configuration.

**CO-02.** No analytic structural decision shall be expressed as a database-global parameter. Under the corrected scope constitution, an axis binding is at most TENANT-scoped; a database-global parameter is a PLATFORM-scoped artefact carrying a TENANT-scoped decision, which is a scope violation by construction.

## 4. THE EQUIPMENT CASE — THE DIRECTIVE'S EXPLICIT QUESTION

The P09 directive asks: **how should non-Asset Equipment costs be tracked?**

The evidence answers that the reference pattern offers no precedent.

| Question | Finding | Class |
|---|---|---|
| Does the maintenance equipment record carry a cost? | one bare untyped scalar, no currency, no company link | A |
| Does it link to any dimension, ledger entry or asset? | **not found in scope** — four maintenance-family modules, both code and view files, one combined pattern, zero matches | **B**, boundary fully declared (COR-P09-04) |
| Is there any equipment-to-accounting bridge at all? | yes, in a **tenant custom module**, and it runs backwards: the *asset* record points at the equipment record, and validating the asset writes a status value back onto the equipment | A within the custom roots (EV-P09-117) |
| Does that custom module carry dead code? | yes — a file in all three custom copies targets a model absent from the reference version, and **no copy imports it** | A (EV-P09-118) |
| How does machine time become cost? | only through the **work centre's** hourly rate and the work centre's own default allocation; work centres and equipment are unrelated objects with no field connecting them | A for the mechanism; B for the non-connection, boundary declared (EV-P09-119) |

**CO-03 — Determination.** Non-asset equipment cost has **no reference precedent**. SMEsPlus shall design it, and the design shall be recorded as an original architectural decision, not as a gap closed by imitation.

**CO-04 — Proposed shape.** An operational resource (equipment, vehicle, tool, facility) shall be a **first-class cost object** with:
- an identity independent of both the asset register and the maintenance register;
- an explicit relationship to an asset where one exists, and an explicit statement that none exists where it does not (the non-asset case is the *normal* case, not the exception);
- a costing basis declared on the object — rate-per-hour, rate-per-use, period charge, or none;
- a scope: **COMPANY** where its cost is attributable to a legal entity, TENANT where it is a shared operational resource whose cost is recharged;
- an internal-usage event that produces Operational Measurement Truth (T3) and, **only where an accounting event is declared**, a financial effect.

**CO-05 — Internal equipment usage** (the directive's "Internal Equipment Usage" item) shall be modelled as a usage event against a cost object, not as a direct write of a costed management record. The reference pattern writes the costed record directly from a duration change, up to three times for one hour of time, with no event and no journal counterpart (EV-P09-111).

## 5. THE COST OBJECT SPECIFICATION PROPOSED FOR SMEsPlus

| Property | Requirement |
|---|---|
| identity | mandatory, immutable, tenant-unique |
| type | mandatory, from a declared closed vocabulary (project, order, resource, responsibility centre, campaign, contract, other) |
| owning scope | mandatory: PLATFORM / TENANT / COMPANY; derived context requirements follow the scope, not a blanket rule |
| financial effect | declared: does cost on this object produce a financial effect, and if so which company owns it |
| lifecycle | open → active → closed → archived, with an explicit **closed** state |
| closing | closing a cost object shall block new management records against it, and shall be a dated event, not a flag |
| dimension binding | a cost object binds to one or more axes by configuration; no axis is privileged |
| budget | a cost object may carry a budget; see `P09_BUDGET_CONTROL_MODEL` |
| deletion | prohibited once referenced; retirement only |

**CO-06 — The closing state is the missing control.** None of the ten de facto cost objects in §2 prevents management records being written against it after it is finished, except by the producing document's own state machine. There is no cost-object-level close. Combined with the fact that a management record can be written against a **closed accounting period** with no barrier (`P09_EDGE_CASE_MATRIX` EC-02), this means management data has **no period control and no object control**.

## 6. SCOPE DETERMINATION FOR COST OBJECTS

Applying the corrected scope model:

| Cost object type | Owns the object | Executes cost capture | Financial effect owned by | Notes |
|---|---|---|---|---|
| responsibility centre (cost centre) | TENANT | COMPANY | the posting company | a tenant may run one cost-centre tree across companies |
| project | TENANT or COMPANY | COMPANY | the posting company | a cross-company project is TENANT-owned with company-scoped effects |
| operational resource / equipment | TENANT or COMPANY | COMPANY | the company that bears the charge | see CO-04 |
| manufacturing order | COMPANY | COMPANY | that company | a production order is a legal-entity artefact |
| contract / campaign | TENANT | COMPANY | the posting company | |

`OWNERSHIP ≠ AVAILABILITY` applies throughout: a TENANT-owned cost object is *available* to several companies, and each company's costs against it remain that company's financial truth.

**PEER DEPENDENCY OPEN — P03 (Manufacture-to-Cost) and P04 (Acquire-to-Retire) own the manufacturing-order and asset determinations respectively; P11 reconciles. P09 records its analysis and continues.**

## 7. TERMINAL STATE

**CO-01 … CO-06 ISSUED AS PROPOSALS. THE COST OBJECT IS DECLARED ABSENT FROM THE REFERENCE PATTERN AND MUST BE AUTHORED. NO GATE MOVED.**
