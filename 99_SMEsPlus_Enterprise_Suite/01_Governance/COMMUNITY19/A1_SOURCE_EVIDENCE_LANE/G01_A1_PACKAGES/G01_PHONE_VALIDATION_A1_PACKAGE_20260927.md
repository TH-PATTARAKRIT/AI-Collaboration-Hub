# G01 PLATFORM_BASE — Module `phone_validation` — RED TEAM A1 Package

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A1 (source-backed research synthesizer) |
| Governed group / module | G01 PLATFORM_BASE / `phone_validation` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_PHONE_VALIDATION_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `069aca0017cae09ae1bddb28f46299671080d36ecbc869b5b1d1923cc998b888` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Freeze (topic lens only) | W1-B10, freeze_hash `0d7f6e94acde38662de420f8947ffaa1ab04cddaaec43516e46b441ce1222010`; bank `G01_PHONE_VALIDATION_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `c70aae33…0a50b8a80` (matches `FREEZE_W1-B10.json`); gate ELIGIBLE |
| Date | 2026-09-27 |
| Lane B dependency | None. A1 did not wait for, view, or use Lane B evidence. |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |

The bank is used only as a topic lens: canonical identity, country interpretation, blacklist lifecycle, scope, authority, search and audit. No QID is answered and the bank is not edited. All paths are relative to `addons/phone_validation/` at the anchor.

## 1. Claims

| Claim ID | Claim (neutral WHAT / WHY / RISK) | Evidence (path @ blob) | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-PHON-C01 | WHAT: hidden, auto-installed module depending on base and mail; it provides number validation/formatting, a phone blacklist and a phone mixin for records. No controllers, cron or settings. | `__manifest__.py` @ 323499d9 (Lane A only) | MED | SOURCE-STATIC |
| A1-G01-PHON-C02 | WHAT: the blacklist entry is unique at database level on its number value. Numbers are sanitized to canonical form on create, on write and in the add/remove API before storage. WHY: one entry per canonical identity. RISK: uniqueness is only as strong as the normalization (see C09). | `models/phone_blacklist.py` @ d94486f6 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-PHON-C03 | WHAT: the blacklist has no company or tenant dimension and no record rules. It is one database-wide list. RISK: a block set in one company's context applies in every company of the database. | `models/phone_blacklist.py` @ d94486f6; `security/ir.model.access.csv` @ fe442d04 (spot-checked: no company field, no rule file) | HIGH | SOURCE-STATIC |
| A1-G01-PHON-C04 | WHAT: data-layer access to the blacklist and to the unblacklist wizard is granted only to system administrators, with an explicit zero-permission row for everyone else. | `security/ir.model.access.csv` @ fe442d04 (spot-checked: 3 rows) | HIGH | SOURCE-STATIC |
| A1-G01-PHON-C05 | WHAT: the set-blacklisted and reset-blacklisted helpers on mixin records call the blacklist with elevated (sudo) rights. RISK: any code path that lets a non-admin trigger them on a record changes the global blacklist and bypasses C04. Which UI paths reach them is not visible here. | `models/mail_thread_phone.py` @ 01ca256f (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-PHON-C06 | WHAT: the blacklist state on records is computed with sudo, and a source comment explains that users without blacklist access could not compute it otherwise. WHY: the state is visible to internal users even though they cannot read the list. RISK: users can probe whether a number is on the list through record flags (a limited existence oracle, gated to internal users). | `models/mail_thread_phone.py` @ 01ca256f (spot-checked: comment + group restriction) | HIGH | SOURCE-STATIC |
| A1-G01-PHON-C07 | WHAT: the entry point that opens the unblacklist wizard from a record checks blacklist write access first. A source comment admits the wizard's own access rights are "currently not working as expected" and let users without access open it. RISK: the control is a pre-check at one entry point, not enforcement by the wizard itself. | `models/mail_thread_phone.py` @ 01ca256f (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-PHON-C08 | WHAT: numbers are validated as "possible" and "valid" with specific rejection reasons. One retry is made for too-long input with a 00/+ prefix variant. WHY: to reject malformed input and not silently coerce it. | `tools/phone_validation.py` @ bf983464 (spot-checked: parse/possible/valid path) | HIGH | SOURCE-STATIC |
| A1-G01-PHON-C09 | WHAT: when the phonenumbers library is missing, parsing yields nothing, formatting returns the raw input unchanged, and a single info-level log line is written. RISK: sanitized values and blacklist entries become unvalidated raw strings. Canonical uniqueness (C02) and matching degrade silently, with only an info log. | `tools/phone_validation.py` @ bf983464 (spot-checked: import fallback branch) | HIGH | SOURCE-STATIC |
| A1-G01-PHON-C10 | WHAT: output format is E.164/RFC3966 when forced, INTERNATIONAL when forced or when the country code differs from the target country, and NATIONAL otherwise. | `tools/phone_validation.py` @ bf983464 (Lane A detail; format branch seen) | MED | SOURCE-STATIC |
| A1-G01-PHON-C11 | WHAT: country resolution order is (1) the record's own country field; (2) the country of a linked mail partner field; (3) the current company's country. In step 2 the loop over partner fields does not stop at the first match, so the last partner field with a country wins. RISK: the same number can be interpreted differently depending on which linked-partner fields a model declares. | `models/models.py` @ dccf9fbf (spot-checked: no break in partner loop; company fallback) | HIGH | SOURCE-STATIC |
| A1-G01-PHON-C12 | WHAT: blacklist add collapses duplicates, finds existing entries including archived ones, and reactivates archived entries (unless told to keep them inactive). Only missing numbers are created. WHY: one logical identity across archive cycles. | `models/phone_blacklist.py` @ d94486f6 (spot-checked: inactive-inclusive search) | HIGH | SOURCE-STATIC |
| A1-G01-PHON-C13 | WHAT: blacklist remove archives, never deletes. A number not yet known is created archived, as an explicit "unblocked" record. The optional reason is recorded through tracking or an internal note. | `models/phone_blacklist.py` @ d94486f6 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-PHON-C14 | WHAT: search by number sanitizes the term, but falls back to the raw term when sanitizing fails. RISK: invalid search input matches raw stored strings (relevant when C09 applies). | `models/phone_blacklist.py` @ d94486f6 (spot-checked: "or value" fallback) | HIGH | SOURCE-STATIC |
| A1-G01-PHON-C15 | WHAT: records get one stored sanitized number, taken from the first phone field that formats successfully. A source comment says the "phone is blacklisted" flag is a heuristic that may be wrong when both phone and mobile exist. In the flag's loop each field overwrites the previous result, so only the last number field decides. RISK: a secondary number can be blocked but reported as not blocked. | `models/mail_thread_phone.py` @ 01ca256f (spot-checked: comment + loop) | HIGH | SOURCE-STATIC |
| A1-G01-PHON-C16 | WHAT: combined phone search requires at least 3 characters, treats +/00 as equivalent and strips separators. It raises an error on models with no phone fields, and skips the sanitized field when its index is missing (TODO). RISK: results can differ between databases depending on upgrade/index state. | `models/mail_thread_phone.py` @ 01ca256f (min length + TODO spot-checked; rest Lane A) | MED | SOURCE-STATIC |
| A1-G01-PHON-C17 | WHAT: when a portal account is deactivated with a blacklist request, the account's formatted numbers are added to the blacklist, and a log names the acting user and the portal user. No sudo is used in this module. Success depends on the caller's rights (C04). | `models/res_users.py` @ ca7def5e (spot-checked: no sudo) | HIGH | SOURCE-STATIC |
| A1-G01-PHON-C18 | WHAT: blacklist number and active flag are tracked through chatter, and the add/remove API records messages. WHY: an audit trail of lifecycle changes. RISK: whether each operation (add vs reactivate vs remove) can be told apart depends on the message text, not on a dedicated event type. | `models/phone_blacklist.py` @ d94486f6 (spot-checked: tracking + message posting) | MED | SOURCE-STATIC |
| A1-G01-PHON-C19 | WHAT: changing a partner's phone reformats it to INTERNATIONAL when possible and keeps the raw input otherwise. | `models/res_partner.py` @ 9d240af4 (Lane A only) | MED | SOURCE-STATIC |
| A1-G01-PHON-C20 | WHAT: numbering metadata is overridden locally for a fixed set of countries (8 loaders plus 2 version-gated format hooks). WHY: to correct upstream library metadata. RISK: interpretation depends on the library version and the vendored files. | `lib/phonenumbers_patch/__init__.py` @ 66fd4a88 (Lane A only) | MED | SOURCE-STATIC |

## 2. Business rules (source-derived, neutral)
- BR1: One blacklist entry per stored (sanitized) number value across the whole database (C02, C03).
- BR2: Blacklist removal is a soft state change (archive), never a hard delete, through the API (C13).
- BR3: Re-adding an archived number reactivates the same entry (C12).
- BR4: Only system administrators may read or change the blacklist directly. Record-level helpers bypass this with elevated rights (C04, C05).
- BR5: Country for interpretation: record country, then linked-partner country (last match wins), then company country (C11).
- BR6: Formatting failure on records is silent by default (returns no value). Direct blacklist create/write raises an error (C02; Lane A #14).

## 3. States / transitions
- Blacklist entry: absent → active (add) → archived (remove) → active (re-add). Absent → archived (remove of unknown number) (C12, C13).
- Record flag: not blacklisted ↔ blacklisted, derived live from the sanitized number and the active entries; not stored (C06, C15).
- Sanitized number: recomputed when phone fields, the country field or stored partner fields change (Lane A #20).

## 4. Exceptions / failure modes
- Invalid/impossible number on blacklist create or write → user error with a reason (C08).
- Duplicate stored number → database uniqueness error "Number already exists" (C02).
- Unblacklist wizard opened without write access → access error at the record entry point only (C07).
- Phone search on a model without phone fields → error; search term under 3 characters → restricted (C16).
- Library absent → silent raw passthrough with one info log (C09).

## 5. Cross-module handoffs
- mail: chatter, tracking, partner-field discovery used for country resolution (C11, C18).
- base: helpers injected into every model; partner and users extended (C17, C19).
- Portal deactivation hook defined outside this module (C17; Lane A G2).
- Downstream SMS/marketing consumers are expected to read the blacklist flags. This is not verified here and the owner modules are not identified.
- No edge to `privacy_lookup`: its lookup does not search phone fields or this blacklist (per privacy_lookup Lane A packet, section 3).

## 6. Evidence gaps (Lane A carried forward + A1)
- GAP-PHON-01 (Lane A G1): vendored per-region metadata content not fetched.
- GAP-PHON-02 (Lane A G2): base portal-deactivation privilege context unknown.
- GAP-PHON-03 (Lane A G3): runtime meaning of the wizard access-rights comment unresolved (C07).
- GAP-PHON-04 (Lane A G4): whether "last partner country wins" is intended is undocumented (C11).
- GAP-PHON-05 (Lane A G5): accuracy limit of the blacklist heuristic (C15).
- GAP-PHON-06 (Lane A G6): search results differ when the index is missing (C16).
- GAP-PHON-07 (Lane A G7): JS/static assets and tests not reviewed.
- GAP-PHON-08 (A1): which UI/server paths let non-admins invoke the sudo set/reset helpers (C05) is not visible in this module.
- GAP-PHON-09 (A1): concurrency behavior of simultaneous add/remove on one number (beyond the DB unique constraint) is not assessable statically.

## 7. CRQ candidates
- CRQ-PHON-01: Must the phone suppression list be scoped per tenant/company, or is it explicitly shared, and who decides? (C03)
- CRQ-PHON-02: Must every path that changes suppression state enforce the same authority as direct list access? (C04, C05, C07)
- CRQ-PHON-03: Must the system refuse to store suppression identities when canonical validation is unavailable, rather than store raw text? (C09, C14)
- CRQ-PHON-04: What deterministic, documented precedence governs country resolution when several linked parties have countries? (C11)
- CRQ-PHON-05: Must every phone field on a record be evaluated against suppression, not only one canonical number? (C15)
- CRQ-PHON-06: Should suppression status be visible to users who cannot read the list, and under what rule? (C06)
- CRQ-PHON-07: Must audit events distinguish add, reactivate, archive and remove as typed events? (C18)
- CRQ-PHON-08: Must search correctness be independent of index/upgrade state? (C16)

## 8. Contradictions
- None CONFIRMED-FROM-SOURCE. All Lane A statements in the spot-check log matched source.
- CANDIDATE-PHON-X1: The ACL restricts the unblacklist wizard to administrators (C04), but a source comment says the wizard's access rights let users without access open it (C07). Enforcement is a code comment against the declared ACL; runtime behavior is unresolved (GAP-PHON-03).
- CANDIDATE-PHON-X2: The admin-only data layer (C04) sits beside the sudo record helpers that change the same global list (C05). This is a design tension; reachability is unverified (GAP-PHON-08).

## 9. Spot-check log
Re-fetched from `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/phone_validation/<path>`; `git hash-object` computed on the scratchpad copy (no repository git operations).

| # | Path | Recorded blob | Computed blob | Match | Content verified |
|---|---|---|---|---|---|
| 1 | `models/phone_blacklist.py` | d94486f63734da6dd4abdbcd6c21f407466c8142 | d94486f63734da6dd4abdbcd6c21f407466c8142 | YES | C02 unique on number + sanitize on create/write; C03 no company field; C12 inactive-inclusive lookup; C13 archive on remove; C14 raw fallback in search |
| 2 | `security/ir.model.access.csv` | fe442d04d2d37de099e3e9bb753478058b0a1a2a | fe442d04d2d37de099e3e9bb753478058b0a1a2a | YES | C04: zero row for all, full CRUD system-only on list and wizard |
| 3 | `models/mail_thread_phone.py` | 01ca256f3e6cd7894eab0e3128bd931c5498697a | 01ca256f3e6cd7894eab0e3128bd931c5498697a | YES | C05 sudo set/reset; C06 sudo compute + comment; C07 access-rights comment + pre-check; C15 heuristic comment + overwrite loop; C16 min length 3 + TODO |
| 4 | `tools/phone_validation.py` | bf9834646506a2a3fe05a08e4dcc26cd4e4941df | bf9834646506a2a3fe05a08e4dcc26cd4e4941df | YES | C08 possible/valid checks; C09 import fallback returns raw input, one info log |
| 5 | `models/models.py` | dccf9fbf8edb7f7add7583b1df7585c451ad108f | dccf9fbf8edb7f7add7583b1df7585c451ad108f | YES | C11: partner-field loop has no break; company-country fallback |
| 6 | `models/res_users.py` | ca7def5ec755c9a2d698204521953bbabf39d4f4 | ca7def5ec755c9a2d698204521953bbabf39d4f4 | YES | C17: add without sudo; log names acting and portal user |

Result: 6 of 6 blobs match, 0 mismatches.

## 10. Provenance
- Input: the Lane A packet (sha256 above), consumed read-only.
- Spot-check fetches: the anchor commit above via raw.githubusercontent. Files were held in the session scratchpad only.
- Topic lens: frozen bank W1-B10 (bank sha256 verified against the freeze manifest). No QID answered.
- No Lane B material, no runtime system and no other lane packets were consulted, except the privacy_lookup Lane A packet for the cross-module edge note.

## 11. Limitations
- Source presence does not mean runtime reachability. Nothing here is runtime proof.
- No Formal Coverage claim, no percentages, no QID answers.
- Clean room: neutral WHAT/WHY/RISK only. Identifiers are evidence pointers, not design recommendations. No code, schema, ORM or workflow reuse.
- Claims marked "Lane A only" were not re-read by A1 (MED confidence).
- Single anchor commit. Library-version-dependent behavior (C20) is not evaluated.
