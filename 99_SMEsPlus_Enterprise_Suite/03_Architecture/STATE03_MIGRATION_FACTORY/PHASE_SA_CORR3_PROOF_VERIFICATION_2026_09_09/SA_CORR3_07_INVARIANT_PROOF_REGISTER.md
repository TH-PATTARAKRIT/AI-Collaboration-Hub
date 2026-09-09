# SA_CORR3_07 — INVARIANT PROOF REGISTER
## CP-SA-C3-40 — INVARIANT PROOF STATUS COMPLETE

Executor: SMEs Core · finding prefix `INV-PR-` · **Topology Scope: `SHARED SaaS POOL`** (declared, per `CF-I-08`)
Frame: **`CORR3-FRAME`**, adopted by pointer.

**Status:** `58 INVARIANTS IN POPULATION — 0 PROVEN — 0 NOT APPLICABLE — 0 SUPERSEDED — 58 HOLD —
PROOF MISSING — 0 LEFT AS "SPECIFIED" — 11 FINDINGS RAISED — RECOMMEND HOLD`

> **Identifier discipline.** Findings are numbered `INV-PR-nn` and **not** `INV-F-nn`. `INV-F-01`…`-41`
> is an **occupied family** in this same corpus (41 Inventory function identifiers), present in 24 blobs
> of the frame. `INV-PR-` returns **0** blobs before this file. **The assigned prefix is honoured; the
> sub-namespace prevents a collision that would have been silent.**

> **Orchestrator intake note.** Same-model executor; `INTERNAL ADVERSARIAL SELF-CHALLENGE`; **not
> adopted on its word.** `INV-PR-08`'s load-bearing negative was re-executed independently and
> **CONFIRMED**: over the 35 unique paths / 35 blobs of the two isolation packages, `BD-ACC-01` → **0**,
> `BD-ACC-02` → **0**, `BD-ACC-03` → **0**, `GB-08` → **0**, while the positive control `MTI-D-01` fires
> at **26**. The instrument reaches; the four rulings are absent.

---

## 1. Declared population and unit

### 1.1 Controls

Positive `BD-ACC-01` = **55 blobs** (declared 55, matches); positive `clean.room` (-i) = **1,266**
(matches); negative `BD-ACC-99zz` = **0**; negative `MTI-99` inside the register = **0**.

### 1.2 Population, unit, path set, pattern

| Clause | Value |
|---|---|
| **POPULATION** | The invariants defined by the conformed set `03_MTI_INVARIANT_SET_R2_CONFORMED.md`, blob `e57fd5be…`, **sole blob for that path across all 184 branch heads** |
| **UNIT** | **One defined invariant** = one row whose leading table cell is an invariant identifier and which carries an R2 status. **Not** a token occurrence, **not** a file, **not** a proof requirement, **not** a matrix row |
| **PATH SET** | `CORR3-FRAME`. The two isolation packages within it resolve to **35 unique text paths** — which is also the figure a peer reports, **and it is `U2`, not `U1`** |
| **PATTERN** | `MTI-[0-9]{2}` and `CF-I-[0-9]{2}`, anchored to a leading table cell. Case-sensitive |

### 1.3 The two-shape count

**Shape 1 — token sweep (deliberately over-wide): 59.**
**Shape 2 — defining rows only: 58.**

**Discriminator, printed before counting.** The one-token difference is `MTI-51`, whose sole occurrence
is prose: *"They are not numbered `MTI-51`+ because folding them into that sequence is a consolidation
act belonging to AAS+ and Boss."* **It is prose about a number that was deliberately not assigned. It is
not an invariant.**

> ### `INV-PR-01` — the denominator of 58 is correct, and it is the *only* published isolation count reproducible to the unit.
> **POPULATION 58, UNIT "one defined invariant", two shapes agreeing at 58 after one explained
> exclusion.** The set is `MTI-01`…`MTI-50` (50) + `CF-I-01`…`CF-I-08` (8). **CORR2's verbatim carry —
> `50 CARRIED + 8 ADDED = 58 INVARIANTS SPECIFIED — 0 PROVEN` — is exact at the invariant unit.**
> Recorded positively because the same programme published "52 files" for a figure that was 35 unique
> paths, **and because a count I could not reproduce would have blocked this whole register.**

### 1.4 What is *not* in the population, stated as a set

