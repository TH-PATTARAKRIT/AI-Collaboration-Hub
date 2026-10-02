# U191 — Gamification: Challenge / Goal / Badge Award System
**Level:** L3 (Deep Technical Evidence)
**Group:** G14 | Priority: P3 | Status: NOT_STUDIED → STUDIED
**Source:** Odoo Community 19.0.post20260921
**Addons path:** `odoo/addons/gamification/`

---

## 1. `gamification.challenge` — Field Inventory

**Model file:** `models/gamification_challenge.py`

| Field | Type | Key Facts |
|---|---|---|
| `name` | Char | Required, translate=True |
| `state` | Selection | draft / inprogress / done; default='draft'; tracking=True |
| `period` | Selection | once / daily / weekly / monthly / yearly; default='once' |
| `start_date` | Date | Start of current period; used by `start_end_date_for_period()` |
| `end_date` | Date | End of current period |
| `user_ids` | Many2many res.users | Explicit participant list; rel table `gamification_challenge_users_rel` |
| `user_domain` | Char | Evaluated domain string; used to auto-populate `user_ids` on create/write |
| `visibility_mode` | Selection | 'personal' (individual goals) or 'ranking' (leaderboard) |
| `reward_id` | Many2one gamification.badge | Badge awarded to every user who reaches all goals (index btree_not_null) |
| `reward_first_id` | Many2one gamification.badge | Badge for 1st place |
| `reward_second_id` | Many2one gamification.badge | Badge for 2nd place |
| `reward_third_id` | Many2one gamification.badge | Badge for 3rd place |
| `reward_failure` | Boolean | If True, top-ranked users receive rank badges even without completing all goals |
| `reward_realtime` | Boolean | Default True; grant `reward_id` immediately on goal completion; prevents duplicate grants |
| `challenge_category` | Selection | 'hr' (HR/Engagement) or 'other' (Settings/Gamification Tools) |

**Company scoping:** No `company_id` field on `gamification.challenge`. The multicompany rule in `security/gamification_security.xml` filters **goals** by `user_id.company_id in company_ids` — challenges themselves are global (cross-company).

---

## 2. `gamification.goal` — Field Inventory

**Model file:** `models/gamification_goal.py`

| Field | Type | Key Facts |
|---|---|---|
| `definition_id` | Many2one gamification.goal.definition | Required; ondelete=cascade |
| `user_id` | Many2one res.users | Required; bypass_search_access=True; index=True |
| `line_id` | Many2one gamification.challenge.line | ondelete=cascade |
| `challenge_id` | related line_id.challenge_id | Stored; readonly; index=True |
| `start_date` | Date | Default today |
| `end_date` | Date | No start/end = always active |
| `target_goal` | Float | Required; the value to reach |
| `current` | Float | Required; current progress value; default=0 |
| `completeness` | Float | Computed; 0–100; `_get_completion()` |
| `state` | Selection | draft / inprogress / reached / failed / canceled |
| `to_update` | Boolean | Flag for pending update |
| `closed` | Boolean | Set True when goal fails after end_date |
| `remind_update_delay` | Integer | Days before reminder for manual goals |
| `last_update` | Date | Set on every `write()`; drives reminder logic |

**Completeness logic (`_get_completion`):**
- condition='higher': `round(100 * current / target_goal, 2)`; caps at 100 when current >= target
- condition='lower': 100 if current < target_goal, else 0 (boolean only)

---

## 3. `gamification.badge` — Field Inventory

**Model file:** `models/gamification_badge.py`

| Field | Type | Key Facts |
|---|---|---|
| `name` | Char | Required; translate=True |
| `description` | Html | Sanitize_attributes=False; translate=True |
| `level` | Selection | bronze / silver / gold; default='bronze' |
| `rule_auth` | Selection | everyone / users / having / nobody; controls who can manually grant |
| `rule_max` | Boolean | Monthly sending limit toggle |
| `rule_max_number` | Integer | Max sends per person per month |
| `challenge_ids` | One2many gamification.challenge | Challenges using this badge as `reward_id` |
| `goal_definition_ids` | Many2many gamification.goal.definition | Definitions that auto-grant this badge |
| `owner_ids` | One2many gamification.badge.user | All grant instances |
| `granted_count` | Integer | Computed total grants |
| `stat_this_month` | Integer | Computed monthly grants |

**`_can_grant_badge()` codes:**
- `CAN_GRANT = 1` — allowed
- `NOBODY_CAN_GRANT = 2` — rule_auth='nobody' (challenges only)
- `USER_NOT_VIP = 3` — not in rule_auth_user_ids
- `BADGE_REQUIRED = 4` — missing required prerequisite badges
- `TOO_MANY = 5` — monthly limit exceeded

---

## 4. `gamification.badge.user` — How Badges Are Awarded

**Model file:** `models/gamification_badge_user.py`

| Field | Purpose |
|---|---|
| `user_id` | Recipient (required; ondelete=cascade) |
| `badge_id` | The badge being granted (required; ondelete=cascade) |
| `sender_id` | The user who manually sent the badge |
| `challenge_id` | Challenge that triggered the award (if automated) |
| `comment` | Optional message from sender |

