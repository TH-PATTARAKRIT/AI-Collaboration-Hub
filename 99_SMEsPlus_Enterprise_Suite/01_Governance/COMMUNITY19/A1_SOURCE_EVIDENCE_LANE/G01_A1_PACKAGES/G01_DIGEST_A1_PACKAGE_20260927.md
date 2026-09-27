# G01 PLATFORM_BASE — Module `digest` — RED TEAM A1 Package

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A1 (source-backed research synthesizer) |
| Governed group / module | G01 PLATFORM_BASE / `digest` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_DIGEST_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `d0f6ec30b0823ac82a20e0ae2b9b8261732d81383b2124a880becb3c49c62afe` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Freeze (topic lens only) | W1-B03, freeze_hash `1247c218ba4e2e6a57e259427030f4350881da56a5a28c59901a20f8b2d3a5d3`; bank `G01_DIGEST_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `1ba4226d…64d74ec` (matches freeze manifest); ELIGIBLE |
| Date | 2026-09-27 |
| Lane B dependency | None. A1 did not wait for, view, or use Lane B evidence. |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |

Bank used as a topic lens only (recipient scope, company aggregation, cutoff/timezone, failure/retry, unsubscribe, manual vs scheduled equivalence, privileged configuration). No QID answered; bank not edited. Paths relative to `addons/digest/` at the anchor.

## 1. Claims

| Claim ID | Claim (neutral WHAT / WHY / RISK) | Evidence (path @ blob) | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-DGST-C01 | WHAT: module sends periodic KPI summary emails to internal users; depends on mail, portal, resource; not auto-installed. | `__manifest__.py` @ 6ee68b6f (spot-checked hash) | HIGH | SOURCE-STATIC |
| A1-G01-DGST-C02 | WHAT: ACL grants ERP managers full CRUD on digests and tips; internal users read-only on both. | `security/ir.model.access.csv` @ 49ef3552 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-DGST-C03 | WHAT: no record rules ship; the digest carries an optional company (default current) but record visibility is not company-separated. RISK: any internal user can read digest and tip records of every company (recipients, KPI toggles), limited only by UI menu visibility. | `__manifest__.py`; ACL file; `models/digest.py` @ 3eea1c39 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-DGST-C04 | WHAT: the messages-sent KPI counts messages in the window by comment subtype and a set of message types (comment, email, outgoing email) with no company filter, unlike the connected-users KPI which uses the company-based helper. RISK: cross-company aggregation, bounded only by the recipient's own message visibility. | `models/digest.py` @ 3eea1c39 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-DGST-C05 | WHAT: company-based KPI helper filters by digest company (or current company if unset); users model filtered by its multi-company field. | `models/digest.py` @ 3eea1c39 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-DGST-C06 | WHAT: KPIs are evaluated as the recipient user under the recipient's company; an access error on a KPI drops that KPI silently from that recipient's email. RISK: recipients get different KPI sets with no indication of omission; zero/absent vs denied is indistinguishable to the reader. | `models/digest.py` @ 3eea1c39 (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-DGST-C07 | WHAT: each KPI has three windows (24 h, 7 d, 30 d) each compared with the preceding window as a margin; window anchor localized to company working-calendar timezone when set. | `models/digest.py` (Lane A only) | MED | SOURCE-STATIC |
| A1-G01-DGST-C08 | WHAT: KPI discovery is by field-name prefix, admitting custom/studio fields. RISK: any privileged field author can add a KPI whose company scoping is not enforced by the module. | `models/digest.py` (Lane A only) | MED | SOURCE-STATIC |
| A1-G01-DGST-C09 | WHAT: scheduler (daily, runs as root) sends activated digests with next date ≤ today; mail-delivery failures are logged and skipped; other exceptions are not caught in the loop. RISK: one failing digest of a non-mail type can abort remaining digests in that run. | `data/ir_cron_data.xml` @ a6c1d091; `models/digest.py` (both spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-DGST-C10 | WHAT: scheduled sends apply an automatic slowdown (escalate periodicity when no recipient logged in during the window); manual send skips it. WHY/RISK: manual and scheduled paths are not equivalent. | `models/digest.py` @ 3eea1c39 (spot-checked: slowdown gated by flag, manual path) | HIGH | SOURCE-STATIC |
| A1-G01-DGST-C11 | WHAT: tip description is an HTML field stored with sanitization disabled; tips are rendered as a template engine under elevated rights, then sanitized. Tips are editable by ERP managers (C02). RISK: template-evaluation surface executed with elevated rights by a privileged, non-system editor. | `models/digest_tip.py` @ 8c0208db; `models/digest.py` (both spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-DGST-C12 | WHAT: `set_periodicity` route is auth=user, checks ERP manager, validates the value, then changes the digest; it declares no method restriction (GET reachable) and is linked from the email. No ownership/company check on the target digest. RISK: state change via GET link; CSRF protection for GET is framework-dependent and unverified. | `controllers/portal.py` @ b0e76145 (spot-checked) | HIGH (route facts) / LOW (CSRF effect) | SOURCE-STATIC |
| A1-G01-DGST-C13 | WHAT: one-click unsubscribe is POST-only and CSRF-exempt (rationale: mail agent has no session); token = HMAC over (digest id, user id) with fixed scope, compared in constant time. | `controllers/portal.py`; `models/digest.py` (spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-DGST-C14 | WHAT: legacy unsubscribe route (GET/POST) without token works only for a logged-in internal user acting on self. | `controllers/portal.py` @ b0e76145 (spot-checked route methods) | MED | SOURCE-STATIC |
| A1-G01-DGST-C15 | WHAT: ACL layer uses ERP manager, but form buttons (send now, activate, deactivate) and recipient/KPI sections are shown only to system group; menus use ERP manager. RISK: ERP managers hold write rights on fields/actions the UI hides from them — UI group is not the enforcement boundary. | `views/digest_views.xml` @ e0dd92c6; ACL file (both spot-checked) | HIGH | SOURCE-STATIC |
| A1-G01-DGST-C16 | WHAT: recipients restricted to non-share users only via UI domain; no server-side constraint; auto-subscribe filters share users. | `models/digest.py`; `models/res_users.py` (Lane A only) | MED | SOURCE-STATIC |
| A1-G01-DGST-C17 | WHAT: emails are queued via elevated create, auto-delete; subject = recipient company name + digest name; sender = digest company email, else current user, else root. RISK: auto-delete limits delivery audit evidence. | `models/digest.py` @ 3eea1c39 (spot-checked subject/sender) | HIGH | SOURCE-STATIC |
| A1-G01-DGST-C18 | WHAT: new internal users are auto-added to the configured default digest when the setting is enabled (seeded on, default digest daily, admin recipient). | `models/res_users.py`; `data/*` (Lane A only) | MED | SOURCE-STATIC |
| A1-G01-DGST-C19 | WHAT: manual send also advances next date (shared routine). | `models/digest.py` (Lane A only) | MED | SOURCE-STATIC |

## 2. Business rules (source-derived, neutral)
- BR1: Only activated digests with next date ≤ today are sent by the scheduler (C09).
- BR2: Next date = today + 1 day / 1 week / 1 month / 3 months per periodicity (Lane A #10).
- BR3: KPI values are personal to the recipient's rights and company (C06), except messages-sent which lacks company filtering (C04).
- BR4: Up to one unseen tip per send, filtered by recipient's groups or unset group; consumed on send (Lane A #19).
- BR5: Unsubscribe requires a valid per-(digest,user) token, or a session of the user acting on self (C13, C14).
- BR6: Periodicity change via link requires ERP manager (C12).

## 3. States / transitions
- Digest: activated ↔ deactivated (explicit actions; system-group buttons in UI).
- Periodicity: daily → weekly → monthly → quarterly (automatic slowdown, capped; scheduled path only) (C10); arbitrary change by ERP manager via form or link (C12).
- Per-send: due → rendered per recipient → queued mail (auto-delete) → next date advanced; mail-delivery failure → logged, digest remains due.

## 4. Exceptions / failure modes
- KPI access error → KPI silently omitted for that recipient (C06).
- Mail delivery exception → skip, retry next run (C09); other exceptions uncaught (C09).
- Invalid periodicity value → value error; non-manager → forbidden (C12).
- Token mismatch → not found (C13).
- Margin is zero when either value is zero or equal — zero-data vs no-change indistinguishable (Lane A #15).

## 5. Cross-module handoffs
- `mail`: message model as KPI source, rendering mixin, outgoing mail queue, comment subtype, settings form.
- `portal`: unsubscribe confirmation layout. `resource`: company calendar timezone for windows.
- `base`: users (login date, share flag, groups, multi-company field), login log (slowdown), company/currency, config params, cron, HMAC helper.
- Extension surface: downstream apps add KPI pairs and KPI→action mapping; their company scoping is outside this module (GAP-DGST-02).
- No direct edge to `bus`.

## 6. Evidence gaps (carried forward from Lane A + A1)
- GAP-DGST-01 (Lane A G1): email template bodies read by structure only.
- GAP-DGST-02 (Lane A G2): downstream KPI contributors' company scoping unknown.
- GAP-DGST-03 (Lane A G3): framework CSRF behavior for GET on `set_periodicity` not evidenced.
- GAP-DGST-04 (Lane A G4): no server-side constraint blocking share users as recipients.
- GAP-DGST-05 (Lane A G5): cross-company aggregation of messages-sent KPI is runtime-unverified.
- GAP-DGST-06 (A1): no catch-up/dedup policy visible for missed runs beyond "remains due"; concurrency of overlapping runs not evidenced.
- GAP-DGST-07 (A1): no audit record of run scope/recipients beyond auto-deleted mail queue entries.

## 7. CRQ candidates
- CRQ-DGST-01: Must summary configuration records be company-isolated for visibility and editing? (C03)
- CRQ-DGST-02: Must every metric be computed within the recipient's active company scope, with no global counters? (C04, C05, C08)
- CRQ-DGST-03: Must omitted/denied metrics be labeled rather than silently dropped? (C06)
- CRQ-DGST-04: Must state-changing links require a non-GET, CSRF-protected or tokenized confirmation? (C12)
- CRQ-DGST-05: Must editable summary content be treated as data (no privileged template evaluation)? (C11)
- CRQ-DGST-06: Must the UI permission group and the enforced permission group for summary administration be the same? (C15)
- CRQ-DGST-07: Must manual and scheduled generation apply equivalent controls? (C10, C19)
- CRQ-DGST-08: Must one failing summary be isolated from others in the same run, with auditable run evidence? (C09, C17)

## 8. Contradictions
- None CONFIRMED-FROM-SOURCE as internal source contradictions.
- REFINEMENT (verified): Lane A #17 describes messages-sent as "comment-type messages"; source filters by comment subtype plus message types comment/email/outgoing email. Risk conclusion (no company filter) unchanged.
- CANDIDATE-DGST-X1: ACL group (ERP manager) vs UI-visibility group (system) for the same actions (C15) — layered-control mismatch, not a code contradiction.
- CANDIDATE-DGST-X2: Company field on digest implies company scoping, but no record rule enforces it (C03).

## 9. Spot-check log
Re-fetched from `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/digest/<path>`; `git hash-object` computed locally (scratchpad, no repo git operations).

| # | Path | Recorded blob | Computed blob | Match | Claim(s) verified in content |
|---|---|---|---|---|---|
| 1 | `security/ir.model.access.csv` | 49ef355262e6ea7d15eba86ab876f0e072ffedba | 49ef355262e6ea7d15eba86ab876f0e072ffedba | YES | C02, C15 (ERP manager CRUD; internal read) |
| 2 | `models/digest.py` | 3eea1c39f8c5aa53b6eb1a43acc986d7f0ed204c | 3eea1c39f8c5aa53b6eb1a43acc986d7f0ed204c | YES | C04 no company filter; C05; C06 recipient user/company + access-error skip; C09 mail-exception catch; C11 elevated render then sanitize; C13 HMAC scope; C17 subject/sender |
| 3 | `models/digest_tip.py` | 8c0208db9ad28ed2d8fc8f803cf245d75b04e078 | 8c0208db9ad28ed2d8fc8f803cf245d75b04e078 | YES | C11 sanitize disabled on tip HTML |
| 4 | `controllers/portal.py` | b0e76145b13ecdbc4b69fd7bdeddcfac66ae5ffc | b0e76145b13ecdbc4b69fd7bdeddcfac66ae5ffc | YES | C12 no method restriction + ERP-manager check + value validation; C13 POST/csrf-exempt + constant-time compare; C14 GET/POST legacy |
| 5 | `views/digest_views.xml` | e0dd92c650bcc21b72564d259240f77147a619d1 | e0dd92c650bcc21b72564d259240f77147a619d1 | YES | C15 buttons/sections system group; menus ERP manager |
| 6 | `data/ir_cron_data.xml` | a6c1d0915a54e21f36867bede259f9b46a7436a1 | a6c1d0915a54e21f36867bede259f9b46a7436a1 | YES | C09 root user, daily, first call +2 h |
| 7 | `__manifest__.py` | 6ee68b6fd27c098ee26ff71351af956f9aed6f67 | 6ee68b6fd27c098ee26ff71351af956f9aed6f67 | YES | C01 (hash only; content per Lane A) |

Result: 7/7 blob matches; 0 mismatches.

## 10. Provenance
- Input: Lane A packet (sha256 above), consumed read-only.
- Spot-check fetches: anchor commit above via raw.githubusercontent; files held in session scratchpad only.
- Topic lens: frozen bank W1-B03 (hash verified against manifest); no QID answered.
- No Lane B material, no runtime system, no other lane packets consulted.

## 11. Limitations
- Source presence != runtime reachability; nothing here is runtime proof.
- No Formal Coverage claim; no percentages; no QID answers.
- Clean room: neutral WHAT/WHY/RISK only; identifiers are evidence pointers, not design recommendations; no code, schema, ORM or workflow reuse.
- Claims marked "Lane A only" were not re-read by A1 (MED confidence).
- Framework-level behavior (CSRF, record-rule defaults, mail message visibility rules) outside module scope; single anchor commit.
