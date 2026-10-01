# B00 — Checkpoint Reconciliation (STATE03 Odoo 19 Community Very Deep Research, L0–L3)

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Not a register, denominator, coverage figure, V-level or gate. Read-only source; Community only (all 692 manifests LGPL-3; no OEEL-1 / OPL-1 / Enterprise manifest in the Community tree). Date: 2026-10-01.

## 1. Worktree / branch validation (L0)
| Item | Result |
|---|---|
| Worktree | `AI-Collaboration-Hub-STATE03-DEEPSEEK` |
| Branch | `claude/local-odoo-source-research` (tracks `origin/claude/local-odoo-source-research`) |
| Status at start | clean (no modified/untracked paths) |
| HEAD at start | `bf481ebe` (STATE03 source/dump worker checkpoint) |
| Source tree | `odoo-19.0.post20260921` — read-only; no write performed |
| Dump ZIP | sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c` — **matches contract**; ZIP not modified (only read/extracted copies in a session scratch area) |

## 2. Carry-forward audit (DELTA-FIRST)
| Carried item | State found | Disposition |
|---|---|---|
| `STATE03_SOURCE_DUMP_EVIDENCE_DELTA_HANDOFF.md` (Rounds 1–4, append-only) | present | **valid, kept**; this work is appended as Round 5 |
| `SOURCE_MAP_CANDIDATE/` (300 module records + index) | present, `L1-CANDIDATE`, 0 `L1 COMPLETE` | **valid as candidate; not recreated**; re-audit by module as L2/L3 touches it |
| Restricted-local structural extracts (692), trace notes (300 core, 117 custom) | present on this machine (not in git) | reused as inputs; custom/third-party notes are **out of scope** for this execution (see §6) |
| `DB_SCHEMA_ONLY/` | derived from the **older** `iTEST02_2026-06-14` schema-only dump | **MATERIAL DELTA — superseded as the DB baseline** by `iTest19C_2026-09-21` (below). Files not deleted or rewritten; marked "pre-delta baseline" for re-audit |
| Interrupted L2+L3 drafts (8; 3 partial, 5 stubs) | not usable | **invalidated for reuse**; function studies are redone from source |
| Existing Function-IDs | 53 IDs across 10 pilot domain registers (`06_DOMAIN_RESEARCH/*/04_FUNCTION_REGISTER.md`) + `DOMAIN_01_ACCOUNTING_CORE` uses its own `FN-nn` series | indexed in `EXISTING_FUNCTION_ID_INDEX_53.json`; any capability without a matching ID is **FUNCTION MAPPING REQUIRED** (no IDs invented) |
| G01–G16 mappings | `GROUP_STRUCTURE_V2_CORE_CANDIDATE_20260928.tsv` (CANDIDATE, 54 rows; not Boss-approved) and `COMM_Group` column of the register workbook | used only as navigation hints; no group is treated as frozen |
| DR002 prompts | `INVENTORY_CORE_BACKBONE/DEEP_RESEARCH_DR002` (readiness + new-session prompt) | read as lineage; inventory capabilities scheduled in batch B04 |
| Previously reported blocker (agent spend limit, HTTP 429) | cause was monthly account quota | to be re-probed at first delegated launch; not assumed cleared |

## 3. Module universe reconciliation (no count is canonical)
Three independent module sets were compared by technical name.

| Set | Count | Provenance |
|---|---|---|
| Source tree `odoo/addons` (modules with a manifest) | **692** | read-only source; all LGPL-3 |
| On-disk register workbook (`…Master_Register_V1.00.xlsx`): CURRENT / NEXT / EVIDENCE-ONLY | 300 / 108 / 284 (= 692) | content check: union equals the source tree exactly; the CURRENT 300 equal the 300 source-map records exactly |
| Dump `manifest.json` modules = DB `ir_module_module` state `installed` | **356** | the two agree exactly; the installed set is closed under declared dependencies and all 356 exist in the source tree |
| Runtime export workbook `Module (ir.module.module) (6).xlsx` | 254 installed / 406 not installed / 23 uninstallable | **different (older/other) runtime snapshot** — does not match the dump's 356; recorded as a contradiction, not used for scope |

Cross-tabulation (installed in dump × register phase): CURRENT 279 · NEXT 38 · EVIDENCE-ONLY 39.
- **21 CURRENT modules are not installed in the dump** (so their runtime reconciliation is impossible with this dump): `account_debit_note`, `account_tax_python`, `account_test`, `account_update_tax_tags`, `auth_ldap`, `auth_oauth`, `auth_password_policy`, `auth_password_policy_portal`, `auth_password_policy_signup`, `auth_timeout`, `base_address_extended`, `base_sparse_field`, `base_vat`, `board`, `cloud_storage`, `cloud_storage_azure`, `cloud_storage_google`, `cloud_storage_migration`, `l10n_account_withholding_tax`, `website_cf_turnstile`, `website_slides_forum`. Their behavior is **source-only; configuration/runtime context UNKNOWN**.
- **77 installed modules are outside the 300** = `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` (38 NEXT-PHASE, 39 EVIDENCE-ONLY): 22 `payment_*` provider modules, 12 `mass_mailing*` / `website_mass_mailing*` modules, 3 `website_event*` modules, 35 `test_*` framework modules, `theme_test_custo`, and 4 others (`account_peppol_advanced_fields`, `account_qr_code_sepa`, `delivery_mondialrelay`, `marketing_card`). Full per-module table: `MODULE_UNIVERSE_RECONCILIATION_692.tsv`. Of these, the ones reached from Sales/Purchase/Inventory/Accounting/O2C/P2P traces are studied as supporting modules (batches B02–B07); `test_*` are evidence of framework tests only, not business functions.
- `ir_module_module` also lists **23 `uninstallable` entries**; 21 of them have **no Community source on disk** (names only; marketplace/enterprise-side entries — **out of scope, not opened, no behavior attributed**). The other two are `iot_box_image`, `iot_drivers` (present in source, flagged uninstallable).
- Denominator status: **NOT FROZEN.** 692 is the source population; 300 is a working phase; 356 is the dump's installed set. None is declared canonical.

**Register hash finding (re-audited):** workbook on disk sha256 `790bcd2a…fe82a1` vs recorded `76aa648b…130c6b`. Content is internally consistent (see above) but the byte-level hash difference is **unexplained** (file mtime 2026-09-21 19:01). Status stays `MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION` (PMO/Boss action; nothing here "fixes" it).

## 4. Dump restore contract (isolated research restore)
| Item | Value |
|---|---|
| Archive | `iTest19C_2026-09-21_11-12-55.zip`, sha256 above; contains `dump.sql` (plain SQL), `manifest.json`, `filestore/` (attachment blobs; **not extracted** in this batch) |
| `dump.sql` sha256 | `abdc19d25ec20b9607f7f73603a11e5aa100b946327a1f34f99791a02e9ae612` (extracted copy, scratch) |
| Dump origin | database `iTest19C`, Odoo `19.0-20260921`, dumped from PostgreSQL 15.19 |
| Restore engine | PostgreSQL **18.6** (Homebrew), fresh private cluster, `trust` auth, **Unix-socket only (`listen_addresses=''`)**, port 54329, `fsync=off` |
| Isolation | cluster created for this session only; no other cluster/database touched (another postgres process on the host was left alone) |
| Restore | `psql -f dump.sql`; **0 errors, 0 warnings in stderr**; ≈6 s |
| Result | 1,435 public tables; DB size 129 MB; `ir_module_module`: 356 installed / 334 uninstalled / 23 uninstallable |
| Data character | **near-empty test database**: 1 company, 4 users, 7 partners; 0 journal entries, sale orders, purchase orders, stock pickings or stock moves. Therefore reconciliation covers **configuration, seeded data, access rules, schedulers and automation records — not transactional behavior** |
| Data handling | no row-level business content is written to git; only counts, names of seeded configuration records and structural facts |
| Cleanup | **OPEN** — cluster and scratch files are removed at the end of the DB phase; completion is recorded in the final checkpoint. Source ZIP never modified |
| Not claimed | no Odoo server was started; no L5/AWT proof; anything depending on runtime execution is **RUNTIME/AWT REQUIRED** |

First DB-side observation recorded as a delta (OBSERVATION): a stock-valuation-layer table (`stock_valuation_layer`, known from earlier-version structure) **does not exist** in the restored schema. Where valuation is held in this version is **UNKNOWN until batch B04 reads source**; any earlier statement that presumes a valuation-layer structure is `RE-AUDIT REQUIRED`.

## 5. Execution batch plan (continues the existing priority: foundation → Sales → Purchase → Inventory → Accounting → O2C/P2P → optional)
| Batch | Scope | Output |
|---|---|---|
| B00 | this reconciliation | this file |
| B01 | incremental Source↔DB reconciliation for all 356 installed modules (models, fields, ACL, record rules, groups, crons, server actions, automations, views, menus, settings keys) | `03_DB_RECONCILIATION/` |
| B02 | foundation: `base`, `product`, `uom`, `analytic`, `mail`, `portal`, `base_automation`, `sales_team`, `resource`, `utm` + multi-company/data-scope mechanics | restricted + neutral |
| B03 | Sales: `sale`, `sale_management`, `sale_stock`, `sale_margin`, `sale_loyalty`, `sale_crm`, supporting | restricted + neutral |
| B04 | Inventory: `stock`, `stock_account`, `stock_landed_costs`, `stock_delivery`/`delivery`, `stock_dropshipping`, `stock_picking_batch` | restricted + neutral |
| B05 | Purchase: `purchase`, `purchase_stock`, `purchase_requisition`, supporting | restricted + neutral |
| B06 | Accounting: `account`, `account_payment`, `account_check_printing`, `account_edi*`, `l10n_th`, tax/lock/reconcile/payment-term/analytic posting | restricted + neutral |
| B07 | cross-module chains O2C and P2P (state transitions, reversal paths, accounting/stock side effects) | restricted + neutral |
| B08+ | optional domains (MRP, project/timesheet, CRM, HR, website/e-commerce, payment providers, themes) | after B07 |

Each capability study covers: happy path · reversal/cancel/negative path · multi-company/data scope · side effects & cross-module triggers · configuration/optionality · validation/constraints · roles/permissions · scheduled/automated behavior · exceptions/failure · accounting/stock/audit/security/compliance implications. Claims carry: Claim-ID, Function-ID (or `FUNCTION MAPPING REQUIRED`), source origin, evidence pointer, source revision (`19.0.post20260921`), Fact/Observation/Inference/Unknown class, configuration condition, contradiction/unknown/runtime flag, neutral abstraction.

## 6. Scope boundaries restated
- Out of scope and not attributed to Community: OEEL-1 / Enterprise, OPL-1, proprietary modules, `Extra_Thailand`, `Extra_Module_scgl`. The earlier `CUSTOM_MODULE_STUDY/` (117 notes) is **retained as prior evidence but is not extended or relied on** in this execution. Where Community behavior is described, it is stated as the Community source behavior only.
- Not claimed here: V-level, Module/Function Complete, coverage percentage, denominator freeze, Gate PASS, Clean-Room compliance approval.

## 7. Blockers
None on the critical path. Open items: register hash mismatch (PMO/Boss), 21 CURRENT modules not installed in the dump (source-only), L4 independent challenge and L5/AWT (outside this execution), delegated-agent quota to be re-probed.
