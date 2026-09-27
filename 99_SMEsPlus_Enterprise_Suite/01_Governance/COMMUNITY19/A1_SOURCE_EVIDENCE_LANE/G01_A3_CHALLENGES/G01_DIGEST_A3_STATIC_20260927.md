# G01 PLATFORM_BASE — RED TEAM A3 Independent Challenge (STATIC scope) — `digest`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3, the independent adversarial challenger |
| Independence statement | This A3 reviewer did not author Lane A, A1, A2, REC or PROOF for `digest` or `bus`. The goal was to disprove the upstream conclusions, not confirm them. A3 re-fetched the source and read it directly instead of relying on upstream paraphrase. No upstream artifact was edited. The Limitations section notes shared session infrastructure. |
| Group / Module | G01 PLATFORM_BASE / `digest` |
| Date | 2026-09-27 |
| Scope | STATIC only. Runtime cases PC-DGST-02, 04, 06, 08, 10, 12, 14, 16, 18 and 20 are **NOT-EXECUTED** because the runtime device is offline. They are not treated as passed or failed. |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/digest/`. A3 re-fetched all 17 files in the Lane A pointer table into scratchpad `a3_bus_dgst/src/digest/`. `git hash-object` equals the recorded blob for **17 of 17** files. Probes for `security/digest_security.xml` and `security/ir_rule.xml` returned 404, which matches the manifest data list (no record-rule file). |
| **Overall disposition** | **A3 STATIC PASS WITH DEFECTS (route to REC, A2, PROOF)**. No A1 WHAT claim was refuted. All four named challenge themes hold on source: GET unsubscribe/periodicity, the company mismatch between labels/currency and KPIs, and the default digest collecting users from every company. The defects are in proof coverage, labels, lineage and proof-case specification. MASTER handoff also stays **pending runtime**. |

### 0.1 Lineage hashes (sha256), intake and exit

Paths are relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`.

| Input | sha256 at intake | sha256 at exit | Git lineage (read-only) |
|---|---|---|---|
| Lane A `G01_LANE_A_PASS1/G01_DIGEST_LANE_A_PASS1_20260927.md` | `d0f6ec30b0823ac82a20e0ae2b9b8261732d81383b2124a880becb3c49c62afe` | identical | 1 commit `7fab4ed` 14:48:28Z; committed blob = disk |
| A1 `G01_A1_PACKAGES/G01_DIGEST_A1_PACKAGE_20260927.md` | `030442be4f9ccd83f2f988e4299749fafcf76a6954a794f2948337c7fa04ba87` | identical | 1 commit `07cca3c` 14:51:32Z; = disk |
| A2 `G01_A2_REVIEWS/G01_DIGEST_A2_REVIEW_20260927.md` | `324bde08f503ea0261aad8fb87f52794b65a0d3a100a3dee2a9ba1d77d3ef44f` | identical | 1 commit `0a5fdbf` 14:58:26Z (in-flight checkpoint); = disk |
| REC `G01_RECONCILIATION/G01_DIGEST_REC_20260927.md` | `6744994d045efe9306665256b9d437f73ed0e7720d8e88302d6032c4c4192ee5` | identical | 1 commit `209f3b1` 15:06:34Z (commit timing only; file mtime 15:05:26Z); = disk |
| PROOF `G01_PROOF/G01_DIGEST_PROOF_20260927.md` | `279e573c6484edf6387847394fa76377c49d48bc5503d5089a350c0008f7bec4` | identical | 1 commit `3215ebe` 15:08:44Z; = disk |
| Bank `../GMVQ/G01_PLATFORM_BASE/G01_DIGEST_GMVQ_MVQ_40_V1.00_DRAFT.md` | `1ba4226db5739143130e0afc1757e3aaa3c0cf1f934ccf3349a907d0c64d74ec` | identical | equals the `FREEZE_W1-B03.json` bank_files entry |
| Freeze `../GMVQ/G01_PLATFORM_BASE/FREEZE_W1-B03.json` | `74ba2caeaf9a4450ff126256df5e1a7b8bdd4018b2907248b9ccec0e5bbb565e` | identical | A3 recomputed freeze_hash `1247c218…a5d3` with the `freeze_batch.py` formula: MATCH. All 4 bank_files hashes equal disk. |
| Proof predeclaration (scratch) `rec_bus_dgst/predeclared_proof_cases.tsv` | `a6f20632b142c60377ecf4b245e52ee36ebd630e48dc7caf51e000689119fe16` (equals the Proof header) | identical | not committed; mtime 15:03:45Z; shared with `bus` |
| Proof blob log (scratch) `rec_bus_dgst/blobcheck.txt` | `886c1c1810cbc9dad2f8a50e862840b5cdd5a0fa2aa27a2d19e5e3ab42882eed` (equals the Proof header) | identical | mtime 15:00:38Z |

