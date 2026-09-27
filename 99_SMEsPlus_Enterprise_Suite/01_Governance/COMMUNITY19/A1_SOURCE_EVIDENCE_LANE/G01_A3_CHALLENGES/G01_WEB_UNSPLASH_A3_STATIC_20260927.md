# G01 PLATFORM_BASE — Module `web_unsplash` — RED TEAM A3 Independent Challenge (STATIC, CLAIM-LEVEL)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3, an independent adversarial challenger. It did not author any upstream stage |
| Module | G01 PLATFORM_BASE / `web_unsplash` |
| Date | 2026-09-27 (intake 15:21:45Z) |
| Scope | STATIC, CLAIM-LEVEL. Runtime NOT-EXECUTED (neither passed nor failed). MVQ lineage **NOT A3-ELIGIBLE** (no bank). Standard 55 sampled |
| External contact | **None.** A3 did not contact the image provider, its CDN or any other external service; the only host used was `raw.githubusercontent.com` |
| Source anchor | `…/8d05257d83f9128953f580a066db67c48fcdb96f/addons/web_unsplash/`. A3 re-fetched the manifest, `controllers/main.py`, `models/res_users.py`, `models/ir_qweb_fields.py`, `models/res_config_settings.py` and `tests/test_unsplash.py`, and all blobs MATCH |
| **Disposition** | **A3 STATIC PASS WITH DEFECTS (route to REC; PROOF)** — the source substance holds; process rules 1–4 are defective; the mock-based runtime design needs a non-substitution guard |

### Intake (sha256)

| Input | sha256 |
|---|---|
| Lane A | `9e1ae1b0265bfb38e931e828feaa7f69ea50301b6e9a1d64fbf5bb2a5322b5ea` |
| A1 | `56fbe9f1bd4dea215de6daae9f829eb4fa2eeb63e522b4f5eecbc14cc9598829` |
| A2 | `7f5695dab66aceb1205ab39f8c9bf13cfd23bb8450f01defba545856cdb3580e` |
| REC | `66eb15218a853ab0f43589e5558b4622586080aa3d8c1a8a2f6eb2a5de1f3ffd` |
| PROOF | `434e20f82ef2832700ce52cd60412aa8fc410fc3a0ebb002bd56dc5f550adf9b` |

## 2. Challenge log

`main.py` = `controllers/main.py`@00cf725f (A3 fetch).

