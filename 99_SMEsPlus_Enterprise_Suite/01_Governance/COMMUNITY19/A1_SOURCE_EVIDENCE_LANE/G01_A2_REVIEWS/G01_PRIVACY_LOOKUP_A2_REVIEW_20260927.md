# G01 PLATFORM_BASE — Module `privacy_lookup` — RED TEAM A2 Review

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 (functional/semantic verifier of A1 conclusions). Independent of A1; A1 package not repaired. |
| Governed group / module | G01 PLATFORM_BASE / `privacy_lookup` |
| A1 package (input, immutable) | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_PRIVACY_LOOKUP_A1_PACKAGE_20260927.md` sha256 `61524ebc7f263672fc0d16d082515661558a3b36b24890e0f6b19b9a7ece056a` |
| Upstream Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_PRIVACY_LOOKUP_LANE_A_PASS1_20260927.md` sha256 `35ccba82e8c3582bc81c43141a812941eadd32044e8e7cb6db7950c36065fe99` (matches the value recorded in the A1 header) |
| Topic-lens bank | `GMVQ/G01_PLATFORM_BASE/G01_PRIVACY_LOOKUP_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `a6327b89e17634339e73777377718bc93e40963163ecd1b2b6f05ee97e0bb694`. It matches `bank_sha256` in `FREEZE_W1-B11.json` (manifest sha256 `19e3a1544a60572e63d22e31955226a9c632b27a25c7468d54fb1fee286678ed`, freeze_hash `94852761617bd3fc7c38182d374f6e82f62b3f5701f59fe17355c3c295202ea5`). The manifest has a reduced field set: no bank_files map, no authorization, no frozen_at. |
| Freeze-basis status | **W1-B11 DELTA-RECHECK, non-canonical freeze basis.** A2 verification proceeds as instructed. **QID-level lineage for privacy_lookup is NOT A3-eligible until canonical re-freeze.** This review does not cure the freeze basis. No QID answered. |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/privacy_lookup/` |
| Date | 2026-09-27 |
| Lane B | None supplied. Not waited for. |
| **Disposition** | **A2 VERIFIED WITH FINDINGS — HANDOFF TO REC (freeze-basis caveat carried; QID lineage A3-ineligible pending re-freeze).** 18 claims: 15 VERIFIED, 3 PARTIAL, 0 NOT_VERIFIED, 0 OUT_OF_SCOPE. 2 new HIGH semantic findings (SF-PRIV-01, SF-PRIV-02) and 9 omissions. 9 runtime proof requirements. No FAIL. |

## 2. Test plan (declared before verdicts)

| # | Test | Method | Pass condition |
|---|---|---|---|
| T1 | Lineage integrity | sha256 of the A1 package, the Lane A packet and the bank, compared with the A1 header and the freeze manifest | Hashes match; freeze-basis status recorded |
| T2 | Source identity | Independent re-fetch of 8 module files from the anchor into the A2 scratchpad; `git hash-object` compared with the Lane A inventory. Context file `odoo/tools/mail.py` (blob 2b05c91f) was fetched only to read the email-normalization contract. | All module blobs match |
| T3 | Claim re-read | Independent re-read of the cited file for every claim C01–C18, including those marked "Lane A only" | The WHAT statement matches source text and control flow |
| T4 | Mandatory semantic re-read | HIGH claims plus the named topics: raw SQL lookup bypassing record/company rules (C03), sudo archive/unlink across companies (C07), no anonymize for found records (C09), editable/deletable log (C14), the email-masking helper returning an error (C12), untrimmed log inputs (C13), "@" name masking (C11), read-access vs sudo inconsistency (C06/X1); X1 and X2 | WHAT and RISK both hold; mitigating or aggravating facts are logged |
| T5 | Business meaning | Read as data-subject request handling (locate / erase / restrict / audit) in a multi-company SaaS under PDPA/GDPR-style expectations | Overclaims and omissions listed |
| T6 | Cross-claim consistency | BR1–BR6, states, exceptions, handoffs and contradictions checked against the verdicts | Inconsistencies listed |
| T7 | Lane B classification | Each claim classified NOT_APPLICABLE, UNCORROBORATED or MISSING_REQUIRED_RUNTIME_PROOF | No FAIL is used for absence of Lane B |
| T8 | Proof requirements | Only for inherently runtime claims: setup, expected result, fail condition | Each requirement is falsifiable |

