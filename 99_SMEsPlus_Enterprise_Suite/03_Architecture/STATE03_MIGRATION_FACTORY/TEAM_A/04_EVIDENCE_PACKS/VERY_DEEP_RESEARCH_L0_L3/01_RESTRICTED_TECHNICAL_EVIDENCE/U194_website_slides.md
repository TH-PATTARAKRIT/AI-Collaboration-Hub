# U194 — website_slides: eLearning Slide Channel, Course Enrollment, Completion Tracking
**Depth:** L3 | **Group:** G12/G14 | **Priority:** P2
**Source:** `odoo/addons/website_slides/` + `odoo/addons/website_slides_survey/`
**Date:** 2026-10-02

---

## 1. Module Identity

| Item | Value |
|------|-------|
| Technical name | `website_slides` |
| Human name | eLearning |
| Version | 2.7 |
| Core dependencies | `portal_rating`, `website`, `website_mail`, `website_profile` |
| Certification extension | `website_slides_survey` (separate addon) |
| Application flag | True |
| License | LGPL-3 |

---

## 2. `slide.channel` — Course Container Model

**File:** `models/slide_channel.py`, class `SlideChannel`

**Mixins inherited:**
- `rating.mixin` — star ratings and reviews
- `mail.activity.mixin` — activity tracking
- `image.mixin` — cover images
- `website.cover_properties.mixin` — header gradient/background
- `website.seo.metadata` — SEO title/description/keywords
- `website.published.multi.mixin` — per-website publish state + `website_id` field
- `website.searchable.mixin` — website search integration

### 2.1 Channel Type

```python
channel_type = fields.Selection([
    ('training', 'Training'),
    ('documentation', 'Documentation')],
    default="training", required=True)
```

- **training**: interactive learning; only `user_id` (Responsible) can publish slides
- **documentation**: resource/guide repository; `allow_comment` auto-set to False; any member of `upload_group_ids` can upload

Note: `channel_type='certification'` does NOT exist in the base module. Certification is a `slide_category` on individual slides, added by `website_slides_survey`.

### 2.2 Visibility

```python
visibility = fields.Selection([
    ('public', 'Everyone'),
    ('connected', 'Signed In'),
    ('members', 'Course Attendees'),
    ('link', 'Anyone with the link'),
], default='public', required=True)
```

- `public`: visible to all (logged-in or not)
- `connected`: visible only to authenticated users
- `members`: visible only to enrolled attendees (forces `enroll='invite'`)
- `link`: visible to anyone holding the access_token URL

SQL constraint enforces: `visibility='members'` requires `enroll='invite'`.

### 2.3 Enroll Policy

```python
enroll = fields.Selection([
    ('public', 'Open'),
    ('invite', 'On Invitation')],
    default='public', required=True)
```

- `public`: any user can self-enroll
- `invite`: access only via invitation or officer/manager action

### 2.4 Membership Counts (computed)

| Field | Meaning |
|-------|---------|
| `members_invited_count` | Status = 'invited' |
| `members_engaged_count` | Status = 'joined' + 'ongoing' |
| `members_completed_count` | Status = 'completed' |
| `members_all_count` | invited + engaged + completed |
| `members_count` | engaged + completed (active members) |

### 2.5 Karma Generation Fields

```python
karma_gen_channel_rank = fields.Integer(default=5)    # awarded when user posts a review
karma_gen_channel_finish = fields.Integer(default=10) # awarded on course completion
```

Karma threshold fields (minimum karma required):
```python
karma_review = fields.Integer(default=10)
karma_slide_comment = fields.Integer(default=3)
karma_slide_vote = fields.Integer(default=3)
```

### 2.6 Prerequisite System

```python
prerequisite_channel_ids = fields.Many2many('slide.channel', ...)
```
- Courses can require completion of other courses before enrollment
- `prerequisite_user_has_completed` computed per-user context

### 2.7 Multi-website Scope

`slide.channel` inherits `website.published.multi.mixin`. The `website_id` field is inherited from this mixin. `slide.slide.website_id` is a related field pointing to `channel_id.website_id`. Channels are thus scoped to one website (or all websites if `website_id` is empty). No custom multi-website filtering beyond what the mixin provides.

---

## 3. `slide.slide` — Individual Lesson/Content Model

**File:** `models/slide_slide.py`, class `SlideSlide`

### 3.1 Slide Category (content type)

```python
slide_category = fields.Selection([
    ('infographic', 'Image'),
    ('article', 'Article'),
    ('document', 'Document'),
    ('video', 'Video'),
    ('quiz', 'Quiz')],
    default='document', required=True)
```

`website_slides_survey` adds: `('certification', 'Certification')`

### 3.2 Slide Type (subtype, computed/stored)

```python
slide_type = fields.Selection([
    ('image', 'Image'),
    ('article', 'Article'),
    ('quiz', 'Quiz'),
    ('pdf', 'PDF'),
    ('sheet', 'Sheet (Excel, Google Sheet, ...)'),
    ('doc', 'Document (Word, Google Doc, ...)'),
    ('slides', 'Slides (PowerPoint, Google Slides, ...)'),
    ('youtube_video', 'YouTube Video'),
    ('google_drive_video', 'Google Drive Video'),
    ('vimeo_video', 'Vimeo Video')],
    compute='_compute_slide_type', store=True, readonly=False)
```

`website_slides_survey` adds: `('certification', 'Certification')`

`slide_type` is computed from `slide_category` + `source_type` + URL analysis. Videos are subclassified by source (YouTube/Google Drive/Vimeo); documents by file type (PDF/sheet/doc/presentation).

### 3.3 Completion Time

```python
completion_time = fields.Float('Duration', digits=(10, 4),
    compute='_compute_category_completion_time', recursive=True,
    readonly=False, store=True)
```

Stored float representing duration in hours. Summed across slides for channel statistics (`total_time` on `slide.channel`).

### 3.4 Can-Complete Logic

```python
can_self_mark_completed = ...  # computed; False for quiz slides (must finish quiz)
can_self_mark_uncompleted = ...  # computed; True if published and is_member
```

Logic: slides without `question_ids` (not quiz) and not `slide_category='quiz'` can be manually marked completed. Quiz slides require completing the quiz to auto-complete. Certification slides (`website_slides_survey`) cannot be manually marked at all.

### 3.5 Quiz Karma Rewards

```python
quiz_first_attempt_reward = fields.Integer(default=10)
quiz_second_attempt_reward = fields.Integer(default=7)
quiz_third_attempt_reward = fields.Integer(default=5)
quiz_fourth_attempt_reward = fields.Integer(default=2)  # also used for attempts 5+
```

Karma is awarded via `_action_set_quiz_done()` → `_add_karma()`.

---

## 4. `slide.channel.partner` — Course Enrollment Record

**File:** `models/slide_channel_partner.py`, class `SlideChannelPartner`

### 4.1 Fields

| Field | Type | Notes |
|-------|------|-------|
| `channel_id` | Many2one → slide.channel | required, cascade delete |
| `partner_id` | Many2one → res.partner | required, cascade delete |
| `member_status` | Selection | invited/joined/ongoing/completed |
| `completion` | Integer (0–100) | % completed, avg aggregator |
| `completed_slides_count` | Integer | count of completed published slides |
| `active` | Boolean | False = left/removed from course |
| `invitation_link` | Char computed | HMAC-signed URL for invite emails |
| `last_invitation_date` | Datetime | used by GC to expire stale invites |
| `next_slide_id` | Many2one computed | next incomplete slide (SQL query) |

Unique constraint: `(channel_id, partner_id)`. Completion check: `0 <= completion <= 100`.

### 4.2 Member Status Flow

```
(invited) → joined (self-enrolls or officer enrolls)
joined → ongoing (completes first slide)
ongoing → completed (completes last slide: completed_slides >= total_slides)
completed → joined/ongoing (if a slide is unpublished, reducing total)
```

Status is set in `_recompute_completion()`.

### 4.3 `_recompute_completion()` — Completion Algorithm

