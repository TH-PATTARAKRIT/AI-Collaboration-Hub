# 05 — STEP0301 Conflict and Duplication Register

Session ID: [SMEPLUS-26-07-15-001] · State 03 / STEP0301 · Control Level /L99.99 · Mode: CORRECTION & REVALIDATION
Target branch: SMEsPlus @ `d995ae2986c4610b102307398591dbaba60be9e0` · Re-inspected (UTC): 2026-07-15T00:20:44Z
Previous inspection SHA (superseded): `5cd3a2ca9649f4e1d5345f8dc7e56688b5b5ef91`

**No conflict is resolved by this task.** Both sides of every conflict are recorded.
Status = OPEN. Decision authority = Boss (with ChatGPT L99 independent review).

| ID | Type | Description | Side A (evidence) | Side B (evidence) | Severity | Next Action | Status |
|---|---|---|---|---|---|---|---|
| CONF-01 | DUPLICATE / CONFLICT | Two State 03 Evidence Registers with different content | Target: `STATE03_EVIDENCE_REGISTER.md` blob `9569ceb7…` (skeleton, all "Pending"/NOT VERIFIED) | PR #26: same path, blob `90351835…` (modified, +57/−21) | P1 | Reconcile to one canonical register (do not silently pick one) | OPEN |
| CONF-02 | STALE | PR #26 recorded base is behind current SMEsPlus HEAD | PR #26 base `8570187b…` (GitHub metadata) | Current SMEsPlus HEAD `d995ae2…` (`git ls-remote`; was `5cd3a2ca…` at prior inspection) | P1 | Rebase PR onto current HEAD before any merge decision | OPEN |
| CONF-03 | CONFLICT (self-description) | PR #26 body claims "Changed files: 21, all within STATE03_ARCHITECTURE_ACCELERATION/ (0 outside)" | PR #26 body text | Actual `get_files` = **30 files**: **21 inside** the folder (body's 21 matches this subtotal) and **9 outside** (`02_Functional_Design/ACC-002..005`, `ACC_GAP_CLOSURE_BATCH01_MANIFEST_SHA256.txt`, `ACC_GAP_CLOSURE_METADATA_FIX/_SUPERSEDED_DO_NOT_USE.md`, `Archived/…/PUSH_READY.md`, root `CLAUDE_EXECUTION_EVIDENCE_STANDARD.md`, `CLAUDE_EXECUTION_GAP_REPORT.md`). The "0 outside" claim is **false**. | P1 | Correct PR body; re-scope before merge | OPEN |
| CONF-04 | CONFLICT (count) | PR #26 file-count inconsistency | GitHub `changed_files: 31` (PR metadata) | `get_files` returns 30 rows (re-verified at correction time) | P2 | Confirm exact changed-file set at review | OPEN |
| CONF-05 | STALE / SELF-CORRECTION | PR #26 body states an earlier note ("branch carries prior unmerged State 02 commits") is "no longer accurate" | PR #26 body (current) | Prior PR note (superseded) | P2 | Verify current commit graph at review | OPEN |
| CONF-06 | UNVERIFIED SELF-VALIDATION | PR #26 ships a self-run validation report "13/13 pass" and its own SHA-256 manifest, presented alongside deliverables | `STATE03_VALIDATION_REPORT.md`, `validate_state03_package.py`, `PACKAGE_MANIFEST_SHA256_STATE03_ARCHITECTURE.txt` | No independent recomputation / no ChatGPT L99 verification on record | P1 | Independent reviewer must recompute SHA-256 and re-run validation | OPEN |
| CONF-07 | DRAFT-PRESENTED-AS-BASELINE (control risk) | Prior control position treats Scope V2 / Gate Model as "baseline" though both are self-declared CONTROLLED DRAFT without Boss approval provenance | Prior control position (task input) | Files declare "CONTROLLED (BASELINE) DRAFT" + "Final Approval Authority: Boss" (not yet approved) | P1 | Boss confirm at Gate A; do not treat as APPROVED_BASELINE | OPEN |
| CONF-08 | SUPERSEDED reference | PR #26 introduces a superseded marker file | `ACC_GAP_CLOSURE_METADATA_FIX/_SUPERSEDED_DO_NOT_USE.md` (PR #26) | Referenced/related manifest `ACC_GAP_CLOSURE_BATCH01_MANIFEST_SHA256.txt` modified | P2 | Confirm no live document references superseded content | OPEN |
| CONF-09 | OWNER inconsistency | Owner Matrix uses role-titles; PR deliverable index uses slightly different owner labels (e.g. "Enterprise Control Architecture AI Owner" not in the 24-row matrix) | `ARCHITECTURE_DOMAIN_OWNER_MATRIX.md` (target) | `STATE03_DELIVERABLE_INDEX.md` (PR #26) | P2 | Normalize owner taxonomy | OPEN |
| CONF-10 | SCOPE vs ACCELERATION mismatch | Scope V2 defines 24 domains; Acceleration README defines 14 immediate work items (ARC-WP) — not a 1:1 mapping (10 domains have no WP) | Scope V2 (24 domains) | Acceleration README (14 WPs) | P1 | Boss decision on how domains map to Steps/WPs (do not auto-convert) | OPEN |
| CONF-11 | TERMINOLOGY (Open ERP constitution) | PR #26 architecture source uses non-canonical `Odoo-first` / `Odoo-style` product terminology, conflicting with the Boss-approved **Open ERP** canonical terminology now on target (`d995ae2`) | Open ERP constitution / target State 01 (`Open ERP-first`) | PR #26 (PR_ONLY, unmerged): **13 occurrences** across `SAAS_ARCHITECTURE_PRINCIPLES.md` (4), `APPLICATION_MODULE_BOUNDARY.md` (2), `ARCHITECTURE_DECISION_REGISTER.md` (3), `ARCHITECTURE_RISK_ASSUMPTION_REGISTER.md` (2), `LOGICAL_COMPONENT_ARCHITECTURE.md` (1), `STATE03_EXECUTION_SUMMARY.md` (1) | P1 | Align PR #26 source to Open ERP under separate Boss authorization; classify clean-room/UX-reference usages as `HISTORICAL_SOURCE_REFERENCE — NOT PROJECT CANONICAL TERMINOLOGY`. **STEP0301 does not modify PR #26.** | OPEN |

## Notes

- No architecture document was found stored **outside** a controlled path on the target
  branch for the 24 domains; the controlled roots are
  `03_Architecture/00_Architecture_Governance/` and
  `03_Architecture/STATE03_ARCHITECTURE_ACCELERATION/`. (PR #26 adds non-architecture files
  outside these roots — see CONF-03.)
- No conflicting tenant/data-isolation model was found on the **target** branch (the tenant
  and isolation deliverables are PR_ONLY); any isolation-model conflict is internal to PR
  #26 and must be assessed there, not on the baseline.
- All conflicts remain OPEN. This task does not choose a winning side.
- **Conflict count: 11** (CONF-01..11). Severity basis: **P1 = 7** (CONF-01, 02, 03, 06, 07, 10, 11);
  **P2 = 4** (CONF-04, 05, 08, 09). These are conflict-register counts and are **not** added to the
  Gap Register's P0/P1/P2 totals (different counting basis).
- **Open ERP terminology classification (CONF-11):** the retained `Odoo` references inside PR #26
  that support clean-room / UX-reference traceability are to be labelled
  `HISTORICAL_SOURCE_REFERENCE — NOT PROJECT CANONICAL TERMINOLOGY` when corrected; the canonical
  project product term is **Open ERP**. The STEP0301 package and the target `03_Architecture/`
  tree contain **zero** non-canonical product-terminology occurrences.
