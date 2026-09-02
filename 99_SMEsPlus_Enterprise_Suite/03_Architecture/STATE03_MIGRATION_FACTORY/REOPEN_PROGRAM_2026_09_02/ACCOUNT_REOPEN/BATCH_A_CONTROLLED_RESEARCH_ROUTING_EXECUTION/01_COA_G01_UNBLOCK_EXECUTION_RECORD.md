# 01 — COA-G01 UNBLOCK EXECUTION RECORD

| Field | Value |
|---|---|
| Decision ID | `ACC-DEC-018` |
| Batch A Approved Direction | Proceed with `COA-G01` unblock routing |
| Batch A Control Status | `HOLD UNTIL EVIDENCE VERIFIED` |
| Boss Approval Record | branch `boss/account-batch-a-research-routing-approval-2026-09-02`, commit `fa75eb0ebfd8c3eee41b0e78c7afb39cbac7e751`, §2 row 1 |
| Source Routing Pack | `09_COA_G01_UNBLOCK_ROUTING_PACK.md`, branch `audit/account-boss-decision-legal-tax-routing-2026-09-02-001`, commit `1fbc64c20d2d2003f1ee0dbeb591bef9a4cd4ff6` |
| Gate Impact | `COA-G01` blocks `COA-G02`, `COA-G03`, `COA-G04`(/S), `COA-G05` |

`No Evidence = No Progress.` This record does not change `COA-G01` status. It executes the routing instruction only: locate what evidence already exists, assign Owner/Evidence Location/Status/Gate Impact/Next Action to each unblock item, and report — nothing here is a PMO sign-off or a Boss decision.

## Unblock item execution table

| # | Item | Owner | Evidence Location | Status | Gate Impact | Next Action |
|---|---|---|---|---|---|---|
| 1 | Reissue/restore access to `งบการเงิน 2567.pdf` or equivalent source evidence (`N-04`) | Boss (custody/re-issue) | Not located in this repository during this research pass; per `audit/account-ai-audit-smeplus-2026-09-02-001` commit `5df588d` (`COA_G01_CORR5_POST_PUBLICATION_CLOSURE.md`), `N-04` / Source Class F remains `EVIDENCE_MISSING / ACCESS_DENIED / OPEN` as of 2026-08-31 | `EVIDENCE REQUIRED` (unchanged) | `COA-G01` primary blocker | Boss to correct file ID/sharing permission or supply equivalent statutory source |
| 2 | Resolve `N-05` and `C-03` Boss decision items | Boss | Same CORR5 closure record (commit `5df588d`): both reclassified `ACCEPTED RESIDUAL UNKNOWN — BOSS DECISION REQUIRED` (a gate-disposition relabel, not a resolution) — no controlling ruling exists yet | `BOSS DECISION REQUIRED` (unchanged) | `COA-G01` blocker | Boss issues a controlling ruling on `N-05` cause and `C-03` substantive status |
| 3 | Prepare independent re-audit instruction for CORR5 | ChatGPT Audit role / independent reviewer | `audit/account-ai-audit-smeplus-2026-09-02-001` commit `356c151` publishes a 15-file AI Audit investigation package (`SMEPLUS-26-09-02-ACC-AI-AUDIT-SMEPLUS-001`) whose stated terminal state is `HOLD / EVIDENCE REQUIRED`, confirming `COA-G01` open rather than carry-forward-closed; the CORR5 closure record (commit `5df588d`) itself states "ChatGPT Independent Re-audit requested, not yet performed" | `ROUTING PARTIALLY SATISFIED — INDEPENDENT CORROBORATION EXISTS, FORMAL RE-AUDIT NOT YET PERFORMED` | `COA-G01` blocker | Boss/PMO to determine whether the existing AI Audit package (commit `356c151`) satisfies the "independent re-audit" requirement, or to commission a separate formal CORR5 re-audit |
| 4 | Prepare PMO verification checklist | PMO | Draft checklist already exists in `09_COA_G01_UNBLOCK_ROUTING_PACK.md` §"PMO verification checklist (draft)" — reproduced below, unmodified, unchecked | `ROUTING REQUIRED — CHECKLIST DRAFTED, NOT EXECUTED` | `COA-G01` blocker | PMO to execute the checklist and record sign-off or itemized non-sign-off |

## PMO verification checklist (carried forward unchecked, per source pack)

- [ ] `งบการเงิน 2567.pdf` (or equivalent) is accessible and matches the entity/period expected by `COA-G01`
- [ ] N-05 has a recorded Boss resolution (link to the resolution record)
- [ ] C-03 has a recorded Boss resolution (link to the resolution record)
- [ ] CORR5 independent re-audit has been commissioned (name of independent reviewer recorded)
- [ ] CORR5 independent re-audit output is attached and does not itself introduce new `HOLD` items without routing them
- [ ] All four items above are cross-referenced back into `COA-G01`'s own evidence file with dates and owners
- [ ] PMO sign-off (or itemized non-sign-off) is recorded and dated

## Note on parallel evidence tracks (transfer accurately, not adjudicate)

Two branches independently touch `COA-G01`:

1. `audit/account-boss-decision-legal-tax-routing-2026-09-02-001` (this record's direct predecessor) — routes the 4 unblock items without resolving any.
2. `audit/account-ai-audit-smeplus-2026-09-02-001` — an independently produced AI Audit package (commit `356c151`) and CORR5 current-state reconciliation (commit `5df588d`) that also confirm `COA-G01 = HOLD / EVIDENCE REQUIRED — BOSS DECISION PENDING`.

Both tracks agree on the terminal status (`HOLD`). This record cites the second track only as an existing evidence pointer for PMO/Boss review. It does not merge, reconcile, or pick a winner between the two tracks — that reconciliation, if needed, is itself a Boss-level decision, consistent with `ACC-DEC-016`/`ACC-DEC-017` (branch lineage) which this record does not reopen.

## Explicit non-claim

**`COA-G01` status is preserved as `HOLD / EVIDENCE REQUIRED — BOSS DECISION PENDING` by this record.** No evidence review, PMO sign-off, or Boss decision is performed or implied here. This is a research and routing execution record only, per the Batch A Operating Directive's instruction to "Understand deeply. Transfer accurately. Preserve verifiably."