T1 result: PASS for the 3 content hashes; the freeze basis is non-canonical (recorded, not cured). T2 result: PASS, 8 of 8 blobs match: `__manifest__.py` 9eaa9987, `models/privacy_log.py` 045a2d25, `models/res_partner.py` 19962c36, `wizard/privacy_lookup_wizard.py` 3b6d52e0, `wizard/privacy_lookup_wizard_views.xml` 9d49f1db, `views/privacy_log_views.xml` 2116cc13, `security/ir.model.access.csv` d70edab3, `data/ir_actions_server_data.xml` 7aac52ec.

## 3. Claim verdict table

| Claim | A1 conf. | A2 verdict | A2 basis (independent re-read; pointers are evidence only) |
|---|---|---|---|
| C01 | HIGH | VERIFIED | Manifest: name "Privacy", Hidden, auto-install, depends mail only, no description or summary. The partner helper opens the wizard prefilled with the partner's name and email. |
| C02 | HIGH | VERIFIED | Query builder trims name and email and normalizes the email; if normalization fails, a user error is raised before any SQL is built. The normalization contract (tools) requires exactly one address and accepts display-name form ("Name <addr>"). |
| C03 | HIGH | PARTIAL | Core verified: pending writes flushed, then one raw SQL statement run directly on the cursor. No company predicate or record-rule filter is applied, so discovery is database-wide. Wording defect: "the module contains no company reference at all" is literally false. A comment cites multi-company rules (line-reference access check) and one searched field name contains "company". Neither applies company scoping, so the substantive conclusion stands. |
| C04 | HIGH | VERIFIED | Fixed scope: partners by normalized email or name; users by login pattern or linked partner email/name; messages by author among matched partners. Dynamic scope: every non-transient, table-backed model except six listed (partner, users, notification, followers, channel member, message), matched on stored email-like fields (four names) and non-cascade many2one references to partners. Nuance: the name condition is added only on models that also have a stored email-like field. |
| C05 | MED | VERIFIED | Name compared case-insensitively as a pattern without added wildcards; non-normalized email fields use surrounding wildcards; normalized fields use equality. No phone, address or free-text fields. Omission: user input is not escaped for pattern metacharacters (SF-PRIV-01). |
| C06 | HIGH | VERIFIED | The line reference is computed only if a read-access check on the target passes (comment cites multi-company rules). The stored display name is computed with sudo and shown in the line list. |
| C07 | HIGH | VERIFIED | Archive/unarchive writes the active flag with sudo; delete unlinks with sudo. Neither checks the operator's read or company access to the target. |
| C08 | HIGH | PARTIAL | A repeat delete on a line raises an error. Bulk delete skips unlinked lines. Bulk archive skips lines whose model has no active flag and lines already inactive. All verified. "The UI asks for confirmation before delete" holds only for the per-line button. The bulk "Delete Selection" server action carries no confirmation attribute (SF-PRIV-09). |
| C09 | HIGH | VERIFIED | Line actions are archive toggle, delete (single/bulk) and open. The "anonymi" term appears only in the log's field names and masking helpers. |
| C10 | HIGH | VERIFIED | The log is created when the wizard has no log and the aggregated details are non-empty; otherwise the existing log's details and found-records text are overwritten. See SF-PRIV-02 for the consequence. |
| C11 | HIGH | VERIFIED | Log fields: date, handler (default current user), masked name, masked email, details, found records, note. Name masking: per space-separated word, first character plus asterisks; a name containing "@" is routed to email masking. Email masking: local part per dot-segment; domain segments masked except TLD; three large public domains left intact. |
| C12 | HIGH / LOW | VERIFIED | For empty or "@-less" input the email-masking helper returns (does not raise) a user-error object, which create would assign as the field value. Reachability refined in SF-PRIV-05: unreachable from the wizard; reachable by direct log creation. |
| C13 | MED | VERIFIED | Log creation passes the wizard's raw name and email, not the trimmed/normalized values. A2 resolves part of GAP-PRIV-08 statically: see SF-PRIV-04 (multiple "@" breaks masking). |
| C14 | HIGH | VERIFIED | ACL: wizard system CRUD; line system read/write/create, no delete; log system full CRUD. Log form fields are not read-only. The actions hide "create" in the UI context only. |
| C15 | HIGH | VERIFIED | Wizard and line: max-hours 24, max-count 0. The log model declares no retention. The module ships no cron or cleanup data. |
| C16 | MED | VERIFIED | The log menu sits under the technical settings menu (the menu id has a typo). Technical model names in found-records appear only for the debug/technical group. The line reference selection lists all models via sudo. |
| C17 | HIGH | PARTIAL | Mechanics verified: lookup clears all lines, then adds the results. The UI hides the Lookup button once lines exist; A1 omits this. RISK not supported: "actions already taken remain only in the log" is contradicted, because the log's details are recomputed from current lines and overwritten when lines are replaced (SF-PRIV-02). |
| C18 | MED | VERIFIED | Partner and user form server actions are bound with the system group. Bulk archive and delete are bound to the line list and kanban. Neither bulk action has its own group; the line ACL is system-only. |

