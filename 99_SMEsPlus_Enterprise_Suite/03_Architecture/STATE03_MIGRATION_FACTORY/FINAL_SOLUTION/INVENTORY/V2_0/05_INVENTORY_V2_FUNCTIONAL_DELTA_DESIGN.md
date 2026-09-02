# 05 — Inventory v2.0 Functional Delta Design

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V2-001` | Jira: `ERPPLUS-139`
Status: `DEPENDENCY-FRAMED DESIGN NOTES — NO NEW FUNCTIONAL DECISION, NO SCHEMA, NO SCREEN`
Clean-room: Layer 1. No reference-ERP name, code, model, field, method, schema, or markup appears below.

This file addresses each of the ten scope areas named in the new-session prompt §4, in order. For each, it states what v1.0 already established, what remains open, and — where the item is gated behind the Accounting COGS Gap (file 02, file 04 Lane C) — the dependency framing rather than a resolved answer.

---

## 1. COGS Gap Dependency Reconciliation

Covered fully in file 02. Summary: the Accounting COGS Gap evidence does not exist as a completed package; nine of twelve Joint Accounting↔Inventory decisions are gated on it (file 04 §3); the controlling next action is execution of the already-readied, already-prompted COGS Deep Research session (file 09).

---

## 2. Valuation Policy Ownership

v1.0 (file 08 §1) already states the requirement set any owner must satisfy — one effective policy per product/company/date, versioned with an effective date, recorded on every valuation fact, printed on every report, changed only by an approved action with a stated treatment for existing stock — without naming an owner. That remains unchanged and correct. This session adds nothing to it, because doing so would require exactly the Product Category / Product accounting-inheritance evidence (COGS research Menu B, Menu C, §11) that is the subject of the gap. **Dependency framing:** whichever owner Accounting's COGS research ultimately supports, it must satisfy the six requirements v1.0 already wrote; this session's only contribution is confirming those six requirements survive unchanged and are not themselves in question.

---

## 3. Period Close and Stock Close Dependency

v1.0 (file 07 §4) already designs the *mechanism* Inventory owns regardless of what Accounting decides: a native period guard, enforcement at movement entry, an exception path with a named grantor/written reason/expiry/permanent record, and an explicit rejection of any global bypass. That mechanism is unaffected by the COGS Gap and is not repeated as new content here. What is gated is the *content* of the close itself — `JT-07` (what the closing snapshot must contain) and the late-arriving-cost rule (`JT-06`) — both Lane C in file 04. **Dependency framing:** the guard exists and stays as designed; what triggers it, and what happens to the value on the other side of the lock date, waits for the COGS research's Menu F evidence.

---

## 4. Landed Cost Posting Dependency

v1.0 (file 08 §4) already states seven design rules (`LC-01`–`LC-07`) that hold regardless of which posting structure Accounting eventually adopts: single allocation per bill per line, a checkable allocation statement, explicit handling when goods are already sold, treatment as a variance question under a standard-cost policy, subjection to the period guard, and the Thai recoverable-VAT question held separately. None of these seven rules requires COGS-specific evidence and none is repeated as new content here. What is gated is `LC-06` — the eligibility rule and posting structure themselves — Lane C in file 04, requiring COGS research §21. **Dependency framing:** the seven rules a landed-cost feature must obey are already fixed; which products and which posting structure remain open until the COGS research exists.

---

## 5. Return Cost Basis

v1.0 (file 07 §2, `C-03`) already records this as unresolved: whether a customer return uses the original issue cost or the current cost. This session does not choose between them — doing so is precisely what COGS research §19 Contract C and scenarios 17–18 exist to evidence. **Dependency framing:** two candidates exist (original issue cost; current cost), both are business-plausible, and this package explicitly declines to prefer either without evidence, because a wrong default here silently misstates margin on every return until caught.

---

## 6. Movement Idempotency Decision Framing

Unlike §2–5 above, this item is **not** gated on the COGS Gap — it is an Inventory-side data-integrity question, already fully framed in v1.0 (file 06 `IV-06`; file 12 `RISK-C02`) and still awaiting only a Boss severity ruling (`T-1`: is it unconditionally blocking, per v1.0 challenge lane `V-4`, or blocking only for automated/migration paths, per lane `S-4`). This session restates the framing without resolving it, and notes explicitly that acquiring the COGS Gap evidence would not resolve it either — the two are independent dependencies that happen to both currently sit open.

---

## 7. Multi-Tenant Invariant Dependency

Also not gated on the COGS Gap. v1.0 (file 12 `RISK-U03`) already records that the Inventory-side multi-tenant invariant set does not exist and must be commissioned by Boss or SaaS Foundation. This session adds one connection point: once a valuation-policy owner is eventually decided (§2 above), that owner must itself be one of the concepts the multi-tenant invariant set scopes correctly — a category, product, or standalone policy object that is not properly tenant-scoped would let one company's valuation policy leak into another's. This is noted as a future cross-check, not a new requirement invented here.

---

## 8. Migration Provenance Dependency

Also not gated on the COGS Gap. v1.0 (file 12 `GAP-FS-08`; challenge lane `E-2`, "the largest silent risk in the package") already records that the provenance reference does not exist and must be designed as a first-class Migration Factory component. This session adds one connection point: once opening-balance certification (`G-5` / `JT-11`, Lane B in file 04) is designed, it will need to carry not just opening quantity and value but the *cost basis and policy version* behind that opening value — which depends on §2 above being resolved first for the certification to be meaningful. Noted as a future sequencing dependency, not resolved here.

---

## 9. Thai User Validation Dependency

Also not gated on the COGS Gap. v1.0 (file 12 `GAP-FS-11`) already records that no Thai user has validated any label, flow, reason code, document name, or report title. Nothing in this file introduces a new Thai-facing label; every Thai name mentioned anywhere in this package that also appears in v1.0 (e.g., valuation, landed cost, stock card) carries the same `UNVALIDATED - THAI USER REVIEW REQUIRED` status v1.0 already assigned it, unchanged.

---

## 10. AAS+ and PMO Recommendation for What May Proceed Before Development

Addressed in full in file 06 (AAS+ and PMO Review) and file 09 (Next Prompt Recommendation). Summary position stated here for completeness: **nothing in this programme is ready for development.** What may proceed before development, in parallel with the COGS Deep Research execution, is design and research work in Lane A of file 04 — Thai user validation, migration provenance design, and the multi-tenant invariant commissioning — none of which touches valuation, COGS, or posting structure.

---

## 11. What This File Explicitly Does Not Do

It does not name a valuation-policy owner. It does not choose a costing method. It does not choose continuous or periodic timing. It does not set COGS recognition timing. It does not choose a return cost basis. It does not design a period-close snapshot. It does not set landed-cost eligibility or posting structure. It does not resolve work-in-progress timing. It does not assert a Thai statutory position. Every one of these remains exactly as open as it was when v1.0 closed, and is registered as such in file 07.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
