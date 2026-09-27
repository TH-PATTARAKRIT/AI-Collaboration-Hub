# G01 PLATFORM_BASE — RED TEAM Proof Package — `resource`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller (Stage 2; REC recorded separately) |
| Governed group / module | G01 PLATFORM_BASE / `resource` |
| REC input | `G01_RECONCILIATION/G01_RESOURCE_REC_20260927.md` (28 REC items) |
| Upstream (sha256 at intake) | A1 `c7f17c21…a0d7d`; A2 `23b99cd6…f4a0`; Lane A `6148482c…ffd` (full values in the REC §2) |
| Question lineage | Standard 55 only (W1-STD, freeze `c64693ee…c213`, verified). **MVQ lineage unavailable.** |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>` |
| Runtime device | OFFLINE (MASTER handoff state: since 2026-09-24T12:53Z). No runtime case was executed. |
| Case predeclaration | Written 2026-09-27T**15:03:14Z** (Asia/Bangkok 22:03:14), before any case was executed. Scratch `rec_rsrc/PROOF_CASES_PREDECLARED.md`, sha256 `14159fb2b786343239b4582c2fda958a619f87b2b2319829827b0516fde114de` (shared with `resource_mail`). Before that timestamp, the only action on the source was fetch plus `git hash-object` (15:02:02Z); no case construct was read. |
| Execution window | 2026-09-27T15:03:30Z – 15:05:00Z (SOURCE/CONFIG only) |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** (21 static cases: 21 PASS, 0 FAIL; 10 runtime cases NOT-EXECUTED) |

## 1. Case design

- Layers: CONFIG (security, data, manifest declarations), SOURCE (static code reading, including one framework helper), and RUNTIME (Odoo instance). No CROSS-MODULE runtime was attempted.
- Each static case names the file and the construct. It has falsifiable Expected and Fail conditions, declared before execution (section 0).
- Blob rule: every fetched file must equal the Lane A blob under `git hash-object`. A mismatch means the case is BLOCKED. There were no mismatches.
- Thailand rule: PC-RSRC-10 uses the source rule, then applies Python stdlib `zoneinfo` arithmetic. It is not an Odoo runtime result.

## 2. Blob verification (executed 2026-09-27T15:02:02Z)

| File (`addons/…` unless stated) | Lane A blob | Recomputed | Result |
|---|---|---|---|
| resource/__manifest__.py | 72b99e4f | 72b99e4faad899e6631ba8d1d96698b9c7ff1e0f | MATCH |
| resource/models/resource_calendar.py | 335a8576 | 335a857625070669ad79bd701fb38be03ec5704a | MATCH |
| resource/models/resource_calendar_attendance.py | d8fb69b1 | d8fb69b117b5c395eedfc213a31e8480f4c79936 | MATCH |
| resource/models/resource_calendar_leaves.py | 841053e6 | 841053e65b7f2ea6693f4fa18d3e98eb7e821fe4 | MATCH |
| resource/models/resource_resource.py | aad3af2f | aad3af2f8b87bff4cc650819abc2856fdb826067 | MATCH |
| resource/models/resource_mixin.py | b68b6a9f | b68b6a9fd53c7a54d29bd5765018202ee8e2e3f5 | MATCH |
| resource/models/res_company.py | 3ba30d24 | 3ba30d249a114b80374e146590bc864fd17aa123 | MATCH |
| resource/models/res_users.py | ef4f8859 | ef4f885919e56161ce218abccbf95e3f69972b0b | MATCH |
| resource/security/ir.model.access.csv | 34ca64a5 | 34ca64a5e94929feffacb29fae63b73e78a0b3c7 | MATCH |
| resource/security/resource_security.xml | 500b70f0 | 500b70f06c5fb917bd5657bbaaf23843920dae0c | MATCH |
| resource/data/resource_data.xml | ffe3cf9e | ffe3cf9ee87bf9ca54cc51f0773b62da4b1ecc4c | MATCH |
| resource/views/resource_resource_views.xml | 46b5626f | 46b5626f24b6861ea8d24aabf2a14b8c6730cc28 | MATCH |
| resource/views/menuitems.xml | 44953339 | 44953339ff89449a697025299372321819786c5d | MATCH |
| `odoo/tools/date_utils.py` (framework; not in Lane A) | — (recorded here) | bde8a94337dd936b2a3b7af5f0ab066d33555e74 | RECORDED |

The blob log is in scratch at `rec_rsrc/blob_log.txt`. Source copies are in `rec_rsrc/src/`. None was committed.

## 3. Static cases — executed (SOURCE / CONFIG)

Line numbers refer to the anchor blob. Evidence is paraphrased; no code is reproduced.

| Case | Layer | REC item(s) | Evidence (file @ blob : lines) | Observation | Result |
|---|---|---|---|---|---|
| PC-RSRC-01 | CONFIG | REC-01 | resource_security.xml @ 500b70f0 : 4–40 | 5 `ir.rule` records: 3 on leaves by group (user read, user modify, access-rights manager modify), 1 global company rule on resource, 1 global company rule on leaves. None on calendar or attendance. | PASS |
| PC-RSRC-02 | CONFIG | REC-02, 03 | ir.model.access.csv @ 34ca64a5 : 2–9 | 8 rows. Resource: read-only for both the internal user and the system group. Calendar and attendance: read-only for users, full for system. Leaves: full for both. | PASS |
| PC-RSRC-03 | CONFIG | REC-04, 28 | resource_security.xml : 4–26 | User read rule: resource empty OR resource user in {none, self}. User modify rule (read flag off): resource set AND resource user in {none, self}. Global-leave modify rule is on `base.group_erp_manager` only. No rule exempts the system group. | PASS |
| PC-RSRC-04 | SOURCE | REC-05 | attendance @ d8fb69b1 : 50–65 | The only `constrains` decorator is on the day period (break in a duration-based calendar). Hour clamp (0–23.99 / 0–24) and ordering are in an onchange only. No `create`/`write` override exists (0 matches). | PASS |
| PC-RSRC-05 | SOURCE | REC-23 | attendance : 82–96 | The duration inverse (duration-based calendars only) sets hours at 12 ± duration, or 12 − d / 12 + d, with no bound. A morning duration > 12 gives a negative start. A full day > 24 gives an end > 24 and a negative start. | PASS |
| PC-RSRC-06 | SOURCE | REC-06, 19 | calendar @ 335a8576 : 123–138, 615–625 | The section error is raised only when the calendar is in two-week mode AND section rows exist AND the first row by sequence is not a section. A two-week calendar with no sections passes. The overlap check runs separately on week type '0' and '1'. Rows with no week type (field default False; attendance : 40–43) are in neither set. Contiguous slots are allowed by a 0.000001 start offset. | PASS (confirms the A2 side of the CONTRADICTION) |
| PC-RSRC-07 | SOURCE | REC-07, 28 | calendar : 854–941 | Both helpers use 14-day windows, `range(100)`, and return False when the target is not reached; neither raises. `compute_leaves` defaults to False in both. Plan-days has no resource parameter (it takes the calendar-level key only). Naive input is localized as UTC. | PASS |
| PC-RSRC-08 | SOURCE | REC-08, 24 | calendar : 56–59, 116–117, 159–161, 250–279 | The rate is weekly hours ÷ full-time hours × 100, with no clamp. It is 100 when the reference is empty or zero. The help text says "should be between 0 and 100 %". The search method filters in memory with no bound. Full-time hours are a stored compute that depends on the calendar's own weekly hours and the company calendar's hours, and is computed only for calendars with a company. The default_get copies the company calendar value at creation. | PASS |
| PC-RSRC-09 | SOURCE | REC-09 | calendar : 328, 506, 727–730, 815–818, 843; date_utils @ bde8a943 : 90–92 | The internal attendance and leave batches assert that input is tz-aware. The public hour count and unusual-days replace a missing tz with UTC. Duration data and the planning helpers use the framework `localized` helper, which adds UTC when tz is missing. | PASS |
| PC-RSRC-10 | SOURCE + stdlib | REC-09 (Thailand) | PC-RSRC-09 rule; Python 3.11.15 `zoneinfo` (scratch `rec_rsrc/thai_case.txt`) | A caller intends the Asia/Bangkok local window 2026-10-01 08:00–17:00 and passes naive values. By the source rule these are read as 08:00–17:00 UTC, which is **15:00 on 1 Oct to 00:00 on 2 Oct Bangkok**: a +7 h shift that crosses the local date boundary. The correct UTC window would be 01:00–10:00. The Asia/Bangkok utcoffset is constant +07:00 at every hour of 2026 (one distinct value), so there is no DST. Arithmetic illustration only: an 08–12 / 13–17 Bangkok schedule has 2 h inside the misread window instead of 8 h. **This is not an Odoo runtime output.** | PASS |
| PC-RSRC-11 | SOURCE | REC-10 | calendar : 238–240 | The offset is formatted from `now` in the calendar tz, not from a scheduled date. | PASS |
| PC-RSRC-12 | SOURCE | REC-11, 20, 21, 22 | calendar : 502–554 | The default domain is time type = leave. The calendar term is {none} ∪ own ids, so calendar-less leaves are included. The resource term is {none} ∪ requested. A resource-less leave is skipped for a resource whose company differs from the leave company; a company-less resource never equals a populated leave company. The leave search runs in the caller's environment with no `sudo` (the only `sudo` in the calendar file is at 566, on attendance work-period metadata). | PASS |
| PC-RSRC-13 | SOURCE | REC-12, 26 | leaves @ 841053e6 : 36–38, 59–61, 75–78 | The company is computed as the calendar's company, else `env.company` (the creator's active company). A constraint rejects start > end. | PASS |
| PC-RSRC-14 | SOURCE | REC-13 | resource @ aad3af2f : 44–59, 218–221 | A database CHECK requires efficiency > 0. The calendar field has a same-company selection domain; no server company check was found in the file. Having no calendar means fully flexible. | PASS |
| PC-RSRC-15 | SOURCE | REC-14 | attendance : 68–75 | Parity = floor((ordinal − 1) / 7) mod 2. There is no ISO week call. | PASS |
| PC-RSRC-16 | SOURCE | REC-15 | mixin @ b68b6a9f : 14–16 | The resource link is required, indexed, restrict-delete, and has the search-access bypass flag set. | PASS |
| PC-RSRC-17 | SOURCE / CONFIG | REC-16, 27 | data xml @ ffe3cf9e : 3–15; res_company @ 3ba30d24 : 12–17, 36–44; calendar : 202–207 | noupdate seeds the standard calendar and calls the backfill. A new company gets a calendar under `sudo`. The company default link is restrict-delete. A calendar's global leaves are rebuilt as **copies** of the company default calendar's global leaves whenever the calendar is new or its company changes (a snapshot, not a link). | PASS |
| PC-RSRC-18 | SOURCE | REC-17 | calendar : 1011; grep of all fetched `resource/` files | The weekday lookup is `ormcache`d on the calendar id. No `clear_cache`, registry clear or `invalidate` call was found in the fetched module files. | PASS |
| PC-RSRC-19 | SOURCE | REC-18 | calendar : 110–112; resource : 52–54, 67–76; res_users @ ef4f8859 : 16–25 | Calendar tz default: context → user → admin → UTC. Resource field default: context → user → UTC. On create, a missing tz comes from the linked user, else the calendar. The admin's tz is copied before first login to their calendar or to the standard calendar. | PASS |
| PC-RSRC-20 | SOURCE | REC-25 | resource : 145–161 | Resources are grouped by calendar (or the company calendar). The batch is called with `tz` = the calendar's tz for all of them. | PASS |
| PC-RSRC-21 | SOURCE | REC-27 | calendar : 299–321 | Leaving two-week mode deletes all attendances and reloads the company defaults. Turning duration-based on deletes break rows. Turning it off deletes all attendances and reloads the defaults. No confirmation logic exists in this file. | PASS |

### 3.1 Refinements observed (for A3; no verdict is changed)

- **R1 (REC-12 / REC-09).** In the leave-interval batch (calendar : 537), the tz variable is reassigned inside the per-resource loop. When the caller passes no `tz`, the first resource's tz is reused for every later resource and leave in that call. The effect on leave clipping for mixed-tz resource sets is **not proven**. It is a runtime candidate, not a claim.
- **R2 (REC-27).** The global-leave copy (calendar : 202–207) also fires when an existing calendar's company is changed: its global leaves are cleared and replaced by the new company's defaults. This is broader than "copied at creation".
- **R3 (REC-19).** In interval generation (calendar : 355–365), a two-week row with no week type is indexed as week 0. Such rows are counted as first-week work while skipping the overlap check (PC-RSRC-06).
- **R4 (Thailand).** The default leave end date (end-of-day fill) uses the user or context tz, else the company calendar tz (leaves : 64–67). For Thai tenants whose users have no tz set, the company calendar tz decides the day boundary.

## 4. Runtime cases — NOT-EXECUTED (device OFFLINE)

These are ready to run on an Odoo 19 instance at the anchor commit with `resource` installed (and no HR/planning modules unless stated). Expected and Fail conditions are carried from A2 §7 unchanged. No result is claimed.

| Case | A2 PR | REC | Preconditions | Steps | Expected | Fail | Status |
|---|---|---|---|---|---|---|---|
| PC-RSRC-R01 | PR-01 | 01 | Companies A and B; user U allowed only A; calendar Cb owned by B with slots | U reads Cb and its attendances by id and by search | If no other module adds a rule: Cb readable | Access error, or Cb absent (record which module adds a rule) | NOT-EXECUTED |
| PC-RSRC-R02 | PR-02 | 02 | Only `resource` installed | System admin creates and edits a resource via UI and RPC | Access error on create/write | Save succeeds without elevation (identify the grant) | NOT-EXECUTED |
| PC-RSRC-R03 | PR-03 | 04 | Plain internal user; material resource with no user | Create, edit and delete a leave on it | All three succeed | Any is denied | NOT-EXECUTED |
| PC-RSRC-R04 | PR-04 | 05, 23 | Calendar; duration-based calendar | RPC write with end < start and end > 24; form save of a 14 h morning duration | Stored; record weekly hours, duration and overlap outcome | Server rejects any of them | NOT-EXECUTED |
| PC-RSRC-R05 | PR-05 | 07 | Empty or sparse calendar | Call plan hours and plan days | Returns False, no error | Error, or a date beyond ~1,400 days | NOT-EXECUTED |
| PC-RSRC-R06 | PR-06 | 08, 24 | 60 h/week calendar vs 40 h reference; a company-less calendar | Read the rate; view it in consumers | 150 shown/stored; the company-less calendar shows 100 | Clamped to 100, or rejected | NOT-EXECUTED |
| PC-RSRC-R07 | PR-07 | 09, 10, 25 | Asia/Bangkok calendar 08–12/13–17; Europe/Berlin calendar | Hour count with naive 08:00–17:00 (Bangkok); aware input for Berlin across the 2026-10-25 DST change; unavailable-interval helper with resource tz ≠ calendar tz | Naive input shifted by 7 h (PC-RSRC-10 prediction); DST result recorded; helper uses the calendar tz | Naive treated as local; wrong DST wall-clock hours | NOT-EXECUTED |
| PC-RSRC-R08 | PR-08 | 17 | Calendar with a Saturday slot | Call the weekday lookup; remove Saturday; call again in the same and another worker | Stale until cache clear (if the claim holds) | Fresh result immediately (claim refuted) | NOT-EXECUTED |
| PC-RSRC-R09 | PR-09 | 22 | User V has a personal leave; plain user U | U computes work hours for V's resource | Leave ignored (hours overstated) unless the consumer elevates | Leave applied | NOT-EXECUTED |
| PC-RSRC-R10 | PR-10 | 21, 26 | Global leave created with active company B on a company-less calendar; resources in A and with no company on that calendar | Compute work intervals for both | Neither loses the day | Either loses the day | NOT-EXECUTED |

## 5. Summary of results

| Layer | Cases | PASS | FAIL | NOT-EXECUTED |
|---|---|---|---|---|
| CONFIG | 3 (PC-01, 02, 03) | 3 | 0 | 0 |
| SOURCE (incl. SOURCE/CONFIG and SOURCE+stdlib) | 18 (PC-04..21) | 18 | 0 | 0 |
| RUNTIME | 10 (PC-R01..R10) | 0 | 0 | 10 |
| **Total** | **31** | **21** | **0** | **10** |

REC item status after Proof:
- The CONTRADICTION (REC-RSRC-06) is **source-confirmed on the A2 side**: the section requirement is not enforced when there are no sections. It stays CONTRADICTION for A3 and is not closed.
- The 9 UNKNOWN_PENDING_PROOF items have their static basis confirmed (every linked static case PASS). **All remain UNKNOWN_PENDING_PROOF** until PC-RSRC-R01..R10 run.
- The 11 GAP items have their source facts confirmed. They are carried forward because Proof cannot repair A1.
- The 7 MATCH items are unchanged.

## 6. A3 eligibility

**Disposition: PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING.**

A3 may challenge the following **now** (static scope):
1. The REC classifications and counts (28 items): the UNKNOWN_PENDING_PROOF versus MATCH split, and the CONTRADICTION class on REC-RSRC-06 (where A2 said PARTIAL).
2. The 21 executed static cases: whether each Expected/Fail pair was falsifiable, whether the observations support PASS, and refinements R1–R4.
3. The Thailand case PC-RSRC-10: its reliance on the naive-as-UTC rule plus stdlib arithmetic, as opposed to Odoo runtime.
4. Standard-55 lineage (16 STD-QIDs mapped; 4 items with no fit). **QID-level A3 lineage is limited to Standard 55. MVQ lineage is unavailable (GMVQ backlog).**
5. Input integrity (the sha256 intake, the freeze-hash recomputation, blob verification) and the predeclaration timing (15:03:14Z, before execution).

**Blocked** until the runtime device is available:
- All 10 runtime cases. Closing any UNKNOWN_PENDING_PROOF item, and judging the practical effect of the CONTRADICTION or of R1, needs runtime evidence. A full A3 → MASTER handoff is **not** eligible yet. This package is eligible for **A3 static-scope challenge only**.

## 7. Limitations

- No runtime was executed and no runtime result is claimed. A static PASS confirms only the source reading.
- Framework behaviour (record-rule union across groups, `ormcache` lifetime, group implication for admins) comes from outside the module files and is routed to runtime.
- Cross-module grants (G2) and company rules (G3) were not searched in other modules.
- JS assets and tests were not read (G1).
- No percentages, no Formal Coverage claim and no git operations. The inputs were not edited. Clean room: paraphrase and pointers only.
