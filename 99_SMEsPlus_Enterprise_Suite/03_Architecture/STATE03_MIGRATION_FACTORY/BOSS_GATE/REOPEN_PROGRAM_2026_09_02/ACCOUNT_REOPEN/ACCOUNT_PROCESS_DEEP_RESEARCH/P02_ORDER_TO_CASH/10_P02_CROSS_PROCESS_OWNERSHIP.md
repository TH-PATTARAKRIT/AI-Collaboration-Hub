# 10 — P02 CROSS-PROCESS OWNERSHIP AND DEPENDENCY REGISTER

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`
Scope model per correction `SMEPLUS-26-09-04-ACC-REV2-CORR1`. See `20_P02_SCOPE_OWNERSHIP_MATRIX.md`.

## 1. Ownership Register — Who Owns Each Fact P02 Touches

`OWNS` = defines the semantics and is the single source of truth.
`CONSUMES` = reads it and must not redefine it.
`CONTRIBUTES` = produces evidence or a requirement for the owner, without deciding.

| Fact | Owner process | P02's role | Scope | Status |
|---|---|---|---|---|
| Customer identity and commercial standing | CRM / Master Data | CONSUMES | TENANT | — |
| Product identity and classification | Master Data | CONSUMES | TENANT | — |
| **Product cost and costing method** | **Inventory** | CONSUMES | COMPANY | `DEPENDENCY OPEN` — see D-01 |
| **Inventory quantity and availability** | **Inventory** | CONSUMES | COMPANY | — |
| **Inventory valuation layers** | **Inventory** | CONSUMES | COMPANY | `DEPENDENCY OPEN` — D-01 |
| **Cost-of-sales recognition policy** | **Core Accounting** (contested) | **CONTRIBUTES** | COMPANY | `HOLD — CROSS-PROCESS RECONCILIATION REQUIRED` — X-01 |
| Reservation and allocation | Inventory | CONSUMES | COMPANY | — |
| **Outflow event (goods leave)** | **P02 jointly with Inventory** | **CO-OWNS** | COMPANY | see §2 |
| **Revenue recognition** | **P02** | **OWNS** | COMPANY | — |
| **Receivable creation** | **P02** | **OWNS** | COMPANY | — |
| **Output tax on a sale** | P02 raises it; **Core Accounting / Tax owns the treatment** | CONTRIBUTES | COMPANY | `HOLD — STATUTORY EVIDENCE REQUIRED` |
| **Withholding suffered on a receipt** | **Core Accounting / Tax** | CONTRIBUTES | COMPANY | `HOLD — STATUTORY EVIDENCE REQUIRED` — S-03 |
| Settlement and matching | **Core Accounting** | CONSUMES | COMPANY | — |
| **Exchange rate source and application** | **Core Accounting** | CONTRIBUTES | **held** | `HOLD — SCOPE EVIDENCE REQUIRED` — SC-01 |
| **Chart of accounts and account roles** | **Core Accounting** | CONTRIBUTES | **held** | `HOLD — SCOPE EVIDENCE REQUIRED` — SC-02 |
| Period close and lock policy | **Core Accounting** | CONSUMES | COMPANY | — |
| **Vendor-side mirror of the return/credit pattern** | **P01** | — | COMPANY | `PEER DEPENDENCY OPEN` — D-05 |
| Intercompany pairing | **P11** (cross-process reconciliation) | CONTRIBUTES | **held** | `HOLD — SCOPE EVIDENCE REQUIRED` — SC-03 |

## 2. The One Genuinely Shared Event

**`FACT VERIFIED` — the outflow is the only event P02 co-owns.** Inventory owns *the goods left*.
P02 owns *the sale occurred*. In the reference these are the same record, and that is exactly where the
`ONE BUSINESS FACT → ONE CANONICAL EVENT OWNER` invariant is hardest to hold.

**`DESIGN CANDIDATE` DC-10-01.** The clean split:

- **Inventory owns the outflow** — quantity, location, timing, valuation layer, and the inventory-relief
  entry. P02 may not create, alter, or re-value an outflow.
- **P02 owns the obligation** — that a delivered unit is now billable and its cost is now attributable to
  a sale.
- The two are connected by an **obligation ledger** that Inventory writes into and P02 consumes from, in
  which each unit is **relieved exactly once and attributed exactly once**.

This one structure resolves, at the root, six of the findings in this package: the two competing delivered
quantities, the two competing cost derivations, the missing outbound-stock owner, the double-valuation
class, the unpicked-completion hole, and the invoice-quantity coupling into cost.

## 3. Dependency Register

| ID | Depends on | Statement | Blocks | Status |
|---|---|---|---|---|
| **D-01** | **Inventory — COGS** | The cost-of-sales recognition design is not settled. The Inventory COGS Deep Research closed at terminal HOLD with the headline that the reference's own perpetual pattern is **unstable across versions**, and the targeted resolution round closed at PARTIAL RESOLUTION with its joint-closure inputs content-empty. | Every cost conclusion in `03_P02_DELIVERY_COGS_TRACE.md` | `DEPENDENCY OPEN` |
| **D-02** | **Inventory — multi-tenant invariants** | The invariant set and its ruling-conformance package define the boundary rules P02's outflow consumption must satisfy. P02 does **not** restate or re-adjudicate them. | `20_P02_SCOPE_OWNERSHIP_MATRIX.md` SF-04 | `DEPENDENCY OPEN` |
| **D-03** | **Core Accounting — Wave A** | Four Wave A findings are confirmed independently from the O2C side and are **not** re-adjudicated here: the silent 1:1 FX fallback, the system-derived accounting date, the absence of a year-close entry, and the absence of event identity. | `09` §4, `01` S7, `06` §3, `05` §3 | `DEPENDENCY OPEN` |
| **D-04** | **Core Accounting — GB-08 FX ruling** | A Boss ruling on FX rate ownership and missing-rate policy exists. P02 adds arm 2 of the fallback (the undated earliest-rate arm), which is more likely and less visible than the 1:1 arm the ruling addressed. | `09` §4 | `DEPENDENCY OPEN` — **material delta supplied** |
| **D-05** | **P01 — Procure-to-Pay** | The vendor-side mirror: whether the purchase return / debit-note pair shows the same structural independence, and whether the inbound interim account has the owner the outbound one lacks. The Thai chart **does** supply an inbound interim account and **not** an outbound one, which suggests the two sides are not symmetric. | `07` §5, `08` §10 | `PEER DEPENDENCY OPEN` — **P02 continues; this blocks only the symmetry conclusion** |
| **D-06** | **P11 — cross-process scope reconciliation** | The three scope holds. | `20` §4, §5, §6 | `PEER DEPENDENCY OPEN` |
| **D-07** | **Accounting-Tax track** | Eight Thai statutory questions, each with its named sources. | `11` §7 | `HOLD — STATUTORY EVIDENCE REQUIRED` |

**Per the correction's cross-process rule, none of D-01 … D-07 stopped this session.** Each blocks only
the specific conclusion named in its "Blocks" column. All unaffected work was completed.

## 4. What P02 Hands To Core Accounting Reconciliation

| # | Handoff | Type |
|---|---|---|
| H-01 | The **obligation-ledger requirement** (§2) — the single structural change that resolves six findings. | requirement |
| H-02 | The **five missing account roles** and the requirement that *goods delivered not invoiced* be a controlled subledger with mandatory ageing and a close gate. | requirement |
| H-03 | The **six competing date rules** across 13 accounting events, and the requirement for one declared rule per event class with occurrence and recognition dates carried separately. | requirement |
| H-04 | The **lock-date semantics finding**: the reference's lock is a period *redirect*, not a period *bar*; it is bypassable by an all-users no-expiry exception and by a context sentinel used in partner merge; and it does not gate the matching state at all. | evidence + requirement |
| H-05 | The **FX evidence**, including arm 2 of the fallback. | evidence |
| H-06 | The **cost-of-sales configuration trap** — three reachable outcomes, of which the third recognises cost **nowhere**, and is the Thai-chart default shape. | evidence + `BOSS CONTROLLED DECISION` |
| H-07 | The **down-payment-to-revenue fallback** and the requirement that a customer advance be a contract liability by construction. | evidence + requirement |
| H-08 | The **eight Thai statutory questions** with their named sources. | routed hold |
| H-09 | The **three scope holds** (rate, chart, intercompany). | routed hold |
| H-10 | The **complete P02 evidence base** — four track extracts, 69 evidence identifiers, all denominators declared. | evidence |

## 5. What P02 Does NOT Decide

Stated explicitly so that no downstream reader mistakes contribution for decision:

- P02 does **not** decide when cost of sales is recognised. It establishes what the choice costs.
- P02 does **not** decide the chart of accounts. It states which roles must exist.
- P02 does **not** decide FX rate ownership. It supplies the O2C-side evidence.
- P02 does **not** decide any Thai statutory question. It names the sources that must be read.
- P02 does **not** adjudicate between the Inventory COGS track and the Core Accounting track. That
  reconciliation is Boss-level.
- P02 does **not** declare any gate satisfied, any module ready, or any implementation authorised.