| # | Challenge | A3 re-check | Disposition |
|---|---|---|---|
| A3-UNSP-01 | Prefix-only URL check without a redirect re-check (C09; PC-UNSP-07) | L84: the allow-list is a string-prefix test on the submitted value. L88: the outbound GET sets no redirect option, so the library default applies (not read). There is no check of the final host. Adversarial refinement: both allowed prefixes end in "/" after the host, so the host is pinned at parse level; parsing tricks cannot reach another host. The only route off the allow-listed host is a redirect served *by* that host. Exploitability therefore depends on real provider behaviour (A1 GAP-5), which is unresolved. | **UPHELD** (exploitability open) |
| A3-UNSP-02 | Public app-id read through elevation (C04; PC-UNSP-01) | L147–149: public auth, elevated parameter read, value returned. Severity context: this is an application identifier, not the access key (which is read only server-side at L21–23). | **UPHELD** |
| A3-UNSP-03 | Access key may appear in errors or logs (REC-UNSP-20; PC-UNSP-21) | The key is sent as a query parameter (L37, L138–139). A notify failure is logged with the exception text (L38–39). The search call (L139) has no handler, so a connection failure propagates to the JSON-RPC error, which can reach any caller the route admits. Whether library exception text contains the query string is library behaviour, so "may" is the correct modality. | **UPHELD** (observation case PC-UNSP-22 NOT-EXECUTED) |
| A3-UNSP-04 | "Authenticated" includes portal users (REC-UNSP-19 GAP) | L130 and L44 use user-level auth with no group check. The manage predicate (`models/res_users.py`@3d4d2d88 L9–16) is consulted only to pick the error code (L135–136, L143–144), never to allow the search. That the user-auth level admits portal users is a framework rule that was not read, so PROOF correctly defers it to PC-UNSP-06. GAP (A1 incomplete) rather than CONTRADICTION is correct. | **UPHELD** |
| A3-UNSP-05 | Save route may clear credentials (REC-UNSP-21; PC-UNSP-23) | L153–156: both values are written, with elevation, exactly as received. There is no presence check, so an absent value is passed through. What the parameter store does with an absent value is framework behaviour, so "may" is correct. Adversarial: A1 state line "no revocation state" is then possibly wrong (an empty save may act as revocation), and REC did not reconcile it. | **UPHELD**; propagation defect → D-UNSP-A3-2 |
| A3-UNSP-06 | Local-mock runtime design must not substitute for claims about real-provider behaviour | The predeclared and PROOF runtime cases run only against a local mock. That design establishes *this module's* behaviour against a controlled endpoint: it follows a redirect, forwards parameters, has no timeout, and aborts the batch. It **cannot** close claims that depend on the real provider: A1 GAP-5 (whether the provider hosts actually redirect, which decides C09 exploitability), A1 BR-5 ("as its API terms require"; the source docstring is the only basis), and any provider-side quota or parameter handling. PROOF §6 specifies a DNS override but (a) does not state this non-substitution limit, and (b) omits TLS trust for the mocked `https` hosts. Without that trust the mock cannot answer on the allow-listed prefixes, unless the current-test bypass is used. The bypass (L34, L84) would disable the very prefix check that PC-UNSP-08 and PC-UNSP-26 need to exercise. | **CHALLENGE-SUSTAINED (PROOF)** — add a non-substitution statement and specify TLS trust and a non-test-mode run for PC-UNSP-08/26 |
| A3-UNSP-07 | Post-declaration additions | PC-UNSP-08 and PC-UNSP-26 steps add "(mock-resolved)" and PC-UNSP-10 adds "(mock)" relative to `predeclared_proof_cases.tsv`, with no `POST-DECLARATION` tag. The additions are material because they fix how the prefix check is satisfied. | **CHALLENGE-SUSTAINED (PROOF)** |
| A3-UNSP-08 | CONTRADICTION-UNSP-1 (notify URL comes from the caller) | L126: the notify target is taken from the caller's item. L34: it is prefix-checked only. L37: the server key is appended. Docstring L26–27 calls it the provider download URL. | **UPHELD** |

### Static PASS re-execution (at least 3 required; 6 executed)

| PC | A3 re-execution | Citation check | Weakness flagged |
|---|---|---|---|
| PC-UNSP-01 | PASS reproduced | L147–149 exact | None |
| PC-UNSP-03 | PASS reproduced | L151–157; predicate L9–16 (elevated group checks L15–16) exact | None |
| PC-UNSP-07 | PASS reproduced | L84–88 exact | Predicate does not record the trailing-slash host pinning (see A3-UNSP-01), which narrows the risk to redirects only |
| PC-UNSP-13 | PASS reproduced: abort causes are (a) disallowed URL, which raises a generic exception inside the try (L84–86); (b) a missing URL, where the string test on an absent value is not a handled type; (c) image processing outside the try (L101). Handlers L94–99 cover connection and timeout only. Notify is at the end of each iteration (L126) | exact | None |
| PC-UNSP-17 | PASS reproduced (shared query variable L72–73, appended at L104, used in the name at L107) | exact | None |
| PC-UNSP-19 | PASS reproduced (`models/ir_qweb_fields.py`@37893572: prefix L16; id L17–19; lookup L21–27 with limit one; default L30) | exact | The lookup runs under the caller's attachment access. Cross-record reuse of a *public* attachment is the claim, and that is correct |
## 3. Process-rule compliance (MASTER C1B systemic findings 1–5)

