# G01 PLATFORM_BASE — Module `phone_validation` — RED TEAM A2 Review

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 (functional/semantic verifier of A1 conclusions). Independent of A1; A1 package not repaired. |
| Governed group / module | G01 PLATFORM_BASE / `phone_validation` |
| A1 package (input, immutable) | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_PHONE_VALIDATION_A1_PACKAGE_20260927.md` sha256 `e128cb2e9905aed013c9447c922441d4680c46467b7355f92ce01d14e0c003b0` |
| Upstream Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_PHONE_VALIDATION_LANE_A_PASS1_20260927.md` sha256 `069aca0017cae09ae1bddb28f46299671080d36ecbc869b5b1d1923cc998b888` (matches the value recorded in the A1 header) |
| Topic-lens bank | `GMVQ/G01_PLATFORM_BASE/G01_PHONE_VALIDATION_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `c70aae333f7a25b558383945b2cca58a66816413eb079c6225161075a50b8a80` — matches `FREEZE_W1-B10.json` bank_files (freeze_hash `0d7f6e94acde38662de420f8947ffaa1ab04cddaaec43516e46b441ce1222010`, manifest sha256 `049aa570fdf26c11ec7289e33d9fb9675399f7410a140761aa00c248243956d8`). Gate W1-B10 ELIGIBLE. Used as topic lens only; no QID answered. |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/phone_validation/` |
| Date | 2026-09-27 |
| Lane B | None supplied. Not waited for. |
| **Disposition** | **A2 VERIFIED WITH FINDINGS — HANDOFF TO REC.** 20 claims: 17 VERIFIED, 3 PARTIAL, 0 NOT_VERIFIED, 0 OUT_OF_SCOPE. 1 new HIGH semantic finding (SF-PHON-01) and 7 omissions. 10 runtime proof requirements. No FAIL. |

## 2. Test plan (declared before verdicts)

| # | Test | Method | Pass condition |
|---|---|---|---|
| T1 | Lineage integrity | sha256 of A1 package, Lane A packet, bank; compare with A1 header and freeze manifest | All hashes match recorded values |
| T2 | Source identity | Independent re-fetch of 13 module files from the anchor via raw.githubusercontent into the A2 scratchpad; `git hash-object` compared to the Lane A inventory | All blobs match |
| T3 | Claim re-read | Independent re-read of the cited file for every claim C01–C20 (including those A1 marked "Lane A only") | WHAT statement matches source text and control flow |
| T4 | Mandatory semantic re-read | HIGH claims and the named contradiction/CRQ topics: normalized-number uniqueness (C02), DB-wide/no company scope (C03), system-only ACL (C04), sudo set/reset (C05), unvalidated storage without the library (C09), last-field-wins flag loop (C15), raw-text search fallback (C14), wizard access comment (C07); plus X1, X2 | WHAT and RISK both hold; any mitigating or aggravating fact A1 did not state is logged |
| T5 | Business meaning | Read claims as a consent-withdrawal / marketing-suppression control in a multi-company SaaS under PDPA/GDPR-style data-subject handling | Overclaims and omissions listed |
| T6 | Cross-claim consistency | Business rules BR1–BR6, states, exceptions, handoffs and contradictions checked against verdicts | Inconsistencies listed |
| T7 | Lane B classification | Per claim: NOT_APPLICABLE / UNCORROBORATED / MISSING_REQUIRED_RUNTIME_PROOF | No FAIL used for absence of Lane B |
| T8 | Proof requirements | Only for inherently runtime claims; each with setup, expected result and fail condition | Falsifiable |

T1 result: PASS (3 of 3 hashes match). T2 result: PASS (13 of 13 blobs match: `__manifest__.py` 323499d9, `tools/phone_validation.py` bf983464, `models/phone_blacklist.py` d94486f6, `models/mail_thread_phone.py` 01ca256f, `models/models.py` dccf9fbf, `models/res_partner.py` 9d240af4, `models/res_users.py` ca7def5e, `wizard/phone_blacklist_remove.py` e882a7a3, `security/ir.model.access.csv` fe442d04, `views/phone_blacklist_views.xml` e8a3183e, `views/res_partner_views.xml` 3fbc1c58, `wizard/phone_blacklist_remove_view.xml` 329009be, `lib/phonenumbers_patch/__init__.py` 66fd4a88).

## 3. Claim verdict table

