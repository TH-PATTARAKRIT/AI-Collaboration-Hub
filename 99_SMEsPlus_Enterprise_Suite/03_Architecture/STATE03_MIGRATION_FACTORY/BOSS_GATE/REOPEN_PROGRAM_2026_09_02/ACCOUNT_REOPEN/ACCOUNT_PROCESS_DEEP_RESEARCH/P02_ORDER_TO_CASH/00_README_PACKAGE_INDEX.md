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

**One exception:** `19_P02_CORE_RECON_HANDOFF_PACK.md` is authored as **LAYER 1 (clean-room)**.
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
| 20 | `20_P02_SCOPE_OWNERSHIP_MATRIX.md` | PLATFORM / TENANT / COMPANY scope determination — added by correction `SMEPLUS-26-09-04-ACC-REV2-CORR1` | L2 |
| 21 | `21_P02_DEPLOYED_DATABASE_EVIDENCE.md` | **Deployed-database evidence** — added after discovering the declared no-database-access statement was an untested negative claim | L2 |
| — | `L2_AUDIT_QUARANTINE/` | Raw evidence extracts from parallel research tracks | L2 |

## 3a. Research Depth Map — L1 … L6 And The Very-Expert Layer

Depth label for this session: `VERY DEEP / L99999.99999`. The structured levels map to deliverables as
follows, so that no level is claimed without a file behind it.

| Level | Question | Where answered |
|---|---|---|
| **L1 — Domain semantics** | What is Order-to-Cash, and what are its irreducible facts? | `01` §1–§2; `19` §1 |
| **L2 — Model and relationship** | Which records hold those facts, how are they related, and which fields are derived, stored or writable? | `01` §3; `05` §1; `13` |
| **L3 — Function forensic** | Which code path produces each effect, under exactly which branch? | `03`, `04`, and the four track extracts |
| **L4 — Event and state** | What business events exist, what accounting events exist, and what triggers each? | `05`, `06` |
| **L5 — Accounting effect** | What does each event do to the ledger, and where can it leave the ledger wrong? | `07`, `09` |
| **L6 — Control and boundary** | What controls exist, what do they actually block, and where is the boundary? | `11`, `20`, `12` |

**Very-expert layer**, as required by the directive:

| Requirement | Where discharged | Result |
|---|---|---|
| Source proof | throughout | **discharged** — 73 evidence identifiers |
| **Database proof** | `21_P02_DEPLOYED_DATABASE_EVIDENCE.md` | **DISCHARGED for configuration and posting-outcome questions.** Originally declared undischarged **on an untested negative claim** — five deployed archives were on the host. See `21` §0 and `RE-13`. |
| **Runtime proof** | — | **NOT DISCHARGED.** Reading a database is not executing the system. `C-04` needs a transaction, not a table. |
| Event-to-ledger | `07` | discharged |
| Revenue / cost separation | `02`, `03`, `04` | discharged |
| Return and reversal | `08` | discharged |
| Thai tax | `11` §7; T3 extract | discharged as **evidence**; every **statutory** conclusion is held |
| SaaS boundary | `20`; T4 extract | discharged at company level; tenant level is design candidate, since the reference has no tenant concept |
| Double-recognition attack | `06` §4 | discharged — six attacks, results stated individually |
| Period-close attack | `11` §6 | discharged |
| Cross-process reconciliation | `10` | discharged as **routing**; the reconciliation itself is Core Accounting's |

**Two of the eleven very-expert requirements are not discharged, both for the same reason: this session
had no database and no runtime.** That is stated here rather than buried, because it bounds what this
package can support.

## 3b. Configuration Premise — Applies To Every Cost Finding In This Package

Stated here once, prominently, because the independent challenge found it was assumed in eleven files and
declared in none.

**Every cost-of-sales finding in files `02`, `03`, `06`, `07` and `11` presumes all three of:**

1. split cost recognition is **on** at company level;
2. the product is **storable**;
3. its category is under **real-time** valuation.

**A Thai company as shipped has none of the three.** The chart does not set the recognition boolean and
the installer defaults it off (`EV-P02-042`, `EV-P02-043`); valuation defaults to manual/periodic by data
(`EV-P02-100`); and real-time valuation cannot even be switched on until three stock accounts exist, which
that chart does not supply (`EV-P02-044`, `EV-P02-045`). The recognition toggle is, moreover, exposed in
**exactly one place in the whole reference root**, and that place is an Enterprise module
(`EV-P02-101`) — so for a Community-equivalent deployment there is no settings-page route to it at all.

**Read every cost finding in this package as conditional on that premise.** Where the premise does not
hold, the finding is replaced by the more serious one in `01` S5: cost of sales is recognised **nowhere**.

## 4. Absolute Invariant Under Test

```
ONE BUSINESS FACT
  -> ONE CANONICAL EVENT OWNER
  -> ONE ACCOUNTING EFFECT PATH
```

Attack surfaces exercised: DOUBLE POSTING · DOUBLE VALUATION · DOUBLE COGS · DOUBLE REVENUE ·
DOUBLE AR · DOUBLE TAX · DOUBLE SETTLEMENT.

## 5. Headline Position (detail in `18_P02_PMO.md` and `21_P02_DEPLOYED_DATABASE_EVIDENCE.md`)

The reference process does **not** satisfy the absolute invariant as a single coherent design. It satisfies
it *per subsystem* while allowing the subsystems to disagree with one another.

**The governing structural fact:**

> **The accounting event that recognises cost is owned by the invoice, not by the physical outflow that
> actually consumed the inventory — so the quantity driving revenue and the quantity driving cost of sales
> are derived independently, and the two are reconciled after the fact by balance matching in an account
> that nobody owns.**

**What that produces, established after independent challenge:**

> **The physical event is immutable, the accounting event is reversible, and the settlement history is
> freely destructible — including across a closed period. The durability ordering is exactly inverted
> relative to accounting importance.**

**Confirmed against a deployed database** (`21`): in a live Thai company carrying **447,384 journal lines**
and **74,982 valuation layers**, the invoice-side cost-of-sales mechanism has **never executed — not
once**. That deployment recognises cost at delivery instead, straight to an expense account, with **no
position of any kind connecting it to the revenue it belongs to** — so a shipment invoiced in a later
period puts cost and revenue in different periods **permanently and undetectably**.

Everything else in this package is a consequence of, or an exception to, those three statements.

## 6. Terminal Position And Reliance

**Terminal state:** `READY FOR CORE ACCOUNTING RECONCILIATION` — which is this session's mandated endpoint
and is a **handoff, not an exit**.

`18_P02_PMO.md` recommends **HOLD** against the eight-criteria exit gate: **0 of 8 satisfied, 5 partially,
3 not**, with **six tolerance-zero candidates open**.

Three things bound reliance on this package and are stated here rather than buried:

1. **One independent challenge has run and it was not clean** — twenty package-changing findings, two of
   which **refuted statements this package had tagged `FACT VERIFIED`**. It examined roughly **half** the
   evidence base; the other half is once-verified, not twice-verified.
2. **The package's own most-repeated limitation was false.** It declared no database evidence existed;
   five deployed archives were on the host. Recorded as `RE-13`; what one pass produced is in `21`.
   **No review caught it, because every review was scoped at the findings and none at the evidence base.**
3. **Eight ordinary business situations have no analysis here** — drop-shipping, credit control,
   period-end unrealised FX revaluation, bill-and-hold, outbound consignment, warranty provisions, freight
   charges, and serial/lot-identified cost of sales.

No gate is declared satisfied. No implementation is authorised. No merge is proposed. Boss is the sole
final approver.