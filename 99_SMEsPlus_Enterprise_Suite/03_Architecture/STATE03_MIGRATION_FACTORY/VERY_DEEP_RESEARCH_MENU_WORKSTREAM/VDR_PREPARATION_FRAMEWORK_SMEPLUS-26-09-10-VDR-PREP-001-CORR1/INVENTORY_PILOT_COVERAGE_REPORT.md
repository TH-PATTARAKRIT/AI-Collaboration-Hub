# INVENTORY_PILOT_COVERAGE_REPORT.md
# Inventory Pilot — Coverage Reconciliation

Session `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]` · **LAYER 1 — CLEAN-ROOM** summary of LAYER 2 measurement
Rule applied: `VDR_COVERAGE_RULE.md` v1.0 · Generation basis: **R1 (series-19, content-verified)**

---

## 1. Reading instruction

Every percentage below carries its numerator and denominator. **Dimensions are not collapsed.**
`VERIFIED` means research state `S4 FUNCTION VERIFIED` or higher. Locating something is `S1`,
not coverage.

---

## 2. Coverage Dashboard

### 2.1 Preparation Framework

| Dimension | Numerator / Denominator | % | Note |
|-----------|------------------------:|--:|------|
| Preparation Controls frozen | 5 / 5 | **100%** | Master List, Nine Registers, Coverage Rule, Challenge Checklist, Execution Order |
| Nine Registers instantiated | 9 / 9 | **100%** | every record carries a Learning ID; **0 orphan records** |
| Controls **exercised by the Pilot** | 5 / 5 | **100%** | each control produced at least one correction to itself |
| Framework corrections incorporated before closure | 21 / 21 | **100%** | `VDR_FRAMEWORK_PILOT_CORRECTION_REGISTER.md` |
| **Preparation Framework Readiness** | — | **92%** | 8 points withheld: the framework has been exercised on **one** domain, by **one** producer, with **no runtime evidence**; see §4 |

### 2.2 Source Learning Population

| Dimension | Numerator / Denominator | % |
|-----------|------------------------:|--:|
| Derivation steps executed and published | 8 / 8 | **100%** |
| Instrument controls executed (I1–I4) | 4 / 4 | **100%** |
| Learning Items with a reproducible evidence pointer (`S1`) | 4,339 / 4,339 | **100%** |
| Learning Items with a generation basis | 4,339 / 4,339 | **100%** |
| Boundary published as a set with its complement | yes | **100%** |

### 2.3 Research coverage, by dimension

| Dimension | Population | `S1` located | `S4` verified | Verified % |
|-----------|-----------:|-------------:|--------------:|-----------:|
| **Menu** | 62 | 62 (100%) | 0 | **0%** |
| **Menu (extra-application)** | 134 | 134 (100%) | 0 | **0%** |
| **Configuration dependency** | 633 gated elements / 43 groups | 633 (100%) | 633 mechanism-verified | **100% of mechanism, 0% of consequence** |
| **Feature Toggle** | 237 | 237 (100%) | 21 of 21 group-toggles resolved to an effect surface | **8.9%** |
| **Function** | 1,795 function-bearing items | 1,795 (100%) | 25 | **1.4%** |
| **Object / Data** | 86 objects · 1,846 fields · 32 constraints | 100% | 0 | **0%** |
| **Cross-Module** | 90 external objects, both directions | 90 (100%) | 0 | **0%** |
| **Hidden Automation** | 350 automated behaviours + 2 located side effects | 350 (100%) | 2 | **0.6%** |
| **SaaS / Security** | 44 groups · 176 grants · 28 rules | 100% | 0 | **0%** |
| **Edge / Reversal** | 86 objects | 2 (`SR-09`) | 2 | **2.3%** |
| **SMEs Core Challenge closure** | 30 questions | 30 dispositioned | — | **100% dispositioned**, see §3 |

**The 25 function-verified items and the 633 mechanism-verified gated elements are not commensurable
and are not added together.** Taking the strict reading — Learning Items at `S4` or higher over the
full population:

```
Overall Verified Coverage  =  25 / 4,339  =  0.58%
```

### 2.4 Critical Area coverage

| Critical Area | Population established | Verified | 100%? |
|---------------|------------------------|---------:|:-----:|
| Financial Posting | partial — code-created postings unmeasured | 0 | **NO** |
| Stock Ownership | yes | 0 | **NO** |
| Stock Quantity | yes | 0 | **NO** |
| Inventory Valuation | **object replaced between generations** | 0 | **NO** |
| Security | yes | 0 | **NO** |
| Tenant Isolation | **no reference population exists** | n/a | **NO** |
| Company Isolation | yes | 0 | **NO** |
| Approval Control | yes — none on domain objects | 0 | **NO** |
| Audit Trail | yes (32 tracked fields) | 0 | **NO** |
| Identity | not opened | 0 | **NO** |
| Immutability | partial — 15 guards, 2 read in full | 2 objects | **NO** |
| Period Close | not opened | 0 | **NO** |
| Reversal | established for 2 of 86 objects (`SR-09`) | 2 objects | **NO** |
| Data Integrity | yes (32 constraints) | 0 | **NO** |
| Cross-Module Financial Handoff | partial (`GAP-INV-06`) | 0 | **NO** |

**Critical Area coverage: 0 of 15 at 100%.**

---

## 3. Gate evaluation

| Gate condition | Threshold | Actual | Result |
|----------------|-----------|--------|--------|
| Overall Verified Coverage | ≥ 95% | 0.58% | **FAIL** |
| Every Critical Area | 100% | 0 of 15 | **FAIL** |

**Disposition: `HOLD`.** Under `VDR_COVERAGE_RULE.md` §6 the Critical Area condition alone is
decisive; the overall figure does not need to be argued.

---

## 4. What this number means, and what it does not

This Pilot was commissioned to **stress-test the Framework**, not to complete Inventory research.
It has done exactly that, and the coverage figure is the correct output of a correct measurement.

The figure is **not** comparable to coverage percentages published by earlier programme rounds,
because those were computed against denominators that were author-chosen. **This denominator was
derived by a published rule, validated by four instrument controls, and its boundary is published as a
set with its complement.** A lower number against a real denominator is worth more than a higher number
against an invented one — and the framework's first job is to make that difference visible.

**The 8 points withheld from Preparation Framework Readiness are, specifically:**

| Withheld | Points | Why |
|----------|-------:|-----|
| Single-domain exercise | 3 | the framework has been tested on Inventory only; a second domain of different shape (a master-data subject, per the parent workstream's own priority order) would test different failure modes |
| Runtime evidence absent | 3 | `GAP-INV-09` — no deployment evidence, so the framework's **reachability** dimension has never been executed at all |
| Single-producer challenge | 2 | the independent challenge was run by a separate reviewer with a separate instrument, but within the same session; a peer-exchange control has not been applied |

**These three are stated as a target of 92%, not as a claim of 95–98%.** The prompt's target of
95–98% preparation readiness is **not met**, and the shortfall is attributable to two conditions that
this session cannot close by working harder — a second domain and a runtime evidence base — plus one
that requires a party outside this session.
