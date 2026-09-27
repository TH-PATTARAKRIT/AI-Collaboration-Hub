# G01 PLATFORM_BASE — RED TEAM A1 Package — `web_hierarchy`

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A1 (source-backed research synthesizer) |
| Group / Module | G01 PLATFORM_BASE / `web_hierarchy` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_WEB_HIERARCHY_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `ec340b9b9d84e1f96a5e3a1c029e9dcc6bd086e4e345cacf7879db9f7adf74ac` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/web_hierarchy/` |
| Gate status (header only) | There is no module MVQ bank; only Standard 55 applies. No QID answered. The Question Gate controls A2+ QID lineage. It does not control A1 synthesis. |
| Lane B dependency | None. A1 does not wait for Lane B. |
| Date | 2026-09-27 |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |

Clean-room note: neutral WHAT / WHY / RISK only. Identifiers are pointers. No vendor code, schema or UI pattern is recommended.

Evidence key: E1 `__manifest__.py` 4415a385…; E2 `__init__.py` d6210b12…; E4 `models/ir_actions.py` e95d2c87… V; E5 `models/ir_ui_view.py` ce1d68e9… V; E6 `models/models.py` 88136e7d… V

## 1. Claims

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-WHIR-C01 | WHAT: A hidden technical module that adds an org-chart-style "hierarchy" view type. It depends only on `web`, has no data files and adds no new tables. Its assets are the lazy backend bundle, dark variables and unit tests. | E1 | HIGH | SOURCE-STATIC |
| A1-G01-WHIR-C02 | WHAT: The window-action view-line model gains a hierarchy view mode that cascades on uninstall. WHY/RISK: uninstalling the module removes action view lines of this mode, so configuration is lost on removal by design. | E4 V | HIGH | SOURCE-STATIC |
| A1-G01-WHIR-C03 | WHAT: The UI view model gains the hierarchy type. It is treated as a template-based view type and advertises a default icon. | E5 V | HIGH | SOURCE-STATIC |
| A1-G01-WHIR-C04 | WHAT: View validation checks the root node's attributes against a fixed allow-list: styling class, client class, title, create/edit/delete toggles, parent field, child field, icon, draggable, default order and a validation-flag attribute. Unknown attributes raise a view error. Children of the root may only be field nodes, plus at most one templates node. Any other tag, or a second templates node, raises a view error. Validation is skipped when the node's validate flag is false. | E5 V | HIGH | SOURCE-STATIC |
| A1-G01-WHIR-C05 | WHAT: Server-side validation does not require a parent field and does not check that one names an existing relation to the same model. It only allows the attribute. RISK: a hierarchy view without a parent field, or with an invalid one, passes server validation. Any enforcement is client-side and unverified. | E5 V | HIGH | SOURCE-STATIC |
| A1-G01-WHIR-C06 | WHAT: A generic hierarchy read helper is added to the abstract base, so every model has it. The parent-field argument is supplied by the caller and is not validated against the model in the helper. An invalid name fails later in the ORM layers. If the caller's read specification omits the parent field, the helper adds it (with display name) by modifying the caller's specification object in place. | E6 V | HIGH | SOURCE-STATIC |
| A1-G01-WHIR-C07 | WHAT: When the search matches one record, the helper adds a one-level neighbourhood around it. If the record has a parent, the result holds the record, its parent, and every record whose parent is either of those two: its siblings and its own direct children. If it has no parent, the result holds the record and its direct children. When the search matches several records, exactly that set is returned. An empty match returns an empty list. | E6 V | HIGH | SOURCE-STATIC |
| A1-G01-WHIR-C08 | WHAT: When no child field is given, per-record child-id lists come from a grouped read on the parent field and are attached under a synthetic key. In single-match mode the grouping covers only records that are not themselves the parent of another record in the result. When a child field is given, the caller's specification must supply the child ids. | E6 V | HIGH | SOURCE-STATIC |
| A1-G01-WHIR-C09 | WHAT: There is no cycle detection, depth limit or recursion on the server. The helper expands exactly one level, so it cannot loop on the server. RISK: the integrity of cyclic or self-referencing data depends on the target model's own parent constraints (outside this module). How the client traverses cyclic data has not been assessed. | E6 V | HIGH (server) / UNKNOWN (client) | SOURCE-STATIC |
| A1-G01-WHIR-C10 | WHAT: The module has no groups, ACL files, record rules or elevated-access calls. The search, grouped read and web read all run under the caller's rights, so the parent, sibling, child and child-id lists are limited to what the caller can read. RISK: child-id lists and neighbourhoods may be incomplete for a caller with restricted access, with no signal that records were hidden (inference from the use of caller-scoped ORM calls). | E6 V | HIGH (caller rights) / MED (silent truncation) | SOURCE-STATIC |
| A1-G01-WHIR-C11 | WHAT: No HTTP routes are declared. The helper can presumably be reached through the generic model-method RPC dispatch owned by `web` or core. That is not declared here, and presence in source does not prove it is reachable at runtime. | Lane A §2.4-13, §2.5-14 | MED | SOURCE-STATIC |
| A1-G01-WHIR-C12 | WHAT: No crons, config parameters, settings, SQL constraints, Python constraints or Python tests. | Lane A §2.2-5, §2.6-15 | HIGH | SOURCE-STATIC |

## 2. Business rules
- BR-1: A hierarchy view definition is restricted to allow-listed root attributes, field children and one templates block (C04).
- BR-2: The parent relation is optional at the server-validation layer (C05).
- BR-3: A focused read returns one level around the matched record. A multi-match read returns the set as it is (C07).
- BR-4: All reads are limited to the caller's own access rights (C10).

## 3. States / transitions
- None. The module is stateless. Its only lifecycle effect is that view lines of this mode are removed when the module is uninstalled (C02).

## 4. Exceptions / failure modes
- A disallowed attribute, a disallowed child tag or a second templates block raises a view error (C04).
- An invalid parent-field name fails in the ORM, not with a domain-specific message (C06).
- An empty search returns an empty list. It is not an error (C07).
- Silent truncation by access rights (C10).

## 5. Cross-module handoffs
- `web`: assets and RPC dispatch (C01, C11).
- Core: window-action view lines, UI view model and abstract base (C02, C03, C06).
- Target models: parent-relation integrity and cycle prevention (C09).
- Downstream consumers that declare hierarchy views, such as org-chart style views: not enumerated.

## 6. Evidence gaps
- GAP-1: the `static/src/**` and `static/tests/**` inventory cannot be enumerated.
- GAP-2: client-side enforcement of the parent field's presence and type, and client handling of cycles (C05, C09).
- GAP-3 (A1): whether consumer views depend on server-side validation of the parent field. This needs consumer or runtime evidence.

## 7. CRQ candidates
- CRQ-WHIR-1: Should the hierarchy view definition require, and validate at definition time, a parent relation that points to the same entity? (C05)
- CRQ-WHIR-2: Where should hierarchy integrity (no cycles, maximum depth) be enforced: in a shared platform service or in each entity? (C09)
- CRQ-WHIR-3: Should a hierarchy read tell the user when nodes are hidden because of access rights, for example a count of restricted children? (C10)
- CRQ-WHIR-4: Should a generic hierarchy read be available on every entity, or only on entities that opt in? (C06)
- CRQ-WHIR-5: Is losing configuration on uninstall acceptable for view-mode registrations? (C02)

## 8. Contradictions
- No source contradictions.
- REFINEMENT-WHIR-1 (CONFIRMED by S1): Lane A §2.3-9 says the single-match mode pulls "the parent's other children **or** the record's own direct children". The re-fetched source shows that when the record has a parent, the lookup covers records whose parent is either the record or its parent. The result therefore includes the siblings **and** the record's own direct children (C07). This is a wording precision issue, not a behavioural conflict.

## 9. Spot-check log (A1 re-fetch at anchor commit; `git hash-object` compared)
| # | Path | Recorded blob | Recomputed blob | Result | Claim(s) checked |
|---|---|---|---|---|---|
| S1 | addons/web_hierarchy/models/models.py | 88136e7d…eaca | 88136e7d2b2bd4545ef6c63e2d4d3ef8c56eeaca | MATCH | C06–C10: spec mutation; one-level neighbourhood; grouped child ids; no recursion/cycle check; no elevation |
| S2 | addons/web_hierarchy/models/ir_ui_view.py | ce1d68e9…6550 | ce1d68e9a6948c85da5df8244bded7c5f6106550 | MATCH | C03–C05: allow-list incl. parent/child field (allowed, not required); single templates; skip when not validating |
| S3 | addons/web_hierarchy/models/ir_actions.py | e95d2c87…4c4d | e95d2c87dd7989c17e11de87aa72d30acd3c4c4d | MATCH | C02: cascade-on-uninstall view mode |

Result: 3 of 3 re-fetched blobs match (HTTP 200).

## 10. Provenance
- Input: only the Lane A packet named in the header, pinned by sha256. Re-fetched from `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/web_hierarchy/<path>` into scratch storage. No Lane B or bank material was used, and no git operations were run on the repository.

## 11. Limitations
- Static server source only. No JS analysis. No runtime proof. No percentages. C10 "silent truncation" and C11 reachability are inferences marked MED.
