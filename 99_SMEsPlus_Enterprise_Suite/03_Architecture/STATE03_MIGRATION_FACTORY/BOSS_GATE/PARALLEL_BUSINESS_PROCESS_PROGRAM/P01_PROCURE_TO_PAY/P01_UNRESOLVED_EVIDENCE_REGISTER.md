# P01 — UNRESOLVED EVIDENCE REGISTER

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.**

Every unresolved item carries the **exact** classification the directive permits, and the
evidence that would settle it. Nothing here is left unclassified.

---

## 1. GATING — a conclusion cannot be drawn without these

| ID | Item | Classification | What would settle it |
|---|---|---|---|
| `U-01` | Which generation and which **copy** of each custom module each deployment runs | **BOSS DECISION REQUIRED AT FINAL GATE** for the target; **HOLD — DATABASE EVIDENCE REQUIRED** for the fact | The live `addons_path` and the module registry per deployment. Partly answered this round: installed-module names are now known for three deployments; the *copy* is not |
| `U-02` | Whether the v19 deployments **intend** to post inventory value at all | **HOLD — RUNTIME EVIDENCE REQUIRED** | A business statement, or a deployment configured to completion. Not answerable from a dump. Note the configuration is internally contradictory as it stands |
| `U-03` | Whether the tenant boundary is tested on the cross-company path | **HOLD — SCOPE EVIDENCE REQUIRED** | Record rules and access paths; assigned to an independent expert this round |
| `U-04` | Ownership of the withholding event — bill or payment | **HOLD — PEER PROCESS RECONCILIATION REQUIRED** | P07 reports the fact is created at payment and reported from the bill line. P11 must reconcile |
| `U-05` | Statutory basis for every Thai tax and withholding position, including which PND mapping is correct | **HOLD — STATUTORY EVIDENCE REQUIRED** | Authoritative sources. **P07 owns this; P01 must not decide it** |
| `U-06` | Owner of the received-not-billed obligation | **BOSS DECISION REQUIRED AT FINAL GATE** | P10 independently reached the same unassignable boundary and offers two designs |

---

## 2. RUNTIME — source and schema cannot answer these

**Nothing in this package was executed.** These are the items where that matters most.

| ID | Item | Classification |
|---|---|---|
| `U-07` | Whether a receipt in the v19 deployments truly produces no entry | **HOLD — RUNTIME EVIDENCE REQUIRED** — cause and effect are both evidenced, execution is not |
| `U-08` | Whether the period lock re-dates on every path or only some | **HOLD — RUNTIME EVIDENCE REQUIRED** |
| `U-09` | Whether resetting a posted bill to draft actually succeeds, and what survives | **HOLD — RUNTIME EVIDENCE REQUIRED** — under independent disproof challenge |
| `U-10` | Whether withholding compounding actually fires on a second partial payment | **HOLD — RUNTIME EVIDENCE REQUIRED** — under independent disproof challenge |
| `U-11` | Whether the vendor advance is netted against the final bill | **HOLD — RUNTIME EVIDENCE REQUIRED** |
| `U-12` | Whether the asset rule and the clearing-account override actually collide on one bill line | **HOLD — RUNTIME EVIDENCE REQUIRED** — `CONTRA-P01-04`, now corroborated by P04 |

**No write execution was attempted.** Where runtime validation would require writing, the
status is `HOLD — RUNTIME WRITE AUTHORIZATION REQUIRED`; P01 holds no such authority and did not
self-authorize.

---

## 3. SCOPE — unresolved under the scope-aware constitution

| ID | Item | Classification |
|---|---|---|
| `U-13` | Is a purchase agreement TENANT- or COMPANY-scoped? | **HOLD — SCOPE EVIDENCE REQUIRED** — a business decision, not a source fact |
| `U-14` | Is a vendor price list TENANT- or COMPANY-scoped? | **HOLD — SCOPE EVIDENCE REQUIRED** |
| `U-15` | Is a storage location TENANT- or COMPANY-scoped? | **HOLD — SCOPE EVIDENCE REQUIRED** — sharpened this round: in v19 the location now carries the **valuation account**, so an under-scoped location would redirect a company's postings |
| `U-16` | Is currency-rate data PLATFORM or TENANT? | **ROUTED** — Account track ruling inherited |
| `U-17` | Is a tax definition TENANT or COMPANY? | **HOLD — STATUTORY EVIDENCE REQUIRED** — routed to P07 |
| `U-18` | Is the item category TENANT or PLATFORM? | **HOLD — SCOPE EVIDENCE REQUIRED** — sharpened: in v19 it no longer carries the clearing account, so its scope weight has changed |
| `U-19` | Does the reconciliation grouping object need company scope? | **HOLD — SCOPE EVIDENCE REQUIRED** — under independent challenge |

---

## 4. POPULATION — declared, not concealed

| ID | Item | Classification |
|---|---|---|
| `U-20` | The **28** population members not installed in any of the **four** databases (corrected from 47 across three — `ERR-P01-15`) | **SOURCE ONLY — NOT INSTALLED VERIFIED** |
| `U-20b` | `D4`'s transaction data — read only for its module registry | **NOT YET SEARCHED — class C, and now known-reachable.** Highest-value remaining P01 work |
| `U-21` | Modules reaching procure-to-pay with no dependency edge to the purchase capability | **NOT YET SEARCHED — class C** by the closure; partially covered by the retained content-token population |
| `U-22` | The fourth database dump, unreadable with available tooling | **NOT YET SEARCHED — class C** |
| `U-23` | Any deployment outside the three readable ones | **NOT YET SEARCHED — class C** |
| `U-24` | Every source root outside the five declared | **NOT YET SEARCHED — class C** |
| `U-25` | The function population | **UNBOUNDED / NOT YET ENUMERABLE** — this is why the package publishes no coverage percentage |

---

## 5. PEER — open across the programme

| ID | Item | Classification |
|---|---|---|
| `U-26` | Zero-rated input-tax sign defect, routed to P01 by P02 | **PEER OWNED — INTAKE OPEN**, not re-derived |
| `U-27` | Bill-line analytic overwrite, routed to P01 by P09 | **PEER OWNED — INTAKE OPEN**, not re-derived |
| `U-28` | The service-period field P10 needs on a vendor bill line | **PEER DEPENDENCY OPEN — P01 owes P10**; no such field was found |
| `U-29` | Whether P05's WHT "Low" rating survives | **HOLD — PEER PROCESS RECONCILIATION REQUIRED** |
| `U-30` | P06's four-entry-point payment intent and its mutation of the bill's payment status | **P11 RECONCILIATION REQUIRED** |
| `U-31` | P01–P10 publication (`DEP-23`) | **P01 ACTION REQUIRED — publication blocked by environment permission** |

---

## 6. METHOD RESIDUE

| ID | Item | Classification |
|---|---|---|
| `U-32` | Whether an expert in the previous round **suppressed** a legitimate observation under the superseded scope reading | Under recheck this round; a re-read cannot see what was never written — see the `DEP-P01-06` disposition |

---

## 7. COUNT

**32 unresolved items.** Six gating, six runtime, seven scope, six population, six peer, one
method. **None is unclassified, and none is presented as closed.**
