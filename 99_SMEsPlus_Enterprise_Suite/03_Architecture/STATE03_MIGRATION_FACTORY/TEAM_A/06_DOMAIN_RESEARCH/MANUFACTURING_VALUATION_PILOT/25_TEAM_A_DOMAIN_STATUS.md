> Domain: MANUFACTURING_VALUATION_PILOT (Gx7) | Status and Stop Point

# 25 — TEAM A DOMAIN STATUS (Gx7)

| Function | Criticality | Target V | Actual V | Status |
|---|---|---|---|---|
| MFG-F01 Raw material consumption → WIP | **C1** | V5/floor V4 | V2 | Blocking Unknown (Black-box/Unavailable); confirms Gx6 model |
| MFG-F02 Finished goods completion | **C1** | V5/floor V4 | V2 | Blocking Unknown; confirms Gx6 model |
| MFG-F03 Manual interim WIP posting | C2 | V4/floor V3 | V2 | Targeted Validation Needed (`GAP-MFG-05`) |
| MFG-F04 MO cost computation | C2 | V4/floor V3 | V2 | Targeted Validation Needed (`GAP-MFG-04`) |
| MFG-F05 Negative-inventory revaluation | **C1 (provisional)** | V5/floor V4 | **V1** (was V0) | Targeted Validation Needed — thread opened, version tension vs. Odoo 19 disclosed, not yet documentation-tier |

## Next action

(1) ~~`GAP-MFG-01` — open the flagged forum thread~~ **done 2026-09-29** — opened and cross-checked, but the thread (pre-19) and a blog source (Odoo 19) disagree; still needs an official Odoo 19 doc page or AWT to reach V2; (2) fold MFG-F01/F02 into the shared cross-Gx AWT capstone session (now spanning Gx1/2/4/5/6/7); (3) per the standing order's own suggestion this round — assess whether this is a good milestone to flag the full Lane C set (Gx1,2,4,5,6,7 = 6 of the original 10 scenarios) as ready for a consolidated CHATGPT_AUDIT pass, rather than continuing to Gx8 immediately.

## Stop point

`DOCUMENTATION STUDY COMPLETE / READY FOR PHASE A REPORT`. Ready for CHATGPT_AUDIT.