No input was modified after handoff. Every file has one commit, and each committed blob equals the file on disk.

## 1. Challenge log

Dispositions: **UPHELD** means the upstream conclusion survived. **CHALLENGE-SUSTAINED** means a defect exists, and the owner stage is named. **INCONCLUSIVE** means it cannot be decided statically.

### 1.1 Challenge 1: independent re-derivation of REC items from source (10 items)

| # | REC item (class) | A3 attempt to refute | A3 finding (source pointer @ anchor) | Disposition |
|---|---|---|---|---|
| 1.1 | REC-DGST-22 (GAP): GET-capable tokenized unsubscribe in the email body | Look for a GET guard, a confirmation step or token expiry | The body link targets `/digest/<id>/unsubscribe` with token and user id (`data/digest_data.xml` L403–405). That route accepts GET and POST (`controllers/portal.py` L25). The method guard only applies to the deprecated `one_click` flag (L41–42). With a valid token, the unsubscribe runs under sudo **before** the confirmation page is rendered (L47–51, L58). The token is an HMAC over (digest id, user id) with a fixed scope and no time input (`models/digest.py` L234–240). The `List-Unsubscribe` header, by contrast, points to the POST-only route (L199–216). Confirmed. | **UPHELD** |
| 1.2 | REC-DGST-12 (UNKNOWN_PENDING_PROOF): periodicity change via GET | Look for a method restriction, CSRF parameter or ownership check | The route declares no methods and no csrf argument (`controllers/portal.py` L62). It checks the ERP-manager group and the value whitelist, then writes on a non-sudo browse with no ownership or company check (L63–73). The only record-level barrier would be record rules, and none ship. Framework CSRF behavior for GET was not read, so the effect stays pending. | **UPHELD** |
| 1.3 | REC-DGST-20 (GAP): subject and currency company vs KPI company | Look for a path where labels and values share one company | Rendering passes `user.company_id` as `company` for the header, layout, subject and currency (`models/digest.py` L171, L190, L220, L277–296). Company-based KPI values filter on `digest.company_id`, falling back to the env company only when it is unset (L58–69, L413–435). Evaluation uses `with_company(user.company_id)` (L278–279). Confirmed on source. **A3 refinement:** because evaluation narrows to the recipient's company, a digest-company KPI will likely come out as zero by record rule rather than "computed for A". A2 itself says this in SF-D02/OM-D02, but PR-DGST-08 predicts "values computed for A" (see D-DGST-04). | **UPHELD** (fact) / proof-spec defect → D-DGST-04 |
| 1.4 | REC-DGST-20 / C18: default digest collects users from every company | Look for a company term in auto-subscribe or a company-scoped default digest | The seeded default digest sets no company (`data/digest_tips_data.xml` L4–11), so the field default takes the installing env company (`models/digest.py` L35). On user creation, every non-share user is added when both config params are set (`models/res_users.py`), with no company term. The params are seeded on (`data/res_config_settings_data.xml`, noupdate). Confirmed. | **UPHELD** |
| 1.5 | REC-DGST-04 (UNKNOWN_PENDING_PROOF): messages KPI has no company filter | Look for any company term | The domain has date, comment subtype and three message types only (`models/digest.py` L78–85). Evaluation runs as the recipient with the company narrowed (L278), so the effective boundary is framework message visibility. Confirmed. | **UPHELD** |
| 1.6 | REC-DGST-06 (UNKNOWN_PENDING_PROOF): silent KPI drop | Look for a label, a notice or a broader catch | Only `AccessError` is caught, and the KPI is filtered out with no marker (L283–292, L306–307). The company helper returns 0 when no grouped row exists (L432–435). Confirmed. | **UPHELD** |
| 1.7 | REC-DGST-07 / 26 (GAP): timezone and cutoff | Test whether GAP should be CONTRADICTION | The window start is naive UTC "now" with the calendar tz attached via `localize`, not converted (L379–383). The windows are rolling offsets (L384–395). The tz comes from the recipient company (L277). The next date uses server `date.today()` (L367–377). A1's word "localized" mirrors the call the source makes, so the A1 wording is not literally false, and GAP is defensible. A3 adds: if the framework's datetime-to-string serialization drops tzinfo, which was not read, the tz handling does nothing at all. That strengthens the GAP but cannot be settled statically. | **UPHELD** (GAP); magnitude **INCONCLUSIVE** pending PC-DGST-08 |
| 1.8 | REC-DGST-09 / 23 (GAP): failure handling | Look for a direct send, a savepoint or a wider catch | The cron catches only `MailDeliveryException` (L225–232). The send path only creates `mail.mail` records with state outgoing and auto-delete (L203–222). A3 found no direct send and no savepoint anywhere in the module. The next date is set after the recipient loop (L149–157). **A3 addition:** the caught exception type therefore cannot normally be raised by the module's own path, so the catch is effectively unreachable. PC-DGST-10 can only be run with fault injection, and the runtime pack does not say so (D-DGST-04). | **UPHELD** |
| 1.9 | REC-DGST-24 (GAP): self-subscribe with sudo and no company check | Look for a company or authority check | `action_subscribe` checks internal status and non-membership, then writes membership under sudo (L103–110). No company check. RPC reachability is framework-dependent. | **UPHELD** |
| 1.10 | REC-DGST-27 (GAP, no PR): recipients who later become share users | Look for a send-time share filter or a cleanup hook | `_action_send` iterates every `user_ids` with no share or active filter (L149–154). The module's only users extension is the create override (`models/res_users.py`). The recipient domain is a field-level UI domain (L27). Confirmed. This is material: it is an external-user delivery path (see 1.7). | **UPHELD** (fact) → D-DGST-01 |

