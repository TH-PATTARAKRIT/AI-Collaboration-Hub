# G01 PLATFORM_BASE — Module `web_tour` — RED TEAM A2 Review

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 (functional/semantic verifier of A1 conclusions). Independent of A1. A1 is not repaired here |
| Governed group / module | G01 PLATFORM_BASE / `web_tour` |
| A1 package under review | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_WEB_TOUR_A1_PACKAGE_20260927.md` |
| A1 package sha256 (consumed) | `d794e25f34cbd6a821661764b3cec356df1219625510605261a9b1fc7546d315`. Recomputed at the start and at the end of this review; the value did not change |
| Upstream Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_WEB_TOUR_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `111e1959eb255d339ac921a3981c090b0bbb9a77d9db1273c2b15d8a96b387d0` (matches the value in the A1 header) |
| Topic lens | W1-B05 bank `G01_WEB_TOUR_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `fdc06e0b530f327b2eec9ffddd3abff4104d387acb43c2fade99344854986f37`. It matches `FREEZE_W1-B05.json`, whose freeze_hash `cc81bc57…91bd3` matches A1. ELIGIBLE. No QID answered |
| Source anchor (independent re-check) | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, fetched from raw.githubusercontent. Blob SHA-1 was computed with `git hash-object` in the session scratchpad only |
| Date | 2026-09-27 |
| Lane B | None exists for this module; see section 6 |
| **Disposition** | **A2 PASS WITH FINDINGS** |

Disposition reasons:
1. There are 15 A1 claims: 13 VERIFIED, 2 PARTIAL, 0 NOT_VERIFIED, 0 OUT_OF_SCOPE. No claim is wrong on the facts it states.
2. C11 ("Export JS" by read-only users): the WHAT is confirmed, but the RISK hypothesis is **refuted statically**. A2 read the `base` server-action run path and the attachment-create path. Both require write access on the guide model, and read-only internal users do not have it. CRQ-WTOUR-01 is answered statically, and runtime proof is still required (PR-T02).
3. C10 (unescaped guide name and URL in the generated script) is confirmed. Exploitability stays bounded by system-group authoring.
4. C05 (per-user progress without a company dimension) is confirmed and extended: the guides themselves carry no company dimension either.
5. There are no lineage defects.

## 2. Test plan (predeclared)

Plan file: scratchpad `a2_web/A2_TEST_PLAN_WEB_WEBTOUR.txt`, sha256 `3c89a627b0662ff850e8e1b08f8fed8290d49f4f6d25810452ffd96d97cc74f0`. It was written after the lineage capture and source re-fetch and before verdicts were assigned. It is shared with the `web` review.

| TP | Test | Pass condition | Result |
|---|---|---|---|
| TP1 | Lineage: sha256 of the A1 package, the Lane A packet and the bank; A1 internal consistency (claim IDs, counts, status, evidence-key prefixes) | Values match; package is coherent | PASS |
| TP2 | Re-fetch all 7 Lane A files that exist at the anchor and recompute blob SHA-1 | Equal to the Lane A table | PASS: 7 of 7 match (manifest, package init, tour models, user extension, session extension, ACL, views) |
| TP3 | Semantic re-read of every HIGH claim and every CRQ item: Export JS by read-only users (C11), unescaped name/URL (C10), per-user no-company progress (C05), consume semantics (C04). For C11, read `base` `ir_actions.py` (blob `45d06ee4…`) and `ir_attachment.py` (`905ae118…`) at the anchor | The claim's meaning matches the source behaviour | Done; section 3 |
| TP4 | Re-read MED claims (C11, C13) | Same | Done |
| TP5 | Business meaning: onboarding and training evidence, multi-company, authoring authority | No overclaim and no omission | SF-T01..SF-T05 |
| TP6 | Omission scan with the bank as topic lens only | Material behaviours missing from A1 are recorded | OM-T01..OM-T06 |
| TP7 | Lane B classification | Never FAIL for absence | Section 6 |
| TP8 | Proof requirements for inherently runtime claims | Falsifiable, with expected and fail conditions | Section 7 (3 items) |

## 3. Claim verdict table

