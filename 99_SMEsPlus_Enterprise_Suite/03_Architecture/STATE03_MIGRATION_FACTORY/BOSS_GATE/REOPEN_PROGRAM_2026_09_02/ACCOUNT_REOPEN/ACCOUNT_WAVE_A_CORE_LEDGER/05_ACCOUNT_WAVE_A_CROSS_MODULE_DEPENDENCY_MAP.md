> **CORR1 CORRECTION NOTICE.** Amended by session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`.
> Corrections landing here: `COR-20`. Governing text where they conflict with the body below: CORR1/C02; statutory consequence HOLD to WAVE-D TAX.
> Prior findings are retained unedited for lineage; see `CORR1/C02_..._ACCEPTED_CORRECTIONS_REGISTER.md`.

# 05 — LEVEL 4: CROSS-MODULE ACCOUNTING DEPENDENCY MAP

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

## Scope discipline

Wave A investigated other domains **only far enough to establish what the core ledger must be able to
receive**. It does not decide any other Wave's semantics, and it does not usurp any other Wave's
Final Research Gate. Every row below is classified with its owning Wave.

Evidence in this file is of three kinds and is never merged:
- `EV-0NN` — primary source read this session;
- `PRIOR` — a prior SMEsPlus session's recorded finding, cited with its own terminal state;
- `UNKNOWN — EVIDENCE REQUIRED` — not established.

## 1. Producer → Event → Accounting consumer → Reporting consumer

| Producer | Business event | Recognition trigger | Accounting consumer in Wave A | Reporting consumer | Wave | Evidence |
|---|---|---|---|---|---|---|
| Sales | Customer invoice issued | document validation | entry in a sale journal; receivable item; **sale lock date applies** | revenue, receivable ageing | `WAVE-B AR` | `EV-008` |
| Sales | Credit note | document validation | reversing/contra entry; auto-matched where it cancels | revenue, ageing | `WAVE-B AR` | `EV-012` |
| Purchase | Vendor bill received | document validation | entry in a purchase journal; payable item; **purchase lock date applies** | expense, payable ageing | `WAVE-C AP` | `EV-008` |
| Payment / Banking | Cash received or paid | payment registration | liquidity item + counterpart; **reconciliation against the open item** | cash position, ageing, payment state | `WAVE-H BANKING` | `EV-014` |
| Payment / Banking | Bank statement line matched | matching | reconciliation record; possibly a suspense clearing entry | bank reconciliation | `WAVE-H BANKING` | `EV-014`, `EV-019` |
| Any settlement in foreign currency | Settlement at a different rate | full or partial match | **exchange difference entry, emitted by reconciliation** | FX gain/loss | Wave A owns; presentation `WAVE-G` | `EV-014` |
| Tax engine | Tax becomes reportable | posting, or cash-basis on settlement | tax items on the entry; **cash-basis tax entries emitted by reconciliation** | tax return | `WAVE-D TAX` | `EV-015` |
| Tax engine | Tax return posted | return closing | an entry, **and the tax lock date is set automatically** | tax return | `WAVE-D TAX` | `EV-008` |
| Inventory | Goods received / issued / valued | receipt, issue, or valuation event | valuation and offset items | inventory valuation, COGS | Inventory domain | `PRIOR` — Inventory v2.0 is `HELD` on an unresolved cost-of-sales dependency |
| Inventory | Cost of sales recognised | delivery or period cost run | cost item against the revenue period | gross margin | Inventory domain | `PRIOR` — COGS Deep Research `ERPPLUS-142` terminal `HOLD`; targeted resolution reached `PARTIAL RESOLUTION`, three questions `NOT DECIDABLE` |
| Assets | Depreciation charge | period run | expense and accumulated-depreciation items | asset schedule, expense | Asset domain | `PRIOR` — Asset Deep L1–L6, terminal state B, two incompatible day conventions selected by one untracked setting |
| Assets | Disposal | disposal event | derecognition and gain/loss items | asset schedule | Asset domain | `PRIOR` |
| Manufacturing | Production order completion | completion | work-in-progress to finished-goods valuation | production cost | Inventory/Manufacturing | `PRIOR` — production cost chain links 2–6 exist; rate derivation from depreciation and the equipment dimension are missing |
| Expense | Employee expense approved | approval | payable item and expense item | expense reporting | `WAVE-C AP` | `UNKNOWN — EVIDENCE REQUIRED` |
| Deferred recognition | Revenue or cost spread over time | period run | periodic reclassification entries | deferral schedules | `WAVE-F TIME-BASED RECOGNITION` | `UNKNOWN — EVIDENCE REQUIRED` |
| Analytic accounting | Management attribution | posting | **derived from the item's analytic distribution** | management reporting | `WAVE-E ANALYTIC` | `EV-012` |
| Budget | Budget line consumed | posting | none — budget consumes the ledger, it does not produce entries | budget vs actual | `WAVE-E ANALYTIC` | `INFERENCE` |
| Multi-company | Shared account used by a second company | posting | the same account, a different per-company code | consolidated reporting | Wave A + `WAVE-G` | `EV-001` |

## 2. What Wave A must be able to receive — the minimum producer contract

Derived from the Wave A evidence, not assumed. Any producing module must supply, per accounting
event:

| Element | Why Wave A needs it | Evidence |
|---|---|---|
| A stable **source-event identity**, unique and idempotent | Wave A found **no business-level duplicate-event guard**; number uniqueness at posting is the only protection, and it does not detect the same business event posted twice under two numbers | `GAP-C03`, `EV-006` |
| The **intended accounting date**, separate from the document date | Because the lock mechanism will silently move the accounting date, the producer's intent must be recorded before that happens | `EV-009` |
| The **transaction currency and the rate basis**, not just a converted amount | Every item carries a currency unconditionally; a converted-only amount cannot be revalued or settled correctly | `EV-013`, `EV-018` |
| The **counterparty** where the posting touches a subledger account | Subledger-to-control agreement depends on it | `EV-014` |
| The **analytic distribution as intent**, not as generated lines | Generated analytic lines are destroyed on un-post and regenerated; the intent must survive | `EV-012` |
| An explicit statement of **which items are open items** | Reconcilability is an account property, but open-item intent belongs to the producer | `EV-014` |
| The **reversal or correction policy** for this event type | Wave A's default correction path is destructive; producers must not rely on it | `EV-012` |

`RECOMMENDATION:` this list is the Wave A input to the Account × Inventory minimum handoff data
contract that already exists in the repository as a Boss-approved item. It should be reconciled
against that contract rather than replacing it — that reconciliation is itself a Boss-level decision
because the two tracks were produced independently.

## 3. What Wave A produces for others

| Consumer | What it reads | Constraint Wave A imposes |
|---|---|---|
| Financial reporting (`WAVE-G`) | items, accounts, account types, periods | The year boundary is **derived from an account-type property**, not from a closing posting (`EV-016`) |
| Tax reporting (`WAVE-D`) | tax items, tax lock date | Entries generated for a locked period land in the **current** period (`EV-015`) |
| Ageing and collections (`WAVE-B`, `WAVE-C`) | residual, due date, maximum match date | Residual is stored-computed and must be reconstructible (`EV-014`) |
| Management reporting (`WAVE-E`) | analytic lines | These are derived and destructible (`EV-012`) |
| Banking (`WAVE-H`) | liquidity items, matching | Bank reconciliation completeness is a **precondition of locking** (`EV-019`) |
| Audit and assurance | entries, numbering, hashes, tracking | Immutability is configuration, not a ledger property (`EV-011`) |

## 4. Dependency risks carried out of Wave A

| # | Risk | Owning Wave | Status |
|---|---|---|---|
| `XM-01` | No business-level idempotency for machine-generated events | Wave A + all producers | `HOLD — DESIGN DECISION REQUIRED` |
| `XM-02` | Generated tax and FX consequences relocate to the current period when their own period is locked, crossing year boundaries | `WAVE-D TAX` | `HOLD / EVIDENCE REQUIRED` — Thai period-attribution consequence must be assessed by the Accounting-Tax track |
| `XM-03` | Analytic attribution is destroyed and regenerated by an ordinary correction | `WAVE-E ANALYTIC` | Raised; decision belongs to Wave E |
| `XM-04` | Cost-of-sales dependency remains unresolved from prior sessions and constrains what the ledger can assert about gross margin | Inventory | `PRIOR` — remains `PARTIAL RESOLUTION`; Wave A does not reopen it |
| `XM-05` | Asset depreciation day-convention ambiguity affects the amount posted to the ledger | Asset | `PRIOR` — the top open blocker recorded there is that the computation mode was never captured from the running system |
| `XM-06` | Account-module gates from the prior Batch A routing session remain open, including the chart-of-accounts gate that blocks four others | Account | Wave A supplies evidence toward them but **moves no gate** |

## CHECKPOINT L4

| Item | Record |
|---|---|
| Scope completed | Producer→event→consumer tracing across 12 producing domains; minimum producer contract derived from evidence; six carried risks |
| Evidence inspected | `EV-001`, `EV-006`, `EV-008`, `EV-009`, `EV-011`–`EV-019`; prior-session findings cited with their own terminal states |
| Verified findings | Reconciliation is a *producer* of accounting events, not only a consumer; the tax lock is set automatically by a downstream process; bank reconciliation completeness gates period locking |
| Contradictions | `CONTRA-04` reinforced — generated consequences can be attributed to the wrong period |
| Unknowns | Expense and deferred-recognition producer contracts not established this session |
| Risks | `XM-01` idempotency is the most serious, because it has no partial mitigation |
| Expert disagreements | Expert 3 review commissioned specifically on localization and integration |
| Audit challenges | Challenge unit tasked to find wrong source-of-truth assumptions in this map |
| Next research target | Level 5 — whole-system semantic model |

`CHECKPOINT L4 RECORDED — CONTINUING AUTOMATICALLY.` Not Boss approval.
