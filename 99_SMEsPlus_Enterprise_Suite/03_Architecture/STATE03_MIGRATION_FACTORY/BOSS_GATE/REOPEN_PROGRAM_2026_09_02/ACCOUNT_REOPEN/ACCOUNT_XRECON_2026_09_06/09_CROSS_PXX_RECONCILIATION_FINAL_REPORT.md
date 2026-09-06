# 09_CROSS_PXX_RECONCILIATION_FINAL_REPORT

**Session** `[SMEPLUS-26-09-06-ACC-P06-P08-P09-P11-XRECON-001]` · `/L99999.99999`
**Branch** `audit/account-xrecon-2026-09-06-001` · **Base** `origin/SMEsPlus` @ `41f3b32`
**Constitution** `[SMEPLUS-26-09-04-ACC-REV2-CORR1]` · **Classification** LAYER 2 — RECONCILIATION QUARANTINE

---

# TERMINAL STATE (§17 — exactly one)

> ## `XRECON-A` — CROSS-Pxx DEFECT LINEAGE RECONCILED — OWNER-BOUNDED CORRECTION PROMPTS READY

**Not `XRECON-B`.** Every cross-Pxx contradiction found was **resolved to an authoritative reading on
evidence**, and each was assigned to exactly one owner. The `5441f8d`-versus-`92de8a1` conflict resolved to
*both true, of different artefacts*. The 18-versus-25 conflict resolved to *the addendum supersedes at claim
level*. The 13-versus-14 handoff-row conflict resolved to *two different populations, no defect*. The
two-19s conflict resolved to *two distinct enumerated families*.

**Not `XRECON-C`.** No required evidence was unavailable. All four references verified unmoved; both audit
branches carry their source packages as ancestors; every artefact needed was readable.

**Not `XRECON-D`.** Authority dependency is **not** all that remains — **11 technical root defects remain
open**, and 13 owner-bounded items are queued.

**This state means the reconciliation is complete. It does not mean anything is repaired.**
**0 of 11 root defects are resolved. Nothing was repaired here, by mandate.**

---

## 1. The single finding that governs everything else

> **Class A is empty.**

Eleven root defects. **Not one is a claim about the ERP that turned out to be false.**

Every source-level claim P06 published re-executed and **held** — the `is_matched` structure, every sampled
v18/v19 line number, the `account_move` SQL, all eight enumerative version counts. P08's evidence base is
**21 of 21 tables byte-identical to the original dumps**. P09's instruments are packaged, package-relative and
checksummed. P11's intake instrument **reproduces exactly** and is published as runnable code.

**What failed, in all eleven cases, is the record of the research:**

- a figure measured correctly at time T and published in the present tense after it stopped being true;
- a correction applied to the one file a blocker named, and not to its siblings in the same claim class;
- a peer consumed at a head that had already moved;
- an instrument that could not fire, returning a silence indistinguishable from a finding.

Both independent verifiers reached this conclusion separately and stated it in nearly the same words:
*"The research is sound; the bookkeeping about the research is not"* (P06) and *"The evidence base is sound …
The reasoning over that evidence is what failed"* (P08).

**The programme's remaining accounting risk is not that it has understood the ERP wrongly. It is that it
cannot currently prove what it has understood.**

## 2. The twelve questions of §5, answered

**1. What material defects actually remain?** **11 deduplicated root defects**, `XRD-001`…`XRD-011`, with
**43 traced manifestations across 24 files**. Local published totals — P06 IEV 25, P08 IEV 17, P09 `M-1`/`M-2`,
P11 39 blockers — are **preserved unchanged** and are **not summed**.

**2. Which are ROOT defects?** All 11. Each is the origin of its manifestations, not a copy of another.

**3. Which are downstream manifestations?** 43, mapped in `03_` §3. The largest single fan-out is
`XRD-001` (8 occurrences / 4 files); the most consequential is `XRD-011` (3 occurrences, one of which is a
**falsification and a derived method rule**).

