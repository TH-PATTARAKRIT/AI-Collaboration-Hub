> **CANDIDATE-ROSTER PILOT — G11 membership is DERIVED, not Boss-confirmed; not Formal Coverage; not a precedent for opening any other G02–G16 group.** See `MASTER_DECISION_LOG_G01_20260927.md` MD-17/MD-18.

# LANE-A-G11-001 — Result

Date: 2026-09-28
Task: Formal LANE A intake/pass evaluation for G11 EVENTS (8-module roster) before A1 admission.
Executor: Claude Code (this session — `ai-collaboration-hub-a6`, working branch `claude/awesome-gauss-jw1934`)

## 1. Roster verification (8/8)

All 8 modules in the controlled G11 input roster exist and were fetched/hash-verified at the
pinned source anchor (`odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`):

| # | Module | Lane A Pass-1 file | Fetch/hash result |
|---|---|---|---|
| 1 | `event` | `A1_SOURCE_EVIDENCE_LANE/G11_LANE_A_PASS1/G11_EVENT_LANE_A_PASS1_20260928.md` | PASS |
| 2 | `event_booth` | `.../G11_EVENT_BOOTH_LANE_A_PASS1_20260928.md` | PASS |
| 3 | `event_booth_sale` | `.../G11_EVENT_BOOTH_SALE_LANE_A_PASS1_20260928.md` | PASS |
| 4 | `event_crm` | `.../G11_EVENT_CRM_LANE_A_PASS1_20260928.md` | PASS |
| 5 | `event_crm_sale` | `.../G11_EVENT_CRM_SALE_LANE_A_PASS1_20260928.md` | PASS |
| 6 | `event_product` | `.../G11_EVENT_PRODUCT_LANE_A_PASS1_20260928.md` | PASS |
| 7 | `event_sale` | `.../G11_EVENT_SALE_LANE_A_PASS1_20260928.md` | PASS |
| 8 | `event_sms` | `.../G11_EVENT_SMS_LANE_A_PASS1_20260928.md` | PASS |

Aggregate: 116 files fetched across the 8 modules (manifest, models, security CSV/XML, seed
data, controllers/wizards/reports where present), 116/116 `git hash-object` blob-hash matches
against the pinned commit's tree, 0 fetch failures, 0 nonexistent paths. No unpinned listing,
code search, or training recall used as evidence (MD-07).

**Membership status: DERIVED, not CONFIRMED.** All 8 names are reconstructed from the
historical "event*(8)" rule + static registry (see `A1_G09_G12_PARALLEL_STATIC_CHECKPOINT_20260924.md`
and `GROUP_STRUCTURE_V2_CORE_CANDIDATE_20260928.tsv`), not from a controlled roster row. This
Lane A pass verifies the 8 modules *exist and are fetchable/hash-verifiable at the anchor* — it
does not and cannot upgrade their group membership to CONFIRMED. That requires the controlled
`GROUP_STRUCTURE_V2_CORE.tsv` or an explicit Boss ruling (per MD-17/18).

## 2. Excluded-row check

`event_sale_iot` and `event_social` were explicitly checked and confirmed **excluded** — both
are OEEL-1 (Odoo Enterprise Edition License), not Community, per the same source checkpoint
that reconstructed the event* family. Neither appears in any Lane A Pass-1 file produced here,
and neither is asserted as part of the Community-scope G11 roster.

## 3. GMVQ Question Bank availability

**Corrected 2026-09-28 per Independent Review (PR #72 comment 5859366737, verified before
applying):** the original version of this section checked only the canonical `GMVQ/` tree on
`SMEsPlus`/this branch and found no `GMVQ/G11_EVENTS/` directory there — true, but incomplete.
Independently re-checked against `pull_request_read(get_files)` on PR #71
(`TH-PATTARAKRIT/AI-Collaboration-Hub#71`, **closed, unmerged**): its file list does contain a
draft candidate question bank for all 8 G11 modules, under
`GMVQ_CANDIDATE_ROSTER_NOT_VERIFIED/G11_EVENTS/` (e.g.
`G11_EVENT_GMVQ_MVQ_62_V1.00_DRAFT.md`, `G11_EVENT_BOOTH_GMVQ_MVQ_50_V1.00_DRAFT.md`, one file
per module, all suffixed `_DRAFT`).

