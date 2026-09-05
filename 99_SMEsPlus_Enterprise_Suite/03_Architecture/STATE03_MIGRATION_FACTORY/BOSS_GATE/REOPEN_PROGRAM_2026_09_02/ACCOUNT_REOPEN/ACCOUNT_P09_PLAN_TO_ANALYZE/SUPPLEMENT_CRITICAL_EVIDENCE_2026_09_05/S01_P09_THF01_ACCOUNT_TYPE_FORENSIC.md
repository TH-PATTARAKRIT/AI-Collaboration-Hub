# S01 — P09_THF01_ACCOUNT_TYPE_FORENSIC

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · supplement `SMEPLUS-26-09-05-…-CRITICAL-EVIDENCE-SUPPLEMENT-001`
**Checkpoint:** `CP-P09S01` · **Layer:** 1 — clean-room.
**Baseline verified:** `70f8d20253fe3095152336fc76a3293e72b5d5b9`, head = remote, tree clean.

---

## 1. THE HEADLINE — MY OWN PRIOR CLAIM IS CONTRADICTED

The previous round's final report stated:

> *"the Thai chart types both accumulated-depreciation accounts as a depreciation-expense type on asset-range codes and ships no fixed-asset account, so the budget query admits the balance-sheet leg and **budget consumption nets to zero on a Thai-chart install**."*

**That generalisation is CONTRADICTED by the deployed data.** The template mistyping is real; the deployed consequence is not. The two were conflated, and the conflation was mine.

## 2. WHAT IS TRUE — THE TEMPLATE

The shipped Thai account template is a 28-line file. Read in full, no truncation.

| Fact | Status |
|---|---|
| two rows are named as accumulated depreciation, on **asset-range codes**, typed as a **depreciation-expense** type | **FACT VERIFIED** |
| every other row in the file conforms to its own code-block convention (1=asset, 2=liability, 3=equity, 4=income, 5=expense) | **FACT VERIFIED** |
| the file contains **no fixed-asset-typed account at all** — exhaustive match on the type token returned 0 | **FACT VERIFIED**, class A, whole file |
| the budget query's account-type gate splits the type on its first token, so a depreciation-expense type resolves to **expense** and is admitted | **FACT VERIFIED** |

**So the template, if used as-is to configure an asset, would admit the balance-sheet leg into budget consumption.** That much of the prior finding stands.

## 3. WHAT IS NOT TRUE — THE DEPLOYED CHART

Measured directly against the deployed database, exhaustively:

| Measurement | Result |
|---|---|
| account records in the deployed chart | **339** |
| accounts on the Thai template's code range (141x / 142x) | **ZERO** |
| accounts named as accumulated depreciation | **10** — all coded 1232xxx |
| their account type | **`asset_fixed` — all ten. Correctly balance-sheet.** |
| accounts typed as depreciation-expense | **13** — all coded 71xxxxx / 72xxxxx, all named as depreciation expense. Correctly profit-and-loss |
| accumulated-depreciation accounts actually referenced by assets | `asset_fixed` on **671** assets, `asset_current` on **13** |
| depreciation-expense accounts actually referenced by assets | depreciation-expense type on **671**, plain expense on **13** |
| fixed-asset accounts referenced by assets | `asset_fixed` on **672**, `asset_current` on **13** |

**The deployment does not use the shipped Thai template.** It uses a custom chart in which the accumulated-depreciation accounts are correctly typed as balance-sheet assets.

## 4. TH-F-01 — CORRECTED CLASSIFICATION

| Aspect | Classification |
|---|---|
| the template mistypes accumulated depreciation | **FACT VERIFIED** |
| the template ships no fixed-asset account | **FACT VERIFIED** |
| a deployment configured from that template would admit the balance-sheet leg to budget consumption | **SUPPORTED INTERPRETATION** — the arithmetic follows, but no such deployment has been observed |
| **budget consumption nets to zero on a Thai-chart install** | **CONTRADICTED** as a general statement. Not observed in the one Thai-market deployment for which data exists |
| **TH-F-01 overall** | **VERIFIED TEMPLATE-LEVEL LATENT RISK — NOT OBSERVED DEPLOYED BEHAVIOUR** |

## 5. THE ROLE TABLE THE DIRECTIVE REQUIRES

Per the instruction not to infer role from name alone — every column below is read from the record, not from the label.

| Role | Deployed code range | Deployed type | Financial-statement role | Analytic eligibility | Budget eligibility |
|---|---|---|---|---|---|
| fixed asset | 1232xxx and others | `asset_fixed` | balance sheet | eligible (no type test on creation) | **excluded** by the type gate |
| accumulated depreciation | 1232xxx | `asset_fixed` | balance sheet (contra) | eligible | **excluded** by the type gate |
| depreciation expense | 71xxxxx / 72xxxxx | depreciation-expense | profit and loss | eligible | **admitted** |
| *(template)* accumulated depreciation | 141x / 142x | **depreciation-expense** | **asserts profit and loss; named as balance sheet** | eligible | **would be admitted** |

**The contradiction is internal to the template file and does not reach this deployment.**

## 6. WHY I GOT IT WRONG, STATED PLAINLY

I read a 28-line template file, verified the mistyping correctly, and then **asserted a deployed consequence without querying the deployment I already had open.** The asset and analytic tables from that same database were extracted in the previous round; the account table was three commands away and I did not run them.

This is the **same defect class as the previous round's truncation failure**, one level up: a correct local observation promoted to a population claim without measuring the population. The prior round's failure was a `head`; this one was an inference.

**Standing rule added:** a finding about a *template* is a claim about **configuration capability**, never about **deployed behaviour**, unless the deployment is measured.

## 7. WHAT SURVIVES, AND IT MATTERS

TH-F-01 remains a real finding, correctly scoped:

- **any deployment that configures an asset against the shipped Thai template's accumulated-depreciation accounts loses that asset's depreciation from budget consumption**, silently;
- the template contains **no** correctly-typed fixed-asset account, so a configurer following it has **no correct option** for the balance-sheet leg;
- this is a **configuration trap**, not a code defect, and it is exactly the kind that survives testing because the arithmetic is correct at every step.

**Severity is reduced from CRITICAL-DEPLOYED to HIGH-LATENT. It is not withdrawn.**

## 8. OWNERSHIP — P09 DOES NOT OWN THIS

P09 owns only the management-accounting consequence. See `S03`. The account-type classification belongs to P08, the Thai statutory question to P07, the asset mapping to P04. **P09 makes no statutory claim: whether the typing is a statutory misclassification, as distinct from an internal inconsistency, is `HOLD — STATUTORY EVIDENCE REQUIRED`.**

## CHECKPOINT

**`CP-P09S01` — COMPLETE — EVIDENCE VERIFIED.** TH-F-01 re-derived from source and deployment; prior claim corrected; ownership routed. Auto-continue to `CP-P09S02`.
