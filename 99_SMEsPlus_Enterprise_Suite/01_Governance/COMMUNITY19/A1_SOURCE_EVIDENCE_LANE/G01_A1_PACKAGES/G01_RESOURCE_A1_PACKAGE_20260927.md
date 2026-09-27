# G01 PLATFORM_BASE — RED TEAM A1 PACKAGE — Module `resource`

| Field | Value |
|---|---|
| Role | RED TEAM A1 (source-backed research synthesizer) |
| Group / Module | G01 PLATFORM_BASE / `resource` |
| Lane A input | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_RESOURCE_LANE_A_PASS1_20260927.md` |
| Lane A sha256 | `6148482c3278b841ef5fa5191c8fd9d3dd9b2c87244046d4f1fb6643cd8ceffd` |
| Anchor commit | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/resource/`) |
| Question gate | **MVQ bank absent — GMVQ backlog.** Standard 55 only, via W1-STD (freeze `c64693ee…`). No QID is answered and no question is invented. A1 proceeds. |
| Lane B dependency | None. A1 does not wait for Lane B. |
| Date | 2026-09-27 |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |
| Clean-room | Neutral WHAT/WHY/RISK only. No code, schema, ORM or workflow is reproduced or recommended for reuse. Identifiers are pointers only. |

## 1. Claims

