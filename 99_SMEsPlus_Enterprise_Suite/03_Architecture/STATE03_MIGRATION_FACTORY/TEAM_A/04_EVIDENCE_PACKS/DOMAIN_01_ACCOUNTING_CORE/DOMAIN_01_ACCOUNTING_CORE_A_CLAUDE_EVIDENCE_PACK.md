# DOMAIN_01 — ACCOUNTING CORE — TEAM A (CLAUDE) EVIDENCE PACK
## AUDIT-READY / CORRECTIVE ROUND CORR-001

| Field | Value |
|---|---|
| Round | SMEPLUS-26-08-29-MIG-A-D01-CORR-001 (controlled corrective) |
| Continues | MIG-A-EXPERT-DR-001 (b2e5a2a / c441443) · MIG-A-D01-ACCOUNTING-CONT-001 |
| Team | A — Source Extraction & Observation (Maker) |
| Board | Board06 — Data & Canonical Model |
| Executor | Claude AI Fable — Maker / Research Executor |
| STEP | **TBD / BASELINE LINKAGE REQUIRED** (STEP0303R5 = prior governance/planning evidence only; **not** bound) |
| Status | **CORRECTIVE ROUND EXECUTED — READY FOR CHATGPT RE-AUDIT — CONDITIONAL, RESIDUAL GAP DOCUMENTED** |

---

## 1. EXECUTIVE SUMMARY
Accounting Core in the reference system is a single generic journal-entry model: one header
(`account.move`) and one line (`account.move.line`) carry every financial document, typed by
`move_type` and classified by journal. Accounts are a coded list under a 19-value type
enumeration. The lifecycle has exactly three states.

This corrective round closed the A5 database gap by **direct observation** and partially closed
A6 by **real independent triangulation**, and in doing so **corrected a materially unsafe claim**
made in the prior round.

## 2. SCOPE
Chart of accounts · account types/groups · journals · entries · items · draft/posted/cancelled
lifecycle · posting rules · debit/credit invariants · period & lock behaviour · multi-company ·
multi-currency · analytic (coupled only) · reversal/correction · audit trail · source-to-dump proof.
**Deferred as dependencies only:** AR/AP · Payments · Tax/VAT/WHT · Assets · Inventory Valuation · Reporting.

## 3. SOURCE BASELINE
```
RESEARCH SOURCE INVENTORY BASELINE = 1,504 modules
NOT product scope · NOT approved functional scope · does NOT authorize reuse
```
62 (`01 ACCOUNT`) + 1,371 (`02 OTHER`) + 69 (`addons_extra`) + 2 (`ks_*`).
`ks_dashboard_ninja` / `ks_dn_advance` remain separately classified; classification unchanged.

## 4. RESEARCH METHOD
Read-only source observation (LGPL-3 only) · manifest/metadata parsing · **direct offline
`pg_restore -l`** metadata listing · independent public-source triangulation · A7 neutralization ·
A8 classification. Source path verified unmodified. No OEEL-1/OPL-1 source body read.

## 5. SOURCE EVIDENCE
34 anchored findings (SE-01…SE-34) in `02_SOURCE_EVIDENCE.md`, each a file+line reference in
the readable `account` module. **Method note recorded:** Odoo 19 declares DB constraints via
`models.Constraint(...)`, not `_sql_constraints` — a grep for the legacy form returns 0 and
would wrongly suggest no DB constraints exist.

## 6. DATABASE EVIDENCE — DIRECTLY RE-VERIFIED
Archive `iTEST02`, created 2026-06-14 14:41:20 UTC, PostgreSQL **18.4**, CUSTOM v1.16-0,
**28,648 TOC entries**, owner `efaplus`.

| Object type | Count |
|---|---:|
| FK CONSTRAINT | 5,141 |
| SEQUENCE | 2,871 |
| TABLE | 2,763 |
| CONSTRAINT (PK/UNIQUE/CHECK) | 1,860 |
| INDEX | 1,808 |
| TABLE DATA | 1,395 |
| VIEW / RULE / EXTENSION | 36 / 9 / 6 |
| **TRIGGER** | **0** |

Tables (1,395) and FK (5,141) **match prior evidence exactly**. CHECK constraints, triggers and
rules are **newly established** — the prior inventory could not represent them.
Record population **not obtained**: listing only, no restore, no row read.

## 7. INDEPENDENT EVIDENCE (A6 — PARTIALLY CLOSED)
`EXTERNAL_RESEARCH_ACCESS = AVAILABLE`. 3 of 9 targets triangulated, 10 real citations, zero
fabricated standards, **no IFRS/TFRS/Thai clause cited anywhere**.
- **Debit=credit** → Universal accounting principle (P1)
- **Correction by reversal, not deletion** → Cross-ERP pattern; SAP B1 *forbids* deleting posted entries (P4)
- **Period close prevents posting** → Cross-ERP pattern; NetSuite uses 3 states + 1 override permission (P4)

