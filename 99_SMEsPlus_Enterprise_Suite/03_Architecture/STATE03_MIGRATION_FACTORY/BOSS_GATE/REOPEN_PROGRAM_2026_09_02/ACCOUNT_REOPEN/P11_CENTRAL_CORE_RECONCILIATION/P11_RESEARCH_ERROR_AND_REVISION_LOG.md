# P11 — RESEARCH ERROR AND REVISION LOG

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**
> This log records **this session's own errors**, not other packages'. Errors found in other packages
> are contradictions and live in `P11_CONTRADICTION_REGISTER.md`.

---

## `P11-E-01` — a headline figure contradicted its own table

| | |
|---|---|
| **Where** | `P11_UNIFIED_EVENT_OWNERSHIP_REGISTER.md` §2 |
| **Error** | The headline was drafted as *"`C2` fails for **8** of 44"*. Re-deriving the count from the §3 table returns **9** business facts |
| **Cause** | The draft figure was written before the table was finished and was not re-derived afterwards |
| **Detection** | Self-caught, by re-deriving the count from the table rather than restating the headline |
| **Correction** | Stated **inside the affected file**, adjacent to both figures, with the corrected value: **`C2` fails for 9 of 44** |
| **Why it is logged at all** | This is **`GB-06`'s exact shape** — a published count contradicting the dispositions beneath it — and it is the defect that produced `FC-F1` in the parent programme. It occurred here, in the first session to write about it. **A log that only recorded other people's instances of `GB-06` would be evidence that the control does not work** |

## `P11-E-02` — the superseded scope assumption

| | |
|---|---|
| **Where** | Every scope statement written before constitution correction `SMEPLUS-26-09-04-ACC-REV2-CORR1` was received |
| **Original assumption** | Tenant context + company context mandatory for every operation, inherited from `BC-02` element 10 and Wave A `TI-01` |
| **Why over-constrained** | `PLATFORM`-scoped reference data legitimately requires neither; a blanket rule would forbid the platform layer from existing |
| **Correction applied** | `P11_SCOPE_OWNERSHIP_MATRIX.md` created; five revalidations `RV-01`…`RV-05` recorded in full, each with original finding → assumption used → why over-constrained → correct analysis → updated classification → architecture impact → cross-process impact → evidence required |
| **Scope of rework** | **Delta only.** No evidence discarded, no checkpoint re-run, no completed enumeration repeated. Findings **not** touching the assumption are preserved byte-for-byte |
| **Net effect on severity** | **`RV-05` did not relax.** The 10-of-10 element-10 failure stands, because all ten material handoffs create a financial effect and are `COMPANY`-scoped. `RV-02` and `RV-03` **sharpened** their findings without changing either disposition. `RV-04` **narrowed** one blast radius. `RV-01` corrected a rule's reach while preserving its intent |

> A correction that relaxes a rule invites the reading that failing counts relax with it. **They did
> not, in four of five cases.** Recording the direction of each revalidation — rather than assuming
> it — is the whole point of running them.

## `P11-E-03` — a peer clone was mis-enumerated on the first pass

| | |
|---|---|
| **Where** | The first peer-intake sweep |
| **Error** | The glob `ACCOUNT_P0*_2026_09_04_EXECUTION` **silently excluded `P10`**, whose directory is `ACCOUNT_P10_TBR_...`. The first reading was "nine clones exist, `P10` has none" |
| **Cause** | An author-chosen pattern that did not cover its own declared population — **the exact defect the denominator rule exists to prevent**, committed while writing the file that states the rule |
| **Detection** | Caught when the enumeration script was written with the population declared **first**, which forced the pattern to cover `P10` |
| **Correction** | `p11_scripts/peer_intake.sh` and `peer_wip_snapshot.sh` both enumerate `P0[1-9]` **and** `P10` explicitly. All counts in this package are from the scripts, not from the first sweep |
| **Consequence if undetected** | The register would have reported a **9**-process peer dependency instead of **10** |

## `P11-E-04` — a peer working tree changed between two observations