Layer for every claim: SOURCE-STATIC. Paths are relative to `addons/resource/`. Blob = git SHA-1 (first 8 characters; full values in Section 10). `[SC]` = re-verified in the spot-check. `[A1+]` = an observation that A1 added during the spot-check, beyond the Lane A text.

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence (path @ blob) | Conf. |
|---|---|---|---|
| A1-G01-RSRC-C01 | WHAT: this module defines **no multi-company record rule on working calendars or on attendance slots**. Company rules exist only for resources and for leaves, and both admit records with no company. Calendar company scoping relies only on selection-domain filters. WHY: calendars are treated as reference data that can be shared. RISK: users may be able to read another company's calendars and their slots by record access. Whether `base` or another module adds a rule is not checked (G3). | `security/resource_security.xml` @ 500b70f0 [SC]; `models/resource_calendar.py` @ 335a8576 [SC] | HIGH (absence in this module); LOW (tenant-wide effect) |
| A1-G01-RSRC-C02 | WHAT: the resource entity is **read-only for both internal users and system administrators** in this module's ACL. No row grants create, write or delete. The mixin's create path in this module shows no privilege elevation. RISK: resource creation and maintenance depend on ACLs from other modules or on elevated contexts. Which module grants them is not identified (G2). | `security/ir.model.access.csv` @ 34ca64a5 [SC]; `models/resource_mixin.py` @ b68b6a9f [SC] | HIGH (ACL rows); UNKNOWN (grant source) |
| A1-G01-RSRC-C03 | WHAT: working calendars and attendance slots are read-only for internal users and fully editable only by system administrators. Leaves are fully granted to both groups at ACL level and then narrowed by record rules. | `security/ir.model.access.csv` @ 34ca64a5 [SC] | HIGH |
| A1-G01-RSRC-C04 | WHAT: on leaves, internal users may read company-wide leaves plus leaves whose resource has no linked user or is linked to themselves. They may create, write and delete resource-specific leaves whose resource has **no linked user** or is linked to themselves. Company-wide leaves can be modified only by the access-rights manager group. WHY: self-service time off. RISK: **any internal user can create, change or delete time off for resources with no linked user** (for example equipment, or people with no login). This can alter capacity and scheduling for everyone who depends on those resources. | `security/resource_security.xml` @ 500b70f0 [SC] | HIGH |
| A1-G01-RSRC-C05 | WHAT: the rule that keeps an attendance slot's end at or after its start, and within 0–24 hours, is applied **only by a form onchange**. No server-side constraint on hour order or hour range exists on the attendance entity. The only server constraint on that entity concerns the day period (the duration-based / break rule). RISK: imports, RPC or programmatic writes can store an inverted slot (end before start), a slot beyond 24 hours, or a negative one. The effect on duration totals and on the overlap check is unproven. | `models/resource_calendar_attendance.py` @ d8fb69b1 [SC] | HIGH (absence); LOW (downstream effect) |
| A1-G01-RSRC-C06 | WHAT: attendance overlap is checked on save for each weekday (each week separately in two-week mode). A very small offset lets back-to-back slots touch. Two-week calendars require every slot to sit under a week section. | `models/resource_calendar.py` @ 335a8576 [SC] | HIGH |
| A1-G01-RSRC-C07 | WHAT: the "plan hours" and "plan days" helpers search forward or backward in 14-day windows, at most 100 of them. If the target is not reached they return false and raise no error. [A1+] Both helpers ignore leaves unless the caller asks for them. RISK: on a sparse or empty calendar, a request gives up silently after about 1,400 days. Callers that do not handle a false result may fail or mis-schedule. A plan made without leaves can land on closing days. | `models/resource_calendar.py` @ 335a8576 [SC] | HIGH |
| A1-G01-RSRC-C08 | WHAT: the work-time rate is the calendar's weekly hours divided by the full-time reference hours. It falls back to the maximum value when there is no reference. The field help says the rate should be between 0 and 100 %, but no constraint or clamp enforces this. RISK: calendars above full time report a rate over the documented maximum. Consumers that assume the documented range may misreport. | `models/resource_calendar.py` @ 335a8576 [SC] | HIGH |
| A1-G01-RSRC-C09 | WHAT: interval computation generates naive slot times per day, then localizes them once for each distinct timezone among the requested resources. Resources are grouped by timezone, and the result is clipped to the requested window in each timezone. Leaf computations assert that the input is timezone-aware. Public count and unusual-day entry points assume that naive input is UTC. [A1+] A context-supplied employee timezone can override the timezone used for attendance intervals. RISK: naive input is read as UTC and not as local time, so a caller that passes local naive datetimes shifts its results. Around daylight-saving changes, results rely on the localization library, and DST edge behaviour is not proven. | `models/resource_calendar.py` @ 335a8576 [SC] | HIGH (mechanism); LOW (DST effect) |
| A1-G01-RSRC-C10 | WHAT: [A1+] the calendar's displayed timezone offset is computed from the **current** date, not from the date being scheduled. RISK: in daylight-saving zones, the offset shown for a future or past period may differ from the offset actually applied. This is a display-only concern (unverified in the UI). | `models/resource_calendar.py` @ 335a8576 [SC] | MED |
| A1-G01-RSRC-C11 | WHAT: leaves without a resource apply to every resource on the matching calendar, but only when the resource's company equals the leave's company. Leaves with a resource apply only to it. By default only leaves typed as "Time Off" reduce work time, and callers may pass a domain. | `models/resource_calendar.py` @ 335a8576 [SC] | HIGH |
| A1-G01-RSRC-C12 | WHAT: a leave's start must not be after its end (server validation). The leave's company is computed from its calendar, or else from the current company. | `models/resource_calendar_leaves.py` @ 841053e6 [SC] | HIGH |
| A1-G01-RSRC-C13 | WHAT: the resource efficiency factor must be strictly positive (database check). A resource with no calendar is treated as fully flexible, meaning available for the whole requested window. The calendar choice is limited to calendars of the resource's own company. | `models/resource_resource.py` @ aad3af2f [SC] | HIGH |
| A1-G01-RSRC-C14 | WHAT: week parity for two-week calendars comes from a day count since a fixed epoch, not from the ISO week number. RISK: the "first/second week" label may not match what users see as odd or even ISO weeks. | `models/resource_calendar_attendance.py` @ d8fb69b1 [SC] | HIGH |
| A1-G01-RSRC-C15 | WHAT: the mixin makes a resource mandatory on consuming records and restricts its deletion. [A1+] Searches through that link bypass access checks on the resource. RISK: filtering by resource attributes on consuming models is not narrowed by the resource's own record rules. | `models/resource_mixin.py` @ b68b6a9f [SC] | MED |
| A1-G01-RSRC-C16 | WHAT: every company gets a default calendar (install backfill, plus automatic creation for new companies), and a calendar in use as a company default cannot be deleted. | `data/resource_data.xml` @ ffe3cf9e; `models/res_company.py` @ 3ba30d24 | MED |
| A1-G01-RSRC-C17 | WHAT: the weekday-worked lookup is cached per calendar, and no invalidation was observed in the module files. RISK: the lookup could return stale results after a schedule change (unverified, G4). | `models/resource_calendar.py` @ 335a8576 | LOW |
| A1-G01-RSRC-C18 | WHAT: the timezone default chain is: calendar from context, then user, then admin user, then UTC. A resource takes its timezone from its linked user or else its calendar on create. When the admin sets a timezone before first login, it is copied to their calendar or the standard calendar. | `models/resource_calendar.py` @ 335a8576 [SC]; `models/res_users.py` @ ef4f8859 | MED |