| Claim | A1 conf. | A2 verdict | A2 basis (independent semantic re-read) |
|---|---|---|---|
| C01 | HIGH | VERIFIED | The manifest depends on `web` only, is auto-install and LGPL-3, and injects test and recorder asset bundles. |
| C02 | HIGH | VERIFIED | The fields and constraint are confirmed. Additions: the completion message is a translatable **HTML** field with a default. The sharing link embeds the raw guide name as a query value without encoding (OM-T02). The step-to-guide link is required, indexed and cascades on delete. |
| C03 | HIGH | VERIFIED | The internal + enabled gate is confirmed. The selection is the first non-custom, unconsumed guide in (sequence, name, id) order; if none remains, the result is false. |
| C04 | HIGH / LOW | VERIFIED | The name lookup runs under the caller's identity; the link to the consumed set is written under sudo with a set-link command and so is idempotent. An unknown name is a silent no-op. For a non-internal caller nothing is linked and the current-guide call returns nothing. Concurrency is still unverified (PR-T01). |
| C05 | HIGH | VERIFIED (extended) | The consumed set is a plain user relation with no company key. The guide model also has no company field, so guides are global to the database as well (SF-T02). |
| C06 | HIGH | VERIFIED | Nuance: "admin" here means the Access-Rights admin role (or superuser), not the Settings/system group. The demo test counts module records flagged as having demo data, under sudo. The value is computed from the creation date and is otherwise editable. |
| C07 | HIGH | VERIFIED | It writes only the current user's flag under sudo. Additions: the method is a model-level RPC-callable method with no internal-user check, so any authenticated user, including portal, can toggle their own flag. The value is not validated beyond boolean coercion (OM-T05). Impact is limited to the caller's own record. |
| C08 | HIGH | VERIFIED | 4 ACL rows: the system group has full CRUD on guide and step; internal users are read-only. The manifest loads no record-rule file and the views file declares none. |
| C09 | HIGH | **PARTIAL** | The RISK holds: every internal user can read every guide, including custom ones, through generic read and through the public by-name retrieval. The WHAT is imprecise: the JSON-building method is private (underscore) and so not directly RPC-callable. It is reached only through the public by-name method and the current-guide method. |
| C10 | HIGH / LOW | VERIFIED | The step list goes through structured JSON serialisation. The guide name and the start URL are interpolated directly into string literals of the generated script. The attachment filename also uses the raw name. Exploitability is bounded: only the system group can author, and the system group already holds broad code-level powers. The residual risk is a supply-chain one: the output is a source-module file meant to be added to code (SF-T03, PR-T03). |
| C11 | MED | **PARTIAL** | The WHAT is confirmed: a code server action bound to the guide form with no group restriction, and the export method is public and runs as the caller. **The RISK is refuted by the `base` read.** (a) Running a server action that has no groups requires write access on the action's model. (b) Creating an attachment linked to a record requires write access on that record. Read-only internal users fail both, whether through the bound action or a direct RPC call to the export method. Runtime confirmation: PR-T02. |
| C12 | HIGH | VERIFIED | Export reads the guide and its steps and creates an attachment. It does not touch the consumed set. |
| C13 | HIGH / MED | VERIFIED | The menu line has no group attribute and sits under a technical parent from `base`. The inherited visibility of that parent was not re-read. |
| C14 | HIGH | VERIFIED | The package init imports only models, so there is no controllers package. The session extension adds the flag and the current guide. |
| C15 | HIGH | VERIFIED | No crons, no config-parameter reads and no server-config reads in any module file. |

Totals: VERIFIED 13, PARTIAL 2 (C09, C11), NOT_VERIFIED 0, OUT_OF_SCOPE 0.

A1 business rules: BR-1, BR-2, BR-3 and BR-5 are consistent. BR-4 is consistent, with the C11 refinement that export also needs write access. A1 declared no contradictions, and A2 finds none.

CRQ status: CRQ-WTOUR-01 is answered statically (denied) and needs PR-T02. CRQ-WTOUR-02..04 are design decisions and remain open. CRQ-WTOUR-05 is confirmed as unescaped and remains open for a design decision.

## 4. Semantic / business findings

- **SF-T01 (completion is self-asserted).** Consumption is recorded when the client calls consume with a name. The server does not check that the steps were performed, so it can be called for any guide name, including custom guides that are never auto-queued. Business meaning: "guide consumed" is a UI dismissal marker. It is not evidence of training completion, and a design must not reuse it as a compliance or training record.
- **SF-T02 (tenant scope).** Guides and progress are both database-global. In a multi-tenant design on shared storage, authored custom guides would be visible to all internal users of every company. That goes beyond the user-level concern A1 raised.
- **SF-T03 (generated code artifact).** The export output is a script meant to become part of a code module. Unescaped interpolation therefore matters mainly as an integrity issue in the path from recorded guide to source file, and it is not a runtime injection vector for ordinary users.
- **SF-T04 (onboarding default).** Automatic onboarding defaults on only for Access-Rights admins on databases with no demo data, outside tests. Regular new users get no automatic guidance unless the flag is set for them. Their self-toggle is available.
- **SF-T05 (one engine, two purposes).** C01's coupling risk is confirmed by the manifest's test and unit-test bundle injection alongside the backend bundle.

## 5. Omissions (material, not in A1)

| ID | Omission | Weight |
|---|---|---|
| OM-T01 | Each export creates a **new** attachment with no deduplication. Attachments linked to a guide are readable by anyone who can read the guide, so every internal user can download them. Bank lens: repeated exports. | LOW |
| OM-T02 | The sharing link embeds the raw guide name without URL encoding, so names with reserved characters give malformed links. | LOW |
| OM-T03 | Progress is bound to the guide record, not its name, once linked. Renaming a guide keeps progress. Deleting a guide drops its progress rows with the relation. Bank lens: rename and delete. | INFO |
| OM-T04 | The session bootstrap runs a current-guide search on every session-info build for internal users with the flag on. This is a per-page-load cost. | LOW |
| OM-T05 | The flag self-toggle has no internal-user check, so portal users can call it (C07 addition). | LOW |
| OM-T06 | The by-name retrieval returns the guide even when it is custom, and a nonexistent name gives an error from the private builder on an empty set, not a clean "not found". The bank lens asks whether fetch-by-name works only when the guide exists. The error path was not runtime-checked. | LOW |

## 6. Lane B classification

No Lane B evidence exists for `web_tour`, so no claim is failed for lack of runtime evidence.

| Class | Claims |
|---|---|
| NOT_APPLICABLE (structural, definitional or configuration declarations) | C01, C02, C08, C12, C13, C14, C15 |
| UNCORROBORATED (user-surface behaviour, source-clear, runtime observation optional) | C03, C05, C06, C07, C09 |
| MISSING_REQUIRED_RUNTIME_PROOF | C04 (concurrency part), C10 (exploitability part), C11. See section 7 |

## 7. Proof requirements

| PR | Claim | Setup | Expected | Fail condition |
|---|---|---|---|---|
| PR-T01 | C04 | One internal user and one guide. Issue two concurrent consume calls for the same name | Both succeed or one retries cleanly. Exactly one membership row exists afterwards, and the next current guide is coherent | A duplicate membership row, or an unhandled error surfaced to the user |
| PR-T02 | C11 | Internal user who is not in the system group. (a) Run the bound "Export JS" action on a guide. (b) Call the export method directly on the guide by RPC | Both are refused with an access error, and no new attachment is linked to the guide | Either path returns a download action or creates an attachment |
| PR-T03 | C10 | A system user creates a guide whose name and start URL contain a double quote, then exports it | Record the actual outcome. Per source, the generated script's string literal breaks or ends early. A correctly escaped literal would contradict C10 | The generated file contains a correctly escaped name and URL (this refutes C10) |

Count: 3.

## 8. Lineage findings

None. The evidence-key prefixes E1, E2 and E4–E8 all match the Lane A pointer table and A2's recomputation. Claim IDs C01–C15 are contiguous, CRQ-WTOUR-01..05 are contiguous, the spot-check log (4 of 4 MATCH) agrees with A2, the Lane A and bank hashes match, and the status is coherent.

## 9. Limitations

- All A2 conclusions are SOURCE-STATIC at one commit. No runtime, database or configuration state was observed. No Formal Coverage is claimed, and no completion measure is implied.
- The JS client (runner, recorder, pointer), the inherited menu-parent groups, the HTML sanitisation of the completion message and the `base` record-access primitive behind the attachment check were not read.
- A2 read the `base` server-action and attachment files only to test A1's C11 dependency. Those reads are A2 evidence, not an A1 repair.
- Clean room: no vendor code is reproduced. Identifiers are evidence pointers only.
