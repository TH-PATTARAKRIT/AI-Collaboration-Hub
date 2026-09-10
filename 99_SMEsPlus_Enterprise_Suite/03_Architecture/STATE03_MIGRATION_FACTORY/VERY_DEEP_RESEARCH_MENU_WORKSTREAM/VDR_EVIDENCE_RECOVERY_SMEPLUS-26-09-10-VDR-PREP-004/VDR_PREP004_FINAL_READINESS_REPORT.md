# VDR_PREP004_FINAL_READINESS_REPORT.md
# Final readiness — evidence recovery, measured

Session `[SMEPLUS-26-09-10-VDR-PREP-004]` · Layer: **LAYER 1 — CLEAN-ROOM.**
Population **V5** · Baseline **B1**, pending independent challenge.

---

## 1. Disposition

> # **HOLD**
>
> **Overall Verified Coverage (Function Complete): 0.00%.** **Critical Areas at 100%: 0 of 15.**
> **Critical Gaps: 2 of 6 CLOSED — the first closures in the programme.**
> **Cell-level coverage: 44.01%, up from 0.29%.**

§18 permits certification only on conditions that include 15 of 15 Critical Areas and ≥95% overall.
Neither is met. **DO NOT FORCE PASS**, and none is forced.

## 2. What moved, and by how much

| Metric | PREP-003 R2 | **PREP-004** | Cause |
|--------|------------:|-------------:|-------|
| **Runtime Observed** | 1.52% (77) | **56.25% (2,854)** | the deployments' own element registries were extracted for the first time |
| **Security** | 0.00% | **72.92% (2,959)** | the inverted grade corrected in the evidenced direction |
| **Cross-Module** | 0.00% | **88.00% (2,560)** | per-item boundary census, not a class constant |
| **Source** | 0.00% | **53.78% (2,729)** | graded by a pointer-resolution test that can fail |
| **Optional Function** | 0.17% (7) | **22.36% (913)** | **deactivation established for all 39 subjects** |
| **Configuration** | 0.17% (7) | **17.31% (709)** | **nine axes determined for all 49 gates** |
| **Data Model** | 0.00% | 24.83% (711) | per-item condition |
| **Edge** | 0.00% | 12.94% (151) | affirmative determinations only; detection-failure vocabulary excluded |
| **Process** | 0.00% | **0.00%** | unchanged — 11 of 20 facets derivable; 9 declared not covered |
| **All cells** | 0.29% | **44.01%** | |
| **Function-complete items** | 0 | **0** | process blocks every item |
| Critical Areas at 100% | 0 of 15 | **0 of 15** | |
| Critical Gaps closed | 0 | **2** | |

**Every increase above is traceable to a named new measurement.** No predicate was relaxed, and the
denominator moved only by a published class rule.

## 3. Why Function Complete is still 0.00%

An item is function-complete only when **every** applicable dimension is verified. The distribution:

| Dimensions verified | Items |
|--------------------:|------:|
| 5 | 230 |
| 4 | 1,375 |
| 3 | 1,314 |
| 2 | 1,060 |
| 1 | 874 |
| 0 | 221 |

**No item reaches 6.** `PROCESS` at 0.00% blocks every process-applicable item, and it is at zero for a
structural reason: the standard requires **twenty** facets, **eleven** are derivable at scale, and the
other nine — calculation semantics, retry, cancel/reverse/return semantics, business-rule intent,
scheduler cadence, dependency ordering, validation messages, compensating action, idempotency — **are
declared not covered rather than silently omitted.**

**This is the single blocking dimension in the programme.** Everything else is now measurable and
measured.

## 4. The fifteen Critical Areas

| # | Area | Cells | Verified | Coverage |
|---|------|------:|---------:|---------:|
| 1 | Financial Posting | 118 | 68 | 57.6% |
| 2 | Stock Ownership | 322 | 175 | 54.3% |
| 3 | Stock Quantity | 182 | 107 | 58.8% |
| 4 | Inventory Valuation | 90 | 50 | 55.6% |
| 5 | **Security** | 898 | 92 | **10.2%** |
| 6 | **Tenant Isolation** | 0 | 0 | **NOT COMPUTABLE — no reference population** |
| 7 | Company Isolation | 389 | 187 | 48.1% |
| 8 | Approval Control | 63 | 31 | 49.2% |
| 9 | Audit Trail | 224 | 124 | 55.4% |
| 10 | Identity | 393 | 202 | 51.4% |
| 11 | Immutability | 186 | 121 | 65.1% |
| 12 | Period Close | 112 | 62 | 55.4% |
| 13 | **Reversal** | 335 | 57 | **17.0%** |
| 14 | Data Integrity | 1,629 | 939 | 57.6% |
| 15 | Cross-Module Handoff | 12 | 4 | 33.3% |

