# U183 — Neutral Knowledge: Internal Note-Taking in Odoo 19 Community
**VDR Unit:** U183 | **Classification:** Neutral / Non-Code | **Date:** 2026-10-02

---

## What This Unit Covers

This unit addresses the "note" capability in Odoo 19 Community — specifically how internal note-taking, personal reminders, and activity annotation are structured. The standalone note application (personal sticky notes with kanban) is absent from the Community edition; this file documents what is available and what is not.

---

## Capability Map

### Available in Community 19

| Capability | Where It Lives | Who Can Use It |
|---|---|---|
| Activity notes (free-text attached to documents) | `mail.activity` | All internal users |
| Internal chatter messages (notes) | `mail.thread` (mt_note subtype) | All internal users; not visible to portal |
| Default note template per activity type | `mail.activity.type.default_note` | Configured by admin |
| Activity completion date tracking | `mail.activity.date_done` | Automatic on archive |
| Activity state visibility | Overdue / Today / Planned / Done | Per-user view |

### NOT Available in Community 19 (Enterprise-only)

| Capability | Enterprise Model | Notes |
|---|---|---|
| Personal sticky notes app | `note.note` | Full note-taking application with kanban |
| Personal kanban stages | `note.stage` | Stage is per-user (user_id field) |
| Note color coding | `note.note.color` | Integer color index |
| Note tag categorization | `note.tag` | Many2many tags on notes |
| Note "mark as done" | `note.note.date_done` | Date field set on completion |
| Note chatter (full mail.thread) | `note.note._inherit` | Enables followers, history on note records |

---

## Key Concepts in Plain Language

### Activity-Based Notes (Community)

In Community Odoo 19, the closest equivalent to a personal note is a **scheduled activity** on a document. An activity is created on any record (invoice, contact, task, etc.), has a due date, can be assigned to a user, and carries a free-text note body. When the user finishes the activity, they mark it done (which archives it), and the completion date is recorded.

Activities are **personal** — each activity is assigned to one user, and that user sees it in their activity list. There are no shared "sticky notes" that float independently of documents.

### Internal Chatter Notes (Community)

Any document record that participates in the chatter system (most Odoo records do) can have internal notes posted to it. These notes use a special "note" message type that is visible only to internal users — portal users and external contacts do not see them. This is how teams leave private comments on orders, customers, or projects without those comments going to the customer.

### Why the Standalone Note App Is Enterprise

The standalone `note` module (visible as "Notes" in the Apps menu of Enterprise) gives users a personal notepad independent of any document — like digital sticky notes. Each note lives in a kanban board with personal stages. This feature requires `note.note`, `note.stage`, and `note.tag` models, which are not present in Community 19.

---

## Claims Mapping to Neutral Concepts

| # | Technical Claim (Restricted File) | Plain-Language Interpretation |
|---|---|---|
| C1 | note.note absent | No standalone note-taking app in Community 19 |
| C4 | mail.activity.note Html field | Activity records carry a free-text note body |
| C5 | date_done computed on archive | Completing an activity records when it was finished |
| C6 | user_id activity assignment | Activities are personal — one owner per activity |
| C10 | Portal cannot see mt_note | Customer-facing users never see internal notes |
| C11 | Activity type governs defaults | Admin can pre-configure default text per activity type |
| C12 | No 'note' category on activity type | Community activity types are: none / upload document / phonecall |
| C13 | mt_note subtype for internal messages | Chatter "Log note" button posts with this subtype |
| C15 | State computation from deadline | Activity urgency (overdue/today/planned) is calculated automatically |

---

## Migration Implication for SMEsPlus

If SMEsPlus 19 Community needs standalone personal notes equivalent to Odoo Enterprise's Notes app, this is a **feature gap** requiring either:
1. A clean-room Community module replicating `note.note` / `note.stage` / `note.tag` behavior
2. Acceptance that users manage notes through activities attached to documents

This gap is classified at **Enterprise-equivalent priority** — the feature is actively used in SME workflows (quick reminders, personal to-do items not tied to a specific document).

---

## Source Verification Status

- Module scanned: `odoo/addons/` — 693 modules, no `note` directory found
- Database iTest19C: no `note` module in `ir.module.module` installed list
- Mail module evidence: directly read from source files at lines cited in restricted file
