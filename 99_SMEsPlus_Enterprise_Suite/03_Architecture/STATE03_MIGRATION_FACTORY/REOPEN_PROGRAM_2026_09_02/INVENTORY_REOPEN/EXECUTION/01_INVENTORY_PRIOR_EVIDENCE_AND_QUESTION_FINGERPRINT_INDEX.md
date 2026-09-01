# Inventory Full Reopen — Prior Evidence Chain Reconstruction & Question Fingerprint Index

Session: `SMEPLUS-26-09-02-INV-REOPEN-001`  
Jira: `ERPPLUS-139`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Execution Branch: `audit/inventory-reopen-2026-09-02-inv-reopen-001`  
Execution Worktree: `INVENTORY_REOPEN_2026_09_02_EXECUTION`  
Control Level: `/L999.999`  
Status: `CP-01 / CP-02 OUTPUT — EVIDENCE RECONSTRUCTION COMPLETE — RESEARCH ONLY, NOT A GATE DECISION`

This document does not close, pass, or authorize anything. It is the mandatory prior-evidence load required before any new question may be asked, per the 9 Veto Council Charter's Challenge Continuity Rule (`5d81d628b9b159f89a93da7ab920c42ef8f09555`, §7): *"load previous challenge ledger → load prior decisions and evidence → build delta → independently challenge the delta → suppress unchanged duplicate questions → reopen only with a documented Delta Trigger."*

All findings below are drawn from three independent read-only research passes against the live git history (not memory), cross-checked against each other where their scopes overlapped. Every claim below is cited to a commit SHA, branch, and/or file path. Where the three research passes disagreed or one deferred to another, that is noted explicitly.

---

## Checkpoint Records

### CP-00 — Branch, Worktree, Source Prompt Verification

| Field | Content |
|---|---|
| Checkpoint | `CP-00` |
| Result | `CONTINUE` |
| Evidence | Isolated worktree created at `INVENTORY_REOPEN_2026_09_02_EXECUTION`, branch `audit/inventory-reopen-2026-09-02-inv-reopen-001` created from `origin/SMEsPlus` (base commit `a85feba`), tracking `origin/SMEsPlus`. Both mandatory prompt files confirmed present on `origin/SMEsPlus`: `00_PRE_PROMPT_9VETO_CHALLENGE_AND_READINESS.md` (118 lines) and `01_NEW_SESSION_PROMPT_SMEPLUS-26-09-02-INV-REOPEN-001.md` (502 lines), both read in full. This execution prompt itself confirmed committed canonically as `02_CLAUDE_SONNET_5_MAX_EXECUTION_PROMPT_SMEPLUS-26-09-02-INV-REOPEN-001.md` (360 lines, commit `a85feba4aff1ad340dd63d40aa1f9e327e235491`, "prompt(inventory): add Claude Sonnet 5 Max execution prompt with AI Audit checkpoints"). All 5 mandatory governance commits verified as real, existing commit objects and read in full: Full Reopen Program `42e04e639f2c83aeef6d7c313152a55170a4c6ef`, 9-Veto Readiness `3cfb26faf04dddda6aea5f59e201ee1f008b94dd` (= the 00_PRE_PROMPT file itself), Governance v2.0 `03b4244b2101e8c0a89d36255cc654fc2537c748`, Council Charter `5d81d628b9b159f89a93da7ab920c42ef8f09555`, Global Challenge Ledger `f8d940900896a5a11e7232bac0e829fc5a60e908`. No collision with the separate `ACCOUNT_REOPEN`/`ACCOUNT_INVENTORY_JOINT` prompt folders or worktrees (confirmed distinct paths under `BOSS_GATE/REOPEN_PROGRAM_2026_09_02/`). Pre-existing, unrelated uncommitted changes were found on the original `AI-Collaboration-Hub` clone's checked-out branch (`audit/inventory-core-corr007b-3high-closure-010`, 2 modified files under `CORR_007B_3HIGH_CLOSURE`) — these belong to a separate, apparently still-open session and were left untouched; the new worktree is fully isolated from them. |
| AI Audit SMEsPlus Impact | Establishes the evidence floor all 9 Veto tracks, 9 Special Teams, and 4 AI Expert Overlays will build on. Audit VETO Track 01 specifically depends on this branch/commit integrity check. |
| % Board | `TBD — BASELINE REQUIRED` (no board/tracker reference available to this session) |
| % STATE | `TBD — BASELINE REQUIRED` (no formulaic STATE03 completion baseline provided) |
| % STEP | `TBD — BASELINE REQUIRED` |
| Open Risks | None blocking. |
| Next Action | CP-01. |

