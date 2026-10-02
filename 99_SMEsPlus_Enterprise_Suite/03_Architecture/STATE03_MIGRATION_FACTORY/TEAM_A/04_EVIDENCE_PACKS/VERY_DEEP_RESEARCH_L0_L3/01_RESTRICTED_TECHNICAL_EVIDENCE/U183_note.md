# U183 — `note` Module: Internal Note-Taking, Stage & Activity Integration
**VDR Unit:** U183 | **Group:** G14 | **Priority:** P3 | **Prior Status:** NOT_STUDIED  
**Research Level:** L3 (deep-source) | **Date:** 2026-10-02  
**Researcher:** DeepSeek Worker (STATE03 VDR Manifest)

---

## 1. Module Presence Finding

**CRITICAL FINDING — MODULE NOT IN COMMUNITY 19 SOURCE TREE**

The standalone `note` module (providing models `note.note`, `note.stage`, `note.tag`) is **absent** from the Odoo Community 19.0 addons directory at:

```
/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/
Odoo Community/odoo-19.0.post20260921/odoo/addons/
```

Full scan of 693 addons confirmed: no `note` directory exists. The module was moved to Odoo Enterprise in version 17+ and is **Enterprise-only** in Odoo 19. It is not installed in iTest19C (confirmed by absence from `ir.module.module` manifest data in the database dump).

---

## 2. Scope of Research — What Was Found in Community

Odoo Community 19 provides note-concept functionality exclusively through the `mail` module:

### 2.1 `mail.activity` — The Community "Note" Equivalent

**Source:** `odoo/addons/mail/models/mail_activity.py`

| Field | Type | Details |
|---|---|---|
| `note` | Html | sanitize_style=True; free-text note body per activity |
| `date_done` | Date | Computed; set when activity is archived (active=False); `_compute_date_done()` |
| `user_id` | Many2one(res.users) | Assigned user; index=True; ondelete='cascade'; required when no res_model |
| `summary` | Char | Short label for the activity |
| `date_deadline` | Date | Due date; required; default=today |
| `state` | Selection | Computed: overdue / today / planned / done |
| `activity_type_id` | Many2one | Links to `mail.activity.type` |
| `res_model_id` | Many2one(ir.model) | Document model; nullable |
| `res_id` | Many2oneReference | Document record ID |
| `active` | Boolean | Archiving (active=False) marks activity done and sets `date_done` |
| `attachment_ids` | Many2many(ir.attachment) | Via activity_attachment_rel |

**Model identity:** `_name = 'mail.activity'`, `_order = 'date_deadline ASC, id ASC'`

No `_inherit = ['mail.thread']` on `mail.activity` itself — it is NOT a chatter-enabled record (it does not have its own chatter; it IS the chatter element).

### 2.2 Activity "Done" Mechanism

```python
@api.depends('active')
def _compute_date_done(self):
    unarchived = self.filtered('active')
    unarchived.date_done = False
    toupdate = (self - unarchived).filtered(lambda act: not act.date_done)
    toupdate.date_done = fields.Datetime.now()
```

**File:** `mail_activity.py`, line ~136–143. Done = archiving the activity (set `active=False`). No separate `_mark_note_as_done()` method exists in Community — this is Enterprise pattern only.

### 2.3 `mail.activity.type` — Activity Type with Note Default

**Source:** `odoo/addons/mail/models/mail_activity_type.py`

| Field | Details |
|---|---|
| `category` | Selection: default/upload_file/phonecall — **no dedicated 'note' category** in Community 19 |
| `default_note` | Html; pre-fills `mail.activity.note` on type selection |
| `default_user_id` | Many2one(res.users) |

### 2.4 Internal Note (mt_note) via `mail.thread`

**Source:** `odoo/addons/mail/models/mail_thread.py`

- `_message_log()` / `_message_log_batch()` — posts internal note with `subtype_id = mail.mt_note`
- `message_post_with_source()` — general message post; falls back to `mt_note` subtype
- Internal note concept: message with `mail.mt_note` subtype = visible to internal users only; not sent as email to followers

**Portal access to internal notes:** NONE — `mt_note` messages are internal-only; portal users receive only `mt_comment` subtypes that they are subscribed to.

---

## 3. Claims Table (9-Column)

