# P01 — EDGE CASE TEST MATRIX

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.**

Every row is a case the session directive `§3` requires. The **Status** column is the honest
state of knowledge, not a plan. `SOURCE-READ` = traced in source and stated. `EXPERT` =
assigned to an independent expert. `NOT SEARCHED` = class C. `RUNTIME REQUIRED` = the answer
cannot come from source alone.

**No row in this matrix was executed against a running system.** No transaction was performed
in this session. Every "expected behaviour" below is a reading of source — except where a row
cites deployed-schema evidence, which was obtained later in the session from dumps of three
live databases (`P01_DEPLOYED_SCHEMA_EVIDENCE.md`). A schema fact is stronger than a source
fact but is still not a behavioural test. Each row remains a **test to be run**, not a test
that passed.

| # | Case | Status | What the source shows / what must be proven |
|---|---|---|---|
| 1 | Order confirmed, nothing received, nothing billed | SOURCE-READ | No accounting effect whatsoever (`EV-P01-01`) |
| 2 | Order confirmed then cancelled, no bill | SOURCE-READ | Permitted; state change only |
| 3 | Order cancelled while a posted bill exists | SOURCE-READ | Blocked with an error (`EV-P01-02`) |
| 4 | Receipt before bill, storable, continuous valuation | SOURCE-READ | Inventory / clearing entry at receipt; clearing discharged at the bill |
| 5 | Receipt before bill, storable, **periodic** valuation | SOURCE-READ | **No entry at receipt**; expense arises only at the bill (`EV-P01-05`) |
| 6 | Receipt before bill, **consumable** | SOURCE-READ | No layer, no entry (`EV-P01-04`) |
| 7 | **Bill before receipt** | RUNTIME REQUIRED | The price-difference engine finds no layer to match; what the clearing balance then represents must be proven, not assumed |
| 8 | Partial receipt | EXPERT (Functional Design) | Governed by the bill control policy |
| 9 | Partial bill | EXPERT (Functional Design) | — |
| 10 | Over-receipt | EXPERT (Functional Design) | Whether it is blocked, warned or silent must be established |
| 11 | Under-receipt then order closed | EXPERT (Functional Design) | Whether the clearing residue is ever cleared |
| 12 | Over-billing beyond received quantity | SOURCE-READ, partial | The price-difference routine clamps corrected quantity to received-minus-already-billed and skips the line at zero; whether the *bill itself* is blocked is `EXPERT` |
| 13 | Price difference, goods still on hand | SOURCE-READ | Valuation layer corrected (`EV-P01-15`) |
| 14 | Price difference, goods already consumed | SOURCE-READ | Posted to item expense vs clearing (`EV-P01-14`) |
| 15 | **Price difference where the item has no expense account** | SOURCE-READ | **Nothing is posted. Silent.** (`EV-P01-14`) — highest-priority test |
| 16 | **Clearing account not flagged reconcilable** | SOURCE-READ | Bridge never closes; balance accumulates; no error (`EV-P01-10`) — highest-priority test |
| 17 | Quantity difference between receipt and bill | EXPERT (Functional Design) | — |
| 18 | Three-way match enforcement | EXPERT (Functional Design) | Capability absent from the active `R1` root (`EV-P01-23`) |
| 19 | Purchase return to vendor | SOURCE-READ, partial | Valued as an outgoing movement crediting inventory, debiting clearing |
| 20 | Vendor credit note / refund | EXPERT (Functional Design + Code & UI) | The price-difference engine has an explicit refund branch keyed to the reversed entry |
| 21 | Return of a previously-returned item | SOURCE-READ | The source contains a special case that fakes the layer price to avoid double-impacting valuation — evidence the general algorithm does not handle it |
| 22 | Landed cost | EXPERT (Code & UI) | — |
| 23 | Landed cost applied after the goods are consumed | EXPERT (Code & UI) | — |
| 24 | Landed cost applied after period close | EXPERT (Code & UI) | — |
| 25 | Advance payment / deposit to vendor, base capability | SOURCE-READ | **Bill-first only**: an advance is recorded as a bill and then attached to an order. No order-side advance wizard exists in `R1` (class A within `R1`) |
| 26 | Advance payment, project custom capability | EXPERT (Localization) | — |
| 27 | Advance applied to a later bill — double-count risk | EXPERT (Localization) + RUNTIME REQUIRED | — |
| 28 | Multi-currency purchase, rate present at every step | EXPERT (Code & UI) | — |
| 29 | Multi-currency purchase, **no rate for the date** | EXPERT (Code & UI) | The Account track already recorded a silent single-rate fallback; whether P01 inherits it must be proven |
| 30 | FX difference on settlement | SOURCE-READ | Created by the reconciliation engine at settlement (`EV-P01-21`) |
| 31 | Purchase VAT | EXPERT (Localization) | — |
| 32 | Thai withholding tax at bill | EXPERT (Localization) | Ownership unresolved (`DEP-P01-03`) |
| 33 | Thai withholding tax at payment | EXPERT (Localization) | Ownership unresolved (`DEP-P01-03`) |
| 34 | Withholding on a partial payment | EXPERT (Localization) + RUNTIME REQUIRED | — |
| 35 | Withholding reversal after certificate issue | EXPERT (Localization) + RUNTIME REQUIRED | — |
| 36 | Bill cancellation after posting | SOURCE-READ | **Derived journal items are deleted, not reversed** (`EV-P01-11`) — highest-priority test |
| 37 | Bill reset to draft after an asset was created | SOURCE-READ | Still-draft assets are deleted (`EV-P01-19`) |
| 38 | Backdated receipt | SOURCE-READ | The entry date is **not** the movement date; it can fall to system-today (`EV-P01-06`) — highest-priority test |
| 39 | Backdating via the project's effective-date capability | EXPERT (Localization) | — |
| 40 | Posting into a locked period | EXPERT (Code & UI) | Two candidate bypass routes recorded: the receipt date context override, and the revaluation routine |
| 41 | Reopening a closed period | EXPERT (Code & UI) | — |
| 42 | Inventory revaluation of previously received goods | SOURCE-READ | A routine exists that creates such an entry (`EV-P01-22`) |
| 43 | **Order-stage accrual run twice for the same orders and date** | SOURCE-READ | No guard found in the routine (class B); no record is written to the order in either generation (`EV-P01-17`) — highest-priority test |
| 44 | Accrual raised, then the bill posted before the reversal date | RUNTIME REQUIRED | Whether accrual and bill overlap in the same period must be proven (`CONTRA-P01-02`) |
| 45 | **Cross-company: approving an order whose vendor is a contact under another company's partner** | SOURCE-READ | A sales order is created in that company, as superuser by default, optionally auto-posted (`EV-P01-27`, `EV-P01-29`, `EV-P01-30`) — highest-priority test |
| 46 | Cross-company where two companies' partners are both ancestors of the contact | SOURCE-READ | First match wins silently (`EV-P01-26`) |
| 47 | Cross-company where the two companies belong to different tenants | RUNTIME REQUIRED | **No tenant test found — class B** (`EV-P01-31`). Tolerance-zero. |
| 48 | Subcontract receipt | SOURCE-READ | Credit split into component cost and service cost, price forced |
| 49 | Asset purchase of a storable, continuously-valued item | RUNTIME REQUIRED | `CONTRA-P01-04` — the account the asset rule reads may already be the clearing account |
| 50 | Migration: bills imported without audit-log history | SOURCE-READ | Every imported bill falls to the fallback ordering branch; layer matching may differ from the source system (`CONTRA-P01-06`) — highest-priority test |

---

## Priority for runtime verification

Seven cases carry a silent or irreversible consequence and should be executed first:
**15, 16, 36, 38, 43, 45, 50.** Each either loses value with no error, overwrites history, or
crosses a company boundary without proving ownership.
