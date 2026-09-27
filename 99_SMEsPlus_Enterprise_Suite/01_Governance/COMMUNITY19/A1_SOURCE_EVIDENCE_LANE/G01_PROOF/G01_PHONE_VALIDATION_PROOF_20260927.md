# G01 PLATFORM_BASE — RED TEAM Proof Package — `phone_validation`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller (Stage 2 of a two-stage REC + PROOF run) |
| Group / Module | G01 PLATFORM_BASE / `phone_validation` |
| Date | 2026-09-27 |
| Upstream REC | `G01_RECONCILIATION/G01_PHONE_VALIDATION_REC_20260927.md` (29 REC items: MATCH 10, CONTRADICTION 3, UNKNOWN_PENDING_PROOF 13, GAP 3) |
| Inputs (sha256 at intake 15:04:27 UTC) | A1 `e128cb2e…c003b0`; A2 `60bccae9…33ec`; Lane A `069aca00…b888`; bank `c70aae33…0a50b8a80` equals FREEZE_W1-B10 `bank_files`; freeze hash `0d7f6e94acde38662de420f8947ffaa1ab04cddaaec43516e46b441ce1222010`; manifest `049aa570…56d8` |
| Predeclaration | Scratchpad `rec_phon_priv/proof_cases_predeclared.txt` (covers both modules), written 2026-09-27 15:05:54 UTC, sha256 `cf3bdecebb7417c002a0eaa9790c1023c891e581ededc99e43c4245a2a20ea83` hashed 15:06:04 UTC. **No source was fetched in this run before that point**; first fetch 15:06:05 UTC |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`, fetched 2026-09-27 15:06:04–05 UTC; every module blob verified with `git hash-object` (section 2) |
| Runtime device | THPATTARAKRIT-SOLUTION-SERVICE-2.local: **OFFLINE** at 2026-09-27 15:08:20 UTC (`getent hosts` rc=2; `curl` rc=6 "Could not resolve host") |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** |

Clean-room note: results are neutral paraphrases of observed source behaviour. Identifiers are evidence pointers only. No vendor code is reproduced. No percentages. No Formal Coverage claim. No git operations. Inputs were not edited. Source copies stay in the scratchpad (`rec_phon_priv/src/`, blob log `rec_phon_priv/blob_log.txt` sha256 `4ce5687c…11fc`).

## 1. Case design

- The 10 A2 proof requirements PR-PHON-01..10 become **runtime cases PC-PHON-01..10**, one to one; setup, expected and fail are A2 §7 unchanged and restated in section 4.
- The static prediction basis for each PR (and for REC contradictions) becomes **SOURCE / CONFIG / CROSS-MODULE static cases PC-PHON-11..26**, predeclared and **executed now**. Priority: PR-PHON-01 (PC-11..15).
- A static PASS confirms only that the source reads as predicted. **It is never counted as a result for the linked runtime case.**
- Layers: SOURCE = module code; CONFIG = ACL/data/view/manifest; CROSS-MODULE = base code read statically; RUNTIME = disposable database built from the anchor.

## 2. Blob verification (executed)

| File (under `addons/phone_validation/` unless noted) | Expected blob (Lane A) | Computed `git hash-object` | Result |
|---|---|---|---|
| `__manifest__.py` | 323499d9… | 323499d990f7f0184e99d93648ef7d616b111972 | MATCH |
| `tools/phone_validation.py` | bf983464… | bf9834646506a2a3fe05a08e4dcc26cd4e4941df | MATCH |
| `models/phone_blacklist.py` | d94486f6… | d94486f63734da6dd4abdbcd6c21f407466c8142 | MATCH |
| `models/mail_thread_phone.py` | 01ca256f… | 01ca256f3e6cd7894eab0e3128bd931c5498697a | MATCH |
| `models/models.py` | dccf9fbf… | dccf9fbf8edb7f7add7583b1df7585c451ad108f | MATCH |
| `models/res_partner.py` | 9d240af4… | 9d240af46e94818be906dc6eee2eb871bab3c3ac | MATCH |
| `models/res_users.py` | ca7def5e… | ca7def5ec755c9a2d698204521953bbabf39d4f4 | MATCH |
| `wizard/phone_blacklist_remove.py` | e882a7a3… | e882a7a36c636fd28ea7fd9efca09fb738e5dcba | MATCH |
| `security/ir.model.access.csv` | fe442d04… | fe442d04d2d37de099e3e9bb753478058b0a1a2a | MATCH |
| `views/phone_blacklist_views.xml` | e8a3183e… | e8a3183ed946f079ab4636bfa17f891fa7dc647e | MATCH |
| `wizard/phone_blacklist_remove_view.xml` | 329009be… | 329009bedf3dd6140137c9d7aa9d92e811d1ce03 | MATCH |
| `lib/phonenumbers_patch/__init__.py` | 66fd4a88… | 66fd4a880f14b8844c29539b8ba30cb03fe36b48 | MATCH |
| `odoo/addons/base/models/res_users.py` (cross-module) | no prior lineage record | 9d42d77ae8ec19028c99b3c668294569ded3a86a | RECORDED (fetched at anchor) |
| `odoo/addons/base/models/res_partner.py` (cross-module) | no prior lineage record | 502616ef7cb343716ce083465d390a04d0168b9c | RECORDED (fetched at anchor) |

12 of 12 module blobs match. 2 core files recorded at the anchor for the create-fallback path.

## 3. Static cases — executed (SOURCE / CONFIG / CROSS-MODULE)

Expected and fail conditions are quoted in substance from the predeclaration.

| Case | Layer | Links | Expected (predeclared) | Fail condition (predeclared) | Actual (observed, paraphrased) | Result |
|---|---|---|---|---|---|---|
| PC-PHON-11 | SOURCE | PR-01(a), O-01, REC-21 | add/_add format without raising and forward a possibly empty result into create, no guard | Empty values filtered or raised before create | The public add formats the input through the acting user's helper with raising off; an unformattable input yields an empty value. The internal add passes the list as-is to a lookup of existing entries and then to create, with no emptiness check | PASS |
| PC-PHON-12 | SOURCE + CROSS-MODULE | PR-01 core, O-01, C02 | create formats through a helper on the acting user's record; a falsy number makes the helper read that record's number field | Helper returns empty/raises on falsy input, or create is user-independent | create calls the generic formatter on the current user's record with raising on. The formatter, when no number is given, requires a singleton and takes the first non-empty value among that record's number fields, then formats it. Result: the acting user's own number becomes the entry's value. If the user has no number, the formatter returns empty **even with raising on**, so create proceeds with an empty value into a required field | PASS |
| PC-PHON-13 | CROSS-MODULE | PR-01 precondition | User model exposes a discoverable number field; no override empties discovery | No field, or override returns none | The generic discovery returns "mobile"/"phone" when present. At the anchor the base user model exposes "phone" through partner delegation; base partner/user define no "mobile" field. No override of discovery for users exists in this module. (Other installed modules were not read) | PASS |
| PC-PHON-14 | SOURCE | PR-01(b), C05 | Set helper passes sanitized value(s) to list add under sudo, no guard | Guard skips empty sanitized | The set helper sends every record's sanitized value (empty when none) to the internal add under sudo; the reset helper does the same to the internal remove. No guard. Sudo does not change the acting user, so the fallback in PC-12 still resolves to the acting user | PASS |
| PC-PHON-15 | SOURCE | O-01 spread, C14 | Write with empty number and search with empty term reach the same fallback, unguarded | Guarded | Write reformats any submitted number value through the acting user's formatter with raising on, so an empty value resolves to the user's own number. The number search maps each term to its formatted value or the raw term; an empty term resolves to the user's number | PASS |
| PC-PHON-16 | SOURCE + CROSS-MODULE | PR-10, O-02 | Country for canonicalization comes from the acting user record, then its partner fields, then current company | Fixed/explicit country or the entry record drives it | All list formatting calls run on the acting user record with no explicit country. Country resolution: the record's country field (present on users through partner delegation), else linked partner fields (discovery helper lives in mail, not read), else the current company's country | PASS |
| PC-PHON-17 | SOURCE | O-04, C06 | Flag search joins active entries in raw SQL; field limited to internal users; id-domain result | No search, or system-group restriction | The "blacklisted" flag declares a search method that runs raw SQL joining the model table with active list rows (and an anti-join for "not in") and returns an id domain. Both flag fields carry the internal-user group, not the system group. Flag compute uses sudo, with a TODO comment | PASS |
| PC-PHON-18 | SOURCE + CONFIG | PR-02, O-03, C07, X1 | Wizard apply not elevated; wizard ACL system-only; entry-point pre-check and comment present | Apply elevated, or non-system wizard ACL | Wizard apply calls the internal remove without sudo. ACL grants the wizard to the system group only. The record entry point checks list write access and raises otherwise; the comment says wizard rights "currently not working as expected". The list model's own open-wizard method has no pre-check (the list itself is system-only) | PASS |
| PC-PHON-19 | SOURCE | PR-05, C09, C14 | Import-failure branch returns raw input with a once-per-process info log; search raw fallback | Raises or rejects | On import failure, parse returns False and format returns the input unchanged, logging one info line guarded by a module-level flag. The model wrapper therefore stores the raw input as "formatted". Search falls back to the raw term | PASS |
| PC-PHON-20 | SOURCE | PR-06, C15 | First formattable field; per-field loop overwrites; overall flag uses sanitized value only | All fields evaluated | Sanitized value = first number field that formats (loop breaks on success). The overall flag compares only that value with the list. The per-field loop assigns on every iteration with no break, so the last field decides | PASS |
| PC-PHON-21 | SOURCE | PR-07, C11 | Partner-field loop has no break; company fallback | Break on first match | After the record's own country, the loop over partner fields assigns the first partner's country for each field with no break, so the last field with a country wins; company country is the final fallback | PASS |
| PC-PHON-22 | SOURCE | PR-08, C16 | Sanitized field skipped when index missing (TODO); min length 3 | No index-dependent branch | The searched set always appends the sanitized field; it is removed when its index is absent (TODO comment). An error is raised only if the set is then empty. Minimum length 3 enforced for non-empty terms | PASS |
| PC-PHON-23 | SOURCE + CROSS-MODULE | PR-09, C17, GAP-02 | Override adds without sudo; base defines the hook; caller elevation recorded | Override elevates | The override collects the user's formatted numbers, calls the base hook, then calls the internal add in the current environment without sudo and logs a message naming the acting and portal users. The base hook exists in base users; it archives the user as superuser but the blacklist call is after it and not elevated. The portal controller that invokes the hook was not read, so the caller's elevation is **not established** | PASS (static only; GAP-02 open) |
| PC-PHON-24 | CONFIG | C04, O-05 | 3 rows; zero row for all; system full CRUD incl. unlink on list and wizard | Other | Exactly three rows: an all-zero row with no group on the list; system group full rights (incl. unlink) on the list and on the wizard | PASS |
| PC-PHON-25 | SOURCE | C12, C13 | Add searches incl. archived and reactivates; remove archives and creates unknown numbers archived | Otherwise | Create searches with the active filter off and reactivates archived entries unless asked to keep them inactive; only missing numbers are created. Remove archives found entries and creates unknown numbers archived | PASS |
| PC-PHON-26 | SOURCE | C20, O-06 | All eight loaders version-gated; BR/MX hooks version-gated | Any loader unconditional | Each of the eight region loaders (CI, CO, IL, MA, MU, PA, SN, KE) is registered only within a library-version condition. BR and MX hooks are registered always but select local metadata / append formats by version | PASS |

**Static totals: 16 executed — PASS 16, FAIL 0.**

### 3.1 PR-PHON-01 result (priority)

Static path **confirmed end to end** (PC-11, PC-12, PC-13, PC-14, PC-15 all PASS): an unformattable number given to the public add, or a record without a sanitized number given to the sudo set helper, reaches create as an empty value; create's formatter runs on the acting user's record and, finding no number, substitutes that user's own phone; the entry for the acting user's number is created or reactivated. Runtime confirmation (PC-PHON-01) is **NOT-EXECUTED**. Static PASS is not a runtime result.

### 3.2 Refinements observed (for A3; they do not change any verdict)

- R1 (PC-11, PC-15; mirror of SF-PHON-01): the same fallback applies on the **removal** side. The public remove with an unformattable number, and the reset helper on a record without a sanitized number, look up existing entries with an empty term, which resolves to the acting user's number. The acting user's entry is then archived (un-suppressed), or created archived if absent. A2 did not state this direction. Relevant to Q013.
- R2 (PC-11): the lookup of existing entries inside the internal add also resolves the empty value to the acting user's number, so a supplied message is logged on the acting user's existing entry.
- R3 (PC-12): with no number on the acting user, the formatter returns empty even with raising on; the failure then comes from the required-field check, not from validation. Consistent with A2.
- R4 (PC-18): wizard apply passes the raw wizard phone to the internal remove (the public remove's pre-sanitization is bypassed); sanitization happens later in search/create.
- R5 (PC-13): base partner/user define no "mobile" field at the anchor. A2's caveat for PR-PHON-06 ("a model with both fields") stands.

## 4. Runtime cases — NOT-EXECUTED (runtime unavailable)

Common preconditions: a disposable database built from the anchored source with `phone_validation` (and, for PC-03, SMS/marketing modules) installed; the `phonenumbers` library installed except in PC-05; named test users with known personal phone numbers and countries. Record verbatim outcomes. Status for all: **NOT-EXECUTED — runtime device THPATTARAKRIT-SOLUTION-SERVICE-2.local offline**. No result is inferred from the static cases.

| Case | Layer | Links (REC) | Steps (ready to run) | Expected | Fail condition | Status |
|---|---|---|---|---|---|---|
| PC-PHON-01 | RUNTIME | PR-01, REC-21, REC-02 | Admin U with valid personal phone N_u. (a) Call list add with an unformattable string. (b) Call the set-blacklisted helper on a mixin record with no phone. Inspect list entries and chatter | Active entry equal to canonical N_u after (a) and (b); audit shows no reference to the submitted input | No entry for N_u created or reactivated; call rejected with a validation error, or no-op | NOT-EXECUTED |
| PC-PHON-02 | RUNTIME | PR-02, REC-07, REC-23 | Internal non-admin opens the unblacklist wizard via direct action/URL with a default phone of an active entry, enters a reason, applies | Access error at wizard save or list access; entry stays active | Entry archived, or reason posted | NOT-EXECUTED |
| PC-PHON-03 | RUNTIME + CROSS-MODULE | PR-03, REC-05 | With SMS/marketing installed, a non-admin internal user uses every UI action that marks/unmarks a record's number as blacklisted | At least one path changes the global list for a non-admin | No non-admin path changes list state | NOT-EXECUTED |
| PC-PHON-04 | RUNTIME | PR-04, REC-03, REC-06 | Companies A and B. Admin in A blacklists N. Contact with N in B viewed by a B-only user; then unblacklist from B | B contact shows blacklisted; unblock from B re-enables in A | Flag false in B, or company-scoped entry | NOT-EXECUTED |
| PC-PHON-05 | RUNTIME + CONFIG | PR-05, REC-09, REC-14 | Without the phone library: add "abc 123", "+66 81 234 5678", "+66812345678"; search list for "abc" | Three raw entries; search hits "abc 123"; one info log line | Input rejected/normalized, or the +66 forms collapse | NOT-EXECUTED |
| PC-PHON-06 | RUNTIME | PR-06, REC-15 | Model with mobile and phone. R1: mobile M listed, phone P not. R2: mobile M2 not listed, phone P2 listed | R1 overall true, per-phone false. R2 overall false although P2 listed | R2 overall true | NOT-EXECUTED |
| PC-PHON-07 | RUNTIME | PR-07, REC-11 | Model with two partner fields, countries C1 (first) and C2 (last); record without own country; national-format number | Interpreted in C2's plan | C1's or company's plan | NOT-EXECUTED |
| PC-PHON-08 | RUNTIME | PR-08, REC-16 | Same data with and without the sanitized index; combined search with E.164 term for a record stored in national format | Found with index; not found without | Same result both states | NOT-EXECUTED |
| PC-PHON-09 | RUNTIME + CROSS-MODULE | PR-09, REC-17 | Portal user deletes own account with the blacklist option via the standard portal flow | Entry created and log names both users; or access error rolls back — record which | Deactivation succeeds, no entry, no error | NOT-EXECUTED |
| PC-PHON-10 | RUNTIME | PR-10, REC-22 | Two admins with different own countries each add the same national-format digits | Two different canonical entries | One entry, or duplicate rejection | NOT-EXECUTED |

**Runtime totals: 10 cases — NOT-EXECUTED 10, PASS 0, FAIL 0.**

## 5. Summary of results

| Layer | Cases | PASS | FAIL | NOT-EXECUTED |
|---|---|---|---|---|
| SOURCE (incl. SOURCE+CONFIG, SOURCE+CROSS-MODULE) | 14 | 14 | 0 | 0 |
| CONFIG | 1 (PC-24) | 1 | 0 | 0 |
| CROSS-MODULE (static) | 1 (PC-13) | 1 | 0 | 0 |
| RUNTIME (incl. runtime + cross-module/config) | 10 | 0 | 0 | 10 |
| **Total** | **26** | **16** | **0** | **10** |

REC item status after Proof:
- The 3 CONTRADICTION items (C07, C16, C20) are **source-confirmed on the A2 side** (PC-18, PC-22, PC-26). They remain CONTRADICTION for A3. C07's runtime effect is pending (PC-02).
- The 13 UNKNOWN_PENDING_PROOF items have their static prediction basis confirmed. **All remain UNKNOWN_PENDING_PROOF** until runtime cases run.
- The 10 MATCH items are unchanged. The 3 GAP items are carried forward.

## 6. Proposed additional runtime cases (post-execution; NOT predeclared; not part of this run's result set)

Declared after static execution, so they are recorded as proposals for the next Proof round only.
- PC-PHON-27 (proposed; O-04): an internal non-admin filters a mixin model by "blacklisted = true" and counts results. Expected: the full set of records with suppressed numbers is returned. Fail: filter refused or empty while entries exist.
- PC-PHON-28 (proposed; R1): admin U whose own number N_u is actively listed calls list remove with an unformattable string. Expected: N_u's entry becomes archived. Fail: N_u stays active and the call is rejected.

## 7. A3 eligibility

**Disposition: PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING.**

A3 can challenge **now** (static scope):
1. REC classifications and counts (29 items), the folds (GAP-02/03/04/05/06/08, O-06→C20) and the severity note (A2 rates SF-02/03/04 MED).
2. The 16 executed static cases, especially the PR-PHON-01 chain PC-11..15 and refinements R1–R5 (R1 wrong-subject un-suppression).
3. The 3 CONTRADICTION items (C07 incl. comment-vs-ACL, C16, C20).
4. Cross-module reasoning in PC-12/13/16/23 (reliance on base user/partner files; mail's partner-field helper and the portal controller not read).
5. QID lineage (39 mapped, 1 no evidence) under W1-B10 — **QID lineage is A3-eligible** (bank sha256 equals freeze entry; gate ELIGIBLE).
6. Input integrity, blob verification and predeclaration timing.

**Blocked** until the runtime device is available: all 10 runtime cases (notably PC-01 wrong-subject effect, PC-02 X1, PC-03 X2, PC-04 cross-company, PC-10 acting-user country); closing any UPP item; settling C07's runtime effect. Full A3 → MASTER handoff is **not** eligible yet; this package is eligible for **A3 static-scope challenge only**.

## 8. Limitations

- No runtime was executed and no runtime result is claimed.
- ORM behaviours (required-field enforcement, sudo/uid semantics, recompute timing) are outside files read and routed to runtime.
- Mail's partner-field discovery, the portal controller, SMS/marketing consumers, vendored metadata files, JS and tests were not read.
- No percentages, no Formal Coverage claim, no git operations. Inputs were not edited.