Also re-checked and **UPHELD**: C02 ACL rows, C10 (slowdown only when `update_periodicity`, L130–147), C11 (tip HTML `sanitize=False` in `digest_tip.py`; sudo qweb render then sanitize at L309–328), C15 (buttons/sections `groups=base.group_system`, menus `base.group_erp_manager` in `digest_views.xml`), C17 (subject/sender/auto-delete at L203–222), and C13 (POST-only, csrf=False, consteq at `portal.py` L14–22, L47–50).

### 1.2 Challenge 2: static PASS cases re-executed (8 of 10)

| PC | A3 re-execution | Citation check | Predicate strength | Disposition |
|---|---|---|---|---|
| PC-DGST-01 | Reproduced (8 data files, no rule file, ACL rows 2–5) | accurate | Adequate | **UPHELD** |
| PC-DGST-03 | Reproduced | L71–85, L401–438 accurate | Adequate | **UPHELD** |
| PC-DGST-05 | Reproduced | L177, L277–307, L432–435 accurate | Adequate | **UPHELD** |
| PC-DGST-07 | Reproduced | L58–69, L277, L367–377, L379–395 accurate | Adequate | **UPHELD** |
| PC-DGST-09 | Reproduced (no savepoint or direct send in the module) | accurate | Adequate; it does not state that the caught path is effectively unreachable | **UPHELD** |
| PC-DGST-13 | Reproduced | `portal.py` L62–73, `digest.py` L352–357 accurate | Adequate | **UPHELD** |
| PC-DGST-15 | Reproduced | `digest.py` L35/171/220/294–296/432–435; `digest_data.xml` L278, L439; `digest_tips_data.xml` L4–11 accurate | Adequate | **UPHELD** |
| PC-DGST-17 | Reproduced | `digest_data.xml` L403–405; `portal.py` L25–56; `digest.py` L234–240 accurate | Adequate | **UPHELD** |

Weak or unfalsifiable expected-fail conditions (runtime, not executed):
- **PC-DGST-04** has no fail condition ("recorded either way"). It is a measurement, not a proof case, and cannot count as proof of REC-DGST-04 in either direction.
- **PC-DGST-16** expects "values computed for A". This conflicts with A2's own SF-D02/OM-D02 (zero by record rule under `with_company(B)`). A runtime zero could be misread as FAIL, or as "labels and values from the same company". The expectation should be disjunctive.
- **PC-DGST-10** cannot happen without fault injection because the caught exception is not raised on the module's queue-only path. The procedure must say that injection is part of the harness.

### 1.3 Challenge 3: predeclaration integrity (disclosed deviation: source fetched before cases were written)

Timeline from scratch mtimes: source fetch 15:00:34–15:00:38Z, `blobcheck.txt` 15:00:38Z, predeclaration TSV 15:03:45Z, digest REC 15:05:26Z, digest Proof 15:07:47Z.

