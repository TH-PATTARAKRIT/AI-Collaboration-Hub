# G07 — FINAL L9 SAAS / MULTI-TENANT BOUNDARY REVIEW (DELTA)

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GAPCLOSE-001` · **delta only** — supersedes the affected rows of file `16`

Re-run limited to what the four closures changed. Unrelated Level 9 content in file `16` stands.

---

## 1. What changed

| Row in file `16` | Prior state | Final state |
|---|---|---|
| Currency rate — keyed to the company **root** | listed as a group-level sharing observation | **`SB-01a` VERIFIED DEFECT** — a **null**-company rate is matched for **every company in the database**, explicitly permitted by the record rule, with no database boundary (`G02`) |
| Currency rate — writer scope | not assessed | **`SB-07` NEW VERIFIED DEFECT** — the live-rate writer stores the **acting** company while the resolver reads the **root**; a branch-maintained rate is invisible to conversion (`G03`) |
| Numbering-control parameter | `SB-01`, database-wide | unchanged — confirmed |
| Identifier-arithmetic ceiling | `SB-02` | unchanged |
| Hash chain keyed on storage identity | `SB-03` | unchanged |
| Deletion evidence leaves the tenant | `SB-04` | **narrowed** — the audit-trail flag is a one-way ratchet, but it **defaults off and freezes at first posting**, so for most tenants the protection is permanently unavailable (`B-01`) |
| Approval control | "none exists" | **`E` contradicted at domain scope** — a Studio engine exists, cannot gate `write`, skipped under elevation (`G05`, `RS-02`) |

## 2. The boundary model, final

| Boundary | Enforced by | Backed by a database constraint? |
|---|---|---|
| Journal → company | field, required, single | no |
| Entry → company | via journal | no |
| Item → company | via entry | no |
| Liquidity account → company | validation refusing multi-company | no |
| Account → companies | many-to-many, by design | no |
| **Currency rate → company** | **record rule that explicitly permits null** | **no** |
| Lock dates → company | per company, hard lock cascading from parents | no |
| Fiscal year → root company only | validation | no |
| **Configuration parameters** | **nothing — no company dimension** | **no** |
| **Tenant** | **no concept exists** in the searched scope | **no** |

> **`VERIFIED FACT`:** **no company or tenant boundary in the accounting domain is enforced at the
> database level** within `addons/account`, `addons/account_accountant` and the framework's company,
> currency and configuration models. Every boundary is an application-layer or record-rule construct.

## 3. The three ways a financial fact can cross a boundary

Established by this round, at supported scope:

| # | Crossing | Direction | Evidence |
|---|---|---|---|
| `X-01` | A **null-company rate** measures any company's new postings and any company's report-time derivations | one → all | `G02` |
| `X-02` | A **branch-scoped rate** is invisible to its own company's conversion, silently substituting the root's rate, an unrelated rate, or par | own → lost | `G03` |
| `X-03` | A **configuration parameter** disables a numbering control for every tenant in the database | one → all | `COR-16` |

`X-01` and `X-03` are genuine cross-tenant crossings. `X-02` is an intra-hierarchy failure with the
same root cause: **inconsistent company scoping between writers and readers of the same fact.**

## 4. Tenant isolation requirements — final

| # | Requirement | Status |
|---|---|---|
| `TI-01` | Every control-affecting configuration value carries a tenant dimension | reaffirmed by `X-03` |
| `TI-02` | No identity encoded by arithmetic over other identities | unchanged |
| `TI-03` | Tamper-evidence keyed on business identity | unchanged |
| `TI-04` | All control evidence stored inside the tenant's data | **strengthened** — the deletion protection defaults off and freezes |
| `TI-05` | Template-derived and tenant-created configuration remain distinguishable | unchanged |
| `TI-06` | Tenant isolation is a `Tolerance = 0` candidate | **reaffirmed — and now evidenced by two verified crossings, not one** |
| `TI-07` | **NEW.** Every measurement, classification and control value carries exactly **one** owning boundary, and **every writer and every reader applies the same scoping rule** | from `X-01`, `X-02` |
| `TI-08` | **NEW.** No boundary may be enforced solely in the application layer where a database constraint can express it | from §2 |

## 5. Level 9 position

The Level 9 conclusion is **unchanged in direction and stronger in evidence**. The reference model's
outermost boundary is the company group, and in three verified places the **database** — which for a
shared-database multi-tenant SaaS is the wrong boundary.

`RECOMMENDATION:` `TI-07` is the single highest-value structural requirement produced by this round.
Both verified crossings, and the branch-rate failure, reduce to the same cause: **the same fact is
scoped differently by different code paths.**