Excluded, with authority: the 60 proof requirements (different unit, different owner); the 35
context-matrix rows; the 41 function rows and 9 enforcement-point classes; the 3 cross-context register
entries; the 16 handoff contract elements and 11 context fields; the 30 proof scenarios and the 8
isolation proofs. **Each is cited *as evidence* below; none is counted *as an invariant*. Conflating any
of them into 58 is the failure mode this section exists to prevent.**

---

## 2. Method — the rule, stated before it is applied

### 2.1 What counts as proof at Phase SA

> **A Phase SA proof is one whose truth-maker exists inside the artefact corpus today.** The proposition
> must be a claim about documents, declared scopes, enumerated sets or standing ruling text, and it must
> be dischargeable by reading and counting them **with a command whose output is published.**
>
> **A Phase SA proof is not** a demonstration that a running system behaves as the invariant requires.
> **No implementation exists** — `0 of 60` proof requirements executable, `0 of 52` negative access tests
> executable, *"because no implementation exists"*. **Nothing about runtime behaviour is reachable from
> here.**

### 2.2 The three things that must never be dressed as a proof — stated as prohibitions

| # | Prohibited move | Why |
|---|---|---|
| **M-1** | Recording *"the invariant's text conforms to a standing Boss ruling"* as a proof **of the invariant** | **Conformance is a property of the *text*. The invariant asserts a property of the *system*.** Proving the first says nothing about the second. **The single most available error in this task**, because 14 of the 58 were re-specified precisely to conform, and the conformance is genuinely well-evidenced |
| **M-2** | Recording an invariant as proven because a *facet* of it is corpus-testable | `MTI-05` has a declaration half (corpus-testable) and a store-and-control half (runtime). **Proving the first is not proving `MTI-05`** |
| **M-3** | Recording an invariant as proven because its **permitted case is presently empty** | `CF-I-06` prohibits reliance on a cross-company correspondence *"until a controlled mapping … is specified"*. No such object exists, so nothing violates it today. **Vacuous non-violation by an absent population is not proof of a prohibition over future paths** |

### 2.3 The classification decision procedure

First match wins. **(1)** Is the content **entirely** a property of the current corpus, and did I run the
test? → the run's outcome decides; **a run returning a counter-example does not yield `PROVEN`**.
**(2)** Out of scope for the shared SaaS pool, evidenced? → `NOT APPLICABLE — EVIDENCE-BACKED`.
**(3)** Replaced by a later standing ruling, evidenced at claim level? → `SUPERSEDED — EVIDENCE-BACKED`.
**(4)** Otherwise → **`HOLD — PROOF MISSING`**, with the exact proof gap and the earliest phase at which
it becomes provable.

### 2.4 Earliest-provable labels

`P-NOW` corpus-testable now · `P-BUILD` provable only against an implementation **(not a Phase SA act and
not a Phase SA authorisation)** · `P-RULE` a build alone is insufficient; an unruled Boss decision fixes
the content or scope first · `P-ENUM` blocked by a missing **enumeration** that is an evidence act, not a
build · `P-CAP` blocked by a capability nobody has designed — **later than `P-BUILD`, not earlier**.

### 2.5 Standing constraints

`AAS-V-01` (element 10 wording is `specified, not built, not verified`, **no substitute**), `AAS-V-02`
(condition satisfied, **not discharged**), `AAS-V-03`, `RC-V-01` (remedy produced, **not discharged**),
`CF-V-01`, `CF-V-02` — **6 in force, 0 discharged.** Under the 8-Criteria Exit Constitution the whole
conformance package is `PROVISIONAL / NON-CANONICAL`. **Nothing below alters any of these.**

---

## 3. The per-invariant register — summary by family

The full per-invariant detail (invariant · why it exists · owner · affected domains · enforcement point ·
evidence · proof logic · verification run · result · earliest-provable) is carried family by family. The
governing facts:

