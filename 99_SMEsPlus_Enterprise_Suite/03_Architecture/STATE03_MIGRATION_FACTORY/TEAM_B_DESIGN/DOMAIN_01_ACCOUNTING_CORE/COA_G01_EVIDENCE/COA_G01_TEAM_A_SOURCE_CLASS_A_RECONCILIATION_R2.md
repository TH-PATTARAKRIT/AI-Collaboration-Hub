# COA-G01 Round 2 — Team A Source Class A Completeness Reconciliation

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Inventory substantive Team A Accounting Core evidence (process, state/event, integration, security, edge-case, migration, data) and record inclusion/exclusion/relevance | Claude (session SMEPLUS-26-08-30-COA-G01R2-001) | GitHub `SMEsPlus` branch, `TEAM_A/` tree | 2026-08-31 | ChatGPT Independent Review (pending); Boss (pending) | Class A = **VERIFIED FACT, evidenced to structural/rule/mechanism depth; not to operational-behaviour or statutory depth (by Team A's own explicit statement)** | Closes AR record Q-02/E-01 |

## 1. Full inventory (62 files read this session, `TEAM_A/` tree)

| Location | Files | Content |
|---|---|---|
| `01_SOURCE_REGISTRY/` | 8 md + 2 machine files | Governance verification, source landscape, database dump register, module master register (1,504 modules, SHA-256 `f11b1d74…5e5faac`), source baseline reconciliation, source manifest, source tree inventory |
| `04_EVIDENCE_PACKS/DOMAIN_01_ACCOUNTING_CORE/` | 1 file, 166 lines | Canonical Claude evidence pack summary |
| `06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/` | 31 files | Part 1 (Fable) domain research: capability map, function register, process register, business rule register (BR-01..21), state/event register, mathematical model register, data semantic register, database observation (4 files), configuration/security/automation/integration/report/edge-case/migration/cross-vendor/provenance/classification/quarantine/unknown registers, Team B candidate input, evidence completeness, domain status |
| `06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/SONNET_DEEP_SYNTHESIS/` | 17 files | Part 2 (Sonnet) deep logic synthesis: critical-finding reasoning, accounting-principle register, business-invariant register (GR-xx), state/event logic analysis, mathematical reasoning, cross-source triangulation, exception/failure analysis, classification reassessment, **residual unknown register (20-item)**, Team B candidate input v2, evidence completeness, Fable/Sonnet disagreement register |
| `09_OPEN_QUESTIONS/` | 1 file, 26 lines | Program-level **11-item** unknown/evidence-gap register (not domain-specific) |
| `05_QUARANTINE/` | 2 files | Clean-room quarantine register (11 gated items: 5 OEEL-1 modules, 3 CLASS-D holds, 2 `ks_*`, vendor pattern/dump-row-data) |
| `A2_SYSTEM_KNOWLEDGE_MAP.md` | 1 file, 86 lines | Cross-domain system map |
| `02_MULTI_SOURCE_RESEARCH/` | README only | No Accounting-Core content |

Directories referenced by the AS prompt as `07_CROSS_DOMAIN_ANALYSIS/` and `08_MIGRATION_ANALYSIS/` **do not exist** as top-level Team A folders — migration classification content is instead inside `06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/17_MIGRATION_CLASSIFICATION.md`. This is recorded as a naming-assumption correction, not a missing-evidence finding.

## 2. Evidence-category completeness (mandatory categories from AS §8.2)

| Category | Assessment | Basis (files, quoted where load-bearing) |
|---|---|---|
| **Process** | **Substantial** | `05_PROCESS_REGISTER.md` — 7 end-to-end processes (PR-01..07) with SE-xx anchors. Example: PR-03 registers *two distinct correction routes* (reset-to-draft vs. reversal) as both existing in source, with neither enforced over the other — directly informs the Do-Not-Merge / reconciliation-behaviour concept fields. |
| **State/Event** | **Substantial** | `07_STATE_EVENT_REGISTER.md` (8 events, two orthogonal statuses `state`/`payment_state`) deepened by `SONNET_DEEP_SYNTHESIS/06_STATE_EVENT_LOGIC_ANALYSIS.md`, which separates vendor technical state from a neutral business lifecycle (RECORDED/COMMITTED/VOIDED/CORRECTED) — this is the clean-room-safe abstraction layer this reconciliation relies on. |
| **Data (structural/DB)** | **Substantial at metadata level; explicitly zero at row-population level** | Directly executed offline `pg_restore -l` TOC census: 28,648 entries, 5,141 FK, 2,763 tables, 1,860 constraints, **0 triggers**. `10_DATABASE_OBSERVATION.md` states row/data-population evidence was deliberately **not obtained** ("would require materialising a database containing customer business and personal data, which this round did not authorise"). This boundary is a deliberate, documented control choice, not an oversight. |
| **Security** | **Thin — explicitly out-of-scope by the researchers' own statement** | `12_SECURITY_PERMISSION_REGISTER.md`: only 5 items; explicitly *"full security model belongs to a separate domain"*; a prior 473-record security inventory exists but *"was not re-derived for this domain."* **Included as Class A evidence with this limitation stated**, not excluded — but any Do-Not-Merge rule resting on security/permission behaviour should be treated as lower-confidence until the security domain is researched. |
| **Integration** | **Thin — coupling inventory only, explicitly not analysed** | `14_INTEGRATION_REGISTER.md`: 10 coupling points (AR/AP, Payments, Tax, Assets, Inventory Valuation, Reporting, Analytic, Reconciliation UI, Budget, Customer layer) listed as dependencies; *"No research performed on the deferred side."* 4 of 10 point into OEEL-1 black-box modules (permanently unreadable under clean-room rule). **Included as Class A evidence** (it correctly identifies *what* is coupled) but does not evidence *how* — downstream Gates (G03, G06, G07) must not assume integration behaviour beyond "a coupling point exists." |
| **Edge-case** | **Substantial** | `16_EDGE_CASE_REGISTER.md` (18 items, EC-01..18) deepened by `SONNET_DEEP_SYNTHESIS/09_EXCEPTION_FAILURE_ANALYSIS.md` (18 scenario rows separating Expected Principle / Reference Behaviour / Independent Evidence / Risk / Unknown). |
| **Migration** | **Substantial** | `17_MIGRATION_CLASSIFICATION.md` (16 items, MC-01..16) with explicit MUST-CARRY / DO-NOT-CARRY / NORMALIZE / DEFER verdicts, e.g. `MC-11`: hash-chain mechanism is `DO NOT CARRY` (vendor-specific) while the *tamper-evidence requirement* carries. |
| **Business rules** | **Substantial** | 21 BR-xx rules (Fable), separated explicitly by enforcement strength: application-only (BR-01..02, BR-04..09) vs. genuinely DB-enforced (`BR-17..20`, via `models.Constraint`, confirmed present in the TOC — note: not `_sql_constraints`, a documented tooling trap for the next reviewer). 13 additional GR-xx neutral rules from Sonnet's synthesis. |

## 3. Inclusion / exclusion rationale

**Included as COA-G01 Class A evidence:** `02_SOURCE_EVIDENCE.md` (SE-01..34 source anchors), `06_BUSINESS_RULE_REGISTER.md` (BR-01..21), `09_DATA_SEMANTIC_REGISTER.md`, `05_PROCESS_REGISTER.md`, `07_STATE_EVENT_REGISTER.md`, `16_EDGE_CASE_REGISTER.md`, `17_MIGRATION_CLASSIFICATION.md`, `CRITICAL_FINDING_REGISTER.md` (6 findings, CF-01..06), and the Sonnet deep-synthesis equivalents where they extend rather than merely restate Part 1. These directly ground the account-concept and Do-Not-Merge reasoning in `COA_G01_CONCEPT_FIELD_COMPLETENESS_R2.md`.

**Included with explicit low-confidence flag:** `12_SECURITY_PERMISSION_REGISTER.md`, `14_INTEGRATION_REGISTER.md` — real evidence, but self-described as thin/deferred. Do not treat silence in these categories as "no risk"; treat it as "not yet researched."

**Excluded (out of Accounting Core / COA-G01 relevance):** `02_MULTI_SOURCE_RESEARCH/README.md` (no content), the sibling `GROUP_01_SALES_INVENTORY_PURCHASE/` domain pack, and the program-level `05_QUARANTINE` items that are non-Accounting modules (OEEL-1 enterprise modules, `ks_*` unknown-loadability modules) — these remain quarantined per existing clean-room rule and are not re-examined here.

**Not re-derived by this session:** row-level/operational-behaviour data (Team A's own stated boundary, respected here rather than re-attempted), and the 473-record wider security inventory (belongs to a future security domain pass, not COA-G01).

## 4. Explicit Team A self-assessment (load-bearing, quoted verbatim)

> `24_EVIDENCE_COMPLETENESS.md`: "This domain is evidenced to structural, rule and mechanism depth. It is not evidenced to operational-behaviour depth (no representative data) nor to statutory depth... No claim of 100% domain completeness is made."

> `25_TEAM_A_DOMAIN_STATUS.md`: "Clean-room Pass NOT declared. Final Pass NOT declared... Next authority: ChatGPT Independent Clean-Room Re-Audit → PMO → Boss Gate."

Both statements are consistent with treating Class A as `VERIFIED FACT` for what it actually covers (structure, rules, mechanisms) while explicitly not extending that status to operational or statutory claims — this reconciliation adopts the same boundary.

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
