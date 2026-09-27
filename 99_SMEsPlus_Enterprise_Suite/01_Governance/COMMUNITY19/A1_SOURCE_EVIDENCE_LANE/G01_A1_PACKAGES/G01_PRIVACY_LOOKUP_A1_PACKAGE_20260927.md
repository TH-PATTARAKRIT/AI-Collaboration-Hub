# G01 PLATFORM_BASE — Module `privacy_lookup` — RED TEAM A1 Package

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A1 (source-backed research synthesizer) |
| Governed group / module | G01 PLATFORM_BASE / `privacy_lookup` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_PRIVACY_LOOKUP_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `35ccba82e8c3582bc81c43141a812941eadd32044e8e7cb6db7950c36065fe99` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Freeze (topic lens only) | W1-B11, freeze_hash `94852761617bd3fc7c38182d374f6e82f62b3f5701f59fe17355c3c295202ea5`; bank `G01_PRIVACY_LOOKUP_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `a6327b89…e0bb694` (matches `FREEZE_W1-B11.json`); gate **DELTA-RECHECK**, non-canonical freeze basis (the manifest has a reduced field set: no bank_files map, authorization or frozen_at). A1 proceeds as instructed. This package does not cure the freeze basis. |
| Date | 2026-09-27 |
| Lane B dependency | None. A1 did not wait for, view, or use Lane B evidence. |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** (freeze-basis DELTA-RECHECK caveat carried) |

The bank is used only as a topic lens: input validation, discovery scope, authority, company/tenant isolation, remediation actions, log masking, retention and staleness. No QID is answered and the bank is not edited. All paths are relative to `addons/privacy_lookup/` at the anchor.

## 1. Claims

| Claim ID | Claim (neutral WHAT / WHY / RISK) | Evidence (path @ blob) | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-PRIV-C01 | WHAT: module "Privacy" is hidden and auto-installed. It depends only on mail and has no description. Its purpose, inferred from code, is to find a data subject's footprint by name and email, archive or delete what is found, and log the action in masked form. | `__manifest__.py` @ 9eaa9987 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-PRIV-C02 | WHAT: the email must normalize to a valid address before any query is built, or a user error is raised. Name and email are trimmed. | `wizard/privacy_lookup_wizard.py` @ 3b6d52e0 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-PRIV-C03 | WHAT: discovery runs as one raw database query, after pending writes are flushed. It is not an ORM search. RISK: it bypasses record rules and company rules, so records in every company of the database are found. The module contains no company reference at all. | `wizard/privacy_lookup_wizard.py` @ 3b6d52e0 (spot-checked: flush + direct execute; zero company references) | HIGH | SOURCE-STATIC |
| A1-G01-PRIV-C04 | WHAT: the fixed scope is matching partners (by normalized email or name), users (by login or linked partner) and messages written by those partners. The dynamic scope is every non-transient, table-backed model except six excluded ones, matched on four stored email-like fields plus a name field, or on non-cascade partner references. | `wizard/privacy_lookup_wizard.py` @ 3b6d52e0 (exclusion list spot-checked; field list seen) | HIGH | SOURCE-STATIC |
| A1-G01-PRIV-C05 | WHAT: name matching uses the raw name as a pattern with no wildcards added, while email display fields use surrounding wildcards. Phone, address and free-text fields are not searched. RISK: false positives from homonyms or partial emails, and false negatives outside the listed fields. Scope grows with installed modules. | `wizard/privacy_lookup_wizard.py` @ 3b6d52e0 (email-field list and match operators seen; precision per Lane A) | MED | SOURCE-STATIC |
| A1-G01-PRIV-C06 | WHAT: result lines hide the openable record reference when the viewer lacks read access (source comment mentions multi-company rules). The record's display name, however, is resolved with sudo. RISK: names of records the operator cannot read may still be shown. | `wizard/privacy_lookup_wizard.py` @ 3b6d52e0 (spot-checked: access check on reference; sudo on name) | HIGH | SOURCE-STATIC |
| A1-G01-PRIV-C07 | WHAT: archive/unarchive writes the active flag on the target record with sudo. Delete removes the target with sudo. RISK: both bypass per-record and company access, giving an administrator a cross-company erasure capability that no scope check limits. | `wizard/privacy_lookup_wizard.py` @ 3b6d52e0 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-PRIV-C08 | WHAT: a second delete on the same line raises an error. Bulk delete skips lines already deleted. Bulk archive skips lines whose model has no active flag and lines already inactive. The UI asks for confirmation before delete. | `wizard/privacy_lookup_wizard.py` @ 3b6d52e0 (spot-checked); confirmation per Lane A (views) | HIGH | SOURCE-STATIC |
| A1-G01-PRIV-C09 | WHAT: the only actions on found records are archive, unarchive, delete and open. There is no action to anonymize or redact fields. "Anonymize" exists only as masking of the subject in the log. RISK: a subject whose records must be kept (e.g. legal hold) cannot be pseudonymized through this module. | `wizard/privacy_lookup_wizard.py` @ 3b6d52e0; `models/privacy_log.py` @ 045a2d25 (spot-checked: "anonymi" appears only in log fields) | HIGH | SOURCE-STATIC |
| A1-G01-PRIV-C10 | WHAT: one log per wizard is created at the first non-empty execution detail. Later actions update the same log's details and found-records description. Lookup alone creates no log. | `wizard/privacy_lookup_wizard.py` @ 3b6d52e0 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-PRIV-C11 | WHAT: the log stores date, handling user, masked name, masked email, details, found records and a note. Masking keeps the first character of each word or dot-segment, keeps the TLD, and keeps three large public mail domains unmasked. A name containing "@" is masked as an email. | `models/privacy_log.py` @ 045a2d25 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-PRIV-C12 | WHAT: when the email is empty or has no "@", the email-masking helper *returns* a user-error object instead of raising it. That object would become the value to store. RISK: a masked field would hold an exception representation, or later processing would fail, instead of a clean rejection. Input validation (C02) makes this path unlikely; reachability is unverified. | `models/privacy_log.py` @ 045a2d25 (spot-checked) | HIGH (defect present) / LOW (reachability) | SOURCE-STATIC |
| A1-G01-PRIV-C13 | WHAT: the log receives the untrimmed wizard name and email, not the normalized values used for lookup. RISK: masking runs on the raw input form; input with several "@" or a display-name form was not evaluated. | `wizard/privacy_lookup_wizard.py` @ 3b6d52e0 (spot-checked: log create uses raw fields) | MED | SOURCE-STATIC |
| A1-G01-PRIV-C14 | WHAT: the wizard, lines and log are available only to system administrators. Lines cannot be deleted. The log has full create/read/write/delete. RISK: audit entries can be edited or deleted by the same role that performs the erasure, with no immutability or separation of duties. | `security/ir.model.access.csv` @ d70edab3 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-PRIV-C15 | WHAT: wizard and line data expire after 24 hours through transient cleanup. The log has no retention rule and is kept indefinitely. | `wizard/privacy_lookup_wizard.py` @ 3b6d52e0 (spot-checked: 24 h on both); log absence per Lane A | HIGH | SOURCE-STATIC |
| A1-G01-PRIV-C16 | WHAT: the log menu sits under the technical settings menu. Technical model names in the found-records description are shown only to the debug group. The target-model selection lists all models via sudo. | `views/privacy_log_views.xml` @ 2116cc13 (menu spot-checked); rest Lane A | MED | SOURCE-STATIC |
| A1-G01-PRIV-C17 | WHAT: running lookup again replaces all existing lines. WHY: results reflect current state. RISK: actions already taken remain only in the log; line history is lost. | `wizard/privacy_lookup_wizard.py` @ 3b6d52e0 (spot-checked: clear-then-add) | HIGH | SOURCE-STATIC |
| A1-G01-PRIV-C18 | WHAT: the "Privacy Lookup" server actions on partner and user forms are restricted to administrators. Bulk "Archive Selection" and "Delete Selection" are bound to the line list. | `wizard/privacy_lookup_wizard_views.xml` @ 9d49f1db; `data/ir_actions_server_data.xml` @ 7aac52ec (Lane A only) | MED | SOURCE-STATIC |

## 2. Business rules (source-derived, neutral)
- BR1: No lookup without a normalizable email (C02).
- BR2: Discovery is database-wide and ignores company and record rules (C03).
- BR3: Remediation is limited to archive (for models with an active flag) or permanent delete, both with elevated rights (C07, C09).
- BR4: Each record is deleted at most once per line; repeat delete is refused (C08).
- BR5: The first remediation creates one masked log per wizard session; later actions update it (C10, C11).
- BR6: Only system administrators can use the module (C14, C18).

## 3. States / transitions
- Wizard: created → lookup run (lines replaced) → remediation (log created/updated) → expired after 24 h (C15, C17).
- Line: found (active or archived) ↔ toggled active/archived → unlinked (terminal; second delete refused) (C07, C08).
- Log: absent → created on first detail → updated per action → persists; editable and deletable by admin (C10, C14).

## 4. Exceptions / failure modes
- Invalid email → user error before the query (C02).
- Delete on an already-unlinked line → user error (C08).
- Empty or "@-less" email reaching log masking → error object returned rather than raised (C12).
- Target changed or removed by another process after lookup → behavior of the sudo write/delete on a missing record is not handled in this module (GAP-PRIV-07).
- Delete blocked or cascaded by the target model's own constraints → not visible here (Lane A G2).

## 5. Cross-module handoffs
- mail: message authorship, notification, followers and channel-member exclusions (C04).
- base: partners, users, model registry and actions. Scope grows with every installed module's tables. There is a special case for a mass-mailing trace model outside the dependencies (Lane A section 3).
- phone_validation: no edge. Phone fields and the phone suppression list are not searched or remediated (C05; phone_validation A1 C03).

## 6. Evidence gaps (Lane A carried forward + A1)
- GAP-PRIV-01 (Lane A G1): whether C12 is reachable at runtime is unknown.
- GAP-PRIV-02 (Lane A G2): cascade/restrict effects of a sudo delete on dependents are not visible.
- GAP-PRIV-03 (Lane A G3): no documented legal scope (e.g. GDPR); purpose is inferred.
- GAP-PRIV-04 (Lane A G4): match precision and false-positive rate cannot be assessed statically.
- GAP-PRIV-05 (Lane A G5): intent behind the editable/deletable log is undocumented.
- GAP-PRIV-06 (Lane A G6): tests not reviewed.
- GAP-PRIV-07 (A1): handling of records changed or deleted between lookup and action.
- GAP-PRIV-08 (A1): masking behavior on raw, untrimmed or display-form email input (C13).
- GAP-PRIV-09 (A1): freeze basis for W1-B11 is DELTA-RECHECK. Topic-lens alignment may need re-check once the freeze is re-based.

## 7. CRQ candidates
- CRQ-PRIV-01: Must personal-data discovery and remediation be bounded to the operator's tenant/company scope? (C03, C07)
- CRQ-PRIV-02: Must remediation offer field-level anonymization/pseudonymization as an alternative to delete? (C09)
- CRQ-PRIV-03: Must the privacy audit log be append-only and protected from the role performing the erasure? (C14)
- CRQ-PRIV-04: What retention period applies to privacy audit logs? (C15)
- CRQ-PRIV-05: Must result labels be restricted to what the operator may read? (C06)
- CRQ-PRIV-06: What discovery field coverage is required (phone, address, free text, cascade-owned data)? (C04, C05)
- CRQ-PRIV-07: Must lookup matching precision be defined (exact vs partial) to control over- and under-matching? (C05)
- CRQ-PRIV-08: Must masking failures be rejected explicitly, never stored? (C12, C13)
- CRQ-PRIV-09: Must stale-result handling be deterministic when targets change after lookup? (GAP-PRIV-07)

## 8. Contradictions
- None CONFIRMED-FROM-SOURCE between Lane A and source. All spot-checked Lane A statements matched.
- CANDIDATE-PRIV-X1: Line references honor read access, citing the multi-company rule comment (C06), while archive and delete on the same lines run with sudo across companies (C07). Read is scoped but write/delete is not. This is an internal design inconsistency, confirmed present in source; its runtime effect needs proof.
- CANDIDATE-PRIV-X2: The email-masking helper signals a failure with an error type but returns it instead of raising it (C12). This is an intent-versus-behavior mismatch, confirmed present in source; reachability is unverified (GAP-PRIV-01).

## 9. Spot-check log
Re-fetched from `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/privacy_lookup/<path>`; `git hash-object` computed on the scratchpad copy (no repository git operations).

| # | Path | Recorded blob | Computed blob | Match | Content verified |
|---|---|---|---|---|---|
| 1 | `wizard/privacy_lookup_wizard.py` | 3b6d52e055a912c67e85970d0299de14d97cc619 | 3b6d52e055a912c67e85970d0299de14d97cc619 | YES | C02 email validation; C03 flush + raw execute, no company refs; C04 exclusion list; C06 read check vs sudo name; C07 sudo write/delete; C08 double-delete error and skips; C10 log once then update; C15 24 h; C17 clear-then-add |
| 2 | `models/privacy_log.py` | 045a2d25f7115f860d558c28d0d2f80301b64781 | 045a2d25f7115f860d558c28d0d2f80301b64781 | YES | C11 masking rules; C12 error object returned, not raised |
| 3 | `security/ir.model.access.csv` | d70edab351c9369c4e8100145b9006d1043029fe | d70edab351c9369c4e8100145b9006d1043029fe | YES | C14: system-only; line no delete; log full CRUD |
| 4 | `views/privacy_log_views.xml` | 2116cc13cac9496ea25a04b48cfba032264e6fc0 | 2116cc13cac9496ea25a04b48cfba032264e6fc0 | YES | C16: menu under technical menu; typo id present |
| 5 | `__manifest__.py` | 9eaa9987cdaa97b006c5fea0f961016490f811cd | 9eaa9987cdaa97b006c5fea0f961016490f811cd | YES | C01: depends mail only, auto-install, Hidden |

Result: 5 of 5 blobs match, 0 mismatches.

## 10. Provenance
- Input: the Lane A packet (sha256 above), consumed read-only.
- Spot-check fetches: the anchor commit above via raw.githubusercontent. Files were held in the session scratchpad only.
- Topic lens: bank W1-B11 (bank sha256 verified against the freeze manifest; freeze basis DELTA-RECHECK). No QID answered.
- No Lane B material, no runtime system and no other lane packets were consulted, except the phone_validation packet for the cross-module edge note.

## 11. Limitations
- Source presence does not mean runtime reachability. Nothing here is runtime proof.
- No Formal Coverage claim, no percentages, no QID answers.
- Clean room: neutral WHAT/WHY/RISK only. Identifiers are evidence pointers, not design recommendations. No code, schema, ORM or workflow reuse.
- Claims marked "Lane A only" were not re-read by A1 (MED confidence).
- The effective discovery scope depends on the installed module set, which is not assessed here. Single anchor commit.
