# 07 — SC-06 VAT / CIT OWNERSHIP EVIDENCE POINTER CHECK

| Field | Required Value |
|---|---|
| SC ID | `SC-06` |
| Decision ID | `ACC-DEC-009` |
| Topic | VAT and CIT ownership (Accounting Core vs. separate Tax domain); scope status of `PND1`/`PND54`/`PP36` |
| Source files checked | `05_ACCOUNT_SCOPE_RESEARCH_REGISTER_SC01_SC10.md` (Batch A); `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` (source pack); `06_LEGAL_TAX_REVIEW_BRIEF.md` (required, source pack); `10_TAX_WHT_VAT_CIT_REPORTING_MAP.md` "Unresolved objections," items 7 and 9 (deep-study, local numbering); `17_AI_AUDIT_SMEPLUS_9_VETO_CHALLENGE.md` section `VC-06` header (deep-study) |
| Evidence pointer result | Partial |
| Owner status | Boss (ownership ruling); Legal-Tax (statutory content, per `06_LEGAL_TAX_REVIEW_BRIEF.md`) |
| Gate impact | `COA-G06` |
| GL impact known? | No — ownership itself (which domain posts VAT/CIT) is undecided, so no posting design exists |
| TB impact known? | No |
| BS / PL / Cash Flow / Tax Report impact known? | Tax Report: Yes — this row is explicitly about `PND1`/`PND54`/`PP36` filing-form scope; BS/PL/Cash Flow: No |
| Subledger or interface impact | N/A (Tax domain question, not a subledger) |
| Thai menu/report communication issue | No — this is an ownership/statutory-scope question, not a naming-fitness one |
| AI Audit SMEsPlus objection | `06_LEGAL_TAX_REVIEW_BRIEF.md` states plainly "**Zero authoritative Thai statutory citations exist in the Account chain today**" — every VAT/CIT/WHT item, including this row, is downstream of a review that has not yet been commissioned (`ACC-DEC-014`, owner `UNASSIGNED`); ruling on ownership without that review risks assigning VAT/CIT to a domain before the statutory shape of the obligation is even known |
| Readiness classification | `READY AFTER BOSS SCOPE DECISION` (ownership ruling) — but note this decision itself should not be finalized before `ACC-DEC-014` (legal-tax review commissioning) returns findings, per the dependency both required registers describe ("Feeds `06_LEGAL_TAX_REVIEW_BRIEF.md`... which covers all forms regardless of eventual ownership split") |
| Next action | Boss rules Accounting Core / separate Tax domain / split-by-form in `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md`; `06_LEGAL_TAX_REVIEW_BRIEF.md` items `WHT-7` (`PND1`), `WHT-8` (`PND54`), `WHT-9` (`PP36`) all remain `LEGAL_TAX_REVIEW_REQUIRED` regardless of the ownership ruling's outcome |

## Detail

Both required registers cite "source `05` row `ACC-DEC-009`; source `10` objections 7, 9; prior `VC-06`." "Source `10` objections 7, 9" resolves outside the required perimeter to `10_TAX_WHT_VAT_CIT_REPORTING_MAP.md`'s "Unresolved objections noticed" list:

- Objection 7: "**CIT is a GAP at every step (TP-05.1–05.4)** and `VC-06` recorded that it is *undecided* whether CIT belongs to Accounting Core at all; the CIT rows here are candidates without a scope decision."
- Objection 9: "**`PND1` / `PND54` / `PP36` (TCAL-08, TO-17)** are present in the chart template but absent from Boss Section 6 and from every register — either out of scope by decision or a silent omission; Boss must state which."

Both are precise, on-point matches to this row's exact topic (CIT ownership undecided; `PND1`/`PND54`/`PP36` scope status). **Verified** for this sub-pointer.

"Prior `VC-06`" was checked against `17_AI_AUDIT_SMEPLUS_9_VETO_CHALLENGE.md`, which does carry a section header "`## VC-06` — Financial / Accounting / Tax / Statutory VETO" (line 76). This session's targeted fetch of that file captured the section headers and the summary table but not the full `VC-06` section body, so the specific content behind "prior `VC-06`" (referenced in objection 7 above as having "recorded that it is undecided whether CIT belongs to Accounting Core") was not independently re-read in full — only its existence as a real, correctly-titled section was confirmed. Marked **Partial** for this specific sub-citation, consistent with not inventing evidence beyond what was actually read.

Row-level result: **Partial** (one of two sub-pointers fully verified; the `VC-06` reference confirmed to exist but not fully read).
