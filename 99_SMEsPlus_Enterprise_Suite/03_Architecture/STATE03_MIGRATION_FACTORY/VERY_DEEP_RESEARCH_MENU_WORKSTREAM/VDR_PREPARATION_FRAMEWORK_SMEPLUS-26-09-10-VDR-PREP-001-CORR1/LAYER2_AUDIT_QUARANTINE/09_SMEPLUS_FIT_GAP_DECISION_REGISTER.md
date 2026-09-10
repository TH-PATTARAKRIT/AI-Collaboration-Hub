# 09_SMEPLUS_FIT_GAP_DECISION_REGISTER.md
# Register 09 — SMEsPlus Fit / Gap / Decision Register (Inventory Pilot)

Session `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]` · **LAYER 2 — AUDIT QUARANTINE** · Generation: **R1 (series-19)**

---

## 1. Rule

`REFERENCE ERP BEHAVIOUR != SMEsPlus TARGET ARCHITECTURE.`

Nothing in this register is a design decision. Every row is either a **gap** (knowledge that does not
yet exist) or a **decision** (a choice reserved to Boss). No row proposes an implementation, and no row
may be read as one.

---

## 2. Critical gaps

| ID | Gap | Evidence | Why it is Critical | State |
|----|-----|----------|--------------------|-------|
| `CRITICAL-GAP-01` | The inventory valuation object **was replaced between the generation most prior research used and the target generation** | Reg 05 `OD-F-05`: 72 referencing files in series-18; **0 declarations** in series-19 | Inventory Valuation is a Critical Area; every prior valuation/cost-of-goods conclusion derived from the series-18 ledger pattern is generation-bounded and does not describe the target | **OPEN — blocks any valuation design** |
| `CRITICAL-GAP-02` | 22 of 47 persistent objects (46.8%) have **no row-level isolation**; isolation is by association | Reg 07 `SS-F-02` | Tenant Isolation and Company Isolation are Critical Areas; isolation-by-association is not a boundary | **OPEN** |
| `CRITICAL-GAP-03` | The physical-counting menu applies a **silent role-dependent record filter** | Reg 08 `HA-F-02` | Audit Trail + Data Integrity: an audit-relevant screen shows different populations to different users with no visible indication | **OPEN** |
| `CRITICAL-GAP-04` | Core inventory structures are **visible across companies when their company field is empty** | Reg 07 `SS-F-01` (9 rules; location, quantity, rule, route, package, storage category) | Company Isolation; directly contradicts the SMEsPlus boundary principle | **OPEN** |

## 3. Gaps (non-Critical or size-unmeasured)

| ID | Gap | Size | State |
|----|-----|------|-------|
| `GAP-INV-01` | Function coverage stands at 0.5% of the derived population | 4,319 of 4,339 items below `S4` | OPEN — expected at this stage; recorded so it is not mistaken for coverage |
| `GAP-INV-02` | 7 configuration toggles take effect outside the screen surface entirely | 7 of 21 | **CLOSED** by `SR-08` — resolved to printed templates (4) and runtime code (3); produced `CORR-F-21` |
| `GAP-INV-03` | Conditional behaviour expressed in code, not in gating attributes, is unenumerated | affects 1,540 of 4,339 items | OPEN — **size known, content unmeasured** |
| `GAP-INV-04` | Reversibility of the write-off and teardown documents | 2 objects | **CLOSED** by `SR-09` — no cancel state, no reverse method, deletion refused once complete; produced `BOSS-DEC-11` and `GAP-INV-13` |
| `GAP-INV-05` | 53 of 431 user-invocable controls do not declare their own type | 53 | OPEN |
| `GAP-INV-06` | Financial postings created in code without a stored reference are invisible to the declared-field census | **size unmeasured** | OPEN |
| `GAP-INV-07` | No segregation-of-duties mechanism on Inventory objects; upstream approval is out of boundary | — | OPEN — boundary question, see `BOSS-DEC-02` |
| `GAP-INV-08` | Menu-open side effects: population is a **floor of 2**, no systematic search performed | **size unmeasured** | OPEN |
| `GAP-INV-09` | **Runtime evidence not established** — no live database; archive artefacts located but not opened | affects **every** finding | OPEN — see §5 |
| `GAP-INV-10` | 10 persistent objects declare no company scope; each needs a disposition | 10 | OPEN |
| `GAP-INV-11` | 141 persistence interceptions unclassified as business rule vs plumbing | 141 | OPEN — prerequisite to Functional Design |
| `GAP-INV-12` | 168 stored computed values have no documented staleness policy | 168 | OPEN |
| `GAP-INV-13` | Code-level deletion guards override access grants; the effective delete surface is smaller than the granted one | floor of 2 objects, **ceiling unmeasured** | OPEN |

