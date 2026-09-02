# 03 — Inventory v1.0 to v2.0 Delta Map

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V2-001` | Jira: `ERPPLUS-139`
Status: `DELTA MAP — WHAT CHANGED, WHAT DID NOT, AND WHY`

---

## 1. Governing Instruction

The new-session prompt §4 is explicit: "Do not rewrite v1.0 wholesale unless the COGS evidence requires a delta." File 02 establishes that the COGS evidence does not exist. It follows that it cannot *require* a delta to the functional design — there is nothing in it to incorporate. This file records, file by file, exactly what changed and what did not, so that a reader comparing v1.0 and v2.0 side by side finds no unexplained difference.

---

## 2. File-by-File Disposition

| v1.0 file | Subject | v2.0 disposition | Reason |
|---|---|---|---|
| `03_INVENTORY_FUNCTIONAL_DESIGN_V1.md` | Functional scope, boundaries, operating model, design principles | **Unchanged. Carried by reference.** | No COGS evidence exists to inform a change; nothing in this file asserts a COGS or valuation-policy conclusion that the gap would affect |
| `04_INVENTORY_MENU_FUNCTION_MATRIX_V1.md` | 29-menu matrix | **Unchanged. Carried by reference.** | Same — the menu matrix describes Inventory-side Purpose/Input/Process/Output/Accounting-Control Impact per menu; it already states impacts as facts emitted, not postings decided (v1.0 file 07 §1), so it is not itself gated |
| `05_INVENTORY_PROCESS_FLOW_CATALOG_V1.md` | Process flows and UAT scenarios | **Unchanged. Carried by reference.** | Same reasoning |
| `06_INVENTORY_OBJECT_DATA_CONCEPT_MODEL_V1.md` | Conceptual object model | **Unchanged. Carried by reference.** | Same reasoning; no schema or account structure is named in this file for COGS evidence to revise |
| `07_INVENTORY_ACCOUNTING_CONTROL_IMPACT_V1.md` | Accounting and control impact | **Unchanged in content. Referenced and gated explicitly in file 02 and file 04 of this package.** | This file already states the interface rule correctly ("Inventory emits facts. Accounting decides postings.") and already lists every open Joint decision (`JT-01`–`JT-12`) as open. The COGS evidence, when it exists, will inform how Accounting resolves those decisions — it does not change what Inventory-side file 07 says today |
| `08_INVENTORY_VALUATION_LANDED_ANALYTIC_COST_V1.md` | Valuation, landed cost, analytic cost | **Unchanged in content. Referenced and gated explicitly in file 02 and file 04 of this package.** | Same reasoning; this file already declines to choose a valuation-policy owner (§1: "This session does not choose") and already marks every Thai costing norm `HOLD / EVIDENCE REQUIRED` |
| `09_INVENTORY_REPORTING_ANALYTICS_V1.md` | Reporting, stock card, dashboards | **Unchanged. Carried by reference.** | Report *requirements* (reproducibility, drill-through, export integrity) do not depend on which valuation policy is eventually chosen |
| `10_INVENTORY_CROSS_MODULE_HANDOFF_V1.md` | Cross-module handoff | **Unchanged. Carried by reference.** | Same reasoning; Accounting handoff rows already state "fact emitted, posting decided by Accounting" |
| `11_INVENTORY_THAI_LOCALIZATION_UX_NAMING_V1.md` | Thai localisation, UX naming, statutory routing | **Unchanged. Carried by reference.** | Not affected by the COGS Gap; still blocked on Thai user validation (`GAP-FS-11`), a separate and independent dependency |
| `12_INVENTORY_RISK_GAP_DECISION_REGISTER_V1.md` | Risk, gap and decision register | **Superseded by `07_RISK_GAP_DECISION_REGISTER_V2.md` of this package**, which carries every v1.0 item forward unchanged, adds explicit COGS-Gap dependency flags to the twelve `JT-*` items and to `GAP-FS-01`/`GAP-FS-12`, and adds one new item for the COGS Deep Research session's non-execution | The register itself is the correct place to record the new dependency flag; nothing else about it changes |
| `13_AI_AUDIT_SMEPLUS_FINAL_SOLUTION_CHALLENGE_V1.md` | 22-lane challenge | **Not re-run. Superseded in scope by `06_AAS_PLUS_AND_PMO_REVIEW_V2.md` of this package**, which is a narrower, focused review of this session's own dependency-gate compliance rather than a second full 22-lane pass over unchanged content | Re-running all 22 lanes over functional content that did not change would not produce new information; the new information this session has to challenge is the dependency-gate decision itself |
| `14_BOSS_FINAL_GATE_PACKAGE.md` | Boss Final Gate package | **Superseded by `08_BOSS_FINAL_GATE_PACKAGE.md` of this package** for v2.0 purposes; the v1.0 file remains the record of what v1.0 itself delivered | New file restates v1.0's still-open Priority 1 and Priority 2 items and adds the COGS Deep Research execution as the controlling new item |
| `15_NEXT_PROMPT_RECOMMENDATION.md` | Next-session recommendation | **Superseded by `09_NEXT_PROMPT_RECOMMENDATION.md` of this package**, which now leads with executing the COGS Deep Research session (v1.0's own recommendation, candidate A, could not start unilaterally at the time; that constraint has not changed, but the prerequisite research Boss separately commissioned for it has itself stalled at readiness) | The candidate list is not discarded — Thai user validation and migration provenance remain valid, independent, unblocked candidates and are carried forward |
| `16_SHA256_MANIFEST.txt` | v1.0 hash manifest | **Not reused.** A new manifest, `10_SHA256_MANIFEST.txt`, is computed over this package's own files | Manifests are branch- and commit-specific by design |
| `17_SESSION_CLOSURE_...md` | v1.0 session closure | **Not reused.** A new closure file, `11_SESSION_CLOSURE_SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V2-001.md`, records this session's own publication | Each session closes itself |

---

## 3. Net Effect

Six of eleven v1.0 content files (03–06, 09–11) are unchanged and are not reproduced in this package — a reader needing them reads them on the v1.0 branch, cited by direct link in file 11 §2 of this package. Two files (07, 08) are unchanged in content but are now cross-referenced by an explicit dependency gate. Three files (12, 13, 14/15 pairs) are superseded in scope, not in substance, by narrower v2.0-specific equivalents that add the dependency framing without re-deciding anything v1.0 left open.

**No menu, process, object, report, handoff, or Thai-naming content changed.** The only genuinely new content in v2.0 is: the dependency register (file 02), the decision matrix of what may proceed versus what must wait (file 04), the explicit dependency framing for the ten scope areas named in the new-session prompt §4 (file 05), and the focused AAS+/PMO review of the gate itself (file 06).

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
