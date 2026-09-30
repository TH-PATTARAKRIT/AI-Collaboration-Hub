# STATE03 Security Advisory — Custom Module Findings (2026-09-30)

Document ID: `STATE03-SECURITY-ADVISORY-2026-09-30`
Status: `CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION` — **not a runtime confirmation, not a claim these modules are installed in any live/production system**; `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET`
Source: Source/Dump Deep Research Worker (Boss's local Claude Code session), read-only static source study, `CUSTOM_MODULE_STUDY/` folder, branch `claude/local-odoo-source-research`, reconciled here by this session (STATE03 Integration/Architecture Knowledge Owner)
Purpose: **Flag findings that are actionable regardless of STATE03's own research-methodology status**, so they reach a decision-maker promptly instead of waiting behind the ordinary evidence-tier review cycle. This document does not change any STATE03 register's evidence status.

## 1. Highest-severity finding: `scgl_jasper_api` — unauthenticated public route can read arbitrary fields on whitelisted models

**Module**: `scgl_jasper_api` (path `addons_Extramodule/addons/scgl_jasper_api`), license LGPL-3, author "SCG Legacy Co., Ltd." (per manifest), version `19.0.1.0.0`. Classified Customer-authorized Custom.

**What the source shows** (static read only, not executed):
- A public HTTP route `/pictures/<model>/<id>/<field>` exists for a whitelist of five models. It runs with `auth="public"` (no login required) and reads data under **elevated rights**, bypassing record rules.
- **There is no check that `<field>` is actually a picture/image field, and no token or credential is required on this route at all.** Any caller who can reach the endpoint and knows or guesses a valid record ID can request any field on those whitelisted models and receive it back as an "image" response.
- A second route, `/pictures/scgl.signature.image/<user_id>/<token>`, is guarded by a single **shared token hard-coded as a constant in the module's own source code**, compared with a plain string match. The worker deliberately did **not** reproduce the token's value in any committed file.
- No outbound calls are made by this module; it exists to let an external JasperReports server pull images for printed documents.

**Why this matters**: if this module is installed and reachable on any environment (test, staging, or production), route 1 is a data-exposure risk independent of the token issue on route 2 — it has no gate at all. This is a control-bypass-by-design finding in actual module code, not a documentation gap or an evidence-tier nuance.

**What is NOT yet known** (and should be checked before deciding this needs urgent remediation):
- Whether `scgl_jasper_api` is actually installed on any reachable environment (this research only confirms the module exists in the source tree studied, on Boss's own machine — installed status is unconfirmed).
- Which of the five whitelisted models are involved, and what field-level data exposure that implies in practice (not detailed further here, to avoid amplifying the risk by cataloguing it).
- Whether the shared token has ever been rotated, or reused elsewhere.

**Recommended immediate action (for whoever owns the actual runtime environment(s), not a STATE03 research task)**: confirm whether this module is installed anywhere reachable from outside a trusted network; if so, restrict or disable the affected route(s) until a token/auth check can be added, independent of STATE03's own schedule.

### 1.1 Boss ruling (2026-09-30)

Boss confirmed directly: **`scgl_jasper_api` is not in use** and authorized removing it ("เราไม่ใช้งาน ตัดออกได้เลย"). This resolves the single biggest open unknown in §1 above (installed/reachable status) — Boss's own knowledge of the actual business system is the authoritative answer here, not something this research could determine on its own.

**What this session can and cannot do about it**: this cloud session has no access to any live Odoo environment, and no filesystem access to Boss's own Mac beyond what the separate local Source/Dump Deep Research Worker session has already read and relayed (read-only, Clean-Room). Actually removing the module is therefore **outside what either Claude session can execute from here** — it requires action on the real environment(s) that hold it. This document is updated to record the decision; the removal action itself is Boss's (or his ops team's) to carry out.

**Recommended concrete steps for whoever executes the removal** (not performed by this session):
1. If `scgl_jasper_api` was ever installed in any Odoo database (not just present as a folder), uninstall it properly through Odoo first (Apps → the module → Uninstall) rather than only deleting the source folder — a bare file deletion can leave orphaned records/menu entries and, in the worst case, break on next upgrade.
2. Then remove the module folder (`addons_Extramodule/addons/scgl_jasper_api`) from every addons path that carries it, including any of the working copies the source/dump research has been reading from (per this Advisory's own provenance, at least the machine used for STATE03's Clean-Room study).
3. If any external JasperReports server configuration still points at either of this module's two routes, update or remove that configuration too, since the routes themselves going away is what actually closes the exposure.

**Status of this item**: Boss-ruled `NOT IN USE — REMOVAL AUTHORIZED`, execution pending (owner: Boss / his ops team, not this session or the research worker).

## 2. Other control-bypass findings from the same round (lower urgency, still worth owner attention)

| Module | License / class | Finding |
|---|---|---|
| `account_asset_management` | AGPL-3, Third-party | "Delete entry" on a depreciation line force-deletes an already-posted journal entry via core's own `force_delete` context, which explicitly skips the sequence-gap guard, the audit-trail guard, and the posted-line delete guard |
| `scgl_advance_expense_request` / `smesplus_advance_expense_request` | LGPL-3, Customer/Company custom | Write cancel-state directly onto vendor bills, skipping core's own cancel-button validation steps |
| `scgl_report_viewer` | LGPL-3, Customer-authorized | Tax-report engine reads ledger data via direct database queries that bypass ORM record rules, scoped only to the "active company" (not the full multi-company allowed set) |
| `purchase_request_level_approve_po` | LGPL-3, Third-party | The last step of its multi-level PO approval calls core's own approve action directly, skipping core's confirmation checks and amount-based double-validation |
| `purchase_request_level_approve` | LGPL-3, Third-party | Four approval settings are saved in configuration but never read anywhere in the module's own code (a dead-configuration finding, not a bypass, but a false sense of control) |
| `sale_order_level_approve` | LGPL-3, Company | Blocks sale-order confirmation for everyone except the superuser — including, per the same note, portal auto-confirmation |

All of the above are `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET` — presence in the source tree studied does not confirm installation on any live environment. None of these findings are runtime-confirmed.

## 2.1 General compatibility risk pattern (not a single module, a class of risk)

The worker separately noted that several custom modules use pre-Odoo-19 constructs (old-style SQL uniqueness declarations Odoo 19 no longer enforces via `_sql_constraints`, removed fields/methods, or version strings from 17/18) — in each such case, the control the module *appears* to add **silently does not run at all** under Odoo 19, rather than erroring. This is a pattern worth checking across the custom-module estate generally, not just the modules named above.

## 3. Reconciliation into STATE03 canonical registers

The `account_asset_management` and `scgl_advance_expense_request`/`smesplus_advance_expense_request` findings are reconciled into `PERIOD_CUTOFF_VALIDATION_PILOT/22_UNKNOWN_AND_GAPS.md` (`GAP-PCO-01`). The `scgl_report_viewer` finding is reconciled into `MULTICOMPANY_ISOLATION_PILOT/22_UNKNOWN_AND_GAPS.md` (`GAP-MCT-02`). The purchase-approval findings are not yet reconciled into a canonical Gap-ID — Purchase is a Carry-forward domain from `GROUP_01_SALES_INVENTORY_PURCHASE`, not this register's own primary evidence; flagged here for whoever owns that track. Full technical detail (file+line pointers) is in `TEAM_A/04_EVIDENCE_PACKS/CUSTOM_MODULE_STUDY/` on the `claude/local-odoo-source-research` branch, cited by reference, not merged.

## 4. What this document is not

Not a Gate PASS, not Formal Coverage, not a claim of installed/live exposure, not authorization for any remediation code change, and not a substitute for a proper security review by whoever owns the actual running environment(s). It exists solely so this class of finding is not stuck behind STATE03's ordinary documentation-tier review cycle.
