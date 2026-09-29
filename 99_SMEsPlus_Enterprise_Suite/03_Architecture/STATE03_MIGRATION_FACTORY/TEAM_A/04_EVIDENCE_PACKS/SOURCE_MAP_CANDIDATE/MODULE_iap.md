# Source Map (candidate) — `iap`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `iap` |
| Display name | In-App Purchases |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `2b5c5b919de580d1` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/iap/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `web`, `base_setup`
- Direct dependents in 300-module list (2): `iap_mail`, `mail_plugin`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `l10n_fr_pdp`, `l10n_in`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / Basic models and helpers to support In-App purchases.
- Inventory of user-facing artifacts (counts): menu items 2, views 3, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `iap.service` (IAP Service); `iap.enrich.api` (IAP Lead Enrichment API); `iap.account` (IAP Account)
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `iap.account` ← Community: `iap_mail`, `l10n_in`, `sms`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: —

## 6. Actions / states / validation / automation / security
- State fields found: `iap.account` → ['banned', 'registered', 'unregistered']
- Validation: 1 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 1); access rows 4

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 46 of 46 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: iap
Revision: 19.0.post20260921 | Scope: Odoo Community addons tree only

## A. Capabilities; core / optional / conditional
- Client side of the vendor's In-App Purchase (paid credits) system: local records of purchased-service accounts, secure calls to the vendor's IAP server, balance display, low-credit email alerts, and link to buy more credits (iap/__manifest__.py:8-11; iap/models/iap_account.py:21-262; iap/tools/iap_tools.py:89-141).
- Conditional/auto: depends on web and base_setup; installs automatically (iap/__manifest__.py:12-15,23). Provides shared tools reused by other paid-service modules, plus compatibility re-exports (iap/__init__.py:7-9).
- Services actually defined here: only "Lead Generation" (technical name reveal), unit "Credits", integer balance; other modules define their own services (iap/data/services.xml:4-11).
- Lead enrichment gateway (abstract) that sends email domains to the vendor's enrichment endpoint using the "reveal" account, 300-second timeout, endpoint overridable by a parameter (iap/models/iap_enrich_api.py:8-39).
- Email helpers: list of free-mail domains so that domain-based searches treat webmail addresses as individual; list of country codes for which state filtering is offered when mining leads (iap/tools/iap_tools.py:20-54,61-86).
- Settings entry "Odoo IAP - View My Services" in the contacts settings area (iap/views/res_config_settings.xml:8-15); menu "IAP Accounts" under the technical menu (iap/views/iap_views.xml:65-76).

## B. Business objects, relationships, lifecycle
- Service: name, technical name (unique, read-only), description and unit name (translatable), integer-balance flag (iap/models/iap_service.py:6-19).
- Account: name (defaults to service name), service, "service locked" flag, account token (secret, defaults to a random value, 43 chars max, not copied), companies (empty = all), balance text (from vendor), low-balance alert threshold, alert recipients, state banned/registered/unregistered (iap/models/iap_account.py:25-43,125-130).
- Lifecycle: an account is created on demand the first time a service is requested by name; if none exists for the user's companies it is created using a separate database connection so a later credit failure cannot roll it back (iap/models/iap_account.py:138-189). Opening an account refreshes balance, threshold, state from the vendor and locks the service choice (iap/models/iap_account.py:57-59,85-123). Accounts lacking a token are deleted when requested (iap/models/iap_account.py:147-158).
- Selection rule: accounts with an assigned company take precedence over company-less ones; newest first (iap/models/iap_account.py:146,186-189).
- Neutralized databases (copies/tests): new accounts are created with a disabled token suffix (iap/models/iap_account.py:132-135).

## C. Validations, automation, security, credentials
- Alert threshold must be non-negative; every alert recipient must have an email address (iap/models/iap_account.py:45-55). When threshold > 0 recipients are required in the form (iap/views/iap_views.xml:31-34).
- Changing threshold or recipients pushes the new alert settings (emails and languages) to the vendor server unless suppressed; failures are logged, not raised (iap/models/iap_account.py:61-83).
- Security: system administrators have full rights on accounts and services; ordinary internal users can read and create accounts, and read services, but cannot edit or delete (iap/security/ir.model.access.csv:2-5). A rule limits internal users to accounts with no company or one of their companies (iap/security/ir_rule.xml:3-8). Token field is readable only by system administrators; other code must elevate rights (iap/models/iap_account.py:30-36). (TEST) a demo user can obtain the account but not read its token; admin can (iap/tests/test_iap.py:10-30).
- Token in forms/lists visible only to debug-feature users (iap/views/iap_views.xml:18,49).
- External-service implication: every operation contacts the vendor's server (default https://iap.odoo.com, overridable via a system parameter) with the database UUID and account token: balance, account information, alert update, credit purchase link; enrichment goes to a separate vendor host (iap/tools/iap_tools.py:13,89-91; iap/models/iap_account.py:89-100,248-257; iap/models/iap_enrich_api.py:11-20). Timeout default 15 seconds; timeouts and network errors surface as access errors with the address in the message; vendor error "InsufficientCreditError" is passed through with its data (iap/tools/iap_tools.py:102-141).
- Credit-purchase link carries a SHA-1 hash of the token (suffix after "+" ignored), not the token itself (iap/models/iap_account.py:196-218). Business note: link-level exposure only to hashed value.
- Calls are disabled during automated tests (iap/tools/iap_tools.py:107-108; iap/models/iap_account.py:87-88).
- Unknown service names raise a user error (iap/models/iap_account.py:160-162). Balance query failure returns -1 (iap/models/iap_account.py:258-260).
- "Manage/config URL" is returned only for debug-feature users (iap/models/iap_account.py:234-235).
- Company scoping: many-to-many companies on the account plus the rule above.

## D. Handoffs to other modules
- Consumers (each defines its service and calls get/get_credits and the JSON-RPC helper): partner autocomplete, SMS, snailmail, lead mining/enrichment, and others named in code comments (iap/models/iap_account.py:197,231; iap/data/services.xml:4). Modules present in this tree: UNKNOWN — EVIDENCE INSUFFICIENT.
- Test helpers for lead-enrichment mocks provided for consuming modules (TEST) (iap/tests/common.py:13-165).
- Settings page: base_setup (iap/views/res_config_settings.xml:6-8).

## E. Configuration/defaults that change outcomes
- System parameters: vendor endpoint (iap.endpoint), enrichment endpoint (enrich.endpoint), database UUID, neutralized-database flag (iap/tools/iap_tools.py:90; iap/models/iap_enrich_api.py:19; iap/models/iap_account.py:97,132).
- Threshold 0 hides recipients and disables alert need (iap/views/iap_views.xml:30-34).
- Balance rounding: 4 decimals unless service uses integer balance (iap/models/iap_account.py:110-112).

## F. Effective extension path
- Consuming modules add services (data records), override the account-information mapping hook and use tools (iap/models/iap_account.py:117-123; iap/tools/iap_tools.py:102); module names: UNKNOWN — EVIDENCE INSUFFICIENT.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: vendor server behavior and pricing.
- UNKNOWN — EVIDENCE INSUFFICIENT: menu visibility for non-debug users (parent menu group not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end widget logic for "Buy credits" buttons (JS not read).

