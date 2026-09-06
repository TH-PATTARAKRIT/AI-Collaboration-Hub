# 51 — P02 PMO ROUND-3 FRESH EXIT ASSESSMENT

`LAYER 2 — AUDIT QUARANTINE.` **CP-09.** Prompt §14. Baseline `aca211e`.

**Assessed from current evidence only.** §14: *a criterion may not improve merely because more work was
performed, and must be downgraded where evidence quality deteriorated.*

---

## 1. Eight Criteria

| EC | Criterion | Previous | **Now** | Evidence delta | Reason for movement |
|---|---|---|---|---|---|
| **EC-01** | Scope bounded | NOT SATISFIED | **PARTIAL** ↑ | Population rebuilt format-complete with per-format positive **and** failure controls and a materially independent second method; **`C-86` shows the source estate is larger and readable** — `C-55` withdrawn. But the coverage assertion was wrong (`C-67`), 39.5% is untested, and four units still have four undeclared denominators. | **Genuine improvement in the evidence base, partly offset by a wrong description of it.** First upward movement in three rounds. |
| **EC-02** | Enumeration converged | NOT | **NOT** | 24 confirmed contradictions this round, 22 of them the same aggregation shape. | Unchanged. Convergence requires a round that raises none. |
| **EC-03** | Unknown exhausted | PARTIAL | **PARTIAL** | `C-04` split; `C-04a` retained as a function-level fact and design input; `C-04b` reachability **re-measured to 11 of 11**. Read-only routes genuinely exhausted **and** the sandbox is now unreachable. | Substance improved, method corrected downward. Net unchanged. |
| **EC-04** | Tolerance-zero closed | NOT | **NOT** | Not re-derived this round — no material delta. | Unchanged. |
| **EC-05** | Cross-process reconciled | PARTIAL | **PARTIAL — with a named regression** | Expert 3: `44`/`45`/`46` contain **zero** references to P06/P07/P08/P09/P10/P11, and `39` predates them. **Three routable items were produced and none routed** (§3). | Held only because the items are now named. |
| **EC-06** | Negative claim controlled | NOT SATISFIED | **NOT SATISFIED** | Failure controls **worked** (`RE-37`, `RE-38`) — the first round where they caught defects before publication. But `RE-40` (a missing utility read as blocked I/O), `C-68` (I/O failure still indistinguishable from `NOTDB`) and `C-67` (the coverage assertion itself wrong) all landed. | **The controls improved and the criterion did not.** A control that reports its own coverage incorrectly cannot discharge this. |
| **EC-07** | Two consecutive clean independent passes | NOT SATISFIED | **NOT SATISFIED** | One pass, four experts, 24 confirmed contradictions. | Unchanged. |
| **EC-08** | Final knowledge package complete | PARTIALLY | **PARTIALLY** | 51 deliverables; registers contiguous (C 86, RE 49); checkpoint and resume state current. Missing: content hashes, per-module versions, the gaps in `50` §4. | Unchanged. |

**0 of 8 satisfied. 5 partial. 3 not satisfied.** **P02 may not be presented for a module exit decision.**

## 2. The Six §14 Verifications

**Evidence identity.** Model built, **tested to destruction twice**, key replaced twice. Now
`ARTEFACT / SNAPSHOT / UUID / LINEAGE / DEPLOYMENT INSTANCE / BUSINESS ENTITY / COMPANY SCOPE`, keyed on
**content ancestry** with a mandatory negative control. **This is the round's most durable output.**

**Population.** `40 artefact paths / 28 distinct contents / 17 snapshots / 14 lineages / ≥9 live
instances (not currently re-derivable)`. **Four numbers, four denominators, all declared.**

**Deployed-code identity.** No archived row grades above `SOURCE AVAILABLE BUT NOT PROVEN DEPLOYED`
after `C-83`/`C-85`. **Materially improved by `C-86`** — the v14/v16 distributions exist, so the
custom-module gap is **smaller** than published (620 → 540; `iSMEs` 13 → 1).

