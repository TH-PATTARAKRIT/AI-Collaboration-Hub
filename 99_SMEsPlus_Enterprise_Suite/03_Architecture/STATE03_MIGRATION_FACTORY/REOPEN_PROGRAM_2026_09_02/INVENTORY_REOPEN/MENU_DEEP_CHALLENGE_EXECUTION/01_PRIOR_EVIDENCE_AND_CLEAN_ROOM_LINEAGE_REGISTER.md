# 01 — Prior Evidence and Clean-Room Lineage Register

Session: `SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub` | Canonical Branch: `SMEsPlus` (head at session start `788479552971940a126a542da5343944f7f3e0d4`)
Execution Branch: `audit/inventory-menu-deep-challenge-2026-09-02-001` (created from `origin/SMEsPlus` at `7884795`)
Status: `CP-01 OUTPUT — PRIOR EVIDENCE RECONCILED — NOT A GATE DECISION`

This register answers prompt §3: what was studied, what carries forward, what must be reopened for menu/process depth, what must be rewritten as clean-room learning, what conflicts, and what is held for evidence. It was built from immutable commits, not memory.

---

## 1. Evidence Sources Loaded (all verified as real objects on `origin`)

| # | Source | Reference | Verification |
|---|---|---|---|
| 1 | Inventory Reopen New Session Prompt | `BOSS_GATE/REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/01_NEW_SESSION_PROMPT_SMEPLUS-26-09-02-INV-REOPEN-001.md` on `SMEsPlus` | Read in full |
| 2 | Claude Sonnet 5 Max Execution Prompt (reopen) | `.../02_CLAUDE_SONNET_5_MAX_EXECUTION_PROMPT_SMEPLUS-26-09-02-INV-REOPEN-001.md` | Read in full |
| 3 | Session Link Register (reopen) | `.../03_SESSION_LINK_REGISTER_SMEPLUS-26-09-02-INV-REOPEN-001.md` (SMEsPlus head `7884795`) | Read in full; confirms 20/20 deliverables published, execution branch unmerged, `C-05` Boss-visible |
| 4 | Inventory Reopen execution branch | `audit/inventory-reopen-2026-09-02-inv-reopen-001` | `git merge-base --is-ancestor` → **NOT merged** into `SMEsPlus` |
| 5 | Inventory Reopen execution commit | `170af9ea7a5afd127abcaae0ffb40aaa1fa25d4d` (2026-09-02 06:03:19 +0700) | Exists; 20 deliverables under `REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/EXECUTION/` |
| 6 | All 20 reopen deliverables | `01`–`20` | Deliverables `01`, `02`, `13`–`20` read in full by the executor; `03`–`12` read in full by three parallel extraction passes, structured extracts returned and reconciled by the executor |
| 7 | Clean-Room remediation branch | `audit/inventory-core-corr007b-3high-closure-010` | Exists on origin; unmerged |
| 8 | Clean-Room remediation commit | `9996072aa3a353dca99de4b22e8611171e24baf4` (2026-09-02 08:46:16 +0700) | Exists; adds `17_CORR007B_CLEAN_ROOM_REMEDIATION_RECORD.md` |
| 9 | CORR-007B clean-room remediation record | `INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/17_...` | Read in full; remediated file `09` (Layer 1 summary) read in part for valuation learning; file `08` not opened (period-close content taken from reopen `08`/`14`/`20`) |
| 10 | Prior DR/CORR/IDR lineage | R01 → DR-002 → IER-003 → CORR-004 → CORR-005 → IDR-006 → IDR-007 → CORR-006 → CORR-007A → CORR-007B | Carried as reconstructed by reopen deliverable `01` Part B; not re-derived (no material delta trigger) |
| 11 | Accounting / Inventory boundary evidence | Reopen `14`, `20`; CORR-007B `N-A12-01` disposition | Read in full |
| 12 | New Prompt Governance v2.0 | `00_Project_Governance/STATE03_PLUS_PRE_PROMPT_INDEPENDENT_CHALLENGE_RULE.md` (v2.0, effective 2026-09-02) | Read in full |
| 13 | 9 Veto / 9 Special Team Charter | `00_Project_Governance/NINE_VETO_COUNCIL_AND_SPECIAL_TEAM_CHARTER.md` (`SMEPLUS-GOV-9VETO-001` v1.0) | Read in full |
| 14 | Global Challenge Ledger | `00_Project_Governance/GLOBAL_CHALLENGE_CONTINUITY_LEDGER.md` | Read in full; still holds only `GOV-CH-001..003`; no `INV-FP` rows (reopen Track 01 carry-forward unchanged) |
| 15 | Clean Room Learning Directive v2.0 | `00_Architecture_Office/Governance/SMEsPlus_Clean_Room_Learning_Directive_v2.0.md` | Read in full |
| 16 | This session's prompt | `04_NEW_SESSION_PROMPT_SMEPLUS-26-09-02-INV-MENU-DEEP-CHALLENGE-001.md` | Copied into `BOSS_GATE/.../INVENTORY_REOPEN/` on the execution branch for evidence preservation (it was not in the repository at session start) |

