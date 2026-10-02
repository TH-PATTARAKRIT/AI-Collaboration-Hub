# U113 — Neutral Knowledge: Chatter + Activity System
## DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
## NOT GATE-PASS — NOT BOSS APPROVAL

---

## Overview

The messaging infrastructure in Odoo 19 Community consists of two tightly integrated systems: the Chatter (discussion thread on business documents) and the Activity system (structured to-do items with deadlines). Both share common notification routing infrastructure and the follower subscription mechanism.

---

## Activity Lifecycle

An Activity is a structured reminder or task attached to a business document. Each activity has a due date, an assigned user, a type classification, and an optional summary and note. Activities can be created manually by users, or created automatically by business rules and workflow logic.

When an activity is created and assigned to a different user, the system immediately notifies that user by email. The assignee is also subscribed as a follower of the related document so they receive future discussion updates.

The status of an activity (planned, due today, or overdue) is computed dynamically each time it is accessed, comparing the deadline to the current date in the assigned user's timezone. This means the same activity can shift from "planned" to "overdue" simply as days pass, without any data change.

When a user marks an activity as done, a completion message is posted to the document's discussion thread, the activity record is archived (not deleted), and an optional feedback comment is stored. Archived activities retain their deadline and completion date as historical record.

If an activity type is configured for automatic chaining, completing the current activity automatically creates the next one. If configured for suggestion, the system presents recommended follow-up activity types to the user without creating them automatically.

---

## Activity Type Configuration

Activity types define the category, icon, default deadline calculation, and chaining behavior. The deadline calculation uses a configurable delay (a number of days, weeks, or months) applied either from the completion date of the previous activity or from the previous activity's deadline. Types may be restricted to a specific document model or made available globally. Types can carry default email templates that are suggested when the activity is completed.

The "Todo" type is a protected system type used for reminders created from the top navigation bar. It cannot be archived or deleted.

---

## Reminder and Scheduled Action

Odoo 19 Community does not provide a dedicated activity reminder cron that proactively sends overdue reminders to users. Instead, the real-time notification mechanism uses the internal bus channel: when an activity is created, updated, or deleted, the assigned user's browser session receives an immediate count update event. This keeps the activity badge counter in the navigation bar current without requiring polling.

Email queue processing is handled by an hourly scheduled action that sends batches of up to 1000 queued outgoing emails at a time. Old read notifications are purged monthly by a garbage collection action that removes notifications older than six months for internal users.

---

## Notification Routing

When a chatter message is posted, the system first computes the set of recipients based on the message subtype and the follower subscription list. Each follower's subscription specifies which subtypes they want to receive. Followers who have the relevant subtype in their subscription receive notifications; others do not.

For each qualifying recipient, the system routes delivery through up to three channels simultaneously: inbox (a notification record visible in the Discuss application), email (an outgoing email record queued for the email scheduler), and web push (if the user has a registered push device). Channel selection per recipient is determined by user preference settings.

If a notification is scheduled for a future date, instead of dispatching immediately the system creates a schedule record that a daily cron processes later.

Inbox delivery creates a notification record and sends a real-time bus event to the user's browser session, allowing the Discuss inbox badge to update without page reload.

---

## Chatter Message Types

The chatter supports seven distinct message types that classify the origin and purpose of each message. User comments and email replies are the main interactive types. System-generated entries include tracking notifications (recording field value changes), automated targeted notifications (sent by business automation rules), out-of-office replies, and user-specific internal notifications.

Three core subtypes control follower filtering:
- Discussion: the standard public conversation type, visible to external contacts
- Note: an internal memo type, visible only to internal users
- Activities: an internal type used specifically for activity completion entries, also visible only to internal users

---

## Follower System

Any document inheriting the chatter mixin maintains a list of followers. Each follower record stores the partner identity and a per-follower list of message subtypes they have subscribed to. A unique constraint prevents a partner from following the same document twice.

The document creator is automatically subscribed as a follower when the record is created, unless the creation context suppresses auto-subscription. When an activity is assigned to a user, that user's partner is also automatically subscribed.

Field-based auto-subscription allows related partners (such as the customer on a sale order, or the project manager on a task) to be automatically followed when certain fields are populated.

Deleting a document removes all associated messages, follower records, and scheduled notifications in the same operation.

---

## Cross-Module Integration

The activity system integrates with any model that inherits the activity mixin. The chatter and notification infrastructure is used across the entire application — from sales leads to project tasks to purchase orders. The follower and subtype mechanism provides a unified subscription system shared by all modules.
