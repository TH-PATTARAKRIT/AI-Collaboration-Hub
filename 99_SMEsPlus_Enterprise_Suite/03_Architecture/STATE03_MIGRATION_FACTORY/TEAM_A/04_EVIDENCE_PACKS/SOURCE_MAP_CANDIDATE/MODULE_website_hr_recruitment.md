# Source Map (candidate) — `website_hr_recruitment`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_hr_recruitment` |
| Display name | Online Jobs |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `b072c20653280d9d` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_hr_recruitment/` |
| auto_install / application | ['hr_recruitment', 'website_mail'] / True |

## 2. Dependencies
- Direct dependencies (manifest): `hr_recruitment`, `website_mail`
- Direct dependents in 300-module list (1): `website_hr_recruitment_livechat`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Manage your online hiring process
- Inventory of user-facing artifacts (counts): menu items 1, views 10, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 6
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (9): `hr.department`, `hr.job`, `website.seo.metadata`, `website.published.multi.mixin`, `website.searchable.mixin`, `website.page`, `website`, `hr.applicant`, `hr.recruitment.source`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `hr.department`, `hr.job`, `website.seo.metadata`, `website.published.multi.mixin`, `website.searchable.mixin`, `website.page`, `website`, `hr.applicant`, `hr.recruitment.source`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 1 (`hr_recruitment.group_hr_recruitment_user`); record rules 4 (of which company-scoped by text 0); access rows 4

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 43 of 44 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_hr_recruitment (Online Jobs)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_hr_recruitment.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: publish open job positions on the website and track application submissions (website_hr_recruitment/__manifest__.py:9-10).

## A. Capabilities / functions
- Conditional app: depends on hr_recruitment and website_mail; auto-installs when both of them are installed; flagged as an application (website_hr_recruitment/__manifest__.py:11, 25-26).
- Core: public job board `/jobs` (12 per page) with search (including fuzzy) and filters by country, department, office, employment type and industry, plus "remote", "other department", "untyped" choices; live counters per filter; country pre-selected from the visitor's location when jobs exist there (website_hr_recruitment/controllers/main.py:21-168).
- Core: job detail page and application page; application form posts to the generic website form with model "applicant" and redirects to `/job-thank-you` (website_hr_recruitment/controllers/main.py:178-201; website_hr_recruitment/views/website_hr_recruitment_templates.xml:200-203, 610).
- Core: registers the applicant model as a website-form target "Apply for a Job" and whitelists: email, name, phone, job, department, LinkedIn profile, custom properties (website_hr_recruitment/data/config_data.xml:20-36).
- Core: job positions become website-publishable records (SEO, multi-website, searchable), with web description, "process details" block (default text about answer time and interview steps), published date and full URL (website_hr_recruitment/models/hr_job.py:10-51).
- Core: "Jobs" menu and launch action installed as data (website_hr_recruitment/data/config_data.xml:3-18); site-wide search and suggested-page hooks (website_hr_recruitment/models/website.py:10-19).
- Core: recruitment sources gain a shareable tracker URL with campaign, medium and source markers (website_hr_recruitment/models/hr_recruitment_source.py:12-24).
- Core: "New job" quick-create for logged-in users from the website (website_hr_recruitment/controllers/main.py:170-176).
- Core: duplicate-application hint for candidates while typing name, email, phone or LinkedIn (website_hr_recruitment/controllers/main.py:203-257).
- Backend: publish toggle and website selector on the job form, website field on lists, "Website > Job pages" list (website_hr_recruitment/views/hr_recruitment_views.xml:14-48; website_hr_recruitment/views/website_pages_views.xml:4-63).

## B. Business objects, relationships, lifecycle
- Job position (hr.job, owned by hr) -> published flag -> optional website -> applicants (hr.applicant, owned by hr_recruitment) created by the form. Department and office/country/contract type/industry drive filters (website_hr_recruitment/controllers/main.py:41-64).
- Publish lifecycle: unpublished -> published (published date = today) -> unpublished on "set open" or archive (website_hr_recruitment/models/hr_job.py:58-68, 78-80, 85-87). The published date is recomputed to today whenever the flag turns true (website_hr_recruitment/models/hr_job.py:58-61).
- Application intake: candidate fills form -> applicant created on the first non-folded stage that applies to the job (or to all jobs) -> extra typed answers are put in an "Other Information" note on the applicant (website_hr_recruitment/models/hr_applicant.py:11-25; website_hr_recruitment/tests/test_website_hr_recruitment.py:87-121 (TEST)). A short introduction answer is relabelled (website_hr_recruitment/controllers/main.py:259-265).
- If the submitter's email matches an existing user/contact, the applicant is linked to that contact; the candidate's typed name is kept on the applicant and the contact is not changed (TEST) (website_hr_recruitment/tests/test_website_hr_recruitment.py:123-145; website_hr_recruitment/models/hr_applicant.py:12-14).
- Applicants whose job was archived/closed cannot be submitted: error "job offer has been closed" (website_hr_recruitment/models/hr_applicant.py:15-18).

## C. Validations, automation, security, multi-company
- Access rows: public, portal and internal users can read jobs; public can read departments (website_hr_recruitment/security/ir.model.access.csv:2-5). Record rules: public and portal see only published jobs; recruitment officers read all jobs; public sees departments that have published jobs (or that have no children) (website_hr_recruitment/security/website_hr_recruitment_security.xml:4-43). Recruitment officer group is made to imply website restricted editor (website_hr_recruitment/security/website_hr_recruitment_security.xml:47-49).
- Public duplicate-check endpoint reads applicants with elevated rights (website_hr_recruitment/controllers/main.py:217). It is scoped to the current website or no website, and to ongoing or refused applications (website_hr_recruitment/controllers/main.py:217-223). Depending on the outcome it tells the caller: a closed application in the last 6 months exists for this job, or an ongoing application exists (with the recruiter's name, email, phone), or a similar application exists (website_hr_recruitment/controllers/main.py:225-257). Privacy implication of exposing this to anonymous callers: UNKNOWN — EVIDENCE INSUFFICIENT.
- Country-filtered search uses elevated access and then re-applies the published filter for non-recruiters (website_hr_recruitment/models/hr_job.py:104, 118-120).
- Sensitive-form logging: the standard "authentication" chatter line is skipped for anonymous applicants (website_hr_recruitment/controllers/main.py:267-270).
- Thank-you page is never cached (website_hr_recruitment/models/website_page.py:9-13).
- Job department display name is computed with elevated rights because portal users cannot read departments (website_hr_recruitment/models/hr_department.py:9-10).
- Tests: technical pages load (TEST) (website_hr_recruitment/tests/test_website_hr_recruitment_technical_page.py:8); job list page renders without error when a job has no address (TEST) (website_hr_recruitment/tests/test_website_hr_recruitment.py:57).
- Multi-website/company: jobs may be tied to one website or all; website field limited to the job's company or none in the form domain (website_hr_recruitment/views/hr_recruitment_views.xml:26). Captcha protection is that of the generic form route (website/controllers/form.py:31).
- Old migration removes an obsolete hidden token block from customised application-page views (website_hr_recruitment/migrations/17.0.1.1/pre-migrate.py).

## D. Handoffs to other modules
- hr_recruitment (owner): applicants, stages, sources, recruiter groups, campaign; hr (jobs, departments, contract types); website (form controller, publish mixin, search, layout); website_mail (follow widget); utm (campaign/medium/source); res.partner industries (filter).
- Downstream survey/skills/SMS extensions of applicants live in hr_recruitment_survey, hr_recruitment_skills, hr_recruitment_sms (extension list below). Chatbot helper: website_hr_recruitment_livechat.
- Website form action key "apply_job" (website_hr_recruitment/data/config_data.xml:22).

## E. Configuration / defaults that change outcomes
- Job "published" flag and website selector; default process text and default web description (website_hr_recruitment/models/hr_job.py:19-49).
- Stage assigned on submission is the first non-folded stage matching the job (website_hr_recruitment/models/hr_applicant.py:19-24).
- GeoIP determines the default country filter (website_hr_recruitment/controllers/main.py:120-129).
- Duplicate-check look-back is a fixed 6 months (website_hr_recruitment/controllers/main.py:205-208).

## F. Effective extension path (module names only)
- hr.job: hr_recruitment, hr_recruitment_skills, hr_recruitment_survey, hr_skills (with website_hr_recruitment). hr.applicant: hr_recruitment_skills, hr_recruitment_sms, hr_recruitment_survey, website_hr_recruitment. Website form controller extended by website_hr_recruitment (see website_crm note for the list). website.page: website, website_hr_recruitment, website_livechat, website_project, website_sale.

## G. Not verified
- Referral and interview scheduling flows: UNKNOWN — EVIDENCE INSUFFICIENT (owned by hr_recruitment).
- Attachment (CV) handling and limits: UNKNOWN — EVIDENCE INSUFFICIENT.
- Data-retention rules for candidate data: UNKNOWN — EVIDENCE INSUFFICIENT.

