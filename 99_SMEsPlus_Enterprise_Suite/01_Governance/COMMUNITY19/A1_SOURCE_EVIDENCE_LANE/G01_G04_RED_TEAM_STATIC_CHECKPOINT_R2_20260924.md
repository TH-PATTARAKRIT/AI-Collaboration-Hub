# SMEsPlus Community19 — RED TEAM G01-G04 Static Checkpoint R2

Date: 2026-09-24
Mode: SOURCE/STATIC ONLY for this run
Runtime A2/A3/MASTER: NOT AUTHORIZED in this run
Formal Coverage: NOT CALCULATED

## G01 PLATFORM_BASE

Verified delta: `base` was deepened beyond manifest/dependency intake using current upstream Odoo 19.0 source anchor.

Static findings now re-anchored:
- `base` manifest: name Base, version 1.3, Hidden, LGPL-3, installable, auto_install, post_init_hook.
- Core model families include metadata/model registry, actions, views, menus, attachments, cron, record rules, config parameters, companies, groups, users, devices, partner/currency/country/bank and report primitives.
- `res.company` is hierarchical and partner-backed; root-delegated field set currently includes `currency_id`; company duplication is blocked.
- `res.users` delegates to `res.partner`, enforces unique login, separates current company from allowed companies, and computes implied groups separately from explicit groups.
- `ir.rule` evaluates with user/current-company/activated-company context; global rules are ANDed and group rules are ORed before combination; superuser mode bypasses record rules.
- Base multi-company security is company-scoped, not tenant-scoped. ERP manager company rule is unrestricted at the record-rule layer.
- `ir.config_parameter` is per-database key/value storage with unique key and default security/login parameters.
- `ir.cron` is delegated from server actions and has explicit scheduling/failure-state controls; source presence is not execution proof.
- `ir.ui.view` supports primary/extension inheritance, group restriction, DB/file architecture and per-user custom view records.

A1 disposition: ACTIVE / VERIFIED STATIC DELTA / BASE NOT COMPLETE.
Question Gate: G01 GMVQ directory exists, but downstream eligibility must be evaluated per exact module/batch; no runtime execution was performed in this run.

## G02 IDENTITY_ACCESS

Governed count: 11.
Exact technical roster: NOT RECOVERED in this run.
Evidence state: current A1 index still requires roster evidence; repository GMVQ root has no G02 governed question-bank directory.
A1 action: roster recovery attempted against controlled `GROUP_STRUCTURE_V2_CORE.tsv` pointer and connected desktop source environment; exact row-level mapping was not obtained, so no module membership was invented.
Disposition: A1 ACTIVE / ROSTER RECOVERY OPEN / WAIT QUESTION.

## G03 MASTER_DATA

Governed count: 11.
Exact technical roster: NOT RECOVERED in this run.
Evidence state: current A1 index still requires roster evidence; repository GMVQ root has no G03 governed question-bank directory.
A1 action: roster recovery attempted; exact controlled row mapping remains unavailable. No module membership credit is granted from semantic similarity alone.
Disposition: A1 ACTIVE / ROSTER RECOVERY OPEN / WAIT QUESTION.

## G04 ACCOUNT_BASE

Governed count: 9.
Exact technical roster: NOT RECOVERED in this run.
Evidence state: current A1 index still requires roster evidence; repository GMVQ root has no G04 governed question-bank directory.
A1 action: roster recovery attempted; accounting source families must not be attributed to G04 until controlled row-level membership is recovered.
Disposition: A1 ACTIVE / ROSTER RECOVERY OPEN / WAIT QUESTION.

## Question Gate Reconciliation

Current Community19 GMVQ root exposes only `G01_PLATFORM_BASE` plus governance/order documents. No governed G02/G03/G04 directory is present. Therefore G02-G04 remain blocked from A2 Runtime, Reconciliation, A3 and MASTER. No question set was invented.

## Static Red-Team Challenge

1. Company controls in `base` do not prove SaaS tenant isolation.
2. ACL/record-rule presence does not prove effective runtime access.
3. Cron definitions do not prove scheduled jobs execute.
4. Upstream Odoo 19.0 source anchor does not by itself prove byte identity with the governed local Community19 distribution.
5. Group counts are planning/control counts, not a Canonical Function-ID denominator.

## Open Evidence Gaps

- Recover exact `GROUP_STRUCTURE_V2_CORE.tsv` row-level bytes or equivalent Boss-controlled current roster.
- Re-anchor source findings to the governed local Community19 package/tree hash.
- Complete G01 `base` extraction for remaining model/action/menu/attachment/API-key/device/module-lifecycle/HTTP surfaces and tests.
- Do not open A2/A3/MASTER for G02-G04 until exact governed question banks are present, verified, and eligible/frozen.

No Evidence = No Progress.
Source Presence != Runtime Reachability.
