# G01 Evidence-First Recovery Pilot — Primary A1 Evidence R1

**Date:** 2026-09-26 (Asia/Bangkok)  
**Branch:** `research/g01-evidence-first-recovery-20260926`  
**Mode:** RED TEAM A1 direct source/static study; Evidence-First; no automation-executor credit  
**Pilot modules:** `base`, `web`, `mail`  
**Upstream reproducible source anchor:** `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`  
**Governed local Community19 byte identity:** NOT VERIFIED in this packet  
**Runtime / A2:** NOT EXECUTED  
**Formal Coverage:** NOT AUTHORIZED / NOT CALCULATED

## 1. Why these three modules

These three modules were selected for the recovery pilot because the governed G01 intake places `base`, `web`, and `mail` inside the exact 23-module G01 roster, and their static dependency positions make them high-coupling platform anchors. The selection is for A1 recovery throughput and evidence quality only; it is not a claim that these are the only critical G01 modules.

## 2. Verified source pointers

### base
- `odoo/addons/base/__manifest__.py` — blob `5250c85200522dd16459e5b845a8017bb958a1c1`
- `odoo/addons/base/models/res_users.py` — blob `9d42d77ae8ec19028c99b3c668294569ded3a86a`
- Carry-forward from G01-G04 R14:
  - `odoo/addons/base/models/ir_attachment.py` — blob `905ae118b8c8e5050fdc33eb1631c88e3926b888`
  - `odoo/addons/base/models/ir_sequence.py` — blob `920e0b2347f850b60c1bf8b392f82a2c7f964272`
  - `odoo/addons/base/models/res_currency.py` — blob `015ca78353c734949545d4364f500d4d57f32d9f`
  - `odoo/addons/base/models/res_lang.py` — blob `563b4eff214fbd9940661b9f76ee3a3aa571c76c`

### web
- `addons/web/__manifest__.py` — blob `72f3f25791583968056ca4a42ab3e9cd13db9e93`
- `addons/web/controllers/home.py` — blob `292aaa75a2c35b71acb3c97488a6dc2c96309c9f`
- `addons/web/controllers/session.py` — blob `2fbcfc872381751ac3336b2549babcca159d76cc`

### mail
- `addons/mail/__manifest__.py` — blob `2f88958b66791f6bfa3eb1b6f3861538edd10ff4`
- `addons/mail/models/mail_thread.py` — blob `c1f8a83bbd4d6667c1ee7cd38b78cef71ad8f374`
- `addons/mail/models/mail_message.py` — blob `4a70962dbcad8cab3d6de3bf1b112e5e753a062b`

## 3. Atomic Knowledge Units — verified static findings

### BASE-AKU-001 — Kernel / platform root
**Dimension:** Manifest / dependency / platform role  
The `base` manifest describes itself as the Odoo kernel needed for installation, has no direct module dependency, is auto-installed, and loads core security groups, security rules, model access, configuration, cron, model metadata, users, companies, languages, currencies, actions, menus, and views.  
**Claim boundary:** static source presence only; no runtime behavior inferred.

### BASE-AKU-002 — User identity is technically separate from partner data
**Dimension:** Model / identity  
`res.users` uses delegated inheritance from `res.partner` and states that user records are dedicated to technical user data while partner records store common person/contact data.  
**Claim boundary:** source semantics only.

### BASE-AKU-003 — Company membership invariant
**Dimension:** Security / company boundary  
Active users are constrained so `company_id` must be included in `company_ids`. Attempts to use a disallowed primary company raise validation. Changes to company membership trigger environment-property resets.  
**A1 implication:** company context is a first-class user security/control concern and must be tested later in A2 rather than assumed from source.

### BASE-AKU-004 — User-type exclusivity and administrator survival
**Dimension:** Security / role integrity  
`res.users` rejects membership in multiple exclusive user-type groups and requires at least one administrator group member after base initialization.  
**Claim boundary:** source rule; actual runtime group composition is not proven.

### BASE-AKU-005 — Authentication has distinct interactive and API-key paths
**Dimension:** Authentication / configuration  
Password credentials are checked through the password hash context for interactive access; non-interactive access may use API-key validation, and a user can be configured to require API keys for RPC.  
**A2 target:** verify actual configured authentication paths and role restrictions.

### BASE-AKU-006 — Self-service field access is deliberately constrained
**Dimension:** Access control  
Self read/write may elevate to sudo only when all requested fields fall inside explicitly allowed self-accessible fields; company switching is filtered against allowed companies. Group changes clear access-related caches.  
**Claim boundary:** static implementation rule.

### WEB-AKU-001 — Web is a core client layer directly dependent on base
**Dimension:** Manifest / dependency  
The `web` module directly depends on `base`, is auto-installed, and defines the core web-client assets, security records, templates, views, reports and test assets.  
**Claim boundary:** source topology only.

### WEB-AKU-002 — Web-client entry is guarded by DB, session and internal-user checks
**Dimension:** Controller / access boundary  
The web-client route ensures database selection and authenticated session, checks session security, rejects non-internal users from the internal client, refreshes session lifetime, and restores the authenticated user into the environment before rendering.  
**A2 target:** verify redirect/session-expiry/internal-vs-external behavior in runtime.

### WEB-AKU-003 — Browser bootstrap carries explicit anti-caching / frame controls
**Dimension:** Security / HTTP surface  
The web-client response sets `X-Frame-Options: DENY` and `Cache-Control: no-store`; the login response uses `SAMEORIGIN` plus a CSP frame-ancestor restriction. A browser cache secret is derived from user session-security values so security events can rotate the browser-side key.  
**Claim boundary:** static header generation; deployed reverse-proxy/header behavior is not proven.

