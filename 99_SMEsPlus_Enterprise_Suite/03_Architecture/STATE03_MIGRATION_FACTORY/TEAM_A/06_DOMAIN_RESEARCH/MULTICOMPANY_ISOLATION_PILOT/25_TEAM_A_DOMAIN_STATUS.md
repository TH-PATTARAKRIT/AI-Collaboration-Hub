> Domain: MULTICOMPANY_ISOLATION_PILOT (Gx9) | Status and Stop Point

# 25 — TEAM A DOMAIN STATUS (Gx9)

| Function | Criticality | Target V | Actual V | Status |
|---|---|---|---|---|
| MCT-F01 Warehouse-company binding | **C1** | V5/floor V4 | V2 | Blocking Unknown (Black-box/Unavailable); high documentation confidence |
| MCT-F02 Inter-company transaction automation | **C1** | V5/floor V4 | V2; source-static lead received (not upgraded) | `GAP-MCT-01` — `SOURCE/DUMP FINDING — CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION` (2026-09-30), `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET` — not resolved; sync feature itself not traced to Community source |
| MCT-F03 Shared/per-company CoA | C2 | V4/floor V3 | V2 | Targeted Validation Needed |
| MCT-F04 Consolidation reporting | C2 | V4/floor V3 | V2 | Targeted Validation Needed (`GAP-MCT-03`) |
| MCT-F05 Warehouse-level access control | **C1** | V5/floor V4 | **V1** (corroborated-absence tier); source-static lead received (not upgraded) | `GAP-MCT-02` — same label, 2026-09-30 — Community-source absence confirmed, custom-module security XML not yet scanned — not resolved |

## Source-code verification round (2026-09-30, per Boss's "STATE03 Odoo Clean-Room Source & Dump Deep Study" prompt, round 2)

Boss's local Claude Code session (Source/Dump Deep Research Worker) delivered `GAP-MCT-01`/`GAP-MCT-02` source-static leads via the consolidated `STATE03_SOURCE_DUMP_EVIDENCE_DELTA_HANDOFF.md` (round 2, `R4`/`R8`). This session (STATE03 Integration/Architecture Knowledge Owner) never read the source or dump directly; it reconciled the wording into `06_BUSINESS_RULE_REGISTER.md`, `22_UNKNOWN_AND_GAPS.md`, `19_PROVENANCE_REGISTER.md`, and `AWT_BACKLOG.md` using the mandated label. **No gap in this pilot is declared closed.** The worker's own round-2 framing treats these as leads, weaker than round-1 `D`-items — carried into this register at the same conservative reading.

## Next action

(1) `GAP-MCT-01` now has a source-static lead but the underlying sync feature was not traced to Community source — still needs a dedicated follow-up (which module actually implements it) before AWT; (2) `GAP-MCT-02`'s Community-source absence is now confirmed at source tier, but custom-module security XML is unscanned — worth a targeted follow-up before AWT; (3) continue to Gx10 (Reconciliation identity/provenance) — the final scenario — per Boss's order.

## Stop point

`DOCUMENTATION STUDY COMPLETE / READY FOR PHASE A REPORT`. Ready for CHATGPT_AUDIT.
