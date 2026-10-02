# U117 — Digest Email: KPI Summary Emails and Scheduled Delivery
## Date: 2026-10-02
## Status: GATE-PENDING / DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

---

## What Is a Digest Email?

A digest email is a periodic summary report sent automatically to selected users. It combines key performance indicators (numbers that describe business health), helpful tips of the day, and links to related reports inside the application. The email is branded with the company name and colour scheme.

Each digest record has a name, a list of subscribers, a sending frequency, and a set of metrics to include. An administrator can create multiple digest configurations, each targeting different user groups with different selections of metrics.

---

## How Subscribers Are Managed

Users who are internal employees (not portal or external users) can subscribe to or unsubscribe from a digest. When subscribing, the user's account is added to the digest's subscriber list. When unsubscribing, they are removed.

New employees created in the system are automatically subscribed to the default digest if the administrator has enabled the "Digest Emails" setting in general configuration. This default digest is also configurable — the administrator selects which digest record serves as the default for new arrivals.

Each digest email contains an unsubscribe link. Clicking it removes the user from the subscriber list without requiring them to log in. A secure code is embedded in the link to prevent anyone other than the intended recipient from unsubscribing the user. Email clients that support one-click unsubscribe (via a special email header) can offer a button directly in the email interface.

---

## Sending Frequency and Scheduling

A digest can be configured to send daily, weekly, monthly, or quarterly. Each digest record stores the date of its next scheduled delivery. After each delivery, this date advances by the appropriate interval.

A background scheduled job (cron) runs once per day. It looks for all active digests whose scheduled delivery date is today or in the past and sends each one. The cron runs as the system administrator account so it can access all data regardless of record-level permissions.

If users on a digest's subscriber list have not logged in recently (within the digest's own interval), the system automatically reduces the sending frequency to avoid sending unwanted email to inactive users. For example, a daily digest may be automatically switched to weekly if none of its recipients have connected recently. A notification about this change is included in the email itself.

An ERP manager (administrator role) can manually change the sending frequency back at any time, either from inside the application or from a link in the email itself.

---

## How Metrics Are Added to a Digest

The digest system uses a well-defined extension pattern. The core digest module provides two built-in metrics: the count of users who connected to the system, and the total number of messages sent.

Other modules add their own metrics by extending the digest model. Each metric follows the same two-field pattern:

- A toggle field (a simple on/off checkbox) that the administrator uses to include or exclude the metric from a digest.
- A computed value field that calculates the actual number to display.

The name convention for these two fields is consistent: the toggle field begins with a short prefix, and the value field has the same name with a suffix indicating it holds the computed result. Custom metrics added via the Studio customisation tool follow the same naming convention and are automatically detected.

The following modules extend the digest with their own metrics:

- Sales management: total value of confirmed sales orders
- Customer relationship management: new leads created, opportunities won
- Accounting: total posted revenue from income accounts
- Project management: count of open tasks
- Recruitment: count of new employees added
- Point of sale: total sales value from completed transactions
- eCommerce: total sales value from orders originating on the website
- Live chat: percentage of satisfied customers, number of conversations handled, average time to answer

Each metric value field checks whether the current user has the appropriate access role. If the user lacks access, the metric is silently skipped rather than showing an error in the email.

---

## Three-Period Comparison Display

Every metric in the digest email is displayed across three time columns: the last 24 hours, the last 7 days, and the last 30 days. Each column shows the actual value for that period alongside a trend indicator (percentage change compared to the equivalent preceding period). An upward trend is highlighted in green; a downward trend in red; no change shows no indicator.

Time windows are computed relative to the company's working calendar timezone, ensuring the "last 24 hours" aligns with the business's local day rather than server time.

---

## Tip of the Day

Each digest email can include one or more tips — short educational hints about how to use the application. Tips are stored as separate records and are tracked per user: once a user has received a tip, it is not shown to them again. Tips can be restricted to specific user groups so that, for example, manager-level tips are only shown to managers.

---

## Metric Action Links

For metrics contributed by other modules, the digest email can include an "Open Report" button that takes the user directly to the relevant report inside the application. Each extending module registers the appropriate report action link alongside its metric definition.

---

## Email Delivery Mechanism

The digest email body is rendered from a QWeb template. The rendered content is then encapsulated in an outer layout template providing mobile-responsive styling. An outgoing mail record is created for each subscriber individually, marked for automatic deletion after sending.

The email subject combines the company name and the digest name. The sender address is the company's email address if configured, otherwise the current user's address, otherwise the system administrator's address.

---

## Administrator Preferences in the Email

For ERP managers who receive a digest, the email footer includes:

- A suggestion to switch from daily to weekly frequency if they prefer a broader overview (with a direct link to make the change).
- A link to the digest configuration form to customise which metrics are included.

If the system has automatically slowed down the digest due to inactivity, the footer explains this and names the new frequency.
