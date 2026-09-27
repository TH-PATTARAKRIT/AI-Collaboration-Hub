# G01 PLATFORM_BASE — LANE A PASS-1 — Module `phone_validation`

| Field | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Slot | T3 (refill) |
| Governed group | G01 PLATFORM_BASE |
| Module | `phone_validation` (roster member per FREEZE_W1-STD.json) |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` — `addons/phone_validation/` |
| Retrieval | raw.githubusercontent.com at the anchor commit. Files found through the manifest and the `__init__` import chains |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** (JS/static assets and vendored region metadata files skipped; see gaps) |
| Clean-room | Neutral WHAT/WHY/RISK only. No code, schema or workflow is reproduced. Identifiers appear only as pointers. |

## 1. Evidence Pointer Table (18 blobs; SHA-1 = `git hash-object`)

| Path (addons/phone_validation/…) | git blob SHA-1 | Purpose |
|---|---|---|
| `__manifest__.py` | 323499d990f7f0184e99d93648ef7d616b111972 | Identity, deps, data list, auto_install |
| `__init__.py` | 252bfcd472dcb99926b81c6e341c8698bb4ac240 | Imports lib, tools, models, wizard |
| `lib/__init__.py` | 1ffdbb394c9c6adf971811c8fdfd3c7dc9c2c26d | Imports the metadata patch package |
| `lib/phonenumbers_patch/__init__.py` | 66fd4a880f14b8844c29539b8ba30cb03fe36b48 | Country-specific numbering metadata overrides |
| `tools/__init__.py` | 1c27cd6ebed3b20ef30b7b1d467287cf6d18f007 | Imports the helper module |
| `tools/phone_validation.py` | bf9834646506a2a3fe05a08e4dcc26cd4e4941df | Parse/format helpers, fallback when the library is missing |
| `models/__init__.py` | 08a4ade5f15a3d30a3b53dbbd7f7fcb00328970d | Model import list |
| `models/phone_blacklist.py` | d94486f63734da6dd4abdbcd6c21f407466c8142 | Blacklist entity, add/remove API |
| `models/mail_thread_phone.py` | 01ca256f3e6cd7894eab0e3128bd931c5498697a | Phone mixin: sanitized field, blacklist flags, search, indexes |
| `models/models.py` | dccf9fbf8edb7f7add7583b1df7585c451ad108f | Generic helpers on every model: number fields, country resolution, formatting |
| `models/res_partner.py` | 9d240af46e94818be906dc6eee2eb871bab3c3ac | Partner gets the mixin; formats phone on change |
| `models/res_users.py` | ca7def5ec755c9a2d698204521953bbabf39d4f4 | Blacklists phone numbers when a portal account is deactivated |
| `wizard/__init__.py` | 7d23a79178e11aab2648de6f8d1b2dc14ae9a0ad | Wizard import |
| `wizard/phone_blacklist_remove.py` | e882a7a36c636fd28ea7fd9efca09fb738e5dcba | Unblacklist wizard with a reason |
| `security/ir.model.access.csv` | fe442d04d2d37de099e3e9bb753478058b0a1a2a | ACL (3 rows) |
| `views/phone_blacklist_views.xml` | e8a3183ed946f079ab4636bfa17f891fa7dc647e | Blacklist list/form/search, action, technical menu |
| `views/res_partner_views.xml` | 3fbc1c58bed88524bce03c7347c3a98cebc7346d | Partner search filter uses the combined phone search |
| `wizard/phone_blacklist_remove_view.xml` | 329009bedf3dd6140137c9d7aa9d92e811d1ce03 | Unblacklist wizard form |

Not present at anchor (404): `controllers/__init__.py`. The module has no controllers.

## 2. Findings by card section

### 2.1 Manifest / dependencies / purpose
1. Category Hidden, version 2.1, auto_install, LGPL-3. It depends on `base` and `mail`. [`__manifest__.py`]
2. Stated purpose: validate and format phone numbers for a destination country, manage a phone blacklist, and provide a mixin that sanitizes numbers and computes blacklist state on records. [`__manifest__.py`]
3. Load order: the metadata patch (lib) loads before tools, models and wizard. [`__init__.py`, `lib/__init__.py`]

### 2.2 Data (models, mixins, fields, constraints)
4. `phone.blacklist` is a persistent entity with a tracked, required number and a tracked active flag. The number is shown as the record name, and its help text expects E.164 format. It inherits chatter (`mail.thread`). [`models/phone_blacklist.py`]
5. **Identity and uniqueness:** a database-level unique constraint on the number, with the message "Number already exists". Because numbers are sanitized before create and write, uniqueness applies to the normalized form, not to raw input. [`models/phone_blacklist.py`]
6. `mail.thread.phone` is an abstract mixin on top of `mail.thread`. It adds four fields:
   - a stored sanitized number, computed with sudo;
   - two non-stored blacklist booleans, computed with sudo and restricted to `base.group_user`;
   - a non-stored search-only phone/mobile field.

   It sets a minimum search length of 3. [`models/mail_thread_phone.py`]
7. On concrete tables, the mixin's init creates expression indexes on the phone fields with separators stripped: a btree index, plus a trigram GIN index when trigram support exists. [`models/mail_thread_phone.py` `init`]
8. Generic model helpers:
   - number fields default to `mobile`/`phone` when present;
   - the country field defaults to `country_id`;
   - the formatter defaults to E.164.

   [`models/models.py`]
9. `res.partner` inherits the phone mixin. [`models/res_partner.py`]
10. `phone.blacklist.remove` is a transient wizard with a required read-only phone and an optional reason. [`wizard/phone_blacklist_remove.py`]

### 2.3 Business rules / states / exceptions
11. **E.164 normalization:**
    - Numbers are parsed twice: once, then again after international formatting, so that the metadata patches apply.
    - A number must be both "possible" and "valid", or a UserError is raised with a reason: invalid country prefix, too short, too long, or wrong prefix.
    - When a number is too long, the parser retries once with a leading `00` rewritten, or with a `+` added, before failing. The final error still shows the original input.

    [`tools/phone_validation.py` `phone_parse`]
12. Output format choice:
    - E.164 and RFC3966 are used when forced.
    - INTERNATIONAL is used when forced, or when the number's country code differs from the target country's code.
    - Otherwise NATIONAL is used.

    [`tools/phone_validation.py` `phone_format`]
13. **Country resolution order:**
    1. the record's own country field;
    2. otherwise the country of any linked mail partner. The loop does not stop at the first hit, so a later partner field can override an earlier one;
    3. otherwise the current company's country.

    [`models/models.py` `_phone_get_country`, `_phone_format`]
14. Formatter failure: by default it returns False (error suppressed), and it raises only when explicitly asked. [`models/models.py` `_phone_format_number`]
15. **Behavior when the phonenumbers library is absent:**
    - parsing returns False;
    - formatting returns the raw input unchanged and logs a single info message;
    - region lookups return empty values;
    - the metadata patch does nothing.

    **RISK:** without the library, "sanitized" values and blacklist entries hold unvalidated raw strings, which weakens uniqueness and matching. [`tools/phone_validation.py`, `lib/phonenumbers_patch/__init__.py`]
16. Metadata overrides:
    - local region loaders replace the library defaults for CI, CO, IL, MA, MU, PA, SN and KE;
    - additional format hooks exist for BR and MX, gated on the library version.

    [`lib/phonenumbers_patch/__init__.py`]
17. **Blacklist add:** input is sanitized using the current user's context (country fallback). Duplicates in the batch are collapsed. Existing entries, including archived ones, are found. Archived entries are reactivated unless the caller explicitly asks for them to stay inactive. Only missing numbers are created. The result keeps the order of the request. [`models/phone_blacklist.py` `create`, `_add`, `add`]
18. **Blacklist remove:** matching entries are archived, not deleted. A number that is not yet known is created in the archived state, which leaves a record that the number was unblocked. An optional message is logged through tracking, or posted as an internal note on new records. [`models/phone_blacklist.py` `_remove`, `remove`]
19. Write re-sanitizes a changed number, and invalid input raises a UserError that asks the user to correct it. Searching by number sanitizes the search term first. [`models/phone_blacklist.py` `write`, `_search_number`]
20. Mixin compute:
    - The sanitized number is the first phone field that formats successfully. It is recomputed when phone fields, the country field or stored partner fields change.
    - The "blacklisted" flag is true when the sanitized number matches an entry.
    - The "phone is blacklisted" flag relies on a documented heuristic, and the code admits it can be inaccurate when a model has both mobile and phone numbers.

    [`models/mail_thread_phone.py`]
21. The blacklist-state search supports only in / not in, and uses raw SQL that joins active blacklist rows. The combined phone search:
    - handles + and 00 equivalence;
    - strips separators;
    - requires at least 3 characters;
    - raises an error if the model defines no phone fields;
    - leaves out the sanitized field when its index is missing (marked TODO).

    [`models/mail_thread_phone.py`]
22. Changing the phone on a partner reformats it to INTERNATIONAL when the formatter succeeds, and keeps the raw input otherwise. [`models/res_partner.py`]
23. When a portal user is deactivated with a blacklist request, their formatted numbers are added to the blacklist and a log message is written naming the acting user and the portal user. [`models/res_users.py`]

### 2.4 Security
24. ACL:
    - `phone.blacklist` has a zero-permission row for all users and full CRUD for `base.group_system` only;
    - the remove wizard gets full CRUD for `base.group_system` only.

    [`security/ir.model.access.csv`]
25. No record rules are defined, and there is no company field or company scoping on the blacklist. The blacklist is database-global. [absence across listed files]
26. Sudo points:
    - blacklist state is computed with sudo;
    - set/reset blacklist on mixin records runs with sudo, so any user who can call those methods on a record changes the global blacklist.

    **RISK:** privilege boundary. [`models/mail_thread_phone.py` `_compute_blacklisted`, `_phone_set_blacklisted`, `_phone_reset_blacklisted`]
27. Opening the unblacklist wizard from a mixin record first checks write access on the blacklist. A comment in the code says the wizard's own access rights "currently not working as expected". [`models/mail_thread_phone.py` `phone_action_blacklist_remove`]
28. The portal-deactivation path adds to the blacklist without an explicit sudo in this module. Whether it succeeds depends on the privileges of the caller (see gaps). [`models/res_users.py`]

### 2.5 UI surfaces (names only)
29. Blacklist list, form and search views. The form has Unblacklist and Blacklist buttons. There is a window action "Blacklisted Phone Numbers" and menus "Phone / SMS" > "Phone Blacklist" under the technical settings menu. [`views/phone_blacklist_views.xml`]
30. The partner search view swaps the phone filter for the combined phone/mobile search. [`views/res_partner_views.xml`]
31. The unblacklist wizard form has an apply button ("Remove phone from blacklist") and a discard button. [`wizard/phone_blacklist_remove_view.xml`]

### 2.6 Jobs / config
32. No cron, config parameter or settings field in this module. Behavior depends on whether the `phonenumbers` Python package is installed, on its version, and on the database trigram extension. [absence; `tools/`, `lib/`, `init`]

## 3. Cross-module edges
- `mail`: the mixin inherits `mail.thread` and uses the partner-field discovery helper, tracking log messages and message posting. [`models/mail_thread_phone.py`, `models/phone_blacklist.py`]
- `base`: `res.partner` and `res.users` are extended, and helpers are injected into every model through `base`, available to any module (SMS and marketing modules are likely consumers; not verified here). [`models/models.py`]
- Portal account deactivation: this module overrides a portal-deactivation hook on `res.users` that it does not define itself. [`models/res_users.py`]
- `res.country` / `res.company` supply the country code and dialing code used for formatting. [`models/models.py`]

## 4. Evidence gaps / contradictions
- G1: The vendored per-region metadata files that the patch loader references (region_XX modules) were not fetched. The override content is unknown; only which countries get overrides is known.
- G2: Where the base `_deactivate_portal_user` is defined, and whether its caller runs with elevated privileges, is outside this module. It is unverified whether non-admin callers can add to the blacklist here.
- G3: The code's own comment admits that wizard access rights for `phone.blacklist.remove` "currently not working as expected". What that means at runtime is unresolved from source alone.
- G4: The country-resolution loop over partner fields does not break on a match, so the last partner field with a country wins. Whether this is intended is not documented.
- G5: The accuracy limit of the "phone is blacklisted" heuristic is admitted in a code comment.
- G6: The combined search leaves out the sanitized field on databases without its index (TODO). Search results can therefore differ between databases.
- G7: JS/static assets and tests were not reviewed.

## 5. Limitations
Static source reading only. Source presence does not prove runtime reachability. No runtime proof, no Formal Coverage claim, no GMVQ QID answers. Clean-room abstractions only.
