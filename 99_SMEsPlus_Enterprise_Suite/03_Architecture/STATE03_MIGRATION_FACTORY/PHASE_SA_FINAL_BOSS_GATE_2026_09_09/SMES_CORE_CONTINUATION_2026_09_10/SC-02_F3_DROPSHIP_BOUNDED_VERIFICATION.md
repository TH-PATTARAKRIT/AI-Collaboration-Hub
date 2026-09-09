# SC-02 — `F3` DIRECT-SHIPMENT (DROPSHIP) BOUNDED VERIFICATION

## CP-SA-SC-20 — F3 BOUNDED VERIFICATION COMPLETE

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`
Branch: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Layer: **LAYER 1 — clean-room business learning.** Layer 2 evidence is cited by document and finding
identifier only; no reference model, path, predicate, module or field name is transcribed.
Boss: **SOLE FINAL APPROVER**

---

## 1. Result, stated first

> # `THE STANDING DISSENT IS UPHELD. F3 GOES FROM TWO BOSS DECISIONS WITH NO RECOMMENDATION TO ONE, NARROWED, WITH A RECOMMENDATION.`

| | Before this file | **After** |
|---|---|---|
| `C2-D-02` — where the cost lands, and by what identity it binds to the sale | Boss decision, *"choosing between them is a determination"* | **CLOSED — determined by existing authority.** Leaves the Boss list |
| `XMC-D-01` — two valuation facts, or none | Boss decision, **no SMEs Core recommendation offered** | **NARROWED + RECOMMENDED.** One residual, and it is a **scope statement about `BD-ACC-03A`**, which only Boss may make |
| The standing dissent | **live and unresolved** across CORR3, CORR5 and the Final Gate pack | **RESOLVED — upheld.** The buy-side evidence did carry the answer |
| SMEs Core recommendation on `F3` | none, deliberately | **(a) the movement chain emits valuation facts under the product category's ruled policy** |

**No Boss ruling is discharged by this file, and no veto is touched.** `F3` carries no veto.

---

## 2. The dissent, quoted, and what it claimed

`SA_CORR3_12` `B-4`, primary text:

> *"Carried with a dissent: **a second executor's buy-side evidence suggests the answer may be available
> without a decision** (§12). Boss should see the dissent before deciding."*

`SA_FINAL_03`'s `F3` card records that the Final Gate session **did not resolve it**: *"doing so would need
the buy-side package re-read, which is outside a final-gate round's delta-first scope."*

**Master prompt §5 `F3` commissions exactly that re-read.** It is performed here.

---

## 3. The bounded re-read — declared before it is run

| Clause | Declaration |
|---|---|
| **POPULATION** | Every artefact in the corpus bearing on supplier→customer direct shipment: the buy-side package (`P01`), the sell-side package (`P02`), the Inventory-owned functional design, and the Phase SA cross-module contract register |
| **UNIT** | One evidenced statement about whether a direct-shipment movement produces a valuation fact, and about where its cost lands |
| **PATH SET** | `origin/research/account-p01-procure-to-pay-2026-09-04-001` · `origin/research/account-p02-order-to-cash-2026-09-04-001` · `origin/architecture/phase-sa-corr5-zero-sme-carryforward-closure-2026-09-09-001` (carrying `SA_CORR3_08`) · `origin/control/account-phase-s-boss-rulings-phase-sa-entry-2026-09-08-001` (the Boss rulings) |
| **PATTERN** | `drop.?ship` case-insensitive, **plus** SMEsPlus's own vocabulary `direct[- ]?(ship\|deliver[a-z]*)\|supplier.{0,25}customer` — because `SA_CORR3_08` §4.2 already established that the vendor word returns **0** in the package that determines the answer |
| **BLIND SPOT, declared as the complement** | An artefact that discusses direct shipment using neither vocabulary. Not measurable by this instrument; stated, not asserted absent |
| **BOUND** | This is a **re-read of existing evidence**. No new research round is opened, no Phase S artefact is reopened, no Boss ruling is revisited |

---

## 4. What the buy-side evidence actually says

### 4.1 The decisive fact: the reference's direct-shipment capability runs in **no** deployment

`P01_TRANSITIVE_MODULE_POPULATION` §3 — *Installed-Status Classification* — is a **deployed-registry**
measurement, not a source reading. Its own declarations: **POPULATION** module rows in the deployed module
registry of each readable database · **UNIT** one module name with state *installed* · **PATH SET** three
readable dumps (`D1` current-generation active, `D2` current-generation near-empty, `D3` prior-generation
heavily used) · **FALSE-NEGATIVE MODE** a module installed in an unreadable dump is invisible.

> **Result: of 65 union members, 18 are installed in at least one readable deployment and 47 are not.
> The reference's direct-shipment module is in the 47.** It is installed in **0 of 3**.

**Second instrument, differently shaped.** `P01_S16` §1 measures at **transaction** level, not registry
level: *"Drop-ship, subcontracting, consignment and intercompany are **correctly absent, each ruled out with
a control**."* `P01_S16_AAS03` records the control's author — an **independent expert**, who additionally
stated the limits of their own sweep.

**Two instruments of different shape — module registry and transaction population — agree.** Neither is the
other's restatement.

### 4.2 What that does to the Phase SA evidence base for `F3`

Every direct-shipment fact in the Phase SA corpus is therefore **source-derived from a capability no
deployment runs**:

| Phase SA finding | What it actually measured |
|---|---|
| `C2-F-02` — the movement is recorded then excluded from valuation on **three independent paths** | Current-generation **source**. `P02` `TC-31` and `S-01` state the three paths and grade them `FACT VERIFIED` — as **source facts** |
| `H-02` — movement→valuation hop `SEMANTICALLY INCOMPATIBLE — MEASURED` | the same unrun source |
| `H-03` — cost→revenue link `NO IDENTITY` | the same |
| *"Both reference generations are `FACT VERIFIED` and they disagree"* | **`P02` §15.3 names the disagreement exactly: the prior generation had a purpose-built entry for this case; the current generation removed it.** `P01_S18` confirms the same split from the buy side — the prior generation has **no** direct-shipment exclusion at the bill-line redirect, the current generation added one |

> **`SC-F3-01` — the two readings the Final Gate pack called *"both consistent with every fact in the
> corpus"* are two readings of two generations of the same unrun capability.** They are not two business
> meanings between which SMEsPlus must choose. **They are one vendor's implementation choice and its
> reversal, in code that no deployment on this estate executes.**

**This is decisive under a standing Boss-approved control, not under an argument invented here.**
`BD-ACC-03A`'s covering ruling states: *"v18/v19/source-generation identity is **Evidence Provenance, not a
SMEsPlus target-platform decision**."* And the Phase SA constitution states **`SOURCE IS EVIDENCE, NOT
DESIGN.`** A question framed as *"which of the two generations do we follow"* is **not a SMEsPlus decision
at all** — the framing is itself the clean-room defect.

---

## 5. `C2-D-02` — CLOSED by existing authority

**The question as escalated:** *"where does the dropship cost land, and by what identity is it bound to the
sale?"* Ground for escalation: `SA_CORR2_02` §6 — *"Both reference generations are `FACT VERIFIED` and they
disagree. **Choosing between them is a determination.**"*

**Two SMEsPlus-owned instruments already determine it, and neither is a vendor generation.**

| Instrument | Status | What it settles |
|---|---|---|
| **`XMC-C-C6`** — the symmetry rule | SMEsPlus-owned contract clause, adopted | *"Every recognition of revenue produces **either** a cost recognition bound to the same identity, **or** an explicit, recorded determination that no cost arises. **Silence is not a permitted answer.**"* — and its own final sentence names this exact case: *"Under this clause a dropship sale **can no longer** recognise revenue, receivable and tax while its cost lands elsewhere, on another date, joined to nothing"* |
| **`BD-ACC-01`** | `CLOSED / BOSS APPROVED` | *"Accounting Core owns the canonical Accounting Event Identity… Every accounting event is bounded by Tenant + Company context."* |

**Determination:** the cost recognition **binds to the same canonical Accounting Event Identity as the
revenue recognition**, owned by Accounting Core, Tenant + Company bounded. The reference's shape — cost on
the vendor bill, at the bill's date, joined to nothing — is **already forbidden by `XMC-C-C6`**, which was
adopted before this file and names it explicitly.

**There is nothing left for Boss to choose on `C2-D-02`**, because both surviving alternatives of
`XMC-D-01` bind the cost the same way: option (a) binds it through the movement chain's valuation fact,
option (b) binds it through the accounting event identity directly. **The binding identity does not vary
with the answer to `XMC-D-01`.** That is why it closes independently.

> **Residual, and it is not `F3`'s.** The **date** of the cost recognition is `F1` (`JT-04`), of which
> direct shipment is one instance. `C2-D-02` does not carry a separate date election, and presenting it as
> one would ask Boss the `F1` question twice. **`C2-D-02` is closed; its timing component is `F1`'s and is
> already before Boss there.**

### 5.1 Clean-room test on this determination — the five mandatory answers

| Question | Answer |
|---|---|
| **What did we learn?** | That a sale can recognise revenue, receivable and tax while its cost arrives on a different document, on a different date, with no join — and that this is invisible until someone asks the cost where its sale went |
| **What did we deliberately NOT inherit?** | Both generations' treatments. The prior generation's purpose-built entry and the current generation's three-path exclusion are **both** rejected as design authority. We inherited **the defect's description**, not either remedy |
| **What alternatives were evaluated?** | (i) cost binds to the sale's accounting event identity; (ii) cost binds to the procurement document, reconciled periodically; (iii) cost binds to neither and a determination is recorded. (ii) reproduces the measured defect at a slower cadence and needs a reconciliation object nothing else needs; (iii) is unavailable on the facts, because a cost demonstrably arises — the supplier bills |
| **Why is this SMEsPlus's own design?** | It derives from `BD-ACC-01`, a SMEsPlus Boss ruling, and `XMC-C-C6`, a SMEsPlus-authored clause. Neither exists in the reference, whose equivalent behaviour is implicit in code and differs between its own generations |
| **What is SMEsPlus doing better or differently?** | The reference permits silence — cost joined to nothing — and that permission is invisible to its user. **SMEsPlus forbids silence and requires the determination to be recorded when it is genuinely made**, so the absence of a cost is itself an auditable fact rather than an absence of one |

---

## 6. `XMC-D-01` — NARROWED, RECOMMENDED, one Boss residual

### 6.1 What discriminates the two options — tested honestly

**`XMC-C-C6` does *not* discriminate**, and a first draft of this file wrongly said it did.

Option (b) as the Final Gate pack framed it is *"none, with an explicit recorded determination under
`XMC-C-C6` **and the cost bound by the accounting event identity instead**"* — which **satisfies `C6`'s
first branch**, not its second. `C6` rules out **the reference's** shape (revenue without a bound cost); it
does not rule out option (b). **Recorded because the elimination was attractive and wrong** — it is the
`EC-06` negative-claim class, caught inside this file by re-reading `C6`'s own text rather than its summary.

**What does discriminate is one SMEsPlus-owned sentence.** `XMC-F-03`, from the SMEsPlus-owned functional
design's list of routing templates a Thai SME user chooses per warehouse:

> *"…a one-step, two-step or three-step receipt; a one-step, two-step or three-step delivery; resupply from
> another warehouse; buy-on-reorder-point; make-or-buy on demand; **direct shipment from supplier to
> customer**; and manufacture — **and the system resolves the movement chain from that choice.**"*

**SMEsPlus's own design places direct shipment in the set of templates from which a *movement chain* is
resolved.** That is SMEsPlus-owned evidence, in SMEsPlus's own vocabulary, bearing directly on whether
movement facts arise — and it points to option **(a)**.

**Its weakness, stated rather than suppressed:** *"resolves the movement chain"* does not by itself exclude
resolving to a **zero-length chain** for a route with no internal end. `XMC-F-03` is strong evidence and not
a proof. **The recommendation rests on it and says so.**

### 6.2 SMEs Core recommendation

> **Option (a).** A direct-shipment route resolves a movement chain, and its valuation facts arise under
> **the product category's ruled policy** — `Perpetual` or `Periodic` per `BD-ACC-03A` — with **no
> route-specific valuation exception**.

**The asymmetry that matters, and the reason this is a genuine narrowing:**

| | Option (a) — recommended | Option (b) |
|---|---|---|
| What it requires of Boss | **Nothing.** It applies `BD-ACC-03A` as ruled: valuation policy authority is Product Category | **A scope statement**: that `BD-ACC-03A`'s Product-Category valuation authority **does not reach** a route with no internal end |
| Authority class | SMEs Core architecture determination, subject to SMT challenge | **Boss-only** — `CF-D-01`'s ground: *"only Boss may state what a Boss ruling covers"* |

> **`SC-F3-02`. `F3`'s remaining Boss content is not a choice between two options. It is a single scope
> question that arises *only if Boss prefers option (b)*.** On the recommendation, `F3` leaves the Boss
> decision list entirely and becomes an SMEs Core determination.

**This session does not make that scope statement**, and does not treat option (b) as eliminated. Stating
what `BD-ACC-03A` covers is Boss's act; **all this file does is show which branch needs it.**

### 6.3 The bias check — run against this file's own conclusion

The Final Gate pack recorded that the executing party's instinct is toward the reading that lets the gate
open, and that its own challenge caught that four times in one round. **This file's conclusion narrows the
Boss list, which is that same direction.** So it is tested:

| Test | Result |
|---|---|
| Does the conclusion rest on a **vendor** fact? | **No.** It rests on `XMC-F-03` (SMEsPlus-owned design), `XMC-C-C6` (SMEsPlus-authored clause) and `BD-ACC-01`/`BD-ACC-03A` (Boss rulings). The vendor evidence is used only to **remove** an option set, never to supply one |
| Does it **discharge** anything Boss owns? | **No.** The one Boss-owned element — the `BD-ACC-03A` scope statement — is explicitly preserved and routed |
| Would the opposite result have been publishable? | **Yes, and it nearly was.** §6.1 records an elimination this file made and then withdrew against its own source text |
| Is a **weakness** of the recommendation published? | **Yes** — §6.1's zero-length-chain reading, which is the strongest argument against the recommendation and is not answered here |
| Does it rely on the argument that a **route** may not override `BD-ACC-03A`? | **No — and that argument was available and was deliberately not used.** It is a scope statement, and using it would have been this session making Boss's ruling for him |

---

## 7. Detection latency — recorded, and it is not an SMT Escape

**It is not an escape.** The dissent was raised by a **second executor** at CORR3, carried visibly through
CORR5 and the Final Gate pack, and reached Boss **labelled as unresolved with an instruction to see it
before deciding**. Boss was never the first detector. **The SMT-first ladder held.**

**What is recorded is latency.** The installed-status evidence has been in the buy-side package since
**2026-09-04**. `F3` was escalated at CORR3, re-escalated at CORR5, and presented at the Final Gate — three
rounds — **without that evidence being joined to it**, because each round was scoped delta-first and the
evidence sat in a peer programme's package under a different vocabulary.

**Prevention control, proposed:** when a decision card's evidence row cites **reference behaviour** as the
ground for an open election, the card must additionally record **whether that behaviour is reachable in any
deployed instance** — the programme's own *latent vs live* rule, applied to decision cards rather than to
defects. **A capability installed in zero deployments cannot supply a business fact about how SMEsPlus's
users work.** Routed to `SC-03` for SMT challenge; not adopted unilaterally.

---

## 8. What this file does **not** claim

1. **It does not close `F3`.** One Boss residual survives, named at §6.2.
2. **It does not eliminate option (b).** It shows what option (b) costs in authority.
3. **It does not claim direct shipment is absent from SMEsPlus.** SMEsPlus's own design names it as a
   routing template (`XMC-F-03`). The reference's *capability* is unrun; **SMEsPlus's requirement is real.**
   Conflating those two would be the same error in the opposite direction.
4. **It does not re-grade `C2-F-02`, `H-02` or `H-03`.** They are correct as source facts. What changes is
   **what they are evidence of** — the reference's implementation, not a business meaning SMEsPlus must adopt.
5. **It does not touch `F1`.** `C2-D-02`'s timing component is `F1`'s and stays there.
6. **It is not independent assurance.** This is SMEs Core's own re-read, subject to SMT challenge at `SC-03`.

---

## 9. Checkpoint

> ## `CP-SA-SC-20 — F3 BOUNDED VERIFICATION COMPLETE`
> **Dissent UPHELD and RESOLVED · `C2-D-02` **CLOSED** by `XMC-C-C6` + `BD-ACC-01`, leaves the Boss list ·
> `XMC-D-01` **NARROWED** to one scope question that arises only on the non-recommended branch ·
> recommendation **(a)** issued with its own weakness published · reference direct-shipment capability
> measured **installed in 0 of 3 deployments** on two differently-shaped instruments · 2 findings
> (`SC-F3-01`, `SC-F3-02`) · 1 self-caught elimination withdrawn · 0 Boss rulings discharged · 0 vetoes
> touched · 0 vendor tokens · SMT challenge pending at `SC-03`.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
