# ADR-0005: Clean Room Engineering Directive for Odoo Source Code and Database Study
Status: SUPERSEDED by ADR-0006 (2026-07-06)
Approved By: Boss, 2026-07-06 (directive document provided directly in AIOS session:
"SMEsPlus Clean Room Engineering Directive v1.0")
Supersedes: The REUSE methodology used in ADR-0004 and in the GAP-TH-01 resolution — see
"Conflict With Prior Work" below. Does NOT supersede ADR-0002 (Evidence-Driven Functional
Specification) or ADR-0003 (As-Is Before To-Be) — this ADR changes what evidence may be used
FOR (concept extraction only, not implementation reuse), not the evidence discipline itself.

## Context
SMEsPlus is being learned from and evidence-matched against a real Odoo-based ERP codebase and
live database dump (per prior Learning phase, Repository Audit, and Phase 2.5 Knowledge
Consolidation work). Boss has now issued a formal Clean Room Engineering Directive establishing
that SMEsPlus is an **independent SaaS ERP platform**, and that studying Odoo is for
**knowledge acquisition only**, never for software reproduction.

## Decision
The full text of "SMEsPlus Clean Room Engineering Directive v1.0" (provided 2026-07-06) is
adopted as binding policy for all AI assistants, engineers, architects, analysts, reviewers, and
contributors on the SMEsPlus project, effective immediately. Summary of the binding rule:

**Allowed:** learning business concepts, processes, schemas, module boundaries, architectural
patterns, validation concepts, security/permission models — and producing documentation, FDS,
business rules, SaaS architecture, Fit/Gap analysis, mapping documents, and design
recommendations from that learning.

**Prohibited:** copying source code, cloning modules, translating source code, reproducing
algorithms line-by-line, reusing implementation details directly, regenerating equivalent source
from existing code, copying XML views/templates/SQL/business logic/database structures as
implementation artifacts, and treating the Odoo implementation as the SMEsPlus implementation.

**Mandatory workflow:** Reference System → Observation → Generic Business Concept → Independent
SMEsPlus Design → SMEsPlus Functional Specification → SMEsPlus Architecture → New Independent
Implementation. No step may be skipped.

## Conflict With Prior Work — Disclosed, Not Silently Resolved

Per this project's own Evidence Rule ("No Evidence = No Progress") and the practice established
across this engagement of surfacing contradictions rather than quietly absorbing them, the
following prior decisions and deliverables were built on a **REUSE-what-already-works**
methodology that this directive now supersedes, and require Boss's explicit disposition before
Phase 3/4 work continues:

| Prior artifact | What it did | Conflict with this directive |
|---|---|---|
| ADR-0004 (Accounting Thailand Localization Scope) | Classified `l10n_th`, `l10n_th_reports` as REUSE — i.e., install and run Odoo's own Thailand localization modules as-is | Directive prohibits "treating the Odoo implementation as the SMEsPlus implementation" — running Odoo's own `l10n_th` module unmodified as SMEsPlus's accounting localization is exactly that |
| GAP-TH-01 resolution | Reclassified the OCA `l10n_th_withholding_tax*` suite (7 modules, real Python source, AGPL-3) from "unsourced gap" to REUSE — i.e., install this third-party module suite as-is | Directive prohibits "copying source code," "cloning modules," "reusing implementation details directly" — this is a direct instance of exactly that, regardless of the module being third-party OCA rather than Odoo-core |
| `BUSINESS_RULE_CATALOG.md` §H (Thai WHT rules, BR-WHT-001–007) | Extracted rules by reading actual OCA method names, constraint logic, and field definitions | Borderline: the directive explicitly permits "study validation concepts" and "produce business rule catalogs," but these specific entries cite exact source file paths and method names rather than only the underlying business concept — needs rewriting to describe the concept independently of the source artifact |
| `CANONICAL_DATA_MODEL.md` | Used Odoo's actual table/model names (`account_move`, `sale_order`, `res_partner`, `stock_move`, etc.) as the proposed SMEsPlus canonical entities | Directive requires an "Independent SMEsPlus Design" step between observation and specification — adopting Odoo's own schema names as SMEsPlus's canonical model skips that step |
| `OPEN_SOURCE_TO_SMESPLUS_GAP.md` | Entire Reuse/Adapt/New/Retire taxonomy assumes MATCHED = "reuse it, no build needed" | The MATCHED classification needs a new definition under Clean Room: MATCHED should mean "the business capability already exists conceptually in the reference system, informing what SMEsPlus's own independent design must cover" — not "install the same code" |
| Evidence Matching Rounds 1–3 / `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` | Same MATCHED-means-reuse assumption, e.g. FR-ACC-001 "fully working, no build needed" | Same as above — "no build needed" is precisely the outcome this directive prohibits for anything derived from Odoo's own implementation |

This ADR does **not** unilaterally rewrite the artifacts above. They are flagged here as the
evidence trail of the conflict; disposition (rework, partial rework, or a scoped exception) is
Boss's decision per §"Open Question," below.

## Open Question Requiring Boss Decision Before Rework Begins

The directive's text focuses on **"the Odoo implementation"** and states "SMEsPlus does not
attempt to reproduce **Odoo**." It does not explicitly address independently-licensed third-party
community (OCA) add-on modules, which are a distinct category in the Odoo ecosystem: OCA modules
are themselves separate, standalone software published specifically for installation on any
Odoo-compatible system, under their own license (AGPL-3), by parties other than Odoo S.A. Two
readings are possible, and they lead to very different amounts of rework:

- **Narrow reading:** Clean Room prohibits reproducing/cloning Odoo S.A.'s own core and Enterprise
  code, and prohibits treating the *combined Odoo platform* as SMEsPlus's implementation — but
  installing a standalone, independently-licensed OCA module (like `l10n_th_withholding_tax`) as
  a genuine third-party dependency is normal software supply-chain practice, not "reproducing
  Odoo," similar to using any other open-source library. Under this reading, ADR-0004 and the
  GAP-TH-01 resolution mostly stand, with the Business Rule Catalog and Canonical Data Model
  needing correction.
- **Broad reading:** Clean Room prohibits reusing *any* code that originated from studying the
  reference system, including OCA modules discovered via that study — meaning SMEsPlus must
  independently re-design and re-implement Thai withholding-tax certificate handling from the
  business concept alone, without installing the OCA modules at all. Under this reading, ADR-0004
  and the GAP-TH-01 resolution are substantially reversed.

**This ADR does not resolve which reading applies — that is Boss's call.** Recommended next step:
Boss confirms narrow or broad reading (or a third, explicitly scoped position), then the
Architecture Team produces a `CLEAN_ROOM_COMPLIANCE_GAP_REGISTER.md` applying that reading to
every artifact in the table above.

## Consequences
- All future Functional Design work (including the pending Phase 2.5→4 Thai Accounting Domain FDS
  task) is held pending the Open Question above, so it is not built on a premise that gets
  reversed later.
- `Archive.zip`'s physical storage location (raised as an open registry question in ADR-0004
  Addendum 2) is now entangled with this decision: if the broad reading applies, those modules
  should not be installed into the SMEsPlus codebase at all, which changes the "where does the
  code live" question into "does this code get used at all."
- Business Rule Catalog and Canonical Data Model will need a rewrite pass that re-expresses every
  Odoo/OCA-sourced entry as an independently-stated business concept, with the reference material
  cited only as "concept origin," never as "implementation to install."

## Review Date
Immediately upon Boss's answer to the Open Question above; no independent implementation work
proceeds until then.
