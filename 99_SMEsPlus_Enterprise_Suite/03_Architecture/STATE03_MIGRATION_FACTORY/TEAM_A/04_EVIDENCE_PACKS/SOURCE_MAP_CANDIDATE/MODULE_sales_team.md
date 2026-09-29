# Source Map (candidate) — `sales_team`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sales_team` |
| Display name | Sales Teams |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `071e0db44f341d9c` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sales_team/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `mail`
- Direct dependents in 300-module list (2): `crm`, `sale`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (1): `product_brand_sale` — AGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / Sales Teams
- Inventory of user-facing artifacts (counts): menu items 0, views 14, window actions 6, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `crm.team` (Sales Team); `crm.team.member` (Sales Team Member); `crm.tag` (CRM Tag)
- Objects extended from other modules (2): `mail.thread`, `res.users`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 2 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `crm.team` ← Community: `crm`, `pos_sale`, `sale`, `sale_crm`, `survey_crm`, `website_sale`; open-license custom/third-party scanned: `product_brand_sale`
- `crm.team.member` ← Community: `crm`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.thread`, `res.users`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 3 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 4 (`group_sale_salesman`, `group_sale_salesman_all_leads`, `group_sale_manager`, `base.default_user_group`); record rules 2 (of which company-scoped by text 1); access rows 9

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 38 of 38 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: sales_team (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities
- Foundation for organising salespeople into Sales Teams, tracking team membership, and giving other sales documents a default team; also defines the shared Sales security levels and a CRM tag list (sales_team/__manifest__.py:4-11; sales_team/models/crm_team.py:17-79; sales_team/security/sales_team_security.xml:9-33; sales_team/models/crm_tag.py:8-21).
- CORE for sales: depends only on base and mail; not auto-installed and not flagged as an application; no menu of its own is defined (sales_team/__manifest__.py:13-22 lists views but no menu entries were found in them). Menus and the Multi Teams setting come from crm (crm/models/res_config_settings.py:17).
- Ships default teams "Sales", "Website", "Point of Sale"; last two archived by default (sales_team/data/crm_team_data.xml:4-25).

## B. Business objects and lifecycle
- Sales Team: name, sequence, active, optional company, team leader, colour, per-user favourite flag for dashboards, chatter (sales_team/models/crm_team.py:8-12,85-122).
- Team Member (membership): links a salesperson (internal user) to a team, with active flag; shows user email/phone/image (sales_team/models/crm_team_member.py:14-40).
- Sales Tag: unique name plus colour (sales_team/models/crm_tag.py:15-21).
- Users gain: list of teams, memberships, and one "User Sales Team" computed from the earliest active membership (sales_team/models/res_users.py:9-17,38-45; (TEST) sales_team/tests/test_sales_team_membership.py:284-295).
- Lifecycle: create team -> add members through the salespersons field or member list (missing memberships created, others archived/reactivated) (sales_team/models/crm_team.py:147-160) -> members auto-added to team favourites (sales_team/models/crm_team.py:217-231,256-258) -> archive user archives their memberships (sales_team/models/res_users.py:47-49; (TEST) sales_team/tests/test_sales_team_membership.py:22-27).

## C. Validations, automation, security
- Default team choice (used by other modules) follows order: my team matching filter, my team, context default, company team matching filter, company team (sales_team/models/crm_team.py:22-31,45-77).
- Membership mode (parameter sales_team.membership_multi): single-team mode archives a user's other active memberships when a new or reactivated one is created and shows a warning in forms; multi-team mode allows several (sales_team/models/crm_team_member.py:153-213; sales_team/models/crm_team.py:162-181; (TEST) sales_team/tests/test_sales_team_membership.py:38,85,120,177,223).
- Duplicate active user+team membership refused (sales_team/models/crm_team_member.py:42-76).
- Member must belong to the team's company; changing team company re-checks members (sales_team/models/crm_team.py:124-135,226-227; sales_team/models/crm_team_member.py:78-86).
- Team leader and members must be internal (non-portal) users (sales_team/models/crm_team.py:93,100; sales_team/models/crm_team_member.py:22).
- Default teams "Website" and "Point of Sale" cannot be deleted (sales_team/models/crm_team.py:233-241).
- Security levels: "User: Own Documents Only" (implies internal user) -> "User: All Documents" -> "Administrator" (also implies canned-response admin; assigned to system user and admin) (sales_team/security/sales_team_security.xml:9-33).
- Access: teams readable by all internal users, full rights for Sales Administrator; memberships readable by internal users, full for Administrator, no group grants nothing; tags: no rights for plain internal users, create/edit/read for Salesperson, full for Administrator (sales_team/security/ir.model.access.csv:2-10; (TEST) sales_team/tests/test_sales_team.py:231-250).
- Record rules: teams limited to user's allowed companies or shared (no company); a second rule lets "All Documents" users see all teams (sales_team/security/sales_team_security.xml:36-47).
- Audit: teams and memberships have chatter; members are not auto-followed (sales_team/models/crm_team_member.py:162-171; sales_team/models/crm_team.py:219).

## D. Handoffs
- Leads/pipeline and multi-team switch: crm. Quotations/orders using default team: sale. Website / POS default teams: website_sale, pos_sale. Activity types shortcut for contacts: mail (sales_team/views/mail_activity_views.xml:3-7). Chatter: mail.

## E. Configuration that changes outcomes
- Multi Teams setting stores sales_team.membership_multi; default single-team (sales_team/models/crm_team.py:139; sales_team/models/crm_team_member.py:117; crm/models/res_config_settings.py:17).
- Team company left empty = team visible to all companies (sales_team/models/crm_team.py:88-89,194).

## F. Extension path
- Depend directly: crm, sale (manifest scan). Inherit crm.team: pos_sale, sale, sale_crm, survey_crm, website_sale. Inherit crm.team.member: crm. Reuse group_sale_*: crm, crm_livechat, event_booth_sale, event_crm, event_sale, pos_sale, sale, sale_expense, sale_management, sale_mrp, sale_pdf_quote_builder, sale_project, sale_purchase, utm, website_crm, website_crm_partner_assign, website_sale, website_sale_slides.

## G. Not verified
- Dashboard button label is a placeholder in this module (sales_team/models/crm_team.py:211); actual label supplied by extenders: UNKNOWN — EVIDENCE INSUFFICIENT.
- Tag visibility for plain internal users beyond the access line: UNKNOWN — EVIDENCE INSUFFICIENT.

