# 01 — Prior Evidence and Question Fingerprint Index

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `EVIDENCE RECONSTRUCTION — CP-01`

---

## 1. Purpose

This file proves prior evidence was read before new conclusions were drawn (governing prompt §4), and fingerprints the open questions this session inherits so no question already answered is re-asked without a material delta, and no open question is silently dropped.

---

## 2. Governance and Prompt Chain Read

| Document | Commit | Status |
|---|---|---|
| Pre-Prompt 9-Veto Challenge and Readiness | `4f8b7d0be000046b1ea62624e5397baea0603125` | Read in full. Readiness verdict: `READY — ISSUE COGS MENU-BY-MENU DEEP RESEARCH NEW SESSION PROMPT / L9999.9999`. No blocking veto before research. |
| New Session Prompt (this governing document) | `d57a52c6f749a89226305b05d05beeb383b10f6c` | Read in full. 37 deliverables, three-layer evidence model, 32 minimum scenarios, 9 Veto + 9 Special Team, Teach-Back gate. |
| Session archive pointer | `8d2c8aa0e4a963b50ee7c9f442a7ae58694b6daf` | Read in full. Confirms `COGS Research Execution Evidence: HOLD / NOT YET CREDITED` at time of archive — i.e. this session is the first to execute it. |
| Boss-approved 22-Scenario Accounting × Inventory Cross-Proof baseline | `296b495144bad0ce20b796ca6ac487dd1604cc40` | Presence verified on branch. Retained as a dependency this session's Contract candidates (file `31`) must feed, **not re-opened or re-litigated here**. |
| Boss-approved 16-field Inventory → Accounting Minimum Handoff Data Contract | `d9e845ede58d5a34c9ab1117482e8883d36e1314` | Presence verified on branch. Same treatment. |

---

## 3. Inventory Final Solution v1.0 — What This Session Inherits

Source: `design/inventory-final-solution-v1-2026-09-02-001`, files `07`, `08`, `10`, `12`, `13`, `14`, `17` (all read in full).

### 3.1 The interface rule already established

`Inventory emits facts. Accounting decides postings.` Inventory never writes a journal entry, selects an account, or decides recognition timing. A **valuation fact** carries: event type, quantity/unit, cost basis and amount, effective date, references, reason/approver, and policy version. This session's account-flow archetypes (file `12`) must stay inside that boundary — describing what Accounting does with a received fact, never redefining what Inventory emits.

### 3.2 Open Joint decisions this session must feed evidence into (not close)

| ID | Decision | This session's evidence file(s) |
|---|---|---|
| `JT-01` | Which concept owns valuation policy — category, product, warehouse, or a standalone versioned policy | `04`, `05`, `11` |
| `JT-02` | Permitted costing methods and change rules | `15` |
| `JT-03` | Continuous (perpetual) vs periodic valuation timing | `12`, `13`, `14` |
| `JT-04` | COGS recognition timing — dispatch vs invoice | `13`, `18` |
| `JT-05` / `C-03` | Cost basis for a customer return | `19` |
| `JT-06` | Late supplier bill after period close | `21`, `23` |
| `JT-07` | Period close design and snapshot content | `08`, `23` |
| `JT-08` | Landed-cost eligibility and posting structure | `21` |
| `JT-09` | Work-in-progress recognition timing | `22` |
| `JT-10` | Inter-company transfer treatment | `25` |
| `JT-11` / `G-5` | Opening-balance certification at cutover | `26` |
| `JT-12` | Period lock policy and backdating exception grants | `08`, `23` |

**This session closes none of `JT-01`–`JT-12`.** Every candidate produced here is explicitly evidence toward a future Joint Accounting ↔ Inventory session, not a decision.

### 3.3 Carried risks and gaps this session's evidence must not contradict

- `RISK-C05` / `RISK-C05B` — CORR-007B history containment: Boss ruling still outstanding. This session opens no pre-remediation commit content.
- `GAP-FS-01` — valuation-policy ownership blocking item, restated above as `JT-01`.
- `GAP-FS-08` — provenance reference for migration does not exist; relevant to file `26`.
- `GAP-FS-11` — no Thai user has validated any label; this session's Thai-language candidates (if any) remain `UNVALIDATED - THAI USER REVIEW REQUIRED`.
- `TH-HOLD-01`…`TH-HOLD-09` (file 07 §6 of the Inventory package) — Thai statutory items already held and routed to the Accounting-Tax track. File `24` of this session is that Accounting-Tax track evidence pass; it must explicitly reconcile against these nine IDs rather than invent a parallel numbering.

