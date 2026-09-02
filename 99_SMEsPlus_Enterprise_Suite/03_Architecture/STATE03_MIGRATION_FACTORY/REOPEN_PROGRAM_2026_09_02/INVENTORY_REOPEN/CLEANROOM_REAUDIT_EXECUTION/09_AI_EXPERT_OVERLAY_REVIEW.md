# 09 — 4 AI Expert Roles Overlay Review

Session: `SMEPLUS-26-09-02-INV-CLEANROOM-REAUDIT-001` | Control Level: `/L999.999`
Status: `CP-07 OUTPUT — OVERLAY CHALLENGE ONLY — NOT APPROVAL, NOT A SUBSTITUTE FOR 9+9`

**Independence disclosure:** four lenses applied in sequence by one session after `07` and `08` were drafted; not four independent parties. These roles may challenge, expose unknowns, and recommend evidence; they may not approve. Per prompt §6 minimum focus: functional design risk, database identity risk, integration/localization risk, code/UI architecture leakage risk.

---

## E1 — Functional Design Risk

**Question:** Does this re-audit's classification of the menu-level process content create any hidden functional-design risk if a future reader over-trusts it?

**Finding:** The main risk is exactly the one named in `05` §1 — confident declarative process prose (file `06` and the operational maps) without a per-claim hedge, which could be mistaken for validated requirements by a reader who only skims file headers. `06`'s classification of these surfaces as `SAFE_FOR_AI_AUDIT_ONLY` (not `SAFE_FOR_TEAM_B_AFTER_BOSS_APPROVAL`) is the correct mitigation at the governance layer, but does not by itself prevent a careless reader from treating the content as more settled than it is.

**Recommendation:** any future prompt that hands this package to a reading session (Team B or otherwise) should explicitly restate, in the prompt itself, that process content is benchmark-derived and Thai-fitness-unvalidated — do not rely on the package's internal header hedges alone to carry that warning forward.

## E2 — Database Identity Risk

**Question:** Does anything in this re-audit's own findings bear on object-identity or migration-key risk?

**Finding:** Not directly — this re-audit did not investigate object-identity design; that remains the province of the original package's own doc `03`/`18` and the still-open `GAP-MD-27` provenance-map gap named there. The one identity-adjacent item this re-audit did surface is structural: file `10`'s carried-over location scaffold (`03` §4) is itself a location-identity structure (a specific parent/child node set), not just a naming choice — if a future schema design used this five-node structure as its starting point without re-deriving it from Thai practice, that would convert a wording issue into an identity-design issue.

**Recommendation:** when file `10` is rewritten (per `03` §4 and `05` §4), the rewrite should explicitly re-derive the location *set*, not just re-word the existing five nodes, so downstream identity design is not anchored to an uncontested benchmark structure.

## E3 — Integration / Localization Risk

**Question:** Does this re-audit's citation/provenance work expose any integration or localization risk?

**Finding:** `04` §3 confirms statutory/localization claims remain properly hedged throughout the package — this is a genuine strength, independently re-verified, not merely re-asserted. The `R:` external-citation convention (`04` §2) is a minor integration-risk item in its own right: because it is undocumented inside the package, any future reader who receives only the 29-file package without the separate reopen package will be unable to resolve `R:` citations at all, which is a localization-of-context risk for the package's own portability.

**Recommendation:** the package's next revision should add one line defining the `R:` convention, or inline the cited reopen content directly, before the package is handed to any reader who may not have the reopen package alongside it.

## E4 — Code / UI Architecture Leakage Risk

**Question:** Does anything in the package or in this re-audit's own findings leak reference-vendor code or UI architecture?

**Finding:** This is the direct subject of `02` and `03`. Summary: the CORR-007B branch-tip surface is mechanically clean (zero true-positive leakage across five check categories, independently verified); the menu package is mechanically clean against seven check categories with one exception (file `10`'s location-path notation, a structural/naming leak rather than a code leak); and the original pre-remediation leak remains reachable in git history, which is a repository-architecture risk rather than a currently-published-content risk. No UI architecture (screens, components, layout) was found leaked anywhere, consistent with prompt §2 prohibition 6 — no file proposes any final SMEsPlus UI, schema, workflow, or architecture.

**Recommendation:** this is the finding that most directly answers the issuing prompt's Mandatory `C-05` Review question 4 ("whether the old risk remains in git history") — yes, and it is the single highest-priority residual item this entire re-audit surfaces. See `10_REMEDIATION_ACTION_REGISTER.md` and `11_BOSS_FINAL_GATE_PACKAGE.md`.

---

## Overlay Convergence

E1 and E3 name process/portability hygiene issues (wording depth, undocumented citation convention) that are real but minor and correctable by the package's maintainers without Boss involvement. E2 names a design-anchoring risk contingent on how file `10` is eventually rewritten — worth a note to whoever performs that rewrite. **E4 is controlling**: it independently confirms the `02`/`03` mechanical findings and correctly identifies the git-history reachability gap as the single most material open item from this entire re-audit.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
