# COA-G01 — SaaS Context Boundary Register

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Apply the Boss SaaS Context Clarification to every significant COA-G01 concept | Claude (session SMEPLUS-26-08-30-COA-G01R-001) | `BOSS_GATE/..._AQ_...md`; this register | 2026-08-30 22:27 +0700 | ChatGPT Independent Review (pending); Boss (pending) | PASS / VERIFIED (classification complete at G01 scope) | Resolves SI-01/SI-03 operational ambiguity for source-baseline classification purposes |

Per the AQ ruling: Platform Template administration = Platform Context; tenant-owned/tenant-access operation = Tenant Context mandatory; company-scoped operation = Tenant + Company Context mandatory; a Platform operation must not impersonate a Tenant operation; a Tenant/Company operation must not access or mutate Platform-owned Published Standard Template data.

## Boundary classification

| Concept / Operation | Context | Rationale |
|---|---|---|
| Publishing or versioning the Standard Thai COA Template | Platform Context | Template administration is explicitly Platform Context per AQ §3.1; no Tenant/Company should be able to author or overwrite it. |
| Provisioning a new Company's COA Instance from the Template | Tenant Context + Company Context (consuming, not mutating, the Template) | This is a tenant-owned/company-scoped operation (AQ §3.2/§3.3) that *reads* the Platform-owned Template; it must not be able to mutate it (AQ §3.5). |
| A Company customizing its own COA Instance (e.g. maintaining Account Groups) | Tenant Context + Company Context | Company-scoped per AQ §3.3; the customization must not redefine Account Type or canonical meaning (session prompt §7; SI-09). |
| Upgrading the Template to a new version | Platform Context, with a Tenant-visible preview/apply step | Template change itself is Platform Context (AQ §3.1); but SI-07 requires the resulting Tenant delta to be explicit, previewable, and auditable to the Tenant — i.e., the *apply* step is a Tenant-Context-visible event even though the *authoring* step is Platform-only. |
| Cross-tenant reporting or support tooling that reads Company data | Platform Context tool acting on Tenant/Company data | Must not "impersonate a Tenant operation" (AQ §4) — any Platform-level access to Tenant/Company data must be auditable and distinguishable from a genuine Tenant-context operation (SI-08 boundary). |
| Financial Statement Mapping (canonical, independent of Company Account Group) | Platform Context definition, Company Context application | The mapping rule itself is Platform-defined (session prompt §7: "independent from Company Account Group"); a Company applies it to its own instance but cannot redefine it, consistent with SI-09. |
| Off-Balance Sheet account handling | Company Context (posting), Platform Context (default exclusion rule) | The exclusion-from-totals *rule* is Platform-level canonical behavior; whether a given account is used is Company-scoped. |

## Explicit non-claims

This register classifies concepts against the AQ boundary; it does **not** claim that any runtime system currently enforces these boundaries — no code exists yet (Development Authorization = NOT GRANTED). Enforcement proof is COA-G04S/COA-G07 scope, not COA-G01.
