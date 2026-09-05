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

## §R17 — SIX AUTHOR ERRORS FOUND BY THE CHALLENGE PHASE

All six were found by reviewers. **None by the author.**

| # | Superseded claim | Correction | Found by |
|---|---|---|---|
| 1 | *"no asset in any located deployment carries an allocation"* — defect **latent** | **670 of 685 assets allocated; 98.57 % of the attribution annihilated.** The strand's listing command ended in a display limit over a 2,553-file directory | functional design |
| 2 | *"budget consumption shows the full cost — correct"* | **not in the target localization.** The Thai chart types accumulated depreciation as an expense type on asset-range codes; the filter splits on the first token, admits the leg, and the figure nets to zero | code & UI / localization |
| 3 | sweep denominator = 45 sites / 11 modules | **82 / 23**, and **the headline write site is outside the declared pattern** — it is a subscript assignment; the author found it by reading, not sweeping | code & UI / localization |
| 4 | five mechanisms are symmetric | **three families are; two re-derive the counterpart and fail by residue** | database design (disprover) |
| 5 | *"the source carries no statement of intent"* | **it does** — the analytic account's only statistic is labelled "Gross Margin" over the net balance. The declared design is a margin ledger | functional design |
| 6 | machine-hour rates recover depreciation, hence a masking interaction | **uncited external premise.** The rate is a bare scalar with no components and no asset link; re-based to untraceable composition | integration |

## §R18 — TWO CLAIMS THE AUTHOR WITHDREW ON REVIEW

- the ranking of the cash-basis pair as the programme's most severe finding — **withdrawn**; the cancellation is arguably *required* there, since the cost was already attributed by the original document;
- the discount rows as a *correct reducing allocation* — **the conclusion survives, the evidence does not.** The mechanism fires only when the accounts differ, and the pair cancels. `AI-E-02` must be re-derived or dropped.

## §R19 — WHAT THE AUTHOR VERIFIED RATHER THAN ACCEPTED

Two reviewer claims were load-bearing enough to re-run rather than adopt:
1. the missed dump and its asset counts — **re-extracted by the author**: 685 assets, 670 allocated;
2. the decisive measurement — **re-run by the author**: 17,716 vs 18,483 records, net −2,961,221.81, gross 206,518,404.07, **98.57 %**.
Both confirmed. A third — the Thai chart typing — was verified directly against the shipped file.

## §R20 — THE STANDING RULE THIS SESSION ADDS

**A negative result is only as good as the command that produced it, including its output limits.** Path set, pattern and unit were all declared correctly in the failed strand. The defeat was a display limit on a listing. **Any enumeration that bounds a claim shall be run without an output limit, or shall report its count separately from its listing.**

## §R21 — AND A SECOND

**Declaring a blind spot is not bounding it.** The sweep declared its false-negative mode correctly and left it unmeasured. Two reviewers opened it; one found the headline mechanism inside it. **A declared class-C residue that bounds a headline claim shall be measured, not merely named.**

## §R22 — WHAT WAS NOT REVISED

`HOLD-AS-01` and `DIS-09` remain untouched and unadjudicated. No class B, C or D was converted to A. The four base blockers are unchanged; two were added.

## CHECKPOINT

**CP-AI14(a) — REVISION LOG EXTENDED.** Seven author errors across the continuation, one degraded control, two new standing rules. **Author-originated material corrections: zero.** Auto-continue.
