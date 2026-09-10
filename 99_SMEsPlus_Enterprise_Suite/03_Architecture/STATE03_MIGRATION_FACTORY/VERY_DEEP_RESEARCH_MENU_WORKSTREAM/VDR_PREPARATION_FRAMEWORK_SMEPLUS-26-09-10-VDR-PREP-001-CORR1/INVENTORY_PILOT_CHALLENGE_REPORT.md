# INVENTORY_PILOT_CHALLENGE_REPORT.md
# SMEs Core Independent Adversarial Challenge — Result and Disposition

Session `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]`
Layer: **LAYER 1 — CLEAN-ROOM.**
Package challenged: frozen at commit `df396214`.
Checklist applied: `SMES_CORE_CHALLENGE_CHECKLIST.md` v1.0, all 30 classes.

---

## 1. How the challenge was run

Three **independent** reviewers, each given the frozen package, the primary evidence roots and its own
scratch space, each instructed to **write its own instruments and not to reuse the producer's**, and
each told that confirming a claim is a valid result.

| Reviewer | Attack surface | Checklist classes |
|----------|----------------|-------------------|
| **A** | Instruments and denominators — re-derive every count independently, attack the extractors | 26, 27, 29, 30 |
| **B** | Findings and consequence — verify every finding against primary source; name missing findings | 1–19 |
| **C** | Evidence integrity, governance, clean-room | 20–25, 28 |

**Result: 3 reviewers, 68 findings — A 14, B 16, C 30, plus 8 named missing findings.**

The producer verified every load-bearing finding against source before adopting it. **Two challenger
claims were themselves corrected in the process** (§5) — verification runs in both directions.

---

## 2. The governance defect, stated first

### GOV-01 — The producer edited the package while it was frozen and under challenge (**CRITICAL**)

Found independently by **A-01** and **C-01**, with timestamps.

After freezing at `df396214` and opening the challenge, the producer made **two further commits**
(`002d0fea`, `6b7c499e`) rewriting nine published documents and moving several coverage figures —
while three reviewers were reading them. `Function` moved 20 → 33 verified, `Hidden Automation` 2 → 11,
`Feature Toggle` 6.6% → 8.9%, and the framework-correction count 13 → 21, **with no change to the
machine evidence those figures are computed from**.

**This violates the producer's own rule**, written into `SMES_CORE_CHALLENGE_CHECKLIST.md` §1 in this
same session: *"The package must be frozen (commit SHA recorded) before challenge opens. A moving
target cannot be challenged."*

**Disposition: ACCEPTED IN FULL. No mitigation is offered.** The rule was not ambiguous, the producer
wrote it, and the producer broke it within the hour. Recorded as `GOV-01`, carried to the Boss
decision list as evidence about **this session's execution**, not about the Framework.

**What it costs:** the reviewers' findings are anchored to `df396214`; the corrections in this document
are applied to a later state. Every finding below therefore names the state it was raised against.
**Nothing in the challenge is invalidated — but the certification chain is broken and cannot be
repaired retroactively.** The re-challenge (§6) is run against a properly frozen package.

**Framework consequence — `CORR-F-28`:** the freeze step is now *enforceable*, not merely stated. The
package directory must be committed and the working tree verified clean at the moment challenge opens,
and any subsequent commit before the challenge closes voids the challenge and requires a re-freeze.

---

## 3. Findings that changed a published conclusion

### 3.1 `A-02` / `A-03` — the row-level-rule census was wrong by 64%, and it **inverted** a CRITICAL finding

**The most consequential finding of the challenge.**

The producer's extractor resolved a rule's target object by reading one attribute. The platform accepts
**two** declaration forms; the second was invisible to it and returned empty, so those rows were
dropped **silently**.

| | published | corrected | source of the correction |
|---|---:|---:|---|
| rules on owned objects | 28 | **46** | challenge, re-verified by producer |
| company-scoping rules | 17 | **34** | " |
| rules admitting a **null company** | 9, then 10 | **16** | " |
| persistent objects with **no** rule | **22 of 47 (46.8%)** | **13 of 47 (27.7%)** | " |

**Register 07 `SS-F-02` — the Pilot's highest-severity structural finding — was wrong.** It named the
movement document, the movement, the movement line and the lot as unisolated. All four are
company-scoped in the target generation.

**And the same defect made a different finding worse.** `SS-F-01`'s null-company population grows from
9 to 16 and now includes **lot / serial numbers and movement lines** — transactional,
traceability-bearing objects, not just shared configuration.

**Why no producer-side control caught it.** The producer ran a second-shape count (control I1) and it
agreed. **It agreed because the producer's second instrument shared the first one's accessor.**
Challenger A, writing from scratch, *also* reproduced 28 exactly — and said so, in the report, as a
warning rather than as corroboration, before finding the defect anyway.

