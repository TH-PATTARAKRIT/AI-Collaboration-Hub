# G01 PLATFORM_BASE — Module `resource` — RED TEAM A3 Independent Challenge (STATIC scope)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3, the independent adversarial challenger |
| Independence | This A3 wrote none of Lane A, A1, A2, REC or PROOF for `resource`. An earlier A3 attempt stopped at intake and produced no output. This attempt starts fresh and reuses none of it. |
| Date | 2026-09-27 (intake 15:1xZ; exit check 2026-09-27T15:14:44Z) |
| Scope | STATIC only (SOURCE and CONFIG). Runtime cases PC-RSRC-R01..R10 are **NOT-EXECUTED**. They are neither passed nor failed. |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`. A3 fetched the files itself and checked each against the recorded blob with `git hash-object` (section 2). |
| Question lineage | Standard 55 only (W1-STD). MVQ lineage is unavailable (GMVQ backlog). |
| **Overall disposition** | **A3 STATIC PASS WITH DEFECTS (route to REC; PROOF)**. There is one sustained low-severity challenge (A3-RSRC-D01) and one wording defect in a runtime case (A3-RSRC-D02). The CONTRADICTION, all 9 UNKNOWN_PENDING_PROOF items and all 10 runtime cases stay open. MASTER handoff is pending runtime. |

### Intake hashes (sha256; scratch `a3_rsrc2/intake.sha256`, file sha256 `83440c1f74652ebbdd221089867ffa8e13ec7518570e85dd5ae5e56515646520`)

Paths are relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`.

| Input | sha256 |
|---|---|
| G01_LANE_A_PASS1/G01_RESOURCE_LANE_A_PASS1_20260927.md | 6148482c3278b841ef5fa5191c8fd9d3dd9b2c87244046d4f1fb6643cd8ceffd |
| G01_A1_PACKAGES/G01_RESOURCE_A1_PACKAGE_20260927.md | c7f17c210f6f4abca84a26d2f024d774577b56cdfaf0b9febe4d7d1b453a0d7d |
| G01_A2_REVIEWS/G01_RESOURCE_A2_REVIEW_20260927.md | 23b99cd698b4aa630616e99dba28d4080c5fc8e4e95fc1242f122c6a04b3f4a0 |
| G01_RECONCILIATION/G01_RESOURCE_REC_20260927.md | e2adc10a1f346bb5dc1fe73100d3187c485a1208c12af6bc3a4732475a0fe259 |
| G01_PROOF/G01_RESOURCE_PROOF_20260927.md | fd150aaf3e72454260994ef66f93a61f38a095a96ed0958da728ee4e21578e89 |
| ../GMVQ/G01_PLATFORM_BASE/QUESTION_BANK_STANDARD_55_V2.00.md | f6726f111932aecce4432daf3e412d0c9de3291fa45fa8908e9e89ee79cb540d |

**Exit check:** at 15:14:44Z, `sha256sum -c` gave OK for every input. The inputs are unchanged and none was edited.

## 2. Blob re-verification (by A3)

A3 fetched each file from raw.githubusercontent at the anchor and ran `git hash-object` on it (scratch `a3_rsrc2/blobs.txt`). Every file matched:

| File | Blob |
|---|---|
| resource/models/resource_calendar.py | 335a857625070669ad79bd701fb38be03ec5704a |
| resource/models/resource_calendar_attendance.py | d8fb69b117b5c395eedfc213a31e8480f4c79936 |
| resource/models/resource_calendar_leaves.py | 841053e65b7f2ea6693f4fa18d3e98eb7e821fe4 |
| resource/models/resource_resource.py | aad3af2f8b87bff4cc650819abc2856fdb826067 |
| resource/security/ir.model.access.csv | 34ca64a5e94929feffacb29fae63b73e78a0b3c7 |
| resource/security/resource_security.xml | 500b70f06c5fb917bd5657bbaaf23843920dae0c |
| odoo/tools/date_utils.py (framework) | bde8a94337dd936b2a3b7af5f0ab066d33555e74 (equals the value PROOF recorded) |

## 3. Challenge log

### CH-1 — Re-derive REC items from source