```python
completed_slides_count = count(slide.slide.partner WHERE completed=True
                                AND slide.is_published=True AND slide.active=True
                                AND channel_id=self.channel_id AND partner_id=self.partner_id)

completion = round(100.0 * completed_slides_count / (channel.total_slides or 1))

# Status transitions:
if completion == 100: member_status = 'completed'
elif completion == 0: member_status = 'joined'
else: member_status = 'ongoing'
```

On `completed → True` transition: fires `_post_completion_update_hook(completed=True)` and `_send_completed_mail()`.
On `completed → False` (regression): fires `_post_completion_update_hook(completed=False)` removing karma.

### 4.4 Completion Email

`_send_completed_mail()` uses `channel.completed_template_id` (`mail_template_channel_completed`). Template rendered per record with `_generate_template()`, wrapped in `mail.mail_notification_light` layout.

### 4.5 Invitation Expiry (GC)

`@api.autovacuum` `_gc_slide_channel_partner()` removes `invited` records with 0 completion older than 3 months.

---

## 5. `_action_add_members()` — Enrollment Mechanism

**Location:** `slide_channel.py`, lines 694–758

Two operating modes controlled by `member_status` parameter:

**Mode 1: `member_status='joined'` (default — enrollment)**
1. Filters channels by enroll policy (`_filter_add_members`)
2. Unarchives existing inactive records → recomputes completion
3. Upgrades `invited` records to `joined` → recomputes completion
4. Creates new `slide.channel.partner` records for new partners
5. Subscribes all joined partners to channel chatter (subtype: `mt_channel_slide_published`)

**Mode 2: `member_status='invited'` (invitation only)**
1. Creates `slide.channel.partner` with `member_status='invited'`
2. Does NOT subscribe to chatter
3. Invited partner can access channel page but not slide content

`_filter_add_members()`: public channels allow all; invite channels require write access (officer/manager).

`_add_groups_members()`: auto-enrolls all users in `enroll_group_ids`.

**Leave/remove:** `_remove_membership()` archives `slide.channel.partner` records and unsubscribes from chatter. Karma gained during the course is retained.

---

## 6. `slide.slide.partner` — Per-Slide Completion Tracking

**File:** `models/slide_slide_partner.py`, class `SlideSlidePartner`

| Field | Type | Notes |
|-------|------|-------|
| `slide_id` | Many2one | cascade delete |
| `channel_id` | Many2one | stored via related, cascade delete |
| `partner_id` | Many2one | cascade delete |
| `completed` | Boolean | True = slide watched/done |
| `vote` | Integer (-1/0/1) | dislike/none/like |
| `quiz_attempts_count` | Integer | incremented each quiz attempt |

Unique constraint: `(slide_id, partner_id)`. Vote constraint: `vote IN (-1, 0, 1)`.

`_recompute_completion()` in this model triggers `slide.channel.partner._recompute_completion()` for matching channel/partner pairs — bridges per-slide completion to overall course completion.

On `create()`: if new record has `completed=True`, immediately triggers channel recompute.
On `write()`: if `completed` value changes, triggers channel recompute.

`website_slides_survey` adds:
- `user_input_ids` (One2many → survey.user_input) — certification attempts
- `survey_scoring_success` (computed Boolean) — True if any attempt scored success
- When `survey_scoring_success` → True, auto-sets `completed=True`

---

## 7. Gamification Integration

### 7.1 Course Finish Karma

`karma_gen_channel_finish` (default 10): awarded in `_post_completion_update_hook()`.
```python
self.env['res.users']._add_karma_batch({user: {'gain': karma, 'source': channel, 'reason': 'Course Finished'}})
```
Reversed (negative) if course becomes un-completed (e.g. slide unpublished).

### 7.2 Course Rank Karma

`karma_gen_channel_rank` (default 5): awarded in `message_post()` when a review comment with rating is posted.
```python
self.env.user._add_karma(self.karma_gen_channel_rank, self, _("Course Ranked"))
```

### 7.3 Quiz Karma (tiered rewards)

Awarded via `_action_set_quiz_done()` → `_add_karma()` on `res.users`.
Reward decreases per attempt: 10, 7, 5, 2 (default). Reversed on `mark_uncompleted`.

