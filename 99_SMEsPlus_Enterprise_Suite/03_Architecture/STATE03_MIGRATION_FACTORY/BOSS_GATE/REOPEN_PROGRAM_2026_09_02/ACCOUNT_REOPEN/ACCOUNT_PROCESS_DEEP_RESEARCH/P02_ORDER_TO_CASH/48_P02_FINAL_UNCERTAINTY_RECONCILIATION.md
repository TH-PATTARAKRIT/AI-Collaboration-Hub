# 48 — P02 FINAL UNCERTAINTY RECONCILIATION

*(mandated semantic name `34_P02_FINAL_UNCERTAINTY_RECONCILIATION.md`; 34 taken, next free number used per §15.)*

`LAYER 2 — AUDIT QUARANTINE.` **CP-06 / CP-10.** Baseline `aca211e`.

The round existed to close three uncertainty classes. **Two are materially narrowed; one is split, with
half closed and half re-opened wider than it was.**

---

## 1. Uncertainty Class 1 — Evidence Identity

| | |
|---|---|
| **Before** | `C-44`/`C-48`/`C-49`: `database.uuid` over-counts and under-counts; artefact ≠ database; no lineage key existed |
| **Now** | A **seven-level model**, keyed on **content ancestry** with a mandatory negative control |
| **Status** | **NARROWED — the model is now falsifiable, and has been falsified twice and repaired** |

**Levels:** `ARTEFACT` · `SNAPSHOT` · `DATABASE UUID` (observed attribute) · `DATABASE LINEAGE` ·
`DEPLOYMENT INSTANCE` · `BUSINESS ENTITY` · **`COMPANY SCOPE`** (added by `C-71`).

**Two keys were proposed and both failed:**
1. birth metadata alone → **false merges** (`iSMEs`/`iMSCG` share a birth timestamp to the microsecond);
2. + founding-company identity → **false split** on `pfp-main`/`pfp-staging` (`C-63`).

**Canonical key (third form):** ≥N rows sharing `(table, id, create_date)` **and** the latest such
`create_date` ≥1 day after database birth, corroborated in ≥2 tables from different modules, validated
against a declared negative-control pair. **`database.uuid`, founding-company name and birth metadata
are all `OBSERVED ATTRIBUTE`.** Free discriminators newly identified: **uuid version** (v1 = written by
the codebase; v4 = platform replacement) and **uuid1 node + embedded timestamp**.

**Residual:** whether the third key survives a fourth test. **It has not been run on the 13 groups it
was not derived from.**

## 2. Uncertainty Class 2 — Population Denominator

| unit | value | basis |
|---|---|---|
| **ARTEFACT PATHS** | **40** | content-led + structure-led discovery |
| **DISTINCT CONTENTS** | **28** accessible (≤32 with the blocked four) | one file occupies 9 paths |
| **SNAPSHOTS** | **17** | distinct `(birth, write, company-count)` tuples — *the published ≥24 was underived and is withdrawn* |
| **LINEAGES** | **14** | content ancestry |
| **LIVE DEPLOYMENT INSTANCES** | **≥9** | `docker` at time of measurement; **not re-derivable now** |

**Status: BOUNDED, NOT CLOSED.** Coverage: **116,977 of 193,222 content-tested (60.5%)**; **76,245 not
tested**, including **807 above the size floor**; **24,258 read failures**. Declared-open shapes: gzipped
tar, nested archives, non-`dump.sql` SQL members, 7z/rar/xz/zstd, encrypted, sparse bundles, VM images,
Time Machine, and 9 stopped container volumes.

**`C-86` improves this class materially:** the reference distributions for six generations exist and are
readable, so the **source** side of the population is far better than published.

## 3. Uncertainty Class 3 — `C-04` Runtime Boundary

**SPLIT. Half closed, half re-opened wider.**

| | |
|---|---|
| **`C-04a`** — is the generator idempotent? | **CLOSED at FUNCTION level: no.** Not independently closed at system level (`C-80`) — `_post` refuses a posted move, so a second pair requires the move **still in draft**, which is the `C-04b` precondition. Under `BP-02` this concerns a mechanism the target does not adopt: it is a **design requirement input** — *the delivery-triggered cost generator must carry an explicit idempotency key* — not a risk carried against the target. `cogs_origin_id` is **written and never read as a guard**. |
| **`C-04b`** — is repeat execution reachable? | **OPEN, and WIDER.** The precondition is present in **11 of 11 deployments**, not 4 (`C-82`) — `account`'s own validate wizard is a soft-mode poster with `force_post` defaulting False. The mechanism has still **never executed** anywhere. |
| **Authorisation** | **PACK WITHDRAWN (`C-74`).** It forbade companies 2–5 and named a script writing to company 2. **Nothing was executed.** Four fixes required before resubmission (`47` §5.6). |

## 4. Business-Scenario Delta (CP-06)

Only scenarios materially affected by the new identity/population/code evidence are restated.

