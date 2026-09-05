# P10 — CONTRADICTION REGISTER

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1

Every material contradiction records: the competing claims, the evidence for each, the scope of each evidence source, the contradiction's type, its disposition, and its downstream impact. **No contradiction is resolved by averaging, majority or reviewer count.**

---

## `P10-C-01` — Does a catch-up mechanism exist for deferrals?

| | |
|---|---|
| **Claim A** | No catch-up exists. Class `A`, scope: the two deferral source files, every method read. |
| **Claim B** | A catch-up does exist: the grouped path recomputes cumulatively from an unbounded earliest date every run, so a skipped or wrong period is absorbed by the next run. |
| **Source of A** | Independent challenge #3 |
| **Source of B** | Independent challenge #4 |
| **Type** | Implementation-specific — the two claims are about **different paths of the same mechanism** |
| **Disposition** | **RESOLVED.** Both are correct within their own path. Re-scoped: no catch-up on the validation path (class `A`); a structural, cumulative catch-up on the grouped path (`E-P10-046`, author-verified). |
| **Consequence** | `P10-F-08` re-scoped. The product **default** path is the fragile one; the optional path is the resilient one. This inverts the author's original reading. |
| **Downstream** | `05` §4.3a, `07` §1, `08` axis 11 |

## `P10-C-02` — Does the multi-company grouped generation post, or fail?

| | |
|---|---|
| **Claim A** | It posts: one entry in the active company built from another company's items. |
| **Claim B** | It fails: the account/company compatibility constraint refuses the entry. |
| **Evidence** | Both are consequences of one conditional. Account/company compatibility is satisfied when any company in the account's company set is a parent of the entry's company (`E-P10-055`). Shared chart → compatible → **posts silently**. Separate charts → **refused loudly**. |
| **Type** | Data-specific |
| **Disposition** | **RESOLVED AS CONDITIONAL, NOT AS A CHOICE.** Both outcomes are real; which one occurs is decided by a configuration that is not a control. |
| **Consequence** | The safer outcome is an accident. `P10-S-02` stands regardless of which branch a given tenant is on. |
| **Evidence still required** | An **executing** reproduction under both chart configurations. Recorded as `P10-U-02`. |
| **Deployed evidence added after `P10-R-08`** | Both deployed databases carrying the function have the shareable chart shape and **no scalar company column at all** — the old structural guarantee is gone. But only 1 account of 544 in one and 0 of 544 in the other are actually shared, so today the loud branch is the likely one. This bounds the realised exposure; it does not change the conditional. |

## `P10-C-03` — How many time-based recognition mechanisms exist?

| | |
|---|---|
| **Claim A** | Five. Primary author's first enumeration. |
| **Claim B** | Seven — and the pattern that produced seven demonstrably missed an eighth. |
| **Type** | Method-specific: two different selecting patterns over the same path set |
| **Disposition** | **RESOLVED AGAINST THE AUTHOR.** The population is a **floor of eight**; no exact total is supportable. Recorded as `NC-01`, class `D`. |
| **Consequence** | This is the project's recurring `PATTERN` defect recurring again. It was caught by independent review, not by the author — the fifth consecutive round in which that has been true. |
| **Downstream** | `01` §4, `05` §1 and §5, `14_P10_REVISION_LOG.md` `P10-R-01` |

## `P10-C-04` — Is the reference product's separation of depreciation and deferral evidence of semantic difference?

| | |
|---|---|
| **Claim A** | Yes — thirteen structural axes differ; they share no code. |
| **Claim B** | No — the asset object in this very root is named for **both** domains and still carries deferred-revenue commentary in its board computation (`E-P10-049`). They were one engine. |
| **Type** | Semantic |
| **Disposition** | **BOTH STAND; NEITHER INFERENCE IS PERMITTED.** The present implementations differ (A is factual). The historical unification refutes the inference that the difference is semantic rather than accidental (B is factual). |
| **Consequence** | The Boss's warning is honoured in both directions: neither "they are the same because both use schedules" nor "they are different because this product separates them" may be asserted. See `08` §1. |