**Award pathway:**
1. `create()` calls `badge.check_granting()` → validates `_can_grant_badge()`
2. `_reward_user(user, badge)` in challenge creates `gamification.badge.user` record then calls `._send_badge()`
3. `_send_badge()` sends a chatter/email notification to the recipient using template `gamification.email_template_badge_received`

**Note:** `sender_id` is for manual peer-to-peer grants. Challenge-automated grants populate `challenge_id` instead.

---

## 5. `_cron_update()` — Scheduled Goal Refresh

**Location:** `GamificationChallenge._cron_update()` (lines 232–261 of `gamification_challenge.py`)

**Execution flow:**
1. Start challenges in 'draft' state whose `start_date <= today` → write state='inprogress'
2. Close challenges in 'inprogress' state whose `end_date < today` → write state='done'
3. Browse in-progress challenges → call `_update_all()`

**`_update_all()` steps:**
1. SQL query selects `gamification.goal` records where the user has had a `mail.presence` interaction since the goal's last write and within `SESSION_LIFETIME` seconds — **only active users trigger recalculation** (performance guard)
2. `Goals.update_goal()` — recomputes each goal's current value via `computation_mode`
3. `_recompute_challenge_users()` — re-evaluates `user_domain`
4. `_generate_goals_from_challenge()` — creates missing goals for new participants
5. Reports scheduled progress
6. `_check_challenge_reward()` — evaluates whether badges should be granted

---

## 6. Survey Module Badge Award — `_mark_done()` Flow

**File:** `odoo/addons/survey/models/survey_user_input.py`, method `_mark_done()` (lines 236–266)

**Step-by-step:**
1. Write `state='done'`, `end_datetime=now()`
2. For each completed user_input where `survey.certification=True` and `scoring_success=True`:
   - Send certification email if template set
   - If `certification_give_badge=True` → collect `certification_badge_id.id` into `badge_ids`
3. If `badge_ids` is non-empty:
   - `Challenge_sudo.search([('reward_id', 'in', badge_ids)])` — find challenges whose reward is a certification badge
   - `Challenge_sudo._cron_update(ids=challenges.ids, commit=False)` — run immediate (non-committing) challenge update

**Key insight:** There is no direct `challenge_update()` method. Survey calls `_cron_update()` directly with targeted challenge IDs, avoiding a full cron pass.

---

## 7. `gamification.goal.definition` — Computation Modes

**Model file:** `models/gamification_goal_definition.py`

| `computation_mode` | Description |
|---|---|
| `'manually'` | User updates the value by hand via wizard; system sends reminders via `_check_remind_delay()` |
| `'count'` | Automatic: `Obj.search_count(domain)` — counts matching records |
| `'sum'` | Automatic: `Obj._read_group(domain, [], [field:sum])` — sums a numeric field |
| `'python'` | Automatic: executes `compute_code` via `safe_eval`; must set `result` to a float/int |

**`domain` field:** Char; default `"[]"`; evaluated with `{'user': goal.user_id}` context in non-batch mode. Allows per-user filtering (e.g. `[('user_id', '=', user.id)]`).

**Batch mode fields:**
- `batch_mode` (Boolean): process all users in one DB query
- `batch_distinctive_field`: field that distinguishes one user from another (e.g. `user_id`, `partner_id`)
- `batch_user_expression`: evaluated expression returning the user's key value (e.g. `user.id`)

---

## 8. Company Scope

`gamification.challenge` has **no `company_id` field** and no record rule on the challenge model itself. Challenges are **global across all companies**.

The only multicompany constraint is an `ir.rule` on `gamification.goal` filtering by `user_id.company_id in company_ids` — meaning a user in company A cannot see goals belonging to users in company B. But the same challenge can span users from multiple companies.

---

## 9. `_check_challenge_reward()` — Winner Determination

**Location:** `GamificationChallenge._check_challenge_reward()` (lines 654–745 of `gamification_challenge.py`)

**Trigger conditions:**
- `force=True` — challenge manually set to 'done' (write state='done' triggers this)
- `challenge_ended = (end_date == yesterday)` — period just completed
- `reward_realtime=True` — checked on every `_update_all()` call mid-period

**Logic (per challenge):**
1. Query goals grouped by `user_id` where `state='reached'` and `end_date=challenge_period_end`
2. If `count == len(challenge.line_ids)` → user has reached ALL assigned goals → eligible for `reward_id`
3. If `reward_realtime`: check `gamification.badge.user` for existing grant; skip duplicates
4. Call `_reward_user(user, reward_id)` → creates `gamification.badge.user` + notifies
5. On period end: call `_get_topN_users(3)` for rank badges (1st/2nd/3rd)
6. `_get_topN_users()` ranks by (all_reached DESC, total_completeness DESC); if `reward_failure=False`, only fully successful users qualify

---

## 10. Supporting Files Referenced

| File | Purpose |
|---|---|
| `models/gamification_challenge_line.py` | Links a `goal.definition` to a challenge with a `target_goal` |
| `models/res_users.py` | Karma field and badge stats on user |
| `security/gamification_security.xml` | IR rules: personal goal visibility + multicompany goal filter |
| `data/` | Default cron action for `_cron_update`, email templates |
| `survey/models/survey_user_input.py` | Calls `_cron_update()` on survey completion |
