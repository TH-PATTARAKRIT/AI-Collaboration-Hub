# Source Map (candidate) — `mail_plugin`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `mail_plugin` |
| Display name | Mail Plugin |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `504759a82edafaea` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mail_plugin/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `web`, `contacts`, `iap`
- Direct dependents in 300-module list (2): `crm_mail_plugin`, `project_mail_plugin`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/CRM / Allows integration with mail plugins.
- Inventory of user-facing artifacts (counts): menu items 1, views 2, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 12
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `res.partner.iap` (Partner IAP)
- Objects extended from other modules (2): `ir.http`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.http`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 42 of 42 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: mail_plugin (Odoo 19.0.post20260921)
Scope: only pointers cited; anything else is UNKNOWN — EVIDENCE INSUFFICIENT.

## A. Capabilities
- Lets an external mailbox add-in (Outlook-style, scope "outlook") connect to the database: look up contacts by email/name/id, search contacts, create a contact, log an email as an internal note. mail_plugin/controllers/mail_plugin.py:132-193,195-220,222-248,250-270; manifest summary mail_plugin/__manifest__.py:9-10.
- Company enrichment via IAP (paid external service): create a company from the email domain, or enrich an existing company. mail_plugin/controllers/mail_plugin.py:29-58,60-130,276-296.
- Core: authorisation handshake + contact lookup/create + email logging. Optional/conditional: enrichment (needs IAP credit; skipped for free-mail domains). mail_plugin/controllers/mail_plugin.py:281-283.
- Optional module; depends web, contacts, iap. mail_plugin/__manifest__.py:11-15. Reports a fixed list of supported modules to the add-in (contacts, crm). mail_plugin/controllers/mail_plugin.py:21-27.

## B. Business objects, relationships, lifecycle
- Partner IAP cache (technical): one record per partner storing the searched domain/email and the raw enrichment response, so the same company is not enriched twice; deleted with the partner. mail_plugin/models/res_partner_iap.py:8-30.
- Partner gets two read-only computed views of that cache; writing them through the partner creates/updates the cache. mail_plugin/models/res_partner.py:8-12,30-68.
- Lifecycle of a connection: user (internal only) sees an Allow/Deny page -> short-lived signed auth code (valid 3 minutes) returned to the add-in -> exchanged for a long-lived access token stored as an API key with a scope. mail_plugin/controllers/authenticate.py:21-32,34-56,65-94,96-128; mail_plugin/views/mail_plugin_login.xml:3-21.
- Contact lifecycle via add-in: not found -> placeholder (id -1) -> existing company matched by cache or by company email -> otherwise, if user may create partners, a company is created from enrichment with a chatter note -> contact created with that company as parent. mail_plugin/controllers/mail_plugin.py:173-191,222-248,333-386.

## C. Validations, automation, security, session/audit
- Add-in calls authenticate with a bearer token whose scope must be the plugin scope; missing/invalid token -> bad request; then the call runs as the token's owner with that user's context. mail_plugin/models/ir_http.py:13-30.
- Only internal users can grant access; others see an error / not found. mail_plugin/controllers/authenticate.py:30-31,115-116.
- Auth code integrity: HMAC-signed, expires after 3 minutes; only scope "outlook" accepted for token exchange. mail_plugin/controllers/authenticate.py:80-81,100-108.
- Token lifetime: system parameter (days), default 30, non-positive falls back to 30; created with elevated rights to bypass API-key limits. mail_plugin/controllers/authenticate.py:84-93.
- Token exchange and version-check routes are public (no login) with cross-origin allowed; contact routes are cross-origin allowed but need the token. mail_plugin/controllers/authenticate.py:58-66; mail_plugin/controllers/mail_plugin.py:21-30.
- Record access follows the token owner's normal permissions: company/contact data shows "No Access" if unreadable; "can write" flag computed by access test. mail_plugin/controllers/mail_plugin.py:316-319,397-401.
- Cache table access: system administrators only. mail_plugin/security/ir.model.access.csv:2. Cache reads/writes done elevated by the code, so ordinary users indirectly populate it. mail_plugin/models/res_partner.py:15,40,49,61; mail_plugin/controllers/mail_plugin.py:306.
- Logging email content: only to whitelisted models (default: contacts); other models -> forbidden. mail_plugin/controllers/mail_plugin.py:260-261,432-437.
- Creating a contact for the system's own notification/from address is refused. mail_plugin/controllers/mail_plugin.py:156-166,230-232.
- Enrichment failures classified: free-mail domain, no credit, unknown, no data. mail_plugin/controllers/mail_plugin.py:281-295.
- Enrichment of existing company only fills empty fields (phone, logo, street, city, zip, website) and posts an internal note. mail_plugin/controllers/mail_plugin.py:88-125.
- Audit: auth code creation is logged (user, scope); IAP enrichment posts a chatter note on the company. mail_plugin/controllers/authenticate.py:127; mail_plugin/controllers/mail_plugin.py:380-384.
- Contact matching takes first match when several share an email. mail_plugin/controllers/mail_plugin.py:168-171.
- Multi-company: response lists the user's allowed companies; no per-company rule in module. mail_plugin/controllers/mail_plugin.py:428.
- Security-relevant observation: email body from add-in is posted as trusted markup. mail_plugin/controllers/mail_plugin.py:269 (observation, sanitisation downstream: UNKNOWN — EVIDENCE INSUFFICIENT).

## D. Handoffs
- iap / iap_mail: enrichment service call, credits link, chatter template "enrich company". mail_plugin/controllers/mail_plugin.py:287-289,121,380.
- res.users.apikeys (base): stores plugin tokens. mail_plugin/models/ir_http.py:22; mail_plugin/controllers/authenticate.py:89.
- mail.alias.domain (mail): identifies notification addresses to exclude. mail_plugin/controllers/mail_plugin.py:156,230.
- contacts menu tree: IAP Partners menu under IAP root. mail_plugin/views/res_partner_iap_views.xml:36-41.
- Sub-modules extend the add-in: crm_mail_plugin, project_mail_plugin (manifests list mail_plugin); hook methods for extra contact data, logging whitelist and translations. mail_plugin/controllers/mail_plugin.py:410-414,432-437,449-454.

## E. Configuration/defaults
- Access token validity days parameter, default 30. mail_plugin/controllers/authenticate.py:84-87.
- Auth-code validity fixed 3 minutes. mail_plugin/controllers/authenticate.py:106-108.
- Search result cap default 30. mail_plugin/controllers/mail_plugin.py:196.
- Free-mail domain lists steer enrichment vs whole-email matching. mail_plugin/controllers/mail_plugin.py:281,447.
- IAP credits and account required for enrichment; commercial terms: UNKNOWN — EVIDENCE INSUFFICIENT.

## F. Effective extension path
- contacts, iap, iap_mail (used); crm_mail_plugin, project_mail_plugin.

## G. Not verified
- Add-in client code (Outlook/Gmail side) is not in this module: UNKNOWN — EVIDENCE INSUFFICIENT.
- Test coverage (TEST): enrich and create company, blacklisted domain, company found/not found, IAP returns different domain, no access, no email from IAP, notification address; IAP cache constraint/compute/create/write. mail_plugin/tests/test_controller.py:14,35,62,78,95,130,165,191; mail_plugin/tests/test_res_partner_iap.py:13,22,44,61.
- Universal rules: none stated.

