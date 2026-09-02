# 12 — Inventory Risk, Gap and Decision Register v1.0

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V1-001` | Jira: `ERPPLUS-139`
Status: `OPEN-ITEM REGISTER — NOTHING BELOW IS CLOSED BY THIS SESSION`

Every item in this register is surfaced again in `14_BOSS_FINAL_GATE_PACKAGE.md`. Nothing here is resolved, accepted or closed by the executor. Severity: `BLOCKING` = a downstream design or gate step cannot proceed; `MATERIAL` = must be decided before build but does not block this package; `CARRIED` = inherited unresolved from an earlier session; `WATCH` = monitor, no decision needed yet.

---

## 1. Clean-Room and Provenance Risks

| ID | Item | Severity | Owner | Required decision or action |
|---|---|---|---|---|
| `RISK-C05` | The pre-remediation history of the earlier evidence chain remains reachable by any ordinary repository clone. The current evidence surface was independently re-scanned clean, and the verdict stands at `SURFACE REMEDIATED / HISTORY QUARANTINE REQUIRED` — **not** `CLOSED`. **This session read no pre-remediation commit content and reproduced none of the quarantined material; nothing in this package reintroduces the exposure.** | `CARRIED` / `BLOCKING` for unconditional downstream reliance | **Boss only** | A written ruling among the four containment options: accept the risk explicitly in writing, restrict repository read access, rewrite history (destructive, shared-state, hard to reverse), or retain the interim warning label already applied. |
| `RISK-C05B` | Formal ratification of the independent tie-breaking read that established the current `C-05` verdict is still outstanding. | `CARRIED` / `BLOCKING` | **Boss only** | A written ruling accepting (or not) that read as the single non-conflicting record. |
| `RISK-CR-01` | Menu-10 clean-room wording fix — vendor-style path notation removed, the five location roles marked benchmark-derived and unvalidated — currently exists on the containment branch and on this design branch, but not on the menu package's original execution branch. | `CARRIED` / `MATERIAL` | Boss | Decide which branch is authoritative going forward and whether the fix propagates. This session preserved the corrected wording (file 03 §5, file 05 §2) and introduced no path notation of its own. |
| `RISK-U07` | Two non-cross-referencing "9 Veto Challenge Council" charter definitions exist, both claiming Boss approval. | `CARRIED` / `MATERIAL` | **Boss only** | Rule on which charter governs, or reconcile them. This session followed the ratified charter by convention, as prior packages did, and says so in file 13. |
| `RISK-CR-02` | This package is a single-session synthesis. No independent party has verified it. | `MATERIAL` | Boss | Decide whether an independent clean-room and content re-audit of this package is required before any downstream use. |

---

## 2. Carried Conflicts and Unknowns From the Evidence Chain

| ID | Item | Severity | Owner | Required decision |
|---|---|---|---|---|
| `RISK-C01` | Cancellation symmetry between the sales side and the purchase side of a movement chain is a recorded conflict. | `CARRIED` / `MATERIAL` | Inventory + Sales + Purchase | Define one cancellation rule that holds on both sides. |
| `RISK-C02` | Movement and demand idempotency: no stable identity exists to make a retried planning run, integration call or migration replay safe. This design treats it as a mandatory invariant (`IV-06`); the carried finding says its severity is Boss's call. | `CARRIED` / `BLOCKING` in this design's own view | **Boss** | Rule on whether idempotency is gate-blocking. |
| `RISK-C03` | The cost basis applied to a customer return — original issue cost or current cost — is unresolved. | `CARRIED` / `BLOCKING` for the return flow | Joint Accounting ↔ Inventory | Decide the basis and the reversal rule. |
| `RISK-U01` | Whether user rights can be scoped to a warehouse or a storage place is unknown. | `CARRIED` / `MATERIAL` | Inventory + Security | Decide the authorisation axis. |
| `RISK-U02` | Whether a distinct damaged-goods state is needed before scrap, or whether a quarantine place suffices. | `CARRIED` / `MATERIAL` | Inventory | Decide, with Thai user input. |
| `RISK-U03` | The Inventory-side multi-tenant invariant set does not exist. | `CARRIED` / `BLOCKING` for any build | **Boss** / SaaS Foundation | Commission and ratify the invariant set. |
| `RISK-G1G2G3` | Period-guard design, the freeze policy for counts, and the treatment of movements during a count are open Joint items. | `CARRIED` / `BLOCKING` for the count flow | Joint | Decide the guard and freeze policy. |
| `RISK-G5` | Certification of the cutover opening balance, quantity and value, against the accountant's opening trial balance. | `CARRIED` / `BLOCKING` for cutover | Joint | Define the certification and who signs it. |
| `RISK-G7` | A prior benchmark lesson records a reconciliation report export that was defective in practice. | `CARRIED` / `MATERIAL` | Inventory | Make export acceptance testing a release condition (`RC-10`). |
| `RISK-N-A12-01` | The account-led period-close functional design was reopened as a high functional-design gap and has not been closed. | `CARRIED` / `BLOCKING` | Joint | Close the period-close design. |

---

## 3. Joint Accounting ↔ Inventory Decisions

None of these can be made by an Inventory session. All are `BLOCKING` for the parts of the design that depend on them.

| ID | Decision | Depends on it |
|---|---|---|
| `JT-01` | Which concept owns valuation policy. | Valuation report, close, landed cost, category design |
| `JT-02` | Permitted costing methods and change rules. | Valuation |
| `JT-03` | Continuous against periodic valuation timing. | Fact emission timing |
| `JT-04` | Cost-of-goods-sold recognition timing. | Delivery flow |
| `JT-05` | Return cost basis (`C-03`). | Return flows |
| `JT-06` | Late supplier bill after period close. | Close |
| `JT-07` | Period close design and snapshot content. | Close, valuation |
| `JT-08` | Landed-cost eligibility and posting structure. | Landed cost |
| `JT-09` | Work-in-progress recognition timing. | Manufacturing handoff |
| `JT-10` | Inter-company transfer treatment. | Multi-company resupply |
| `JT-11` | Opening-balance certification (`G-5`). | Cutover |
| `JT-12` | Period lock policy and exception granting. | Period guard |

---

## 4. Design Gaps Raised or Carried by This Session

| ID | Gap | Severity | Owner |
|---|---|---|---|
| `GAP-FS-01` | Valuation-policy ownership and close design. | `BLOCKING` | Joint |
| `GAP-FS-02` | Product category as owner of both valuation policy and put-away behaviour — acceptable, or must they be separated? | `MATERIAL` | Joint |
| `GAP-FS-03` | Variant identity when the attribute set changes after variants hold stock. | `MATERIAL` | Data design track |
| `GAP-FS-04` | The tie-break rule when the product-kind derivation is ambiguous. | `MATERIAL` | Inventory |
| `GAP-FS-05` | Whether handling units migrate live, as history, or both. | `MATERIAL` | Migration |
| `GAP-FS-06` | Whether movement idempotency is gate-blocking (same as `RISK-C02`). | `BLOCKING` | Boss |
| `GAP-FS-07` | The cross-company transfer path was never traced end to end. | `MATERIAL` | Inventory + Joint |
| `GAP-FS-08` | The provenance reference does not exist and must be designed from scratch. | `BLOCKING` for cutover | Migration |
| `GAP-FS-09` | Opening-balance certification (same as `G-5`). | `BLOCKING` for cutover | Joint |
| `GAP-FS-10` | Inventory-side multi-tenant invariant set (same as `U-03`). | `BLOCKING` for build | Boss |
| `GAP-FS-11` | **No Thai user has validated any label, flow, reason code, document name or report title.** | `BLOCKING` for user-facing design | Boss to commission |
| `GAP-FS-12` | Whether analytic cost belongs in Inventory v1.0 or a later release. | `MATERIAL` — scope | Boss |
| `GAP-FS-13` | Whether the management indicator set matches what Thai SME owners want. | `MATERIAL` | Thai user validation |
| `GAP-FS-14` | Report retention and archive policy for closed periods. | `MATERIAL` | Boss / Accounting |
| `GAP-FS-15` | Whether a point-of-sale channel is in SMEsPlus v1.0 scope, and if so whether it issues stock in real time or in batches. | `MATERIAL` — scope | Boss |
| `GAP-FS-16` | Over-receipt tolerance policy — the threshold and who approves beyond it. | `MATERIAL` | Inventory + Purchase |
| `GAP-FS-17` | Which count freeze policy Thai SMEs can actually operate. | `MATERIAL` | Thai user validation |
| `GAP-FS-18` | How granular separation of duties needs to be per document type. | `MATERIAL` | Thai user validation + Security |
| `GAP-FS-19` | Whether Manufacturing is in SMEsPlus v1.0 scope, which determines whether the manufacturing handoffs are live or deferred. | `MATERIAL` — programme scope | Boss |
| `GAP-FS-20` | Eight of the 29 menus rest on no prior evidence and were written as this session's design hypothesis: landed cost, variants, warehouse analysis, storage categories, put-away rules, attributes, packagings, barcode formats. | `MATERIAL` | Boss to commission validation |
| `GAP-FS-21` | The five internal location roles remain benchmark-derived and unvalidated; what Thai SME warehouses actually use is unknown. | `MATERIAL` | Thai field validation |
| `GAP-FS-22` | Whether the reservation policy should default to reserve-on-confirm or reserve-on-pick for Thai SMEs. | `MATERIAL` | Thai user validation |

---

## 5. Thai Statutory Items — Held and Routed

All are `HOLD / EVIDENCE REQUIRED` and routed to the **Accounting-Tax track**. This session asserts none of them.

| ID | Item |
|---|---|
| `TH-HOLD-01` | Statutory stock-report format and title |
| `TH-HOLD-02` | Scrap destruction procedure and deductibility evidence |
| `TH-HOLD-03` | Import duty and import VAT treatment in landed cost |
| `TH-HOLD-04` | Withholding-tax correlation with product kind |
| `TH-HOLD-05` | Accepted Thai costing norms |
| `TH-HOLD-06` | Warehouse against registered tax branch |
| `TH-HOLD-07` | Witnessed annual physical count requirements |
| `TH-HOLD-08` | Sector traceability obligations for food, pharmaceutical and cosmetic goods |
| `TH-HOLD-09` | Delivery document to tax invoice linkage and numbering conventions |

---

## 6. Register Roll-Up

| Category | Count |
|---|---:|
| Clean-room and provenance risks | 5 |
| Carried conflicts and unknowns | 10 |
| Joint Accounting ↔ Inventory decisions | 12 |
| Design gaps raised or carried | 22 |
| Thai statutory items held | 9 |
| **Total open items** | **58** |

| Severity | Count |
|---|---:|
| `BLOCKING` (in whole or for a named part) | 20 |
| `MATERIAL` | 29 |
| `HOLD / EVIDENCE REQUIRED` (statutory) | 9 |
| Closed by this session | **0** |

---

## 7. What Would Change This Register

Only a written Boss ruling, a Joint Accounting ↔ Inventory session that closes its own rows, an Accounting-Tax track response carrying authoritative evidence, or a completed Thai user validation record. This session performs none of those and closes nothing.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