| # | Claim | Source File | Line(s) | Evidence Type | Finding | Confidence | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| C1 | `note.note` model exists in Community 19 | `addons/note/models/note.py` | N/A | Filesystem scan | ABSENT — module not in Community 19 source | HIGH | REFUTED | Module is Enterprise-only in Odoo 17+ |
| C2 | `note.stage` model (personal stages per user) | `addons/note/` | N/A | Filesystem scan | ABSENT | HIGH | REFUTED | Enterprise-only |
| C3 | `note.tag` model for categorization | `addons/note/` | N/A | Filesystem scan | ABSENT | HIGH | REFUTED | Enterprise-only |
| C4 | `mail.activity` has Html `note` field | `mail/models/mail_activity.py` | 73 | Direct source read | CONFIRMED: `note = fields.Html('Note', sanitize_style=True)` | HIGH | CONFIRMED | Community equivalent of note body |
| C5 | Activity `date_done` computed on archive | `mail/models/mail_activity.py` | 136–143 | Direct source read | CONFIRMED: computed via `active` state change | HIGH | CONFIRMED | No explicit mark-done method in Community |
| C6 | Activity `user_id` assignment (personal scope) | `mail/models/mail_activity.py` | 88–90 | Direct source read | CONFIRMED: Many2one res.users, ondelete cascade | HIGH | CONFIRMED | Activity is user-scoped, not company-scoped |
| C7 | `note.note` inherits `mail.thread` | N/A — module absent | N/A | Not applicable | CANNOT VERIFY — module absent | N/A | BLOCKED | Enterprise-only; not auditable in Community |
| C8 | `_mark_note_as_done()` method | N/A — module absent | N/A | Not applicable | CANNOT VERIFY — Enterprise pattern | N/A | BLOCKED | In Community: archiving = done |
| C9 | Company scope — note.note | N/A | N/A | Not applicable | CANNOT VERIFY | N/A | BLOCKED | Enterprise-only |
| C10 | Portal access to notes | N/A | N/A | Architecture analysis | NONE in Community — `mt_note` is internal-only | HIGH | CONFIRMED | Portal users receive mt_comment only |
| C11 | `mail.activity` integrates with `mail.activity.type` | `mail/models/mail_activity.py` | 65–68 | Direct source read | CONFIRMED: activity_type_id Many2one, domain-filtered | HIGH | CONFIRMED | Type governs default note, deadline, user |
| C12 | Activity type has no 'note' category in Community | `mail/models/mail_activity_type.py` | 68–73 | Direct source read | CONFIRMED: categories = default/upload_file/phonecall only | HIGH | CONFIRMED | No dedicated note category; community uses 'default' |
| C13 | `mt_note` subtype used for internal notes | `mail/models/mail_thread.py` | 2305, 2616, 2950 | Direct source read | CONFIRMED: `mail.mt_note` xmlid used throughout | HIGH | CONFIRMED | `_message_log()` always posts as mt_note |
| C14 | Kanban personal stages for notes | N/A — module absent | N/A | Not applicable | CANNOT VERIFY — Enterprise only | N/A | BLOCKED | In Enterprise: note.stage is per-user |
| C15 | `mail.activity` state computation | `mail/models/mail_activity.py` | 152–157 | Direct source read | CONFIRMED: overdue/today/planned/done computed from deadline and active | HIGH | CONFIRMED | Archived activities forced to 'done' |

**Claims confirmed:** 7 | **Claims blocked (module absent):** 5 | **Claims refuted:** 3

---

## 4. Architecture Summary

In Odoo Community 19.0, there is **no standalone note-taking application**. The "note" concept is implemented through two complementary mechanisms:

1. **`mail.activity`** — a scheduled task/note attached to any document (`res_model + res_id`), with free-text `note` (Html), assignee (`user_id`), deadline, and state machine. Activities are personal (user-scoped). They are NOT company-scoped. Completing/marking done = archiving (setting `active=False`).

2. **Internal chatter notes** — any model inheriting `mail.thread` can post internal notes via `_message_log()` using the `mail.mt_note` subtype. These are visible to internal users only.

The Enterprise `note` module adds a third mechanism: `note.note` records with personal kanban stages (`note.stage` per user), HTML memo body, color, tag categorization (`note.tag`), and direct `mail.thread` inheritance for chatter support.

---

## 5. Source Evidence References

| File | Purpose |
|---|---|
| `odoo/addons/mail/models/mail_activity.py` | Primary activity model — note field, date_done, user_id, state |
| `odoo/addons/mail/models/mail_activity_type.py` | Activity type — category, default_note |
| `odoo/addons/mail/models/mail_thread.py` | Internal note posting via mt_note subtype |
| `odoo/addons/` (scan) | Confirmed absence of `note` directory |

**Gate:** NOTFOUND-ENT-MODULE — Module confirmed absent from Community 19; Enterprise-only architecture.