| Module | Question Bank existence | Artifact path (in PR #71) | Source PR | PR state | Merge state | Governance status |
|---|---|---|---|---|---|---|
| `event` | YES (candidate) | `GMVQ_CANDIDATE_ROSTER_NOT_VERIFIED/G11_EVENTS/G11_EVENT_GMVQ_MVQ_62_V1.00_DRAFT.md` | #71 | closed | NOT merged | FOUND_CANDIDATE_UNMERGED / NOT YET ADMITTED TO CANONICAL GMVQ TREE |
| `event_booth` | YES (candidate) | `GMVQ_CANDIDATE_ROSTER_NOT_VERIFIED/G11_EVENTS/G11_EVENT_BOOTH_GMVQ_MVQ_50_V1.00_DRAFT.md` | #71 | closed | NOT merged | FOUND_CANDIDATE_UNMERGED / NOT YET ADMITTED TO CANONICAL GMVQ TREE |
| `event_booth_sale` | YES (candidate) | `GMVQ_CANDIDATE_ROSTER_NOT_VERIFIED/G11_EVENTS/G11_EVENT_BOOTH_SALE_GMVQ_MVQ_50_V1.00_DRAFT.md` | #71 | closed | NOT merged | FOUND_CANDIDATE_UNMERGED / NOT YET ADMITTED TO CANONICAL GMVQ TREE |
| `event_crm` | YES (candidate) | `GMVQ_CANDIDATE_ROSTER_NOT_VERIFIED/G11_EVENTS/G11_EVENT_CRM_GMVQ_MVQ_48_V1.00_DRAFT.md` | #71 | closed | NOT merged | FOUND_CANDIDATE_UNMERGED / NOT YET ADMITTED TO CANONICAL GMVQ TREE |
| `event_crm_sale` | YES (candidate) | `GMVQ_CANDIDATE_ROSTER_NOT_VERIFIED/G11_EVENTS/G11_EVENT_CRM_SALE_GMVQ_MVQ_48_V1.00_DRAFT.md` | #71 | closed | NOT merged | FOUND_CANDIDATE_UNMERGED / NOT YET ADMITTED TO CANONICAL GMVQ TREE |
| `event_product` | YES (candidate) | `GMVQ_CANDIDATE_ROSTER_NOT_VERIFIED/G11_EVENTS/G11_EVENT_PRODUCT_GMVQ_MVQ_50_V1.00_DRAFT.md` | #71 | closed | NOT merged | FOUND_CANDIDATE_UNMERGED / NOT YET ADMITTED TO CANONICAL GMVQ TREE |
| `event_sale` | YES (candidate) | `GMVQ_CANDIDATE_ROSTER_NOT_VERIFIED/G11_EVENTS/G11_EVENT_SALE_GMVQ_MVQ_50_V1.00_DRAFT.md` | #71 | closed | NOT merged | FOUND_CANDIDATE_UNMERGED / NOT YET ADMITTED TO CANONICAL GMVQ TREE |
| `event_sms` | YES (candidate) | `GMVQ_CANDIDATE_ROSTER_NOT_VERIFIED/G11_EVENTS/G11_EVENT_SMS_GMVQ_MVQ_48_V1.00_DRAFT.md` | #71 | closed | NOT merged | FOUND_CANDIDATE_UNMERGED / NOT YET ADMITTED TO CANONICAL GMVQ TREE |

Governance boundary (explicit, per this remediation's own instruction): question bank
existence above proves none of the following, and none of the following may be inferred from
it — canonical roster membership, canonical GMVQ admission, downstream authorization, or
Formal Coverage eligibility. G11's roster membership stays exactly what it already was
(DERIVED, per MD-18) — this correction does not upgrade it, and the module name list itself
was never in question (all 8 names are independently confirmed present and hash-verified via
this task's own Lane A Pass-1 evidence, §1 above).

This status is **evidence of question-authoring state only, not roster-membership evidence**
(per this task's own instruction and MD-08) — a draft bank existing in a closed, unmerged PR
does not confirm G11's DERIVED membership, does not admit G11 to A1, and PR #71 itself is not
treated as canonical or downstream-authorized (its own governance status, unchanged since it
was closed, is CANDIDATE / ROSTER NOT VERIFIED / NOT FOR DOWNSTREAM CONSUMPTION). If/when PR
#71's content — or an equivalent — is merged to the canonical `GMVQ/` tree, this status should
be re-checked and updated accordingly.

## 4. Duplicate / cross-group conflict check

- **No duplicate technical names.** None of the 8 `event*` modules appears under any other
  group in `GROUP_STRUCTURE_V2_CORE_CANDIDATE_20260928.tsv` or any G01 evidence.
- **No cross-group conflict found.** `event_crm` and `event_crm_sale` share a manifest
  dependency on `crm` (G09's own anchor module) — this is a dependency relationship, not a
  group-membership claim, and is recorded as such in each file's Lane A Pass-1 evidence, per
  MD-07/08 discipline (dependencies never imply group ownership).
- **event_sale's ACL widening finding (carried forward for A1's attention):**
  `event_sale/security/event_security.xml` grants every `sales_team.group_sale_salesman`
  member the `event.group_event_registration_desk` group via `implied_ids` — a source-confirmed,
  install-time widening of an existing group's permissions. This is a Lane A observation only;
  its functional/business-rule significance is A1's to assess, not Lane A's.

## 5. Evidence lineage

All 8 Lane A Pass-1 files carry: source anchor + commit, per-file evidence-pointer tables
(path + blob SHA-1 + purpose), WHAT/WHY/RISK findings, explicit evidence gaps/limitations
sections, and the CANDIDATE-ROSTER PILOT banner. No existing G01 file, GMVQ candidate TSV, or
any other prior artifact was modified — this task only added the 8 new Lane A Pass-1 files
(prior commits) and this RESULT file.

## 6. Required disposition

**`LANE_A_PASS_RECOMMENDATION`**

Rationale: every Lane A-scope check this task requires (module existence, source-anchor
fetch/hash verification, GMVQ bank check, duplicate check, cross-group conflict check,
excluded-row check, evidence lineage) is complete and clean for all 8 modules — nothing
found requires remediation, and nothing found is a reason to hold. The one open item (roster
membership is DERIVED, not CONFIRMED) is not a Lane A defect; it is the explicit, disclosed,
Boss-authorized condition this entire pilot operates under (MD-18) and is carried forward as a
standing caveat into A1, not treated as a Lane A blocker. This recommendation is Lane A's
recommendation only — it does not itself admit G11 to A1; that transition must still be
recorded as a separate, explicit governed step per this task's acceptance boundary.

## 7. Commit SHA(s)

Lane A Pass-1 evidence commits (already pushed to `claude/awesome-gauss-jw1934`):
`346a749`, `bc81171`, `61b09df`, `b7eb854`, `94ad51d`. Original RESULT submission commit:
`0603fa44`. Remediation commit (§8 below): `943e82e1` (GMVQ evidence-state correction only)
plus the commit introducing this expanded §8/table.

## 8. Independent Review Remediation

- **Defect identified:** PR #72 review comment (`5859366737`, author `scglegacy`, "Independent
  Review") found that §3's original `NOT_FOUND` conclusion for GMVQ Question Bank availability
  was incomplete.
- **Root cause:** §3 originally checked only the canonical `GMVQ/` tree on
  `SMEsPlus`/this working branch. It did not check other open or closed PRs for candidate
  question-bank content, so it missed draft banks that exist only in a different, unmerged PR.
- **Verification performed before correcting:** independently queried
  `pull_request_read(method: get_files)` on PR #71 directly (not taken on the reviewer's word
  alone) — confirmed all 8 `GMVQ_CANDIDATE_ROSTER_NOT_VERIFIED/G11_EVENTS/*_DRAFT.md` paths
  exist in that PR's file list, and independently confirmed PR #71's own state is `closed`,
  `merged: false`.
- **Corrected evidence:** §3 above, now with a full per-module table (existence, artifact path,
  source PR, PR state, merge state, governance status) instead of a single aggregate
  `NOT_FOUND` line.
- **Affected statement:** the original §3 aggregate-`NOT_FOUND` line is superseded by the
  `FOUND_CANDIDATE_UNMERGED / NOT YET ADMITTED TO CANONICAL GMVQ TREE` table; the original
  wording is preserved in this file's git history (commit `0603fa44`), not deleted.
- **Disposition after correction:** **`LANE_A_PASS_RECOMMENDATION` — unchanged.** This was the
  only defect found; every other Lane A-scope check in §1–§5 remains satisfied. Per this
  remediation's own allowed-outcome rule, a question-bank evidence-state correction with no
  other defect does not by itself require downgrading to `LANE_A_REMEDIATION_REQUIRED` or
  `LANE_A_HOLD_RECOMMENDATION`. G11's roster membership remains DERIVED (unchanged, MD-18); A1
  admission is not self-approved by this remediation.
