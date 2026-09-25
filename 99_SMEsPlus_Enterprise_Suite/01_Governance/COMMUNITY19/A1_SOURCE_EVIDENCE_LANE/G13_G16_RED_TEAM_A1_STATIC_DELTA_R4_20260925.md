# SMEsPlus Community19 - G13-G16 RED TEAM A1 Static Delta R4

Date: 2026-09-25
Mode: Four independent logical RED TEAM stations
Pipeline: A1 Source Evidence -> QUESTION GATE -> A2 Blind Runtime -> Reconciliation -> A3 Independent Adversarial Verification -> MASTER

## Station state

| Group | A1 Source Evidence | QUESTION GATE | Downstream |
|---|---|---|---|
| G13 PEOPLE | ACTIVE - additional upstream source evidence admitted as secondary source-trace only | WAIT QUESTION | A2 / Reconciliation / A3 / MASTER BLOCKED |
| G14 COLLABORATION | ACTIVE - additional upstream source evidence admitted as secondary source-trace only | WAIT QUESTION | A2 / Reconciliation / A3 / MASTER BLOCKED |
| G15 DASHBOARD_REPORT | ACTIVE - additional upstream source evidence admitted as secondary source-trace only | WAIT QUESTION | A2 / Reconciliation / A3 / MASTER BLOCKED |
| G16 TECHNICAL_INTEGRATION | ACTIVE - additional upstream source evidence admitted; material roster delta 20 -> 19 remains open | WAIT QUESTION | A2 / Reconciliation / A3 / MASTER BLOCKED |

## Roster reconciliation control

- Current governed A1 counts remain G13=29, G14=16, G15=11, G16=19.
- Historical Group Structure V2 counts remain G13=29, G14=16, G15=11, G16=20.
- Historical controlled roster pointer remains GROUP_STRUCTURE_V2_CORE.tsv with carried-forward SHA-256 203ff43e7844a734de5e9aaebb91529e46dd7998423d4d5772999ed0db9ff5bf.
- Authorized desktop device remains offline in this run, so the historical TSV row bytes are not runtime-reachable and the hash cannot be freshly recomputed.
- No technical module name is admitted as the G16 changed/reclassified row by inference. The G16 20 -> 19 delta remains MATERIAL DELTA OPEN.

## Static source evidence delta R4

The evidence below is from the public upstream Odoo 19.0 branch observed on 2026-09-25. It is secondary source-trace evidence only. It does not prove controlled Community19 package byte equality, governed roster membership, runtime reachability, configuration reachability, or Formal Coverage.

### G13 PEOPLE

- addons/hr_holidays/models/hr_leave.py: confirms hr.leave behavior around request dates, employee/calendar linkage, duration, approval actors, approval state restrictions, allocation/balance computation, and validation constraints.
- Delta value: expands PEOPLE static evidence beyond employee/attendance anchors into time-off lifecycle and approval controls.

### G14 COLLABORATION

- addons/mail/models/models.py: confirms collaboration-supporting mail base behavior including suggested recipients, reply-to construction, alias handling, and generic mail integration at the ORM layer.
- addons/calendar/models/calendar_alarm_manager.py: confirms event alarm management and scheduled notification support for calendar collaboration.
- Delta value: expands COLLABORATION static evidence beyond mail.thread into recipient/alias behavior and calendar notification control.

### G15 DASHBOARD_REPORT

- odoo/addons/base/models/ir_actions.py: confirms the generic action framework, including action binding, report binding_type, model linkage, server-action sequencing, and scheduled-action linkage.
- Delta value: expands DASHBOARD_REPORT static evidence beyond report rendering endpoints into the underlying action/report binding framework.

### G16 TECHNICAL_INTEGRATION

- addons/auth_oauth/models/res_users.py: confirms OAuth provider/user identity linkage, unique provider+OAuth UID constraint, protected token storage, token removal authorization, provider validation RPC, and OAuth sign-in plumbing.
- Delta value: expands TECHNICAL_INTEGRATION static evidence beyond OAuth controller routing into identity/token persistence and authorization controls.
- This evidence is not used to identify the unresolved historical G16 roster row.

## QUESTION GATE re-verification

- GitHub repository search found no governed frozen question-bank package explicitly eligible for exact COMM-G13, COMM-G14, COMM-G15, or COMM-G16 group/module/batch scope.
- Jira ERPPLUS-171 remains an A1-only control record and does not supply an eligible frozen question bank for these four groups.
- Existing G01 banks/freeze artifacts are not eligible substitutes.

Therefore each station independently remains A1 -> WAIT QUESTION. No A2 Blind Runtime, Reconciliation, A3, or MASTER transition is authorized in this delta.

## Integrity controls

- No Evidence = No Progress.
- Source Presence != Runtime Reachability.
- Upstream source presence != controlled package byte equality.
- No guessed roster membership.
- No improvised question bank.
- No gate bypass.
- Formal Coverage remains prohibited until the Canonical Function-ID denominator is Boss-frozen.

Final state: G13-G16 continue independently in A1. Static source evidence advanced for all four groups. G16 20 -> 19 remains unresolved pending direct controlled row-level roster evidence.
