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

> All four were re-examined by independent challenge. **One is unchanged, two are strengthened, one is
> re-graded down.** The movements are shown because a gap register that only moves in one direction is
> not being audited.

| ID | Gap | Evidence | State |
|----|-----|----------|-------|
| `CRITICAL-GAP-01` | **STRENGTHENED.** The inventory valuation object was replaced between the generation most prior research used and the target generation — **and in the target generation the valuation figure is writable and its only override log is deletable by the same role** | Reg 05 `OD-F-05`, `OD-F-07` | **OPEN — blocks any valuation design** |
| `CRITICAL-GAP-02` | **RE-STATED AT A SMALLER MAGNITUDE.** Persistent objects with no row-level isolation: **13 of 47 (27.7%)**, not 22 of 47 (46.8%). The core movement objects **are** company-scoped; the original finding named four of them as unisolated and was wrong | Reg 07 `SS-F-02`, challenge `A-02`/`A-03` | **OPEN at the corrected magnitude** |
| `CRITICAL-GAP-03` | **RE-GRADED CRITICAL → MATERIAL.** The counting menu applies a role-dependent record filter — but as a **visible, removable search facet**, not a silent injection. Its severity rested on the invisibility clause, which is disproved | Reg 08 `HA-F-02`, challenge `B-11` | **OPEN as MATERIAL** |
| `CRITICAL-GAP-04` | **STRENGTHENED.** Records with an empty company are visible across companies — **16** rules admit this, not 9, and the set now includes **lot / serial numbers and movement lines**, which are transactional. A **shipped** transit location is company-less, and stock in it is cross-company visible, cross-company editable and **valued by no company** | Reg 07 `SS-F-01`, `SS-F-10`, `SS-F-11` | **OPEN** |
| `CRITICAL-GAP-05` | **NEW.** Opening a menu mutates data in **4 of 9** cases, one of which runs the full procurement scheduler as superuser with intermediate commits; the maintenance routine runs **raw SQL outside the object layer**, table-wide and cross-company; and the switch said to suppress it guards **2 of its 5 call sites** and is itself **undeclared** | Reg 08 `HA-F-01`, `HA-F-09`, `HA-F-10`, `HA-F-11` | **OPEN** |

## 3. Gaps (non-Critical, or size-unmeasured)

| ID | Gap | Size | State |
|----|-----|------|-------|
| `GAP-INV-01` | Function coverage stands at **1.24%** of the derived population | 63 of 5,074 at `S4` | OPEN — expected at this stage; recorded so it is not mistaken for coverage |
| `GAP-INV-02` | Configuration toggles taking effect outside the screen surface | 7 of 21 | **CLOSED** by `SR-08` — printed templates (4), runtime code (3); produced `CORR-F-21` |
| `GAP-INV-03` | Conditional behaviour expressed in code, not in gating attributes | affects 1,540+ items | OPEN — **size known, content unmeasured** |
| `GAP-INV-04` | Reversibility of the write-off and teardown documents | 2 objects | **CLOSED** by `SR-09` — terminal by construction; produced `BOSS-DEC-11`, `GAP-INV-13` |
| `GAP-INV-05` | User-invocable controls that do not declare their own type | 53 of 431 | OPEN |
| `GAP-INV-06` | Financial postings created in code without a stored reference | **size unmeasured** | OPEN |
| `GAP-INV-07` | No segregation-of-duties mechanism on domain objects; upstream approval is out of boundary | — | OPEN — boundary question, see `BOSS-DEC-02` |
| `GAP-INV-08` | Menu-open side effects | population **9**, mutating **4** | **CLOSED** by `SR-10` + challenge `B-04`; residual bound is trace depth, stated |
| `GAP-INV-09` | **Runtime evidence not established** — no live database; archive artefacts located but not opened | affects **all 5,074 items**; `reachability` is `UNMEASURED` for every one | OPEN — the largest single bound on the package |
| `GAP-INV-10` | Persistent objects declaring no company scope | 9 dispositions (was 10; one closed as a defect) | OPEN |
| `GAP-INV-11` | Persistence interceptions unclassified as business rule vs plumbing | 141 | OPEN — prerequisite to Functional Design |
| `GAP-INV-12` | Stored computed values with no documented staleness policy | 168 | OPEN |
| `GAP-INV-13` | Code-level deletion guards override access grants | floor of 2 objects, **ceiling unmeasured** (13 of 15 guards unread) | OPEN |
| `GAP-INV-14` | **NEW.** Write-by-read entry points that are **not menus** — a product-form control, a lot-form control and a relocation wizard reach the same mutating routine | floor of 3, **no census run** | OPEN — the blind spot was declared in the unit *menu* and does not cover these |
| `GAP-INV-15` | **NEW.** Effective versus declared menu visibility gates — a third-party module rewrites two of them at install time | 2 known, **no census run** | OPEN |
| `GAP-INV-16` | **NEW.** Eligibility rule for automation: **binding object is not functional ownership**. 10 of 26 scheduled jobs in domain modules are bound to objects the domain does not own — including an **inventory valuation closing** job declared on the company object | 10 | OPEN — see `BOSS-DEC-12` |

