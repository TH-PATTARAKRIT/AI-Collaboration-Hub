# G01 PLATFORM_BASE — RED TEAM A1 PACKAGE — Module `resource_mail`

| Field | Value |
|---|---|
| Role | RED TEAM A1 (source-backed research synthesizer) |
| Group / Module | G01 PLATFORM_BASE / `resource_mail` |
| Lane A input | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_RESOURCE_MAIL_LANE_A_PASS1_20260927.md` |
| Lane A sha256 | `7ddbb4501027579e85e689feefd4acf91cc73a29907d0e9fb8c6e89d5c453c45` |
| Anchor commit | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/resource_mail/`) |
| Question gate | **MVQ bank absent — GMVQ backlog.** Standard 55 only, via W1-STD (freeze `c64693ee…`). No QID is answered and no question is invented. A1 proceeds. |
| Lane B dependency | None. A1 does not wait for Lane B. |
| Date | 2026-09-27 |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** (the Python and manifest surface is fully covered; the JS UI is an open gap) |
| Clean-room | Neutral WHAT/WHY/RISK only. No code, schema, ORM or workflow is reproduced or recommended for reuse. Identifiers are pointers only. |

## 1. Claims

Layer for every claim: SOURCE-STATIC. Paths are relative to `addons/resource_mail/`. `[SC]` = re-verified in the spot-check (Section 10).

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence (path @ blob) | Conf. |
|---|---|---|---|
| A1-G01-RMAIL-C01 | WHAT: a hidden bridge that depends on `resource` and `mail` and **auto-installs** when both are present. It ships no data, security, view or menu files. WHY: extends user-facing messaging features to resources. RISK: every database with both parents gets this module's fields and UI without an explicit decision to install it. | `__manifest__.py` @ 032a25c2 [SC] | HIGH |
| A1-G01-RMAIL-C02 | WHAT: the resource gets a stored colour index whose default is random within a small fixed range. Colours are not unique and not deterministic. RISK: colour cannot serve as an identifier, and repeated installs or tests do not produce the same colours. | `models/resource_resource.py` @ 797be7bd [SC] | HIGH |
| A1-G01-RMAIL-C03 | WHAT: the resource gets a non-stored presence value taken from the linked user's messaging presence. Resources with no user have no presence (this follows from the relation; it is not runtime-verified). | `models/resource_resource.py` @ 797be7bd [SC] | HIGH (definition); MED (empty case) |
| A1-G01-RMAIL-C04 | WHAT: a public avatar-card method returns the fields that the caller names, using the standard read path with no added filter and no elevation. WHY: shows a resource popover the same way a user popover is shown. RISK: the caller chooses the fields, so exposure is limited only by model, field and record access. That access is read-only for internal users, plus the multi-company rule on resources, as set in `resource`. | `models/resource_resource.py` @ 797be7bd [SC]; cross-ref `resource/security/ir.model.access.csv` @ 34ca64a5 [SC in resource package] | HIGH |
| A1-G01-RMAIL-C05 | WHAT: there are no new models, constraints, timezone handling, crons, controllers or ACL/rule files. All access control is inherited from `resource` and `mail`. | `__manifest__.py` @ 032a25c2 [SC]; `models/__init__.py` @ 756a33c3 [SC] | HIGH |

## 2. Business rules
- BR1: A resource's presence mirrors its linked user's presence. There is no independent presence for resources.
- BR2: Colour is assigned at creation, and nothing enforces it or makes it unique.

## 3. States / transitions
- None defined in this module. The presence states belong to `mail` (not re-read, G2).

## 4. Exceptions / failure modes
- No explicit errors are raised. Avatar-card reads fail with a standard access error when the caller lacks read rights or names a field it cannot access (inferred from the standard read path; not runtime-verified).

## 5. Cross-module handoffs
- `resource` → extended in place (resource entity).
- `mail` → supplies the presence value on the user.
- JS consumers of the avatar-card method are presumed but not evidenced (G1, G3).

## 6. Evidence gaps
- G1: The static JS and its tests were not reviewed, so the UI behaviour is unevidenced.
- G2: The presence field's definition in `mail` was not re-read.
- G3: No caller of the avatar-card method was identified.

## 7. CRQ candidates
- CRQ-RMAIL-01: Confirm the avatar-card UI and which fields it requests (C04).
- CRQ-RMAIL-02: Confirm that presence is empty for resources with no linked user (C03).
- CRQ-RMAIL-03: Confirm auto-install when `resource` and `mail` are both present (C01).

## 8. Contradictions
- None observed. There are no CONFIRMED-FROM-SOURCE or CANDIDATE contradictions.

## 9. Provenance
- The sole analytic input is the Lane A packet above (sha256 recorded). Spot-check source: `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/resource_mail/<path>`, fetched 2026-09-27 into the session scratchpad and not committed.

## 10. Spot-check log (3 files; `git hash-object` vs the Lane A blob)

| # | File | Recorded blob | Recomputed | Claim content checked | Result |
|---|---|---|---|---|---|
| 1 | `__manifest__.py` | 032a25c2cd5c1be067974b60ca1efb7c5848d54c | identical | depends on `resource` and `mail`; auto-install true; no data/demo keys | MATCH |
| 2 | `models/resource_resource.py` | 797be7bd04f8ef3f089dbda74db6cf9841b84406 | identical | random colour default in a small range; related presence; avatar-card method is a plain read of caller-named fields | MATCH |
| 3 | `models/__init__.py` | 756a33c3d3d50e77c2563c6caad30b45d78602a6 | identical | single model import | MATCH |

## 11. Limitations
- SOURCE-STATIC only. Source presence does not prove runtime reachability.
- There is no Formal Coverage claim and no percentages. A2, Lane B, Reconciliation and Proof are still pending.
- There is no module MVQ bank, so no QID mapping exists (GMVQ backlog).
