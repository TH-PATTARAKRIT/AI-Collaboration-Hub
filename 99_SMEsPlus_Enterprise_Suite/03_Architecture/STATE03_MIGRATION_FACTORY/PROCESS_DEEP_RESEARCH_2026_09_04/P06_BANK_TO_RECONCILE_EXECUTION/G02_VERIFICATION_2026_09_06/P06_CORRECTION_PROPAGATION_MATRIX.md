# P06_CORRECTION_PROPAGATION_MATRIX.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-CORRECTION-INTEGRITY-VERIFICATION-004]` · prompt commit `774aa0b`
**Session:** P06 — INDEPENDENT CORRECTION-INTEGRITY VERIFICATION (CP-P06V02)
**Classification:** LAYER 2 — AUDIT QUARANTINE

> **This matrix answers prompt §4.3 and §4.4:** for every corrected claim, is the corrected wording consistent across **all** P06 deliverables that repeat it, and does any stale version remain marked current — especially in a downstream handoff?
>
> **The method that matters is the denominator.** A correction population must be enumerated by **the claim class**, never by the phrase the author happens to remember. Round 5 enumerated by phrase. So did this verifier's first sweep. **Both under-counted, and the second only found the first's misses after deliberately re-scoping.**

---

## 1. The nine corrected claim classes, with their true populations

**UNIT: a current statement of the claim.** A *record* of a past statement — a revision log entry, a challenge quotation, a before/after table — is **not** a current statement and is correctly left untouched. That distinction is the whole matrix.

| Claim class | Search pattern executed | Total hits | Records (leave) | **Current statements** | Corrected R5 | **Missed by R5** | Now |
|---|---|---|---|---|---|---|---|
| `X-08` answered ⇒ closed | `closed by P06\|answered and closable\|may close .X-08\|may be closed` | 16 | 7 | **9** | **9** | **0** | **COMPLETE** |
| P08 / P01 unpublished | `not published\|NOT PUBLISHED\|unpublished` | 30 | 8 (incl. 3 time-bounded) | **19** | 8 | **11** | **COMPLETE** |
| *"filtered distribution/build/tree"* | `filtered distribution\|filtered build\|filtered tree\|same filter` | 24 | 13 | **11** | 4 | **7** | **COMPLETE** |
| `is_matched` *"2 of 3 branches"* | `2 of 3 branches\|two of its three\|three branches` | 6 | 2 | **4** | **4** | **0**, but **1 defective** (`C-01`) | **COMPLETE** |
| *"an eighth settlement door"* | `eighth settlement door\|eighth door` | 15 | 11 | **4** | 1 | **3** | **COMPLETE** |
| *"broad default ACL"* | `broad default ACL\|broad ACL` | 5 | 4 | **1** | **1** | **0** | **COMPLETE** |
| *"numbers become re-issuable"* | `re-issuable\|reissuable` | 2 | 1 | **1** | **1** | **0** | **COMPLETE** |
| generation gap / *"only deployment evidence is Odoo 19"* | `only deployment evidence` | 5 | 3 | **2** | **2** | **0** | **COMPLETE** |
| G02 blocker population count | `population at G02 close` | 2 | 0 | **2** | 1 (wrong: 62) | **1** | **COMPLETE** |

**TOTALS — current statements: 53. Corrected by round 5: 31. Missed: 22.** *(31 rather than 30 because `C-25` corrected one statement and left its own trailing clause, so one correction site carried two statements.)*

**`PROP-F-01` — Round 5 corrected 31 of 53 current statements: 58%.** It reported 100%.

**`PROP-F-02` — Every one of the 22 misses is explained by one method choice: the population was scoped by phrase, not by claim class.** Round 5 grepped `"P08"`, `"P01 unpublished"`, `"filtered distribution"`. It did not grep `"unpublished"`, `"not published"`, `"filtered build"`, `"filtered tree"`. **The claim was about a peer's publication status; the search was about a peer's name.**

**`PROP-F-03` — The verifier repeated the error before catching it.** This round's first sweep also searched `"P01 unpublished"` and found four misses. Only re-scoping to the claim class — `"unpublished|not published"` — found the other seven, including `36_`:13 `D-02` (a **P08** row that a P01-scoped search structurally cannot see) and `66_`:16 (**a veto condition**). **Two independent passes made the same mistake; the difference was the unit, not the effort.**

## 2. Downstream propagation into outbound handoffs — prompt §4.4 / §4.5