Eleven areas moved from ~0% to roughly half. **Two remain low for reasons that are themselves
findings:** Security at 10.2% because the dimension's standard — *"the grants and rules that govern
it"* — **does not fit the security classes themselves**, which grant rather than are governed; and
Reversal at 17.0% because process is zero and the reverse path is affirmatively established for only 151
of 1,167 items.

**737 distinct items** are mapped to at least one area; 912 memberships.

## 5. Critical Gaps — 2 CLOSED, 4 HOLD, 0 referred upward

| Gap | Status | Movement |
|-----|--------|----------|
| `-01` valuation object replaced | **HOLD** | **relocation CLOSED — both sides now observed.** The value field is confirmed **writable** from the deployment's own field registry |
| `-02` unisolated persistent objects | **HOLD** | 44 of 46 rules now runtime-confirmed; per-object exposure not assessed |
| `-03` role-dependent audit filter | **CLOSED** | research complete; a policy choice remains |
| `-04` company-less transactional records | **CLOSED** | mechanism fully characterised; a design act remains |
| `-05` menus that mutate on open | **HOLD** | 5 of 9 menus untraced |
| `-06` the reference object | **HOLD** | **factual claims now CONFIRMED at runtime** — element-observed on all three current-generation deployments, 11,878 rows, **1 access grant, 0 record rules**. Its severity is higher than when raised |

## 6. The five findings a SMEsPlus designer should read first

1. **A capability switch turned OFF does not revoke it from anyone holding it directly.** 48 of 49 gates behave this way, and the settings page reads OFF while the capability is live. *Any SMEsPlus switch must revoke what it grants.*
2. **Module deactivation is destructive; capability-switch deactivation is not.** 40 tables and **278 columns on models the modules do not own** are destroyed across 25 optional modules. **Not one is safe.** *This decides whether a SMEsPlus capability should be a module or a switch.*
3. **The largest interface gate in the domain is not a security control** — every internal user is already in it, and the framework treats it as a display flag. **Anything protected only by it is protected by nothing**, including the object at the centre of `CRITICAL-GAP-06`.
4. **The inventory value is writable, and on a perpetual-configured current-generation deployment with 3,680 completed movements, no accounting link is located by any of three routes.**
5. **FEFO silently degrades to FIFO** when an optional module is removed — no error, no log, unrecoverable configuration.

## 7. Boss decision hygiene — the point of this round

| | Count |
|---|---:|
| Boss decisions proposed by PREP-003 | 6 |
| **Removed as misrouted, and then answered by the team** | **4** |
| Split, team half measured, Boss half deferred until it is decidable | 1 |
| Retained unchanged | 1 |
| Promoted from closed research as genuine policy | 2 |
| **Unresolved technical facts carried to the Boss** | **0** |

**The four removals were not administrative.** Each was measured, and **three changed the package**:
the valuation premise was contradicted, the database question was settled with none relevant, and the
boundary rule turned out to rest on a denominator that is **incomplete at hop 1** — 44 objects directly
related to owned objects are not carried, including four that are financially material.

## 8. What is honestly still missing

- **Process depth.** Nine of twenty facets are not derivable at scale and are declared, not hidden.
- **The 1,144 items with no possible element record** — a method and a view sub-element are not database records. Closing this needs controlled execution or logs.
- **Which state each gate is actually in on each deployment.** The implication and membership tables were not extracted; the OFF/ON *consequence* is established, the OFF/ON *state* is not.
- **The 60 register rows classified optional with no activation condition** — an internal contradiction, recorded and left visible rather than quietly repaired.
- **A second-shape sweep of the host for database artefacts was still running when this baseline was frozen.** It is declared incomplete rather than reported as a result.

## 9. Certification and next step

**PMO certification: see `PMO_PREP004_CERTIFICATION_REPORT.md`.** This baseline is frozen for
independent challenge; the challenge outcome will be published as a new baseline per §16, and this one
will not be edited.

**RECOMMEND HOLD.** No AI may issue FINAL APPROVED, and none is issued.