| Target | A3 re-derivation (paraphrase, with pointers) | Disposition |
|---|---|---|
| REC-RSRC-06 CONTRADICTION (C06) | calendar : 126–130. The section error needs three things at once: two-week mode, at least one section row, and a first row by sequence that is not a section. A two-week calendar with no sections passes. The check also inspects only the **first** row, so "every slot under a week section" is not enforced even when sections exist. The overlap check (126–138, 615–625) filters to week type first or second in two-week mode. Rows with no week type (attendance : 40–43, default empty) escape it. The micro start offset allows contiguous slots. So the A2 side holds, and the A1 wording is refuted. The CONTRADICTION class is correct, since A2 cites source against an explicit A1 statement. | **UPHELD** (stays CONTRADICTION; not closed) |
| REC-RSRC-01 (C01): no company rule on calendars or attendances | resource_security.xml has 5 rules. Four are on leaves (3 by group plus 1 global company rule) and one is a global company rule on resource. There is none on calendar or attendance. The calendar company field has only a selection domain limited to the session's companies (calendar : 72–74). The claim is confined to the module, as A1 G3 (other modules) records. | **UPHELD** (runtime R01 pending) |
| REC-RSRC-08 / REC-24 (C08, OM-06): unbounded rate | calendar : 116–117 and 250–257. The rate is weekly hours divided by the reference, times 100, with no clamp. It is 100 when the reference is empty or zero. The help text states a 0–100 range. The search method (259–279) filters in memory with no bound. The rate field is **not stored** (no store flag), while the reference field is stored and editable (93–95). **However**, REC-24 says company-less calendars "get no computed reference, so the rate falls back to 100". That drops A2 F-04's own caveat ("unless a create-time default populated it"). In the source, default_get (56–59) seeds the reference from the company default calendar of the default company, which is the session company unless a company is given. The field is also user-editable. The compute only skips company-less records (159–161); it does not zero them. So falling back to 100 is conditional, not general. | C08 part **UPHELD**. REC-24 wording: **CHALLENGE-SUSTAINED (REC)**, see D01 |
| REC-RSRC-09 / PC-RSRC-10 (C09): naive input read as UTC; Thailand +7 h | calendar : 815–818 (hour count) and 727–730 (unusual days) replace a missing tz with UTC. 843–844 and 864–865/909–910 use the framework helper, which adds UTC when tz is missing (date_utils : 90–92). 328 and 506 assert tz-aware input. A3 recomputed with stdlib: naive 08:00–17:00 read as UTC is 15:00 on 1 Oct to 00:00 on 2 Oct in Bangkok, a +7 h shift. Asia/Bangkok has a single offset through 2026. With a Bangkok calendar of 08–12/13–17, only 15:00–17:00 on 1 Oct falls inside the window, which gives 2 h against the intended 8 h. **The reading is correct.** It is **not overclaimed**: PROOF labels it stdlib arithmetic, not Odoo runtime, and routes it to R07. One scope note, which is not a defect: a helper that finds the nearest working time (calendar : 671–672) **rejects** naive input with an error rather than reading it as UTC. The REC summary "naive input read as UTC" is therefore true for the listed entry points (as A1 C09 and PC-09 scope it) but not for every entry point. | **UPHELD** (scope note O-1) |
| PROOF R1 (REC-12/09): leave lookup reuses the first resource tz | calendar : 537. Inside the nested leave × resource loop, the tz argument is overwritten on the first pass when it was not given, and every later resource **and later leave** in the same call reuses it. The static fact is confirmed. PROOF correctly records it as a runtime candidate, not a claim. | **UPHELD** (runtime) |
| REC-RSRC-21 / 26 (OM-03, OM-08) | leaves : 36–38 and 59–61. The leave company is the calendar company, else the environment's active company, and it is stored and readonly. calendar : 535 skips a resource-less leave for any non-empty resource whose company differs, so a company-less resource never matches a populated leave company. Refinement: the compute depends on the calendar, so a later change of calendar recomputes the company from the **modifier's** active company, not only the creator's. | **UPHELD** (refinement O-2) |
| REC-RSRC-04 (C04) | ACL: leaves are full for the internal user group. The modify rule requires a resource set and a resource user that is none or self. Any internal user can therefore modify leaves of user-less resources, subject to the global company rule on leaves. | **UPHELD** (runtime R03 pending) |

### CH-2 — Re-executed static PASS cases