### CP-01 — Prior Evidence Chain Reconstruction

| Field | Content |
|---|---|
| Checkpoint | `CP-01` |
| Result | `CONTINUE` |
| Evidence | Three independent research passes, detailed in full below. All claims cite commit SHA / branch / file path. |
| AI Audit SMEsPlus Impact | Directly informs Audit VETO Track 01 (evidence chain currency — see Material Finding F-01 below), all 9 Special Team deltas (right-sizes what is genuinely still open vs. already resolved), and all 4 AI Expert Overlays (grounds review in actual current state rather than the Reopen Program's own incomplete baseline). |
| % Board | `TBD — BASELINE REQUIRED` |
| % STATE | `TBD — BASELINE REQUIRED` |
| % STEP | `TBD — BASELINE REQUIRED` |
| Open Risks | See Material Findings F-01 through F-04 below — none are blocking (none are contradictions that invalidate the reopen), but all are material and must carry into CP-03 Audit VETO Track 01. |
| Next Action | CP-02 (fingerprint index, below) → CP-03 (9 Veto Council, via Workflow, per Boss/user direction). |

---

## Part A — Material Findings (Governance & Traceability)

These are new findings surfaced by this reconstruction itself, not carried over from any prior document. They are flagged up front because they change how the rest of this reopen must be read.

### F-01 — Canonical `SMEsPlus` is stale by at least three full corrective rounds for Inventory Core Backbone

The complete Inventory Core Backbone lineage — R01 → **DR-002** → **IER-003** → CORR-004 (superseded) → **CORR-005** → IDR-006 (dead) → **IDR-007** → **CORR-006** → **CORR-007A** → **CORR-007B** — consists of nine distinct execution branches. Every one of them returns `NOT-MERGED` under `git merge-base --is-ancestor origin/<branch> origin/SMEsPlus`, verified against a freshly-fetched `origin`. Canonical `SMEsPlus` carries only prompt files and two supersession/non-execution notices for this entire chain — no execution deliverables at all. Three rounds — **CORR-006, CORR-007A, and CORR-007B (the latest and currently-controlling round)** — have **zero footprint on canonical, not even a prompt file**.

This is by design for the non-merge (every prompt in the chain explicitly forbids merging execution branches to `SMEsPlus` pending a Boss Gate decision that has not yet occurred), but it means anyone reading only canonical `SMEsPlus` — including, apparently, the Full Reopen Program itself — cannot see the true current state.

### F-02 — The Full Reopen Program's own written baseline (§4.2) does not cite CORR-006, CORR-007A, or CORR-007B

`STATE03_BOSS_ACCOUNT_INVENTORY_FULL_REOPEN_PROGRAM_2026_09_02.md` (commit `42e04e639f2c83aeef6d7c313152a55170a4c6ef`, 2026-09-02 01:25:29 +0700) states its Inventory baseline as "DR-002, corrective evidence through CORR-005, independent review lineage, fresh IDR-007 readiness/prompt... no IDR-007 execution-result commit had been verified on canonical `SMEsPlus`." It does not mention CORR-006 or CORR-007A, both of which chronologically preceded this program's authorship (CORR-006 tip `46a84837`, 2026-09-01 23:15:42; CORR-007A tip `deceb733`, 2026-09-01 23:44:55 — both before 01:25:29 the next... same-day but earlier). CORR-007B's final commit (`0eb78c68`, 2026-09-02 01:29:26) landed roughly four minutes *after* this program's authorization commit, i.e. was being finished concurrently.

This is best read as a **documentation/traceability gap, not a decision-making failure**: the evidence available (from Agent research covering CORR-006 and CORR-007B) shows Boss personally drove both escalations — Boss explicitly rejected IDR-007's "zero elevation-worthy" finding and ordered the CORR-006 re-proof of 8 Medium items by name, and Boss personally challenged the CORR-007B disposition of `N-A12-01` across five rounds before its final "HIGH FUNCTIONAL DESIGN GAP — REOPENED" label was set. So Boss (the person) was almost certainly aware of this work as it happened; what is missing is a canonical written record that cross-references it. Separately, both of the two most-recent canonical governance rulings (see F-03) **do** generically acknowledge that IDR-007 (and, for the separate GROUP_A SIP track, RV-011) results exist on branches but are "not yet verified on canonical" — so the general non-canonical-branch pattern is institutionally known; the specific CORR-006/007A/007B rounds are simply not yet cross-referenced anywhere in the written record. **This is itself the exact class of finding Audit VETO Track 01 exists to surface**, and it is carried into that track below rather than resolved here.

### F-03 — Two canonical governance rulings, both dated today, are more current than the Reopen Program's own baseline section

- `BOSS_GATE/STATE03_BOSS_GROUP_A_SALES_PURCHASE_AND_INVENTORY_PARALLEL_CLOSURE_WITH_ACCOUNT_HOLD_DIRECTIVE_2026_09_02.md` (commit `47018139405868c1ce2acdf618e398eb8d25efe6`, 2026-09-02 00:11:00) — restructures "GROUP A" going forward to Sales+Purchase only; Inventory becomes its own independent "Stock Truth Backbone," paired with Accounting/COA as a dual-backbone program (not merged into one domain). States explicitly: *"no RV-011 execution-result commit has been verified on canonical `SMEsPlus`"* and *"no IDR-007 execution-result commit has been verified on canonical `SMEsPlus`."* Hard-holds Accounting×Inventory Cross-Proof, final GROUP A design freeze, Team C handoff, and Development until `COA-G08` closes.
- `STATE03_BOSS_ACCOUNT_INVENTORY_FULL_REOPEN_PROGRAM_2026_09_02.md` (commit `42e04e63`, 01:25:29) — the Full Reopen Program itself, issued ~75 minutes later, ordering the three new reopen tracks (`ERPPLUS-138/139/140`) under 9-Veto-Council governance.

Both are read in full and are internally consistent with each other and with this reconstruction.

### F-04 — The canonical `GROUP_A_EVIDENCE_CHAIN_INDEX.md` is stale by two rounds

`BOSS_GATE/GROUP_A_SALES_INVENTORY_PURCHASE/GROUP_A_EVIDENCE_CHAIN_INDEX.md` (canonical, commit `b8ced41a`, 2026-08-31 14:19:50) is the project's own designated traceability map for the GROUP_A Sales-Inventory-Purchase lineage. It stops at "RV-009 pending" and predates CORR-010 and RV-011 entirely (both landed 1–2 hours later). No canonical commit since has updated it. This is a GROUP_A SIP (not Inventory Core Backbone) finding, included here because the two lineages share origin evidence and the same staleness pattern; it is out of this session's direct authority to fix (GROUP_A SIP is no longer active-Inventory scope per F-03) but is noted for the Audit VETO track and for `20_INVENTORY_PENDING_JOINT_SESSION_3_INTERFACE_REGISTER.md`.

---

## Part B — Prior Evidence Chain: Inventory Core Backbone (primary lineage)

All branches below are `origin/*` remote-tracking refs unless noted; all are `NOT-MERGED` into `origin/SMEsPlus`.

| Round | Branch | Tip commit | Timestamp (+07:00) | On canonical? | Terminal status (document's own words) |
|---|---|---|---|---|---|
| R01 | — (no execution ever occurred) | — | — | Prompt + supersession notice only | Superseded by DR-002 before execution |
| DR-002 | `claude/inventory-core-backbone-dr002` | `b31597fa` | 2026-08-31 16:39:36 | Prompt only | `HOLD / EVIDENCE REQUIRED — MATERIAL UNKNOWN EXHAUSTION NOT ACHIEVED` |
| IER-003 | `audit/inventory-core-dr002-independent-review-003` | `45c749ea` | 2026-09-01 01:42:17 | Prompt only | `INDEPENDENT INVENTORY EVIDENCE REVIEW COMPLETE — READY FOR BOSS INVENTORY EVIDENCE GATE DECISION` |
| CORR-004 | `claude/inventory-core-backbone-h2-h3-corr004` | frozen at `b31597fa` (never advanced) | prompt 2026-09-01 | Prompt + supersession notice only | `SUPERSEDED BEFORE EXECUTION` (Boss bh_/bhpro_ exclusion + branch-baseline ruling invalidated its premise) |
| CORR-005 | `claude/inventory-core-backbone-register-recon-corr005` | `d69da790` | 2026-09-01 08:16:37 | Prompt only | `READY FOR INDEPENDENT DELTA RE-REVIEW — INVENTORY EVIDENCE GATE NOT YET APPROVED` |
| IDR-006 | `audit/inventory-core-corr005-delta-rereview-006` | frozen at `d69da790` (never advanced) | prompt 2026-09-01 12:07:59; non-exec record 18:29:03 | Prompt + non-execution record only | `PROMPT EXISTS — EXECUTION NOT PUBLISHED — TREAT AS NOT EXECUTED` |
| IDR-007 | `audit/inventory-core-corr005-delta-rereview-007` | `ed26918a4b15e9a2de3f2e865aa97e1dad138e2a` | 2026-09-01 18:55:53 | Prompt only | `INDEPENDENT DELTA RE-REVIEW COMPLETE — READY FOR BOSS INVENTORY EVIDENCE GATE DECISION` (never acted on — see F-01/F-02) |
| CORR-006 | `audit/inventory-core-corr006-boss-high-reproof-008` | `46a848375b4878f6d4b3e82cfeab4e2e6d6cb552` | 2026-09-01 23:15:42 | **Not present at all** | `CORR-006 BOSS HIGH RE-PROOF COMPLETE — READY FOR BOSS RE-CONSIDERATION` |
| CORR-007A | `audit/inventory-core-corr007a-grpa-m18-wht-50twi-009` | `deceb7339b39eba309236782f159f8393224f5fd` | 2026-09-01 23:44:55 | **Not present at all** | `CORR-007A COMPLETE — READY FOR BOSS GRPA-M18 DECISION` |
| **CORR-007B (latest)** | `audit/inventory-core-corr007b-3high-closure-010` | `0eb78c68ae1d6c340dce163fb6aa609920d98226` | 2026-09-02 01:29:26 | **Not present at all** | **`OPEN FOR BOSS CHALLENGE`** — not closed |

### DR-002 (Account-Grade Inventory Deep Research)

Full Odoo-source-grounded research across 22 mandatory domains. Central technical findings: no `stock.valuation.layer` model exists (valuation lives on `stock.move`); no `uom.category`/`product.packaging` models; no `procurement.group` model (uses `stock.reference` instead); product classification is a two-field `type`/`is_storable` gate; over/under-fulfillment and negative-quantity prevention are enforced entirely at the application layer with zero DB CHECK constraints. Opened 5 High findings: **GRPA-H4** (fiscal position unlocated), **GRPA-H5/H2** (orphaned `bh_parent_company` partner-brand/HQ columns), **GRPA-H8/H3** (two uncoordinated Thai "branch" concepts), **N-A7-03/N-A9-02/H4** (cutoff/timing evidence missing), **N-A13-02/H5** (company ACL/tenant-isolation enforcement unverified). 21/21 mandatory deliverables produced.

### IER-003 (independent review of DR-002)

Independently re-derived 10 representative claims (all corroborated) and issued independent verdicts on all 5 High items: H4→`VERIFIED CLOSED`; H5/H2→`PARTIALLY VERIFIED — TARGETED CORRECTION REQUIRED` (external dependency: vendor source acquisition); H8/H3→`CONFLICTING EVIDENCE` + `REQUIRES REAL USER VALIDATION` (external dependency: real Thai-user validation); N-A7-03/N-A9-02→`VERIFIED CLOSED`; N-A13-02→`VERIFIED WITH CONDITIONS`.

### CORR-004 (superseded before execution)

Authored to close H2/H3 via further source study; superseded when Boss issued two binding scope rulings before any session ran: (1) `bh_*`/`bhpro_*` source families excluded entirely from SMEsPlus learning (ruling file: `BOSS_GATE/INVENTORY_CORE_BACKBONE/BOSS_INVENTORY_SCOPE_RULING_BH_EXCLUSION_AND_BRANCH_BASELINE_2026_09_01.md`, commit `997809d`); (2) the approved SaaS Multi-Company/Multi-Branch architecture is an existing baseline not to be reopened by Inventory research absent material contradiction.

### CORR-005 (DR-002 register reconciliation)

Reconciled all 5 original High items against IER-003 and the Boss scope rulings: H4→`VERIFIED CLOSED`; H5/H2→`CLOSED BY BOSS SCOPE EXCLUSION` (controlled migration carry-forward only); H8/H3→`CLOSED AS AN INVENTORY ARCHITECTURE QUESTION` (controlled Migration/TBRAC + Accounting/Tax carry-forward); N-A7-03/N-A9-02→`VERIFIED CLOSED`; N-A13-02→`VERIFIED WITH CONDITIONS`. Recomputed residual: 21 open (0 Critical / 0 High / 14 Medium / 7 Low).

### IDR-006 (dead round)

Prompt published to canonical; branch never advanced past CORR-005's own tip; formally recorded as not executed and superseded by a fresh reissue (IDR-007).

### IDR-007 (independent delta re-review of CORR-005) — verified genuine, complete, unacted-on

Independently recomputed SHA-256 for all 27 manifest-covered files from raw git blob content (27/27 match); re-opened primary source directly for 4 of 5 former High items; individually challenged all 21 open Medium/Low items for elevation risk and found **zero** warranting elevation (one item, `N-CONC-01`, found to be *more conservative* than the evidence supported). All 12 mandated deliverables present and substantively read; not boilerplate. Confirmed genuinely connected to the same GitHub remote and genuinely IDR-007-specific content (not a mislabeled folder) via commit-hash identity between the local `IDR_007_EXECUTION` worktree and `origin/audit/inventory-core-corr005-delta-rereview-007`. Terminal verdict recorded inside the result itself: `INDEPENDENT DELTA RE-REVIEW COMPLETE — READY FOR BOSS INVENTORY EVIDENCE GATE DECISION` — explicitly not a Gate PASS. **This Gate decision was never made; the Reopen Program was issued instead** (see F-01/F-02).

### CORR-006 (Boss High escalation re-proof)

Boss explicitly rejected IDR-007's "zero elevation-worthy" finding and directed 8 named Medium items be treated as High and re-proven: `GRPA-M18`, `GRPA-M12`, `GRPA-M11`, `GRPA-M15`, `GRPA-M16`, `N-A7-01`, `N-A7-02`, `N-A12-01`. Results: `GRPA-M11`→RESOLVED; `GRPA-M12`→RESOLVED; `N-A7-02`→RESOLVED; `GRPA-M16`→RESOLVED AS READ-GAP (dropship carried to design); `GRPA-M15`→HIGH REMAINS; `GRPA-M18`→HIGH REMAINS; `N-A7-01`→HIGH REMAINS; `N-A12-01`→HIGH REMAINS. Post-reproof: 4 items High.

### CORR-007A (GRPA-M18 Thai WHT/50-twi closure)

Split `GRPA-M18` into 5 sub-items. A (module existence)→RESOLVED. B (field mapping)→PARTIAL, high-confidence, 3 named gaps. C (render/print path)→RESOLVED AS STATIC CHAIN PROOF. D (PND3/PND53 monthly filing)→formally separated as **Accounting/Tax-owned**, never an Inventory concern despite the shared label. E (legal sign-off)→`LEGAL_TAX_REVIEW_REQUIRED`. Recommendation: remove `GRPA-M18` from the Inventory Evidence Gate High-blocker list entirely; track D under Accounting/Tax and E as legal review.

### CORR-007B (3-High closure — latest round, currently controlling)

- **`GRPA-M15`** (PO-line source/dump drift) → **RESOLVED**. 9th column (`purchase_request_id`) classified legacy-orphan, carried forward for a pre-cutover data-content check only.
- **`N-A7-01`** (count-freeze/conflict) → **RESOLVED AS SOURCE BEHAVIOR; DESIGN POLICY REQUIRED**. Odoo reference behavior is soft conflict-detection only, no hard freeze; the freeze-policy choice is now explicitly a Team B design decision (4 named options), not an evidence gap.
- **`N-A12-01`** (fiscal-year/cross-year continuity) → Boss rejected an earlier "carry-forward" disposition as insufficient for Functional Design and reopened it across five rounds of challenge. Final standing disposition: **`N-A12-01 = HIGH FUNCTIONAL DESIGN GAP — REOPENED`**, full title *"Account-led monthly close, year-end close, stock cut-off, product category valuation policy, periodic/perpetual posting behavior, carry-forward balance, GL reconciliation, and retained earnings functional design gap — HIGH until proven."* Genuine mechanism proof exists (Periodic/Perpetual posting gate, closing cron/aggregation mechanism, Product Category as true policy owner) plus one negative finding of note: **no source-evidenced year-end P&L-to-Retained-Earnings closing entry anywhere in the reference system**. None of this evidence depth counts as closing the item per Boss's explicit ruling.
- `GRPA-M18` (WHT) reconfirmed untouched/correctly out-of-scope by this package's own independent Team I4 audit.

**Open items (8 total, explicitly tracked):** (1) `purchase_request_id` data-content check [Team A/Migration]; (2) count-freeze design-policy selection [Team B, not yet authorized]; (3) G-1 lock-date/closing sequencing unproven; (4) G-2 asymmetric post-close correction governance; (5) G-3 backdate enforcement at picking- not move-level; (6) G-5 migration-cutover opening-balance cross-proof [needs Accounting]; (7) G-6 no year-end retained-earnings entry — new design decision needed; (8) G-7 `stock_valuation_report.py` PDF/XLSX export methods are empty stubs (a source-verified code defect, noted as a fact about the reference system, not a target-design instruction). **Terminal: `CORR-007B = OPEN FOR BOSS CHALLENGE`. `Account + Inventory Backbone Reference Baseline = HOLD`. Not closed. No Gate PASS declared anywhere in this package. Team B and Team C remain unauthorized.**

---

## Part C — Related/Dependency Context: GROUP_A Sales-Inventory-Purchase Lineage

This lineage is the shared origin of Inventory's earliest evidence (DR-002/CORR-003 for GROUP_A predates and partly overlaps the Inventory-Core-Backbone-specific DR-002 above) but, per F-03, **"GROUP A" is redefined as of today to Sales+Purchase only** — Inventory now has its own independent Stock Truth Backbone track. This section is retained as dependency context and for the Session-3 interface register, not as live Inventory scope.

Chain (all `NOT-MERGED` to canonical): DR-002/CORR-003 (`8b0993d8`) → IER-004 (`626873c3`, `PASS/VERIFIED`) → **Boss Evidence Gate Approval** (canonical, `bd9b87f9`, PASS) → Team B Design CD-005 (`b98a3b9f`) → FV-006 (`535724c0`, rework required) → CORR-007 (dead, superseded by CORR-008) → CORR-008 (`359f96c0`, 9 findings closed) → RV-009 (`b2f7cbd3`, rework required — surfaced a mistracked-item control issue) → CORR-010 (`e4418644`, non-Accounting closure) → **RV-011** (`77e93d44`, latest: `NON-ACCOUNTING CLOSURE VERIFIED — PRE-DEVELOPMENT GATE STILL HOLD FOR ACCOUNTING/CONTROLLED DEPENDENCIES`).

Two items remain open and unwaived at the head of this chain: **A1** (Sales-side cancellation-gate symmetry vs. Purchase — an Accounting/AR-AP-dependent design question) and **A2** (legacy approval-module internal-workflow evidence, source unobtainable from this machine). Both are Accounting-dependent or out-of-reach, not Inventory-owned. RV-011's result, like IDR-007's, is genuine and complete but **not yet canonically verified** per Boss's own 2026-09-02 ruling (F-03).

---

## Part D — Question Fingerprint Index (CP-02)

Per the Council Charter's 6-way taxonomy. "Reopen Track" indicates which of the 9 Veto/Special Team mandates owns any further work.

| Fingerprint | Question / Finding | Classification | Evidence | Reopen Track |
|---|---|---|---|---|
| `INV-FP-01` | Fiscal position handling (GRPA-H4) | `CLOSED_WITH_EVIDENCE` | IER-003 + CORR-005, `VERIFIED CLOSED` | — |
| `INV-FP-02` | Partner brand/HQ orphan columns, `bh_parent_company` (GRPA-H5/H2) | `CLOSED_WITH_EVIDENCE` (by Boss scope exclusion, not technical proof) | Boss ruling `997809d`; CORR-005 `CLOSED BY BOSS SCOPE EXCLUSION` | Track 08 (Clean-Room) should confirm the exclusion is still being honored; Track 01 (Audit) notes this is governance closure, not technical closure |
| `INV-FP-03` | Thai branch dual-concept conflict (GRPA-H8/H3) | `CLOSED_WITH_EVIDENCE` (architecture ruling) with `CARRY_FORWARD — VERIFIED WITH PRECISION NOTE` residue | Boss architecture ruling; CORR-005 `CLOSED AS AN INVENTORY ARCHITECTURE QUESTION`; IER-003 flagged `REQUIRES REAL USER VALIDATION` | Track 02 (TBRAC) — real-user validation remains an open external dependency, worth restating not re-researching |
| `INV-FP-04` | Cutoff/timing evidence (N-A7-03/N-A9-02) | `CLOSED_WITH_EVIDENCE` | IER-003 + CORR-005, `VERIFIED CLOSED` | — |
| `INV-FP-05` | Company ACL / tenant isolation enforcement (N-A13-02) | `CARRY_FORWARD — VERIFIED WITH PRECISION NOTE` | IER-003/CORR-005 `VERIFIED WITH CONDITIONS` — conditions not itemized in the summary layer read so far | Track 07 (Security) should re-confirm the specific conditions from CORR-005's own text before treating this as fully closed |
| `INV-FP-06` | GRPA-M18 Thai WHT/50-twi | `CLOSED_WITH_EVIDENCE` for the Inventory-owned parts (A/B/C); `OUT_OF_INVENTORY_SCOPE` for D (Accounting/Tax) and E (Legal) | CORR-007A, `COMPLETE — READY FOR BOSS GRPA-M18 DECISION` | Track 06 (Financial/Tax) owns D; Legal owns E — neither is Inventory's to close |
| `INV-FP-07` | GRPA-M15 PO-line source/dump drift | `CLOSED_WITH_EVIDENCE`, with one `CARRY_FORWARD` sub-item | CORR-007B, RESOLVED | Team A/Migration owns the pre-cutover data-content check |
| `INV-FP-08` | Count-freeze / conflict handling (N-A7-01) | `CLOSED_WITH_EVIDENCE` as a research question; the freeze-policy itself is `NOT YET REACHED` (Team B design, not authorized in this session) | CORR-007B, `RESOLVED AS SOURCE BEHAVIOR; DESIGN POLICY REQUIRED` | Track 03 (IBPV) should record the 4 named policy options as input for the eventual Team B decision; this reopen may not select one |
| `INV-FP-09` | **Account-led monthly/year-end close, stock cut-off, product category valuation policy, periodic/perpetual posting, GL reconciliation, retained earnings (N-A12-01)** | **`REOPEN_ELIGIBLE — DELTA TRIGGER EXISTS`** (Delta Trigger: `INV-DELTA-05`/`06` — dedicated Accounting×Inventory joint research now exists and Accounting is progressing through COA-G03; also the item's own standing disposition is literally `HIGH FUNCTIONAL DESIGN GAP — REOPENED` as of CORR-007B, the most recent evidence) | CORR-007B, `OPEN FOR BOSS CHALLENGE` | **Primary live item for Track 06 (Financial/Accounting interface) and Track 03 (IBPV)**; boundary-classify per Section 7 of the execution prompt — do not close independently |
| `INV-FP-10` | `stock_valuation_report.py` PDF/XLSX export stubs (G-7, under N-A12-01) | `UNKNOWN — STILL MATERIAL` as a source fact; not yet evidence-tested as a target requirement | CORR-007B G-7 | Track 04 (IDTM) / Track 05 (IESA) |
| `INV-FP-11` | Does a verified IDR-007 result exist, and what is its exact current status? | `CLOSED_WITH_EVIDENCE` (yes, it exists and is genuine) as a factual question; `UNKNOWN — STILL MATERIAL` as a governance question (the Gate decision on it was never made) | This document, Part B, IDR-007 | **Track 01 (Audit VETO) — primary evidence-chain-currency question for this reopen** |
| `INV-FP-12` | Is canonical `SMEsPlus` a reliable single source of current Inventory status? | `CONFLICTING — REOPEN REQUIRED` — demonstrably no, per F-01 | This document, Part A | **Track 01 (Audit VETO)** |
| `INV-FP-13` | Stockable / Consumable / Service routing as a target-design hypothesis | `UNKNOWN — STILL MATERIAL` | DR-002 documented the *source's* two-field `type`/`is_storable` gate as a fact; no evidence pass yet directly tests Boss's 3-way target routing hypothesis against Thai business reality or edge cases | **New research required — Track 03 (IBPV), Track 02 (TBRAC), and deliverable `12_STOCKABLE_CONSUMABLE_SERVICE_DEEP_PROOF.md`** |
| `INV-FP-14` | Is Inventory the Stock Truth domain for inventory-managed items? | `CARRY_FORWARD — NO MATERIAL DELTA` (per `00_PRE_PROMPT_9VETO_CHALLENGE_AND_READINESS.md` §2, reaffirmed by F-03's dual-backbone ruling) | Boss governance direction | — |
| `INV-FP-15` | Is Accounting the Financial Truth owner? | `CARRY_FORWARD — NO MATERIAL DELTA` (interface *details* still open — see `INV-FP-09`) | Same as above | — |
| `INV-FP-16` | Boss `bh_*`/`bhpro_*` source-scope exclusion — still binding? | `CLOSED_WITH_EVIDENCE` | `BOSS_INVENTORY_SCOPE_RULING_BH_EXCLUSION_AND_BRANCH_BASELINE_2026_09_01.md`, commit `997809d`; no contradicting later ruling found | Track 08 (Clean-Room) confirms ongoing compliance only |
| `INV-FP-17` | GROUP_A SIP evidence chain index currency | `SUPERSEDED — HISTORICAL ONLY` for Inventory purposes (GROUP_A no longer includes Inventory per F-03); flagged `CONFLICTING` for the GROUP_A/Sales+Purchase track itself, out of this session's authority | F-04 | Not this session's to fix; note in deliverable `20` |

No question above is being re-asked from a blank state; every classification is grounded in the evidence located during CP-01. `INV-FP-09` (N-A12-01) and `INV-FP-13` (Stockable/Consumable/Service routing) are the two items this reopen must treat as genuinely open going into CP-03. `INV-FP-11` and `INV-FP-12` are new governance findings this reopen itself surfaced, not carried from any prior document, and both route to Audit VETO Track 01 first.

---

## Part E — Administrative / Boundary Notes

- **Boss `bh_*`/`bhpro_*` exclusion ruling**, in full: `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/INVENTORY_CORE_BACKBONE/BOSS_INVENTORY_SCOPE_RULING_BH_EXCLUSION_AND_BRANCH_BASELINE_2026_09_01.md` (commit `997809d`). Six other files reference/apply it consistently; no contradiction found.
- **Current Account-domain state** (context only, not this session's to close): `COA-G01`/`G02` = `CLOSED`; `COA-G03` = Team B semantic-consolidation evidence published (`82b5569`, 2026-09-01), self-reports `READY FOR FRESH INDEPENDENT AUDIT`, no Boss Gate/PASS recorded; `COA-G04..G08` = `NOT CLOSED`. Per F-03, the whole Account+Inventory backbone baseline is formally `HOLD` pending the three new reopen tracks.
- **`IDR_007_EXECUTION` worktree** (`/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/IDR_007_EXECUTION`) — verified genuinely connected to `TH-PATTARAKRIT/AI-Collaboration-Hub` and genuinely holding IDR-007 content (commit-hash-identical to `origin/audit/inventory-core-corr005-delta-rereview-007`), not a mislabeled folder.
- **`ACCOUNT` directory** (`/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT`) — confirmed not a git repository root at its top level; belongs to the separate, parallel Account Reopen work area; not read beyond a top-level listing, not modified, per the parallel-session safety rules in Section 4/11.4 of the execution prompt.
- **`00_REOPEN_ACCOUNT_INVENTORY_SESSION_PACKAGE_INDEX.md`** (canonical, commit `1c233f0`) names three prompt files (`01_ACCOUNT_FULL_REOPEN_DEEP_RESEARCH_PROMPT.md` etc.) that were never actually created under those names anywhere in git history — superseded in practice by the `REOPEN_PROGRAM_2026_09_02/{ACCOUNT_REOPEN,INVENTORY_REOPEN,ACCOUNT_INVENTORY_JOINT}/` package this session is actually executing against. Minor stale index reference, not a governance conflict; noted for completeness.

---

## Sources

Three independent research passes (full reports preserved in this session's transcript; available on request): (1) Inventory DR-002 → corrective chain reconstruction; (2) Independent review lineage + GROUP_A SIP evidence; (3) IDR-007 result hunt + Boss exclusions + backbone roadmap. Plus direct reads by the session executor of: the Council Charter (`5d81d628b9b159f89a93da7ab920c42ef8f09555`), Global Challenge Ledger (`f8d940900896a5a11e7232bac0e829fc5a60e908`), and Full Reopen Program (`42e04e639f2c83aeef6d7c313152a55170a4c6ef`).
