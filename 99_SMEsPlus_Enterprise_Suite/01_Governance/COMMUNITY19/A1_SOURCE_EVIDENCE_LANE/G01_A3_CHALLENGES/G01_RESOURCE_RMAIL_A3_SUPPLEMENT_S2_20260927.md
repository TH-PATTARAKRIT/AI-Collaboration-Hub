# MASTER registration — A3 divergence supplement (resource / resource_mail)

- Registered by: MASTER (Claude Code), 2026-09-27
- Source: second independent A3 pass (scratch), sha256 801fa35809693ebe98efce2874cc4d0a6ac20ecf23aa2d432a3d9bf7b8ed8dc4
- Committed A3 files (G01_RESOURCE_A3_STATIC_20260927.md, G01_RESOURCE_MAIL_A3_STATIC_20260927.md) are NOT modified (append-only lineage).
- MASTER disposition rule: where two independent A3 passes diverge, the stricter result governs.
  - resource: A3 STATIC PASS WITH DEFECTS — defects = committed D01/D02 + supplement S-A..S-F (LOW / LOW-MED); S-G INCONCLUSIVE.
  - resource_mail: upgraded from "STATIC PASS" to **A3 STATIC PASS WITH DEFECTS (LOW; route to REC)** per M-A/M-B.
  - N1–N7: new runtime-bound candidates; routed to REC/Proof remediation batch as UNKNOWN_PENDING_PROOF.
- Process note: the pass reported "stopped at intake" in error before completing; its findings are adopted on content, not on the original report.

---

# A3 supplementary challenge log (second independent A3 pass) - resource / resource_mail - 2026-09-27
Status: SCRATCH ONLY. Governed outputs G01_A3_CHALLENGES/G01_RESOURCE[_MAIL]_A3_STATIC_20260927.md were already written and committed (37823e6) by a replacement A3 pass; this pass did NOT overwrite them.
Intake 15:11Z: all 10 inputs and 2 lineage files matched the hashes recorded upstream (e.g., PROOF fd150aaf..., REC e2adc10a..., RMAIL PROOF c15b9e11...). Blobs re-verified with git hash-object (13 files + 2 views): all match.

## Agreement with the committed A3 files
- C06 CONTRADICTION upheld (calendar 123-138); C01 upheld; unbounded rate upheld; naive-as-UTC mechanism upheld; Thai arithmetic reproduced (15:00-24:00 BKK; 2.0 h vs 8 h; one 2026 offset, +07:00); R1 upheld; lineage one-line R4 diff = accuracy fix, dispositions 21/0/10 and 6/0/3 intact.
- REC-24 wording (company-less calendar rate "falls back to 100") drops A2's caveat; default_get (calendar 56-59) seeds the reference -> CHALLENGE-SUSTAINED REC, and PROOF (R06 expected). (= committed D01/D02)

## Additional challenges from this pass (not in the committed resource file)
S-A GAP/CONTRADICTION items that have no runtime proof requirement: REC-RSRC-06, 11, 19, 20, 27, 28 are linked to static cases only. REC-28 depends on the framework (does the admin group imply erp_manager?); REC-19 reachability (a two-week calendar with no sections is reachable only by non-form writes, because the form onchange raises when there is not exactly one section per week); REC-27 destructive toggles. -> CHALLENGE-SUSTAINED (PROOF case design; REC routing). LOW-MED.
S-B Lane B label: REC defines NOT_APPLICABLE as "static declaration", yet applies it to runtime-observable behaviour: REC-RSRC-06, 12 (date validation), 13 (DB check), 16 (provisioning), 18 (tz defaults), 19; REC-RMAIL-02 (random colour). -> CHALLENGE-SUSTAINED (REC), LOW. No FAIL-for-absence misuse found.
S-C Materiality overclaim: REC section 7 / A2 section 4 say naive-as-UTC "is material (7-hour shift)" without a condition. The rule matches the framework convention (stored datetimes are naive UTC; plan helpers also return naive UTC via to_timezone(None)), so harm arises only for a caller that passes local naive values, and no such caller is identified. -> CHALLENGE-SUSTAINED (REC; A2 origin), LOW. The arithmetic and the PROOF labelling are correct.
S-D PC-RSRC-10 falsifiability: its fail branch "source treats naive as local" duplicates PC-09, and the only independent branch is a tzdata fact. It adds no independent source evidence yet counts in the 21 PASS. Recommend relabelling it ILLUSTRATION. -> CHALLENGE-SUSTAINED (PROOF), LOW.
S-E The PROOF header records upstream A1/A2/Lane A hashes but not the sha256 of the REC file it consumed (both modules). REC was finalized (>=15:05Z, committed 15:06:51Z) after static execution (15:03:30-15:05:00Z), and the predeclared cases are keyed to A1/A2 ids, not REC ids. -> CHALLENGE-SUSTAINED (PROOF lineage), LOW; REC-before-PROOF freeze order INCONCLUSIVE.
S-F Clean room: PROOF uses literal code tokens beyond pointers ("range(100)", the parity expression "floor((ordinal - 1) / 7) mod 2", "0.000001", "12 +/- duration"). No code blocks anywhere. -> CHALLENGE-SUSTAINED (PROOF), LOW. Recommend paraphrase.
S-G Predeclaration independence: the predeclared cases name fields and defaults (compute_leaves default, full_time_required_hours, time_type 'leave', hour_from/hour_to, work_time_rate) that appear in no upstream document. They come either from prior knowledge or from reading the source between 15:02:02Z and 15:03:14Z. -> INCONCLUSIVE.

## A3 source-visible candidates (new; no stage claims them; runtime-bound)
N1 calendar 202-208: the global-leave compute fires on ANY company change, including to empty (unlike the attendance compute at 174, which requires a non-empty company). Clearing a calendar's company clears its global leaves; whether they are deleted or orphaned into calendar-less leaves (which then apply to all calendars, REC-20) depends on the framework.
N2 calendar 515/535: the company guard applies only when a resource is given. Calendar-level computations (plan_days, get_work_hours_count, unusual days without company_id) therefore subtract calendar-less leaves of any company visible to the caller.
N3 calendar 1011-1018: the cached weekday lookup counts section rows (Monday, week 0/1) and break rows as worked, and its cache key is the calendar id only. It has no caller in the module files.
N4 leaves 65-67: the fallback reads company on the whole recordset, so a batch compute with more than one leave and no user/context tz may raise a singleton error.
N5 calendar 307-310: leaving two-week mode also silently turns duration-based off (F-09 omission).
N6 R1 precision: the tz is frozen by the first MATCHING (leave, resource) pair, not the first resource. Because clipping compares aware instants, the likely effect is limited to output tzinfo and to whole-day widening of flexible leaves (_handle_flexible_leave_interval).
N7 calendar 615-625: overlap is tested on one weekly timeline (day x 24 + hour). Out-of-range hours (REC-05/23) can therefore collide across adjacent days; "per weekday" is an approximation.

## resource_mail additions
M-A REC-RMAIL-06 exposure list is incomplete. The resource also exposes the linked user's avatar image (resource_resource.py 39, 61-64; a plain compute, not a related field, so it may run with the caller's rights: framework, INCONCLUSIVE) and the linked-user reference. -> CHALLENGE-SUSTAINED (REC; A2 origin), LOW. The committed file records "No challenge sustained".
M-B Same Lane B label issue as S-B (REC-RMAIL-02). Same REC-hash lineage gap as S-E.
Upheld: C01-C05; PC-RMAIL-01/02/03/04/06 re-executed (read expands an empty list to fields_get, which filters by field read access: models.py 3349-3370, 3474-3496).