**4. Which were authored by the verifier/auditor?** **3 of 11 — 27%** (`XRD-001`, `XRD-002`, `XRD-007`),
separated in `04_` and excluded from every owner's source queue.

**5. Which are stale publication defects only?** `XRD-001`, `XRD-002`, `XRD-003`, `XRD-007` — figures and
pointers, no research consequence. **They are still material**: `P06-B-58`, the reliance-risk blocker, is
scaled on one of them.

**6. Which changed surfaces require fresh challenge?** **Six** — `RC-01`…`RC-06`. One (`RC-07`) explicitly
does not. All six are constrained by `AASP-P11-C3-VETO-04`: **no owner may select its own challenger.**

**7. Which Pxx owns each repair?** P06 **4**, P08 **3**, P09 **2**, P11 **4**, Boss **1**. No item has two
owners; `XRD-006` and `XRD-011` are **split into disjoint halves** with a mandatory notification between them.

**8. Which issues are Veto conditions rather than defects?** **17 vetoes standing**, 0 discharged, registered
in `06_` and **excluded from the defect count**.

**9. Which are Boss Decisions rather than defects?** **51 open Boss decisions** across four distinct
identifier families (P08 **19**, P11 **19**, P09 **10**, P06 **3**), plus **`Q-BOSS-01`**, the
structural-independence ruling. **Class F, not counted as defects, none answered here.**

**10. Which statements have propagated into another Pxx?** Measured, not assumed:
**`XRD-011` DID propagate** — P08's no-referent *"3 at 1e-7"* reached three P11 artefacts and became a
falsifier. **`XRD-006` DID propagate** — the `HO-` collision reached P11 and produced a live mis-attribution.
**`XRD-003` DID NOT propagate** — P11 consumed the files carrying P06's wrong counts but carried the
`om_data_remove` finding, not the counts. *That negative was measured against a positive control, not
assumed.*

**11. Which peer packages consumed superseded information?** **P11, from all three of P06, P08 and P09** —
and, uniquely, **the Boss**, whose brief for this session cites the P06 addendum's 25/2/19 against a terminal
report still publishing 18/15.

**12. What exact owner-bounded correction must happen next?** 13 items in `07_`, four executable prompts in
`08_`. **The highest-value single item is `Q-P11-04`** — P11 does not yet know that the figure it falsified
on has no referent.

## 3. The three findings worth the Boss's attention

### 3.1 A repair was scoped to a file instead of a claim class, and the defect survived in the two places that matter most

P11's `B-37` names the defect exactly: the package pins peers at superseded heads. `B-37` was repaired — in
`P11_AUTO_RESUME_STATE.md`, **the file it named**. In P11's two **live outbound registers**, the same defect
survives at six occurrences.

**And the shape of the survival is the finding.** In those two files, the **seven peers whose heads did not
move are pinned correctly**. The **only three that moved — P06, P08, P09 — are the only three still at CORR2
heads.** The three that needed re-pinning are precisely the three not re-pinned, because the sweep was
defined by *where the blocker was found* rather than by *what the blocker was about*.

### 3.2 A falsification, and a method rule, built on a number with no referent

P08 published *"at 1e-7 the answer is 3"* in its P11-bound handoff — **naming its own float instrument as the
cause in the same sentence**. Its independent verifier re-derived the figure in exact Decimal and found **0
unbalanced at 0.005, 1e-4, 1e-7 and exact equality**, on both computed and stored balance. **The "3" is an
artefact of the instrument, not a property of the ledger.**

P11 consumed it three times. At `P11_CORR3_RECONVERGENCE_AND_FALSIFICATION.md`:15, `F-02` asks *"is there a
tolerance at which the count is non-zero?"*, answers **YES** on that figure, re-states P08's soundness claim
on that basis, and **derives a standing method rule**: *"a soundness claim without a tolerance is not a
claim."*

**The correct answer to `F-02`'s own question is NO.** The rule may well be sound — **but it is not supported
by the instance that produced it**, and it is currently in circulation as though it were. **A method rule
inherits the evidential standing of the case that generated it, and this one has none.**

### 3.3 Neither independent verification is structurally independent, and both said so first

