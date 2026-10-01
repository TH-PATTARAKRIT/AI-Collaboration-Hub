# Scope rule — Accounting localization = Thailand only

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Standing instruction from the programme owner (received 2026-10-02). Classification only; **no denominator is frozen and no coverage figure is declared** (those remain Boss/PMO authority). The Applicable SMEsPlus denominator is not defined by this file.

## Rule applied
1. Research generic Odoo Community accounting mechanisms and Thailand-applicable localization at L0–L3.
2. All non-Thai country localization modules are **FOREIGN LOCALIZATION / OUT OF SMEsPlus BUSINESS SCOPE**: only manifest, dependencies, installation status and any technical override that materially affects the generic core or Thai scope are inspected; no country-specific accounting-rule research.
3. Foreign localization modules are not counted in any Applicable denominator.
4. Evidence already collected is **preserved** and re-labelled (nothing deleted).

## Mechanical classification of the 692-module source population
(`SCOPE_CLASSIFICATION_THAILAND_ONLY_692.tsv`; rule = module-name prefix, from manifests)
| Class | Count | Note |
|---|---|---|
| THAILAND LOCALIZATION | 1 | `l10n_th` (installed in the dump; register CURRENT) |
| GENERIC | 461 | includes all non-localization modules |
| GENERIC (localization-prefixed mechanism, not country-specific) | 3 | `l10n_account_withholding_tax`, `l10n_account_withholding_tax_pos`, `l10n_account_edi_ubl_cii_tests` — kept in scope as generic mechanisms (withholding tax is relevant to Thailand; see U23/U24) |
| FOREIGN LOCALIZATION / OUT OF SMEsPlus BUSINESS SCOPE | 227 | all `l10n_*` of other countries/regions (incl. regional families). **All 227 are register EVIDENCE-ONLY; none is CURRENT or NEXT; none is installed in the dump.** 119 of them extend core accounting models (recorded as a fact for risk awareness only; no rules studied) |

Effect on the current register: the CURRENT-phase 300 already contain no foreign localization module, so no current-phase module changes status.

## Preserved evidence re-labelled
- Claims whose pointer lies in a foreign localization module (5): `FOREIGN_LOCALIZATION_EVIDENCE_QUARANTINE.tsv` — label **FOREIGN LOCALIZATION / OUT OF SMEsPlus BUSINESS SCOPE**. They are not removed and must not be used as Thai-scope evidence.
- Unit texts that merely *mention* foreign `l10n_*` module names (discovered-supporting-module lists, grep-only observations): `FOREIGN_LOCALIZATION_MODULE_MENTIONS_BY_UNIT.tsv` — same label; these mentions carry no accounting-rule research.