| Claim | A1 conf. | A2 verdict | A2 basis (independent re-read; pointers are evidence only) |
|---|---|---|---|
| C01 | MED | VERIFIED | Manifest re-read: Hidden category, auto-install, depends base+mail, data list has ACL, views and wizard view only (no cron, no settings data). "No controllers" rests on the Lane A file inventory (no controllers directory listed); A2 did not list the tree independently. |
| C02 | HIGH | VERIFIED | DB unique constraint on the number with message "Number already exists"; create and write reformat through the acting user's format helper with raise enabled; add/remove format without raise. See SF-PHON-01 and SF-PHON-02 for a failure mode and a country dependency that A1 did not state. |
| C03 | HIGH | VERIFIED | Blacklist model has only number + active (plus chatter); no company field; module data list contains no record-rule file. |
| C04 | HIGH | VERIFIED | Three ACL rows: an all-zero row with no group for the list; full CRUD for system group on list and on the unblacklist wizard. |
| C05 | HIGH | VERIFIED | Mixin set/reset helpers call the list's add/remove internals under sudo (`models/mail_thread_phone.py` lines 242–246). Callers are not in this module (GAP-PHON-08 stands). |
| C06 | HIGH | VERIFIED | Flag computed with compute-sudo plus an explicit sudo search, with a TODO comment stating non-authorised users could not compute it otherwise; both flag fields restricted to internal-user group. Aggravating fact in SF-PHON-04. |
| C07 | HIGH | PARTIAL | WHAT verified: record entry point checks list write access and raises otherwise; comment says wizard access rights "currently not working as expected". RISK framing incomplete: the wizard's apply step calls the list removal **without** elevation and the wizard model itself is system-only in the ACL, so the effective control is the list ACL, not only the pre-check. See SF-PHON-03. |
| C08 | HIGH | VERIFIED | Parse twice (second parse after international formatting so local metadata patches apply); possible-check with reason-specific errors; TOO_LONG retried once with "00"→"+" or with "+" prepended; validity check last. |
| C09 | HIGH | VERIFIED | Import-failure branch: parse returns False, format returns input unchanged, an info log is emitted once per process (module-level flag). The model-level wrapper therefore passes raw input through as the "formatted" value. |
| C10 | MED | VERIFIED | Format branch re-read: E164 / RFC3966 when forced; INTERNATIONAL when forced or country code differs; NATIONAL otherwise. |
| C11 | HIGH | VERIFIED | Resolution: record country field → partner fields (no break; each field with a country overwrites; within one field the first partner's country is used) → current company country. |
| C12 | HIGH | VERIFIED | Create collapses duplicates in the request, searches including archived, reactivates archived unless the request says inactive, creates only missing, returns in request order. |
| C13 | HIGH | VERIFIED | Remove archives found entries; unknown numbers are created archived; reason goes to tracking log message or an internal note. Note: "never deletes" holds for the API only; ACL grants administrators hard delete (SF-PHON-06). |
| C14 | HIGH | VERIFIED | Number search replaces each term with its formatted value or, if formatting yields nothing, the raw term (both scalar and list operators). |
| C15 | HIGH | VERIFIED | Sanitized value = first number field that formats. Flag loop assigns on each iteration without break, so only the last listed number field decides the per-field flag; source comment calls it a hack and states the single-sanitized-value limitation. The overall "blacklisted" flag compares only the first formattable number, so a secondary number on the list is never evaluated. |
| C16 | MED | PARTIAL | Min length 3, "+"/"00" equivalence, separator stripping and index-missing skip (TODO) verified. "Raises an error on models with no phone fields" is imprecise: the sanitized field is always appended to the searched set, so the error fires only when there are no stored number fields **and** the sanitized index is missing. The raw query returns ids that are then filtered through the normal domain, so it is not a record-rule bypass. |
| C17 | HIGH | VERIFIED | Numbers collected before calling the parent deactivation; list add called without sudo; log names portal user and acting user by name and id. |
| C18 | MED | VERIFIED | Number and active are tracked; existing entries get a tracking log message; new entries get an internal note. No typed event exists. |
| C19 | MED | VERIFIED | Partner change handler on phone/country/company reformats to INTERNATIONAL or keeps raw. It is a UI change handler only (SF-PHON-07). |
| C20 | MED | PARTIAL | Count re-read: eight region loaders (CI, CO, IL, MA, MU, PA, SN, KE) plus two hooks (BR, MX). Correction: the eight loaders are themselves version-gated (registered only below given library versions); the BR hook chooses local vs library metadata by version; the MX hook appends formats only above a version. A1's wording implies only the two hooks are gated. |

A1 structural statements checked under T6:

| Item | A2 result |
|---|---|
| BR1 one entry per stored value DB-wide | Holds, but the stored value depends on the acting user's country for national-format input (SF-PHON-02). |
| BR2 archive, never delete, through the API | Holds as worded ("through the API"). |
| BR3 re-add reactivates | Holds. |
| BR4 admin-only + sudo helpers bypass | Holds. |
| BR5 country precedence | Holds for records; for blacklist writes the "record" is the acting user (SF-PHON-02). |
| BR6 direct create/write raises on invalid | Holds for non-empty invalid input only; empty/unformattable input via add/remove/mixin does not raise and is redirected (SF-PHON-01). |
| §5 "no edge to privacy_lookup" | Holds: privacy lookup searches email/name fields and partner references only; the blacklist has neither. |
| CANDIDATE-PHON-X1 | Confirmed present in source; practical impact narrower than framed (SF-PHON-03). Runtime proof PR-PHON-02. |
| CANDIDATE-PHON-X2 | Confirmed present in source; reachability outside module. Runtime proof PR-PHON-03. |

## 4. Semantic findings

- **SF-PHON-01 (HIGH, new, static inference — not in A1).** The list's add and remove entry points format the input without raising. For unformattable input the result is empty, and that empty value is passed into create. Create's formatter is invoked on the acting user's record; when given no number it falls back to reading a number field of that record. Read literally, an invalid number submitted to add (or a mixin record with no sanitized number passed to the sudo set helper, C05) would be replaced by the **acting user's own phone number**, which is then suppressed. If the acting user has no number, the required constraint fails instead. The same fallback applies to write with an empty number and to number search with an empty term. Impact: silent suppression of the wrong data subject and a misleading audit entry. Runtime proof PR-PHON-01. Relevant to CRQ-PHON-03 (reject rather than store when canonical validation fails).
- **SF-PHON-02 (MED, new).** Blacklist canonicalization runs on the acting user's record, so the country used for national-format input is the acting user's country (then that user's partner-field countries, then the current company's). Two administrators in different countries entering the same national-format digits can create two different entries. C02's uniqueness is therefore per acting-user interpretation, not per data subject. Runtime proof PR-PHON-10.
- **SF-PHON-03 (MED, refines C07/X1).** The wizard apply path is not elevated and the wizard model is system-only. A non-admin who reaches the wizard form should still fail when the transient record is saved or when the list is searched. The source comment remains an admission that the ACL did not behave as declared at some point. X1 is a defense-in-depth gap, not an established bypass. Runtime proof PR-PHON-02.
- **SF-PHON-04 (MED, aggravates C06).** The blacklisted flag also has a search implementation that joins record numbers against active list entries in raw SQL. Internal users can therefore filter all records whose number is suppressed. The oracle works at bulk enumeration scale, not only per-record probing. Final results still pass through the record's normal domain filtering.
- **SF-PHON-05 (LOW, precision on C16).** See verdict note. Search correctness depends on index state, as A1 states. The error condition is narrower than A1 states.
- **SF-PHON-06 (MED, business).** Administrators can hard-delete entries through the ACL and the standard list. A hard delete removes the entry and its chatter, which erases the evidence that an objection was recorded. Under a GDPR/PDPA-style regime a suppression entry is itself personal data kept to honour an objection. Deleting it silently re-enables contact with no trace.
- **SF-PHON-07 (LOW).** Partner reformatting (C19) happens only in the interactive change handler. Imports and API writes keep raw input in the phone field. The stored sanitized value is still computed independently.
- **Business meaning review (T5).** The module's list works as a marketing-suppression / right-to-object register. In a multi-company SaaS database where companies can be distinct controllers: (a) an objection recorded for one company suppresses all companies (over-suppression and implicit cross-controller disclosure through the visible flag); (b) any system administrator can un-suppress for all companies; (c) entries carry no company, channel, lawful-basis, consent-source or expiry attribute, and the reason is free text in chatter. A1's CRQ-PHON-01/02/06/07 capture (a)–(c) in part. A1 does not overclaim purpose. A1 omits that the list is identity-by-number only, with no link to a data subject, so erasure tooling (privacy_lookup) can neither find nor intentionally retain it.

## 5. Omissions (A1 did not state; A2 found in source or by semantic reading)

| # | Omission | Severity | Link |
|---|---|---|---|
| O-PHON-01 | Empty/unformattable number falls back to the acting user's own number (SF-PHON-01) | HIGH | C02, C05, BR6, CRQ-PHON-03 |
| O-PHON-02 | Blacklist canonical form depends on the acting user's country (SF-PHON-02) | MED | C02, C11, CRQ-PHON-04 |
| O-PHON-03 | Wizard apply is non-elevated and the wizard model is system-only, which mitigates X1 (SF-PHON-03) | MED | C07 |
| O-PHON-04 | Flag is searchable, giving a bulk enumeration oracle (SF-PHON-04) | MED | C06, CRQ-PHON-06 |
| O-PHON-05 | Hard delete available to admins despite archive-only API (SF-PHON-06) | MED | C13, CRQ-PHON-07 |
| O-PHON-06 | All eight metadata loaders are version-gated (C20 correction) | LOW | C20 |
| O-PHON-07 | No consent/lawful-basis/company/channel attributes on suppression entries | MED | C03, CRQ-PHON-01 |

## 6. Lane B classification

No Lane B evidence was supplied. Absence is never a FAIL.

| Class | Claims |
|---|---|
| NOT_APPLICABLE (internal structure, not user-surface observable) | C01, C05, C10, C20 |
| UNCORROBORATED (user-surface observable, no Lane B yet; source-verified) | C04, C08, C12, C13, C17, C18, C19 |
| MISSING_REQUIRED_RUNTIME_PROOF (inherently runtime; see §7) | C02 (with SF-PHON-01/02), C03, C06/C07 (X1), C09, C11, C14, C15, C16, C05 reachability (X2) |

## 7. Proof requirements

| ID | Claim(s) | Setup / action | Expected (if A1/A2 reading holds) | Fail condition (reading falsified) |
|---|---|---|---|---|
| PR-PHON-01 | SF-PHON-01, C02, BR6 | Admin user with a valid personal phone N_u. (a) Call list add with an unformattable string. (b) Call the mixin set-blacklisted helper on a record with no phone. | An active entry equal to N_u's canonical form exists after (a) and after (b). Its audit trail shows no reference to the submitted input. | No entry for N_u is created or reactivated; the call is rejected with a validation error or a no-op. |
| PR-PHON-02 | C07, X1, SF-PHON-03 | Internal non-admin user opens the unblacklist wizard through a direct action/URL (bypassing the record entry point) with a default phone of an active entry, enters a reason, applies. | An access error at wizard save or at list access; the entry stays active. | The entry becomes archived, or the reason is posted. |
| PR-PHON-03 | C05, X2 | In a deployment with the SMS/marketing modules installed, a non-admin internal user uses every UI action that marks or unmarks a record's number as blacklisted. | At least one path changes the global list for a non-admin (the bypass is reachable). | No non-admin path changes list state; C05 RISK is theoretical in that module set. |
| PR-PHON-04 | C03 | Two companies A and B. Admin in A blacklists N. A contact with N exists in B; a B-only user views it. | The contact in B shows blacklisted = true. Un-blacklisting from B re-enables it in A. | The flag is false in B, or a company-scoped entry exists. |
| PR-PHON-05 | C09, C14, C02 | Runtime without the phone library. Add "abc 123", "+66 81 234 5678" and "+66812345678" to the list; search the list for "abc". | Three distinct raw entries are stored; the search matches the raw "abc 123" entry; one info log line is written. | An input is rejected or normalized; the two +66 forms collapse to one entry. |
| PR-PHON-06 | C15 | A model with both mobile and phone fields. Record R1: mobile M blacklisted, phone P not. Record R2: mobile M2 not blacklisted, phone P2 blacklisted. | R1: overall flag true, per-phone flag false. R2: overall flag false even though P2 is on the list. | R2 overall flag true (all numbers evaluated). |
| PR-PHON-07 | C11 | A model declaring two partner fields whose partners have different countries C1 (first) and C2 (last); record without its own country; national-format number. | The sanitized number is interpreted in C2's numbering plan. | It is interpreted in C1's plan or the company's. |
| PR-PHON-08 | C16 | Same data with and without the sanitized-number index; combined phone search using an E.164 term for a record stored only in national format. | Found with the index; not found without it. | Same result in both states. |
| PR-PHON-09 | C17, GAP-PHON-02 | A portal user deletes their own account with the blacklist request option, through the standard portal flow. | An entry is created and the log names the acting and portal users. If the flow is not elevated, an access error rolls back the deactivation. Record which outcome occurs. | The deactivation succeeds but no entry is created and no error is shown (silent loss of the opt-out). |
| PR-PHON-10 | SF-PHON-02, C02 | Two admins whose own countries differ each add the same national-format digits. | Two different canonical entries exist. | A single entry exists, or the second add is rejected as a duplicate. |

Count: 10 proof requirements.

## 8. Limitations

- Static source only; no runtime system. Findings SF-PHON-01..04 are A2 inferences from control flow and need PR execution before REC treats them as confirmed.
- Callers outside this module (SMS, mass mailing, portal deactivation in base, web client toggles) were not read. Reachability statements are bounded to this module.
- Whether the current partner model in the anchor still declares a separate mobile field was not checked. PR-PHON-06 therefore specifies "a model with both fields".
- JS/static assets, tests and vendored metadata files were not reviewed (A1 GAP-PHON-01/07 stand).
- Bank used only as a topic lens; no QID answered. No percentages, no Formal Coverage, no git operations. Clean room: neutral description, no code reproduced.
