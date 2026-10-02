# U61 — website portal bridge modules: forum, recruitment, livechat, slides, payment, project, timesheet (restricted technical evidence)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

- Unit: U61
- Modules: website_forum, website_google_map, website_hr_recruitment, website_hr_recruitment_livechat, website_links, website_livechat, website_mail, website_partner, website_payment, website_profile, website_project, website_slides, website_slides_forum, website_sms, website_timesheet
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope notes: Full study for all bridge modules. Source evidence only; RT flags for runtime unknowns.

---

## CAP-U61-01 — Forum: public Q&A with karma-gated participation

### D1 — Model identity
`ForumForum` (`forum.forum`) inherits `mail.thread`, `image.mixin`, `website.seo.metadata`, `website.multi.mixin`, `website.searchable.mixin`. It stores a `mode` field with selections `questions` (one answer) and `discussions` (multiple answers). A `privacy` field gates visibility to `public`, `connected`, or `private` groups.

### D2 — Karma generation fields (forum.forum)
Fifteen karma-generation integer fields exist on the forum record: `karma_gen_question_new` (default 2), `karma_gen_question_upvote` (default 5), `karma_gen_question_downvote` (default -2), `karma_gen_answer_upvote` (default 10), `karma_gen_answer_downvote` (default -2), `karma_gen_answer_accept` (default 2), `karma_gen_answer_accepted` (default 15), `karma_gen_answer_flagged` (default -100).

### D3 — Karma threshold fields (forum.forum)
Thresholds gate actions: `karma_ask` (default 3), `karma_answer` (default 3), `karma_edit_own` (1) / `karma_edit_all` (300), `karma_close_own` (100) / `karma_close_all` (500), `karma_unlink_own` (500) / `karma_unlink_all` (1000), `karma_tag_create` (30), `karma_upvote` (5), `karma_downvote` (50), `karma_flag` (500), `karma_moderate` (1000), `karma_editor` (30), `karma_post` (100).

### D4 — ForumPost model
`ForumPost` (`forum.post`) inherits `mail.thread`, `website.seo.metadata`, `website.searchable.mixin`. State selection: `active`, `pending`, `close`, `offensive`, `flagged`. `parent_id` links answers to questions; `is_correct` marks accepted answers. `vote_count` stored computed field derived from `forum.post.vote` records.

### D5 — Vote enforcement
`ForumPostVote` (`forum.post.vote`) enforces a unique constraint `(post_id, user_id)`. On `create`, karma rights are checked via `_check_karma_rights`; an `AccessError` is raised if `karma_upvote` or `karma_downvote` threshold is not met. Vote values: `'1'`, `'-1'`, `'0'`. A user cannot vote on their own post.

### D6 — Post creation karma enforcement
In `ForumPost.create`, if `not post.can_ask` an `AccessError` is raised with `karma_ask` threshold. If `not post.can_answer`, `AccessError` with `karma_answer`. If user lacks `karma_post`, post state is set to `'pending'` automatically via `post.sudo().state = 'pending'`.

### D7 — Forum tag karma gate
`ForumTag.create` checks `self.env.user.karma < forum.karma_tag_create` and raises `AccessError` with the threshold value. Unique constraint on `(name, forum_id)`.

### D8 — Post karma rights computed field
`_compute_post_karma_rights` computes 19 boolean can_* fields per post per user: `can_ask`, `can_answer`, `can_accept`, `can_edit`, `can_close`, `can_unlink`, `can_upvote`, `can_downvote`, `can_comment`, `can_comment_convert`, `can_view`, `can_post`, `can_flag`, `can_moderate`, `can_use_full_editor`. These are `compute_sudo=False`, so they reflect the current user.

### D9 — Relevancy scoring
`relevancy` stored computed field uses formula: `math.copysign(1, vote_count) * (abs(vote_count-1) ** relevancy_post_vote / (days+2) ** relevancy_time_decay)`. Default parameters: `relevancy_post_vote=0.8`, `relevancy_time_decay=1.8`.

### D10 — Forum website search integration
`Website._search_get_details` delegates to `forum.forum._search_get_detail`, `forum.post._search_get_detail`, and `forum.tag._search_get_detail` for search types `forums`, `forums_only`, `forum_posts_only`, `forum_tags_only`, `all`.

---

## CAP-U61-02 — Google Maps: partner/company location widget

### D1 — Controller
`GoogleMap` controller at route `/google_map` renders an iframe-embeddable map page. Accepts `partner_ids` (comma-separated) or `dom` query parameters. Filters `is_company=True` and `website_published=True`. Default limit 80 partners.

### D2 — Google Maps API key
The controller reads `request.website.google_maps_api_key` and passes it to the template `website_google_map.google_map`. Key is stored on the `website` model.

### D3 — Partner URL routing
If `'customers'` is in the `partner_url` parameter, the redirect base is `/customers/`; otherwise `/partners/`. Partner data serialised as JSON via `scriptsafe.dumps`.

---

## CAP-U61-03 — HR Recruitment: public job listing and online application

### D1 — HrJob website publishing
`HrJob` inherits `website.seo.metadata`, `website.published.multi.mixin`, `website.searchable.mixin`. Field `website_published` (Boolean) gates public visibility. `_compute_published_date` stores `published_date` when set to True. `website_url` computed as `/jobs/{slug}`.

### D2 — Job website description fields
`description` (Html, translatable), `website_description` (Html, translatable), `job_details` (Html). `job_details` has a default HTML template showing "Time to Answer", "Process", and "Days to get an Offer" info blocks.

### D3 — Job set_open and archive
`set_open` calls `self.write({'website_published': False})` before calling `super()`. `action_archive` sets `website_published=False` on active records before archiving.

### D4 — Recruitment controller /jobs route
`WebsiteHrRecruitment.jobs` handles routes `/jobs` and `/jobs/page/<int:page>`. Accepts filters: `country_id`, `department_id`, `office_id`, `contract_type_id`, `is_remote`, `is_other_department`, `contract_type_id`, `industry_id`, `is_industry_untyped`. `_jobs_per_page = 12`.

### D5 — HrApplicant website form filter
`HrApplicant.website_form_input_filter` validates the `job_id` is active (raises `UserError` if not), then finds the first non-folded recruitment stage matching the job and sets `stage_id`.

### D6 — UTM tracker URL on recruitment source
`HrRecruitmentSource._compute_url` computes a UTM-tagged URL combining the job's website URL with `utm_campaign`, `utm_medium`, and `utm_source` parameters.

### D7 — HrDepartment sudo display
`HrDepartment` overrides `display_name` with `compute_sudo=True` to allow portal users to read department names without direct model access.

### D8 — Website search integration
`Website._search_get_details` delegates to `hr.job._search_get_detail` for `search_type in ['jobs', 'all']`.

---

## CAP-U61-04 — HR Recruitment Livechat: chatbot for recruitment flow

### D1 — Module dependency
`website_hr_recruitment_livechat` depends on `website_hr_recruitment` and `im_livechat`. No Python models defined. A demo chatbot XML is provided for guiding visitors through the recruitment process.