- **Shaping to observed results: not found.** Each static EXPECTED/FAIL_IF in the TSV traces to A2 text committed before the fetch (14:58:26Z). Examples: PC-DGST-07 comes from the A2 C07 basis ("attaches … without converting"; "rolling offsets"), PC-DGST-09 from the A2 C09 basis, PC-DGST-15 from OM-D01, PC-DGST-17 from OM-D03 ("no expiry"), and PC-DGST-19 from OM-D05. No predicate introduces a fact that appears only in source. The deviation is **not material**. → **UPHELD**
- **Structural weakness:** the predicates only confirm A2. None tests a refuting alternative. For example, no case checks whether the caught exception is reachable, or whether the PC-DGST-16 expectation agrees with SF-D02.
- **Post-predeclaration edits:** the Proof document's Expected text goes beyond the TSV. PC-DGST-05 adds "the helper returns zero when no grouped row exists", which supports REC-DGST-21. PC-DGST-13 adds "declares no … CSRF parameter". Fail conditions are unchanged, and no verdict depends on the additions, but they are not marked. → **CHALLENGE-SUSTAINED (minor, PROOF)** → D-DGST-05
- **Sequencing:** REC was written (15:05:26Z) after the same controller had fetched source, while REC says it "re-reads no source". A3 found no REC content absent from A2. → **INCONCLUSIVE** (observation only)

### 1.4 Challenge 4: overclaim check

| Item | Text | A3 finding | Disposition |
|---|---|---|---|
| A2 OM-D03 / REC-DGST-22 | "a link scanner or prefetcher can unsubscribe the recipient" | The mechanism is source-visible: a GET executes the unsubscribe before rendering. Whether scanners actually fetch it is environmental, and PR-DGST-09 is linked. The modal wording is acceptable. | **UPHELD** |
| A2 OM-D05 | "an internal user could join any company's digest" | Qualified in the same sentence ("reachability via RPC is runtime"), and PR-DGST-10 is linked | **UPHELD** |
| A1 C09 | "one failing digest of a non-mail type can abort remaining digests in that run" | A2 correctly marked the uncaught effect as framework-dependent (rollback of the whole run vs abort). The A1 RISK is stated with "can". | **UPHELD** (A2 correction stands) |
| A1 C12 | CSRF effect | A1 marked it LOW / framework and A2 did not assert it | **UPHELD** |
| Proof §4–5 | Static PASS "is **not** runtime proof" | Scoped correctly | **UPHELD** |

### 1.5 Challenge 5: Lane B use and labels

- A3 searched independently and found no Lane B, Gemini or evidence-pool record for `digest`. No stage used Lane B, and none marked FAIL for its absence. → **UPHELD**
- **Label collapse:** REC §3 shows A2's MISSING_REQUIRED_RUNTIME_PROOF as UNCORROBORATED for 7 items (C03, C04, C06, C07, C09, C11, C12 → REC-DGST-03, 04, 06, 07, 09, 11, 12). The proof link keeps the requirement, but the Lane B column loses the distinction. → **CHALLENGE-SUSTAINED (REC)** → D-DGST-02

### 1.6 Challenge 6: QID lineage

- Bank sha256 equals the freeze entry. A3 recomputed the freeze hash and it matches. The bank has 40 QIDs. REC arithmetic checks out: the table QIDs equal "Mapped (27)", and mapped ∪ no-evidence = Q001–Q040 with no overlap. → **UPHELD**
- No QID is answered in any of the 5 artifacts. → **UPHELD**
- Topical fit, 8 sampled: REC-DGST-02→Q028 fits. REC-DGST-04→Q002/Q005/Q006/Q031 fits. REC-DGST-06→Q001/Q008/Q016/Q038 fits. REC-DGST-13→Q012/Q033 fits. REC-DGST-17→Q027 fits. REC-DGST-20→Q002/Q005/Q029/Q030 fits. REC-DGST-27→Q011/Q035 fits. REC-DGST-12→Q019 is weak: the route changes periodicity but does not recompute the next date, so there is no backfill mechanism to relate it to. → **UPHELD** with one weak fit
- **The "No evidence yet" list is inaccurate:**
  - **Q015** (summary includes protected detail denied in-app). C06 (evaluation with recipient rights plus a silent drop) and C04 (messages KPI with no company term) are direct upstream evidence.
  - **Q007** (cached values after access loss). Lane A #4 shows KPI values are non-stored computes, and source L284–289 invalidates the cache per window, so upstream evidence of no persisted cache exists.
  - **Q032** is partially covered: C18 (auto-subscribe happens only at user creation) and the static recipient list are relevant.
  - → **CHALLENGE-SUSTAINED (REC)** → D-DGST-03

### 1.7 Challenge 7: GAP items with no proof requirement