### 3.4 Handoff rows from the Inventory package this session must reconcile with (file 10, Inventory v1.0)

`HX-07` (receipt valuation fact), `HX-08` (supplier bill price vs receipt cost basis — `JT-06`), `HX-09` (issue/COGS fact — `JT-04`), `HX-10` (return facts — `JT-05`), `HX-11` (adjustment fact), `HX-12` (scrap fact + `TH-HOLD-02`), `HX-13`/`HX-14` (landed cost bills and allocation — `JT-08`), `HX-15` (valuation policy — `JT-01`/`JT-02`/`JT-03`), `HX-16` (period lock — `JT-12`), `HX-17` (close valuation summary — `JT-07`), `HX-20` (manufacturing valuation — `JT-09`), `HX-24` (certified opening balances — `JT-11`/`G-5`).

File `31` (COGS-to-Inventory handoff contract candidates) must be written so that Contracts A/B/C map cleanly onto this existing `HX-*` register rather than inventing a second, conflicting vocabulary.

---

## 4. Account Module Evidence — Last Known State

Per session memory (`smeplus-account-module-batch-a-gate-status`, snapshot at Batch A close, 2026-09-02): the Account module gate register is **entirely open**. `COA-G01` is `HOLD / EVIDENCE REQUIRED — BOSS DECISION PENDING` and blocks `COA-G02`–`COA-G05`; `COA-G06` (VAT/CIT/WHT ownership) is open; the Account + Inventory Backbone baseline is `HOLD` pending Joint Session 3 (`ERPPLUS-140`), not yet convened.

**This snapshot was not re-verified against a fresh read of the live Account gate register in this session** (out of this session's assigned scope — COGS/costing/valuation, not Account-module governance mechanics). It is treated here strictly as *last known state as of 2026-09-02*, and file `34` (Next Controlled Action and Owner Matrix) flags that a fresh Account-module read is needed before any Joint session convenes on the strength of this package.

---

## 5. Question Fingerprint Register

Fingerprints the 18 mandatory questions from the governing prompt §6, so each is traceably answered or held, once, without duplication.

| Q# | Question (abbreviated) | Primary answering file(s) | Status at index time |
|---|---|---|---|
| 1 | Where is valuation/accounting policy configured; inheritance/override precedence | `03`, `04`, `11` | Open — assigned |
| 2 | Exact meaning of Product Category accounting fields | `04` | Open — assigned |
| 3 | Exact meaning of Product → Accounting tab Income/Expense Account and when each is used | `05` | Open — assigned |
| 4 | Periodic vs Perpetual lifecycle, Purchase → Receipt → Bill → Sale → Delivery → Invoice → Closing | `12`, `13`, `17`, `18` | Open — assigned |
| 5 | What event recognizes COGS under each pattern/version | `13`, `14`, `18` | Open — assigned |
| 6 | How Inventory Value reaches Balance Sheet inventory accounts | `06`, `12`, `13` | Open — assigned |
| 7 | How cost is released from Inventory Value to COGS/other classification | `12`, `13`, `27` | Open — assigned |
| 8 | Which stock decreases are NOT COGS | `20` | Open — assigned |
| 9 | Costing method interaction with recognition timing | `15` | Open — assigned |
| 10 | Product Category default vs Product override, historical/config change impact | `11` | Open — assigned |
| 11 | Return/reversal cost basis, link to original cost fact | `19` | Open — assigned |
| 12 | Late supplier bills / landed cost / price difference after partial or full sale | `21` | Open — assigned |
| 13 | Period close / stock closing / cut-off / backdating | `08`, `23` | Open — assigned |
| 14 | Manufacturing RM/WIP/FG/COGS boundary | `22` | Open — assigned |
| 15 | Multi-company/tenant isolation and account-policy ownership | `25` | Open — assigned |
| 16 | Migration/opening inventory and historical COGS continuity | `26` | Open — assigned |
| 17 | Reconciliation identities: physical qty, Inventory valuation, Accounting balance, COGS | `27` | Open — assigned |
| 18 | Version-delta behavior across reference versions; no silent carry-forward | `02` | Open — assigned |

No question above is answered by this file. This file is the routing index; the answering files are `02`–`27`, synthesized in `33`.

---

## 6. No-Repeat-Without-Delta Statement

Every question in §5 is materially distinct from the Inventory Final Solution v1.0 package (which explicitly declined to answer any of them — see §3.2) and from the Account module Batch A pass (which is a governance/routing pass, not a COGS technical study). No question in this register duplicates a already-answered question from either source. This satisfies the governing prompt's `No repeated question without a material delta` rule.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
