# SA_CORR4_05 — FOUR-CONDITION CLOSURE MATRIX

## CP-SA-C4-50 — FOUR CONDITIONS CLOSED OR EXACT HOLD RECORDED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR4-PREGATE-CLOSURE-001]`
Branch: `architecture/phase-sa-corr4-pregate-closure-2026-09-09-001`
Boss: **SOLE FINAL APPROVER**

---

## 1. The rule this matrix applies

Master prompt §7: **"No condition may be called closed merely because a document exists."**

Each condition below is judged against **its own stated closure criterion, quoted verbatim from the
master prompt**, and against nothing else. A condition is `CLOSED` only where the criterion is met on
evidence; where it is not, the exact residue is named and the condition is not closed.

> ### Result: `3 of 4 CLOSED · 1 EXECUTED TO THE LIMIT OF THIS SESSION'S AUTHORITY AND NOT CLOSED`

---

## 2. The matrix

| Condition | Evidence | SMEs Core result | Residual gap | **Gate effect** |
|---|---|---|---|---|
| **`C4-01`** Privileged-bypass path enumeration | `SA_CORR4_01` — **13 path classes** over 185 branches / 3,604 paths; positive + negative controls; coverage 21/21 tokens; **2 false zeros found and corrected** | **`ENUMERATION COMPLETE — EXACT BOUNDED GAPS LISTED`** | **5 named gaps `G1`–`G5`.** `G1`/`G3`/`G5` are SMEs Core design acts; `G2` is a contradiction inside a Boss-owned baseline (`C4-D-02`); `G4` has a named future owner | **CLOSED** — and it makes downstream security testing **writable**, which is the criterion |
| **`C4-02`** `XMC-C-D1` tenant + company emitting contract | `SA_CORR4_02` — **13 of 13** elements; **9 of 9** rules; **10 flows** proved | **`2 CONTRACT-SUFFICIENT · 8 CONTRACT-GAP`** | **8 flows have no artefact authored by the emitting party** — corrected from 5 by independent challenge (`C4-02-F-09`): Sales→Inventory, Sales→Manufacturing, Purchase→Inventory, Manufacturing→Inventory, AR/AP→Payment→Accounting, Asset→Accounting, Expense→Accounting, plus dropship's control-floor breach | **CLOSED** — the criterion is that the semantics are explicit and challenged across representative domains. **They are, and the 8 gaps are the absence of a counterparty, not of the contract** |
| **`C4-03`** `CF-I-03` authorization conformance control | `SA_CORR4_03` — 5 triggers · 6 inputs · 3 results · **8 deny conditions** · 1 exception path · **25 test classes** | **`MTI-43 CONTROL REFERENCE CLOSED`** | `P1`–`P6` test preconditions absent — **all runtime**. `MTI-50` is a hard upstream dependency; `CF-D-02` is Boss-gated | **CLOSED** — the criterion is a concrete testable specification with a real `MTI-43` dependency. **Both are met** |
| **`C4-04`** Compliance retraction propagation | `SA_CORR4_04` — denominator re-measured `185 / 2 / 183 / 0`; claim class established as **1 file on four instruments**; correction audited **4 of 4** and passes | **`PROPAGATION HOLD`** | **`origin/SMEsPlus` carries the uncorrected blob, and the repository is public — the claim is fetchable unauthenticated, `HTTP 200`** | **NOT CLOSED** — §3 |

---

## 3. `C4-04`, judged against its own criterion, and why it is not closed

**The criterion, verbatim:** *"The compliance retraction is propagated across the actual current
affected branch population, **or** any exceptions are explicitly **non-material** and
**authority-bounded**."*

**Two tests, and the exception must pass both.**

| Test | Result |
|---|---|
| Is the exception **authority-bounded**? | **YES, exactly.** The containment rule, master prompt §0 and master prompt §12 each independently forbid this session writing to another branch. The blocker is named to the clause |
| Is the exception **non-material**? | **NO.** The uncorrected claim sits on the **default branch of a public repository** and returns `HTTP 200` to an unauthenticated fetch. **A prohibited claim that is externally readable is the case Boss decisions `03` and `05` exist to prevent** |