| Family | Span | n | Result | Binding earliest-provable |
|---|---|---:|---|---|
| **A — Context Spine** | `MTI-01`…`06` | 6 | all `HOLD — PROOF MISSING` | `P-BUILD` ×4, `P-ENUM` ×1 (`MTI-02`), `P-CAP` ×1 (`MTI-06`) |
| **B — Object Anchors** | `MTI-07`…`16` | 10 | all `HOLD` | `P-BUILD` ×5, `P-RULE` ×4 (`MTI-08`, `-09`, `-13`, `-16` valuation facet), `P-CAP` ×1 (`MTI-15`) |
| **C — Enforcement** | `MTI-17`…`22` | 6 | all `HOLD` | `P-BUILD` ×4, `P-ENUM` ×1 (`MTI-18`), `P-RULE` ×1 (`MTI-22`) |
| **D — Visibility and Derivation** | `MTI-23`…`28` | 6 | all `HOLD` | `P-BUILD` ×5, `P-RULE` ×1 (`MTI-25`) |
| **E — Execution Boundary** | `MTI-29`…`33` | 5 | all `HOLD` | `P-BUILD` ×3, `P-CAP` ×1 (`MTI-31`), `P-RULE` ×1 (`MTI-33`) |
| **F — Configuration and Template** | `MTI-34`…`37` | 4 | all `HOLD` | `P-BUILD` ×2, `P-RULE` ×2 |
| **G — Identity, Event, Audit, Replay** | `MTI-38`…`42` | 5 | all `HOLD` | `P-BUILD` ×2, `P-RULE` ×1, `P-CAP` ×2 (`MTI-41`, `-42`) |
| **H — Handoff Carriage** *(the element 10 family)* | `MTI-43`…`46` | 4 | all `HOLD` | `P-BUILD` ×2, `P-RULE` ×2 |
| **I — Lifecycle** | `MTI-47`…`50` | 4 | all `HOLD` | `P-BUILD` ×3, `P-RULE` ×1 (`MTI-49`) |
| **CF — added by the rulings** | `CF-I-01`…`08` | 8 | all `HOLD` | `P-BUILD` ×5, `P-RULE` ×2, `P-NOW` ×1 (`CF-I-08`, **tested and contradicted**) |

**6 + 10 + 6 + 6 + 5 + 4 + 5 + 4 + 4 + 8 = 58** ✓, and each family's row count equals its declared
identifier span.

### 3.1 The rows that carry the register

- **`MTI-02`** — no cross-tenant effect *"under **any** code path"*. **The "any code path" quantifier
  means the proof needs the *path set*, not a sample — and the privileged-path enumeration does not
  exist.** `P-ENUM`, then `P-BUILD`.
- **`MTI-05`** — *"exactly one context anchor"*, **contradicted now** by the declaration half (§6.1).
- **`MTI-11`** — the product-identity invariant, **inverted** by ruling Option B. `RC-P-05` is the
  discriminating test: creating the identical code/name/barcode/UoM set in two companies must **succeed
  in both with no duplicate condition, warning, merge suggestion or data-quality flag** — **the proof
  that Option B was *implemented* rather than *tolerated*.** Not run. **A conformance edit is not a
  proof (M-1).**
- **`MTI-17`** — enforcement beneath application code. **Not merely unbuilt:** whether such enforcement
  is achievable in a chosen technology is a question *"not approached by any session in this chain,
  including this one."*
- **`MTI-18`** — no unaudited privileged bypass. **Unverifiable in principle today**: the bypass-path
  audit was **started and never completed**, so the path set is not enumerated, and the corresponding
  proof requirement is `NOT DEFINABLE` for the same reason. **The single deepest gap in the set**, and it
  blocks `MTI-02`, `MTI-17` and part of `MTI-38`.
- **`MTI-19`** — the context conformance control. **The hard case is on the record:** a replay without an
  attempt identity produces duplicates *individually context-correct and collectively wrong*, **and
  `MTI-19` would report no breach.**
- **`MTI-31`** — supplies run scoping and mutual exclusion, and **explicitly does not supply what
  matters**: no idempotency identity, so *a retried run remains indistinguishable from a second genuine
  run*. **`MTI-31` narrows the exposure; it must not be reported as removing it.**
- **`MTI-41`** — **the row where a passing test would be misleading.** A replay without an attempt
  identity satisfies `MTI-41` while producing duplicates. **The property would be satisfied by a broken
  system.**
- **`MTI-42`** — migration context explicit and evidenced. **The invariant now carries more than it can
  evidence**: deliberate duplicate preservation is a migration requirement, so `MTI-42` **prohibits the
  wrong act without being able to evidence the right one** — that evidence is a provenance reference
  **which does not exist**.
- **`MTI-43`** — element 10's carriage invariant. **Element 10 is satisfied by the tuples plus *both*
  attestations, never by a tuple alone and never by one attestation alone.** Its first negative test
  **cannot be constructed**: the second attestation references a control (`CF-I-03`) that **does not
  exist**. **The attestation is presently a reference to nothing.**