Delta since the reopen package: (a) CORR-007B remediation record and rewritten files `08`/`09` (`9996072a`); (b) session link register update on canonical (`7884795`); (c) Boss's new intent: menu-by-menu process depth, Thai naming, four AI Expert Roles overlay as mandatory layer. No new Boss Gate decision on the reopen package was found on canonical or any branch.

---

## 2. Prior-Study Classification (prompt §3 taxonomy)

### 2.1 `CARRY_FORWARD_WITH_EVIDENCE` — no material delta, not re-asked

| Item | Prior evidence | Carried into |
|---|---|---|
| Inventory = Stock Truth owner; Accounting = Financial Truth owner (`INV-FP-14/15`) | Reopen `01` Part D; Boss dual-backbone ruling | 04, 15 |
| Movement lifecycle semantics: demand, reservation, on-hand, available, done; receipt, delivery, internal transfer, backorder, return, scrap mechanisms (`02` items 7–14, 18) | Reopen `05`, `06` | 11, 14 |
| Location type enumeration closed (`02` item 5) | Reopen `07` | 08, 10 |
| Lot/serial identity facts; app-layer-only uniqueness (`02` items 20–21) | Reopen `06` | 09 |
| UoM conversion facts: no per-unit rounding, up-rounding default, non-retroactive factors (`02` item 3) | Reopen `06` | 08, 09 |
| Company/tenant ORM-layer isolation with named residuals `SAAS-03`, bypass audit (`N-A13-02`) | Reopen `09`, `07` | 19 |
| Append-only done-move history (`02` item 38) | Reopen `09` | 11, 16, 19 |
| Product type two-axis gate; 989/83,753 invariant violations; Thai วัสดุสิ้นเปลือง alignment (`INV-FP-13` CARRY_FORWARD) | Reopen `12` | 09 |
| Product Category as benchmark valuation-policy owner (Layer 1) | CORR-007B `09` (rewritten) | 08, 15 |
| `N-A12-01 = HIGH FUNCTIONAL DESIGN GAP — REOPENED`; Backbone baseline `HOLD` | CORR-007B; reopen `08`, `14`, `20` | 15, 24, 25 |
| Boss `bh_*`/`bhpro_*` exclusion honoured (`INV-FP-16`) | Reopen `10` | 20 |
| Route dispatch mechanism; no procurement-group model; idempotency partially supported (`02` item 24) | Reopen `07`, `11` | 10, 12 |
| Zero migration/ETL code; no provenance field (`02` item 35) | Reopen `11`, `06` | 18 |
| Warehouse step change regenerates flow graph (`SAAS-04`) | Reopen `07` | 08, 10 |

### 2.2 `REOPEN_FOR_MENU_PROCESS_DEPTH` — studied, but not at menu / process / handoff / Thai-user depth

| Item | Why menu depth missing | Addressed in |
|---|---|---|
| Replenishment as a user process (review, edit, confirm, snooze, explain) | Only dispatch mechanism studied | 12 |
| Physical count and adjustment as a Thai control process (count sheet, approval, reason, year-end witness) | Only conflict mechanism studied (`N-A7-01`) | 13 |
| Transfers as three Thai documents; partial/backorder/return user flow | Only movement semantics studied | 11, 14 |
| Scrap reasons and Thai destruction control | Only model existence studied | 13 |
| Scheduler as explainable, auditable background function | Only AI-control boundary studied | 12 |
| Products master-data process, mandatory fields, Thai labels | Only type routing studied | 09 |
| Lots/serial as recall/expiry/warranty process | Only identity constraints studied | 09 |
| All six reports as user artifacts by audience | Never studied (only `G-7`) | 16 |
| Settings switches, operation types, routes/rules as Thai templates | Only structural facts studied | 08, 10, 11 |

### 2.3 `REWRITE_AS_CLEAN_ROOM_LEARNING`

| Item | Reason | Handling |
|---|---|---|
| Product Category valuation policy (CORR-007B `09`) | Already rewritten at `9996072a`; independent re-audit pending (`C-05`) | Only Layer 1 text used; `C-05` preserved as Boss-visible control (24, 25) |
| Account-led period close (CORR-007B `08`) | Same | Not opened; content taken from reopen `14`/`20` summaries |
| Route/rule and state-machine vocabulary | Reopen `05` §7 names it a Team B transcription risk | Expressed as Thai flow templates and business states (10, 11); vendor vocabulary excluded |
| Reopen deliverables `03`–`12` citation style (`file:line -- method`) | Acceptable A17 citation style for Layer 1 audit documents, but not for menu reference consumed later by Team B | This package cites only deliverable/item IDs, never source paths or method names (20) |