---

## CAP-U61-05 — Website Links: short-link tracking and UTM

### D1 — LinkTracker website override
`LinkTracker` (inheriting `link.tracker`) overrides `_compute_short_url_host` to use the current website's base URL when a website context is active. Falls back to company base URL.

### D2 — Short URL statistics action
`action_visit_page_statistics` returns an `ir.actions.act_url` that opens `{short_url}+` in a new tab to show click statistics.

### D3 — Controller: create short link
Route `/website_links/new` (jsonrpc, auth=user, POST) calls `request.env['link.tracker'].search_or_create([post])`. Returns empty URL error if `url` is absent.

### D4 — Controller: statistics page
Route `/r/<string:code>+` (auth=user, website=True) renders `website_links.graphs` template with the tracker's read data. Redirects to `/` with 301 if code not found.

### D5 — Controller: recent links
Route `/website_links/recent_links` (jsonrpc, auth=user) calls `link.tracker.recent_links(filter, limit)`.

### D6 — Controller: add custom code
Route `/website_links/add_code` (jsonrpc, auth=user) searches for an existing `link.tracker.code` by `init_code`, then creates a new code entry if the `new_code` does not already exist for that tracker.

---

## CAP-U61-06 — Website Livechat: live chat widget and visitor tracking

### D1 — Website channel link
`Website` model gains `channel_id` field (`Many2one` to `im_livechat.channel`). Method `_get_livechat_channel_info` returns livechat info dict for the website's assigned channel, using `sudo()`.

### D2 — Visitor link to discuss channel
`WebsiteVisitor` gains `livechat_operator_id` (stored computed, `res.partner`), `discuss_channel_ids` (One2many to `discuss.channel`), and `session_count` (computed from channels with messages).

### D3 — Chat request from operator
`action_send_chat_request` creates a `discuss.channel` with `is_pending_chat_request=True` and links it to `livechat_visitor_id`. Raises `UserError` if the visitor is already in an active chat or no `channel_id` is configured for the website.

### D4 — Discuss channel visitor data
`DiscussChannel` gains `is_pending_chat_request` (Boolean) and `livechat_visitor_id` (`Many2one` to `website.visitor`). `channel_pin(pinned=False)` deletes empty livechat channels automatically.

### D5 — Guest name from visitor
`WebsiteLivechat` controller overrides `_get_guest_name` to return `'Visitor #%d' % visitor_sudo.id` when a website visitor is found.

### D6 — im_livechat channel create from website
`Im_LivechatChannel.create` with context `create_from_website=True` sets `website.channel_id` to the new channel and creates a rule using the `welcome_bot` chatbot if available.

### D7 — Chatbot test action
`ChatbotScript.action_test_script` returns `ir.actions.act_url` to `/chatbot/{id}/test`.

### D8 — WebsitePage cache post-processing
`WebsitePage._post_process_response_from_cache` calls `request.website._get_livechat_channel_info()` on every cached page response to inject livechat configuration.

### D9 — ir.http translation
`IrHttp._get_translation_frontend_modules_name` appends `'im_livechat'` so frontend translation strings are available for the chat widget.

### D10 — Config settings channel field
`ResConfigSettings` gains `channel_id` field related to `website_id.channel_id` (readable/writable) for website-level livechat configuration.

---

## CAP-U61-07 — Website Mail: email subscription (follow) management

### D1 — Follow/unfollow route
`/website_mail/follow` (jsonrpc, auth=public, website=True) subscribes or unsubscribes a partner to/from a record. Calls `record.sudo().message_subscribe(partner_ids)` or `message_unsubscribe`. For public users, verifies reCAPTCHA token before partner lookup.

### D2 — Follower check route
`/website_mail/is_follower` (jsonrpc, auth=public, readonly=True) accepts a dict of `{model: [res_ids]}` and returns a list of `res_ids` for which the current user (or session partner) is a follower.

### D3 — ir.http translation
`IrHttp._get_translation_frontend_modules_name` appends `'mail'` so mail module frontend strings are available.

### D4 — Publisher warranty flag
`Publisher_WarrantyContract._get_message` sets `msg['website'] = True` in the diagnostic message payload.

---

## CAP-U61-08 — Website Partner: public partner directory

### D1 — ResPartner website fields
`ResPartner` inherits `website.seo.metadata`. Gains `website_description` (Html, `strip_style=True`, translatable), `website_short_description` (Text, translatable), `is_published` (Boolean, tracking=True).

### D2 — Partner website URL
`_compute_website_url` sets `partner.website_url = "/partners/%s" % ir_http._slug(partner)`.

### D3 — Partner publish tracking
`_track_subtype` returns `website_partner.mt_partner_published` or `website_partner.mt_partner_unpublished` subtypes based on `is_published` change.

### D4 — Partner detail controller
Route `/partners/<partner_id>` (auth=public, website=True): resolves slug, checks `website_published` or editor group, redirects on slug mismatch, renders `website_partner.partner_page`.

---

## CAP-U61-09 — Website Payment: multi-website provider and donation

### D1 — PaymentProvider website_id field
`PaymentProvider` gains `website_id` (`Many2one` to `website`, `check_company=True`, `ondelete='restrict'`). `copy()` override preserves `website_id` only when company hierarchy matches.

### D2 — Compatible provider filtering
`_get_compatible_providers` override filters to providers where `not p.website_id or p.website_id.id == website_id`. Reports excluded providers with reason `incompatible_website`.

### D3 — Base URL from request
`PaymentProvider.get_base_url` returns `iri_to_uri(request.httprequest.url_root)` when a request is active, enabling correct URLs for multi-website.

### D4 — PaymentTransaction donation fields
`PaymentTransaction` gains `is_donation` (Boolean). `_post_process` sends a donation email and logs payment details when `state == 'done'` and `is_donation`.

### D5 — Donation email method
`_send_donation_email` renders template `website_payment.donation_mail_body` via `ir.qweb`, encapsulates with `mail.mail_notification_light`, and creates a `mail.mail` record.

### D6 — AccountPayment donation relay
`AccountPayment` gains `is_donation` related to `payment_transaction_id.is_donation`.

### D7 — Portal controller website-aware override
`PaymentPortal.payment_pay` overrides to pass `website_id=request.website.id` to `super()`. `payment_method` also passes `website_id`.

### D8 — Donation pay route
Route `/donation/pay` (http, GET/POST, auth=public, website=True) calls `self.payment_pay(**kwargs)` with `is_donation=True`. POST stores session values; GET reads them back with defaults (`amount=25.0`, `currency_id` from company).

### D9 — Donation transaction route
Route `/donation/transaction/<minimum_amount>` (jsonrpc, auth=public) validates `amount >= minimum_amount`, handles public partner details (name, email, country required), creates transaction with `is_donation=True`, sends internal notification email.

### D10 — Supported payment methods snippet endpoint
Route `/website_payment/snippet/supported_payment_methods` (http, GET, auth=public) returns payment brands and primary-without-brands methods. Cache-Control: `public, max-age=604800, stale-while-revalidate=86400` for public users.

