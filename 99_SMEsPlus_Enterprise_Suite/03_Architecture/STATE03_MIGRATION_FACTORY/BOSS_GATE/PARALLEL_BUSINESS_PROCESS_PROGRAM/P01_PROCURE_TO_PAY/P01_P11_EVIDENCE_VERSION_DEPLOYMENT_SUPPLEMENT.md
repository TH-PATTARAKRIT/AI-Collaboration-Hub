# P01 → P11 — EVIDENCE / VERSION / DEPLOYMENT SUPPLEMENT

> ## SUPPLEMENT TO THE PRIOR P01 HANDOFF — **NOT A REPLACEMENT**

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Branch: `research/account-p01-procure-to-pay-2026-09-04-001`
Layer: **1.** **Material delta only.** The prior handoff stands in full.


> ### ⚠ SUPERSEDED IN PART — `ERR-P01-23`
>
> This document states that **no deployed series-18 database exists** and that P01's source and
> deployment evidence **do not overlap on any series**. **Both are false.** A series-18
> deployment exists on this host with **4 companies, 15,522 journal entries, 47,801 valuation
> layers, and the goods-received clearing account configured**. See
> `P01_SERIES18_DEPLOYMENT_DISCOVERY.md`. **No accounting finding is withdrawn** — each remains
> bound to the database it was measured in.

---

## 1. DATABASE IDENTITY REPAIR

| Item | Delta |
|---|---|
| Archives → identities | **CORRECTED (`ERR-P01-22`): 10 artefacts = 5 distinct database identities**, keyed on uuid. The two 44-company archives are **different databases** sharing a clone lineage — agreement inherited, not independent. Earliest artefact **2026-03-30** |
| Distinct companies | **WITHDRAWN** — computed from the wrong identity model. Any aggregated company figure must state the identity it counts |
| The excluded archive | **Readable.** Root cause: it was dumped by a newer database engine and carries an archive format the invoked restore binary predates. A capable binary was already installed |
| Independent corroboration | **Two archives of one estate are not two witnesses** |

## 2. VERSION MISMATCH

| Item | Delta |
|---|---|
| Application series | one deployment at **16.0**, two at **19.0** |
| **Series 18** | **no deployment anywhere in the estate** — yet it is the series P01 analysed in source |
| Series-16 **custom** source | **found** — outside the original path set; six of six module versions match the deployment |
| Series-16 **core** source | **`VERIFIED ABSENCE`** — 13 core trees on the volume, 9 at series 18, 4 at series 19, **0 at series 14–17**; all nine unextracted archives are 18 or 19 |
| Classification | `SOURCE/DB VERSION MISMATCH` + `MODULE VERSION MISMATCH`; **root cause is an analyst-side labelling error, not an artifact defect** |
| **Challenge status** | **UNCHALLENGED** — the disproof layer for version identity did not return (`AASV-P01-04`) |

## 3. FALSIFIED PRIOR FINDINGS

Three claims **false**, one count wrong, plus two self-characterisations corrected:
three-way match, subcontracting and requisition were each reported *"installed nowhere"* and are
**installed** in the excluded deployment · *"47 of 65 source-only"* → **28 of 65** ·
*"most relevant database"* → three axes, not one · *"two v19 deployments"* → **two different databases in a clone lineage** (`ERR-P01-22`).

## 4. THE HEADLINE CAUSE WAS WRONG — CONCLUSION SURVIVES

| | Published | Corrected |
|---|---|---|
| Cause | *"no valuation account resolves"* — 0 of 37 | **false zero.** Company-dependent values also resolve from a company-level defaults table: **44 rows, 43 with a real account** |
| Actual cause | — | **the company stock journal is unset on 44 of 44** — and the entry-creation path takes its journal from exactly there |
| **Remediation implied** | configure category accounts *(already configured — would achieve nothing)* | **configure the company stock journal** |
| Other v19 deployment | — | **its journal IS configured** — so the absence there is a usage fact |

## 5. LANDED COST — DEPLOYMENT REALITY

Installed in **all four archives**, exercised in **none**. 43 of 44 companies cannot compute an
adjustment — **but the one that can is the only one that transacts, and the operating deployment
is fully configured.** Read as *"the business cannot use it"*, **CONTRADICTED**.
**The real finding: it is unexercised in the operating deployment against a 103,949-movement
denominator, with every prerequisite satisfied.**

## 6. SUBCONTRACT — DEPLOYMENT REALITY

Estate-wide "zero" merged **undefined** (three deployments lack the columns) with a **measured
zero** (one deployment: 0 of 163 orders). That deployment holds **one subcontract bill of
materials with a subcontractor assigned** — so *"not configured"* is contradicted. The
ten-module population **is not the same ten across series**.

## 7. PERIOD LOCK

`MIXED — PATH-DEPENDENT` **and** `VERSION-DEPENDENT`; operative behaviour on every P01 path is
**`SOFT RE-DATE`**. **The hard lock re-dates too** — verified. **A purchase document can never be
refused by any lock configuration.** Landed cost splits document from entry across the boundary;
one reconciliation path catches the refusal and continues; a third rule relocates to *today*.
**No lock has ever been exercised anywhere.**