## `P10-C-05` — Prepaid expense versus deferred charge

| | |
|---|---|
| **Claim A** | They are one concept; the reference product models them identically, distinguished only by which account is chosen. |
| **Claim B** | Thai practice commonly distinguishes them, and statutory presentation may require it. |
| **Type** | Statutory / presentation |
| **Disposition** | **HOLD / EVIDENCE REQUIRED.** No statutory claim is made by this session. Routed to the Accounting-Tax track (`P07`). |
| **Consequence** | A design that merges them is not yet supportable, and a design that splits them is not yet required. |

## `P10-C-06` — Accrual treatment across a tax period

| | |
|---|---|
| **Claim A** | A reversing accrual is a pure accounting device with no tax consequence. |
| **Claim B** | Where the accrual crosses a tax period, the accrual basis of taxable income and of accounting may diverge. |
| **Type** | Statutory |
| **Disposition** | **HOLD / EVIDENCE REQUIRED.** Routed to `P07`. |

## `P10-C-07` — Two reference roots at the same build string

| | |
|---|---|
| **Observation** | Two directories carry the identical build string; one holds 1,753 module manifests, the other 793. The difference is an entire archived module tree. |
| **Type** | Evidence-integrity |
| **Disposition** | **DECLARED, NOT RESOLVED.** This session declares `RR-1` as its reference root and states that every negative claim is bounded to it. Which copy is deployed is unknown. |
| **Consequence** | Any P10 negative claim re-used by another session must carry the root declaration with it. Recorded as `P10-U-05`. |

## `P10-C-08` — The report display and the report's own generation disagree

| | |
|---|---|
| **Observation** | The display path selects the allocation method by direction; the generation path passes a boolean where the direction is expected, so the comparison always fails and the **revenue** method is applied on both reports (`E-P10-050`). |
| **Type** | Implementation defect producing a semantic contradiction inside one screen |
| **Disposition** | **CONFIRMED BY THE PRIMARY AUTHOR** by direct reading of the call site, the callee signature, the failing comparison, and the correct display call. |
| **Consequence** | Where the two direction settings differ, the figure a user reads and the figure the button posts are produced by different rules. This is the single clearest instance in the package of *the same economic fact having two answers inside one mechanism*. |
| **Downstream** | `02` §5.2, `03` §2, `15`, `16` |

## `P10-C-09` — Does the shared teardown ever cancel rather than reverse?

| | |
|---|---|
| **Claim A** | Three outcomes exist: unlink, cancel, reverse. |
| **Claim B** | The cancel outcome is unreachable — reaching it requires one expression to be simultaneously false and true (`E-P10-059`). |
| **Type** | Implementation |
| **Disposition** | **RESOLVED IN FAVOUR OF B**, re-verified by the primary author by reading all three method bodies. |
| **Consequence** | With the audit trail enabled, a previously-posted recognition entry is always reversed. The intended middle ground does not exist. Any SMEsPlus design that assumes a cancel outcome would be designing against behaviour that never occurs. |

---

## Summary

| Disposition | Count |
|-------------|-------|
| Resolved on evidence | 5 (`C-01`, `C-02` as conditional, `C-03`, `C-08`, `C-09`) |
| Both claims stand; inference forbidden | 1 (`C-04`) |
| HOLD / EVIDENCE REQUIRED, routed to Accounting-Tax | 2 (`C-05`, `C-06`) |
| Declared, not resolved | 1 (`C-07`) |
| **Unresolved as a difference of opinion** | **0** |


## `P10-C-10` — The package's own evidence-base declaration contradicted the host

