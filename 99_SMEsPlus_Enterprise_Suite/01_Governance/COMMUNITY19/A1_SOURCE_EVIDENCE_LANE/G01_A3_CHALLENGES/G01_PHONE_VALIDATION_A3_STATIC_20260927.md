# G01 PLATFORM_BASE — Module `phone_validation` — RED TEAM A3 Independent Challenge (STATIC scope)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3, independent adversarial challenger. A3 did not author Lane A, A1, A2, REC or Proof for this module. |
| Group / module | G01 PLATFORM_BASE / `phone_validation` |
| Date | 2026-09-27 (intake 15:16:17 UTC; first A3 source fetch 15:16:53 UTC) |
| Scope | STATIC only (source, config, cross-module static reads). Runtime NOT-EXECUTED: neither passed nor failed. |
| Intake hashes (A3 recomputed; scratchpad `a3_phon_priv/intake.sha256`, sha256 `49747416…4888`) | Lane A `069aca00…b888`; A1 `e128cb2e…c003b0`; A2 `60bccae9…33ec`; REC `87a34f17…a7187a717`; Proof `c0b58670…ca9`; bank `c70aae33…0a50b8a80`; FREEZE_W1-B10 manifest `049aa570…56d8`. All equal the values recorded by the upstream stages and by the REC/Proof output log. |
| Freeze basis | W1-B10. Bank sha256 equals manifest `bank_files`. A3 recomputed the freeze hash read-only from batch id + module list + both bank files (method of `freeze_batch.py`): `0d7f6e94acde38662de420f8947ffaa1ab04cddaaec43516e46b441ce1222010` = manifest. QID lineage is A3-eligible. |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`. A3 fetched independently; blob log `a3_phon_priv/blob_log.txt` (sha256 `d720c3c7…14b8`). |
| Lane B | None exists for this module (REC 0.2). Not used by A3. |
| **Overall disposition** | **A3 STATIC PASS WITH DEFECTS (route to PROOF, REC, A2) — MASTER HANDOFF PENDING RUNTIME.** No challenge overturned a verdict. Sustained challenges are LOW and do not block; all 10 runtime cases remain NOT-EXECUTED. |

Clean-room note: neutral paraphrase only. Identifiers are evidence pointers. No vendor code, schema or workflow reproduced. No percentages. No Formal Coverage claim. Git used read-only. Inputs not edited.

## 2. Challenge log

### CH-1 PR-PHON-01 wrong-subject suppression and mirror R1 — **UPHELD** (refutation attempts failed)

Independent re-derivation at the anchor (blobs verified: list model `d94486f6…`, generic helpers `dccf9fbf…`, mixin `01ca256f…`, base users `9d42d77a…`, base partner `502616ef…`):

1. Public add formats the input on the acting user's record with raising off. The formatter catches the parse error and returns empty. No emptiness check before the internal add.
2. Internal add first looks up existing entries with the (empty) list, then calls create with the empty value.
3. Create formats each value on the acting user's record with raising on. The generic formatter, when given no number, requires a singleton (the user is one) and takes the first non-empty discovered number field of that record. On users, "phone" is exposed through partner delegation; base defines no "mobile" field. The acting user's own number is then formatted and becomes the entry's value. If the user has no number, the formatter returns empty (raising does not trigger), and the failure comes later from the required-field check.
4. The mixin set/reset helpers pass each record's sanitized value (empty when absent) to internal add/remove under sudo. A3 confirmed the elevation helper changes only the superuser flag in the environment, not the user id, so step 3 still resolves to the acting user.

Refutation attempts made by A3:
- **Earlier guard that raises on empty?** None in add, internal add, the mixin helpers, or create. The required-field check fires only when the substituted value is itself empty.
- **Does the ORM skip the custom number search for a stored field, or drop the empty value first?** Checked the anchor ORM domain optimizer (`odoo/orm/domains.py` blob recorded in the A3 blob log). The field's search method is honoured at full optimization level for any field that declares one, stored or not. The optimization that removes null values from "in" conditions on required fields applies only when the field type has no falsy value. Text fields declare an empty string as their falsy value (`odoo/orm/fields_textual.py`), so the empty value is **not** removed. The number search therefore receives it and maps it to the acting user's number.
- Result: the lookup inside internal add (Proof R2) and the lookup inside internal remove (Proof R1) both resolve to the acting user's number.

R1 re-derived: remove with an unformattable input, or reset on a record with no sanitized number, finds the acting user's entry (active or archived) and archives it (un-suppression). If no entry exists, a follow-up create makes an **archived** entry for the acting user's number. This is a false "unblocked" event.

Bounded caveat (not a refutation): in-module UI paths do not feed an empty value. The record-level add uses the stored number, and the portal-deletion override adds only non-empty formatted numbers. Reachability of the defect depends on callers outside the module (SMS/marketing consumers, RPC by administrators). Those callers were not read by any stage. Runtime PC-PHON-01 calls the methods directly, so it confirms the mechanism, not UI reachability.

### CH-2 Severity (SF-PHON-01 HIGH; R1) — **CHALLENGE-SUSTAINED (A2, LOW)**

A3 concurs with HIGH for SF-PHON-01. A2 did not state the removal direction (R1). R1 lifts an existing objection for the acting user with no request from them. Its consequence is at least as serious as the add direction. It should carry the same HIGH rating under SF-PHON-01, not remain a Proof "refinement" that "does not change any verdict". Route: A2 (severity statement) and REC (fold into REC-21 / Q013; this is already mapped).

### CH-3 Proof static PASS re-execution (≥3) — **UPHELD, with one weak case sustained**

| Case | A3 re-execution | A3 result |
|---|---|---|
| PC-PHON-11 | Add/internal add: no guard; empty value forwarded (CH-1 steps 1–2) | Confirmed |
| PC-PHON-12 | Create → user formatter → fallback to the user's number field; empty return even with raising on | Confirmed |
| PC-PHON-14 | Set/reset helpers pass sanitized value under sudo, unguarded; sudo keeps user id | Confirmed |
| PC-PHON-15 | Write reformats through the user formatter with raising on; number search maps each term (empty included) through the formatter | Confirmed (empty string and null both reach the search method; see CH-1) |
| PC-PHON-18 | Wizard apply calls internal remove unelevated with the raw wizard phone; wizard ACL system-only | Confirmed |
| PC-PHON-24 | ACL: all-zero ungrouped row on the list; system full rights on the list and wizard | Confirmed |
| PC-PHON-23 | Override collects non-empty formatted numbers, calls the base hook, then internal add unelevated; base hook archives the user as superuser | Mechanics confirmed. **Weak PASS:** the predeclared expectation included recording caller elevation. The portal controller was not read, so that element was not met. It should be PARTIAL, not PASS (static only). Route PROOF (LOW). |

Weak-condition notes (no route): PC-PHON-13's fail condition considers only this module's overrides. A module that adds a "mobile" field to partners/users would change which field the fallback reads, but not whether a fallback happens. PC-PHON-11..15 are phrased so that PASS equals "defect present". That is correct for this proof, but MASTER should read PASS as "prediction confirmed", not "behaviour acceptable".

### CH-4 Predeclaration timing — **UPHELD, wording defect sustained (PROOF, LOW)**

Scratchpad evidence: predeclared file mtime 15:05:54.96; its hash record 15:06:04.872; fetch-time marker 15:06:04.877; earliest fetched source file mtime 15:06:05.15. Hash `cf3bdece…ea83` recomputed and matches. Order: predeclared, then hashed, then fetched. Verified. However, the Proof header "Source anchor" row says "fetched 15:06:04–05 UTC", which contradicts "first fetch 15:06:05" in the row above. The marker time, not a download, explains the 15:06:04 value. Correct the wording.

### CH-5 QID lineage fit (sample 4 + the "no evidence" QID) — **UPHELD; Q039 CHALLENGE-SUSTAINED (REC, LOW)**

- Q003 (malformed input must not silently become another valid number) → REC-21/O-01: direct fit. CH-1 is the disconfirming observation pattern.
- Q013 (removing an unseen number must not affect a different identity) → REC-13, REC-21 (R1): direct fit, confirmed by CH-1.
- Q029 (no crossing of customer boundary) → REC-03: fit (entries are global, no company attribute).
- Q031 (no enumeration without list access) → REC-06, REC-24/O-04: fit (flag search open to internal users; flag computed under sudo).
- Q039 "no evidence": partially disputed. The retry clause ("retry changes the state twice") has static evidence: add is idempotent (existing entries returned or reactivated, unique number) and remove is idempotent (archive). REC-12/REC-13 (and REC-29/GAP-09 for concurrency) are topically relevant. The first clause (outcome knowable before retry) remains runtime/UX. Route REC: map Q039 → REC-12, REC-13, REC-29 as partial lineage. Lineage only; the QID is not answered.

### CH-6 Overclaim, Lane B, clean room, PDPA — **UPHELD with one LOW wording note (A2)**

- Overclaim: A1 BR2 ("removal never a hard delete, through the API") is scoped correctly to the API; A2 SF-PHON-06 covers ACL hard delete. A1 missed SF-PHON-01 (an omission, correctly caught by A2). No percentages, no Formal Coverage wording found in the ten inputs.
- Lane B: none exists; REC marks every Lane B cell UNCORROBORATED/NOT_APPLICABLE and never FAIL for absence. No misuse.
- Clean-room scan (code-like tokens, query text, framework calls) over all inputs: none found. Identifiers appear only as pointers.
- PDPA: REC section 4 is neutral and states design implications only. A2 SF-PHON-06 ("Under a GDPR/PDPA-style regime a suppression entry is itself personal data kept to honour an objection") reads as a legal characterization. Rephrase it as a design-implication statement. Route A2 (LOW).

### CH-7 Stage ordering in REC — **CHALLENGE-SUSTAINED (REC, LOW)**

REC section 6 states it used "the static proof results from Stage 2" for classification support, and cites PC-18/22/26 and Proof R1. REC classes did not change (contradictions stay CONTRADICTION), so no verdict is affected. Still, a REC record that cites downstream Proof weakens stage independence. REC should mark these citations as post-Proof annotations.

## 3. Lineage

| Artifact | sha256 (A3 intake) | Commit (read-only `git log --follow`) | Working tree |
|---|---|---|---|
| Lane A PASS-1 | 069aca00…b888 | 9f74da8 (Lane A G01 PASS-1: phone_validation, privacy_lookup) | clean |
| A1 package | e128cb2e…c003b0 | 4a500d1 (message names web/web_tour/portal/utm) | clean |
| A2 review | 60bccae9…33ec | 0aad8c0 (message names base_sparse_field/google_recaptcha) | clean |
| REC | 87a34f17…a7187a717 | 811e8ae (message names base_sparse_field/google_recaptcha) | clean |
| Proof | c0b58670…ca9 | 91bc1d4 (in-flight checkpoint) | clean |
| Bank | c70aae33…0a50b8a80 | 309c45d | clean |
| FREEZE_W1-B10 | 049aa570…56d8 | f59a44a, 2d768ed | clean |

Each stage file has a single commit and the committed content equals the intake. Observation (LOW, route Integration Control): four of five stage files were committed in checkpoint commits whose messages name other modules. Hash lineage is intact. Commit-message provenance is not module-attributable.

Source blobs: A3 fetched 12 files at the anchor (7 module files, base users/partner, core mail tools, core SQL tools, mail models) plus 5 ORM files. Every module blob A3 fetched matches the Lane A/Proof values (list model, helpers, mixin, users override, tools, wizard, ACL). Base users `9d42d77a…` and base partner `502616ef…` match Proof. ORM files are new A3 lineage records (see blob log).

## 4. Defects routed

| ID | Severity | Route | Summary |
|---|---|---|---|
| A3-PHON-D1 | LOW | A2 / REC | R1 (removal-side wrong-subject un-suppression) confirmed. It should carry HIGH under SF-PHON-01, not remain a verdict-neutral refinement. |
| A3-PHON-D2 | LOW | PROOF | PC-PHON-23 recorded PASS although the predeclared caller-elevation element was not established. Reclassify as PARTIAL (static). |
| A3-PHON-D3 | LOW | PROOF | Header wording "fetched 15:06:04–05" conflicts with "first fetch 15:06:05". Correct it. |
| A3-PHON-D4 | LOW | REC | Q039 "no evidence": map partial lineage to REC-12/13/29 (retry idempotency clause). |
| A3-PHON-D5 | LOW | REC | Post-Proof citations inside REC classification basis. Annotate them as post-Proof. |
| A3-PHON-D6 | LOW | A2 | SF-PHON-06 legal-style characterization. Rephrase as neutral design implication. |
| A3-PHON-D7 | LOW | Integration Control | Commit messages do not name this module for A1/A2/REC/Proof. |
| A3-PHON-P1 | proposal | PROOF | Add a cross-module reachability case: identify a UI path in SMS/marketing consumers that feeds an empty sanitized value to the set/reset helpers. PC-PHON-28 (proposed) should also assert the absent-entry branch (an archived entry is created for the acting user's number). |

## 5. Runtime / gate-blocked items

- PC-PHON-01..10 NOT-EXECUTED (runtime device offline at Proof time). They are neither passed nor failed. No A3 result is inferred for them.
- The 13 UNKNOWN_PENDING_PROOF REC items stay open. C07 runtime effect (PC-02), cross-company effect (PC-04) and acting-user country (PC-10) are pending.
- GAP-02 (portal controller elevation) is open.
- MASTER handoff is pending runtime execution and a follow-up A3 runtime-scope challenge.

## 6. Limitations

- Static reading only. ORM runtime semantics beyond the files read (required-field enforcement timing, recompute order) were not executed.
- Callers outside the module (SMS, marketing, portal controller), mail's partner-field discovery, JS and tests were not read.
- The ORM domain-optimizer reasoning in CH-1 is a static reading of the anchor ORM. It needs runtime PC-PHON-01 / proposed PC-PHON-28 for confirmation.
- No percentages, no Formal Coverage claim. Git read-only. Inputs not edited.