## 2. Business rules
- BR1: Slots on the same weekday (and in the same week, for two-week mode) must not overlap. Touching end-to-start is allowed (C06).
- BR2: Duration-based calendars cannot contain break rows (server constraint on the day period).
- BR3: A leave must start at or before its end (C12).
- BR4: Resource efficiency must be greater than zero (C13).
- BR5: Company-wide leaves reduce work only for resources in the same company (C11).
- BR6: Only leaves typed as "Time Off" reduce work by default. "Other" leaves do not (C11).
- BR7: Averages exclude breaks and section rows, are halved in two-week mode, and are entered by hand for flexible calendars (Lane A #16).

## 3. States / transitions
- Calendar mode: one-week ↔ two-week. The switch rebuilds attendances, copying them into two weeks or resetting to the company default. Duration-based mode can be turned on and off.
- Calendar schedule type: fixed ↔ flexible (a stored flag).
- Records carry an active flag (archive/unarchive). There is no approval or state machine on leaves in this module.

## 4. Exceptions / failure modes
- Validation error: overlapping slots; a two-week slot with no section; leave start after end.
- User error: a break row in a duration-based calendar.
- Database rejection: efficiency ≤ 0.
- Blocked deletion: a calendar used as a company default; a resource linked from a mixin record.
- Silent: planning returns false after about 1,400 days (C07); an inverted slot stored through a non-form write (C05); a rate above the documented maximum (C08).
- Assertion failure when naive datetimes reach the internal interval methods directly (C09).

## 5. Cross-module handoffs
- Upstream: `base` (company, user, timezone list) and `web`.
- Downstream (from source comments only, not verified): contract modules override calendar validity; work-order duration uses the efficiency factor; planning/forecast uses unavailable intervals; `resource_mail` extends the resource (see its package).
- The mixin is the integration contract: consumers get an auto-created resource plus work-day and leave-day helpers.

## 6. Evidence gaps
- G1: Static JS and tests were not reviewed (Lane A scope).
- G2: The source of resource create/write/delete rights is unknown (C02).
- G3: A calendar multi-company rule from `base` or other modules was not checked (C01).
- G4: Cache invalidation for the weekday lookup is unverified (C17).
- G5: The `utils.py` helpers have no identified caller.
- G6 (A1): The effect of an inverted slot (C05) on the duration and overlap computations is unproven.
- G7 (A1): Interval results across daylight-saving transitions are unproven (C09).

## 7. CRQ candidates
- CRQ-RSRC-01: Confirm whether any installed module adds a company rule for calendars and attendances. If none, confirm that cross-company read is possible at runtime (C01).
- CRQ-RSRC-02: Identify which module(s) grant create/write/delete on resources, and under which group (C02).
- CRQ-RSRC-03: Confirm that a plain internal user can create, edit and delete leaves on a resource with no linked user (C04).
- CRQ-RSRC-04: Confirm that a non-form write can store an inverted or over-24h slot, and observe the resulting durations (C05).
- CRQ-RSRC-05: Confirm what callers do with the silent false result of the planning helpers (C07).
- CRQ-RSRC-06: Confirm that a calendar above full time shows a rate over the documented maximum, and how consumers render it (C08).
- CRQ-RSRC-07: Test work-hour counts across a daylight-saving boundary and with naive local input (C09, C10).
- CRQ-RSRC-08: Confirm cache staleness after a schedule edit (C17).

## 8. Contradictions
- CONFIRMED-FROM-SOURCE: the work-time rate help text states a 0–100 % range, but no enforcement exists and the computation can exceed the maximum (C08; spot-check #1).
- CANDIDATE: "Resources are managed" (implied by menus and actions for resources) vs a read-only ACL for all groups in this module (C02). This may be resolved by other modules.

## 9. Provenance
- The sole analytic input is the Lane A packet above (sha256 recorded). Spot-check source: `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/resource/<path>`, fetched 2026-09-27 into the session scratchpad and not committed.
- `[A1+]` items come only from those spot-checked files.

## 10. Spot-check log (8 files; `git hash-object` vs the Lane A blob)

| # | File | Recorded blob | Recomputed | Claim content checked | Result |
|---|---|---|---|---|---|
| 1 | `models/resource_calendar.py` | 335a857625070669ad79bd701fb38be03ec5704a | identical | rate formula, fallback and 0–100 % help with no bound; 14-day × 100 planning loops returning false; leaves off by default; tz grouping and localization; tz-aware asserts; naive→UTC in public entry points; overlap micro-offset; leave company match | MATCH |
| 2 | `models/resource_calendar_attendance.py` | d8fb69b117b5c395eedfc213a31e8480f4c79936 | identical | hour clamp/order only in onchange; sole constraint on day period; epoch-based parity | MATCH |
| 3 | `security/ir.model.access.csv` | 34ca64a5e94929feffacb29fae63b73e78a0b3c7 | identical | 8 rows; resource read-only for user and system; calendar/attendance read-only for users; leaves full | MATCH |
| 4 | `security/resource_security.xml` | 500b70f06c5fb917bd5657bbaaf23843920dae0c | identical | 5 rules; leave rules admit resources with no user; company rules only on resource and leaves | MATCH |
| 5 | `models/resource_calendar_leaves.py` | 841053e65b7f2ea6693f4fa18d3e98eb7e821fe4 | identical | start ≤ end constraint; computed company | MATCH |
| 6 | `models/resource_resource.py` | aad3af2f8b87bff4cc650819abc2856fdb826067 | identical | efficiency > 0 check; same-company calendar domain | MATCH |
| 7 | `models/resource_mixin.py` | b68b6a9fd53c7a54d29bd5765018202ee8e2e3f5 | identical | required, restrict-delete resource; no elevation in create; search-access bypass on link | MATCH |
| 8 | `__manifest__.py` | 72b99e4faad899e6631ba8d1d96698b9c7ff1e0f | identical | blob identity only | MATCH |

## 11. Limitations
- SOURCE-STATIC only. Source presence does not prove runtime reachability, and statements of absence cover only this module's files.
- There is no Formal Coverage claim and no percentages. A2, Lane B, Reconciliation and Proof are still pending.
- There is no module MVQ bank, so no QID mapping exists (GMVQ backlog).
- C16 and C17 rely on Lane A pointers and were not spot-checked for content.
