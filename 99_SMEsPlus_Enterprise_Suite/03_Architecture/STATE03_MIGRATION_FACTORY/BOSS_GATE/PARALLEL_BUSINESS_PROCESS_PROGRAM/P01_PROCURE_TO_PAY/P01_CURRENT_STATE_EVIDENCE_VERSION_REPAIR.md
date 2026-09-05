# P01 — CURRENT STATE: EVIDENCE / VERSION REPAIR

Session: P01 — Procure-to-Pay (one continuing session, four prompts)
Prompt: `SMEPLUS-26-09-05-ACC-P01-P2P-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Execution: **SUPPLEMENTAL TARGETED CONTINUATION — NO RESET.**
Layer: **1.**

---

## 1. BASELINE VERIFIED

| Item | Value |
|---|---|
| Branch | `research/account-p01-procure-to-pay-2026-09-04-001` |
| Claimed baseline | `49d0fe3490f6b2c1c3773d2a53d24394a1ef5950` |
| **Verified** | **present, is a commit, equals local HEAD, equals remote HEAD** — 48 package files |

---

## 2. WHAT THIS ROUND REPAIRED

| # | Repair | Effect |
|---|---|---|
| 1 | **The excluded archive's root cause proven** | It was dumped by a newer database engine (PostgreSQL 18.4, archive format 1.16) than the restore binary invoked (16.15). A capable binary (18.6) was already installed at a sibling path. **A tool-version mismatch, not an unreadable artifact** |
| 2 | **Version identity established from evidence, not inference** | Nine facets separated per deployment. Application series read from the deployed module registry, never inferred from feature presence |
| 3 | **Two archives found to be one deployment** | Identical 44-company identifier sets, same creation-date span. **Three distinct deployments in four archives.** Distinct companies: **46**, not 90 |
| 4 | **"Most relevant database" corrected** | Highest module coverage (453), **10 journal entries in total**. Decisive for *what is installed*, near-useless for *what happens* |
| 5 | **The missing source root found and searched** | A series-16 custom root exists on the volume, was never in the declared path set, and **is the source of the series-16 deployment's custom layer** — six of six module versions match |
| 6 | **The withholding code that actually ran located and read in full** | Closes the prior round's *"no deployment runs this code"* gap |

---

## 3. THE STRUCTURAL FINDING THAT GOVERNS EVERYTHING

> **P01's source analysis and P01's deployment evidence do not overlap on any application
> series.**

| | Series 16 | Series 18 | Series 19 |
|---|---|---|---|
| Source in the original declared path set | **no** | yes (primary) | yes |
| Deployment in the estate | **yes — the only one with real accounting history** | **none** | yes, but 26 journal entries across two |

The clearing-bridge account of procure-to-pay — three rounds of work — is **series-18 source with
no deployed representative anywhere**. The only deployment with 183,590 journal entries is
series 16, for which P01 had read no source until this round.

**This round narrowed the gap** by locating the series-16 **custom** root. The series-16 **core**
remains unread.

---

## 4. WHAT CHANGED IN P01's CONCLUSIONS

| Prior conclusion | Status now |
|---|---|
| Three-way match / subcontracting / requisition *"installed nowhere"* | **FALSE — all installed** in the excluded deployment. Corrected in round 3, root-caused here |
| *"The deployed withholding code matches no copy in the path set"* | **RESOLVED** — the path set was incomplete; the code is now located and read |
| Withholding compounds | **remains withdrawn**; and the deployed series-16 code **has no such term at all** — a stronger disproof |
| Withholding repeats the full base, linearly | **STRENGTHENED — now verified in the deployed source**, not just in a copy nobody runs |
| *"D1 and D2 both show X"* | **not two witnesses** — one estate observed twice |
| Vendor advance ownership accepted | **traced, and a defect found**: the deduction control is inert |

**No verified fact was withdrawn this round. Two were strengthened, three were re-scoped, and two
evidence-base defects were repaired.**

---

## 5. WHAT DID NOT CHANGE

- All prior evidence, contradictions, error records, dissent, AAS+ hold positions and the PMO
  recommendation are **preserved**.
- Nothing was executed. **No runtime evidence exists in any P01 round.**
- No statutory claim is made anywhere; all are routed to P07.
- No target-architecture or Boss-level decision is made.

---

## 6. PUBLICATION

Prior round published successfully after a push that had been refused a round earlier **with no
change by the executor**. Both stale blockers — the refused push and the "unreadable" archive —
are retired in `P01_TRANSIENT_PERMISSION_BLOCKER_REGISTER.md`.
