# ADR-0006: Clean Room Learning Directive v2.0 — Policy A Adopted; Odoo/OCA Are Concept-Only Reference Material
Status: APPROVED
Approved By: Boss, 2026-07-06 ("SMEsPlus Clean Room Learning Directive v2.0", provided directly in
AIOS session, explicitly adopting "Policy A")
Supersedes: ADR-0005 (v1.0 of the directive). ADR-0005's evidence trail (the conflict table listing
ADR-0004 and the GAP-TH-01 resolution) remains valid history; this ADR resolves the "Open Question"
ADR-0005 left open.
Also Informed By: `00_PROJECT_STANDARD/TECHNOLOGY_STACK_STANDARD.md` (Boss-provided, 2026-07-06,
same day) — see §"Technology Stack Confirms the Policy" below.

## Context
ADR-0005 recorded Boss's v1.0 Clean Room directive and flagged one open question: whether "Clean
Room" prohibits only reproducing Odoo S.A.'s own core/Enterprise code (narrow reading), or also
prohibits adopting independently-licensed third-party OCA community modules as real dependencies
(broad reading) — since ADR-0004 and the GAP-TH-01 resolution had classified `l10n_th`,
`l10n_th_reports`, and the OCA `l10n_th_withholding_tax*` suite as "REUSE."

Boss has now answered this directly, in "Clean Room Learning Directive v2.0," which:
1. Reframes the entire current project phase as **Architecture Discovery Only** — no
   implementation, no source code generation, no implementation artifacts.
2. States explicitly: Odoo Community, Odoo Enterprise, OCA modules, the PostgreSQL dump,
   configuration examples, and public documentation are **reference material for learning
   concepts only** — "not the implementation target."
3. Proposes **Policy A**: Odoo Core and OCA may be studied for concepts and analysis only; copying
   or reproducing implementation is prohibited; SMEsPlus's Blueprint must be an entirely
   independent design; **if OCA is later adopted as a real dependency, that is a separate
   architecture + licensing/compliance decision, made explicitly, and is not part of the Learning
   phase's conclusions.**

## Decision
**Policy A is adopted, in full, effective immediately.**

1. The current and all prior "Learning," "Knowledge Consolidation," and "Evidence Matching" work
   on this project is retroactively reframed as **Architecture Discovery**, not implementation
   planning. No deliverable produced under this phase authorizes installing, cloning, or shipping
   any reference-system code (Odoo core, Odoo Enterprise, or OCA modules) as part of SMEsPlus.
2. **"MATCHED" / "REUSE" is retired as a phase-ending classification.** It is replaced by:
   - **Concept Match** — the business capability is already solved conceptually in the reference
     material. This tells the Architecture Team *what problem SMEsPlus's own independent design
     must solve* and *what edge cases and business rules that design must account for*. It does
     **not** mean any code, schema, or module from the reference system is adopted.
   - **Dependency Consideration (deferred)** — a separate, later, explicitly-labeled Architecture +
     Licensing decision, to be made only when SMEsPlus is ready to evaluate real third-party
     packages against its own actual technology stack (see below), never bundled into a Blueprint,
     FDS, or Gap Analysis conclusion.
3. **"GAP" / "New"** keeps its meaning: no concept match exists in reference material; SMEsPlus's
   design and requirement must be derived from first-principles business need.
4. **"Retire" / "Out of Scope"** keeps its meaning: explicitly excluded by Boss decision (e.g. the
   `efaplus` two-level PO approval extension).

## Technology Stack Confirms the Policy (Not Just a Policy Choice — a Technical Fact)
Boss additionally provided `00_PROJECT_STANDARD/TECHNOLOGY_STACK_STANDARD.md` the same day. It
defines SMEsPlus's actual target stack as:
- Frontend: Next.js 15 / React 19 / TypeScript 5
- Backend: **FastAPI / Python 3.12**, REST API, Pydantic v2
- Data: **PostgreSQL 17 with SQLAlchemy 2.x + Alembic**, Redis, MinIO
- Auth: JWT / OAuth2 / OpenID Connect
- Infra: Docker on self-hosted Debian 13, reserved future Kubernetes