**Negative-claim control.** The weakest criterion, and the most instructive. **Failure controls caught
two defects before publication for the first time** — and three further control failures still landed.

**Mutation boundary.** Held. **Nothing was executed.** The pack that would have breached it was caught
in review (`C-74`).

**Layer-1 integrity.** `19` and `43` unchanged this round; both previously scanned clean with injection
controls. **Not re-scanned — no delta.**

## 3. Named Regression PMO Requires Closed

**`39` was not updated by this round.** Three routable items exist and are unrouted:

| To | Item |
|---|---|
| **P07** | Thai branch identity: **9 of 44 company partners have NULL `company_registry`** and compute to `"Headquarter"`; **two companies emit the identical branch code `00009`**; one has NULL country. **Fact set only — P02 does not decide Thai law.** |
| **P08 / P09 / P11** | `odoo_cff_golive_99` has **neither a source basis nor a behavioural marker** — which invalidates source-derived negatives for **every** process on that deployment, not only P02's. |
| **P06 / P11** | **9 stopped `postgres:16*` containers** retain volumes never enumerated. |

## 4. PMO Position

**`RECOMMEND HOLD`.**

**What improved, genuinely:** the evidence estate is larger and more readable than the package believed;
the identity model is now falsifiable and has been falsified twice and repaired; failure controls caught
defects before publication for the first time; and a safety defect was caught **before** it reached a
Boss.

**What did not:** every count the package published about itself this round was wrong at least once, and
the criterion that governs exactly that — `EC-06` — cannot be discharged by controls that misreport
their own coverage.

**The honest summary is the same as the previous round's, one level up.** This round did the most
methodologically rigorous work in the programme **and** had the most of its own output corrected. Those
are the same fact: **the work was specific enough to be checkable, and it was checked.**

**PMO accepts the terminal state as a bounded handoff, not an exit**, on the explicit condition that
every consumer reads `50` §4 and §3 above before relying on any figure.

---

## TERMINAL STATE — round `SMEPLUS-26-09-05-G02-P02-O2C-FINAL-UNCERTAINTY-CLOSURE-003`

**`G02-P02 MAXIMUM AVAILABLE EVIDENCE REACHED — HOLD FOR NAMED DEPENDENCY`**

**Terminal A was considered and rejected.** It requires that the evidence-identity and population method
is *"no longer itself an unresolved blocker"*. It still is: the content-ancestry key has **not** been run
on the 13 groups it was not derived from, and **only 60.5% of candidates were content-tested**.

**Terminal C was considered and rejected.** The method's contradictions were **all caught and corrected
within the round**, and every substantive accounting finding **reproduced on an independent instrument**.
Reliance on the findings is possible with the bounds stated; the package is not in integrity failure.

### Named dependencies

| # | Dependency | Owner |
|---|---|---|
| 1 | **`C-04b`** — the authorisation pack is **WITHDRAWN** (`C-74`) and must be re-submitted per `47` §5.6 | **Boss** |
| 2 | Content-ancestry key untested on 13 lineage groups | P02 |
| 3 | 76,245 candidates untested, incl. 807 above the floor; content hashes; per-module versions | P02 |
| 4 | Containerised databases in or out of the population — **decision required in writing** | P02 → P11 |
| 5 | Thai branch identity — 9 NULL registries, duplicate branch code `00009` | **P07** |
| 6 | `odoo_cff` has neither source basis nor behavioural marker | **P08 / P09 / P11** |
| 7 | 9 stopped container volumes never enumerated | **P06 / P11** |
| 8 | Revenue: billing vs performance | **Boss** (`BP-03`) |
| 9 | Three scope holds | **P11** |

**Not PASS. Not approved. Not frozen. Not merged. No implementation authorised. No mutation occurred.**
