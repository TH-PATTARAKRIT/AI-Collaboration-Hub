# U191 — Gamification System: Neutral Knowledge Summary
**Unit:** U191 | Gamification — Challenge/Goal/Badge Award System
**Level:** L3 | Group: G14 | Priority: P3

---

## What the System Does

Odoo's gamification module lets administrators define measurable objectives (goals) and group them into timed competitions (challenges). When users meet their objectives, they receive digital recognition tokens (badges). The system automates progress tracking and reward distribution through a scheduled background process.

---

## Claims Table (9-column VDR Format)

| # | Claim | Source File | Lines | Evidence Type | Confidence | Neutral Reference | SMEsPlus Impact | Notes |
|---|---|---|---|---|---|---|---|---|
| C01 | A challenge defines its recurrence period from five options: non-recurring, daily, weekly, monthly, or yearly. The period controls how goal start and end dates are calculated each cycle. | `gamification_challenge.py` | 92–101 | Code field definition | HIGH | A competition can run once or repeat on a calendar cycle; the cycle governs when fresh objectives are created for participants. | Multi-period challenge support needed in migration | `period` Selection field; `start_end_date_for_period()` helper |
| C02 | A challenge can scope its participants either by an explicit list of users or by a domain expression that is re-evaluated on every update, automatically adding or removing users who match or no longer match. | `gamification_challenge.py` | 88–89, 319–328 | Code field + method | HIGH | Participant lists can be dynamic (role-based) rather than manually maintained, reducing admin overhead. | Domain-based enrollment must be preserved in migration | `user_domain` field; `_recompute_challenge_users()` |
| C03 | A challenge supports up to four badge rewards: one for all users who complete every goal, plus separate first-, second-, and third-place awards granted only at period end. | `gamification_challenge.py` | 112–117 | Code field definitions | HIGH | Multiple reward tiers within a single competition; top-rank badges are not granted in real time. | Four badge FK columns per challenge row | `reward_id`, `reward_first_id`, `reward_second_id`, `reward_third_id` |
| C04 | The "reward as soon as reached" flag causes the general completion badge to be granted immediately when a user finishes all goals, rather than waiting for the period to end. A duplicate-grant guard prevents the same badge from being awarded twice to the same user in the same challenge. | `gamification_challenge.py` | 117, 682–692 | Code field + conditional | HIGH | Real-time recognition vs. batch-end recognition is configurable; idempotency is enforced in code. | Real-time grant path must be replicated | `reward_realtime` Boolean; badge-user existence check |
| C05 | Each goal tracks the participant's current numeric score against a target, plus a completeness percentage. For objectives where a higher value is better, completeness is proportional. For objectives where a lower value is better, completeness is binary (0 or 100 percent). | `gamification_goal.py` | 77–89 | Computed field logic | HIGH | Two distinct comparison semantics for measuring progress; not a single linear scale. | Completeness calculation must respect condition direction | `_get_completion()`; `condition` field |
| C06 | Goal progress can be measured in four ways: manual entry by the user, automatic count of records matching a domain, automatic sum of a numeric field across matching records, or execution of custom Python code that produces a numeric result. | `gamification_goal_definition.py` | 25–31 | Selection field definition | HIGH | Four computation strategies with different runtime costs and maintenance implications. | All four modes need parity in target system | `computation_mode` Selection |
| C07 | The goal update engine only recomputes goals for users who have recently interacted with the web client (within the session lifetime), measured by a presence-tracking join. Inactive users are excluded from each update cycle to limit database load. | `gamification_challenge.py` | 276–292 | SQL query logic | HIGH | Performance optimisation: goal updates are gated by user activity, not run unconditionally for all participants. | Presence-join dependency on `mail.presence` table | `_update_all()` method; `mail_presence` join |
| C08 | Badges carry a granting-permission rule with four levels: anyone, a named list of users, users who already hold prerequisite badges, or nobody (challenge-only). A separate monthly sending cap can also apply. | `gamification_badge.py` | 34–50, 197–218 | Field definitions + method | HIGH | Peer-to-peer badge gifting is permission-controlled; challenge-only badges cannot be sent manually. | Badge permission rules must carry over; `rule_auth='nobody'` is the automation path | `_can_grant_badge()` |
| C09 | When a survey is completed and the participant passes a certification score threshold, the survey module directly triggers the gamification cron for challenges linked to the certification badge, rather than waiting for the next scheduled run. | `survey/models/survey_user_input.py` | 236–266 | Cross-module method call | HIGH | Survey certification is an event-driven trigger for the badge award flow, bypassing the normal daily cron lag. | Survey-gamification integration must be preserved | `_mark_done()` calls `_cron_update(ids=..., commit=False)` |
| C10 | Challenge records have no company identifier field. They operate across all companies. The only multicompany control is an access rule on individual goal records that restricts visibility to goals belonging to users in the viewer's own companies. | `gamification_challenge.py` (no company_id) + `gamification_security.xml` | — | Absence of field + security rule | HIGH | A single challenge can draw participants from multiple companies; per-user goal isolation is enforced at the record-rule layer. | Multi-company challenges are by design; goal-level isolation is the boundary | IR rule: `user_id.company_id in company_ids` |
| C11 | The winner determination method ranks participants by whether they completed all goals and by total aggregate completeness. If the "reward bests even if not succeeded" option is off, only users who finished every assigned goal can receive top-place badges. | `gamification_challenge.py` | 747–802 | Method logic | HIGH | Completion of all goals is the primary ranking criterion; partial completers are excluded unless the failure-reward flag is set. | Ranking logic replicated in reporting layer | `_get_topN_users()`; `reward_failure` flag |
| C12 | The scheduled background job starts draft challenges whose start date has arrived, closes in-progress challenges whose end date has passed, then refreshes all remaining running challenges in one pass, including creating goals for newly added participants. | `gamification_challenge.py` | 232–261 | Cron method logic | HIGH | A single daily job manages the full challenge lifecycle: start, update, close, reward. | Cron dependency in deployment; must be retained or re-triggered | `_cron_update()` |
| C13 | A badge award instance records the recipient, the badge, an optional sender (for peer grants), and the originating challenge (for automated grants). The two grant pathways are structurally separate fields on the same record. | `gamification_badge_user.py` | 15–21 | Field definitions | HIGH | Peer-sent and challenge-generated badges share one table; the type of grant is distinguished by which foreign key is populated. | Single award table; grant-type audit via field presence | `sender_id` vs `challenge_id` on `gamification.badge.user` |
| C14 | Manual goals send an email reminder to the assigned user if the goal has not been updated within a configurable number of days, but only once per overdue period and only while the goal is in progress. | `gamification_goal.py` | 91–114 | Method logic | HIGH | Inactivity nudge for human-entry goals; prevents silent staleness without flooding. | Reminder mechanism must survive migration | `_check_remind_delay()`; `remind_update_delay` |
| C15 | Batch computation mode allows a single database query to cover all users for a given goal definition simultaneously, using a distinctive field (such as user ID) to split aggregate results back to individual goals. | `gamification_goal_definition.py` | 53–55 | Field definitions | HIGH | Batch mode is a performance optimisation for high-volume deployments where per-user queries would be prohibitive. | Batch mode fields must be migrated; query logic may need adaptation | `batch_mode`, `batch_distinctive_field`, `batch_user_expression` |

---

## Dependency Map

- `gamification.challenge` → `gamification.challenge.line` → `gamification.goal.definition`
- `gamification.challenge` → `res.users` (participants)
- `gamification.challenge` → `gamification.badge` (rewards)
- `gamification.goal` → `gamification.challenge` (via line_id)
- `gamification.badge.user` → `gamification.badge` + `res.users`
- `survey.user_input._mark_done()` → `gamification.challenge._cron_update()`
- `gamification.goal._update_all()` → `mail.presence` (activity gate)

---

## Migration Risk Notes

1. **No company_id on challenges** — intentional design; multi-company isolation is at goal level only
2. **Presence-table join** — `_update_all()` depends on `mail.presence`; must confirm this table exists in target
3. **Survey integration** — `_cron_update(commit=False)` called synchronously in survey completion; integration hook must be preserved
4. **Batch mode** — three fields drive an alternate query path; all three must migrate together
5. **Four reward badge FKs** — all four columns needed; none are nullable in a functional sense
