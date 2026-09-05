# P09_CROSS_PROCESS_OWNERSHIP

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Process:** P09 Plan-to-Analyze
**Layer:** 1 — clean-room. Evidence identifiers resolve in the Layer 2 quarantine.

---

## 1. THE QUESTION

Who owns the management dimension assignment for a given cost, at which step, and can a later step change it?

## 2. THE OWNERSHIP TABLE

| Process | First set at | Ownership mechanism | Survives downstream? | Can a later step change it silently? | Evidence |
|---|---|---|---|---|---|
| **P01 Procure-to-Pay** | purchase order line | copied to the bill line by a **compute**, guarded by "only if the bill line has none". The compute depends on the account, the partner and the product — **not** on the order line | yes, on first creation | **YES** — reclassifying the bill line's account re-runs the compute; the order guard then blocks the re-copy, and a matching assignment rule **overwrites** the inherited value outright. No warning, no audit entry. Comparable fields have a protective guard; the allocation does not | X3-01 |
| **P02 Order-to-Cash** | sales order line | mirror image of the above, same host compute, same guard | yes | **YES** — structurally identical; class **B** (inferred from code-path symmetry, not independently traced end to end) | X3-01 |
| **P05 Expense-to-Pay** | expense record | its own compute, depending on the product, the account and the employee | yes | **YES** — same shape; an account or employee change re-triggers it. A separate editability gate governs *who* may write, not whether a rule may supersede | X3-01 |
| **P04 Acquire-to-Retire** | asset record, as a **balance-weighted average** of its originating ledger rows | its own compute | yes | **NO** — re-propagation is explicitly restricted to **draft** depreciation entries, with a source comment naming the reason | X3-02 |
| **Inventory / valuation** | copied from the posted entry's own row | value builder | the value survives; **the ledger link does not** — it is structurally discarded even where the entry exists | n/a | COR-P09-05, X1-01 |
| **P03 Manufacture-to-Cost** | **work-centre master data** — it inherits from no document at all | the work centre is itself an allocation carrier | n/a | the assignment changes whenever the master data changes; historical records are not re-derived | EV-P09-111, X1-04 |
| **P06 Bank-to-Reconcile** | copied from the matched ledger row where one exists, else from rules | widget compute | yes | **YES**, same overwrite shape; not independently traced for a state guard — class **B** | X3 §3 |
| **Tax** | inherited **conditionally** — only where the tax record carries an analytic flag, or the repartition row is not used in tax closing; otherwise forced empty | repartition inheritance | conditional | deliberate non-allocation is indistinguishable from unfilled | EV-P09-107 |

**Only one of eight processes — asset accounting — has a coded ownership boundary.** In the other seven, ownership is an emergent property of a dependency list, and the allocation is the one field in its class with no protective guard against recomputation.

**CP-01.** Ownership of a management assignment shall be **declared**, not emergent. Each process shall state which step owns the assignment and at which point ownership transfers.

**CP-02.** A downstream change to an inherited assignment shall be an explicit, recorded act. A rule engine shall never silently supersede a value that a document propagated or a user entered.

**CP-03.** Deliberate non-allocation shall be an explicit value. The tax case shows that "not allocated on purpose" and "not filled in yet" are today the same state.

## 3. THE COMPANY BOUNDARY — INTER-COMPANY MIRRORING

When a document is mirrored into a second company, the reference pattern **drops the allocation**:

1. every allocation key whose axis value carries a company is identified;
2. those keys are **removed**; only company-less axis values survive;
3. the mirrored line's allocation is set **only if** the receiving company has its own matching rule, or some company-less key survived. If neither holds, the mirrored line carries **no allocation at all**;
4. where the receiving company does have a rule match, that result is the **base**, and surviving keys are merged on top — so the receiving company's own default silently outranks the sending document;
5. the module's own test asserts the empty outcome as expected behaviour.

