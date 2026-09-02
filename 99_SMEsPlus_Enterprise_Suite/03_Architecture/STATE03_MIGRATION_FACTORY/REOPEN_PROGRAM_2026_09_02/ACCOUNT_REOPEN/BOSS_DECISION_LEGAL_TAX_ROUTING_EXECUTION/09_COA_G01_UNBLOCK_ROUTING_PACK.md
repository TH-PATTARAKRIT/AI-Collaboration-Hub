# 09 — COA-G01 UNBLOCK ROUTING PACK

| Field | Value |
|---|---|
| Decision ID | `ACC-DEC-018` |
| Source | `20_GAP_OWNER_GATE_IMPACT_REGISTER.md` EG-01; `21_BOSS_FINAL_GATE_PACKAGE.md` §6 item 7; `22_NEXT_PROMPT_RECOMMENDATION.md` §2 item 2 |
| Owner | Boss / PMO / ChatGPT Audit role |
| Status | `COA-G01 HOLD / EVIDENCE REQUIRED — BOSS DECISION PENDING` (**unchanged by this session**) |
| Gate Impact | `COA-G01` blocks `COA-G02`, `COA-G03`, `COA-G04`(/S), `COA-G05` — every configuration handoff inherits the G01 HOLD (source `20` EG-01: "inherited by every configuration handoff") |

This pack does **not** change `COA-G01` status. It only assembles the four unblock items already on record, unresolved since the prior session, into an executable routing checklist.

## Mandatory unblock items (per governing prompt §8)

| # | Item | Detail | Owner | Status |
|---|---|---|---|---|
| 1 | Reissue or restore access to `งบการเงิน 2567.pdf` or equivalent source evidence | This is the underlying statutory financial-statement PDF referenced as `N-04` in prior-session records (source `20` EG-01 cross-reference). Without it, no COA configuration can be verified against real Thai statutory statements. | Boss (has custody or can request re-issue) | `EVIDENCE REQUIRED` |
| 2 | Resolve N-05 and C-03 Boss decision items | These are prior-session open items carried forward unchanged; this package does not have visibility into their original content beyond the citation in source `20` EG-01 and must not fabricate their substance. Boss should resolve using the original prior-session record. | Boss | `BOSS DECISION REQUIRED` |
| 3 | Prepare independent re-audit instruction for CORR5 | CORR5 is a prior remediation package; source `20` recommends an **independent** re-audit (i.e., not the same session/role that produced CORR5) before `COA-G01` can rely on it. | ChatGPT Audit role (or equivalent independent reviewer) | `ROUTING REQUIRED` |
| 4 | Prepare PMO verification checklist | A structured checklist PMO can execute against items 1–3 above plus the original `COA-G01` evidence set, to produce a sign-off (or a specific, itemized non-sign-off) record. | PMO | `ROUTING REQUIRED` |

## PMO verification checklist (draft, for PMO to execute — not pre-filled)

- [ ] `งบการเงิน 2567.pdf` (or equivalent) is accessible and matches the entity/period expected by `COA-G01`
- [ ] N-05 has a recorded Boss resolution (link to the resolution record)
- [ ] C-03 has a recorded Boss resolution (link to the resolution record)
- [ ] CORR5 independent re-audit has been commissioned (name of independent reviewer recorded)
- [ ] CORR5 independent re-audit output is attached and does not itself introduce new `HOLD` items without routing them
- [ ] All four items above are cross-referenced back into `COA-G01`'s own evidence file with dates and owners
- [ ] PMO sign-off (or itemized non-sign-off) is recorded and dated

## Explicit non-claim

**`COA-G01` status is preserved as `HOLD / EVIDENCE REQUIRED` by this pack.** Nothing in this document constitutes evidence review, PMO sign-off, or a Boss decision on N-05/C-03. This is a routing checklist only, per governing-prompt §8's explicit instruction to preserve current status "until actual verification and Boss decision."
