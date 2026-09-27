# G01 PLATFORM_BASE — Module `web_unsplash` — RECONCILIATION (Stage 1)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RECONCILIATION controller (Stage 1 of REC + PROOF; Proof recorded separately) |
| Governed group / module | G01 PLATFORM_BASE / `web_unsplash` |
| Date | 2026-09-27 (intake 2026-09-27T15:06:49Z) |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/web_unsplash/`) |
| Question lineage | **No module MVQ bank exists** (GMVQ backlog). **MVQ lineage: NOT A3-ELIGIBLE (bank absent).** Lineage lens = Standard 55 only (W1-STD). |
| Lane B | None exists (search recorded in section 3) |
| External service | No request was made to the image provider or any other external service by this controller |
| Next stage | PROOF → `G01_PROOF/G01_WEB_UNSPLASH_PROOF_20260927.md` |
| **Disposition** | **REC COMPLETE — HANDOFF TO PROOF** (26 REC items: 9 MATCH, 9 GAP, 0 CONTRADICTION, 8 UNKNOWN_PENDING_PROOF) |

Format reference: `G01_RECONCILIATION/G01_BUS_REC_20260927.md` and `G01_RESOURCE_REC_20260927.md`.

## 2. Intake (immutable inputs, sha256 recorded at intake)

Paths are relative to `99_SMEsPlus_Enterprise_Suite/01_Governance/COMMUNITY19/`.

| Input | Path | sha256 | Check |
|---|---|---|---|
| Lane A | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_WEB_UNSPLASH_LANE_A_PASS1_20260927.md` | `9e1ae1b0265bfb38e931e828feaa7f69ea50301b6e9a1d64fbf5bb2a5322b5ea` | Equals the value recorded in the A1 and A2 headers |
| A1 | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_WEB_UNSPLASH_A1_PACKAGE_20260927.md` | `56fbe9f1bd4dea215de6daae9f829eb4fa2eeb63e522b4f5eecbc14cc9598829` | Equals the value recorded in the A2 header |
| A2 | `A1_SOURCE_EVIDENCE_LANE/G01_A2_REVIEWS/G01_WEB_UNSPLASH_A2_REVIEW_20260927.md` | `7f5695dab66aceb1205ab39f8c9bf13cfd23bb8450f01defba545856cdb3580e` | A2 PASS WITH FINDINGS; 18 claims (17 VERIFIED, 1 PARTIAL: C12); 7 omissions (OM-U01..U07); 5 business findings (SF-U01..U05); 13 proof requirements (PR-UNSP-01..13) |
| Standard 55 | `GMVQ/G01_PLATFORM_BASE/QUESTION_BANK_STANDARD_55_V2.00.md` | `f6726f111932aecce4432daf3e412d0c9de3291fa45fa8908e9e89ee79cb540d` | Equals the `FREEZE_W1-STD.json` entry |
| Freeze manifest (STD) | `GMVQ/G01_PLATFORM_BASE/FREEZE_W1-STD.json` | `370b92b43d56a99d6e6e444916356eb56e305fdf6bb86b4c7cd0d885a7ff317d` | `freeze_hash` `c64693eee3957388907637ad028ebdeea6fbeb19a093d1c459c5289f45f5c213` recomputed — MATCH; `web_unsplash` is in the module list |

Inputs were only read; none edited. No git operations.

## 3. Lane B evidence-pool search (recorded)

Same search as the `onboarding` REC section 3 (log `laneb_search.txt` sha256 `21b8a78d400b23d6da3f2ecdefd7b315143b81f8b6f2b73c9927bd6802d0ce7f`): 4 filename hits (none mentions `web_unsplash`), 22 content hits (none a runtime observation). Runtime device OFFLINE since 2026-09-24T12:53Z. **Result: no Lane B runtime evidence exists for `web_unsplash`.** Nothing is FAIL for lack of Lane B.

## 4. Classification rules applied

Same as the `onboarding` REC section 4. CONTRADICTION-UNSP-1 is a source-internal documentation-vs-trust finding on which A1 and A2 agree; it is not an A1-vs-A2 contradiction and is carried in REC-UNSP-16.

## 5. Reconciliation table

C01–C18 are the A1 claims `A1-G01-UNSP-Cnn`. SF-U01 is promoted to a REC item because it changes the population A1's "any authenticated user" risk applies to. SF-U02..SF-U05 are carried as context in the items they refine. **No QID is answered.**

| REC ID | Source item | A1 position (summary) | A2 verdict / correction | REC class | Lane B | Proof link | MODULE+STD-QID lineage |
|---|---|---|---|---|---|---|---|
| REC-UNSP-01 | C01 | Hidden, auto-install stock-image integration in the editor media dialog; outbound surface present wherever deps are installed | VERIFIED | MATCH | NOT_APPLICABLE | — | web_unsplash+STD-Q01, Q03 |
| REC-UNSP-02 | C02 | Config = two free-text system parameters, unvalidated; no tables, ACL, groups, rules | VERIFIED | MATCH | NOT_APPLICABLE | — | web_unsplash+STD-Q30 |
| REC-UNSP-03 | C03 | Four JSON-RPC routes: add (user, POST), search (user), app-id (public), save (user, gated) | VERIFIED | MATCH | NOT_APPLICABLE | — | web_unsplash+STD-Q02, Q03 |
| REC-UNSP-04 | C04 | Public app-id route reads with elevation; beacon sends browser-side pings to provider | VERIFIED (SF-U03 privacy context) | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-UNSP-01 | web_unsplash+STD-Q02 |
| REC-UNSP-05 | C05 | Access key read with elevation; never returned by normal routes; sent as query parameter | VERIFIED; error path in REC-UNSP-20 | MATCH | UNCORROBORATED | — | — (no clear fit) |
| REC-UNSP-06 | C06 | Save route: access-rights admin OR website restricted editor; elevated unvalidated writes; else not-found | VERIFIED (SF-U02 separation-of-duties context) | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-UNSP-02 | web_unsplash+STD-Q02, Q30 |
| REC-UNSP-07 | C07 | Search proxy forwards all caller parameters under the server key (key set last); role-dependent errors | VERIFIED | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-UNSP-03 | web_unsplash+STD-Q02, Q55 |
| REC-UNSP-08 | C08 | Per-item prefix allow-list; fetch; non-OK skipped; connection/timeout logged and skipped; resolution check | VERIFIED (trailing slash rejects look-alike hosts) | MATCH | UNCORROBORATED | — | web_unsplash+STD-Q08 |
| REC-UNSP-09 | C09 | Allow-list on submitted string only; redirects not disabled; no post-redirect host check (SSRF-like) | VERIFIED; exploitability open | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-UNSP-04 | — (no clear fit) |
| REC-UNSP-10 | C10 | Test-mode flag disables both allow-lists | VERIFIED; refinement: keyed to process-wide test state (SF-U04) | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-UNSP-05 | web_unsplash+STD-Q54 |
| REC-UNSP-11 | C11 | No timeout, size cap, rate limit or item cap on outbound calls | VERIFIED | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-UNSP-06 | web_unsplash+STD-Q55 |
| REC-UNSP-12 | C12 | Disallowed URL aborts the whole request; rollback of earlier items unknown | PARTIAL — **more batch-stop conditions**: image-processing failure (non-image or over-resolution) and a missing URL field also abort; external notifications for earlier items cannot be undone | GAP | UNCORROBORATED | PR-UNSP-07 | web_unsplash+STD-Q09, Q43 |
| REC-UNSP-13 | C13 | Target model defaults to view model; record id honoured only for another model; editor helper access check (test) | VERIFIED | MATCH | UNCORROBORATED | — | web_unsplash+STD-Q29, Q39 |
| REC-UNSP-14 | C14 | Local URL set with elevation, deliberately bypassing the binary+URL serving protection; token generated | VERIFIED | MATCH | UNCORROBORATED | — | web_unsplash+STD-Q39 |
| REC-UNSP-15 | C15 | Path/name from raw caller item key + sanitised query; extensions accumulate across a batch | VERIFIED (sanitised query keeps spaces and Unicode letters) | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-UNSP-08, PR-UNSP-09 | web_unsplash+STD-Q39 |
| REC-UNSP-16 | C16 (+ CONTRADICTION-UNSP-1) | Download notification only under API photos prefix; failures logged, never raised; docstring implies trusted value but it is caller-supplied | VERIFIED; CONTRADICTION-UNSP-1 confirmed (source-internal) | MATCH | UNCORROBORATED | (PR-UNSP-13) | web_unsplash+STD-Q09 |
| REC-UNSP-17 | C17 | HTML save-back picks first attachment matching path and (same record OR public); no match → empty | VERIFIED; no record id in element → default handling; lookup under caller rights (SF-U05 integrity context) | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-UNSP-10 | web_unsplash+STD-Q36, Q39 |
| REC-UNSP-18 | C18 | Settings view inheritance visible with module toggle; no cron | VERIFIED | MATCH | NOT_APPLICABLE | — | web_unsplash+STD-Q30 |
| REC-UNSP-19 | SF-U01 | (A1 said "any authenticated user") | **"Authenticated" at this auth level includes portal (external) users**, so external customers can consume the provider quota and pass arbitrary search parameters | GAP | UNCORROBORATED | PR-UNSP-03 | web_unsplash+STD-Q02, Q55 |
| REC-UNSP-20 | OM-U01 | (not in A1) | **Access key may appear in errors/logs**: key travels as a URL query parameter; notify failure logged with exception text; search connection failure uncaught (inference) | GAP | UNCORROBORATED | PR-UNSP-11 | — (no clear fit) |
| REC-UNSP-21 | OM-U02 | (not in A1) | **Save route may clear credentials**: writes whatever it receives, including absent values (inference on framework parameter semantics) | GAP | UNCORROBORATED | PR-UNSP-12 | web_unsplash+STD-Q30 |
| REC-UNSP-22 | OM-U03 | (not in A1) | **Provider notifications are not rolled back** when a later item aborts the request | GAP | UNCORROBORATED | PR-UNSP-07 | web_unsplash+STD-Q09, Q43 |
| REC-UNSP-23 | OM-U04 | (not in A1) | Serving by shared local path; framework resolution of duplicates not read | GAP | UNCORROBORATED | — | web_unsplash+STD-Q39 |
| REC-UNSP-24 | OM-U05 | (not in A1) | Search route calls the public app-id method internally; both key and app id required although only the key is sent | GAP | NOT_APPLICABLE | — | web_unsplash+STD-Q05 |
| REC-UNSP-25 | OM-U06 | (not in A1) | Attachment add accepts an arbitrary caller-supplied target model; only the editor helper's access check stands in between | GAP | UNCORROBORATED | — | web_unsplash+STD-Q29, Q39 |
| REC-UNSP-26 | OM-U07 | (not in A1) | Manage predicate references a website group that does not exist without website; behaviour not verified | GAP | UNCORROBORATED | — | web_unsplash+STD-Q02 |

### Counts

| Class | Count | Items |
|---|---|---|
| MATCH | 9 | REC-UNSP-01, 02, 03, 05, 08, 13, 14, 16, 18 |
| GAP | 9 | REC-UNSP-12, 19–26 |
| CONTRADICTION | 0 | — |
| UNKNOWN_PENDING_PROOF | 8 | REC-UNSP-04, 06, 07, 09, 10, 11, 15, 17 |
| **Total** | **26** | 18 A1 claims + 1 promoted business finding + 7 A2 omissions |

Lane B column: NOT_APPLICABLE 5 (REC-UNSP-01, 02, 03, 18, 24); UNCORROBORATED 21. FAIL: 0.

## 6. MODULE+STD-QID lineage summary (Standard 55, W1-STD)

- **MVQ lineage: NOT A3-ELIGIBLE (bank absent).**
- **Mapped STD-QIDs (13 distinct):** Q01, Q02, Q03, Q05, Q08, Q09, Q29, Q30, Q36, Q39, Q43, Q54, Q55. (Q02 and Q39 carry the most items.)
- REC items with no clear fit: REC-UNSP-05, 09, 20 (credential secrecy and outbound-fetch safety have no dedicated Standard-55 question).
- Standard-55 sections B, C, D and F have no topical fit. Recorded as no fit, not as an answer.

## 7. Carried forward

- Evidence gaps GAP-1..GAP-6 remain open (JS inventory; editor helper and serving-protection internals; `base_setup` toggle; rollback; provider redirect behaviour; path collisions).
- CRQ-UNSP-1..9 carried. A2 widening of CRQ-UNSP-9 (all abort causes) recorded against REC-UNSP-12. New CRQ candidates from REC-UNSP-20 (secret in exception text) and REC-UNSP-21 (credential clearing).
- REFINEMENT-UNSP-1 (notify allow-list also bypassed in test mode) confirmed; carried in REC-UNSP-10.

## 8. Handoff to PROOF

All 13 A2 proof requirements (PR-UNSP-01..13) pass to Proof. Any runtime case must replace the provider with a local mock; no traffic to the real provider.

## 9. Limitations

- REC reconciles documents; the source re-read is Proof Stage 2. No Lane B evidence exists.
- No Formal Coverage; no percentages; no QID answered; no bank edited.
- Clean room: neutral summaries; identifiers (routes, parameter keys, hosts) are pointers; no code reproduced.