- **`MTI-45`** — **verification run executed:** the obligation matrix enumerates **8 distinct modules**,
  matching the invariant's list exactly. ***That verifies the module list is internally consistent; under
  M-1 it proves nothing about any consumer's behaviour.***
- **`MTI-49`** — tenant offboarding/erasure. **Empty in content**: the applicable data-protection scope
  has **zero coverage anywhere in the evidence chain**. **No AI may supply a legal scope and none is
  supplied here** — `HOLD / EVIDENCE REQUIRED` in the statutory dimension.
- **`MTI-50`** — **the invariant that makes every other invariant's evidence exist.** Nothing in the
  corpus retains anything, **because nothing runs.**
- **`CF-I-03`** — **the load-bearing absence in the whole set:** the authorization conformance control
  *does not exist*, `HF-CTX-11` references it anyway, and `CF-V-01` vetoes recording it as available.
  **It gates `MTI-43`.**
- **`CF-I-05`** — **the class enumeration does not exist and its closure is a Boss decision whose option
  (c) is to rule the whole construct out and withdraw `CF-I-05`.**
- **`CF-I-06`** — **Move M-3 explicitly refused.** The permitted case is empty today because no mapping
  object exists, **and vacuous non-violation is not converted into a proof.**

### 3.2 The one executed proof — `CF-I-08`

**Proposition.** Every artefact governed by `CF-I-08` states its isolation topology.
**Population.** The **35 unique text paths** of the two isolation packages, derived from the frame's
path join. **Unit: one file.** Chosen because `CF-I-08` names *invariants, matrix rows, enforcement
points, proofs, proof scenarios and attacks* — **every one of which lives inside these 35 files and
nowhere else.**
**Pattern.** `^Topology Scope:` (-i), per file. **Controls:** positive — the pattern fires on the
conformed register; negative — `Topology Scope zzqx` → 0.

| Outcome | Count | Which |
|---|---:|---|
| File **states** its topology | **8 of 35** | Conformance package files `03`–`10` only |
| File **does not** | **27 of 35** | Conformance `00`, `01`, `02`, `11`–`17`, **and all 16 files of the published invariant-set package** — including the authoritative text for the 50 carried invariants, the 35-row matrix, the enforcement points, the 8 isolation proofs and the attack register |

**At the stricter unit `CF-I-08` actually names — the invariant, not the file — the result is `0 of 58`.**
No invariant row states a topology. Coverage is supplied by **one blanket sentence in one file**, which
**does not reach the 50 invariants whose authoritative text lives in a different blob.**

**Classification.** **Not `PROVEN`.** The allowed vocabulary has no slot for *tested and contradicted*, so
it lands at `HOLD — PROOF MISSING` with the contradiction at §6.3 — **and the vocabulary gap is itself
raised as `INV-PR-11`.**

---

## 4. Result tally, cross-checked against its own rows

| Result | Count | Cross-check |
|---|---:|---|
| `PROVEN` | **0** | No row carries it |
| `NOT APPLICABLE — EVIDENCE-BACKED` | **0** | No row carries it |
| `SUPERSEDED — EVIDENCE-BACKED` | **0** | No row carries it. §6.5 gives the one near-miss and why it is not supersession |
| **`HOLD — PROOF MISSING`** | **58** | 6+10+6+6+5+4+5+4+4+8 = **58** ✓ |
| **Left as merely `SPECIFIED`** | **0** | Required by master prompt §10; §3 assigns an allowed result to every one of the 58 |

### 4.1 `INV-PR-02` — a tally published that contradicted its own listing, corrected in place

> The first `P-BUILD`/`P-RULE` header counts were written **before** the members were enumerated;
> enumerating them gave different figures. **The listings govern.** Final, reconciled:
> **`P-NOW` 1 · `P-BUILD` 32 · `P-RULE` 14 · `P-ENUM` 2 · `P-CAP` 5 · split-assigned 4 = 58.**
>
> **Two failed attempts are recorded rather than only the answer, because a prior round shipped six
> tables whose class tallies contradicted their rows while summing correctly, and a tally that is right
> on the third try but presented as right on the first teaches a reader nothing about how much to trust
> it.**

### 4.2 `INV-PR-03` — the conformed register's own status tally contradicts its own rows in two classes while summing to the correct total

Two shapes agree on the row-level classification:

