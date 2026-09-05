# P01 — BUSINESS EVENT REGISTER

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.**

Rule applied: `ONE BUSINESS FACT → ONE CANONICAL EVENT OWNER → ONE ACCOUNTING EFFECT PATH`.

Each row states the business fact, the document that owns it, whether the reference evidence
shows a *single* owner, and the classification of that statement.

| ID | Business fact | Canonical owner (candidate) | Single owner in evidence? | Class |
|---|---|---|---|---|
| `BE-P01-01` | A need to buy has been raised | Purchase Request | **No base capability.** Custom-only in the searched roots | SUPPORTED INTERPRETATION |
| `BE-P01-02` | Suppliers have been asked to quote | Request for Quotation (same record as the order) | Yes | FACT VERIFIED (`R1`) |
| `BE-P01-03` | A commitment to buy has been made | Purchase Order approval | Yes — but the resulting state depends on a company setting | FACT VERIFIED (`R1`) `EV-P01-01`,`EV-P01-03` |
| `BE-P01-04` | Goods have physically arrived | Goods Receipt | Yes | FACT VERIFIED (`R1`) |
| `BE-P01-05` | A service has been rendered | **No owner found.** Services have no receipt document; the fact first appears at the bill | NOT FOUND IN SEARCHED SCOPE — CLASS B | UNRESOLVED — EVIDENCE REQUIRED |
| `BE-P01-06` | The arrived goods now have a value | Goods Receipt, **only** when storable and continuously valued | **No** — three of four item shapes produce no valuation event | FACT VERIFIED (`R1`) `EV-P01-04`,`EV-P01-05` |
| `BE-P01-07` | The purchase is an inventory item / an expense | Item configuration, applied at receipt | Yes, but the decision is a configuration attribute, not a business act | FACT VERIFIED (`R1`) |
| `BE-P01-08` | The purchase is a capital asset | **Vendor Bill posting**, from a flag on the bill line's ledger account | Yes — but the field it reads may already have been overwritten (`EV-P01-09`) | FACT VERIFIED for the mechanism; **CONTRA-P01-04** for the collision |
| `BE-P01-09` | A liability to the vendor now exists | Vendor Bill | Yes — this is the one event every purchase shape passes through | FACT VERIFIED (`R1`) |
| `BE-P01-10` | The billed price differs from the received value | Vendor Bill posting | Yes, but split across two effects and silently dropped when an account is missing | FACT VERIFIED (`R1`) `EV-P01-14` |
| `BE-P01-11` | An obligation exists for goods received but not yet billed | **Two owners.** Implicitly by the clearing-account balance; explicitly by the order-stage accrual routine | **No — dual ownership.** `CONTRA-P01-02` | FACT VERIFIED (both paths exist) |
| `BE-P01-12` | Tax is recoverable / payable on the purchase | Vendor Bill | Assigned to the Localization expert | UNRESOLVED — EVIDENCE REQUIRED |
| `BE-P01-13` | Tax must be withheld from the vendor | **UNRESOLVED — bill or payment?** | Assigned to the Localization expert | UNRESOLVED — EVIDENCE REQUIRED |
| `BE-P01-14` | Money has been advanced to the vendor before delivery | Order down-payment lines exist in the base; a dedicated advance-payment capability exists in the custom sets | **Two candidate owners** | UNRESOLVED — EVIDENCE REQUIRED |
| `BE-P01-15` | The vendor has been paid | Payment — **but only where an outstanding account is configured**; otherwise the payment exists with no accounting effect | Yes, conditionally | FACT VERIFIED (`R1`) `EV-P01-20` |
| `BE-P01-16` | The payable has been settled | Reconciliation of the payable | Yes | FACT VERIFIED (`R1`) |
| `BE-P01-17` | An exchange gain or loss has arisen | Reconciliation at settlement | Yes | FACT VERIFIED (`R1`) `EV-P01-21` |
| `BE-P01-18` | Goods have been returned to the vendor | Return movement, valued as an outgoing movement against the clearing account | Yes | FACT VERIFIED (`R1`) |
| `BE-P01-19` | The vendor has refunded / credited us | Credit note | Assigned to the Functional Design expert | UNRESOLVED — EVIDENCE REQUIRED |
| `BE-P01-20` | Additional costs must be absorbed into the goods' value | Landed cost | Assigned to the Code & UI Architect expert | UNRESOLVED — EVIDENCE REQUIRED |
| `BE-P01-21` | The value of already-received goods has been restated | Manual revaluation routine | Yes | FACT VERIFIED (`R1`) `EV-P01-22` |
| `BE-P01-22` | A previously-recorded purchase fact was wrong and must be corrected | **No preserving owner found.** The mechanism observed deletes rather than reverses | `CONTRA-P01-01` | FACT VERIFIED (`R1`) `EV-P01-11`,`EV-P01-12`,`EV-P01-19` |