| # | Scenario | Delta this round |
|---|---|---|
| 1, 3, 4 | Drop-shipping · FX · Bill-and-hold | **Narrowed to standard code.** Source-derived halves now carry the unreadable-module bound. |
| 2 | Credit control | **Reinforced, denominator corrected.** The 19.0 partner aggregate spans what is **two** lineages; recount required. |
| 5, 6 | Outbound consignment · Warranty provision | **Materially narrowed (`C-62`)** — restated *"not representable / not found **in standard v18/v19**"*, with unreadable-module counts attached. |
| 7 | Freight | **Over-claim withdrawn (`C-61`)** — module-level, not deployment-level. |
| 8 | Lot/serial COGS | **Quantified (`C-60`)** — **non-empty as master data, empty as transactions**: 984 journal lines across the three carriers = **0.199%**. `P02 RETAINS`. |

**`C-86` reduces the unreadable-module bound on all of them** (620 → 540 non-standard rows).

## 5. Every Remaining Uncertainty, Named And Owned

| # | Uncertainty | Class | Owner |
|---|---|---|---|
| U-1 | `C-04b` reachability | **BOSS AUTHORISATION** — pack must be re-submitted per `47` §5.6 | Boss |
| U-2 | 76,245 candidates untested; 807 above the floor | EVIDENCE REQUIRED | P02 |
| U-3 | Content hashes; per-module versions | EVIDENCE REQUIRED | P02 |
| U-4 | The third lineage key untested on 13 groups | EVIDENCE REQUIRED | P02 |
| U-5 | Containerised databases in or out of the population | **DECISION REQUIRED, in writing** | P02 → P11 |
| U-6 | Thai branch identity (9 NULLs, duplicate `00009`) | **STATUTORY** | **P07** |
| U-7 | `odoo_cff` has neither source basis nor behavioural marker | PEER — affects every process on it | **P08 / P09 / P11** |
| U-8 | 9 stopped container volumes | EVIDENCE REQUIRED | **P06 / P11** |
| U-9 | Revenue: billing vs performance | **BOSS DECISION** (`BP-03`) | Boss |
| U-10 | Three scope holds | PEER | **P11** |

**No unnamed `OPEN` remains.**

## 6. P11 / G02 Handoff

**G02-P10 may receive a controlled handoff**, with these conditions attached in writing:
the cut-off figures carry the `C-34` draft-basis caveat and are floors for 7 of 8 databases; the
delivered-not-invoiced direction is **withdrawn for `iSMEs`**; and every population figure must be
quoted **by unit** (`48` §2), never as a single number.

**P11 receives:** the seven-level identity model and its content-ancestry key; `U-5`, `U-7`, `U-10`; the
six design candidates (`DC-38-01` … `06`); and the record that `BP-02` remains unsatisfiable by
configuration on the target generation.

## 7. Terminality Audit (§17)

| Check | Result |
|---|---|
| Load-bearing background tasks | **0 running.** All shell tasks and all four expert agents completed or were dispositioned |
| Remote contains the final evidence | verified per commit |
| Remote HEAD = intended local commit | verified |
| Required deliverable only local | none |
| Unresolved task hidden behind prose | none — §5 names all ten |
| Every HOLD has an owner | yes — §5 |
| P10 / P06 started automatically | **no** |
| Any write or mutation | **none** |

---

## TERMINAL STATE — round `SMEPLUS-26-09-05-G02-P02-O2C-FINAL-UNCERTAINTY-CLOSURE-003`

**`G02-P02 MAXIMUM AVAILABLE EVIDENCE REACHED — HOLD FOR NAMED DEPENDENCY`**

**Terminal A was considered and rejected.** It requires that the evidence-identity and population method
is *"no longer itself an unresolved blocker"*. It still is: the content-ancestry key has **not** been run
on the 13 groups it was not derived from, and **only 60.5% of candidates were content-tested**.

**Terminal C was considered and rejected.** The method's contradictions were **all caught and corrected
within the round**, and every substantive accounting finding **reproduced on an independent instrument**.
Reliance on the findings is possible with the bounds stated; the package is not in integrity failure.

### Named dependencies

| # | Dependency | Owner |
|---|---|---|
| 1 | **`C-04b`** — the authorisation pack is **WITHDRAWN** (`C-74`) and must be re-submitted per `47` §5.6 | **Boss** |
| 2 | Content-ancestry key untested on 13 lineage groups | P02 |
| 3 | 76,245 candidates untested, incl. 807 above the floor; content hashes; per-module versions | P02 |
| 4 | Containerised databases in or out of the population — **decision required in writing** | P02 → P11 |
| 5 | Thai branch identity — 9 NULL registries, duplicate branch code `00009` | **P07** |
| 6 | `odoo_cff` has neither source basis nor behavioural marker | **P08 / P09 / P11** |
| 7 | 9 stopped container volumes never enumerated | **P06 / P11** |
| 8 | Revenue: billing vs performance | **Boss** (`BP-03`) |
| 9 | Three scope holds | **P11** |

**Not PASS. Not approved. Not frozen. Not merged. No implementation authorised. No mutation occurred.**
