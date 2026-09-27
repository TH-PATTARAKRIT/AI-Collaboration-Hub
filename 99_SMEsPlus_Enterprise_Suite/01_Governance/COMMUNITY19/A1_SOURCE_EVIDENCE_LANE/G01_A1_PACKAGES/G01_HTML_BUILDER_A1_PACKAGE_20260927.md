# G01 PLATFORM_BASE — RED TEAM A1 Package — `html_builder`

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A1 (source-backed research synthesizer) |
| Group / Module | G01 PLATFORM_BASE / `html_builder` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_HTML_BUILDER_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `76275bbb39379c2736d2b8411bdcb331771aa28f378bfef5c1eeb574f143deec` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/html_builder/` |
| Gate status (header only) | Question batch W1-B06 = **HOLD-LOCAL**. No QID answered, no bank edited. The Question Gate controls A2+ QID lineage. It does not control A1 synthesis. |
| Lane B dependency | None. A1 does not wait for Lane B. |
| Date | 2026-09-27 |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** (short package: the module has no server-side Python and ships assets only) |

Clean-room note: this package contains neutral WHAT / WHY / RISK statements only. Identifiers are pointers only.

Evidence key: E1 `__manifest__.py` f55fb070… V; E2 `__init__.py` e69de29b… V (empty); E3 `tests/__init__.py` 171a01d1…; E4 `tests/test_html_builder_assets_bundle.py` 7792507b…; E5 `i18n/html_builder.pot` dd82b494…; E6 `static/src/builder.js` 8ff24b4c…

## 1. Claims

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-HBLD-C01 | WHAT: A client-side HTML content builder that other modules reuse. The manifest description names the website builder and the mass-mailing editor as its consumers. | E1 V | HIGH | SOURCE-STATIC |
| A1-G01-HBLD-C02 | WHAT: The module has no server-side Python. The package init file is empty (0 bytes; its blob is the empty-file hash), and there is no models or controllers package at the anchor (404). As a result there are no models, fields, constraints, routes, business rules, states or server-side exceptions. | E2 V; S3 (404) | HIGH | SOURCE-STATIC |
| A1-G01-HBLD-C03 | WHAT: The manifest has no `data` key, so the module loads no views, menus, actions, ACL, record rules or seed data. It also has no crons or config parameters. | E1 V | HIGH | SOURCE-STATIC |
| A1-G01-HBLD-C04 | WHAT: It depends on `base`, `html_editor` and `mail`. A manifest comment says the `mail` dependency exists only for a client-side helper. RISK: installing the builder pulls in the mail stack for a technical coupling, not a functional one. | E1 V | HIGH | SOURCE-STATIC |
| A1-G01-HBLD-C05 | WHAT: The manifest defines three new asset bundles: the lazily loaded builder bundle, an in-iframe bundle and an add-snippet dialog bundle. It also contributes to four existing web bundles, including the public frontend bundle. The builder bundle removes edit-only and dark SCSS files by glob. WHY: keeps editor-chrome styling separate from edited-content styling. | E1 V | HIGH | SOURCE-STATIC |
| A1-G01-HBLD-C06 | WHAT: The only server-side guard is a post-install test asserting that the builder bundle contains no edit-mode-only SCSS. RISK: the separation is enforced at test time only, not at runtime. | E4; E1 V (remove directives) | HIGH | SOURCE-STATIC |
| A1-G01-HBLD-C07 | WHAT: A background SCSS file is injected into the public frontend bundle, so public pages carry a styling surface from this module even outside edit mode. | E1 V | HIGH | SOURCE-STATIC |
| A1-G01-HBLD-C08 | WHAT: The client surface is large. At least 79 static files contain translatable strings (32 JS and 47 XML), with 528 message IDs, and none of them come from Python. This is a lower bound, based on .pot references only. | E5 | MED (lower bound) | SOURCE-STATIC |
| A1-G01-HBLD-C09 | WHAT/RISK: The module defines no groups, ACL or elevation. Access control for any persistence that the builder triggers must live in consumer or dependency modules (`html_editor`, website, mass mailing), which this pass did not verify. | E2 V; E1 V | HIGH (absence) | SOURCE-STATIC |

## 2. Business rules
- BR-1: No server-side business rules exist. All behaviour is client-side, and that is out of scope for this pass (C02, C09).
- BR-2: Edit-only styling must not ship in the builder shell bundle. This is enforced by a test (C06).

## 3. States / transitions
- None on the server side (C02).

## 4. Exceptions / failure modes
- None on the server side. A mis-globbed asset that leaks edit styling would be caught only by the bundle test (C06).

## 5. Cross-module handoffs
- Outbound: `html_editor` (editor core, styles and plugins), `web` (variables, helpers, frontend and dark bundles, unit tests), `mail` (client helper only) and `base` (C04, C05).
- Inbound (declared intent only): website builder and mass-mailing editor. Not verified from consumer manifests (C01).
- Save paths, RPC calls and access control belong to other modules (C09).

## 6. Evidence gaps
- GAP-1 (G-HB-1): client-side JS/XML behaviour, including save paths and RPC targets, was not analysed.
- GAP-2 (G-HB-2): the full static inventory is unknown. The file count of 79 is a lower bound (C08).
- GAP-3 (G-HB-3): inbound consumers are not confirmed from the consumer manifests.

## 7. CRQ candidates
- CRQ-HBLD-1: Should the content builder be separated from mail-platform dependencies so it can be installed without the messaging stack? (C04)
- CRQ-HBLD-2: Which module owns authorisation and validation for content saved through a client-only builder, and is that enforced server-side? (C09)
- CRQ-HBLD-3: Should the separation between editor styling and public styling be guarded at build or runtime, not only by tests? (C06, C07)

## 8. Contradictions
- None. The spot-checks confirm Lane A's "no server Python / assets only" finding.

## 9. Spot-check log (A1 re-fetch at anchor commit; `git hash-object` compared)
| # | Path | Recorded blob | Recomputed blob | Result | Claim(s) checked |
|---|---|---|---|---|---|
| S1 | addons/html_builder/__init__.py | e69de29b…5c391 | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | MATCH (0 bytes) | C02 |
| S2 | addons/html_builder/__manifest__.py | f55fb070…b575b498 | f55fb07044ff6db8e5aee583226f781f3575b498 | MATCH | C01, C03–C05, C07: description consumers; depends base/html_editor/mail with mail-comment; no `data`; bundle remove directives; frontend contribution |
| S3 | addons/html_builder/models/__init__.py | (absence) | HTTP 404 | ABSENCE CONFIRMED | C02 |

Result: 2 of 2 blobs match, and 1 absence was confirmed.

## 10. Provenance
- Input: only the Lane A packet named in the header, pinned by sha256. The files were re-fetched from `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/html_builder/<path>` into scratch storage. No Lane B or bank material was used, and no git operations were run on the repository.

## 11. Limitations
- Static source only. Client behaviour was excluded. No runtime proof. No percentages. C08 is a lower bound taken from the translation inventory, not a file listing.
