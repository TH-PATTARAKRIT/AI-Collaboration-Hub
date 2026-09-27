# G01 Evidence-First Recovery — Primary A1 Evidence R4

Date: 2026-09-27 (Asia/Bangkok)
Branch: research/g01-evidence-first-recovery-20260926
Scope: G01 A1 recovery expansion — resource, resource_mail, privacy_lookup
Scope change: NONE
Governance change: NONE
Denominator change: NONE
Architecture change: NONE
Source anchor: odoo/odoo 19.0 @ 8d05257d83f9128953f580a066db67c48fcdb96f
Governed local Community19 byte identity: NOT VERIFIED; authoritative source device offline
Runtime/A2: NOT EXECUTED
Formal Coverage: NOT AUTHORIZED / NOT CALCULATED

## 1. Governed roster basis
The governed G01 A1 static intake includes resource, resource_mail, and privacy_lookup in the 23-module G01 roster:
- 99_SMEsPlus_Enterprise_Suite/01_Governance/COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/G01_PLATFORM_BASE_A1_STATIC_INTAKE_V1.00.md
Question-programme status artifacts also track these modules inside G01. This packet is A1 source evidence only and does not convert question-programme counts into Functional Coverage.

## 2. Verified exact source pointers
- addons/resource/__manifest__.py — 72b99e4faad899e6631ba8d1d96698b9c7ff1e0f
- addons/resource/models/resource_resource.py — aad3af2f8b87bff4cc650819abc2856fdb826067
- addons/resource/security/resource_security.xml — 500b70f06c5fb917bd5657bbaaf23843920dae0c
- addons/resource/security/ir.model.access.csv — 34ca64a5e94929feffacb29fae63b73e78a0b3c7
- addons/resource_mail/__manifest__.py — 032a25c2cd5c1be067974b60ca1efb7c5848d54c
- addons/resource_mail/models/resource_resource.py — 797be7bd04f8ef3f089dbda74db6cf9841b84406
- addons/privacy_lookup/__manifest__.py — 9eaa9987cdaa97b006c5fea0f961016490f811cd
- addons/privacy_lookup/wizard/privacy_lookup_wizard.py — 3b6d52e055a912c67e85970d0299de14d97cc619
- addons/privacy_lookup/models/privacy_log.py — 045a2d25f7115f860d558c28d0d2f80301b64781
- addons/privacy_lookup/models/res_partner.py — 19962c362f2b31fd12ad0aa383071db82fbd97d5
- addons/privacy_lookup/security/ir.model.access.csv — d70edab351c9369c4e8100145b9006d1043029fe
- addons/privacy_lookup/data/ir_actions_server_data.xml — 7aac52ec8a0b8773de14cfc1670da285eeacf952

All 12 blob SHAs were revalidated against the anchored upstream commit before this artifact was persisted.

## 3. New verified AKUs

### RESOURCE-AKU-001 — Resource is a platform scheduling module
resource depends on base and web and loads ACL/rule/calendar surfaces. Static dependency only.

### RESOURCE-AKU-002 — Resource records are company-sensitive
resource.resource has company_id defaulting to the active company; calendar_id is domain-restricted to the selected company.

### RESOURCE-AKU-003 — Company/calendar defaults are executable configuration behavior
On creation, a resource with company_id and no calendar_id inherits the company's resource calendar. Missing timezone can be derived from user or calendar.

### RESOURCE-AKU-004 — Resource identity can bridge to user identity
resource.resource may link user_id and exposes related share/email/phone data. This is a source-level identity bridge, not a runtime disclosure proof.

### RESOURCE-AKU-005 — Efficiency has a hard positive invariant
time_efficiency is required and constrained by CHECK(time_efficiency > 0).

### RESOURCE-AKU-006 — Resource write can suppress no-op updates under explicit context
When check_idempotence is set for a single record, write removes values equal to current values and returns without write when no changes remain.

### RESOURCE-AKU-007 — Resource/calendar ACL is role-sensitive
Internal users have read-only access to resource calendars/attendance/resources in the declared ACL set while system users receive full calendar/attendance permissions. Effective access also depends on record rules.

### RESOURCE-AKU-008 — Leave modification has own/global and multi-company rule boundaries
Resource leave rules distinguish employee own/global access and admin global modification, and constrain company_id to active company_ids plus False.

