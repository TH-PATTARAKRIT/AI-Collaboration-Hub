# COA-G01 — Thai Relevance Register

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Register Thailand-specific relevance findings and their SI-10 boundary implications | Claude (session SMEPLUS-26-08-30-COA-G01R-001) | Local `ACCOUNT` folder (source of these findings); GitHub `SMEsPlus` branch (target-side rulings) | 2026-08-30 22:27 +0700 | ChatGPT Independent Review (pending); Boss (pending) | HOLD / EVIDENCE REQUIRED | Directly informs SI-10 ("SaaS Core must not hard-code Thailand-specific source architecture") and COA-G06 scope |

All items in this register originate from the local `STATE03` architecture findings (S1–S11) and Thai localization toolchain findings (T1–T9), frozen 2026-08-23 with file:line source citations.

**CORR4 update (2026-08-31):** these findings are **no longer local-only**. Per Boss directive `COA-G01R2-CORR4` §4.3, all supporting files are now ported, hashed, and independently verified in `COA_G01_SOURCE_PORT/STATE03_LOCAL/` — see `COA_G01_LOCAL_STATE03_SOURCE_PORT_MANIFEST_R4.md`. `COA_G01_SOURCE_CONFLICT_REGISTER.md` item C-01 is `RESOLVED`. The findings below were originally reproduced by reference; S1/S3/S4/S5 have since been re-verified against the primary ported source text in `COA_G01_SI10_CLASSIFICATION_ANALYSIS_R4.md`.

## Findings with direct SI-10 implication

| ID | Finding | SI-10 implication | Status |
|---|---|---|---|
| S1 | Thai statutory reporting logic (report layout/computation) is not source-observable — it lives in proprietary Odoo Enterprise modules (`l10n_th_reports`, gated `OEEL-1`) that clean-room rules forbid reading. | SaaS Core must obtain Thai statement layout from an independent, licensable source (Revenue Department published forms or clean-room black-box observation), never by reading the gated module. Reinforces SI-10: this specific Thai capability cannot become a SaaS Core dependency on vendor-proprietary code by construction. | VERIFIED FACT (ported to GitHub, CORR4); PLANNING-BASELINE AUTHORIZED route (b), NOT YET EXECUTED (see C-03) |
| S4 | Thai statutory reference data (WHT income-type/rate/condition tables) must be modeled as **versioned data**, not hard-coded logic. | Directly supports SI-10: the localization-specific facts must live in a Thailand Localization Profile / reference-data layer, not in SaaS Core code paths. | VERIFIED FACT (ported to GitHub, CORR4) |
| T1–T9 (Thai toolchain findings: Buddhist-era dates, Thai number-to-words, PromptPay QR, XLSX statutory output, Thai party/address hierarchy) | Each is a Thailand-specific behavior observed in vendor source, evidence-cited `[E]`. | Each is a candidate item for the Thailand Localization Profile layer (not SaaS Core) once COA-G04S/G06 design that layer. This register does not decide layering — only flags candidacy. | VERIFIED FACT (ported to GitHub, CORR4); layering decision deferred |

## Findings with Tenant/Company Context implication (cross-reference to SI-01/SI-02)

| ID | Finding | Implication | Status |
|---|---|---|---|
| S3 | Thai party identity requires tax ID + tax branch + Thai company title, beyond generic party/customer fields. | Company Context master data must carry Thailand-specific identity attributes; this is Company-scoped, not Platform-scoped. | VERIFIED FACT (ported to GitHub, CORR4) |
| S5 | Two-level Tenant → Company is insufficient for Thai statutory filing; correct model is Tenant → Legal Entity (Company) → Tax Branch. | Directly shapes how SI-01/SI-02 must be implemented for Thailand — Company Context alone under-models the real filing unit. Also recorded in the AQ ruling, §4, and in `COA_G01_ACCOUNT_CONCEPT_UNIVERSE.md`. | VERIFIED FACT (ported to GitHub, CORR4) |
| S2 | WHT is recognized at payment, not at invoice — a posting-engine timing constraint. | Company-scoped posting behavior; no cross-tenant implication identified. | VERIFIED FACT (ported to GitHub, CORR4) |

## Explicit non-finding: no genuine Thai financial-statement presentation evidence exists

Despite Thai statutory tax accounts (VAT/WHT/CIT structures) being evidenced as behavior/data-model facts above, **no actual Thai P&L or Balance Sheet presentation layout or filled example was found anywhere in GitHub or the local `ACCOUNT` folder.** This is recorded as EVIDENCE_MISSING in `COA_G01_SOURCE_BASELINE_REGISTER.md` (class F) and must not be inferred or fabricated by any downstream Gate using this register. The one database dump checked locally (`iTEST02`) contained 6 journal entries and zero WHT certificates — insufficient to derive a presentation example even indirectly.

## ROUND 2 UPDATE (2026-08-31): TBRAC cross-reference and explicit Fact Status separation

`COA_G01_TBRAC_TB01_TB13_MATRIX_R2.md` (new, Round 2) formally applies the Thailand Business Reality & User Fitness Control (commit `d57cca7`, Jira `ERPPLUS-134`) to COA-G01. Cross-references from this register:

- **TB-05 (Thai Compliance Reality)** governs findings S1–S5/T1–T9 above: `HOLD / EVIDENCE REQUIRED` — statutory claims are correctly deferred to COA-G06, not asserted as regulatory-verified here.
- **TB-09 (Digital Government & e-Tax Ecosystem)** governs the tax-related workbook rows (VAT/WHT/CIT concepts, see `COA_G01_CONCEPT_FIELD_COMPLETENESS_R2.md`): `HOLD / EVIDENCE REQUIRED`.
- **TB-06 (Document Reality)** governs the Thai financial-statement presentation gap: `HOLD / EVIDENCE REQUIRED`, confirmed evidence-missing.

Per CORR1 correction, every finding in this register carries **two distinct, non-merged fields**, restated explicitly here to remove any ambiguity:

| ID | Evidence Character | Fact Status |
|---|---|---|
| S1 | Source Observation (source-code structural observation: statutory report logic lives in a gated OEEL-1 module) | VERIFIED FACT (at the source-observation layer only — not a statement of Thai statutory law itself) |
| S2 | Source Observation | VERIFIED FACT (source-system posting-timing behavior only) |
| S3 | Source Observation | VERIFIED FACT (source-system data-model requirement only) |
| S4 | Source Observation | VERIFIED FACT (source-system data-model requirement only) |
| S5 | Source Observation | VERIFIED FACT (source-system data-model requirement only) |
| T1–T9 | Source Observation | VERIFIED FACT (vendor source-code behavior observation only) |

None of the above is `Regulatory Verification` or `Real-User Validation` Evidence Character — no item in this register has been elevated beyond what a source-code/template observation actually supports, consistent with TB-05/TB-08's "no marketing claim without product evidence" and "usability must be measured, not assumed" principles.

## Boundary statement (repeated for downstream Gates)

Every finding above is a **source-system behavior observation**, evidenced against Odoo/`l10n_th`/Odoo18-workbook artifacts under clean-room rules (business facts and semantics only — no architecture, schema, ORM, or code copied). None of these findings license copying Odoo's own Thai-localization module architecture into SMEsPlus SaaS Core; SI-10 requires the opposite — that SMEsPlus implement the underlying Thai business facts through its own, non-hard-coded localization layer.
