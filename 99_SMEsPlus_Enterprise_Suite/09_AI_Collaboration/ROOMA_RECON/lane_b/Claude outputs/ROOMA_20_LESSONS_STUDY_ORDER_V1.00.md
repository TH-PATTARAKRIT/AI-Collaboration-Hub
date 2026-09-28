# ROOM A — 20 LESSONS · STUDY ORDER
## What must be understood before the next thing makes sense

**Version:** V1.00 DRAFT
**Date:** 2026-09-22 · Asia/Bangkok
**Drafted by:** RED TEAM (internal audit)
**Status:** `PREPARED ONLY / READY FOR INDEPENDENT REVIEW`
**Origin:** Boss instruction, 2026-09-22 — *"เอาบทเรียน ๒๐ บทมากาง … อะไรเป็น base ก็ควรทำก่อน
เพื่อให้เข้าใจตรงกัน เพราะว่าทุกคนอ้างอิงเหมือนกัน"*

---

## 1. Why this replaces the earlier ordering proposals

Three orderings have been proposed for ROOM A. They disagree.

| Proposal | Unit | Problem |
|---|---|---|
| RED TEAM — by `COMM_Group` | module family | Cuts the seams. `stock_account` lands in G04, `account` in G05, so the inventory↔accounting bridge can never be tested. |
| Boss — by station (A/B/C/D) | business flow | Correct for the value chain, but covers only 108 of 300 modules, and business-flow order conflicts with technical dependency order at bridge modules. |
| **Boss — by lesson** | **concept** | **Resolves both.** A concept is studied once, and every station afterwards references the same understanding. |

### The finding that settles it

`account` is **not one thing**. Part of it is foundation and part is process:

| Concept | Nature | Referenced by |
|---|---|---|
| Chart of accounts, journals, taxes, periods, numbering | **FOUNDATION** | Sale, Purchase, Warehouse, Payroll, Project — everyone |
| Invoice lifecycle, payment matching, reconciliation | **PROCESS** | the accounting station itself |

The same is true of `stock`: **locations and warehouse structure are foundation; goods movement is process.**

A station model cannot express this, because a station owns a whole module. A lesson model can,
because a lesson owns a concept. This is exactly what Boss meant by *"ทุกคนอ้างอิงเหมือนกัน"*.

---

## 2. Evidence — an ordering already exists in the project and nobody cited it

`99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/FDS/02_BUSINESS_CONTEXT.md` §2 already records
a Module Priority Context:

| Priority | Modules |
|---|---|
| 1 | SaaS Foundation, Accounting, Purchase, Inventory |
| 2 | Sales, CRM, Product |
| 3 | Manufacturing, HR, Payroll |
| 4 | Remaining |

`⚠️ REPORTED — not re-verified in this session, and its approval status is "Draft — In Review".`

Two observations RED TEAM must record:

1. **It broadly agrees with the lesson order below** — foundation, then accounting/purchase/inventory,
   then sales, then manufacturing and HR. That is supporting evidence, not RED TEAM's invention.
2. **It disagrees on one point:** it puts Product in Priority 2, while every lesson model — and
   Odoo's own dependency graph — makes Product foundation. Sale cannot be studied before Product.

The same document also refers to **"14 module groups"**, while `COMM_Group` in Baseline V1.00 has
**10**. Two different group counts exist in the project. `RT-LES-003` below.

---

## 3. THE 20 LESSONS

Ordering rule: a lesson may only depend on lessons before it.

### PART I — FOUNDATION (L01–L10)
*Everything after this references these. Study once, reference forever.*