P06's prompt carried an explicit precondition — *"THIS PROMPT MUST NOT BE EXECUTED BY THE SAME P06 CORRECTION
ACTOR."* **It was.** P08's verifier states plainly: *"procedural independence was met; structural independence
was not. The verifying agent is the same model that authored the repairs."*

**Both disclosed it unprompted, in their own terminal reports, against their own interest.** Neither can
repair it. It is the binding constraint on `AASP-VETO-07` and on `AAS+-PS-VETO-01` C-6, and it is
**`Q-BOSS-01`** — the one question this session routes to the Boss and does not touch.

**The question is identical on both tracks. It may be one decision rather than two. This session does not
assert that it is.**

## 4. What this session got wrong, recorded first-person

**`XR-I-01`.** The first cross-Pxx peer-SHA sweep used `git grep -o`, which **returns nothing in this
environment**. It reported **zero P09 SHA citations across the entire P11 package** — a clean, plausible,
publishable negative. **The positive control caught it**: `9356557`, a SHA known present, also returned zero.

**Had it stood, this report would have published *"P11 cites no P09 SHA"* — the exact inverse of the truth —
and `XRD-005` and `XRD-008` would not exist.**

**`XR-I-02`.** `\bP06-B-[0-9]{2}\b` returned **0** against a population of **67**; `git grep`'s ERE does not
support `\b`. Caught only because it was run as the second form of a two-form count.

**Both are the defect class this session was convened to reconcile — an instrument that cannot fire, returning
a silence indistinguishable from a result. They recurred anyway.** That is the strongest available evidence
for `XRD-004` and for the standard this package asks of every owner: **publish the command and its output, and
put a positive control inside every negative's population.**

## 5. What is affirmed

Stated because a reconciliation that reports only defects misrepresents the state as much as one that reports
none.

- **P06** — every source-level claim re-executed and held; 63 of 84 per-file hashes match and **all 21 that
  differ are files the round edited**; the evidence-base denominators have **no rival value anywhere**;
  `57_` is a **model negative-claim file** — population, pattern, path set **and** exclusion class all present.
- **P08** — **21 of 21** tables byte-identical to source; arithmetic sound across four independent
  re-derivations; **zero vendor tokens** across Layer-1; identifier families contiguous. And across **six**
  defensible eligibility predicates the numerator is **0 in every one** — *two rounds of denominator
  correction could not have changed any conclusion.*
- **P09** — `L-4` was **split rather than force-closed**, the honest disposition; `L-2` closed only on its
  **third** specification, after two that could not fail; the ephemeral-locator defect **fixed, not asserted**.
- **P11** — the CORR3 instrument **reproduces exactly** and is published as runnable code; **its positive
  control caught an inert loop before publication**; and it **fails its own full 12-member control set on
  `S06`, and says so.**

**Four packages, and in every one the round reported its own failures in stronger terms than a defensive
author would.** That is why this reconciliation was possible at all.

## 6. Prohibitions observed

| | |
|---|---|
| Peer evidence artefacts edited | **NONE** |
| Peer branches pushed to | **NONE** |
| Vetoes discharged | **NONE** (17 standing) |
| Boss decisions answered | **NONE** (51 open) |
| Boss-reserved options eliminated or narrowed | **NONE** |
| Child correction prompts executed | **NONE** |
| PHASE SA/B/C or Functional Design started | **NO** |
| Merged to `SMEsPlus` | **NO** |
| Accounting PASS declared | **NO** |
| Local published totals altered | **NONE** — preserved as audit lineage |
| Historical wrong statements erased | **NONE** — superseded, never deleted |

## 7. Next action

**Boss reviews `07_` and `08_`, and decides `Q-BOSS-01`.**

The four child prompts in `08_` are executable independently and in parallel, with **one ordering
constraint**: `Q-P08-01` owes `Q-P11-04` a written notification — though **P11 need not wait**, since
`IVR-F-16` is already evidence at `bd95d1d`.

**`Q-P11-04` is the highest-value single item in the queue.**