No warning, no message, no exception on either path (X3-03, class A, corroborated by the source's own test).

**Assessment.** Under the corrected scope constitution this is not automatically wrong — a COMPANY-scoped axis value legitimately cannot be used by another company. What is wrong is the **silence** and the **precedence**: a management assignment is lost at the boundary with no record that it was lost, and the receiving company's default outranks the originating document with no marker.

**CP-04.** Where a management assignment cannot cross a scope boundary, the loss shall be **recorded on the receiving document** as an explicit unmapped state, and shall be reportable. Silent loss is prohibited.

**CP-05.** Cross-scope mapping shall be an explicit, configured correspondence between the sending scope's axis values and the receiving scope's, not a fallback to the receiving side's defaults.

**CP-06.** A TENANT-scoped axis value — the corrected constitution's legitimate case for a shared dimension — is precisely what would make CP-05 unnecessary for the shared part of the tree. This is a direct argument for the scope model in `P09_SCOPE_OWNERSHIP_MATRIX`: the reference pattern's only mechanism for a cross-company dimension is an **undeclared** null company, and it then treats that null as the sole survivor at the boundary.

## 4. EXPORT SURFACE

No export or electronic-invoicing path in the searched scope carries management data outside the system. All modules matching the three export-family name patterns at root depth were swept across code and view files: **zero matches**. Class **A** for that pattern and path set; statutory exports under other naming are class **C** (X3-04).

**CP-07.** This is a deliberate design point for SMEsPlus, not an inherited default: management dimensions **should not** leave the system through statutory channels unless a named requirement demands it. Record the decision explicitly rather than inheriting the silence.

## 5. THAI LOCALIZATION

Ten Thai-named modules were enumerated across four roots — two in the reference set, eight in the tenant custom sets — and every one returns **zero** matches for the analytic, budget, cost-centre and department pattern, in every copy where it exists. Class **A** within that pattern and path set (X3 §C).

**Withholding tax is structurally independent of the management-accounting layer** in the searched scope.

### Held, routed to the Accounting-Tax track
| ID | Item | Status |
|---|---|---|
| HOLD-TH-01 | whether Thai statutory practice requires cost-centre or department segregation in management accounts, tax reporting, or withholding-tax certificates | **HOLD / EVIDENCE REQUIRED.** Not evidenced anywhere in the searched code. This package makes **no claim** about whether that silence is a gap or a correct reflection of no requirement. A named statutory citation is required; a code search cannot settle it. |
| HOLD-TH-02 | whether the tenant department-dimension extension is intended to satisfy a Thai cost-centre practice | **HOLD / EVIDENCE REQUIRED.** Design question, not decidable from source. |
| HOLD-TH-03 | a **statutory** Thai capability differs between deployment copies — one withholding-tax module is present in two custom copies and absent from the third | **HOLD / EVIDENCE REQUIRED**, severity above HOLD-TH-02 because the varying item is statutory. Which copy is deployed is class **D**. |

All Thai names encountered anywhere are **candidate / UNVALIDATED**; none is transcribed into this package.

## 6. PEER DEPENDENCIES

| ID | Dependency | Counterpart | Status |
|---|---|---|---|
| PD-01 | scope of the manufacturing order and the work centre as cost objects | P03 | **PEER DEPENDENCY OPEN** |
| PD-02 | asset↔equipment relationship and asset cost-object scope | P04 | **PEER DEPENDENCY OPEN** |
| PD-03 | whether commitment is ledger-visible | P01 | **PEER DEPENDENCY OPEN** |
| PD-04 | accounting-event identity, which P09's trace requires and the reference pattern lacks | Core Ledger / P11 | **PEER DEPENDENCY OPEN** |
| PD-05 | whether a tenant may span jurisdictions, which decides whether a tenant-scoped budget is admissible | P07 / P11 | **PEER DEPENDENCY OPEN** |
| PD-06 | the platform definition of tenant, which P09 assumes and does not own | P11 | **PEER DEPENDENCY OPEN** |
| PD-07 | the bill-line overwrite path (P01) and its sales mirror (P02) are P09 findings inside another process's territory | P01, P02 | **PEER DEPENDENCY OPEN — findings handed over, not adjudicated** |

P09 does not stop for any of these and does not adjudicate against another process's determination.

## 6A. CONTINUATION ADDENDUM — ANALYTIC ECONOMIC INTEGRITY

The `AI_ANALYTIC_ECONOMIC_INTEGRITY/` continuation adds four cross-process items to this register. Full detail in `AI10_P09_PEER_HANDOFF_MATRIX`.

| ID | Handed to | Item |
|---|---|---|
| **CP-A1** | **P10 Time-Based Recognition** | the cut-off / change-period accrual wizard allocates **both** legs of a mirrored pair, so the attribution nets to zero. **Routing question raised and left open:** whether this is a P09 finding or a P10 finding — P09 records it and does not claim it |
| **CP-A2** | **P07 TH Tax Compliance** | the cash-basis tax entry builds its counterpart on the **same account** with the same allocation, so the attribution is zero on **every** surface. Same routing question; P09 records and does not claim |
| **CP-A3** | **P03 Manufacture-to-Cost** | the masking interaction — whether work-centre hourly rates recover depreciation, in which case a cost centre can show a plausible total while both contributing mechanisms are wrong. **`UNRESOLVED — EVIDENCE REQUIRED`**, a costing-policy fact, not a code fact |
| **CP-A4** | **P04 Acquire-to-Retire** | the algebra, the unconditionality, the surface divergence, and the deferred-recognition variants sharing the same shape. P09 **confirms P04's original finding in full** and adds to it |

**Nothing in this addendum settles `HOLD-AS-01` or `DIS-09`.** Strengthening a finding does not confer authority to adjudicate between two parallel evidence tracks.

## 7. TERMINAL STATE

**CP-01 … CP-07 ISSUED AS PROPOSALS. THREE THAI ITEMS HELD. SEVEN PEER DEPENDENCIES OPEN PLUS FOUR CONTINUATION HANDOFFS. NO GATE MOVED.**