## Scope questions raised (not decided here)
Non-`l10n_` modules that are region- or country-specific by nature — e.g. e-invoicing network/format modules (Peppol family, SEPA QR), country-specific payment gateways and POS payment terminals, print-on-demand integrations, a regional delivery-point module — were **not** reclassified because the instruction names *accounting localization*. Their Thailand relevance is stated in the unit files where studied (for payment gateways see U20's Thailand table). Recommendation for Boss/PMO: decide whether the rule extends to them. Pending that decision they remain GENERIC in the classification file.

## Thailand-applicable deepening
Unit **U24 `thailand_localization`** (running) covers `l10n_th` end to end, Thai VAT/withholding/document/partner-identity aspects, PromptPay/EMV QR, the Thai-relevant parts of `base_vat`, `base_address_extended`, `account_debit_note`, `l10n_account_withholding_tax`, and a Thai-gaps list (statutory outputs not present in Community), plus a mechanical foreign-localization boundary table. Prior Thai evidence: U13 (CAP-U13-08), U23 (CAP-U23-01/03).

---
## Correction 2 (2026-10-02, append-only) — global transaction capabilities and language rule

**Scope correction from the programme owner (supersedes any reading of the rule above that could exclude these):**
| Capability | Scope |
|---|---|
| Multi-currency | **APPLICABLE / IN SCOPE** |
| Foreign customer / vendor | **APPLICABLE / IN SCOPE** |
| International transaction | **APPLICABLE / IN SCOPE** |
| Thailand accounting localization | **IN SCOPE** |
| Non-Thai accounting localization | **OUT OF BUSINESS SCOPE** |

These global transaction capabilities must not be confused with foreign-country accounting localization. Consequences recorded here: (a) the out-of-scope label applies only to the 227 non-Thai `l10n_*` modules and evidence pointing into them; it never applies to currency, rate, exchange-difference, foreign-partner, fiscal-position-by-country, incoterm or cross-border features; (b) existing evidence on those capabilities (U01 CAP-U01-06, U12 exchange differences/multi-currency reconciliation, U13 CAP-U13-04, U23 `base_vat`/VIES foreign-VAT validation, U20 THB gateway table, and chain hand-offs in C01/C02) is **in scope** and not quarantined; (c) the dedicated cross-module unit **U25 `multicurrency_international`** was started to study them end to end; (d) the Thailand worker U24 was told of the clarification.

**Language rule (design constraint, recorded not researched as a requirement):** canonical and default system language = English (en_US); Thai (th_TH) = translation layer with stable translation keys; no hard-coded Thai UI text in source. Unit **U26 `language_translation_layer`** studies how Odoo 19 Community handles language/translation (whether stable keys exist or the English source text is the key, translatable master-data fields, translation files, locale formats, a mechanical count of hard-coded non-English literals) so the target design can be compared with this constraint. Any Thai-language label found in Community evidence (e.g. a fixed invoice title in the Thai localization) is to be treated as a translatable-text observation, never as a requirement.

---
## Correction 3 (2026-10-02, append-only) — APPROVED SCOPE DELTA: global transaction & localization architecture

`BOSS SCOPE DELTA = APPROVED` · `FORMAL COVERAGE = N/A UNTIL CANONICAL DENOMINATOR VALIDATION`. This correction **supersedes the label** "FOREIGN LOCALIZATION / OUT OF SMEsPlus BUSINESS SCOPE" used above and in `SCOPE_CLASSIFICATION_THAILAND_ONLY_692.tsv`, `FOREIGN_LOCALIZATION_EVIDENCE_QUARANTINE.tsv`, `FOREIGN_LOCALIZATION_MODULE_MENTIONS_BY_UNIT.tsv` (files preserved unchanged; v2 file added).

1. **In scope (global transaction capabilities):** multi-currency; foreign customer/vendor; international transaction; English canonical/default language (en_US); Thai translation layer (th_TH).
2. **Current deep study (full L0–L3):** country-neutral accounting core; Thailand accounting localization; Thai VAT, withholding tax, statutory documents and applicable reporting; foreign-owned Thai companies; Thai subsidiaries of foreign groups; foreign-company branches, representative offices and regional offices operating in Thailand. → units U24 (Thailand), U25 (multi-currency/international), U26 (language), **U27 (localization framework architecture)**, **U28 (Thai entity structures)**; prior U01/U11/U12/U13/U23 remain valid inputs.
3. **Localization architecture (in scope, to research and define as neutral CANDIDATE):** Country-Neutral Accounting Core → Localization Framework → Optional Country Packs; each Company may use the accounting jurisdiction applicable to its own legal/accounting entity (U27).
4. **Non-Thai country packs = FUTURE OPTIONAL COUNTRY PACK:** inspect manifest, dependency, extension boundary, configuration pattern and integration contract only; no country-specific tax/accounting research or adoption; **country-specific functions are excluded from the current Applicable Business Denominator**. Mechanical result (`SCOPE_CLASSIFICATION_V2_COUNTRY_PACKS_692.tsv`, `COUNTRY_PACK_BOUNDARY_PROFILE_227.tsv`; heuristic archetype/template columns, verification in U27): 227 packs — 186 auto-install from their dependencies, 119 extend core accounting models, 30 declare install hooks, 14 declare uninstall hooks; all register EVIDENCE-ONLY, none installed in the dump.
5. **Language architecture:** canonical technical/business terminology = English; default UI = en_US; Thai UI = translation layer (th_TH); no hard-coded Thai menu/field/help/validation text; **Thai statutory documents may use legally required Thai presentation independently of UI language** (U26 extended to establish how document language is chosen vs UI language).
6. **Clean-Room:** only neutral concepts are extracted — localization boundary, configuration contract, posting/tax/report integration points, country-pack lifecycle, company-to-jurisdiction assignment. No cloning of vendor models/schema/methods/ORM/structure.
7. **Automatic feedback loop** (DeepSeek → Claude verification → correction request → DeepSeek delta research → Claude re-verification) continues; routine cycles need no Boss approval (see `../05_CORRECTION_LOOP/00_PROTOCOL.md`).

Statutory limit disclosed: this programme researches what Community **source** and the restored **dump** provide. Thai legal/regulatory requirements (VAT return content, withholding certificates, e-tax invoice rules, branch rules) are **not** asserted; any such requirement is `UNKNOWN — STATUTORY SOURCE REQUIRED` until an authoritative statutory source is supplied by Boss/PMO.
