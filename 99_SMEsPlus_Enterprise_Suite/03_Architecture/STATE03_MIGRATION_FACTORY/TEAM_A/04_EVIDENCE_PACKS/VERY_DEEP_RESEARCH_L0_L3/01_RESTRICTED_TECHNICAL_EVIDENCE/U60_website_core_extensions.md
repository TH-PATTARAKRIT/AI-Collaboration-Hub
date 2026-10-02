# U60 — website core remaining and CRM/livechat/blog extensions (restricted technical evidence)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Unit: U60
- Modules: website (remaining delta), website_blog, website_crm, website_crm_iap_reveal, website_crm_livechat, website_crm_partner_assign, website_crm_sms, website_customer
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope notes: DELTA-FIRST for website (U19 breadth). Full study for bridge modules. Source evidence only; RT flags for runtime unknowns.

---

## CAP-U60-01 — Website view Copy-on-Write (COW) isolation

### D1 — COW on write
`ir.ui.view` inherits `website.seo.metadata` in addition to the base `ir.ui.view`. The `write()` method implements Copy-on-Write: when a `website_id` context key is present and `no_cow` is absent, editing a generic view causes a website-specific copy to be created for the current website rather than mutating the generic record. Sibling specific copies and inheriting children are also COW'd in cascade.

### D2 — COW on unlink
`unlink()` implements Copy-on-Unlink (COU): when a generic view is deleted while a `website_id` context is set, website-specific copies are created for all other websites so they retain the view.

### D3 — View deduplication
`filter_duplicate()` returns the most website-specific view per `key` in the current website context; in a non-website context it removes all website-bound views. This is used by `_view_get_inherited_children()` and `_get_inheriting_views()`.

### D4 — Template domain extension
`_get_template_domain()` restricts to views whose `website_id` is either NULL or matches the context website.

### D5 — Visibility enforcement
The `visibility` selection field on `ir.ui.view` governs four modes: Public, Signed In, Restricted Group, With Password. `_handle_visibility()` enforces these at render time, raising HTTP 403 for denied access. Password visibility stores a bcrypt hash in `visibility_password` and verifies it against session-stored IDs.

### D6 — Root attributes for sections
`_get_allowed_root_attrs()` extends the base list to include `data-bg-video-src`, `data-shape`, `data-scroll-background-ratio`, `data-visibility*` (with per-UTM and per-lang variants), enabling website-specific section behaviours.

### Ten-dimension table — CAP-U60-01

| Dimension | Finding |
|---|---|
| Existence | Confirmed: `website/models/ir_ui_view.py` |
| Boundaries | COW active only when `website_id` context present and `no_cow` absent |
| Data model | Adds `website_id`, `page_ids`, `visibility`, `visibility_password`, `track` to `ir.ui.view` |
| Access control | Visibility check in `_handle_visibility`; website designer bypasses visibility |
| Performance | `_get_cached_template_prefetched_keys` prefetches `active`, `visibility`, `track` to reduce N+1 |
| Error handling | `_fetch_template_views` annotates `MissingError` with website context for debugging |
| Translations | `_get_base_lang()` uses website `default_lang_id.code`; `_update_field_translations` forces `no_cow` |
| Multi-website | `_create_all_specific_views` uses raw SQL to propagate missing child views to existing COW trees |
| Lifecycle | `_set_noupdate` skipped in website context so generic views stay upgradeable |
| Integration | Inherits `website.seo.metadata`; interacts with `website.page`, `website.controller.page`, `website.menu` |

---

## CAP-U60-02 — Website visitor tracking

### D1 — Access token mechanism
Anonymous visitors receive a SHA-1 access token derived from `remote_addr + HTTP_USER_AGENT + session.sid` (truncated to 32 hex chars). Authenticated users use their `partner_id` integer as the token. Logic at `website/models/website_visitor.py:34-49`.

### D2 — UPSERT visitor
`_upsert_visitor()` performs a single raw-SQL `INSERT … ON CONFLICT (access_token) DO UPDATE` to atomically create or update a visitor record. Visit count increments only when the last connection was more than 8 hours ago. A `website_track` record is inserted in the same CTE when `force_track_values` is provided.

### D3 — Page tracking
`WebsiteTrack` model (`website.track`) stores `visitor_id`, `page_id`, `url`, and `visit_datetime`. The model disables `_log_access`. Tracks are appended with a 30-minute deduplication window in `_add_tracking()`.

### D4 — Visitor statistics
`_compute_page_statistics()` uses `_read_group` against `website.track` to compute `visitor_page_count`, `page_count`, and `page_ids`. `_compute_last_visited_page_id()` returns the most recently visited `website.page`.

### D5 — Visitor merge on login
`_merge_visitor()` transfers `website_track_ids` from an anonymous visitor to a partner-linked visitor and deletes the anonymous record. This is called when a user logs in to consolidate multi-device browsing history.

### D6 — Visitor cleanup cron
`_cron_unlink_old_visitors()` deletes inactive visitors in batches. The inactive domain: `last_connection_datetime < now - N days AND partner_id = False`. Default is 60 days from `website.visitor.live.days` system parameter.

### D7 — Timezone detection
`_get_visitor_timezone()` reads the `tz` cookie; falls back to `env.user.tz` for authenticated users. Timezone updates use `FOR NO KEY UPDATE SKIP LOCKED` to avoid concurrent update errors.

### Ten-dimension table — CAP-U60-02

| Dimension | Finding |
|---|---|
| Existence | Confirmed: `website/models/website_visitor.py` |
| Boundaries | Requires active HTTP request; returns empty if `request.env.uid` absent |
| Data model | `website.visitor`: `access_token` (unique), `partner_id`, `country_id`, `lang_id`, `timezone`, `visit_count`, `last_connection_datetime`. `website.track`: `visitor_id`, `page_id`, `url`, `visit_datetime` |
| Access control | `page_ids` restricted to `group_website_designer` |
| Performance | UPSERT via raw SQL bypasses ORM overhead; timezone update uses `SKIP LOCKED` |
| Error handling | `_get_visitor_from_request` returns `None` if no uid; never raises on mobile app context |
| Geo-location | Country resolved via `request.geoip.country_code` at visitor creation (RT) |
| Multi-website | `website_id` stored on visitor; visitors are per-website |
| Lifecycle | Cron cleanup removes partner-free visitors older than configured threshold |
| Integration | Extended by `website_crm`, `website_crm_sms`, `website_livechat` |

---

## CAP-U60-03 — URL rewriting and routing management

### D1 — WebsiteRoute model
`website.route` enumerates all GET-accessible application routes. `_refresh()` calls `ir_http._generate_routing_rules()` to synchronise the route table with the current routing map, creating and deleting rows as needed.

### D2 — WebsiteRewrite model
`website.rewrite` stores URL redirect/rewrite rules per website. Types: `404` (block), `301` (permanent redirect), `302` (temporary redirect), `308` (rewrite/alias). Constraints enforce non-empty `url_from`/`url_to` for redirects, reject fragment-only URLs, and validate regex syntax in `url_to` for 308 rules.

### D3 — Routing cache invalidation
On create/write/unlink of any `308` or `404` rewrite, `_invalidate_routing()` calls `registry.clear_cache('routing')` to force re-generation of the routing map on all workers.

### D4 — Import template
`get_import_templates()` returns a reference to `/website/static/xls/redirects_import_template.xlsx` for bulk import.

### Ten-dimension table — CAP-U60-03