| | |
|---|---|
| **Where** | `P01`'s working tree, between the intake script and the WIP snapshot, minutes apart |
| **Not an error — a property of the observation** | The peer sessions are **live**. `P01` showed `worktree_changes=0` on the first run and one untracked file on the second |
| **Correction to method** | Every peer-state count in this package is stamped `SNAPSHOT_UTC=2026-09-04T22:41:38+0700` and is described as a reading at an instant, not a stable population |
| **Why it is logged** | Because the alternative — reporting a count of peer work-in-progress as a finding — would have been a measurement presented as a fact about the programme |

---

## Summary

| Measure | Count |
|---|---|
| Errors made by this session | **3** (`P11-E-01`, `P11-E-02`, `P11-E-03`) |
| Self-caught before publication | **3 of 3** |
| Caught by an external reviewer | **0** — and this is **not** evidence of quality. `EC-07` requires two consecutive clean independent passes; this session has had **none** |
| Method observations logged | **1** (`P11-E-04`) |

---

# PART 2 — POST-CHALLENGE

## `P11-E-05` — a Boss ruling inverted and attributed to the ruling that superseded it

| | |
|---|---|
| **Where** | `P11_SCOPE_OWNERSHIP_MATRIX.md` §3 product-master row; repeated in `P11_SAAS_ACCOUNTING_BOUNDARY.md` §1 |
| **Error** | P11 recorded *"Product master \| `TENANT` (per Boss ruling `D-01`)"*. `MTI-D-01` rules **`OPTION B — Company-owned Product Master`**, and its §4 records that the ruling **supersedes** the earlier AAS+ recommendation preferring a tenant-level master. P11 reinstated the superseded position and cited the ruling that killed it as its authority |
| **Why it matters beyond the row** | P11's own table defines `TENANT` as *company context not required*. The placement therefore licenses exactly the shared cross-company product identity the ruling refuses — and the ruling's stated business reason is two companies performing a same-looking transport service under **different withholding-tax conditions** |
| **Detection** | **Three times independently** — P11's own re-read of the ruling, `X3-F06`, and `X1-F01` |
| **Correction** | Product master → `COMPANY` owns/mutates; a separate `TENANT`-scoped **mapping-layer** object added per ruling rule 5 (reference only, no financial effect) |

## `P11-E-06` — an undecided decision package listed among the controls that govern the round

`BC-04` sat in the table headed *"Boss-approved controls that **govern** this reconciliation"* while
the GB-08 artefact reads **`BOSS DECISION REQUIRED — GB-08` / "This file does not select an option"**
— and P11's own `DEP-14` says *"packaged, not decided"*. **§1's declared POPULATION was contaminated
by it**, because the population is defined as *"named in a `PEER-PUBLISHED` artefact or a
`BOSS-APPROVED` control"*. Found by `X1-F02`. Reclassified to `PEER-PUBLISHED`, pending decision.

## `P11-E-07` — the trace-lane headline contradicted itself in one sentence

*"2 reach a statement line without an unresolved break … and each carries an open tolerance-zero or
contract failure at the end of the lane."* Self-caught, and independently by `X4-F12`, which
re-derived **3** lanes with no ✘ and **0** free of an unresolved break. Corrected to state both tests
separately.

## `P11-E-08` — accounting-standard requirements presented as Thai statute

`P11_TAX_ARCHITECTURE.md` §1 headed three positions *"Statutory"*. The source reserves
`THAI STATUTORY REQUIREMENT` for Revenue Code s.65 bis (2) and Royal Decree 145 alone, classifies
TAS 2 ¶12/¶13 as **`ACCOUNTING STANDARD REQUIREMENT (TFRS)`**, and the DBD finding as
**`THAI REGULATORY FACT`**. Self-caught and independently by `X3-F01`. **P11 closes no
`THAI STATUTORY REQUIREMENT`.**

## `P11-E-09` — two of TAS 2 ¶13's four requirements dropped

Requirement **1** (normal capacity *"taking into account capacity lost to planned maintenance"*; the
actual level may be used **if close to normal capacity**) and requirement **4** (in abnormally high
production the per-unit fixed amount is **reduced**, so inventory is **not carried above cost**).
Consequence: `CVP-01` mandated absorption **with no upper bound** — the half of ¶13 that protects the
balance sheet. Self-caught and independently by `X3-F02`.