### WEB-AKU-004 — Login and session authentication are separate controller surfaces
**Dimension:** Authentication / controller  
`/web/login` performs interactive login flow and can invoke request reCAPTCHA depending on user logic; `/web/session/authenticate` accepts JSON-RPC credentials, checks the database filter, establishes the session, and returns session information.  
**A2 target:** verify enabled paths, CAPTCHA conditions, DB selection exposure and session renewal behavior.

### MAIL-AKU-001 — Mail is a cross-cutting application, not a leaf utility
**Dimension:** Manifest / dependency / cross-module  
`mail` depends on `base`, `base_setup`, `bus`, `web_tour`, and `html_editor`; its declared scope includes Discuss, mail gateway, chatter, incoming mail and document-linked conversations. It also loads cron, server-action, security, notification, alias, guest and activity surfaces.  
**A1 implication:** mail must be treated as a platform handoff layer touching security, background jobs, external integration and business-document messaging.

### MAIL-AKU-002 — Posting to a mail-thread document defaults to write-level document access
**Dimension:** Business rule / security  
`mail.thread` defaults `_mail_post_access = 'write'`. Model-specific extensions may override it, so downstream modules can materially change posting semantics.  
**A2 / cross-module target:** test representative modules because source inheritance can change this rule.

### MAIL-AKU-003 — Mail behavior can be materially altered by context flags
**Dimension:** Configuration / execution context  
The thread implementation documents context controls that can disable auto-subscription, creation logging, tracking or the entire mail-thread feature set for create/write flows.  
**A1 implication:** source presence of chatter/tracking does not prove runtime tracking occurred for a transaction.

### MAIL-AKU-004 — External/portal follower search is restricted
**Dimension:** Security / external-user boundary  
For non-internal users, follower searching is constrained to the user's own partner/commercial-partner identities; searching other follower identities raises access error.  
**A2 target:** verify portal/public behavior under actual access rules.

### MAIL-AKU-005 — Message access is document-aware and user-class aware
**Dimension:** Security / record access  
`mail.message` applies additional access logic beyond generic ORM access: non-employees are prevented from seeing internal messages/logs, while read/write/create/unlink eligibility considers authorship, creator, recipients/notifications and access to the related document.  
**Claim boundary:** static access algorithm; concrete role matrices must be runtime-tested.

### MAIL-AKU-006 — Linked-message resolution explicitly drops sudo
**Dimension:** Security / anti-bypass  
When resolving message links originating from user-controlled message content, the code deliberately performs the search with `sudo(False)` so arbitrary message IDs do not become readable through elevated context.  
**A1 implication:** this is a security invariant worth preserving conceptually in SMEsPlus, not code to copy.

## 4. Cross-module synthesis

1. `base -> web` is a direct dependency and establishes identity/company/access primitives below the web-client boundary.
2. `mail` sits above `base` and depends on `bus`, `web_tour`, `html_editor`, and setup capabilities, making it a high-coupling bridge rather than an isolated feature.
3. Web session security and base user/company controls must be reconciled together before any A2 authentication or multi-company scenario is designed.
4. Mail access ultimately depends on both mail-specific conditions and the related business document's access rights, so cross-module tests are mandatory; source-only study cannot establish effective runtime access.
5. Context flags in `mail.thread` create a source/runtime gap risk: a feature can exist in source while tracking/logging is intentionally disabled for a specific execution path.

## 5. Contradictions / open gaps

- **GAP-G01-LOCAL-ANCHOR-001:** this packet uses the reproducible public Odoo 19.0 commit anchor. It does not prove byte identity with the governed local `19.0.post20260921` snapshot.
- **GAP-G01-RUNTIME-001:** no A2 runtime proof has been performed for authentication, company switching, web session behavior, external-user access, chatter posting or message access.
- **GAP-G01-QUESTION-001:** existing GMVQ author-side freezes do not equal Independent Question Review PASS. QID-level release remains governed separately.
- **GAP-G01-MAIL-INHERITANCE-001:** downstream modules may override `mail.thread` posting/access behavior; representative inheritors must be mapped before declaring mail-thread semantics complete.
- **GAP-G01-WEB-PROXY-001:** generated HTTP security headers do not prove final deployed headers after reverse proxy / ingress layers.

## 6. Independent challenge — R1

### Functional / SMEs Core challenge
PASS RECOMMENDATION for continued A1 study. Findings are platform/business-behavior relevant, but no end-user workflow completeness claim is made.

### Technical / Architecture challenge
CONDITIONAL PASS RECOMMENDATION. Source pointers are reproducible and exact for the public upstream anchor, but local governed byte identity is unresolved.

### SaaS / Security challenge
CONDITIONAL PASS RECOMMENDATION. Company/user/message access controls expose high-value invariants; tenant isolation is not established by Odoo source and must not be inferred.

### QA / Testability challenge
CONDITIONAL PASS RECOMMENDATION. Each finding yields concrete A2 targets, but runtime evidence is absent and Question Gate clearance is independent.

## 7. R1 disposition

**A1 RECOVERY PILOT R1 = CONDITIONAL PASS RECOMMENDATION FOR CONTINUED STUDY**

This packet proves that the direct Evidence-First study path can produce inspectable primary evidence again. It does **not** authorize A2, does not close G01, does not certify any QID, and does not change Formal Coverage.