| REC | Material enough to need proof? | Disposition |
|---|---|---|
| REC-DGST-27 (recipients later made share/portal users stay recipients) | **Yes.** Internal KPI digests, company name and digest name would go to an external (share) user. Delivery is not filtered by share status at send time (1.1 row 1.10). It maps to Q011/Q035, and a runtime check is needed: convert a recipient to share, run the scheduler, and inspect the queued mail. | **CHALLENGE-SUSTAINED** (REC; A2 raised no PR) → D-DGST-01 |
| REC-DGST-25 (connected-users margin is based on last login) | No. It is a business-meaning finding, and the static basis is enough. | UPHELD |

### 1.8 Challenge 8: clean-room scan (all 5 `digest` artifacts)

- There are no code blocks, domains, XML records or decorators. Identifiers appear only as evidence pointers. There are no coverage percentages (the "percentage margin" wording describes source behavior only) and no Formal Coverage claim. No verbatim source comments longer than a few words appear. → **UPHELD**

## 2. Defects routed

| ID | Owner stage(s) | Defect | Required action |
|---|---|---|---|
| D-DGST-01 | REC (A2 for PR) | REC-DGST-27 is a material external-recipient path with no proof requirement. | Add a PR/PC: a recipient converted to share status is still queued a digest by the scheduler. |
| D-DGST-02 | REC | Lane B label collapse: MISSING_REQUIRED_RUNTIME_PROOF shown as UNCORROBORATED for 7 items. | Restore A2's label in the Lane B column. |
| D-DGST-03 | REC | QID "no evidence" list is wrong for Q015 and Q007, and partially for Q032. | Correct the lineage lists. They remain lineage only, with no answers. |
| D-DGST-04 | A2 (PR-DGST-05, PR-DGST-08), PROOF (PC-DGST-10, PC-DGST-16) | PC-DGST-16's expectation contradicts A2's own zero-by-rule analysis. PC-DGST-10 needs fault injection that is not declared, because the caught exception is effectively unreachable on the module's queue-only path. | Make the PC-DGST-16 expectation disjunctive: values for A, or zero by rule, with labels B in both cases. Declare fault injection in PC-DGST-10. Record the unreachable catch as a finding under REC-DGST-09. |
| D-DGST-05 | PROOF | The Proof document's Expected text for PC-DGST-05 and PC-DGST-13, among others, goes beyond the predeclared TSV and is not marked. | Mark the text as post-predeclaration, or restore the TSV text. Verdicts are unaffected. |

No defect reverses an A1 WHAT claim or a REC class, and none rises to A3 FAIL.

## 3. Runtime-blocked items (NOT-EXECUTED; neither passed nor failed)

| PC | Linked REC | A3 note for runtime pack |
|---|---|---|
| PC-DGST-02 | REC-DGST-03 | As written |
| PC-DGST-04 | REC-DGST-04 | Measurement only; no pass/fail meaning |
| PC-DGST-06 | REC-DGST-06/21 | As written |
| PC-DGST-08 | REC-DGST-07/26 | Also record the serialized window strings, which settles whether tz handling does anything (1.1 row 1.7) |
| PC-DGST-10 | REC-DGST-09/23 | Declare fault injection (D-DGST-04) |
| PC-DGST-12 | REC-DGST-11 | As written (harmless marker only) |
| PC-DGST-14 | REC-DGST-12 | As written |
| PC-DGST-16 | REC-DGST-20 | Make the expectation disjunctive (D-DGST-04) |
| PC-DGST-18 | REC-DGST-22 | As written |
| PC-DGST-20 | REC-DGST-24 | As written |
| (new) | REC-DGST-27 | Needs PR/PC (D-DGST-01) |

Lane B stays UNCORROBORATED for every runtime-observable item. A3 treats no runtime prediction as proven.

## 4. Limitations

- Static only, on a single anchor commit. Framework internals were not read: CSRF on GET, record-rule defaults, `with_company` allowed-company semantics, message visibility, datetime serialization, cron transaction scope, RPC method exposure, and x2many domain enforcement. Conclusions that depend on them are marked.
- The GitHub directory-listing API was unavailable in this session. File-inventory completeness rests on the manifest, import lists and targeted 404 probes. Email template bodies were read only for company, currency and unsubscribe usage.
- Independence note: A3 is a separate role instance and authored no upstream stage. It does run under the same parent session infrastructure as the upstream controllers (shared scratchpad root), so independence is at the role level, not the infrastructure level.
- No percentages, no Formal Coverage claim, no QID answered. Git use was read-only, and no input was edited. Clean room: findings are neutral, identifiers and line numbers are evidence pointers, and no code is reproduced.
- Scratch: `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/a3_bus_dgst/`.
