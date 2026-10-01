# Correction packet SCOPE-R1 — country-pack boundary profile (controller's mechanical file)

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Request CR-018 · CORRECTION_REQUIRED · Normal (denominator-adjacent, so reviewer attention requested) · raised by unit U27's recount (content `c0…` see packet HP_U27) · original: `00_CONTROL/COUNTRY_PACK_BOUNDARY_PROFILE_227.tsv`, `SCOPE_CLASSIFICATION_V2_COUNTRY_PACKS_692.tsv`, scope-rule Correction 3 and its PR notification (commit `6ecd29c6`). Originals unchanged.

| Superseded statement / column | Status | Corrected value (source) | Basis |
|---|---|---|---|
| Profile column `archetype` (116 base / 39 other / 34 edi / 17 pos / 16 bridge / 5 payroll-hr) | SUPERSEDED | U27 recount: 125 chart packs, 34 e-document, 24 POS bridge, 24 stock/sale/purchase/website bridge, 4 time-off/expense layout, 16 other; `l10n_hr` and `l10n_hr_kuna` are Croatian chart packs mis-classified by name prefix; no payroll pack exists | U27 T1; controller reproduced the misclassification (name-prefix `hr`) |
| Profile column `template_data_files` (non-zero for 10 packs) | SUPERSEDED — measured a manifest data-list pattern, not template presence | 126 packs have a `data/template` directory (controller count) / 125 per U27 | directory listing |
| Profile column `core_accounting_models_extended` and Correction-3 text "119 extend core accounting models" | SUPERSEDED — not reproducible | U27: 176 packs extend a core model of the set including the chart loader, 104 excluding it; 86 distinct core models extended overall | U27 T3 |
| Counts "186 auto-install · 30 install hooks · 14 uninstall hooks" | CONFIRMED | U27 recount: 0 disagreements over 227 packs for dependencies, auto-install, hook flags and data-file counts | U27 T1 |
| Scope classification v2 class assignment (227 FUTURE OPTIONAL COUNTRY PACK / 1 Thai / 3 generic l10n-prefixed / 461 generic) | UNCHANGED | name-prefix rule applied to manifests; unaffected by the corrections above | — |

Authoritative pack-boundary tables: `01_RESTRICTED_TECHNICAL_EVIDENCE/U27_localization_framework.md` (T1–T4).
