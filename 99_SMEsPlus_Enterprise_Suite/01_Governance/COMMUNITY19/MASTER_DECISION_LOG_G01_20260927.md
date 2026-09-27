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

## Addendum — 2026-09-27 (post-B3a A3 re-check)

| ID | Decision | Basis | Effect |
|---|---|---|---|
| MD-07 | **Evidence admissibility rule.** Only bytes fetched at the pinned source anchor (`odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`) and verified by `git hash-object` are admissible as SOURCE-STATIC evidence. Default-branch GitHub code search, code indexes, training recall and any unpinned listing are NOT admissible and may be used only to generate candidates that are then verified at the anchor. Any claim resting on unpinned evidence is classified `UNVERIFIED-AT-ANCHOR` and may not be consolidated. | A3 B3a re-check §3–§6: the sign-up-link caller list came from a default-branch code search; its `hr_employee` and `website_sale` candidates do not exist at the anchor, and two anchored callers were missing from the Proof table. | Cross-module caller enumeration must be redone at the anchor by following manifests and `__init__` imports. Applies to all stages and all G. |
| MD-08 | Cross-module enumeration claims ("the only callers are …", "no caller exists") are inadmissible as completeness claims unless the enumeration method is stated and anchor-reproducible; otherwise record as bounded evidence ("these callers are confirmed") plus an explicit completeness gap. | Same finding | Prevents false-negative completeness claims (e.g., onboarding route owner, base_automation call sites). |
| MD-09 | Runtime execution for base_automation R1, RCAP/SPRS R1 and B3a packs must be performed by an author that is neither the addenda controller nor the A3 re-checker of that pack. | MD-04 extended per A3 B3a §10 (A3's own cases were not blind) | Recorded for the runtime cycle, once a runtime environment exists. |

### A3 B3a re-check outcome (2026-09-27)

- `base_setup`, `base`, `portal`: **A3 STATIC PASS — MASTER HANDOFF PENDING RUNTIME** (no residual defects).
- `auth_signup`, `base_automation`: **A3 STATIC PASS WITH RESIDUAL DEFECTS** — R-ASGN-1/2, R-BAUT-1 (all LOW) → R2 cycle.
- No A3 finding overturned an upstream verdict in this batch.

## Addendum — 2026-09-27 (post-R2A A3 re-check)

| ID | Decision | Basis | Effect |
|---|---|---|---|
| MD-10 | **Repeat MD-07 violation pattern.** A remediation addendum self-certified "MD-07 MET" while asserting an unfetched transitive dependency chain (`website_slides → website_mail → portal → auth_signup`) that does not exist at the anchor (`website_mail` depends only on `website`/`mail`). This is the second occurrence of this failure mode (first: B3a sign-up-link callers from a default-branch search). Self-certification of MD-07/MD-08 compliance in a rule-compliance table is NOT sufficient evidence of compliance; A3 re-check must independently re-fetch every manifest/dependency edge a remediation cites as its enumeration method, every time, not just spot-check. | A3 R2A re-check on auth_signup (R-ASGN-3, MED) | A3 re-check prompts must always include "independently re-fetch every manifest edge the addendum's enumeration method cites" as a named task, not an optional spot-check. |

### R2 re-check running tally (2026-09-27)

- Clean (STATIC PASS, no residual): base_automation, bus, phone_validation, onboarding, web_unsplash (R2A/R2D).
- Open: auth_signup — new residual R-ASGN-3 (MED, route A2/REC/PROOF): re-enumerate the auth_signup cross-module caller chain at the anchor only, per manifest edges actually fetched; the website_slides call-site conclusion itself still stands (verified via the real chain website_slides → portal_rating → portal → auth_signup) — only the false alternate chain needs retraction.
- Pending: R2B (resource/resource_mail/recaptcha/sparse), R2C (web/mail) re-checks.
