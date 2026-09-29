# Source Map (candidate) — `utm`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `utm` |
| Display name | UTM Trackers |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c38c68b91300db61` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/utm/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `web`
- Direct dependents in 300-module list (7): `crm`, `event`, `hr_recruitment`, `im_livechat`, `link_tracker`, `sale`, `website`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `mass_mailing`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Marketing / —
- Inventory of user-facing artifacts (counts): menu items 5, views 14, window actions 5, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (7): `utm.medium` (UTM Medium); `utm.mixin` (UTM Mixin); `utm.source` (UTM Source); `utm.source.mixin` (UTM Source Mixin); `utm.stage` (Campaign Stage); `utm.tag` (UTM Tag); `utm.campaign` (UTM Campaign)
- Objects extended from other modules (1): `ir.http`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `utm.medium` ← Community: `mass_mailing`, `mass_mailing_sms`; open-license custom/third-party scanned: —
- `utm.mixin` ← Community: `crm`, `hr_recruitment`, `link_tracker`, `sale`, `test_mass_mailing`; open-license custom/third-party scanned: —
- `utm.source` ← Community: `hr_recruitment`, `marketing_card`, `mass_mailing`; open-license custom/third-party scanned: —
- `utm.source.mixin` ← Community: `hr_recruitment`, `im_livechat`, `mass_mailing`, `test_mass_mailing`; open-license custom/third-party scanned: —
- `utm.campaign` ← Community: `crm`, `hr_recruitment`, `link_tracker`, `mass_mailing`, `mass_mailing_crm`, `mass_mailing_crm_sms`, `mass_mailing_sale`, `mass_mailing_sale_sms`, `mass_mailing_sms`, `sale`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `ir.http`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 4 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 10

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 51 of 51 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: utm
Revision: 19.0.post20260921 | Scope: Odoo Community addons tree only

## A. Capabilities; core / optional / conditional
- Marketing attribution trackers: campaign, medium and source records, plus a reusable mixin that stamps campaign/source/medium onto other business records (leads, mailings, etc.) (utm/__manifest__.py:7-9; utm/models/utm_mixin.py:13-23).
- Captures marketing origin from web-address parameters (utm_campaign, utm_source, utm_medium) into browser cookies valid 31 days, marked as "optional" cookies (i.e., subject to consent handling), then applies them as defaults on new records (utm/models/ir_http.py:14-26; utm/models/utm_mixin.py:33-60).
- Optional (not auto-installing); depends on base and web; category Marketing (utm/__manifest__.py:6,11). Dependents that use the mixin: UNKNOWN — EVIDENCE INSUFFICIENT in this module (comments mention CRM, mass mailing, HR, website links: utm/models/utm_mixin.py:51; utm/tests/test_utm_consistency.py:14-15).
- Menus (Campaigns, Mediums, Sources) shown only to debug-feature users (utm/views/utm_menus.xml:7-29).

## B. Business objects, relationships, lifecycle
- Campaign: title (translatable) and identifier (auto-derived from title, unique, editable), responsible user (default current), stage (required, default first stage), tags, auto-generated flag, color, active flag (utm/models/utm_campaign.py:8-34).
- Stage (ordered by sequence, name translatable) and Tag (unique name, random color 1-11) classify campaigns (utm/models/utm_stage.py:11-16; utm/models/utm_tag.py:12-27).
- Medium: unique name, active flag, alphabetical (utm/models/utm_medium.py:11-22). Source: unique name (utm/models/utm_source.py:7-16).
- Source mixin for records that own a source (mailing, social post): requires a source link, restricts deletion of the source, name mirrors source name; a source is auto-created from the record's main text when none is given (utm/models/utm_source.py:51-89).
- Seed data: one campaign stage "New" (kept in data because stage is mandatory), one tag "Marketing", ten sources (incl. Referral, Newsletter, Search engine) and ten mediums (incl. Website, Direct, Email, Phone, Banner) (utm/data/utm_stage_data.xml:3-8; utm/data/utm_tag_data.xml:4-7; utm/data/utm_source_data.xml:4-31; utm/data/utm_medium_data.xml:4-31). Demo campaigns/stages are demo-only (utm/__manifest__.py:25-28).
- Lifecycle: tracking parameter arrives -> cookie set on the response if changed -> on new record creation, defaults read cookie -> a text value is matched by name (case-insensitive, archived included) or created (utm/models/utm_mixin.py:41-45,88-103). New auto-created campaigns are flagged as automatically generated (utm/models/utm_mixin.py:99-100).

## C. Validations, automation, security, credentials
- Names are kept unique automatically: a duplicate becomes "Name [2]", "Name [3]", filling gaps; blank stays blank (utm/models/utm_mixin.py:105-164; utm/models/utm_campaign.py:36-53; utm/models/utm_medium.py:24-29; utm/models/utm_source.py:25-30). Database uniqueness constraints back this up for campaign, medium, source, tag (utm/models/utm_campaign.py:31-34; utm/models/utm_medium.py:19-22; utm/models/utm_source.py:13-16; utm/models/utm_tag.py:24-27). (TEST) campaign identifier derived from title and de-duplicated (utm/tests/test_utm.py:12-23); name generation and duplicate marks (utm/tests/test_utm.py:106-217).
- Protected records: the "Referral" source cannot be deleted; six required mediums (Email, Direct, Website, X, Facebook, LinkedIn) cannot be deleted (utm/models/utm_source.py:18-23; utm/models/utm_medium.py:31-51). (TEST) deleting the Email medium raises an error even for system user (utm/tests/test_utm_consistency.py:12-18).
- Access: all internal users can read/create/edit campaigns, mediums, sources but not delete; stages and tags are read-only for internal users; system administrators have full rights (utm/security/ir.model.access.csv:2-11). (TEST) employees cannot delete campaign/medium/source (utm/tests/test_utm_security.py:46-79).
- Salesperson exception: users in the sales-team salesman group do not receive tracking defaults unless the operation runs as superuser (utm/models/utm_mixin.py:29-31). The group belongs to the sales-team module: UNKNOWN — EVIDENCE INSUFFICIENT for its presence.
- Privacy: tracking cookies are written for any visitor whose request carries the parameters; cookie type "optional" ties to consent handling elsewhere (utm/models/ir_http.py:21). Cookie domain is the request host (utm/models/ir_http.py:11-12).
- Web callers can create records by name through the find-or-create helper, subject to normal access rights; non-UTM models are simply created (utm/models/utm_mixin.py:70-86).
- Source names auto-generated as "content (model created on date)", truncated to 20 characters plus ellipsis when content is 24 or longer (utm/models/utm_source.py:32-48).
- Fetch-or-create medium by name: finds the module-qualified medium, or creates and registers it with elevated rights (utm/models/utm_medium.py:53-67). (TEST) covered (utm/tests/test_utm.py:60).
- No company scoping; no external services or credentials.

## D. Handoffs to other modules
- Consumers of the mixin and source mixin (CRM, mass mailing, recruitment/HR, website link tracker, social): owning modules inherit these models; identities beyond comments: UNKNOWN — EVIDENCE INSUFFICIENT.
- Web session/dispatch: base HTTP layer, extended for post-dispatch cookie writing (utm/models/ir_http.py:23-26).

## E. Configuration/defaults that change outcomes
- Cookie lifetime 31 days; cookie names odoo_utm_campaign/source/medium; tracking triple list overridable by other modules through the abstract mixin (utm/models/utm_mixin.py:55-60; utm/models/ir_http.py:21).
- Default stage = first stage by sequence; default responsible = current user (utm/models/utm_campaign.py:19-23).
- Kanban shows all stages even if empty (utm/models/utm_campaign.py:55-61).
- Debug-mode requirement for menu visibility (utm/views/utm_menus.xml).

## F. Effective extension path
- Modules add tracking parameters by overriding the tracking-fields list on the mixin, adding fields and defaults automatically (utm/models/utm_mixin.py:48-60); override cookie domain hook for multi-domain sites (utm/models/ir_http.py:10-12).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: list of dependent modules in this tree and how each uses the mixin.
- UNKNOWN — EVIDENCE INSUFFICIENT: how the cookie consent mechanism interprets the "optional" type.
- UNKNOWN — EVIDENCE INSUFFICIENT: view-level details (kanban/form of campaigns) beyond menu visibility.

