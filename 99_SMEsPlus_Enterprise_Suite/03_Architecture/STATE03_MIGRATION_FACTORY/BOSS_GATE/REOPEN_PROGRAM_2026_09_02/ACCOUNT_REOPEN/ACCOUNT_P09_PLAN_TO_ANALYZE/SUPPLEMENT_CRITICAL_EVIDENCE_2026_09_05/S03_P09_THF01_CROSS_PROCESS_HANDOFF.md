# S03 — P09_THF01_CROSS_PROCESS_HANDOFF

**Checkpoint:** `CP-P09S03` · **Layer:** 1 — clean-room.

---

## 1. THE OWNERSHIP SPLIT

TH-F-01 is **not a P09 finding**. P09 discovered it and owns exactly one part of it.

| Part | Owner | P09's position |
|---|---|---|
| whether an account named as accumulated depreciation may be typed as a depreciation **expense** | **P08 — Record-to-Report** | P09 evidences the internal contradiction and **makes no ruling on canonical account-type semantics** |
| whether that typing is a **Thai statutory** misclassification, and how Thai statute requires accumulated depreciation to be presented | **P07 — TH Tax Compliance** | **`HOLD — STATUTORY EVIDENCE REQUIRED`. P09 makes no statutory claim of any kind** |
| whether an asset may be mapped to such an account, and what the asset module should do about it | **P04 — Acquire-to-Retire** | P09 supplies the mapping evidence and the deployed census |
| **the management-accounting consequence** — that a balance-sheet-typed leg admitted to a consumption gate destroys the attribution | **P09** | **owned and stated** |
| canonical reconciliation across all four | **P11** | supplied as material delta |

## 2. WHAT EACH PROCESS RECEIVES

### → P08 (last consumed `4bdf8a2`)
- the shipped template types two accounts named as accumulated depreciation, on asset-range codes, as a depreciation-**expense** type, and the same file ships **no** fixed-asset-typed account — **FACT VERIFIED**, 28-line file read in full;
- the consumption gate matches on the **first token** of the type, so a depreciation-expense type resolves to expense and is admitted;
- **the question P08 owns:** is the first-token match a correct reading of account-type semantics, or does it conflate a *statement* classification with a *nature* classification?
- **P09 does not redefine Core Ledger truth and offers no answer.**

### → P07 (last consumed `9a99c01`)
- the template facts above, as evidence only;
- **every statutory reading is `HOLD — STATUTORY EVIDENCE REQUIRED`**, including whether the typing is a misclassification at all;
- **the deployed correction:** the one Thai-market deployment measured does **not** use those template accounts — its accumulated-depreciation accounts are correctly typed balance-sheet. **P09's prior claim that budget consumption zeroes on a Thai-chart install is withdrawn**, and P07 should not inherit it;
- all Thai names remain **candidate / UNVALIDATED**.

### → P04 (last consumed `6953856`)
- the deployed asset census: **781 assets across 5 databases, 670 allocated, all in one deployment**;
- in that deployment, accumulated-depreciation accounts are typed as fixed assets on **671** assets and as current assets on **13**;
- **the configuration trap:** a configurer following the shipped template has **no correctly-typed fixed-asset account available** for the balance-sheet leg;
- P09 confirms P04's original depreciation finding in full and adds the measured annihilation.

### → P11
- the corrected classification, the retraction, and the ownership split — as material delta only. **Prior P09 evidence is not replaced.**

## 3. THE ROUTING FAILURE THIS CORRECTS

The prior round produced a high-severity Thai finding and **routed it to no named process**. That was found by review, not by the author. This supplement adds a standing check: **every finding is tested for a localization or statutory implication before the package closes, and any such implication is routed and marked HOLD.**

**CONTRADICTED after publication — see `S23` §4.** This paragraph claimed a *complete* list of four routed items. An independent sweep of all 65 package files found **14**, of which **5 remain unrouted** — including the Thai statutory constraint on **cross-company management reporting**, which couples directly to the re-opened scope row. **A completeness claim over an author-chosen set, made inside the document written to correct exactly that failure.** The 14-item list and its routing are in `S23` and must be worked from instead.

## CHECKPOINT

**`CP-P09S03` — COMPLETE — EVIDENCE VERIFIED.** Four peer routings issued, four statutory items held. Auto-continue.
