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
| `00_P07_FINDINGS_REGISTER.md` | 26209 | `1c3dcdb40651cb6e2b059069a2a0c211b2cee61cd9ea0e84c7ced263bb742f48` |
| `01_P07_THAI_TAX_REQUIREMENT_REGISTER.md` | 23430 | `20ba6bb949bf7395785800f5438933d730167223cde374240a95076cf460f47d` |
| `02_P07_VAT_EVENT_MODEL.md` | 14309 | `de1599ad27ac936505cb5e56c7c1a6fab9457898be6b215c15bead21b5c30ae2` |
| `03_P07_WHT_EVENT_MODEL.md` | 22751 | `8dfd44ce33db36c86d961a4df0c71603e5232b9bbe33114394747ab00ffeb3ef` |
| `04_P07_TAX_POINT_MATRIX.md` | 8964 | `efac07084e0293866bc69409b08fe1c96137735b11369371c4ca15de0e3a5012` |
| `05_P07_TAX_DOCUMENT_MATRIX.md` | 12460 | `263f3db5ebb536404c04cb441485d9924a9caf8d3d9352a9a7a574466a59422b` |
| `06_P07_EVENT_TO_GL_MATRIX.md` | 15040 | `1c363f31059e9fbc5270b2318792ed2a75d88a80d91d1a1cfd6105939d7b4148` |
| `07_P07_TAX_REPORT_TRACEABILITY.md` | 13817 | `140612a49a3b319a67dc37bdb23ea1159f66e76e0bd3ce817e5614b1df7d0246` |
| `08_P07_CORRECTION_ADJUSTMENT_MATRIX.md` | 15231 | `c28b943d19677d978e6425fd1b7e14d428f378245e2e8b3f3946e3504f198d81` |
| `09_P07_STATUTORY_SOURCE_REGISTER.md` | 25320 | `06409e6589bc1a457bec27c3b983e9d5aab7fd9e1a1eee6966e21440776bf72f` |
| `10_P07_CROSS_PROCESS_OWNERSHIP.md` | 7122 | `8a378fbb7b9fc1161e6ddd7aef766f14e58c375b97fcffebaa7f19c252b6a5f4` |
| `11_P07_CONTRADICTION_REGISTER.md` | 16194 | `02e3c560ea1f1f097167e643a18c221eb9c21f98bd1ddf5fcca323a4107edc72` |
| `12_P07_DEPENDENCY_REGISTER.md` | 13060 | `4686c8e13b1c9e21274de0dad0e7bcbcdfc734694c2173d3f709dca8008c99c9` |
| `13_P07_SOURCE_LINK_REGISTER.md` | 19017 | `dc34515b339629aa53f1a0bc7609773d3834358976666c9285128687da89d1a0` |
| `15_P07_REVISION_LOG.md` | 50087 | `24d2e86fee36b2c26e0f3fdd1777badb627427a6b70c5fb51d12b6db53ea3163` |
| `16_P07_AAS03_CHALLENGE.md` | 12188 | `75b7a24c34419f3f2c2f53da00f517af3d04d042aa2b8a3a07cb7be4565bed50` |
| `17_P07_AAS_PLUS.md` | 7031 | `afdd8ec09a6c0e40f93c0c6eb15715e77da17e4d9d306f8aab37441cc92b15ae` |
| `18_P07_PMO.md` | 9934 | `ecb08a9117fa9af7e33e81faf2dab9be6dd99fb8ef4925545573dc66c03ad1a1` |
| `19_P07_CORE_RECON_HANDOFF_PACK.md` | 11318 | `e800467b0491fb4f0c0555c4c2c1f1eb0c76fe4510d584624da1392502b4d3ce` |
| `20_P07_SCOPE_OWNERSHIP_MATRIX.md` | 16198 | `4de61445fb70925355ea783db81c35231821d89ccb0536e677aa3e46d20a619a` |
| `21_P07_PEER_EVIDENCE_INTAKE_P04.md` | 14311 | `af5cc79985e4b3db176588156b6e2380e3df22e40d3f09947f5f1e3897ef7742` |
| `22_P07_RUNTIME_EVIDENCE.md` | 52149 | `2d3f16649aaed54e037e5e7e367d9f8144e9dff4fc83115170f7bd8c385b4053` |

## 3. Primary Evidence Sources Cited

| Source class | Location | Use |
|---|---|---|
| Reference-ERP source, declared PATH SET | `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE/{01 ACCOUNT, 02 OTHER, addons_extra}` | every Layer-2 citation in this package |
| Comparison surfaces, excluded | the roots tabled at `13 §2.1` | `P07-N-03`, `P07-F-47`, `P07-D-01` |
| Statutory text | `www.rd.go.th/english/*`, retrieved 2026-09-04 | `09 §2`, sources `S-01`…`S-34` |
| Statutory instrument reporting | secondary, for the rate-reduction decree only | `S-35`, held at `U-04` |
| Project governance | `bootstrap/AI_BOOTSTRAP_PACKAGE.md`; `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/SMEPLUS_VERY_DEEP_RESEARCH_8_CRITERIA_UNIVERSAL_EXIT_CONSTITUTION.md`; `FR_DETAIL_TENANT_MANAGEMENT.md` | `13 §1`, `18 §2`, `P07-F-50` |

**Superseded.** A database of the declared generation **was** read, table-at-a-time and read-only, after this session's incapacity claim was tested and found false. See `22_P07_RUNTIME_EVIDENCE.md` §2 and §3. No code was executed. `U-02` no longer applies package-wide; it applies to every finding except those listed at `22 §5`.

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