| # | Lesson | Why it is foundation | Primary evidence modules |
|---|---|---|---|
| **L01** | **Scope hierarchy** — tenant, company, branch, division | Every record belongs to a scope. Get this wrong and every later lesson is wrong. Constitution §3.3. | `base`, `base_setup` |
| **L02** | **Identity and access** — user, role, permission, record rules | Determines what any later observation is even able to see. | `base`, `auth_*` |
| **L03** | **Partner** — customer, vendor, employee as one entity | Sale, Purchase and HR all point at the same object. | `contacts`, `base_address_extended`, `partnership` |
| **L04** | **Product and category** | The thing that is sold, bought, stored and costed. | `product`, `product_matrix` |
| **L05** | **Unit of measure and conversion** | Quantity is meaningless without it. `STD-Q35`. | `uom` |
| **L06** | **Chart of accounts and journals** | The destination of every posting in every later lesson. | `account` (foundation part) |
| **L07** | **Taxes — definition** (VAT, withholding) | *How tax is defined*, not yet how a document applies it. | `account`, `base_vat`, `l10n_th`, `l10n_account_withholding_tax` |
| **L08** | **Currency, rate, rounding** | Where rounding lands is a foundation decision, not a per-document one. | `base`, `account` |
| **L09** | **Document numbering and sequences** | Statutory. Every business document depends on it. `STD-Q26`. | `base`, `account` |
| **L10** | **Periods, fiscal year and lock dates** | Defines when anything may be posted at all. `STD-Q18`. | `account` |

### PART II — STRUCTURE BEFORE MOVEMENT (L11–L12)

| # | Lesson | Why here | Primary evidence modules |
|---|---|---|---|
| **L11** | **Warehouse and location structure** | The map must exist before anything moves on it. | `stock` (structure part) |
| **L12** | **Analytic and cost attribution** | Cost has to land somewhere; decided before costs are generated. | `analytic` |

### PART III — THE TWO VALUE CHAINS (L13–L17)

| # | Lesson | Why in this position | Primary evidence modules |
|---|---|---|---|
| **L13** | **Goods movement** — stock moves, reservation, shortage | Uses L04, L05, L11. Still no accounting yet. `STD-Q31`, `STD-Q32`, `STD-Q34`. | `stock`, `stock_picking_batch`, `barcodes` |
| **L14** | **Inventory valuation — the bridge** | 🔴 Joins L13 to L06. **The single highest-risk lesson in the whole programme.** `STD-Q33`. | `stock_account`, `stock_landed_costs` |
| **L15** | **Purchase to Pay** — PR → PO → receipt → bill | Needs L03, L04, L13, L14, L06, L07. | `purchase*`, `purchase_stock` |
| **L16** | **Order to Cash** — quotation → order → delivery → invoice | Same dependencies as L15, opposite direction. | `sale*`, `sale_stock`, `crm` |
| **L17** | **Payment and reconciliation** | Closes both chains. | `account_payment`, `payment`, `account` |

### PART IV — DERIVED AND CROSS-CUTTING (L18–L20)

| # | Lesson | Why last | Primary evidence modules |
|---|---|---|---|
| **L18** | **Manufacturing** — BoM, work order, cost roll-up | A consumer of L13, L14, L15. Cannot be understood before them. | `mrp*` |
| **L19** | **Approval, execution and posting separation** | The SMEsPlus mandate (§3.2). Must be observed **across** the chains, so it comes after them. `STD-Q11`–`STD-Q14`. | cross-cutting |
| **L20** | **Audit trail, closing and reporting** | What the whole system must be able to prove afterwards. `STD-Q22`, `STD-Q30`. | `account`, `board`, `spreadsheet_*` |

---

## 4. What the lessons do not cover, and where it goes

Three streams sit outside this 20 because they are separate value chains or platform concerns.
They get their own ordering after L20, not squeezed into it.

| Stream | Modules | Note |
|---|---|---|
| **People** — Hire → Work → Pay | ~31 (`hr*`, `fleet`) | A value chain of its own. Depends on L01–L03, L06, L12. |
| **Project delivery** | ~14 (`project*`) | Depends on L12, L16. |
| **Platform and channel** | ~130 (`web*`, `theme_*`, `mail*`, technical) | Not business concepts. `theme_*` scope still undecided — `T6`. |

---

## 5. How a lesson maps to the work already agreed

Nothing already decided changes. The lesson is the **sequencing** layer; the question bank is the
**depth** layer.

