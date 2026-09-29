# Source Map (candidate) — `rating`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `rating` |
| Display name | Customer Rating |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `a750923b50227e3c` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/rating/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `mail`
- Direct dependents in 300-module list (3): `im_livechat`, `portal_rating`, `project`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_mail_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Productivity / —
- Inventory of user-facing artifacts (counts): menu items 1, views 9, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 2
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `rating.parent.mixin` (Rating Parent Mixin); `rating.rating` (Rating); `rating.mixin` (Rating Mixin)
- Objects extended from other modules (2): `mail.thread`, `mail.message`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `rating.parent.mixin` ← Community: `im_livechat`, `project`; open-license custom/third-party scanned: —
- `rating.rating` ← Community: `im_livechat`, `portal_rating`; open-license custom/third-party scanned: —
- `rating.mixin` ← Community: `im_livechat`, `project`, `test_mail_full`, `website_sale`, `website_slides`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.thread`, `mail.message`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 4

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 32 of 32 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — rating
Source revision: 19.0.post20260921 | Module: "Customer Rating" v1.1, category Productivity, LGPL-3 (rating/__manifest__.py:5-7,40). Basis: static reading of models, controllers, access file; one security test read (TEST).

## A. Capabilities and optionality
- A1. Lets a customer (or an employee on their behalf) give a score of 0 to 5 plus a comment on any business record that has a discussion thread; scores are turned into Happy / Neutral / Unhappy / Not Rated labels. rating/models/rating.py:44-48; rating/models/rating_data.py:20-25,57-66
- A2. Optionality: core-style helper, depends only on mail, no auto_install flag, no settings switch. It is a foundation installed because other apps depend on it. rating/__manifest__.py:11-13. Community modules that inherit its statistics mixins: project, im_livechat, website_slides, website_sale (grep of "rating.mixin"/"rating.parent.mixin").
- A3. Provides a Ratings list/kanban/pivot/graph screen under the Discuss technical menu. rating/views/rating_rating_views.xml:214-244
- A4. Public web pages let the customer open the request link, choose Happy/Neutral/Unhappy, add a comment and submit. rating/controllers/main.py:27-88

## B. Objects, relationships, lifecycle
- B1. Rating record: points to any business record (model + id), optionally to its parent record (e.g. project of a task), the rated person (operator) and the rating customer; stores value, comment, message link, secret token, "consumed" flag and rated-on time. rating/models/rating.py:28-55
- B2. Lifecycle: a blank rating with a random token is created on demand for a customer (reused if an unconsumed one exists for the same customer); customer submits -> value/comment stored, flagged consumed, and a chatter message posted/updated; "reset" clears value, comment, consumed flag and issues a new token. rating/models/mail_thread.py:55-76,99-163; rating/models/rating.py:166-173
- B3. Rated-on timestamp is refreshed whenever value or comment is written. rating/models/rating.py:130-131,137-138
- B4. Deleting a rated record deletes its ratings; deleting a rating deletes its chatter message. rating/models/mail_thread.py:18-23; rating/models/rating.py:141-144
- B5. Parent is discovered from a record's declared parent field if the record type defines one. rating/models/rating.py:146-160
- B6. Statistics mixins compute count, average, satisfaction percentage, last value/comment on the rated record or its parent, counting only consumed ratings with value >= 1. rating/models/rating_mixin.py:51-59,80-97; rating/models/rating_parent_mixin.py:31-55

## C. Validations, automation, security
- C1. Database rule: value must be between 0 and 5; code also rejects out-of-range values in the apply routine. rating/models/rating.py:57-60; rating/models/mail_thread.py:122-123
- C2. Public submission accepts only values 1 (unhappy), 3 (neutral), 5 (happy). rating/controllers/main.py:29,69; rating/models/rating_data.py:15-17
- C3. Access: employees read/write/create (no delete); portal and public have no direct rights; administrators have full rights. rating/security/ir.model.access.csv:2-5. (TEST) portal/public cannot create or write; employee can. rating/tests/test_security.py:45-76
- C4. The token acts as the credential for the public pages. Unknown token or missing record gives "not found". If the visitor is logged in and belongs to a different commercial partner than the rating's customer, an "invalid partner" page is shown instead. rating/controllers/main.py:43-49,90-98
- C5. No record rules and no company field are defined in this module; company visibility therefore follows the rated record only where the record itself is read. UNKNOWN — EVIDENCE INSUFFICIENT for tenant/company isolation of rating rows.
- C6. Posting a comment with a rating value creates the rating under elevated rights; linking a rating to its message only happens if same author and same record. rating/models/mail_thread.py:166-179,184-191
- C7. Optional delayed notification (2 hours) when applying a rating, so the customer can still edit. rating/models/mail_thread.py:117-118,137-140
- C8. Rating stats shown in the chatter are hidden unless the record type overrides the "allow publish" hook (default: not published). rating/models/rating_mixin.py:233-236; rating/models/mail_message.py:58-67

## D. Handoffs
- D1. Sending the request email: any thread-enabled record can send a template; only project (task stage rating email) is a Community caller found. rating/models/mail_thread.py:81-97; project/models/project_task.py:2150. Owner: mail for message posting.
- D2. Operator/customer defaults come from the record's user and partner fields. rating/models/mail_thread.py:34-50
- D3. Public chatter for portal: portal (controller subclass is empty here). rating/controllers/portal_thread.py:6-7

## E. Configuration that changes outcomes
- E1. Grade thresholds are fixed constants: >=4 great/happy, >=3 neutral, >=1 unhappy; averages >=3.66 happy, >=2.33 neutral. rating/models/rating_data.py:8-17
- E2. A parent type may limit satisfaction to the last N days (default: all). rating/models/rating_parent_mixin.py:15,35-36

## F. Extension path
- project, im_livechat, website_slides, website_sale (rating statistics mixins); test_mail_full (tests only).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: content of the customer-facing pages and email templates (rating_templates.xml not read in detail).
- UNKNOWN — EVIDENCE INSUFFICIENT: how each consuming app decides when to send requests (only project's caller located).
- UNKNOWN — EVIDENCE INSUFFICIENT: menu visibility group of the technical menu (mail module, not read).

