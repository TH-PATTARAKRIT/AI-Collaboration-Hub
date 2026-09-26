# G01 Evidence-First Recovery — Primary A1 Evidence R2

Date: 2026-09-26
Branch: research/g01-evidence-first-recovery-20260926
Scope: existing G01 pilot only — base, web, mail
Source anchor: odoo/odoo 19.0 @ 8d05257d83f9128953f580a066db67c48fcdb96f
Local governed byte identity: NOT VERIFIED; source device offline
Runtime/A2: NOT EXECUTED
Formal Coverage: NOT AUTHORIZED

## Verified source pointers
- odoo/addons/base/models/ir_rule.py — e64f4e2c88209836d39f2bfe163469def41b71c0
- odoo/addons/base/models/ir_cron.py — e8762b920da6a68fd655dccf1a936671838c561d
- addons/web/controllers/action.py — 384f3063b85831674c89d964d42b90cecf91ea26
- addons/web/controllers/dataset.py — a1c5bdd99c32a38e5e2e0b8f4ea682aa42c50823
- addons/mail/models/mail_notification.py — f16b7b45618f3df9d97395e81d4df23dbb8cbc21
- addons/mail/models/mail_followers.py — 915ebee70c212830edd820b67c7153f57dee445a
- addons/mail/models/mail_scheduled_message.py — 9ddc7a4c5cae898dc634733981c00cba2b917c5c

## New verified AKUs
1. Record-rule evaluation is company-context-sensitive: active company IDs are part of rule evaluation and cache context. This is company evidence only, not Tenant proof.
2. Global record rules combine restrictively while applicable group rules combine as alternatives; inherited parent-model rules may also contribute.
3. Record-rule create/write/delete clears authorization-related cache, confirming stale authorization as a material control risk.
4. Cron execution uses single-job acquisition/locking and avoids concurrent acquisition by multiple workers; runtime behavior remains unproven.
5. Cron processing checks code/database version and pending module state before normal execution and tracks failure/progress lifecycle.
6. Web action metadata loading and server-action execution are distinct boundaries; UI visibility cannot be treated as execution authorization.
7. Authenticated dataset RPC can dispatch model methods/buttons independently of the visible UI; runtime role/state checks require proof.
8. Notification creation requires access to the underlying message; non-admin users cannot rebind notification message/recipient.
9. Notification lifecycle explicitly distinguishes delivery/failure states and prevents duplicate partner notification for one message.
10. Follower mutation is treated as access-affecting and invalidates document cache; duplicate follower identity is constrained.
11. Recipient derivation distinguishes internal/share/customer contexts and filters internal subtype delivery from shared recipients.
12. Scheduled-message creation checks posting authority, and posting rechecks authority using the original creator identity.
13. Scheduled-message target record cannot be changed by normal write after creation.
14. Scheduled-message cron has explicit failure/rollback/notification handling; runtime duplication/leak behavior remains unproven.

## Cross-module synthesis
- Base authorization plus web RPC demonstrates why hidden UI is not a security boundary.
- Cron plus scheduled messaging demonstrates why deferred execution must preserve actor, scope, concurrency and failure semantics.
- Follower state can affect access, so messaging and base authorization require cross-module runtime proof.
- Company-context controls must not be promoted to SMEsPlus Tenant-isolation proof.

## QID trace candidates — NOT release credit
- G01-BASE-Q004 -> A1-PARTIAL / RUNTIME-REQUIRED
- G01-BASE-Q005 -> A1-PARTIAL / RUNTIME-REQUIRED
- STD-Q45 -> A1-PARTIAL / RUNTIME-REQUIRED
- G01-MAIL-Q023 -> A1-PARTIAL / RUNTIME-REQUIRED
- G01-MAIL-Q032 -> A1-PARTIAL / RUNTIME-REQUIRED
- G01-MAIL-Q048 -> A1-PARTIAL / RUNTIME-REQUIRED
- G01-MAIL-Q050 -> A1-PARTIAL / RUNTIME-REQUIRED

## Gap delta
OPEN: GAP-G01-LOCAL-ANCHOR-001, GAP-G01-RUNTIME-001, GAP-G01-QUESTION-001, GAP-G01-MAIL-INHERITANCE-001, GAP-G01-WEB-PROXY-001
NEW: GAP-G01-RPC-AUTHZ-001, GAP-G01-CRON-RUNTIME-001, GAP-G01-MAIL-SCHEDULED-REAUTH-001

## Role-based challenge — not formal independent clearance
Functional: PASS RECOMMENDATION for continued A1 study.
Technical: CONDITIONAL PASS — exact upstream pointers verified; local governed bytes unavailable.
SaaS/Security: CONDITIONAL PASS — company evidence is not Tenant proof; RPC/deferred execution remain runtime risks.
QA: CONDITIONAL PASS — concrete runtime scenarios now exist.
Question Governance: HOLD for release credit — independent per-QID clearance is not established.

## Disposition
A1 RECOVERY PILOT R2 = CONDITIONAL PASS RECOMMENDATION FOR CONTINUED STUDY.
No A2 authorization. No QID certification. No Formal Coverage.
