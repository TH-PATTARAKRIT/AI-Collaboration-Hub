# Corrected A1 QID Research — web / W1-B01

You are a fresh ROOM A source-facing A1 worker. Do not read or reuse either pre-model S1/S2 package.

Before any source read, run exactly:
`/Users/admin/.claude/bin/smeplus_qid_web_safe_tool preflight`

Controlled config: `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/01_ACTIVE/ROOM_A_COMMUNITY19_QID_EXECUTOR_20260922_REV001/config/modules/web.json`
Output directory: `/Volumes/iMacSys/SMEsPlus_COMMUNITY19_CLEAN_EXECUTION_20260922/QID_PIPELINE/W1-B01/web/A1_ATT001`

Read the frozen Standard 55 bank and the frozen module-specific bank from the config. Study only the V1.00-admitted LGPL-3 module source in the config. Produce exactly 105 unique `MODULE=web + QID` rows using the contract in `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/01_ACTIVE/ROOM_A_COMMUNITY19_PREMODEL_OPTION_B_REBASE_20260922_REV001/06_NEW_A1_MODULE_QID_OUTPUT_CONTRACT.md`.

Mandatory files: `00_README.md`, `01_ANSWER_REGISTER.tsv`, `02_EVIDENCE_INDEX.tsv`, `03_GAP_REGISTER.tsv`, `04_CRQ_REGISTER.tsv`, `05_FUNCTION_CANDIDATE_REGISTER.tsv`, `06_RULE_REGISTER.tsv`, `07_SCENARIO_REGISTER.tsv`, `08_SELF_CHECK.json`, `TERMINAL_RESULT.json`, `MANIFEST_SHA256.txt`.

Use new evidence IDs prefixed `QID-A1-WEB-`. Restricted evidence index may contain exact source pointers, but `ANSWER_TEXT` and other clean answer fields must remain source-neutral and must not copy code, identifiers, paths, XML IDs or algorithms. Keep five proof layers separate. Every non-ANSWERED row needs a real reason and what was checked. Do not claim Formal Coverage, ROOM B release, or Final Approval.

Write only in the output directory. At the end run exactly:
`/Users/admin/.claude/bin/smeplus_qid_web_safe_tool finalize`

Set `TERMINAL_RESULT.json` to `A1-QID-SEALED` only when finalization returns PASS; otherwise set `A1-QID-PARTIAL` with exact unresolved items. Return to the Controller only.