## 8–14. CAPABILITIES · PROCESSES · RULES · STATE/EVENTS · MATH · DATA SEMANTICS · CONFIG
15 capabilities · 7 processes · 21 business rules (incl. 4 **database-enforced**) · 3 states +
8 events · 7 mathematical model statements · 15 data-semantic entries · 14 configuration items.
Full detail in artifacts 03–11.

## 15–17. SECURITY · AUTOMATION · EXCEPTIONS
5 security observations (incl. per-user lock variants) · 8 automations (incl. the balance-check
suppression) · 6 database exceptions with DBX-06 **retracted and corrected**.

## 18. EDGE CASES
18 registered, incl. three newly added: two conditions **prevented at database level**
(EC-16, EC-17) and one lock-bypass escape (EC-18).

## 19. MIGRATION RELEVANCE
16 classified items. Headline: **MC-05 — the balance invariant must be re-established, not
inherited.** Derived columns recomputed, not carried. Vendor packaging not inherited.

## 20. CROSS-DOMAIN DEPENDENCIES
10 couplings registered; **4 are to OEEL-1 black-box modules** that write into the core.

## 21. CLASSIFICATION A–G
**A 4 · B 4 · C 2 · D 4 · E 7 · F 2 · G 4 = 27 findings** (prior round 22; +5 this round).
E/F remain RESTRICTED/QUARANTINE. G carries **zero progress credit**.

## 22. PROVENANCE P1–P8
P1 accounting principle — **now used** (triangulated) · P4 cross-vendor documentation — **now
used** · P6 customer-approved DB evidence — **now direct** · P7 vendor source observation — used ·
P8 inference — marked wherever used. P2/P3/P5 per register. No finding rests on an
unavailable provenance.

## 23. CRITICAL FINDING REGISTER — CANONICAL
```
Critical Findings registered = 6
Neutralization records       = 5   (N-02 covers CF-04 + CF-06)
Verified Fact (mechanism)    = 6
Evidence Missing (data-level)= 1   (CF-01 data-level balance)
```
CF-01 entry-level balance not DB-enforceable · CF-02 opt-in tamper evidence · CF-03 six lock
controls + bypass · CF-04 reversal is a relationship · CF-05 exact decimal money · CF-06 posted
history mutable. Full table in `CRITICAL_FINDING_REGISTER.md`.

### THE CORRECTION THAT MATTERS
The prior round claimed "zero CHECK constraints, therefore no database enforcement". That
reasoning is **retracted**: the inventory it relied on contains only FK/PK/UNIQUE across all
1,395 tables and **cannot represent CHECK constraints at all**. Direct observation shows four
CHECK constraints **do** exist on `account_move_line`.

The conclusion nonetheless survives, on stronger and narrower evidence: *entry-level*
`Σdebit = Σcredit` cannot be enforced by a row-level CHECK (it is an aggregate), and the
database contains **zero triggers**. So the only enforcement is application code that is
explicitly suppressible.

**Migration consequence (principle candidate, not design):**
> Migrated Accounting Entries must be independently validated for debit/credit balance and not
> assumed valid merely because records exist in the source database.

## 24. UNKNOWN REGISTER
12 open gaps. 1 closed this round (GAP-D01-02). 3 added (data-level balance; A6 remainder;
`account_move` CHECK enumeration). Class G = 4.

## 25. QUARANTINE REGISTER
11 items — 5 OEEL-1 modules, 3 CLASS-D, 2 `ks_*`, vendor patterns (E), dump row data.
**No quarantined content appears in Team B Candidate Input.**

## 26. ADVANCEMENT CANDIDATES — 7
All labelled `ADVANCEMENT_CANDIDATE — TEAM B INPUT ONLY AFTER AUDIT`. ADV-03 and ADV-04 are now
**independently supported** by NetSuite and SAP B1 documentation respectively. No target code,
schema, API, DTO, class, service or workflow appears anywhere in this pack.

## 27. EVIDENCE COMPLETENESS
Critical findings validated (mechanism) **6/6 = 100%** · data-level proof **0/1 = 0%** ·
direct DB structural verification **13/13 = 100%** · record population **0%** ·
independent triangulation **3/9 = 33%** · traceability **34/34 = 100%** ·
unknowns **4** · quarantine **11**.
Domain coverage vs total scope: `TBD / BASELINE REQUIRED`.

## 28. RESIDUAL GAPS
Data-level balance unverified · A6 six targets outstanding · Thai statutory authority not
located · Enterprise behaviour unobservable · no representative dataset ·
`account_move` CHECK constraints not enumerated.

## 29. TEAM A STATUS
```
CORRECTIVE ROUND EXECUTED
EVIDENCE PACK PREPARED
READY FOR CHATGPT RE-AUDIT
CONDITIONAL — RESIDUAL GAP DOCUMENTED
```
Not proceeding to Sonnet · not to Team B · not to another domain.
**Clean-room Pass NOT declared. Final Pass NOT declared.** Boss is sole Final Approver.