| Class | `§15` asserts | Rows actually say | Delta |
|---|---:|---:|---|
| `SPECIFIED` unconditional | **41** | **42** | −1 |
| `SPECIFIED — CONDITIONAL` | 7 | 7 | ✓ |
| `SPECIFIED — VALUE HELD` | **5** | **4** | +1 |
| `SPECIFIED — RANK DEPENDENT` | 5 | 5 | ✓ |
| Total | 58 | 58 | ✓ |

> §15 lists the fifth `VALUE HELD` member as *"and the costing facet of the `MTI-11` category
> attachment"* — **a facet, not an invariant.** `MTI-11`'s own status row reads `SPECIFIED`, unqualified.
> **Counting a facet as a fifth member is a unit conflation inside the roll-up of the register whose
> entire subject is unit discipline, and it borrows the missing one from the unconditional class so the
> total still reads 58.** The predecessor set had it right; the conformed set regressed. **Corrected R2
> distribution: 42 / 7 / 4 / 5 = 58.** Materiality: low for the total, **material for reliance** — any
> downstream body counting "5 invariants held by the COGS Gap" **will look for a fifth and find a facet.**

### 4.3 A count I got wrong, published because the second shape caught it

First shape for "14 re-specified" returned **12**. Second shape returned **14**. **The register's claim
of 14 is correct; my first pattern was under-scoped** because two families carry an extra column and two
identifiers do not match a pattern anchored on the marker being the second cell. **The 14 stands. The
defect was mine.**

---

## 5. The invariants that gate handoff element 10

Element 10 is **unconditional** in the contract text (verified independently at `SA_CORR3_06` §1.1), and
its status is, and remains, **`specified, not built, not verified`** — wording mandatory under
`AAS-V-01`, **no substitute**.

### 5.1 The gating set — 11 of 58

| Invariant | What it must deliver for element 10 | What exactly would discharge it |
|---|---|---|
| `MTI-01` | A resolved single context per emitted fact | All 41 functions exercised and shown to emit a resolved pair; **`0 of 41` today** |
| `MTI-04` | Company never null on any record | The **bulk** reconfiguration case executed, showing **no** record re-derived without its company |
| `MTI-05` | The **anchor path** — the derivation chain, not just the value | (a) the matrix declaring **exactly one** anchor per object type — **contradicted today**; (b) the derived value stored and a control asserting stored = derived |
| `MTI-17` | Enforcement **beneath application code**, so the value is a *guarantee* not an assertion | Demonstrated against every path class. **Blocked upstream by `MTI-18`, and its feasibility is unapproached by anyone** |
| `MTI-18` | No unenumerated hole in the guarantee | **The privileged-bypass path enumeration.** **An evidence act, not a build — the earliest thing on this list that could start.** Until it exists, `MTI-02`, `MTI-17` and part of `MTI-38` are all unprovable |
| `MTI-19` | The **context** conformance control whose run the attestation names | The control built, running continuously, **raising without repairing**, runs retained and dereferenceable |
| `MTI-50` | Retention and inspectability of those runs | **Without it an attestation is a reference to something nobody can read** |
| `MTI-43` | Both attestations on the payload, and the rule that **neither alone suffices** | The three negative forms executed: attestation absent → reject; referenced run breaching → reject; referenced run predating the act → reject |
| `MTI-45` | Eight consumers treating context and authorization as mandatory, non-inferable | Per-module negative tests. **The Payment half additionally needs a ruling, and no Inventory-to-Payment handoff is published within the boundary** |
| `MTI-46` | Conservation — emitted population = received population per context | Count half executable against a build. **Value half `HOLD — ACCOUNTING COGS GAP` and not discharged by anything in this lane** |
| `CF-I-03` | The **authorization** conformance control the second attestation names | **The control does not exist.** No published invariant states it; a veto forbids recording the field as available meanwhile |

### 5.2 What this means for the `0 of 22`

> **`INV-PR-04`.** Element 10's gating set is **11 invariants, and not one of them is closer to proof
> than any other**, because all eleven bottom out in the same two absences: **no implementation, and no
> privileged-path enumeration.** Ranking them by effort would be an **invented ordering**. The only
> genuine ordering in the evidence is a **dependency** one: **`MTI-18`'s enumeration is the sole item that
> is an evidence act rather than a build**, and three other gating invariants are unprovable until it
> exists. **If any single thing on this list can start before a build is commissioned, it is that
> enumeration** — stated as a dependency observation, **not as a recommendation to commission anything,
> which is not my act.**