| Case | A3 re-execution | Falsifiability of the predeclared Expected/Fail | Disposition |
|---|---|---|---|
| PC-RSRC-01 | 5 rules, none on calendar or attendance. Confirmed. | Strong (exact count plus model list) | UPHELD |
| PC-RSRC-02 | 8 ACL rows. Resource read-only for both groups; calendar and attendance read for users and full for system; leaves full. Confirmed. | Strong | UPHELD |
| PC-RSRC-04 | The attendance file's only constrains decorator is on the day period (61). The hour clamp and ordering sit in an onchange (50–59). No create or write override exists. Confirmed. | Strong | UPHELD |
| PC-RSRC-05 | The duration inverse is 12 ± d (or ± d/2 for a full day), with no bound. Confirmed. | Adequate | UPHELD |
| PC-RSRC-06 | See CH-1. Confirmed. | Strong (either alternative is falsifiable) | UPHELD |
| PC-RSRC-07 | calendar : 879–897 and 920–939. Each helper has two loops of range(100) over 14-day steps and returns False. Confirmed. | Strong | UPHELD |
| PC-RSRC-08 | The mechanism is confirmed. The case is also marked PASS for REC-24, but its predeclared Expected covers only "derived from company calendar on hours change", and its Fail condition is only "clamp/constraint present". **Neither condition tests the company-less "rate 100" statement.** The observation cell itself records the default_get copy, which undercuts that statement. | **Weak for REC-24** | CHALLENGE-SUSTAINED (PROOF), see D01 |
| PC-RSRC-10 | Recomputed (CH-1). | Adequate. The "2 h vs 8 h" illustration was added after predeclaration and is labelled illustrative. | UPHELD |
| PC-RSRC-15 | attendance : 68–75. Epoch-ordinal week parity, no ISO call. Confirmed. | Strong | UPHELD |
| PC-RSRC-18 | calendar : 1011 caches the working-hours lookup per calendar id. A3's grep of the fetched module files found no clear or invalidate call. | Adequate, but limited to module files (framework-level invalidation is out of static reach) | UPHELD |

Other weak or generic predeclared Fail conditions (flagged, verdicts not changed): PC-RSRC-14 ("Missing"), PC-RSRC-19 ("Deviation") and PC-RSRC-03 (a one-directional fail that tests only exclusion of user-less resources). All are falsifiable in principle, but loosely.

### CH-3 — Predeclaration integrity

| Check | Finding | Disposition |
|---|---|---|
| Predeclared file | Scratch `rec_rsrc/PROOF_CASES_PREDECLARED.md` has sha256 `14159fb2…114de`, equal to the value PROOF records. It was born 15:03:14.632Z and last modified 15:03:14.638Z. The `.ts` sidecar reads 15:03:14Z. | UPHELD |
| Ordering | The `src/resource` fetch directory is timestamped 15:02:01Z, before predeclaration and consistent with "fetch and hash only". The framework fetch (`src/odoo`) is 15:04:10Z and `thai_case.txt` is 15:04:25Z, both after predeclaration. | UPHELD |
| Blob log | `blob_log.txt` was born 15:07:37Z. That is **after** the stated execution window (15:03:30–15:05:00Z) and after the stated blob-verification time (15:02:02Z). The log was written later than the verification it records. This does not show tampering, because A3 re-verified every blob independently. | INCONCLUSIVE (record-timing note O-3) |
| Case content | The executed cases match the predeclared Expected conditions. The observation additions (R1–R4 and the 2 h/8 h illustration) are labelled refinements and change no verdict. | UPHELD |

### CH-4 — Lineage

See section 4.

### CH-5 — Overclaim, Lane B, Standard 55 and clean room

| Check | Finding | Disposition |
|---|---|---|
| Overclaim | The dispositions are "PROOF PARTIAL" and "REC COMPLETE — HANDOFF TO PROOF". No runtime result is claimed, no UNKNOWN_PENDING_PROOF item is closed, and there are no percentages and no Formal Coverage claim. The only overclaim found is REC-24 (D01). In runtime case R06, the Expected "150 shown/stored" is inaccurate because the rate field is not stored (D02). | See D01, D02 |
| Lane B misuse | No Lane B evidence exists. Its absence is shown as UNCORROBORATED or NOT_APPLICABLE and never as FAIL. No Lane B material is used as source. | UPHELD |
| Standard-55 fit (3 sampled) | REC-01 maps to Q27/Q28/Q49 (company scope and cross-boundary): good fit. REC-09 maps to Q50 (time zone and date boundary): good fit. REC-05 maps to Q54 (every path enforces the same controls; the onchange-only clamp is bypassed by RPC and import): good fit. No QID is claimed as answered. | UPHELD |
| Clean room | The 5 input files have 0 fenced code blocks. Identifiers such as method names, `range(100)` and `__init__` appear only as evidence pointers, with no reproduced logic. This A3 file paraphrases in the same way. | UPHELD |

