# RED TEAM REGISTER — Lane B (Gemini) — as of 2026-09-26
Maintained by RED TEAM (Lane B audit). Status changes carry the Boss evidence that made them. IDs are never reused.

| ID | Sev | Item | Status | Evidence / Boss reference |
|---|---|---|---|---|
| RT-LANEB-011 | MED | 8 test records `ROOMB_TEST_OBS_PARTNER*` in ROOMB_TEST | **CLOSED** — cleanup CLEAN, 0 remain (09:46); Boss ack item 2, 26 Sep | `reports/STEP2_COLLECTOR_ATTENDED_20260926_094658.txt`, `batches/W1-STD/artifacts/s6_cleanup.json` |
| RT-LANEB-015 | HIGH | S4/S5 unreachable | **RETIRED (partial)** — act_window + config.settings reachable since 09:35; 4 surfaces remain outside grant, not needed by census | `reports/PROBE_RT_20260926_093544_after_optionA.txt` |
| RT-LANEB-016 | MED | RUN_ALL step-4 gate grepped the odoo-shell view, not the observer's live rights | **CLOSED** — live pre-flight `ops/laneb_preflight_unlink.py`; Boss ack item 2, 26 Sep | `reports/PREFLIGHT_PROBE_RT_20260926_094607.txt`, `_superseded/RUN_ALL_V1.00_pre-RT-LANEB-016_20260926.sh` |
| RT-LANEB-017 | LOW | `census_menu_tree.py` labelled the full system menu list as "visible to this account" | **CLOSED** — label + JSON note fixed; re-run reproduces tree hash `c5d68d14…` and byte-identical TSV; Boss order item 2, 26 Sep | `reports/MENUTREE_RERUN_RT_*.txt`, `_superseded/W1-SCREENS_menutree_20260926_0249/` |
| RT-SEC-003 | HIGH→design | observer in 7 shared groups; coverage side: 108/492 leaves reachable | **DECIDED — BOSSDEC-003 A–E approved 26 Sep** (two-account model; census group set; deferred sections excluded; Settings excluded from UI census; groups 90/29 deferred to MVQ) | `reports/RT-SEC-003_DECISION_PACKAGE_V1.00.md`; Boss chat item 1 |
| RT-SEC-004 | MED | admin login password lost | OPEN — not in Lane B scope; unchanged | handover |
| RT-GOV-004 | — | RED TEAM audited Lane A while being Lane A (outgoing session) | OPEN — outside this session's role (Lane B only) | handover |
| DOC-DRIFT-001 | — | FREEZE_W1-STD.json floor 95 vs BOSSDEC-002 B 103; Project Instructions V2.0 §10.2/§10.3/§25 pre-date 26 Sep decisions | OPEN — governance finding for the Governance Controller | this session |
| HYG-001 | LOW | `reports/RUN_20260926_0249.txt` (outgoing session) contains an install path | OPEN — not edited; scrubbed in the repository intake copy only | this session |
