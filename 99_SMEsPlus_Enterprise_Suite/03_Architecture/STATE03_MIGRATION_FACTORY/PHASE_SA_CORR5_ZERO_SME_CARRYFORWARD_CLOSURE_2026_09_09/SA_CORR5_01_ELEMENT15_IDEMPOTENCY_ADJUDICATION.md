# SA_CORR5_01 — ELEMENT 15 DETERMINISTIC IDEMPOTENCY IDENTITY — ADJUDICATION

## CP-SA-C5-10 — ELEMENT 15 ADJUDICATED OR EXACTLY BOUNDED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR5-ZERO-SME-CARRYFORWARD-001]`
Branch: `architecture/phase-sa-corr5-zero-sme-carryforward-closure-2026-09-09-001`
Workstream: **A** · Authority: `BD-ACC-01` express grant — *"Phase SA may design the technical
representation independently"* — exercised **narrower than granted**: business-semantic clauses only;
no identifier format, no schema, no generation scheme.
Boss: **SOLE FINAL APPROVER**

---

## 1. What element 15 is, at primary text

Boss-approved handoff contract (`03_BOSS_APPROVAL_INVENTORY_TO_ACCOUNTING_MINIMUM_HANDOFF_DATA_CONTRACT`,
`BOSS APPROVED / EFFECTIVE`), §3 item 15, verbatim:

> `WHICH Idempotency Identity` — **deterministic identity used to prevent duplicate processing/effect.**

and §4, the gate clause: a scenario may not be declared `PASS / VERIFIED` if any material element is
*"unable to prevent duplicate/replayed effects **when idempotency is required**"*. The 22-scenario
baseline §3 names the same object as *"idempotency / duplicate-protection identity"*.

**Two properties are asked for and they are distinct:** *deterministic* (same fact in, same identity
out, on every run and any later date) and *duplicate-preventing* (a second presentation is recognised
as the same). A carrier that is unique but not deterministic (a minted UUID) satisfies neither; a
carrier that is deterministic but empty-allowed satisfies neither. Both failures are present in the
positions surveyed below.

---

## 2. Existing-work discovery first — every candidate position located (`AUTO-C5-02`)

**Measured over `CORR5-FRAME` (186 heads, `U2` = 3,620 paths), pattern `idempoten` (case-insensitive):
327 unique paths** (`git grep -l -i idempoten <186 refs> -- '*.md' '*.txt' '*.csv'`; a challenger's
run over 186 refs excluding this branch returned 318). **Reduction rule (`CHA-02` — the first freeze
published none):** a path is a *position* if it (a) is SMEsPlus-owned (not Layer-2 observation, not a
prompt, not a governance boilerplate list), (b) states a rule, obligation, identity basis or mechanism
for idempotency rather than citing one, and (c) is not superseded by a later version of the same
artefact. Applying (a)–(c) by reading, plus the stranded architecture branch head `098798f7` and the
reference-estate findings carried by the joint cross-proof, yields **fifteen positions** — the twelve
below and three the first freeze missed (`P13`–`P15`). **None was originated here.**

