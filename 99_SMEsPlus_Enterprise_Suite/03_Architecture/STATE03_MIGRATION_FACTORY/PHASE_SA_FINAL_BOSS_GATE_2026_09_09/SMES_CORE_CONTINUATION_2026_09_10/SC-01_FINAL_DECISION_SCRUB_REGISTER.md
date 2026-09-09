# SC-01 — FINAL DECISION SCRUB REGISTER (`F1`–`F8`)

## CP-SA-SC-10 — F1–F8 AUTHORITY SCRUB COMPLETE

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`
Branch: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Input population: the **26 decisions in 8 families** of `SA_FINAL_03` (parent `9d5bc2db`), taken as an
**input population, not as automatically Boss-bound questions** (master prompt §4).
Boss: **SOLE FINAL APPROVER**

---

## 1. Result

### 1.0 The count unit, declared before any number

**UNIT: one atomic Boss decision as `SA_FINAL_02` §2/§3 counts them** — the 32-candidate decomposition less
1 relocated and 5 acts, giving **26**. On that unit `F5` is **8** (three restatement subjects plus
`POH-D-01`…`POH-D-05`), **not** the *"six decisions"* its own family card states. **The two readings are both
in the parent and they differ**; this register uses the one the 26 is built from, so the delta is comparable.
Mixing them is the programme's recorded count-unit-vs-population defect and is the reason the unit is
declared before the total rather than after it.

| Measure | Parent (`9d5bc2db`) | **After this scrub** |
|---|---:|---:|
| Boss decisions on the Phase SA list | **26** | **25** |
| — of which **conditional** (arise only on a non-recommended branch) | 0 | **1** (`XMC-D-01`) |
| Decisions **closed** | — | **1** (`C2-D-02`) |
| Decisions **materially narrowed but not removed** | 2 | **9** (§1.1) |
| Families with **no** SMEs Core recommendation | **1** (`F3`) | **0** |
| Families carrying a Boss decision | 8 | **8** |
| Pre-Test **entry**-gating members | 3 | **3** — unchanged; §7.2 records why the reading that reduced it was withdrawn |
| New Boss decisions originated | 0 | **0** |
| Boss **acts** (not decisions) | 5 | **5** — unchanged |

### 1.1 The nine narrowed decisions, enumerated rather than asserted

`JT-04`, `JT-05` — by the four-event separation (§4.2) · `XD1-P1`, `TV6-BOSS-01`, over-receipt tolerance —
by the five mechanism invariants binding on every branch (§5) · `XMC-D-01` — reduced to a **conditional**
scope question (`SC-02`) · `XMC-D-02` — a direct recommendation with its rationale and cost (§6.1) ·
`C2-D-01` — its shortage-exit half closed as a defect (§6.2) · `BLK-07` — restated to the live choice set
with the invalidated branch removed (§7.1). **Nine.**

### 1.2 What this scrub did **not** achieve, stated plainly

> **The count moved by one.** `26 → 25`. Eight of the nine narrowings **change what Boss is deciding, not
> whether Boss decides it**, and the ninth is conditional rather than removed.
>
> **As at the parent round, `0 of 26` were wrongly escalated on authority.** A first draft of this file
> reported `26 → 22` by counting `F5` as 6 while the parent's 26 counts it as 8, and by counting two
> **specification acts** — `F2`'s mechanism invariants and `C2-D-01`'s shortage exit — as **closures**.
> They are not: both narrow a decision that Boss still owns. **`SC-F-02`, corrected in place.** The
> flattering number was available, was written, and did not survive its own arithmetic check.

---

## 2. The scrub register

Columns are master prompt §4's required set.

| Family | Original IDs | SMEs Core closable | SMT required | Targeted research required | Existing Boss ruling applicable | **Remaining Boss-only decision** | SMEs Core recommendation | Evidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| **`F1`** COGS recognition & reversal basis | `JT-04`, `JT-05` | **NO** — `08_JT04` §8 primary: `NOT DECIDABLE`; adopting a control without `SME-Q-03` *"would be designing blind"* | **YES** — Accounting / Thai Accounting-Tax | **NO** — §4.1: the two missing inputs are a **business-SME fact** and a **Thai statutory fact**; neither is answerable by research into the reference corpus | **PARTIAL** — `BD-ACC-03A`/`03B` rule the values and their authority; `BD-ACC-01` rules that reversal **references** the original event. **None rules the recognition event** | **2** — the recognition event (`JT-04`) and the return cost basis incl. the Average-costing reconciliation (`JT-05`) | `JT-04` → recognition at the **business event**, with `Perpetual`/`Periodic` **defined wherever they appear** (`ND-10`). `JT-05` → **original cost** | `08_JT04` §5/§8 · `09_JT05` §5 · `ND-10` (`SA_CORR2_01`) · `BD-ACC-01` primary text | **BOSS — 2, narrowed by the event-model separation at §4.2** |
| **`F2`** Commercial control-default policy | `XD1-P1`, `TV6-BOSS-01`, over-receipt tolerance default | **PARTIAL — the mechanism, YES** (§5). The **default value**, no | **YES** — Internal Control / Audit | **NO** — `SA_CORR2_05` returns **0** for tolerance/over-receipt in the corpus; there is nothing to find, only something to elect | **NO** — `ND-03` and `XMC-C-D3` bind the control **floor**, not the default | **3** — the default posture on each member. **One principle answers all three**, but on the unit declared at §1.0 they remain three decisions | **`block`** on all three, ruled once; **and the mechanism invariants at §5 hold on every branch** | `SA_CORR3_01` §§5–12 · `SA_CORR3_12` `B-1` · `SA_CORR2_05` | **BOSS — 3, mechanism specified so the election carries no unspecified consequence** |
| **`F3`** Direct shipment (dropship) | `XMC-D-01`, `C2-D-02` | **`C2-D-02` YES — CLOSED** by `XMC-C-C6` + `BD-ACC-01`. `XMC-D-01` narrowed | **YES** — Inventory, Accounting, Cross-Module | **NO — and the prescribed re-read was performed instead** (`SC-02`) | **YES** — `BD-ACC-01`, `BD-ACC-03A`, and `BD-ACC-03A`'s covering ruling that generation identity is *"Evidence Provenance, not a SMEsPlus target-platform decision"* | **1, conditional** — a **scope statement on `BD-ACC-03A`**, required **only** on the non-recommended branch | **(a)** the movement chain emits valuation facts under the product category's ruled policy; no route-specific exception | `SC-02` · `XMC-F-03` · `XMC-C-C6` · `P01_TRANSITIVE_MODULE_POPULATION` §3 · `P01_S16` §1 · `P02` `TC-31`/`S-01` | **NARROWED — 1 conditional** (was 2 unconditional, no recommendation) |
| **`F4`** Cross-module contract scope & supply binding | `XMC-D-02`, `C2-D-01` | **The shortage-exit half YES** (§6.2). Contract scope **NO** — it amends a Boss-approved control | **YES** — Cross-Module Integration, Inventory | **NO** — `XMC-D-02` is *"nothing to research; something to decide"*; the binding position is already stated and `FACT VERIFIED` | **YES** — the handoff-contract approval §1, whose scope at primary text is *"every material handoff **from Inventory Core to Accounting Core**"* — **one boundary, one direction, unambiguous** | **2** — extend the contract's scope (an amendment); confirm **soft** binding | **`XMC-D-02` → extend, as one general contract with declared per-boundary applicability — not twelve bespoke contracts** (§6.1). **`C2-D-01` → confirm soft binding** | handoff-contract approval §1/§3/§4 · `SA_CORR2_02` §6 · `SA_CORR2_03` §3.1 · `XMC-C-D2`, `XMC-C-D4` | **BOSS — 2, one narrowed** |
| **`F5`** Manufacturing overhead governance | `POH-D-06` (covering `BLK-07`, `BLK-08`, veto limb 2), `POH-D-01`…`POH-D-05` | **NO** — *"A Boss-owned blocker can only be retired, restated or confirmed by Boss"* | **YES** — Manufacturing/Costing, Thai Accounting-Tax | **NO for the corpus.** `POH-D-02`'s **tax consequences are unresearched and are a Thai statutory item** under standing `HOLD / EVIDENCE REQUIRED` — routed, not researched here | **YES** — `BD-02` already closes the **destination of unabsorbed overhead**; `BD-04` is the decision `POH-D-01` proposes to depart from | **8** on the unit declared at §1.0 — three restatement subjects plus five elections (`POH-D-06` is the restatement *act*, not a ninth) | **Restate.** The live choice set is reduced to the **three live options** at §7.1; the invalidated branch is removed from the paper rather than re-offered | `SA_CORR3_03` `POH-D-06` · `POH-F-12` · `SA_CORR5_10A` · `BD-02`, `BD-04` | **BOSS — 8** (unchanged count, **restated so no dead branch is offered**) |
| **`F6`** Cross-company visibility & commercial scope | `MTI-D-04`, `RC-D-03`, `RC-D-04`, `TV6-BOSS-02` | **NO** — *"Only Boss may authorise a door"* | **YES** — SaaS/Multi-Company, Internal Control | **NO** | **YES — and it is decisive on the statutory half.** `BD-ACC-02` already closes cross-company **statutory** posting/offset/settlement/aggregation/filing. §8 confirms **this family re-asks none of it** | **4** — all on the **management-information** side of `BD-ACC-02`'s boundary, none on the statutory side | `MTI-D-04` → **no cross-company grant in v1**; `TV6-BOSS-02` → **company-scoped** | `BD-ACC-02` primary text · R1 `11` · `XCR-02`, `CF-XCR-GAP-01` · `MTI-22` | **BOSS — 4, statutory scope confirmed NOT re-asked** |
| **`F7`** Authorization axis & configurable-record scope | `RC-D-01`, `RC-D-02`, `CF-D-01`, `CF-D-02` | **NO** — `CF-D-01`'s ground: *"only Boss may state what a Boss ruling covers"* | **YES** — Internal Control / Audit, SaaS/Multi-Company | **NO** | **YES** — `MTI-D-02` ruled `AUTH` = **Company + Warehouse + Operation-Type**; `MTI-D-03` names the tenant-changeable boundary | **4** | As the registers state; **no new position originated.** The **Pre-Test denominator is stated explicitly at §7.2** | `CF-I-01`, `CF-I-05`, `CF-I-07` · `MTI-D-02`/`-D-03` rulings | **BOSS — 4, denominator now explicit** |
| **`F8`** Idempotency severity | `C-02` | **NO** — five independent instruments name the owner *"Boss directly"*; CORR5 tried to close it and its own challenge reversed that | **YES** — Internal Control / Audit | **NO** | **YES — and it settles the object.** `BD-ACC-01`: *"Same-event retry must not create duplicate accounting events"* + Accounting Core owns the identity. **`UAE-29` is thereby ruled** | **1 — severity only.** Whether idempotency is **required** is **not** open and is not re-asked | **(b) design input, not phase-holding** — the handoff contract §4 already forbids `PASS / VERIFIED` where duplicate effects cannot be prevented *"when idempotency is required"*, so the protection option (a) would buy exists one level down | `BD-ACC-01` · handoff-contract §4 primary text · `E15-A1`, `XMC-C-A14` | **BOSS — 1, object confirmed ruled** |

**Totals, summed from the rows above on the unit declared at §1.0:**
`F1` 2 · `F2` 3 · `F3` **1** (conditional) · `F4` 2 · `F5` 8 · `F6` 4 · `F7` 4 · `F8` 1 = **25**.
Parent **26**; the single reduction is `C2-D-02`, closed at `SC-02` §5.

*(Verified by addition, not by restating a headline: `2+3+1+2+8+4+4+1 = 25`. The check was run because the
first draft's headline and its own rows disagreed — see §1.2.)*

---

## 3. Test-by-test disposition (master prompt §4 A–F)

| Test | Removed | Narrowed | Why the number is what it is |
|---|---:|---:|---|
| **A** existing Boss ruling resolves it | **1** | **3** | **Removed: `C2-D-02`** (`XMC-C-C6` + `BD-ACC-01`). **Narrowed, not removed:** `F8`'s *object* half (`BD-ACC-01` rules that idempotency is required; only severity is asked) and `F6`'s statutory half (`BD-ACC-02`) — **both were already not being asked**, so §8 records a confirmation, not a removal |
| **B** SMEs Core architecture authority | **0** | **4** | `F2`'s five mechanism invariants narrow three decisions; `C2-D-01`'s shortage exit narrows one. **None removes a decision** — each leaves a policy or confirmation act Boss still owns. *(A first draft scored this `2` removed; specification is not closure — §1.2)* |
| **C** SMT specialist challenge | 0 | **8 families routed** | `SC-03` |
| **D** targeted Very Deep Research | **0** | 0 | §4.1 — a **determination with a stated basis**, not a default |
| **E** clean-room test | 0 | **1 premise corrected** | §4.3 |
| **F** genuinely Boss-only | **25 survive** | — | §2 |

---

## 4. `F1` — the mandatory family-specific handling

### 4.1 Targeted research would not close `F1`, and opening it would be the wrong instrument

`08_JT04` §8 names the three missing inputs at primary text: `SME-Q-03` (SMEsPlus's actual invoice/delivery
sequencing — **Business SME**), `TH-NEW-01` (does TAS 2 constrain the trigger — **Thai statutory**), and a
bounded technical re-fetch (`CGS-U20`/`CGS-U31` — Docs/Research).

- **`SME-Q-03` is not a research question.** It asks how SMEsPlus's own customers actually sequence invoice
  and delivery. **No amount of reading the reference corpus can produce it**, and the source session
  rejected `DECIDABLE WITH CONTROL` for exactly this reason.
- **`TH-NEW-01` is a statutory question** under the programme's standing rule that Thai statutory claims are
  `HOLD / EVIDENCE REQUIRED` and route to the Accounting-Tax track. Targeted VDR over the reference estate
  cannot answer what a Thai accounting standard requires.
- **Only the third is a research act**, and it is *"a bounded re-fetch task, technical not a ruling"* — it
  does not change the election.

> **Master prompt §6: *"Do not use Very Deep Research as a substitute for making an architecture decision
> when evidence is already sufficient."* The converse governs here: do not open it where it cannot close
> the gap.** Opening a research round against these two inputs would consume a gate cycle and return the
> same `NOT DECIDABLE`.

### 4.2 The four-event separation — an SMEs Core act that removes a phantom conflict

Master prompt §5 `F1` requires the model layers to be distinguished, and any apparent conflict with prior
Boss-approved direction to be classified as a **true policy conflict** or **terminology/model-layer
confusion**.

| Layer | What it is | Who owns it | Already ruled? |
|---|---|---|---|
| **Business recognition event** | the moment the entity has performed — goods have left its control | Source Module (**Stock Truth**) | **No.** This is `JT-04` |
| **Accounting posting event** | the moment the ledger records it | Posting Engine | **Yes** — `BD-ACC-01` separates identity from posting, and the handoff contract separates element 3 *when physical* from element 4 *when financial* |
| **Invoice event** | the commercial claim on the customer, carrying revenue, receivable and tax | Accounting Core | **Not as a cost trigger.** It is an event in its own right whatever `JT-04` rules |
| **Return / reversal cost basis** | the measurement of a reversing event | Accounting Core | **Partly** — `BD-ACC-01`: *"Reversal is a new accounting event **referencing the original** accounting event."* The **relationship** is ruled; the **measurement** is `JT-05` |

> **The separation matters because three of the four are already settled.** `JT-04` is a question about
> **one** layer — which business event constitutes performance — and it has been presented as though it were
> a question about the whole stack. **The handoff contract already requires both dates to be carried
> separately (elements 3 and 4), so the audit trail is date-complete under either answer.** That is why
> `F1` blocks **expected values**, not test structure.

### 4.3 `SC-F-03` — the master prompt's `F1` premise does not resolve to an approved direction

Master prompt §5 `F1` instructs: *"Reconcile the existing approved direction that COGS is associated with
delivery/physical movement with the current Phase SA event model."*

**Measured.** POPULATION: every branch head whose name marks it a Boss/ruling/control/approval surface.
PATTERN: `COGS.{0,80}(delivery|physical movement|goods issue)` and its reverse, case-insensitive. Positive
control: the pattern fires, returning 4–11 hits per branch.

**Every hit is one of three things, and none is an approved direction:**

| Class | Example, verbatim | What it is |
|---|---|---|
| a **commissioning prompt asking the question** | *"Is COGS triggered by delivery, invoice, or another event…"* | a question, not a ruling |
| a **scope bullet pairing the words** | *"Sales delivery / COGS;"* · *"delivery/COGS handoff;"* | a workstream list |
| a **vocabulary example** | *"Examples include … Delivery, Invoice … Inventory Valuation, COGS…"* | a glossary |

**The Boss-approved rulings were read at primary text** (`01_BOSS_APPROVED_ARCHITECTURE_RULINGS.md` and
`04_PHASE_S_CONDITIONAL_CLOSURE_AND_PHASE_SA_ENTRY.md`). `BD-ACC-01`/`02`/`03A`/`03B` and the Product
override boundary contain **no** statement binding COGS to delivery.

**What does exist with that content is `ND-10`** — *"SMEsPlus defines `Perpetual` explicitly as recognition
at the physical movement"* — and `SA_CORR2_12` records it as **a SMEs Core position, not Boss-approved.**

> **Classification: neither a true policy conflict nor terminology confusion. It is a *provenance*
> mis-attribution.** `ND-10` has the content the instruction describes and **not its status**. Reading it as
> an approved direction would elevate an SMEs Core position to a Boss ruling — **which is precisely the
> error CORR5's first freeze committed (`C10-A1`) and which two independent challengers falsified.**
>
> **This session does not repeat it.** `F1` therefore stays Boss-owned, and the recommendation carried to
> Boss is labelled a **recommendation**, not a confirmation of something already ruled.

*(A commissioning prompt is not a ruling. The programme has recorded this class before; it recurs here in
the instruction itself, which is why it is stated rather than quietly worked around.)*

---

## 5. `F2` — what SMEs Core closed, and what stays Boss

Master prompt §5 `F2` requires verification that `block`, `warn-and-allow` and any override path **preserve
audit evidence and Company scope**. That verification is an SMEs Core act and is performed here.

**Mechanism invariants — determined by SMEs Core, binding on every branch Boss may rule:**

| # | Invariant | Ground |
|---|---|---|
| `M-1` | Every control firing emits an **event**, whether it blocks or allows. An allowed breach that emits nothing is a **silent no-op**, which `EP-P` forbids | `EP-P`; `XMC-C-C6`'s silence principle applied to controls |
| `M-2` | Under `warn-and-allow`, the recorded **owed-condition is non-dismissible** and carries who allowed it, when, and on what basis | `XMC-C-C2`/`C3` — an assertion carries who, when, basis, obligation; *"the system" is not an asserter* |
| `M-3` | The **override is Company-scoped configuration**; the **default is platform-owned** | `CF-I-07`; `BD-ACC-02`'s company boundary |
| `M-4` | An override may not lower a control **floor** — `ND-03` and `XMC-C-D3` bind the floor independently of the default | `ND-03`, `XMC-C-D3` |
| `M-5` | The audit record is identical in **shape** on both branches, so a tenant that changes the default does not change what is auditable | handoff contract §3 element 16 |

> **Consequence: Boss's choice is a pure default election with no unspecified consequences.** Before this
> section, ruling `warn-and-allow` left open what an allowed breach records. **It is now specified, and it
> is specified the same way on both branches**, so the election cannot smuggle in a control weakening.

**What stays Boss: the default value itself.** It is a risk-appetite election, and for `XD1-P1` the owning
session **reserved it to Boss in writing**; SMEs Core may not discharge a reservation it does not hold.

---

## 6. `F4` — the direct architecture recommendation master prompt §5 requires

### 6.1 `XMC-D-02` — recommendation: **extend, with declared per-boundary applicability**

**The finding that decides it:** of the 16 mandated elements, **13 are domain-general** — what happened, who
owns it, when physically, when financially, how much, valuation basis, company/tenant, source document,
original event, reversal linkage, migration batch, idempotency identity, evidence. **Only 3 are
stock-shaped** — unit of measure, product/lot/serial, warehouse/location — **and the contract already
handles that itself**: §3 requires `N/A` **plus reason** where an element does not apply.

> **The contract's *content* is domain-general; only its approved *scope* is domain-specific.** `XMC-C-D2`
> — *"a rule addressed to a receiver with no element capable of satisfying it is not a rule"* — is the
> SMEsPlus clause that makes eleven uncontracted boundaries an architecture defect rather than an omission.

**Why not twelve bespoke contracts:** twelve vocabularies for one property is exactly the defect
`XMC-C-D4` names — two derivations of one fact with silence between them. **One contract, twelve
applicability declarations.**

**Why not leave it at one boundary — the deliberate rationale tested, as §5 demands:** the only rationale
that would support the limitation is that the elements are Inventory-specific. **They are not**, on the
13-of-16 count above. **No other deliberate architecture rationale for the limitation was found**, and its
absence is stated as a measured result rather than assumed.

**The honest cost:** extension multiplies the attestation obligations (`HF-CTX-06`, `-11`) across eleven
more boundaries and enlarges Pre-Test scope accordingly. **That is a cost, not an objection** — and a
blanket extension *without* the applicability declaration would degrade the contract into recording `N/A`
sixteen times on boundaries carrying no goods, which is why the recommendation is **extend with declared
applicability**, not **extend verbatim**.

**Clean-room test on this recommendation:**

| Question | Answer |
|---|---|
| **What did we learn?** | That cross-module fact transfers fail in five measured ways — duplicate effect, unlinked reversal, silent re-dating, cost joined to nothing, and lost company/tenant context — and that all five are failures to **carry** something, not failures to compute it |
| **What did we deliberately NOT inherit?** | Any schema, message shape, field name, table or endpoint. The 16 elements are **questions a payload must answer**, not fields. We did not inherit the reference's practice of letting each receiving document carry its own date and identity |
| **What alternatives were evaluated?** | one general contract with applicability declarations · twelve bespoke contracts · leave at one boundary. §6.1 states why each of the latter two is rejected |
| **Why is this SMEsPlus's own design?** | It derives from `BD-ACC-01` (a SMEsPlus Boss ruling) and `XMC-C-D1`/`D2`/`D4` (SMEsPlus-authored clauses), and applies SMEsPlus's own `N/A + reason` discipline to keep a general contract honest where an element does not apply |
| **What is SMEsPlus doing better or differently?** | The reference has **no** cross-module handoff contract; its equivalent guarantees are implicit in code and **differ between its own generations**. SMEsPlus makes the guarantee explicit, uniform and testable, and **forbids silence** — an inapplicable element must say so and say why |

### 6.2 `C2-D-01` — the shortage exit is a defect, not an election

The source sentence has two clauses, and the second is the one a prior round suppressed and its own
challenge restored (`CHF-03`): *"the shortage state exits only on reservation completing, never on
procurement being raised. **A shortage can therefore be entered and never left by supply.**"*

**A state that can be entered and never left by the mechanism intended to leave it is a design defect, not a
policy option.** Specifying that the shortage state carries a **supply-raised exit** is an architecture act
within SMEs Core authority, and it is performed here as a specification requirement.

> **What this session deliberately does NOT do:** it does **not** re-grade `E2E-04` to `TRAVERSABLE`.
> A prior round attempted that re-grade and **withdrew it under challenge**; reversing a withdrawal that a
> challenge produced, on the strength of a specification this same session wrote, would be the
> self-interested-classification failure the programme has recorded. **The specification is published and
> the re-grade is routed to SMT** (`SC-03`), which owns it.

**`C2-D-01`'s Boss content therefore reduces to one thing: confirming the *soft* binding** — a position the
target fact-ownership matrix already states and grades `FACT VERIFIED`.

---

## 7. `F5` and `F7` — the two remaining mandatory handlings

### 7.1 `F5` — the live choice set, with the invalidated branch removed

Master prompt §5 `F5`: *"Do not present a false binary where one branch is already invalidated by evidence.
Restate the decision family into only live choices."*

`BLK-07` as worded asks **normal capacity or actual hours**. **Its own register already rejected the second
branch by name** — *"`REJECTED — INVALID ASSUMPTION` … breaches TAS 2 ¶13, undefined at zero output,
capitalises idleness into inventory"* (`POH-F-12`).

| | Presented as | **Restated to the live set** |
|---|---|---|
| Statutory / not electable | normal capacity vs actual hours | **Normal capacity is the absorption denominator.** It comes from statute, not from analysis preference. **Not a choice** — a confirmation |
| **The live election** | carried under a different identifier and never surfaced with the blocker | **`POH-D-02` — straight-line vs units-of-production absorbed at normal capacity**, with its **tax consequences unresearched and stated as such** |
| The governance act | — | **Restate `BLK-07`, `BLK-08` and veto limb 2** — only Boss may restate a Boss-owned blocker |

**The over-absorption cap's *strength* remains a declared statutory dependency under `HOLD`** and is not
resolved here or presented as resolved.

### 7.2 `F7` — the Pre-Test denominator, stated explicitly

Master prompt §5 `F7`: *"The Pre-Test denominator must be explicit before entry."*

> **DECLARED DENOMINATOR — the authorization axis set is `3`: Company, Warehouse, Operation-Type**, as ruled
> by `MTI-D-02`. **`location` is not among them.** The negative-access substitution suite `S-01`…`S-08`
> enumerates over these **3**, and `RC-D-01` asks whether a **4th** is added.

**And the honest limitation, which is the reason this does not open the gate.** A first reading of this
section concluded that stating the denominator makes `RC-D-01` non-entry-gating — an increment rather than a
re-scope. **That reading is wrong and is withdrawn.** Adding an axis is not purely additive: cases that
today assert **access allowed across locations** would, on a ruling that location is an axis, become
**denials**. **The denial enumeration extends; the positive complement inverts.**

> **So the denominator is now explicit — which is what §5 requires — and `RC-D-01` remains Pre-Test-entry
> relevant for the positive half.** It is recorded this way because the opposite conclusion was the one that
> advanced the gate, and it did not survive its own test.

---

## 8. `F6` — confirming that closed statutory scope is not re-asked

Master prompt §5 `F6`: *"Do not re-ask already-closed statutory scope."* **Tested, not assumed.**

`BD-ACC-02` at primary text closes: consolidation accounting; cross-company **tax posting, offsetting,
settlement, statutory aggregation and filing authority**. It **permits** multi-company
management/informational views.

| `F6` member | Which side of `BD-ACC-02`'s line | Re-asks closed scope? |
|---|---|---|
| `MTI-D-04` cross-company **read** grant | management information | **No** |
| `RC-D-03` Private-Company escalation criteria | tenancy model | **No** |
| `RC-D-04` mapping-layer ownership | commissioning | **No** |
| `TV6-BOSS-02` base sell-price scope | commercial master data | **No** |

> **`0 of 4` re-ask closed statutory scope.** All four sit on the **management-information** side of a
> boundary Boss has already drawn. **`BD-ACC-02` is not re-opened, re-interpreted or re-asked by this
> family**, and the recommendation (*no grant in v1*) moves **away** from that boundary, not toward it.

---

## 9. Findings raised by this scrub

| ID | Finding | Class | Disposition |
|---|---|---|---|
| **`SC-F-02`** | This file's own §1 headline (`23`) did not equal the sum of its own rows (`22`) | totals-are-unverified-claims | **Corrected in place** by summing the rows; §1 restated |
| **`SC-F-03`** | The master prompt's `F1` premise — *"the existing approved direction that COGS is associated with delivery/physical movement"* — does not resolve to an approved direction; every hit is a commissioning prompt, a scope bullet or a glossary entry. The content exists as `ND-10`, **an SMEs Core position explicitly recorded as not Boss-approved** | provenance mis-attribution | **Stated, not worked around.** `F1` stays Boss-owned; the position is carried as a **recommendation** |
| **`SC-F-04`** | `F5`'s `BLK-07` continues to be carried in a form whose own register rejected one branch by name | false binary | **Restated at §7.1**; the restatement act itself remains Boss's |
| **`SC-F-05`** | The 16-element contract's content is **13/16 domain-general** while its approved scope is one boundary — the limitation has **no** stated architecture rationale | scope/content mismatch | **Recommendation issued** (§6.1); the amendment remains Boss's |

---

## 10. Checkpoint

> ## `CP-SA-SC-10 — F1–F8 AUTHORITY SCRUB COMPLETE`
> **Count unit declared before the total (§1.0) · `26 → 25` Boss decisions · **1** closed (`C2-D-02`) ·
> **9** materially narrowed but not removed, enumerated at §1.1 · 1 survivor conditional (`XMC-D-01`) ·
> 0 families now lack a recommendation (was 1) · 0 new Boss decisions originated · **0 wrongly escalated
> on authority, as at the parent round** · targeted research required: **0**, with basis (§4.1) ·
> `F1` premise corrected (`SC-F-03`) · Pre-Test entry-gating members **3, unchanged** — the reading that
> reduced them was withdrawn (§7.2) · `F6` re-asks `0 of 4` closed statutory items · 4 findings, one of
> them against this file's own first draft (`SC-F-02`) · all 8 families routed to SMT at `SC-03`.**

No Evidence = No Progress. Never Skip Gate. Exhaust Team Authority Before Boss Escalation.
Boss remains the sole Final Approver.