## `P11-E-10` — `DC-09` overclaimed as novel

The Asset package already names the **analytic-tag-plus-rate** variant: *"if depreciation reaches
product cost **both** through an analytic tag **and** through a derived machine rate, nothing in the
platform notices."* P11's contribution is the **expense-relief** variant only. Self-caught. Both are
now registered, and `P04` has since shown the true count of competing monetisations is **five**.

## `P11-E-11` — the stated subledger rule was not the rule applied

`X2-F06`, **CRITICAL**. §1 declares *"a structure failing `S3` **or** `S4` is a derived view"*; §2
applied *"fails both"* and awarded *"of record"* to four rows failing one criterion. Under the stated
rule the register reads **3 of record, 5 derived views, 2 unknown** — and `X2-F07` then shows AR and
AP fail on the same evidence used to fail Settlement, taking *"3 unqualified"* to **0**. **A logic
error, not a citation error.**

## `P11-E-12` — a pattern that could not cover its declared population, twice

`P11-E-03` recorded the first instance (a glob excluding `P10`). `X4-F02` found the second and worse
one: **`peer_intake.sh` section C was inert by construction** — `set -e` plus a piped `for` loop
killed the subshell at the first ref with no match, so declared PATTERN (b) **could never return a
hit**. The published empty result was an **artefact**, not a measurement. Corrected as v2 with the
`set -e` removed, `|| true` per ref, and a **positive control** whose value (86 matching paths) makes
an empty section C evidence rather than silence.

> **This is the most serious methodological failure of the round.** The defect was invisible to every
> reading of the script and was found only by an independent party **executing** it. It is the
> programme's own rule — *a denominator must be executed, not quoted* — proven again, against the
> session that wrote the rule down.

## `P11-E-13` — the negative-claim boundary was declared once and not applied package-wide

`X2-F11`, `X1-F11`, `X4-F14`. `F7` was stated *"not implemented at all"* where the governing CORR1
disposition is **`PARTIALLY VERIFIED`** — *"a real database constraint exists, but only with an
optional module installed, and it is **table-global rather than tenant-scoped**"*. And `X4-F14`
established that the blanket class-`C` demotion was simultaneously **over-broad** (two packages **did**
declare exhaustive search boundaries) and **inconsistent** (P11 relies on those same negatives as
fact). **P11 conflated *applicability* with *verification*: `MCU-21` is which root SMEsPlus targets,
not which scope was searched.**

## `P11-E-14` — the premise expired mid-session

Recorded in full at `P11_PEER_INTAKE_DELTA_01.md`. P11's synthesis was written against **0** published
peer packages; its four-expert challenge was commissioned against **0** and reviewed against **2**;
**six** had published by session close, and **two were already at a later SHA than P11 read**.

**Not an error of fact** — every count was stamped and labelled a reading at an instant, and one
reviewer declined to endorse it rather than assume it. **It is an error of sequencing**: a
reconciliation was scheduled before the things it reconciles existed.

---

## Summary — both parts

| Measure | Count |
|---|---|
| Errors made by this session | **13** (`P11-E-01`…`P11-E-14`, less `P11-E-04` which is a method observation) |
| Self-caught before the challenge | **3** |
| Self-caught in parallel with the challenge | **4** |
| Found only by independent challenge | **6**, including both CRITICAL |
| Findings raised by the four panels | **86** · accepted **86** · disputed **0** |
| Defects found by two or more panels independently | **6**, three of them found three times |
| Errors corrected at source in this session | see `P11_BOSS_FINAL_GATE_PACK` §26 |

> **The controlling lesson, and it is not new — it is the fourth recorded instance:**
> **independent review found what self-review could not, and the two it found first were the two that
> invalidated the round's own instruments.** Self-review found 3 before the challenge; the challenge
> found 86, including a broken evidence script and a rule stated one way and applied another. A
> round that reported only its self-caught errors would have published a false picture of its own
> reliability.