A1 structural statements checked under T6:

| Item | A2 result |
|---|---|
| BR1 no lookup without a normalizable email | Holds. Display-name form is accepted (SF-PRIV-04). |
| BR2 database-wide, ignores company/record rules | Holds. |
| BR3 archive or delete with elevated rights | Holds. |
| BR4 at most one delete per line | Holds per line. Each model contributes one row per record, because its conditions are combined in a single disjunction, so duplicate lines for the same record are not expected from the query structure. |
| BR5 first remediation creates one masked log; later actions update it | Holds, but the update is a snapshot overwrite, not an append (SF-PRIV-02). |
| BR6 system administrators only | Holds at ACL level. |
| States: Log "updated per action → persists" | Incomplete: details can be blanked (SF-PRIV-02). |
| §5 no edge to phone_validation | Holds. |
| CANDIDATE-PRIV-X1 | Confirmed present in source (C06 vs C07). Aggravated by the stored sudo display name. Runtime proof PR-PRIV-01. |
| CANDIDATE-PRIV-X2 | Confirmed present in source (C12). Reachability narrowed (SF-PRIV-05); runtime proof PR-PRIV-06. |

## 4. Semantic findings

- **SF-PRIV-01 (HIGH, new; not in A1).** Name and email are inserted as case-insensitive pattern operands without escaping pattern metacharacters. A name consisting of the multi-character wildcard matches every partner. That makes every partner an "indirect reference", so every user, every message authored by any partner, and every record on any model holding a non-cascade partner reference becomes a result line. A valid email is still required but does not constrain the name branch. Combined with C07 (sudo, cross-company) and O-PRIV-08 (no bulk-delete confirmation), one operator action could erase large parts of the database across companies. Single-character wildcards in names and emails also broaden matches. Runtime proof PR-PRIV-02. Relevant to CRQ-PRIV-07.
- **SF-PRIV-02 (HIGH, new; contradicts C17 RISK, aggravates C14).** The wizard's stored details are a join of the current lines' details, and each line holds only its latest action text. Each recomputation pushes that snapshot into the log. Consequences, read from control flow: (a) archive then unarchive of one record leaves only "Unarchived" in the log; (b) re-running lookup (hidden in the UI once lines exist, but callable) clears lines and blanks the log's details while replacing its found-records text; (c) transient cleanup may blank details if lines are removed before their wizard. The ordering of (c) is runtime-dependent. The log is therefore not a reliable record of erasure actions even before C14's edit/delete rights are considered. Runtime proofs PR-PRIV-03 and PR-PRIV-04.
- **SF-PRIV-03 (MED, new).** The archive/unarchive side effect runs inside the line's field-change handler, which performs a sudo write immediately. The audit detail reaches the log only when the line is saved. An interactive toggle that is then discarded may leave the target archived with no log entry. Runtime proof PR-PRIV-05.
- **SF-PRIV-04 (MED, resolves part of GAP-PRIV-08).** Display-name email input passes validation. Non-normalized email fields are then matched against the whole display string wrapped in wildcards, which causes false negatives on those fields. The log masks the raw display string. Masking splits on "@" and expects exactly two parts. Raw input with more than one "@" (e.g. a quoted display name containing "@", or a name field containing two "@") fails during log creation. Log creation happens inside the recomputation at the first remediation save, so the failure surfaces as an error on that action. Whether the preceding sudo delete is rolled back is runtime (PR-PRIV-07).
- **SF-PRIV-05 (LOW, refines C12/X2).** Through the wizard, the email reaching the masking helper has already passed normalization, which requires "@". The name branch calls the email helper only when "@" is present. The returned-error path is therefore unreachable from the wizard. It is reachable by direct log creation, which the ACL allows even though the UI hides create. The stored value would then be whatever the character field makes of an exception object, possibly including the unmasked input in the error text. Runtime proof PR-PRIV-06.
- **SF-PRIV-06 (MED, business).** The masking keeps first letters, segment lengths (asterisk count), TLD and common domains. Together with date, handler, model names and record ids in found-records, the log is pseudonymized, not anonymous, under GDPR/PDPA-style standards. The "anonymized" field naming overstates the protection. A1 C11 describes the mechanics correctly but does not evaluate them.
- **SF-PRIV-07 (LOW).** Unmasked subject identifiers persist for up to 24 hours in the wizard (raw name/email) and on lines (stored sudo display names). The masked log therefore does not bound exposure during that window.
- **SF-PRIV-08 (MED, refines C04/C05).** Messages are found only through an author partner. The message model is excluded from dynamic scope, so messages carrying the subject only as a raw sender address, or addressed to the subject, are not discovered.
- **SF-PRIV-09 (MED).** The bulk "Delete Selection" server action has no confirmation step, unlike the per-line delete (C08 correction).
- **Business meaning review (T5).** The module covers locate, restrict-like archive and erase for a single subject. Measured against GDPR/PDPA-style data-subject handling in a multi-company SaaS:
  - It has no access/export (portability), rectification or anonymization/pseudonymization of retained records (C09).
  - It has no request intake, requester identity verification, deadline tracking or controller/company attribution on the log (the log has no company field, so a request addressed to company A cannot be distinguished from one for company B).
  - Its reach is database-wide under a single system role (C03/C07). In a database hosting several controllers, that means over-erasure risk and processing of other controllers' data without scope checks.
  - Its audit is mutable (C14, SF-PRIV-02) and pseudonymized, not anonymized (SF-PRIV-06).
  - Archive is not equivalent to "restriction of processing": archived records remain processable by code.
  - Phone-based suppression and phone data are outside scope (A1 §5 handoff correct).
  - A1's inferred purpose statement (C01) is accurate and not overclaimed. A1's GAP-PRIV-03 (no legal scope) is correctly left open.