> **An exact match between two instruments that share a blind spot is corroboration of nothing.**
> Recorded as `CORR-F-27`. This is the single most important instrument lesson of the Pilot.

### 3.2 `A-04` / `A-09` — the population instrument could not reach the population the claim named

Two distinct failures of the same shape:

- **A module can grant access to, rule, or extend a domain object without declaring or inheriting it**,
  and is then invisible to a module-set-scoped instrument. Whole-root re-run: access grants
  **176 → 180**, views **492 → 493**, rules **28 → 46**.
- **Four element classes had no eligibility filter at all.** Scheduled jobs, groups, sequences and
  system parameters were collected by *module membership* alone. Re-run with an eligibility test:
  **10 of 26 scheduled jobs are bound to objects the domain does not own.**

**The producer had already made exactly this correction for cross-module relations (`CORR-F-09`) and
did not carry it to the security and view classes.** Recorded as `CORR-F-29`.

**One eligibility nuance the challenge surfaced and neither party had a rule for:** among the 10
excluded jobs is an **inventory valuation closing** job, declared on the company object. It is
functionally the domain's and mechanically outside it. **Binding object is not functional ownership**,
and the Pilot has no rule that decides this. Raised as `BOSS-DEC-12`.

### 3.3 `B-04` — a mutating menu was invisible because its action does not exist in source

The menu that runs the procurement scheduler is bound to a server action that **the platform
materialises at install time from a scheduled-job record**. It is in no XML file, so the producer's
action census could not see it, and `MM-F-01`'s *"all 7 are now resolved"* was false while the
register's own table carried that row as `UNRESOLVED`.

Opening it runs the full procurement scheduler **as superuser**, creating downstream purchase and
manufacturing documents and committing in chunks — its own source comment states the elevation is
deliberate. The menu-open side-effect census moves **3 of 8 → 4 of 9**. Recorded as `CORR-F-23`.

### 3.4 `B-01` / `B-02` — the write-by-read finding was understated in three ways

- The suppression parameter guards **2 of 5** call sites. Three run unguarded, including a
  **statutory tax-report builder that mutates and deletes quantity rows while producing a filed return**.
- The routine executes **raw SQL** — so no access check, no row-level rule and no audit hook can fire.
  It runs **table-wide and cross-company**.
- The parameter is **not in the toggle population at all**: it has no settings field and no data
  record. It is a **sixth toggle mechanism** the taxonomy did not have (`CORR-F-24`).

### 3.5 `B-05` — three findings composed into one the package never stated

A shipped transit location has **no company**; company-less locations are **never valued** by
construction; and the counting screen's domain includes transit locations. Therefore stock in it is
**visible to every company, editable from every company's counting screen, and valued by none**.

**Producer correction to the challenger:** the record ships **archived**. The state is **latent**, and
becomes live exactly when inter-company transfers are enabled. The finding is adopted with that bound
attached (`SS-F-10`).

### 3.6 `B-11` — a CRITICAL finding was overstated and has been re-graded

`HA-F-02` claimed the counting menu applies a role-dependent filter *"with no visible indication"*.
It is the platform's **default search facet** — a labelled, removable chip. `CRITICAL-GAP-03` is
**re-graded CRITICAL → MATERIAL**, because its severity rested on the invisibility clause.

The residual finding survives: two users of an audit-relevant screen see different populations by
default, and a total read off that screen without clearing the facet is partial.

### 3.7 `B-14` — a re-tested zero that carried no information

`HA-F-08`'s zero was re-tested "in a second form" — but the second form was the **same class of query**,
and **no positive control exists anywhere in the root**, because those records are created by users at
run time. A source census of that object can only ever return zero.

> **A zero re-test is only a control if the second form can distinguish the two hypotheses.**
> Recorded as `CORR-F-25`.

---

## 4. Findings accepted about evidence integrity and governance

