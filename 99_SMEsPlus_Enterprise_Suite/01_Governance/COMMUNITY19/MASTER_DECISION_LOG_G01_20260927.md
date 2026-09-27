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

## Addendum — 2026-09-27 (post-R2B A3 re-check)

| ID | Decision | Basis | Effect |
|---|---|---|---|
| MD-11 | **Commit bundling caveat.** MASTER's own commit script batches several artifacts into one commit at whatever time the batch script runs, which is unrelated to each artifact's internal freeze/predeclare timestamps. Git commit time is NOT evidence of a stage's internal ordering — only each artifact's self-declared UTC timestamps and its own sha256 self-citation chain are. A3 re-checks must keep verifying ordering via the sha256 chain (as they have), not via git commit metadata. | A3 R2B re-check R2B-3 (3 addenda + 1 unrelated file landed in one commit; commit time postdates a self-declared internal begin-time) | No process change needed — this confirms the sha256-chain method already in use is the correct one; git commit timing is explicitly out of scope for stage-ordering evidence going forward. |

R-3 (single-controller identity across remediation stages) stays an open, non-blocking process residual carried forward system-wide; it does not gate content acceptance where re-checks independently re-verify substance from the anchor.

### R2 re-check running tally (2026-09-27), updated

- Clean (STATIC PASS, no residual): base_automation, bus, phone_validation, onboarding, web_unsplash, base_sparse_field.
- Open, non-blocking (LOW/MED, route noted, MASTER handoff still pending runtime only): auth_signup (R-ASGN-3), resource, resource_mail (R-3, R2B-3), google_recaptcha (R2B-1, R2B-2, R-3, R2B-3).
- Pending: R2C (web/mail) re-check.

## Addendum — 2026-09-27 (post-R2C A3 re-check)

| ID | Decision | Basis | Effect |
|---|---|---|---|
| MD-12 | **Rule 4/5 "disclosed rationalization" is not compliance.** A stage that runs its own predeclare+execute cycle before its own REC freeze, then writes a fresh "official" predeclaration afterward with outcomes already known, does NOT satisfy rules 4/5 — disclosure of the shortcut does not launder it, and it is a materially different case from an upstream stage's ordinary prior file read (which the B3B R1 recheck correctly excused). Applying disclosure-only leniency to one stage's premature predeclare-execute while requiring genuine independent re-derivation for an analogous ordering issue elsewhere in the same recheck is a double standard and is rejected. | A3 R2C re-check, RES-C1 (mail PROOF R2C) | `mail` stays STATIC PASS WITH RESIDUAL DEFECTS for this reason alone (substantive PASS results independently reproduced and not overturned). Requires a genuine re-run: freeze REC (or re-cite its existing sha256) BEFORE any new predeclare, predeclare blind (no prior execution of the same cases), then execute. Route to R3. |

### R2 re-check final tally (2026-09-27) — all 4 batches (A/B/C/D) complete

- **Clean, STATIC PASS, no residual (16):** digest, base, base_setup, portal, web_tour, http_routing, html_editor, privacy_lookup, utm, html_builder, web_hierarchy, base_automation, bus, phone_validation, onboarding, web_unsplash, web, base_sparse_field. (17, recount: digest/base/base_setup/portal/web_tour/http_routing/html_editor/privacy_lookup/utm/html_builder/web_hierarchy = 11 from A3-original; + base_automation/bus/phone_validation/onboarding/web_unsplash/web/base_sparse_field = 7 from R2 = 18 total clean of 23.)
- **Open, non-blocking process residuals only (route noted, content not overturned):** auth_signup (R-ASGN-3), resource, resource_mail (R-3 process, R2B-3 commit-bundling — informational per MD-11), google_recaptcha (R2B-1, R2B-2, R-3, R2B-3).
- **Open, needs a genuine re-run (R3):** mail (RES-C1 — rule 4/5 ordering must be redone for real, not just re-derived).
- No module FAIL. No PASS result overturned by any re-check.

## Addendum — 2026-09-27 (post-R3 A3 re-check, mail)

RES-C1 CLOSED — genuine cure verified independently by A3 (REC-basis hash match, predeclare-before-fetch mtime order confirmed, no undisclosed reconnaissance within the R3 cycle, all 4 cases re-derived a second time). `mail` residual status now carries only pre-existing, already-routed items (D03/K1/K4/K5 ordering residue → REC, informational; commit-subject naming → MASTER/IC, covered by MD-06/MD-11) — no new remediation owed for mail.

### Final G01 tally after R1/R2/R3 (2026-09-27)

- **Clean, STATIC PASS, no residual (19/23):** digest, base, base_setup, portal, web_tour, http_routing, html_editor, privacy_lookup, utm, html_builder, web_hierarchy, base_automation, bus, phone_validation, onboarding, web_unsplash, web, base_sparse_field, mail (RES-C1 closed; carries only already-routed, non-blocking process notes).
- **Open, non-blocking (route noted, content not overturned, 4/23):** auth_signup (R-ASGN-3 MED — needs a real re-enumeration, not just documentation), resource, resource_mail (R-3 process-only), google_recaptcha (R2B-1 LOW citation fix, R2B-2 accepted-with-note, R-3 process-only).
- **No module FAIL anywhere in the cycle.**
