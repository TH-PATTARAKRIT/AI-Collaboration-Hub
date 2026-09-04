> **CORR1 CORRECTION NOTICE.** Amended by session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`.
> Corrections landing here: `COR-12, COR-16, COR-18`. Governing text where they conflict with the body below: CORR1/C03 CC-05.
> Prior findings are retained unedited for lineage; see `CORR1/C02_..._ACCEPTED_CORRECTIONS_REGISTER.md`.

# 16 — LEVEL 9: SAAS / MULTI-TENANT / MULTI-COMPANY BOUNDARY MODEL

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

## 1. The finding that governs this Level

**The reference model has no tenant concept.** Its outermost boundary is the **company group** —
a root company and its descendants. Several structures are keyed to that root rather than to the
individual company. In a deployment where multiple tenants share one database, those structures are
shared at exactly the level a SaaS must keep separate.

This is not a defect in the reference system, which was not built for that deployment. It is a
**boundary mismatch** that SMEsPlus must close deliberately.

## 2. Boundary register

| Structure | Keyed to | Tenant-safe in a shared database? | Evidence |
|---|---|---|---|
| Journal | one company | yes | `EV-006` |
| Entry | one company, via journal | yes | `EV-006` |
| Item | one company, via entry | yes | `EV-006` |
| Liquidity account | one company; **sharing refused** | yes | `EV-019` |
| Account | **many companies** | within a group, by design | `EV-001` |
| Account code | **the root company** | shared across the whole group | `EV-001` |
| Currency rate | **the root company** | shared across the whole group | `EV-018` |
| Fiscal year | **root companies only**; child companies refused | shared across the whole group | `COR-01` |
| Hard lock date | **cascades from every parent** | a parent locks its children irreversibly | `EV-008` |
| Soft lock dates | resolved up the parent chain | as above | `EV-008` |
| Lock exception | one company, optionally **every user** | user scope is not tenant-scoped | `EV-021` |
| Numbering/date control parameter | **nothing — no company dimension at all** | **no. One write affects every tenant in the database** | `COR-16` |
| Per-company code grid identifier encoding | arithmetic on identifiers, ceiling 10,000 | **no. Fails once any company identifier reaches 10,000** | `COR-18` |
| Integrity hash chain | journal + number prefix + **storage row identifiers** | cannot survive a tenant split, merge, or migration | `COR-12` |
| Deletion evidence | the **application log** | leaves the tenant's data entirely; in a shared deployment it lands in shared infrastructure | `EV-011` |

## 3. The four genuine SaaS boundary failures

| # | Failure | Mechanism | Severity |
|---|---|---|---|
| `SB-01` | **Cross-tenant control disable.** The configuration store has no company dimension, so disabling the numbering/date-alignment control disables it for **every tenant in the database**, invisibly. | `COR-16` | **highest** |
| `SB-02` | **Identifier-arithmetic ceiling.** The per-company code grid encodes `account × 10000 + company`. Once any company identifier reaches 10,000 — reached by cumulative creation, not by live count — the encoding aliases and the grid reads or writes another company's code. It fails silently rather than raising. | `EV-020`, `COR-18` | high |
| `SB-03` | **Tamper-evidence cannot cross a tenancy boundary.** The hash chain is keyed on storage row identifiers, so a tenant split, merge, restore or migration invalidates it — precisely when assurance matters most. | `COR-12` | high |
| `SB-04` | **Control evidence leaves the tenant.** Deletion evidence is written to the application log. In shared infrastructure it is neither tenant-scoped nor tenant-accessible, and it is not part of the tenant's own records. | `EV-011` | high |

## 4. Template, provisioning and customisation

| Concern | Reference position | Evidence | SMEsPlus position |
|---|---|---|---|
| Chart provisioning | a template is loaded per company at creation; a child company inherits its parent group's template | `EV-019` | `ADAPT` |
| Template versioning | a reload path exists that updates only selected fields on existing records | `EV-019` | `EXTEND` — a tenant's chart must record which template version it derives from |
| Standard vs tenant-specific accounts | **no distinction exists** — once provisioned, template accounts and tenant accounts are indistinguishable | `EV-001` | **`EXTEND` — this is a required SMEsPlus concept** |
| Tenant customisation of a standard account | unrestricted | `EV-001` | `EXTEND` — must be bounded |
| Upgrade of the standard chart | the reload path | `EV-019` | `EXTEND` |
| Rollback | **none identified** | `GAP-S01` | `UNKNOWN` |
| Company-specific accounts | supported through the many-to-many | `EV-001` | `ADAPT` |
| Localization boundary | Thai localization modules exist in the build and define a chart, taxes and statutory extracts | `COR-13` | `WAVE-D TAX` owns the content; Wave A owns the boundary |

**The most important gap in this table** is the third row. Boss question 16 asks which chart-of-accounts
concepts belong to the standard SaaS template versus tenant configuration. The reference model
**cannot answer it**, because it retains no record of which accounts came from the template. Once
provisioned, the distinction is gone. SMEsPlus must introduce it; there is nothing to adapt.

## 5. Company boundary — preserved invariants

Wave A found nothing contradicting the existing SMEsPlus SaaS invariants, and adds three
evidence-backed positions:

1. **Liquidity accounts must not be shared across companies.** The reference refuses it, and the
   reason is sound: a bank account belongs to exactly one legal entity.
2. **Bank reconciliation completeness should gate period locking.** A good pattern, worth
   generalising into the close checklist (file 12).
3. **A parent's irreversible lock cascading to subsidiaries is a policy choice, not a technical
   necessity** — and it couples entities a tenant may consider independent. Raised as decision
   `CL-05`.

## 6. Tenant isolation requirements derived from this Level

| # | Requirement | Derived from |
|---|---|---|
| `TI-01` | Every control-affecting configuration value carries a tenant dimension. No configuration may have database-wide effect. | `SB-01` |
| `TI-02` | No identity may be encoded by arithmetic over other identities. | `SB-02` |
| `TI-03` | Tamper-evidence keys on business identity, so it survives migration and tenant reshaping. | `SB-03` |
| `TI-04` | All control evidence — including evidence of destructive acts — is stored inside the tenant's own data. | `SB-04` |
| `TI-05` | Template-derived and tenant-created configuration remain distinguishable for the life of the tenant. | Boss question 16 |
| `TI-06` | Tenant isolation of ledger data and controls is a `Tolerance = 0` candidate. | constitution principle 13 |

## CHECKPOINT L9

| Item | Record |
|---|---|
| Scope completed | 15-structure boundary register; four boundary failures; provisioning and template model; six isolation requirements |
| Verified findings | No tenant concept exists; the outermost boundary is the company group; three structures are keyed to the group root; one configuration store has no company dimension at all |
| Contradictions | `CONTRA-02` (identifier ceiling), plus `SB-01`, `SB-03`, `SB-04` |
| Unknowns | Template rollback (`GAP-S01`) |
| Risks | Boss question 16 has no reference answer — the standard-versus-tenant distinction must be invented |
| Next research target | Level 10 — migration and historical continuity |

`CHECKPOINT L9 RECORDED — CONTINUING AUTOMATICALLY.` Not Boss approval.