| Dimension | Finding |
|---|---|
| Existence | Confirmed: `website/models/website_rewrite.py` |
| Boundaries | 308 rules must not target an existing page; `url_to` must start with `/` |
| Data model | `website.rewrite`: `name`, `website_id`, `active`, `url_from`, `route_id`, `url_to`, `redirect_type`, `sequence` |
| Access control | No custom ACL in this file; inherits standard website security |
| Validation | `@api.constrains` validates URL format, fragment, self-referencing, existing-page collision |
| Cache | Only `308` and `404` types invalidate routing cache; `301`/`302` served as fallback |
| Integration | `website.route` refreshed via `website.route._refresh()` using `ir.http._generate_routing_rules` |
| Multi-website | `website_id` scopes rewrites per website |
| Lifecycle | On unlink, routing cache invalidated if type was `308` or `404` |
| Import | XLS import template provided |

---

## CAP-U60-04 — Website menu tree

### D1 — Menu hierarchy constraints
`_validate_parent_menu()` enforces: maximum two nesting levels; mega menus cannot have parent or children; menus with children cannot be sub-menus. These are enforced via `@api.constrains`.

### D2 — Menu creation with multi-website broadcasting
When a menu is created without `website_id` (and no website context), the system creates one copy per website. The last record is returned as the canonical record.

### D3 — URL resolution
`_compute_url` automatically sets `url = '#'` for mega menus and dropdown containers. `save()` resolves the `url` against `website.page` domain to populate `page_id`.

### D4 — Mega menu content
`is_mega_menu` is a computed/inverse Boolean backed by `mega_menu_content` HTML field. Setting `is_mega_menu=True` triggers rendering of the `website.s_mega_menu_odoo_menu` template to seed the content.