| | |
|---|---|
| **Claim A** | "This session had source evidence only; no database access existed." Asserted in three Layer 1 documents. |
| **Claim B** | Four deployed database archives were present on the execution host, three readable with installed tooling. |
| **Type** | Evidence-integrity — a negative claim about the research's own evidence base, made without the search that would support it |
| **Disposition** | **RESOLVED IN FAVOUR OF B.** Claim A withdrawn and replaced by `22_P10_DEPLOYED_EVIDENCE_CORRELATION.md`. |
| **Consequence** | One new finding, eight new evidence items, corrections to three exit criteria, and a material re-ordering of which defects are live versus latent. |
| **How it was found** | Not by the author's review and not by any of the four challenges — none was scoped to the evidence base. It surfaced from a **peer session's recorded lesson** that these archives exist and are readable. |
| **Lesson** | A declared absence of evidence is a negative claim and needs a declared search, exactly like any other. See `14` `P10-R-08`. |

### Summary, revised

| Disposition | Count |
|-------------|-------|
| Resolved on evidence | 6 |
| Both claims stand; inference forbidden | 1 |
| HOLD / EVIDENCE REQUIRED, routed to Accounting-Tax | 2 |
| Declared, not resolved | 1 |
| **Unresolved as a difference of opinion** | **0** |

## `P10-C-11` — P10's process taxonomy against the published peer set

| | |
|---|---|
| **Claim A** | The parent package: `P04` is the ledger owner; `P08` and `P09` are not P10 counterparties. |
| **Claim B** | The published peer branch set: `P04` is Acquire-to-Retire (assets), `P08` is Record-to-Report (the ledger), `P09` is Plan-to-Analyze (analytic). |
| **Type** | Evidence-integrity — a material population inferred rather than enumerated |
| **Disposition** | **RESOLVED IN FAVOUR OF B.** Claim A withdrawn; see `P10-R-09`. |
| **Aggravating context** | `P11-F-04` establishes the taxonomy is not written down anywhere in the canonical repository, so no correct source existed to check against. The defect is the *inference*, not the ignorance. |

## `P10-C-12` — Is the locked-period re-date a defect or a convention?

| | |
|---|---|
| **Claim A** | P10: it is a silent misstatement — an amount is reported in a period it does not belong to, with no record. |
| **Claim B** | The product's own executed test asserts it as correct behaviour, which is at least consistent with a deliberate convention: catch up in the first open period. |
| **Type** | Semantic — the same behaviour, two readings |
| **Disposition** | **BOTH READINGS CARRIED.** The behaviour is not in dispute; its status is. `28` classifies four options without choosing, precisely because this contradiction is a decision and not a fact. |
| **What settles it** | Nothing in the source. It is settled by the Boss choosing what period accuracy is worth relative to close integrity |

## `P10-C-13` — P10's own gate independence

| | |
|---|---|
| **Claim A** | P10 holds `EC-04` open because its tolerance-zero exposures are unreproduced. |
| **Claim B** | Those exposures resolve into the shared posting layer, which `P08` owns and holds at 0 of 8 with 8 tolerance-zero boundaries open. On that reading P10's `EC-04` is not P10's to close at all. |
| **Type** | Control-specific — a question about which process owns a boundary |
| **Disposition** | **RESOLVED AS B, WITH A GUARD.** `31` records `EC-04` as structurally dependent on `P08`. The guard: the constitution forbids routing a current-scope blocker to a later wave, so P10 states the boundary is `P08`'s **scope**, not a later **wave**, and holds rather than advancing |
| **Challenged** | This disposition was put to an independent challenger as a prosecution case in the fresh round — see `34` |

### Summary, revised

| Disposition | Count |
|-------------|-------|
| Resolved on evidence | 8 |
| Both claims stand; inference forbidden | 2 |
| HOLD / EVIDENCE REQUIRED, routed to Accounting-Tax | 2 |
| Declared, not resolved | 1 |
| **Unresolved as a difference of opinion** | **0** |
