# 17 — AI AUDIT SMEsPlus: 9 VETO CHALLENGE COUNCIL

| Field | Value |
|---|---|
| Session | `SMEPLUS-26-09-02-ACC-MENU-PROCESS-DEEP-STUDY-001` |
| Jira | `ERPPLUS-138` |
| Repository / Canonical Branch | `TH-PATTARAKRIT/AI-Collaboration-Hub` / `SMEsPlus` (base `788479552971940a126a542da5343944f7f3e0d4`) |
| Execution Branch | `audit/account-menu-process-deep-study-2026-09-02-001` |
| Mode | `READ ONLY / PROCESS BENCHMARK / CLEAN-ROOM / EVIDENCE-FIRST / L999.999` |
| Document status | `PROCESS REFERENCE ONLY` — challenge record; not a Gate PASS, not a Final Solution, not development/production authorization |
| Ai Audit structure | `Ai Audit SMEsPlus = 9 Veto Challenge Council + 9 Special Team Challenge + 4 AI Expert Roles Overlay` — three separate layers, kept in files 17 / 18 / 19 |

`No Evidence = No Progress.` `Never Skip Gate.` `Boss is the sole Final Approver.` `Open ERP / Odoo = Process Benchmark Only.` `SMEsPlus = New Thai Business Process Design Candidate, not final solution.`

## 0. Execution disclosure

The nine Council mandates below were executed as nine independent first-pass reviews of the three mandatory analytical files (02, 03, 04) and the deep-dive files (05–16) by this session, one mandate at a time, before consolidation (anti-groupthink rule, Charter §8). Each finding carries: question, delta trigger, evidence inspected, classification, gate impact, unresolved objection, required evidence before any Gate movement. No mandate is filtered for convenience (Charter §5). No majority vote applies (Charter §6): any single material veto below is enough to keep the package at `HOLD` on that point.

Classification vocabulary: `CARRY FORWARD — VERIFIED` / `CARRY FORWARD — WITH PRECISION NOTE` / `REVALIDATE — NEW MATERIAL DELTA` / `REOPENED — CONTRADICTING EVIDENCE` / `HOLD / EVIDENCE REQUIRED` / `NOT YET REACHED` / `CONFIRMED GAP`.

## VC-01 — Audit VETO / Evidence & Governance

**Question:** Do files 02/03/04 rest on verifiable evidence with consistent status propagation, and is the package's own lineage honest?
**Delta trigger:** New evidence layer (instance menu metadata A1/A2) not present in any prior Account round; governing prompt lives on an unmerged branch.
**Evidence inspected:** 00 (CP-00 record), 01 §A–§E, 02 §4, 03 Part C, 04 §4, A1 §A, A2 §B; `git` verification of base commit and prompt commit.
**Findings:** (a) Every row in 02/03/04 has non-blank evidence/owner/verifier/gate/status by construction (generated from one record set) — but 64 of 98 menu rows and 44 of 53 object rows carry `UNVERIFIED (this session reading only)`; the package is a single-session reading, not an independently verified one. (b) The prompt names `Claude Sonnet 5 Max` as executor; the runtime reports a different Claude model — recorded in 00, not hidden. (c) Three Account artefacts (this package, prior Ai Audit package, this prompt) live only on unmerged branches; a reader of `SMEsPlus` cannot find them. (d) File 02 originally stated "17 tax templates" while the template has 18 ids (found by file 10) — corrected in 02/03 by re-render before publication; recorded here as a self-found defect. (e) BR-04/BR-05 identifiers collide between Team A 06 and Team B B06 numbering (file 05 objection 1) — unresolved upstream.
**Classification:** `CARRY FORWARD — WITH PRECISION NOTE` for evidence discipline; `CONFIRMED GAP` for independent verification and canonical discoverability.
**Gate impact:** None moved. Package may be read as process reference only.
**Unresolved objection:** No independent verifier has signed any row of 02/03/04.
**Required evidence before Gate movement:** an independent (ChatGPT / PMO) re-performance of A1/A2 extraction and a sample of 02/03 rows; Boss decision on merging the three Account branches.

