# Source Map (candidate) — `phone_validation`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `phone_validation` |
| Display name | Phone Numbers Validation |
| Manifest version | 2.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c9a5b4d3d5c27b4a` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/phone_validation/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `mail`
- Direct dependents in 300-module list (4): `crm`, `event`, `hr`, `sms`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `point_of_sale`, `test_mail_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / Validate and format phone numbers
- Inventory of user-facing artifacts (counts): menu items 2, views 5, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `phone.blacklist.remove` (Remove phone from blacklist); `mail.thread.phone` (Phone Blacklist Mixin); `phone.blacklist` (Phone Blacklist)
- Objects extended from other modules (4): `mail.thread`, `base`, `res.users`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `mail.thread.phone` ← Community: `crm`, `hr_recruitment`, `mass_mailing_sms`, `test_mail_sms`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.thread`, `base`, `res.users`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 3

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 32 of 32 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: phone_validation (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities
- Validates and normalises phone numbers for a destination country; keeps a blacklist (do-not-message list) of numbers; supplies a reusable behaviour ("mixin") that gives any record with phone/mobile fields a normalised number and a blacklisted flag (phone_validation/__manifest__.py:7,14-21; phone_validation/models/mail_thread_phone.py:14-30).
- CONDITIONAL/technical: category Hidden, auto_install True, depends base and mail (phone_validation/__manifest__.py:9,28-32).
- Number checks rely on an external phone-number library; if it is missing, numbers are returned unverified with a one-time info log (phone_validation/tools/phone_validation.py:112-125).
- Ships local corrections to the library's country metadata (BR, CI, CO, IL, KE, MA, MU, PA, SN, MX...) applied only when the installed library is older than the fixing version (phone_validation/lib/phonenumbers_patch/__init__.py; (TEST) phone_validation/tests/test_phonenumbers_patch.py:79-145).

## B. Business objects and lifecycle
- Phone Blacklist entry: number (required, unique, tracked), active flag, with chatter (phone_validation/models/phone_blacklist.py:10-16,18-21).
- Lifecycle: add -> entry created (or dormant entry reactivated) -> optional note logged; remove -> entry archived (or an inactive entry created) with optional reason note (phone_validation/models/phone_blacklist.py:23-59,82-127). Removal goes via a confirmation dialog capturing a reason (phone_validation/wizard/phone_blacklist_remove.py:11-22).
- Partners gain the phone mixin (normalised number, blacklisted flags, combined phone/mobile search) (phone_validation/models/res_partner.py:8; phone_validation/models/mail_thread_phone.py:36-47).
- Generic record helpers: default number fields are mobile then phone; country taken from the record or its linked partner, else company country (phone_validation/models/models.py:15-21,23-51,89-90).

## C. Validations, automation, security
- Every blacklisted number is converted to international (E164) form; unparsable/impossible numbers are refused with reason (too short, too long, bad prefix, invalid) (phone_validation/models/phone_blacklist.py:35-37,64-67; phone_validation/tools/phone_validation.py:30-57).
- Duplicates prevented; creating an existing number re-activates it instead of failing (phone_validation/models/phone_blacklist.py:18-21,43-59; (TEST) phone_validation/tests/test_phonenumbers_blacklist.py:10-32 searches sanitise input).
- Partner form auto-reformats the phone to international style when phone, country or company changes (phone_validation/models/res_partner.py:10-13).
- Phone search on records: minimum 3 characters; finds +/00 prefix equivalents and ignores separators (phone_validation/models/mail_thread_phone.py:34,117-120,124-152).
- Blacklisted flags are visible to internal users only (phone_validation/models/mail_thread_phone.py:41,44); flags are computed with elevated rights so users lacking blacklist access still see status (phone_validation/models/mail_thread_phone.py:185-188).
- Access: blacklist and removal dialog are full-rights only for system administrators; a rule with no group grants no permissions (phone_validation/security/ir.model.access.csv:2-4). Unblacklist button re-checks write right and refuses otherwise (phone_validation/models/mail_thread_phone.py:248-261). Menu sits under technical settings (phone_validation/views/phone_blacklist_views.xml:63-72). No record rules / company scoping (no rules file, phone_validation/__manifest__.py:22-27).
- Audit: number and active changes are tracked in chatter (phone_validation/models/phone_blacklist.py:15-16); removal reasons and block reasons are logged as notes (phone_validation/models/phone_blacklist.py:98-101; phone_validation/wizard/phone_blacklist_remove.py:15-17).
- Privacy hook: when a portal account is deleted with the "blacklist" request, the account's phone numbers are added to the blacklist with a log note naming the deleting user (phone_validation/models/res_users.py:10-32).

## D. Handoffs
- Messaging engine that honours the blacklist: sms and mass_mailing_sms (uses of the mixin: model scan). Portal account deactivation flow: portal/mail (phone_validation/models/res_users.py:20). Chatter/tracking: mail.

## E. Configuration
- Country used to interpret local-format numbers: record country, else linked partner country, else current company country (phone_validation/models/models.py:36-45,89-90). Missing country + local format changes outcome: UNKNOWN — EVIDENCE INSUFFICIENT for specific results.
- Search "min length" (default 3) can be overridden per model (phone_validation/models/mail_thread_phone.py:34).

## F. Extension path
- Depend on it: crm, event, hr, point_of_sale, sms, test_mail_full (manifest scan). Use of phone helpers/mixin (model scan): calendar_sms, crm, event, event_crm, hr, hr_recruitment, mass_mailing_sms, payment_nuvei, payment_razorpay, point_of_sale, sale, sms, website_crm.

## G. Not verified
- Behaviour on installations lacking the phone-number library beyond logging: UNKNOWN — EVIDENCE INSUFFICIENT.
- Search performance indexes (trigram) depend on database capability; outcome per database: UNKNOWN — EVIDENCE INSUFFICIENT (phone_validation/models/mail_thread_phone.py:85).

