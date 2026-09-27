# G01 PLATFORM_BASE — RED TEAM A2 REVIEW — Module `resource_mail`

## 1. Header

| Field | Value |
|---|---|
| Role | RED TEAM A2 (functional/semantic verifier of A1 conclusions). Independent of A1; A1 package not repaired. |
| Group / Module | G01 PLATFORM_BASE / `resource_mail` |
| Date | 2026-09-27 |
| A1 input | `G01_A1_PACKAGES/G01_RESOURCE_MAIL_A1_PACKAGE_20260927.md` — sha256 `f3f552c5098154ed344d338ff91148b6a0f39a6c605fdb6df5284ff16cc88ee8` |
| Lane A upstream | `G01_LANE_A_PASS1/G01_RESOURCE_MAIL_LANE_A_PASS1_20260927.md` — sha256 `7ddbb4501027579e85e689feefd4acf91cc73a29907d0e9fb8c6e89d5c453c45` (matches A1) |
| Question gate | `FREEZE_W1-STD.json` file sha256 `370b92b43d56a99d6e6e444916356eb56e305fdf6bb86b4c7cd0d885a7ff317d`; freeze_hash `c64693eee3957388907637ad028ebdeea6fbeb19a093d1c459c5289f45f5c213`. Standard 55 only; no module MVQ bank. MODULE+QID lineage beyond Standard 55 **not available (GMVQ backlog)** — not an A1 defect. |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/resource_mail/` (+ `addons/resource/` cross-refs). |
| Source blob re-check (`git hash-object`) | `__manifest__.py` 032a25c2; `models/__init__.py` 756a33c3; `models/resource_resource.py` 797be7bd; cross-ref `resource/security/ir.model.access.csv` 34ca64a5, `resource/security/resource_security.xml` 500b70f0, `resource/models/resource_resource.py` aad3af2f — **all identical**. |
| Layer | SOURCE-STATIC re-read. No runtime executed. |
| **Disposition** | **A2 VERIFIED WITH FINDINGS — HANDOFF TO REC.** All 5 claims verified; 2 omissions; 3 runtime proof requirements. Lane B NOT_APPLICABLE. |

## 2. Test plan (predeclared)

| TP | Target | Method | Pass | Fail |
|---|---|---|---|---|
| TP-01 | Lineage | sha256 + `git hash-object` | All match | Mismatch → HOLD |
| TP-02 | C01/C05 manifest scope | Re-read manifest keys and import chain | Depends resource+mail; auto-install; no data/security keys; single model import | Any data/security file or extra model |
| TP-03 | C02 colour | Re-read default | Random in small fixed range; no uniqueness | Deterministic or unique |
| TP-04 | C03 presence | Re-read field definition | Non-stored related to linked user's presence | Stored or independent |
| TP-05 | C04 avatar-card method | Re-read method; cross-check `resource` ACL/rules and resource fields mirrored from user | Plain read of caller-named fields, no filter/elevation | Any filter, elevation or field whitelist |
| TP-06 | Business meaning | Multi-company SaaS exposure, HR/planning UI | Omissions logged | — |

TP-01: PASS.

## 3. Claim verdict table

| Claim | A1 conf. | A2 verdict | A2 note |
|---|---|---|---|
| C01 hidden auto-install bridge, no data/security/views | HIGH | **VERIFIED** | Category Hidden; depends on `resource` and `mail`; auto-install true; only asset bundles (backend, unit tests); no data/demo keys. |
| C02 random colour | HIGH | **VERIFIED** | Stored integer; default random integer 1–11 inclusive; no constraint or uniqueness. |
| C03 presence mirrors linked user | HIGH / MED | **VERIFIED** (definition) | Non-stored related field through the linked user. Empty-for-no-user case follows from the relation; runtime confirmation → PR-02. |
| C04 avatar-card = plain read of caller-named fields | HIGH | **VERIFIED** | Public method returns a standard read of the given field list; no filter, no elevation, no whitelist. Access bounded by `resource` ACL (read for internal user/system admin only; no portal/public row) and the resource company rule. See O-01. |
| C05 no new models/constraints/tz/crons/controllers/ACLs | HIGH | **VERIFIED** | Single inherited extension; controllers/wizard absent (Lane A probes). |

Verdict counts: VERIFIED 5 · PARTIAL 0 · NOT_VERIFIED 0 · OUT_OF_SCOPE 0.

## 4. Semantic findings

- **F-01 (C04, exposure precision).** The resource entity (from `resource`) mirrors the linked user's email, phone and share flag as related fields, and this module adds presence. The avatar-card method can therefore return a linked user's contact data and presence to any internal user who can read the resource (same company or company-less resource). Related fields are normally computed with elevated rights in the framework (framework behaviour not re-read here), so exposure is governed by resource readability, not by the user record's own rules. A1's risk statement is correct in principle but does not name these concrete fields.
- **F-02 (C04).** Standard read semantics: an empty field list returns all readable fields, so "caller names fields" includes "caller asks for everything".
- **F-03 (C01, SaaS).** Auto-install means every tenant database with messaging and resources exposes presence of people via resources; for material resources presence is empty. No configuration switch exists in this module.
- Thailand implications: none specific (no tz, holiday or localisation logic here). PDPA-type personal-data exposure consideration follows from F-01 and belongs to downstream IAM design.

## 5. Omissions

| ID | Omission | Claim | Severity |
|---|---|---|---|
| O-01 | Concrete user-mirrored fields (email, phone, share, presence) reachable through avatar-card read | C04 | MED |
| O-02 | Empty field list returns all readable fields | C04 | LOW |

## 6. Lane B classification

No Lane B evidence exists for `resource_mail`. Classification: **NOT_APPLICABLE**; all claims **UNCORROBORATED** by runtime. No FAIL.

## 7. Proof requirements (MISSING_REQUIRED_RUNTIME_PROOF)

| PR | Claim | Setup / action | Expected | Fail condition |
|---|---|---|---|---|
| PR-01 | C01 | Fresh DB; install `resource` then `mail` (no explicit install of bridge) | Bridge installed automatically; colour and presence fields exist on resource | Bridge absent |
| PR-02 | C03 | Material resource with no user; read presence | Empty value, no error | Non-empty value or error |
| PR-03 | C04/O-01 | Internal user in company A calls avatar-card method on a same-company resource linked to another user, requesting email, phone, presence; also with empty field list; then on a company-B resource | Same-company: values returned; empty list returns all readable fields; company-B: access error | Fields filtered/denied on same-company, or company-B data returned |

Count: 3.

## 8. Limitations

- SOURCE-STATIC only. Static JS (avatar card/presence UI) and tests not reviewed (A1 G1/G3 stand). Presence field definition in `mail` not re-read (A1 G2 stands).
- No module MVQ bank; no MODULE+QID mapping (GMVQ backlog). No Formal Coverage, no percentages.
- REC, PROOF and A3 pending.
