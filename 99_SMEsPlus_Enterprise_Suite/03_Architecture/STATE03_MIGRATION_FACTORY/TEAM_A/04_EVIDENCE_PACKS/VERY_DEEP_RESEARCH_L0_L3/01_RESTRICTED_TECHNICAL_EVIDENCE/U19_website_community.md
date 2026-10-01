# U19 website_community - RESTRICTED TECHNICAL EVIDENCE

> **RESTRICTED - TECHNICAL EVIDENCE - NOT FOR NEUTRAL DISTRIBUTION**
> Status: **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION**

| Field | Value |
|---|---|
| Unit | U19 `website_community` (VDR L2/L3 worker output) |
| Modules owned | website, website_blog, website_crm, website_crm_iap_reveal, website_crm_livechat, website_crm_partner_assign, website_crm_sms, website_customer, website_event, website_event_booth, website_event_crm, website_forum, website_google_map, website_hr_recruitment, website_hr_recruitment_livechat, website_links, website_livechat, website_mail, website_mail_group, website_mass_mailing, website_mass_mailing_sms, website_partner, website_payment, website_profile, website_project, website_slides, website_slides_survey, website_sms, website_timesheet, im_livechat, rating, portal_rating, mail_group, html_builder, html_editor, web_unsplash |
| Source revision | `19.0.post20260921` (Odoo 19 Community, `odoo/addons`) |
| Date | 2026-10-02 |
| Claim-ID prefix / Neutral prefix | `VDR-U19-C###` / `N-U19-###` |
| Method | static source read (every pointer viewed) plus read-only configuration queries on the restored DB (counts, flags, names of seeded configuration only; no partner, user or credential values recorded). No source modified, Odoo not started, no git state change. |
| Limits | No V-level, completeness, coverage %, Gate PASS or Clean-Room approval is asserted. Anything needing execution is flagged `RT`. Breadth over depth: public-route security, scoping, consent, publishing, form-to-record and the payment hook were prioritised; most model-internal business logic of slides, forum, event and live chat was only skimmed. |

## 0. Scope notes

**Function-ID mapping.** No entry of `EXISTING_FUNCTION_ID_INDEX_53.json` (domains: goods receipt, inventory adjustment, sales delivery, manufacturing, multicompany isolation, partial fulfilment, period cut-off, product routing, reconciliation provenance) genuinely matches a public-website capability, so every capability and claim is `FUNCTION MAPPING REQUIRED`. `MULTICOMPANY_ISOLATION_PILOT` was considered and rejected: it concerns inventory/accounting company isolation, not website scoping.

**Capabilities derived (10).** CAP-U19-01 page serving/visibility/publishing; 02 form submission to records; 03 multi-website, consent, visitor tracking; 04 blog, partner showcase, follow; 05 forum and profiles; 06 online courses; 07 live chat and bots; 08 events and booths; 09 newsletter, mail groups, rating links; 10 payment hook and public integration endpoints. D-levels: all capabilities are given D1 (purpose), D2 (objects) and D3 (flow/state/override chain) below; the depth of each is uneven (see Depth map).

**Environment facts (DB, config only).** 356 installed modules; this unit's 35 modules are all installed (website_slides_survey, website_crm_sms, website_mass_mailing_sms, website_sms, website_timesheet, website_hr_recruitment_livechat included). `website_sale` and all other e-commerce modules are NOT installed (`ir_module_module` state uninstalled); `website_cf_turnstile` (alternative captcha) uninstalled; `google_recaptcha` installed with no secret key. 30 `theme_*` modules installed, producing 29 websites (one real, 28 theme demo websites) on one company, all with the cookie bar off. Signup scope per website `b2b`.

**Depth map (honest).** Read in depth: website (routing, page, visibility, form, visitor, cookie, user, model page), website_crm, website_hr_recruitment (controller+model), website_project (controller), website_mass_mailing (controller), mail_group (controllers, rules, tokens), rating, portal_rating, website_mail, website_partner, website_payment, website_links, website_event (registration controller), website_event_booth (controller), website_crm_iap_reveal (hook+cron), website_livechat, im_livechat (controllers/channel/rules/chatbot step customer values), website_profile controller, website_forum (rules, post model karma, key routes), website_slides (rules, channel visibility/enrol, join/invite/embed/quiz routes), html_editor (link preview, upload, shape routes), web_unsplash controller, website_google_map controller, website_crm_partner_assign (controller, lead portal methods), website_customer (routes, rule). Skimmed or not read: website_slides model internals (karma, ranking, survey), website_slides_survey, website_blog templates/comments, website_forum vote/flag arithmetic and templates, website_event models, event booth/sponsor models, website_mail_group, website_mass_mailing_sms, website_sms/website_crm_sms internals (read: visitor composer hooks only), website_timesheet (read: one method), website_hr_recruitment_livechat (manifest only), html_builder (no Python), website theme/snippet/asset machinery, website config settings, SEO, sitemap generation, translations, images/binary route, IAP clearbit service beyond the call.

**DISCOVERED SUPPORTING MODULES** (read only as far as needed, outside the assignment): `base` (ir_http.py:348-352 dispatcher captcha hook, :451-456 cookie hook), `google_recaptcha` (ir_http.py), `auth_signup` (signup scope, captcha=), `mail` (link_preview.py), `mass_mailing` (mailing.list is_public, unsubscribe token controller), `link_tracker` (/r redirect), `crm` and `crm_iap_mine`/`iap_crm` (reveal, lead fields), `hr_recruitment`, `project`, `event`/`event_booth`/`event_crm`, `payment`/`account_payment`, `gamification`, `utm`, `http_routing`, `portal`, `survey`. Claims on these carry that condition.

**Contradictions with prior evidence (`CONTRA`).** None asserted. Prior candidate records `MODULE_website.md` and `MODULE_website_links.md` were spot-checked only: they agree on the form builder whitelist, visibility modes, cache conditions and counts (website: 44 access rows, 8 rules, 2 crons). Note on the prior structural extract: its `groups` lists contain references to groups defined elsewhere (website: 7 entries versus 4 groups actually defined in the DB for this module), and its controller counts for `website_links` come from a `controller/` (singular) directory, not `controllers/`. Neither is a contradiction.

**Cron list (owned, config only).** website: 'Website Visitor : clean inactive visitors' - 1 day - active; website: 'Disable unused snippets assets' - 1 week - active; website_crm_iap_reveal: 'Lead Generation: Leads/Opportunities Generation' - 1 day - active; mail_group: 'Mail List: Notify group moderators' - 1 day - active. No base.automation rows; ir.actions.server rows: website 4, mail_group 1, website_crm_iap_reveal 1, website_livechat 1 (not studied).

**Config counts reconciled (DB ir_model_data owned by module vs source).** ACL: website 44, website_blog 16, website_crm 2, website_crm_iap_reveal 4, website_crm_partner_assign 11, website_customer 6, website_event 27, website_event_booth 4, website_forum 15, website_hr_recruitment 4, website_links 3, website_livechat 2, website_mass_mailing 1, website_profile 1, website_slides 41, website_slides_survey 5, im_livechat 15, rating 4, mail_group 9, html_editor 2 - all equal the source declarations. Rules: website 8, website_blog 2, website_crm_iap_reveal 4, website_crm_partner_assign 4, website_customer 1, website_event 8, website_event_booth 1, website_forum 12, website_hr_recruitment 4, website_slides 21, website_slides_survey 5, im_livechat 3, mail_group 10 - all equal source. Groups defined in DB: website 4, website_slides 2, im_livechat 2, mail_group 1 (website_event and website_hr_recruitment only reference foreign groups). Note ir_model_data 'website_event' also lists the event rules 'Event Question ... event_ids any' which are in website_event/security/event_security.xml.

## CAP-U19-01 Public page serving, visibility levels and publishing control

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 (business purpose & process semantics)** Business purpose: let anonymous visitors see published marketing pages (and optionally generic record listings) while restricting editing and publishing to trusted roles. Visibility modes (public / signed-in / group / password) let the operator keep some pages private without a separate site. [C013 C015 C017 C018] [C005 C006 C007] [C008 C009 C010 C011]

**D2 (architecture / data / object relationships)** Objects: website.page (inherits ir.ui.view via _inherits, mixes website.published.multi.mixin, website.searchable.mixin, website.page_options.mixin), ir.ui.view (visibility, visibility_password, group_ids, website_id, track), website.controller.page (model page; _inherits ir.ui.view; record_domain, name_slugified), website.menu (group_ids rule), website.rewrite (redirects). Mixins: website.published.mixin (is_published, can_publish), website.multi.mixin (website_id). [C001 C004 C039] [C033 C036] [C028 C029 C030 C031]

**D3 (source / technical / workflow logic)** Control flow: ir.http._serve_fallback -> super (attachments) -> _frontend_pre_dispatch -> _serve_page (website.page._get_page_info then _get_response with optional cache) -> _serve_redirect -> 404. Rendering goes through ir.ui.view._render_template which calls _handle_visibility on the main view. Model pages are served by a normal route /model/<slug>, not by the fallback. Publishing writes go through website.published.mixin.write/create. [C001 C004 C039] [C013 C015 C017 C018] [C020 C022 C024 C025]

State diagram (list):
- page draft (is_published False) -> published [write is_published by user with can_publish]
- published -> scheduled [date_publish in the future] -> visible [date reached]
- visible (password) -> unlocked for session [correct visibility_password POST]
- visible -> restricted [visibility connected / restricted_group / password]

Ten-dimension table:

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Anonymous GET resolves a published page by url, renders it, and may serve it from a one-hour cache [C001 C004 C039] [C005 C006 C007] [C020 C022 C024 C025]. |
| 2 Reversal / cancel / negative path | Unpublish by writing is_published False (needs can_publish); deleting a page also deletes its view unless shared or inherited [C041 C042 C044]. A hidden or restricted page returns 403/404 [C013 C015 C017 C018]. |
| 3 Multi-company / data-scope | website_domain() selects pages with website_id empty or equal to the current website; most specific wins; routes with model arguments return 404 when another website [C001 C004 C039] [C028 C029 C030 C031]. |
| 4 Side effects & cross-module triggers | Rendering applies view rules; menu entries are filtered by group; search index only includes published, indexed, accessible pages [C026 C027] [C013 C015 C017 C018]. Cookie-consent state is part of the cache key [C021 C023]. |
| 5 Configuration & optionality | Per-page visibility, password, groups, publication date, indexing, homepage; per-website homepage; cache can be disabled by dev mode xml [C020 C022 C024 C025]. |
| 6 Validation & constraints | Concrete model required for model pages; page url unique per website; visibility password hashed; AccessError on unauthorised publish [C028 C029 C030 C031] [C008 C009 C010 C011] [C032 C035]. |
| 7 Roles & permissions | Designer group: CRUD on pages/views; restricted editor: read views only; public/portal: read via router sudo and rules on published pages; database rows confirm ACL 44 and rules 8 for module website [C028 C029 C030 C031] [C013 C015 C017 C018]. |
| 8 Scheduled / automated behaviour | No cron serves pages; website disable-unused-snippets weekly job is asset housekeeping (not studied further); date_publish makes scheduled visibility. |
| 9 Exception & failure behaviour | Forbidden/404/403-with-password-prompt; PageCannotBeCached falls back to uncached result; invalid model page configuration raises ValidationError [C013 C015 C017 C018] [C032 C035]. |
| 10 Accounting, stock, audit, security & compliance | Content security: password stored hashed; designers bypass restrictions; a cached unlocked page could leak to other sessions (RT) [C021 C023]; model pages widen public data surface [C034]. No accounting or stock effect. |

**DB reconciliation (restored DB, configuration only):** Restored DB (config only): website pages 37 (36 published; 29 website-specific, 8 generic), website menus 240, ir_ui_view qweb views 4271 all with visibility empty (public) and 0 password-protected views, website_controller_page 0 rows, website_rewrite 0 rows, ir_model_access rows owned by module website 44 (equals CSV), ir_rule rows 8 (equals XML), res.groups owned: group_website_designer, group_website_restricted_editor, website_page_controller_expose, group_multi_website (4; source lists 7 groups because it also references base groups). Crons owned by website: 'Website Visitor : clean inactive visitors' daily and 'Disable unused snippets assets' weekly, both active.

**Unknown / Runtime list:**
- Whether the cached response replays unlocked pages (RT) [C257 C258].
- Whether ordering by hidden fields is possible on model pages [C257 C258].
- Contents of arbitrary site pages (4271 views) were not read; only the serving mechanism.

## CAP-U19-02 Website form submission creating business records

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 (business purpose & process semantics)** Business purpose: capture leads, applications, tasks, newsletter sign-ups and contact emails from the public site and turn them directly into back-office records with no visitor account. The controller is generic; each business module opts its model in. [C055 C080] [C270]

**D2 (architecture / data / object relationships)** Objects: ir.model (website_form_access, website_form_default_field_id, website_form_key, website_form_label), ir.model.fields (website_form_blacklisted), crm.lead, hr.applicant, project.task, mailing.contact, mail.mail, ir.attachment, website.visitor. Per-model hooks: website_form_input_filter on crm.lead and hr.applicant; extract_data/insert_record overridden in website_crm, website_project and website_hr_recruitment controllers. [C048] [C049 C050 C051 C052] [C070 C071 C072]

**D3 (source / technical / workflow logic)** Flow: POST /website/form/<model> -> dispatcher captcha hook -> CSRF check (authenticated sessions only) -> savepoint -> _handle_website_form -> extract_data (authorised fields, binary/attachments, custom text, metadata, model filter) -> insert_record (SUPERUSER create, custom text into default field or chatter) -> insert_attachment -> JSON id. mail.mail path verifies the HMAC signature and sends immediately. Overrides when installed: website_crm (phone formatting, GeoIP state, visitor/partner linking, company, lead assignment defaults), website_project (task partner by email), website_hr_recruitment (closed job refusal, stage). [C047 C061 C081] [C054 C059 C060] [C070 C071 C072] [C074 C075]

State diagram (list):
- form posted -> fields authorised [website_form_access and not blacklisted]
- authorised -> record created [SUPERUSER create inside savepoint]
- record created -> attachments linked [files posted]
- any -> rolled back, JSON error [ValidationError/UserError/AccessDenied in savepoint]
- success -> session remembers last created record [form_builder_* session keys]

Ten-dimension table:

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Visitor posts form; record created with custom text appended; JSON id; confirmation page reads session [C047 C061 C081] [C055 C080]. |
| 2 Reversal / cancel / negative path | Savepoint rollback on validation errors; no undo of a committed record; IntegrityError returns false [C046 C053 C062] [C047 C061 C081]. |
| 3 Multi-company / data-scope | Lead company defaults to the website company; website of the form is not stored on most records; hr applicant ignores website_id [C070 C071 C072] [C073]. |
| 4 Side effects & cross-module triggers | Creates leads/applicants/tasks/contacts/mails; links visitor and partner; mail.mail is sent at once; attachments created sudo [C070 C071 C072] [C054 C059 C060] [C057]. |
| 5 Configuration & optionality | Model opt-in via ir.model flag; field whitelist by designer; metadata via ICP; captcha keys via settings [C048] [C049 C050 C051 C052] [C058] [C045 C063 C064 C065]. |
| 6 Validation & constraints | Required fields without default must be present; field types cast by filters (int/float/html/binary); signature HMAC for mail; hr closed job; phone format [C046 C053 C062] [C074 C075]. |
| 7 Roles & permissions | Anonymous may call; creation uses SUPERUSER (no ACL needed); designer group alone can whitelist fields; DB shows 5 form-enabled models (crm.lead, project.task, mail.mail, mailing.contact, hr.applicant) [C049 C050 C051 C052] [C048]. |
| 8 Scheduled / automated behaviour | No cron; visitor/lead synchronisation is synchronous; email sending is immediate not queued [C054 C059 C060]. |
| 9 Exception & failure behaviour | Errors returned as JSON fields list or message; AccessDenied for bad signature rolls back; captcha failure raises UserError (no-op without key) [C045 C063 C064 C065]. |
| 10 Accounting, stock, audit, security & compliance | Security: unauthenticated record creation with elevated rights; lead assignment and project selection are visitor-controlled [C068 C069] [C079]; PII enumeration [C076 C077]; no secret configured so no bot challenge [C067]; consent: metadata capture storing IP is optional [C058]. |

**DB reconciliation (restored DB, configuration only):** Restored DB: ir_model.website_form_access true for crm.lead (default field description, key create_lead), project.task (create_task), mail.mail (send_mail), mailing.contact (create_mailing_contact), hr.applicant (apply_job). Non-blacklisted fields: crm.lead 10 (contact_name, description, email_from, lead_properties, name, partner_name, phone, reveal_ip, team_id, user_id), hr.applicant 7, mail.mail 5 (attachment_ids, body_html, email_from, email_to, subject), mailing.contact 9, project.task 7. ICP enable_recaptcha = True, recaptcha_min_score = 0.7, no recaptcha_public_key / recaptcha_private_key rows, so the challenge is inactive. Note reveal_ip is whitelisted on crm.lead (written by the lead generation module).