> **`INV-PR-05`.** Element 10's obligation **grew** under conformance, **and the growth is not visible in
> any status line.** Before: value + anchor path + **one** attestation. After: value + anchor path +
> authorization + **two** attestations, **one of which references a control that does not exist.** Both
> status lines read `specified, not built, not verified`, **identically, before and after.** **A status
> field that cannot express a regression will report a regression as stasis.** Any Phase SA body reading
> only the status will conclude element 10 did not move; **it moved further away.**

> **`INV-PR-06`.** `C2-F-12` is **verified against primary text and stands**, with one correction to its
> framing. `RISK-U03`'s stated ground — *"the invariant set does not exist"* — is false today: **it
> exists, 58 invariants, 35 unique paths**, read at the register rather than at a summary. **The
> correction:** `C2-F-12` characterises the remedy as *"Build and prove it — a Pre-Test / Development
> activity"*. **That is incomplete. Three of the eleven gating invariants cannot be proven by any amount
> of building** — `MTI-18` needs an enumeration nobody has done, `MTI-45`'s Payment half needs a ruling,
> and `MTI-46`'s value half needs the COGS Gap. **Framing the whole remedy as "build it" reproduces, one
> level along, the very error `C2-F-12` identifies: a correct conclusion carried on an incomplete cause.**

---

## 6. Contradictions and exceptions

### 6.1 `INV-PR-07` — `MTI-05`'s "exactly one context anchor" is contradicted, and the conformance session's claim that it removed "the only two" is measurably wrong

**The claim:** *"Row 5 was the only row in the matrix declaring two anchors for one object"*, repeated as
*"remove the only two matrix rows that declared a two-part anchor."*

**The measurement**, 35 numbered rows, two shapes agreeing:

| Anchor form | Count | Rows |
|---|---:|---|
| Single | 26 | — |
| Compound `X / Y` | **2** | Product, Product category |
| Compound `X + Y` | **5** | Lot/Serial, Reordering rule, Put-away rule, Adjustment/count, Scrap |
| **No anchor** | **2** | Tenant (the root — **legitimately anchorless**), **Inter-company transfer** |

**Both readings stated.** (i) If "two-part anchor" means only the slash form, the claim is true — **but
then `MTI-05`'s *"exactly one"* is left contradicted by five `company + X` rows nobody has looked at.**
(ii) If it means "more than one anchor declared", **the claim is false on its face by six rows.**
**`MTI-05` requires a *declared* anchor, so the notation is the declaration**, which favours reading
(ii). A defensible author intent for `company + location` is *"company, derived via location"* — a single
anchor written with its path — **but if so, the register whose entire subject is anchor singularity is
using an ambiguous notation in the one place it cannot afford to.**

**Not resolved here.** Re-scoring another body's matrix is that body's act. **Consequence:** `MTI-05` and
`CF-I-07` both inherit this.

### 6.2 `INV-PR-08` — the 58-invariant set has never been read against four standing Boss rulings, and `MTI-11` is under-constrained against two of them

**Method.** For each ruling, count files among the 35 in the isolation corpus that mention it. **Positive
control `MTI-D-01` → 26 of 35. Corpus-wide positive control `BD-ACC-01` → 55 blobs.** Negative → 0.

| Ruling | Files in the 35 |
|---|---:|
| `MTI-D-01`/`-02`/`-03` | **26** |
| `BD-ACC-01` · `BD-ACC-02` · `BD-ACC-03A`/`03B` · `GB-08` | **0 · 0 · 0 · 0** |

**Why this is material, not bookkeeping.** All four are **company- or tenant-scoping rulings by
subject**: `BD-ACC-02` is a statement about the `MTI-03` company boundary and about what `MTI-22` may ever
admit; **`GB-08` is already listed in Phase SA's own boundary matrix "by subject"** — so Phase SA knows it
belongs here, **and the invariant set does not carry it**; and `BD-ACC-03A`/`03B` set valuation and
costing **Product Category ONLY, no Product override**.

**The specific non-conformance.** `MTI-11` reads: *"every operational and financial attachment is anchored
to the same `company` … Costing and valuation attachment is company-scoped."* **As written this permits a
*product-level* costing/valuation attachment that happens to be company-scoped. `BD-ACC-03A`/`03B`
prohibit a Product override outright.** The composition *does* work structurally, because a conformance
delta makes Product Category company-anchored for both facets — **but the invariant does not say so, and
its text admits the prohibited shape.** `MTI-16` carries the same wording one family along.