## 5. Omissions (A1 did not state; A2 found in source or by semantic reading)

| # | Omission | Severity | Link |
|---|---|---|---|
| O-PRIV-01 | Unescaped pattern metacharacters in name/email; the name wildcard causes whole-database scope (SF-PRIV-01) | HIGH | C05, CRQ-PRIV-07, CRQ-PRIV-01 |
| O-PRIV-02 | Log details are a mutable snapshot overwritten by later actions and by re-lookup (SF-PRIV-02) | HIGH | C10, C17, CRQ-PRIV-03 |
| O-PRIV-03 | Archive executes inside a field-change handler before save (SF-PRIV-03) | MED | C07, C10 |
| O-PRIV-04 | Display-form email accepted; multi-"@" raw input breaks log masking (SF-PRIV-04) | MED | C13, CRQ-PRIV-08 |
| O-PRIV-05 | Masking returned-error path unreachable from the wizard, reachable by direct log creation (SF-PRIV-05) | LOW | C12 |
| O-PRIV-06 | Log is pseudonymized, not anonymous (SF-PRIV-06) | MED | C11 |
| O-PRIV-07 | Messages not discoverable by raw sender or recipient address (SF-PRIV-08) | MED | C04, CRQ-PRIV-06 |
| O-PRIV-08 | Bulk delete has no confirmation (SF-PRIV-09) | MED | C08 |
| O-PRIV-09 | No controller/company attribution on the log; no request lifecycle | MED | C11, C14, CRQ-PRIV-01 |

## 6. Lane B classification

No Lane B evidence was supplied. Absence is never a FAIL.

