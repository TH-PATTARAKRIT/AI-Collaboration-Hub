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

| Module | Question Bank status |
|---|---|
| event, event_booth, event_booth_sale, event_crm, event_crm_sale, event_product, event_sale, event_sms | `FOUND_CANDIDATE_UNMERGED / NOT YET ADMITTED TO CANONICAL GMVQ TREE` (all 8; PR #71, closed, unmerged, path prefix `GMVQ_CANDIDATE_ROSTER_NOT_VERIFIED/`) |

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
`346a749`, `bc81171`, `61b09df`, `b7eb854`, `94ad51d`. This RESULT file is committed
separately; see the commit introducing it for its own SHA.