**Unknown / Runtime list:**
- Infrastructure rate limiting and upload ceilings [C259].
- Behaviour when mail.mail posts only email_cc: signature value includes ':email_cc' and is checked at website/controllers/form.py:84-92 (read), not executed.
- Consequences of the whitelisted mail.mail.attachment_ids field (many2many replace command from visitor input) were not traced end to end.

## CAP-U19-03 Multi-website scoping, company binding, cookie consent and visitor tracking

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 (business purpose & process semantics)** Business purpose: run several branded websites on one database with separate content, domains, login scope and consent behaviour, and measure visitors for sales follow-up. [C082 C108 C109] [C272]

**D2 (architecture / data / object relationships)** Objects: website (domain, company_id, cookies_bar, block_third_party_domains, specific_user_account, auth_signup_uninvited, language_ids, user_id, crm_default_team/user, channel_id), res.users (website_id via partner, unique(login, website_id)), res.company.website_id (computed), website.visitor / website.track, crm.reveal.rule / crm.reveal.view, link.tracker. website.multi.mixin carries website_id on records. [C083] [C085 C086 C087] [C097 C098 C100]

**D3 (source / technical / workflow logic)** Flow: ir.http._match -> get_current_website (session force, context, host, fallback) -> _frontend_pre_dispatch sets allowed_company_ids and website_id context -> routes/rules use website_domain(). Cookie flow: ir.http._is_allowed_cookie('optional') -> website.cookies_bar -> cookie website_cookies_bar. Visitor flow: _post_dispatch -> _register_website_track -> website.visitor._handle_webpage_dispatch -> upsert + track. Authentication hook merges visitors. Reveal flow: _serve_page override inserts crm.reveal.view; daily cron sends IPs to the IAP service. [C082 C108 C109] [C091 C092 C093 C094] [C097 C098 C100] [C101] [C104 C105 C106]

State diagram (list):
- anonymous visitor created [first tracked page, hash of ip+user agent+session]
- anonymous visitor -> contact visitor [login, merge]
- visitor -> deleted [idle for 60 days, no partner, no lead; daily cron]
- cookie consent unset -> accepted/refused [website_cookies_bar cookie, bar enabled]
- reveal view to_process -> not_found or lead created [daily IAP cron]

Ten-dimension table:

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Request host selects the website, language and company context; tracked pages create visits [C082 C108 C109] [C097 C098 C100]. |
| 2 Reversal / cancel / negative path | Merging visitors on login; purge job deletes idle anonymous visitors; cookie bar off/on creates or deletes the policy page [C101] [C102 C103] [C096 C107]. |
| 3 Multi-company / data-scope | One company in DB; website sets allowed_company_ids; sign-up users get the website company; login names unique per website; website_id enforced via website_domain and _pre_dispatch [C085 C086 C087] [C083] [C084]. |
| 4 Side effects & cross-module triggers | Visitors feed leads (website_crm), live chat, events, SMS composer; reveal rules create leads via IAP [C112 C113] [C104 C105 C106]. |
| 5 Configuration & optionality | Per-website settings: domain, cookie bar, 3rd-party blocking, signup scope, specific_user_account, retention ICP [C096 C107]. |
| 6 Validation & constraints | Unique domain; unique login/website; company with website cannot be archived [C084]. |
| 7 Roles & permissions | Designer/system groups for visitors; public routes create visitors via sudo; DB: res.groups group_multi_website seeded [C097 C098 C100]. |
| 8 Scheduled / automated behaviour | website_visitor_cron daily active; reveal cron daily active; snippets cron weekly [C102 C103] [C096 C107]. |
| 9 Exception & failure behaviour | Cookie parse failure resets legacy cookie; reveal errors are swallowed so page views never fail; unknown website falls back to first [C082 C108 C109] [C104 C105 C106]. |
| 10 Accounting, stock, audit, security & compliance | Privacy/compliance: consent bar controls only optional cookies and embeds, visitor profiling and IP forwarding to reveal service are not gated [C099] [C104 C105 C106]; DB has 29 websites with cookies_bar false [C275]; global sharing gaps [C110 C111]. |

**DB reconciliation (restored DB, configuration only):** Restored DB: 29 websites (1 My Website + 28 theme websites from 30 installed theme modules), all with cookies_bar false, block_third_party_domains true, domain empty, specific_user_account false, auth_signup_uninvited b2b, 1 company, only 1 website has a live chat channel set; 4 visitor rows (count only); crm_reveal_rule 0 rows; ICP auth_signup.invitation_scope b2c and auth_signup.reset_password True, base.login_cooldown_after 10. Crons: website_visitor_cron daily (active), ir_cron_crm_reveal_lead daily (active). website_crm_iap_reveal ACL 4 and rules 4 equal source.

**Unknown / Runtime list:**
- GeoIP availability [C260].
- Legal sufficiency of consent handling is outside the evidence.
- Which of the 28 theme websites are intentionally live: their content and domains were not inspected (domains are empty).

## CAP-U19-04 Blog, partner showcase pages, and follow subscriptions

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 (business purpose & process semantics)** Business purpose: publish blog articles and partner/customer showcase pages, notify followers, let reseller partners work assigned leads from the portal, and allow anonymous follows. [C276] [C277]

**D2 (architecture / data / object relationships)** Objects: blog.blog, blog.post (mail.thread, website.published.multi.mixin, seo, cover, searchable), blog.tag, res.partner (website_partner: website_description, is_published), res.partner.grade, crm.lead partner_assigned_id/partner_declined_ids, mail.followers, website.visitor. [C114 C115 C116] [C127 C128 C129 C137] [C131 C132 C136]

**D3 (source / technical / workflow logic)** Flow: /blog routes render posts filtered by website_domain and post_date; publish write sets published_date and posts a message; follow route -> record.check_access(read) -> _partner_find_from_emails_single -> message_subscribe/unsubscribe (sudo). Partner pages: /partners/<slug> sudo browse -> render. Assigned leads: portal routes call crm.lead model methods guarded by _assert_portal_write_access. [C114 C115 C116] [C117 C118] [C123 C124 C126] [C131 C132 C136]

State diagram (list):
- post draft -> published [is_published True, published_date now]
- published -> hidden until post_date [post_date in future]
- published -> archived [active False sets is_published False]
- lead assigned -> interested/converted [portal partner accepts] or -> declined [partner declines; optional spam tag]

Ten-dimension table:

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Designer publishes a post, followers are notified, visitors read it [C114 C115 C116] [C117 C118]. |
| 2 Reversal / cancel / negative path | Archive unpublishes; decline returns the lead to unassigned with the declining partner remembered [C117 C118] [C119 C133]. |
| 3 Multi-company / data-scope | Posts and blogs may carry website_id; blog lists use website_domain; partner showcase is not website-scoped [C114 C115 C116] [C130]. |
| 4 Side effects & cross-module triggers | Publishing posts to blog followers; partner acceptance converts a lead to an opportunity and may create activities [C117 C118] [C131 C132 C136]. |
| 5 Configuration & optionality | Blog website assignment, scheduling, partner grade publication, Google map key [C278]. |
| 6 Validation & constraints | Portal write limited to commercial-entity leads; opportunity creation needs a grade [C135]. |
| 7 Roles & permissions | Public/portal read published; designers write; portal reseller methods use sudo after ownership check; DB: website_blog ACL 16 and rules 2, website_crm_partner_assign ACL 11 and rules 4, website_customer ACL 6 rule 1 equal source [C114 C115 C116] [C131 C132 C136]. |
| 8 Scheduled / automated behaviour | No crons in these modules; scheduled posts use post_date comparison at read time [C114 C115 C116]. |
| 9 Exception & failure behaviour | Unknown post redirects to the blog; accessing a lead without right raises AccessError [C135]. |
| 10 Accounting, stock, audit, security & compliance | Security: unauthenticated follow/unfollow by email [C125]; unsanitised article HTML [C120]; sudo partner pages and maps [C130]; stage change not validated [C134]. No accounting impact. |

**DB reconciliation (restored DB, configuration only):** Restored DB: 1 blog ('Our blog', no website assigned), blog_post 0 rows, res_partner rows flagged published: 1 (count only), website_track 5 rows. website_blog ir_model_access 16 and ir_rule 2, website_partner none, website_crm_partner_assign ir_model_access 11 and ir_rule 4, website_customer ACL 6 rule 1, website_google_map no ACL: all equal source declarations. No cron owned by these modules.

**Unknown / Runtime list:**
- Blog comment posting route (portal chatter in module portal) [C261].
- Template content of showcase pages beyond the address block; sitemap generation was not read.

## CAP-U19-05 Community forum and public profiles with reputation-gated actions

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 (business purpose & process semantics)** Business purpose: run a self-moderating Q&A community where reputation unlocks capabilities, with public profiles that surface expertise. [C280] [C281]

**D2 (architecture / data / object relationships)** Objects: forum.forum (privacy, mode, authorized_group_id, all karma_* thresholds), forum.post (parent_id, state, vote, favourite), forum.post.vote, forum.post.reason, forum.tag, res.users.karma (gamification), website.karma_profile_min. [C138 C139] [C142 C144 C148]

**D3 (source / technical / workflow logic)** Flow: public read routes -> ir.rule privacy; signed-in routes (/ask, /new, /reply, comment, vote, flag, close, delete, validate) -> forum.post.create/write enforce karma computed in _compute_post_karma_rights; profile routes -> _check_user_profile_access. Question author below karma_post -> pending -> moderator validate. [C145 C150 C151 C156] [C143 C146] [C153 C154]

State diagram (list):
- question created -> pending [author karma < karma_post]
- pending -> active [moderator validate, karma_moderate]
- active -> flagged -> offensive or active [flag, moderate]
- active -> closed -> active [close/reopen with karma]
- active -> deleted(archived) -> active [unlink/undelete with karma]

Ten-dimension table:

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Signed-in user asks/answers; reputation awarded; others vote/comment [C142 C144 C148] [C145 C150 C151 C156]. |
| 2 Reversal / cancel / negative path | Delete/close/reopen/refuse paths each with karma thresholds and karma reversal; undelete exists [C147]. |
| 3 Multi-company / data-scope | Forum privacy controls visibility; no company field on forum models; website scoping not applied by the studied controller code [C138 C139]. |
| 4 Side effects & cross-module triggers | Karma changes, notifications to followers, badges via gamification; question edit/answer edit messages [C147] [C142 C144 C148]. |
| 5 Configuration & optionality | All thresholds per forum; privacy; mode; website karma_profile_min [C142 C144 C148] [C153 C154]. |
| 6 Validation & constraints | Closed/deleted parents refuse answers; valid email required to ask; karma errors raise AccessError [C145 C150 C151 C156]. |
| 7 Roles & permissions | Portal and employees can write forum.post at ACL level, public read only; real checks in model; managers (base.group_erp_manager) all; DB ACL 15 and rules 12 equal source [C140 C141] [C138 C139]. |
| 8 Scheduled / automated behaviour | No cron in website_forum or website_profile. |
| 9 Exception & failure behaviour | AccessError on insufficient karma; redirect to profile to complete email; flagged queue for moderators [C145 C150 C151 C156]. |
| 10 Accounting, stock, audit, security & compliance | Security: reputation gaming is possible by design; contact existence oracle [C152]; sign-up scope interplay [C158]; user biography exposure controlled by karma_user_bio. Compliance: published profile exposes personal data only with owner flag [C153 C154]. |

**DB reconciliation (restored DB, configuration only):** Restored DB: 1 forum (privacy public, questions mode, active); website_forum ir_model_access 15 and ir_rule 12 equal source; website_profile ACL 1 equal source; no res.groups or crons owned; ICP auth_signup.invitation_scope b2c seeded by website_forum while all websites override with b2b.

**Unknown / Runtime list:**
- Vote/flag karma arithmetic and moderation queues [C262].
- Badge awarding rules (gamification, outside unit).

## CAP-U19-06 Online courses: visibility, enrolment, invitations and completion

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 (business purpose & process semantics)** Business purpose: sell or share training content online with controlled enrolment, tracked progress, quizzes and reputation. [C284] [C285]

**D2 (architecture / data / object relationships)** Objects: slide.channel (visibility, enroll, enroll_group_ids, upload_group_ids, user_id), slide.slide, slide.channel.partner (member_status invited/joined/completed), slide.slide.partner, slide.question/answer, slide.channel.invite wizard, res.groups officer/manager. [C159 C160 C161 C175] [C162 C163 C164] [C165 C166 C167]

**D3 (source / technical / workflow logic)** Flow: /slides routes -> channel/slide ir.rule by visibility and membership; /slides/channel/join -> _action_add_members with _filter_add_members; /slides/<id>/invite with invite_hash -> consteq -> redirects or preview; quiz submit -> sudo answers compare -> _action_mark_completed -> channel completion recompute -> karma/ranks. Embed routes increment counters before access check. [C162 C163 C164] [C165 C166 C167] [C170] [C172]

State diagram (list):
- attendee invited -> joined [user enrols or accepts invite]
- joined -> completed [all slides completed]
- slide not viewed -> viewed -> completed [view, quiz pass or manual]
- invitation pending -> expired [3 months]

Ten-dimension table:

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Learner opens course, enrols if allowed, views lessons, passes quizzes, completes course [C159 C160 C161 C175] [C162 C163 C164] [C170]. |
| 2 Reversal / cancel / negative path | Leave channel and uncomplete lesson exist (auth=user); removed membership clears session answers [C286]. |
| 3 Multi-company / data-scope | Courses may carry website_id; slide routes check can_access_from_current_website; no company field [C159 C160 C161 C175]. |
| 4 Side effects & cross-module triggers | Reputation and rank updates, completion emails, course reviews via portal rating [C170] [C288]. |
| 5 Configuration & optionality | Visibility/enrol/upload groups/prerequisites configurable per course [C287]. |
| 6 Validation & constraints | Enrol policy constraint; quiz completeness; officers own-only writes [C162 C163 C164] [C174]. |
| 7 Roles & permissions | Officer (own courses), Manager (all) groups; DB res.groups group_website_slides_officer and group_website_slides_manager; ACL 41 and rules 21 equal source [C169] [C174]. |
| 8 Scheduled / automated behaviour | No cron in website_slides; invitation expiry evaluated at request time [C165 C166 C167]. |
| 9 Exception & failure behaviour | Forbidden handler redirects; 'expired' and 'hash_fail' invitation errors; embed forbidden template [C159 C160 C161 C175] [C173]. |
| 10 Accounting, stock, audit, security & compliance | Security/compliance: invitation links are bearer secrets; signup link creation by link holder [C168]; embed counter manipulation [C172]; quiz integrity [C171]; karma is the only 'financial' effect (none). |

**DB reconciliation (restored DB, configuration only):** Restored DB: slide_channel 0 rows; website_slides ir_model_access 41, ir_rule 21, res.groups 2 (officer, manager), mail templates 6 — all equal source; website_slides_survey ACL 5 and rules 5 equal source (module not studied in depth).

**Unknown / Runtime list:**
- website_slides_survey certification flows [C263].
- Slide file/document access tokens and payment (shop not installed).

## CAP-U19-07 Live chat sessions, chat bots and visitor conversion

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 (business purpose & process semantics)** Business purpose: engage website visitors in real time through human agents or scripted bots, capture contact data and leads, collect ratings and keep a conversation log. [C289] [C290]

**D2 (architecture / data / object relationships)** Objects: im_livechat.channel (user_ids, rules, max_sessions, review_link), im_livechat.channel.rule, chatbot.script/step/answer/message, discuss.channel (livechat), mail.guest, rating.rating, website.visitor, crm.lead. [C176 C177 C178] [C179 C180] [C182]

**D3 (source / technical / workflow logic)** Flow: web client init (match_rule) -> /im_livechat/get_session (public) -> _get_operator_info -> _get_livechat_discuss_channel_vals -> sudo create discuss.channel -> bus broadcast; chatbot step routes -> chatbot.script.step._process_answer/_process_step; feedback route creates/updates rating; close routes end the session. website_livechat links visitor and cancels pending chat requests. [C176 C177 C178] [C184] [C187] [C191 C192]

State diagram (list):
- session started -> in_progress [get_session]
- in_progress -> closed [visitor leaves or agent closes]
- operator chat request pending -> cancelled [visitor starts own chat]
- bot step -> next step -> forward operator or lead [script logic]

Ten-dimension table:

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Visitor chats with an agent or bot, may rate, may become a lead [C176 C177 C178] [C184] [C187]. |
| 2 Reversal / cancel / negative path | Visitor leaves session; pending chat requests cancelled; chat message of closure [C191 C192]. |
| 3 Multi-company / data-scope | Channel not company-scoped in the studied code; website link via website.channel_id; guest per session [C176 C177 C178]. |
| 4 Side effects & cross-module triggers | Creates guests, partners (bot email), ratings, leads, visitor links [C185] [C193 C194 C195]. |
| 5 Configuration & optionality | Agents, capacity mode, rules, bot scripts, languages, review link [C181] [C179 C180]. |
| 6 Validation & constraints | Capacity > 0; email validation in bot; internal-only transcript email [C186 C188]. |
| 7 Roles & permissions | Groups im_livechat_group_user/manager; livechat users read all livechat channels; DB: ACL 15, rules 3, groups 2 equal source [C189 C190]. |
| 8 Scheduled / automated behaviour | No cron in im_livechat/website_livechat; session closure is event driven. |
| 9 Exception & failure behaviour | Unavailable operator returns False; invalid email stays in step [C186 C188] [C176 C177 C178]. |
| 10 Accounting, stock, audit, security & compliance | Security: anonymous session creation without challenge [C291]; button rules are not access rules [C183]; contact creation from anonymous input [C185]. Chat content is personal data retained in discuss.channel. |

