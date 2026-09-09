# SC-03 — SMT FIRST-LINE CHALLENGE REGISTER

## CP-SA-SC-40 — SMT FIRST-LINE CHALLENGE COMPLETE · CP-SA-SC-30 — TARGETED RESEARCH DETERMINED

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`
Branch: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Boss: **SOLE FINAL APPROVER**

---

## 0. What the disposition words mean here, and what they do not

Master prompt §7 mandates the vocabulary `PASS / PASS WITH CONDITION / RETURN TO SME CORE / TARGETED VERY
DEEP RESEARCH / BOSS-ONLY DECISION`. **These are used strictly as that classification vocabulary, applied to
one family by one specialist team.**

> **No Phase SA gate is declared passed by this file. No phase, package, scenario, invariant or contract is
> graded. `0 of 22` scenarios are verified, as before.** A family marked with the mandated `PASS` token means
> only *"this SMT raises no condition on this family"*.

**And this is not independent assurance.** It is **internal first-line challenge by specialist role**, drawn
from the same corpus assembled by the same party — the limitation `ND-12` records. `SC-04` §5 keeps that
distinction live.

---

## 1. Result

| Measure | Value |
|---|---:|
| Families challenged | **8 of 8** — none reaches Boss without a disposition |
| SMTs engaged | **6** |
| Challenges raised | **11** |
| Challenges that **changed** an SMEs Core conclusion | **6** |
| Returned to SMEs Core and **closed in-session** | **4** |
| Returned to SMEs Core and **still open** | **0** |
| Dispositions requiring **targeted Very Deep Research** | **0** — §5 |
| New Boss decisions created by the challenge | **0** |
| New Boss **consequences** surfaced for an existing decision | **2** (`SC-SMT-05`, `SC-SMT-09`) |

**The challenge was productive against this session's own work: 6 of 11 changed something.** Three of the
six landed on conclusions this session had published one file earlier.

---

## 2. The register

| # | SMT | Family | Challenge raised | SMEs Core response | **Disposition** |
|---|---|---|---|---|---|
| `SC-SMT-01` | **Accounting / Thai Accounting-Tax** | `F1` | **`JT-05` → original cost leaves a residual under `Average` costing that nothing in the recommendation places.** `BD-02` closes the destination of *unabsorbed overhead*; it says nothing about a returns-costing difference. The recommendation is **incomplete as written** | **Accepted.** SMEs Core cannot close it: `09_JT05` §5 assigns *"the reconciliation-control design for the **AVCO admitted gap**"* to **Boss** at primary text. The residual is now **named** in the `F1` card rather than latent inside a one-word recommendation | **BOSS-ONLY DECISION** |
| `SC-SMT-02` | **Accounting / Thai Accounting-Tax** | `F1` | `JT-04`'s recommendation rests on `ND-10`, and **whether TAS 2 constrains the recognition trigger is untested** (`TH-NEW-01`) | **Accepted.** The recommendation carries an explicit **`HOLD / EVIDENCE REQUIRED`** statutory marker and is routed to the Accounting-Tax track. **No statutory claim is made** | **BOSS-ONLY DECISION**, statutory input pending |
| `SC-SMT-03` | **Accounting / Thai Accounting-Tax** | `F8` | `SC-01` claims the handoff contract §4 already protects duplicate prevention *"when idempotency is required"*. **Who determines when it is required?** If undefined, the protection `SC-01` relies on to recommend option (b) is **vacuous** | **Accepted, and closed by existing authority.** `BD-ACC-01` at primary text: *"**Same-event retry must not create duplicate accounting events.**"* It is unqualified. **For accounting events, idempotency is always required**, so §4's condition is always met and the protection is not vacuous. **`SC-01`'s option-(b) recommendation survives on a stated ground rather than an assumed one** | **PASS WITH CONDITION** — the ground must be cited, not implied |
| `SC-SMT-04` | **Inventory** | `F3` | **`SC-02`'s option (a) is under-specified.** If a direct-shipment chain emits valuation facts, the goods **never occupy an internal location**. Handoff element 9 (warehouse/location) would be recorded `N/A` on a movement the model calls real. **A valuation fact with no location is incoherent under the Inventory model** | **Accepted and closed in-session.** SMEs Core specifies: a direct-shipment movement's location context is the **counterparty pair** — supplier origin and customer destination — recorded as **external endpoints with their reason**, **not** as `N/A`. The contract's own `N/A + reason` rule is for elements that *do not apply*; here the element applies and its values are external. **This is a specification act, and it strengthens rather than weakens option (a)** | **PASS WITH CONDITION** — the endpoint semantics are part of the recommendation |
| `SC-SMT-05` | **SaaS / Multi-Company** | `F6` | **`MTA-11` records that every grant mechanism degrades toward permanence and that no review cadence is designed anywhere.** `F6` carries no decision covering this. On the recommended branch it is moot; **on any grant-permitting branch it is an undesigned element Boss would be ruling into existence unseen** | **Accepted.** Not a new Boss decision — it is a **consequence of an existing one**. Carried into `SC-06` as a stated consequence of the non-recommended branches of `MTI-D-04` | **BOSS-ONLY DECISION** — consequence surfaced, no new item |
| `SC-SMT-06` | **Internal Control / Audit** | `F2` | **`M-1` can be defeated.** It requires every control firing to emit an event, but nothing in the five invariants says the **emission itself** is outside the override surface. A configuration that can suppress the event turns `warn-and-allow` into `allow-silently` **without electing it** | **Accepted and closed in-session.** SMEs Core adds **`M-6`: the control event's *emission* is not configurable; only the control's *outcome* is.** An override changes what happens, never whether it is recorded. **This is the defect shape the programme has already measured once — a hard control defeated through an adjacent configuration surface** | **PASS WITH CONDITION** — `M-6` is part of the mechanism set |
| `SC-SMT-07` | **Internal Control / Audit** | `F7` | `SC-01` §7.2 declares the **denial** denominator (3 axes) and concedes the **positive complement inverts** on `RC-D-01`. **A Pre-Test entry condition that states only half of a denominator is the wrong-denominator class again** | **Accepted.** The entry condition at `SC-05` states **both** halves: the denial enumeration over the ruled 3 axes, **and** the positive complement whose expected results invert if a 4th axis is ruled in | **BOSS-ONLY DECISION** — `RC-D-01` remains entry-relevant |
| `SC-SMT-08` | **Cross-Module Integration** | `F4` | **`SC-01`'s "extend with declared applicability" is self-weakening as written.** If the **boundary owner** declares which elements apply, a boundary can exempt itself from the elements it finds inconvenient — and the contract becomes a form each party fills in against its own convenience | **Accepted and closed in-session.** SMEs Core specifies: **an applicability declaration is part of the contract amendment and carries the same authority as the contract — it is not a boundary-owner act.** A boundary may *propose*; it may not *declare*. **This materially changes the `XMC-D-02` recommendation and is the single most consequential challenge in this register** | **PASS WITH CONDITION** — the authority of the declaration is part of what Boss rules |
| `SC-SMT-09` | **Cross-Module Integration** | `F4` | Extending to twelve boundaries multiplies attestation obligations, **and Pre-Test scope grows with it**. `SC-01` states this as a cost. **Boss should see the magnitude, not the word "cost"** | **Accepted.** `SC-06` states the consequence in the units Boss decides in: **1 boundary contracted today → 12 on the recommendation**, with attestation obligations and Pre-Test matrix scope scaling accordingly | **BOSS-ONLY DECISION** — consequence quantified, no new item |
| `SC-SMT-10` | **Cross-Module Integration** | `F3` | **Verify `SC-02`'s load-bearing claim** that the binding identity *"does not vary with the answer to `XMC-D-01`"*. If it varies, `C2-D-02` cannot close independently and `SC-02`'s headline collapses | **Verified and upheld.** Under option (a) the cost recognition binds to the sale's canonical Accounting Event Identity through the chain's valuation fact; under option (b) it binds to the same identity directly. **`BD-ACC-01` makes the identity the binder in both cases**, and neither branch relocates it. **The claim holds** | **PASS** |
| `SC-SMT-11` | **Manufacturing / Costing** | `F5` | The restatement calls **normal capacity** *"not a choice — a confirmation"*, **but the over-absorption cap's strength is a declared statutory dependency under `HOLD`.** A denominator whose cap strength is unknown is not fully specified, and calling it a confirmation overstates its settledness | **Accepted.** The restatement retains *"normal capacity"* as the denominator **and carries the cap-strength `HOLD` on the same line**, so Boss confirms a denominator whose one open element is visible rather than folded away | **PASS WITH CONDITION** — the `HOLD` travels with the confirmation |

---

## 3. Disposition summary by family

| Family | SMT(s) | Disposition |
|---|---|---|
| `F1` | Accounting / Thai Accounting-Tax | **BOSS-ONLY DECISION** — 2 decisions, 1 statutory input pending |
| `F2` | Internal Control / Audit | **PASS WITH CONDITION** on the mechanism (`M-6` added); **BOSS-ONLY DECISION** on the default |
| `F3` | Inventory · Cross-Module Integration | **PASS WITH CONDITION** on option (a)'s endpoint semantics; **PASS** on `C2-D-02`'s closure; **BOSS-ONLY DECISION** on the one conditional scope question |
| `F4` | Cross-Module Integration · Inventory | **PASS WITH CONDITION** on the recommendation's declaration authority; **BOSS-ONLY DECISION** on the amendment and the binding confirmation |
| `F5` | Manufacturing / Costing · Thai Accounting-Tax | **PASS WITH CONDITION** on the restatement; **BOSS-ONLY DECISION** on the restatement act and five elections |
| `F6` | SaaS / Multi-Company · Internal Control | **BOSS-ONLY DECISION** — 4 decisions, 1 consequence newly surfaced |
| `F7` | Internal Control / Audit · SaaS / Multi-Company | **BOSS-ONLY DECISION** — 4 decisions, denominator now stated in both halves |
| `F8` | Internal Control / Audit · Accounting | **PASS WITH CONDITION** on the recommendation's ground; **BOSS-ONLY DECISION** on severity |

**`RETURN TO SME CORE` still open: `0`.** Four were returned and all four were closed inside this session
(`SC-SMT-04`, `-06`, `-08`, and `-03`'s ground). **Boss is not being asked to compensate for unfinished team
work**, which is the master prompt's Terminal D failure state and is not entered.

---

## 4. SMT Escape test

> ### `SMT ESCAPES THIS ROUND: 0`

**Definition applied:** a reasonably detectable material defect that reaches Boss **without** prior
SMT/peer detection.

| Item that could have been an escape | Was it detected before Boss? | Verdict |
|---|---|---|
| `F3`'s standing dissent | **Yes** — raised by a **second executor** at CORR3, carried visibly through CORR5 and the Final Gate pack, and presented to Boss **labelled unresolved with an instruction to see it before deciding** | **Not an escape.** The ladder held |
| `F5`'s `BLK-07` false binary | **Yes** — `POH-F-12` detected and published it before any Boss pack carried it as a live binary | **Not an escape** |
| `F8`'s severity | **Yes** — CORR5's own challenge reversed CORR5's attempt to close it, **before** publication | **Not an escape** |
| `SC-01`'s `26 → 22` miscount | **Yes** — caught by this session's own arithmetic check **before** publication | **Not an escape**; a pre-publication self-correction |
| `SC-02`'s withdrawn `XMC-C-C6` elimination | **Yes** — caught inside `SC-02` §6.1 **before** publication | **Not an escape** |

### 4.1 Detection **latency** — recorded, with a prevention control

**Not an escape, but not free either.** The buy-side installed-status evidence that resolved `F3` has
existed since **2026-09-04**. `F3` was escalated at CORR3, re-escalated at CORR5 and presented at the Final
Gate — **three rounds** — before that evidence was joined to it.

> **Prevention control, proposed by SMEs Core and adopted by the Inventory and Cross-Module SMTs:**
> **when a decision card cites *reference behaviour* as the ground for an open election, the card must also
> record whether that behaviour is reachable in any deployed instance.** A capability installed in **zero**
> deployments cannot supply a business fact about how SMEsPlus's users work — it can only supply a
> description of someone else's implementation. **This is the programme's *latent vs live* rule applied to
> decision cards rather than to defects.**
>
> **Scope of adoption:** SMEs Core adopts it for Phase SA decision cards. **It is not applied
> retroactively to close any other family**, and it is not proposed as a project-wide rule — that would be a
> governance act outside this session's authority.

---

## 5. `CP-SA-SC-30` — targeted Very Deep Research determination

> # `NO TARGETED VERY DEEP RESEARCH RE-ENTRY REQUIRED`

**Basis, stated per open item rather than asserted for the set.** Every remaining open element falls into
one of four classes, and **none is a research question about the evidence corpus**, which is what re-entry
is for.

| Class | Items | Why re-entry is the wrong instrument |
|---|---|---|
| **Boss policy election** | all 25 surviving decisions | Research cannot produce an election. Master prompt §6: *"Do not use Very Deep Research as a substitute for making an architecture decision when evidence is already sufficient"* |
| **Business-SME input** | `SME-Q-03` (invoice/delivery sequencing), `SME-Q-02` | Asks how SMEsPlus's **own customers** operate. **No reading of the reference corpus can produce it**, and `08_JT04` §8 rejected `DECIDABLE WITH CONTROL` for exactly this reason |
| **Thai statutory input** | `TH-NEW-01`, `TH-NEW-02`, `POH-D-02`'s tax consequences, the over-absorption cap strength | Under standing rule these are `HOLD / EVIDENCE REQUIRED` and route to the **Accounting-Tax track**. VDR over the reference estate cannot establish what a Thai standard requires |
| **Runtime / build proof** | element 10, element 15, `CF-I-03`, the 58 invariants, the 22 scenarios | Needs an implementation and an executed test. Unreachable at Phase SA **by construction** |

**The one place a re-read was prescribed — `F3` — was performed rather than escalated** (`SC-02`), and it
resolved the dissent. **That is the correct use of the re-entry right: bounded, evidence-preserving,
non-resetting, and it returned an answer instead of a request.**

**One bounded technical item is noted and is not re-entry:** `CGS-U20`/`CGS-U31`, described by its own
source as *"a bounded re-fetch task, technical not a ruling"*. It is a Docs/Research act that **does not
change the election** and does not require a research round.

**No `SC-TVR-xx` file is published, because none is required.** This section is that result, with its basis.

---

## 6. What this register does not do

1. **It does not grade any Phase SA artefact.** The mandated `PASS` token classifies an SMT's position on a
   family and nothing else.
2. **It does not constitute independent assurance** and is not offered as any part of one.
3. **It does not discharge a veto** — see `SC-04`.
4. **It does not close a family.** Every family still carries its Boss content, and the conditions raised
   travel with it into `SC-06`.
5. **It does not apply the `E2E-04` re-grade** that `SC-01` §6.2's specification bears on. That re-grade is
   routed here and is **held**: reversing a withdrawal that a prior challenge produced, on the strength of a
   specification written by the same session in the same round, is the self-interested-classification
   failure the programme has recorded. **It is left for the structurally independent reviewer Boss appoints.**

---

## 7. Checkpoint

> ## `CP-SA-SC-40 — SMT FIRST-LINE CHALLENGE COMPLETE`
> **8 of 8 families dispositioned by 6 SMTs · 11 challenges · 6 changed an SMEs Core conclusion · 4 returned
> and 4 closed in-session · `0` still open · `0` SMT escapes · 1 detection-latency finding with a scoped
> prevention control · 2 Boss consequences surfaced, 0 new Boss decisions · `E2E-04` re-grade deliberately
> held.**

> ## `CP-SA-SC-30 — NO TARGETED VERY DEEP RESEARCH RE-ENTRY REQUIRED`
> **Basis given per class (§5): Boss election · business-SME input · Thai statutory input · runtime proof.
> `0` items are research questions about the corpus. The one prescribed re-read was executed at `SC-02` and
> returned an answer.**

No Evidence = No Progress. Never Skip Gate. Boss must not be the first detector.
Boss remains the sole Final Approver.
