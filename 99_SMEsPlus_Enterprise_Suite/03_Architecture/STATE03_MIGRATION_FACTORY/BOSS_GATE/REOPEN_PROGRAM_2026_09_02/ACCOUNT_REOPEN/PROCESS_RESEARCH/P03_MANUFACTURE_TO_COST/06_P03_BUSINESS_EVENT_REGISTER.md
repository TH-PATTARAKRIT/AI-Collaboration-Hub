# 06 — P03 BUSINESS EVENT REGISTER

**LAYER 2 — AUDIT QUARANTINE.**

A business event is a fact about the world. It has exactly one owner. This register
establishes ownership before any accounting effect is discussed.

---

## 1. Register

| ID | Business event | Owner (single) | Evidence that it occurred | Tenant/company carrier | Class |
|---|---|---|---|---|---|
| `BE-01` | Demand for a manufactured item arises | Demand source (sales order, reorder rule, forecast) | The procurement group | On the MO | `FACT VERIFIED` |
| `BE-02` | A manufacturing order is created | MO | MO record, state `draft`/`confirmed` | `company_id` on the MO | `FACT VERIFIED` |
| `BE-03` | A BOM version is chosen | MO | `bom_id` on the MO | inherited | `FACT VERIFIED` |
| `BE-04` | Work is scheduled to a resource | Work order | Work order + calendar leave | inherited | `FACT VERIFIED` |
| `BE-05` | **Material is physically issued to production** | Raw stock move | Move in state `done`, `picked = true` | on the move | `FACT VERIFIED` |
| `BE-06` | **A person spends time on an operation** | Time log | Time log with start, end, employee | on the time log | `FACT VERIFIED` |
| `BE-07` | **A machine is occupied for a period** | **No owner** | **None — see §3** | — | `FACT VERIFIED`, scope in `02` §3 |
| `BE-08` | Work is interrupted, for a stated cause | Time log + blocking reason | Log with a non-productive category | on the log | `FACT VERIFIED` |
| `BE-09` | Good units are produced | Finished move | Move `done`, quantity | on the move | `FACT VERIFIED` |
| `BE-10` | A by-product emerges | By-product move | Move with a cost share | on the move | `FACT VERIFIED` |
| `BE-11` | Material or output is scrapped | Scrap record → move | Scrap record | on the move | `FACT VERIFIED` |
| `BE-12` | Work is subcontracted and returns | Subcontract receipt | Receipt move, `is_subcontract` | on the move | `FACT VERIFIED` |
| `BE-13` | The order is partially completed | MO + backorder MO | Backorder sequence | inherited | `FACT VERIFIED` |
| `BE-14` | The order is cancelled | MO | State `cancel` | inherited | `FACT VERIFIED` |
| `BE-15` | A completed order is undone | Unbuild order | Unbuild record | on the record | `FACT VERIFIED` |
| `BE-16` | **A period ends with work in progress** | **No owner** | **A transient wizard, not a record — see §4** | — | `FACT VERIFIED` |
| `BE-17` | Output is rejected and reworked | **No owner — no object exists** | **None** | — | `FACT VERIFIED`, scope in `11` §3 |

## 2. Ownership test

Seventeen events. **Fourteen have exactly one owner.** Three do not:

| Event | Problem |
|---|---|
| `BE-07` machine occupancy | No owner, and it is the event that machine cost must be causally attached to |
| `BE-16` period-end WIP | Owned by a transient wizard that reverses its own output |
| `BE-17` rework | No object at all |

## 3. `BE-07` — the event that carries no evidence

`ASSET_DR_CONTINUATION/07` §2 established this from the asset side: every measurement in
the reference product resolves to a **work centre**, never to a machine — not on the
operation, not on the work order, not on the time log.

P03 confirms it from the cost side and adds the consequence:

> Machine cost is charged **as a function of human time logs**. A machine running
> unattended generates no time log and therefore no cost. A machine idle while two people
> stand at it generates two hours of machine cost (`DC-01`).
>
> **Machine cost in the reference product is not causally connected to machine use.**

`FACT VERIFIED`. This is the cost-causality finding the prompt's *Cost Causality Forensic*
extension asks for, and it is the reason `04` `R-01` exists.

## 4. `BE-16` — a period-end fact owned by a transient

The WIP wizard (`mrp_account/wizard/mrp_wip_accounting.py`) is a `TransientModel`. Its
output is an entry that is immediately paired with a reversal at `:146-150`.

Therefore:
- There is **no durable record** that a period-end WIP position was ever determined.
- Its inputs are recomputed on demand (`:117-122`), never stored.
- Re-running it for the same date creates a **second** entry; nothing prevents it.

**A period-end business fact with no event identity.** This is the same class as the "no
event identity" finding in `smeplus-account-wave-a-core-findings`, reached independently
in the manufacturing domain. `FACT VERIFIED`.

## 5. Scope analysis

**Revised under `SMEPLUS-26-09-04-ACC-REV2-CORR1`.** The original text of this section
asserted that tenant and company context are required for every event. That is
over-constrained. Applying the canonical scope model instead:

| Event class | Scope | Context required |
|---|---|---|
| `BE-01` … `BE-04` — demand, MO creation, BOM choice, scheduling | `COMPANY` for the MO; **`TENANT`** for the BOM and routing it selects | Tenant always; company for the MO |
| `BE-05` … `BE-15` — every event with a financial effect | **`COMPANY`** | Tenant **and** company mandatory |
| `BE-16` — period-end WIP | **`COMPANY`** | Tenant and company mandatory |
| Reference taxonomies the events cite | `PLATFORM` candidate | Neither |

The full determination is `18_P03_SCOPE_OWNERSHIP_MATRIX.md`. The material consequence
for this register is that **`BE-03` selects a `TENANT`-scoped object (`SCOPE-01`) into a
`COMPANY`-scoped event**, and the reference product's company-less BOM makes that
selection unowned.

Every event in §1 carries a company through its own record, and `check_company` guards are
present on the configuration fields. **Two exceptions found, both in the `COMPANY` scope
class where company context is mandatory:**

| Exception | Detail |
|---|---|
| `DC-11` | `_post_labour` resolves company-dependent accounts in the acting user's company, not the MO's — `05` §4 |
| `BE-16` | The WIP wizard reads `self.env.company` (`:71`, `:105`) and company-dependent fallbacks (`:75-78`), never an MO's company, while accepting MOs from a multi-company selection |

Both are routed to the Inventory multi-tenant invariant conformance track, not resolved
here — `14_P03_DEPENDENCY_REGISTER.md` `DEP-05`.