> **The exception is authority-bounded and it is not non-material. The criterion requires both.
> `C4-04` is therefore NOT closed, and this matrix says so rather than reporting three-and-a-half
> conditions as four.**

### 3.1 What was closed inside `C4-04`, stated so the residue is not overstated either

| Sub-item | Status |
|---|---|
| The denominator — re-measured, not inherited | **CLOSED.** `185 / 2 / 183 / 0`, two shapes. CORR3's `183` and CORR4's `183` have different arithmetic |
| The claim-class population — is one file the population? | **CLOSED.** Four independently-shaped instruments; B fires and returns zero prohibited claims; C and D converge on the same one file |
| Is the correction itself sound? | **CLOSED.** Audited on all four required tests — no unqualified claim remains, nothing evidence-backed removed, no new contradictory variant, Thailand line carries both required qualifiers |
| Is the exposure understood? | **CLOSED, and it is worse than recorded.** `public` · `HTTP 200` — no prior round measured this |
| How many acts does propagation actually take? | **CLOSED. One** — mainline. The other 182 are historical branches unmerged by design |
| **Is the claim corrected where it is readable?** | **OPEN. This is the whole of the residue** |

### 3.2 Why this is not escalated to Boss as a decision

Master prompt §13: *"Boss must not be the first detector or resolver of a routine Phase SA defect,"*
and §7: *"do NOT escalate an `UNKNOWN`/`UNPROVEN`/`UNVERIFIED` condition to Boss as a design question."*

**This condition is none of those.** It is fully known, fully measured, and its remedy is a single
mechanical act. **And it is not a Boss decision**: Boss decisions `03` and `05` **already prohibit the
claim class**. Applying a prohibition Boss has already issued is **execution of a standing ruling**, not
the making of a new one — the reasoning `SA_CORR3_05` §3.3 established and which this round adopts
unchanged.

> **It is carried to the Boss Final Gate as a `PMO / repository-owner` action item with a named owner,
> a one-line remedy and a reproducible completion test — not as a question.**

---

## 4. The closure criteria, tested one by one

### `C4-01` — *"Privileged paths are enumerated sufficiently to support downstream security/conformance testing."*

**Met.** The test of sufficiency is whether a downstream test can be written, and it now can:

- `SA_CORR4_03`'s **8 deny conditions** and **25 test classes** are written against a **named path set**;
  before this enumeration `CF-I-03` `D4` had no domain to quantify over.
- `SA_CORR4_07` §5.2 orders the first five Pre-Test acts, and **two of them are attacks on named path
  classes** — `CF3-B-07` on the membership/execution boundary, and the four unscoped classes of `G1`.
- **`MTI-18`'s dependency is discharged.** CORR3: *"unprovable **in principle** today … because the set
  of privileged paths is not enumerated."* The set is enumerated.

**And the residual is stated in the same breath:** the population is **documentary**, so the
enumeration is *a floor on the path set, never a ceiling*. **`CF-I-03` §3.8 is written to fail closed on
exactly that residual** — an unknown privileged path is `D4`, never a pass. **Sufficiency for testing is
established; exhaustiveness is not claimed.**

### `C4-02` — *"Tenant + Company semantics are explicit in the cross-module emitting handoff contract and challenged across representative domains."*

**Met, and the challenge produced the finding — and then corrected it.** 13 elements stated; 9 rules
stated with their basis class published (`6 RULED` / `3 SPECIFIED` / **`0` newly determined**); 10
representative flows tested. **Independent challenge moved the flow result from `5/5` to `2/8`**
(`C4-02-F-09`) and over-extended citations were withdrawn (`C4-02-F-08`); **the condition still meets
its criterion, and the corrected result is worse and better-founded.**

