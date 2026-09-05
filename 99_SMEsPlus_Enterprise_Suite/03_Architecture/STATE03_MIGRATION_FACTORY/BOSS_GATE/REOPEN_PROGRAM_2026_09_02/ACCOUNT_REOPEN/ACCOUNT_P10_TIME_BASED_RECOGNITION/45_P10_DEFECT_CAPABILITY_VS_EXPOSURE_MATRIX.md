# P10 — DEFECT CAPABILITY vs EXPOSURE MATRIX

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D08`.

The prior package used the phrase *"live exposure"* for what was only **capability**. This matrix separates the four states the directive requires and forbids the conflation that produced the error.

---

## 1. The Four States, Defined

| State | Definition | What proves it |
|-------|-----------|----------------|
| **CODE CAPABILITY PRESENT** | The behaviour exists in the software | Source, and better, an executed test |
| **CONFIGURATION REACHABLE** | The deployed configuration makes the path executable | Configuration data in the deployed database |
| **DEPLOYMENT EXPOSED** | Real records exist that the path can act on | Record populations in the deployed database |
| **OBSERVED EXECUTION** | The path has demonstrably run | Records bearing its signature |

**A claim at one level is not evidence at any other.** Capability without reachability is dormant. Reachability without records is unexposed. Exposure without observation is untested.

## 2. The Lock-Triggered Re-Date Defect

| DB | Code capability | Configuration reachable | Deployment exposed | Observed execution | Classification |
|----|-----------------|------------------------|--------------------|--------------------|----------------|
| A | **PRESENT** | **NO** — no lock on any of 44 companies | no | no | **NOT REACHABLE** |
| B | **PRESENT** | **NO** — no lock on any of 44 | no | no | **NOT REACHABLE** |
| C | **PRESENT** in the posting layer; the deferral mechanism is **absent** | **NO** — no lock is set. **Corrected `67` §6:** three lock columns **do** exist here | **the only database with real records: 669 assets, 30,038 asset-linked entries** | **3 candidate signatures, cause undetermined — `UNRESOLVED`** | **NOT REACHABLE** on the lock path; see `52` |
| D | **PRESENT** | **YES** — four locks set on its single company | **NO** — 10 journal entries, none a recognition entry, **and no assets, only templates** | no | **CURRENTLY DORMANT** |

**Estate position: capability present in four of four; configuration reachable in one of four; deployment exposed in none *on the lock path*; observed execution in none.**

> **Qualified after `P10-R-13`.** The only database holding real records has **no lock**, so it is not reachable on the lock path — but it does hold **3 entries carrying the signature a re-date would leave**, in 30,032. That signature is also produced by a legitimate catch-up stub. `UNRESOLVED — EVIDENCE REQUIRED`, and it is the strongest reason not to treat "observed execution: none" as settled.

## 3. The Lock-Free Mutation Path

The peer's second path fires on an upstream document-date edit **with no lock configured**.

| DB | Code capability | Configuration reachable | Deployment exposed | Observed | Classification |
|----|-----------------|------------------------|--------------------|----------|----------------|
| A | **PRESENT** | **YES — trivially. No configuration is required** | **UNKNOWN** — not enumerated | **UNKNOWN** | **UNKNOWN — EVIDENCE REQUIRED** |
| B | **PRESENT** | **YES** | UNKNOWN | UNKNOWN | **UNKNOWN — EVIDENCE REQUIRED** |
| C | **PRESENT** | **YES** | UNKNOWN | UNKNOWN | **UNKNOWN — EVIDENCE REQUIRED** |
| D | **PRESENT** | **YES** | 10 entries only | no | CURRENTLY DORMANT |

> **This is the finding that matters, and it inverts the priority the prior package set.**
>
> The path P10 spent two rounds on is **not reachable in 3 of 4 deployed databases and dormant in the fourth**. The path P10 has never enumerated is **reachable in all four, because it requires no configuration at all**, and its exposure is **unknown**.

## 4. Consequence for the Decision

The Boss is not choosing how to remediate a live misstatement. On the lock path there is nothing live to remediate. On the lock-free path nobody knows.

This makes the disruptive options **cheaper** than the prior package implied, and it makes the **trace-based** options more important than the **refusal-based** ones — which is independently what the peer's refined close condition concluded, by a different route.

## 5. Prohibited Phrasing — P10-internal, and proposed for programme adoption

> **Within P10**, the phrase **"live exposure"** may not be used unless **DEPLOYMENT EXPOSED** is evidenced. P10 **proposes** the same for the programme; adopting it is a PMO matter, not P10's. Capability is not exposure. Configuration is not exposure. A defect that cannot fire in a deployment is **NOT REACHABLE** there, and saying otherwise misstates the risk to the person deciding.

## 6. Classification

| Statement | Class |
|-----------|-------|
| Capability present in all four | **FACT VERIFIED** |
| Configuration reachable in one of four | **FACT VERIFIED** |
| Deployment exposed in none | **FACT VERIFIED** for the lock path |
| Lock-free path reachable in all four | **SUPPORTED INTERPRETATION** — it follows from requiring no configuration; P10 has not enumerated its call sites |
| Lock-free path exposure | **UNRESOLVED — EVIDENCE REQUIRED** |

---

## 7. The Prohibited-Phrasing Rule Applies Symmetrically — `67` §8

The rule in §5 forbids claiming exposure without evidence. **It was not applied to the negative claim.**

> *"No lock exists in the estate"* is a statement about **four database images dated between 2026-07-11 and 2026-08-03**.

A snapshot dated **2026-08-26** — newer than anything P10 read — exists on this host. Reading it was **refused by this session's permission controls, and no attempt was made to work around that.** The negative claim does not reach it.

**Corrected form:** *no lock is set in any of the four images examined, which are between two and eight weeks old; a newer image exists and was not readable.*

## 8. And the Population Beneath the Matrix Is a Floor

Every row of this matrix describes one of **four** databases selected from a declared population that a host-wide search shows holds **at least ten**. The matrix is correct about the four. It is **not** a statement about the estate, and the earlier phrasing implied it was.