Source of the rules: `01_Governance/COMMUNITY19/MASTER_CONTROLLED_HANDOFF_STATE_20260927_C1B.md` section "Systemic process findings". Evidence below is from the inputs, the upstream scratch folder `scratchpad/rec_ui4` (read only) and read-only `git log`/`git show`.

| # | Rule | Result for this batch (onboarding, html_builder, web_hierarchy, web_unsplash) | Evidence |
|---|---|---|---|
| 1 | Preserve the A2 `MISSING_REQUIRED_RUNTIME_PROOF` (MRRP) label; do not collapse it into `UNCORROBORATED` | **NOT MET** | None of the four RECs uses the MRRP label in any row. The label is kept only indirectly, where the REC class is UNKNOWN_PENDING_PROOF (whose definition cites MRRP). Where A2 classed a claim MRRP but REC gave it another class, only `UNCORROBORATED` remains: onboarding C11 (CONTRADICTION) and C17 (GAP); web_hierarchy C10 (GAP); web_unsplash C12 (GAP). html_builder has one MRRP claim (C06); it is UNKNOWN_PENDING_PROOF, so it is preserved indirectly only. |
| 2 | Tag any Expected/predicate text added after predeclaration `POST-DECLARATION` | **NOT MET** | 0 `POST-DECLARATION` tags in the four PROOF files. Untagged changes against `predeclared_proof_cases.tsv`: PC-ONBD-05 scope narrowed from "all module .py / any elevation call" to "module runtime code" (tests excluded); PC-UNSP-08 and PC-UNSP-26 steps gained "(mock-resolved)", and PC-UNSP-10 gained "(mock)". Most other rows are wording changes with the same meaning. |
| 3 | REC scans all A1 item classes (BR / states / exceptions / handoffs / gaps / CRQ) | **NOT MET** | The four REC tables reconcile only the claims (Cnn) and A2 omissions (OM). GAP and CRQ items are carried forward in prose. No BR-, state, exception or handoff item is reconciled (0 `BR-` mentions in the four RECs). Effect: onboarding BR-5 and the state line "Panel scope: global → per-company (one way)" still state the negated C11 position; web_unsplash state lines and BR-5 are not updated for REC-UNSP-12/21 and CONTRADICTION-UNSP-1. |
| 4 | REC frozen (sha256 recorded) before PROOF; PROOF header records the REC sha256 it consumed | **NOT MET** | None of the four PROOF headers records a REC sha256 (they give path + item count only). The REC files cite `laneb_search.txt` (sha256 `21b8a78d…0ce7f`), and that file's mtime is 15:13:14Z, after PROOF source fetch began (first `src/` file 15:11:03Z; `blobcheck.txt` 15:11:12Z). REC files were first committed at 15:14:38Z (onboarding), 15:15:22Z (html_builder), 15:16:10Z (web_hierarchy) and 15:17:15Z (web_unsplash), all after PROOF execution started. The html_builder REC was edited again between commits `b31a0e8` and `37823e6` (a one-line correction to a freeze-hash abbreviation; nothing recorded the change), and REC-HBLD-08 cites a PROOF case (PC-HBLD-07). |
| 5 | Cases-file sha256 + UTC timestamp written before first source fetch | **MET (with note)** | `predeclared_proof_cases.tsv` recomputed sha256 = `2203bab7a4d6ebdd38a61dccda74340a5c02c66774a6c5644e48441a2b22f307` (MATCH); `predeclared_sha256.txt` and `predeclared_time.txt` = 2026-09-27T15:10:27Z; first source file 15:11:03Z; 67 case IDs present (19 + 8 + 14 + 26). Note: `tree_probe.json` (15:09:19Z, before predeclaration) records a GitHub API tree-listing attempt that returned 403 with no source content. The timestamp evidence still rests on self-written files and mtimes in scratch, not on a committed record. |

