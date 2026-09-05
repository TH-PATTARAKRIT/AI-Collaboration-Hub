# P07 — EVIDENCE MANIFEST

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE` (except file `19`, which is `LAYER 1`)
Date: `2026-09-04`

## 1. Repository Lineage

| Item | Value |
|---|---|
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Canonical branch | `SMEsPlus` (not modified) |
| Working branch | `research/account-p07-th-tax-compliance-2026-09-04-001` |
| Branch point | `88f52cd7ba6dc40b8951c4bfc4e0016af7cbb7ad` |
| Package path | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/P07_TH_TAX_TO_COMPLIANCE_EXECUTION` |
| Merge | **NONE.** Boss decides. |

## 2. Package Digests (SHA-256)

| File | Bytes | SHA-256 |
|---|---|---|
| `00_P07_FINDINGS_REGISTER.md` | 45456 | `1795b0ddb62ad0dde941df2aa55719b54723ef092eb0f3cf6cb5293c424eca6f` |
| `01_P07_THAI_TAX_REQUIREMENT_REGISTER.md` | 23438 | `949449c2340e52d7a18e194f5594c925df6d0adf1f1e5898c6ae43fb97f903e1` |
| `02_P07_VAT_EVENT_MODEL.md` | 14317 | `575750dad92dc8ff94ac12c2d61f8c8be9b1e88db92c3d6d9b7110dc6bec6307` |
| `03_P07_WHT_EVENT_MODEL.md` | 22759 | `1d4cb544a0ac9357d9ada3bdaa7b176914ab5d7345e7a9516c9a877bdb9056a8` |
| `04_P07_TAX_POINT_MATRIX.md` | 8976 | `9a5097a6ea73ee039e22d0584b5de857f3ceb468c87b9d646c4fb3c518aeb4e4` |
| `05_P07_TAX_DOCUMENT_MATRIX.md` | 12508 | `073ee91fff769d891d033fd9109bd60b58a414f59181602e8ac18a75e2490be2` |
| `06_P07_EVENT_TO_GL_MATRIX.md` | 16026 | `d51d84fe9cbe6c0d81fd70e2e0fe57c504735ecf9155e9d443b2e55a574abd7a` |
| `07_P07_TAX_REPORT_TRACEABILITY.md` | 13901 | `c1dd1d0598e93d3fca6cc6106b39b0c7582aa5d291c886ceb896ee5ec27dc593` |
| `08_P07_CORRECTION_ADJUSTMENT_MATRIX.md` | 15255 | `973323c2a6b4dec5f386c45b259c0cc129d90e41064bede73c0d18797f2b57d4` |
| `09_P07_STATUTORY_SOURCE_REGISTER.md` | 25380 | `64c76cd19fbcceb24b28c8c2abcb82ad462d4318771d80c5f11bf0e9e21a9363` |
| `10_P07_CROSS_PROCESS_OWNERSHIP.md` | 7124 | `6fceb35bc89deea1c9d0dda219be18356d5fc025d2a4bd3e9c4b9795932ea29a` |
| `11_P07_CONTRADICTION_REGISTER.md` | 16198 | `588fbfbdc3155f51a2bb4087731f5708a1e1e71c54a5fd45087578acdeb5bc32` |
| `12_P07_DEPENDENCY_REGISTER.md` | 13094 | `93fae369e4984d74ad3a3f12431bfff1eb91861f9f081b249aa7400ec5dfd16d` |
| `13_P07_SOURCE_LINK_REGISTER.md` | 19041 | `bc51790eab43ab5df3f0f64002efc3af491a5cfa35b8d3e70fb72da980aefdd4` |
| `15_P07_REVISION_LOG.md` | 74505 | `104e8df17479203e6d8a303d234b47e8a1c25f5fe1e4278e173f28ec115a7b72` |
| `16_P07_AAS03_CHALLENGE.md` | 12188 | `75b7a24c34419f3f2c2f53da00f517af3d04d042aa2b8a3a07cb7be4565bed50` |
| `17_P07_AAS_PLUS.md` | 7051 | `1558a678cbce6922a63ef416329c1b2a0c909b2a721d8ef3259660ae0c47c0e6` |
| `18_P07_PMO.md` | 9938 | `209a031addb24bc42c7be499e6a6a8bf1d9d6e3af65ff835230534b45d7a9324` |
| `19_P07_CORE_RECON_HANDOFF_PACK.md` | 13235 | `482fc987e86a758b74936ae6f18175dcb5e49485da4244bd29eb1cac95efb56c` |
| `20_P07_SCOPE_OWNERSHIP_MATRIX.md` | 16198 | `4de61445fb70925355ea783db81c35231821d89ccb0536e677aa3e46d20a619a` |
| `21_P07_PEER_EVIDENCE_INTAKE_P04.md` | 14355 | `8992c34e2f8e6c474edb6b06de055d503b8383280060d3a92813677c81cdad61` |
| `22_P07_RUNTIME_EVIDENCE.md` | 113406 | `3285f6e0d7287014b98502a441de9960f7afe99aea5598cca2ca0de0aed4202d` |

## 3. Primary Evidence Sources Cited

| Source class | Location | Use |
|---|---|---|
| Reference-ERP source, declared PATH SET | `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE/{01 ACCOUNT, 02 OTHER, addons_extra}` | every Layer-2 citation in this package |
| Comparison surfaces, excluded | the roots tabled at `13 §2.1` | `P07-N-03`, `P07-F-47`, `P07-D-01` |
| Statutory text | `www.rd.go.th/english/*`, retrieved 2026-09-04 | `09 §2`, sources `S-01`…`S-34` |
| Statutory instrument reporting | secondary, for the rate-reduction decree only | `S-35`, held at `P07-U-04` |
| Project governance | `bootstrap/AI_BOOTSTRAP_PACKAGE.md`; `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/SMEPLUS_VERY_DEEP_RESEARCH_8_CRITERIA_UNIVERSAL_EXIT_CONSTITUTION.md`; `FR_DETAIL_TENANT_MANAGEMENT.md` | `13 §1`, `18 §2`, `P07-F-50` |

