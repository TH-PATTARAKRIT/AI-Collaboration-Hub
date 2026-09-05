# P01 — THE SERIES-18 DEPLOYMENT

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Layer: **1.**

> **This document exists because the governing finding of this round was false.**
> A series-18 deployment **does** exist in this estate, it holds real accounting history, and the
> clearing bridge P01 traced for four rounds **is configured in it**.

---

## 1. WHAT WAS FOUND

| Property | Value |
|---|---|
| Application series | **18.0** — `361 of 361` installed modules at `18.0.x`; core modules at `18.0.1.x` |
| Database engine | PostgreSQL 17.9 |
| Companies | **4** |
| **Journal entries** | **15,522** |
| **Stock valuation layers** | **47,801**, every one carrying a value |
| Custom purchase-request module | **installed**, at a series-18 version |
| **Goods-received clearing account** | **CONFIGURED** — on **15 of 126** item categories, plus a company-level default; the account exists in the chart under a name meaning *uninvoiced receipts* |
| Inventory valuation account | **CONFIGURED** — same 15 categories, plus a company-level default |
| **Valuation journal** | **CONFIGURED — one per company, all four** |

Alongside it, a second series-18 database with seven snapshots exists in a simulation directory.

---

## 2. WHAT THIS FALSIFIES

| Published claim | Status |
|---|---|
| *"There is no readable deployed series-18 database in this estate"* | **FALSE** |
| *"The generation P01 analysed in source has no deployed representative"* | **FALSE** |
| *"P01's source analysis and deployment evidence do not overlap on any series"* — the governing statement of `P01_VERSION_SENSITIVE_FINDING_REGISTER.md` §4 | **FALSE** |
| *"The clearing-bridge account is series-18 source with no deployed representative anywhere"* | **FALSE — it is configured, in a database with 15,522 journal entries** |
| *"The deployed databases lack the clearing account and the valuation-layer table"* | **True of the three series-19 databases. False of the estate** |

Logged as `ERR-P01-23`.

---

## 3. WHY THE VALUATION LAYERS CARRY NO JOURNAL LINK — AND WHY THAT IS *NOT* THE v19 FINDING

**0 of 47,801** valuation layers are linked to a journal entry. That is the same *shape* as the
series-19 result and it has a **completely different cause**:

| | Series-19 estate | **This series-18 deployment** |
|---|---|---|
| Valuation account | configured | **configured** |
| Valuation **journal** | **unset on 44 of 44 companies** | **configured, one per company, all four** |
| Company-level valuation **policy** | perpetual on 27–28 of 37 categories | **`manual_periodic`** |
| Why no receipt-time entries | **the journal is missing — a configuration gap** | **periodic valuation is the configured policy — working as designed** |

> **Under periodic valuation a receipt creates a valuation layer and posts no journal entry.**
> That is documented behaviour, established in P01 round 1 (`EV-P01-05`), and it is exactly what
> 47,801 unlinked layers look like.

**So the two zeros mean opposite things.** One is a misconfiguration; the other is a policy
choice operating correctly. Reading them as the same finding would have been a serious error, and
it is the reason this section exists.

---

## 4. WHAT THIS DOES *NOT* CHANGE

| Finding | Status |
|---|---|
| The series-19 journal gap (`ERR-P01-19`) | **UNCHANGED** — a different database, a different cause |
| v19 recognises inventory at invoicing by design | **UNCHANGED** — a source finding |
| Period lock re-dates, including the hard lock | **UNCHANGED** |
| Correction destroys business-semantic lineage | **UNCHANGED** |
| Withholding repeats the full base | **UNCHANGED** |
| Company ownership `INFERRED ONLY` | **UNCHANGED** |
| Every accounting finding | **UNCHANGED** — each is bound to the database it was measured in |

**No accounting finding is withdrawn.** What changes is the *evidence position*: P01 now has a
deployed series-18 system against which its central source analysis **can** be tested. It has not
been tested yet.

---

## 5. WHY IT WAS MISSED — AND IT SHOULD NOT HAVE BEEN

| Cause | Detail |
|---|---|
| **Population scoped by directory** | P01 enumerated one download directory. The pattern was never run across the home directory. Running it returns **19 archives and at least nine distinct database names**, not four |
| **It was already named in project memory** | The project's own standing notes record runtime evidence captured against *"Odoo 18 UAT db `idemo18_uat`"*. **The database was named in this session's own context from the first turn, and P01 never searched for its backup** |

The second is the more serious. This was not a hidden artefact; it was a **known** one.

---

## 6. WHAT MUST NOW BE DONE — AND HAS NOT BEEN

| # | Action | Status |
|---|---|---|
| 1 | Re-test P01's series-18 source findings against this deployment — the clearing bridge, the price-difference engine, the three-way match, the bill-line account override | **NOT DONE** |
| 2 | Establish which categories are perpetual and whether *those* receipts posted entries | **NOT DONE** |
| 3 | Read the second series-18 database and its seven snapshots | **NOT DONE** |
| 4 | Re-run the full artefact census across the home directory, keyed on database identity | **partially done** |

**This is now the highest-value remaining work in P01**, displacing the runtime-access
recommendation of the previous rounds — because a deployed series-18 database with 15,522 journal
entries can answer, from data already on this host, questions that previously required live access.
