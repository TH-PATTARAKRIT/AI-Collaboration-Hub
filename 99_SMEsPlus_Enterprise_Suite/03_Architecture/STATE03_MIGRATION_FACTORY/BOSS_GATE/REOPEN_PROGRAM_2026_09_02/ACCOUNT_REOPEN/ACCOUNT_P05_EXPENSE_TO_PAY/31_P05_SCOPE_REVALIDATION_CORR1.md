# 31 — P05 `CORR1` SCOPE REVALIDATION (CONTINUATION)

`LAYER 2 — AUDIT QUARANTINE`
`SMEPLUS-26-09-04-ACC-REV2-CORR1` — SCOPE-AWARE EVERYWHERE.

**This file does not re-run `22`.** Per the continuation directive, only findings *materially
affected* are revalidated. `22 §3 R-01`..`R-06` remain the authoritative revalidation and are
**confirmed unchanged** except where the new evidence in `24`/`25` bears on them — recorded below.

## 1. Confirmation of `22 §3`

| ID | Original disposition in `22` | Affected by the new evidence? | Confirmed |
|---|---|---|---|
| `R-01` | `hr.expense.vendor_id` missing `check_company` — **WITHDRAWN as a scope defect** (`res.partner` is TENANT-scoped; `REFERENCE SCOPE ≠ FINANCIAL SCOPE`). The separate identity-completeness defect stands. | No | **CONFIRMED** — put to Expert 4 for adversarial re-test (`36 §4`) |
| `R-02` | `petty.cash` is COMPANY-scoped **by derivation** (its balance is Σ posted GL lines on a company's account); company context required and absent. | Partly — reach is now **LATENT** (`24 §3`), which changes severity, **not scope** | **CONFIRMED** |
| `R-03` | `account.withholding.tax` is **OVER-constrained**: one record conflates PLATFORM statutory reference with COMPANY mapping (`SC-01`). | **Yes, strengthened** — see §2 | **CONFIRMED AND STRENGTHENED** |
| `R-04` | Advance approver resolved through a One2many without determining the executing scope. | Partly — reach is **LATENT** | **CONFIRMED** |
| `R-05` | `hr.expense.sheet.company_id` required + readonly — correct, not over-constrained. | No | **CONFIRMED** |
| `R-06` | Findings carrying no scope assumption, preserved verbatim. | No | **CONFIRMED** |

## 2. `R-03` / `SC-01` — Strengthened by Database Evidence

The `22` analysis was structural: one record conflates two scopes, so the statutory rate must be
duplicated per company with nothing keeping copies equal. The new evidence adds a measurement.

| Registry | `account_withholding_tax` rows | Companies in the certificate population |
|---|---|---|
| `iSMEs` v16 | **7** | 1 |
| `iEVING` v19 | **4** | — |
| `BK12MAY26` v19 | **4** | — |

| Finding | Class |
|---|---|
| The object requires `company_id` and is company-scoped in every deployment examined. | **FACT VERIFIED** |
| Where a tenant runs several companies, the rate table must be duplicated; nothing in the model links the copies. | **FACT VERIFIED** (structural) |
| The duplication mechanism is itself defective: `update_wt` searches with **no company domain**, so the global rule hides a record belonging to another company and a **second** record is created; and `l_vals` never copies the tax's `company_id`, so the new record inherits the **acting user's** company. | **FACT VERIFIED** — `07 TX-17` |
| Divergence between per-company copies would be undetectable. | **SUPPORTED INTERPRETATION** — not measurable here: the certificate population is single-company (`company_id = 1` for all 5,201), so multi-company divergence is **not exercised** in the available data. Class **C — NOT YET SEARCHED** for a multi-company deployment. |
| Whether Thai WHT rates are uniform across companies of one taxpayer | **`HOLD — STATUTORY EVIDENCE REQUIRED`** — P07's. P05 asserts only the structure. |

**Scope determination, unchanged and now better evidenced:** the statutory half (rate, form class,
tag semantics) is a **PLATFORM** candidate; the ledger mapping (account, journal) is **COMPANY**.
Routed to P11 as `H-P11-3`.

## 3. Scope of the Newly Obtained Evidence Itself

The continuation introduced a new class of object — deployment registries and database dumps — which
must itself be scope-classified rather than used unclassified.

| Object | Owns | Access | Financial effect | Data character | Required context |
|---|---|---|---|---|---|
| `ir_module_module` registry of a deployment | **TENANT** (it describes one customer's installation) | TENANT | No | TENANT-owned deployment metadata | Tenant only |
| A database dump of a customer deployment | **TENANT** | TENANT, restricted | No, by itself | TENANT-owned data at rest | Tenant only |
| `account.withholding.tax` **rate + form class** | **PLATFORM** candidate | PLATFORM | No | statutory reference | neither required |
| `account.withholding.tax` **GL mapping** | **COMPANY** | COMPANY | Yes, when applied | COMPANY legal truth | Tenant + Company |
| `withholding.tax.cert` (a certificate) | **COMPANY** | COMPANY | Yes — it evidences a withheld amount | COMPANY legal/statutory artefact | Tenant + Company |
| `purchase.advance.payment.bill` | **COMPANY** | COMPANY | **Yes** — it creates a vendor bill | COMPANY accounting truth | Tenant + Company |

> **`SC-02` NEW SCOPE FINDING.** `purchase.advance.payment.bill` creates a COMPANY-scoped financial
> effect, yet its ACL grants full CRUD to `base.group_user` and its creation runs under `sudo()`
> (`30 §1 H-P01-2`). Under `MISSING REQUIRED SCOPE = DENY`, an operation with a company-owned
> financial effect must prove company-scoped authority; here it proves none and elevates instead.
> **Live in all four distinct databases evidenced.** Routed to **P01** — P05 does not decide P01's
> authorisation model.

> **`SC-03` NEW SCOPE OBSERVATION.** Certificate evidence is single-company in the only population
> available, so **no multi-company scope behaviour in the WHT chain was exercised by any evidence in
> this session**. Class **C**. This bounds `SC-01`'s measurable half and is stated rather than
> glossed.

## 4. Open Scope Determinations

`22 §4` `SO-01`..`SO-04` are re-examined against the new evidence:

| ID | Question | Movement |
|---|---|---|
| `SO-01` | Is `hr.employee` TENANT-scoped with company-specific contracts, or one record per company? | **UNCHANGED — `HOLD — SCOPE EVIDENCE REQUIRED`.** Not resolvable from module registries; would need employee-table extraction across a multi-company deployment, and the only P05-relevant population is single-company. |
| `SO-02` | Is an expense category (product) TENANT reference or COMPANY reference? | **UNCHANGED — `HOLD`.** |
| `SO-03` | Do unrelated independent companies in the deployment share a tenant? | **PARTIALLY INFORMED.** The registries are **separate databases** with different owners (`scgl`, `efaplus`) — consistent with `CORR1`'s default that unrelated independent companies are separate tenants. But this evidences the *reference estate's* deployment topology, **not** the SMEsPlus SaaS target's. Remains `HOLD — SCOPE EVIDENCE REQUIRED`; class **C** for the target. |
| `SO-04` | Which scope owns an expense evidence document once copied onto a company's entry? | **UNCHANGED — `HOLD`.** |

## 5. Peer Impact

All four `CORR1` contributions are routed to P11 (`30 §6 H-P11-3`), now joined by `SC-02` (to P01)
and `SC-03` (a bound on `SC-01`). `PEER DEPENDENCY OPEN` for P01, P07, P11. Unaffected work continued
throughout, per `CORR1 §7`.
