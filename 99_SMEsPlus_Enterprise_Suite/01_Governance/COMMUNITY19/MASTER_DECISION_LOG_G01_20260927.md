# MASTER Decision Log — G01 PLATFORM_BASE

Date: 2026-09-27
Authority: MASTER (Claude Code, Preparer/Executor). Boss remains Sole Final Approver; none of these decisions is Final Approval or Formal Coverage.

| ID | Decision | Basis | Effect |
|---|---|---|---|
| MD-01 | Where two independent A3 passes diverge, the stricter result governs; later passes are registered as supplements, originals are never edited. | A3 divergence on resource / resource_mail | resource_mail → A3 STATIC PASS WITH DEFECTS (LOW). See G01_A3_CHALLENGES/G01_RESOURCE_RMAIL_A3_SUPPLEMENT_S2_20260927.md |
| MD-02 | SUSPEND MASTER consumption of REC-RCAP-09/10/11. | A3 HIGH sustained (G01_A3_CHALLENGES/G01_GOOGLE_RECAPTCHA_A3_STATIC_20260927.md) | Items barred from consolidation. |
| MD-03 | LIFT MD-02 in favour of REC-RCAP-09R1/10R1/11R1 (and C08R1-a/b/c, SF-1R1). Originals remain superseded, not deleted. | A3 R1 re-check: all 8 original defects CLOSED on content; A3 states MASTER MAY LIFT (G01_A3_CHALLENGES/G01_RCAP_SPRS_A3_RECHECK_R1_20260927.md) | R1 items eligible for consolidation once runtime proof runs. |
| MD-04 | Runtime proof cases for any module whose remediation addenda were written by a single controller across owner stages must be executed by a different author than that controller. | A3 residual R-3 (recaptcha/sparse) and base_automation R1 separation-of-duties concern | Applies to base_automation R1 and RCAP/SPRS R1 runtime packs. |
| MD-05 | Process rules 1–5 (MASTER_CONTROLLED_HANDOFF_STATE_20260927_C1B.md) are mandatory in every dispatch from batch3 onward; each addendum carries a rule-compliance table. | Repeated rule breaches found by A3 in R1 re-checks | Enforced in remediation B3a/B3b/B3c prompts. |
| MD-06 | Commit subjects are generated from the artifact file names actually committed; commit body lists every path. | A3 Integration Control findings (multiple modules) | Content lineage unaffected; label lineage corrected going forward. |

## Open residuals carried (not blocking MD-03)

- RCAP/SPRS R-2 (MED): REC R1 written after Proof and citing Proof — rule 4 breach; remediation B3 series to re-freeze REC ordering.
- RCAP/SPRS R-5: Lane A item 12 erratum to be issued by the Lane A owner (next Lane A cycle).
- base_automation R1 residuals RD-1..RD-6 → remediation B3a.
