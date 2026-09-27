# G01 PLATFORM_BASE — Module `web_hierarchy` — RED TEAM A2 Review

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 (functional/semantic verifier of A1 conclusions); independent of A1 |
| Governed group / module | G01 PLATFORM_BASE / `web_hierarchy` |
| A1 package under review | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_WEB_HIERARCHY_A1_PACKAGE_20260927.md` |
| A1 package sha256 | `45c325c42cd33aca747b18e11875086246257c9a1ef289453c53eef2115434a2` |
| Upstream Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_WEB_HIERARCHY_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `ec340b9b9d84e1f96a5e3a1c029e9dcc6bd086e4e345cacf7879db9f7adf74ac` (equals the value recorded in the A1 header) |
| Question Gate | No module MVQ bank exists; Standard 55 only. A2 verifies claims only. QID-level lineage is **NOT A3-eligible** until GMVQ authors a module bank. Gate condition, not an A1 defect. |
| Source anchor (independent re-check) | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/web_hierarchy/`; blobs via `git hash-object` in scratchpad |
| Date | 2026-09-27 |
| Lane B | None exists (section 6) |
| **Disposition** | **A2 PASS WITH FINDINGS** |

Disposition reasons:
1. 12 claims: 11 VERIFIED, 1 PARTIAL, 0 NOT_VERIFIED, 0 OUT_OF_SCOPE.
2. REFINEMENT-WHIR-1 (siblings **and** own children) is independently confirmed.
3. PARTIAL C10: caller-rights scoping is verified, but "silent truncation" does not hold for the parent node, which is added by following the relation, not by a search. An unreadable parent would most likely cause an access error for the whole call, not a silent omission.
4. Material omission: the multi-match mode has no result limit (OM-W01). Handoff: Reconciliation, carrying 7 proof requirements.

## 2. Test plan (predeclared before verification)

Plan file sha256 `e2900673ec0a4e3f7b9e5f412da8497bbe0ff0c0c3444a44f9b87e2323bb71d6` (scratchpad).

| TP | Test | Pass condition | Result |
|---|---|---|---|
| TP-1 | Lineage hashes | Recorded equals recomputed | PASS |
| TP-2 | Re-fetch 6 Lane A pointer files; probe controllers/security/tests absence | Blobs match; absences 404 | PASS (6 of 6 match; 3 absences 404) |
| TP-3 | Semantic re-read of all HIGH claims; focus: one-level read under caller rights incl. siblings + children (C07, C10); no server cycle check (C09); parent field optional (C05); specification mutation (C06); child ids (C08) | Meaning matches source | Done, section 3 |
| TP-4 | Business framing + omission scan of 3 model files and manifest | Omissions recorded | SF-W01..SF-W03, OM-W01..OM-W06 |
| TP-5 | Lane B classification | Never FAIL for absence | Section 6 |
| TP-6 | Proof requirements | Falsifiable | Section 7 (7 items) |
| TP-7 | Gate note | No bank recorded | Header |

## 3. Claim verdict table

| Claim | A1 conf. | A2 verdict | A2 basis (independent re-read) |
|---|---|---|---|
| A1-G01-WHIR-C01 | HIGH | VERIFIED | Hidden, depends on `web`, no data key; assets to lazy backend, lazy-dark and unit-test bundles; no new stored model. |
| A1-G01-WHIR-C02 | HIGH | VERIFIED | Selection extension on window-action view lines with cascade on removal. |
| A1-G01-WHIR-C03 | HIGH | VERIFIED | View type added; treated as template-based; default icon advertised in view info. |
| A1-G01-WHIR-C04 | HIGH | VERIFIED | Root attribute allow-list (12 entries incl. the internal validation flag); children only field or a single templates node; skipped when not validating. Refinement: only direct children and attribute names are checked, not attribute values or template content (OM-W05). |
| A1-G01-WHIR-C05 | HIGH | VERIFIED | Parent and child field are allowed names only; no presence or type check. |
| A1-G01-WHIR-C06 | HIGH | VERIFIED | Read helper on the abstract base; parent field name unvalidated; caller's specification object gains the parent field with display name in place when missing. |
| A1-G01-WHIR-C07 | HIGH | VERIFIED | One match with parent: record + parent + all records whose parent is either (siblings and own children), excluding the two. One match without parent: record + own children. Several matches: that set. None: empty list. Confirms REFINEMENT-WHIR-1. Refinement: the grandparent is never included (one level up only). |
| A1-G01-WHIR-C08 | HIGH | VERIFIED | Without a child field, a grouped read on the parent field supplies child-id lists under a synthetic key. In single-match mode the grouping excludes every record that is a parent of some record in the result, so the focused record and its parent get no child list (their children are already in the result). Records without children get no key at all. With a child field, nothing is added. |
| A1-G01-WHIR-C09 | HIGH/UNKNOWN | VERIFIED | No recursion, depth limit or cycle check; exactly one expansion. See OM-W03 for the self-parent edge. |
| A1-G01-WHIR-C10 | HIGH/MED | PARTIAL | Verified: no groups/ACL/rules/elevation; search and grouped read run under the caller's rights. Not verified as stated: in single-match mode the parent is added by following the record's relation, not by a search, so it is not filtered by record rules. If the caller cannot read the parent, the final read would most likely raise an access error for the whole call rather than truncate silently (inference; framework behaviour, PR-WHIR-02). Silent truncation holds for siblings, children and child-id lists. |
| A1-G01-WHIR-C11 | MED | VERIFIED | Public (non-underscore) model method, no route; reachability via generic RPC is an inference that is correctly marked MED. |
| A1-G01-WHIR-C12 | HIGH | VERIFIED | No cron, config, settings, constraints; Python tests package 404. |

