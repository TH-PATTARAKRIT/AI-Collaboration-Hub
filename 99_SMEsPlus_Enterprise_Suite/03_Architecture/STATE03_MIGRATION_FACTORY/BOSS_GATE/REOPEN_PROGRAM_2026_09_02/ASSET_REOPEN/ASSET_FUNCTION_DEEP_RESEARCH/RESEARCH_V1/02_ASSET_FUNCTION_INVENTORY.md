# 02 — Asset Function Inventory

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `EVIDENCE COLLECTION — FLAT CATALOG, PRE-ANALYSIS`

---

## 1. Purpose

A flat catalog of every function/field/state named in the research objects, before any analysis or classification. This file is deliberately non-evaluative — see files `03`–`14` for forensic analysis of each item.

---

## 2. Asset Model (template-level policy record)

Name, active flag, depreciation method (Straight Line / Declining / Declining Then Straight Line), duration/number of depreciations, computation method (No Prorata / Constant Periods / Based on Days per Period), not-depreciable value (salvage/residual carve-out), fixed asset account, depreciation expense account, accumulated depreciation account, journal, analytic distribution, company, currency, first-depreciation-date behavior.

## 3. Asset (instance record)

All Asset Model fields (inherited, potentially overridden), acquisition/purchase date, original value, book value, depreciation board/schedule (planned entries: date, depreciable value, cumulative depreciation, book value), state (draft/running/paused/close/disposed — exact state machine `UNRESOLVED`, see file `07`), linked vendor bill/purchase source (if any), disposal date and disposal value, gain/loss on disposal.

## 4. Equipment

Name/identity, equipment category, owner type (company vs. employee), used-by employee or department, company, serial number, assigned/effective date, work center link, product link (if any — see file `05`), maintenance team, scheduled/preventive maintenance frequency, maintenance request history, status (candidate states: in service / idle / standby / under maintenance / breakdown / out of service / disposed — cardinality and exact enum `UNRESOLVED`, see file `04`).

## 5. Maintenance Request

Equipment reference, work center reference (if applicable), maintenance type (corrective/preventive), request date, scheduled date, duration, team, technician/responsible, stage/state (new/in progress/repaired/scrap), priority, cost fields (if any — challenged directly in file `06`, not assumed present).

## 6. Work Center

Name, code, company, cost per hour (per-workcenter rate), cost per employee (per-employee rate), individual employee hourly-cost override, capacity/efficiency, working schedule/time-off, equipment assigned to the work center (candidate cardinality: one-to-many — `UNRESOLVED` whether enforced or advisory, see file `11`).

## 7. Product ↔ Equipment ↔ Asset Lineage Candidates

Product type (storable/consumable/service — terminology varies by reference-ERP version; treated generically), purchase order line, receipt/goods-receipt event, automatic-vs-manual Equipment creation trigger, automatic-vs-manual Asset creation trigger, capitalization threshold/trigger (candidate, not evidenced as a built-in feature — see file `05`).

## 8. Depreciation Engine Mechanics

Depreciation board generation, prorata-first-period computation, prorata-last-period/disposal computation, month-length handling (28/29/30/31-day months), leap-year handling, rounding rule, partial-period handling on modify/pause/dispose, residual-value carve-out from depreciable base, posted vs. draft journal-entry states per depreciation line.

## 9. Financial Posting / GL Concepts

Fixed Asset account (balance sheet), Accumulated Depreciation account (contra-asset), Depreciation Expense account (P&L), disposal gain/loss account, journal used for depreciation entries, analytic account/distribution for cost-center attribution.

## 10. Residual / Salvage Value

Not-Depreciable Value field (reference-ERP term observed), Depreciable Value = Original Value − Not Depreciable Value (documented formula), treatment at full depreciation, treatment at disposal, treatment on early disposal above/below book value.

## 11. Manufacturing Cost Stack Candidates

Raw material cost, direct labor cost, work center operating cost (hourly), equipment-specific cost (candidate — not confirmed as a distinct field from work center cost), service/subcontracting cost, manufacturing overhead, depreciation-as-overhead (candidate, IAS/TAS 16 concept — see file `15`), maintenance cost (challenged, see file `06`), WIP account, finished-goods valuation, COGS.

## 12. Off-Balance / Internal Costing Candidates (SMEsPlus-target, not reference-ERP-evidenced)

Internal Equipment Usage Cost account (Off-Balance type, candidate), Internal Equipment Usage Offset account (Off-Balance type, candidate), audit-trail reference fields (Asset, Equipment, Work Center, MO, period, rate, usage quantity, source Asset Model) — all `DESIGN CANDIDATE`, see file `14`.

## 13. Boss-Provided Hypotheses (catalogued here, evaluated in file `21`)

- Hypothesis A: active-depreciation cost flows into production cost.
- Hypothesis B: single allocation driver for equipment/work-center cost absorption.
- Hypothesis C: a fully depreciated but still-productive asset may carry non-zero internal economic usage cost.
- Boss-selected residual costing hypothesis (post-depreciation internal usage formula, file `13`).
- Continuous residual usage hypothesis (usage continues to accrue an internal cost indefinitely after full depreciation, until disposal/removal).
- Off-balance accounting model (file `14`).
- Asset-model target control point (which record — Asset Model vs. Asset instance — should be the primary policy control point).
- Factual claim: "Thai depreciation uses daily calculation" (file `08`, file `21`).

---

This inventory is exhaustive of the research objects named in the governing brief; it is not exhaustive of every field the reference ERP's asset/maintenance modules may contain — fields not named in the governing brief's research objects were not separately catalogued.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