## 4. Decisions reserved to Boss

| ID | Decision | Why it cannot be taken below Boss | Evidence |
|----|----------|-----------------------------------|----------|
| `BOSS-DEC-01` | Whether prior valuation / cost-of-goods conclusions are **superseded** by the generation change, and whether the target generation is confirmed | Supersession across workstreams; affects a standing programme HOLD | Reg 05 `OD-F-05`, `OD-F-07` |
| `BOSS-DEC-02` | Whether the Inventory research subject **includes** the manufacturing, quality, point-of-sale, repair, field-service and delivery clusters the mechanical boundary draws in | Scope of a bounded subject; changes every downstream denominator | Reg 06 `XM-F-03`, Reg 07 `SS-F-07` |
| `BOSS-DEC-03` | Whether a tenant may switch a **module-installer** toggle (41 of 237) | Deployment act, not a preference | Reg 03 `FT-F-02` |
| `BOSS-DEC-04` | Whether a **null-scope record** may exist at all in SMEsPlus | Boundary principle; the reference pattern contradicts it, and now includes transactional objects | Reg 07 `SS-F-01`, `SS-F-10` |
| `BOSS-DEC-05` | Whether any of the 31 transient interactions must leave a **persistent record** | Audit and identity policy | Reg 05 `OD-F-01` |
| `BOSS-DEC-06` | Which fields require an **immutable audit trail** (reference: 32 of 1,846) | Cannot be inherited; must be specified | Reg 05 `OD-F-04` |
| `BOSS-DEC-07` | Which deletions must be **impossible** rather than restricted (reference grants delete on 59 of 180, an **upper bound** — guards override grants) | Immutability is a Critical Area | Reg 07 `SS-F-04`, `GAP-INV-13` |
| `BOSS-DEC-08` | Confirmation that **a read must never write** in SMEsPlus | The reference does the opposite on four audit-relevant menus | Reg 08 `HA-F-01` |
| `BOSS-DEC-09` | Whether tenant administrators must be able to **see, audit and disable** automated behaviour | SaaS operability and auditability | Reg 08 `HA-F-08` |
| `BOSS-DEC-10` | Whether the **stop-at-one-hop** boundary rule is adopted as the universal standard | Governs every future subject's denominator | `00_SOURCE_LEARNING_MASTER_LIST.md` §7 |
| `BOSS-DEC-11` | Whether SMEsPlus adopts **terminal-plus-compensation** or **reversal-with-linkage** for write-off and teardown | Determines the audit trail for two value-moving documents | Reg 04 `FN-F-04` |
| `BOSS-DEC-12` | **NEW.** The eligibility rule for domain membership: **binding object, or functional ownership?** An inventory valuation closing job is declared on the company object and is mechanically outside the domain | Changes every denominator in every future subject | `GAP-INV-16`, challenge `A-09` |
| `BOSS-DEC-13` | **NEW.** Whether this session's governance defect `GOV-01` — the producer edited the package while frozen and under challenge — requires the Pilot to be **re-challenged from a clean freeze** before its findings may be relied on | The producer cannot adjudicate its own violation | `INVENTORY_PILOT_CHALLENGE_REPORT.md` §2 |

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