## 8. BILL CORRECTION AND LINEAGE

`MIXED`. Two of seven paths preserve history. The audit record **cannot distinguish a deletion
from a destroy-and-recreate**; **unlogged destructions outnumber logged ones 3:2**; posted
document numbers were **overwritten** on cancel. Every protective guard is **off in every
deployment**. **Business-semantic lineage does not survive** — and the model's links are
`ON DELETE SET NULL` in both deployed series, so the gap predates any correction.

## 9. FINANCIAL COMPANY OWNERSHIP

`INFERRED ONLY`. **533 of 563 posted journal items sit in a company that does not own the account
they post to.** One ordinary, active, non-superuser account is a member of **28 of 44
companies** — no privilege trick needed. The declared guard is **inert**; the company-consistency
guard **executes and is vacuous**. **Zero auto-generated documents exist** — real and unrealised.

## 10. WHT — CORRECTED, AND STRENGTHENED

`REPEATED FULL-BASE WITHHOLDING`, linear. **Now verified in the code the operating deployment
actually runs.** 100,000 at 3% in two halves → **6,000 against a 3,000 liability**; the bill
**closes**, so the vendor is permanently under-paid. The **compounding** mechanism is
`VERSION-INAPPLICABLE` — **absent from the deployed body entirely**.

## 11. PND

Conflict confirmed; deployed owner identified. *"The operator picks the form"* is **BROKEN for the
later series** — three automatic couplings agree. **The statutory export reads neither mapping.**
**All statutory questions → P07.**

## 12. PEER DELTAS

| Peer | Delta |
|---|---|
| **P02** | **The cross-company bill trigger is a customer invoice — a P02 object.** P01's prior attribution was wrong |
| **P03** | Delta correction issued: the subcontract cost premise holds for series 18 and **not** for series 19 |
| **P05** | Vendor advance owned by P01, traced, and a defect found — **the deduction control is inert**. WHT remains `BOTH PARTIAL`, P01's half now weaker |
| **P06** | Caveat **activated**; **no conflicts found**; P06's pattern commended |
| **P07** | WHT arithmetic, the PND conflict, the export finding, the tax-period divergence, two impossible bill dates |
| **P08** | Period-lock re-dating incl. the hard lock; correction and lineage; overwritten document numbers |

## 13. `DEP-P01-06`

`PARTIALLY RESOLVED`. Residue is **unwritten-observation risk**; the word *tenant* appears once
in 384,836 bytes of prior expert output. Shrunk twice by re-running assignments under the
corrected constitution; **three of four original assignments remain un-rerun**.

## 14. `EC-06`

**NOT SATISFIED — METHOD**, and re-diagnosed. The criterion requires the boundary to be
**declared *and proven***; P01 had been proving only the declaration. Two of four boundary proofs
closed this round; **a new false zero was found**.

## 15. OPEN CONTRADICTIONS

**17 open — 4 CRITICAL, 8 HIGH, 5 MEDIUM. 1 closed** — the first closure in P01's history, and it
closed by repairing a boundary, not by reinterpreting a finding.

---

## 16. WHAT P11 SHOULD DO WITH THIS

1. **Do not treat P01's source findings as validated anywhere.** The analysed series has no
   deployment; the deployment with history has no core source.
2. **Re-derive the three highest-consequence expert findings before relying on them** — the
   533-of-563 divergence, the unlogged destructions, and the statutory-export route.
3. **Seven of seventeen contradictions fall to one read-only runtime session.** That is the
   highest-leverage action available to the programme and has never been performed.
4. **Correct the P02 attribution** in any cross-process matrix that inherited P01's error.
5. Note `AASV-P01-04`: **this round's own central repair is unchallenged.**

---

# §17 — LATE MATERIAL DELTA: A SERIES-18 DEPLOYMENT EXISTS (`ERR-P01-23`)

Received after this supplement was first published, from the challenge layer that had not
returned. **Verified independently before acceptance.**

| Item | Delta |
|---|---|
| Series-18 deployment | **EXISTS.** 361/361 modules at series 18 · **4 companies** · **15,522 journal entries** · **47,801 valuation layers** · custom purchase-request module installed |
| **The clearing bridge** | **CONFIGURED** — goods-received clearing account on 15 item categories, valuation account likewise, **valuation journal on all four companies** |
| Valuation policy there | **`manual_periodic`** — which is why 0 of 47,801 layers carry a journal link. **A policy operating correctly, not the series-19 configuration gap** |
| Artefact population | **19 archives, ≥9 distinct database names** — P01 had enumerated one directory |
| Governing claim of §1–§16 | *"source and deployment do not overlap on any series"* is **FALSE** |
| Exit criteria | **`EC-01` falls back to NOT SATISFIED; 7 of 8 not satisfied — no improvement over the prior round** |

**What P11 should do:** treat P01's series-18 source findings as **testable against real deployed
data on this host**, and not as unvalidatable. That is a better position than this supplement
originally described — and it is **untested work**, not a result.

**No accounting finding is withdrawn.** Each remains bound to the database it was measured in.
