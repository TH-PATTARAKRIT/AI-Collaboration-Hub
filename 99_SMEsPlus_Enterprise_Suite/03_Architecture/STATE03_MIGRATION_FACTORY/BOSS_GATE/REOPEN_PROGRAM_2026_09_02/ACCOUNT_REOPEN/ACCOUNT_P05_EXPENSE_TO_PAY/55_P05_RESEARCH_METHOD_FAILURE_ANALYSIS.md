# 55 — P05 RESEARCH METHOD FAILURE ANALYSIS

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E16`
**Method, not attribution.** The question is which control was missing, not who missed it.

## 1. The Seven Diagnostic Questions

| # | Question | Round 1 | Round 2 | Round 3 (this) |
|---|---|---|---|---|
| 1 | Was the **evidence population** challenged? | **NO** — assumed source-only | **NO** — enumerated found dumps | **YES** — exhaustive filesystem search (`41 §2`) |
| 2 | Was the **denominator** challenged? | partly | **NO** — "six registries" never proved a population | **YES** — 9 identities declared, 1 unread and flagged |
| 3 | Was the **tooling** challenged? | **NO** | **NO** — `-s -t` false negative shipped | **YES** — `-s` unfiltered; Challenge B commissioned on parsing |
| 4 | Was **extraction completeness** challenged? | n/a | **NO** | **YES** — Challenge B tasked to quantify COPY-parse loss |
| 5 | Was arithmetic **mechanically recomputed**? | n/a | by reviewers only | **YES** — by reviewers, and every figure reproduced |
| 6 | Were **reports compared against exports**? | **NO** | source-only | **YES** — `50`, both predicates traced |
| 7 | Were **installed modules verified before risk ranking**? | **NO** — ranked on source alone | **PARTLY** — verified, but on a population missing the target | **YES** — and the ranking inverted twice as a result |

## 2. The Failure Sequence

1. **Round 1** ranked risk from **source alone**, with no deployment evidence. It produced a headline
   finding (`TZ-01`) that was *source-true*.
2. **Round 2** discovered deployment evidence, ranked by **reach**, and reclassified `TZ-01` to
   `LATENT` — on a population that **contained no petty cash and no expense claims at all**
   (`iSMEs`: 2 expenses, 0 sheets). The reclassification was arithmetically correct over the wrong set.
3. **Round 3** found the target-platform database and `TZ-01` came out **contradicted** — the opposite
   of both prior positions.

> **The finding did not change. The population did — three times.** Each round's conclusion was sound
> given its evidence base and wrong given the next one's. **The defect was never in the reasoning
> about the finding; it was always in the reasoning about the evidence base.** That is why the
> directive's mandated review order — population → denominator → tool → extraction → *then* finding —
> is the correct order, and why P05 had it backwards twice.

## 3. Why Self-Review Did Not Catch It

Across three rounds, **every** material correction came from independent review; none from the author,
after review. The mechanism is now clear and is not a matter of diligence:

**A search boundary is invisible from inside the search.** The author who chose to look in
`~/Downloads` had no signal that `~/OCC_BACKUP` existed. Nothing in the returned evidence indicates
what is missing — absence produces no output. This is structurally different from an arithmetic error,
which the data itself can expose, and it is why *"re-run a zero result in a second form"* (`RE-06`)
did not help: the results were **not** zero. They were plausible, non-empty, and incomplete.

**The only controls that work against it are external:** a reviewer with a different starting
assumption, or a directive that forces a search wider than the author would have chosen. Both
appeared here — Round 3's exhaustive search was run **because the directive demanded it**, not because
the author suspected a gap.

## 4. Controls Adopted

| Control | From |
|---|---|
| An evidence-population claim is only as good as its **root**. Make the root the filesystem, not a folder where something was already found. State root + pattern + unit. | `RE-20` |
| Verify **installed modules before ranking risk**, and verify that the population includes the **target platform**. | `RE-21` |
| A population that lacks the phenomenon cannot reclassify it. Before reclassifying finding X, confirm the population **contains** X's data. | `RE-21`, and the sharpest lesson of this round |
| Prove a tool can express a **positive** before accepting its negative. | `RE-13` |
| Never assume which of two fields is authoritative — **join to the authority**. | `RE-10` |
| **Decompose a count** before publishing it as a defect. | `RE-11` |
| Count identities, not files. | `RE-15` |

## 5. Residual Method Risk

`U-16` — the deployed module does not match the analysed source copy despite an identical version
string. **Every source-only finding in this package rests on a code copy that is not demonstrably the
deployed code.** No control currently in place detects that; the only fix is to extract the deployed
module source from the environment itself, which requires runtime access (`U-02b`).
