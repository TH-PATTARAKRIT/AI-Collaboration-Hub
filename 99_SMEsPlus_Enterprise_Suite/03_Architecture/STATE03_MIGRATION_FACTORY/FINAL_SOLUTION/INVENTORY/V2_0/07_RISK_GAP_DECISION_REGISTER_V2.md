# 07 — Inventory Risk, Gap and Decision Register v2.0

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V2-001` | Jira: `ERPPLUS-139`
Status: `OPEN-ITEM REGISTER — NOTHING BELOW IS CLOSED BY THIS SESSION`

This register carries forward every item from `12_INVENTORY_RISK_GAP_DECISION_REGISTER_V1.md` (v1.0) **unchanged in substance**. Nothing is re-worded to sound more resolved than it was. Two changes only: (1) items that depend specifically on the Accounting COGS Gap evidence now carry an explicit `COGS-GATED` flag, cross-referenced to file 04's lane classification; (2) one new item, `RISK-COGS-01`, is added for the COGS Deep Research session's non-execution.

---

## 1. Clean-Room and Provenance Risks (unchanged from v1.0 §1)

| ID | Item | Severity | Owner | Required decision or action | v2.0 flag |
|---|---|---|---|---|---|
| `RISK-C05` | Pre-remediation history remains reachable by any ordinary clone; verdict stands at `SURFACE REMEDIATED / HISTORY QUARANTINE REQUIRED`. | `CARRIED` / `BLOCKING` for unconditional downstream reliance | **Boss only** | Written ruling among four containment options. | Unchanged |
| `RISK-C05B` | Formal ratification of the independent tie-breaking read still outstanding. | `CARRIED` / `BLOCKING` | **Boss only** | Written ruling. | Unchanged |
| `RISK-CR-01` | Menu-10 clean-room wording fix authoritative-branch question. | `CARRIED` / `MATERIAL` | Boss | Decide authoritative branch. | Unchanged |
| `RISK-U07` | Two rival "9 Veto Challenge Council" charter definitions. | `CARRIED` / `MATERIAL` | **Boss only** | Rule on which charter governs. | Unchanged |
| `RISK-CR-02` | v1.0 is single-session synthesis, unverified by an independent party. | `MATERIAL` | Boss | Decide whether independent re-audit is required. | Unchanged — applies equally to v2.0, which is also single-session synthesis |

---

## 2. Carried Conflicts and Unknowns From the Evidence Chain (unchanged from v1.0 §2, flags added)

| ID | Item | Severity | Owner | Required decision | v2.0 flag |
|---|---|---|---|---|---|
| `RISK-C01` | Cancellation symmetry, sales side vs. purchase side. | `CARRIED` / `MATERIAL` | Inventory + Sales + Purchase | Define one cancellation rule. | Not COGS-gated |
| `RISK-C02` | Movement and demand idempotency — no stable identity for retry safety. | `CARRIED` / `BLOCKING` in Inventory's own view | **Boss** | Rule on whether idempotency is gate-blocking. | Not COGS-gated — file 05 §6 |
| `RISK-C03` | Customer-return cost basis unresolved. | `CARRIED` / `BLOCKING` for the return flow | Joint Accounting ↔ Inventory | Decide the basis and reversal rule. | **`COGS-GATED`** — Lane C, file 04 §3 (`JT-05`) |
| `RISK-U01` | Whether user rights can be scoped to a warehouse or storage place. | `CARRIED` / `MATERIAL` | Inventory + Security | Decide the authorisation axis. | Not COGS-gated |
| `RISK-U02` | Whether a distinct damaged-goods state is needed before scrap. | `CARRIED` / `MATERIAL` | Inventory | Decide, with Thai user input. | Not COGS-gated |
| `RISK-U03` | Inventory-side multi-tenant invariant set does not exist. | `CARRIED` / `BLOCKING` for any build | **Boss** / SaaS Foundation | Commission and ratify. | Not COGS-gated — file 05 §7 |
| `RISK-G1G2G3` | Period-guard design, count freeze policy, movements during a count. | `CARRIED` / `BLOCKING` for the count flow | Joint | Decide the guard and freeze policy. | Guard mechanism itself not gated (file 05 §3); freeze-policy content partially touches `JT-07` |
| `RISK-G5` | Cutover opening balance certification. | `CARRIED` / `BLOCKING` for cutover | Joint | Define certification and signer. | Lane B, file 04 §3 (`JT-11`) — proceeds now with Joint-session confirmation pending |
| `RISK-G7` | Reconciliation export defect lesson. | `CARRIED` / `MATERIAL` | Inventory | Make export acceptance testing a release condition. | Not COGS-gated |
| `RISK-N-A12-01` | Account-led period-close functional design reopened as a high gap, not closed. | `CARRIED` / `BLOCKING` | Joint | Close the period-close design. | **`COGS-GATED`** — Lane C, file 04 §3 (`JT-07`) |

---

## 3. Joint Accounting ↔ Inventory Decisions (unchanged from v1.0 §3, flags added)

| ID | Decision | Depends on it | v2.0 flag |
|---|---|---|---|
| `JT-01` | Which concept owns valuation policy | Valuation report, close, landed cost, category design | **`COGS-GATED`** — Lane C |
| `JT-02` | Permitted costing methods and change rules | Valuation | **`COGS-GATED`** — Lane C |
| `JT-03` | Continuous vs. periodic valuation timing | Fact emission timing | **`COGS-GATED`** — Lane C |
| `JT-04` | COGS recognition timing | Delivery flow | **`COGS-GATED`** — Lane C |
| `JT-05` | Return cost basis (`C-03`) | Return flows | **`COGS-GATED`** — Lane C |
| `JT-06` | Late supplier bill after period close | Close | **`COGS-GATED`** — Lane C |
| `JT-07` | Period close design and snapshot content | Close, valuation | **`COGS-GATED`** — Lane C |
| `JT-08` | Landed-cost eligibility and posting structure | Landed cost | **`COGS-GATED`** — Lane C |
| `JT-09` | Work-in-progress recognition timing | Manufacturing handoff | **`COGS-GATED`** — Lane C |
| `JT-10` | Inter-company transfer treatment | Multi-company resupply | Lane B — scoping may proceed |
| `JT-11` | Opening-balance certification (`G-5`) | Cutover | Lane B — scoping may proceed |
| `JT-12` | Period lock policy and exception granting | Period guard | Lane B — mechanism unblocked, late-cost consequence gated via `JT-06` |

---

## 4. Design Gaps Raised or Carried by v1.0 (unchanged from v1.0 §4, flags added where relevant)

All 23 v1.0 items (`GAP-FS-01` through `GAP-FS-23`) are carried forward unchanged. Only those with a COGS-Gap connection are re-listed here for visibility; the remainder are unchanged and are not repeated — see v1.0 file 12 §4 for the full list.

| ID | Gap | Severity | Owner | v2.0 flag |
|---|---|---|---|---|
| `GAP-FS-01` | Valuation-policy ownership and close design. | `BLOCKING` | Joint | **`COGS-GATED`** — Lane C (same item as `JT-01`) |
| `GAP-FS-02` | Product category as owner of both valuation policy and put-away behaviour. | `MATERIAL` | Joint | **`COGS-GATED`** — resolving `JT-01` first is a precondition to answering this cleanly |
| `GAP-FS-12` | Whether analytic cost belongs in Inventory v1.0 or a later release. | `MATERIAL` — scope | Boss | Lane A — scope question, not COGS-gated (file 04 §3) |

All other `GAP-FS-*` items (`03`–`11`, `13`–`23`) are unaffected by the COGS Gap and are carried forward with no change in status.

---

## 5. Thai Statutory Items — Held and Routed (unchanged from v1.0 §5)

All nine `TH-HOLD-*` items are carried forward unchanged. `TH-HOLD-03` (import duty/VAT treatment in landed cost) and `TH-HOLD-05` (accepted Thai costing norms) additionally sit inside the COGS Deep Research's own Thai Accounting/Tax/Audit track (COGS research §13) — meaning that track's eventual completion is *one* of the evidence sources that could move them toward closure, but statutory closure still separately requires authoritative Thai evidence regardless of what the COGS research itself finds about reference-system behaviour.

---

## 6. Register Roll-Up

| Category | v1.0 count | v2.0 count | Change |
|---|---:|---:|---|
| Clean-room and provenance risks | 5 | 5 | Unchanged |
| Carried conflicts and unknowns | 10 | 10 | Unchanged |
| Joint Accounting ↔ Inventory decisions | 12 | 12 | Unchanged (9 now explicitly `COGS-GATED`) |
| Design gaps raised or carried | 23 | 23 | Unchanged (2 now explicitly `COGS-GATED`) |
| Thai statutory items held | 9 | 9 | Unchanged |
| New items raised by this session | 0 | 1 | `RISK-COGS-01`, below |
| **Total open items** | **59** | **60** | +1 |

| Severity | v1.0 count | v2.0 count |
|---|---:|---:|
| `BLOCKING` (in whole or for a named part) | 20 | 21 |
| `MATERIAL` | 30 | 30 |
| `HOLD / EVIDENCE REQUIRED` (statutory) | 9 | 9 |
| Closed by this session | **0** | **0** |

---

## 7. New Item Raised by This Session

| ID | Item | Severity | Owner | Required decision or action |
|---|---|---|---|---|
| `RISK-COGS-01` | The Accounting COGS Deep Research session (`SMEPLUS-26-09-02-COGS-DR-001`, Jira `ERPPLUS-142`) was readied and prompted by Boss but has not been executed. No commit, branch, or archived record exists for any of its 37 mandatory deliverables. This is the controlling blocker for nine of the twelve `JT-*` items above. | `BLOCKING` | Boss to commission execution; Accounting Owning Team to execute and pass the Teach-Back gate (COGS research prompt §17) | Schedule and run the already-authorized session. No new Boss authorization is required — only execution of what readiness commit `4f8b7d0` and prompt commit `d57a52c` already permit. |

---

## 8. What Would Change This Register

Unchanged from v1.0 §7, with one addition: **execution of the COGS Deep Research session to a terminal status** would, on its own, resolve `RISK-COGS-01` and supply the evidence needed to move all nine `COGS-GATED` `JT-*` items from Lane C to decidable (though not to *decided* — a Joint session would still need to rule using that evidence). This session performs none of that and closes nothing.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