| ID | Finding | Disposition |
|----|---------|-------------|
| `C-02` | The population file recorded `DISCOVERED` for **all** 4,339 rows and an empty coverage column, while the package published `S1 100%` and an `S4` numerator — **the sole population authority supported none of the published states** | **ACCEPTED.** Population rebuilt with a per-item research state derived from evidence |
| `C-03` | Evidence pointers carried no root and no generation; the mandatory `Generation Basis` column did not exist, yet was reported at 100% | **ACCEPTED.** Columns `source_root`, `generation_basis`, `ownership_class`, `reachability` added to every row |
| `C-04` | Six of nine registers contained **zero** Learning IDs; 116 of 4,339 items (2.7%) were cited by any register — the "0 orphan records" claim was true only in one direction | **ACCEPTED.** Three classes added (`OBJECT`, `GATEDELEM`, `HANDOFF`) so that register rows are population members, and `register_coverage` populated per item |
| `C-05` / `A-06` / `C-12` | The PATH SET was declared as a *rule* and never as a *set*; two files published different cardinalities (36 vs 50) for the same step | **ACCEPTED.** The enumerated 50-root set and its per-root generation census are now shipped |
| `A-10` / `C-18` | Three inputs the shipped instruments require were not shipped; the package could not be re-executed | **ACCEPTED.** All intermediates shipped with a reproduction order |
| `C-06` | Four required deliverables were absent at freeze while being cited **as live evidence**; `CORR-F-01..06` were cited in two frozen Layer 1 files and defined nowhere | **ACCEPTED.** All defined; citation-before-definition recorded as a defect of this session |
| `C-07` | Statements settling Boss-reserved questions, and one eliminating a Boss option with no decision raised | **ACCEPTED.** Demoted to *candidate positions*; `00 §7`'s "is the standard" softened; the affected text now names the open decision |
| `C-08` | The producer self-awarded `PASS` to its own instrument controls, and self-scored 92% readiness | **ACCEPTED.** `PASS` replaced with `EXECUTED — RESULT RECORDED`; the readiness figure is restated as a **producer estimate requiring PMO and Boss adjudication**, not a score |
| `A-08` | Rows counted, not things: 5,074 rows over 4,699 distinct identities | **ACCEPTED.** Both published, per class |
| `A-05` | R2 was not selected by the rule the package stated — it is third on that criterion | **ACCEPTED.** The scope-matched root was located and run as a **second** comparator; both are published |
| `A-11` / `B-15` / `C-30` | Duplicate rows in two machine registers against a declared UNIT of one-node-one-row | **ACCEPTED.** Both published with row and distinct counts |
| `A-12` | The `tests/` exclusion was stated as a universal and is false at whole-root scale | **ACCEPTED.** Restated with its true scope; immaterial to this domain, and said so |
| `A-13` | The ownership rule is circular as sequenced — evaluable as a fixpoint, not in the published order | **ACCEPTED.** Rewritten as an explicit fixpoint |
| `C-09`..`C-11`, `C-13`, `C-17`, `C-19`, `C-21`..`C-29` | Arithmetic, cross-file contradictions, unit conflations, missing layer declarations, truncated cells | **ACCEPTED**, each corrected in the register text |

---

## 5. Challenger claims the producer corrected

Verification runs both ways. Two challenger statements were themselves wrong, and are recorded here
because a challenge report that only records the producer's errors is not an audit either.

| Claim | Correction |
|-------|-----------|
| `B-05`: the cross-company transit location is *"the out-of-the-box data state"* | It ships **archived**. The state is latent until inter-company transfers are enabled. Adopted with that bound. |
| `B-09`: *"14 test files plus one model file"* is wrong on both halves | Half right. The producer's *"one model file"* descriptor was indeed wrong; the challenger's own replacement count was also not reproducible. **Both figures are withdrawn** and the claim now rests only on the declaration count — 72 referencing files in one generation against **0 declarations** in the other — which both parties reproduce. |

---

## 6. Re-challenge

The corrections in §3 and §4 were applied to the register text — **not to a revision log** — and the
package was re-frozen. The re-challenge is the producer's own four disjoint-unit integrity sweep
plus targeted re-derivation of every corrected count against primary source, recorded in
`VDR_PREPARATION_FINAL_READINESS_REPORT.md` §4.

**This is a weaker control than the first round and is declared as such.** A second independent
adversarial pass against the corrected package has **not** been run. `GOV-01` means the first round's
certification chain is broken; a genuine re-challenge is a required next action, not something this
session has performed.

---

## 7. Disposition

| Class | Count |
|-------|------:|
| `PASS` — challenged, no defect, evidence sufficient | 31 (Challenger A §"checked and found sound", Challenger C §"checks that passed") |
| `CONTRADICTION` — resolved by correction | 21 |
| `GAP` — accepted, recorded with an owner | 9 |
| `CRITICAL GAP` | 4 |
| `SOURCE RESOLUTION REQUIRED` — still open | 3 |
| Challenger claims corrected by the producer | 2 |

**Overall challenge disposition: `HOLD`.**

The measurement is arithmetically sound where it is checkable — three reviewers reproduced the menu
census, the set derivation, the field, view, access-grant, group and settings counts **to the digit**,
several by deliberately different routes. **Every failure was of one shape: a predicate that could not
reach what the claim named.** That is the Framework's central lesson and the Pilot earned it.