## VC-02 — TBRAC / Thailand Business Reality & User Fitness

**Question:** Are the Thai candidate names and the Thai process references grounded in Thai practice, or only in one benchmark instance plus a draft FDS?
**Delta trigger:** First-ever Thai naming register (file 15) and first evidence that benchmark Thai labels are mistranslated (A1 §C.5).
**Evidence inspected:** 15 §1–§8; A1 (Thai labels); l10n_th Thai account names; ACC-001 (draft); file 10 §4 calendar; file 09 §4 taxonomy skeleton.
**Findings:** (a) 151 candidate names exist; zero were validated by a Thai practitioner; owner `UNASSIGNED`. (b) Benchmark labels are demonstrably unfit (`ฐานะทางการเงิน`, `ปิด`, `การเข้าสู่ระบบที่ปลอดภัย`, `บัญชีวิเคราะห์` collision) — the package correctly refuses to copy them. (c) Two seed names were refined (Balance Sheet, WT report) without Boss instruction (file 15 objection 2). (d) Every Thai statutory statement (PP30, PND, 50 ทวิ, DBD, NPAE cash-flow requirement, legal reserve, statutory books, per-branch VAT) is `LEGAL_TAX_REVIEW_REQUIRED`; the package contains **no** authoritative Thai source. (e) The benchmark ships no Thai label at all for the Thailand-specific WHT menus — the instance itself was not Thai-user-fit.
**Classification:** `CONFIRMED GAP` (real-user and authoritative-source evidence absent); naming register usable only as TBRAC input.
**Gate impact:** Blocks any claim of Thai user fitness; COA-G05/G06 stay HOLD.
**Unresolved objection:** The package could be mistaken for an approved Thai vocabulary — every file says "candidate", but the risk remains once files circulate.
**Required evidence before Gate movement:** TBRAC validation session with Thai SME accountants/owners; legal-tax review outputs (file 22 items 3, 5).

## VC-03 — EXPERT IBPV / Business Process & Design Integrity

**Question:** Is the process map (04/05) coherent end-to-end, with single ownership at each handoff and no duplicate financial ownership across Sales, Purchase, Inventory, Expense, Asset, Tax?
**Delta trigger:** First handoff map (31 handoffs) and first menu-by-menu map (98 rows).
**Evidence inspected:** 04 §1–§3; 05 §2–§3; 08 §4; 12 §9; 13 §6; 14 §2.
**Findings:** (a) Sequence integrity holds: no statement conclusion is drawn before HO-01..HO-19 are mapped. (b) **Ownerless handoffs exist**: HO-11/HO-12 (Treasury, "not yet designed"), HO-16/HO-17 (assets/deferrals, no gate), HO-29 (analytic, nobody names it as neighbour), HO-31 (HR expense, not in Boss scope), the Inventory->Account posting-architecture fork (named "Accounting-owned" by Inventory, opened by no Account deliverable). (c) Depreciation posting is described by three registers with no run-governance owner (file 12 objection 4). (d) Consumption triggers for Thai document classes (what makes a fact "consumed" so that only additive correction is allowed) are not enumerated — every correction row depends on them (file 05 objection 5). (e) Boss Section 6 omits menus the instance shows as live (Tax Returns, Employee Expenses, WT Certificates, Cash Roundings, manufacturing) — surfaced as scope questions, not added.
**Classification:** `CARRY FORWARD — WITH PRECISION NOTE` for sequence; `CONFIRMED GAP` for ownership of five handoff families.
**Gate impact:** None moved; `GAP OWNER ROUTING REQUIRED` for Treasury, Assets/Deferrals, Analytic, HR-expense, posting-architecture fork.
**Unresolved objection:** A process reference with ownerless handoffs can be read as implicit scope approval — it is not.
**Required evidence before Gate movement:** Boss scope decisions (file 20 SC-01..SC-06); Joint Session 3 for HO-14/15/18/23.

## VC-04 — EXPERT IDTM / Data, Identity, Reconciliation & Integrity

**Question:** Does the package preserve identity, reconciliation and migration-integrity principles (no double counting, subledger tie-out, opening balances) rather than benchmark data shapes?
**Delta trigger:** First GL/TB traceability (file 07) and first explicit G1/G2/G3 tie-out statement (file 09).
**Evidence inspected:** 03 Part A; 07; 09 §2.1 RC-13, objection 10; 11 (subledger tie-out GAP); 12 §8; 14 §4 REC-*; B10 MG-C01..C16.
**Findings:** (a) GL/TB principles are carried from audited Team B work (MP-12, MG-C11, MG-C15). (b) **Subledger tie-out (AR/AP aging, WHT receivable/payable, asset register, inventory value) at cutover remains a GAP** — no research, no mechanism, and file 09 adds that the target must be G1, which no prior document stated. (c) Data-level balance of stored source entries is still `EVIDENCE_MISSING` (CF-01 data half) — MG-C10's necessity has never been demonstrated on real data (file 14 OBJN-12). (d) The Thai template's `999999 Current Year Earnings` placeholder conflicts with the derived-RE model — migration will meet it on day one (file 09 objection 3). (e) System-generated lines (tax/term/rounding) coexist with user lines — migration double-count risk remains open (AU-08 / GAP-D01-10).
**Classification:** `CARRY FORWARD — VERIFIED` for GL/TB principles; `CONFIRMED GAP` for subledger/opening-balance integrity.
**Gate impact:** MG-C11 cannot be claimed satisfiable; Joint G-5 remains highest fabrication risk.
**Unresolved objection:** The package maps where reconciliation must happen but cannot show that any reconciliation has ever been rehearsed.
**Required evidence before Gate movement:** AR/AP + asset research pass (file 22 item 6); data-level balance check on an authorized restore (GAP-D01-11); Boss decision on 999999 mapping (COA-G03/MG-C15).

## VC-05 — EXPERT IESA / ERP & SaaS System Integrity

**Question:** Do the mapped processes remain coherent as one multi-tenant, multi-company SaaS accounting core (template/instance, isolation, upgrade, reporting continuity)?
**Delta trigger:** Menus for Tax Units, Multi-Ledger, Horizontal Groups, inter-company rules and online sync appear in the instance; none had been mapped before.
**Evidence inspected:** 02 M-CFG-06/11/12, M-JRN-07, M-BNK-04; 03 OBJ-53; 14 §1 CTL-10, §6; B09 CO-09/CO-10; prior AI Audit VC-05/ST-08.
**Findings:** (a) Company boundary (CAP-05, two-entry inter-company pattern) carried forward. (b) **Standard COA template mechanics remain explicitly unapproved** (B13 DT-03) — unchanged. (c) Tax Units (group VAT filing) and per-branch VAT (สาขา) are unresolved both as statute and as tenancy design — branch may be a regulated attribute rather than a dimension (file 13 objection 2). (d) Both domains rely on ORM-layer tenant trust only, with no database backstop (Inventory file 20 §5) — the Account side is flagged "still pending" in its own source. (e) Bank online synchronization is a third-party data flow with no PDPA/security review. (f) No Financial Reporting design owner exists (file 09 RU-08) — reporting continuity across upgrades cannot be assessed.
**Classification:** `CARRY FORWARD — WITH PRECISION NOTE` (isolation); `HOLD / EVIDENCE REQUIRED` (template, branch, backstop, reporting owner).
**Gate impact:** COA-G04S / COA-G07 stay HOLD.
**Unresolved objection:** A single "one answer per (date, class, company)" period control may re-inherit the benchmark's fragmented lock shape if class-level locks are added without design (file 14 OBJN-05).
**Required evidence before Gate movement:** Boss decision DT-03; legal-tax answer on per-branch VAT; Team B period-control class model; Financial Reporting owner assignment.

## VC-06 — Financial / Accounting / Tax / Statutory VETO

**Question:** Are posting, reversal, period, AR/AP, asset, bank, VAT/WHT/CIT, retained earnings and statement semantics evidenced for Thailand without statutory overclaim?
**Delta trigger:** First reading of the LGPL Thai tax/asset templates and PP30/PND grid names; first instance fact that the benchmark ran single-rate WHT.
**Evidence inspected:** 10 (all); 09 §3–§5; 11; 12 §6; 03 OBJ-24..31; A2 §B.1; WHT branch 05 §5–§6.
**Findings (material vetoes):** (a) **VAT and CIT research remain zero**; the tax template contradicts its own Thai description for exempt input VAT and covers no non-deductible input VAT and no Undue VAT process although Boss AK names both under COA-G06 (file 10 objections 4, 6). (b) **Tax groups net purchase-side WHT liabilities against sales-side WHT assets** — literal use of template closing accounts would be an accounting error; never noticed before (file 10 objection 5). (c) The reference deployment ran without `l10n_th_withholding_tax_multi`; ACC-WHT-06 stays HIGH by construction if "what iTEST02 ran" is the baseline. (d) Sales-side WHT has no report grid and no received-certificate tracking — the CIT credit chain is unevidenced end-to-end. (e) PND1 / PND54 / PP36 exist in the chart but nowhere in scope lists. (f) Legal reserve, dividend appropriation, statutory year-end calendar, cash-flow requirement for NPAEs, statutory books — all unanchored. (g) Monthly close and retained-earnings derivation remain the best-evidenced items (carried from Rounds 2–7).
**Classification:** `CARRY FORWARD — VERIFIED` (close/RE); `CONFIRMED GAP` (VAT, CIT, sales-side WHT, tax-group netting, Undue VAT); `HOLD / EVIDENCE REQUIRED` (all statutory forms).
**Gate impact:** COA-G06 remains HOLD; **veto on any statement that this package evidences Thai tax compliance**.
**Unresolved objection:** The candidate monthly tax calendar (file 10 §4) could be copied as design constants — it contains no verified date.
**Required evidence before Gate movement:** licensed Thai tax review of file 10 §5; Boss scope ruling on VAT/CIT ownership and module baseline (ACC-WHT-06).

## VC-07 — Security / Privacy / Resilience VETO

**Question:** Are SoD, roles, audit trail, retention, destructive-action and backup/recovery controls evidenced at process level?
**Delta trigger:** First full mapping of B09 CO-01..CO-16 to menus/controls (file 14), closing prior next-action #17 as a reading only.
**Evidence inspected:** 14 §1, §5, §6, §7; 02 M-CTL-07..10; A1 (Secure Entries, Audit Trail); B09; prior VC-07.
**Findings:** (a) SoD is "supported, not mandated" (CO-02) — defensible for 2-person SMEs but a Veto seat may not accept it as a control without a recorded compensating measure (file 14 OBJN-01). (b) Backup/recovery is outside DOMAIN_01 and no platform document was located — resilience cannot be answered from Accounting evidence (OBJN-03). (c) Hard/irreversible lock after statutory filing has no Team B counterpart (OBJN-06). (d) Audit-trail retention floor (5–7 years) is relayed, not re-verified (OBJN-04). (e) Bank online sync and PromptPay/cheque modules (CLASS-D) carry privacy/security exposure with no review. (f) Benchmark group names appear in file 02 M-CTL-10 as evidence only (Class F) — acceptable, but must not migrate into design.
**Classification:** `HOLD / EVIDENCE REQUIRED` (SoD policy, backup, irreversible lock, retention source); `CARRY FORWARD` (audit-trail principle CAP-08/CO-07).
**Gate impact:** None moved; Security items routed to `GAP OWNER ROUTING REQUIRED` (platform owner UNASSIGNED).
**Unresolved objection:** Approval-before-posting (ACC-004) is assumed in the close checklist but scoped by nobody (OBJN-07).
**Required evidence before Gate movement:** platform security/resilience document; Boss scope ruling on approval workflow; authoritative retention source.

## VC-08 — Clean-Room / IP / Provenance VETO

**Question:** Did any benchmark code, ORM, schema, XML, workflow or naming leak into the candidate process reference?
**Delta trigger:** New evidence types used for the first time: dump metadata tables, OEEL manifests, label-file grep.
**Evidence inspected:** 16 (compliance self-check); A1 §A; A2; 00 CP-00/CP-02; Team A quarantine registers; scratchpad extraction method.
**Findings:** (a) No OEEL-1 / OPL-1 / CLASS-D body was opened; only labels, manifests and metadata tables were used — consistent with Q-01..Q-11. (b) Dump extraction touched three metadata tables only; no business rows; temporary copy deleted — but the docker-based extraction path was **not** in the earlier sessions' recorded authorization and is disclosed here for Boss review. (c) Benchmark model names appear in some evidence citations relayed from Team A / WHT registers (Class F) — evidence only, never as target. (d) Benchmark Thai labels are reproduced in A1 and file 15 as evidence; a residual risk that they are reused as UI labels exists and is flagged in 15 and 16. (e) The Inventory G-2 "template" wording (Accounting lock-exception model as template for Inventory) is a back-door inheritance risk at the Joint seam (file 14 OBJN-08). (f) ACC-001 draft API/entity names are STATE04 drafts, not design — cited as lineage only.
**Classification:** `CARRY FORWARD — VERIFIED` (no leakage found); `HOLD` on the docker extraction authorization question.
**Gate impact:** None. Not a `FAIL / FROZEN` condition.
**Unresolved objection:** Whether metadata-table extraction from the dump counts as "restore" under prior Boss rulings — Boss to confirm.
**Required evidence before Gate movement:** Boss acknowledgment of the extraction method (A1 §A).

## VC-09 — AI Control / Automation / Human Oversight VETO

**Question:** Does the package keep AI in a proposal role, with deterministic controls and Boss approval non-probabilistic, and is its own production reproducible?
**Delta trigger:** This package was produced by one AI session plus AI sub-agents under rate-limit interruptions.
**Evidence inspected:** 00; 16 §compliance; generator scripts in scratchpad (menu/object/handoff JSON -> 02/03/04); SHA-256 manifest (file 23).
**Findings:** (a) Every conclusion is a candidate; Boss approval language is present in every file; no in-product AI feature is proposed. (b) Files 02/03/04 are reproducible from one record set (deterministic generation); files 05–16 are authored prose by sub-agents — reproducible only by re-reading, not by regeneration. (c) Two sub-agent batches were terminated by usage limits before writing; the completed files were checked for terminal sections, but **a partial-write risk was possible** — mitigated by tail checks, recorded here. (d) No transaction, reconciliation figure or statutory value was invented; every unknown is labelled. (e) Thresholds (aging, approval) are named "policy inputs" by analogy to CO-16 — this session's reasoning, not a Team B principle (file 14 OBJN-10).
**Classification:** `CARRY FORWARD — VERIFIED` (AI authority boundary); `HOLD` note on reproducibility of prose files.
**Gate impact:** None.
**Unresolved objection:** Sub-agent authored files were not independently re-read by a second AI or human before publication.
**Required evidence before Gate movement:** independent read of files 05–16 (ChatGPT audit role) before any downstream prompt consumes them.

## Council consolidated position

| Seat | Classification | Material veto on |
|---|---|---|
| VC-01 | CARRY FORWARD — WITH PRECISION NOTE / CONFIRMED GAP | independent verification absent |
| VC-02 | CONFIRMED GAP | no Thai practitioner / authoritative source |
| VC-03 | CONFIRMED GAP | ownerless handoffs |
| VC-04 | CONFIRMED GAP | subledger / opening-balance integrity |
| VC-05 | HOLD / EVIDENCE REQUIRED | template mechanics, branch, reporting owner |
| VC-06 | CONFIRMED GAP | VAT/CIT/sales-WHT/tax-group netting |
| VC-07 | HOLD / EVIDENCE REQUIRED | SoD policy, backup, irreversible lock |
| VC-08 | CARRY FORWARD — VERIFIED (+ HOLD on extraction authorization) | none |
| VC-09 | CARRY FORWARD — VERIFIED (+ HOLD on prose reproducibility) | none |

**Council recommendation to Boss:** `READY FOR BOSS FINAL GATE REVIEW - PROCESS REFERENCE ONLY` for the package as a reference; every gate remains `HOLD / EVIDENCE REQUIRED` or `NOT YET REACHED`; Special Team deep-dives in file 18 are activated on VC-03, VC-04, VC-06 and VC-08 items.

## Addendum — Council first-pass on files 06, 07, 11, 16 (completed after the main pass)

| Seat | Finding from the late files | Classification |
|---|---|---|
| VC-01 Audit | Rule-ID drift confirmed a second time: Team B MG-C10 cites "BR-05 period validity" while Team A BR-05 is tax-country and the period rule is BR-12 (07 W-08). Files quote both; upstream correction required. | CONFIRMED GAP (documentation) |
| VC-03 IBPV | AR/AP ownership is itself undecided: B03 §3 lists Sales/AR and Purchasing/AP as undesigned neighbours while file 02 assigns M-ARP rows to Accounting Core; file 11 proposes subledger/aging/follow-up outside Core (11 UKA-02). Whether CAP-07 integrity applies to *received* vendor documents is unstated (UKA-09). | HOLD / EVIDENCE REQUIRED — BOSS SCOPE DECISION |
| VC-04 IDTM | Eight needed concepts have no account in the Thai template (prepayment, contract liability, bad-debt expense, gain/loss on disposal, stock inbound clearing, purchase variance, count difference, inter-company due-to/from) — COA-G02/G03 inputs (06 §4). Off-Balance type has no template account and no defined effect on the G1 identity. Source-side TB horizon for the MG-C11 tie-out is ambiguous (G1-like vs G2-like) because the benchmark TB is black-box (07). | CONFIRMED GAP |
| VC-06 Financial | Purchase-side regulated-document coverage (vendor tax-invoice reference for input VAT) is not a CAP-07 class; Thai VAT tax point (receipt as tax invoice for services) zero-researched; debit note Mandatory for Thailand yet absent from the instance (11 UKA-03/04). | CONFIRMED GAP |
| VC-07 Security | CLASS-D SMEsPlus-authored modules (`invoice_promptpay`, `print_voucher_request`, `full_summarize_bills`, `smesplus_special_access_rights`) embody current practice invisible to this study pending Boss CLASS-D ruling (16 RRK-06). | HOLD / EVIDENCE REQUIRED |
| VC-08 Clean-room | File 16 self-check (SCK-01..12) and negative-example list (NEG-01..10) complete; residual risks RRK-01..10 recorded; an independent Veto scan for benchmark model names in citations is still requested (RRK-03). | CARRY FORWARD — VERIFIED (+ HOLD RRK-03) |
| VC-09 AI control | Several audit events named in file 07 are candidates not in B04 §3's event list, and the Thai label for the G3 bridge line was invented by this session — Team B extension or rejection needed. | HOLD |

Council position unchanged: `READY FOR BOSS FINAL GATE REVIEW - PROCESS REFERENCE ONLY`; no gate moved.
