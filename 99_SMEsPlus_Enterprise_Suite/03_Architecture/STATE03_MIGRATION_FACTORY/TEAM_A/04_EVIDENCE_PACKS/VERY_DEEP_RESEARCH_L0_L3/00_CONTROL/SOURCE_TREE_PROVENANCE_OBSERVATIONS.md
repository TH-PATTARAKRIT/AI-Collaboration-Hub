# Source-tree provenance observations

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** The source tree is read-only for this programme; nothing below was changed by this work.

| ID | Observation | Evidence | Handling |
|---|---|---|---|
| SP-01 | `odoo-19.0.post20260921/odoo/addons/` contains a **non-source file**, `STATE03_SMD_SOURCE_VERIFICATION_FINDINGS.md` (≈14 KB, modified 2026-09-30 01:25, Thai-language text), authored by an earlier STATE03 session. It is not a Community module and not Odoo code; its own text claims no files were modified. | file listing in the source tree; first lines read for provenance only | Excluded from every count (module universe: 692 = directories with a manifest; the earlier module-universe check already listed it as a non-module entry) and from all hard-coded-text counts (U26). **Not relied on as evidence.** Not moved or deleted (read-only rule). Recommend the owner relocate it outside the source tree and record the earlier modification in provenance. |
| SP-02 | Source tree is not a git checkout; revision identified by package metadata `19.0.post20260921` only; no commit hash exists. | B00 | unchanged |
| SP-03 | Register workbook hash mismatch (`790bcd2a…` vs `76aa648b…`) unresolved. | B00 | unchanged; PMO/Boss |
