# VDR_OPEN_CRITICAL_GAP_CLOSURE_REGISTER.md
# Six open Critical Gaps — each addressed individually, none closed

Session `[SMEPLUS-26-09-10-VDR-PREP-003]` · Layer: **LAYER 1 — CLEAN-ROOM.**
Commissioning instruction §11: *close each open critical gap individually.*

---

## 1. Closure standard applied

A Critical Gap is **CLOSED** only when all four hold:

1. the condition it asserts is **re-measured** on the current frozen population;
2. the measurement carries an **instrument validation** — second shape, positive control drawn from the
   corpus, coverage assertion, zero re-test;
3. the closure is **independently challenged** and survives;
4. **PMO certifies** it.

Nothing less is closure. In particular: *re-stating a gap more precisely is not closing it*, and
*retracting the overstated half of a gap is not closing the remainder*.

## 2. The register

### `CRITICAL-GAP-01` — the valuation object was replaced between generations

| | |
|---|---|
| **Critical Areas** | 1 Financial Posting · 4 Inventory Valuation |
| **Action this session** | re-measured on the transacted current-generation deployment |
| **Result** | **the stronger form was RETRACTED.** The previous claim — *"the current generation is not writing per-movement valuation"* — is **false**. The value **relocated onto the movement row**: 100% of 3,680 completed movements carry one — **a denominator that is unreconciled against the same package's 14,441 (`CH-17`), and is carried to PMO as a blocking item.** The earlier comparison had no state basis (the deployment measured had zero completed movements) and no configuration control (every located current-generation deployment runs periodic valuation, under which no movement posts in *any* generation) |
| **Residual gap** | the dedicated valuation ledger table is genuinely absent; its replacement holds 85,832 rows of which **0 carry a movement reference**; the valuation figure is **writable** and its only override log is **deletable by the same role** |
| **State** | **OPEN — re-stated at MATERIAL weight.** Prior conclusion preserved as audit lineage per PREP-002 §17 |
| **What would close it** | a controlled install under *perpetual* valuation, current generation, with a movement completed and the resulting records read — the counterfactual the original comparison never ran. **Note added after challenge:** a controlled-install lab exists on this host with an evidence directory named for that very configuration. It is the **prior** generation and does not discharge the current-generation requirement — but the R1 text asserted the counterfactual was never run without naming a lab built to run it (`CH-13`) |

### `CRITICAL-GAP-02` — persistent objects with no row-level isolation

| | |
|---|---|
| **Critical Areas** | 5 Security · 7 Company Isolation |
| **Action this session** | the record-rule resolver was rebuilt and re-run |
| **Result** | **RE-STATED SMALLER, and the original was wrong in a way that mattered.** 13 of 47 (27.7%), not 22 of 47 (46.8%). The four core movement objects the original named as unisolated **are** company-scoped |
| **Why it was wrong** | the resolver applied a string transform instead of a lookup (yielding 12), then read only one of the two declaration forms (yielding 28). The correct figure is **46** rules. My own second-shape control agreed at 28 — **because both instruments shared the same accessor.** Agreement between instruments that share a defect is not corroboration |
| **State** | **OPEN at the corrected magnitude** |
| **What would close it** | the 13 unisolated objects enumerated individually, each with its exposure assessed against a real deployment's data |

### `CRITICAL-GAP-03` — role-dependent record filter on an audit-relevant screen

| | |
|---|---|
| **Critical Areas** | 5 Security · 9 Audit Trail |
| **Result** | **RE-GRADED CRITICAL → MATERIAL.** The filter is real, but it is applied as a **visible, removable search facet**, not a silent injection. Its severity rested entirely on the invisibility clause, and that clause is disproved |
| **State** | **OPEN as MATERIAL** |
| **What would close it** | a decision, not more evidence: whether SMEsPlus accepts role-dependent default filtering on audit screens at all |

### `CRITICAL-GAP-04` — records with an empty company are visible across companies

| | |
|---|---|
| **Critical Areas** | 2 Stock Ownership · 7 Company Isolation |
| **Result** | **STRENGTHENED.** 16 rules admit company-less records, not 9 — and the set now includes **lot/serial numbers and movement lines**, which are transactional, not reference data. A **shipped** transit location is company-less: stock in it is cross-company visible, cross-company editable, and **valued by no company** |
| **State** | **OPEN — strengthened** |
| **What would close it** | for SMEsPlus this is not closable by research. The recommendation put to the Boss is a design prohibition — **no transactional record without an owning scope** — and it is a recommendation, not an adopted rule. **Boss decision** |

### `CRITICAL-GAP-05` — opening a menu mutates data

| | |
|---|---|
| **Critical Areas** | 9 Audit Trail · 11 Immutability · 14 Data Integrity |
| **Result** | **4 of 9** menus mutate data on open — corrected up from 3, then from 2. One runs the full procurement scheduler as superuser with intermediate commits. The maintenance routine runs **raw SQL outside the object layer**, table-wide and cross-company. The switch said to suppress it guards **2 of its 5** call sites and is itself **undeclared**. Now confirmed **LIVE on a transacted deployment** |
| **Why the count moved twice** | the method-body resolver returned the first definition in walk order on an overridden method (2→3); then a menu bound to an action **materialised at install from a scheduled-job record** was found, which the census had missed entirely (3→4, census 8→9) |
| **State** | **OPEN** |
| **What would close it** | the remaining 5 menus traced to the same depth, and the undeclared switch's 5 call sites enumerated |

### `CRITICAL-GAP-06` — the reference object

| | |
|---|---|
| **Critical Area** | 10 Identity |
| **Result** | unchanged and unaddressed. The object is the **2nd most populated in the domain**, joining **91% of movements and 99.9% of sales orders**, and has **no controls, no validations, no behaviours and no record rule**. It is reachable only through a **technical-only** group — one of the 55 elements so gated (`C3-F-02`) |
| **Covered by prior research** | **no — by none of it** |
| **State** | **OPEN** |
| **What would close it** | a full nine-dimension study of the object and its identity semantics. Identity is a Critical Area at 44.0%, and this object is the reason it cannot rise |

## 3. Roll-up

| | Count |
|---|---:|
| Open at session start | 6 |
| **Closed to the standard in §1** | **0** |
| Retracted in part | 1 (`-01`) |
| Corrected downward | 1 (`-02`) |
| Re-graded downward | 1 (`-03`) |
| Strengthened | 2 (`-04`, `-05`) |
| Unmoved | 1 (`-06`) |
| **Open at session end** | **6** |

**Three gaps moved and none closed.** Movement is not closure, and this register does not present it as
closure. §11 requires individual closure; **that requirement is not met**, and it is one of the reasons
the disposition is HOLD.

Every movement above preserves the prior statement as audit lineage. No gap was withdrawn to make a
number look better, and the two that grew were allowed to grow.
