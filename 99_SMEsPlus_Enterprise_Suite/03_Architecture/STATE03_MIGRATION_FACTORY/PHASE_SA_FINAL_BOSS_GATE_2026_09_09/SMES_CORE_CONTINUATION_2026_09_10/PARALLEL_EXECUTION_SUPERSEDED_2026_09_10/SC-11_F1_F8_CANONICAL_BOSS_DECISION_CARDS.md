# SC-11 — `F1`–`F8` CANONICAL BOSS DECISION CARDS

## CP-SA-SC-110 — `F1`–`F8` DECISION CARDS COMPLETE

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`
Execution host: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Executing body: **SMEs CORE** · Challenge body: **SMEs CORE specialist roles**
Canonical population: **23 atomic Boss decisions** (`SC-10`)
Boss: **SOLE FINAL APPROVER**

> **NOMENCLATURE.** Active body = **`SMEs CORE`**. Historical artefacts using `SMT` are quoted verbatim
> and marked **`LEGACY NAME — CURRENT BODY = SMEs CORE`**.

> **IDENTIFIER NOTE.** `SC-SMT-01`…`SC-SMT-11` are **historical finding identifiers** minted in `SC-03`
> (published at `2139088b`, before the nomenclature control). They are retained verbatim so citation
> lineage is not severed. **`LEGACY NAME — CURRENT BODY = SMEs CORE`.** They name findings, never the
> active body.

---

## 0. Family labels — verified, and two corrected

The prompt's expected labels were tested against the canonical membership rather than assumed.

| Family | Expected label | **Canonical label** | Why |
|---|---|---|---|
| `F1` | COGS recognition / reversal basis | **unchanged** | membership `JT-04`, `JT-05` matches |
| `F2` | Commercial control-default policy | **unchanged** | |
| **`F3`** | Dropship valuation / **cost landing** | **`Direct shipment (dropship) — valuation only`** | **`C2-D-02`, the cost-landing half, is CLOSED** (`SC-10` §4). Keeping *"cost landing"* in the label would advertise a decision that is no longer asked |
| `F4` | Cross-module contract scope / supply binding | **unchanged** | |
| `F5` | Manufacturing overhead governance | **unchanged** | |
| `F6` | Cross-company visibility / commercial scope | **unchanged** | |
| `F7` | Authorization axis / configurable-record scope | **unchanged** | |
| **`F8`** | Idempotency severity / **gate consequence** | **`Idempotency severity`** | *"Gate consequence"* is the **consequence of the answer**, not a second subject. `C-02` asks one thing: severity. **Whether idempotency is required is already ruled by `BD-ACC-01` and is not asked** |

**Neither correction changes an authority scope.** Both remove wording that would put a settled item back
in front of Boss.

---

## `F1` — COGS RECOGNITION AND REVERSAL BASIS · **2 decisions**

**1. The question.** *Under `BD-ACC-03A`'s `Perpetual`, which business event recognises cost of sales — the
physical movement or the customer invoice (`JT-04`) — and does a customer return reverse cost at the
original cost or the current cost, including how the `Average`-costing difference is reconciled (`JT-05`)?*

**2. Atomic IDs.** `JT-04` · `JT-05`

**3. Why Boss authority.** `08_JT04` §5: *"Final event selection → **Boss**, informed by the above but not
derivable from them alone."* §8 records the source session **rejecting** `DECIDABLE WITH CONTROL` because
`SME-Q-03` is unknown and adopting a control without it *"would be designing blind."* `09_JT05` §5:
*"Final return-cost-basis rule (and the reconciliation-control design for the **`AVCO` admitted gap**) →
**Boss**."*

**4. Existing rulings checked.** `BD-ACC-03A` rules the **values** (`Periodic | Perpetual`) and the
**authority** (Product Category, no Product override). `BD-ACC-03B` the same for `Standard | Average |
FIFO`. `BD-ACC-01` rules that *"Reversal is a new accounting event **referencing** the original accounting
event"* — **the relationship, not the measurement**. **None rules the recognition event.**

> **The premise that a Boss direction already binds COGS to delivery does not hold.** Measured across every
> Boss/ruling/control surface: every hit is a commissioning prompt (*"Is COGS triggered by delivery,
> invoice, or another event…"*), a scope bullet (*"Sales delivery / COGS;"*) or a glossary entry. The
> content exists only as **`ND-10`, an SMEs Core position explicitly recorded as not Boss-approved**
> (`SC-01` §4.3). **No prior Boss freeze is claimed here.**

**5. SMEs Core recommendation.** `JT-04` → **recognition at the business event (physical movement)**, with
`Perpetual` and `Periodic` **defined wherever the terms appear**. `JT-05` → **original cost**.

**6. Best alternative.** `JT-04` → invoice-triggered, which matches the current reference generation's own
label and is simpler where invoicing precedes shipping. `JT-05` → current cost, which keeps the running
average internally consistent at the cost of manufacturing a margin no sale earned.

**7. Dissent / challenge.** CORR5's first freeze adopted `ND-10` **as if `BD-ACC-03A` had ruled it**, and
**two independent challengers falsified that**; the adjudication was withdrawn. *"The executing party's
instinct was to decide this."* **Specialist challenge this round added the live gap:** original-cost
reversal leaves a residual under `Average` costing **that nothing in the recommendation places**, and
`BD-02` closes the destination of *unabsorbed overhead* only — not of a returns-costing difference.

**8. Consequences.**

| Dimension | `JT-04` = movement | `JT-04` = invoice |
|---|---|---|
| Sales / AR | revenue and cost may fall in different periods; the gap is visible and datable | revenue and cost always co-timed; a shipped-not-invoiced order carries no cost |
| Purchase / AP | none | none |
| Inventory | valuation fact emitted at the movement — Inventory is the trigger owner | Inventory holds value until Accounting invoices; **Inventory cannot close independently** |
| Manufacturing | finished-goods issue is the recognition point | recognition detaches from production flow |
| Accounting / Posting | posting date and recognition date differ and **both are already carried** (contract elements 3 and 4) | one date serves both |
| Tax / Payment | **`HOLD / EVIDENCE REQUIRED`** — whether TAS 2 constrains the trigger (`TH-NEW-01`) is **untested**. No statutory claim is made | same `HOLD` |
| SaaS / Tenant / Company | none — identity is Tenant + Company bounded either way | none |
| Audit / Standards | the audit contract carries both dates regardless | same |
| **Pre-Test entry** | **not gating.** Test cases writable now; **expected values pending on 10 of 22 rows** | same |

| Dimension | `JT-05` = original cost | `JT-05` = current cost |
|---|---|---|
| Sales / AR | credit note reverses exactly what the sale recognised | reversal amount differs from the sale's; margin appears with no sale |
| Inventory | requires per-unit original-cost lineage as a **data-model requirement** | no lineage needed |
| Accounting / Posting | `XMC-C-A8` binds the reversal to the original event's identity, so the amount is always recoverable | simpler; loses the tie |
| **Open on both branches** | **the `Average`-costing residual has no named destination.** Boss's ruling should name it or record it as an open element | same |
| Audit / Standards | reversal is provably the sale's own cost | reversal is not tied to the sale |
| Pre-Test entry | not gating | not gating |

**9. Evidence.** `08_JT04` §5/§8 · `09_JT05` §5 · `ND-10` (`SA_CORR2_01`) · `SA_CORR2_12` (its status) ·
`BD-ACC-01`/`03A`/`03B` primary text · `SC-01` §4.2–§4.3 · `SC-03` `SC-SMT-01`, `SC-SMT-02`

**10. Downstream after ruling.** Set expected accounting values on **10 of 22** cross-proof rows and on
`E2E-01`, `-03`, `-11`, `-12`, `-13` · fix the recognition role inside the immutable identity basis
(`XMC-C-A3` part 5) · set the `RC-03` reconciliation posture (continuous under `Perpetual`, at the closing
boundary under `Periodic`) · **name the `Average` residual's destination or record it open** · route
`TH-NEW-01`/`TH-NEW-02` to the Accounting-Tax track · `AAS-V-03`'s COGS-gap limb resolves only if `F6`
also permits a grant.

---

## `F2` — COMMERCIAL CONTROL-DEFAULT POLICY · **3 decisions, one principle**

**1. The question.** *When a commercial control fires and the business has not configured a preference,
does SMEsPlus default to `block`, to `warn-and-allow` into a recorded owed-condition, or to
`allow-silently`?*

**2. Atomic IDs.** `XD1-P1` (sell-side cancellation gate) · `TV6-BOSS-01` (credit exposure at commitment
confirmation) · over-receipt tolerance default

**3. Why Boss authority.** A **risk-appetite election**. `SA_CORR3_00` §5.1: *"both surviving options are
architecturally sound and equally auditable"* — they differ only in whose work the friction lands on. For
`XD1-P1` the owning session **reserved the election to Boss in writing** and the reservation is
undischarged; **SMEs Core may not discharge a reservation it does not hold.**

**4. Existing rulings checked.** **None rules a default.** `ND-03` and `XMC-C-D3` bind the control
**floor**, not the default. `CF-I-07` makes the override company-scoped.

**5. SMEs Core recommendation.** **`block` on all three, ruled once as a principle** — Boss may still split
the ruling.

**6. Best alternative.** `warn-and-allow` with a non-dismissible recorded owed-condition, which keeps
throughput and moves the control to a reconciliation step.

**7. Dissent / challenge.** CORR3 deliberately kept the items separate so as not to conflate
separately-evidenced elections; this pack combines them and **states the separation so Boss can still
split**. **Specialist challenge added `M-6`**: without it, a configuration could suppress the control event
and turn `warn-and-allow` into `allow-silently` **without anyone electing it**.

> **The mechanism is now fully specified on every branch, so the election carries no unspecified
> consequence.** `M-1` every firing emits an event · `M-2` an allowed breach records a **non-dismissible**
> owed-condition carrying who, when, on what basis · `M-3` override is Company-scoped, default is
> platform-owned · `M-4` no override may lower a control **floor** · `M-5` the audit record has the **same
> shape** on both branches · **`M-6` the event's *emission* is not configurable; only the control's
> *outcome* is.**

**8. Consequences.**

| Dimension | `block` | `warn-and-allow` |
|---|---|---|
| Sales / AR | a sell-side cancellation is refused while a blocking invoice state stands; friction at the moment | cancellation proceeds; an owed-condition is raised against the invoice |
| Purchase / AP | over-receipt above the ordered quantity is refused at the dock | receipt recorded with an evented exception and a reason class |
| Inventory | **stock truth cannot be corrupted before a control sees it** | stock truth moves first; the exception is the record |
| Manufacturing | consumption beyond commitment refused | permitted with a recorded condition |
| Accounting / Posting | fewer corrective entries; more refused transactions | more reversal/correction entries, each evented |
| Tax / Payment | sell-side cancellation carries a statutory element the buy-side gate never protected | that element becomes a recorded exposure rather than a prevented one |
| SaaS / Tenant / Company | default platform-owned; override company-scoped (`M-3`) | identical |
| Audit / Standards | strongest posture; nothing to reconcile | **sound only because `M-1`/`M-2`/`M-6` forbid silence** |
| **Pre-Test entry** | **not gating** — both branches testable; the suite writes the branch Boss rules | same |

**9. Evidence.** `SA_CORR3_01` §§5–12, §14.3 · `SA_CORR3_12` `B-1` · `SA_CORR2_05` (returns **0** for
tolerance/over-receipt — nothing to find, only something to elect) · `SC-01` §5 · `SC-03` `SC-SMT-06`

**10. Downstream after ruling.** Set the platform default for all three controls · specify the
company-scoped override surface · **implement `M-1`…`M-6` on whichever branch is ruled** · write the
Pre-Test assertions for the unconfigured case, which is the commonest case in a new tenant.

---

## `F3` — DIRECT SHIPMENT (DROPSHIP) — VALUATION ONLY · **1 decision, conditional**

**1. The question.** *Does `BD-ACC-03A`'s Product-Category valuation authority reach a route with **no
internal end** — or does a supplier→customer direct shipment carry a route-specific exception that emits no
valuation facts?*

**2. Atomic ID.** `XMC-D-01` — **conditional: it arises only if Boss prefers option (b).**
**`C2-D-02` is CLOSED** (`SC-10` §4) and is **not** asked.

**3. Why Boss authority.** **Only on the non-recommended branch.** Option (b) requires Boss to state that
`BD-ACC-03A` does **not** reach this route — a scope statement about a Boss ruling, governed by `CF-D-01`:
*"only Boss may state what a Boss ruling covers."* **Option (a) requires nothing of Boss: it applies
`BD-ACC-03A` as ruled.**

**4. Existing rulings checked.** `BD-ACC-03A` (Product Category authority, no Product override) · its
covering ruling: *"v18/v19/source-generation identity is **Evidence Provenance, not a SMEsPlus
target-platform decision**"* · `BD-ACC-01` · `XMC-C-C6` · `XMC-F-03`.

**5. SMEs Core recommendation.** **Option (a)** — the direct-shipment route resolves a movement chain and
its valuation facts arise under **the product category's ruled policy**, with **no route-specific
exception**. On this branch **`F3` leaves the Boss decision list entirely**.

**6. Best alternative.** Option (b) — no movement/valuation facts, with the cost bound to the sale by the
accounting event identity directly and a recorded determination under `XMC-C-C6`.

**7. Dissent / challenge — and the clean-room finding that decides the weight of the evidence.**

> **The reference's direct-shipment capability is installed in `0` of 3 readable deployments**, measured on
> two differently-shaped instruments — the deployed module registry, and an independent expert's
> transaction-population control. **Every direct-shipment "fact" in the corpus is therefore source-derived
> from a capability no deployment runs**, and the two readings the parent called *"both consistent with
> every fact in the corpus"* are **one vendor's implementation choice and its reversal between generations**.
>
> **No vendor implementation choice becomes SMEsPlus policy without independent rationale.** The
> recommendation rests on SMEsPlus's own instruments — `XMC-F-03` (*"…**direct shipment from supplier to
> customer**; and manufacture — **and the system resolves the movement chain from that choice**"*) and
> `BD-ACC-03A` — **not on either generation.**
>
> **Published weakness:** *"resolves the movement chain"* does not by itself exclude resolving to a
> **zero-length** chain. **`XMC-F-03` is strong evidence, not a proof.**
>
> **Withdrawn argument:** an earlier draft eliminated option (b) via `XMC-C-C6`. **That was wrong and was
> withdrawn against `C6`'s own text** — `C6` forbids *silence*, and option (b) is not silence.
>
> **Specialist condition, accepted:** option (a) must specify the location semantics of a movement with no
> internal end. **Closed in-session:** the location context is the **counterparty pair** — supplier origin
> and customer destination — recorded as **external endpoints with reason**, not `N/A`.

**8. Consequences.**

| Dimension | (a) valuation facts arise — recommended | (b) no valuation facts + recorded determination |
|---|---|---|
| Sales / AR | revenue, receivable and tax as any sale; cost bound to the same identity | identical on the revenue side |
| Purchase / AP | the vendor bill settles a liability; it is **not** the cost's binding point | same — `C2-D-02` closed this on both branches |
| Inventory | a direct-shipment line **creates movement facts**, with external endpoints | **no movement facts**; Inventory has no record of goods it never held |
| Manufacturing | none | none |
| Accounting / Posting | cost recognised under the category's ruled policy | cost recognised via the accounting event identity, with a recorded determination as the audit artefact |
| Tax / Payment | unchanged; `BD-ACC-02` company scope holds | unchanged |
| SaaS / Tenant / Company | none | none |
| Audit / Standards | no exception class to maintain or test | **the recorded determination must be evented**, and every future no-internal-end route raises the question again |
| **Pre-Test entry** | **not gating** either way | not gating |

**9. Evidence.** `SC-02` (whole file) · `XMC-F-03` · `XMC-C-C6` · `BD-ACC-01`, `BD-ACC-03A` primary text ·
`P01_TRANSITIVE_MODULE_POPULATION` §3 · `P01_S16` §1 · `P01_S16_AAS03` · `P02` `TC-31`, `S-01` ·
`SC-03` `SC-SMT-04`, `SC-SMT-10`

**10. Downstream after ruling.** On (a): no act — the ruled policy applies; specify the external-endpoint
semantics in the handoff contract's element 9 · `E2E-05`'s two named breaks close · row 18's carve-out
resolves. On (b): Boss's scope statement is recorded against `BD-ACC-03A`; the recorded-determination
object is commissioned and evented; `E2E-05` keeps a named break.

> **`SC-BOSS-LEVER-01` on this card's face.** `C2-D-02` was closed by SMEs Core on `BD-ACC-01` +
> `XMC-C-C6`. **If Boss judges the binding identity a policy election, `C2-D-02` is reinstated and the
> canonical count is `24`, not `23`.** One word from Boss; no further work from anyone.

---

## `F4` — CROSS-MODULE CONTRACT SCOPE AND SUPPLY BINDING · **2 decisions · one gates Pre-Test entry**

**1. The question.** *Does the Boss-approved 16-element handoff contract govern **every** cross-module
boundary or only Inventory → Accounting (`XMC-D-02`)? And when a manufacturing shortage raises supply, is
the fulfiller hard-bound or soft-bound (`C2-D-01`)?*

**2. Atomic IDs.** `XMC-D-02` · `C2-D-01`

**3. Why Boss authority.** The contract's approved scope is unambiguous at primary text — *"every material
handoff **from Inventory Core to Accounting Core**"* — **one boundary, one direction.** Widening it
**amends a Boss-approved control**. `C2-D-01` is assigned *"SMEs Core design position → **Boss confirm**"*.

**4. Existing rulings checked.** The handoff-contract approval §1 (scope), §3 (the 16 elements and the
`N/A` + reason rule), §4 (the `PASS / VERIFIED` gate) · `XMC-C-D2` · `XMC-C-D4`.

**5. SMEs Core recommendation.** **`XMC-D-02` → EXTEND, as ONE general contract with declared per-boundary
applicability** — not twelve bespoke contracts, and not verbatim extension. **`C2-D-01` → confirm soft
binding.**

> **The finding that decides it: 13 of the 16 elements are domain-general.** Only unit of measure,
> product/lot/serial and warehouse/location are stock-shaped — **and the contract already handles that
> itself** with `N/A` **plus reason**. **The contract's *content* is domain-general; only its approved
> *scope* is domain-specific, and no deliberate architecture rationale for that limitation was found.**
>
> **Specialist condition, accepted and material:** if the **boundary owner** declares which elements apply,
> a boundary can exempt itself from what it finds inconvenient. **Closed in-session: an applicability
> declaration is part of the contract amendment and carries the same authority as the contract. A boundary
> may *propose*; it may not *declare*.**

**6. Best alternative.** Leave the contract at one boundary and give each further boundary its own contract
as it matures — lower immediate cost, at the price of twelve vocabularies for one property.

**7. Dissent / challenge.** None outstanding on `XMC-D-02`. On `C2-D-01`, the source sentence's second
clause — *"a shortage can therefore be entered and never left by supply"* — was suppressed by one round and
restored by its own challenge. **SMEs Core specifies the supply-raised exit as a defect fix.**
**Deliberately NOT done:** `E2E-04` is **not** re-graded `TRAVERSABLE`; reversing a challenge-produced
withdrawal on this session's own specification is held for the independent reviewer.

**8. Consequences.**

| Dimension | `XMC-D-02` = extend | `XMC-D-02` = leave at one boundary |
|---|---|---|
| Sales / AR | the sell-side handoff gains provenance, both dates, original-event and idempotency identity | it keeps none of them contractually |
| Purchase / AP | same gain on the buy-side boundary | same loss |
| Inventory | unchanged as producer; gains contracted consumers | unchanged |
| Manufacturing | the shortage/supply boundary becomes contracted | stays uncontracted |
| Accounting / Posting | **12 boundaries carry elements 1–16 with declared applicability** | **1 boundary; eleven mandated handoffs have no element contract** |
| Tax / Payment | tax-bearing handoffs gain company/tenant carriage contractually | unchanged |
| SaaS / Tenant / Company | `HF-CTX-01`/`-02` mandatory carriage extends to eleven more boundaries | unchanged |
| Audit / Standards | attestation obligations (`HF-CTX-06`, `-11`) scale to 12; **`XMC-C-D2` satisfied** | **a rule addressed to receivers with no element capable of satisfying it — `XMC-C-D2` says that is not a rule** |
| **Pre-Test entry** | **GATING.** The Matrix is built over **12** boundaries from the start | **GATING.** Built over **1**, and eleven discovered later — a re-scope, not an increment |

| Dimension | `C2-D-01` = soft binding (recommended) | `C2-D-01` = hard binding |
|---|---|---|
| Inventory / Manufacturing | shortage raises a demand; no named party is obligated | a named fulfiller carries an obligation |
| Accounting / Posting | no commitment liability arises from a shortage | a commitment may need recognition |
| **On both branches** | **the shortage state gains a supply-raised exit** — specified by SMEs Core as a defect fix, not an election | same |
| **Pre-Test entry** | not gating | not gating |

**9. Evidence.** handoff-contract approval §1/§3/§4 primary text · `SA_CORR2_02` §6 · `SA_CORR2_03` §3.1
(*"Hard trigger, soft binding"*, `FACT VERIFIED`) · `XMC-C-D2`, `XMC-C-D4` · `SC-01` §6 · `SC-03`
`SC-SMT-08`, `SC-SMT-09`

**10. Downstream after ruling.** On extend: publish the applicability declaration per boundary **at
contract authority** · scope the Pre-Test Matrix to **12** boundaries · extend `HF-CTX-01`/`-02` carriage
and `HF-CTX-06`/`-11` attestation. On `C2-D-01`: record the confirmed binding strength · implement the
shortage state's supply-raised exit · **the `E2E-04` traversability re-grade is for the independent
reviewer, not for SMEs Core.**

---

## `F5` — MANUFACTURING OVERHEAD GOVERNANCE · **6 decisions**

**1. The question.** *Restate or confirm `BLK-07`, `BLK-08` and the standing veto's limb 2 in the form the
evidence supports (`POH-D-06`), and rule the five policy elections beneath them.*

**2. Atomic IDs.** `POH-D-06` (the governance act, **two named subjects — `BLK-07`, `BLK-08` — with veto
limb 2 appended to the same request**) · `POH-D-01` · `POH-D-02` · `POH-D-03` · `POH-D-04` · `POH-D-05`

**3. Why Boss authority.** *"**Governance act.** A Boss-owned blocker can only be retired, restated or
confirmed by Boss."* `POH-D-01` **modifies a standing Boss decision** (`BD-04`). `POH-D-02` *"changes the
charge itself, is an accounting-policy election, has **unresearched tax consequences**."*

**4. Existing rulings checked.** **`BD-02` — the destination of unabsorbed overhead is already CLOSED by
Boss.** `BD-04` — one allocation driver per configuration context, which `POH-D-01` proposes to depart
from. The three SMEs Core design gaps beneath the blocker (`POH-G-01` pool + denominator + capture,
`POH-G-02` receiver, `POH-G-04` variance) were **closed at specification level at CORR5**.

**5. SMEs Core recommendation.** **Restate.** Confirm **normal capacity** as the absorption denominator —
*"it comes from statute, not from analysis preference"* — confirm the `BD-04` departure per cost class, and
put the live election before Boss as **`POH-D-02`: straight-line vs units-of-production absorbed at normal
capacity**, with its tax consequences unresearched and stated.

**6. Best alternative.** Re-affirm the original binary, or retire `BLK-07` and carry only `POH-D-02`.

**7. Dissent / challenge.** **`BLK-07` as worded is unanswerable**: its §3 states *normal capacity or actual
hours* and **its own §6 already rejected the second branch by name** — *"`REJECTED — INVALID ASSUMPTION` …
breaches TAS 2 ¶13, undefined at zero output, capitalises idleness into inventory."* **Specialist condition,
accepted:** the over-absorption cap's **strength** remains a declared statutory dependency under `HOLD`, and
**the `HOLD` travels on the same line as the confirmation**.

> **Two consequences of `POH-D-06` that no prior round has carried** (`SC-08` §4.1, from primary source):
>
> 1. **`POH-D-06` is not a Boss-only act.** `POH-F-06`: *"**Restating a veto limb is reserved to the veto's
>    issuer and Boss.**"* Its limb-2 component needs **AAS+ as issuer** as well as Boss. **Boss ruling
>    `POH-D-06` alone does not complete the restatement it requests.**
> 2. **`POH-F-06`: *"Deciding `BLK-07` alone would not lift the veto."*** **Ruling `F5` does not discharge
>    the standing manufacturing veto.** A reader could reasonably have assumed it does.

**8. Consequences.**

| Dimension | Restate (recommended) | Re-affirm the original binary |
|---|---|---|
| Sales / AR | none | none |
| Purchase / AP | none | none |
| Inventory | WIP value composition gains the absorbed-overhead component | unchanged, and the component stays unspecified |
| Manufacturing | absorption runs at normal capacity; the live method election is visible as `POH-D-02` | **Boss chooses between an option and one his own register rejected by name** |
| Accounting / Posting | variance owner, mechanism and destination follow; **`BD-02` already fixes under-absorption's destination** | the variance stays an event with no owner |
| Tax / Payment | **`POH-D-02`'s tax consequences are unresearched — `HOLD / EVIDENCE REQUIRED`.** Over-absorption cap strength is a statutory `HOLD` | same, and undisclosed |
| SaaS / Tenant / Company | capacity register is company-scoped; operation classes platform-owned | unchanged |
| Audit / Standards | per-pool closure identity is the publication gate; a non-zero residual raises and never re-absorbs | unchanged |
| **Pre-Test entry** | **not gating.** Two rows keep an expected-value gap either way | same |

**9. Evidence.** `SA_CORR3_03` `POH-D-01`…`-06`, `POH-F-06`, `POH-F-12`, `POH-F-16` primary text ·
`SA_CORR5_10A` · `BD-02`, `BD-04` · `SC-01` §7.1 · `SC-03` `SC-SMT-11` · `SC-08` §4

**10. Downstream after ruling.** Publish the restated `BLK-07`/`BLK-08` · **obtain AAS+'s concurrence for
the limb-2 restatement — Boss's ruling alone does not complete it** · set the numeric absorption expectation
on 2 cross-proof rows and `E2E-03`, `-13`, `-17` · route `POH-D-02`'s tax consequences to the
Accounting-Tax track · **note that the standing veto is not lifted by this ruling.**

---

## `F6` — CROSS-COMPANY VISIBILITY AND COMMERCIAL SCOPE · **4 decisions · one gates Pre-Test entry**

**1. The question.** *Does a sanctioned cross-company **read** exist inside a tenant at all (`MTI-D-04`);
who owns the mapping layer (`RC-D-04`); what escalates a tenant to the Private Company model (`RC-D-03`);
and is a product's base sell price a tenant fact or a company fact (`TV6-BOSS-02`)?*

**2. Atomic IDs.** `MTI-D-04` · `RC-D-03` · `RC-D-04` · `TV6-BOSS-02`

**3. Why Boss authority.** *"A real Thai SME group need, and a deliberate hole in an isolation boundary.
**Only Boss may authorise a door.**"* The other three are the door's consequences and one commercial scope
election.

**4. Existing rulings checked — and the statutory scope is confirmed NOT re-asked.** **`BD-ACC-02` closes
cross-company statutory posting, offsetting, settlement, aggregation and filing authority, and permits
multi-company management/informational views.** **All 4 members sit on the management-information side of
that line; `0 of 4` re-ask closed statutory scope**, and the recommendation moves **away** from the
boundary. `MTI-D-01`/`-02`/`-03` ruled; `MTI-22` is the only permitted cross-company means.

**5. SMEs Core recommendation.** `MTI-D-04` → **no cross-company grant in v1**; the group-view need is met
by **per-company export**, which becomes the **designed** answer rather than the informal one.
`TV6-BOSS-02` → **company-scoped**.

**6. Best alternative.** A read-only enumerated grant with grant identity, granting authority, scope,
expiry and a log entry per use.

**7. Dissent / challenge.** Recorded counter-argument: *"Not deciding is not neutral — the need gets met by
export, which is the worst outcome."* **Specialist consequence surfaced this round:** `MTA-11` records that
**every grant mechanism degrades toward permanence** and that **no review cadence is designed anywhere**.
**On any grant-permitting branch Boss would be ruling an undesigned review obligation into existence.**

**8. Consequences.**

| Dimension | `MTI-D-04` = no grant in v1 (recommended) | `MTI-D-04` = enumerated read-only grant |
|---|---|---|
| Sales / AR | group views assembled outside the system by export | live cross-company commercial visibility |
| Purchase / AP | same | same |
| Inventory | the mapping/provenance object (`RC-D-04`) is **not commissioned** | it must be commissioned and owned |
| Manufacturing | none | none |
| Accounting / Posting | **`BD-ACC-02`'s boundary is unaffected either way** | unaffected — but the grant must be provably non-posting |
| Tax / Payment | no cross-company statutory path exists to misuse | the grant must be provably incapable of carrying statutory content |
| SaaS / Tenant / Company | **the company boundary has no sanctioned crossing.** `CF-XCR-GAP-01` stays un-numbered, correctly | **a deliberate hole exists**; `XCR-02` needs identity, authority, scope, expiry and per-use logging |
| Audit / Standards | nothing to review periodically | **an undesigned review cadence, on a mechanism that degrades toward permanence** |
| **Pre-Test entry** | **GATING — and it resolves cleanly.** `CF3-P-04` is **struck**; the isolation suite's exception set is **empty and known** | **GATING.** `CF3-P-04` needs test data that does not yet exist |
| **Vetoes** | **`AAS-V-03` becomes vacuous; `CF-V-02`'s first limb closes** | **`AAS-V-03`'s COGS-gap limb survives and `F1` must also be ruled** |

**9. Evidence.** `BD-ACC-02` primary text · R1 `11` (*"Only Boss may authorise a door"*) · `XCR-02`,
`CF-XCR-GAP-01`, `MTI-22`, `MTA-11` · `SC-01` §8 · `SC-03` `SC-SMT-05` · `SC-04` §3

**10. Downstream after ruling.** On *no grant*: strike `CF3-P-04`; record the export route as the designed
answer; **notify AAS+ that `AAS-V-03`'s subject has ceased to exist and `CF-V-02`'s first limb is closed —
discharge remains AAS+'s act.** On *grant*: commission `XCR-02` with its five attributes **and a review
cadence that does not yet exist anywhere**; number `CF-XCR-GAP-01`; rule `F1` as well.

---

## `F7` — AUTHORIZATION AXIS AND CONFIGURABLE-RECORD SCOPE · **4 decisions · one gates Pre-Test entry**

**1. The question.** *Is `location` an authorization axis (`RC-D-01`)? What closes the configurable-record
enumeration (`RC-D-02`)? Is `MTI-D-03`'s "Unit of Measure Category" the same object as the context matrix's
"Unit group and unit" (`CF-D-01`)? What closes the platform-owned operation-class enumeration (`CF-D-02`)?*

**2. Atomic IDs.** `RC-D-01` · `RC-D-02` · `CF-D-01` · `CF-D-02`

**3. Why Boss authority.** `CF-D-01`'s ground is decisive and general: ***"only Boss may state what a Boss
ruling covers."*** The other three close enumerations that Boss rulings opened.

**4. Existing rulings checked.** **`MTI-D-02` ruled `AUTH` = Company + Warehouse + Operation-Type, and
`location` is not among them.** `MTI-D-03` names the tenant-changeable boundary.

**5. SMEs Core recommendation.** **As the registers state; no new position is originated.** What is new is
the denominator:

> **DECLARED PRE-TEST DENOMINATOR, in both halves.**
> **Denial enumeration: 3 axes — Company, Warehouse, Operation-Type.** `S-01`…`S-08` enumerate over these.
> **Positive complement: INVERTS** if a 4th axis is ruled in — cases asserting *access allowed across
> locations* become **denials**.
>
> **A reading that made `RC-D-01` non-entry-gating was drafted and withdrawn**: adding an axis is **not**
> purely additive, so it is a **re-scope**, not an increment. **`RC-D-01` remains entry-relevant.**

**6. Best alternative.** `CF-D-02` in particular: close at the eight illustrated classes with an addition
process · derive from the `INV-F-*` function set · rule that no platform class exists and **withdraw
`CF-I-05` entirely**.

**7. Dissent / challenge.** None outstanding. Specialist challenge required both halves of the denominator
to be stated, because declaring only the denial half is the wrong-denominator class the programme has
recorded repeatedly.

**8. Consequences.**

| Dimension | `RC-D-01` = location IS an axis | `RC-D-01` = location is NOT an axis (as ruled today) |
|---|---|---|
| Sales / AR | pickers/sellers can be confined below warehouse | confinement stops at warehouse |
| Purchase / AP | same | same |
| Inventory | **location becomes an authorization boundary as well as a record anchor** | location anchors records only (`CTX`) |
| Manufacturing | operation access can be location-confined | not |
| Accounting / Posting | indirect, through the operation-class binding of controls | same |
| Tax / Payment | none | none |
| SaaS / Tenant / Company | a finer confinement axis inside a company | the ruled three-axis tuple stands |
| Audit / Standards | **`AUD-C-A5`** (the situational location axis) resolves; `CF-I-03` `D5`'s domain widens | `AUD-C-A5` stays situational |
| **Pre-Test entry** | **GATING.** The denial set grows **and the positive complement inverts** | **GATING.** The suite is written over the ruled 3 |

**9. Evidence.** `MTI-D-02`, `MTI-D-03` rulings · `CF-I-01`, `CF-I-05`, `CF-I-07` · `AUD-C-A5` ·
`SC-01` §7.2 · `SC-03` `SC-SMT-07`

**10. Downstream after ruling.** Fix the axis set and **write both halves of the negative-access suite** ·
close `CF-I-05`'s and `CF-I-07`'s conditional status · settle `MTI-05` row 17's remaining anchor ·
`RC-V-01`'s under-inclusive condition touches the same rows and the wider five-row set still governs.

---

## `F8` — IDEMPOTENCY SEVERITY · **1 decision**

**1. The question.** *Is the absence of a deterministic idempotency identity **gate-blocking**, or a design
input that a phase may pass with?*

**2. Atomic ID.** `C-02`

**3. Why Boss authority.** Owner *"Boss directly"* on multiple instruments, including **the SMEsPlus-owned
functional design itself** — *"Carried finding `C-02`: whether this is gate-blocking is Boss's decision."*
*(The parent claimed five instruments; AR re-verified the phrase at two and stated so. **A claim of five
checked at two is not repeated as five.**)*

**4. Existing rulings checked — the object is ruled and is NOT re-asked.** **`BD-ACC-01`: *"Same-event
retry must not create duplicate accounting events"*, and the Accounting Core owns the identity.**
**`UAE-29`, the Account programme's root blocker, is thereby ruled.** `C-02` asks **severity only**.

**5. SMEs Core recommendation.** **(b) design input, not phase-holding.**

> **The ground, stated rather than assumed.** Specialist challenge asked *who determines when idempotency is
> required* — if undefined, the protection this recommendation leans on is **vacuous**. **`BD-ACC-01`'s
> sentence is unqualified: for accounting events, idempotency is always required.** The handoff contract §4
> condition is therefore always met, and the duplicate-prevention precondition on `PASS / VERIFIED` **exists
> one level down** on a stated ground.

**6. Best alternative.** (a) gate-blocking — no phase closes while element 15 is unproven.

**7. Dissent / challenge.** **CORR5's first freeze declared this dissolved by standing rulings and two
challengers independently reversed it** — a commissioning prompt is not a ruling. **It is presented as open
precisely because the executing party twice tried to close it.**

**8. Consequences.**

| Dimension | (b) design input — recommended | (a) gate-blocking |
|---|---|---|
| Sales / AR | none to the specification | no phase closes until proven |
| Purchase / AP | none | same |
| Inventory | none — `MTI-31` and `XMC-C-A14` stand either way | same |
| Manufacturing | none | same |
| Accounting / Posting | none to the specification; **the estate's only carrier is table-global and populated on `0` of 13,814 rows, so a uniqueness test over it passes on every row** | the same fact becomes gate-blocking |
| Tax / Payment | none | none |
| SaaS / Tenant / Company | none | none |
| Audit / Standards | duplicate prevention is enforced at scenario level by contract §4 | **no gate may close until `RT-E15-01`…`-09` execute** |
| **Pre-Test entry** | **not gating — but it sets Pre-Test *exit* criteria** and should be ruled before those are agreed | **entry and exit both blocked**; element 15 is the join key, so **every** row is affected |

**9. Evidence.** `BD-ACC-01` primary text · handoff-contract §4 primary text · `E15-A1`, `XMC-C-A14` ·
`03_INVENTORY_FUNCTIONAL_DESIGN_V1` · `SC-01` §2 · `SC-03` `SC-SMT-03`

**10. Downstream after ruling.** On (b): element 15's proof becomes a Pre-Test/build obligation; **agree
Pre-Test exit criteria against this ruling before the Matrix is scoped**. On (a): `RT-E15-01`…`-09` must
execute before any gate closes, and Phase SA cannot exit until element 15 is built.

---

## Checkpoint

> ## `CP-SA-SC-110 — F1–F8 DECISION CARDS COMPLETE`
> **8 cards · **23** atomic decisions, membership summing exactly to the canonical count · 2 family labels
> corrected on membership grounds, **0** authority scopes changed · all 10 required elements per card ·
> consequences stated across all 9 dimensions · **3 entry-gating members** identified (`XMC-D-02`,
> `MTI-D-04`, `RC-D-01`) · **2 `F5` consequences surfaced that no prior round carried** · **1 Boss reversal
> lever published on the `F3` card** · no vendor implementation treated as SMEsPlus policy · **no prior Boss
> COGS freeze claimed**.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