### 7.4 Action Karma Thresholds

`karma_review` (10), `karma_slide_comment` (3), `karma_slide_vote` (3): gating computed fields `can_review`, `can_comment`, `can_vote` on `slide.channel`. Officers/managers bypass karma gates via `can_publish`.

---

## 8. Certification (via `website_slides_survey`)

### 8.1 Certification Slide

`slide_category='certification'` added to `slide.slide` by `website_slides_survey`.
`survey_id = fields.Many2one('survey.survey', 'Certification', ...)` — required for certification slides (SQL constraint).

Cannot be manually marked as completed (`can_self_mark_completed=False`, `can_self_mark_uncompleted=False`).

`_generate_certification_url()`: creates or retrieves `survey.user_input` for the partner. Uses `invite_token` to distinguish enrollment pools (in case a partner re-enrolls after leaving).

### 8.2 Survey Channel Partner Extension

```python
survey_certification_success = fields.Boolean('Certified')  # on slide.channel.partner
```
Set to True when `slide.slide.partner.survey_scoring_success=True` for any certification slide in the channel.

`members_certified_count` on `slide.channel` counts partners with `survey_certification_success=True`.

### 8.3 Challenge/Badge Integration

`_ensure_challenge_category()` sets gamification challenge category to `'slides'` when a survey with a certification badge is linked to a slide (enables it to appear on the ranks/badges page).

---

## 9. Multi-website Channel Scope

`slide.channel` inherits `website.published.multi.mixin` (via `website.published.mixin` chain), which provides:
- `website_id = Many2one('website')` — scopes channel to a specific website (or all if None)
- `is_published` / `website_published` — per-website publication state
- `get_base_url()` — returns the website's domain

`slide.slide.website_id` is a `related` field pointing to `channel_id.website_id` (read-only). All slides in a channel inherit the same website scope.

`website.py` (`Website` model extension) registers a "Courses" suggested controller for the website `/slides` route and registers `slide.channel` + `slide.slide` in the website full-text search pipeline.

---

## 10. Access Control Summary

| Scenario | Enforced by |
|----------|------------|
| View channel listing | `visibility` + `is_visible` computed |
| Self-enroll | `enroll='public'` + `_action_add_members()` |
| Invite-only enroll | Officer/Manager via wizard → `_action_add_members()` |
| Auto-enroll (groups) | `enroll_group_ids` → `_add_groups_members()` |
| Upload slides | `upload_group_ids` or `user_id` or eLearning Manager group |
| Publish slides | `can_publish` = upload right + (responsible or Manager) |
| Post review | `karma >= karma_review` AND `is_member` |
| Post comment | `karma >= karma_slide_comment` AND `is_member` |
| Vote on slide | `karma >= karma_slide_vote` AND `is_member` |
| Access slide content | `is_member` OR `is_preview=True` on slide |

Security groups:
- `group_website_slides_officer` — can see attendance data, manage all courses
- `group_website_slides_manager` — extends officer; can publish any course, manage all

---

## 11. Key Computed Field: `completion` on `slide.channel`

```python
@api.depends('slide_partner_ids', ...)
@api.depends_context('uid')
def _compute_user_statistics(self):
    ...
    record.completion = 100.0 if completed else round(100.0 * completed_slides_count / (record.total_slides or 1))
```

This is a **per-user, non-stored** field on `slide.channel` showing the current user's progress. It reads from `slide.channel.partner` (which stores the `completion` integer persistently).

---

## 12. Relevant Database Tables

| Table | Description |
|-------|-------------|
| `slide_channel` | Course master record |
| `slide_slide` | Individual slides/lessons |
| `slide_channel_partner` | Enrollment join table (with completion %) |
| `slide_slide_partner` | Per-slide completion and vote data |
| `slide_channel_tag_rel` | Channel-to-tag many2many |
| `rel_upload_groups` | Channel-to-group many2many (upload rights) |
| `slide_channel_prerequisite_slide_channel_rel` | Prerequisite relationships |
| `survey_user_input` | Certification attempts (website_slides_survey) |
