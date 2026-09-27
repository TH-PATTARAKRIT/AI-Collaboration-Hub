# G01 PLATFORM_BASE — Module `resource` — RECONCILIATION (Stage 1)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RECONCILIATION controller (Stage 1 of REC + PROOF; Proof recorded separately) |
| Governed group / module | G01 PLATFORM_BASE / `resource` |
| Date | 2026-09-27 (intake 2026-09-27T15:02Z; Asia/Bangkok 22:02) |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/resource/`) |
| Question lineage | **MVQ lineage unavailable** — no module MVQ bank exists for `resource` (GMVQ backlog). Lineage lens = Standard 55 only (W1-STD). |
| Lane B | None exists (search recorded in section 3) |
| Next stage | PROOF → `G01_PROOF/G01_RESOURCE_PROOF_20260927.md` |
| **Disposition** | **REC COMPLETE — HANDOFF TO PROOF** (28 REC items: 7 MATCH, 11 GAP, 1 CONTRADICTION, 9 UNKNOWN_PENDING_PROOF) |

Format reference: `G01_RECONCILIATION/` and `G01_PROOF/` did not exist at intake (15:02Z). They were created by parallel controllers during this session. This document follows the structure of `G01_RECONCILIATION/G01_BUS_REC_20260927.md` as found at 15:05Z, including its classification rules.

## 2. Intake (immutable inputs; sha256 recorded at intake)

Paths are relative to `99_SMEsPlus_Enterprise_Suite/01_Governance/COMMUNITY19/`.

| Input | Path | sha256 | Check |
|---|---|---|---|
| Lane A | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_RESOURCE_LANE_A_PASS1_20260927.md` | `6148482c3278b841ef5fa5191c8fd9d3dd9b2c87244046d4f1fb6643cd8ceffd` | Equals the value recorded in the A1 and A2 headers |
| A1 | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_RESOURCE_A1_PACKAGE_20260927.md` | `c7f17c210f6f4abca84a26d2f024d774577b56cdfaf0b9febe4d7d1b453a0d7d` | Equals the value recorded in the A2 header |
| A2 | `A1_SOURCE_EVIDENCE_LANE/G01_A2_REVIEWS/G01_RESOURCE_A2_REVIEW_20260927.md` | `23b99cd698b4aa630616e99dba28d4080c5fc8e4e95fc1242f122c6a04b3f4a0` | A2 VERIFIED WITH FINDINGS; 18 claims (16 VERIFIED, 2 PARTIAL: C06, C11); 9 omissions (O-01..O-09); 10 proof requirements (PR-01..PR-10) |
| Standard 55 | `GMVQ/G01_PLATFORM_BASE/QUESTION_BANK_STANDARD_55_V2.00.md` | `f6726f111932aecce4432daf3e412d0c9de3291fa45fa8908e9e89ee79cb540d` | Equals the `bank_files` entry in `FREEZE_W1-STD.json` — MATCH |
| Freeze manifest | `GMVQ/G01_PLATFORM_BASE/FREEZE_W1-STD.json` | `370b92b43d56a99d6e6e444916356eb56e305fdf6bb86b4c7cd0d885a7ff317d` | Internal `freeze_hash` `c64693eee3957388907637ad028ebdeea6fbeb19a093d1c459c5289f45f5c213`, recomputed with the `freeze_batch.py` formula (batch id, sorted modules, sorted file:sha256) — MATCH. `resource` is in the module list. |

The inputs were only read; none was edited. No git operations were run. The sha256 values were re-checked at close and were unchanged.

## 3. Lane B evidence-pool search (recorded)

- Scope: the whole repository tree (`.git` excluded).
- Filename search (`*lane_b*`, `*laneb*`, `*gemini*`, `*evidence_pool*`, `*runtime*`, case-insensitive): 4 hits. All 4 are under `03_Architecture/STATE03_MIGRATION_FACTORY/CORE_RESOURCE_*` and are infrastructure governance drafts, where "resource" means compute resources. None concerns the `resource` module.
- Content search (files that mention Lane B, Gemini, evidence pool or runtime observation and also name `resource_mail`, `resource.calendar` or `resource.resource`): 4 hits. They are the A1 packages for resource/resource_mail, the resource_mail A2 review and the `W1_B04_AUTHORING_QA_CHECKPOINT_20260925.md` roster list. Each either states that Lane B is not consumed or only lists the module. None is a runtime observation record.
- `MASTER_CONTROLLED_HANDOFF_STATE_20260927.md` records the runtime device as OFFLINE since 2026-09-24T12:53Z.
- **Result: no Lane B runtime evidence exists for `resource`.** In the Lane B column, UNCORROBORATED means runtime-observable but not observed. NOT_APPLICABLE means a static declaration. Nothing is marked FAIL for lack of Lane B evidence.

## 4. Classification rules applied (same as the BUS REC reference)

| Class | Rule |
|---|---|
| MATCH | A2 VERIFIED the A1 claim on WHAT and WHY/RISK, and no A2 runtime proof requirement is needed to hold it |
| GAP | A2 PARTIAL where the A1 framing is incomplete, or an A2 omission (promoted to a new REC item) |
| CONTRADICTION | A2 directly contradicts an A1 statement, citing source |
| UNKNOWN_PENDING_PROOF | A2 VERIFIED the source fact, but the conclusion is behavioural or security-related and A2 requires runtime proof |

## 5. Reconciliation table

C01–C18 are the A1 claims `A1-G01-RSRC-Cnn`. OM items are A2 omissions or partial corrections promoted to REC items. The QID column is lineage mapping to Standard 55 by clear topical fit only. **No QID is answered.**

| REC ID | Source item | A1 position (summary) | A2 verdict / correction | REC class | Lane B | Proof link | MODULE+STD-QID lineage |
|---|---|---|---|---|---|---|---|
| REC-RSRC-01 | C01 | No company rule on calendars or attendances; scoping by selection domain only; tenant effect LOW (G3) | VERIFIED; leave calendar company flag is domain-level only | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-01 → PC-RSRC-01, R01 | resource+STD-Q27, Q28, Q49 |
| REC-RSRC-02 | C02 (+ A2 F-01 CANDIDATE) | Resource read-only for user and system admin; grant source unknown (G2) | VERIFIED; F-01: admin menu and multi-edit list exist, but no write grant in the module (CANDIDATE across modules) | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-02 → PC-RSRC-02, R02 | resource+STD-Q02, Q29 |
| REC-RSRC-03 | C03 | Calendar/attendance read-only for users, full for system; leaves full, narrowed by rules | VERIFIED | MATCH | NOT_APPLICABLE | PC-RSRC-02 | resource+STD-Q29 |
| REC-RSRC-04 | C04 | Any internal user can create/write/delete leaves of resources with no linked user | VERIFIED (union of group rules) | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-03 → PC-RSRC-03, R03 | resource+STD-Q29 |
| REC-RSRC-05 | C05 | Hour order and range enforced only by form onchange; no server constraint | VERIFIED; see OM-05 | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-04 → PC-RSRC-04, R04 | resource+STD-Q08, Q54 |
| REC-RSRC-06 | C06 | Overlap per weekday with micro offset; "two-week calendars require every slot under a week section" | PARTIAL — the overlap mechanism is verified; the section requirement is **contradicted**: the check fails only when sections exist and the first row is not a section, so a two-week calendar with no sections passes | **CONTRADICTION** | NOT_APPLICABLE | PC-RSRC-06 | resource+STD-Q08 |
| REC-RSRC-07 | C07 | Planning helpers: 14-day × 100 windows, silent false; leaves off by default | VERIFIED; plan-days takes no resource (see OM-10) | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-05 → PC-RSRC-07, R05 | — (no clear fit) |
| REC-RSRC-08 | C08 | Work-time rate unbounded vs 0–100 % help (source-internal contradiction) | VERIFIED; contradiction CONFIRMED-FROM-SOURCE (A1 and A2 agree); see OM-06 | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-06 → PC-RSRC-08, R06 | — (no clear fit) |
| REC-RSRC-09 | C09 | Naive input read as UTC; localization per timezone group; DST effect LOW | VERIFIED; tz argument overrides every resource tz; see OM-07 | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-07 → PC-RSRC-09, PC-RSRC-10 (Thailand), R07 | resource+STD-Q50 |
| REC-RSRC-10 | C10 | Displayed tz offset computed from today, not the scheduled date | VERIFIED; display only | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-07 → PC-RSRC-11, R07 | resource+STD-Q50 |
| REC-RSRC-11 | C11 | Company-wide leaves apply on the matching calendar when the company matches; time-type default; caller domain | PARTIAL — stated rules verified; omitted nuances promoted as OM-02, OM-03, OM-04 | GAP | UNCORROBORATED | PC-RSRC-12 | resource+STD-Q27, Q49 |
| REC-RSRC-12 | C12 | Leave start ≤ end; company computed from calendar, else current company | VERIFIED; business effect in OM-08 | MATCH | NOT_APPLICABLE | PC-RSRC-13 | resource+STD-Q08 |
| REC-RSRC-13 | C13 | Efficiency > 0; no calendar = fully flexible; same-company calendar | VERIFIED; the same-company restriction is a selection domain only (no server check) | MATCH | NOT_APPLICABLE | PC-RSRC-14 | resource+STD-Q05, Q08 |
| REC-RSRC-14 | C14 | Week parity from an epoch day count, not the ISO week | VERIFIED | MATCH | NOT_APPLICABLE | PC-RSRC-15 | — (no clear fit) |
| REC-RSRC-15 | C15 | Mixin resource required, delete restricted, searches bypass resource access | VERIFIED | MATCH | NOT_APPLICABLE | PC-RSRC-16 | resource+STD-Q36, Q37 |
| REC-RSRC-16 | C16 | Every company gets a default calendar; a default in use cannot be deleted | VERIFIED (A2 read the content; A1 had not spot-checked it); see OM-09 | MATCH | NOT_APPLICABLE | PC-RSRC-17 | resource+STD-Q46 |
| REC-RSRC-17 | C17 | Weekday lookup cached per calendar; no invalidation seen | VERIFIED (absence in module files); staleness is runtime | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-08 → PC-RSRC-18, R08 | — (no clear fit) |
| REC-RSRC-18 | C18 | Timezone default chain; resource tz from user, else calendar; admin first-login copy | VERIFIED | MATCH | NOT_APPLICABLE | PC-RSRC-19 | resource+STD-Q46, Q50 |
| REC-RSRC-19 | OM-01 (A2 C06 PARTIAL) | (not in A1) | A two-week calendar **without week sections** passes the section check. In two-week mode the overlap check covers only rows typed first or second week, so a row with no week type **skips the overlap check** | GAP | NOT_APPLICABLE | PC-RSRC-06 | resource+STD-Q08, Q54 |
| REC-RSRC-20 | OM-02 (A2 O-01) | (in Lane A #18; dropped by A1) | **Leaves with no calendar apply to every calendar** | GAP | UNCORROBORATED | PC-RSRC-12 | resource+STD-Q27, Q49 |
| REC-RSRC-21 | OM-03 (A2 O-02) | (not in A1) | **Resources with no company never receive company-wide leaves**, because a leave's company is always populated | GAP | UNCORROBORATED | PR-10 → PC-RSRC-12, R10 | resource+STD-Q27 |
| REC-RSRC-22 | OM-04 (A2 O-03 / F-06) | (not in A1) | **Leave and attendance lookups run under the caller's access rights** (no elevation), so results depend on the caller | GAP | UNCORROBORATED | PR-09 → PC-RSRC-12, R09 | resource+STD-Q29, Q38 |
| REC-RSRC-23 | OM-05 (A2 O-04 / F-03) | (not in A1; A1 C05 cited import/RPC only) | In **duration-based calendars the duration inverse stores out-of-range hours** (negative start, end > 24) on a normal form save | GAP | UNCORROBORATED | PR-04 → PC-RSRC-05, R04 | resource+STD-Q08, Q54 |
| REC-RSRC-24 | OM-06 (A2 O-05 / F-04) | (not in A1) | Full-time reference hours are overwritten when hours change; shared (company-less) calendars get no computed reference, so the rate falls back to 100 | GAP | UNCORROBORATED | PR-06 → PC-RSRC-08, R06 | resource+STD-Q49 |
| REC-RSRC-25 | OM-07 (A2 O-06 / F-05) | (not in A1) | The **planning/forecast unavailable-interval helper forces the calendar timezone** on all resources of that calendar | GAP | UNCORROBORATED | PR-07 → PC-RSRC-20, R07 | resource+STD-Q50 |
| REC-RSRC-26 | OM-08 (A2 O-07 / F-07) | (not in A1) | A **company-wide leave with no company-owned calendar takes the creator's active company** | GAP | UNCORROBORATED | PR-10 → PC-RSRC-13, R10 | resource+STD-Q41, Q46 |
| REC-RSRC-27 | OM-09 (A2 O-08 / F-08 / F-09) | (not in A1; A1 §3 understated the mode toggles) | **Company holidays are copied once** into a new calendar (a snapshot; later holidays do not propagate). Turning duration-based or two-week mode off deletes all slots and reloads the company defaults | GAP | UNCORROBORATED | PC-RSRC-17, PC-RSRC-21 | resource+STD-Q04, Q46, Q47 |
| REC-RSRC-28 | OM-10 (A2 O-09 / F-02) | (not in A1) | The system-admin group is not exempt from leave rules (other users' personal leaves cannot be modified inside this module). Plan-days has no resource parameter, so it sees only calendar-level leaves | GAP | UNCORROBORATED | PC-RSRC-03, PC-RSRC-07 | resource+STD-Q29 |

### Counts

| Class | Count | Items |
|---|---|---|
| MATCH | 7 | REC-RSRC-03, 12, 13, 14, 15, 16, 18 |
| GAP | 11 | REC-RSRC-11, 19–28 |
| CONTRADICTION | 1 | REC-RSRC-06 |
| UNKNOWN_PENDING_PROOF | 9 | REC-RSRC-01, 02, 04, 05, 07, 08, 09, 10, 17 |
| **Total** | **28** | 18 A1 claims + 10 A2 omission/partial items |

Lane B column: NOT_APPLICABLE 9 (REC-RSRC-03, 06, 12, 13, 14, 15, 16, 18, 19) and UNCORROBORATED 19. FAIL: 0.

## 6. MODULE+STD-QID lineage summary (Standard 55, W1-STD)

This is lineage only. The mapped QIDs are **not answered** and carry no coverage meaning. **MVQ lineage unavailable** (no `resource` module bank; GMVQ backlog), so A3 challenge at QID level is limited to Standard 55.

- **Mapped (16 distinct STD-QIDs):** Q02, Q04, Q05, Q08, Q27, Q28, Q29, Q36, Q37, Q38, Q41, Q46, Q47, Q49, Q50, Q54. Q08, Q27, Q29 and Q46 carry the most items.
- REC items with no clear fit: REC-RSRC-07, 08, 14, 17.
- Standard-55 sections B, C, D and F (Q11–Q26, Q31–Q35: approval, accounting, tax, inventory) have no topical fit to `resource` evidence. This is recorded as no fit, not as an answer.

## 7. Carried forward

- A1 evidence gaps G1–G7 remain open. G2 (resource write-grant source) and G3 (calendar company rule in other modules) are cross-module and cannot be closed inside `resource`.
- The CRQ candidates CRQ-RSRC-01..08 are carried unchanged.
- The source-internal contradiction on the rate help (C08) is kept as recorded by A1/A2. It is classed UNKNOWN_PENDING_PROOF for consumer effect, not as an A1-vs-A2 contradiction.
- REC-RSRC-06 (CONTRADICTION) must not be resolved in favour of the A1 wording "require every slot under a week section".
- A2 Thailand note carried forward: Asia/Bangkok has no DST, so the DST risk in C09/C10 is not material for Thai-only tenants. The naive-as-UTC rule is material (7-hour shift); see PC-RSRC-10.

## 8. Handoff to PROOF

All 10 A2 proof requirements (PR-01..PR-10) pass to Proof as runtime cases PC-RSRC-R01..R10. Static cases PC-RSRC-01..21 cover the source basis of every REC item.

## 9. Limitations

- REC reconciles documents. The source re-read is Proof Stage 2.
- No Lane B evidence exists, so nothing here is runtime-corroborated.
- There is no Formal Coverage claim and no percentages. No QID is answered and the bank was not edited.
- Clean room: neutral WHAT/WHY/RISK summaries. Identifiers are evidence pointers only, and no code is reproduced.