## 4. Lineage

| Artifact | Commits (read-only) | Content check |
|---|---|---|
| Lane A | `1ee5230` 14:52:49Z | = intake |
| A1 | `63318b8` 14:57:33Z | = value recorded by A2 |
| A2 | `209f3b1` 15:06:34Z | = value recorded by REC |
| REC | `d59dd2b` 15:17:15Z | Committed after PROOF source fetch began; not frozen before PROOF |
| PROOF | `123da2d` 15:20:53Z | = intake |

Commit subjects are ignored, because checkpoint subjects name other modules (for example `d59dd2b` "A3 … resource"). Only content is judged. Predeclaration verified (`2203bab7…f307`, 15:10:27Z; the 26 PC-UNSP rows are present). Standard-55 sample: REC-UNSP-19 → Q02 (who may use it) and Q55 (one customer cannot destabilise another, via provider quota) fit. REC-UNSP-17 → Q36 and Q39 fit. REC-UNSP-09 (SSRF-like) "no clear fit" is acceptable. No QID is answered; MVQ has no bank.

Overclaim, Lane B and clean room: no runtime claimed; no percentages; no Formal Coverage. No Lane B exists, and none was misused. One overclaim risk sits upstream: A1 BR-5 ("as its API terms require") is a statement about the real provider, supported only by a source docstring, and REC did not reconcile it. Clean room: 0 code fragments; hosts, routes and parameter keys are used as pointers only.

## 5. Defects routed

| ID | Owner | Severity | Defect | Action |
|---|---|---|---|---|
| D-UNSP-A3-1 | REC | LOW | C12 was MRRP in A2 and is a GAP in REC with only UNCORROBORATED shown; the other eight MRRP claims are kept only through their class (rule 1) | Show the MRRP label explicitly |
| D-UNSP-A3-2 | REC | MED | BR and state items were not reconciled (rule 3): the state line "URL rejected / fetch fails" misses the A2-widened abort causes; "no revocation state" conflicts with REC-UNSP-21; BR-5 is a real-provider claim that conflicts with CONTRADICTION-UNSP-1 | Add REC rows; mark BR-5 as a provider claim that is not source-provable |
| D-UNSP-A3-3 | REC / PROOF | MED | REC was not frozen before PROOF, and the PROOF header has no REC sha256 (rule 4) | Freeze the REC and re-issue the PROOF header |
| D-UNSP-A3-4 | PROOF | MED | The mock-based runtime pack lacks a non-substitution statement, TLS trust for the mocked `https` hosts, and a non-test-mode requirement for PC-UNSP-08/26 | Amend the runtime pack as a tagged post-declaration change. Record that mock outcomes cannot close GAP-5 or any real-provider claim |
| D-UNSP-A3-5 | PROOF | LOW | Untagged post-declaration "(mock-resolved)" / "(mock)" additions (rule 2) | Tag them `POST-DECLARATION` |

## 6. Runtime / gate-blocked items

- RUNTIME NOT-EXECUTED: PC-UNSP-02, 04, 06, 08, 10, 12, 14, 16, 18, 20, 22, 24, 26 (device OFFLINE; no Lane B). Every case must use a local mock, and no traffic may go to the real provider.
- Claims about real-provider behaviour (GAP-5; BR-5 "API terms") stay open whatever the mock results; no case in this pack is designed to close them.
- MASTER handoff pending runtime and the gate (no MVQ bank for `web_unsplash`; Formal Coverage not authorized).

## 7. Limitations

One anchor commit. The following were not read: the `html_editor` attachment helper, core serving protection, parameter-store semantics for absent values, the user-auth level definition, JSON-RPC error serialization, HTTP-library redirect and timeout defaults, and the client JS. There was no runtime and no external contact beyond `raw.githubusercontent.com`. Git was used read-only; inputs were not edited. No percentages; no Formal Coverage; no QID answered.