### D5 — Active state detection
`_is_active()` compares the menu URL (and unslug'd variant) against `request.httprequest.url`. Query-string and netloc are also checked. Mega menus are never considered active.

### D6 — Designer group auto-addition
`write()` ensures that when `group_ids` is written on a menu, `website.group_website_designer` is automatically added to the groups set.

### D7 — Unlink cascade
`unlink()` extends deletion to remove menus on all websites sharing the same URL when the deleted menu was under the default main menu.

### Ten-dimension table — CAP-U60-04

| Dimension | Finding |
|---|---|
| Existence | Confirmed: `website/models/website_menu.py` |
| Boundaries | Max 2 levels; mega menus are leaf-only |
| Data model | `website.menu`: `name`, `url`, `page_id`, `controller_page_id`, `new_window`, `sequence`, `website_id`, `parent_id`, `child_id`, `parent_path`, `is_mega_menu`, `mega_menu_content`, `mega_menu_classes`, `group_ids` |
| Access control | `group_ids` visibility restricted to `base.group_user`; designer auto-added on group write |
| Visibility | `is_visible` computed: checks page `is_visible` and view `_handle_visibility` for public users |
| Performance | `get_tree()` builds nested dict in Python from ORM; template cache cleared on create/write/unlink |
| Multi-website | Menu without `website_id` at create time is broadcast to all websites |
| URL logic | Anchor-only URLs (#top, #bottom) handled explicitly; mailto prefix added when email in URL |
| Integration | Page `page_id` M2O linked; `website.page` URL updates back-propagated on save |
| Lifecycle | Main menu ref protected from deletion via `_unlink_except_master_tags` |

---

## CAP-U60-05 — Website form controller

### D1 — Public form POST endpoint
`WebsiteForm.website_form()` handles POST to `/website/form/<model_name>`. CSRF token validated only for authenticated sessions. Uses a savepoint to allow graceful rollback on validation error without rolling back the whole transaction.

### D2 — Model access gate
`_handle_website_form()` validates that `ir.model.website_form_access = True` for the target model before proceeding.

### D3 — Field extraction and type coercion
`extract_data()` iterates submitted values and applies `_input_filters` mapping (char, text, html, date, datetime, many2one, one2many, many2many, selection, boolean, integer, float, binary, monetary, tags) to coerce values to correct Python types. Custom (unauthorised) fields are collected as a free-text `custom` string.

### D4 — Record insertion and attachment handling
`insert_record()` creates the target record with `SUPERUSER_ID`. Custom text and metadata are appended to the configured `website_form_default_field_id` or posted as a `mail.message` log note. `insert_attachment()` creates `ir.attachment` records linked to the newly created record.

### D5 — Metadata capture
When `website_form_enable_metadata` system parameter is set, `extract_data()` appends IP, User-Agent, Accept-Language, and Referer to the `meta` field.

### D6 — mail.mail special handling
For `mail.mail` target model, `email_from` is replaced with a company-branded sender, and `reply_to` is set to the submitted `email_from`. HMAC signature validation prevents abuse of `email_to` and `email_cc` parameters.

### Ten-dimension table — CAP-U60-05

| Dimension | Finding |
|---|---|
| Existence | Confirmed: `website/controllers/form.py` |
| Boundaries | Only models with `website_form_access = True` accepted |
| Security | Partial CSRF check for authenticated sessions; HMAC validation for `mail.mail` email_to |
| Input filters | `_input_filters` dict maps ORM field types to coercion functions |
| Attachments | Uploaded files attached to created record; orphan attachments logged as mail message |
| Extensibility | `website_form_input_filter()` hook on destination model for pre-processing |
| Error handling | ValidationError returns JSON `{error_fields: [...]}` or `{error: ...}` |
| Savepoint | Savepoint wraps entire `_handle_website_form` call; closed without rollback on success |
| Session state | `form_builder_model_model`, `form_builder_model`, `form_builder_id` stored in session |
| Multi-language | None explicit in this controller |

---

## CAP-U60-06 — Blog publishing system (website_blog)

### D1 — BlogBlog model
`blog.blog` inherits `mail.thread`, `website.seo.metadata`, `website.multi.mixin`, `website.cover_properties.mixin`, `website.searchable.mixin`. Archiving a blog cascades to its posts.

### D2 — BlogPost model
`blog.post` inherits `mail.thread`, `website.seo.metadata`, `website.published.multi.mixin`, `website.page_visibility_options.mixin`, `website.cover_properties.mixin`, `website.searchable.mixin`. URL pattern is `/blog/<blog-slug>/<post-slug>`.

### D3 — Teaser computation
`teaser` is computed from `teaser_manual` if set, else from the first 200 characters of `text_from_html(content, True)`. Inverse `_set_teaser` updates `teaser_manual` without overwriting the English source.

### D4 — Publication date
`post_date` is computed from `published_date` if set, else from `create_date`. Setting `is_published=True` triggers `_check_for_publication()`, which posts a `mail.message` via template `website_blog.blog_post_template_new_post` with subtype `website_blog.mt_blog_blog_published`.

### D5 — Open Graph meta
`_default_website_meta()` populates `og:type = article`, `article:published_time`, `article:modified_time`, `article:tag`, `og:image` (from `cover_properties` JSON `background-image`).

### D6 — Search integration
`_search_get_detail()` for `blog.blog` returns search fields `['name', 'subtitle']` with mapping including `website_url` as `/blog/<id>`. For `blog.post`, search fields include `content` (HTML), `author_name`, with optional date detail.

### D7 — Tag system
`blog.tag` has `name`, `category_id` (→ `blog.tag.category`), `color`, `post_ids`. `blog.blog.all_tags()` runs a raw SQL GROUP BY to count tag usage per blog with min-frequency threshold.

### D8 — Reply-to spam guard
`blog.blog.message_post()` overrides to demote replies to a published-blog notification email as internal notes, preventing follower notification flood.

### Ten-dimension table — CAP-U60-06

| Dimension | Finding |
|---|---|
| Existence | Confirmed: `website_blog/models/website_blog.py` |
| Boundaries | Post visible only if `post_date <= now` and `is_published = True`; designers see drafts |
| Data model | `blog.blog`: sequence, name, subtitle, active, content, blog_post_ids. `blog.post`: name, subtitle, author_id, tag_ids, content, teaser, teaser_manual, post_date, visits, website_id (related from blog_id) |
| Access control | `mail_post_access = 'read'` — public can read messages on posts |
| Published notification | Subtype `website_blog.mt_blog_blog_published` used; spam guard via override |
| SEO | OG tags fully populated; inherits `website.seo.metadata` |
| Visits field | `visits` integer, default 0; incremented at runtime (RT) |
| Search types | `'blogs'`, `'blogs_only'`, `'blog_posts_only'`, `'all'` handled by `website.py` |
| Archiving | Archiving blog sets `active=False` on all its posts |
| Copy | `copy_data()` appends "(copy)" to name |

---

## CAP-U60-07 — Website CRM lead capture (website_crm)

### D1 — Website fields on crm.lead
`website_crm` adds `visitor_ids` (M2M → `website.visitor`) and `visitor_page_count` (Integer computed) to `crm.lead`.

### D2 — Form input filter
`crm.lead.website_form_input_filter()` normalises form submissions: removes `email_from`/`phone` if `partner_id` present; assigns `medium_id` (fetches/creates utm.medium 'website'); assigns default `team_id` and `user_id` from `request.website.crm_default_team_id` and `crm_default_user_id`; sets `type` to `'lead'` or `'opportunity'` depending on team configuration.

### D3 — Website model extension
`website_crm/models/website.py` adds `crm_default_team_id` (M2O → `crm.team`) and `crm_default_user_id` (M2O → `res.users`, internal only) to `website`.

### D4 — Visitor extension for CRM
`website_crm/models/website_visitor.py` adds `lead_ids` (M2M → `crm.lead`, restricted to `sales_team.group_sale_salesman`) and `lead_count` to `website.visitor`. The `_compute_email_phone` override also checks lead email/phone when the partner provides none.

### D5 — Visitor lifecycle with leads
`_inactive_visitors_domain()` appended with `lead_ids = False`, so visitors linked to at least one lead are never automatically deleted.

### D6 — Visitor merge preserves leads
`_merge_visitor()` overrides to transfer `lead_ids` from the anonymous visitor to the partner-linked target before unlinking the anonymous record.

### D7 — Phone formatting override
`website_crm/controllers/website_form.py` overrides `_handle_website_form` to format phone fields using `phone_validation.phone_format()` with country from visitor partner or GeoIP. Also auto-populates `state_id` from GeoIP for `crm.lead` forms.

### D8 — Lead-visitor linking on form insert
`insert_record()` override (in `website_crm/controllers/website_form.py`) links the newly created lead to the current visitor (`visitor_ids [(4, lead_id)]`). If this is the visitor's first lead and they have no partner, `visitor.name` is set from `lead.contact_name`.

### D9 — Merge fields
`_merge_get_fields_specific()` adds `visitor_ids` to the CRM merge logic, accumulating all visitor IDs from merged leads.

### Ten-dimension table — CAP-U60-07

| Dimension | Finding |
|---|---|
| Existence | Confirmed: `website_crm/models/crm_lead.py`, `website_crm/models/website.py`, `website_crm/models/website_visitor.py`, `website_crm/controllers/website_form.py` |
| Boundaries | Form access gated by `ir.model.website_form_access`; phone formatting only when country available |
| Data model | Adds `visitor_ids`, `visitor_page_count` to crm.lead; `crm_default_team_id`, `crm_default_user_id` to website |
| UTM | Medium auto-assigned to 'website' utm.medium if not in form |
| Geo state | GeoIP state auto-populated into `state_id` if form did not supply it |
| Visitor retention | Visitors with leads excluded from cleanup cron |
| Lead type | Determined by team `use_leads` flag; fallback to `crm.group_use_lead` group |
| Phone | Formatted using `INTERNATIONAL` format via `phone_validation.phone_format` |
| Merge | Both visitors and leads are merged on CRM lead merge |
| Page view count | Computed via raw SQL JOIN across `crm_lead_website_visitor_rel`, `website_visitor`, `website_track` |

---

## CAP-U60-08 — IAP company reveal for anonymous visitors (website_crm_iap_reveal)

### D1 — Reveal rule definition
`crm.reveal.rule` models configurable lead generation rules. Fields: `country_ids`, `state_ids`, `regex_url`, `industry_tag_ids`, `filter_on_size`, `company_size_min/max`, `contact_filter_type`, `preferred_role_id`, `seniority_id`, `extra_contacts` (1–5), `lead_for` (companies/people), `lead_type`, `team_id`, `tag_ids`, `user_id`, `priority`, `suffix`, `website_id`.

### D2 — Active rules cache
`_get_active_rules()` returns an `ormcache`-decorated structure mapping country codes to rule indices and storing per-rule `regex`, `website_id`, `country_codes`, `state_codes`. Cache is cleared on rule create/write/unlink.

### D3 — Page-view hook in ir.http
`website_crm_iap_reveal/models/ir_http.py:_serve_page()` fires after every successful 200 public page response. If the visitor has no existing leads (checked via `visitor_sudo.lead_ids`), `crm.reveal.view._create_reveal_view()` is called with IP, URL, country, and state. Matching rule IDs are stored in a cookie `rule_ids` to prevent duplicate views.

### D4 — Reveal view deduplication
`crm.reveal.view` records are inserted with `ON CONFLICT DO NOTHING` (unique on `(reveal_rule_id, reveal_ip)`). State transitions: `to_process` → `not_found` (when IAP service returns no match).

### D5 — Batch IAP processing (cron)
`_process_lead_generation()` cron: cleans old views, removes IPs already having leads (within 6 months), batches up to `DEFAULT_REVEAL_BATCH_LIMIT=25` IPs, calls `iap_tools.iap_jsonrpc` to endpoint `https://iap-services.odoo.com/iap/clearbit/1/reveal`, creates leads from response.

### D6 — Lead creation from IAP response
`_create_lead_from_response()` checks for existing `reveal_id` (clearbit ID) to prevent duplicates. Calls `_lead_vals_from_response()` which assembles lead values via `crm.iap.lead.helpers.lead_vals_from_response`. Posts a message with template `iap_mail.enrich_company` as an internal note.

### D7 — crm.lead IAP fields
`website_crm_iap_reveal/models/crm_lead.py` adds `reveal_ip`, `reveal_iap_credits`, `reveal_rule_id` to `crm.lead`. These are included in `_merge_get_fields`.

### Ten-dimension table — CAP-U60-08

| Dimension | Finding |
|---|---|
| Existence | Confirmed: `website_crm_iap_reveal/models/crm_reveal_rule.py`, `website_crm_iap_reveal/models/crm_reveal_view.py`, `website_crm_iap_reveal/models/ir_http.py`, `website_crm_iap_reveal/models/crm_lead.py` |
| Boundaries | Fires only for public users on 200 responses; skipped if visitor already has leads |
| IAP endpoint | `https://iap-services.odoo.com/iap/clearbit/1/reveal` (configurable via `reveal.endpoint` sys param) |
| Deduplication | `ON CONFLICT DO NOTHING` in SQL; 6-month lead creation check before batch |
| Credit handling | `_notify_no_more_credit` called on credit error; `reveal.already_notified` flag prevents repeat notifications |
| Cleanup | `_clean_reveal_views` removes `not_found` views older than `reveal.view_weeks_valid` weeks (default 5) |
| Rule caching | `@ormcache()` with clear on create/write/unlink |
| Cookie | `rule_ids` cookie stores matched rule IDs per session (optional cookie) |
| Batch limit | 25 IPs per batch |
| Lead suffix | Optional suffix appended to lead name from rule |

---

## CAP-U60-09 — Live chat to CRM bridge (website_crm_livechat)

### D1 — Lead session count on crm.lead
`website_crm_livechat/models/crm_lead.py` adds `visitor_sessions_count` (computed Integer, restricted to `im_livechat.im_livechat_group_user`) counting distinct `discuss.channel` records across all linked visitors. Action `action_redirect_to_livechat_sessions` filters by `livechat_visitor_id` and `has_message = True`.

### D2 — Chatbot lead enrichment
`website_crm_livechat/models/chatbot_script_step.py` overrides `_chatbot_crm_prepare_lead_values()` to set the lead name from `livechat_visitor_id.display_name` and link the visitor ID to the new lead's `visitor_ids`.

### D3 — /lead command visitor linking
`website_crm_livechat/models/discuss_channel.py` overrides `_convert_visitor_to_lead()` to write the new lead into `visitor_sudo.lead_ids` and copies visitor `country_id` onto the lead when the lead has no country.

### Ten-dimension table — CAP-U60-09

| Dimension | Finding |
|---|---|
| Existence | Confirmed: `website_crm_livechat/models/crm_lead.py`, `website_crm_livechat/models/chatbot_script_step.py`, `website_crm_livechat/models/discuss_channel.py` |
| Boundaries | Session count restricted to livechat user group |
| Integration | Bridges `discuss.channel` (livechat), `website.visitor`, `crm.lead` |
| Chatbot | Lead name prefixed with visitor display name when livechat_visitor_id present |
| /lead command | Visitor linked to lead on channel `/lead` command; country_id propagated |
| Controllers | No controller file under `website_crm_livechat/controllers/` |
| Dependencies | `website_livechat`, `website_crm`, `im_livechat` |
| Multi-visitor | `lead.visitor_ids.discuss_channel_ids` traverses M2M for session aggregation |
| Lead origin | Lead can be created from chatbot step or from operator /lead command |
| Merge | No explicit merge override; relies on `website_crm._merge_visitor` |

---

## CAP-U60-10 — Partner/reseller locator (website_crm_partner_assign)

### D1 — Partner grade system
`res.partner.grade` inherits `website.published.mixin`. `partner_weight` (Integer) controls lead assignment probability. `_default_is_published()` returns `True`. Grade URL: `/partners/grade/<slug>`.

### D2 — Lead geo-assignment
`crm.lead.assign_partner()` calls `search_geo_partner()` which performs a six-tier geographic fallback search: ±2°/±1.5° → ±4°/±3° → ±8°/±8° → country-wide → closest point (raw SQL `point(longitude, latitude) <-> point(x, y)` distance). Weighted random selection from matching partners using `partner_weight`.

### D3 — Portal lead/opportunity views
`WebsiteAccount` (CustomerPortal) provides `/my/leads`, `/my/leads/page/<n>`, `/my/opportunities`, `/my/lead/<id>`, `/my/opportunity/<id>`. Domain: `partner_assigned_id child_of user.commercial_partner_id`.

### D4 — Partner locator public pages
`WebsiteCrmPartnerAssign.partners()` serves `/partners` with filtering by grade and country; reads GeoIP country for default filter. Partners ordered by `grade_sequence ASC, implemented_partner_count DESC, complete_name ASC, id ASC`.

### D5 — Portal interest/disinterest actions
`partner_interested()` / `partner_desinterested()` allow portal users to accept or decline leads. Declined leads write to `partner_declined_ids` M2M. Portal users can also update lead details via `update_contact_details_from_portal()` and stage via `update_stage_from_portal()`.

### D6 — Portal opportunity creation
`create_opp_portal()` allows graded portal users to self-report new opportunities with `priority='2'`, auto-assigned to their commercial partner.

### D7 — Access guard
`_assert_portal_write_access()` checks `partner_assigned_id child_of user.commercial_partner_id` for portal users; raises `AccessError` otherwise.

### D8 — Implemented partner count
`res.partner.implemented_partner_count` counts published customers (`assigned_partner_id` → `res.partner.implemented_partner_ids`) to rank partners on the locator page.

### Ten-dimension table — CAP-U60-10

| Dimension | Finding |
|---|---|
| Existence | Confirmed: `website_crm_partner_assign/models/crm_lead.py`, `website_crm_partner_assign/models/res_partner.py`, `website_crm_partner_assign/models/res_partner_grade.py`, `website_crm_partner_assign/controllers/main.py` |
| Boundaries | Portal write access gated to assigned partner hierarchy |
| Geo search | Six-tier progressive geographic radius fallback; final fallback is closest-point raw SQL |
| Weighting | `random.choices` with `partner_weight` list |
| Portal routes | `/my/leads`, `/my/opportunities`, `/my/lead/<id>`, `/my/opportunity/<id>` |
| Public routes | `/partners`, `/partners/grade/<grade>`, `/partners/country/<country>` and combinations |
| Salesman sync | `assign_salesman_of_assigned_partner()` sets lead `user_id` from `partner.user_id` |
| Activity | Portal users can create/update activities on opportunities |
| Mail ACL | `_mail_get_operation_for_mail_message_operation` grants `read` level for assigned-partner portal writes |
| Declined tracking | `partner_declined_ids` M2M prevents re-assignment to declined partners |

---

## CAP-U60-11 — SMS from website visitor context (website_crm_sms)

### D1 — SMS composer context
`website_crm_sms/models/website_visitor.py` overrides `_check_for_sms_composer()` and `_prepare_sms_composer_context()`. If no partner but leads exist, it checks for leads whose `phone` matches `visitor.mobile`. If found, the SMS composer context is `{default_res_model: 'crm.lead', default_res_id: lead.id, number_field_name: 'phone'}`.

### Ten-dimension table — CAP-U60-11

| Dimension | Finding |
|---|---|
| Existence | Confirmed: `website_crm_sms/models/website_visitor.py` |
| Boundaries | Falls back to lead phone only when `visitor.partner_id` absent |
| Lead selection | Leads filtered by `phone == visitor.mobile`, sorted by confidence level descending |
| Context | SMS composer target switches from `res.partner` to `crm.lead` when appropriate |
| Controllers | No controllers in this module |
| Dependencies | `website_crm`, `sms` |
| Models | Only `website.visitor` extended |
| Integration | Companion to `website_crm` visitor extension |
| Tests | `website_crm_sms/tests/` present |
| Scope | Minimal glue module |

---

## CAP-U60-12 — Customer showcase (website_customer)

### D1 — Partner website tags
`website_customer/models/res_partner.py` adds `website_tag_ids` (M2M → `res.partner.tag`) for filtering on the `/customers` page. `get_backend_menu_id()` returns the Contacts menu for portal back-navigation.

### D2 — ResPartnerTag model
`res.partner.tag` inherits `website.published.mixin`. Fields: `name`, `partner_ids`, `classname` (Bootstrap colour selection: info/primary/success/warning/danger), `active`. `_default_is_published()` returns `True`.

### D3 — Customers controller
`WebsiteCustomer.customers()` serves `/customers` and paged/filtered variants (by country and industry). Domain: `website_published = True AND assigned_partner_id != False`. Industries and countries computed by `_read_group` for filter widgets. Pager at 20 per page.

### D4 — Customer detail
`customers_detail()` serves `/customers/<partner_id>`. Validates `website_published` and redirects on slug mismatch. Uses `SUPERUSER_ID` implicitly via `sudo()`.

### D5 — Sitemap integration
`sitemap_industry()` generator yields `/customers`, `/customers/industry/<slug>`, and `/customers/country/<slug>` entries for sitemap.

### D6 — Website suggested controllers
`website_customer/models/website.py` appends `_('References')` → `/customers` to `get_suggested_controllers()`.

### Ten-dimension table — CAP-U60-12

| Dimension | Finding |
|---|---|
| Existence | Confirmed: `website_customer/models/res_partner.py`, `website_customer/models/website.py`, `website_customer/controllers/main.py` |
| Boundaries | Only `website_published=True` and `assigned_partner_id != False` partners shown |
| Data model | `res.partner.tag`: name, classname (Bootstrap), active, partner_ids. Adds `website_tag_ids` to `res.partner` |
| Pager | 20 per page (class constant `_references_per_page`) |
| Search | Free-text against name, website_description, industry_id.name |
| Tag filter | `website_tag_ids` in domain filter; `website_published=True` on tags |
| Google Map | Controller extends `GoogleMap` base class from `website_google_map` |
| Sitemap | Yields country and industry sub-paths |
| Slug redirect | Detail route redirects if current slug does not match computed slug |
| Tag colours | Five Bootstrap classes: info, primary, success, warning, danger |

---

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U60-C001 | CAP-U60-01 | `website/models/ir_ui_view.py:18` | `_inherit = ["ir.ui.view", "website.seo.metadata"]` | FACT | Always | — | `ir.ui.view` inherits both `ir.ui.view` and `website.seo.metadata` mixins | N-U60-001 |
| VDR-U60-C002 | CAP-U60-01 | `website/models/ir_ui_view.py:20` | `website_id = fields.Many2one('website', ondelete='cascade'` | FACT | Always | — | `website_id` M2O with cascade delete added to ir.ui.view | N-U60-001 |
| VDR-U60-C003 | CAP-U60-01 | `website/models/ir_ui_view.py:24` | `track = fields.Boolean(string='Track', default=False` | FACT | Always | — | Boolean `track` field added to control visitor tracking per view | N-U60-002 |
| VDR-U60-C004 | CAP-U60-01 | `website/models/ir_ui_view.py:25-33` | visibility = fields.Selection | FACT | Always | — | Four-state visibility selection on ir.ui.view | N-U60-003 |
| VDR-U60-C005 | CAP-U60-01 | `website/models/ir_ui_view.py:43-47` | `r.sudo().visibility_password = (r.visibility_password_display and crypt_context.hash(r.visibility_password_display))` | FACT | When type=qweb | — | Password visibility stores bcrypt hash via `_crypt_context().hash()` | N-U60-003 |
| VDR-U60-C006 | CAP-U60-01 | `website/models/ir_ui_view.py:93-168` | def write(self, vals) | FACT | When website_id context set | — | Copy-on-Write mechanism creates website-specific view copies on generic view write | N-U60-004 |
| VDR-U60-C007 | CAP-U60-01 | `website/models/ir_ui_view.py:99` | `if not current_website_id or self.env.context.get('no_cow'):` | FACT | Always | — | COW can be bypassed via `no_cow` context key | N-U60-004 |
| VDR-U60-C008 | CAP-U60-01 | `website/models/ir_ui_view.py:146` | `website_specific_view = view.copy(copy_vals)` | FACT | During COW | — | COW creates website-specific view via `copy()` with same key | N-U60-004 |
| VDR-U60-C009 | CAP-U60-01 | `website/models/ir_ui_view.py:213-235` | def unlink(self) | FACT | During COU | — | Copy-on-Unlink creates specific copies for other websites before deletion | N-U60-004 |
| VDR-U60-C010 | CAP-U60-01 | `website/models/ir_ui_view.py:234` | `self.env.registry.clear_cache('templates')` | FACT | After unlink | — | Template cache cleared after view unlink | N-U60-004 |
| VDR-U60-C011 | CAP-U60-01 | `website/models/ir_ui_view.py:288-311` | `def filter_duplicate(self):` | FACT | Always | — | `filter_duplicate()` returns most specific view per key for current website | N-U60-001 |
| VDR-U60-C012 | CAP-U60-01 | `website/models/ir_ui_view.py:383` | `return domain & Domain('website_id', 'in', (False, self.env.context.get('website_id', False)))` | FACT | Template lookup | — | Template domain restricts to generic (website_id=False) or current-website views | N-U60-001 |
| VDR-U60-C013 | CAP-U60-01 | `website/models/ir_ui_view.py:395` | `return f"website_id asc, {super()._get_template_order()}"` | FACT | Template query | — | Template ordering prepends `website_id asc` so generic views sort before specific | N-U60-001 |
| VDR-U60-C014 | CAP-U60-01 | `website/models/ir_ui_view.py:403-438` | `def _handle_visibility(self, do_raise=True):` | FACT | At render | — | Visibility enforcement: public→signed-in→group→password; designer bypasses all | N-U60-003 |
| VDR-U60-C015 | CAP-U60-01 | `website/models/ir_ui_view.py:418-425` | elif visibility == 'password' and | FACT | Password visibility | — | Password verified with bcrypt context against stored hash; stored in session on success | N-U60-003 |
| VDR-U60-C016 | CAP-U60-01 | `website/models/ir_ui_view.py:509-519` | def _get_allowed_root_attrs(self) | FACT | Always | — | Root attrs extended with UTM-visibility parameters | N-U60-003 |
| VDR-U60-C017 | CAP-U60-02 | `website/models/website_visitor.py:29-49` | class WebsiteVisitor(models.Model) | FACT | Always | — | Anonymous token = SHA-1 of (remote_addr + user_agent + session.sid)[:32]; authenticated = partner_id int | N-U60-005 |
| VDR-U60-C018 | CAP-U60-02 | `website/models/website_visitor.py:51-78` | `access_token = fields.Char(required=True, default=_get_access_token, copy=False)` | FACT | Always | — | access_token unique constraint on visitor table | N-U60-005 |
| VDR-U60-C019 | CAP-U60-02 | `website/models/website_visitor.py:66` | visit_count = fields.Integer | FACT | Always | — | New visit counted only when last connection was more than 8 hours ago | N-U60-006 |
| VDR-U60-C020 | CAP-U60-02 | `website/models/website_visitor.py:194-258` | `def _upsert_visitor(self, access_token, force_track_values=None):` | FACT | Always | — | Single raw SQL UPSERT atomically creates/updates visitor and optionally inserts track record | N-U60-006 |
| VDR-U60-C021 | CAP-U60-02 | `website/models/website_visitor.py:233-235` | DO UPDATE SET | FACT | On UPSERT conflict | — | Visit count SQL increment uses 8-hour interval check | N-U60-006 |
| VDR-U60-C022 | CAP-U60-02 | `website/models/website_visitor.py:291-303` | `def _handle_webpage_dispatch(self, website_page):` | FACT | On tracked page dispatch | — | Calls `_get_visitor_from_request(force_create=True, force_track_values=...)` to track visits | N-U60-006 |
| VDR-U60-C023 | CAP-U60-02 | `website/models/website_visitor.py:305-312` | `def _add_tracking(self, domain, website_track_values):` | FACT | Always | — | 30-minute deduplication window before adding new track record | N-U60-006 |
| VDR-U60-C024 | CAP-U60-02 | `website/models/website_visitor.py:314-332` | `def _merge_visitor(self, target):` | FACT | On user login | — | Anonymous visitor tracks transferred to partner visitor; anonymous record deleted | N-U60-007 |
| VDR-U60-C025 | CAP-U60-02 | `website/models/website_visitor.py:349-360` | `def _inactive_visitors_domain(self):` | FACT | Cron | — | Inactive domain: last_connection < now - N days AND partner_id = False; default 60 days | N-U60-007 |
| VDR-U60-C026 | CAP-U60-02 | `website/models/website_visitor.py:362-372` | `def _update_visitor_timezone(self, timezone):` | FACT | Always | — | Timezone update via raw SQL with `FOR NO KEY UPDATE SKIP LOCKED` | N-U60-005 |
| VDR-U60-C027 | CAP-U60-02 | `website/models/website_visitor.py:388-395` | `def _get_visitor_timezone(self):` | FACT | Always | — | Timezone from `tz` cookie; fallback `env.user.tz` for authenticated users | N-U60-005 |
| VDR-U60-C028 | CAP-U60-03 | `website/models/website_rewrite.py:13-18` | class WebsiteRoute(models.Model) | FACT | Always | — | `website.route` table enumerates all GET routes in the application | N-U60-008 |
| VDR-U60-C029 | CAP-U60-03 | `website/models/website_rewrite.py:38-57` | def _refresh(self) | FACT | On demand | — | Route table synchronised with routing map via `ir_http._generate_routing_rules()` | N-U60-008 |
| VDR-U60-C030 | CAP-U60-03 | `website/models/website_rewrite.py:70-81` | redirect_type = fields.Selection | FACT | Always | — | Four redirect types: 404 block, 301 permanent, 302 temporary, 308 alias | N-U60-008 |
| VDR-U60-C031 | CAP-U60-03 | `website/models/website_rewrite.py:159-165` | def _invalidate_routing(self) | FACT | On 308/404 change | — | Only 308 and 404 types trigger routing cache invalidation | N-U60-008 |
| VDR-U60-C032 | CAP-U60-04 | `website/models/website_menu.py:15-57` | class WebsiteMenu(models.Model) | FACT | Always | — | `website.menu` uses `_parent_store = True` for efficient hierarchy traversal | N-U60-009 |
| VDR-U60-C033 | CAP-U60-04 | `website/models/website_menu.py:79-108` | `def _validate_parent_menu(self):` | FACT | On create/write | — | Max 2 nesting levels; mega menu cannot have parent or child; menus with children cannot be sub-menus | N-U60-009 |
| VDR-U60-C034 | CAP-U60-04 | `website/models/website_menu.py:109-151` | `def create(self, vals_list):` | FACT | On create | — | Menu without website_id is broadcast to all websites; website context narrows creation | N-U60-009 |
| VDR-U60-C035 | CAP-U60-04 | `website/models/website_menu.py:153-160` | def write(self, vals) | FACT | On write with group_ids | — | Designer group auto-added when group_ids written to menu | N-U60-009 |
| VDR-U60-C036 | CAP-U60-04 | `website/models/website_menu.py:208-261` | `def _is_active(self):` | FACT | With request context | — | Menu active state uses URL comparison with unslug normalisation and query-string matching | N-U60-009 |
| VDR-U60-C037 | CAP-U60-05 | `website/controllers/form.py:25` | `@http.route('/website/form', type='http', auth="public", methods=['POST'], multilang=False, readonly=True)` | FACT | Always | — | Empty POST endpoint at `/website/form` prevents language prefix on form actions | N-U60-010 |
| VDR-U60-C038 | CAP-U60-05 | `website/controllers/form.py:31` | `@http.route('/website/form/<string:model_name>', type='http', auth="public", methods=['POST'], website=True, csrf=False, captcha='website_form')` | FACT | Always | — | Main form endpoint uses `captcha='website_form'` and disables CSRF | N-U60-010 |
| VDR-U60-C039 | CAP-U60-05 | `website/controllers/form.py:37-39` | csrf_token = request.params.pop | FACT | Authenticated sessions | — | Partial CSRF check only for authenticated sessions | N-U60-010 |
| VDR-U60-C040 | CAP-U60-05 | `website/controllers/form.py:63` | `model_record = request.env['ir.model'].sudo().search([('model', '=', model_name), ('website_form_access', '=', True)])` | FACT | Always | — | `website_form_access` flag on ir.model controls which models accept website forms | N-U60-010 |
| VDR-U60-C041 | CAP-U60-05 | `website/controllers/form.py:144-161` | _input_filters = | FACT | Always | — | 14 field type coercion handlers in `_input_filters` dict | N-U60-010 |
| VDR-U60-C042 | CAP-U60-05 | `website/controllers/form.py:263-296` | `def insert_record(self, request, model_sudo, values, custom, meta=None):` | FACT | Always | — | Record created with SUPERUSER_ID; custom fields and metadata appended to `website_form_default_field_id` or as mail log note | N-U60-010 |
| VDR-U60-C043 | CAP-U60-06 | `website_blog/models/website_blog.py:17-23` | _inherit = | FACT | Always | — | BlogBlog inherits 5 mixins | N-U60-011 |
| VDR-U60-C044 | CAP-U60-06 | `website_blog/models/website_blog.py:164-166` | _inherit = ['mail.thread | FACT | Always | — | BlogPost inherits 6 mixins including `website.published.multi.mixin` | N-U60-011 |
| VDR-U60-C045 | CAP-U60-06 | `website_blog/models/website_blog.py:170-175` | def _compute_website_url(self) | FACT | Always | — | Blog post URL: `/blog/<blog-slug>/<post-slug>` | N-U60-011 |
| VDR-U60-C046 | CAP-U60-06 | `website_blog/models/website_blog.py:203` | `visits = fields.Integer('No of Views', copy=False, default=0, readonly=True)` | FACT | Always | — | `visits` counter field on blog.post; incremented at runtime (RT) | N-U60-011 |
| VDR-U60-C047 | CAP-U60-06 | `website_blog/models/website_blog.py:241-251` | def _check_for_publication(self, vals) | FACT | On publish | — | Publishing a post triggers blog-level mail notification with subtype `mt_blog_blog_published` | N-U60-011 |
| VDR-U60-C048 | CAP-U60-06 | `website_blog/models/website_blog.py:261-273` | result = True | FACT | On write | — | Archiving a post unpublishes it | N-U60-011 |
| VDR-U60-C049 | CAP-U60-06 | `website_blog/models/website_blog.py:317-328` | `res['default_opengraph']['og:type'] = 'article'` | FACT | SEO | — | OG type set to 'article'; published_time, modified_time, tag from model fields | N-U60-011 |
| VDR-U60-C050 | CAP-U60-06 | `website_blog/models/website_blog.py:66-98` | `def all_tags(self, join=False, min_limit=1):` | FACT | Always | — | Raw SQL GROUP BY on `blog_post_blog_tag_rel` to compute tag frequency per blog | N-U60-012 |
| VDR-U60-C051 | CAP-U60-06 | `website_blog/models/website_blog.py:55-64` | def message_post | FACT | On reply to published notification | — | Reply to blog publication email demoted to internal note to prevent follower flood | N-U60-011 |
| VDR-U60-C052 | CAP-U60-06 | `website_blog/models/website.py:11-13` | `suggested_controllers.append((_('Blog'), self.env['ir.http']._url_for('/blog'), 'website_blog'))` | FACT | Always | — | Blog URL `/blog` added to website suggested controllers | N-U60-011 |
| VDR-U60-C053 | CAP-U60-07 | `website_crm/models/crm_lead.py:10` | `visitor_ids = fields.Many2many('website.visitor', string="Web Visitors")` | FACT | Always | — | M2M `visitor_ids` added to crm.lead | N-U60-013 |
| VDR-U60-C054 | CAP-U60-07 | `website_crm/models/crm_lead.py:47-64` | `def website_form_input_filter(self, request, values):` | FACT | On form submit | — | `website_form_input_filter` hook normalises medium, team, user, and lead type for crm.lead | N-U60-013 |
| VDR-U60-C055 | CAP-U60-07 | `website_crm/models/crm_lead.py:52-54` | values['medium_id'] = values.get('medium_id') or | FACT | On form submit | — | UTM medium defaulted to 'website' when not supplied in form | N-U60-013 |
| VDR-U60-C056 | CAP-U60-07 | `website_crm/models/website.py:15-21` | crm_default_team_id = fields.Many2one | FACT | Always | — | Default team and salesperson per website for Contact Us form leads | N-U60-013 |
| VDR-U60-C057 | CAP-U60-07 | `website_crm/models/website_visitor.py:10-11` | lead_ids = fields.Many2many | FACT | Always | — | `lead_ids` M2M on website.visitor restricted to sales group | N-U60-013 |
| VDR-U60-C058 | CAP-U60-07 | `website_crm/models/website_visitor.py:45-47` | def _inactive_visitors_domain(self) | FACT | Cron | — | Visitors with leads excluded from cleanup cron | N-U60-013 |
| VDR-U60-C059 | CAP-U60-07 | `website_crm/controllers/website_form.py:49-55` | if model_name = | FACT | On CRM form submit | — | GeoIP state auto-populated into `state_id` for crm.lead forms | N-U60-013 |
| VDR-U60-C060 | CAP-U60-07 | `website_crm/controllers/website_form.py:58-91` | `def insert_record(self, request, model_sudo, values, custom, meta=None):` | FACT | On CRM form submit | — | Lead linked to visitor; visitor.name set from lead.contact_name if first lead and no partner | N-U60-013 |
| VDR-U60-C061 | CAP-U60-08 | `website_crm_iap_reveal/models/crm_reveal_rule.py:18-19` | DEFAULT_ENDPOINT = 'https://iap-services.odoo.com | FACT | Always | — | IAP endpoint default and batch limit of 25 IPs | N-U60-014 |
| VDR-U60-C062 | CAP-U60-08 | `website_crm_iap_reveal/models/crm_reveal_rule.py:35` | `regex_url = fields.Char(string='URL Expression', help='Regex to track website pages.` | FACT | Always | — | Regex URL field for rule page matching | N-U60-014 |
| VDR-U60-C063 | CAP-U60-08 | `website_crm_iap_reveal/models/crm_reveal_rule.py:118` | `@tools.ormcache()` | FACT | Always | — | `_get_active_rules()` is ormcache-decorated for performance | N-U60-014 |
| VDR-U60-C064 | CAP-U60-08 | `website_crm_iap_reveal/models/crm_reveal_rule.py:150-178` | for rule in rules_records | FACT | Always | — | Returns nested structure: `{country_rules: {country_code: [rule_indices]}, rules: [...]}` | N-U60-014 |
| VDR-U60-C065 | CAP-U60-08 | `website_crm_iap_reveal/models/ir_http.py:17-45` | def _serve_page(cls) | FACT | After 200 public page | — | Reveal view creation triggered after every successful 200 public page response | N-U60-014 |
| VDR-U60-C066 | CAP-U60-08 | `website_crm_iap_reveal/models/ir_http.py:23` | `if not (visitor_sudo and visitor_sudo.lead_ids):` | FACT | On page serve | — | Reveal skipped if visitor already has leads | N-U60-014 |
| VDR-U60-C067 | CAP-U60-08 | `website_crm_iap_reveal/models/ir_http.py:33` | `rules_excluded = (request.cookies.get('rule_ids') or '').split(',')` | FACT | On page serve | — | Previously matched rule IDs stored in `rule_ids` cookie to prevent duplicate reveal views | N-U60-014 |
| VDR-U60-C068 | CAP-U60-08 | `website_crm_iap_reveal/models/crm_reveal_view.py:43-51` | INSERT INTO crm_reveal_view | FACT | On reveal view create | — | `ON CONFLICT DO NOTHING` prevents duplicate reveal views per IP/rule pair | N-U60-014 |
| VDR-U60-C069 | CAP-U60-08 | `website_crm_iap_reveal/models/crm_reveal_rule.py:207-226` | `def _process_lead_generation(self, autocommit=True):` | FACT | Cron | — | Cron batches reveal views, calls IAP, creates leads; auto-commits each batch | N-U60-014 |
| VDR-U60-C070 | CAP-U60-08 | `website_crm_iap_reveal/models/crm_reveal_rule.py:352-354` | `endpoint = self.env['ir.config_parameter'].sudo().get_param('reveal.endpoint', DEFAULT_ENDPOINT) + '/iap/clearbit/1/reveal'` | FACT | On IAP call | — | IAP endpoint configurable via `reveal.endpoint` system parameter | N-U60-014 |
| VDR-U60-C071 | CAP-U60-08 | `website_crm_iap_reveal/models/crm_reveal_rule.py:365-370` | `already_created_lead = self.env['crm.lead'].search_count([('reveal_id', '=', result['clearbit_id'])], limit=1)` | FACT | On lead create | — | Duplicate lead prevention via clearbit_id (`reveal_id`) check | N-U60-014 |
| VDR-U60-C072 | CAP-U60-08 | `website_crm_iap_reveal/models/crm_lead.py:10-12` | reveal_ip = fields.Char(string='IP Address') | FACT | Always | — | Three IAP reveal fields added to crm.lead | N-U60-014 |
| VDR-U60-C073 | CAP-U60-09 | `website_crm_livechat/models/crm_lead.py:10` | `visitor_sessions_count = fields.Integer('# Sessions', compute="_compute_visitor_sessions_count", groups="im_livechat.im_livechat_group_user")` | FACT | Always | — | Live chat session count on crm.lead restricted to livechat user group | N-U60-015 |
| VDR-U60-C074 | CAP-U60-09 | `website_crm_livechat/models/chatbot_script_step.py:12-16` | values = super()._chatbot_crm_prepare_lead_values | FACT | On chatbot lead creation | — | Chatbot lead name set from visitor display name; visitor linked to lead | N-U60-015 |
| VDR-U60-C075 | CAP-U60-09 | `website_crm_livechat/models/discuss_channel.py:16-18` | if visitor_sudo | FACT | On /lead command | — | Lead linked to visitor; visitor country propagated to lead | N-U60-015 |
| VDR-U60-C076 | CAP-U60-10 | `website_crm_partner_assign/models/crm_lead.py:14-16` | partner_latitude | FACT | Always | — | Geo lat/long fields (10,7 precision) added to crm.lead | N-U60-016 |
| VDR-U60-C077 | CAP-U60-10 | `website_crm_partner_assign/models/crm_lead.py:145-215` | `def search_geo_partner(self):` | FACT | Always | — | Six-tier geographic partner search with progressive radius expansion | N-U60-016 |
| VDR-U60-C078 | CAP-U60-10 | `website_crm_partner_assign/models/crm_lead.py:196-207` | `point(partner_longitude, partner_latitude) <-> point(%s,%s)) AS distance` | FACT | Fallback | — | Final fallback uses PostgreSQL point-distance operator for nearest partner | N-U60-016 |
| VDR-U60-C079 | CAP-U60-10 | `website_crm_partner_assign/models/crm_lead.py:211-214` | res_partner_ids[lead.id] = random.choices | FACT | On assignment | — | Weighted random partner selection using `random.choices` with `partner_weight` | N-U60-016 |
| VDR-U60-C080 | CAP-U60-10 | `website_crm_partner_assign/models/res_partner.py:21-26` | partner_weight = fields.Integer | FACT | Always | — | `partner_weight` computed from `grade_id.partner_weight` | N-U60-016 |
| VDR-U60-C081 | CAP-U60-10 | `website_crm_partner_assign/models/res_partner_grade.py:10-11` | `_inherit = ['res.partner.grade', 'website.published.mixin']` | FACT | Always | — | Partner grade inherits `website.published.mixin` | N-U60-016 |
| VDR-U60-C082 | CAP-U60-10 | `website_crm_partner_assign/controllers/main.py:52-93` | `@http.route(['/my/leads', '/my/leads/page/<int:page>'], type='http', auth="user", website=True)` | FACT | Always | — | Portal `/my/leads` and `/my/opportunities` routes require auth="user" | N-U60-016 |
| VDR-U60-C083 | CAP-U60-10 | `website_crm_partner_assign/controllers/main.py:164-168` | `@http.route(['''/my/lead/<model('crm.lead', "[('type','=', 'lead')]"):lead>''']` | FACT | Always | — | Portal lead route uses inline domain model converter to restrict to type='lead' | N-U60-016 |
| VDR-U60-C084 | CAP-U60-10 | `website_crm_partner_assign/models/crm_lead.py:36-41` | `def _assert_portal_write_access(self):` | FACT | Portal write | — | Portal write access gated to leads where `partner_assigned_id child_of user.commercial_partner_id` | N-U60-016 |
| VDR-U60-C085 | CAP-U60-10 | `website_crm_partner_assign/models/crm_lead.py:299-325` | `def create_opp_portal(self, values):` | FACT | Portal | — | Portal users with grade can create opportunities; priority='2', partner_assigned_id = commercial partner | N-U60-016 |
| VDR-U60-C086 | CAP-U60-11 | `website_crm_sms/models/website_visitor.py:10-16` | `def _check_for_sms_composer(self):` | FACT | Always | — | SMS composer availability check extended to leads when no partner | N-U60-017 |
| VDR-U60-C087 | CAP-U60-11 | `website_crm_sms/models/website_visitor.py:18-28` | `def _prepare_sms_composer_context(self):` | FACT | Always | — | SMS composer context switches to crm.lead target when lead phone matches visitor mobile | N-U60-017 |
| VDR-U60-C088 | CAP-U60-12 | `website_customer/models/res_partner.py:10-17` | website_tag_ids = fields.Many2many | FACT | Always | — | `website_tag_ids` M2M for filtering customers on /customers page | N-U60-018 |
| VDR-U60-C089 | CAP-U60-12 | `website_customer/models/res_partner.py:26-40` | _description = 'Partner | FACT | Always | — | `res.partner.tag` with Bootstrap classname selection and `website.published.mixin` | N-U60-018 |
| VDR-U60-C090 | CAP-U60-12 | `website_customer/controllers/main.py:54-63` | @http.route | FACT | Always | — | 8 route patterns for /customers with industry and country facets | N-U60-018 |
| VDR-U60-C091 | CAP-U60-12 | `website_customer/controllers/main.py:69` | `domain = [('website_published', '=', True), ('assigned_partner_id', '!=', False)]` | FACT | Always | — | Customer list requires website_published=True AND assigned_partner_id != False | N-U60-018 |
| VDR-U60-C092 | CAP-U60-12 | `website_customer/controllers/main.py:15-16` | class WebsiteCustomer(GoogleMap) | FACT | Always | — | WebsiteCustomer extends GoogleMap; 20 results per page | N-U60-018 |
| VDR-U60-C093 | CAP-U60-10 | `website_crm_partner_assign/controllers/main.py:188-207` | class WebsiteCrmPartnerAssign | FACT | Always | — | Partner locator extends WebsitePartnerPage and GoogleMap; 40 per page | N-U60-016 |
| VDR-U60-C094 | CAP-U60-10 | `website_crm_partner_assign/controllers/main.py:335-337` | partner_ids = partner_obj.sudo().search | FACT | Always | — | Partner locator sort order: grade_sequence ASC, implemented_partner_count DESC, name ASC | N-U60-016 |
| VDR-U60-C095 | CAP-U60-06 | `website_blog/models/website_blog.py:193` | `website_message_ids = fields.One2many(domain=lambda self: [('model', '=', self._name), ('message_type', '=', 'comment'), '&', ('is_internal', '=', False), ('subtype_id.internal', '=', False)])` | FACT | Always | — | Blog post public comments restricted to non-internal comment messages | N-U60-011 |
| VDR-U60-C096 | CAP-U60-06 | `website_blog/models/website_blog.py:168` | `_mail_post_access = 'read'` | FACT | Always | — | `_mail_post_access = 'read'` allows public posting of comments on blog posts | N-U60-011 |
| VDR-U60-C097 | CAP-U60-01 | `website/models/ir_ui_view.py:364-369` | def _get_cached_template_prefetched_keys(self) | FACT | Template cache | — | `website_id` context value added to template cache key to separate per-website caches | N-U60-001 |
| VDR-U60-C098 | CAP-U60-08 | `website_crm_iap_reveal/models/crm_reveal_rule.py:235-244` | months_valid = self.env['ir.config_param | FACT | Cron | — | Leads created within `reveal.lead_month_valid` months (default 6) suppress new reveal views for same IP | N-U60-014 |
| VDR-U60-C099 | CAP-U60-04 | `website/models/website_menu.py:43` | `page_id = fields.Many2one('website.page', 'Related Page', ondelete='cascade', index='btree_not_null')` | FACT | Always | — | `page_id` M2O with cascade delete and partial index on menu | N-U60-009 |
| VDR-U60-C100 | CAP-U60-04 | `website/models/website_menu.py:44` | `controller_page_id = fields.Many2one('website.controller.page', 'Related Model Page', ondelete='cascade', index='btree_not_null')` | FACT | Always | — | `controller_page_id` M2O linking menu to model-based controller page | N-U60-009 |
| VDR-U60-C101 | CAP-U60-02 | `website/models/website_visitor.py:92-103` | def _compute_partner_id(self) | FACT | Always | — | `partner_id` computed from token: if not 32-char hex, token is interpreted as integer partner ID | N-U60-005 |
| VDR-U60-C102 | CAP-U60-06 | `website_blog/models/website_blog.py:206-213` | @api.depends('content', 'teaser_manual') | FACT | Always | — | Auto-teaser is first 200 plain-text chars of content with ellipsis; overridden by `teaser_manual` | N-U60-011 |
| VDR-U60-C103 | CAP-U60-10 | `website_crm_partner_assign/models/res_partner.py:40-50` | @api.depends('implemented_partner_ids.is | FACT | Always | — | Published customer count computed per partner for partner locator ranking | N-U60-016 |
| VDR-U60-C104 | CAP-U60-05 | `website/controllers/form.py:239-246` | if request.env['ir.config_parameter'].sudo | FACT | When ICP set | — | Metadata (IP, User-Agent, Accept-Language, Referer) captured when `website_form_enable_metadata` ICP set | N-U60-010 |
| VDR-U60-C105 | CAP-U60-12 | `website_customer/models/res_partner.py:39` | def _default_is_published(self) | FACT | On create | — | Partner tags are published by default | N-U60-018 |