### 2.4 `CONFLICTING - REOPEN REQUIRED` (preserved, not arbitrated)

| Item | Conflict | Status here |
|---|---|---|
| `C-01` Purchase-side cancellation cascade (`MOV-31`) | Council `PARTIALLY VERIFIED` vs Special Team `CLOSED` | Carried; affects 14 §6 |
| `C-02` Idempotency/replay severity and ownership | Gate-blocking vs Team A design input | Carried; Boss decision (12, 18) |
| `C-03` Return cost basis (`FIN-DELTA-05`) | Untraced vs traced-and-confirmed | Carried; affects 14, 15 |
| `C-04` `N-CONC-01` reservation locking | Unfollowed lead vs partially verified | Carried; 19 |
| `C-05` CORR-007B files 08/09 clean-room exposure | Language drift vs verbatim code; remediated at branch surface; independent re-audit not yet performed | **Preserved as Boss-visible control**; 20, 24, 25 |
| Track-level verdict conflicts 07, 08, 09 (reconciled `HOLD`) | Threshold judgement | Carried into 21 |
| `U-07` Which "9 Veto Challenge Council" definition governs | Rival CORR-007B artifact vs ratified Charter | This session follows the ratified Charter `SMEPLUS-GOV-9VETO-001`; conflict carried (24) |

### 2.5 `HOLD / EVIDENCE REQUIRED`

| Item | Evidence missing | Owner |
|---|---|---|
| Product variants / attributes | No dedicated evidence in any round | Track 04 / S2 |
| Landed cost allocation mechanism | Source path never read | Track 06 / S6 |
| Storage categories, putaway rules, packagings, barcode nomenclatures, warehouse analysis | Never studied | Track 05, 04, 03 |
| Expiry workflow depth; consignment stock (`N-A5-02/03`) | Unread since 2026-08-31 | Track 02, 04 |
| Thai real-user validation of any Inventory practice | Never performed (structural TBRAC gap) | Track 02; Boss (membership) |
| Thai statutory items: scrap destruction, stock report format, import duty/VAT, costing norm (`TH-INV-03`), WHT correlation | Authoritative evidence required | Accounting-Tax track |
| Boss screenshot image files | Not in repository | PMO |
| Empirical invariant incidence (`N-DB-01`) | Sandbox permission | Team A |

---

## 3. Clean-Room Lineage Statement

| Layer | Used by this session? | How |
|---|---|---|
| Layer 1 — Clean-Room Learning Pack | Yes | Reopen deliverables (business findings and IDs), CORR-007B remediation record and rewritten file `09`, governance documents |
| Layer 2 — Audit Quarantine | **No** | No reference source code, dump, schema, or the pre-remediation versions of CORR-007B `08`/`09` were opened. The V2.0 module/view export CSV was opened only to confirm the inventory module family exists in the evidence set; no view/menu content was read |
| Layer 3 — SMEsPlus Original Design | Not authorized | This package is reference input for a future Layer 3, not Layer 3 itself |
| Layer 4 — Development | Not authorized | — |

`C-05` status carried unchanged: current branch surface of CORR-007B `08`/`09` remediated; historical risky text preserved in git history; independent Clean-Room Re-Audit not yet performed; Team B/C and Development not authorized; no Gate PASS.

---

## 4. Where Inventory Owns Truth vs Receives Handoff (prompt §1 question 3)

| Domain | Owns | Receives from Inventory | Gives to Inventory |
|---|---|---|---|
| Inventory | Quantities, movements, locations, lots, reservations, replenishment proposals, stock reports | — | — |
| Accounting | Valuation policy, postings, period close, GL reconciliation, tax | Valuation facts (receipt, issue, return, adjustment, scrap, landed cost, close summary) | Policy, lock dates, cost bills |
| Sales | Orders, prices, invoices | Delivered qty/lot | Demand |
| Purchase | POs, vendors, bills | Received qty | Expected receipts, replenishment conversion |
| Manufacturing | MOs, BOMs | Consumed/produced qty | Component demand, FG expectation |
| Migration | Provenance, replay | Reconciliation identities | Master data, history, opening balances (Joint certification) |

Full matrix: `04_INVENTORY_PROCESS_HANDOFF_MAP.md`.

---

## 5. Register Statement

Nothing in this register closes, passes, or authorizes. Classification counts: 14 carry-forward groups, 9 menu-depth reopen groups, 4 rewrite items, 7 conflicts preserved, 8 hold groups. All are traced into the remaining deliverables by ID.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
