# G01 Evidence-First Recovery — Primary A1 Evidence R3

Date: 2026-09-27
Branch: research/g01-evidence-first-recovery-20260926
Scope: existing G01 pilot only — base, web, mail
Source anchor: odoo/odoo 19.0 @ 8d05257d83f9128953f580a066db67c48fcdb96f
Local governed byte identity: NOT VERIFIED; authoritative source device remains offline
Runtime/A2: NOT EXECUTED
Formal Coverage: NOT AUTHORIZED

## Verified source pointers
- odoo/addons/base/models/res_company.py — 86aa2fb0f6974bdf0f541efb2c871b37a43c140c
- odoo/addons/base/models/ir_model.py — ca0c48b566843ece9948c8c5e7f759714a3faf8e
- addons/web/controllers/binary.py — 7b7b84f771eeb5a0f096500f7530a48c956f41b1
- addons/web/controllers/export.py — cb750f193c5548fe70a01422d644c66805a20e69
- addons/mail/models/mail_mail.py — 44c9e2d2066e5d0d01908e95298f3c7662e34b80
- addons/mail/models/mail_gateway_allowed.py — 17a6aa94cdfb17dd348a678d04bf1be8752d059b

## New verified AKUs
1. Company hierarchy is explicit through parent/child, parent_path and computed root relationships; company tree semantics are therefore a platform control surface, not presentation-only metadata.
2. Existing company hierarchy cannot be changed through normal write of parent_id; source rejects the change.
3. Root-delegated company fields currently include currency and are copied to new branches and propagated from roots to branches when changed.
4. Company creation clears registry cache and links the creating user plus superuser into the created-company membership set.
5. Archiving a company cascades active=False to child companies, making lifecycle changes hierarchy-sensitive.
6. ir.model exposes inheritance, ACLs, record rules, manual/base state, abstract/transient state and defining-module metadata as first-class model metadata.
7. Creating manual/custom models triggers registry setup and database schema initialization; custom-model configuration is therefore an executable platform mutation surface.
8. Module/base models are protected from manual deletion, while structural model fields including model/state/abstract/transient are not normally mutable.
9. Public binary/image routes resolve records through ir.binary with optional access_token; when a token is supplied the resulting stream may be marked public after record resolution.
10. Binary cache controls such as unique/immutable/max_age and nocache are response-cache controls and must not be treated as authorization proof.
11. CSV/XLSX export routes require an authenticated user and export through ORM browse/search/export_data paths; UI visibility alone must not be treated as the export authorization boundary.
12. Outgoing mail validates selected mail-server ownership and rejects use of another user's personal mail server.
13. Outgoing mail distinguishes attachments readable by the current user from restricted attachments and prevents normal attachment updates from bypassing read access.
14. Mail queue processing explicitly documents per-message commit behavior, is non-transactional, and auto-commits outside test mode; retry/idempotency/reconciliation require runtime proof.
15. mail.gateway.allowed defines trusted sender addresses that bypass the normal incoming gateway loop/rate threshold, creating an explicit security/configuration exception path.

## Cross-module synthesis
- Company hierarchy and user-company membership affect authorization context and cannot be reduced to UI company switching.
- Dynamic/custom model creation changes the runtime registry/schema and therefore needs configuration-governance and migration proof before SMEsPlus adopts any analogous capability.
- Public binary token access, authenticated export, and mail attachment access are separate data-exposure surfaces and require negative-role testing.
- Mail queue auto-commit plus scheduled/deferred work means transactional rollback assumptions cannot be inferred from synchronous business flows.
- Trusted gateway exemptions are security exceptions and must be explicitly governed, scoped and auditable.

## QID trace status — no new release credit
R2 candidate QIDs remain traceable in governed question artifacts:
- G01-BASE-Q004
- G01-BASE-Q005
- STD-Q45
- G01-MAIL-Q023
- G01-MAIL-Q032
- G01-MAIL-Q048
- G01-MAIL-Q050

R3 does not upgrade any QID to PASS. Existing candidates remain A1-PARTIAL / RUNTIME-REQUIRED unless later independent review and runtime/configuration evidence prove otherwise.

## Gap delta
OPEN carry-forward:
- GAP-G01-LOCAL-ANCHOR-001
- GAP-G01-RUNTIME-001
- GAP-G01-QUESTION-001
- GAP-G01-MAIL-INHERITANCE-001
- GAP-G01-WEB-PROXY-001
- GAP-G01-RPC-AUTHZ-001
- GAP-G01-CRON-RUNTIME-001
- GAP-G01-MAIL-SCHEDULED-REAUTH-001

NEW:
- GAP-G01-BINARY-TOKEN-RUNTIME-001
- GAP-G01-EXPORT-AUTHZ-001
- GAP-G01-MAIL-QUEUE-TXN-001
- GAP-G01-GATEWAY-TRUST-001
- GAP-G01-DYNAMIC-MODEL-CONFIG-001

## Governance contradiction
ERPPLUS-171 still contains the older instruction "DO NOT answer GMVQ/QID now" while the later approved operating model requires A1 QID trace before A1 Single Exit. Jira/Slack are paused by standing instruction, so this packet records the contradiction without mutating Jira.

## Role-based challenge — not formal independent clearance
Functional: PASS RECOMMENDATION for continued A1 study.
Technical: CONDITIONAL PASS — exact upstream pointers verified; local governed byte identity unavailable.
SaaS/Security: CONDITIONAL PASS — binary token, export and trusted-gateway exception paths require explicit negative/runtime proof.
QA: CONDITIONAL PASS — concrete role, token, export, retry, rollback and gateway scenarios now exist.
Question Governance: HOLD for release credit — PR #68 remains open/draft and independent per-QID clearance is not established.

## Disposition
A1 RECOVERY PILOT R3 = CONDITIONAL PASS RECOMMENDATION FOR CONTINUED STUDY.
This artifact resolves the prior Primary-Evidence persistence gap for the R3 source delta only. It does not close G01, authorize A2, certify QIDs, or authorize Formal Coverage.