Totals: VERIFIED 11 · PARTIAL 1 · NOT_VERIFIED 0 · OUT_OF_SCOPE 0.

Contradiction/CRQ items: no source contradiction; REFINEMENT-WHIR-1 confirmed. CRQ-WHIR-1..5 are well-founded. CRQ-WHIR-3 should be split: silent truncation for children versus hard failure for an unreadable parent (C10 PARTIAL). Add a CRQ candidate for result bounding (OM-W01).

## 4. Semantic / business findings

- SF-W01 (org-chart meaning, C07): The focused read shows the person, their manager, their peers and their direct reports. That fits an org-chart "focus" view. It never shows the manager's manager, so upward navigation needs repeated calls.
- SF-W02 (access, C10): For HR-like hierarchies across companies, what is shown depends on record rules. Peers and reports disappear silently, while a restricted manager node is likely to break the call. That difference matters for UX error states and for information disclosure design.
- SF-W03 (platform-wide helper, C06/C11): Because the helper exists on every model, any model with a self-relation can be read as a tree by any caller who can search it. No privilege is gained, since standard rights apply, but there is no opt-in (CRQ-WHIR-4 is correct).

## 5. Omissions (material, not in A1)

- OM-W01 No result bound: the multi-match mode searches without a limit and reads every match, with child-id grouping for all of them. A broad domain on a large model returns everything in one call (performance and resource risk).
- OM-W02 Parent inclusion bypasses search filtering (see C10 PARTIAL).
- OM-W03 Self-referencing parent (inference): recordsets are concatenated, not merged, so a record whose parent is itself could appear twice in the result.
- OM-W04 The ordering argument is also applied to the grouped read. Many-to-one display names in the result come from the framework read routine, whose privilege for display names was not read here.
- OM-W05 View validation checks attribute names only; values of parent/child field, ordering and flags are not validated server-side.
- OM-W06 Leaf records carry no child-list key (absence rather than empty list); consumers must treat absence as "no children".

## 6. Lane B classification

No Lane B evidence exists for `web_hierarchy`. Absence is not a failure.

| Claim | Classification |
|---|---|
| C01, C02, C03, C12 | NOT_APPLICABLE (static declarations) |
| C04, C05, C06, C07, C08, C09 | UNCORROBORATED (runtime-observable, fully determined by source) |
| C10, C11 | MISSING_REQUIRED_RUNTIME_PROOF (access and reachability conclusions depend on framework runtime) |

## 7. Proof requirements

| PR | Claim(s) | Procedure | Expected | Fail condition |
|---|---|---|---|---|
| PR-WHIR-01 | C10 | Caller whose record rules hide one sibling and one child of a focused record; call the helper | Hidden records absent, no error, no indication | Hidden records returned, or error raised |
| PR-WHIR-02 | C10, OM-W02 | Caller can read a record but not its parent; single-match call | Access error for the call | Result returned with parent omitted or included |
| PR-WHIR-03 | C05 | Install a hierarchy view definition without a parent field, and one with a nonexistent field name | Both pass server validation | Either rejected at server validation |
| PR-WHIR-04 | C06 | Call with a nonexistent parent field name | ORM-level error, not domain-specific | Domain-specific validation message |
| PR-WHIR-05 | OM-W01 | Call with an always-true domain on a model with many records; measure rows returned | All matching rows returned (no limit) | Result capped |
| PR-WHIR-06 | C09, OM-W03 | Record whose parent is itself; single-match call | Duplicate row for the record (source prediction) | No duplicate, or the call loops |
| PR-WHIR-07 | C11 | Call the helper through the generic model-method RPC endpoint as an internal user | Reachable under the caller's rights | Not reachable |

## 8. Limitations

- Static server source only; JS view (client-side parent-field enforcement, cycle traversal) and framework internals (read routine, record-rule application to relation traversal) not read.
- No QID answered; no module bank. QID lineage not A3-eligible until a bank is authored. No Formal Coverage; no percentages.
- Clean room: neutral statements; identifiers are pointers; no code reproduced. Inputs unmodified; no git operations.