## 4. Decisions reserved to Boss

| ID | Decision | Why it cannot be taken below Boss | Evidence |
|----|----------|-----------------------------------|----------|
| `BOSS-DEC-01` | Whether prior valuation / cost-of-goods conclusions are **superseded** by the generation change, and whether the target generation is confirmed as series-19 | Supersession across workstreams; affects a standing programme HOLD | Reg 05 `OD-F-05` |
| `BOSS-DEC-02` | Whether the Inventory research subject **includes** the manufacturing, quality, point-of-sale, repair, field-service and delivery clusters that the mechanical boundary draws in | Scope of a bounded subject; changes every denominator downstream | Reg 06 `XM-F-03`, Reg 07 `SS-F-07` |
| `BOSS-DEC-03` | Whether a tenant may switch a **module-installer** toggle (41 of 237) | Deployment act, not a preference; platform-level | Reg 03 `FT-F-02` |
| `BOSS-DEC-04` | Whether a **null-scope record** may exist at all in SMEsPlus | Boundary principle; the reference pattern contradicts it | Reg 07 `SS-F-01` |
| `BOSS-DEC-05` | Whether any of the 31 transient interactions must leave a **persistent record** | Audit and identity policy | Reg 05 `OD-F-01` |
| `BOSS-DEC-06` | Which Inventory fields require an **immutable audit trail** (reference: 32 of 1,846) | Cannot be inherited; must be specified | Reg 05 `OD-F-04` |
| `BOSS-DEC-07` | Which Inventory deletions must be **impossible** rather than restricted (reference grants delete on 59 of 176) | Immutability is a Critical Area | Reg 07 `SS-F-04` |
| `BOSS-DEC-08` | Confirmation that **a read must never write** in SMEsPlus | The reference does the opposite on two audit-relevant menus | Reg 08 `HA-F-01` |
| `BOSS-DEC-09` | Whether tenant administrators must be able to **see, audit and disable** automated behaviour (reference: 0 of ~350 are declarative) | SaaS operability and auditability | Reg 08 `HA-F-08` |
| `BOSS-DEC-10` | Whether the Inventory Pilot's **stop-at-one-hop** boundary rule is adopted as the universal standard | Governs every future subject's denominator | `00_SOURCE_LEARNING_MASTER_LIST.md` §7 |
| `BOSS-DEC-11` | Whether SMEsPlus adopts **terminal-plus-compensation** or **reversal-with-linkage** for stock write-off and teardown | Determines the audit trail's shape for two value-moving documents; the reference is terminal by construction | Reg 04 `FN-F-04` |

## 5. The bound that governs the whole register

**Every finding above is a source finding.** No runtime or database evidence was established
(`GAP-INV-09`). Therefore:

- **No finding here is ranked by reachability.** Whether a behaviour is latent or live on any real
  deployment is not established, and source analysis alone cannot establish it.
- **Severity labels in this register are structural, not empirical.** `CRITICAL` means "governs a
  Critical Area", not "observed to occur".
- **No fit assessment is offered.** A fit/gap judgement against SMEsPlus requires a SMEsPlus design to
  judge against; none exists yet, and inventing one here would be exactly the downstream guessing the
  programme forbids.

`NO EVIDENCE = NO PROGRESS.` · Boss is the sole Final Approver.
