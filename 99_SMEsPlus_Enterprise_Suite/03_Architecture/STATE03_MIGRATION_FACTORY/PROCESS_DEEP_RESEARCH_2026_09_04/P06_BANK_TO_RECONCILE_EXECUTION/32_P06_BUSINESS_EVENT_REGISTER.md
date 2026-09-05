# P06_BUSINESS_EVENT_REGISTER.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Scope model:** CORR1 applied. **Clean-room:** these are *business events*, expressed in business language. No implementation shape is transferred.

---

## 1. Purpose

The prior package registered **bank events** (what arrives from a bank) and **accounting events** (what hits the ledger). This file registers the layer between them that the reference has no object for: **the business events that P06 owns**. It exists because the semantic trace required by the constitution runs *Business Event → Runtime Behaviour → Accounting Event*, and P06's business-event layer was implicit.

---

## 2. The register

**Owner column:** which process authors the fact. **Scope:** the financial-effect scope under CORR1.

| ID | Business event | Owner | Scope | Creates a financial effect? | Reference support |
|---|---|---|---|---|---|
| BE-01 | An obligation to pay is recognised | P01 / P05 | COMPANY | no (recognised earlier) | open item + residual |
| BE-02 | An entitlement to receive is recognised | P02 | COMPANY | no | as above |
| BE-03 | **A decision to settle is taken** | P06 | COMPANY | no | **NOT FOUND as an object** — four entry points, no author (`P06-B-04`) |
| BE-04 | **An instruction is issued to a bank or provider** | P06 | COMPANY | no | boolean `is_sent` only (SSM-F-05) |
| BE-05 | **The instruction becomes irrevocable** | P06 | COMPANY | no | **NOT FOUND** — no state |
| BE-06 | Money leaves an own account | external | COMPANY | **yes** | bank event |
| BE-07 | Money arrives in an own account | external | COMPANY | **yes** | bank event |
| BE-08 | **An external party confirms the movement** | external, recorded by P06 | COMPANY | **yes** | **NOT FOUND** — no confirmation fact (`P06-B-06`) |
| BE-09 | A bank item is identified as corresponding to a known obligation | P06 | COMPANY | no | matching |
| BE-10 | An obligation is discharged | P06, applied to the obligation | COMPANY | **yes** | reconciliation |
| BE-11 | A difference is accepted and written off | P06 | COMPANY | **yes** | six entry points, no approval (`P06-B-22`) |
| BE-12 | The bank charges for its service | external | COMPANY | **yes** | **no first-class concept** (`P06-B-17`) |
| BE-13 | The bank pays interest | external | COMPANY | **yes** | **no first-class concept** |
| BE-14 | A provider retains commission from a settlement | external | COMPANY | **yes** | **not modelled in v18** |
| BE-15 | An exchange difference is realised | P06 triggers, P-CORE owns | COMPANY | **yes** | exchange-difference move |
| BE-16 | Money is moved between two own accounts | P06 | COMPANY | **yes ×2** | two unlinked legs (`P06-B-16`) |
| BE-17 | Money moves between two group companies | P06 ×2 | **two COMPANY effects in one TENANT** | **yes ×2** | no carrier object (`P06-B-20`) |
| BE-18 | Money is received that cannot be identified | P06 | COMPANY | **yes** | suspense, no ageing (`P06-B-18`) |
| BE-19 | Money is received in advance of any obligation | P02 / P01 | COMPANY | **yes** | invoice-shaped in 3 of 4 paths |
| BE-20 | **A settled item is returned or dishonoured** | external | COMPANY | **yes** | **not migrated v14→v18** (`P06-B-35`) |
| BE-21 | An instruction is rejected by the bank | external | COMPANY | depends | bare state assignment, no cause (SSM-F-03) |
| BE-22 | A settlement is corrected after the fact | P06 | COMPANY | **yes** | destroys the match silently (attack A5) |
| BE-23 | A period is closed | P08 | COMPANY, inherited | no | lock dates, cascading (PC-F-02) |
| BE-24 | Tax is withheld at the moment of settlement | P07 | COMPANY | **yes** | custom modules mutate the settled amount (`P06-B-13`) |
| BE-25 | A cash till is counted and closed | P06 | COMPANY | **yes** | no session/custodian model (`P06-B-33`) |

**25 business events.** **DENOMINATOR:** POPULATION: events named in the P06 directive plus events discovered during evidence gathering across both rounds. UNIT: business event. **This is the P06 business-event set as declared — Class B for anything outside it.**

---

## 3. What the register makes visible

**BER2-F-01 — Six of twenty-five business events have no object in the reference at all.**
BE-03, BE-05, BE-08, BE-12, BE-13, BE-14. Every one of them is a fact a treasury operator states in plain language every day: *"we decided to pay"*, *"it's gone, we can't stop it"*, *"the bank confirmed"*, *"the bank charged us"*, *"the bank paid interest"*, *"the provider kept its cut"*.
**The reference models the ledger consequences of banking but not the business of banking.** That is the single clearest way to state what P06 found.

**BER2-F-02 — Every event that creates a financial effect is COMPANY-scoped without exception**, except BE-17 which creates two, in two companies, inside one tenant. That is the only place a tenant-scoped carrier is required, and it is the one place none exists.

**BER2-F-03 — Three events are authored externally and merely *recorded* by P06** (BE-06, BE-07, BE-08, BE-20, BE-21). The reference gives P06 no way to distinguish "we believe" from "they told us", which is the same absence as `P06-B-06` seen from the business side.

---

# End
