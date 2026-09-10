# SMES_CORE_PREP005_CHALLENGE_REPORT.md
# Independent challenge — two challengers, and two of my own conclusions overturned

Session `[SMEPLUS-26-09-10-VDR-PREP-005]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 11.

---

## 1. Round constitution

The PREP-004 baseline `75b00dc1` was frozen and challenged by two independent reviewers, scoped so
neither could produce the other's failure mode: **D** on grade legitimacy, **E** on missing surface and
false exclusion. **Round opened `2026-09-10T14:57:04Z`; no commit entered that package path while it
was open** — the control adopted after `GOV-01` recurred, and this time it held.

**32 findings returned. Every one re-run here before disposition.**

## 2. The verdict in one line

> **The coverage this programme published was, outside two dimensions, a measure of its own register's
> authoring rather than of evidence — and two conclusions it published as corrections were themselves
> wrong, one of them contradicted by a file inside its own package.**

## 3. The two overturns — accepted in full, and verified

### `CH5-01` — the valuation configuration was read off the wrong object *(challenger E, CRITICAL)*

PREP-004 published: *"the premise 'every current-generation deployment runs periodic valuation' is
FALSE — the transacted deployment is configured perpetual on 27 of 37 categories."* That claim was
carried into a Critical Gap, a readiness finding, and the Boss-decision filter.

**It is wrong.** The category setting is a **company-dependent** value, stored per company, and it was
set for **company 1 only on a 44-company deployment**. The governing value is the company setting, and
in the current generation the category property falls back to it. Read from the deployment's own company
records:

| Deployment | Companies | `inventory_valuation` | `inventory_period` |
|---|--:|---|---|
| **`BK12MAY26`** (transacted) | 44 | **periodic × 44 of 44** | manual × 44 |
| `iEVING` | 44 | periodic × 43, real time × 1 | manual × 43 |
| `iTEST02` | 1 | **real time × 1** | **daily** |

**The transacted deployment is periodic.** The original premise — which PREP-004 retracted — **is
restored, and is now confirmed from the deployments' own records rather than assumed.** The
configuration column of PREP-004's five-deployment spread is **inverted for two of the three
current-generation deployments.**

> **The file that disproves it was inside the frozen package.** `res_company` was extracted, hashed,
> shipped — and never read. This is the *evidence-at-rest* defect: the evidence was not missing, it was
> unexamined.

### `CH5-02` — the accounting-link control could never have fired *(challenger E, CRITICAL)*

PREP-004 published: *"no accounting link is located by any of three routes,"* offering as its positive
control *"could the column ever hold a value? 0 of 14,441."*

**That is not a control — it measures the same negative twice in the same configuration.** The writer
exists and is named in source; it is gated by a five-way condition that requires a valuation account on
the source or destination location. Measured: **0 of 525 locations on the transacted deployment carry
one, and 0 of 5,192 on the other.** The link is null **by construction of the configuration**, not by
absence of a mechanism.

**And a fourth route was never enumerated:** a daily scheduled job, running as superuser, that posts a
valuation closing **at company level with no movement reference at all**. No per-movement route could
have found it — and that job is one of **138 action records that exist on live deployments and are in no
learning item** (§4).

**The corrected finding:** *the per-movement link mechanism is located, and its precondition is
measurably unsatisfied on every deployment; a company-level closing route exists and was not examined.*
That is a materially different design conclusion from *"no link exists."*

### `CH5-03` — the bounded claim was restated unbounded, three times, in the file that bounds it
*"nothing consumes it"* · *"no link at all"* · *"if it runs at all"* — and a §9 row declaring the
question **"MEASURED THIS ROUND… no longer an open one."** It was closed on the wrong basis. **Accepted.**

## 4. Missing surface — the population is incomplete at hop zero *(challenger E)*

PREP-004 framed its boundary problem as a hop-1 question. **The larger problem is that surface which
never entered the relational graph at all was never counted:**

| Finding | Measured |
|---------|---------|
| Domain-declared **field** records on objects the population calls **owned**, carried by nothing | **652** |
| **Action** records on generation-19 deployments, owned by domain modules, in no learning item | **138** — including the **valuation-closing job**, the **procurement scheduler** (the subject of `CRITICAL-GAP-05`), and the valuation report |
| **Models** declared by the domain's own modules, in neither the owned nor the boundary set | **251** |
| Modules **installed** on the transacted deployment with **no source in the declared path set** | **39** — 1,647 records, 287 of them landing on population objects; including one that modifies the valuation report and one that hides menus |

One owned object has **three** learning items in a 5,074-row population — one menu, one object row, one
handoff row. Zero fields, buttons, views, behaviours, constraints, access rules or record rules.

**The one-hop rule cannot be invoked for surface that never entered the graph.**

## 5. The §6 claim of zero violations is false *(challenger E)*

The prohibited reason — *another module owns the workflow* — survives, **relocated from a per-row `NA`
into the class rule table**. The boundary class is granted three applicable dimensions where the owned
class gets nine, and the only discriminator is ownership. Measured cost: **76 live record rules on the
transacted deployment govern population objects and are in no learning item.**

**Accepted.** The class rule is an exclusion by construction, which is precisely what the false-exclusion
register claimed to have caught elsewhere.

## 6. "No ORM record can exist" is false for 415 of 1,144 *(challenger E)*

PREP-004 declared a categorical limit. **411 of 487 parsable gated view sub-elements are present, with
their gate, in the deployment's stored view definitions** — a table the package never extracted — and 4
of 5 system parameters are element-observable by the same join the element tier uses.

**Only the 614 Python methods genuinely resist.** A negative about the package's own capability was
published without testing the tool that would have refuted it.

## 7. Grade legitimacy *(challenger D)* — accepted, and already acted on

Five dimensions were graded by a pure string test over the register's own authored columns, with **zero
exceptions in 5,074 rows**; in one case the script **wrote** the qualifying string and **tested for it
thirteen lines later in the same loop**. Gate elements were credited by inheriting a determination made
about a gate that is itself graded not-verified.

**All six retracted. Coverage 44.01% → 21.96%, then 25.39% after `EDGE` was re-derived from the AST
instrument.** The rule adopted: *research-verified requires an instrument outside the register, with a
control that can fail.*

## 8. Two more recurrences of the same governance defect

- **The container repair hard-coded the three identifiers a reviewer had named** — the fourth consecutive round in which this family stated a correction rule and applied it only where a reviewer pointed. This round the rule keys on the **property**, and the population is **54**, not 17.
- **`CRITICAL-GAP-04` was closed at 16 rules; the deployment's own records say 60** — the closure's direction is right and its magnitude understated roughly fourfold. **The closure is re-opened.**
- **`CRITICAL-GAP-03` was closed without naming a single affected element** — no learning ID, no identity, no Critical Area. **No reviewer can audit it. Re-opened on traceability.**

## 9. Confirmations — recorded so their silence is not read as absence of testing

The denominator is derivable from the published rule table, exactly · every movement count reproduces to
the digit (14,441 / 3,680 / 2,431 / 1,249) · the 617 absent items stay absent against a **sixth and
larger** generation-19 registry, with both controls firing · the valuation object's replacement is
confirmed, and the old name is genuinely absent from the current generation · menus and scheduled jobs
are essentially completely carried — 1 exception in 125 · the manifest verifies 75 of 75 · the runtime
tier structure is honest and **materially more conservative** than counting an indirect route as
element-level · the freeze held.

## 10. Disposition

**Round R1 of PREP-004 is INVALIDATED as a baseline.** Its corrections are carried into this package,
which supersedes it. **Two of its published conclusions are retracted, and one premise it had retracted
is restored.**

**Findings: 32. Adopted: 30. Not adopted: 2** — one unlocatable artefact the challenger correctly
declined to declare absent, and one classification whose disposition is right on a wrong stated ground
(recorded, not reversed).

**No challenger approved anything, and none was asked to.**
