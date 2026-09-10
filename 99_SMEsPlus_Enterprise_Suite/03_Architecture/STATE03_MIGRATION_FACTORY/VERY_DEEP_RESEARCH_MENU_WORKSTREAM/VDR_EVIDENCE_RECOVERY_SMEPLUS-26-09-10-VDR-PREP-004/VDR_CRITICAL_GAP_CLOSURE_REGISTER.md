# VDR_CRITICAL_GAP_CLOSURE_REGISTER.md
# Six Critical Gaps, taken individually — CLOSED or HOLD, never "Boss to decide"

Session `[SMEPLUS-26-09-10-VDR-PREP-004]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 10.

§13 permits two final statuses only: **CLOSED** or **HOLD**. *"Boss to decide"* is not available for an
unresolved technical fact, and no gap below uses it.

---

## `CRITICAL-GAP-01` — the valuation object was replaced between generations

| Field | Content |
|-------|---------|
| **Affected Learning IDs** | Critical Areas 1 (Financial Posting, 16 items) and 4 (Inventory Valuation, 12 items) |
| **Root cause** | the record that carries inventory value moved between generations, and the prior conclusion was derived from the generation that no longer applies |
| **Functional owner** | the valuation-accounting module — established from the field registry, not inferred |
| **Source evidence** | the per-movement value field is declared in that module's extension of the movement object |
| **Runtime evidence** | **both sides of the replacement now observed.** Generation 19: value on the movement row, 3,680 of 3,680 completed movements; the dedicated ledger table **absent from the dump's table of contents entirely**. Generations 16 and 18: value **not** on the movement row across **127,957** completed movements, and present in the ledger instead (74,982 rows on the 16-generation deployment) |
| **Configuration evidence** | the transacted deployment is configured **real-time (perpetual) on 27 of 37 categories** — retracting the prior claim that every current-generation deployment runs periodic |
| **Optional function evidence** | the valuation-accounting module is core, not optional; landed costs — an optional module, 42 elements — is an additional value input |
| **Contradiction** | the prior *"periodic configuration explains the absence of postings"* is **contradicted by the deployment's own configuration records** |
| **Independent challenge** | a challenger independently corroborated the relocation from a **sixth, previously unnamed** snapshot: the movement column list there carries the value, direction and accounting-link columns |
| **Resolution — half one** | **CLOSED.** The relocation is measured, on both sides, with a negative control that behaves as a negative control should |
| **Resolution — half two** | **CONFIRMED AND OPEN.** *"the valuation figure is writable"* — read from the deployment's own field registry: the value field is **`readonly = false`**, stored, monetary. The discriminating control: `reference`, `is_in` and `is_out` on the same object are `readonly = true`, so the flag distinguishes. **The number that values inventory is writable by anything that can write the record.** |
| **Final status** | **HOLD** — the replacement is closed; the writability exposure is confirmed, not remediated, and remediation is a SMEsPlus design act, not a research act |

## `CRITICAL-GAP-02` — persistent objects with no row-level isolation

| Field | Content |
|-------|---------|
| **Affected** | Critical Areas 5 and 7 |
| **Root cause** | a resolver defect, twice: a string transform instead of a lookup, then only one of two declaration forms |
| **Source evidence** | 46 record rules, corrected from 12 then 28 |
| **Runtime evidence** | **new this round: 44 of 46 rules are element-observed** on real deployments; 43 of 44 groups likewise |
| **Magnitude** | **13 of 47 (27.7%)**, re-stated *smaller*; the original 22 of 47 named four core movement objects as unisolated that are in fact scoped |
| **Independent challenge** | the correction survived; the shared-accessor defect that produced the wrong intermediate value is recorded |
| **Required research** | enumerate the 13 individually with each one's exposure |
| **Resolution** | the count is settled and now runtime-confirmed. **The per-object exposure assessment was not performed this round** |
| **Final status** | **HOLD** |

## `CRITICAL-GAP-03` — role-dependent record filter on an audit-relevant screen

| Field | Content |
|-------|---------|
| **Root cause** | a default search facet that varies by role |
| **Evidence** | the filter is a **visible, removable** search facet, not a silent injection; the severity rested on an invisibility clause that is disproved |
| **Runtime evidence** | the screen and its action are element-observed on all three current-generation deployments |
| **Re-grade** | **CRITICAL → MATERIAL**, and the re-grade holds |
| **Resolution** | the technical fact is fully established. What remains is **whether SMEsPlus permits role-dependent default filtering on audit screens** — a policy question with the evidence complete |
| **Final status** | **CLOSED as a research item.** Carried to the Boss decision list as a **TRUE** policy decision under §15, because no further evidence can decide it |

## `CRITICAL-GAP-04` — records with an empty company are visible across companies

| Field | Content |
|-------|---------|
| **Affected** | Critical Areas 2 and 7 |
| **Source evidence** | **16** record rules admit company-less records, including lot/serial numbers and movement lines — transactional, not reference data |
| **Runtime evidence** | the rules are element-observed; a shipped transit location is company-less, cross-company visible, cross-company editable and valued by no company |
| **Required research** | none outstanding — the mechanism is fully characterised |
| **Resolution** | the exposure is measured and confirmed. It is **not closable by research**: it is a property of the reference design, and SMEsPlus's response is a design act |
| **Final status** | **CLOSED as a research item**, carried forward as a design constraint recommendation — *no transactional record without an owning scope*. **A recommendation, not an adopted rule** |

## `CRITICAL-GAP-05` — opening a menu mutates data

| Field | Content |
|-------|---------|
| **Affected** | Critical Areas 9, 11, 14 |
| **Root cause** | menu actions bound to methods that write; one runs the procurement scheduler as superuser with intermediate commits |
| **Source evidence** | **4 of 9** menus mutate on open — corrected up from 2, then 3, as two resolver defects were fixed |
| **Runtime evidence** | **live on a transacted deployment**; the maintenance routine runs raw SQL outside the object layer, table-wide and cross-company; the suppression switch guards **2 of its 5** call sites and is itself undeclared |
| **Required research** | the remaining 5 menus traced to the same depth; the undeclared switch's 5 call sites enumerated |
| **Resolution** | **not performed this round** |
| **Final status** | **HOLD** |

## `CRITICAL-GAP-06` — the reference object

| Field | Content |
|-------|---------|
| **Affected** | Critical Area 10 (Identity) |
| **Root cause** | an object central to the domain with no controls, no validations, no behaviours and no record rule, reachable only through a technical-only group |
| **Source evidence** | the object is declared in the domain's core module |
| **Runtime evidence — NEW** | **element-observed on 3 of 5 deployments (all three current-generation)**, and it carries **11,878 rows** on the transacted deployment. It is not theoretical |
| **Security evidence — NEW** | read from the deployment's own registry: **1 access grant, 0 record rules.** The "no record rule" half of the gap is now **confirmed at runtime**, not inferred from source |
| **Cross-module evidence** | the movement object's reference field is populated on **100% of 14,441 movement rows** |
| **Prior research** | **covered by none of it** |
| **Required research** | the full nine-dimension study of the object |
| **Resolution** | the gap's factual claims are now **confirmed**, and its severity is **higher** than when raised: a heavily populated, universally referenced object with one access grant and no row-level isolation |
| **Final status** | **HOLD** |

---

## Roll-up

| | Count |
|---|---:|
| Open at round start | 6 |
| **CLOSED as research items** | **2** (`-03`, `-04`) |
| **HOLD** | **4** (`-01`, `-02`, `-05`, `-06`) |
| Referred to the Boss as an unresolved technical fact | **0** |
| Gaps whose factual claims moved **up** on new evidence | 2 (`-01` writability confirmed; `-06` runtime presence and isolation confirmed) |

**Two gaps closed — the first closures in the programme.** Both closed because their research was
genuinely complete, not because the round needed a number. The four on HOLD each name the specific,
bounded measurement that would close them, and none of them names the Boss.