**Superseded.** A database of the declared generation **was** read, table-at-a-time and read-only, after this session's incapacity claim was tested and found false. See `22_P07_RUNTIME_EVIDENCE.md` §2 and §3. No code was executed. `P07-U-02` no longer applies package-wide; it applies to every finding except those listed at `22 §5`.

## 4. Clean-Room Scrub Result

Mechanical scan of the Layer-1 file `19_P07_CORE_RECON_HANDOFF_PACK.md` for vendor tokens
— model prefixes, field names, module names, file extensions, ORM identifiers, and the
translation-key and rate literals that appear in the Layer-2 files:

    grep -nEi 'account\.[a-z_]+|res\.[a-z_]+|l10n_|odoo|\.py|ir\.[a-z]|sudo|_compute|
               __manifest__|xlsx|move_id|partner_id|tax_line_id|price_subtotal|
               payment_state|addons|jsonb|en_US|VAT 7' 19_P07_CORE_RECON_HANDOFF_PACK.md

**Result: zero matches**, re-run after every edit to that file, including after the §8
rewrite that introduced the translation-trigger material. Thai statutory terms
(ใบกำกับภาษี, ภ.พ.30, ภ.ง.ด.3 / 53 / 54) appear in Layer-2 files only and are legal terms,
not vendor tokens.

Files `00`–`18` and `20` are `LAYER 2 — AUDIT QUARANTINE` and carry `file:line` citations
by design. They must not be transcribed into any downstream reference package.

## 5. Reproduction Commands

Every quantitative claim in this package can be re-run:

    # PATH SET manifest counts (13 §2)          -> 62 / 1371 / 69
    find "<root>/<member>" -maxdepth 2 -name "__manifest__.py" | wc -l

    # return-type peer baseline (P07-F-37)      -> 118
    grep -rl 'model="account.return.type"' "<02 OTHER>" --include=*.xml \
      | sed 's|.*/02 OTHER/||; s|/.*||' | sort -u | wc -l

    # fiscal-position peer baseline (P07-F-38)  -> 94 of 126
    find "<02 OTHER>" -maxdepth 4 -name 'account.fiscal.position-*.csv' \
      | sed 's|.*/02 OTHER/||; s|/.*||' | sort -u | wc -l
    find "<02 OTHER>" -maxdepth 4 -name 'account.tax-*.csv' \
      | sed 's|.*/02 OTHER/||; s|/.*||' | sort -u | wc -l

    # PND token census (13 §5.2)                -> 99 / 77 / 9 / 12 / 2 / 1
    grep -rIoi --exclude-dir=__pycache__ --exclude='*.po' --exclude='*.pot' \
      -e pnd3 -e pnd53 -e pnd3a -e pnd1 -e 'pnd 54' -e pnd2 <PATH SET> | wc -l

    # tenant ORM model, whole volume (P07-F-50) -> 0
    grep -rlE "_name *= *['\"][a-z_.]*tenant" --include='*.py' /Volumes/iMacSys | wc -l

    # tax_period consumers (P07-N-02)
    grep -rn 'tax_period' <PATH SET> | grep -v __pycache__ | grep -v '\.po'

## 6. Deliverable Coverage Against the Session Directive

| Directive deliverable | File |
|---|---|
| `P07_THAI_TAX_REQUIREMENT_REGISTER.md` | `01` |
| `P07_VAT_EVENT_MODEL.md` | `02` |
| `P07_WHT_EVENT_MODEL.md` | `03` |
| `P07_TAX_POINT_MATRIX.md` | `04` |
| `P07_TAX_DOCUMENT_MATRIX.md` | `05` |
| `P07_EVENT_TO_GL_MATRIX.md` | `06` |
| `P07_TAX_REPORT_TRACEABILITY.md` | `07` |
| `P07_CORRECTION_ADJUSTMENT_MATRIX.md` | `08` |
| `P07_STATUTORY_SOURCE_REGISTER.md` | `09` |
| `P07_CROSS_PROCESS_OWNERSHIP.md` | `10` |
| `P07_CONTRADICTION_REGISTER.md` | `11` |
| `P07_DEPENDENCY_REGISTER.md` | `12` |
| `P07_SOURCE_LINK_REGISTER.md` | `13` |
| `P07_EVIDENCE_MANIFEST.md` | `14` (this file) |
| `P07_REVISION_LOG.md` | `15` |
| `P07_AAS03_CHALLENGE.md` | `16` |
| `P07_AAS_PLUS.md` | `17` |
| `P07_PMO.md` | `18` |
| `P07_CORE_RECON_HANDOFF_PACK.md` | `19` |
| — added by `SMEPLUS-26-09-04-ACC-REV2-CORR1` | `20_P07_SCOPE_OWNERSHIP_MATRIX.md` |
| — added after independent challenge found 39 dangling finding references | `00_P07_FINDINGS_REGISTER.md` |
| — added on intake of peer statutory evidence from P04 | `21_P07_PEER_EVIDENCE_INTAKE_P04.md` |
| — filed outside this package, for Boss ratification | `00_PROJECT_STANDARD/SMEPLUS_EVIDENCE_SUBSTITUTION_STANDARD_PROPOSED.md` |

All eighteen named deliverables are present. Three files were added: one required by the
mid-session constitution correction, one required to make the others readable, and one
recording peer statutory evidence taken in from P04 and the disposition of three questions
it routed here.