**Classification.** **Not `SUPERSEDED`** — a Boss ruling narrowing an invariant's admissible shapes
requires a re-specification act by the owning body, **and declaring supersession on my own authority is
precisely the defect of promoting an open item to a rule.** **Recorded as an open non-conformance
requiring a delta the conformance package never ran.**

**Negative-claim boundary.** Tool `grep -c` per literal token, per blob, over the 35 paths. **I did not
search the Account-side packages for the reverse direction, and I claim nothing about it.** Authority for
the exclusion: my scope is the invariant register.

### 6.3 `INV-PR-09` — `CF-I-08` is contradicted over the corpus it governs

**8 of 35 files** state a topology; **0 of 58 invariants** state one individually. **Every file of the
published invariant-set package — holding the authoritative text of the 50 carried invariants, the 35
matrix rows, the enforcement points, the isolation proofs and the scenarios `CF-I-08` names by name —
carries no topology statement at all.**

**The mitigating fact, stated fairly:** the conformed file applies the scope in one blanket sentence and
**explicitly says *"Stating the scope does not supply the delta"*.** The session was honest about what the
statement is worth. **The unmitigated fact:** that sentence **cannot reach the other file**, and `CF-I-08`
was written to bind **the artefacts**, not one summary of them. **A pool-established result cited later as
evidence about a Private Company topology would find nothing on the artefact to stop it — which is the
exact harm the veto exists to prevent.**

**Exception permitted?** **No.** `CF-I-08` states none, **and I may not create one.**

### 6.4 Exceptions recorded

| Invariant | Exception | Permitted? |
|---|---|---|
| `MTI-04` | Platform template content | **Yes, and it is not an exception** — template content is a **separate object class**. `MTI-04` itself *"admits no exception"* |
| `MTI-14` | Within-company nested reordering overlap | **Not an exception — a non-closure.** `MTI-14` closes only the cross-company half; **the within-company overlap remains and no enforcement point addresses it.** Recorded so this register is not where it is lost |
| `MTI-24` | Cross-context aggregation | **Yes, exactly one:** a Report Grant under `MTI-25` — itself conditional on an unruled decision, and **under `AAS-V-03` may carry no valuation content** |
| `MTI-40` | A product's **own** company in the anchor-change list | **Prohibited outright** — *"is not in this list, and must not be added to it"* |
| `MTI-02`, `CF-I-08` | any | **None stated, none created** |
| `MTI-12` | Identical batch values across two companies | **Legitimate, not an exception.** What is prohibited is **presenting the bare value as the identity** |

### 6.5 The one near-miss on `SUPERSEDED`, and why it is not one

The **published** `MTI-11` **is** superseded by ruling Option B. **But the published `MTI-11` is not a
member of my population** — my population is the **conformed** set, in which `MTI-11` is already the R2
text. **Recording it as `SUPERSEDED` would be scoping a write wider than the read.** **0 members
classified `SUPERSEDED`, and the supersession that did occur is recorded as already applied.**

---

## 7. Residual uncertainty, exact proof gaps, and what to attack first

### 7.1 What could not be proven, and the exact gap

| Gap | Exact form |
|---|---|
| **57 of 58 invariants are unreachable from Phase SA** | Their truth-makers are runtime behaviours. `0 of 41` functions verified, `0 of 13` enforcement surfaces, `0 of 60` proof requirements, `0 of 52` negative tests, *"because no implementation exists"*. **This is not a defect of the invariants and is not reported as one. It is the boundary of the phase** |
| **The 58th was reachable and returned a counter-example** | `CF-I-08`, §3.2 / §6.3 |
| **`MTI-18` is unprovable in principle today, and is upstream of three others** | The privileged/system/background/administrative/migration path set is **not enumerated**; the audit was **started and never finished**, with the Gate blocked |
| **Five invariants are blocked behind a capability nobody has designed** | `MTI-06`, `-15`, `-31`, `-41`, `-42`. **`P-CAP` is later than `P-BUILD`, not earlier** |
| **`CF-I-03` gates `MTI-43` and therefore element 10, and does not exist** | No published invariant states it; a veto forbids recording it as available |
| **The reverse direction was not verified** | Whether Account-side packages compose the isolation rulings. **Tool: none run.** Authority: my population is the invariant register |
| **The 35-path population was not re-derived from a second source** | It matches a peer's independently reported figure — **two agreeing instruments, one of which I did not build, but both reading the same corpus.** A challenger with a different corpus should re-derive it |
| **The frame's complement is inherited, not re-measured** | **I did not test whether a later invariant revision exists only in non-head history** |

