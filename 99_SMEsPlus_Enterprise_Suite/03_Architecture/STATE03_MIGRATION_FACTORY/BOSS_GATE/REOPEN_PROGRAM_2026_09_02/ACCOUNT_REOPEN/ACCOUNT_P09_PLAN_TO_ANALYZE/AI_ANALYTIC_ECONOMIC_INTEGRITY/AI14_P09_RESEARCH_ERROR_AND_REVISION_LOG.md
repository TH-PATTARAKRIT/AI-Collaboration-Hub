# AI14 — P09_RESEARCH_ERROR_AND_REVISION_LOG (continuation)

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · continuation `…ANALYTIC-ECONOMIC-INTEGRITY-001`
**Extends** `14_P09_REVISION_LOG` §R1–§R9 in the base package. Numbering continues at §R10.
**Layer:** 1 — clean-room.

---

## §R10 — THE CONTINUATION ITSELF

Targeted continuation, no reset. Nothing from the base package or the P04 amendment was discarded, and no verified work was repeated. Every base finding cited in `AI01` was read from the repository at commit `9a3bded`, not from the prompt's summary.

## §R11 — AN AUTHOR ERROR, CAUGHT BY A COMMISSIONED REVIEWER

| Field | Content |
|---|---|
| **Where** | `AI04` §3, first draft |
| **The error** | It stated that the financial-report analytic column "contributes **0**" for a depreciation pair. |
| **Why it was wrong** | The shadow view keys its account column to **each record's own general account**, and each report line then filters to its own accounts. The two records therefore land in **different buckets and never meet**, so a profit-and-loss analytic column shows the **full** amount, not zero. |
| **Who caught it** | an independently tasked reviewer with a disjoint assignment. **Not the author.** |
| **What it changed** | The whole characterisation. The defect is **not** "the cost disappears from management reporting"; it is "the cost disappears from **net-balance** surfaces while account-bucketed surfaces show it correctly, so the surfaces disagree with each other". |
| **Why it made the finding worse, not better** | Because the correct figures are correct **by accident** — the budget query filters to income and expense accounts for unrelated reasons, and report columns bucket by account because that is how reports work. Neither is a control against symmetric allocation. |

**This is the second author error in this session** (the first being the base package's producer-list denominator). **The count of material corrections originating with the author remains zero.**

## §R12 — A CLAIM THAT BECAME STRONGER, NOT WEAKER

The base package's row E19 said depreciation allocates both legs. The continuation establishes that:
- it is **unconditional**, not configuration-dependent (`AI02` Corollary 1);
- it is **not unique to depreciation** — five mechanisms, three in core accounting (`AI07`);
- one of them — the cash-basis pair — is **worse than depreciation**, because both legs share one account and therefore **no surface can see past it**.

The base package's `NS-12` / `DEP-P09-12` ("whether any other event does this — not searched") is **discharged**.

## §R13 — A FINDING THAT CUTS AGAINST THE TEAM'S OWN THESIS, RECORDED ANYWAY

`AI08` §4 records that a net of zero is **correct** for a change-account transfer, because that entry carries no new economic effect. `AI07` §5 records that discount rows carry a **correct** opposite-signed allocation.

Both weaken the simple reading "opposite signs are a defect". They are recorded because the sweep discriminated rather than pattern-matched, and because a finding that admits its own limits is the only kind worth handing to Boss.

## §R14 — A NEGATIVE RESULT THAT CHANGED THE SEVERITY FRAMING

`AI05` establishes that **no asset in any located deployment carries an allocation**. The precondition for the depreciation defect is therefore **not present anywhere data was found**.

This was recorded exactly as measured. It does not weaken the algebra — a proof needs no witness — but it bounds the observed incidence to zero and forbids the session from claiming an active production defect. The honest statement is **latent and armed**.

## §R15 — A CONTROL THAT DEGRADED, AND IS RECORDED RATHER THAN GLOSSED

The four AAS-03 challenges were commissioned as required. **One evidence strand — the event-type sweep — failed mid-execution on a model rate limit and was not re-run by a subagent; the author executed that sweep directly instead.**

**This is a material weakening of the independence control**, and it lands on the single most important new result of the continuation (`AI07`). It is recorded here, in `AI15`, and in the PMO review, and the sweep is flagged as **author-executed, not independently executed**. The project's own standing lesson is that independent review is the discovery engine and that self-review finds a fraction of what external review finds; this continuation's sweep did not receive that control.

**Mitigation applied:** the sweep's denominator, pattern, path set, unit and **declared false-negative mode** are all stated in `AI07` §1 and §7, and two of the four AAS-03 challenges were explicitly tasked to attack the sweep and to close its declared blind spots. That is a partial substitute, not an equivalent.

## §R16 — WHAT WAS NOT REVISED

No base-package finding was withdrawn. No class B, C or D was converted to A. `HOLD-AS-01` and `DIS-09` were preserved untouched, and the continuation explicitly declined to settle them despite strengthening the underlying finding — because strengthening a finding does not confer authority to adjudicate between two evidence tracks.

## CHECKPOINT

**CP-AI14(a) — REVISION LOG EXTENDED.** One author error, one degraded control, both recorded. Auto-continue.