## 4. Lineage adjudication

| File | Commits (`git log --follow`) |
|---|---|
| G01_PROOF/G01_RESOURCE_PROOF_20260927.md | `69d312f` 15:09:02Z "in-flight REC/Proof/A3 artifacts checkpoint" (133 lines added); `6302d8f` 15:10:22Z "SMEsPlus REC/Proof G01: resource, resource_mail" (1 line changed) |
| G01_RECONCILIATION/G01_RESOURCE_REC_20260927.md | `47a33b7` 15:06:51Z "in-flight … checkpoint" (added; no later change) |

- **The post-checkpoint diff (`6302d8f`)** is one line in refinement R4. It changes "Leave date defaults use the user tz" to "The default leave end date (end-of-day fill) uses the user or context tz". A3 checked it against leaves : 64–72, which read the environment tz and fall back to the company calendar tz only when neither the user tz nor the context tz is set. The new wording is **more accurate**. It touches a "no verdict changed" refinement. The counts **21 PASS / 0 FAIL / 10 NOT-EXECUTED are intact**, and the 28-item REC counts are unchanged.
- **Authorship:** every commit carries the same author identity and the same session trailer, so git metadata cannot tell stage agents apart. The commit title "REC/Proof G01: resource, resource_mail" matches the Proof controller's own scope. Nothing indicates that a non-author changed the content, but git cannot prove who authored it. **Adjudication: content integrity UPHELD. Author attribution INCONCLUSIVE from git alone.** The change is non-substantive.
- **Hygiene note (routed to Integration Control):** the first commits of both the REC and the PROOF file are "in-flight checkpoint" commits that also carry other modules' files. This is cross-stage commit bundling. It is not a content defect.

## 5. Defects routed

| ID | Severity | Owner stage | Defect | Required action |
|---|---|---|---|---|
| A3-RSRC-D01 | LOW | REC (primary), PROOF | REC-RSRC-24 says company-less calendars' rate "falls back to 100" without A2 F-04's caveat. The source shows the reference is seeded by default_get from the default (session) company's calendar and is user-editable, so 100 happens only when the reference is empty or zero. PC-RSRC-08 marks REC-24 PASS without a predeclared Expected/Fail that tests this statement. | REC: restore the conditional wording. PROOF: add a falsifiable static or runtime case (for example, a company-less calendar created with a session company whose calendar has a non-zero reference, and a check of whether the rate is 100). Carry it into R06. |
| A3-RSRC-D02 | LOW | PROOF | In PC-RSRC-R06, the Expected "150 shown/stored" is wrong on "stored": the rate is a non-stored compute. The R06 Expected "company-less calendar shows 100" inherits D01. | Correct the R06 Expected/Fail before runtime execution. |

Non-blocking observations (no routing required): O-1, the nearest-working-time helper rejects naive input (it does not read it as UTC); a scope note for REC-09. O-2, the leave company can be recomputed from the modifier's active company on a calendar change (REC-26). O-3, the blob log was written after the stated window.

## 6. Runtime-blocked items (NOT-EXECUTED — neither passed nor failed)

- PC-RSRC-R01..R10 (A2 PR-01..PR-10). These cover the company-rule effect, the admin write grant, the user-less-leave CRUD, RPC/out-of-range hours, the plan cutoff, rate display (fix D02 first), naive/DST/Thai behaviour, cache staleness, caller-rights leave lookup, and company-less global leaves.
- The practical effect of the REC-RSRC-06 CONTRADICTION and of rows with no week type (R3). The mixed-tz effect of R1. The elevation of related fields and the record-rule union (framework).
- All 9 UNKNOWN_PENDING_PROOF items stay open.

## 7. Limitations

- Static only. A3 re-read the module files listed in section 2 plus one framework helper. JS assets, tests and other modules (G1, G2, G3) were not read, and the cross-module grants and company rules stay open.
- Framework behaviour (cache lifetime, computes that leave a stored field unassigned, rule unions) is inferred, not proven.
- No percentages, no Formal Coverage claim and no QID answered. Git was used read-only. The inputs were not edited. Clean room: paraphrase and pointers only.