| Outbound artefact | Consumer | Stale current statements before | After |
|---|---|---|---|
| `18_P06_CORE_RECON_HANDOFF_PACK.md` | **P11** | **5** — the five of §4.5. All corrected in round 5 | **0** |
| `70_P06_P11_SUPPLEMENTAL_CRITICAL_RISK_HANDOFF.md` | **P11** | 1, corrected in round 5; re-checked for others | **0** |
| `35_P06_PEER_HANDOFF_MATRIX.md` | all peers | **3** missed (`:15` P01 row, `:27` summary, `:22`'s pair) | **0** |
| `36_P06_DEPENDENCY_REGISTER.md` | all peers | **2** missed (`:13` `D-02`, `:68`) | **0** |
| `34_P06_CROSS_PROCESS_OWNERSHIP_REGISTER.md` | **P11** | **4** missed (`:25` legend, `:34`, `:43`, `:45`, `:51`) | **0** |
| `54_P06_P07_BLOCKING_DEPENDENCY_MATRIX.md` | **P07** | **1** missed (`:99`) | **0** |
| `53_P06_P08_INTAKE_AND_DEPENDENCY_REFRESH.md` | **P08** | **2** missed (`:16`, `:111`) | **0** |
| `66_P06_AAS_PLUS_VETO_SUPPLEMENTAL_RECHECK.md` | **Boss / PMO** | **1** — **a veto condition standing on a false premise** | **0** |

**`PROP-F-04` — The handoff pack built for P11 was clean; the registers P11 would read alongside it were not.** Round 5 corrected `18_` completely and left `34_`, `35_` and `36_` — the ownership, handoff and dependency registers — carrying nine false current statements between them. **Correcting the document labelled "handoff" is not the same as correcting what is handed off.**

**`PROP-F-05` — `66_`:16 is the most serious single miss in either round.** An AAS+ veto condition read `(c′) P01 read — NOT MET, still unpublished`. **P01 has been published at `b820b29` since 2026-09-04.** The condition remains `NOT MET`, but the reason changes from *"impossible"* to *"not attempted, by scope"* — and those two license entirely different Boss decisions. **A false premise under a veto condition is worse than a false premise under a finding, because a veto condition is what a decision-maker reads when deciding whether to wait.**

## 3. Consistency of the corrected wording — prompt §4.3

| Claim | Statements | Consistent? |
|---|---|---|
| `X-08` status | 9 across `18_`, `34_`×2, `35_`×3, `36_`, `39_`, `57_`, `70_` | **YES** — all read *answered by P06, closable only by P10*; none claims closure |
| `is_matched` branch count | 4 across `01_`, `18_`, `25_`, `46_` | **NO before repair** — `01_` said *"unconditionally"*, the other three *"by configuration"*. **YES after** (`REV-E-22`) |
| `is_matched` unit | `25_`:40 counts **branches**, `25_`:67 counts **sites** | **Both correct, unit was undeclared. Declared now** |
| evidence-base boundary | 11 statements | **YES after repair** — all read *relocated, loadable set 791 of 1752*; `40_`/`AAS+` add *2 of 16 roots* |
| peer publication status | 19 statements | **YES after repair** — all read *published; dependency still open; not consumed* |
| G02 blocker population | `40_` B.3 = **63**; `46_` Note 2 = 62 → **63** | **YES after repair** |

## 4. What propagation did NOT change

- **No dependency was closed.** Publication status is not dependency status. `D-01`, `D-02`, `D-15`, `F-02`, `F-06`, `F-15`, `F-17`, `B-46`, `B-54` all remain **OPEN / HOLD** with their existing owners.
- **`P06-B-08` remains `BOSS DECISION REQUIRED`.** Untouched.
- **`P06-OQ-98`** (the prompt's `P06-Q-98`) **remains `HOLD — DEPLOYMENT REGISTRY EVIDENCE REQUIRED`.** Untouched.
- **`AASP-VETO-06`, `REV-E-18`, `HO-03`/`HO-04`** retain their owners and their `WRITTEN, NOT DELIVERED` status.
- **No peer package was consumed.** P01 published and unconsumed → `P06-OQ-124`. The other eight published-and-unconsumed peers → **`P06-OQ-128`**.
- **No new blocker was raised from business evidence.** The two raised are about the package: `P06-B-64` (correction populations scoped by phrase) and `P06-B-65` (a veto condition carried a false premise for two rounds).

---

# PART II — INDEPENDENT FROZEN-SURFACE RECOVERY (2026-09-06, frozen SHA `5212756`)

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-INDEPENDENT-FROZEN-SURFACE-RECOVERY-005]`

> **Part I above is preserved as issued and is materially wrong about its own completeness.** Its nine rows are each marked **COMPLETE**; an independent pass over the frozen surface found residual stale CURRENT statements in **five** of the nine. Part I is not deleted — it is the record of what was believed, and Part II is what measurement says.

## II.1 Re-measured propagation, by claim class

| Claim class | Part I said | **Measured at freeze** | Survivors found | Now |
|---|---|---|---|---|
| `X-08` answered ⇒ closed | COMPLETE | **11 CURRENT, all consistent, none claiming closure** | **0** | **CONFIRMED COMPLETE** |
| Peer publication status | COMPLETE | 20 CURRENT | **1** — `13_`:103 *"8 of 9 — P01 absent"*, in a file rounds 5 and 6 never opened | **REPAIRED** |
| Evidence base filtered/relocated | COMPLETE | 15 CURRENT | **3** — `56_`:68/:70/:78, *in the file that produced the correction* | **REPAIRED** |
| `is_matched` branches/sites | COMPLETE | 21 CURRENT | **1 defective + 2 unit-undeclared** — `01_`:115 contradicted `01_`:122 **seven lines apart in one file** | **REPAIRED** |
| *"eighth settlement door"* | COMPLETE | 6 CURRENT | **4** — `35_`:97/:99, `36_`:58, `34_`:57 vs `:81` | **REPAIRED** |
| `res.config.settings` ACL | COMPLETE | 1 CURRENT | **0** | **CONFIRMED COMPLETE** |
| `ir.sequence` re-issuable | COMPLETE | 1 CURRENT | **0** | **CONFIRMED COMPLETE** |
| Generation gap | COMPLETE | 3 CURRENT | **3** — `40_`:69 *(the PRIMARY `B-44` row)*, `42_`:53, `24_`:42 | **REPAIRED** |
| `P06-B-*` population totals | COMPLETE | — | **4** — `13_`:94, `18_`:214, `70_`:108, and `46_`:124 *on a line round 6 edited* | **REPAIRED** |

**Executed: 21 repairs across 14 files** under `[REV-E-23, 2026-09-06]`, plus 3 supersession/snapshot markers. **Round 5's 30 and round 6's 40 markers are untouched.**

## II.2 Why every survivor was invisible

**`PROP-F-06` — Not one survivor is a reasoning failure. Every one is a pattern that could not match its own class.**

| Class | The declared pattern | What it structurally cannot see |
|---|---|---|
| evidence base | `filtered distribution\|filtered build\|filtered tree` | **the hyphen** — `filtered-build`, `filtered-tree` (9 lines) |
| eighth door | `eighth settlement door\|eighth door` | **the ordinal and the noun** — *"eighth ingestion/settlement door"*, *"eighth settlement path"*, *"a fifth settlement door"*, *"an 8th path"* |
| publication | `unpublished\|not published` | **the paraphrase** — *"P01 absent"* |
| generation gap | `only deployment evidence` | **the synonym** — *"the only available deployment evidence"* |
| population | `population at G02 close` | **the header** — *"Blocker population"*, *"with 55 blockers"* |

**`PROP-F-07` — Part I named this defect (`PROP-F-02`) and then committed it nine more times. That is the third consecutive round to commit the defect it had just diagnosed.**

## II.3 Outbound propagation — re-measured

| Outbound artefact | Consumer | Part I said | **Measured** | Now |
|---|---|---|---|---|
| `18_` Core Recon Handoff Pack | **P11** | **0 stale** | **2 stale** — `:169` peers-read, `:214` blocker total | **0** |
| `70_` P11 Supplemental Handoff | **P11** | **0 stale** | **1 stale** — `:108` blocker total | **0** |
| `34_` Cross-Process Ownership | **P11** | **0 stale** | **3** — `:51` tally, `:57`/`:81` ordinal | **0** |
| `35_` Peer Handoff Matrix | all peers | **0 stale** | **2** — `:97`, `:99` | **0** |
| `36_` Dependency Register | all peers | **0 stale** | **1** — `:58` | **0** |
| `13_` Evidence Manifest | integrity record | not in scope | **2** — `:94`, `:103` | **0** |

**`PROP-F-08` — `VER-F-08` and `PROP-F-04` both certified `18_` as carrying zero stale current statements. It carried two, and one of them — *"7 of 9 read; P01 and P08"* — is contradicted by `48_`:96 in the same package.** The certification was scoped to the five statements the round already knew about.

## II.4 What did NOT change

- **No dependency closed.** `D-01`, `D-02`, `D-15`, `F-02`, `F-06`, `F-15`, `F-17`, `B-46`, `B-54` remain OPEN/HOLD with existing owners.
- **`P06-B-08` BOSS DECISION REQUIRED · `P06-B-09` statutory · `P06-OQ-98` HOLD · `AASP-VETO-06` · `HO-03`/`HO-04` WRITTEN NOT DELIVERED · `X-08`/`D-08`/`PD-08` peer-owned** — all untouched, verified by grep.
- **No peer package consumed.** No new business question opened.
- **`AASP-VETO-07` NOT DISCHARGED.**
