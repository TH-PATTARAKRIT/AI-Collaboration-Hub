# G01 PLATFORM_BASE — Module `onboarding` — RECONCILIATION (Stage 1)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RECONCILIATION controller (Stage 1 of REC + PROOF; Proof recorded separately) |
| Governed group / module | G01 PLATFORM_BASE / `onboarding` |
| Date | 2026-09-27 (intake 2026-09-27T15:06:49Z) |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/onboarding/`) |
| Question lineage | MVQ bank W1-B09 = **HOLD-LOCAL / FREEZE-INTEGRITY** (freeze hash not reproducible). **MVQ lineage: NOT A3-ELIGIBLE (gate HOLD).** Lineage lens used here = Standard 55 only (W1-STD). |
| Lane B | None exists (search recorded in section 3) |
| Next stage | PROOF → `G01_PROOF/G01_ONBOARDING_PROOF_20260927.md` |
| **Disposition** | **REC COMPLETE — HANDOFF TO PROOF** (26 REC items: 11 MATCH, 9 GAP, 1 CONTRADICTION, 5 UNKNOWN_PENDING_PROOF) |

Format reference: `G01_RECONCILIATION/G01_BUS_REC_20260927.md` and `G01_RESOURCE_REC_20260927.md` (present at intake). Structure and classification rules follow them.

## 2. Intake (immutable inputs, sha256 recorded at intake)

Paths are relative to `99_SMEsPlus_Enterprise_Suite/01_Governance/COMMUNITY19/`.

| Input | Path | sha256 | Check |
|---|---|---|---|
| Lane A | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_ONBOARDING_LANE_A_PASS1_20260927.md` | `c2f11c68f411264a84864064bec52d54dedfa63e1d694a6c54e91952eaf3f651` | Equals the value recorded in the A1 and A2 headers |
| A1 | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_ONBOARDING_A1_PACKAGE_20260927.md` | `50b0f4d675880e20dd64319ba8d904fbe31ac6f60e0e4cfdc0df2959c12271a9` | Equals the value recorded in the A2 header |
| A2 | `A1_SOURCE_EVIDENCE_LANE/G01_A2_REVIEWS/G01_ONBOARDING_A2_REVIEW_20260927.md` | `8f1ab5f7313f49ab16e77725a79dd02c75f4cd24d4a57a46d260cbb899386089` | A2 PASS WITH FINDINGS; 18 claims (16 VERIFIED, 2 PARTIAL: C11, C17); 9 omissions (OM-O01..O09); 10 proof requirements (PR-ONBD-01..10) |
| MVQ bank (not used for lineage) | `GMVQ/G01_PLATFORM_BASE/G01_ONBOARDING_GMVQ_MVQ_40_V1.00_DRAFT.md` | `5725a262ef3e82a8471eb9d9384dd250652c9fbee255aee5f09400aa7f439ae1` | Equals the `FREEZE_W1-B09.json` bank entry, but the manifest `freeze_hash` `f9f50636…5530` does **not** reproduce with the canonical `freeze_batch.py` formula (recomputed `0eecca3c…6614`). This agrees with `QUESTION_GATE_G01_FREEZE_REPLAY_20260927.md`: HOLD-LOCAL. |
| Standard 55 | `GMVQ/G01_PLATFORM_BASE/QUESTION_BANK_STANDARD_55_V2.00.md` | `f6726f111932aecce4432daf3e412d0c9de3291fa45fa8908e9e89ee79cb540d` | Equals the `bank_files` entry in `FREEZE_W1-STD.json` |
| Freeze manifest (STD) | `GMVQ/G01_PLATFORM_BASE/FREEZE_W1-STD.json` | `370b92b43d56a99d6e6e444916356eb56e305fdf6bb86b4c7cd0d885a7ff317d` | `freeze_hash` `c64693eee3957388907637ad028ebdeea6fbeb19a093d1c459c5289f45f5c213` recomputed with the canonical formula — MATCH; `onboarding` is in the module list |

The inputs were only read; none was edited. No git operations were run. Intake hashes are kept in the scratchpad (`intake_sha256.txt`).

## 3. Lane B evidence-pool search (recorded)

- Scope: the whole repository tree (`.git` excluded), 2026-09-27. Log `laneb_search.txt` sha256 `21b8a78d400b23d6da3f2ecdefd7b315143b81f8b6f2b73c9927bd6802d0ce7f` (shared with the `html_builder`, `web_hierarchy` and `web_unsplash` RECs).
- Filename search (`*lane_b*`, `*laneb*`, `*gemini*`, `*evidence_pool*`, `*runtime*`, case-insensitive): 4 hits, all under `03_Architecture/STATE03_MIGRATION_FACTORY/CORE_RESOURCE_*`. Each has zero whole-word mentions of any of the four modules.
- Content search (files that mention Lane B, Gemini, evidence pool or runtime observation AND name one of the four modules): 22 hits. All are Lane A packets, A1 packages, A2 reviews, other modules' REC files, a GMVQ bank, a QA checkpoint or the REV-A ballot. None is a runtime observation record.
- `MASTER_CONTROLLED_HANDOFF_STATE_20260927.md` records the runtime device as OFFLINE since 2026-09-24T12:53Z.
- **Result: no Lane B runtime evidence exists for `onboarding`.** Lane B column: UNCORROBORATED (runtime-observable, not observed) or NOT_APPLICABLE (static declaration). Nothing is FAIL for lack of Lane B.

## 4. Classification rules applied (same as the BUS / RESOURCE REC references)

| Class | Rule |
|---|---|
| MATCH | A2 VERIFIED the A1 claim on WHAT and WHY/RISK, and A2 did not class it MISSING_REQUIRED_RUNTIME_PROOF (a proof link may still be supplementary) |
| GAP | A2 PARTIAL where the A1 framing is incomplete, or an A2 omission (promoted to a new REC item) |
| CONTRADICTION | A2, citing source, directly negates an A1 statement |
| UNKNOWN_PENDING_PROOF | A2 VERIFIED the source fact, but classed the conclusion MISSING_REQUIRED_RUNTIME_PROOF |

## 5. Reconciliation table

C01–C18 are the A1 claims `A1-G01-ONBD-Cnn`. OM items are A2 omissions promoted to REC items (OM-O05 is the same finding as the C17 PARTIAL and is folded into REC-ONBD-17). The QID column is lineage to Standard 55 by clear topical fit only. **No QID is answered.** MVQ lineage: NOT A3-ELIGIBLE (gate HOLD).

| REC ID | Source item | A1 position (summary) | A2 verdict / correction | REC class | Lane B | Proof link | MODULE+STD-QID lineage |
|---|---|---|---|---|---|---|---|
| REC-ONBD-01 | C01 | Hidden reusable guidance-panel engine; depends on `web` only; ships no panel content | VERIFIED | MATCH | NOT_APPLICABLE | — | onboarding+STD-Q01 |
| REC-ONBD-02 | C02 | Four entities; globally unique route key; ordered panel↔step link; shared steps | VERIFIED; "one word" not enforced (see REC-ONBD-24) | MATCH | NOT_APPLICABLE | — | — (no clear fit) |
| REC-ONBD-03 | C03 | One tracker per (panel\|step, company-or-none); concurrent first creation → uncaught uniqueness violation | VERIFIED; concurrency test is tagged non-standard | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-ONBD-10 | onboarding+STD-Q10, Q44 |
| REC-ONBD-04 | C04 | not_done → just_done only; idempotent; lazy step-progress creation | VERIFIED | MATCH | UNCORROBORATED | — | onboarding+STD-Q06, Q07, Q10 |
| REC-ONBD-05 | C05 | Validation by external reference: three outcomes; missing = quiet | VERIFIED | MATCH | UNCORROBORATED | — | onboarding+STD-Q07 |
| REC-ONBD-06 | C06 | Render read converts just_done → done ("celebrate once"); read path writes | VERIFIED; refinement: consumption crosses panels and companies (REC-ONBD-20) | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-ONBD-01 | onboarding+STD-Q07 |
| REC-ONBD-07 | C07 | Stored panel state only not_done/done; just_done and closed exist only in render output | VERIFIED; refinement: a not-done, not-closed panel has no panel-state key in render output | MATCH | UNCORROBORATED | — | onboarding+STD-Q06 |
| REC-ONBD-08 | C08 | Consolidation runs before the closed check; closed render consumes just_done | VERIFIED | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-ONBD-01 | onboarding+STD-Q07 |
| REC-ONBD-09 | C09 | Adding a step to a completed (even closed) panel makes it not done | VERIFIED; refinement: closed flag untouched, render stays `closed` | MATCH | UNCORROBORATED | — | onboarding+STD-Q07 |
| REC-ONBD-10 | C10 | Close/toggle per tracker; close by missing reference = no-op | VERIFIED; close with no tracker also a silent no-op (REC-ONBD-26) | MATCH | UNCORROBORATED | — | onboarding+STD-Q07 |
| REC-ONBD-11 | C11 | Per-company flag is sticky; "panel scope can only move from global to per-company" | PARTIAL — stickiness holds **only while a company-bearing progress record exists**. With no company tracker (never created, or removed), removing the last per-company step reverts the panel to global. A1's one-way statement is **negated** by A2's source reading | **CONTRADICTION** | UNCORROBORATED | PR-ONBD-04 | onboarding+STD-Q27, Q49 |
| REC-ONBD-12 | C12 | Step scope change deletes all progress; rebuild for the writer's company only | VERIFIED; refinements: refresh runs on every step write; closed flag also discarded (REC-ONBD-25) | MATCH | UNCORROBORATED | — | onboarding+STD-Q27, Q46 |
| REC-ONBD-13 | C13 | Current tracker = context company or none; filter only; co-existence unhandled | VERIFIED; co-existence most likely raises a singleton error (inference) | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-ONBD-07 | onboarding+STD-Q27, Q28 |
| REC-ONBD-14 | C14 | Shared step counts toward both panels | VERIFIED | MATCH | UNCORROBORATED | — | — (no clear fit) |
| REC-ONBD-15 | C15 | System group only; no elevation in module; ordinary users need consumer elevation | VERIFIED; module test comment supports the implication | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-ONBD-03 | onboarding+STD-Q02, Q29 |
| REC-ONBD-16 | C16 (+ CONTRADICTION-ONBD-1) | No routes; field comment and docstring refer to an absent `/onboarding/<route_name>` controller | VERIFIED; CONTRADICTION-ONBD-1 (source-internal: documentation vs module structure) confirmed by A1 and A2 alike | MATCH | NOT_APPLICABLE | (PR-ONBD-08) | onboarding+STD-Q03 |
| REC-ONBD-17 | C17 (+ OM-O05) | Callback names dispatched by the client; step cannot be linked without an open callback | PARTIAL — the rule is checked only when the step-side panel link is written; clearing the callback on a linked step is not re-checked; panel-side linking not established | GAP | UNCORROBORATED | PR-ONBD-06 | onboarding+STD-Q03, Q08 |
| REC-ONBD-18 | C18 | Two technical menus; no cron/config; company deletion cascades (test skipped) | VERIFIED | MATCH | NOT_APPLICABLE | — | onboarding+STD-Q48 |
| REC-ONBD-19 | OM-O01 | (not in A1) | Rendering requires an existing current tracker (single-record assertion); tracker creation is the consumer's job | GAP | UNCORROBORATED | PR-ONBD-09 | onboarding+STD-Q03 |
| REC-ONBD-20 | OM-O02 (+ SF-O01) | (not in A1) | Consolidation acts on shared step trackers: rendering panel A consumes panel B's (and, for global steps, other companies') celebration | GAP | UNCORROBORATED | PR-ONBD-02 | onboarding+STD-Q28 |
| REC-ONBD-21 | OM-O03 | (not in A1) | A panel with zero steps is stored as done as soon as a tracker exists | GAP | UNCORROBORATED | — | onboarding+STD-Q06 |
| REC-ONBD-22 | OM-O04 | (not in A1) | Step-set change recomputes links of **all** trackers using the current company's step progress — cross-company contamination (inference) | GAP | UNCORROBORATED | PR-ONBD-05 | onboarding+STD-Q28, Q46 |
| REC-ONBD-23 | OM-O06 | (not in A1) | Step images served via the generic image URL; non-system viewers depend on framework placeholder/access behaviour | GAP | UNCORROBORATED | — | onboarding+STD-Q39 |
| REC-ONBD-24 | OM-O08 | (not in A1) | Route key "one word" is a label only; only required + unique | GAP | NOT_APPLICABLE | — | onboarding+STD-Q08 |
| REC-ONBD-25 | OM-O07 | (not in A1) | Scope-change rebuild discards the closed/hidden flag, so a hidden panel reappears | GAP | UNCORROBORATED | — | — (no clear fit) |
| REC-ONBD-26 | OM-O09 | (not in A1) | Close/hide before any tracker exists is silently lost | GAP | UNCORROBORATED | — | onboarding+STD-Q09 |

### Counts

| Class | Count | Items |
|---|---|---|
| MATCH | 11 | REC-ONBD-01, 02, 04, 05, 07, 09, 10, 12, 14, 16, 18 |
| GAP | 9 | REC-ONBD-17, 19–26 |
| CONTRADICTION | 1 | REC-ONBD-11 |
| UNKNOWN_PENDING_PROOF | 5 | REC-ONBD-03, 06, 08, 13, 15 |
| **Total** | **26** | 18 A1 claims + 8 A2 omission items |

Lane B column: NOT_APPLICABLE 5 (REC-ONBD-01, 02, 16, 18, 24); UNCORROBORATED 21. FAIL: 0.

## 6. MODULE+STD-QID lineage summary (Standard 55, W1-STD)

Lineage only. Mapped QIDs are **not answered** and carry no coverage meaning.

- **MVQ lineage (W1-B09 bank): NOT A3-ELIGIBLE (gate HOLD).** No MVQ QID is mapped. Mapping resumes only after a canonical GMVQ re-freeze of W1-B09.
- **Mapped STD-QIDs (16 distinct):** Q01, Q02, Q03, Q06, Q07, Q08, Q09, Q10, Q27, Q28, Q29, Q39, Q44, Q46, Q48, Q49. (Q07 carries the most items.)
- REC items with no clear fit: REC-ONBD-02, 14, 25.
- Standard-55 sections B, C, D and F (approval, accounting, tax, inventory) have no topical fit to `onboarding` evidence. This is recorded as no fit, not as an answer.

## 7. Carried forward

- Evidence gaps GAP-1..GAP-5 from A1 remain open. GAP-1 (route owner) and GAP-3 (consumer elevation) are cross-module.
- CRQ-ONBD-1..7 are carried unchanged, with A2 widenings: CRQ-ONBD-1 (cross-panel/company consumption, REC-ONBD-20), CRQ-ONBD-2 (closed-flag loss, REC-ONBD-25), CRQ-ONBD-6 (cross-company recompute, REC-ONBD-22).
- REC-ONBD-11 (CONTRADICTION) must not be resolved in favour of the A1 wording "panel scope can only move from global to per-company" without the PR-ONBD-04 runtime result.
- A2 business findings SF-O02..SF-O05 are carried as context, not as separate REC items.

## 8. Handoff to PROOF

All 10 A2 proof requirements (PR-ONBD-01..10) pass to Proof. Items needing proof: REC-ONBD-03, 06, 08, 11, 13, 15, 17, 19, 20, 22 (supplementary: REC-ONBD-16 via PR-ONBD-08).

## 9. Limitations

- REC reconciles documents; the source re-read is Proof Stage 2.
- No Lane B evidence exists, so nothing here is runtime-corroborated.
- No Formal Coverage claim; no percentages; no QID answered; no bank edited.
- Clean room: neutral WHAT/WHY/RISK summaries; identifiers are evidence pointers only; no code reproduced.
