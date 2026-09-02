# 02 — Accounting COGS Dependency Register

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V2-001` | Jira: `ERPPLUS-139`
Status: `MANDATORY FIRST GATE RECORD — ACCOUNTING COGS GAP EVIDENCE NOT AVAILABLE`

---

## 1. What This File Is

The new-session prompt for Inventory Final Solution v2.0 (§2) requires that, before writing any valuation, COGS, landed-cost posting, period-close, return-cost-basis, or build-readiness conclusion, this session locate and read the Accounting COGS Gap evidence, and record: a direct GitHub link, a commit SHA, a status (open / hold / closed / Boss-approved), and an Accounting or Joint Accounting-Inventory owner.

This file is that record. It reports the search performed (full detail in `01_EVIDENCE_INTAKE_REGISTER.md` §3) and its result: **the evidence does not exist as a completed, published package.**

---

## 2. The Dependency Package That Was Authorized But Not Executed

| Item | Value |
|---|---|
| Session name | `SMEPLUS-26-09-02-COGS-DR-001` |
| Jira | `ERPPLUS-142` |
| Control level | `/L9999.9999` |
| What was authorized | A Boss-directed, read-only, menu-by-menu, field-by-field, evidence-first deep research session into COGS, costing policy, Periodic vs. Perpetual accounting, Product Category and Product accounting configuration, and their interface with Inventory Final Solution v1.0 |
| Pre-prompt readiness verdict | `READY — ISSUE COGS MENU-BY-MENU DEEP RESEARCH NEW SESSION PROMPT / L9999.9999` (commit `4f8b7d0be000046b1ea62624e5397baea0603125`) |
| New-session prompt issued | Yes (commit `d57a52c6f749a89226305b05d05beeb383b10f6c`), naming 37 mandatory deliverables under a dedicated controlled execution path, three permitted terminal statuses, and an explicit Owner Teach-Back gate |
| Execution performed | **No.** No deliverable file, no menu evidence sheet, no periodic or perpetual model, no 32-scenario register, no 9-Veto/9-Special-Team findings, no Teach-Back record, no manifest, and no session closure exist for this session name anywhere this session could reach |
| Terminal status reached by that session | **None.** Readiness to start is not a terminal status; the prompt's own three permitted terminal statuses (`COGS DEEP RESEARCH COMPLETE...`, `HOLD / EVIDENCE REQUIRED...`, `FAIL / FROZEN...`) were never assigned |
| Direct GitHub link to a completed evidence package | **None exists** |
| Commit SHA for a completed evidence package | **None exists** — the only commit SHAs that exist are for the pre-prompt readiness record and the prompt itself, both of which authorize research rather than report it |
| Status | **NOT STARTED** — readiness and authorization exist; execution does not |
| Owner named for a result | **None** — there is no result to assign an owner to. The prompt names the Accounting Owning Team as the party who must eventually pass the Teach-Back gate (prompt §17), but that team has not yet executed the research the gate would test |

---

## 3. Why This Is a Material Delta Trigger, Not a Formality

The COGS Deep Research prompt itself explains why the gap matters (prompt §1, §2): Inventory Final Solution v1.0 already emits valuation facts and already leaves twelve Joint Accounting↔Inventory decisions open, beginning with which concept owns valuation policy. Before Accounting can rule on any of those twelve decisions, Accounting itself must first establish verified understanding — not assumed, not carried over from a reference system — of COGS recognition timing, Periodic-versus-Perpetual accounting, Product Category and Product accounting inheritance, and how a decrease in Inventory Value is or is not COGS.

Put directly: **the Inventory side of the design (files 07–08 of v1.0) describes what Inventory emits. The Accounting side of the interface — what happens to what Inventory emits — has not yet been researched at the depth Boss himself commissioned.** Advancing any valuation, COGS, landed-cost, period-close, or return-cost-basis conclusion in this session would mean this session inventing the Accounting half of a boundary that only Accounting is authorized to define, using no evidence, which is exactly what the Boss Ruling §3 and the new-session prompt §2 forbid.

---

## 4. Every v1.0 Item That Depends on This Gap

| Register ID | Item | Depends on COGS Gap evidence because |
|---|---|---|
| `JT-01` / `GAP-FS-01` | Which concept owns valuation policy | The COGS research's Menu B (Product Category accounting) and Menu C (Product accounting tab) are the mandatory evidence source for how the reference system's category/product inheritance model informs — without dictating — an SMEsPlus policy-ownership design |
| `JT-02` | Permitted costing methods and change rules | COGS research §9 (costing-method deep research) is the mandatory evidence source |
| `JT-03` | Continuous vs. periodic valuation timing | COGS research §8 (Periodic vs. Perpetual deep research) is the mandatory evidence source |
| `JT-04` | Cost-of-goods-sold recognition timing | COGS research §8.2 and §12 (COGS recognition/account flow proof) are the mandatory evidence source |
| `JT-05` / `C-03` | Return cost basis | COGS research scenario 17/18 (customer return, same/later period) and §19 Contract C are the mandatory evidence source |
| `JT-06` | Late supplier bill after period close | COGS research scenario 5/6 and §8.1 are the mandatory evidence source |
| `JT-07` | Period close design and snapshot content | COGS research Menu F (stock closing/period close) is the mandatory evidence source |
| `JT-08` / `LC-06` | Landed-cost eligibility and posting structure | COGS research §21 (landed cost, late cost, price difference) is the mandatory evidence source |
| `JT-09` | Work-in-progress recognition timing | COGS research §7 Special Team, Menu H, and scenarios 27–29 are the mandatory evidence source |
| `GAP-FS-12` | Whether analytic cost belongs in Inventory v1.0 or a later release | Indirectly gated: analytic cost (v1.0 file 08 §5) must stay distinguishable from financial valuation, and that distinction is sharper once financial valuation itself is evidenced |
| `TH-HOLD-03` | Import duty/VAT treatment in landed cost | COGS research §13 (Thai accounting/tax/audit track) is the designated evidence source; still `HOLD / EVIDENCE REQUIRED` regardless |
| `TH-HOLD-05` | Accepted Thai costing norms | Same as above |

**Not gated — may proceed independently of this evidence:** `RISK-C02` (movement idempotency), `RISK-U03` (multi-tenant invariants), `GAP-FS-08` (migration provenance), `GAP-FS-11` (Thai user validation), and every non-valuation menu, process, and control item in v1.0 files 03–06, 09–11. These are carried forward unchanged; see file 05 §1.

---

## 5. What This Session Does Instead

Per the new-session prompt §2 and the Boss Ruling §3, this session does not stop entirely. It produces the controlled V2.0 dependency package this file belongs to: a register of what is gated (this file), a decision matrix of what may proceed and what must wait (file 04), a functional delta design that states dependency framing rather than resolved conclusions for every scope area named in the new-session prompt (file 05), and an AAS+/PMO review of whether this dependency gate was correctly honored (file 06).

**Nothing in files 02–09 of this package states a valuation, COGS, landed-cost, period-close, or return-cost-basis conclusion as decided.** Where v1.0 already used a form of words that could be misread as a conclusion, this package does not repeat it without the same qualification v1.0 used.

---

## 6. Required Next Action

The single controlling next action for the Inventory-Accounting interface is **execution of the COGS Deep Research session that has already been readied and prompted but never run.** This is not a new authorization request — Boss already authorized it (readiness commit `4f8b7d0`, prompt commit `d57a52c`) — it is a statement that the authorized work has not yet happened. See file 09 for the full next-session recommendation.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