### 7.2 What a challenger should attack first, with my confidence stated

1. **`INV-PR-08`, the four unread Boss rulings.** Highest-value and the one with the most ways to be
   wrong. The negative is over a **narrow, declared** population — **narrow deliberately, because narrow
   negatives survive and wide ones rot.** But **a literal-token grep cannot see a ruling referenced by
   paraphrase, by its subject, or by a different identifier form.** **Attack it by searching for the
   rulings' *content* rather than their *identifiers*** — "Product Category", "no Product override",
   "FX", "accounting rate", "statutory posting" — across the same 35 files. **If any fires, my finding
   narrows from "never read against" to "read against without citing", which is materially weaker.**
2. **The `MTI-11` under-constraint.** I reasoned from the invariant's *wording* admitting a shape the
   ruling prohibits. **A challenger should test whether another file already closes it — and I read the
   most likely candidate only via extracts, not in full. That is a real gap in my own reading and I name
   it rather than let it be found.**
3. **`INV-PR-07`, the anchor count.** Two shapes agreed, **so the arithmetic is safe. The interpretation
   is not.** If the matrix owner states that `company + location` denotes one anchor and its derivation
   path, **my contradiction collapses to a notation observation on two rows.** **Get the owner's reading,
   not mine.**
4. **`INV-PR-09`, the `CF-I-08` test.** **The unit choice — file — is mine**, and `CF-I-08`'s own unit is
   the invariant/row/proof/scenario. **Both are reported precisely so the choice is visible.** Attack the
   population — **though `0 of 58` at the invariant unit does not move under any file-level re-scoping.**
5. **The blanket `HOLD — PROOF MISSING` on all 58.** The strongest attack on this whole register is:
   *"you found a way to do no work by declaring nothing provable."* **My defence is §2.2's three
   prohibitions, written before §3 and applied against my own interest** — at `MTI-05` (a facet I could
   test and refused to promote), at `MTI-45` (a run I executed **successfully** and explicitly declined to
   count as proof of the invariant), and at `CF-I-06` (a vacuously-unviolated prohibition I refused to
   call proven). **A challenger should test whether I applied them consistently, or only where the answer
   was going to be negative anyway — that is the shape of self-interested classification, and it is
   invisible to me.**
6. **`INV-PR-02`.** I published two wrong tallies before the right one. **Recount independently rather
   than trust the third attempt because it was the third.**

### 7.3 `INV-PR-11` — a vocabulary defect raised against the master prompt's own instrument

> **The four allowed results cannot express "tested and contradicted", and that collapses the most
> informative outcome into the least informative label.** `CF-I-08` was **executed**, with a positive
> control, a negative control, a declared population and two unit readings, **and it failed.** It is filed
> as `HOLD — PROOF MISSING` — **the same label carried by 57 invariants nobody could test at all.**
>
> **A register in which a disproof and an untested item are indistinguishable will lose the disproof at
> the first summarisation.** The same collapse hides `INV-PR-07` and `INV-PR-08`. **I have not invented a
> fifth label, because the allowed set is stated as closed and inventing one is not my act**; instead
> every such row is flagged and the contradiction stated at §6 — **and the flagging is recorded here as a
> workaround for a defect in the instrument, not a property of the evidence.**

### 7.4 Terminal position

**`58 invariants specified, 0 proven` was accurate when CORR2 reported it, and it remains accurate after
this register.** What this register adds is **not a change to that number** — it is **the reason the
number cannot move at Phase SA**, stated per invariant with the earliest phase at which each becomes
provable; **four contradictions the conformance chain had not recorded**; and the finding that **the
register's headline was arithmetically inconsistent with its own rows in two classes.**

**Nothing here discharges any veto.** `AAS-V-01`, `-02`, `-03`, `RC-V-01`, `CF-V-01`, `CF-V-02` — **6 in
force, 0 discharged, 0 findings closed, 0 capabilities built.** The conformance package remains
`PROVISIONAL / NON-CANONICAL`. Its discharge needs **two consecutive clean independent passes**, and this
register — same model, same session — is **`INTERNAL ADVERSARIAL SELF-CHALLENGE` and is neither of them.**

> ## `RECOMMEND HOLD.`

Checkpoint completion is **not** Boss approval. Boss remains the sole Final Approver.