**DB reconciliation (restored DB, configuration only):** Restored DB: im_livechat_channel 1 row ('YourWebsite.com'), linked to 1 website; im_livechat ACL 15, rules 3, res.groups 2 (user, manager) equal source; website_livechat ACL 2 and no rules; no crons.

**Unknown / Runtime list:**
- Guest cookie and bus behaviour [C264].
- AI/operator extensions are not present in Community code studied.

## CAP-U19-08 Public event registration and booth booking

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 (business purpose & process semantics)** Business purpose: sell or take registrations for events online and lease booths, without accounts, capturing attendee and lead data. [C292] [C293]

**D2 (architecture / data / object relationships)** Objects: event.event, event.event.ticket, event.slot, event.registration (+answers), event.question, event.booth/category, website.event.menu, website.visitor, crm lead rules. [C196] [C197] [C206 C208]

**D3 (source / technical / workflow logic)** Flow: /event/<id>/register -> tickets selection -> /registration/new (form render) -> /registration/confirm (captcha hook, process form, verify seats, sudo create registrations with visitor) -> success page by visitor. Booth: /booth -> /booth/register -> register_form -> /booth/confirm -> _get_requested_booths -> action_confirm with partner from email. [C201 C202] [C199 C200 C205] [C206 C208]

State diagram (list):
- registration created (draft/open by event settings) -> confirmed [auto confirm or organiser]
- booth available -> booked [booth confirm]
- ticket not launched/expired -> refused [process form]

Ten-dimension table:

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Visitor chooses tickets/slots, fills attendee form, registrations are created [C201 C202] [C199 C200 C205]. |
| 2 Reversal / cancel / negative path | Cancel/reversal of registrations lives in the event module (not read); booth unbook is back-office. |
| 3 Multi-company / data-scope | Events carry website_id and are checked by can_access_from_current_website through route models; booth listing endpoints do not [C196] [C209]. |
| 4 Side effects & cross-module triggers | Leads from lead rules; visitors updated; partner created for booth contact [C210] [C206 C208]. |
| 5 Configuration & optionality | Seat limits, slots, ticket windows, questions, booth categories [C295]. |
| 6 Validation & constraints | Seat checks twice; ticket availability; booth category uniqueness [C201 C202] [C206 C208]. |
| 7 Roles & permissions | Public/portal read published; registration by sudo; event groups for staff; DB ACL 27 and rules 8 (website_event), ACL 4 and rule 1 (booth) equal source [C196]. |
| 8 Scheduled / automated behaviour | No crons in these modules (event schedulers belong to event module). |
| 9 Exception & failure behaviour | recaptcha_failed and insufficient_seats redirects; boothError and existingPartnerError JSON [C201 C202] [C207]. |
| 10 Accounting, stock, audit, security & compliance | Security: partner linkage and contact oracle [C198] [C207]; unpublished-event booth disclosure [C209]; no payment (shop not installed); personal data in registrations. |

**DB reconciliation (restored DB, configuration only):** Restored DB: event_event 0 rows; website_event ir_model_access 27 and ir_rule 8, website_event_booth ACL 4 and rule 1, website_event_crm none — equal source; ICP none; the 'Event: Mail Scheduler' and 'Event CRM' crons belong to event/event_crm (outside this unit).

**Unknown / Runtime list:**
- Concurrent seat overbooking [C265].
- Track, sponsor, quiz and shop features are not installed here.

## CAP-U19-09 Newsletter subscription, public mailing groups and rating feedback links

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 (business purpose & process semantics)** Business purpose: build a consented audience (newsletters, discussion groups) and measure satisfaction through email links, with minimal friction for the visitor. [C297] [C298]

**D2 (architecture / data / object relationships)** Objects: mailing.list (is_public), mailing.contact, mailing.subscription (opt_out), mail.group, mail.group.member, mail.group.message, mail.group.moderation, rating.rating (access_token, consumed, publisher_comment). [C211 C212] [C218 C220 C221 C222] [C228 C229]

**D3 (source / technical / workflow logic)** Flow: newsletter subscribe -> verify captcha -> sudo find/create contact -> find/create subscription or reset opt_out -> session stores email. Group subscribe -> check group token or read access -> public: email with action token -> confirm route -> join. Rating: /rate/<token>/<value> -> render form; POST submit_feedback -> rating_apply -> message on record. [C211 C212] [C218 C220 C221 C222] [C228 C229]

State diagram (list):
- not subscribed -> subscribed [subscribe]
- subscribed -> opted out [unsubscribe with token]
- opted out -> subscribed [public subscribe without confirmation]
- group non-member -> pending confirmation -> member [email token]
- rating requested -> submitted -> resubmitted [token reusable]

Ten-dimension table:

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Visitor subscribes; confirms group email; clicks rating link [C211 C212] [C218 C220 C221 C222] [C228 C229]. |
| 2 Reversal / cancel / negative path | Unsubscribe via token; group leave via email token or one-click; rating can be overwritten [C216 C223] [C218 C220 C221 C222] [C231]. |
| 3 Multi-company / data-scope | No website scoping on subscription endpoints; group visibility via access modes [C224 C225 C226]. |
| 4 Side effects & cross-module triggers | Subscription affects mailing audiences; group messages go to members; rating posts a chatter message [C211 C212] [C228 C229]. |
| 5 Configuration & optionality | List public flag, group access mode, moderation, captcha keys [C215]. |
| 6 Validation & constraints | Tokens are keyed hashes; rating values 1, 3 or 5 [C230 C232 C235]. |
| 7 Roles & permissions | Public/portal read groups by rule; managers/moderators write; rating ACL employees RW; DB ACL mail_group 9, rules 10, group 1; rating ACL 4; portal_rating none [C224 C225 C226] [C230 C232 C235]. |
| 8 Scheduled / automated behaviour | mail_group cron 'Mail List: Notify group moderators' daily active; moderation reminder in source [C214]. |
| 9 Exception & failure behaviour | Invalid token pages and 404s; captcha errors toast; invalid rating raises [C216 C223] [C211 C212]. |
| 10 Accounting, stock, audit, security & compliance | Compliance: consent evidence is weak for newsletter and public group paths [C300]; oracles and relay [C219] [C302]; list targeting [C301]; rating token reuse [C231]. |

**DB reconciliation (restored DB, configuration only):** Restored DB: mailing_list 1 public list ('Newsletter'), mail_group 0 rows; mail_group ir_model_access 9, ir_rule 10, res.groups 1 (group_mail_group_manager), ir_cron 1 (active, daily), mail templates 3, server actions 1 equal source; rating ACL 4 equal source; website_mass_mailing ACL 1; ICP mass_mailing.show_blacklist_buttons True.

**Unknown / Runtime list:**
- Mail group posting by alias and outgoing mail delivery [C266].

## CAP-U19-10 Donation payment hook and public integration endpoints

**Function-ID(s):** FUNCTION MAPPING REQUIRED

**D1 (business purpose & process semantics)** Business purpose: allow donations through the shared payment engine on the website, scope payment providers per website, and provide editor tools (link previews, stock photos, short links, map data). No online shop is installed, so no order checkout exists here. [C255] [C303]

**D2 (architecture / data / object relationships)** Objects: payment.provider (website_id), payment.transaction (is_donation), account.payment (is_donation related), mail.mail, link.tracker/code/click, ir.attachment (editor media), ICP unsplash.app_id/access_key, website.google_maps_api_key. [C236 C237 C246] [C238 C241] [C252]

**D3 (source / technical / workflow logic)** Flow: /donation/pay (public) -> payment_pay with is_donation -> /donation/transaction/<min> (public JSON) -> create tx with public partner -> send internal notification email now -> provider processing -> _post_process on done sends donor mail and logs payment chatter. Editor routes are auth=user except link_preview_external and get_app_id (public). [C238 C241] [C243] [C244] [C247]

State diagram (list):
- donation tx created -> pending [provider processing]
- pending -> done -> donor confirmation + chatter log [post-processing]
- pending -> error/cancel [provider outcome]

Ten-dimension table:

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Donor submits amount and details; transaction created; provider flow; confirmation [C238 C241] [C244]. |
| 2 Reversal / cancel / negative path | Failed/cancelled transaction sends no donor email; internal notification already sent [C243]. |
| 3 Multi-company / data-scope | Providers can be limited to a website; transactions use the website public partner and the company in context [C236 C237 C246] [C238 C241]. |
| 4 Side effects & cross-module triggers | Notification mail at creation; donor mail on success; payment chatter log [C243] [C244]. |
| 5 Configuration & optionality | Provider website assignment; donation snippet options; unsplash keys; google maps key [C236 C237 C246] [C249 C250 C251]. |
| 6 Validation & constraints | Name/email/country required; amount signed token; min amount from route [C238 C241] [C239] [C240]. |
| 7 Roles & permissions | Public may call donation routes; editors authenticated; DB payment providers 25 (custom enabled, demo test, others disabled), website_payment no ACL/rules [C236 C237 C246]. |
| 8 Scheduled / automated behaviour | No crons; payment post-processing is the payment engine's job. |
| 9 Exception & failure behaviour | Provider errors surface via payment engine; link preview failures return false [C247]. |
| 10 Accounting, stock, audit, security & compliance | Accounting: a donation payment creates a payment with is_donation flag; journal impact is in account_payment (not studied). Security: mail relay [C242]; min bypass [C305]; SSRF [C248]; host-header base address [C245]; open redirects [C253]. |

**DB reconciliation (restored DB, configuration only):** Restored DB: payment_provider 25 rows (custom enabled, demo test, 23 disabled; none has website_id); website_payment has no ACL, rule or cron; no website_sale module; ICP has no unsplash keys; link_tracker 0 rows; web_unsplash/html_editor ACL 2 (html_editor) equal source.

**Unknown / Runtime list:**
- Real provider callbacks and network egress controls [C254 C267].
- The exact accounting entries of donation payments (account_payment, account units).

## Claims table