### D11 — ResConfigSettings website domain filter
`_get_active_providers_domain` overrides to add `['|', ('website_id', '=', False), ('website_id', '=', self.website_id.id)]` to provider domain.

---

## CAP-U61-10 — Website Profile: karma-based public user profile

### D1 — Website karma_profile_min
`Website` gains `karma_profile_min` (Integer, default 150). Profile visibility for other users is gated by this threshold.

### D2 — ResUsers SELF fields
`SELF_READABLE_FIELDS` extended with `'karma'`. `SELF_WRITEABLE_FIELDS` extended with `'country_id'`, `'city'`, `'website'`, `'website_description'`, `'website_published'`.

### D3 — Profile token generation
`_generate_profile_token` creates a SHA-256 hash of `(today_date, profile_uuid, user_id, email)`. The `profile_uuid` is stored in `ir.config_parameter` as `website_profile.uuid`.

### D4 — Profile email validation
`_send_profile_validation_email` sends a `website_profile.validation_email` template with token URL. `_process_profile_validation_token` verifies token and grants `VALIDATION_KARMA_GAIN = 3` karma to users with 0 karma.

### D5 — Avatar access check
`_check_avatar_access` returns True only when the user's `website_published` is True and `karma > 0`.

### D6 — Profile access check
`_check_user_profile_access` allows own profile always. Denies if `not user_sudo.website_published` with message "This profile is private!". Denies if `request.env.user.karma < request.website.karma_profile_min` with message about insufficient karma.

### D7 — GamificationBadge published
`GamificationBadge` inherits `website.published.mixin`, making badges publishable on the website.

---

## CAP-U61-11 — Website Project: task submission portal

### D1 — ProjectTask website fields
`ProjectTask` gains `partner_name` (Char, related `partner_id.name`, stored, writable) and `partner_company_name` (Char, related `partner_id.company_name`, stored, writable). Both have `tracking=False`.

### D2 — WebsiteForm insert_record
When `model_name == 'project.task'`, the form controller looks up the website visitor's `partner_id` and sets it on the task. Sets `values.setdefault('user_ids', False)` to avoid OdooBot assignment.

### D3 — WebsiteForm extract_data partner lookup
For `project.task` with `email_from`: looks up partner via `_partner_find_from_emails_single`. If found, sets `partner_id` and moves `partner_name`/`partner_phone`/`partner_company_name` to custom. If not found, sets `email_cc` and preserves contact fields.

### D4 — WebsitePage cache bypass
`WebsitePage._allow_to_use_cache` returns `False` for path `/your-task-has-been-submitted` to prevent caching the confirmation page.

---

## CAP-U61-12 — Website Slides (eLearning): courses, slides, quizzes, enrollment

### D1 — SlideChannel model identity
`SlideChannel` (`slide.channel`) inherits `rating.mixin`, `mail.activity.mixin`, `image.mixin`, `website.cover_properties.mixin`, `website.seo.metadata`, `website.published.multi.mixin`, `website.searchable.mixin`. Description: "Course".

### D2 — Channel type
`channel_type` selection: `training` (default) or `documentation`.

### D3 — Enroll policy
`enroll` selection: `public` (Open) or `invite` (On Invitation). `enroll_group_ids` (`Many2many` to `res.groups`) auto-enrols group members.

### D4 — Visibility field
`visibility` selection: `public`, `connected`, `members`, `link`. Affects who can see the course and content.

### D5 — Membership statuses
`slide_channel_partner.member_status` selection: `invited`, `joined`, `ongoing`, `completed`. `completion` (Integer, avg aggregator) tracks percentage.

### D6 — Prerequisite courses
`prerequisite_channel_ids` (`Many2many` self-referential) requires completing listed courses before accessing this one. Domain constrains to same visibility and website_published state.

### D7 — Karma fields on channel
`karma_gen_channel_rank` (default 5), `karma_gen_channel_finish` (default 10). Action rights: `karma_review` (10), `karma_slide_comment` (3), `karma_slide_vote` (3).

### D8 — SlideSlide model
`SlideSlide` (`slide.slide`) inherits `mail.thread`, `image.mixin`, `website.seo.metadata`, `website.published.mixin`, `website.searchable.mixin`. `slide_category` selection: `infographic`, `article`, `document`, `video`, `quiz`. `source_type`: `local_file` or `external` (Google Drive).

### D9 — Slide content types
`slide_type` computed stored field with values: `image`, `article`, `quiz`, `pdf`, `sheet`, `doc`, `slides`, `youtube_video`, `google_drive_video`, `vimeo_video`.

### D10 — YouTube/Vimeo/Google Drive regex
Static regex constants on `SlideSlide`: `YOUTUBE_VIDEO_ID_REGEX`, `GOOGLE_DRIVE_DOCUMENT_ID_REGEX`, `VIMEO_VIDEO_ID_REGEX` for URL parsing.

### D11 — Quiz fields on slide
`question_ids` (One2many to `slide.question`). Reward fields: `quiz_first_attempt_reward` (10), `quiz_second_attempt_reward` (7), `quiz_third_attempt_reward` (5), `quiz_fourth_attempt_reward` (2).

### D12 — SlideQuestion model
`slide.question` with `question` (Char, required, translatable), `answer_ids` (One2many to `slide.answer`). Constraint: at least one correct and one incorrect answer. Statistics: `attempts_count`, `attempts_avg`, `done_count` (officer-only).

### D13 — SlideAnswer model
`slide.answer` with `text_value` (Char, required), `is_correct` (Boolean), `comment` (Text, shown to user on selection).

### D14 — SlideEmbed tracking
`SlideEmbed` (`slide.embed`) tracks third-party website embedding. Fields: `slide_id`, `url`, `count_views` (default 1). Description: "Embedded Slides View Counter".

### D15 — SlideChannelPartner invitation link
`_compute_invitation_link` builds URL `{base_url}/slides/{channel_id}/invite?invite_partner_id={partner_id}&invite_hash={hash}`.

### D16 — SlideSlidePartner completion recompute
On `create` or `write` when `completed` changes, `_recompute_completion` updates the channel partner's completion percentage. Vote constraint: `CHECK(vote IN (-1, 0, 1))`.

### D17 — ResUsers auto-enrol on group change
`ResUsers.create` and `write` search for channels with `enroll_group_ids` matching the user's groups and call `_action_add_members`. This handles group-based automatic enrollment.

### D18 — Website Google App Key
`Website.website_slide_google_app_key` field (Char, groups=`base.group_system`) stores the Google Docs API key for slide imports.

### D19 — Gamification challenge category
`GamificationChallenge.challenge_category` selection extended with `('slides', 'Website / Slides')`.

### D20 — Karma tracking origins
`GamificationKarmaTracking._get_origin_selection_values` adds `('slide.slide', 'Course Quiz')` and `('slide.channel', ...)` to the karma origin selection.

---

## CAP-U61-13 — Website Slides Forum: forum embedded within eLearning channel