| Class | Claims |
|---|---|
| NOT_APPLICABLE (internal structure, not observable on the user surface) | C01, C04, C15 (retention internals) |
| UNCORROBORATED (observable on the user surface, no Lane B yet; verified in source) | C02, C06 (label vs link visibility), C08, C09, C11, C14, C16, C18 |
| MISSING_REQUIRED_RUNTIME_PROOF (inherently runtime; see §7) | C03 and C07 (with X1), C05 (SF-PRIV-01), C10 and C17 (SF-PRIV-02/03), C12 (X2), C13 (SF-PRIV-04), GAP-PRIV-02, GAP-PRIV-07 |

## 7. Proof requirements

| ID | Claim(s) | Setup / action | Expected (if A1/A2 reading holds) | Fail condition (reading falsified) |
|---|---|---|---|---|
| PR-PRIV-01 | C03, C07, X1 | Two companies A and B. A system admin whose allowed companies are A only. The subject has a contact and a company-scoped record in B. Run lookup, archive the B record, then delete it. | The B records appear as lines with a name shown but no openable link. Archive and delete both succeed. | The B records are absent from the results, or archive/delete is refused by access rules. |
| PR-PRIV-02 | C05, SF-PRIV-01 | Lookup with a valid email of a non-existent subject and a name made of the multi-character wildcard only. | The result lines include unrelated partners, users and partner-referencing records across the database. | Only records matching the email are returned, or the input is rejected. |
| PR-PRIV-03 | C10, C17, SF-PRIV-02 | (a) Archive then unarchive one line, and inspect the log. (b) Delete one line, confirm the log shows the deletion, then invoke lookup again (via the RPC/action), and inspect the log. | (a) The log details show only the unarchive. (b) The log details are empty after re-lookup and the found-records text is replaced. | The log keeps both events in (a), or keeps the deletion detail in (b). |
| PR-PRIV-04 | C15, SF-PRIV-02 | Perform a deletion and let the transient cleanup expire lines and wizard (or trigger the cleanup). Inspect the log. | The log details are retained unchanged (the A1 C15 reading: the log persists). | The details are blanked or altered by the cleanup. |
| PR-PRIV-05 | SF-PRIV-03 | In the line list, toggle the active switch for one record, then discard without saving (if the widget allows). Inspect the target and the log. | The target is archived and no log detail records it. | The target is unchanged, or a log detail exists. |
| PR-PRIV-06 | C12, X2, SF-PRIV-05 | As admin, create a log record directly (RPC or import) with an email value lacking "@". | The record is stored with a non-masked or error-text value in the masked email field, or the store fails with a non-user-facing error. | A clean user-facing validation error is raised and nothing is stored. |
| PR-PRIV-07 | C13, SF-PRIV-04 | Lookup with email input in display form whose display name contains "@" (single valid address), then delete one line. | The lookup succeeds; the delete action raises an error during log creation. Record whether the deletion persisted. | The log is created normally with a masked value. |
| PR-PRIV-08 | GAP-PRIV-02 | Delete, via a line, a partner referenced by records with restrict and with cascade dependencies. | The restrict dependency blocks the delete with an error and no partial state. The cascade dependents are removed and are not listed in the log. | Partial deletion persists, or the log lists cascade-removed dependents. |
| PR-PRIV-09 | GAP-PRIV-07 | After lookup, delete a target record through another session; then run delete and archive on its line. | An error or an explicit no-op; the log does not claim a deletion that this action did not perform. | The log records "Deleted" for the already-missing record, and no error is shown. |

Count: 9 proof requirements.

## 8. Limitations

- Freeze basis W1-B11 is DELTA-RECHECK (non-canonical). This review is valid as A2 claim verification, but QID-level lineage is not A3-eligible until canonical re-freeze. No QID was answered.
- Static source only; no runtime system. SF-PRIV-01..05 are A2 inferences from control flow and SQL semantics; they need PR execution before REC treats them as confirmed.
- ORM behaviors outside this module (transient cleanup ordering, character-field coercion of non-string values, change-handler transaction handling in the web client) were not read. The related PRs state expected outcomes and fail conditions rather than assuming them.
- The effective discovery scope depends on the installed module set (not assessed). Tests and JS were not reviewed.
- No percentages, no Formal Coverage, no git operations. Clean room: neutral description only, no code reproduced.