| # | Position | Where | Status of the source | Bears on |
|---:|---|---|---|---|
| **P1** | **`BD-ACC-01`** — Source Module owns the Business Fact; Accounting Core owns the canonical Accounting Event Identity; Posting Engine owns Ledger Posting; identity distinct from document / journal / matching numbers; immutable in identity and provenance; *"Same-event retry must not create duplicate accounting events"*; reversal is a new event referencing the original; every event bounded by Tenant + Company | `…/BOSS_CLOSURE_AND_PHASE_SA_ENTRY_2026_09_08/01_BOSS_APPROVED_ARCHITECTURE_RULINGS.md` | **`CLOSED / BOSS APPROVED`, 2026-09-08. Must not be re-asked** | ownership, retry, reversal, scope |
| **P2** | **`XMC-C-A1`…`A13`** — the deterministic **identity basis**: six parts (tenant · company · owning source domain · business-fact occurrence as its owner identifies it · recognition role · policy version in force at recognition); exclusions (`A5`); retry (`A6`); replay (`A7`); reversal (`A8`); correction (`A9`); scope and fail-closed (`A10`); consumer reliances and non-reliances (`A11`, `A12`); namespace (`A13`) | `SA_CORR3_08` §3.1 | **Phase SA specification, 2026-09-09, under `BD-ACC-01`'s grant. Reviewed by nobody outside the executing party** (its own §1.4) | **the identity itself** |
| **P3** | **`ARC-WP-010`** §12.4 events *"append-only, versioned, tenant-scoped"* with an owning source; §12.5 *"at-least-once delivery with idempotent consumers"*; §12.7 *"every consumer uses an idempotency key (event ID / business key)"*; §17 *"idempotency prevents double-apply on replay"*; `ADR-ARC-017` **`PROPOSED`**; `R-010-01` non-idempotent consumer → duplicate posting, **Critical** | stranded branch `claude/state-03-architecture-deliverables-su8cg6` @ `098798f7`, 2026-07-14 | **`DRAFT · NOT VERIFIED · Gate Status: HOLD`**, named review never occurred; **cited by 0 `MTI-*` or Phase SA artefacts** (`C4-02-F-07`) | consumer obligation; key *source* |
| **P4** | **`ARC-WP-004`** §12.1 *"Posting Engine … enforces idempotency; emits immutable posting results"*; §17 *"posting must be idempotent to avoid double-post after retry"*; `R-004-01` mitigation *"idempotent posting keys"* | same branch | same status | posting-side obligation |
| **P5** | **`MTI-31`** run identity scoped to `CTX`, mutual exclusion — and its own scope note: *"It does not supply the idempotency identity"*; R2 consistency row `CF-I-02 × MTI-31`: a fully resolved run *"is still indistinguishable from a retry of itself"* | `03_INVENTORY_MULTI_TENANT_INVARIANT_SET` §7.2; R2 `03` §14 | `SPECIFIED — RANK 2 DEPENDENT` | run scoping only |
| **P6** | **`L8-09` / `RISK-C02` / `IV-06` / `GAP-MD-21`** — the movement fact's canonical identity is *"document line plus **attempt identity**"*, and the attempt component **`IDENTITY DOES NOT EXIST`**; severity `BLOCKING`, owner **Boss** (`C-02`), *"Lane A — not COGS-gated"* | R4 `09_L8_DATA_IDENTITY_IMMUTABILITY_REGISTER` §`L8-09`; `05_L4` §4 row 15 | Open since R4 (2026-09-04); **carried by every round since** | source-side duplicate |
| **P7** | **`09_DATA_IDENTITY…` §3.1–3.2** — *"a guaranteed context makes a duplicate attributable; it does not make it detectable"*; *"context conformance and duplicate freedom are independent properties"* | MTI set `09` | `SPECIFIED` | the exact boundary between element 10 and element 15 |
| **P8** | **The reference-estate carrier** — one inbound-channel constraint, optional module, *"table-global rather than tenant-scoped"*, **populated on 0 of 13,814 rows** | `SA_CORR3_06` §3.4 `JCP3-F-05b`; `X2-F11` (`ACCEPTED`); `P08-AEI-01` (`FACT VERIFIED`) | Layer 2 observation | **a carrier to reject** |
| **P9** | **`FDS_INTEGRATION`** `FR-INT-004` *"Retry Supported"* with **no idempotency key**, no tenant/company column (`SA_CORR4_01` class 6) | `01_SaaS_Foundation/FDS/Domains/FDS_INTEGRATION.md`, 186/186 branches | `Draft` | an unkeyed retry path |
| **P10** | **`SA09`/`SA_CORR2_09` §3** — idempotency *"graded `ESTABLISHED` … recorded absent in four Accounting packages"*; **`UAE-29`** *"no accounting-event identity"* is P11's root blocker `B-02`, *"Boss design decision. No research closes it"* | `SA_CORR2_09`; P11 `P11_BLOCKER_REGISTER_CORR1.md` | `UAE-29` **ruled** as `BD-ACC-01` on 2026-09-08 (`C5-B-03`) | Account side has no carrier; Boss has ruled the owner |
| **P11** | **`CROSS_MODULE_DATA_TRANSFER_PERFORMANCE_POLICY`** lists *"Integration & Idempotency"* as a mandatory assurance category | `00_Project_Governance/POLICIES/` | governance | test obligation exists |
| **P12** | **`SA17` §3** control row *"Same-event retry is idempotent; a reversal creates a new event referencing the original — `BD-ACC-01`"* | `SA17` | Pre-Test control list | the test the Pre-Test Matrix already expects |
| **P13** | **`FV006-INT-001` — the general Confirm / Movement-Execution idempotency contract** of the Group A Team B design: *"every action that transitions a Commitment … or triggers a `Movement Executed` event carries a business identity… must expose the original action's already-recorded outcome"*, protected effect *"Financial Handoff write"*; **listed for re-verification in the IBPV `RV-009` prompt; the `RV_009` report's result for it was not located** (`CHD-14` — a challenger's *"verified Covered"* was not reproduced at source) | `TEAM_B_DESIGN/GROUP_A_SALES_INVENTORY_PURCHASE/12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §11 (`CORR-008` closure), branch `claude/team-b-group-a-sip-corr-008` | Team B design (`CORR-008` closure), IBPV re-verification result not located | **an act-level attempt-identity contract — the prior source of `A14`** (`CHA-02`) |
| **P14** | **Inventory Final Solution V1** `03` line 132: *"**Idempotent.** A demand identity — source document line, template, and attempt — must be unique, so a retry cannot create a second movement chain. Carried finding `C-02`: whether this is gate-blocking is Boss's"*; line 178 similar for movement chains | `FINAL_SOLUTION/INVENTORY/V1_0/03_INVENTORY_FUNCTIONAL_DESIGN_V1.md` | adopted design (V1) | the *attempt* component named as part of identity — agrees with `L8-09`; and **restates `C-02` as Boss's** |
| **P15** | **Accounting Core Team B `B11` row 9**: *"Every proposed Entry from an originating domain must carry that domain's own idempotency reference as part of its origin data"* | `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/B11_EXCEPTION_FAILURE_MODEL.md` | Team B design | **apparent conflict with `XMC-C-A2`** (*the source module never assigns identity*) — reconciled at §3: the *"domain's own idempotency reference"* is the occurrence + attempt identity the emitter owns (`E15-A1` payload parts), not an accounting-event identity |

> **`C5-01-F-01`. The object the programme has recorded as *"does not exist"* and *"none has been
> designed"* exists as a specified identity basis (`P2`), a Boss-ruled ownership model (`P1`), a
> consumer obligation (`P3`, `P4`), a scoping half (`P5`), **an act-level attempt-identity contract
> in a Team B design (`P13`) and an adopted V1 design naming the attempt component
> (`P14`)** — in seven documents that do not cite each other.** What has never existed is **one adjudicated statement** of which position governs which
> question, and a reconciliation of the one genuine conflict among them (`P6`, §6). **That is an
> adjudication, exactly as `C4-02-F-07` predicted, and this file is it.**

---

## 3. Who owns the business fact, and therefore what element 15 *is* on the handoff

`BD-ACC-01` settles ownership and it settles the shape of element 15 with it:

| Object | Owner (`BD-ACC-01`) | Consequence for element 15 |
|---|---|---|
| The **business fact** (a completed movement, a scrap, a count application…) | **Source module** — Inventory | Inventory identifies the **occurrence** and presents it. It may present the same occurrence repeatedly (`XMC-C-A2`); it **never mints an accounting identity** |
| The **Accounting Event Identity** | **Accounting Core** | Computed **deterministically** from the basis (`XMC-C-A3`); recognises a repeat presentation as the same event (`XMC-C-A6`) |
| The **posting** | Posting Engine | Consumes the identity; enforces idempotency of posting on it (`ARC-WP-004` §12.1) |

> ### Adjudication `E15-A1` — what the payload carries
> **Element 15 on the emitting side is not a key minted by the emitter. It is the *deterministic
> identity basis* of the presented fact — the components the emitter owns:**
> **(tenant, company, owning source domain, business-fact occurrence identity as the owner identifies it).**
> **The Accounting Core completes the basis with the recognition role and the policy version in force
> (both Accounting-owned), and derives the Accounting Event Identity from all six parts and nothing
> else.** *(Adopted verbatim from `XMC-C-A3`; the adjudication adds only the split of ownership of the
> six parts, which `A3` leaves implicit.)*

Two consequences the programme has been missing by treating element 15 as *one* object:

1. **A Pre-Test case for element 15 is writable today** — *present the same basis twice; expect one
   event* — against a specification that exists (`P2`). It is not executable (§9). **This changes the
   reading of `SA_CORR4_07` §5's *"must not be written"*: written yes, executed or read as passing no**
   (`CHA-14`; logged at `SA_CORR5_06` row 16).
2. **The source-side attempt identity (`P6`) is a different object.** It prevents *one physical act
   being recorded as two facts*; element 15 prevents *one fact being recognised as two events*. §6.

---

## 4. Reconciliation with `BD-ACC-01`, clause by clause

| `BD-ACC-01` clause | Reconciled by | Result |
|---|---|---|
| Source Module owns the Business Fact | `E15-A1`; `XMC-C-A2` | **CONSISTENT** — the emitter owns the occurrence, presents it, never assigns identity |
| Accounting Core owns the canonical Accounting Event Identity | `XMC-C-A2`, `A3` | **CONSISTENT** |
| Posting Engine owns Ledger Posting | `ARC-WP-004` §12.0/12.1 | **CONSISTENT** — the posting engine is a *consumer* of the identity and idempotent *on* it |
| Identity distinct from Source Document / Journal Entry / Reconciliation Matching Number | `XMC-C-A5` — **stronger**: such numbers may not be *inputs* either. **Live hazard on the record**: an evidenced reset-to-1 path re-issues journal-entry numbers (P08, entry numbers not unique) | **CONSISTENT, and the contract is stricter than the ruling in the direction the evidence requires** |
| Immutable in identity and provenance | `XMC-C-A11`(iv) identity does not change when policy changes — because policy version is *inside* the basis; `A7` replay provenance travels **beside** the identity | **CONSISTENT** |
| Same-event retry must not create duplicate accounting events | `XMC-C-A6` | **CONSISTENT** — and stated as an obligation on the party that owns identity |
| Reversal is a new accounting event referencing the original | `XMC-C-A8`, `A9` | **CONSISTENT** |
| Every accounting event bounded by Tenant + Company | `XMC-C-A10`; tenant and company are basis parts 1 and 2 | **CONSISTENT** — and it is this clause that **disqualifies `P8`** (§7) |

**8 of 8 clauses reconciled; 0 conflicts.** The contract was written under the ruling and follows it;
the reconciliation was never *published* as a table, which is the visibility failure `C4-01-F-07`
named.

---

## 5. Tenant + Company scope, and the four behaviours the master prompt names

### 5.1 Scope

- **Identity is Tenant + Company bounded by construction**, because both are basis components
  (`XMC-C-A3`, `A10`; `MTI-01`, `MTI-04`). Two tenants presenting byte-identical occurrence identities
  produce two different event identities. **Cross-tenant identity collision is impossible, not
  prevented** — which is what `SCOPE-AWARE EVERYWHERE` requires of a `COMPANY`-scoped fact.
- **A fact whose company cannot be determined has no identity and cannot be recognised** (`A10`). The
  contract fails closed, in the same direction as `MTI-20` and `CF-I-03` §3.11.
- **Namespace** (`A13`): the owning domain is part of the basis, so Inventory and Manufacturing cannot
  mint one identity for two facts.
- **Replay preserves tenant and company** (`XMC-C-D1` rule `R6`; `MTI-41`): a replayed fact keeps the
  identity of the fact it replays; context is never re-resolved from current configuration.

### 5.2 Behaviour matrix

| Behaviour | Rule | Source |
|---|---|---|
| **Retry** (same occurrence presented again by the same emitter) | Same basis → **same identity → no second event.** The emitter need not know it is retrying | `A6` |
| **Duplicate submission** (same occurrence presented twice by two paths, e.g. interactive and integration) | Same basis → same event. **The path is not in the basis** (`A5` excludes processing actor and arrival order) | `A3`, `A5` |
| **Second genuine occurrence** (two real movements of the same product) | **Different occurrence identity** — the fact's **canonical identity as `L8-09`/`P14` define it: document line + attempt identity**, each a distinct owner-assigned immutable identity; **never the human-readable document *number* or any sequence** (`XMC-C-A5` excludes those as inputs — `CHA-06`; the first freeze cited `MTI-09` numbering here and is corrected). `MTI-15`: one fact resolves to exactly one company → **two events, correctly** | `L8-09`, `P14`, `A5`, `MTI-15` |
| **One fact, two roles** (a validated outbound movement bears stock-issue **and** cost-of-sales roles) | **Two events over one fact**, because the role is in the basis | `A4` |
| **Reversal** | A **new** event whose basis includes the reversed identity in the reversal role; each discoverable from the other; never mutation, never deletion | `A8` |
| **Correction after effect** | Reversal + new event only. Re-dating is alteration, not correction | `A9` |
| **Replay / migration** | Identity preserved; replay-batch provenance (element 14) travels **beside** the basis, never inside it — inside, replay would become duplication | `A7` |
| **Cross-module join** | The event identity is sufficient to join every downstream artefact of one commercial act, cost half and revenue half included | `A11`(ii) |
| **Out-of-order arrival** | Consumers reconcile; they never infer from order. An identity implies neither a posting nor a final amount | `A12` |
| **Policy change** | Identity unchanged. **Clarification of `A3` part 6 (`CHA-07`):** the policy version in the basis is the version **in force at the fact's physical event date** (element 3) — a value derivable from the fact, never from processing time (`A5`); a retry that crosses a policy-version boundary therefore yields the **same** identity (`A6` holds), and a deliberate re-recognition under a later policy is a **correction event** (`A9`), not a second identity. **Category policy versioning (effective-dated, `MTI-36` pattern) is a specification obligation this clarification creates — `BD-ACC-03A/B` rule values and owner, not versions.** Stated here as the SMEs Core position: every category policy value carries effective-from, and a recognised event is not re-computed by a later change. **The behaviour on a policy or category change mid-period is the open COGS research item `CGS-U07`/`U08` (`SA_CORR5_10` §3.1); this clause does not pre-empt it** (`CHD-08`) | `A3` part 6, `A5`, `A6`, `A9`, `A11`(iv) |

---

## 6. The one genuine conflict — the source-side attempt identity — separated exactly

`P6` states that the movement fact's identity is *"document line plus attempt identity"* and that the
attempt component does not exist. `P2` states that a second presentation of the same basis is the same
event. **Read together they appear to disagree about whether element 15 exists.** They do not, once the
two duplicates are distinguished — which `P7` already does in principle and nobody has applied:

| Duplicate class | What happens | Detected by | Governing object |
|---|---|---|---|
| **D-HANDOFF** — one fact, presented twice | Accounting would recognise two events | The identity basis — same basis, same identity | **Element 15 = `E15-A1`. Specified** |
| **D-SOURCE** — one physical act, recorded as two facts (a completion written twice because the *write* was retried) | Inventory holds two facts with two occurrence identities; both are correctly contextualised (`MTI-19` reports no breach); each yields its own accounting event, **correctly, over a wrong Stock Truth** | **Nothing today** — `L8-09` | **Not element 15.** It is a Stock Truth integrity property of the Inventory write path |

> ### Adjudication `E15-A2` — the attempt identity is specified here as a contract clause, and is not element 15
> **`XMC-C-A14` (new, Phase SA):** *Every state-changing act on a business fact carries a
> caller-declared **attempt identity**, scoped to the act's `CTX`. The store commits at most one fact
> per (`CTX`, attempt identity); a repeated attempt returns the result of the first and records that
> it did so. An act presented with no attempt identity is refused, never defaulted.* Lineage:
> `MTI-31` (run-level scoping and mutual exclusion — this clause is the act-level form), `MTI-20`
> (fail closed), `L8-09` (the missing component named), `IV-06`.
>
> **This closes the *specification* of `RISK-C02` at Phase SA level and nothing more.** The runtime
> property — that the write path actually commits at most once — is a build-and-test obligation
> (§9, `RT-E15-06`). **It is owned by Inventory + SaaS Foundation, not by Accounting**, and it is
> deliberately kept out of the identity basis: an attempt identity is a processing artefact of the
> kind `A5` excludes, and putting it inside the basis would make a retried write a second event.

**Why Phase SA may state `A14`:** the Boss closure act authorises *"interface/boundary definition"*
and *"data-model design subject to the SMEsPlus DNA constitution"*; `A14` is a boundary obligation on
the emitting side stated in business-semantic terms with no representation. It extends the `XMC-C-A`
family, which is Phase SA's own artefact, rather than minting into the Inventory `MTI-*`/`CF-I-*`
namespaces.

---

## 7. Carriers rejected (master prompt §4 item 7)

| Carrier | Why rejected |
|---|---|
| **`P8` — the reference-estate constraint** | Table-global (violates `A10` / `BD-ACC-01` clause 8 by construction); optional module; **admits unlimited empty values** — a uniqueness check over it passes on every row (`C4-07-F-03`). Non-deterministic *and* not duplicate-preventing |
| **`P3` §12.7 "event ID" read as a delivery-time identifier** | A delivery/publish identifier is minted at processing time → excluded by `A5`. **Accepted only under the reading that the event ID *is* the Accounting Event Identity derived from the basis** — in which case `P3` and `P2` agree. Recorded as a **correction owed to `ARC-WP-010`** when it is reviewed (`C4-D-01` fold): *"event ID / business key"* must read *"the deterministic event identity of `XMC-C-A3`"* |
| **Any wall-clock, actor, arrival-order, resettable counter, document / journal / matching number** | `A5`, with the live entry-number-reset hazard on the record |
| **`P9` — an unkeyed retry** | `FR-INT-004` is the **outbound** webhook (`CHA-05`); its rule is that the payload carries the event identity so the external receiver can deduplicate. The **inbound** client paths (`FR-INT-001`/`-003`) carry no tenant, company or key: handled at `SA_CORR5_02` class 6 — an inbound presentation is bound by `A14` and `E15-A1` like any other emitter |
| **An identity that is the attempt identity** (`A14` inside the basis) | Would make a retried write a new event — §6 |

---

## 8. Semantic sufficiency for Phase SA — tested against the contract's own §4 gate

| §4 disqualifier | Element 15 after this file |
|---|---|
| missing | **No** — basis, ownership split, behaviours, exclusions, namespace and scope are all stated |
| ambiguous | **No** — six parts declared; ownership of each part declared (§3); the one ambiguity (`P3`'s key source) resolved and recorded |
| unsupported by evidence | **Specified, not built, not verified** — runtime (§9). *A specification is not evidence of behaviour; it is evidence that a test can be written* |
| contradictory across the two domains | **No** — the only apparent contradiction (`P6` vs `P2`) is two objects, §6 |
| dependent on an unapproved assumption | **No** — depends on `BD-ACC-01` (approved) and, for the policy-version part, `BD-ACC-03A`/`03B` (approved 2026-09-08) |
| unable to link reversal/correction to the original | **No** — `A8`/`A9` put the reversed identity in the basis |
| unable to prevent duplicate/replayed effects when required | **Prevented by specification; proof runtime** |
| missing company/tenant isolation context | **No** — parts 1 and 2 |

> **Element 15 is semantically sufficient for Phase SA.** What it is not is *proven*, and no Phase SA
> round can make it so.

---

## 9. Runtime-only proof obligations — separated, and written so a Pre-Test case can be scheduled

| ID | Obligation | Positive / negative / instrument |
|---|---|---|
| `RT-E15-01` | Present one basis twice → exactly one Accounting Event; second presentation returns the first identity | positive |
| `RT-E15-02` | Same occurrence, two recognition roles → two events, each joinable to the occurrence | positive |
| `RT-E15-03` | Reversal event discoverable from its original and vice versa; the original is unchanged byte-for-byte | positive |
| `RT-E15-04` | Two tenants, byte-identical occurrence identities → two distinct events; **never-transacted tenant returns a structurally different result from a clean one**, not the same zero | negative + discriminating population |
| `RT-E15-05` | Replay of a batch reproduces identical identities and adds zero events; batch identity present beside each, absent from the basis | positive + element 14 |
| `RT-E15-06` | `A14`: the same attempt identity written twice → one fact; a write with no attempt identity → refused and recorded | positive + negative |
| `RT-E15-07` | An identity computed on day 1 and recomputed on day 90 from the stored basis is byte-identical (determinism across time) | positive |
| `RT-E15-08` | **Synthetic injection**: inject one fact whose basis differs by one part; confirm the event count moves `1 → 2`. Proves the predicate can fire | instrument |
| `RT-E15-09` | **Coverage assertion**: presentations requested vs recognised vs refused published beside every run | instrument |

`MTI-31`'s run-level property and `A14`'s act-level property are tested separately (`N-05` binds: one
axis per test).

---

## 10. Re-run of what element 15 alone was blocking (master prompt §4 item 9)

**Invariants.** `MTI-31` was `SA-SPEC-GAP` *only* because *"it is element 15"* (`SA_CORR4_06` row 13).
With `E15-A1` and `A14` specified it moves to **`SA-SPEC-COMPLETE / RUNTIME PROOF REQUIRED`** — the
same class as the other 18. `MTI-15`'s *"attempt component of the fact's identity is `RISK-C02`, not
designed"* qualifier is discharged at specification level. `MTI-46`'s count half was already runtime.

**Scenarios.** Element 15 was the one blocker common to all 22 (`SA_CORR4_07` §5). Removing it from the
Phase SA ledger changes the **idempotency-contract dimension** to `SA CONTRACT COMPLETE — RUNTIME
PROOF REQUIRED` on **22 of 22**. It does **not** by itself change any scenario's aggregate class: the
other gap classes — the re-measured COGS residual, the eight named mechanisms, the Boss elections and
element 14 — are adjudicated dimension by dimension at `SA_CORR5_10`, which is where the aggregate is
computed. **A round reporting 22 aggregate movements from this file alone should be disbelieved, for
the same reason CORR3's counterfactual applied to element 10.**

**Handoff elements.** Element 15 moves from *"Not suppliable — `RISK-C02`"* (`06` §4) to **`specified,
not built, not verified`** — the `AAS-V-01` wording, applied to element 15 by analogy and no other.
Element 12 (*original event*) and 13 (*reversal/correction link*) lose the qualifier *"weakened by the
absence of the attempt identity"*; their carriers are `A3` part 4 and `A8`. **`0 of 10` handoffs
contract-compliant is unchanged.**

---

## 11. Boss decisions on element 15 — one remains (`C-02`), and why

| Question carried | Disposition |
|---|---|
| *"Is idempotency gate-blocking?"* — `UAE-29`, carried by CORR4 as Boss's | **`UAE-29` is the Account root blocker *"no accounting-event identity"* (P11 `B-02`), and Boss ruled it as `BD-ACC-01` on 2026-09-08.** The closure act lists `BD-ACC-01` among rulings that *"must not be re-asked without material delta."* **Not a Boss decision; a Boss decision already taken** (`C5-B-03`) |
| Inventory `C-02` — *"idempotency and replay: gate-blocking, or design input"* — owner **"Boss directly"** (R4 `07_L6` line 210; restated at line 222 *"an unresolved Boss decision across multiple rounds… R4 does not decide it"*; R1 `03` §7.2; R2 `04` §7.2; `P14`; `GAP-FS-06`) | **Remains an open Boss severity election** (`CHA-01`, `CHB-06`). The first freeze of this file declared it *dissolved* on two instruments — the contract's §4 gate and the CORR5 master prompt's own law — and that was SMEs Core deciding a Boss-reserved item: four registers say it is Boss's, R4 itself advanced the same contract-§4 argument and still declined, and a commissioning prompt is not a ruling by identifier. **SMEs Core position, offered and not adopted:** at scenario level the contract §4 already makes duplicate prevention a `PASS / VERIFIED` precondition; at phase level the specification is complete and the proof is runtime, so `C-02` is *design input, not phase-holding*. **Boss decides; the election is cell-neutral in `SA_CORR5_10`** |

---

## 12. Outcome

> # `ADJUDICATED — SA SPEC COMPLETE / RUNTIME PROOF REQUIRED`

**Adopted:** `P1` (governs ownership and scope) · `P2` (governs the identity — `XMC-C-A1`…`A13`
verbatim) · `P3`/`P4` (governs consumer and posting obligations, under the §7 reading) · `P5`
(run scoping) · `P7` (the two-duplicates distinction).
**Originated, as contract clauses in Phase SA's own namespace:** `E15-A1` (ownership of the six basis
parts and what the payload carries) · `XMC-C-A14` (attempt identity on state-changing acts).
**Rejected:** `P8`, the delivery-time reading of `P3` §12.7, and every `A5`-class input.
**Corrections owed to other artefacts, recorded and not applied here:** `ARC-WP-010` §12.7 wording
(fold into `C4-D-01`); `06_CROSS_MODULE_HANDOFF_CONTRACT_FIELDS` §4 row 15 status (Inventory-owned;
non-material once this file is the controlled reading — `SA_CORR5_14` §3).

---

## 13. Residual, and what a challenger should attack first

1. **`A14` consolidates `P13` (`FV006-INT-001`, Team B design) and `P14`/`L8-09` into
   the cross-module contract; it is not without prior source** (`CHA-02` — the first freeze said it
   was). Attack it on authority: is an act-level attempt identity a *boundary* obligation (within
   authority) or a *storage design* (outside it)? The defence is that it states a property of the
   emitting side's acts, not a representation, and that a Team B design already states it.
2. **`E15-A1` assigns the recognition role to Accounting.** A reader could argue the emitter knows the
   role (a delivery *is* a cost-of-sales trigger). The defence is `BD-ACC-03A`: recognition timing is a
   Product-Category **policy**, owned on the Accounting side, so the role cannot be the emitter's to
   declare.
3. **The determinism claim is a claim about a function nobody has written.** `RT-E15-07` is the test;
   nothing here executes it.
4. **`P3` and `P4` are `DRAFT · HOLD` and unreviewed.** Adopting their obligations does not lift their
   status; `C4-D-01` carries the review.

## 14. Checkpoint

> ## `CP-SA-C5-10 — ELEMENT 15 ADJUDICATED`
> **15 candidate positions located (327-path population, reduction rule published) · 7 adopted (`P1`, `P2`, `P3`, `P4`, `P5`, `P13`, `P14`; `P7` consumed as the boundary; `P15` reconciled; `P6`, `P8`–`P12` characterised) ·
> 2 clauses stated in the contract namespace (`E15-A1`, `XMC-C-A14` — the latter consolidating `P13`/`P14`)
> · 5 carriers rejected · 8 of 8 `BD-ACC-01` clauses reconciled · 1 clarification to `A3` part 6 ·
> 9 runtime obligations separated · 1 Boss election remaining (`C-02`, carried; `UAE-29` ruled by
> `BD-ACC-01`) · 1 finding (`C5-01-F-01`) · corrected by `CHA-01`, `-02`, `-05`, `-06`, `-07`, `-14`.**
> **Element 15: `specified, not built, not verified`. `0 of 10` handoffs compliant. 0 vetoes discharged.**

**Next autonomous action:** `CP-SA-C5-20`, `G1` execution-context closure (`SA_CORR5_02`).

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
