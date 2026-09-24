# SMEsPlus Community19 - RED TEAM G01-G04 Static Checkpoint R3

Date: 2026-09-25
Mode: A1 SOURCE/STATIC + QUESTION-GATE RECONCILIATION
Formal Coverage: NOT CALCULATED

## 1. Environment and evidence state

- Authorized Community19 desktop source device is currently OFFLINE; last connected evidence cannot be used as a fresh byte-level local re-anchor.
- Reproducible upstream Odoo 19.0 branch head observed: 8d05257d83f9128953f580a066db67c48fcdb96f (committer timestamp 2026-09-24T14:26:22Z).
- Upstream source is a static anchor only. It is not asserted byte-identical to the governed local Community19 package.
- Current module control counts remain G01=23, G02=11, G03=11, G04=9.
- No module-count value is a Canonical Function-ID denominator.

## 2. G01 PLATFORM_BASE - verified A1 delta

The base module was deepened beyond the R2 slices.

Current source blobs re-read:
- ir_model.py = ca0c48b566843ece9948c8c5e7f759714a3faf8e
- ir_ui_menu.py = c23c100b817f05c41369fa9a20c7519e3f9b467d
- ir_actions.py = 45d06ee4210b6e5559c6c96ab82ddc238a891a52
- ir_attachment.py = 905ae118b8c8e5050fdc33eb1631c88e3926b888
- ir_http.py = d9d2a00b9bc7d3e7f439b7ff4ecc46488876953a
- res_device.py = 024373541e712686b4dbe3ea86e66ee090f3fcc7

Static findings:
1. ir.model explicitly links model metadata to fields, inherited models, ACL rows, record rules and views; model/field state distinguishes manual vs base objects/fields.
2. ir.model.fields carries required/readonly/index/translate/company_dependent/store/domain/relation metadata plus relation and dependency validation surfaces.
3. ir.ui.menu visibility is not group-only: menus are first filtered by groups, then action-linked models are checked for read access before the menu and ancestors are admitted as visible.
4. ir.actions bindings are model-scoped and view-type scoped; action collections discard entries whose destination model fails read access.
5. ir.attachment supports configured DB/file storage. Filestore writes are content-addressed from checksum/path logic, file garbage collection is an autovacuum path, and effective attachment access follows public/read, linked-record access and creator/admin cases.
6. ir.http implements explicit auth methods including none, public, user and bearer; bearer credentials use API-key validation. Existing sessions are security-checked before route authentication continues.
7. res.device.log records session identifier, platform/browser, IP/geography, device type, user and activity timestamps. Device revocation is identity-checked and invalidates matching stored sessions; device-log cleanup is autovacuum-driven.
8. These are static capabilities only. No runtime menu reachability, API-key behavior, filestore GC execution, route enforcement or session-revocation behavior is claimed.

G01 disposition: A1 ACTIVE / VERIFIED STATIC DELTA / BASE NOT COMPLETE.

## 3. G01 QUESTION GATE

Verified repository freeze state:
- W1-STD: all 23 G01 modules, Standard 55 = FROZEN / VERIFIED.
- W1-B01: base, mail, web = FROZEN; W1_FREEZE_VERIFICATION explicitly verifies this batch.
- W1-B02: auth_signup, base_automation, bus = FROZEN; W1_FREEZE_VERIFICATION explicitly verifies this batch.
- W1-B03: digest, portal, utm = FROZEN in rolling status and has a freeze JSON, but the independent verification document inspected in this run explicitly lists only B01 and B02 under rolling freezes executed.

Gate handling:
- B01/B02 are question-bank eligible from repository evidence, but Runtime A2 was NOT executed because the authorized runtime/source device is unavailable in this run.
- B03 remains HOLD for downstream transition until verification eligibility is independently reconciled.
- The remaining 14 G01 modules have only the frozen Standard 55 and no module-specific frozen bank.

## 4. G02 IDENTITY_ACCESS - roster reconciliation delta

Controlled count remains 11. Exact row-level controlled membership is still unavailable.

A reproducible secondary-register candidate family was reconstructed from LGPL Community source metadata while excluding auth_signup because auth_signup is already frozen inside the verified G01 roster:
- auth_ldap
- auth_oauth
- auth_passkey
- auth_passkey_portal
- auth_password_policy
- auth_password_policy_portal
- auth_password_policy_signup
- auth_timeout
- auth_totp
- auth_totp_mail
- auth_totp_portal

This list has exactly 11 entries and is consistent with the governed G02 count. However it is NOT promoted to canonical G02 membership because GROUP_STRUCTURE_V2_CORE.tsv row bytes and current installed/current-study membership are not freshly available. Status: CANDIDATE RECONSTRUCTION ONLY / NO MEMBERSHIP CREDIT.

No governed G02 GMVQ directory is present. G02 remains A1 ACTIVE / WAIT QUESTION.

## 5. G03 MASTER_DATA

Controlled count remains 11. Exact roster not recovered.

Current evidence supports product, uom and analytic as relevant master-data source anchors, but there is insufficient controlled row evidence to claim the remaining eight names or to certify ownership boundaries. No names are invented.

No governed G03 GMVQ directory is present. G03 remains A1 ACTIVE / WAIT QUESTION.

## 6. G04 ACCOUNT_BASE

Controlled count remains 9. Exact roster not recovered.

Accounting static source families exist in Community source evidence, but ACCOUNT_BASE vs ACCOUNT_PROCESS ownership must not be assigned from prefix/category similarity. Exact nine-name membership remains blocked on the controlled row-level roster.

No governed G04 GMVQ directory is present. G04 remains A1 ACTIVE / WAIT QUESTION.

## 7. RED TEAM challenge and reconciliation

- Source Presence != Runtime Reachability.
- Group-count equality does not prove row membership.
- A candidate roster that happens to match the governed count is not canonical evidence.
- Upstream Odoo branch content does not prove local Community19 byte identity.
- Static ACL/menu/action/auth/device declarations do not prove effective runtime enforcement.
- Company-level platform controls are not SaaS tenant-isolation proof.
- No A2/A3/MASTER is permitted for G02-G04 while exact governed question banks are absent.
- No Formal Coverage until the Canonical Function-ID denominator is Boss-frozen.

Final state:
- G01 = A1 ACTIVE / BASE DEEP STATIC / QUESTION GATE PARTIAL / RUNTIME A2 NOT EXECUTED
- G02 = A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION
- G03 = A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION
- G04 = A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION
