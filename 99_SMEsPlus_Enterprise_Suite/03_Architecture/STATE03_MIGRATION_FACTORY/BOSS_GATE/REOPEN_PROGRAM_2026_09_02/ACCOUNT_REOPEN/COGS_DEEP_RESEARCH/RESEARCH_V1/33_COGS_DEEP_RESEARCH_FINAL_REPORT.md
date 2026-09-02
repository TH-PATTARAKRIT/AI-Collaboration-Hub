# 33 — COGS Deep Research Final Report

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Project: `SMEsPlus ENTERPRISE SUITE` | STATE: `STATE03 — Architecture`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub` | Canonical Branch: `SMEsPlus` (unchanged, not merged into)
Execution Branch: `audit/cogs-deep-research-2026-09-02-001` | Base: `origin/SMEsPlus`
Executor: Claude Sonnet 5 (coordinating session, with fourteen delegated research passes operating under this session's direct brief and reviewed before publication) | **Boss: Sole Final Approver**

---

## 1. What Was Authorized, and What Was Done

Boss directed a dedicated COGS Deep Research session — menu-by-menu, field-by-field, Periodic vs. Perpetual, with the reference ERP treated strictly as a benchmark/learning source — before any Accounting × Inventory Final Cross-Proof, because Inventory Final Solution v1.0 left twelve Joint decisions (`JT-01`–`JT-12`) explicitly open and none of them can be closed without first understanding COGS, costing, and inventory-valuation accounting semantics in depth.

That is what was done. Thirty-seven deliverables were produced in `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/COGS_DEEP_RESEARCH/RESEARCH_V1/`, covering: a reference-version behavior delta register; eight menu-by-menu field evidence sheets (Menus A–H); a twelve-case Product Category/Product precedence matrix; full Periodic and Perpetual end-to-end accounting models (two research passes each); a fourteen-dimension Periodic-vs-Perpetual comparison matrix; a four-method costing deep-research matrix; a thirty-two-scenario evidence register; dedicated purchase-side and sales-side account-flow proofs; return/reversal, adjustment/scrap/write-down, landed-cost/late-cost, and manufacturing RM/WIP/FG research; a period-close/cut-off reconciliation model; a primary-source-grounded Thai accounting/tax/statutory evidence register; a multi-company/tenant policy-isolation register; a migration/opening-cost/idempotency register; a five-identity reconciliation register; a full 9-Veto Council challenge; nine Special Team reports; a fifty-nine-item material unknown/conflict register; three candidate COGS-to-Inventory handoff contracts; a ten-question owner Teach-Back; this report; a next-action/owner matrix; a SHA-256 manifest; and this session's closure record.

---

## 2. What Was Explicitly Not Done

| Not done | Confirmation |
|---|---|
| No `PASS` declared, on this or any prior COGS/Accounting/Inventory package | Nowhere in files `00`–`36`; independently verified by targeted grep across all files |
| No Team B, Team C, Development, Production, or Release authorization | Nowhere in files `00`–`36` |
| No merge into `SMEsPlus` | The canonical branch is untouched; this session executes entirely on `audit/cogs-deep-research-2026-09-02-001` |
| No push to any branch other than this session's own execution branch | Only this session's branch was pushed |
| No git history rewrite, no force-push, no commit deletion | Only ordinary commits |
| No vendor/product name, ORM identifier, table name, or fenced code block in any Layer 1/2 output | Independent mechanical clean-room scan across all 26 research files returned zero matches (see file `28` §0, V-1, V-8) |
| No Thai statutory claim asserted without primary-source classification | Every Thai claim in file `24` is classified `AUTHORITATIVE / VERIFIED`, `INTERPRETATION — REVIEW REQUIRED`, or `NOT FOUND / HOLD` |
| No fabricated journal entry, account code, or cost figure | Verified directly by this executor (file `28` V-9); every numeric example is attributed to its source as that source's own illustration |
| No open Joint decision (`JT-01`–`JT-12`) closed | All twelve remain open; every candidate in files `12`–`27` and `31` is explicitly conditioned on them |
| No Account-module blocker (`N-04`) closed | File `24` §2.10 explicitly disclaims closing it despite a related finding |

---

## 3. Headline Findings, in Order of Materiality

1. **The reference ERP's own "Perpetual" pattern is not one stable mechanism.** Independently corroborated across at least seven of the twenty-six research files: pre-major-version-19 posts real-time at every physical stock movement; version-19+ posts at the invoice/bill level only, retiring the interim-account mechanism in favor of a Variation buffer plus explicit accrual entries. This is the single most repeated, most heavily cross-corroborated finding in the package (`CGS-U01`) and means `JT-03`/`JT-04` cannot be resolved by "match reference behavior" — there is no single reference behavior to match.

2. **Customer return cost basis (`JT-05`/`C-03`) is the package's single most material carried-forward gap.** The reference ERP's own feature-level return documentation is silent on cost basis; where the answer exists elsewhere, AVCO and FIFO disagree in mechanism, a documented credit-note-vs-inventory-reversal discrepancy exists with "manual adjustment" as the reference system's own stated remedy, and three independently-settable dates apply to a later-period return with no forced alignment.

3. **The naive Periodic COGS formula (`Opening + Purchases − Closing = COGS`) silently absorbs scrap, shrinkage, and write-down unless those are separately measured and subtracted first** — a direct, evidence-backed instance of the governing prompt's central rule that not every inventory-value decrease is COGS (file `27` §5.2).

4. **Landed cost after full sale is version-inconsistent and, in at least one reported case, generates no journal entry at all** — a control break, not merely an open design question (Scenario 11, the single most material scenario in the 32-scenario register).

5. **"Loss is not COGS" is configuration-dependent, not automatic.** The reference ERP's structural separation of scrap/loss from COGS requires deliberate configuration of a distinct Inventory Loss location and account; no documented fallback exists for an unconfigured loss.

6. **A completed Inventory-side multi-tenant invariant set would not, by itself, guarantee costing-policy isolation across companies.** Product Category's own company-scoping could not be confirmed against official documentation, sharpening (not resolving) `RISK-U03`/`GAP-FS-10`.

7. **Inventory-side movement-fact idempotency does not make Accounting-side postings safe from duplication.** A cardinality mismatch exists (one movement fact vs. one aggregate closing posting under Periodic); a separate, posting-level idempotency key is required, and `GAP-FS-08` (the migration provenance reference) does not yet exist.

8. **NRV/write-down has no reference-ERP pattern to adapt, but is a real, `AUTHORITATIVE` Thai TAS 2 requirement** (with full worked examples, directly read from the Federation of Accounting Professions' own explanatory manual) — this is original design work for SMEsPlus, not adaptation work.

9. **The Thai evidence base is materially stronger than expected for a documentation-only pass**: primary Revenue Code text (§65 bis (6)), a primary Revenue Department destruction/scrap procedure order (Por.79/2541, with its witness regime and VAT-waiver mechanics), and TFAC's own TAS 2 explanatory manual (cost composition, NRV write-down/reversal with worked examples, the literal COGS-matching recognition principle) were all directly opened and read, materially advancing four of the nine pre-existing `TH-HOLD-*` items and opening four new `TH-HOLD-COGS-*` items.

10. **No manufacturing standard-cost variance posting mechanism exists in the reference ERP**, sharply asymmetric against the well-evidenced purchase-side Price Difference Account — if SMEsPlus ever needs this, it is original design work.

---

## 4. Coverage and Compliance Statement

| Check | Result |
|---|---|
| Menus A–H covered, all five mandatory research dimensions per menu | Yes — files `03`–`10`, no blank material cells, `UNKNOWN`/`HOLD` used explicitly where evidence was absent |
| Twelve-case Product Category/Product precedence matrix built | Yes — file `11`, all twelve dimensions per case |
| Full Periodic model, all ten §8.1 research questions answered | Yes — file `12` |
| Full Perpetual model (both regimes), all nine §8.2 research questions answered | Yes — file `13` |
| Fourteen-dimension comparison matrix, no recommendation made | Yes — file `14` |
| Four costing methods researched, thirteen sub-dimensions each | Yes — file `15` |
| Minimum 32 COGS scenarios, both Periodic and Perpetual where applicable | Yes — file `16`, all 32 covered |
| Nine account-flow archetype categories (purchase, sale, returns, adjustment, scrap, landed cost, manufacturing, closing, migration) | Yes — files `17`–`23`, `26` |
| Thai Accounting/Tax/Audit track, classification discipline applied | Yes — file `24`, six `AUTHORITATIVE` findings, four `INTERPRETATION`, one explicit `NOT FOUND` |
| Five reconciliation identities derived and tested, not assumed | Yes — file `27`, one `VERIFIED` (as governing constraint only), four `CANDIDATE` |
| 9 Veto Council run | Yes — file `28`, all nine lanes, no `PASS` |
| 9 Special Team reports produced | Yes — file `29`, all nine teams |
| Material unknown/conflict register | Yes — file `30`, fifty-nine items, zero closed |
| COGS-to-Inventory candidate contracts A/B/C | Yes — file `31`, reconciled against the existing `HX-*` register, no new vocabulary invented |
| Owner Teach-Back, ten questions | Yes — file `32`, all ten answered from evidence, HOLD items named explicitly |
| Clean-room mechanical scrub over this session's output | Yes — zero vendor-name, code-token, or fenced-code-block matches, independently verified by this executor |
| Every open gap registered and surfaced | Yes — file `30`, cross-referenced into this file and file `34` |

---

## 5. Governance Position

This package researches. It does not decide, approve, or freeze any design. The executor's own challenge layer (files `28`, `29`) is disclosed plainly as single-session synthesis, not independent verification. Not declared anywhere in this package: `PASS`, `APPROVED`, `COGS FINAL SOLUTION ACCEPTED`, `READY FOR DEVELOPMENT`, `READY FOR PRODUCTION`, `TEAM B AUTHORIZED`, `TEAM C AUTHORIZED`, `CLOSED`.

---

## 6. Terminal Status

**`HOLD / EVIDENCE REQUIRED — COGS MATERIAL UNKNOWN NOT EXHAUSTED`**

This status is chosen deliberately over `COGS DEEP RESEARCH COMPLETE — READY FOR INDEPENDENT COGS RESEARCH AUDIT AND COGS FINAL SOLUTION CANDIDATE`, for three stated reasons, each traceable to a specific registered item rather than a generic caution:

1. A materially large slice of this package's most-current-version (19.0) evidence rests on search-index reconstruction because direct fetch of the primary Finance/Accounting settings page failed twice — flagged `PROVISIONAL, REQUIRES DIRECT-FETCH RE-VERIFICATION` throughout, and this has not been closed (`CGS-U04`).
2. Two items are explicitly identified as unresolvable by documentation-only research and requiring a live reference-instance verification pass before being relied upon: Case 8 of the precedence matrix (category reassignment with existing stock, `CGS-U07`) and the FIFO customer-return layer discrepancy (`CGS-U32`).
3. `JT-05`/`C-03` (return cost basis) and `JT-04` (COGS recognition timing) — the two decisions this research most directly feeds — remain genuinely undecidable from reference-ERP evidence alone, by this research's own finding, and require a Joint session with Thai-evidence input this package could only partially supply.

`HOLD` here does not mean the research failed — file `28` §4 states explicitly that this package is "sufficient as a Boss-facing research evidence record." It means the research's own conclusion is that material unknowns are not yet exhausted, and declaring otherwise would misstate what was found.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