### D1 — SlideChannel forum link
`SlideChannel` gains `forum_id` (`Many2one` to `forum.forum`, indexed, copy=False). Unique constraint `unique(forum_id)`. `forum_total_posts` related field.

### D2 — Forum visibility inheritance
`ForumForum` gains `slide_channel_ids` (One2many, inverse of `forum_id`) and `slide_channel_id` (computed stored first channel). `visibility` on forum is related to `slide_channel_id.visibility`.

### D3 — Forum image from course
`ForumForum._compute_image_1920` copies the channel image to the forum if no forum image is set.

### D4 — Forum privacy on channel write
When a channel's `forum_id` is changed: new forum's privacy is set to `False` (public). Old forum's privacy is set to `'private'` with `authorized_group_id` = slides officer group.

### D5 — Redirect to forum action
`SlideChannel.action_redirect_to_forum` returns a list-view action for `forum_post_action` filtered to `forum_id`.

### D6 — Slides forum controller
`WebsiteSlidesForum._prepare_user_profile_parameters` injects `forum_id` from the linked channel when a `channel_id` is present in the profile parameters.

---

## CAP-U61-14 — Website SMS: SMS contact action from visitor

### D1 — WebsiteVisitor SMS action
`WebsiteVisitor._check_for_sms_composer` returns `bool(self.partner_id.phone)`. `action_send_sms` raises `UserError` if no phone/mobile, otherwise opens `sms.composer` form with `default_res_model='res.partner'`, `default_composition_mode='comment'`, `default_number_field_name='phone'`.

---

## CAP-U61-15 — Website Timesheet: portal timesheet visibility gate

### D1 — _show_portal_timesheets method
`AccountAnalyticLine._show_portal_timesheets` searches `ir.ui.view` for key `hr_timesheet.portal_my_home_timesheet` (with `active_test=False`), calls `filter_duplicate()`, and returns whether the resulting view is `active`. RT: actual portal rendering depends on the timesheet module's portal views.

