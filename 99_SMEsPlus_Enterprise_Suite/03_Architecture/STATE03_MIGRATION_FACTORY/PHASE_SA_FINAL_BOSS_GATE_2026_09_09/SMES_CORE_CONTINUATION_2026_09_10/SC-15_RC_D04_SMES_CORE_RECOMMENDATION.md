# SC-15 — `RC-D-04` SMEs CORE RECOMMENDATION
## Mapping-layer ownership

Session `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · Head consumed `ce987553`
**This is a SMEs Core recommendation, NOT a Boss ruling. `RC-D-04` remains an open Boss decision.**

---

## 1. Which mapping layer is in scope — answered first, because it is contested

The prompt §4 requires this before anything else. **The corpus names exactly one:**

`SA_FINAL_03` line 170, verbatim:

> *"**`CF-XCR-GAP-01`** — **a required mapping/provenance relationship class** — **is deliberately
> un-numbered because giving it an entry would place an unspecified object in a register whose
> completeness is the isolation claim.**"*

and line 170 also: *"`XCR-02` (the cross-context report grant) is **`SPECIFIED — CONDITIONAL
(MTI-D-04)`**."*

> ### The layer in scope is the **cross-company read mapping/provenance layer** that `XCR-02` would require. It is **`CF-XCR-GAP-01`**, and it is deliberately un-numbered.

**It is NOT** the 12-boundary handoff element contract (`XMC-D-02`, ruled at `SC-BD-02` — that has an owner
and an authority rule already), and it is **not** a migration mapping. Widening `RC-D-04` to those would be
scope creep into decisions already ruled.

## 2. What the `MTI-D-04` ruling did to it

`SA_FINAL_02` line 75, verbatim: *"**`RC-D-04` is gated on `MTI-D-04`** and is a **commissioning-plus-policy
act**."*

**Boss ruled `MTI-D-04` = no cross-company grant in v1** (`SC-BD-03`). Its gate therefore resolved
**negative**: with no grant, `XCR-02` is settled and **the layer `CF-XCR-GAP-01` describes has no v1
subject to map.**

### 2.1 Why that does NOT dissolve the decision

**The tempting move is to say `RC-D-04` dissolves the way `F3` did. It does not, and the veto register is
the reason.**

`SA_CORR5_09` line 37, `CF-V-02`'s release path, verbatim:

> *"**`MTI-D-04` + `RC-D-04` ruled and the mapping layer specified** (lifts the first limb)"*

**Three conditions. `MTI-D-04` is one of them.** A dissolved `RC-D-04` leaves limb 1 permanently unliftable
and leaves an active AAS+ veto with no closure path — which is why `SC-GAP-F-01` records that
`SC-BD-03`'s *"first limb closed"* was overstated.

> **`RC-D-04` must be RULED, and the mapping layer must be SPECIFIED, even though the grant is declined.**
> The specification is what makes the un-numbered class safe to leave un-numbered.

## 3. Semantic ownership vs technical implementation ownership

| Layer of ownership | Question it answers |
|---|---|
| **Semantic** | what a mapped identity *means*, and which side is canonical when two contexts disagree |
| **Technical / mechanical** | who builds, stores, versions, publishes, activates, retires and audits the mapping |
| **Consumption** | who may read a mapping, and for what |

**Conflating them is the failure mode**: a team that builds the store drifts into deciding what the
identities mean, and the mapping becomes an authority nobody granted it.

## 4. The controlling principle to preserve

**Approval Engine approves only · Source Module executes · Posting Engine posts.**

Applied here: **a mapping layer resolves identity; it must never originate, alter or authorise a fact.**

> **The prohibition to rule, in one line: a mapping layer may never become a source of truth.**
> If a mapping can change what a figure *is* — rather than only which record it *corresponds to* — it has
> become a shadow ledger, and `BD-ACC-01`'s canonical Accounting Event Identity is no longer canonical.

`MTA-11` reinforces the risk class: *"every grant mechanism degrades toward permanence"*, with **no review
cadence designed anywhere** (`SC-SMT-05`).

## 5. Three ownership models evaluated

| | Model | Verdict |
|---|---|---|
| **(a)** | **Split** — **semantic** ownership to **Accounting Core** (it owns canonical event identity under `BD-ACC-01`); **mechanics** (store, versioning, publication, activation, retirement, audit) to **SaaS Foundation**; **consumption** by Posting and reporting, read-only | **RECOMMENDED** |
| **(b)** | **Single owner** — SaaS Foundation owns semantics and mechanics end-to-end | **Rejected.** Puts accounting meaning under a platform team and creates exactly the shadow-source-of-truth this decision exists to prevent |
| **(c)** | **Per-boundary owner** — each boundary owns its own mapping | **Rejected on a ruling Boss has already made.** `SC-BD-02` closed `SC-SMT-08` with *"a boundary may propose; it may not declare."* (c) is that defect shape |

**(c)'s rejection is not a preference — it is consistency with `SC-BD-02`.**

## 6. SMEs Core recommendation

> ### `RC-D-04` → **MODEL (a) SPLIT OWNERSHIP, PRE-ASSIGNED NOW, WITH THE LAYER DORMANT IN v1.**

**Rule the ownership now even though the grant is declined**, so that a future grant cannot create an
unowned layer. Concretely:

| Lifecycle act | Who |
|---|---|
| **propose** a mapping | the requesting boundary or module — **propose only** |
| **approve** semantics | **Accounting Core** |
| **publish / version / activate / retire** | **SaaS Foundation** |
| **audit** | Internal Control, over the SaaS Foundation store |
| **consume** | Posting and reporting, **read-only** |

**Scope:** every mapping is **Tenant-scoped and Company-qualified**; no mapping may span companies for a
statutory purpose (`BD-ACC-02`), and none may span tenants at all.

**Immutability / versioning / audit:** mappings are **append-only and versioned**; activation and
retirement are **events, not edits**; every version carries who, when and basis; **retirement never
rewrites history**. This mirrors `M-1`/`M-6` from `SC-BD-07` — *the record's emission is not configurable* —
so a mapping change can never be silent.

**v1 status:** **`SPECIFIED — DORMANT — NO SUBJECT`.** The layer is specified and owned; **it instantiates
nothing in v1** because `MTI-D-04` declined the grant. **This is what satisfies `CF-V-02` limb 1's
*"and the mapping layer specified"* without authoring a grant Boss refused.**

## 7. Best alternative

**Defer ownership entirely with the grant** — rule `RC-D-04` as *"not applicable in v1"*.
**Consequence:** `CF-V-02` limb 1 has **no closure path**, since its release requires the layer
*specified*; the veto stays active indefinitely on a condition nobody is tasked to meet; and a future grant
arrives with an unowned mapping layer, which is the `MTA-11` degradation pattern.

## 8. Downstream effects

**Cross-module contracts** — consistent with `SC-BD-02`: propose/declare separation is now the same rule in
two places. **Migration** — a dormant, versioned, append-only layer is safe to carry; an unowned one is
not. **Reconciliation** — semantic ownership sitting with Accounting Core keeps canonical identity in one
place, so reconciliation has a single authority to appeal to. **Auditability** — append-only plus
activation-as-event makes the mapping's history reconstructible, which an edit-in-place store never is.
**Isolation claim** — `CF-XCR-GAP-01` can remain **un-numbered** because it is now **specified and dormant**
rather than **unspecified and absent**; the register's completeness claim is preserved either way.

## 9. Clean Room rationale

**What we learned:** that identity-mapping layers accrete authority unless ownership is split before they
exist. **What we deliberately did NOT inherit:** no reference ERP mapping table, cross-company matching
routine, ORM relation or integration-mapping module was read or used; the model is derived from SMEsPlus's
own `BD-ACC-01` canonical-identity ruling and its own Approval/Execute/Post separation.
**Alternatives considered:** §5. **Why this is SMEsPlus's own design:** most systems create the mapping
first and assign ownership afterwards, which is how a mapping becomes a shadow source of truth.
**What SMEsPlus does differently:** ownership and the never-a-source-of-truth prohibition are ruled
**before** the layer has a subject, and the layer ships **dormant**.

## 10. Disposition sought

**`PASS TO BOSS DECISION`** on model (a), the lifecycle authority split, the Tenant/Company scope, the
immutability rules and the `SPECIFIED — DORMANT — NO SUBJECT` v1 status.
**`RC-D-04` remains an open Boss decision.**
