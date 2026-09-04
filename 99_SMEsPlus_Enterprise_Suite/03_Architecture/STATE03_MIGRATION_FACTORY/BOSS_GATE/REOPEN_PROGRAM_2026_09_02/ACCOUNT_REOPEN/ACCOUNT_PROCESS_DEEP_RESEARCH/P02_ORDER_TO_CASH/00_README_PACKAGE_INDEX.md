# P02 ORDER-TO-CASH — FULL-SPECTRUM BUSINESS + ACCOUNTING FORENSIC DEEP RESEARCH

| Field | Value |
|---|---|
| Session ID | `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001` |
| Process | `P02 — Order-to-Cash` |
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Canonical branch | `SMEsPlus` |
| Working branch | `research/account-p02-order-to-cash-2026-09-04-001` |
| Base commit | `88f52cd` (`governance: approve canonical evidence acquisition flow`) |
| Research depth | `VERY DEEP / L99999.99999` |
| Execution model | Claude Opus 5 (high) |
| Execution date | `2026-09-04` |
| Terminal state | `READY FOR CORE ACCOUNTING RECONCILIATION` |
| Boss interaction | FINAL GATE ONLY — no Boss contact occurred during execution |

## 0. Classification Notice — READ FIRST

This package is **LAYER 2 — AUDIT QUARANTINE**.

It contains reference-ERP source citations in `path:line — method` form. Those citations are
evidence for Boss / PMO / AI-Audit only. They must **not** be transcribed into any downstream
clean-room reference package, Functional Design document, or Team B artefact.

**One exception:** `18_P02_CORE_RECON_HANDOFF_PACK.md` is authored as **LAYER 1 (clean-room)**.
It carries no vendor model name, field name, module path, method name, or file extension, and is
the only file in this package cleared for downstream semantic transfer.

Reference systems are **learning / benchmark only**. Nothing in this package authorises copying
code, schema, ORM structure, workflow implementation, or UI implementation. SMEsPlus is a new
100% clean-room Node.js SaaS ERP.

## 1. Constitutional Compliance Statement

- `NO EVIDENCE = NO PROGRESS` — every material finding carries an `EV-P02-###` evidence ID.
- `NEVER SKIP A GATE` — CP-00 .. CP-10 and CP-FINAL are recorded in `15_P02_REVISION_LOG.md`.
- `PARTIAL != PASS` — this package issues **no** advancement verdict. It issues a recommendation
  to Boss and a handoff to Core Accounting Reconciliation.
- `Independent Review != Truth. Verified Evidence = Truth Basis.`
- Boss was **not** contacted during execution. No option selection, checkpoint approval, or
  routine confirmation was requested.

## 2. Finding Classification Vocabulary

Every material statement in this package carries exactly one tag:

| Tag | Meaning |
|---|---|
| `FACT VERIFIED` | Directly observed in primary source with an `EV-P02-###` citation. |
| `SUPPORTED INTERPRETATION` | Derived from observed code paths by reasoning; not directly executed. |
| `DESIGN CANDIDATE` | A proposed SMEsPlus behaviour. Not evidence. Not approved. |
| `BOSS CONTROLLED DECISION` | Requires Boss ruling. AI has no authority. |
| `CONTRADICTED` | Evidence contradicts an earlier or obvious reading. |
| `UNRESOLVED — EVIDENCE REQUIRED` | Open. The exact missing evidence is named. |
| `HOLD — STATUTORY EVIDENCE REQUIRED` | Thai law / accounting standard / Revenue Department evidence needed. |
| `DEPENDENCY OPEN` | Blocked on a peer process (P01, Inventory, Core Ledger). |
| `HOLD — CROSS-PROCESS RECONCILIATION REQUIRED` | Blocked pending P02 ↔ Core Accounting reconciliation. |

The words `PASS`, `FAIL`, `APPROVED`, `CERTIFIED`, `PRODUCTION READY` and `SIGN-OFF` are not used
as verdicts anywhere in this package.

## 3. Deliverable Index

| # | File | Purpose | Layer |
|---|---|---|---|
| 00 | `00_README_PACKAGE_INDEX.md` | This file | L2 |
| 01 | `01_P02_PROCESS_MAP.md` | Quotation → Close spine, stage by stage | L2 |
| 02 | `02_P02_INVOICE_POLICY_MATRIX.md` | Invoice policy ≠ COGS recognition policy | L2 |
| 03 | `03_P02_DELIVERY_COGS_TRACE.md` | Inventory-out → valuation → COGS forensic trace | L2 |
| 04 | `04_P02_REVENUE_AR_TRACE.md` | Revenue → AR forensic trace | L2 |
| 05 | `05_P02_BUSINESS_EVENT_REGISTER.md` | Business events, owners, identity | L2 |
| 06 | `06_P02_ACCOUNTING_EVENT_REGISTER.md` | Accounting events and their trigger conditions | L2 |
| 07 | `07_P02_EVENT_TO_GL_MATRIX.md` | Event → journal / subledger effect | L2 |
| 08 | `08_P02_RETURN_CREDIT_REFUND_MATRIX.md` | Return vs credit note vs refund separation | L2 |
| 09 | `09_P02_PAYMENT_RECONCILIATION_MATRIX.md` | Receipt ≠ settlement ≠ reconciliation | L2 |
| 10 | `10_P02_CROSS_PROCESS_OWNERSHIP.md` | Who owns each fact across P01/P02/Inventory/Core | L2 |
| 11 | `11_P02_EDGE_CASE_MATRIX.md` | Partial / backorder / backdate / lock / cancel / FX | L2 |
| 12 | `12_P02_CONTRADICTION_REGISTER.md` | Material contradictions, with disposition | L2 |
| 13 | `13_P02_SOURCE_LINK_REGISTER.md` | `EV-P02-###` → `path:line — method` | L2 |
| 14 | `14_P02_EVIDENCE_MANIFEST.md` | Population, denominators, SHA-256 manifest | L2 |
| 15 | `15_P02_REVISION_LOG.md` | Checkpoints, research errors, revisions | L2 |
| 16 | `16_P02_AAS03_CHALLENGE.md` | Four AAS-03 expert challenges | L2 |
| 17 | `17_P02_AAS_PLUS.md` | AAS+ synthesis, preserved disagreements | L2 |
| 18 | `18_P02_PMO.md` | PMO control view and gate recommendation | L2 |
| 19 | `19_P02_CORE_RECON_HANDOFF_PACK.md` | Clean-room handoff to Core Accounting Reconciliation | **L1** |
| — | `L2_AUDIT_QUARANTINE/` | Raw evidence extracts from parallel research tracks | L2 |

## 4. Absolute Invariant Under Test

```
ONE BUSINESS FACT
  -> ONE CANONICAL EVENT OWNER
  -> ONE ACCOUNTING EFFECT PATH
```

Attack surfaces exercised: DOUBLE POSTING · DOUBLE VALUATION · DOUBLE COGS · DOUBLE REVENUE ·
DOUBLE AR · DOUBLE TAX · DOUBLE SETTLEMENT.

## 5. Headline Position (detail in `18_P02_PMO.md`)

The reference process does **not** satisfy the absolute invariant as a single coherent design.
It satisfies it *per subsystem* while allowing the subsystems to disagree with one another. The
governing structural fact discovered in this research is:

> **In P02 the quantity that drives revenue and the quantity that drives cost of sales are two
> independent, separately mutable counters, and the accounting event that recognises cost is
> owned by the invoice, not by the physical outflow that actually consumed the inventory.**

Everything else in this package is a consequence of, or an exception to, that sentence.