```
LESSON  (order — what is studied when)
   └── MODULE  (unit — from Baseline V1.00)
         ├── STANDARD 35   answered for every module
         └── MODULE-SPECIFIC ≥40   authored by Tester + Odoo Functional
              → combined floor ≥75 per module   (Boss rules ๑–๔, V7: no tiering)
```

Handoff questions raised in one lesson and answerable only in a later one go into
`HANDOFF_QUESTION_REGISTER`. **A lesson cannot be closed while a handoff it raised is still open.**

---

## 6. Proposed wave plan by lesson

| Wave | Lessons | Character | Modules (approx.) |
|---|---|---|---|
| **W1** | L01–L10 | Foundation. Everyone references it. **Do not start anything else first.** | ~35 |
| **W2** | L11–L14 | Structure, movement, and the valuation bridge | ~30 |
| **W3** | L15–L17 | P2P, O2C, payment | ~75 |
| **W4** | L18–L20 | Manufacturing, separation, audit and closing | ~30 |
| **W5** | People stream | | ~31 |
| **W6** | Project stream | | ~14 |
| **W7** | Platform and channel | pending `T6` | ~85 |

**W1 and W2 together are the load-bearing part of the programme.** If the model is going to fail,
it fails there, and failing there early is cheap.

---

## 7. Gaps, risks and blockers

| ID | Item | Severity |
|---|---|---|
| `RT-LES-001` | The lesson order is RED TEAM's proposal. It agrees with the project's existing Priority Context on most points but is not itself evidence. | PROCESS |
| `RT-LES-002` | The existing Priority Context places Product at Priority 2; the dependency graph places it in foundation. One of the two is wrong. | MEDIUM |
| `RT-LES-003` | `02_BUSINESS_CONTEXT.md` refers to **14 module groups**; Baseline V1.00 `COMM_Group` has **10**. Two group counts exist in the project and nobody has reconciled them. | MEDIUM |
| `RT-LES-004` | `account` and `stock` each appear in both a foundation lesson and a process lesson. The register has one row per module, so a module-level status cannot express "foundation part done, process part not". A `LESSON` tag per answer is required. | MEDIUM |
| `RT-P3-001` | **WITHDRAWN 2026-09-22 — raised in error.** TECHNOLOGY_STACK_STANDARD v1.0 (Approved Baseline, 2026-07-06) §25 already replaced "Odoo-first" with "Open ERP-first"; §4/§24 mandate FastAPI/Python 3.12; ADR-0006 already ruled "not the Odoo runtime … Concept Match only". No conflict existed. | **WITHDRAWN** |
| `RT-P3-002` | Backend runtime is an open decision, not a conflict — Baseline §24 says FastAPI/Python, ALL TEAM D1 proposes Node.js, study still running. ROOM A output is runtime-neutral (Concept Match only). Architecture Review due before ROOM B build, not before ROOM A study. | DECISION POINT |
| `RT-GOV-001` | Claude Project Instructions §3.1 still reads "Odoo-first", contradicting the Approved Baseline. Every new AI session inherits the stale term. | **HIGH — open, owner Boss** |

---

## 8. Boss decisions required

| # | Question | Options |
|---|---|---|
| **L-1** | Adopt lessons as the sequencing layer, above stations and above `COMM_Group` | ADOPT / REJECT |
| **L-2** | Is Product foundation (L04) or Priority 2 as the existing document says | FOUNDATION / PRIORITY-2 / defer to ALL TEAM |
| **L-3** | Reconcile 14 groups versus 10 `COMM_Group` | RED TEAM investigates / PMO investigates / defer |
| **L-4** | Add a `LESSON` tag to every answer record (`RT-LES-004`) | ADOPT / REJECT |
| **L-5** | Start at W1 (L01–L10) | YES / start elsewhere |

---

```text
This output is a draft for independent review only.
It is not Boss Final Approval.
RED TEAM drafted this ordering and therefore cannot certify it.
The Module Priority Context cited in §2 is REPORTED, not independently re-verified.
```
