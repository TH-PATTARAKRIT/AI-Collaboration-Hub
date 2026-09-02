# 04 — Valuation / COGS / Period-Close Decision Matrix

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V2-001` | Jira: `ERPPLUS-139`
Status: `DEPENDENCY CLASSIFICATION — NOTHING BELOW IS A DECISION, ONLY A ROUTING`

---

## 1. Purpose

The new-session prompt §2 permits this session to "produce a controlled V2.0 dependency package that lists what can proceed and what must wait" even though the Accounting COGS Gap evidence is missing. This file is that list. It classifies every open valuation-adjacent item from v1.0's register (file 12) into one of four lanes. It resolves nothing; it routes.

This matrix directly answers Boss decision **#14** from v1.0's Boss Final Gate Package ("Does the whole Inventory design wait on the valuation decision, or may non-valuation design continue?", tension `T-2`, v1.0 file 13 lane `S-6`) with the evidence now available: the Accounting side of the interface has not been researched, so the question is no longer only "is the Inventory design blocked" but "which specific items are blocked on the *missing research*, as opposed to blocked on a *decision Accounting could make today if convened*."

---

## 2. The Four Lanes

| Lane | Meaning |
|---|---|
| **A — Proceeds now, unaffected** | Not a valuation-adjacent item. No dependency on the COGS Gap. Already unblocked in v1.0. |
| **B — Proceeds now, valuation-adjacent but not gated** | Touches valuation vocabulary but does not require COGS-specific accounting evidence to decide; a Joint session could rule on it today using v1.0's evidence alone. |
| **C — Waits for Accounting COGS Gap evidence specifically** | Cannot be responsibly decided — by Joint session or by Boss — until the COGS Deep Research menu-by-menu evidence exists, because the decision requires proven Accounting-side behaviour this programme has not yet researched. |
| **D — Waits for a Boss-only ruling, independent of COGS evidence** | Blocked on governance, not on accounting research. COGS evidence would not unblock these even if it existed today. |

---

## 3. Classification

| Register ID | Item | Lane | Reasoning |
|---|---|---|---|
| `JT-01` / `GAP-FS-01` | Which concept owns valuation policy | **C** | Requires proven understanding of Product Category vs. Product accounting-configuration inheritance and precedence — COGS research Menu B, Menu C, §11 |
| `JT-02` | Permitted costing methods and change rules | **C** | Requires COGS research §9 |
| `JT-03` | Continuous vs. periodic valuation timing | **C** | Requires COGS research §8 |
| `JT-04` | Cost-of-goods-sold recognition timing | **C** | Requires COGS research §8.2, §12 |
| `JT-05` / `C-03` | Return cost basis | **C** | Requires COGS research §19 Contract C and scenarios 17–18 |
| `JT-06` | Late supplier bill after close | **C** | Requires COGS research §8.1 and scenario 5–6 |
| `JT-07` | Period close design and snapshot content | **C** | Requires COGS research Menu F |
| `JT-08` / `LC-06` | Landed-cost eligibility and posting structure | **C** | Requires COGS research §21 |
| `JT-09` | Work-in-progress recognition timing | **C** | Requires COGS research Menu H, scenarios 27–29 |
| `JT-10` | Inter-company transfer treatment | **B** | This is primarily an Inventory-side company-boundary and dual-fact-emission question (v1.0 file 07 §2, "two facts in two companies"); the Joint session could scope it without waiting on COGS-specific evidence, though the Accounting posting on each side still ultimately depends on `JT-01`–`JT-04` |
| `JT-11` / `G-5` | Opening-balance certification | **B** | This is a migration/cutover certification process question, not a costing-method question; it can be designed in parallel (see also candidate D, migration provenance, in file 09) |
| `JT-12` | Period lock date policy and exception granting | **B** | The *mechanism* (named grantor, written reason, expiry, no global bypass — v1.0 file 07 §4) is already fully specified on the Inventory side; only the *late-arriving-cost* consequence of a backdated exception is gated, and that consequence is `JT-06`, already lane C |
| `RC-03` | Valuation-to-ledger reconciliation report | **B, with a C dependency for full closure** | The report *requirement* (v1.0 file 08 `VR-04`) can be designed now; the report cannot be *validated against real figures* until `JT-01`–`JT-04` are resolved |
| `GAP-FS-12` | Whether analytic cost belongs in v1.0 scope | **A** | This is a programme-scope question for Boss (v1.0 file 08 §5 already separates analytic cost from financial valuation categorically); COGS evidence does not change the scope question |
| `TH-HOLD-03` | Thai import duty/VAT treatment in landed cost | **C, and separately statutory-held regardless** | Gated on the Thai Accounting/Tax/Audit track inside the COGS research (prompt §13); remains `HOLD / EVIDENCE REQUIRED` even after that research completes, until authoritative Thai evidence is obtained |
| `TH-HOLD-05` | Accepted Thai costing norms | **C, and separately statutory-held regardless** | Same reasoning |
| `RISK-C02` | Movement idempotency | **A** | Not a valuation question; already open on its own track (Boss-only severity ruling, v1.0 `T-1`) |
| `RISK-U03` | Multi-tenant invariant set | **A** | Not a valuation question |
| `GAP-FS-08` | Migration provenance | **A** | Not a valuation question, though it will eventually need to carry cost history once `JT-01`–`JT-04` are resolved — see file 05 §7 |
| `GAP-FS-11` | Thai user validation | **A** | Not a valuation question |
| `RISK-C05` / `RISK-C05B` | History containment | **D** | Boss-only governance ruling; unrelated to accounting evidence |
| `RISK-U07` | Charter conflict | **D** | Boss-only governance ruling |
| `RISK-CR-01` | Authoritative-branch decision | **D** | Boss-only governance ruling |

---

## 4. Reading This Matrix

**Everything in Lane A can proceed today** as its own independent design or research session — none of it is blocked by this HOLD. **Everything in Lane B can be scoped or drafted today**, with the explicit caveat that final acceptance still waits on Lane C items. **Everything in Lane C is what the COGS Deep Research session, once executed, will unblock in a single pass** — this is the strongest argument for making that session the controlling next action (file 09). **Everything in Lane D needs Boss directly and would not move even if the COGS research were complete tomorrow.**

Nine of the twelve `JT-*` items land in Lane C. This confirms, with evidence rather than assertion, that the Boss Ruling's dependency lock (§3) is doing real work: it is not blocking the whole Inventory module, but it is blocking the specific decisions that make up most of what "closing the valuation design" would mean.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