Claim ids shortened in prose as `Cnnn` = `VDR-U19-Cnnn`.

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U19-C001 | FUNCTION MAPPING REQUIRED | website/models/ir_http.py:347 | website_page = cls._serve_page() | FACT | module website installed | — | _serve_fallback first lets the parent serve a stored attachment, then runs frontend pre-dispatch and _serve_page; a page is rendered only if no controller route and no attachment matched. | N-U19-001 |
| VDR-U19-C002 | FUNCTION MAPPING REQUIRED | website/models/ir_http.py:352 | redirect = cls._serve_redirect() | FACT | always | — | If no page matches, _serve_fallback falls through to website.rewrite redirects and returns an HTTP redirect with the stored redirect type. | N-U19-009 |
| VDR-U19-C003 | FUNCTION MAPPING REQUIRED | website/models/ir_http.py:361 | only designers can specify redirects | FACT | always | — | Redirect targets are emitted with local=False and a comment states this is safe because only designers can define redirects. | N-U19-009 |
| VDR-U19-C004 | FUNCTION MAPPING REQUIRED | website/models/website_page.py:489 | order='website_id asc' | FACT | always | — | _get_page_info searches website.page by exact url (then case-insensitive) restricted to website_domain(), ordering website_id asc so a website-specific page wins over a generic one. | N-U19-001 |
| VDR-U19-C005 | FUNCTION MAPPING REQUIRED | website/models/website_page.py:66 | page.date_publish < fields.Datetime.now() | FACT | always | — | is_visible is website_published and (no date_publish or date_publish in the past). | N-U19-006 |
| VDR-U19-C006 | FUNCTION MAPPING REQUIRED | website/models/website_page.py:461 | self.env.user.has_group('website.group_website_designer') or self.is_visible | FACT | always | — | _get_response_raw renders the page only if the user is a designer or the page is_visible, and the page is website-specific or the most specific view for the current website. | N-U19-006 |
| VDR-U19-C007 | FUNCTION MAPPING REQUIRED | website/security/website_security.xml:64 | website.page: portal/public: read published pages | FACT | always | — | ir.rule limits portal and public readers of website.page to website_published pages. | N-U19-006 |
| VDR-U19-C008 | FUNCTION MAPPING REQUIRED | website/models/mixins.py:247 | if 'is_published' in vals and any(not | FACT | always | — | website.published.mixin.write raises AccessError (message from _get_can_publish_error_message) when is_published is written by a user for whom can_publish is false. | N-U19-007 |
| VDR-U19-C009 | FUNCTION MAPPING REQUIRED | website/models/mixins.py:241 | if any(record.is_published and not record.can_publish | FACT | always | — | On create, any record that is published without the creator being able to publish raises AccessError. | N-U19-007 |
| VDR-U19-C010 | FUNCTION MAPPING REQUIRED | website/models/mixins.py:263 | _check_user_can_modify(record) | FACT | always | — | Default can_publish is computed by website._check_user_can_modify, i.e. publishing needs write access on the record. | N-U19-007 |
| VDR-U19-C011 | FUNCTION MAPPING REQUIRED | website/models/website.py:1968 | record.check_access('write') | FACT | always | — | website._check_user_can_modify simply checks write access on the record (overridable per module). | N-U19-007 |
| VDR-U19-C012 | FUNCTION MAPPING REQUIRED | website/models/website_page.py:87 | record.can_publish = True | FACT | user in website.group_website_designer | — | website.page._compute_can_publish short-circuits to True for the designer group. | N-U19-007 |
| VDR-U19-C013 | FUNCTION MAPPING REQUIRED | website/models/ir_ui_view.py:30 | ('password', 'With Password') | FACT | always | — | ir.ui.view.visibility selection offers Public, Signed In, Restricted Group and With Password. | N-U19-004 |
| VDR-U19-C014 | FUNCTION MAPPING REQUIRED | website/models/ir_ui_view.py:46 | crypt_context.hash(r.visibility_password_display) | FACT | always | — | A page password typed in visibility_password_display is stored hashed in visibility_password (field readable only by base.group_system) using the user's crypt context. | N-U19-005 |
| VDR-U19-C015 | FUNCTION MAPPING REQUIRED | website/models/ir_ui_view.py:416 | visibility == 'connected' and request.website.is_public_user() | FACT | always | — | _handle_visibility raises 403 for visibility 'connected' when the website user is public. | N-U19-004 |
| VDR-U19-C016 | FUNCTION MAPPING REQUIRED | website/models/ir_ui_view.py:423 | request.session.setdefault('views_unlock' | FACT | visibility == password | — | A correct visibility_password POST parameter verified against the stored hash adds the view id to session key views_unlock; otherwise 403 website_visibility_password_required. | N-U19-005 |
| VDR-U19-C017 | FUNCTION MAPPING REQUIRED | website/models/ir_ui_view.py:415 | if visibility and not request.env.user.has_group('website.group_website_designer') | FACT | always | — | Visibility checks are skipped for users in the designer group. | N-U19-004 |
| VDR-U19-C018 | FUNCTION MAPPING REQUIRED | website/models/ir_ui_view.py:451 | view._handle_visibility(do_raise=True) | FACT | always | — | ir.ui.view._render_template invokes _handle_visibility on the main template, so enforcement happens at render time (the docstring at line 407 says other views called by the main content remain available over RPC). | N-U19-004 |
| VDR-U19-C019 | FUNCTION MAPPING REQUIRED | website/security/website_security.xml:71 | Website View Visibility Public | FACT | always | — | ir.rule restricts public readers of qweb views to visibility in (public, False); a second rule allows connected visibility for portal. | N-U19-004 |
| VDR-U19-C020 | FUNCTION MAPPING REQUIRED | website/models/website_page.py:329 | only cache for unlogged user | FACT | always | — | _allow_to_use_cache is true only for GET without parameters, for a public user, and when the page has no group restriction. | N-U19-012 |
| VDR-U19-C021 | FUNCTION MAPPING REQUIRED | website/models/website_page.py:368 | request.website._allConsentsGranted(), | FACT | always | — | The cache key is (website id, language code, request path, debug flag, all-consents-granted); it does not contain the session unlock state of password-protected views. | N-U19-015 |
| VDR-U19-C022 | FUNCTION MAPPING REQUIRED | website/models/website_page.py:36 | _CACHE_DURATION = 3600 | FACT | always | — | A cached anonymous page response is considered valid for 3600 seconds. | N-U19-012 |
| VDR-U19-C023 | FUNCTION MAPPING REQUIRED | website/models/website_page.py:423 | tools.ormcache('self._get_cache_key(request)' | INFERENCE | cache enabled (dev mode xml not set) | RT | On a cache hit _get_response_cached does not re-execute _get_response_raw, so _render_template/_handle_visibility (lines ir_ui_view.py:403-451) is not re-run; combined with the cache key lacking session state, a page unlocked by one session (views_unlock) and re-fetched with no parameters can be inserted into the cache and replayed to other public visitors. Not executed. | N-U19-015 |
| VDR-U19-C024 | FUNCTION MAPPING REQUIRED | website_hr_recruitment/models/website_page.py:11 | /job-thank-you | FACT | website_hr_recruitment installed | — | The job thank-you page is explicitly excluded from the anonymous response cache. | N-U19-012 |
| VDR-U19-C025 | FUNCTION MAPPING REQUIRED | website_project/models/website_page.py:11 | /your-task-has-been-submitted | FACT | website_project installed | — | The task-submitted confirmation page is explicitly excluded from the anonymous response cache. | N-U19-012 |
| VDR-U19-C026 | FUNCTION MAPPING REQUIRED | website/models/website_page.py:214 | ('visibility', '!=', 'password') | FACT | user not designer | — | Page search excludes password pages, excludes connected pages for public users and requires published and indexed pages with matching group membership. | N-U19-008 |
| VDR-U19-C027 | FUNCTION MAPPING REQUIRED | website/models/website_page.py:205 | requires_sudo = True | FACT | always | — | Search reads website.page with sudo and re-applies an explicit domain, noting that the rule must be reinforced because of sudo. | N-U19-008 |
| VDR-U19-C028 | FUNCTION MAPPING REQUIRED | website/models/website_page.py:175 | .with_context(website_id=website_id).get_unique_path(url) | FACT | always | — | On write, a changed page url is slugified and made unique per website via get_unique_path; menu urls and homepage url are kept in sync. | N-U19-014 |
| VDR-U19-C029 | FUNCTION MAPPING REQUIRED | website/security/website_security.xml:18 | base.group_sanitize_override | FACT | always | — | website.group_website_designer implies group_website_restricted_editor and base.group_sanitize_override (HTML sanitising override). | N-U19-014 |
| VDR-U19-C030 | FUNCTION MAPPING REQUIRED | website/security/ir.model.access.csv:12 | access_website_page_designer | FACT | always | — | website.page ACL: only group_website_designer has CRUD; there is no ACL row for public/portal (public read happens through sudo in the router). | N-U19-014 |
| VDR-U19-C031 | FUNCTION MAPPING REQUIRED | website/security/website_security.xml:33 | website_designer_edit_qweb | FACT | always | — | A rule lets the designer group read/write/create/delete qweb views; non-qweb views are read-only for designers and base.group_system has a separate all-views rule. | N-U19-014 |
| VDR-U19-C032 | FUNCTION MAPPING REQUIRED | website/controllers/model_page.py:39 | if not Model.has_access("read") | FACT | always | — | generic_model raises Forbidden unless the current user (including public) has read access on the exposed model. | N-U19-010 |
| VDR-U19-C033 | FUNCTION MAPPING REQUIRED | website/controllers/model_page.py:44 | implements_published_mixin | FACT | exposed model has website_published | — | For non-designers the listing and detail domains add website_published = True only if the model has that field; models without it are listed by record_domain alone. | N-U19-002 |
| VDR-U19-C034 | FUNCTION MAPPING REQUIRED | website/controllers/model_page.py:73 | searches.setdefault("order", "create_date desc") | FACT | always | — | The order query parameter is passed to Model.search(order=...) without a controller-side whitelist. | N-U19-016 |
| VDR-U19-C035 | FUNCTION MAPPING REQUIRED | website/models/website_controller_page.py:58 | A page must be set to | FACT | always | — | Creating or retargeting a model page raises ValidationError for transient, abstract or non-table models and requires read access for the editor. | N-U19-010 |
| VDR-U19-C036 | FUNCTION MAPPING REQUIRED | website/security/website_security.xml:95 | Public access to arbitrary exposed model | FACT | always | — | A group website_page_controller_expose is implied by base.group_public and base.group_portal and carries the read rule for published website.controller.page records. | N-U19-002 |
| VDR-U19-C037 | FUNCTION MAPPING REQUIRED | website/controllers/main.py:136 | '/website/force/<int:website_id>' | FACT | always | — | Forcing a different website for the session is an authenticated (auth=user) route. | N-U19-013 |
| VDR-U19-C038 | FUNCTION MAPPING REQUIRED | website/models/ir_http.py:218 | if not record.can_access_from_current_website() | FACT | always | — | _pre_dispatch returns 404 for route model arguments whose website_id belongs to another website (403 if the field is unreadable). | N-U19-014 |
| VDR-U19-C039 | FUNCTION MAPPING REQUIRED | website/controllers/main.py:249 | '/sitemap.xml' | FACT | always | — | sitemap and crawler instruction routes are public (auth=public). | N-U19-001 |
| VDR-U19-C040 | FUNCTION MAPPING REQUIRED | website/security/website_security.xml:28 | Website menu: group_ids | FACT | always | — | A global rule hides website.menu entries whose group_ids does not intersect the user's groups. | N-U19-004 |
| VDR-U19-C041 | FUNCTION MAPPING REQUIRED | website/models/website_page.py:189 | if vals['visibility'] != 'restricted_group' | FACT | always | — | Writing a visibility other than restricted_group clears group_ids on the page. | N-U19-011 |
| VDR-U19-C042 | FUNCTION MAPPING REQUIRED | website/models/website_page.py:190 | vals['group_ids'] = False | FACT | always | — | Group restriction is reset when visibility changes away from restricted_group. | N-U19-011 |
| VDR-U19-C043 | FUNCTION MAPPING REQUIRED | website/models/website_page.py:192 | 'url' in vals or 'visibility' in | FACT | always | — | Writing url, visibility or group_ids clears the template registry cache because the response depends on path and rendering. | N-U19-012 |
| VDR-U19-C044 | FUNCTION MAPPING REQUIRED | website/models/website_page.py:152 | views_to_delete = self.view_id.filtered( | FACT | always | — | Deleting a page also deletes its view unless the view is shared with another page or has inheriting child views (the ORM does not cascade from page to view). | N-U19-011 |
| VDR-U19-C045 | FUNCTION MAPPING REQUIRED | website/controllers/form.py:31 | captcha='website_form' | FACT | always | — | POST /website/form/<model_name> is auth=public, csrf=False, website=True and declares captcha='website_form'. | N-U19-029 |
| VDR-U19-C046 | FUNCTION MAPPING REQUIRED | website/controllers/form.py:38 | if request.session.uid and not request.validate_csrf | FACT | always | — | CSRF token is validated only when the session is authenticated; anonymous posts are exempt. | N-U19-033 |
| VDR-U19-C047 | FUNCTION MAPPING REQUIRED | website/controllers/form.py:46 | with request.env.cr.savepoint() as sp | FACT | always | — | The whole form handling runs in a savepoint; ValidationError/UserError are returned as JSON {'error': ...} and the savepoint rolls back. | N-U19-030 |
| VDR-U19-C048 | FUNCTION MAPPING REQUIRED | website/controllers/form.py:63 | ('website_form_access', '=', True) | FACT | always | — | The target model must exist in ir.model with website_form_access True, else an error JSON is returned. | N-U19-021 |
| VDR-U19-C049 | FUNCTION MAPPING REQUIRED | website/models/website_form.py:46 | website_form_blacklisted', '=', False | FACT | model != mail.mail | — | _get_form_writable_fields allows only ir.model.fields rows whose website_form_blacklisted is False. | N-U19-022 |
| VDR-U19-C050 | FUNCTION MAPPING REQUIRED | website/models/website_form.py:229 | 'Blacklisted in web forms', default=True | FACT | always | — | website_form_blacklisted defaults to True, and init() sets the SQL column default true so fields are opt-in (whitelist). | N-U19-022 |
| VDR-U19-C051 | FUNCTION MAPPING REQUIRED | website/models/website_form.py:211 | if not self.env.user.has_group('website.group_website_designer') | FACT | always | — | formbuilder_whitelist (raw SQL UPDATE that un-blacklists fields) returns False unless the caller is in website.group_website_designer. | N-U19-022 |
| VDR-U19-C052 | FUNCTION MAPPING REQUIRED | website/models/website_form.py:68 | Remove readonly, JSON, and magic fields | FACT | always | — | Readonly, many2one_reference, json and magic fields are removed from the authorised field map; string domains are dropped. | N-U19-022 |
| VDR-U19-C053 | FUNCTION MAPPING REQUIRED | website/models/website_form.py:63 | Unrequire fields with default values | FACT | always | — | Fields that have a default value are made non-required for the form. | N-U19-033 |
| VDR-U19-C054 | FUNCTION MAPPING REQUIRED | website/models/website_form.py:40 | 'email_to', 'email_cc', 'email_bcc' | FACT | model == mail.mail | — | For mail.mail the writable set is hard-coded (email_from, email_to, email_cc, email_bcc, body, reply_to, subject) instead of using the blacklist flag. | N-U19-024 |
| VDR-U19-C055 | FUNCTION MAPPING REQUIRED | website/controllers/form.py:270 | with_user(SUPERUSER_ID).with_context( | FACT | always | — | insert_record creates the record as SUPERUSER with mail_create_nosubscribe, i.e. the visitor never needs create rights on the target model. | N-U19-019 |
| VDR-U19-C056 | FUNCTION MAPPING REQUIRED | website/controllers/form.py:233 | elif field_name not in ('context', 'website_form_signature') | FACT | always | — | Any posted input that is not an authorised field becomes a 'custom' field, joined as text and written to the model's website_form_default_field_id or logged as a comment message. | N-U19-022 |
| VDR-U19-C057 | FUNCTION MAPPING REQUIRED | website/controllers/form.py:314 | request.env['ir.attachment'].sudo().create(attachment_value) | FACT | always | — | Uploaded files are stored as sudo ir.attachment linked to the new record; no size/mimetype check appears in this controller. | N-U19-023 |
| VDR-U19-C058 | FUNCTION MAPPING REQUIRED | website/controllers/form.py:239 | website_form_enable_metadata | FACT | ICP set | — | If ICP website_form_enable_metadata is set, IP, user agent, accept-language and referer are appended to the record notes. | N-U19-025 |
| VDR-U19-C059 | FUNCTION MAPPING REQUIRED | website/controllers/form.py:92 | invalid website_form_signature | FACT | model == mail.mail and email_to/cc posted | — | For mail.mail, when email_to or a cc field is posted the HMAC website_form_signature must match consteq; otherwise AccessDenied (inside the savepoint, rolled back). | N-U19-024 |
| VDR-U19-C060 | FUNCTION MAPPING REQUIRED | website/controllers/form.py:93 | request.env[model_name].sudo().browse(id_record).send() | FACT | model == mail.mail | — | The created mail.mail is sent immediately (sudo .send()) instead of waiting for the queue. | N-U19-024 |
| VDR-U19-C061 | FUNCTION MAPPING REQUIRED | website/controllers/form.py:101 | form_builder_model_model | FACT | always | — | After success the session stores the model, name and id of the created record for the confirmation page. | N-U19-030 |
| VDR-U19-C062 | FUNCTION MAPPING REQUIRED | website/controllers/form.py:98 | except IntegrityError | FACT | always | — | A database IntegrityError (e.g. SQL constraints not checked generically) returns json false without a field name. | N-U19-033 |
| VDR-U19-C063 | FUNCTION MAPPING REQUIRED | base/models/ir_http.py:350 | captcha = endpoint.routing.get('captcha') | FACT | route declares captcha and unsafe HTTP method | — | The dispatcher calls _verify_request_recaptcha_token(captcha) for non-safe methods on routes that declare captcha; the base implementation returns without checking. | N-U19-029 |
| VDR-U19-C064 | FUNCTION MAPPING REQUIRED | google_recaptcha/models/ir_http.py:82 | return 'no_secret' | FACT | module google_recaptcha installed and no private key | — | _verify_recaptcha_token returns 'no_secret' when ICP recaptcha_private_key is empty, and the caller treats 'no_secret' as success (accepts the request). | N-U19-029 |
| VDR-U19-C065 | FUNCTION MAPPING REQUIRED | google_recaptcha/models/ir_http.py:50 | recaptcha_result in ['is_human', 'no_secret'] | FACT | google_recaptcha installed | — | Verification passes for is_human and no_secret, raising errors for wrong key, wrong token, timeout, bad request and bot score; the call to the external service has a 2 second timeout. | N-U19-029 |
| VDR-U19-C066 | FUNCTION MAPPING REQUIRED | google_recaptcha/models/ir_http.py:85 | www.recaptcha.net/recaptcha/api/siteverify | FACT | private key set | RT | Verification POSTs the secret, token and visitor IP to the recaptcha.net siteverify endpoint (external network behaviour is RT). | N-U19-032 |
| VDR-U19-C067 | FUNCTION MAPPING REQUIRED | auth_signup/controllers/main.py:39 | captcha='signup' | FACT | always | — | Outside website_form, only signup and password-reset routes declare captcha= in the studied addons; other public endpoints in this unit (newsletter, event registration, follow) call the verifier explicitly or not at all. | N-U19-037 |
| VDR-U19-C068 | FUNCTION MAPPING REQUIRED | website_crm/data/ir_model_data.xml:20 | 'team_id', | FACT | website_crm installed | — | The crm.lead form whitelist includes team_id and user_id (as well as name, contact_name, partner_name, email_from, phone, description, lead_properties). | N-U19-034 |
| VDR-U19-C069 | FUNCTION MAPPING REQUIRED | website_crm/models/crm_lead.py:57 | values['user_id'] = values.get('user_id') or | FACT | website_crm installed | — | website_form_input_filter keeps visitor-supplied team_id/user_id and falls back to website crm_default_team/user only when absent; type becomes lead or opportunity by team.use_leads. | N-U19-034 |
| VDR-U19-C070 | FUNCTION MAPPING REQUIRED | website_crm/controllers/website_form.py:64 | visitor_partner.email_normalized == values_email_normalized | FACT | website_crm installed | — | If the posted email equals the visitor's partner email, partner_id is set on the lead (phone is only reused when equal or empty); company_id defaults to the website company. | N-U19-026 |
| VDR-U19-C071 | FUNCTION MAPPING REQUIRED | website_crm/controllers/website_form.py:87 | vals = {'lead_ids': [(4, result)]} | FACT | website_crm installed | — | The created lead is linked to the website.visitor (lead_ids) and the visitor name is set from the contact name when the visitor had none. | N-U19-026 |
| VDR-U19-C072 | FUNCTION MAPPING REQUIRED | website_crm/controllers/website_form.py:41 | phone_validation.phone_format( | FACT | website_crm installed | — | Posted phone fields are formatted to international format using the posted country, the visitor partner country, or GeoIP country. | N-U19-026 |
| VDR-U19-C073 | FUNCTION MAPPING REQUIRED | website_hr_recruitment/models/hr_applicant.py:18 | The job offer has been closed | FACT | website_hr_recruitment installed | — | website_form_input_filter refuses applications when the posted job_id is not active (only the active flag is checked, not website_published or website_id). | N-U19-038 |
| VDR-U19-C074 | FUNCTION MAPPING REQUIRED | website_hr_recruitment/models/hr_applicant.py:24 | values['stage_id'] = stage.id | FACT | website_hr_recruitment installed | — | The applicant stage is set to the first unfolded stage valid for the job. | N-U19-027 |
| VDR-U19-C075 | FUNCTION MAPPING REQUIRED | website_hr_recruitment/data/config_data.xml:34 | 'linkedin_profile', | FACT | website_hr_recruitment installed | — | hr.applicant form whitelist: email_from, partner_name, partner_phone, job_id, department_id, linkedin_profile, applicant_properties. | N-U19-027 |
| VDR-U19-C076 | FUNCTION MAPPING REQUIRED | website_hr_recruitment/controllers/main.py:203 | check_recent_application | FACT | website_hr_recruitment installed | — | Public JSON-RPC /website_hr_recruitment/check_recent_application searches hr.applicant with sudo by name, email, phone or LinkedIn value and reports refused or ongoing applications. | N-U19-035 |
| VDR-U19-C077 | FUNCTION MAPPING REQUIRED | website_hr_recruitment/controllers/main.py:238 | recruiter_contact | FACT | ongoing application has recruiter | — | For an ongoing application of the same job the response text includes the recruiter user's name, email and phone. | N-U19-035 |
| VDR-U19-C078 | FUNCTION MAPPING REQUIRED | website_project/controllers/main.py:53 | data['record']['partner_id'] = partner.id | FACT | website_project installed | — | For project.task forms, a posted email_from is matched to an existing contact (no_create) and that contact becomes the task partner; email_from is read from raw values although it is not whitelisted. | N-U19-036 |
| VDR-U19-C079 | FUNCTION MAPPING REQUIRED | website_project/data/website_project_data.xml:18 | 'project_id', | FACT | website_project installed | — | project.task form whitelist includes project_id, so the visitor chooses the target project. | N-U19-028 |
| VDR-U19-C080 | FUNCTION MAPPING REQUIRED | website_mass_mailing/data/ir_model_data.xml:18 | 'list_ids', | FACT | website_mass_mailing installed | — | mailing.contact form whitelist includes list_ids (mailing lists), email, names, tags and country. | N-U19-019 |
| VDR-U19-C081 | FUNCTION MAPPING REQUIRED | website/models/website_form.py:18 | request.session['form_builder_model_model'] | FACT | always | — | Website._website_form_last_record reads the created record back from the session. | N-U19-030 |
| VDR-U19-C082 | FUNCTION MAPPING REQUIRED | website/models/website.py:1378 | the website forced in session `force_website_id` | FACT | always | — | get_current_website resolves in order: session force_website_id, context website_id, request host (frontend or fallback), then the first website. | N-U19-040 |
| VDR-U19-C083 | FUNCTION MAPPING REQUIRED | website/models/website.py:106 | return Domain('website_id', 'in', [False, *self.ids]) | FACT | always | — | website_domain() = records with website_id empty or equal to the website; used by page, blog, event, job and filter searches. | N-U19-043 |
| VDR-U19-C084 | FUNCTION MAPPING REQUIRED | website/models/website.py:218 | _domain_unique = models.Constraint( | FACT | always | — | website.domain is unique (SQL constraint). | N-U19-053 |
| VDR-U19-C085 | FUNCTION MAPPING REQUIRED | website/models/res_users.py:17 | 'unique (login, website_id)' | FACT | always | — | res.users has unique(login, website_id); _check_login separately forbids duplicate logins when website_id is empty. | N-U19-044 |
| VDR-U19-C086 | FUNCTION MAPPING REQUIRED | website/models/res_users.py:41 | return super()._get_login_domain(login) & website.website_domain() | FACT | always | — | Login and email lookups are restricted to users of the current website or without website. | N-U19-044 |
| VDR-U19-C087 | FUNCTION MAPPING REQUIRED | website/models/res_users.py:58 | values['company_id'] = current_website.company_id.id | FACT | always | — | Sign-up users are created in the website company; website_id is set only when website.specific_user_account is true (otherwise portal users can log in on all websites). | N-U19-044 |
| VDR-U19-C088 | FUNCTION MAPPING REQUIRED | website/models/res_users.py:68 | current_website.auth_signup_uninvited or super | FACT | always | — | The sign-up scope is the website's auth_signup_uninvited if set, else the global ICP; website.auth_signup_uninvited defaults to b2b (invitation). | N-U19-045 |
| VDR-U19-C089 | FUNCTION MAPPING REQUIRED | website/models/website.py:214 | ('b2b', 'On invitation'), | FACT | always | — | website.auth_signup_uninvited selection is b2b (On invitation) or b2c (Free sign up), default b2b. | N-U19-045 |
| VDR-U19-C090 | FUNCTION MAPPING REQUIRED | website_forum/data/ir_config_parameter_data.xml:3 | auth_signup.invitation_scope | FACT | website_forum installed | — | website_forum sets the global ICP auth_signup.invitation_scope to b2c at install (noupdate); DB observation: ICP is b2c while all 29 websites have b2b, so the website override wins. | N-U19-045 |
| VDR-U19-C091 | FUNCTION MAPPING REQUIRED | website/models/website.py:131 | cookies_bar = fields.Boolean('Cookies Bar' | FACT | always | — | Website.cookies_bar defaults to False; block_third_party_domains defaults to True. | N-U19-046 |
| VDR-U19-C092 | FUNCTION MAPPING REQUIRED | website/models/ir_http.py:432 | Cookies bar is disabled on this | FACT | always | — | _is_allowed_cookie('optional') returns True when the website has no cookie bar; otherwise it reads the website_cookies_bar cookie dict and returns accepted['optional'] or False. | N-U19-046 |
| VDR-U19-C093 | FUNCTION MAPPING REQUIRED | base/models/ir_http.py:452 | return True if cookie_type == 'required' | FACT | always | — | The base implementation allows required cookies always and optional cookies only when a user environment exists. | N-U19-046 |
| VDR-U19-C094 | FUNCTION MAPPING REQUIRED | website/models/website.py:2377 | user implemented his own consent behavior | FACT | cookies_bar off | — | _allConsentsGranted doc: with no cookie bar, consent is deemed fully granted, assuming the operator implemented consent through custom code. | N-U19-046 |
| VDR-U19-C095 | FUNCTION MAPPING REQUIRED | website/models/website.py:2402 | and not self.env.user.has_group('website.group_website_restricted_editor') | FACT | cookies_bar and block_third_party_domains | — | Third-party scripts/iframes are stripped from HTML only when the bar is on, blocking is on, optional cookies are not accepted and the viewer is not an editor. | N-U19-046 |
| VDR-U19-C096 | FUNCTION MAPPING REQUIRED | website/models/website.py:365 | existing_policy_page.unlink() | FACT | write cookies_bar | — | Turning the cookie bar off deletes the /cookie-policy page; turning it on creates a published page from the cookie_policy view. | N-U19-051 |
| VDR-U19-C097 | FUNCTION MAPPING REQUIRED | website/models/website_visitor.py:49 | hashlib.sha1(msg).hexdigest()[:32] | FACT | public user | — | For public users the visitor access_token is sha1 of (remote_addr, user agent, session sid)[:32]; for signed-in users it is the partner id. | N-U19-047 |
| VDR-U19-C098 | FUNCTION MAPPING REQUIRED | website/models/ir_http.py:198 | ['track'] | FACT | always | — | A visit is recorded in _register_website_track only when the rendered template/view has track=True and the response is 200, the client is not a bot, header X-Disable-Tracking is not 1 and the cursor is not readonly. | N-U19-047 |
| VDR-U19-C099 | FUNCTION MAPPING REQUIRED | website/models/ir_http.py:183 | def _register_website_track | INFERENCE | always | — | No call to _is_allowed_cookie or _allConsentsGranted appears in _register_website_track or in the visitor upsert code read (website_visitor.py:194-300); visitor rows are created irrespective of the cookie consent state. | N-U19-054 |
| VDR-U19-C100 | FUNCTION MAPPING REQUIRED | website/models/website_visitor.py:232 | ON CONFLICT (access_token) | FACT | always | — | Visitors are upserted by raw SQL on access_token, incrementing visit_count when the last connection was more than 8 hours ago, and optionally inserting a website_track row in the same query. | N-U19-047 |
| VDR-U19-C101 | FUNCTION MAPPING REQUIRED | website/models/res_users.py:90 | visitor_pre_authenticate_sudo._merge_visitor(visitor_current_user_sudo) | FACT | always | — | On authentication the anonymous visitor is merged into the contact's visitor (tracks reassigned, anonymous deleted), or the anonymous visitor token is replaced by the partner id. | N-U19-048 |
| VDR-U19-C102 | FUNCTION MAPPING REQUIRED | website/models/website_visitor.py:358 | delay_days = int( | FACT | cron active | — | Inactive visitors (no partner, last connection older than ICP website.visitor.live.days, default 60) are deleted by _cron_unlink_old_visitors in batches of 1000. | N-U19-049 |
| VDR-U19-C103 | FUNCTION MAPPING REQUIRED | website_crm/models/website_visitor.py:46 | Visitors tied to leads are considered | FACT | website_crm installed | — | With website_crm, visitors linked to leads are excluded from the inactive-visitor purge. | N-U19-049 |
| VDR-U19-C104 | FUNCTION MAPPING REQUIRED | website_crm_iap_reveal/models/ir_http.py:35 | request.env['crm.reveal.view'].sudo()._create_reveal_view | FACT | website_crm_iap_reveal installed; public user; GeoIP country; no existing lead | — | Each 200 public page served by _serve_page can insert crm.reveal.view rows (visitor IP, rule) for matching crm.reveal.rule URL/country rules, without a consent check. | N-U19-055 |
| VDR-U19-C105 | FUNCTION MAPPING REQUIRED | website_crm_iap_reveal/models/ir_http.py:41 | cookie_type='optional' | FACT | website_crm_iap_reveal installed | — | The rule_ids cookie that suppresses repeat matching is set with cookie_type='optional' (honouring the consent gate for the cookie only, not for row creation). | N-U19-055 |
| VDR-U19-C106 | FUNCTION MAPPING REQUIRED | website_crm_iap_reveal/models/crm_reveal_rule.py:354 | iap_tools.iap_jsonrpc(endpoint, params=params, timeout=timeout) | FACT | website_crm_iap_reveal installed | RT | The daily cron sends reveal payloads (visitor IPs grouped by rules) with the IAP account token to the reveal endpoint /iap/clearbit/1/reveal and creates leads from the response; network behaviour is RT. | N-U19-055 |
| VDR-U19-C107 | FUNCTION MAPPING REQUIRED | website_crm_iap_reveal/data/ir_cron_data.xml:9 | model._process_lead_generation() | FACT | website_crm_iap_reveal installed | — | ir.cron 'Lead Generation: Leads/Opportunities Generation' runs _process_lead_generation daily as base.user_root. | N-U19-051 |
| VDR-U19-C108 | FUNCTION MAPPING REQUIRED | website_links/models/link_tracker.py:23 | current_website.get_base_url() if current_website == self.env.company.website_id | FACT | website_links installed | — | link.tracker short URL host follows the current website when it is the company's website, else the company base URL. | N-U19-040 |
| VDR-U19-C109 | FUNCTION MAPPING REQUIRED | website/models/ir_model.py:32 | if 'website_id' in self and self.sudo().website_id.domain | FACT | always | — | get_base_url on any record prefers the record's website domain, then the company website domain, then the global base URL. | N-U19-040 |
| VDR-U19-C110 | FUNCTION MAPPING REQUIRED | website_partner/controllers/main.py:17 | partner_sudo.website_published or is_website_restricted_editor | FACT | website_partner installed | — | The partner page controller serves any published partner via sudo and does not call can_access_from_current_website, so a partner's website_id is not enforced on this route. | N-U19-057 |
| VDR-U19-C111 | FUNCTION MAPPING REQUIRED | website_event_booth/controllers/event_booth.py:95 | request.env['event.booth'].sudo().search([ | FACT | website_event_booth installed | — | get_booth_category_available_booths searches booths with sudo by event id and category id without a website or publication check. | N-U19-057 |
| VDR-U19-C112 | FUNCTION MAPPING REQUIRED | website/security/ir.model.access.csv:30 | access_website_visitor_designer | FACT | always | — | website.visitor ACL: designer and system groups can read/write/delete; the tracking itself runs with sudo. | N-U19-052 |
| VDR-U19-C113 | FUNCTION MAPPING REQUIRED | website_livechat/models/website_visitor.py:109 | def _upsert_visitor | FACT | website_livechat installed | — | On a newly inserted visitor, website_livechat links the guest's existing live chat channels to the visitor and copies the visitor country. | N-U19-052 |
| VDR-U19-C114 | FUNCTION MAPPING REQUIRED | website_blog/security/website_blog_security.xml:5 | Blog Post: public: published only | FACT | website_blog installed | — | ir.rule limits public/portal blog.post reads to website_published = True; blog.blog to active = True. | N-U19-061 |
| VDR-U19-C115 | FUNCTION MAPPING REQUIRED | website_blog/security/ir.model.access.csv:9 | blog_post,blog.post,model_blog_post,website.group_website_designer | FACT | always | — | blog.post ACL: public/portal/employee read only; website designer full CRUD. | N-U19-061 |
| VDR-U19-C116 | FUNCTION MAPPING REQUIRED | website_blog/controllers/main.py:260 | blog_post_domain += [('post_date', '<=', fields.Datetime.now())] | FACT | user not designer | — | The post page controller redirects to the blog index when the post is not among posts whose post_date is not in the future, so scheduled posts are hidden by the controller (the ir.rule itself only checks website_published). | N-U19-061 |
| VDR-U19-C117 | FUNCTION MAPPING REQUIRED | website_blog/models/website_blog.py:241 | def _check_for_publication | FACT | always | — | Publishing an active post posts a message with subtype mt_blog_blog_published on its blog (followers are notified). | N-U19-062 |
| VDR-U19-C118 | FUNCTION MAPPING REQUIRED | website_blog/models/website_blog.py:264 | vals['is_published'] = False | FACT | write active=False | — | Archiving a post unpublishes it. | N-U19-062 |
| VDR-U19-C119 | FUNCTION MAPPING REQUIRED | website_blog/models/website_blog.py:270 | published_date'] = vals[list(published_in_vals)[0]] | FACT | write is_published | — | Changing the published flag sets published_date to now (or clears it) unless a date is given. | N-U19-067 |
| VDR-U19-C120 | FUNCTION MAPPING REQUIRED | website_blog/models/website_blog.py:189 | content = fields.Html('Content', default=_default_content, translate=html_translate, sanitize=False) | FACT | always | — | Blog post content is not HTML-sanitised. | N-U19-074 |
| VDR-U19-C121 | FUNCTION MAPPING REQUIRED | website_blog/models/website_blog.py:168 | _mail_post_access = 'read' | FACT | always | — | Posting a message on a blog post requires only read access. | N-U19-063 |
| VDR-U19-C122 | FUNCTION MAPPING REQUIRED | website_blog/models/website_blog.py:193 | website_message_ids = fields.One2many(domain= | FACT | always | — | Public comments are non-internal comment messages with a non-internal subtype. | N-U19-063 |
| VDR-U19-C123 | FUNCTION MAPPING REQUIRED | website_mail/controllers/main.py:19 | record.check_access('read') | FACT | website_mail installed | — | /website_mail/follow is public; it requires read access on the posted model/id for the current user. | N-U19-064 |
| VDR-U19-C124 | FUNCTION MAPPING REQUIRED | website_mail/controllers/main.py:27 | _verify_request_recaptcha_token('website_mail_follow') | FACT | public user | — | For public users, a failing captcha only sets no_create=True for the partner lookup by email; the follow still proceeds with an existing partner. | N-U19-064 |
| VDR-U19-C125 | FUNCTION MAPPING REQUIRED | website_mail/controllers/main.py:35 | record.sudo().message_unsubscribe(partner_ids) | FACT | public user | — | Unfollow and follow use sudo and the partner found by the posted email; no token or ownership proof is required. | N-U19-071 |
| VDR-U19-C126 | FUNCTION MAPPING REQUIRED | website_mail/controllers/main.py:39 | request.session['partner_id'] = partner_ids[0] | FACT | follow | — | A successful follow stores the partner id in the session; is_follower then returns that partner's email to the same session. | N-U19-064 |
| VDR-U19-C127 | FUNCTION MAPPING REQUIRED | website_partner/controllers/main.py:15 | partner_sudo = request.env['res.partner'].sudo().browse(partner_id) | FACT | website_partner installed | — | Public partner page /partners/<slug> renders the sudo partner when published or when the viewer is a restricted editor. | N-U19-065 |
| VDR-U19-C128 | FUNCTION MAPPING REQUIRED | website_partner/views/website_partner_templates.xml:33 | "fields": ["address", "website", "phone", "email"] | FACT | website_partner installed | — | The partner detail block displays address, website, phone and email of the published partner. | N-U19-065 |
| VDR-U19-C129 | FUNCTION MAPPING REQUIRED | website_crm_partner_assign/controllers/main.py:335 | partner_obj.sudo().search( | FACT | website_crm_partner_assign installed | — | The /partners listing reads published company partners with a grade (grade must be published for non-editors) using sudo, filters by country/grade/industry/search text. | N-U19-065 |
| VDR-U19-C130 | FUNCTION MAPPING REQUIRED | website_google_map/controllers/main.py:43 | limit = post.get('limit') and int(post['limit']) or | FACT | website_google_map installed | — | /google_map is public, reads published company partners with sudo and takes the result limit from the request without an upper bound. | N-U19-072 |
| VDR-U19-C131 | FUNCTION MAPPING REQUIRED | website_crm_partner_assign/models/crm_lead.py:41 | Only users with commercial partner which | FACT | portal user | — | _assert_portal_write_access requires that all leads are within partner_assigned_id child_of the user's commercial partner (skipped for non-portal users and sudo). | N-U19-066 |
| VDR-U19-C132 | FUNCTION MAPPING REQUIRED | website_crm_partner_assign/models/crm_lead.py:225 | lead.sudo().convert_opportunity(lead.partner_id) | FACT | assigned partner accepts | — | partner_interested posts a message and converts the lead to an opportunity with sudo after the ownership assertion. | N-U19-066 |
| VDR-U19-C133 | FUNCTION MAPPING REQUIRED | website_crm_partner_assign/models/crm_lead.py:248 | values['partner_declined_ids'] = [(4, p, 0) for | FACT | partner declines | — | partner_desinterested unassigns the lead, records the declining partners, unsubscribes them, and can tag the lead as spam. | N-U19-067 |
| VDR-U19-C134 | FUNCTION MAPPING REQUIRED | website_crm_partner_assign/models/crm_lead.py:296 | self.sudo().write({'stage_id': stage_id}) | FACT | portal assigned partner | — | update_stage_from_portal writes the posted stage_id with sudo after the ownership assertion, without validating the stage against the lead's team. | N-U19-073 |
| VDR-U19-C135 | FUNCTION MAPPING REQUIRED | website_crm_partner_assign/models/crm_lead.py:302 | raise AccessDenied() | FACT | portal | — | create_opp_portal (sudo) requires the user's partner or commercial partner to have a grade. | N-U19-070 |
| VDR-U19-C136 | FUNCTION MAPPING REQUIRED | website_crm_partner_assign/security/ir_rule.xml:6 | Portal Graded Partner: read and write | FACT | website_crm_partner_assign installed | — | The rule named 'read and write assigned leads' grants only read (perm_write False) on leads whose partner_assigned_id is child_of the commercial partner; writes go through sudo model methods. | N-U19-066 |
| VDR-U19-C137 | FUNCTION MAPPING REQUIRED | website_customer/controllers/main.py:170 | partner = request.env['res.partner'].sudo().browse(partner_id) | FACT | website_customer installed | — | /customers/<slug> serves a published partner with sudo. | N-U19-065 |
| VDR-U19-C138 | FUNCTION MAPPING REQUIRED | website_forum/security/ir_rule_data.xml:4 | Website forum: Public user can only | FACT | website_forum installed | — | Public users see only forums with privacy = public; signed-in users see public and connected forums and private forums whose authorized_group_id they belong to; erp managers see all. | N-U19-078 |
| VDR-U19-C139 | FUNCTION MAPPING REQUIRED | website_forum/security/ir_rule_data.xml:38 | Website forum post: Public user can | FACT | website_forum installed | — | Post and tag rules mirror forum privacy for public vs portal/internal users. | N-U19-078 |
| VDR-U19-C140 | FUNCTION MAPPING REQUIRED | website_forum/security/ir.model.access.csv:7 | access_forum_post_portal | FACT | website_forum installed | — | Portal users have full read/write/create/unlink ACL on forum.post (vote ACL read/write/create); no ACL-level ownership restriction exists. | N-U19-088 |
| VDR-U19-C141 | FUNCTION MAPPING REQUIRED | website_forum/security/ir.model.access.csv:14 | access_forum_tag_public | FACT | website_forum installed | — | forum.tag ACL grants public and portal read and create (no write/unlink). | N-U19-088 |
| VDR-U19-C142 | FUNCTION MAPPING REQUIRED | website_forum/models/forum_forum.py:107 | karma_ask = fields.Integer(string='Ask questions', default=3) | FACT | always | — | Default thresholds include ask 3, answer 3, edit own 1, edit all 300, retag 75, close own 100 / all 500, delete own 500 / all 1000, flag 500, moderate 1000, post without validation 100. | N-U19-079 |
| VDR-U19-C143 | FUNCTION MAPPING REQUIRED | website_forum/models/forum_forum.py:132 | karma_post = fields.Integer(string='Ask questions without validation', | FACT | always | — | Questions by authors below karma_post are created pending validation. | N-U19-080 |
| VDR-U19-C144 | FUNCTION MAPPING REQUIRED | website_forum/models/forum_post.py:257 | post.can_edit = is_admin or user.karma >= | FACT | always | — | Post rights are computed per user karma against forum thresholds; is_admin (env.is_admin) bypasses all. | N-U19-079 |
| VDR-U19-C145 | FUNCTION MAPPING REQUIRED | website_forum/models/forum_post.py:327 | karma required to create a new | FACT | always | — | create raises AccessError when a new question is created without can_ask, or an answer without can_answer; answers to closed or deleted questions raise UserError. | N-U19-087 |
| VDR-U19-C146 | FUNCTION MAPPING REQUIRED | website_forum/models/forum_post.py:331 | post.sudo().state = 'pending' | FACT | author karma below karma_post | — | Questions from users who cannot post directly are set pending. | N-U19-080 |
| VDR-U19-C147 | FUNCTION MAPPING REQUIRED | website_forum/models/forum_post.py:348 | trusted_keys = ['active', 'is_correct', 'tag_ids'] | FACT | always | — | write checks karma for state, active, is_correct, retag and any non-trusted key; closed/flag/unlink/accept each need their own threshold. | N-U19-084 |
| VDR-U19-C148 | FUNCTION MAPPING REQUIRED | website_forum/models/forum_post.py:753 | user comments have a restriction on | FACT | always | — | Comments (message_post type comment) require can_comment and are posted with sudo so users can notify followers they cannot read. | N-U19-079 |
| VDR-U19-C149 | FUNCTION MAPPING REQUIRED | website_forum/models/forum_post.py:427 | if content and self.env.user.karma < forum.karma_dofollow | FACT | always | — | Content from authors below karma_dofollow gets links marked nofollow; below karma_editor images and links are refused (AccessError). | N-U19-081 |
| VDR-U19-C150 | FUNCTION MAPPING REQUIRED | website_forum/controllers/website_forum.py:403 | @http.route(['/forum/<model("forum.forum"):forum>/ask'], type='http', auth="user" | FACT | always | — | Asking, replying, commenting, voting, flagging, closing and deleting routes are auth=user; reading forum, question and tags routes are public. | N-U19-087 |
| VDR-U19-C151 | FUNCTION MAPPING REQUIRED | website_forum/controllers/website_forum.py:406 | if not user.email or not tools.single_email_re.match(user.email) | FACT | always | — | The ask route redirects users without a valid email to their profile. | N-U19-087 |
| VDR-U19-C152 | FUNCTION MAPPING REQUIRED | website_forum/controllers/website_forum.py:658 | partner.user_ids[0].id | FACT | always | — | Public /forum/<f>/partner/<id> searches res.partner with sudo and redirects to the forum page of the first linked user, or to the forum home when none. | N-U19-089 |
| VDR-U19-C153 | FUNCTION MAPPING REQUIRED | website_profile/controllers/main.py:48 | User can access - no matter | FACT | always | — | A profile is visible to others only if user.website_published and the viewer's karma >= website.karma_profile_min; own profile always. | N-U19-082 |
| VDR-U19-C154 | FUNCTION MAPPING REQUIRED | website_profile/models/website.py:10 | karma_profile_min = fields.Integer | FACT | always | — | karma_profile_min defaults to 150. | N-U19-082 |
| VDR-U19-C155 | FUNCTION MAPPING REQUIRED | website_profile/controllers/main.py:38 | return user.website_published and user.karma > 0 | FACT | always | — | Avatar images for public visitors are served with sudo only for published users with positive karma. | N-U19-083 |
| VDR-U19-C156 | FUNCTION MAPPING REQUIRED | website_profile/controllers/main.py:153 | whitelisted_values = {key: values[key] for key | FACT | user logged in | — | Profile save only writes fields in the user's self-writable set; an admin may edit another user via user_id. | N-U19-087 |
| VDR-U19-C157 | FUNCTION MAPPING REQUIRED | website_profile/controllers/main.py:328 | request.env['res.users'].sudo().browse(int(user_id))._process_profile_validation_token | FACT | always | — | /profile/validate_email is public and validates a token with sudo; redirect_url is passed to request.redirect (local redirect). | N-U19-087 |
| VDR-U19-C158 | FUNCTION MAPPING REQUIRED | website_forum/data/ir_config_parameter_data.xml:3 | 'b2c' | OBSERVATION | DB reconciled | — | DB: 1 forum (public, questions mode), ICP auth_signup.invitation_scope = b2c, every website auth_signup_uninvited = b2b; res.groups seeded by website_forum: 0; ACL 15 and rules 12 in DB equal the CSV/XML counts. | N-U19-090 |
| VDR-U19-C159 | FUNCTION MAPPING REQUIRED | website_slides/security/website_slides_security.xml:33 | Channel: public: restricted to public/link-based and | FACT | website_slides installed | — | Public users read slide.channel only if published and visibility in (public, link); portal/internal also see connected, and members/invited channels; officers read all and write their own; managers all. | N-U19-094 |
| VDR-U19-C160 | FUNCTION MAPPING REQUIRED | website_slides/security/website_slides_security.xml:114 | Slide: public: restricted to published or | FACT | website_slides installed | — | Public users read slide.slide only when slide and channel are published, channel visibility is public/link and the slide is a category or preview. | N-U19-094 |
| VDR-U19-C161 | FUNCTION MAPPING REQUIRED | website_slides/models/slide_channel.py:140 | ('link', 'Anyone with the link'), | FACT | always | — | visibility selection: public, connected, members, link. | N-U19-094 |
| VDR-U19-C162 | FUNCTION MAPPING REQUIRED | website_slides/models/slide_channel.py:204 | CHECK(visibility != 'members' OR enroll = | FACT | always | — | A SQL constraint forces enroll = invite when visibility is members. | N-U19-095 |
| VDR-U19-C163 | FUNCTION MAPPING REQUIRED | website_slides/models/slide_channel.py:761 | allowed = self.filtered(lambda channel: channel.enroll == | FACT | always | — | _filter_add_members allows self-enrolment only on open courses; controlled courses require write access (raise_on_access). | N-U19-095 |
| VDR-U19-C164 | FUNCTION MAPPING REQUIRED | website_slides/controllers/main.py:884 | success = channel.sudo()._action_add_members(request.env.user.partner_id) | FACT | invited member joins | — | A user with an invited membership on an invite-only course joins via sudo; other users go through the access-checked path. | N-U19-095 |
| VDR-U19-C165 | FUNCTION MAPPING REQUIRED | website_slides/controllers/main.py:735 | relativedelta(months=3) < fields.Datetime.now() | FACT | member_status invited | — | A pending invitation is valid for 3 months from last_invitation_date; enrolled members' invitation hashes have no expiry check. | N-U19-096 |
| VDR-U19-C166 | FUNCTION MAPPING REQUIRED | website_slides/controllers/main.py:730 | if not consteq(channel_partner_sudo._get_invitation_hash(), invite_hash) | FACT | always | — | Invitation links carry partner id and an HMAC hash compared with consteq; the channel must be published. | N-U19-096 |
| VDR-U19-C167 | FUNCTION MAPPING REQUIRED | website_slides/models/slide_channel_partner.py:159 | 'website_slides-channel-invite' | FACT | always | — | The hash is HMAC over (partner id, channel id) with a fixed purpose string. | N-U19-096 |
| VDR-U19-C168 | FUNCTION MAPPING REQUIRED | website_slides/controllers/main.py:849 | invite_partner.signup_prepare() | FACT | invited partner has no user | — | For an enrolled invitee without a user, a public visitor holding the valid link is redirected to a signup URL generated for that partner. | N-U19-105 |
| VDR-U19-C169 | FUNCTION MAPPING REQUIRED | website_slides/models/slide_channel.py:403 | Publishing is restricted to the responsible | FACT | always | — | can_publish for a channel is true for the responsible user or for managers when the user can upload; the same message is used for slides. | N-U19-097 |
| VDR-U19-C170 | FUNCTION MAPPING REQUIRED | website_slides/controllers/main.py:1281 | user_answers.mapped('question_id') != all_questions | FACT | always | — | slide_quiz_submit requires a non-public user, answers covering exactly the slide's questions, completes the slide when no answer is incorrect and returns karma and rank progress. | N-U19-098 |
| VDR-U19-C171 | FUNCTION MAPPING REQUIRED | website_slides/controllers/main.py:1284 | user_bad_answers = user_answers.filtered(lambda answer: not answer.is_correct) | INFERENCE | always | — | Answers are looked up by posted ids with sudo and only checked for covering each question and for correctness; picking one correct answer per question is sufficient to complete, so multiple selections of one question are not rejected. | N-U19-106 |
| VDR-U19-C172 | FUNCTION MAPPING REQUIRED | website_slides/controllers/main.py:1545 | slide.sudo()._embed_increment(referer_url) | FACT | external embed route | — | slides_embed_external increments the embed counter with sudo before the read-access check, for any existing active slide id. | N-U19-104 |
| VDR-U19-C173 | FUNCTION MAPPING REQUIRED | website_slides/controllers/main.py:1547 | if not slide.has_access('read'): | FACT | always | — | Embedded views then render a forbidden template when the visitor cannot read the slide. | N-U19-099 |
| VDR-U19-C174 | FUNCTION MAPPING REQUIRED | website_slides/security/website_slides_security.xml:241 | Resource: read restricted to channel members | FACT | website_slides installed | — | Downloadable resources are readable only by channel members for portal/internal users; officers read all. | N-U19-103 |
| VDR-U19-C175 | FUNCTION MAPPING REQUIRED | website_slides/controllers/main.py:534 | handle_params_access_error=handle_wslide_error | FACT | always | — | Slide routes declare handle_params_access_error=handle_wslide_error, which turns an AccessError into a 302 redirect to /slides?invite_error=no_rights instead of a bare 403. | N-U19-094 |
| VDR-U19-C176 | FUNCTION MAPPING REQUIRED | im_livechat/controllers/main.py:82 | @http.route('/im_livechat/get_session', methods=["POST"], type="jsonrpc", auth='public') | FACT | always | — | get_session is public; it creates a discuss.channel with sudo for the chosen livechat channel, creating a mail.guest for public users. | N-U19-110 |
| VDR-U19-C177 | FUNCTION MAPPING REQUIRED | im_livechat/controllers/main.py:145 | guest = guest.sudo()._get_or_create_guest( | FACT | public user | — | Public visitors get a guest created or reused (name Visitor or Visitor #id with website_livechat), with country and timezone from the request. | N-U19-110 |
| VDR-U19-C178 | FUNCTION MAPPING REQUIRED | im_livechat/controllers/main.py:120 | channel_id = -1 | FACT | always | — | A non-persisted mode returns a temporary channel id -1 without creating a record (bot welcome steps), otherwise the conversation is stored. | N-U19-110 |
| VDR-U19-C179 | FUNCTION MAPPING REQUIRED | im_livechat/models/im_livechat_channel.py:372 | chatbot_script_id in self.rule_ids.chatbot_script_id.ids | FACT | always | — | A requested chatbot script is used only if it appears in the channel's rules; otherwise an agent is selected. | N-U19-111 |
| VDR-U19-C180 | FUNCTION MAPPING REQUIRED | im_livechat/models/im_livechat_channel.py:433 | def _get_operator( | FACT | always | — | Agent selection considers availability, same language, country and expertise (helpers same_language, same_country, all/one_expertise) and picks the least active operator. | N-U19-111 |
| VDR-U19-C181 | FUNCTION MAPPING REQUIRED | im_livechat/models/im_livechat_channel.py:84 | Concurrent session number should be greater | FACT | always | — | Channel capacity is max_sessions per agent when max_sessions_mode is limited; the constraint requires a positive value. | N-U19-117 |
| VDR-U19-C182 | FUNCTION MAPPING REQUIRED | im_livechat/models/im_livechat_channel.py:635 | def match_rule(self, channel_id, url, country_id=False) | FACT | always | — | Rules are matched by regex on the page URL and optionally the country, country rules first; a bot rule is skipped when the script is inactive/empty or the operator-availability condition fails. | N-U19-112 |
| VDR-U19-C183 | FUNCTION MAPPING REQUIRED | im_livechat/controllers/webclient.py:68 | match_rule(params, url, country_id) | FACT | always | — | match_rule is called only from the web client session initialisation (button display), not from get_session. | N-U19-122 |
| VDR-U19-C184 | FUNCTION MAPPING REQUIRED | im_livechat/controllers/chatbot.py:39 | @http.route("/chatbot/step/trigger", type="jsonrpc", auth="public") | FACT | always | — | Chatbot restart, answer save, step trigger and email validation are public routes protected by discuss.channel access (guest context) and write the chatbot state with sudo. | N-U19-113 |
| VDR-U19-C185 | FUNCTION MAPPING REQUIRED | im_livechat/models/chatbot_script_step.py:184 | partner = self.env['res.partner'].create({ | FACT | public user and create_partner | — | _chatbot_prepare_customer_values creates a res.partner from the typed email/phone for public users (otherwise updates the user's partner when email/phone empty). | N-U19-121 |
| VDR-U19-C186 | FUNCTION MAPPING REQUIRED | im_livechat/models/chatbot_script_step.py:322 | if self.step_type == 'question_email' and not | FACT | always | — | An email step rejects an invalid email with a ValidationError and does not advance. | N-U19-119 |
| VDR-U19-C187 | FUNCTION MAPPING REQUIRED | im_livechat/controllers/main.py:211 | limit the creation : only ONE | FACT | always | — | feedback creates one rating per channel (sudo) and later calls rewrite it; it posts a feedback message with the rating image. | N-U19-114 |
| VDR-U19-C188 | FUNCTION MAPPING REQUIRED | im_livechat/controllers/main.py:250 | if not request.env.user._is_internal(): | FACT | always | — | email_livechat_transcript is auth=user and refuses non-internal users; download_livechat_transcript is public but looks up the channel under the user's own access rules. | N-U19-119 |
| VDR-U19-C189 | FUNCTION MAPPING REQUIRED | im_livechat/security/im_livechat_channel_security.xml:28 | discuss.channel: livechat users can read all | FACT | im_livechat installed | — | Livechat users can read all livechat discuss channels and members (rule with read-only perms); managers inherit and also configure bots and channels. | N-U19-115 |
| VDR-U19-C190 | FUNCTION MAPPING REQUIRED | im_livechat/security/ir.model.access.csv:11 | access_chatbot_script_user | FACT | im_livechat installed | — | chatbot.script, steps, answers and messages ACL: only im_livechat_group_manager. | N-U19-115 |
| VDR-U19-C191 | FUNCTION MAPPING REQUIRED | website_livechat/models/im_livechat_channel.py:19 | visitor_sudo = self.env['website.visitor']._get_visitor_from_request() | FACT | website_livechat installed | — | Sessions started on the website are linked to the visitor and cancel any pending operator-initiated chat request for that visitor. | N-U19-116 |
| VDR-U19-C192 | FUNCTION MAPPING REQUIRED | website_livechat/models/website_visitor.py:73 | is_pending_chat_request | FACT | operator sends chat request | — | An operator can create a chat request channel for a visitor (adds operator to the livechat channel users); a guest is created if the visitor has no partner. | N-U19-116 |
| VDR-U19-C193 | FUNCTION MAPPING REQUIRED | website_crm_livechat/models/chatbot_script_step.py:15 | values['visitor_ids'] = [(4, discuss_channel.livechat_visitor_id.id)] | FACT | website_crm_livechat installed | — | A lead created by a chatbot step or the lead command is linked to the livechat visitor. | N-U19-118 |
| VDR-U19-C194 | FUNCTION MAPPING REQUIRED | website_crm_livechat/models/discuss_channel.py:17 | visitor_sudo.write({'lead_ids': [(4, lead.id)]}) | FACT | website_crm_livechat installed | — | Converting a visitor via the lead command links the lead to the visitor and fills the country. | N-U19-118 |
| VDR-U19-C195 | FUNCTION MAPPING REQUIRED | website_hr_recruitment_livechat/__manifest__.py:4 | Chatbot for the HR Recruitment | FACT | module installed | — | website_hr_recruitment_livechat is data and demo only (no Python models). | N-U19-118 |
| VDR-U19-C196 | FUNCTION MAPPING REQUIRED | website_event/security/event_security.xml:5 | Event: public/portal: published read | FACT | website_event installed | — | Public/portal read events, tickets, slots, tags, questions and answers only for published events. | N-U19-126 |
| VDR-U19-C197 | FUNCTION MAPPING REQUIRED | website_event/models/event_registration.py:12 | return {'name', 'phone', 'email', 'company_name', 'event_id', | FACT | website_event installed | — | The website registration allowed fields include partner_id and event_ticket_id/event_slot_id. | N-U19-129 |
| VDR-U19-C198 | FUNCTION MAPPING REQUIRED | website_event/controllers/main.py:435 | registration_values['event_id'] = event.id | FACT | always | — | event_id is overwritten by the route event; partner_id is honoured when supplied, else visitor partner or the signed-in partner. | N-U19-136 |
| VDR-U19-C199 | FUNCTION MAPPING REQUIRED | website_event/controllers/main.py:446 | return request.env['event.registration'].sudo().create(registrations_to_create) | FACT | always | — | Registrations are created with sudo, linked to the visitor (force_create) and to the visitor partner. | N-U19-128 |
| VDR-U19-C200 | FUNCTION MAPPING REQUIRED | website_event/controllers/main.py:442 | registration_values['visitor_id'] = visitor_sudo.id | FACT | always | — | Each registration records the website visitor profile. | N-U19-128 |
| VDR-U19-C201 | FUNCTION MAPPING REQUIRED | website_event/controllers/main.py:465 | event._verify_seats_availability(list({ | FACT | always | — | registration_confirm verifies seats per (slot, ticket) combination and redirects with an insufficient_seats error before creating. | N-U19-127 |
| VDR-U19-C202 | FUNCTION MAPPING REQUIRED | website_event/controllers/main.py:357 | This ticket is not available for | FACT | always | — | A ticket that is missing, not launched or expired raises UserError. | N-U19-127 |
| VDR-U19-C203 | FUNCTION MAPPING REQUIRED | website_event/controllers/main.py:455 | _verify_request_recaptcha_token('website_event_registration') | FACT | always | — | registration_confirm calls the captcha verifier explicitly and redirects with recaptcha_failed on UserError (no-op when no key). | N-U19-134 |
| VDR-U19-C204 | FUNCTION MAPPING REQUIRED | event/models/event_registration.py:98 | def _check_seats_availability | FACT | event seats limited | RT | A constrains method on active/state/event/slot/ticket re-checks seats at save time; behaviour under concurrent submission is RT. | N-U19-139 |
| VDR-U19-C205 | FUNCTION MAPPING REQUIRED | website_event/controllers/main.py:484 | ('visitor_id', '=', visitor.id), | FACT | always | — | The success page lists only registrations belonging to the current visitor and event. | N-U19-128 |
| VDR-U19-C206 | FUNCTION MAPPING REQUIRED | website_event_booth/controllers/event_booth.py:100 | if booth_ids != booths.ids or len(booths.booth_category_id) | FACT | always | — | Requested booths must be exactly the available booths of one category. | N-U19-130 |
| VDR-U19-C207 | FUNCTION MAPPING REQUIRED | website_event_booth/controllers/event_booth.py:117 | return 'existingPartnerError' | FACT | public user | — | A public booking whose normalised email matches an existing partner returns existingPartnerError, which reveals existence. | N-U19-137 |
| VDR-U19-C208 | FUNCTION MAPPING REQUIRED | website_event_booth/controllers/event_booth.py:89 | booths.action_confirm(booth_values) | FACT | always | — | Confirmation books the booths with sudo and the contact found/created by _partner_find_from_emails_single; no captcha is called in this route. | N-U19-130 |
| VDR-U19-C209 | FUNCTION MAPPING REQUIRED | website_event_booth/controllers/event_booth.py:51 | request.env['event.booth'].sudo().browse([int(booth_id) for booth_id in booth_ids.split(',')]) | FACT | always | — | The booth details form browses booth ids from the query string with sudo, without checking the event. | N-U19-138 |
| VDR-U19-C210 | FUNCTION MAPPING REQUIRED | website_event_crm/models/event_registration.py:33 | lead_values['visitor_ids'] = self.visitor_id | FACT | website_event_crm installed | — | Lead generation rules add the visitor, visitor language and registration answers to the lead. | N-U19-131 |
| VDR-U19-C211 | FUNCTION MAPPING REQUIRED | website_mass_mailing/controllers/main.py:36 | /website_mass_mailing/subscribe | FACT | website_mass_mailing installed | — | /website_mass_mailing/subscribe is a public JSON route taking list_id, value and subscription_type; it verifies a captcha (action website_mass_mailing_subscribe) and returns a toast on UserError. | N-U19-143 |
| VDR-U19-C212 | FUNCTION MAPPING REQUIRED | website_mass_mailing/controllers/main.py:72 | elif subscription.opt_out: | FACT | always | — | subscribe_to_newsletter runs with sudo: it creates the contact if absent, creates the subscription, and sets opt_out False for an existing opted-out subscription, with no confirmation email. | N-U19-143 |
| VDR-U19-C213 | FUNCTION MAPPING REQUIRED | website_mass_mailing/controllers/main.py:19 | (f'contact_id.{fname}', '=', value) | FACT | always | — | The list is searched by posted list_id only; no is_public check appears in this controller (the mailing.list model defines is_public used elsewhere in mass_mailing). | N-U19-144 |
| VDR-U19-C214 | FUNCTION MAPPING REQUIRED | website_mass_mailing/controllers/main.py:75 | request.session[f'mass_mailing_{fname}'] = value | FACT | always | — | The subscribed email/phone is stored in the session and later returned by is_subscriber. | N-U19-150 |
| VDR-U19-C215 | FUNCTION MAPPING REQUIRED | mass_mailing/models/mailing_list.py:40 | is_public = fields.Boolean( | FACT | mass_mailing installed | — | mailing.list has an is_public flag used by the unsubscribe and preferences pages. | N-U19-151 |
| VDR-U19-C216 | FUNCTION MAPPING REQUIRED | mass_mailing/controllers/main.py:48 | not consteq(mailing_sudo._generate_mailing_recipient_token | FACT | always | — | Unsubscribe pages require a hash token tied to (mailing, document, email); public users without a token get 400; logged-in non-mailing users without a mailing id use their own page. | N-U19-145 |
| VDR-U19-C217 | FUNCTION MAPPING REQUIRED | website_mass_mailing/data/ir_model_data.xml:20 | 'tag_ids', | FACT | website_mass_mailing installed | — | mailing.contact is form-enabled with name fields, email, list_ids, country and tag_ids. | N-U19-144 |
| VDR-U19-C218 | FUNCTION MAPPING REQUIRED | mail_group/controllers/portal.py:73 | token != group._generate_group_access_token() | FACT | always | — | /groups with group_id and token shows that group (sudo) when the HMAC group token matches, otherwise lists groups visible to the user's rules. | N-U19-146 |
| VDR-U19-C219 | FUNCTION MAPPING REQUIRED | mail_group/controllers/portal.py:89 | members_data = mail_groups._find_members(email_normalized, partner_id) | FACT | public user | — | For public users the posted email is used to flag is_member per listed group (a membership oracle); logged-in users are forced to their own email. | N-U19-156 |
| VDR-U19-C220 | FUNCTION MAPPING REQUIRED | mail_group/controllers/portal.py:273 | group_sudo._send_subscribe_confirmation_email(email) | FACT | public user | — | Public subscribe sends a confirmation email to the posted address; logged-in users are joined directly. | N-U19-146 |
| VDR-U19-C221 | FUNCTION MAPPING REQUIRED | mail_group/controllers/portal.py:329 | elif not token: | FACT | always | — | Without a token the caller must have read access on the group; with a valid group token the access rule is bypassed. | N-U19-146 |
| VDR-U19-C222 | FUNCTION MAPPING REQUIRED | mail_group/controllers/portal.py:385 | return group if token == excepted_token | FACT | always | — | subscribe/unsubscribe confirm routes compare the action token with == (not consteq) and then join or remove all members with that email. | N-U19-146 |
| VDR-U19-C223 | FUNCTION MAPPING REQUIRED | mail_group/controllers/portal.py:237 | group_sudo._leave_group(email) | FACT | always | — | One-click unsubscribe is a CSRF-exempt POST validated by an email-bound HMAC with consteq. | N-U19-145 |
| VDR-U19-C224 | FUNCTION MAPPING REQUIRED | mail_group/security/mail_group_security.xml:4 | Mail Group: Access only public and | FACT | mail_group installed | — | Group readers see public groups, groups for their authorised group, groups where they are members (members mode) or groups they moderate. | N-U19-147 |
| VDR-U19-C225 | FUNCTION MAPPING REQUIRED | mail_group/security/mail_group_security.xml:47 | Mail Group Message: Only accepted message | FACT | mail_group installed | — | Public/portal readers see only accepted messages of groups visible to them; moderators and managers see more. | N-U19-147 |
| VDR-U19-C226 | FUNCTION MAPPING REQUIRED | mail_group/controllers/portal.py:26 | return [('moderation_status', '!=', 'rejected')] | FACT | always | — | Rejected messages are never shown on the website, even to administrators. | N-U19-147 |
| VDR-U19-C227 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:258 | email_has_access = self.search_count([('id', '=', self.id), ('access_group_id.user_ids.email_normalized', | FACT | access_mode == groups | — | Incoming email posts are accepted by mode: public, members-only (sender must be member) or authorised group (sender email must belong to a group user); moderation then accepts, rejects or holds. | N-U19-146 |
| VDR-U19-C228 | FUNCTION MAPPING REQUIRED | rating/controllers/main.py:91 | rating_sudo = request.env['rating.rating'].sudo().search([('access_token', '=', token)]) | FACT | always | — | Rating pages look up the rating by access_token with sudo; no token expiry or consumed check is applied. | N-U19-148 |
| VDR-U19-C229 | FUNCTION MAPPING REQUIRED | rating/controllers/main.py:77 | record_sudo.rating_apply( | FACT | POST submit_feedback | — | submit_feedback POST applies the rating via rating_apply on the sudo record; a GET only renders the page; rating GET no longer applies the rating. | N-U19-148 |
| VDR-U19-C230 | FUNCTION MAPPING REQUIRED | rating/models/rating.py:20 | return uuid.uuid4().hex | FACT | always | — | Rating tokens are uuid4 hex strings. | N-U19-153 |
| VDR-U19-C231 | FUNCTION MAPPING REQUIRED | rating/models/mail_thread.py:129 | rating.write({'rating': rate, 'feedback': feedback, 'consumed': True}) | FACT | always | — | rating_apply overwrites rating and feedback and marks consumed True without refusing an already consumed rating; updates the existing message when present. | N-U19-158 |
| VDR-U19-C232 | FUNCTION MAPPING REQUIRED | rating/models/mail_thread.py:123 | raise ValueError(_('Wrong rating value. | FACT | always | — | rating_apply validates the value range 0-5; the public controller accepts only the three constants happy=5, neutral=3, unhappy=1 (rating_data.py:15-17). | N-U19-153 |
| VDR-U19-C233 | FUNCTION MAPPING REQUIRED | portal_rating/models/rating_rating.py:41 | Updating rating comment require write access | FACT | portal_rating installed | — | Publisher comments need membership of website.group_website_restricted_editor (if that group exists) or write access on the rated record; publisher and date are auto-filled. | N-U19-149 |
| VDR-U19-C234 | FUNCTION MAPPING REQUIRED | portal_rating/controllers/portal_rating.py:18 | rating.write({'publisher_comment': publisher_comment}) | FACT | portal_rating installed | — | /website/rating/comment is auth=user and writes the comment under the user's rights. | N-U19-149 |
| VDR-U19-C235 | FUNCTION MAPPING REQUIRED | rating/security/ir.model.access.csv:2 | access_rating_user | FACT | rating installed | — | rating.rating ACL: employees read/write/create (no delete); public and portal have a row with no permissions; no ir.rule exists. | N-U19-153 |
| VDR-U19-C236 | FUNCTION MAPPING REQUIRED | website_payment/models/payment_provider.py:39 | providers = providers.filtered( | FACT | website_payment installed | — | _get_compatible_providers keeps providers with no website or the requested website and reports the rest as incompatible_website. | N-U19-162 |
| VDR-U19-C237 | FUNCTION MAPPING REQUIRED | website_payment/controllers/payment.py:13 | website_id=request.website.id | FACT | website_payment installed | — | payment_pay and payment_method are overridden to pass the current website id to provider filtering. | N-U19-162 |
| VDR-U19-C238 | FUNCTION MAPPING REQUIRED | website_payment/controllers/portal.py:19 | @http.route('/donation/pay', type='http', methods=['GET', 'POST'], auth='public' | FACT | website_payment installed | — | /donation/pay is public; POST stores amount and options in the session and redirects (303) to the GET. | N-U19-163 |
| VDR-U19-C239 | FUNCTION MAPPING REQUIRED | website_payment/controllers/portal.py:50 | kwargs['access_token'] = payment_utils.generate_access_token( | FACT | public user | — | For public users the access token is generated server-side from (public partner id, amount, currency). | N-U19-172 |
| VDR-U19-C240 | FUNCTION MAPPING REQUIRED | website_payment/controllers/portal.py:56 | if float(amount) < float(minimum_amount): | FACT | always | — | The donation minimum comes from the route parameter minimum_amount (URL path), so a requester controls it. | N-U19-165 |
| VDR-U19-C241 | FUNCTION MAPPING REQUIRED | website_payment/controllers/portal.py:67 | partner_id = request.website.user_id.partner_id.id | FACT | public user | — | Anonymous donations use the website public user's partner and require name, email and country in partner_details; donor details are written to the transaction. | N-U19-163 |
| VDR-U19-C242 | FUNCTION MAPPING REQUIRED | website_payment/controllers/portal.py:100 | tx_sudo._send_donation_email(True, comment, recipient_email) | FACT | always | — | donation_transaction sends the internal notification at creation time with comment and donation_recipient_email taken from kwargs. | N-U19-173 |
| VDR-U19-C243 | FUNCTION MAPPING REQUIRED | website_payment/models/payment_transaction.py:57 | 'email_to': recipient_email if is_internal_notification else self.partner_email, | FACT | always | — | _send_donation_email creates a sudo mail.mail from the company email address to the given recipient (internal) or the donor (confirmation) and sends immediately. | N-U19-164 |
| VDR-U19-C244 | FUNCTION MAPPING REQUIRED | website_payment/models/payment_transaction.py:15 | for donation_tx in self.filtered(lambda tx: tx.state | FACT | always | — | The donor confirmation and the payment chatter log happen in _post_process only for done donation transactions. | N-U19-169 |
| VDR-U19-C245 | FUNCTION MAPPING REQUIRED | website_payment/models/payment_provider.py:57 | return iri_to_uri(request.httprequest.url_root) | FACT | request present | RT | payment.provider.get_base_url prefers the request url_root (host header derived) for callbacks. | N-U19-176 |
| VDR-U19-C246 | FUNCTION MAPPING REQUIRED | website_payment/controllers/portal.py:199 | with_user(website.user_id) | FACT | always | — | The supported-payment-methods snippet endpoint is public, readonly, reads providers sudo as the website user and caches responses for non-internal users for 7 days. | N-U19-162 |
| VDR-U19-C247 | FUNCTION MAPPING REQUIRED | html_editor/controllers/main.py:686 | @http.route('/html_editor/link_preview_external', type="jsonrpc", auth="public", methods=['POST']) | FACT | html_editor installed | — | link_preview_external is public and calls link_preview.get_link_preview_from_url(preview_url). | N-U19-166 |
| VDR-U19-C248 | FUNCTION MAPPING REQUIRED | mail/tools/link_preview.py:33 | requests.get(url, timeout=3, headers=headers, allow_redirects=True, stream=True) | FACT | always | RT | The helper performs requests.get with redirects on the supplied URL and shows no private-address or scheme filtering in this function; effectiveness of network egress controls is RT. | N-U19-175 |
| VDR-U19-C249 | FUNCTION MAPPING REQUIRED | web_unsplash/controllers/main.py:84 | not url.startswith(('https://images.unsplash.com/', 'https://plus.unsplash.com/')) | FACT | not in test | — | Unsplash image import is auth=user and accepts only Unsplash hosts (outside tests); requests.get has no timeout argument. | N-U19-167 |
| VDR-U19-C250 | FUNCTION MAPPING REQUIRED | web_unsplash/controllers/main.py:148 | def get_unsplash_app_id | FACT | always | — | get_app_id is public and returns ICP unsplash.app_id; save_unsplash needs manage-settings rights. | N-U19-167 |
| VDR-U19-C251 | FUNCTION MAPPING REQUIRED | html_editor/controllers/main.py:375 | @http.route(['/web_editor/attachment/add_data', '/html_editor/attachment/add_data'], type='jsonrpc', auth='user' | FACT | html_editor installed | — | Editor media upload and URL-add routes are auth=user; images are checked against supported mimetypes and processed. | N-U19-167 |
| VDR-U19-C252 | FUNCTION MAPPING REQUIRED | website_links/controller/main.py:9 | @http.route('/website_links/new', type='jsonrpc', auth='user', methods=['POST']) | FACT | website_links installed | — | Link shortener routes are auth=user and the module's ACL gives link.tracker CRUD to the designer group (base ACL gives employees read). | N-U19-168 |
| VDR-U19-C253 | FUNCTION MAPPING REQUIRED | link_tracker/controller/main.py:23 | return request.redirect(redirect_url, code=301, local=False) | FACT | link_tracker installed | — | /r/<code> is public, records a click for non-bots and issues a permanent redirect to the stored URL (local=False). | N-U19-177 |
| VDR-U19-C254 | FUNCTION MAPPING REQUIRED | website_links/controller/main.py:26 | new_code = request.env['link.tracker.code'].search_count( | INFERENCE | website_links installed | — | add_code assigns the integer result of search_count to new_code and then calls new_code.read() when it is positive, which cannot work for an int; the duplicate-code branch is a latent error. | N-U19-178 |
| VDR-U19-C255 | FUNCTION MAPPING REQUIRED | website/controllers/main.py:999 | '/website/google_maps_api_key' | FACT | always | — | The Google Maps API key configured on the website is returned to anyone by a public JSON route. | N-U19-160 |
| VDR-U19-C256 | FUNCTION MAPPING REQUIRED | website_payment/__manifest__.py:25 | 'auto_install': True | FACT | always | — | website_payment is an auto-install bridge between website, account_payment and portal; DB: payment providers 25 rows, one enabled custom provider and a demo provider in test state, no website-assigned provider. | N-U19-171 |
| VDR-U19-C257 | FUNCTION MAPPING REQUIRED | n/a | — | UNKNOWN | always | RT | UNKNOWN - EVIDENCE INSUFFICIENT: whether website_page response cache replays a password-unlocked page to other public visitors (needs runtime with two sessions). | N-U19-018 |
| VDR-U19-C258 | FUNCTION MAPPING REQUIRED | n/a | — | UNKNOWN | always | — | UNKNOWN - EVIDENCE INSUFFICIENT: whether the model page order parameter can sort by fields hidden from the public user (ORM order validation not read). | N-U19-018 |
| VDR-U19-C259 | FUNCTION MAPPING REQUIRED | n/a | — | UNKNOWN | always | RT | UNKNOWN - EVIDENCE INSUFFICIENT: reverse proxy rate limits, request body size limits and upload ceilings on /website/form (infrastructure). | N-U19-039 |
| VDR-U19-C260 | FUNCTION MAPPING REQUIRED | n/a | — | UNKNOWN | always | RT | UNKNOWN - EVIDENCE INSUFFICIENT: GeoIP database availability and accuracy used by visitor country, reveal rules and form phone formatting. | N-U19-058 |
| VDR-U19-C261 | FUNCTION MAPPING REQUIRED | n/a | — | UNKNOWN | always | — | UNKNOWN - EVIDENCE INSUFFICIENT: blog comment moderation and portal chatter token flow (portal module not studied here, owned by U03). | N-U19-075 |
| VDR-U19-C262 | FUNCTION MAPPING REQUIRED | n/a | — | UNKNOWN | always | — | UNKNOWN - EVIDENCE INSUFFICIENT: forum voting karma arithmetic, offensive-post handling and moderation queue routes were only listed. | N-U19-091 |
| VDR-U19-C263 | FUNCTION MAPPING REQUIRED | n/a | — | UNKNOWN | website_slides_survey installed | — | UNKNOWN - EVIDENCE INSUFFICIENT: website_slides_survey certification, retake and certificate download access were not read. | N-U19-107 |
| VDR-U19-C264 | FUNCTION MAPPING REQUIRED | n/a | — | UNKNOWN | always | RT | UNKNOWN - EVIDENCE INSUFFICIENT: guest cookie lifetime, bus presence and operator availability under concurrency (runtime). | N-U19-123 |
| VDR-U19-C265 | FUNCTION MAPPING REQUIRED | n/a | — | UNKNOWN | always | RT | UNKNOWN - EVIDENCE INSUFFICIENT: concurrent registration overbooking and iCal/Google calendar link generation (event module internals not studied). | N-U19-140 |
| VDR-U19-C266 | FUNCTION MAPPING REQUIRED | n/a | — | UNKNOWN | always | RT | UNKNOWN - EVIDENCE INSUFFICIENT: outgoing mail delivery, bounce handling and mail group posting by email aliases. | N-U19-159 |
| VDR-U19-C267 | FUNCTION MAPPING REQUIRED | n/a | — | UNKNOWN | always | RT | UNKNOWN - EVIDENCE INSUFFICIENT: egress filtering for link preview, real payment provider callbacks and Unsplash/IAP service behaviour. | N-U19-178 |
| VDR-U19-C268 | FUNCTION MAPPING REQUIRED | website/security/website_security.xml:10 | Restricted Editor | FACT | always | — | Two website roles exist: Restricted Editor (sequence 10) and Editor and Designer (sequence 20, implies restricted editor), granted by default to root and admin and implied by base.group_system. | N-U19-003 |
| VDR-U19-C269 | FUNCTION MAPPING REQUIRED | website/models/ir_ui_view.py:407 | It only check the visibility on | FACT | always | — | The _handle_visibility docstring states that only the main view's visibility is checked and other views called stay available over RPC. | N-U19-017 |
| VDR-U19-C270 | FUNCTION MAPPING REQUIRED | website/controllers/form.py:34 | is no real risk for | FACT | always | — | A source comment justifies skipping CSRF for unauthenticated sessions because embedded cross-site forms would otherwise break (SameSite). | N-U19-020 |
| VDR-U19-C271 | FUNCTION MAPPING REQUIRED | website/models/website_form.py:27 | website_form_access = fields.Boolean('Allowed to use in | FACT | always | — | ir.model carries website_form_access, website_form_default_field_id, website_form_label and website_form_key, which are the per-model form-builder configuration. | N-U19-031 |
| VDR-U19-C272 | FUNCTION MAPPING REQUIRED | website/models/website_visitor.py:67 | website_track_ids = fields.One2many('website.track' | FACT | always | — | website.visitor links to website.track (visited pages) and computes page statistics, country, language and timezone. | N-U19-041 |
| VDR-U19-C273 | FUNCTION MAPPING REQUIRED | website_crm/models/website_visitor.py:10 | lead_ids = fields.Many2many('crm.lead' | FACT | website_crm installed | — | With website_crm a visitor can be linked to leads (visible to salesmen) and the visitor email and phone are derived from them. | N-U19-042 |
| VDR-U19-C274 | FUNCTION MAPPING REQUIRED | website/models/website_visitor.py:315 | Merge an anonymous visitor data to | FACT | always | — | _merge_visitor reassigns tracks of the anonymous visitor to the partner visitor and unlinks it; website_crm and website_livechat extend it to carry leads and chat sessions. | N-U19-050 |
| VDR-U19-C275 | FUNCTION MAPPING REQUIRED | website/models/website.py:131 | cookies_bar = fields.Boolean('Cookies Bar' | OBSERVATION | DB reconciled | — | DB: all 29 websites have cookies_bar false (and block_third_party_domains true); consequently _is_allowed_cookie('optional') returns True on every website. | N-U19-056 |
| VDR-U19-C276 | FUNCTION MAPPING REQUIRED | website_blog/models/website_blog.py:162 | _name = 'blog.post' | FACT | website_blog installed | — | blog.post inherits mail.thread, website.seo.metadata, website.published.multi.mixin, cover and searchable mixins. | N-U19-059 |
| VDR-U19-C277 | FUNCTION MAPPING REQUIRED | website_blog/models/website_blog.py:245 | blog_post_template_new_post | FACT | website_blog installed | — | Publishing renders a template message to the blog so that followers learn of new content. | N-U19-060 |
| VDR-U19-C278 | FUNCTION MAPPING REQUIRED | website_blog/models/website_blog.py:204 | website_id = fields.Many2one(related='blog_id.website_id' | FACT | website_blog installed | — | A post's website is taken from its blog. | N-U19-068 |
| VDR-U19-C279 | FUNCTION MAPPING REQUIRED | website_blog/__manifest__.py:11 | 'depends': ['website_mail', 'website_partner', 'html_builder'] | FACT | always | — | website_blog depends on website_mail, website_partner and html_builder. | N-U19-069 |
| VDR-U19-C280 | FUNCTION MAPPING REQUIRED | website_forum/models/forum_forum.py:17 | _name = 'forum.forum' | FACT | website_forum installed | — | forum.forum carries privacy, mode, authorized group and all karma thresholds. | N-U19-076 |
| VDR-U19-C281 | FUNCTION MAPPING REQUIRED | website_forum/models/forum_forum.py:104 | karma_gen_answer_accepted | FACT | always | — | Karma awards (question new 2, upvote 5, answer upvote 10, accepted 15, flagged -100) make reputation the self-moderation currency. | N-U19-077 |
| VDR-U19-C282 | FUNCTION MAPPING REQUIRED | website_forum/models/forum_forum.py:59 | privacy = fields.Selection([ | FACT | always | — | Forum privacy is public, connected or private (authorized group); mode is questions or discussions. | N-U19-085 |
| VDR-U19-C283 | FUNCTION MAPPING REQUIRED | website_forum/__manifest__.py:18 | 'website_profile', | FACT | always | — | website_forum depends on auth_signup, website_mail and website_profile (which depends on gamification). | N-U19-086 |
| VDR-U19-C284 | FUNCTION MAPPING REQUIRED | website_slides/models/slide_channel.py:21 | _name = 'slide.channel' | FACT | website_slides installed | — | slide.channel is the course object with visibility, enrol policy, groups, karma settings and responsible user. | N-U19-092 |
| VDR-U19-C285 | FUNCTION MAPPING REQUIRED | website_slides/models/slide_channel_partner.py:171 | karma = channel.karma_gen_channel_finish | FACT | always | — | Completing a course awards the channel's finish karma, linking training to the reputation system. | N-U19-093 |
| VDR-U19-C286 | FUNCTION MAPPING REQUIRED | website_slides/models/slide_channel_partner.py:13 | member_status = fields.Selection([ | FACT | always | — | slide.channel.partner member_status distinguishes invited, joined, ongoing and completed attendees. | N-U19-100 |
| VDR-U19-C287 | FUNCTION MAPPING REQUIRED | website_slides/models/slide_channel.py:135 | enroll_group_ids = fields.Many2many('res.groups' | FACT | always | — | Auto-enrol groups, upload groups, enrol policy and visibility are per-course settings. | N-U19-101 |
| VDR-U19-C288 | FUNCTION MAPPING REQUIRED | website_slides/__manifest__.py:23 | 'portal_rating', | FACT | always | — | website_slides depends on portal_rating, website, website_mail and website_profile. | N-U19-102 |
| VDR-U19-C289 | FUNCTION MAPPING REQUIRED | im_livechat/models/im_livechat_channel.py:25 | _name = 'im_livechat.channel' | FACT | im_livechat installed | — | im_livechat.channel is the live chat channel with agents, rules and capacity. | N-U19-108 |
| VDR-U19-C290 | FUNCTION MAPPING REQUIRED | im_livechat/controllers/main.py:189 | def _post_feedback_message | FACT | always | — | Visitor feedback is posted as a conversation notification with the rating image, so every rating is traceable in the conversation log. | N-U19-109 |
| VDR-U19-C291 | FUNCTION MAPPING REQUIRED | im_livechat/controllers/main.py:160 | ).sudo().create(channel_vals) | INFERENCE | always | — | get_session (lines 82-187) creates a discuss.channel with sudo on every persisted call and no captcha, throttle or token check appears in that method. | N-U19-120 |
| VDR-U19-C292 | FUNCTION MAPPING REQUIRED | website_event/controllers/main.py:212 | <model("event.event"):event>/register | FACT | website_event installed | — | Visitors reach the registration form via public routes /register, /registration/new and /registration/confirm. | N-U19-124 |
| VDR-U19-C293 | FUNCTION MAPPING REQUIRED | website_event/controllers/main.py:330 | '/event/<model("event.event"):event>/registration/new' | FACT | website_event installed | — | Event registration needs no account (auth=public); the success page is bound to the visitor profile. | N-U19-125 |
| VDR-U19-C294 | FUNCTION MAPPING REQUIRED | website_event_booth/controllers/event_booth.py:97 | ('state', '=', 'available') | FACT | website_event_booth installed | — | Only booths in state available can be requested; confirmation books them. | N-U19-132 |
| VDR-U19-C295 | FUNCTION MAPPING REQUIRED | website_event/controllers/main.py:294 | if event.seats_limited: | FACT | always | — | Seat checks apply only when the event has limited seats; slot seats are used when a slot is chosen. | N-U19-133 |
| VDR-U19-C296 | FUNCTION MAPPING REQUIRED | website_event/controllers/main.py:470 | insufficient_seats | FACT | always | — | Capacity overflow redirects the visitor to the register page with error code insufficient_seats. | N-U19-135 |
| VDR-U19-C297 | FUNCTION MAPPING REQUIRED | website_mass_mailing/controllers/main.py:12 | /website_mass_mailing/is_subscriber | FACT | website_mass_mailing installed | — | A public route returns whether the session or user email is subscribed to a list, so the form can adapt. | N-U19-141 |
| VDR-U19-C298 | FUNCTION MAPPING REQUIRED | rating/controllers/main.py:52 | rating.rating_external_page_submit | FACT | rating installed | — | The rating email links open a public feedback page with happy/neutral/unhappy choices rendered in the contact language. | N-U19-142 |
| VDR-U19-C299 | FUNCTION MAPPING REQUIRED | website_mass_mailing/__manifest__.py:13 | 'depends': ['website', 'mass_mailing', 'google_recaptcha'] | FACT | always | — | website_mass_mailing depends on website, mass_mailing and google_recaptcha. | N-U19-152 |
| VDR-U19-C300 | FUNCTION MAPPING REQUIRED | website_mass_mailing/controllers/main.py:71 | ContactSubscription.create({'contact_id': contact_id.id, 'list_id': int(list_id)}) | INFERENCE | always | — | The subscribe path creates contact and subscription in one request; no verification email, double opt-in or ownership check appears in the method (lines 54-75). | N-U19-154 |
| VDR-U19-C301 | FUNCTION MAPPING REQUIRED | website_mass_mailing/controllers/main.py:47 | self.subscribe_to_newsletter(subscription_type, value, list_id, fname) | INFERENCE | always | — | list_id is cast with int() and used directly; subscribe() does not check mailing.list.is_public, so non-public lists can be targeted. | N-U19-155 |
| VDR-U19-C302 | FUNCTION MAPPING REQUIRED | mail_group/controllers/portal.py:307 | group_sudo._send_unsubscribe_confirmation_email(email) | INFERENCE | public user with a valid group token or readable group | — | An anonymous caller may trigger confirmation emails (subscribe or unsubscribe) to any address given in the email parameter; no captcha call appears in these routes. | N-U19-157 |
| VDR-U19-C303 | FUNCTION MAPPING REQUIRED | website_payment/__manifest__.py:9 | multi-website support for payment providers | FACT | always | — | website_payment is described as a bridge adding multi-website support for payment providers. | N-U19-161 |
| VDR-U19-C304 | FUNCTION MAPPING REQUIRED | website_payment/models/payment_provider.py:15 | website_id = fields.Many2one( | FACT | always | — | payment.provider.website_id (check_company, ondelete restrict) is the per-website assignment; copy handled to avoid company inconsistencies. | N-U19-170 |
| VDR-U19-C305 | FUNCTION MAPPING REQUIRED | website_payment/controllers/portal.py:55 | minimum_amount=0 | INFERENCE | always | — | minimum_amount is a URL path parameter of the public JSON route, set by the rendered form (transaction_route built from donation options) and re-supplied by the client, so the server does not independently know the configured minimum. | N-U19-174 |