---

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U61-C001 | CAP-U61-01 | `website_forum/models/forum_forum.py:15` | `_name = 'forum.forum'` | FACT | Always | — | `forum.forum` model defined with name string 'Forum' | N-U61-001 |
| VDR-U61-C002 | CAP-U61-01 | `website_forum/models/forum_forum.py:17` | _name = 'forum.forum | FACT | Always | — | `forum.forum` inherits five mixins including multi-website and SEO | N-U61-001 |
| VDR-U61-C003 | CAP-U61-01 | `website_forum/models/forum_forum.py:53` | sequence = fields.Integer('Sequence', default=1) | FACT | Always | — | Forum mode selection: `questions` (one answer) vs `discussions` (multiple answers) | N-U61-002 |
| VDR-U61-C004 | CAP-U61-01 | `website_forum/models/forum_forum.py:59` | privacy = fields.Selection | FACT | Always | — | Forum privacy has three levels: public, connected (signed-in), private | N-U61-003 |
| VDR-U61-C005 | CAP-U61-01 | `website_forum/models/forum_forum.py:94` | total_favorites | FACT | Always | — | Creating a new question awards 2 karma points by default | N-U61-004 |
| VDR-U61-C006 | CAP-U61-01 | `website_forum/models/forum_forum.py:95` | count_posts_waiting_validation | FACT | Always | — | A question upvote awards 5 karma to the author by default | N-U61-004 |
| VDR-U61-C007 | CAP-U61-01 | `website_forum/models/forum_forum.py:98` | `karma_gen_answer_upvote = fields.Integer(string='Answer upvoted', default=10)` | FACT | Always | — | An answer upvote awards 10 karma by default | N-U61-004 |
| VDR-U61-C008 | CAP-U61-01 | `website_forum/models/forum_forum.py:102` | `karma_gen_answer_accepted = fields.Integer(string='Answer accepted', default=15)` | FACT | Always | — | Having an answer accepted awards 15 karma by default | N-U61-004 |
| VDR-U61-C009 | CAP-U61-01 | `website_forum/models/forum_forum.py:103` | `karma_gen_answer_flagged = fields.Integer(string='Answer flagged', default=-100)` | FACT | Always | — | Having an answer flagged deducts 100 karma by default | N-U61-004 |
| VDR-U61-C010 | CAP-U61-01 | `website_forum/models/forum_forum.py:105` | `karma_ask = fields.Integer(string='Ask questions', default=3)` | FACT | Always | — | Minimum 3 karma required to ask a question by default | N-U61-005 |
| VDR-U61-C011 | CAP-U61-01 | `website_forum/models/forum_forum.py:109` | `karma_edit_own = fields.Integer(string='Edit own posts', default=1)` | FACT | Always | — | 1 karma required to edit own posts; 300 for others | N-U61-005 |
| VDR-U61-C012 | CAP-U61-01 | `website_forum/models/forum_forum.py:125` | `karma_flag = fields.Integer(string='Flag a post as offensive', default=500)` | FACT | Always | — | 500 karma required to flag a post as offensive | N-U61-005 |
| VDR-U61-C013 | CAP-U61-01 | `website_forum/models/forum_forum.py:131` | `karma_moderate = fields.Integer(string='Moderate posts', default=1000)` | FACT | Always | — | 1000 karma required to moderate posts | N-U61-005 |
| VDR-U61-C014 | CAP-U61-01 | `website_forum/models/forum_post.py:16` | `_name = 'forum.post'` | FACT | Always | — | `forum.post` model with ordering `is_correct DESC, vote_count DESC, last_activity_date DESC` | N-U61-001 |
| VDR-U61-C015 | CAP-U61-01 | `website_forum/models/forum_post.py:38` | ('active', 'Active') | FACT | Always | — | Forum post has five states: active, pending, close, offensive, flagged | N-U61-006 |
| VDR-U61-C016 | CAP-U61-01 | `website_forum/models/forum_post.py:71` | `is_correct = fields.Boolean('Correct', help='Correct answer or answer accepted')` | FACT | Always | — | `is_correct` boolean marks an accepted/correct answer | N-U61-007 |
| VDR-U61-C017 | CAP-U61-01 | `website_forum/models/forum_post.py:183` | def _compute_relevancy(self) | FACT | post has create_date | — | Relevancy formula uses vote count and days since creation with two configurable exponent parameters | N-U61-008 |
| VDR-U61-C018 | CAP-U61-01 | `website_forum/models/forum_post.py:283` | LEFT JOIN res_users u ON p.create_uid = u.id | FACT | On create | — | Insufficient karma on ask raises `AccessError` with the threshold | N-U61-005 |
| VDR-U61-C019 | CAP-U61-01 | `website_forum/models/forum_post.py:289` | u.karma > 0 | FACT | On create | — | Posts below `karma_post` threshold are auto-set to `pending` state | N-U61-006 |
| VDR-U61-C020 | CAP-U61-01 | `website_forum/models/forum_post_vote.py:14` | `vote = fields.Selection([('1', '1'), ('-1', '-1'), ('0', '0')]` | FACT | Always | — | Vote values are strings: '1' (upvote), '-1' (downvote), '0' (retracted) | N-U61-009 |
| VDR-U61-C021 | CAP-U61-01 | `website_forum/models/forum_post_vote.py:22` | def _get_karma_value | FACT | Always | — | Database unique constraint prevents duplicate votes per user per post | N-U61-009 |
| VDR-U61-C022 | CAP-U61-01 | `website_forum/models/forum_post_vote.py:72` | vote._check_karma_rights(upvote) | FACT | On create/write | — | Voting on own post raises `UserError` | N-U61-009 |
| VDR-U61-C023 | CAP-U61-01 | `website_forum/models/forum_tag.py:28` | @api.depends("post_ids | FACT | Always | — | Tag names are unique per forum | N-U61-010 |
| VDR-U61-C024 | CAP-U61-01 | `website_forum/models/forum_tag.py:45` | raise AccessError | FACT | On create | — | Creating a tag requires `karma_tag_create` (default 30) karma | N-U61-005 |
| VDR-U61-C025 | CAP-U61-01 | `website_forum/models/res_users.py:14` | return self.mapped | FACT | Always | — | `website_forum` extends `res.users` to add a forum redirect to gamification data | N-U61-011 |
| VDR-U61-C026 | CAP-U61-01 | `website_forum/models/website.py:6` | class Website(models.Model) | FACT | Always | — | `website` model gains `forum_count` field tracking number of associated forums | N-U61-001 |
| VDR-U61-C027 | CAP-U61-01 | `website_forum/models/gamification_karma_tracking.py:9` | `return super()._get_origin_selection_values() + [('forum.post', self.env['ir.model']._get('forum.post').display_name)]` | FACT | Always | — | Karma tracking origin selection extended with `forum.post` as a source | N-U61-004 |
| VDR-U61-C028 | CAP-U61-02 | `website_google_map/controllers/main.py:32` | `@http.route(['/google_map'], type='http', auth="public", website=True, sitemap=False)` | FACT | Always | — | Route `/google_map` is public, website-aware, excluded from sitemap | N-U61-012 |
| VDR-U61-C029 | CAP-U61-02 | `website_google_map/controllers/main.py:35` | if post.get('partner_ids') | FACT | partner_ids param present | — | Google map filters to companies only when `partner_ids` param is provided | N-U61-012 |
| VDR-U61-C030 | CAP-U61-02 | `website_google_map/controllers/main.py:44` | `domain += [('website_published', '=', True)]` | FACT | domain not empty | — | Only `website_published=True` partners appear on the map | N-U61-012 |
| VDR-U61-C031 | CAP-U61-02 | `website_google_map/controllers/main.py:55` | for partner in partners.with_context | FACT | Always | — | Google Maps API key read from `request.website.google_maps_api_key` | N-U61-013 |
| VDR-U61-C032 | CAP-U61-03 | `website_hr_recruitment/models/hr_job.py:11` | _inherit = | FACT | Always | — | `hr.job` inherits website publishing and SEO mixins | N-U61-014 |
| VDR-U61-C033 | CAP-U61-03 | `website_hr_recruitment/models/hr_job.py:35` | `website_published = fields.Boolean(help='Set if the application is published on the website of the company.', tracking=True)` | FACT | Always | — | `website_published` Boolean with tracking logs publish/unpublish events | N-U61-014 |
| VDR-U61-C034 | CAP-U61-03 | `website_hr_recruitment/models/hr_job.py:54` | def _compute_full_url(self) | FACT | Always | — | `published_date` is set to today when `website_published` becomes True | N-U61-014 |
| VDR-U61-C035 | CAP-U61-03 | `website_hr_recruitment/models/hr_job.py:67` | else | FACT | Always | — | Job website URL pattern is `/jobs/<slug>` | N-U61-014 |
| VDR-U61-C036 | CAP-U61-03 | `website_hr_recruitment/models/hr_job.py:70` | def _compute_website_url(self) | FACT | Always | — | Re-opening a job position removes website publication | N-U61-014 |
| VDR-U61-C037 | CAP-U61-03 | `website_hr_recruitment/models/hr_applicant.py:13` | `def website_form_input_filter(self, request, values)` | FACT | On website form submission | — | Applicant form filter validates job is active and assigns first suitable recruitment stage | N-U61-015 |
| VDR-U61-C038 | CAP-U61-03 | `website_hr_recruitment/models/hr_recruitment_source.py:12` | `url = fields.Char(compute='_compute_url', string='Tracker URL')` | FACT | Always | — | Recruitment source computes a UTM-tagged tracking URL for each job/source combination | N-U61-016 |
| VDR-U61-C039 | CAP-U61-03 | `website_hr_recruitment/models/hr_department.py:8` | `display_name = fields.Char(compute_sudo=True)` | FACT | Always | — | Department `display_name` computed with sudo so portal users can read it | N-U61-017 |
| VDR-U61-C040 | CAP-U61-03 | `website_hr_recruitment/controllers/main.py:19` | `class WebsiteHrRecruitment(WebsiteForm):` | FACT | Always | — | Recruitment controller inherits `WebsiteForm` | N-U61-015 |
| VDR-U61-C041 | CAP-U61-03 | `website_hr_recruitment/controllers/main.py:21` | `_jobs_per_page = 12` | FACT | Always | — | Job listing page size is 12 per page | N-U61-014 |
| VDR-U61-C042 | CAP-U61-04 | `website_hr_recruitment_livechat/__manifest__.py:4` | 'summary': 'Chatbot for the HR Recruitment | FACT | Always | — | The recruitment livechat bridge module depends on `website_hr_recruitment` and `im_livechat` | N-U61-018 |
| VDR-U61-C043 | CAP-U61-05 | `website_links/models/link_tracker.py:14` | 'type': 'ir.actions.act_url | FACT | Always | — | Statistics URL is formed by appending `+` to the short URL | N-U61-019 |
| VDR-U61-C044 | CAP-U61-05 | `website_links/models/link_tracker.py:21` | `current_website = self.env['website'].get_current_website(fallback=False)` | FACT | Always | — | Short URL host uses current website's base URL when available | N-U61-019 |
| VDR-U61-C045 | CAP-U61-05 | `website_links/controller/main.py:9` | `@http.route('/website_links/new', type='jsonrpc', auth='user', methods=['POST'])` | FACT | Always | — | Short link creation endpoint is jsonrpc POST, requires authentication | N-U61-019 |
| VDR-U61-C046 | CAP-U61-05 | `website_links/controller/main.py:11` | if 'url' not in post or post['url'] == | FACT | On empty URL | — | Returns `{'error': 'empty_url'}` dict when no URL is provided | N-U61-019 |
| VDR-U61-C047 | CAP-U61-05 | `website_links/controller/main.py:24` | def add_code(self, **post) | FACT | Always | — | The `/r` route renders the link shortener page | N-U61-019 |
| VDR-U61-C048 | CAP-U61-05 | `website_links/controller/main.py:37` | `@http.route('/r/<string:code>+', type='http', auth="user", website=True)` | FACT | Always | — | Statistics for a short code are at `/r/<code>+` | N-U61-019 |
| VDR-U61-C049 | CAP-U61-06 | `website_livechat/models/website.py:10` | `channel_id = fields.Many2one('im_livechat.channel', string='Website Live Chat Channel')` | FACT | Always | — | `website` model gains a `channel_id` FK to `im_livechat.channel` | N-U61-020 |
| VDR-U61-C050 | CAP-U61-06 | `website_livechat/models/website_visitor.py:13` | `livechat_operator_id = fields.Many2one('res.partner', compute='_compute_livechat_operator_id', store=True, string='Speaking with', index='btree_not_null')` | FACT | Always | — | `website.visitor` gains stored computed field showing current livechat operator | N-U61-021 |
| VDR-U61-C051 | CAP-U61-06 | `website_livechat/models/website_visitor.py:15` | discuss_channel_ids | FACT | Always | — | Visitor has One2many to all their livechat discussion channels | N-U61-021 |
| VDR-U61-C052 | CAP-U61-06 | `website_livechat/models/website_visitor.py:46` | `def action_send_chat_request(self)` | FACT | Always | — | Operator-initiated chat request creates a `discuss.channel` with `is_pending_chat_request=True` | N-U61-022 |
| VDR-U61-C053 | CAP-U61-06 | `website_livechat/models/discuss_channel.py:10` | _inherit = 'discuss.channel | FACT | Always | — | `is_pending_chat_request` flag on discuss.channel tracks operator-initiated but unopened chats | N-U61-022 |
| VDR-U61-C054 | CAP-U61-06 | `website_livechat/models/discuss_channel.py:14` | `livechat_visitor_id = fields.Many2one('website.visitor', string='Visitor', index='btree_not_null')` | FACT | Always | — | `discuss.channel` links to the `website.visitor` via `livechat_visitor_id` | N-U61-022 |
| VDR-U61-C055 | CAP-U61-06 | `website_livechat/models/discuss_channel.py:22` | If active empty livechat channel | FACT | On channel_pin(False) | — | Unpinning an empty livechat channel automatically deletes it | N-U61-022 |
| VDR-U61-C056 | CAP-U61-06 | `website_livechat/models/im_livechat_channel.py:7` | _inherit = 'im_livechat.channel | FACT | Always | — | `im_livechat.channel` is extended to link visitor to the new discuss channel | N-U61-020 |
| VDR-U61-C057 | CAP-U61-06 | `website_livechat/models/im_livechat_channel.py:31` | operator_name = | FACT | context create_from_website=True | — | When created from website context, the first new channel is set as `website.channel_id` | N-U61-020 |
| VDR-U61-C058 | CAP-U61-06 | `website_livechat/models/website_page.py:11` | super()._post_process_response_from_cache | FACT | On cached page response | — | Livechat channel info is injected after every cached page response | N-U61-020 |
| VDR-U61-C059 | CAP-U61-06 | `website_livechat/models/res_config_settings.py:8` | _inherit = 'res.config.settings | FACT | Always | — | Settings form exposes the website's livechat channel as a writable field | N-U61-020 |
| VDR-U61-C060 | CAP-U61-06 | `website_livechat/controllers/main.py:10` | def _get_guest_name(self) | FACT | Always | — | Guest chat name is `'Visitor #N'` when a website visitor record exists | N-U61-021 |
| VDR-U61-C061 | CAP-U61-07 | `website_mail/controllers/main.py:9` | `@http.route(['/website_mail/follow'], type='jsonrpc', auth="public", website=True)` | FACT | Always | — | Follow/unfollow endpoint is public-accessible jsonrpc | N-U61-023 |
| VDR-U61-C062 | CAP-U61-07 | `website_mail/controllers/main.py:22` | if request.env.user != request.website.user_id | FACT | Public user follow | — | reCAPTCHA verification called for public-user follow subscriptions | N-U61-023 |
| VDR-U61-C063 | CAP-U61-07 | `website_mail/controllers/main.py:28` | except Exception | FACT | is_follower=True | — | Toggling follow when already following unsubscribes the partner | N-U61-023 |
| VDR-U61-C064 | CAP-U61-07 | `website_mail/controllers/main.py:35` | record.sudo().message_unsubscribe(partner_ids) | FACT | Always | — | Follower check endpoint is read-only public jsonrpc | N-U61-023 |
| VDR-U61-C065 | CAP-U61-08 | `website_partner/models/res_partner.py:9` | `_inherit = ['res.partner', 'website.seo.metadata']` | FACT | Always | — | `res.partner` inherits `website.seo.metadata` for SEO fields | N-U61-024 |
| VDR-U61-C066 | CAP-U61-08 | `website_partner/models/res_partner.py:10` | `website_description = fields.Html('Website Partner Full Description', strip_style=True, sanitize_overridable=True, translate=html_translate)` | FACT | Always | — | Partners gain a full HTML description field for the website, with style stripping | N-U61-024 |
| VDR-U61-C067 | CAP-U61-08 | `website_partner/models/res_partner.py:12` | `is_published = fields.Boolean(tracking=True)` | FACT | Always | — | Partner publication status has tracking=True for chatter logging | N-U61-024 |
| VDR-U61-C068 | CAP-U61-08 | `website_partner/models/res_partner.py:15` | def _compute_website_url(self) | FACT | Always | — | Partner URL pattern is `/partners/<slug>` | N-U61-024 |
| VDR-U61-C069 | CAP-U61-08 | `website_partner/controllers/main.py:8` | `@http.route(['/partners/<partner_id>'], type='http', auth="public", website=True)` | FACT | Always | — | Partner detail page route is public and website-aware | N-U61-024 |
| VDR-U61-C070 | CAP-U61-08 | `website_partner/controllers/main.py:17` | `if partner_sudo.exists() and (partner_sudo.website_published or is_website_restricted_editor)` | FACT | Always | — | Partner page accessible only if published or viewer is a restricted editor | N-U61-024 |
| VDR-U61-C071 | CAP-U61-09 | `website_payment/models/payment_provider.py:14` | website_id = fields.Many2one | FACT | Always | — | `payment.provider` gains `website_id` with company check and restrict-on-delete | N-U61-025 |
| VDR-U61-C072 | CAP-U61-09 | `website_payment/models/payment_provider.py:27` | one provided in the kwargs. | FACT | website_id provided | — | Compatible provider filter excludes providers set to a different website | N-U61-025 |
| VDR-U61-C073 | CAP-U61-09 | `website_payment/models/payment_provider.py:37` | if website_id | FACT | Request active | — | Provider base URL uses current HTTP request's URL root for multi-website correctness | N-U61-025 |
| VDR-U61-C074 | CAP-U61-09 | `website_payment/models/payment_transaction.py:11` | `is_donation = fields.Boolean(string="Is donation")` | FACT | Always | — | `payment.transaction` gains `is_donation` Boolean field | N-U61-026 |
| VDR-U61-C075 | CAP-U61-09 | `website_payment/models/payment_transaction.py:14` | super()._post_process() | FACT | On _post_process | — | Completed donation transactions trigger email send | N-U61-026 |
| VDR-U61-C076 | CAP-U61-09 | `website_payment/controllers/portal.py:20` | def donation_pay(self, **kwargs) | FACT | Always | — | Donation payment page is public, excluded from sitemap | N-U61-026 |
| VDR-U61-C077 | CAP-U61-09 | `website_payment/controllers/portal.py:36` | for key in ('amount | FACT | GET request | — | Default donation amount is 25.0 when not specified | N-U61-026 |
| VDR-U61-C078 | CAP-U61-09 | `website_payment/controllers/portal.py:54` | `@http.route('/donation/transaction/<minimum_amount>', type='jsonrpc', auth='public', website=True, sitemap=False)` | FACT | Always | — | Donation transaction creation endpoint enforces a minimum amount | N-U61-026 |
| VDR-U61-C079 | CAP-U61-09 | `website_payment/controllers/portal.py:56` | if float(amount) < float(minimum_amount) | FACT | amount < minimum | — | `ValidationError` raised if donation amount is below configured minimum | N-U61-026 |
| VDR-U61-C080 | CAP-U61-09 | `website_payment/controllers/portal.py:113` | if is_donation | FACT | Always | — | Supported payment methods endpoint for display on website snippets | N-U61-027 |
| VDR-U61-C081 | CAP-U61-09 | `website_payment/controllers/portal.py:148` | return rendering_context | FACT | Public/portal user | — | Payment methods list cached 7 days with 1-day stale-while-revalidate for public users | N-U61-027 |
| VDR-U61-C082 | CAP-U61-10 | `website_profile/models/website.py:7` | `karma_profile_min = fields.Integer(string="Minimal karma to see other user's profile", default=150)` | FACT | Always | — | Website stores minimum karma threshold (default 150) to view other users' profiles | N-U61-028 |
| VDR-U61-C083 | CAP-U61-10 | `website_profile/models/res_users.py:17` | `return super().SELF_READABLE_FIELDS + ['karma']` | FACT | Always | — | Users can read their own `karma` field value | N-U61-028 |
| VDR-U61-C084 | CAP-U61-10 | `website_profile/models/res_users.py:21` | @property | FACT | Always | — | Users can self-update profile fields including `website_published` and `website_description` | N-U61-028 |
| VDR-U61-C085 | CAP-U61-10 | `website_profile/models/res_users.py:26` | @api.model | FACT | Always | — | Email validation grants exactly 3 karma points to zero-karma users | N-U61-029 |
| VDR-U61-C086 | CAP-U61-10 | `website_profile/models/res_users.py:28` | def _generate_profile_token(self, user_id, email) | FACT | Always | — | Profile validation token uses a secret UUID stored in `ir.config_parameter` | N-U61-029 |
| VDR-U61-C087 | CAP-U61-10 | `website_profile/models/gamification_badge.py:4` | from odoo import models | FACT | Always | — | `gamification.badge` gains `website.published.mixin` making badges publishable | N-U61-030 |
| VDR-U61-C088 | CAP-U61-10 | `website_profile/controllers/main.py:40` | def _check_user_profile_access(self, user_id) | FACT | Always | — | Avatar visible publicly only if `website_published=True` and `karma > 0` | N-U61-028 |
| VDR-U61-C089 | CAP-U61-10 | `website_profile/controllers/main.py:49` | if user_sudo.id == request.env.user.id | FACT | Always | — | Unpublished user profile returns "This profile is private!" denial message | N-U61-028 |
| VDR-U61-C090 | CAP-U61-10 | `website_profile/controllers/main.py:53` | if not user_sudo.website_published | FACT | Always | — | Viewer below `karma_profile_min` receives karma-insufficient denial | N-U61-028 |
| VDR-U61-C091 | CAP-U61-11 | `website_project/models/project_task.py:5` | `partner_name = fields.Char(string='Customer Name', related="partner_id.name", store=True, readonly=False, tracking=False)` | FACT | Always | — | `project.task` gains `partner_name` stored-related field for website form use | N-U61-031 |
| VDR-U61-C092 | CAP-U61-11 | `website_project/controllers/main.py:15` | visitor_sudo = request.env['website.visi | FACT | project.task form submit | — | Website visitor's partner auto-fills `partner_id` on task creation | N-U61-031 |
| VDR-U61-C093 | CAP-U61-11 | `website_project/controllers/main.py:18` | `values.setdefault('user_ids', False)` | FACT | project.task form submit | — | `user_ids` defaulted to False to prevent OdooBot assignment | N-U61-031 |
| VDR-U61-C094 | CAP-U61-11 | `website_project/models/website_page.py:8` | @api.model | FACT | Always | — | Task submission confirmation page bypasses page cache | N-U61-031 |
| VDR-U61-C095 | CAP-U61-12 | `website_slides/models/slide_channel.py:18` | `_name = 'slide.channel'` | FACT | Always | — | `slide.channel` model (description: 'Course') inherits seven mixins including rating, mail.activity, image, cover_properties, SEO, published.multi, and searchable | N-U61-032 |
| VDR-U61-C096 | CAP-U61-12 | `website_slides/models/slide_channel.py:61` | name = fields.Char | FACT | Always | — | Course type is either `training` or `documentation` | N-U61-032 |
| VDR-U61-C097 | CAP-U61-12 | `website_slides/models/slide_channel.py:101` | total_slides = fields.Integer | FACT | Always | — | Enrol policy is `public` (open) or `invite` (invitation-only) | N-U61-033 |
| VDR-U61-C098 | CAP-U61-12 | `website_slides/models/slide_channel.py:107` | allow_comment = fields.Boolean | FACT | Always | — | Course visibility has four levels including link-based access | N-U61-033 |
| VDR-U61-C099 | CAP-U61-12 | `website_slides/models/slide_channel.py:134` | default=_get_default_enroll_msg | FACT | Always | — | Rating a course awards 5 karma by default | N-U61-034 |
| VDR-U61-C100 | CAP-U61-12 | `website_slides/models/slide_channel.py:135` | enroll_group_ids | FACT | Always | — | Completing a course awards 10 karma by default | N-U61-034 |
| VDR-U61-C101 | CAP-U61-12 | `website_slides/models/slide_channel_partner.py:12` | channel_id = fields.Many2one | FACT | Always | — | Course enrolment has four statuses: invited, joined, ongoing, completed | N-U61-033 |
| VDR-U61-C102 | CAP-U61-12 | `website_slides/models/slide_channel_partner.py:54` | self.next_slide_id = False | FACT | Always | — | Invitation link includes partner ID and a hash for secure access | N-U61-033 |
| VDR-U61-C103 | CAP-U61-12 | `website_slides/models/slide_slide.py:25` | `_name = 'slide.slide'` | FACT | Always | — | `slide.slide` model (description: 'Slides') inherits mail.thread, image.mixin, SEO, published, and searchable mixins | N-U61-035 |
| VDR-U61-C104 | CAP-U61-12 | `website_slides/models/slide_slide.py:41` | _order = 'sequence asc, is_category asc, id asc | FACT | Always | — | YouTube video ID regex is a class-level constant on `slide.slide` | N-U61-035 |
| VDR-U61-C105 | CAP-U61-12 | `website_slides/models/slide_slide.py:79` | quiz_first_attempt_reward | FACT | Always | — | Slide content category has five values: infographic, article, document, video, quiz | N-U61-035 |
| VDR-U61-C106 | CAP-U61-12 | `website_slides/models/slide_slide.py:97` | ('local_file', 'Upload from Device') | FACT | Always | — | Correct quiz on first attempt rewards 10 karma | N-U61-034 |
| VDR-U61-C107 | CAP-U61-12 | `website_slides/models/slide_question.py:15` | question = fields.Char | FACT | Always | — | `slide.question` model stores quiz questions with ordered answers | N-U61-036 |
| VDR-U61-C108 | CAP-U61-12 | `website_slides/models/slide_question.py:30` | if questions_to_fix | FACT | On constrains | — | At least one correct and one incorrect answer required per quiz question | N-U61-036 |
| VDR-U61-C109 | CAP-U61-12 | `website_slides/models/slide_embed.py:8` | `_name = 'slide.embed'` | FACT | Always | — | `slide.embed` model tracks third-party site embedding with `count_views` counter | N-U61-037 |
| VDR-U61-C110 | CAP-U61-12 | `website_slides/models/slide_slide_partner.py:18` | quiz_attempts_count | FACT | Always | — | Slide vote is constrained to -1, 0, or 1 at database level | N-U61-035 |
| VDR-U61-C111 | CAP-U61-12 | `website_slides/models/res_users.py:9` | @api.model_create_multi | FACT | On user create | — | New users are auto-enrolled in courses whose `enroll_group_ids` match the user's groups | N-U61-033 |
| VDR-U61-C112 | CAP-U61-12 | `website_slides/models/res_config_settings.py:7` | class ResConfigSettings(models.TransientModel) | FACT | Always | — | Config setting controls optional installation of `website_slides_forum` | N-U61-032 |
| VDR-U61-C113 | CAP-U61-12 | `website_slides/models/res_config_settings.py:8` | _inherit = "res.config.settings | FACT | Always | — | Config setting controls optional installation of certifications module | N-U61-032 |
| VDR-U61-C114 | CAP-U61-12 | `website_slides/models/website.py:8` | `website_slide_google_app_key = fields.Char('Google Doc Key', groups='base.group_system')` | FACT | Always | — | Google Docs API key stored on `website` model, accessible by system group only | N-U61-035 |
| VDR-U61-C115 | CAP-U61-13 | `website_slides_forum/models/slide_channel.py:8` | `forum_id = fields.Many2one('forum.forum', 'Course Forum', copy=False, index='btree_not_null')` | FACT | Always | — | `slide.channel` gains `forum_id` FK to `forum.forum` for embedded forum | N-U61-038 |
| VDR-U61-C116 | CAP-U61-13 | `website_slides_forum/models/slide_channel.py:12` | _forum_uniq = models.Constraint | FACT | Always | — | One-to-one unique constraint: a forum can be linked to at most one course | N-U61-038 |
| VDR-U61-C117 | CAP-U61-13 | `website_slides_forum/models/forum_forum.py:9` | slide_channel_ids | FACT | Always | — | `forum.forum` gains `slide_channel_ids` inverse relation to courses | N-U61-038 |
| VDR-U61-C118 | CAP-U61-13 | `website_slides_forum/models/forum_forum.py:12` | visibility = fields.Selection | FACT | Always | — | Forum visibility is inherited from the linked course's visibility setting | N-U61-038 |
| VDR-U61-C119 | CAP-U61-13 | `website_slides_forum/models/slide_channel.py:39` | if 'forum_id' in vals | FACT | On write | — | Assigning a forum to a course sets the forum's privacy to False (public) | N-U61-038 |
| VDR-U61-C120 | CAP-U61-13 | `website_slides_forum/models/slide_channel.py:41` | if old_forum != self.forum_id | FACT | On forum_id change | — | The old forum is set to private with slides officer access when unlinked | N-U61-038 |
| VDR-U61-C121 | CAP-U61-14 | `website_sms/models/website_visitor.py:10` | def _check_for_sms_composer(self) | FACT | Always | — | SMS send is blocked if visitor's partner has no phone number | N-U61-039 |
| VDR-U61-C122 | CAP-U61-14 | `website_sms/models/website_visitor.py:17` | def _prepare_sms_composer_context(self) | FACT | Always | — | SMS composer opens against the visitor's linked `res.partner` record using the `phone` field | N-U61-039 |
| VDR-U61-C123 | CAP-U61-14 | `website_sms/models/website_visitor.py:28` | raise UserError | FACT | Always | — | `action_send_sms` opens `sms.composer` form in a new dialog window | N-U61-039 |
| VDR-U61-C124 | CAP-U61-15 | `website_timesheet/models/account_analytic_line.py:6` | `def _show_portal_timesheets(self)` | FACT | Always | — | `_show_portal_timesheets` on `account.analytic.line` determines portal timesheet visibility | N-U61-040 |
| VDR-U61-C125 | CAP-U61-15 | `website_timesheet/models/account_analytic_line.py:9` | `domain = [("key", "=", "hr_timesheet.portal_my_home_timesheet")]` | FACT | Always | — | Portal timesheet visibility gated by the active status of view with key `hr_timesheet.portal_my_home_timesheet` | N-U61-040 |
| VDR-U61-C126 | CAP-U61-15 | `website_timesheet/models/account_analytic_line.py:10` | `return self.env["ir.ui.view"].sudo().with_context(active_test=False).search(domain).filter_duplicate().active` | FACT | Always | — | View search uses `active_test=False` and `filter_duplicate()` before checking `.active` | N-U61-040 |
| VDR-U61-C127 | CAP-U61-09 | `website_payment/controllers/payment.py:9` | `class PaymentPortal(account_payment.PaymentPortal)` | FACT | Always | — | `website_payment` controller inherits `account_payment.PaymentPortal` and overrides payment_pay and payment_method to pass `website_id` | N-U61-025 |
| VDR-U61-C128 | CAP-U61-03 | `website_hr_recruitment/models/hr_job.py:76` | job.website_url | FACT | Always | — | Archiving a job unpublishes it from the website before archiving | N-U61-014 |
| VDR-U61-C129 | CAP-U61-12 | `website_slides/models/slide_channel_tag.py:9` | class SlideChannelTagGroup(models.Model) | FACT | Always | — | `slide.channel.tag.group` inherits `website.published.mixin` for publication control | N-U61-032 |
| VDR-U61-C130 | CAP-U61-01 | `website_forum/models/forum_post.py:45` | `website_url = fields.Char('Website URL', compute='_compute_website_url')` | FACT | Always | — | Post URL computed as `/forum/<forum_slug>/<post_slug>` with `#answer_<id>` fragment for child posts | N-U61-007 |