> **The distribution is the result.** All nine rules were **already settled** — six by standing Boss
> rulings, three by published invariants, **none requiring a new determination.** What was missing was
> never the rules; **it was that nobody had assembled them into one contract**, so a party holding one
> half could not see the other. **Three independent findings — `C4-02-F-01`, `-F-02`, `-F-03` — are the
> same shape.**

**Explicitly not claimed:** element 10 does not move; `0 of 10` handoffs contract-compliant is
unchanged; element 15 is untouched.

### `C4-03` — *"`CF-I-03` is a concrete testable control specification and its `MTI-43` dependency is real, not a placeholder."*

**Met on both halves.**

- **Concrete and testable:** trigger, inputs, authoritative policy source, decision set, deny
  conditions, exception path, privileged handling, evidence, audit event, severity, preconditions and
  **25 test classes** including four instrument controls on the control itself.
- **The `MTI-43` dependency is real:** `HF-CTX-11` now references a specification that **exists, is
  owned, is testable and carries ruling lineage.** `MTI-43`'s **three negative forms are constructible**
  where CORR3 correctly recorded that the first *"cannot be constructed."*

**And the placeholder question is answered in the other direction too:** `CF-I-03` was **never** a
placeholder — it is a published `SPECIFIED` invariant that **CORR3's own register counted among its
58** while stating in another section that no published invariant states it.

### `C4-04` — see §3. **Not met.**

---

## 5. Was anything closed merely because a document exists?

**Tested against each condition, because §7 requires it.**

| Condition | Would it survive deleting this round's document and keeping only the evidence? |
|---|---|
| `C4-01` | **Yes.** The evidence is the `FDS` family on 185/185 branches, the `MTI-*`/`CF-I-*` families, and the seven 2026-09-09 Boss decisions. **The document organises evidence that exists; it does not constitute it** |
| `C4-02` | **Yes** for 12 of 13 elements and **9 of 9** rules — every one is sourced to a Boss ruling or a published invariant. **No** for element 10 of §3.1, the contract semantic version, which **is** new here and is flagged as the one `✎` |
| `C4-03` | **Partly.** The invariant `CF-I-03` exists independently. **The control specification is this document**, and it is the one place a reader should apply the §7 test hardest |
| `C4-04` | **Yes.** Every figure is a measurement over the repository |

> **`C4-05-F-01`. The condition most exposed to the "a document exists" objection is `C4-03`, and this
> matrix says so rather than letting the objection be raised elsewhere.** Its mitigation is that the
> specification is **elaboration of a published invariant with a stated lineage**, not invention — and
> that it has been handed to independent challenge at `SA_CORR4_08` with §3.4 named as its weakest
> point by its own author.

---

## 6. What no condition closed

**Stated together so that no reader infers closure by adjacency.**

| | |
|---|---|
| Invariants proven | **`0` of 58** |
| Scenarios verified | **`0` of 22** |
| Handoffs contract-compliant | **`0` of 10** |
| Isolation proofs · enforcement surfaces · negative access tests | **`0 of 8` · `0 of 13` · `0 of 52`** |
| Vetoes | **6 in force · `0` discharged** |
| Element 10 | **`specified, not built, not verified`** — `AAS-V-01` wording, no substitute |
| Element 15 | **Unchanged.** Not one of the four conditions, and it blocks all 22 scenarios |
| The COGS gap | **Unchanged** |
| `GAP-KC-01` | **Open, PMO-owned, not re-escalated** |

---

## 7. Checkpoint

> ## `CP-SA-C4-50 — FOUR CONDITIONS CLOSED OR EXACT HOLD RECORDED`
> **`C4-01` CLOSED · `C4-02` CLOSED · `C4-03` CLOSED · `C4-04` NOT CLOSED.**
> **`C4-04`'s exception is authority-bounded and is NOT non-material; its criterion requires both.**
> **Owner: PMO / repository owner. Remedy: one act. Not a Boss decision.**
> **`0` invariants proven · `0` vetoes discharged · element 10 does not move.**

**Next autonomous action:** `CP-SA-C4-80`, SMEs Core final re-challenge.

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
