# P01 ↔ P05 — WHT RECONCILIATION v2

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Layer: **1.**

---

## 1. PEER DELTA CHECK — NO REPROCESSING

| Peer | Head at this round | Changed since P01 last consumed it? |
|---|---|---|
| P05 | `96748109c1d5` | **Unchanged** since the prior round's intake |

Per the directive, **an unchanged peer SHA is not reprocessed.** The prior reconciliation stands
except where P01's *own* evidence changed — which it did, in two ways.

---

## 2. CLASSIFICATION — UNCHANGED

> ### `BOTH PARTIAL`
>
> **No peer overruled.** P05's rating stands on its own terms; P05 had already retired the
> justification P01 challenged; and two of P01's supporting statements were wrong and were
> corrected by P01, not by P05.

---

## 3. WHAT CHANGED ON THE P01 SIDE THIS ROUND

Two P01-side facts materially weaken P01's half of the original disagreement:

| # | New P01 evidence | Effect on the reconciliation |
|---|---|---|
| 1 | **The deployed withholding module version matches no copy in P01's declared source path set.** The code P01 analysed is not demonstrably the code any deployment runs | **P01's mechanism claims are source-only and unverified in any deployment.** P05's more conservative rating looks better supported, not worse |
| 2 | **The only deployment with real accounting history is application series 16**, and P01 has read **no series-16 source at all** | The withholding subsystem that actually processed transactions has **never been read by P01** |

> **P01's half of this disagreement rests on source it cannot tie to any running system.** That
> is stated plainly rather than left implicit.

---

## 4. THE COMPARISON REQUIRED BY THE DIRECTIVE

| Dimension | P01 | P05 | Status |
|---|---|---|---|
| Mechanism population | two subsystems, plus a third latent | two subsystems (stated in P05's detail sections) | **agreement** |
| Installed modules | the second path installed in none of four databases | not contested | **agreement** |
| Database reality | the deployed code matches no source copy P01 holds | not addressed by P05 | **P01 finding, no conflict** |
| Partial-payment arithmetic | repeated full withholding, linear — **corrected from a withdrawn compounding claim** | not P05's scope | **P01 owns; unverified in deployment** |
| Certificate logic | two shipped copies map to opposite forms; neither observed governing | not P05's scope | **P01 owns; routed to P07** |
| Report logic | tag-engine report unions both sources | — | **P01 corrected itself here** |
| Export logic | **P01 was wrong** — the statutory export joins on a field null on the write-off line | **P05 is the more precise party** | **P05 correct** |

---

## 5. AUTHORITY BOUNDARY — RESTATED

`Peer Position ≠ Peer Decision ≠ Boss Decision`.

- P01 **does not** overrule P05 on the rating.
- P01 **does not** determine which withholding treatment is correct — that is **P07's**, and
  every such question is `HOLD — STATUTORY EVIDENCE REQUIRED`.
- P01 **does not** ask P05 to amend its package. The summary cell P01 originally challenged is a
  summary of material P05 states more fully elsewhere, and **P05 reached the better position
  first**.

---

## 6. WHAT P01 CARRIES FORWARD

| ID | Item | Status |
|---|---|---|
| `W2-01` | The withholding code that deployments actually run has not been located | **HOLD — SOURCE EVIDENCE REQUIRED** |
| `W2-02` | A third withholding engine, latent | **peer-reported, not re-derived** |
| `W2-03` | One subsystem files without certifying; the other certifies without filing | **peer-reported, not re-derived** — owned by neither process |
| `W2-04` | All statutory questions | **HOLD — STATUTORY EVIDENCE REQUIRED — P07** |

**Final classification: `BOTH PARTIAL`, with P01's half now explicitly weaker than when the
disagreement was raised.**
