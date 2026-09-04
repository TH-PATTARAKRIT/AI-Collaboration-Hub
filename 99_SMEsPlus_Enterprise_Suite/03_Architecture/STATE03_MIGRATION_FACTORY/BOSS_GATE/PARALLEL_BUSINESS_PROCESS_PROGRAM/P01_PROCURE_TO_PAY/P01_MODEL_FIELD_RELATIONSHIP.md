# P01 — MODEL / FIELD RELATIONSHIP MAP

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.** Object names below are business names.

Per `§2.6`, the physical schema is **supporting** evidence. The primary trace is
Object → Relationship → Function → Business Event → Accounting Event.

---

## 1. THE OBJECT CHAIN

```
Vendor  ──┐
          ├─→ Purchase Order ──→ Order Line ──┬──→ Stock Movement ──→ Valuation Layer ──→ Journal Entry
Item ─────┘                                   │                            ▲                    ▲
   │                                          │                            │                    │
   └─→ Item Category ──(company-dependent)────┼──→ Account Map ────────────┘                    │
                                              │                                                 │
                                              └──→ Bill Line ──→ Vendor Bill ────────────────────┘
                                                       │              │
                                                       │              └──→ Payable Line ──→ Reconciliation ──→ Payment
                                                       │                                          │
                                                       └──→ Asset (auto, at posting)              └──→ FX Difference Entry
```

## 2. THE LINKS THAT CARRY ACCOUNTING MEANING

| From | To | Nature | Note |
|---|---|---|---|
| Order line | Bill line | explicit, stored | the backbone of quantity control |
| Order line | Stock movement | explicit, stored | the backbone of receipt control |
| Stock movement | Valuation layer | explicit, stored | one movement can produce several layers (lot-valued items) |
| Valuation layer | Journal entry | explicit, stored | present only under continuous valuation |
| Valuation layer | Bill line | explicit, stored | used for price-difference corrections |
| Bill line | Valuation layer it settles | **derived at posting time by replaying history** | `EV-P01-13` — **not a stored link, and the derivation consults a non-accounting audit table** |
| Bill line | Asset | explicit, stored | asset created at posting |
| Payable line | Payment line | via reconciliation objects | where FX difference is recognised |
| Order | Its accrual entry | **no link at all** | `EV-P01-17` |
| Source document | Cross-company generated document | **chatter message only; no structured link observed** | `EV-P01-28` |

**The two missing links are the finding.** A purchase whose payable, receipt and accrual all
exist cannot be reconstructed end-to-end from stored relationships alone.

## 3. FIELD-LEVEL FACTS THAT DRIVE THE ACCOUNTING

| Field (business name) | Lives on | Decides |
|---|---|---|
| Item type — storable / consumable / service | Item | whether a receipt event exists at all |
| Valuation mode — continuous / periodic | Item category | whether the receipt produces a journal entry |
| Cost method | Item category | what unit value the receipt layer carries |
| Bill control policy — on ordered / on received quantity | Item, with a company default | when a line becomes billable |
| Clearing-account model on/off | Company | whether the bill debits clearing or expense |
| Inventory valuation account | Item category, **company-dependent value** | debit side of the receipt |
| Goods-received clearing account | Item category, **company-dependent value**, overridable per storage location | credit side of the receipt |
| Item expense account | Item / item category, **company-dependent value** | debit side of a non-clearing bill; destination of consumed-quantity price differences |
| Vendor payable account | Vendor, **company-dependent value** | credit side of the bill |
| Asset-creation flag | **Ledger account** | whether posting a bill creates an asset |
| Allow-reconciliation flag | Ledger account | whether the clearing bridge ever closes (`EV-P01-10`) |
| Outstanding-payments account | Payment / journal | whether a payment produces any entry (`EV-P01-20`) |
| Order lock setting | Company | the terminal shape of an approved order |
| Cross-company generation flags and "create as" user | **Target** company | whether an action here creates a document there (`EV-P01-29`, `EV-P01-30`) |

**Observation.** Of the fourteen switches above, **one** is a business decision made per
transaction (bill control policy, and even that is defaulted from configuration). The rest are
configuration. The accounting shape of a purchase is therefore almost entirely a
*configuration* outcome, not a *transactional* one — which is why the same document type
produces five different ledger patterns (`P01_EVENT_TO_GL_MATRIX.md`).

## 4. SCOPE OF EACH OBJECT

See `P01_SCOPE_OWNERSHIP_MATRIX.md` §2. The single most consequential row: **every account in
the table above is a company-scoped value stored on a tenant-scoped object.**

## 5. WHAT IS NOT IN THIS MAP

Constraint-level, index-level and access-rule-level detail were assigned to the Database
Design expert and are reported in `P01_AAS03_EXPERT_CHALLENGE.md`. Tax, withholding, landed
cost and advance-payment objects were assigned to other experts. An absent object here means
**not covered by this document** — class C — never absent from the system.