---

## Ownership conflicts carried forward

| ID | Conflict | Status |
|---|---|---|
| `CONTRA-P01-02` | The received-not-billed obligation has two representations that are not reconciled to each other: a clearing-account balance and a self-reversing accrual entry. Nothing observed prevents both from being present for the same order at the same date. | **DESIGN DECISION REQUIRED AT FINAL GATE** |
| `CONTRA-P01-04` | Asset classification and inventory-clearing both write the same field on the same bill line. | **UNRESOLVED — RUNTIME EVIDENCE REQUIRED** |
| `BE-P01-05` | The service-received business fact has no document of its own. | **UNRESOLVED — EVIDENCE REQUIRED** |

---

## Double-posting attack results (`§2.7`)

| Attack | Result in searched scope | Class |
|---|---|---|
| DOUBLE AP | Not found: the payable arises at exactly one document | B — not found in searched scope (`R1`, journal-entry creation-site population C) |
| DOUBLE VALUATION | **Found, conditionally**: the order-stage accrual and the receipt valuation can both be live for the same received-not-billed quantity | FACT VERIFIED that both paths exist; simultaneity **not** runtime-confirmed |
| DOUBLE COST ABSORPTION | Not established — landed cost not yet traced | C — not yet searched |
| DOUBLE TAX | Not established — assigned to Localization expert | C — not yet searched |
| DOUBLE WHT | Not established — assigned to Localization expert | C — not yet searched |
| DOUBLE SETTLEMENT | Not found | B — not found in searched scope |
| DOUBLE DEPRECIATION | Out of P01 scope; routed to the Asset track | ROUTED |
| DOUBLE COGS / DOUBLE REVENUE | Out of P01 scope; routed to P02 and the COGS track, which is on standing HOLD | ROUTED |

**Every "not found" above is class B or C. None is a statement that the condition cannot occur.**

---

# ADDENDUM — OWNERSHIP AFTER PEER INTAKE AND INSTALLED-STATUS EVIDENCE (2026-09-05)

| ID | Change |
|---|---|
| `BE-P01-01` need to buy | The custom purchase-request capability is **installed in the v16 deployment only**. The approvals pair is also installed there. **Two requisition mechanisms are live in v18 and none in v19** — so this fact has two owners in one deployment and no owner in the other |
| `BE-P01-06` arrived goods have a value | **In the v19 deployments the value exists on the movement and never in the ledger.** The business fact is recorded; its accounting counterpart is not |
| `BE-P01-08` purchase is a capital asset | **P04 independently confirms nobody owns this.** No classification field exists on the order or the receipt in either generation; the decision is taken by whoever configures the chart of accounts |
| `BE-P01-09` liability to the vendor | **P05 reports a second route**: an expense line can name a vendor and post to vendor-facing accounts with **no purchase document**. P01 is no longer the sole path to a vendor liability |
| `BE-P01-11` received-not-billed obligation | **In the v19 deployments neither representation exists.** The obligation has no accounting form at all between receipt and bill |
| `BE-P01-13` tax to be withheld | **P07 reports the fact is created at payment and reported from a P01 artefact** — two processes claim one fact. Still `UNRESOLVED`, now with a peer position on the record |
| `BE-P01-14` money advanced to a vendor | **P01 accepts ownership.** The custom module is **installed in all three deployments**, and its two copies **behave differently** |
| `BE-P01-15` vendor has been paid | **P06 reports four entry points and no single author** for payment intent |
| `BE-P01-20` additional costs absorbed | Landed cost is **installed in all three deployments** — live, not theoretical. P11 holds ownership open with an audit veto retained |
| `BE-P01-22` a prior purchase fact was wrong | Unchanged, and now under independent disproof challenge |

## New business facts identified this round

| ID | Business fact | Owner | Class |
|---|---|---|---|
| `BE-P01-23` | *"The period a purchased service covers"* | **should be P01; no field exists** | **P01 GAP — P10 needs it** |
| `BE-P01-24` | *"This advance offsets that future bill"* | P01 | **HOLD — RUNTIME EVIDENCE REQUIRED**; if it fails, the cost is recognised twice |
| `BE-P01-25` | *"This purchase belongs to another company"* | **unproven** — inferred from a tenant-scoped contacts hierarchy | **TOLERANCE-ZERO — HOLD**, now live on the v19 line |
