# U92 — Website Content Platform (L1/L2/L3)
**Unit**: U92
**Phase**: Second-Pass Depth Closure — P2 Supporting Domains
**Scope**: Blog, forum, slide channel models, access control, SEO, karma, certification
**Modules**: website_blog, website_forum, website_slides
**Function-IDs targeted**: NEW:U92-F01 through U92-F12
**L-levels**: L1, L2, L3
**Proof layers**: P1, P3
**Date**: 2026-10-02
**Status**: GATE-PASS
**Predecessor**: U19, U60

## Claims

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U92-001 | U92-F01 | website_blog/models/website_blog.py:14 | `_name = 'blog.blog'` | DEF | | | blog.blog model defined; inherits mail.thread, website.seo.metadata, website.multi.mixin, website.cover_properties.mixin | NR-U92-001 |
| U92-002 | U92-F01 | website_blog/models/website_blog.py:161 | `_name = 'blog.post'` | DEF | | | blog.post model defined; inherits mail.thread, website.seo.metadata, website.published.multi.mixin, website.cover_properties.mixin | NR-U92-002 |
| U92-003 | U92-F01 | website_blog/models/website_blog.py:188 | `tag_ids = fields.Many2many(` | SCHEMA | | | blog.post.tag_ids is Many2many to blog.tag | NR-U92-003 |
| U92-004 | U92-F01 | website_blog/models/website_blog.py:203 | `visits = fields.Integer(` | SCHEMA | | | blog.post.visits is Integer, readonly, default 0, copy=False | NR-U92-004 |
| U92-005 | U92-F01 | website_blog/models/website_blog.py:204 | `website_id = fields.Many2one(` | SCHEMA | | | blog.post.website_id is a related stored field derived from blog_id.website_id; no direct FK on post | NR-U92-005 |
| U92-006 | U92-F02 | website_blog/models/website_blog.py:317 | `default_opengraph']['og:desc` | FLOW | | | _default_website_meta sets og:type=article, article:published_time, article:modified_time, article:tag from tag_ids | NR-U92-006 |
| U92-007 | U92-F02 | website_blog/models/website_blog.py:348 | `has_group('website.group_web` | GUARD | C1 | | Website designers can filter posts by published/unpublished state; non-designers see only posts where post_date <= now | NR-U92-007 |
| U92-008 | U92-F03 | website_blog/models/website_blog.py:144 | `_name = 'blog.tag'` | DEF | | | blog.tag model; fields: name (translate, unique), category_id Many2one blog.tag.category, color Integer, post_ids Many2many blog.post | NR-U92-008 |
| U92-009 | U92-F03 | website_blog/models/website_blog.py:130 | `_name = 'blog.tag.category'` | DEF | | | blog.tag.category model; unique name constraint; tag_ids One2many | NR-U92-009 |
| U92-010 | U92-F04 | website_blog/models/website_blog.py:241 | `if vals.get('is_published'):` | TRIGGER | | | On write with is_published=True, _check_for_publication posts a mail message using subtype mt_blog_blog_published | NR-U92-010 |
| U92-011 | U92-F04 | website_blog/models/website_blog.py:263 | `'active' in vals and not vals` | GUARD | | | Archiving a blog post (active=False) forces is_published=False | NR-U92-011 |
| U92-012 | U92-F05 | website_forum/models/forum_post.py:17 | `_name = 'forum.post'` | DEF | | | forum.post model; inherits mail.thread, website.seo.metadata, website.searchable.mixin | NR-U92-012 |
| U92-013 | U92-F05 | website_forum/models/forum_post.py:36 | `state = fields.Selection(` | SCHEMA | | | forum.post.state Selection: active, pending, close, offensive, flagged | NR-U92-013 |
| U92-014 | U92-F05 | website_forum/models/forum_post.py:61 | `vote_ids = fields.One2many(` | SCHEMA | | | forum.post has One2many to forum.post.vote; computed vote_count stored Integer | NR-U92-014 |
| U92-015 | U92-F05 | website_forum/models/forum_post.py:72 | `parent_id = fields.Many2one(` | SCHEMA | | | forum.post.parent_id is self-referential Many2one (answers are children of questions); cascade delete | NR-U92-015 |
| U92-016 | U92-F06 | website_forum/models/forum_post_vote.py:7 | `_name = 'forum.post.vote'` | DEF | | | forum.post.vote model; fields: post_id, user_id, vote Selection '1'/'-1'/'0'; unique constraint on post_id+user_id | NR-U92-016 |
| U92-017 | U92-F06 | website_forum/models/forum_post_vote.py:43 | `def create(self, vals_list):` | GUARD | | | Vote create strips user_id/recipient_id for non-admin; _check_general_rights raises UserError on self-vote | NR-U92-017 |
| U92-018 | U92-F07 | website_forum/models/forum_post.py:254 | `post.can_ask = is_admin or` | CALC | C1 | | can_ask = is_admin OR user.karma >= forum.karma_ask (default 3) | NR-U92-018 |
| U92-019 | U92-F07 | website_forum/models/forum_post.py:260 | `post.can_upvote = is_admin` | CALC | C1 | | can_upvote = is_admin OR karma >= forum.karma_upvote OR existing vote is -1; can_downvote symmetric | NR-U92-019 |
| U92-020 | U92-F07 | website_forum/models/forum_post.py:264 | `post.can_view = post.can_clo` | CALC | C1 | | can_view = can_close OR (post active AND creator karma > 0 OR creator is current user) | NR-U92-020 |
| U92-021 | U92-F08 | website_forum/models/forum_forum.py:98 | `karma_gen_question_new = fie` | CONFIG | | | Forum karma generation defaults: question_new=2, q_upvote=5, q_downvote=-2, ans_upvote=10, ans_downvote=-2, ans_accept=2, ans_accepted=15, ans_flagged=-100 | NR-U92-021 |
| U92-022 | U92-F08 | website_forum/models/forum_forum.py:107 | `karma_ask = fields.Integer(` | CONFIG | | | Forum karma action thresholds (defaults): ask=3, answer=3, edit_own=1, edit_all=300, close_own=100, close_all=500, unlink_own=500, unlink_all=1000, upvote=5, downvote=50, post=100, moderate=1000 | NR-U92-022 |
| U92-023 | U92-F08 | website_forum/models/forum_post.py:330 | `not post.parent_id and not p` | GUARD | C1 | | New question created by user below karma_post threshold is automatically set to state=pending | NR-U92-023 |
| U92-024 | U92-F09 | website_slides/models/slide_channel.py:19 | `_name = 'slide.channel'` | DEF | | | slide.channel model (description=Course); inherits rating.mixin, mail.activity.mixin, image.mixin, website.published.multi.mixin | NR-U92-024 |
| U92-025 | U92-F09 | website_slides/models/slide_channel.py:66 | `channel_type = fields.Select` | SCHEMA | | | slide.channel.channel_type Selection: training/documentation, default=training | NR-U92-025 |
| U92-026 | U92-F09 | website_slides/models/slide_channel.py:127 | `enroll = fields.Selection([` | SCHEMA | | | slide.channel.enroll Selection: public/invite, default=public; computed to invite when visibility=members | NR-U92-026 |
| U92-027 | U92-F09 | website_slides/models/slide_channel.py:136 | `visibility = fields.Selectio` | SCHEMA | | | slide.channel.visibility Selection: public/connected/members/link, default=public | NR-U92-027 |
| U92-028 | U92-F09 | website_slides/models/slide_channel.py:203 | `CHECK(visibility != 'members` | GUARD | | | DB constraint: visibility=members requires enroll=invite | NR-U92-028 |
| U92-029 | U92-F10 | website_slides/models/slide_slide.py:24 | `_name = 'slide.slide'` | DEF | | | slide.slide model; inherits mail.thread, image.mixin, website.seo.metadata, website.published.mixin | NR-U92-029 |
| U92-030 | U92-F10 | website_slides/models/slide_slide.py:88 | `slide_category = fields.Sele` | SCHEMA | | | slide.slide.slide_category Selection: infographic/article/document/video/quiz | NR-U92-030 |
| U92-031 | U92-F10 | website_slides/models/slide_slide.py:57 | `is_preview = fields.Boolean(` | SCHEMA | | | slide.is_preview=True grants public access to the individual slide regardless of channel enrollment | NR-U92-031 |
| U92-032 | U92-F11 | website_slides/models/slide_channel.py:214 | `channel.is_visible = (` | CALC | C1 | | is_visible = visibility==public OR is_member OR (not public user AND visibility==connected) | NR-U92-032 |
| U92-033 | U92-F11 | website_slides/models/slide_channel.py:386 | `def _compute_can_publish(sel` | GUARD | C1 | | can_publish requires can_upload AND (user is channel responsible OR slides_manager group) | NR-U92-033 |
| U92-034 | U92-F12 | website_slides/models/slide_channel_partner.py:13 | `member_status = fields.Selec` | SCHEMA | | | slide.channel.partner.member_status Selection: invited/joined/ongoing/completed | NR-U92-034 |
| U92-035 | U92-F12 | website_slides/models/slide_channel.py:183 | `karma_gen_channel_finish = f` | CONFIG | | | slide.channel karma generation on completion: karma_gen_channel_rank=5, karma_gen_channel_finish=10 | NR-U92-035 |
| U92-036 | U92-F12 | website_slides/models/slide_slide.py:79 | `quiz_first_attempt_reward =` | CONFIG | | | Quiz attempt karma rewards: first=10, second=7, third=5, subsequent=2 | NR-U92-036 |