### RESOURCE-MAIL-AKU-001 — resource_mail is an auto-installed cross-module bridge
resource_mail depends on resource and mail and is auto-installed.

### RESOURCE-MAIL-AKU-002 — Presence and avatar-card data are exposed through the resource bridge
The extension relates im_status to user_id.im_status and get_avatar_card_data returns a normal read(fields) result. Effective field access remains runtime/ACL-dependent.

### PRIVACY-AKU-001 — privacy_lookup is an auto-installed mail-dependent administrative surface
privacy_lookup depends on mail and is auto-installed. Its wizard, lines and persistent log ACLs are limited to base.group_system.

### PRIVACY-AKU-002 — Lookup validates normalized email and scans persistent models
The lookup normalizes the supplied email and raises on invalid format. It enumerates model metadata but excludes transient and non-auto models from the broad search path.

### PRIVACY-AKU-003 — Lookup explicitly flushes ORM state before SQL execution
action_lookup calls env.flush_all() before executing the generated SQL query. Source presence does not prove production timing or transaction behavior.

### PRIVACY-AKU-004 — Display/reference behavior has two different privilege paths
resource_ref first checks normal read access and suppresses references that fail read access, while res_name is computed through sudo(). This creates a disclosure boundary requiring negative-role runtime proof.

### PRIVACY-AKU-005 — Remediation actions execute with sudo and include bulk/idempotence guards
Archive/unarchive and unlink execute against target records with sudo(). Duplicate unlink is rejected; bulk archive/delete skip already-inapplicable lines. Authorization, audit and blast-radius behavior require runtime/config proof.

### PRIVACY-AKU-006 — Remediation is persisted into an anonymized handler-attributed log
privacy.log is persistent, stores date, anonymized name/email, current user as Handled By, execution details and found-record descriptions. Wizard and line models are transient with 24-hour maximum age.

## 4. Cross-module synthesis
1. resource couples company, calendar, user identity and leave authorization; company context must not be mistaken for SMEsPlus tenant isolation.
2. resource_mail creates a presence/data bridge from mail/user state into resources; field-level and role-level exposure require A2 proof.
3. privacy_lookup is intentionally administrative but uses both normal-access checks and sudo execution/display paths; remediation and disclosure must be tested separately.
4. privacy remediation is destructive and persistent-log-backed; archive/delete idempotence, company boundaries, audit completeness and rollback behavior are runtime concerns.
5. Source Presence != Runtime Reachability: none of these findings prove enabled configuration, reachable UI/action paths, or deployed authorization behavior.

## 5. QID trace candidates — NOT release credit
Source-backed privacy_lookup candidates in the governed W1-B11 bank:
Q001, Q008, Q009, Q013, Q014, Q017-Q030, Q033, Q034, Q036.
They remain A1-PARTIAL / RUNTIME-REQUIRED. This packet does not provide Independent RED TEAM per-QID PASS.

## 6. Gap delta
OPEN carry-forward:
- GAP-G01-LOCAL-ANCHOR-001
- GAP-G01-RUNTIME-001
- GAP-G01-QUESTION-001

NEW:
- GAP-G01-RESOURCE-CALENDAR-RUNTIME-001
- GAP-G01-RESOURCE-LEAVE-AUTHZ-RUNTIME-001
- GAP-G01-RESOURCE-MAIL-RUNTIME-001
- GAP-G01-PRIVACY-SUDO-REMEDIATION-001
- GAP-G01-PRIVACY-LABEL-DISCLOSURE-001
- GAP-G01-PRIVACY-COMPANY-RUNTIME-001

## 7. Role-based challenge — not formal independent clearance
Functional: PASS RECOMMENDATION for continued A1 study.
Technical: CONDITIONAL PASS — exact upstream source pointers verified; governed local byte identity remains unavailable.
SaaS/Security: CONDITIONAL PASS — sudo remediation, label disclosure and company-boundary behavior require negative/runtime proof.
QA: CONDITIONAL PASS — concrete role, company, archive/delete, duplicate-action and disclosure scenarios exist.
Question Governance: HOLD for release credit — mandatory independent per-QID clearance is not established.

## 8. Disposition
A1 RECOVERY PILOT R4 = CONDITIONAL PASS RECOMMENDATION FOR CONTINUED STUDY.
This artifact is Primary A1 source evidence for the three listed G01 modules only. It does not authorize A2, certify any QID, close G01, change the denominator, or authorize Formal Coverage.
