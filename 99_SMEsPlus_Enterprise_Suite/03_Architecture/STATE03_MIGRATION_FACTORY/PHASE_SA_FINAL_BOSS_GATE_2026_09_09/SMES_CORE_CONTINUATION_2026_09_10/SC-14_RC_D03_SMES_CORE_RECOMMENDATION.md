# SC-14 — `RC-D-03` SMEs CORE RECOMMENDATION
## Private Company escalation criteria

Session `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · Head consumed `ce987553`
**This is a SMEs Core recommendation, NOT a Boss ruling. `RC-D-03` remains an open Boss decision.**

**Why it did not exist before:** `SA_FINAL_03` line 172 records recommendations for `MTI-D-04` and
`TV6-BOSS-02` only; `SA_FINAL_02` line 75 lists `RC-D-03`/`RC-D-04` as *"`F` KEEP"* with no recommendation.
It is a real gap, not a transcription loss (`SC-BD-F-01`).

---

## 1. The exact business problem this decision controls

SMEsPlus ships one operating topology: **`SHARED SaaS POOL`**. Some tenants will present needs the pool
cannot lawfully or safely serve. `RC-D-03` fixes **what objectively qualifies a tenant to leave the shared
pool for a dedicated (Private Company) operating model** — and, by omission, what does not.

**Without it:** escalation happens case-by-case under commercial pressure, and the isolation boundary that
`MTI-D-01`/`-02`/`-03` and `BD-ACC-02` establish becomes negotiable per customer.

## 2. The deployment boundaries, distinguished

| Boundary | What it is | Who owns it |
|---|---|---|
| **Tenant** | the isolation root; one customer organisation's data universe | Platform |
| **Company** | the statutory accounting entity inside a tenant. **`BD-ACC-02`: no cross-company statutory posting, offsetting, settlement, aggregation or filing.** Management views permitted | Platform core + tenant config overlay (`MTI-D-03`) |
| **Private Company (topology)** | a **dedicated operating model** outside the shared pool | **Undefined in the Phase SA corpus — see §3** |

**`Private Company` is a *topology*, not a company record.** Conflating it with the `Company` boundary
would be a category error; the two words share a token and nothing else.

## 3. ⚠ The constraint that shapes everything — `CF-I-08`

**Enumerated population:** *"Private Company"* occurs **19 times repo-wide** at `HEAD`
(`git grep -in "private.company"`), against a **222-file** control for *"tenant"* in the same tree — so the
sweep fires and the scarcity is real. **Every substantive occurrence is a prohibition:**

| Source | Verbatim |
|---|---|
| `SA_CORR4_03` L147 | *"Topology scope: **`SHARED SaaS POOL` only.** `CF-I-08` binds: **nothing here may be asserted to hold, transfer or fail inside a Private Company operating model**"* |
| `SA_CORR4_03` L400 | *"Author anything for the **Private Company** topology — **No.** `CF-I-08`"* |
| `SA_CORR4_10` L197 | *"**Anything about the Private Company topology** — `CF-I-08`. **Nothing here transfers**"* |
| `SA_CORR3_07` L381 | *"evidence about a Private Company topology **would find nothing on the artefact to stop it**"* |

**And `CF-I-08` is itself contradicted over the corpus it governs** — `SA_CORR3_07` L372:
*"**8 of 35 files** state a topology; **0 of 58 invariants** state one individually."*

### 3.1 The distinction that makes `RC-D-03` authorable at all

`CF-I-08` prohibits authoring **behaviour inside** the Private Company topology. It does **not** prohibit
authoring an **exit condition from the shared pool**.

> **`RC-D-03` must be written as a boundary condition on the `SHARED SaaS POOL`, not as a specification of
> the Private Company model.** *"When does a tenant cease to be servable by the pool"* is a pool fact.
> *"How the dedicated model behaves"* is `CF-I-08` territory and is **not** authored here.

**This is the single most important control in this recommendation, and it is the reason the decision was
authorable after three rounds treated it as untouched.**

## 4. What `RC-D-03` now carries that it did not before

**`MTI-D-04` was ruled *no cross-company grant in v1*** (`SC-BD-03`), with the group-view need met by
per-company export.

> **The pressure that a cross-company grant would have released now has nowhere else to go.**
> Private Company escalation becomes **the only designed route** for a tenant whose needs exceed the shared
> model. **`RC-D-03` is more load-bearing after that ruling, not less** — a consequence of `SC-BD-03` that
> no record states.

**And `CF-V-02`'s second limb depends on it.** `SA_CORR5_09` L37: *"**`RC-D-03` ruled and Private Company
escalation criteria stated** (second limb)."* **Both halves are required** — a ruling alone will not lift it
(`SC-GAP-F-01`).

## 5. What must NEVER be an escalation trigger

**This list is the control. It is recommended for ruling with the same force as the model itself.**

| # | Never a trigger | Why |
|---:|---|---|
| 1 | **A wish for cross-company statutory posting, offsetting, settlement, aggregation or filing** | **`BD-ACC-02` forbids it in *every* topology.** Escalation must not become a way to purchase a ruling Boss has closed |
| 2 | **A wish for cross-company visibility** | `MTI-D-04` ruled the answer: **per-company export**. Escalation must not be the workaround for a ruled election |
| 3 | **Commercial willingness to pay, alone** | makes the isolation boundary a price list |
| 4 | **Customer-specific customisation of platform-owned core** | `MTI-D-03`: *"No customer-specific change may force a platform-owned core change."* Escalation must not be a customisation channel |
| 5 | **Tenant size, revenue or headcount, alone** | a scale proxy is not an isolation requirement |

## 6. Three alternative policy models evaluated

| | Model | Trigger basis | Verdict |
|---|---|---|---|
| **(a)** | **Objective-threshold** — escalation only on a named, measurable, externally-attributable requirement, with a fixed decision authority and the §5 `NEVER` list binding | regulatory mandate for physical isolation · data-residency obligation · a security/attestation obligation the pool cannot meet · a quantified performance/SLA class the pool cannot meet | **RECOMMENDED** |
| **(b)** | **Commercial-tier** — escalation is a purchasable tier | price | **Rejected.** Collides with §5.3 and makes isolation a commercial artefact |
| **(c)** | **Case-by-case discretion** — reviewed per request on merits | judgement | **Rejected as the primary model.** It is what happens by default when no criteria exist, and it is unauditable. **Retained only as an exception path *under* (a)**, requiring the same authority and a recorded basis |

## 7. SMEs Core recommendation

> ### `RC-D-03` → **MODEL (a) — OBJECTIVE-THRESHOLD, WITH THE §5 `NEVER` LIST BINDING, AUTHORED AS A POOL-EXIT CONDITION ONLY.**

**The four trigger classes** are recommended as the **closed** set for v1: regulatory mandate for physical
isolation · data-residency obligation · unmeetable security/attestation obligation · unmeetable quantified
performance/SLA class. **Each must be externally attributable** — to a regulator, a contract or a measured
pool limit — **never to a preference.**

**Decision authority:** escalation is a **platform** decision, not a tenant or account-management one, and
each escalation records the trigger class, the external attribution and the deciding authority.

**Explicitly out of scope of this recommendation, by `CF-I-08`:** how the Private Company topology behaves;
whether any Phase SA invariant, contract or control holds inside it; any migration mechanics into it.
**None of that is authored here and none of it transfers.**

## 8. Best alternative

**(c) as the primary model**, i.e. Boss declines a closed trigger set and keeps escalation discretionary.
**Consequence:** every escalation is defensible individually and the boundary is indefensible in aggregate;
`CF-V-02`'s second limb — *"escalation criteria **stated**"* — **would not be satisfied**, so the veto stays
active on that limb.

## 9. ⚠ What SMEs Core cannot supply, declared rather than invented

**The four trigger *classes* are architecture policy and are recommended.** The **specific threshold
values inside them are not producible by SMEs Core**:

| Needed | Owner | Status |
|---|---|---|
| Which regulations mandate physical isolation for a Thai SME group | **Thai statutory / legal** | `HOLD / EVIDENCE REQUIRED` — the standing Thai statutory HOLD applies |
| Which data-residency obligations bind | **Legal / commercial** | not researched; not researchable from source |
| The pool's measured performance/SLA ceiling | **Operations** | requires a built pool; **`RC-V-01` bars implementation start** |
| Which attestations the pool can and cannot meet | **Security / Compliance** | no certification is held — mainline records all five standards `NOT ASSESSED` |

> **No statutory, residency, SLA or attestation claim is made anywhere in this file.** The recommendation
> is the **model, the authority and the `NEVER` list** — all architecture policy, all within SMEs Core
> authority. **The threshold values are a business input, not a research gap**, so this does **not** trigger
> targeted Very Deep Research.

## 10. Downstream effects

**SaaS architecture** — the pool keeps one topology; escalation is an exit, not a variant, so no
dual-topology branching enters the core. **Data isolation** — the boundary stops being negotiable per
customer. **Operations / support** — each escalation carries a recorded trigger class and authority, so the
population is auditable. **Migration** — deliberately **not** designed here (`CF-I-08`). **Commercial
packaging** — escalation is **not** a sellable tier (§5.3), which is a commercial constraint Boss should
see plainly.

## 11. Clean Room rationale

**What we learned:** that a shared-pool product needs a defined exit, and that the exit is where isolation
guarantees are won or lost. **What we deliberately did NOT inherit:** no reference ERP's multi-company or
hosting topology, schema, deployment model or tiering was read, cited or used — the four trigger classes are
derived from **SMEsPlus's own** ruled constraints (`BD-ACC-02`, `MTI-D-03`, `MTI-D-04`, `CF-I-08`), not from
any vendor's packaging. **Alternatives considered:** §6. **Why this is SMEsPlus's own design:** it inverts
the usual vendor pattern — escalation is a **constraint-driven exit governed by a prohibition list**, not an
**upsell**. **What SMEsPlus does differently:** the `NEVER` list is ruled with the same authority as the
triggers, so the boundary cannot be eroded one deal at a time.

## 12. Disposition sought

**`PASS TO BOSS DECISION`** on the model, the authority and the `NEVER` list.
**Threshold values remain a declared business input.** `RC-D-03` stays an **open Boss decision**.
