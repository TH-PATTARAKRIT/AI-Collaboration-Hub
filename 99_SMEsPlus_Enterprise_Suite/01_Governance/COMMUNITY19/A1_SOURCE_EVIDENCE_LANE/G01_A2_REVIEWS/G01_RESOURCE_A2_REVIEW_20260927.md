# G01 PLATFORM_BASE — RED TEAM A2 REVIEW — Module `resource`

## 1. Header

| Field | Value |
|---|---|
| Role | RED TEAM A2 (functional/semantic verifier of A1 conclusions). Independent of A1; A1 package not repaired. |
| Group / Module | G01 PLATFORM_BASE / `resource` |
| Date | 2026-09-27 |
| A1 input | `G01_A1_PACKAGES/G01_RESOURCE_A1_PACKAGE_20260927.md` — sha256 `c7f17c210f6f4abca84a26d2f024d774577b56cdfaf0b9febe4d7d1b453a0d7d` |
| Lane A upstream | `G01_LANE_A_PASS1/G01_RESOURCE_LANE_A_PASS1_20260927.md` — sha256 `6148482c3278b841ef5fa5191c8fd9d3dd9b2c87244046d4f1fb6643cd8ceffd` (matches the value recorded in A1) |
| Question gate | `GMVQ/G01_PLATFORM_BASE/FREEZE_W1-STD.json` — file sha256 `370b92b43d56a99d6e6e444916356eb56e305fdf6bb86b4c7cd0d885a7ff317d`; internal freeze_hash `c64693eee3957388907637ad028ebdeea6fbeb19a093d1c459c5289f45f5c213` (matches A1 prefix `c64693ee…`). Standard 55 only. No module MVQ bank exists for `resource` (confirmed: no `G01_RESOURCE_GMVQ_*` file). MODULE+QID lineage beyond Standard 55 is **not available (GMVQ backlog)** — recorded as a governance gap, not an A1 defect. |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/resource/`. Independent A2 re-fetch into scratchpad `a2_rsrc/` (not committed). |
| Source blob re-check (`git hash-object`, 16 files) | `__manifest__.py` 72b99e4f; `models/resource_calendar.py` 335a8576; `models/resource_calendar_attendance.py` d8fb69b1; `models/resource_calendar_leaves.py` 841053e6; `models/resource_resource.py` aad3af2f; `models/resource_mixin.py` b68b6a9f; `models/res_company.py` 3ba30d24; `models/res_users.py` ef4f8859; `models/utils.py` 38137c26; `data/resource_data.xml` ffe3cf9e; `security/ir.model.access.csv` 34ca64a5; `security/resource_security.xml` 500b70f0; `views/menuitems.xml` 44953339; `views/resource_resource_views.xml` 46b5626f; `views/resource_calendar_views.xml` 40289018; `views/resource_calendar_leaves_views.xml` d217acd5 — **all identical** to Lane A pointers. |
| Layer | SOURCE-STATIC re-read. No runtime executed. |
| Clean-room | Neutral WHAT/WHY/RISK. No code pasted; identifiers are pointers only. |
| **Disposition** | **A2 VERIFIED WITH FINDINGS — HANDOFF TO REC.** No A1 claim is contradicted by source. 2 claims PARTIAL (scope nuance), 9 semantic omissions logged, 10 runtime proof requirements raised. Lane B NOT_APPLICABLE. |

## 2. Test plan (predeclared before verdicting)

| TP | Target | Method | Pass condition | Fail condition |
|---|---|---|---|---|
| TP-01 | Lineage | sha256 of A1 + Lane A; `git hash-object` of every cited blob | All match recorded values | Any mismatch → HOLD |
| TP-02 | C01 multi-company on calendars/attendances | Re-read record-rule file end to end; check calendar model for company auto-check | No rule on calendar/attendance models; company scoping only domain-level | Any rule or auto company check on those models |
| TP-03 | C02/C03 ACL + CANDIDATE contradiction (menus/actions vs read-only) | Re-read all 8 ACL rows; menu parent and resource list view; mixin create path for elevation | Resource rows read-only for both groups; menus/actions present; no elevation | Any write/create/unlink grant on resource, or elevation in mixin create |
| TP-04 | C04 leave rules | Re-read 5 rules with per-permission flags; evaluate group-rule union for plain user, access-rights manager, system admin | Plain user can create/write/delete resource-specific leaves where resource user is empty or self | Rule domain excludes no-user resources for modify |
| TP-05 | C05 hour ordering | Search attendance model for constraints/overrides touching hours; check inverse paths that write hours | Only onchange clamps; no server hour constraint | Any server constraint or create/write override on hours |
| TP-06 | C06 overlap/two-week | Re-read overlap helper and constraint | Per-weekday check; micro offset; two-week split | Different grouping or no offset |
| TP-07 | C07 planning cutoff + leaves default | Re-read both planning helpers: window size, loop count, return value, default of leave flag | 14-day × 100 windows, returns false, leaves off by default | Error raised, different bounds, or leaves on by default |
| TP-08 | C08 rate vs help | Re-read rate compute, help text, any constraint/clamp | Unbounded ratio × 100; fallback 100; help states 0–100 | Clamp or constraint exists |
| TP-09 | C09/C10 tz | Re-read tz-aware asserts, naive→UTC entry points, per-tz localization, context tz override, offset compute | Mechanism as claimed; offset uses current instant | Offset uses scheduled date, or naive treated as local |
| TP-10 | C11/C12 leaves semantics | Re-read leave-interval batch + leave model computes/constraint | Company match, time-type default, start ≤ end | Mismatch |
| TP-11 | C13–C18 | Re-read resource model, attendance parity, mixin field flags, company/users extensions, install data, cache decorator | As claimed | Mismatch |
| TP-12 | Business meaning | Evaluate multi-company SaaS, HR/project/MRP planning, Thailand (Asia/Bangkok, no DST; public holidays) | Omissions/overclaims logged | — |

TP-01 result: PASS (all hashes match; see Header).

## 3. Claim verdict table

| Claim | A1 conf. | A2 verdict | A2 independent re-read note (semantic) |
|---|---|---|---|
| C01 no company rule on calendars/attendances | HIGH / LOW | **VERIFIED** | Rule file holds exactly 5 rules: 3 on leaves by group, 1 global company rule on resources, 1 global company rule on leaves. None on calendar or attendance. Calendar model has no company auto-check; its company field has only a selection domain. Additionally the leave's calendar field is flagged company-checked, but the leave model does not enable automatic company checking, so that flag is domain-level only (supports A1's "selection-domain filters only"). Tenant-wide effect correctly left LOW pending G3. |
| C02 resource read-only for all groups | HIGH / UNKNOWN | **VERIFIED** | Both resource ACL rows (internal user, system admin) grant read only. Mixin create builds the resource with the caller's rights (no elevation). Company auto-provisioning is elevated but concerns calendars, not resources. CANDIDATE contradiction: see §4 F-01. |
| C03 calendar/attendance/leave ACL | HIGH | **VERIFIED** | Calendar and attendance: read for internal users, full for system admin. Leaves: full for both, narrowed by rules. |
| C04 any internal user edits leaves of no-user resources | HIGH | **VERIFIED** | Modify rule (internal-user group; read flag off) = resource set AND resource user in {empty, self}. Read rule = resource empty OR resource user in {empty, self}. Global-leave modify rule is on the access-rights manager group. Group rules combine by union, so a plain internal user can create/write/delete leaves on any resource with no linked user (subject to the leave company rule). See F-02 for the admin corollary. |
| C05 hour order only by onchange | HIGH / LOW | **VERIFIED** | Only server constraint on the attendance model is the break-in-duration-based rule. No create/write override. Clamp and order live solely in an onchange. See F-03: a server-side inverse can itself produce out-of-range hours. |
| C06 overlap check / two-week sections | HIGH | **PARTIAL** | Overlap mechanism VERIFIED (per weekday, micro offset on start, per week in two-week mode). Overclaim: "two-week calendars require every slot to sit under a week section". The server check only fails when sections exist and the first row by sequence is not a section; a two-week calendar with no section rows passes. Also in two-week mode the overlap check covers only rows typed first/second week; a row with no week type escapes the overlap check. |
| C07 14 days × 100 windows, silent false, leaves off by default | HIGH | **VERIFIED** | Both helpers loop 100 windows of 14 days forward or backward and return false; no error. Leave flag defaults to off in both. Additional: "plan days" takes no resource argument, so even with leaves on it only sees calendar-level (company-wide) leaves; "plan hours" accepts a resource. Naive input is localized as UTC. |
| C08 unbounded rate vs 0–100 % help | HIGH | **VERIFIED** (contradiction CONFIRMED-FROM-SOURCE) | Rate = weekly hours ÷ full-time hours × 100; 100 when reference is zero/empty; help says "should be between 0 and 100 %"; no constraint, clamp, or search-side bound. See F-04 for the full-time reference semantics. |
| C09 naive-as-UTC; per-tz localization | HIGH / LOW | **VERIFIED** | Internal attendance and leave batches assert tz-aware input. Public hour count and unusual-days replace missing tz with UTC; duration data, planning helpers and mixin helpers localize naive input as UTC. Slots generated naive per day then localized once per distinct tz, clipped per tz. A tz argument (including the context employee tz on the work-interval path) overrides every resource's own tz. See F-05 for a path that forces calendar tz. |
| C10 tz offset from today | MED | **VERIFIED** | Offset is computed from the current instant in the calendar tz. Display-only; no computation consumes it in this module. |
| C11 global vs resource leaves; time-type default | HIGH | **PARTIAL** | Stated rules VERIFIED. Omitted material nuances: (a) leaves with no calendar are included for every calendar (Lane A #18 had this; A1 dropped it); (b) a resource with no company never matches a company-wide leave, because the leave's company is always populated (computed from calendar, else creator's active company); (c) leaves are fetched with the caller's record rules, not elevated (see F-06). |
| C12 start ≤ end; computed company | HIGH | **VERIFIED** | Server constraint on dates; company = calendar's company or current company (read-only computed). See F-07 on the business effect. |
| C13 efficiency > 0; no calendar = fully flexible; same-company calendar | HIGH | **VERIFIED** | Database check on efficiency; help and helper treat no calendar as fully flexible (whole window available). Same-company restriction is a selection domain only; no server company check on the resource's calendar field (programmatic cross-company assignment not blocked in this module). |
| C14 epoch-based week parity | HIGH | **VERIFIED** | Day ordinal since year 1 ÷ 7, modulo 2; not ISO week. |
| C15 mixin search bypasses resource access | MED | **VERIFIED** | Mixin resource link: required, indexed, restrict-delete, search-access bypass flag set. |
| C16 default calendar per company | MED | **VERIFIED** (A2 content re-read; A1 had not spot-checked) | Install data seeds a 40 h calendar for the main company (noupdate) and calls the backfill; new companies get one under elevation; company default link is restrict-delete. See F-08. |
| C17 cached weekday lookup, no invalidation seen | LOW | **VERIFIED** (absence in module files) | Lookup is cached keyed on calendar id only; no cache clear in any module file; attendance model has no write override. Staleness itself is runtime → PR-08. |
| C18 tz default chain; admin first-login copy | MED | **VERIFIED** | Calendar default: context → user → admin user → UTC. Resource on create: linked user tz, else calendar tz; field default context → user → UTC. Admin first-login tz copied to own calendar or to the standard calendar. |

Verdict counts: VERIFIED 16 · PARTIAL 2 · NOT_VERIFIED 0 · OUT_OF_SCOPE 0.

Other A1 sections re-read: BR1–BR7, States (§3), Exceptions (§4), Handoffs (§5) — consistent with source except the BR1/C06 two-week nuance and the omissions below. A1 §3 "duration-based mode can be turned on and off" understates destructiveness (F-09).

## 4. Semantic findings

- **F-01 (CRQ/contradiction, C02).** A2 confirms within module scope: the "Resources" menu (under technical settings, admin-facing) opens a list that allows multi-edit, yet no group, including system admin, has write/create/delete on resources in this module. In a database where only `resource` (and its dependents without extra ACLs) is installed, resource maintenance through these surfaces cannot succeed. Status stays CANDIDATE across modules (consumers such as HR may add grants; G2).
- **F-02 (C04 corollary, omission).** Record rules are not bypassed by the system-admin group. Within this module, no rule lets anyone but the linked user modify a leaf on a resource linked to another user; admins get only the no-user/own set plus company-wide leaves (via the access-rights manager group, assumed implied for admins — base implication not re-read). Business effect: in `resource` alone, HR-style administration of other people's time off is impossible without other modules' rules or elevation.
- **F-03 (C05 extension, omission).** In duration-based calendars the duration inverse rewrites hours around midday server-side. A morning duration above 12 h yields a negative start; a full-day duration above 24 h yields an end beyond 24. This path runs on normal form saves, so out-of-range slots are reachable without import/RPC.
- **F-04 (C08 extension).** The full-time reference is recomputed from the company default calendar's weekly hours whenever the calendar's own weekly hours change, overwriting any manual value; the company default calendar therefore always reports 100. Company-less (shared) calendars get no computed reference, so the rate falls back to 100 regardless of hours unless a create-time default populated it. Consumers deriving FTE/part-time status from shared calendars may misreport.
- **F-05 (C09 extension).** The resource-level unavailable-interval helper (source comment: used by planning/forecast) forces the calendar's tz for all resources of that calendar, not each resource's own tz. Resources whose tz differs from their calendar are computed in calendar time on that path. For per-tz localization, A1's claim is correct for the generic path only.
- **F-06 (C11/HIGH, omission).** Leave and attendance lookups inside the engine run with the caller's access (no elevation in this module). A plain internal user computing work time for a resource linked to another user cannot see that user's personal leaves (read rule excludes them), and the leave company rule hides leaves of non-allowed companies. Results are therefore caller-dependent unless consumers elevate. Needs runtime proof (PR-09).
- **F-07 (C12, business meaning).** A company-wide leaf with no calendar takes the creator's **active** company. In multi-company SaaS the company switcher at entry time silently decides which company's resources lose that day; a leaf on a shared (company-less) calendar also takes the creator's company.
- **F-08 (C16, omission).** New calendars copy the company default calendar's attendances **and company-wide leaves** at creation (snapshot, not linked). Public holidays added later to the default calendar do not propagate to earlier calendars; switching two-week mode off, or duration-based mode off, deletes all slots and reloads the company default (F-09).
- **F-09 (States, omission).** Toggling duration-based on deletes break rows; toggling it off, or leaving two-week mode, deletes every attendance and restores company defaults. Customised schedules are lost without confirmation logic in this module.

Business meaning review (working-time engine for HR/project/MRP planning, multi-company SaaS):
- The engine is calendar-centric with optional per-resource leaves; company isolation for calendars is UI-level only (C01), while leaves and resources are rule-scoped. For a SaaS tenant with several companies, calendars (including their holiday leaves via one-to-many) may be readable cross-company — a data-leak and mis-assignment risk that SMEsPlus design must close server-side.
- Thailand: Asia/Bangkok has no DST, so C09/C10 DST risks are non-material for Thai-only tenants, but naive-as-UTC (C09) is material: a naive local datetime shifts results by 7 hours, enough to move work across a day boundary. The module ships no holiday data; Thai public holidays (including substitution days) must be maintained as company-wide leaves per calendar, and F-07/F-08 make them fragile (creator's active company; snapshot copy). Six-day work weeks are representable by weekday slots; no Thai-specific rule exists.
- Planning (C07) default ignoring leaves means consumers that do not pass the flag can schedule onto public holidays.

## 5. Omissions (A1 vs source / Lane A)

| ID | Omission | Linked claim | Severity |
|---|---|---|---|
| O-01 | Calendar-less leaves apply to all calendars (in Lane A #18, dropped by A1) | C11 | MED |
| O-02 | Company-less resources never receive company-wide leaves | C11 | MED |
| O-03 | Engine results depend on caller's leave visibility (no elevation) | C11/F-06 | HIGH |
| O-04 | Duration inverse can store out-of-range hours via normal form | C05/F-03 | MED |
| O-05 | Full-time reference overwritten on hours change; shared calendars rate 100 | C08/F-04 | MED |
| O-06 | Planning/forecast helper forces calendar tz | C09/F-05 | MED |
| O-07 | Active-company decides company of global leaves | C12/F-07 | MED |
| O-08 | Calendar creation snapshots company holidays; mode toggles wipe slots | C16/F-08/F-09 | MED |
| O-09 | Admin group not exempt from leave rules; "plan days" has no resource | C04/C07 | LOW |

## 6. Lane B classification

No Lane B evidence exists for `resource`. Classification: **NOT_APPLICABLE** at module level; every claim is **UNCORROBORATED** by runtime. No claim is failed for lack of Lane B.

## 7. Proof requirements (MISSING_REQUIRED_RUNTIME_PROOF — inherently runtime only)

| PR | Claim | Setup / action | Expected | Fail condition |
|---|---|---|---|---|
| PR-01 | C01 | Two companies A,B; user allowed only A; calendar owned by B; user reads B calendar and its slots by id/search | If no other module adds a rule: B calendar readable | Access error or B calendar absent → C01 risk refuted for that install (record which module adds the rule) |
| PR-02 | C02/F-01 | Install `resource` only; system admin creates/edits a resource via UI and RPC | Access error on write/create | Save succeeds without elevation → identify the grant |
| PR-03 | C04 | Plain internal user; material resource with no user; create, edit, delete its leave | All three succeed | Any denied |
| PR-04 | C05/F-03 | RPC write of end < start and end > 24; duration-based calendar with 14 h morning via form | Records stored; observe weekly hours, duration and overlap outcome | Server rejects any of them |
| PR-05 | C07 | Calendar with a single slot every ~5 years (or empty); request plan hours/days | Returns false, no error | Error raised or date returned beyond 1,400 days |
| PR-06 | C08 | Calendar with 60 h/week vs 40 h reference | Rate 150 shown/stored in consumers | Value clamped to 100 or rejected |
| PR-07 | C09/C10 | Asia/Bangkok calendar; call hour count with naive 08:00–17:00 local; also Europe/Berlin across DST change | Naive input treated as UTC (7 h shift); DST result recorded | Naive treated as local; DST interval wrong vs expected wall-clock hours |
| PR-08 | C17 | Call weekday-worked lookup; remove Saturday slot; call again in same and another worker | Stale result until cache clear (if claim holds) | Fresh result immediately → claim refuted |
| PR-09 | F-06 | Plain user computes work hours for a resource linked to another user who has a personal leave | Leave ignored (hours overstated) unless consumer elevates | Leave applied → engine or consumer elevates |
| PR-10 | O-02/F-07 | Global leave created while active company = B; resource with no company and one in A on same calendar | Neither A nor company-less resource loses the day | Either resource loses the day |

Count: 10.

## 8. Limitations

- SOURCE-STATIC only; absence statements cover this module's files at the anchor commit. `base` group implications, the interval utility, and the localization helper were not re-read (framework behaviour assumed only where stated).
- Static JS and tests not reviewed (A1 G1 stands).
- No module MVQ bank; no MODULE+QID mapping (GMVQ backlog). No Formal Coverage, no percentages.
- REC, PROOF and A3 pending.