This is **not the Odoo runtime** (Odoo's own Python framework, ORM, and QWeb/XML view engine) at
all. This means the "Dependency Consideration" question for the Odoo/OCA modules referenced during
Learning (`l10n_th`, `l10n_th_reports`, `l10n_th_withholding_tax*`, `purchase_request`, etc.) is not
merely a licensing question — those modules cannot run unmodified inside a FastAPI/SQLAlchemy
backend regardless of license, because they are written against a different framework and ORM
entirely. Practically, this makes the "broad reading" the operative one for anything below the API
boundary: Concept Match only, full independent re-implementation in the SMEsPlus stack, always.

## Retroactive Reclassification of Prior Work
The following are corrected under this ADR (each document gets its own targeted amendment, tracked
separately, not silently rewritten):

| Prior artifact / verdict | Old label | New label |
|---|---|---|
| ADR-0004 — `l10n_th`, `l10n_th_reports`, VAT engine, PromptPay QR | REUSE | Concept Match — informs SMEsPlus's own independent FastAPI/SQLAlchemy implementation of Thai accounting localization; no Odoo code is adopted |
| GAP-TH-01 — OCA `l10n_th_withholding_tax*` suite | REUSE (resolved) | Concept Match — the 7 OCA modules are studied to extract the Thai withholding-tax certificate business rules and PND form-type logic (see `BUSINESS_RULE_CATALOG.md` §H, to be reworded concept-first); SMEsPlus implements this independently in its own stack |
| Evidence Matching Rounds 1–3 (Purchase module) — "MATCHED, no build needed" (FR-FD-002, FR-PUR-001, FR-PUR-006, FR-INV-001, FR-ACC-001) | REUSE / no build needed | Concept Match — each of these still requires a full independent SMEsPlus build (FastAPI service + SQLAlchemy model + Next.js UI); "no build needed" is corrected to "the business logic and validation rules are already proven in reference material, reducing *design risk*, not *build effort*" |
| `CANONICAL_DATA_MODEL.md` | Presented Odoo table names (`account_move`, `sale_order`, etc.) as if they were SMEsPlus's schema | Reframed: Odoo/OCA table names are cited only as the *origin of the observed concept*; SMEsPlus's actual schema is an independent SQLAlchemy model design, to be produced in Phase 3/4 SDS work, informed by but not copied from these names |
| `l10n_th_withholding_tax*` physical storage question (raised in ADR-0004 Addendum 2) | "Where should this code live in our repo?" | Moot as originally framed — this code is not going to be installed into the SMEsPlus codebase at all under Policy A + the FastAPI stack fact above. It may still be kept as **reference material** (e.g. under a clearly-labeled `99_Reference_Material/` path, not a code dependency path) for ongoing concept lookup during independent design. |

## Consequences
- Every future Functional Design, SDS, or Business Rule Catalog entry that cites Odoo/OCA material
  must use the "Concept Match" framing: what business problem, why it exists, how SMEsPlus
  independently solves it — never "install/reuse this module."
- The Phase 2.5→4 Thai Accounting Domain FDS task (held pending since ADR-0005) may now resume,
  under Policy A framing throughout.
- `BUSINESS_RULE_CATALOG.md` §H (Thai WHT rules) will be reworded to state each rule as an
  independent SMEsPlus business requirement, citing the OCA module only as the concept's origin,
  not as the source of the rule's wording or implementation.
- `OPEN_SOURCE_TO_SMESPLUS_GAP.md`'s Reuse/Adapt/New/Retire taxonomy is retitled "Concept
  Match/Adapt-the-Concept/New/Retire" in spirit, with REUSE entries re-worded to remove any
  implication of code adoption.
- No change to ADR-0002 (Evidence-Driven Functional Specification) or ADR-0003 (As-Is Before
  To-Be) — evidence discipline is unchanged; only what the evidence is used *for* changes.

## Review Date
At Phase 3/4 SDS kickoff for Thai Accounting, to confirm the reworded Business Rule Catalog and
Canonical Data Model correctly reflect Concept Match framing throughout.
