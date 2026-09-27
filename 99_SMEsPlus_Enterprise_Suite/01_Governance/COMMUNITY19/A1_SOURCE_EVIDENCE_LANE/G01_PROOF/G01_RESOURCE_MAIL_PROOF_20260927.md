# G01 PLATFORM_BASE — RED TEAM Proof Package — `resource_mail`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller (Stage 2; REC recorded separately) |
| Governed group / module | G01 PLATFORM_BASE / `resource_mail` |
| REC input | `G01_RECONCILIATION/G01_RESOURCE_MAIL_REC_20260927.md` (7 REC items) |
| Upstream (sha256 at intake) | A1 `f3f552c5…8ee8`; A2 `e4e630b9…2a9`; Lane A `7ddbb450…453c45` (full values in REC §2) |
| Question lineage | Standard 55 only (W1-STD, freeze `c64693ee…c213`, verified). **MVQ lineage unavailable.** |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>` |
| Runtime device | OFFLINE (since 2026-09-24T12:53Z per MASTER handoff state). No runtime case executed. |
| Case predeclaration | 2026-09-27T**15:03:14Z** (Asia/Bangkok 22:03:14), before execution. Scratch `rec_rsrc/PROOF_CASES_PREDECLARED.md` sha256 `14159fb2b786343239b4582c2fda958a619f87b2b2319829827b0516fde114de` (shared file with `resource`). |
| Execution window | 2026-09-27T15:03:30Z – 15:05:00Z |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** (6 static cases: 6 PASS, 0 FAIL; 3 runtime cases NOT-EXECUTED) |

## 1. Case design

- Layers: CONFIG (manifest), SOURCE (module model + `resource` cross-reference + one framework method), RUNTIME.
- Blob rule as in the `resource` Proof; mismatch ⇒ BLOCKED. No mismatch.
- Timezone / Thailand: `resource_mail` has no timezone or date logic (C05, verified by PC-RMAIL-05). The Thailand naive-time case is executed in the `resource` Proof (PC-RSRC-10) where the logic lives.

## 2. Blob verification (executed 2026-09-27T15:02:02Z)

| File | Lane A / A2 blob | Recomputed | Result |
|---|---|---|---|
| addons/resource_mail/__manifest__.py | 032a25c2 | 032a25c2cd5c1be067974b60ca1efb7c5848d54c | MATCH |
| addons/resource_mail/models/__init__.py | 756a33c3 | 756a33c3d3d50e77c2563c6caad30b45d78602a6 | MATCH |
| addons/resource_mail/models/resource_resource.py | 797be7bd | 797be7bd04f8ef3f089dbda74db6cf9841b84406 | MATCH |
| addons/resource/models/resource_resource.py (cross-ref) | aad3af2f | aad3af2f8b87bff4cc650819abc2856fdb826067 | MATCH |
| addons/resource/security/ir.model.access.csv (cross-ref) | 34ca64a5 | 34ca64a5e94929feffacb29fae63b73e78a0b3c7 | MATCH |
| addons/resource/security/resource_security.xml (cross-ref) | 500b70f0 | 500b70f06c5fb917bd5657bbaaf23843920dae0c | MATCH |
| odoo/orm/models.py (framework; not in Lane A) | — (recorded here) | 11f50c4e0b676fbb4b8a45e9703326946348ff98 | RECORDED |

Blob log: scratch `rec_rsrc/blob_log.txt`.

## 3. Static cases — executed (SOURCE / CONFIG)

| Case | Layer | REC item(s) | Evidence (file @ blob : lines) | Observation | Result |
|---|---|---|---|---|---|
| PC-RMAIL-01 | CONFIG | REC-RMAIL-01 | __manifest__.py @ 032a25c2 : 4–20 | Category Hidden; depends `resource`, `mail`; auto-install true; only `assets` (backend bundle, unit-test bundle); no `data`/`demo` keys | PASS |
| PC-RMAIL-02 | SOURCE | REC-RMAIL-02 | models/resource_resource.py @ 797be7bd : 3, 11–14 | Colour: stored integer, default = random integer 1–11 inclusive; no constraint | PASS |
| PC-RMAIL-03 | SOURCE | REC-RMAIL-03 | same : 15 | Presence: non-stored field related through the linked user to the user's presence value | PASS (definition; empty-case runtime pending) |
| PC-RMAIL-04 | SOURCE | REC-RMAIL-04, 06 | same : 17–18; resource/models/resource_resource.py @ aad3af2f : 38–42; ir.model.access.csv @ 34ca64a5 : 6–7; resource_security.xml @ 500b70f0 : 30–34 | Avatar-card method returns a plain `read` of the caller-given list: no `sudo`, no filter, no whitelist. Resource mirrors linked user's email, phone and share flag as related fields; this module adds presence. Resource read granted to internal user and system groups; global company rule admits own companies plus no-company | PASS |
| PC-RMAIL-05 | SOURCE | REC-RMAIL-05 | models/__init__.py @ 756a33c3 : 4; manifest (no data keys) | Single import of the resource extension; no new model, constraint, tz, cron, controller or ACL file | PASS |
| PC-RMAIL-06 | SOURCE (framework) | REC-RMAIL-07 | odoo/orm/models.py @ 11f50c4e : 3475–3496 (read), 3349–3365 (fields_get) | When the field list is empty/None, `read` expands it to all fields returned by `fields_get`, which skips fields the caller has no read access to ⇒ "all readable fields" | PASS |

### 3.1 Refinements observed (for A3; they change no verdict)

- **R1 (REC-RMAIL-06).** Related fields on the resource are computed through the framework; whether their values are fetched with elevated rights (so user-record rules do not narrow them) is framework behaviour not re-read here — A2 F-01 states it as assumption. Routed to PC-RMAIL-R03.
- **R2 (REC-RMAIL-04).** Resource ACL has no portal/public row, so the avatar-card path is internal-user only at ACL level (config fact from PC-RMAIL-04).

## 4. Runtime cases — NOT-EXECUTED (device OFFLINE)

| Case | A2 PR | REC | Preconditions | Steps | Expected | Fail | Status |
|---|---|---|---|---|---|---|---|
| PC-RMAIL-R01 | PR-01 | 01 | Fresh DB at anchor | Install `resource`, then `mail`; do not install bridge explicitly | Bridge installed automatically; colour and presence fields exist on resource | Bridge absent | NOT-EXECUTED |
| PC-RMAIL-R02 | PR-02 | 03 | Material resource without user | Read presence | Empty value, no error | Non-empty or error | NOT-EXECUTED |
| PC-RMAIL-R03 | PR-03 | 04, 06, 07 | Companies A,B; internal user U in A; resource Ra (A) linked to user W with email/phone; resource Rb (B) | U calls avatar-card on Ra with [email, phone, presence]; with empty list; then on Rb | Ra values returned; empty list returns all readable fields; Rb access error | Fields filtered/denied on Ra, or Rb data returned | NOT-EXECUTED |

## 5. Summary of results

| Layer | Cases | PASS | FAIL | NOT-EXECUTED |
|---|---|---|---|---|
| CONFIG | 1 (PC-01) | 1 | 0 | 0 |
| SOURCE (incl. framework) | 5 (PC-02..06) | 5 | 0 | 0 |
| RUNTIME | 3 (PC-R01..R03) | 0 | 0 | 3 |
| **Total** | **9** | **6** | **0** | **3** |

REC item status after Proof: 3 UNKNOWN_PENDING_PROOF remain pending (static basis confirmed); 2 GAP items source-confirmed and carried; 2 MATCH unchanged; no CONTRADICTION.

## 6. A3 eligibility

**Disposition: PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING.**

A3 can challenge **now** (static scope): the REC classification (7 items); the 6 executed static cases and R1/R2; the reliance on a framework file (PC-RMAIL-06) outside Lane A; Standard-55 lineage (3 STD-QIDs mapped; **QID-level A3 lineage limited to Standard 55 — MVQ lineage unavailable**); input integrity and predeclaration timing.

**Blocked** until runtime is available: PC-RMAIL-R01..R03 — auto-install effect, empty presence, and actual avatar-card exposure (including elevation of related fields). Eligible for **A3 static-scope challenge only**; not for A3 → MASTER.

## 7. Limitations

- No runtime executed; no runtime result claimed.
- JS assets (the avatar-card UI consumer) and tests not read (A1 G1/G3); presence field definition in `mail` not re-read (G2).
- No percentages, no Formal Coverage claim, no git operations; inputs not edited; clean room (paraphrase and pointers only).
