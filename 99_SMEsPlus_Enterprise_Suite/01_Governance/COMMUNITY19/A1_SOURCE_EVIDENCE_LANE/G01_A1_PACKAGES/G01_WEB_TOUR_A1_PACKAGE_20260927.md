# G01 PLATFORM_BASE — RED TEAM A1 Package — `web_tour`

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A1 (source-backed research synthesizer) |
| Group / Module | G01 PLATFORM_BASE / `web_tour` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_WEB_TOUR_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `111e1959eb255d339ac921a3981c090b0bbb9a77d9db1273c2b15d8a96b387d0` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/web_tour/` |
| Question bank (lens only) | `GMVQ/G01_PLATFORM_BASE/G01_WEB_TOUR_GMVQ_MVQ_40_V1.00_DRAFT.md` (sha256 `fdc06e0b…6f37`, matches `FREEZE_W1-B05.json`) |
| Freeze | batch W1-B05, freeze hash `cc81bc57f3686bfec5eda5fff354599e4d2ba5a9855078e9c2eaa13a6ca91bd3`, ELIGIBLE |
| Lane B dependency | None. A1 does not wait for Lane B; no runtime evidence consumed |
| Date | 2026-09-27 |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |

Clean-room note: claims are neutral WHAT / WHY / RISK statements. Identifiers are evidence pointers only. No vendor code is reproduced, and no reuse of vendor schema, ORM, workflow, UI or naming is recommended. No QIDs are answered. The bank was used only as a topic lens: per-user completion, custom versus system guide selection, repeat or concurrent consumption, the existence of consumed guides, export side effects, and authoring authority.

Evidence key (blob SHA-1 from Lane A; "V" = re-verified by A1 spot-check): E1 `__manifest__.py` 5945c156…; E2 `__init__.py` 0650744f…; E4 `models/tour.py` 575bf0a5… V; E5 `models/res_users.py` 9ab9decb… V; E6 `models/ir_http.py` 1e7889a9…; E7 `security/ir.model.access.csv` 71ea4517… V; E8 `views/tour_views.xml` c80188dc… V

## 1. Claims

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-WTOUR-C01 | WHAT: The module provides guided onboarding and scripted UI walkthroughs for the web client. It depends only on `web`, installs automatically and is LGPL. WHY: in-app guidance plus UI test infrastructure. RISK: one step engine serves both user onboarding and automated tests. | E1 | HIGH | SOURCE-STATIC |
| A1-G01-WTOUR-C02 | WHAT: A guide has a unique name, a start URL (default is the web client root), a computed sharing link (base URL plus a guide query parameter), a translatable completion message, an ordering sequence, a "custom" flag and a set of users who have consumed it. Steps have a required trigger, content, a tooltip position, a free-text run instruction and a sequence. They belong to one guide and are deleted with it. | E4 (S1) | HIGH | SOURCE-STATIC |
| A1-G01-WTOUR-C03 | WHAT: The current guide is returned only when the caller is an internal user with onboarding enabled. It is the first guide in order that is not flagged custom and that the caller has not consumed. RISK: custom (recorded) guides never enter the automatic queue, and a user with onboarding disabled gets nothing even if unconsumed guides exist. | E4 (S1) | HIGH | SOURCE-STATIC |
| A1-G01-WTOUR-C04 | WHAT: For an internal caller, consume looks the guide up by name. If it exists, the caller is linked to its consumed set under sudo, and the next current guide is returned. An unknown name is silently ignored. Repeating consume is idempotent because linking is set-based. RISK: no error is raised for an unknown name. Behaviour under concurrent consumption is decided by the database, not by this module. | E4 (S1) | HIGH (logic) / LOW (concurrency) | SOURCE-STATIC |
| A1-G01-WTOUR-C05 | WHAT: Consumption is recorded per user across the whole database, with no company or tenant dimension. RISK: in a multi-company deployment, a user who completed a guide in one company context has completed it everywhere. | E4 (S1) | HIGH | SOURCE-STATIC |
| A1-G01-WTOUR-C06 | WHAT: The per-user onboarding flag is stored, editable and computed when the user is created. It is true only for admin users when no module has demo data and no test is running. The demo count runs under sudo. RISK: non-admin users start with onboarding off. The default depends on install-time demo state. | E5 (S2) | HIGH | SOURCE-STATIC |
| A1-G01-WTOUR-C07 | WHAT: A model-level method lets any caller set their own onboarding flag under sudo. The write targets only the current user. WHY: a self-service toggle without granting write on the user model. RISK: the sudo self-write bypasses the user-model ACLs for this field, but only for the caller's own record. | E5 (S2) | HIGH | SOURCE-STATIC |
| A1-G01-WTOUR-C08 | WHAT: The system group has full CRUD on guides and steps. The internal-user group has read-only access. No record rules are declared. RISK: guide content, including free-text step instructions executed by the client, can be authored only by the system group. That holds only as long as no other module widens the ACLs. | E7 (S3) | HIGH | SOURCE-STATIC |
| A1-G01-WTOUR-C09 | WHAT: Retrieving a guide by name and producing its JSON are public model methods. Any user with read access (internal users) can call them through the generic RPC layer of `web`. RISK: every internal user can read every guide, including custom ones. | E4 (S1); E7 (S3) | HIGH | SOURCE-STATIC |
| A1-G01-WTOUR-C10 | WHAT: Export serialises a guide into a client-registry script file, stores it as an attachment linked to the guide, and returns a download URL that points to the `web` content route. Step data is serialised as structured data. The guide name and URL are inserted into the script text directly, without that structured serialisation. RISK: an authored name or URL containing quote characters could corrupt or alter the generated script. Authoring is limited to the system group (C08). | E4 (S1) | HIGH (construction) / LOW (exploitability) | SOURCE-STATIC |
| A1-G01-WTOUR-C11 | WHAT: A code-type server action named "Export JS" is bound to the guide form view and calls export. No group restriction on the binding was observed in the view file. The export method is a public record method that runs under the caller's identity. RISK: an internal user with read-only guide access might be able to trigger export and so create an attachment. Whether this works depends on server-action and attachment ACLs in `base`. | E8 (S4); E4 (S1) | MED | SOURCE-STATIC |
| A1-G01-WTOUR-C12 | WHAT: Export does not touch consumed-user progress. | E4 (S1) | HIGH | SOURCE-STATIC |
| A1-G01-WTOUR-C13 | WHAT: The management menu sits under a technical parent from `base`. No menu-level group was observed. | E8 (S4) | HIGH (menu line) / MED (inherited visibility) | SOURCE-STATIC |
| A1-G01-WTOUR-C14 | WHAT: The module has no HTTP controllers of its own. All server interaction goes through the generic RPC layer, and the session bootstrap is extended with the onboarding flag and the current guide. | E2; E6; Lane A §2.5-15, §2.6-17 | HIGH | SOURCE-STATIC |
| A1-G01-WTOUR-C15 | WHAT: No crons are declared and no config parameters are read. The only toggle is the per-user flag. | E1; Lane A §2.6-16 | HIGH | SOURCE-STATIC |

## 2. Business rules
- BR-1: Automatic guidance is offered only to internal users with onboarding enabled. The next guide is the first non-custom, unconsumed guide in order (C03).
- BR-2: Completion is per user, set-based and idempotent. Unknown guide names are ignored (C04, C05).
- BR-3: By default, onboarding is on only for admins on non-demo, non-test databases. Users toggle it themselves (C06, C07).
- BR-4: Only the system group can author guides. All internal users can read them (C08, C09).
- BR-5: Export produces a downloadable attachment and has no effect on progress (C10, C12).

## 3. States / transitions
- Per (user, guide): not consumed → consumed, through consume. There is no reverse transition in the source (C04).
- Per user: onboarding on ↔ off, through the self-toggle. The initial value is set when the user is created (C06, C07).
- Guides have no workflow state. The "custom" flag only affects queue eligibility (C03).

## 4. Exceptions / failure modes
- The guide name must be unique. That constraint is the only explicit validation (Lane A §2.3-10; E4).
- Consuming an unknown name is a silent no-op, and the current guide is still returned (C04).
- A non-internal caller gets no current guide, and its consume call is ignored (C03, C04).
- A malformed name or URL could corrupt the generated export script (C10).

## 5. Cross-module handoffs
- `web`: the session-info extension point, asset bundles, the generic RPC layer and the content download route for exports.
- `base`: the user model, the module registry (demo count), attachments, the technical menu parent, server-action execution and ACLs.
- Client registry: code-defined guides register client-side under a registry category. Server records hold custom or recorded guides (Lane A §3).

## 6. Evidence gaps (Lane A carried forward + A1)
- G-1 (Lane A): no controllers package exists. This is recorded as an absence and is consistent with C14.
- G-2 (Lane A): the JS client (runner, pointer, recorder) was not studied, so how step run-instructions execute and any client-side guards are unevidenced.
- G-3 (Lane A): the view XML was examined only for ids, the menu and the binding. A1 additionally checked for group attributes on the menu and binding lines only.
- G-4 (Lane A): tests and static assets were not reviewed.
- G-A1-1: the server-action execution permission and the attachment-create ACL in `base` are unread (C11).
- G-A1-2: concurrency semantics of set-based linking under simultaneous consume are unverified (C04).

## 7. CRQ candidates
- CRQ-WTOUR-01: Confirm whether a read-only internal user can run the bound export action or call export through RPC and create an attachment (C11).
- CRQ-WTOUR-02: Decide whether guide progress needs a company or tenant dimension (C05).
- CRQ-WTOUR-03: Decide whether consuming an unknown guide should fail rather than be ignored (C04).
- CRQ-WTOUR-04: Decide whether the default of onboarding only for admins is the intended policy for new non-admin users (C06).
- CRQ-WTOUR-05: Check how authored names and URLs are escaped when exported guides are generated (C10).

## 8. Contradictions
| ID | Statement | Classification |
|---|---|---|
| — | No contradiction was found between Lane A and the spot-checked source. Lane A RISK item 13 ("authoring limited to system group") is supported by the ACL file (S3), subject to C11 for the export path. | NONE |

## 9. Spot-check log (A1 re-fetch from raw.githubusercontent.com at anchor commit; `git hash-object` compared)
| # | Path | Recorded blob | Recomputed blob | Result | Claim(s) checked |
|---|---|---|---|---|---|
| S1 | addons/web_tour/models/tour.py | 575bf0a5…24ac | 575bf0a5953a383c2733c7775ec699f6e73724ac | MATCH | C02-C05, C09, C10, C12: internal+enabled gate, non-custom queue, sudo link, unknown-name no-op, export construction |
| S2 | addons/web_tour/models/res_users.py | 9ab9decb…236d | 9ab9decb169d9902b0a51494694447f972b5236d | MATCH | C06, C07: admin/no-demo/no-test default; sudo self-toggle |
| S3 | addons/web_tour/security/ir.model.access.csv | 71ea4517…4619 | 71ea4517ba59b0a592677b7cc6e6c3ccaec14619 | MATCH | C08: 4 ACL rows, system group CRUD, internal-user read-only |
| S4 | addons/web_tour/views/tour_views.xml | c80188dc…1b | c80188dc901a523a0ffb2ec0c3a78b33d828dc1b | MATCH | C11, C13: form-bound code server action; menu without group attribute |
Result: 4 of 4 re-fetched blobs match (HTTP 200 each).

## 10. Provenance
- Input: the Lane A packet (sha256 above). A1 re-fetched only the 4 files listed in section 9, from the anchor commit, into a session scratchpad outside the repository. None of that content is reproduced here.
- Topic lens: the frozen W1-B05 bank. Its hash was verified against the freeze manifest, and it was not edited. No QIDs were answered.
- No Lane B, runtime, DB or config state consumed. No git operations performed.

## 11. Limitations
- Source presence is not runtime reachability. Installed modules, inherited menu groups and client behaviour can change what users actually see.
- All claims are SOURCE-STATIC at a single commit. No Formal Coverage is claimed and no completion percentage is implied.
- Client-side step execution is entirely unevidenced (G-2). LOW and MED claims need A2 or Proof follow-up.
