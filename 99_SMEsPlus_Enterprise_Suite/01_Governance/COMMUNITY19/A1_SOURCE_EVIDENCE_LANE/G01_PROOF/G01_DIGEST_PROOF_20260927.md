# G01 PLATFORM_BASE — Module `digest` — PROOF (Stage 2)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller (Stage 2; Reconciliation recorded separately) |
| Governed group / module | G01 PLATFORM_BASE / `digest` |
| Date | 2026-09-27 |
| Upstream REC | `G01_RECONCILIATION/G01_DIGEST_REC_20260927.md` (27 REC items) |
| Upstream A2 | `G01_A2_REVIEWS/G01_DIGEST_A2_REVIEW_20260927.md` sha256 `324bde08f503ea0261aad8fb87f52794b65a0d3a100a3dee2a9ba1d77d3ef44f` (10 proof requirements PR-DGST-01..10) |
| Upstream A1 / Lane A | sha256 `030442be…fa04ba87` / `d0f6ec30…c62afe` (full values in REC intake) |
| Frozen bank | W1-B03, freeze_hash `1247c218ba4e2e6a57e259427030f4350881da56a5a28c59901a20f8b2d3a5d3` (recomputed MATCH) |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/digest/<path>` |
| Runtime device | OFFLINE (last recorded 2026-09-24T12:53Z, `MASTER_CONTROLLED_HANDOFF_STATE_20260927.md`) |
| Lane B | None exists (search recorded in REC section 3) |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** |

The format reference `G01_PROOF/G01_BASE_AUTOMATION_PROOF_20260927.md` was **not present** at intake.

## 2. Predeclaration

- There are 20 proof cases: 10 SOURCE/CONFIG and 10 RUNTIME, one of each per A2 proof requirement. Expected and fail conditions were fixed in `predeclared_proof_cases.tsv` (sha256 `a6f20632b142c60377ecf4b245e52ee36ebd630e48dc7caf51e000689119fe16`, written 2026-09-27T15:03:45Z, shared with `bus`) before any results were recorded.
- The static predicates are the source-visible preconditions of A2's runtime predictions. The source had been fetched for blob verification before the predeclaration was written; this is disclosed for A3.
- The RUNTIME cases are NOT-EXECUTED because the runtime device is OFFLINE. They are ready to run, and no outcomes have been invented.

## 3. Source retrieval and blob verification

All 17 files in the Lane A pointer table were re-fetched from the anchor on 2026-09-27 and hashed with `git hash-object`. The copies are held in the scratchpad only, and no repository git operations were run. The log is `blobcheck.txt` (sha256 `886c1c1810cbc9dad2f8a50e862840b5cdd5a0fa2aa27a2d19e5e3ab42882eed`).

| Path | Blob (recorded = computed) | Result |
|---|---|---|
| `__manifest__.py` | 6ee68b6fd27c098ee26ff71351af956f9aed6f67 | MATCH |
| `__init__.py` | 7d34c7c054abd3105d5bb41fe9674111e1c27c16 | MATCH |
| `models/__init__.py` | 1882e860af3dc5ffa10af7d15448d6fae4784f15 | MATCH |
| `controllers/__init__.py` | 903b755e71e3d1673e604f1c47e60a45e9181542 | MATCH |
| `models/digest.py` | 3eea1c39f8c5aa53b6eb1a43acc986d7f0ed204c | MATCH |
| `models/digest_tip.py` | 8c0208db9ad28ed2d8fc8f803cf245d75b04e078 | MATCH |
| `models/res_config_settings.py` | 59f13bdff4ec4cafb69c9bd268b35a0cec11da75 | MATCH |
| `models/res_users.py` | 4488455454832441de947a9e8c49eedcc5214fc9 | MATCH |
| `controllers/portal.py` | b0e76145b13ecdbc4b69fd7bdeddcfac66ae5ffc | MATCH |
| `security/ir.model.access.csv` | 49ef355262e6ea7d15eba86ab876f0e072ffedba | MATCH |
| `data/digest_data.xml` | 649268fe3378ae29f32a48159bea7a35dd4aa146 | MATCH |
| `data/digest_tips_data.xml` | 29c504458e102e5e13c6f6b0c817da9ef0e28b16 | MATCH |
| `data/ir_cron_data.xml` | a6c1d0915a54e21f36867bede259f9b46a7436a1 | MATCH |
| `data/res_config_settings_data.xml` | cacc318daf09fbdc42f9fe7de2533d718ec0c931 | MATCH |
| `views/digest_views.xml` | e0dd92c650bcc21b72564d259240f77147a619d1 | MATCH |
| `views/digest_templates.xml` | 9f7ddb754dfa3695cb28695abce41c246f166c9c | MATCH |
| `views/res_config_settings_views.xml` | 0c99862f74e6beeaf0ccb16d3ccf31d53c5cf6c7 | MATCH |

17 of 17 match; there are 0 mismatches.

## 4. Proof cases and results

Evidence cites `path` @ short blob and line ranges in the fetched copy. Summaries are neutral, and no code is reproduced.

| PC | PR / REC | Layer | Preconditions | Steps | Expected | Fail condition | Result | Evidence |
|---|---|---|---|---|---|---|---|---|
| PC-DGST-01 | PR-DGST-01 / REC-DGST-03 | CONFIG | Anchor files blob-verified | Read the manifest data list, the security folder and the ACL rows | No record-rule file is declared or present, and internal users have read access on both digest and tip | Any record rule, or company-restricted read | **PASS** | `__manifest__.py`@6ee68b6f data list (8 files, no rule file); `security/` contains only the ACL file; `security/ir.model.access.csv`@49ef3552 rows 2–5 |
| PC-DGST-02 | PR-DGST-01 | RUNTIME | Isolated multi-company instance. User in company B without ERP-manager rights | Read company-A digest and tip records over RPC | Records are readable | Access is denied or the records are filtered | **NOT-EXECUTED** (runtime device OFFLINE; ready to run) | — |
| PC-DGST-03 | PR-DGST-02 / REC-DGST-04 | SOURCE | Same | Compare the messages-KPI search domain with the users KPI | The messages KPI domain has date, subtype and message-type terms but no company term. The users KPI goes through the company helper. | A company term is present in the messages KPI | **PASS** | `models/digest.py`@3eea1c39 L71–85, L401–438 |
| PC-DGST-04 | PR-DGST-02 | RUNTIME | Recipient has access to companies A and B, with A as default. Comment messages exist on B documents within the window | Send the digest | Record whether B messages are counted | None; the result is recorded either way, and the RISK stands only if they are counted | **NOT-EXECUTED** | — |
| PC-DGST-05 | PR-DGST-03 / REC-DGST-06, 21 | SOURCE | Same | Read the KPI evaluation loop and the helper's fallback value | Evaluation runs as the recipient under the recipient's default company. Only the access-error type is caught. The failing KPI is removed from the list with no label. The helper returns zero when no grouped row exists. | A dropped KPI gets a label or notice, or a broader exception catch exists | **PASS** | `models/digest.py`@3eea1c39 L177, L277–307, L432–435 |
| PC-DGST-06 | PR-DGST-03 | RUNTIME | Recipient 1 has no access to the KPI source model. Recipient 2 has access but a different default company | Send the digest | Recipient 1: KPI absent with no notice. Recipient 2: zero or restricted value | The KPI is shown with a denial label, or an error appears | **NOT-EXECUTED** | — |
| PC-DGST-07 | PR-DGST-04 / REC-DGST-07, 26 | SOURCE | Same | Read the timeframe builder, the compute-parameter serialization and the next-date computation | Window start is the naive UTC current time with the calendar timezone attached, not converted. Windows are rolling offsets. The timezone comes from the recipient's default company calendar. The next date uses the server date. | Conversion to local calendar-day boundaries | **PASS** (effect on serialized query values depends on the framework; see PC-DGST-08) | `models/digest.py`@3eea1c39 L58–69, L277, L367–377, L379–395 |
| PC-DGST-08 | PR-DGST-04 | RUNTIME | Company calendar timezone far from UTC. Records created at a local-day boundary | Send the digest | Windows roll from the send instant | Windows align to local calendar days | **NOT-EXECUTED** | — |
| PC-DGST-09 | PR-DGST-05 / REC-DGST-09, 23 | SOURCE | Same | Read the cron loop, the send routine and mail creation. Search the module for direct sends and savepoints | The cron catches only the mail-delivery exception type. The send routine only creates outgoing, auto-delete mail records and never sends directly. There is no savepoint per digest. The next date is set after the per-recipient loop. | A direct send, a savepoint, or a broader catch | **PASS** | `models/digest.py`@3eea1c39 L140–157, L203–222, L225–232; module-wide search found no direct send or savepoint |
| PC-DGST-10 | PR-DGST-05 | RUNTIME | Isolated instance with no real delivery | Force the caught exception after the first recipient is queued, then rerun the cron | The first recipient gets a duplicate on rerun, and the digest stayed due | No duplicate, or the next date advanced | **NOT-EXECUTED** | — |
| PC-DGST-11 | PR-DGST-06 / REC-DGST-11 | SOURCE/CONFIG | Same | Read the tip field declaration, the tip rendering and the tip ACL | The tip HTML is stored with sanitization off. It is rendered through the render mixin under elevated rights with the template engine, then sanitized. ERP managers have write access on tips. | Sanitization on store, or a non-elevated render | **PASS** | `models/digest_tip.py`@8c0208db L19; `models/digest.py`@3eea1c39 L309–328; `security/ir.model.access.csv`@49ef3552 row 4 |
| PC-DGST-12 | PR-DGST-06 | RUNTIME | ERP manager without system rights. A tip containing a harmless marker expression that shows the execution identity | Send the digest | The expression is evaluated with elevated identity, and the output is sanitized | The expression renders as literal text | **NOT-EXECUTED** | — |
| PC-DGST-13 | PR-DGST-07 / REC-DGST-12 | SOURCE | Same | Read the route declaration and handler, and where the email embeds the link | The route requires auth=user and declares no method restriction or CSRF parameter. The handler checks the ERP-manager group and the value whitelist, then writes to the browsed id with no ownership or company check. The link is embedded in the preferences for daily digests sent to ERP managers. | A method restriction or ownership check exists | **PASS** (framework CSRF behaviour on GET not evidenced) | `controllers/portal.py`@b0e76145 L62–73; `models/digest.py`@3eea1c39 L352–357 |
| PC-DGST-14 | PR-DGST-07 | RUNTIME | Authenticated ERP manager. A digest of another company | Follow a cross-site GET to the periodicity route | Periodicity changes | The request is rejected (CSRF, method or ownership) | **NOT-EXECUTED** | — |
| PC-DGST-15 | PR-DGST-08 / REC-DGST-20 | SOURCE | Same | Trace the company used for subject, header, currency and KPI values. Read the default digest record and auto-subscribe | Subject, header name and currency formatting use the recipient's default company. Company-based KPI values use the digest company. The default digest record sets no company, so it takes the installing context. Auto-subscribe adds non-share users with no company term. | Labels and values come from the same company | **PASS** | `models/digest.py`@3eea1c39 L35, L171, L220, L294–296, L432–435; `data/digest_data.xml`@649268fe L278, L439; `data/digest_tips_data.xml`@29c50445 L4–11; `models/res_users.py`@44884554 (create override) |
| PC-DGST-16 | PR-DGST-08 | RUNTIME | Digest company A. Recipient default company B with a different currency. A monetary KPI present | Send the digest | Subject, header and currency show B; values are computed for A | Labels and values come from the same company | **NOT-EXECUTED** | — |
| PC-DGST-17 | PR-DGST-09 / REC-DGST-22 | SOURCE | Same | Read the email-body unsubscribe link, the legacy route methods, the tokenized branch and token generation | The body link targets the legacy route with token and user id. That route accepts GET and POST. The tokenized branch needs no session. The token has no expiry input. | GET refused on the tokenized path, or an expiry exists | **PASS** | `data/digest_data.xml`@649268fe L403–405; `controllers/portal.py`@b0e76145 L25–56; `models/digest.py`@3eea1c39 L234–240 |
| PC-DGST-18 | PR-DGST-09 | RUNTIME | No session | Send a plain GET to the email unsubscribe link | The recipient is unsubscribed | GET refused, or confirmation required | **NOT-EXECUTED** | — |
| PC-DGST-19 | PR-DGST-10 / REC-DGST-24 | SOURCE | Same | Read the subscribe action and its membership writer | The public action checks internal-user status and non-membership, then writes membership with elevated rights. There is no company check. | A company check is present | **PASS** (RPC reachability not evidenced) | `models/digest.py`@3eea1c39 L103–110 |
| PC-DGST-20 | PR-DGST-10 | RUNTIME | Internal user of company B | Call the subscribe action on company A's digest over RPC | The user is added as a recipient | The call is refused | **NOT-EXECUTED** | — |

### Result totals

| Result | Count | Cases |
|---|---|---|
| PASS | 10 | PC-DGST-01, 03, 05, 07, 09, 11, 13, 15, 17, 19 |
| FAIL | 0 | — |
| NOT-EXECUTED | 10 | PC-DGST-02, 04, 06, 08, 10, 12, 14, 16, 18, 20 (all RUNTIME) |

There are no failures, so none had to be preserved. A static PASS confirms only the source-visible precondition. It is **not** runtime proof of the A2 prediction.

## 5. Effect on REC items

| REC item | Status after Proof |
|---|---|
| REC-DGST-03, 04, 06, 11, 12 (UNKNOWN_PENDING_PROOF) | Source or config preconditions PASS. They remain UNKNOWN_PENDING_PROOF until the RUNTIME cases run. |
| REC-DGST-07, 09 (GAP from A2 PARTIAL) | The A2 correction is confirmed on source (PC-DGST-07, PC-DGST-09). The runtime effect is pending. |
| REC-DGST-20–24, 26 (GAP, A2 omissions with a PR) | Confirmed on source. The runtime effect is pending. |
| REC-DGST-25, 27 (GAP, no PR) | No proof case. The A2 source basis stands, and A3 may challenge it. |

## 6. Runtime pack (ready to run when the device is online)

- Use an authorized, isolated test instance at anchor `8d05257d`, with at least two companies with different currencies and calendar timezones.
- Outgoing mail must be captured (no real delivery). The tip test uses a harmless marker only.
- For each case, record the queued mail records (captured before auto-delete), RPC responses, the digest state before and after, and the user/company context.
- Record FAIL outcomes as observed. Do not re-run a case to obtain a PASS.

## 7. A3 eligibility and challenge surface

**A3 may challenge now:**
1. The REC classifications. This includes the absence of any CONTRADICTION, since REC-DGST-07 (C07 timezone overstatement) is classed GAP rather than CONTRADICTION.
2. The QID lineage mapping: 27 QIDs mapped, 13 with no evidence, and 1 REC item with no fit.
3. The 10 executed SOURCE/CONFIG cases: predicate sufficiency, line citations and blob verification.
4. Predeclaration independence, since the source was fetched before the predeclaration (disclosed in section 2).
5. Clean-room compliance and lineage hashes.
6. The GAP items that have no proof requirement (REC-DGST-25, 27).

**A3 may not treat as proven:** any RUNTIME case outcome (the even-numbered cases PC-DGST-02 to PC-DGST-20). These remain NOT-EXECUTED, and Lane B stays UNCORROBORATED.

## 8. Limitations

- Evidence comes from a single anchor commit. Framework internals were not read: CSRF on GET, record-rule defaults, message visibility, datetime serialization, cron transaction scope, RPC method exposure and ERP-manager group powers.
- Email template bodies were read only for the unsubscribe link and the company fields.
- No runtime execution was performed, and no results were fabricated.
- There is no Formal Coverage claim, no percentages and no QID answered.
- Clean room: summaries are neutral, identifiers and line numbers are evidence pointers, and no code is reproduced.
- Inputs were not edited and no git operations were run. Scratch: `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/rec_bus_dgst`.
