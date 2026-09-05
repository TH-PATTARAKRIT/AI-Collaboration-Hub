# P01 — `DEP-P01-06` RECHECK: EXPERT OUTPUT AGAINST THE SCOPE-AWARE CORRECTION

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.**

---

## 1. WHAT `DEP-P01-06` IS

In the previous round the Boss scope-aware correction arrived **after** four expert briefs had
been issued, and **could not be forwarded** because inter-agent messaging is disabled in this
environment. The recorded risk: an expert may have **suppressed a legitimate observation** by
judging it against the superseded *"tenant and company context required everywhere"* reading —
and **suppression is invisible to a re-read of what was written.**

---

## 2. STATUS

> ### `PARTIALLY RESOLVED`

---

## 3. RESULT OF THE RECHECK

All four prior expert reports were re-read against the corrected scope model.

| Outcome | Count |
|---|---|
| Findings that **fall** under the corrected model | **0** |
| Findings **strengthened** by the correction's residual rules | **7** |
| Findings **weakened** | **4** |

The four weakened items are: an isolation finding on supplier records; a count of unscoped
models; an account-field sub-claim; and one localization scope claim.

**No expert conclusion was reversed by the correction.** The correction changed the *weight* of
several findings and the *framing* of others, and reversed none.

---

## 4. TWO WEAKENED ITEMS WERE CLOSED BY EXECUTION, NOT ROUTING

The expert performing the recheck **ran the two queries** that the recheck itself identified as
decisive, rather than routing them onward:

| Item | Query | Result |
|---|---|---|
| A localization scope claim | do any companies share a partner? | **0 of 90** — the claim is sound as deployed |
| An isolation residual | are there company-less supplier records? | **0 of 13,152** — the residual is latent |

Both are now settled on deployed evidence.

---

## 5. WHY IT IS ONLY *PARTIALLY* RESOLVED

The tenant residue is **not** closed, and the evidence for that is direct:

> The word *tenant* appears **once in 384,836 bytes** of prior expert output — as a heading.

The four experts, briefed under the superseded reading, **effectively did not analyse tenancy at
all**. That is not suppression of a specific finding; it is the **absence of a whole dimension**
from their analysis.

A re-read cannot recover it, because there is nothing written to re-read. Only **re-running the
isolation assignment with the corrected constitution attached** can close it.

---

## 6. THE HONEST LIMIT

A re-read establishes that **nothing written is wrong under the corrected model**. It cannot
establish that **nothing was left unwritten because of the superseded one**. The byte count in
§5 is the best available proxy, and it points the wrong way: a dimension that appears once, as a
heading, in nearly 400 kilobytes was not being considered.

---

## 7. WHAT WOULD CLOSE IT

| # | Action |
|---|---|
| 1 | Re-run the **Database Design isolation assignment** with the scope-aware constitution in the brief from the start |
| 2 | Require an explicit **PLATFORM / TENANT / COMPANY** determination per object, so that an omission is visible as an empty cell rather than an absent thought |
| 3 | Re-check the four weakened items against that output |

This round has partially discharged (1): the isolation work was re-run **with** the corrected
constitution in the brief, and produced the cross-tenant reachability finding that the previous
round did not have. **That is itself evidence that the residue was real.**

---

## 8. DISPOSITION

| | |
|---|---|
| Status | **`PARTIALLY RESOLVED`** |
| Findings lost to the superseded reading | **none identified in what was written** |
| Dimension absent from the prior round | **tenancy** |
| Residual | **open**, and it is a gap in coverage, not an error in conclusions |
| Carried to | **P11**, together with the scope matrix |
