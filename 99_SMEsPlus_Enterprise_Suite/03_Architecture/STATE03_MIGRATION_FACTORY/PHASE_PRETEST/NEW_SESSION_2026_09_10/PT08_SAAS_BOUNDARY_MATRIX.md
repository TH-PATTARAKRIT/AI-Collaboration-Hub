# PT-08 — SaaS / TENANT / COMPANY / SECURITY BOUNDARY MATRIX

## `CP-PT-08 — SAAS BOUNDARIES TESTABLE`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]`
Branch: `architecture/account-phase-pretest-new-session-2026-09-10-001` · head consumed `80cfe6e2`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **NO EXECUTED CROSS-TENANT RUNTIME PROOF IS CLAIMED ANYWHERE IN THIS FILE.**
> **`EC-04` `0/3` · `0 of 58` invariants proven · `0 of 8` isolation proofs · `0 of 60` negative cases.**

---

## 1. Result

| | |
|---|---|
| Governing register | `SA10_TENANT_COMPANY_BOUNDARY_MATRIX.md` — status **`HOLD`** |
| Its own headline | ***"the strongest specification in the SMEsPlus baseline, and none of it is proven"*** |
| Invariants | **`58` specified** (`50` carried + `8` added) · **`0` proven** · `14` re-specified |
| Isolation proofs executed | **`0 of 8`** |
| Negative access cases executable | **`0 of 60`** (`52` rejection cells + `S-01`…`S-08`) |
| Enforcement surfaces verified | **`0 of 13`** |
| Cross-context register entries proven | **`0 of 3`** — the register is **empty** |
| SaaS closure gates mandated / existing | **`8` mandated · `3` exist · `5` do not** |
| Lock-defeat paths | **`2`** — and the second leaves **no record of any kind** |
| **Material findings** | **`2`** — `PT08-F-01`, `PT08-F-02` |
| **Executed runtime isolation proof claimed here** | **`0` — and `EC-04` is NOT advanced by this checkpoint** |

---

## 2. The prohibition this checkpoint operates under

**Master prompt `PT-08`, verbatim:** *"Do not claim executed cross-tenant runtime proof without lawful
runtime evidence."*

**`SA17` §2b prohibition 1, verbatim:** *"**Nothing may be read as testing tenant isolation until an
implementation exists.**"*

**`8C-CLARIFICATION-01` clause 3:** **specification evidence NEVER satisfies `EC-04`.**

> **Everything below is test *design*. `0` of it is proof.** The distinction is the entire content of this
> checkpoint, and it is why `EC-04` leaves it at `0/3`, exactly as it entered.

---

## 3. The measured state — every figure a zero, and each with a named denominator

| Obligation | Executed / Total |
|---|---|
| `L9` isolation proofs | **`0 of 8`** |
| Cross-proof scenarios | **`0 of 22`** |
| Material handoffs contract-compliant | **`0 of 10`** |
| Joint decisions ready | **`0 of 12`** |
| Thai validations | **`0 of 78`** |
| Enforcement surfaces verified | **`0 of 13`** |
| Functions verified against any axis | **`0 of 41`** |
| Proof requirements executable | **`0 of 60`** |
| Negative access tests executable | **`0 of 52`** — *"because no implementation exists"* |
| Cross-context register entries proven | **`0 of 3`** — *"the only door, and it is currently empty"* |
| Invariants proven | **`0 of 58`** |
| **Findings closed · capabilities built · vetoes discharged** | **`0` · `0` · `0`** |

> **Eleven denominators, eleven zeros.** This is not a package with weak evidence; it is a package with a
> **complete specification and no execution**. `SA10-F-01` states the consequence in its own words:
> **"a specification is not a control. The isolation guarantees may be cited as *design intent* and may
> NOT be cited as *assurance*."**

---

## 4. `PT08-F-01` — the tolerance-zero boundary, and why measured reachability does not reduce it

### The defect

**`SA10-F-03`:** a **Critical** tenant-isolation defect exists — **company-dependent accounts are resolved
in the *user's* company, not the *transaction's*.**

### The measurement that looks like mitigation

> *"measured reachability is **nil**: both manufacturing databases are **single-company**"*

### Why that does not reduce the severity — the register's own rule

> **"Severity ranking must use the target architecture, not the reference deployment's accident."**

> **A defect that cannot fire in the reference estate because the estate happens to be single-company is
> not a defect that cannot fire in a multi-company SaaS product.** The reachability measurement is
> evidence about **the estate**, not about **SMEsPlus**. **Recording `nil` reachability as mitigation would
> be inheriting a vendor deployment accident as a SMEsPlus safety property.**

**Carried:** `EC-04` boundary `1` (`CF-I-03` `D3` cross-tenant) and boundary `3` (`SA10` tenant/company
matrix, self-declared **`TOLERANCE-ZERO — HOLD`**) remain **open at `0 of 3`**, closable only by
**executed runtime proof + independent reproduction, no later than the State gate.**

---

## 5. `PT08-F-02` — two lock-defeat paths, and only one is visible to a remediation

| Path | Mechanism | **Record left** |
|---|---|---|
| **1** Contacts-role counterparty merge | *"an explicit bypass token; no company clause, elevated privilege, every company in the database"* | *"a message on the **counterparty record**, **not** on the affected entries; unhashed entries absorb the change **silently**"* |
| **2** Account merge | ***"no bypass token — the lock control is simply NOT ON THIS PATH"*** | ***"no record of any kind"*** |

**Reachability:** *"reachable through ordinary UI **with no accounting rights**"*; escalated as *"a
**systemic property of the reference model**, not a local defect"*.

**`SA10-F-05`, verbatim:** *"Earlier SMEsPlus records describe this as **one** defeat path. There are
**two** … A remediation aimed at the bypass token would close one path and **not the other**."*

**The SMEsPlus determination that answers both:** **`ND-07` — *a period lock is a property of the entry,
not of the path that reaches it.*** A control bound to the entry cannot be defeated by arriving via an
uncovered path.

### The caveat that must travel with all of it

> **"No lock has ever been exercised anywhere in this estate. … So the entire matrix above is **source
> capability**, observed nowhere. `HOLD`."**

> **The two defeat paths are read from source, not observed in operation.** Publishing them without this
> caveat would convert a source reading into a behavioural claim. **`PT-12` carries the caveat on the row,
> not in a footnote.**

---

## 6. Boundary status — what is specified vs what is verified

| Boundary | Specified? | **Verified?** |
|---|---|---|
| Tenant isolation | **Yes — `58` invariants** | **No — `0` proofs** |
| Warehouse-operation-type | — | **No — `0 of 13` enforcement surfaces** |
| Context carriage on handoffs | — | **No — `0 of 10` handoffs compliant** |
| Cross-company register | — | **No — register empty** |
| Company boundary | — | **No** |
| Platform-vs-tenant configuration | — | **No** |

**Governing scope rule, and it is a correction that must not be reverted:**

> **`SCOPE-AWARE EVERYWHERE` (`PLATFORM` / `TENANT` / `COMPANY`)** — §8.2 **withdraws** any blanket reading
> that tenant + company are mandatory on **every** operation. `SA10` §1's *"context spine — never
> optional"* **is the `COMPANY`-scope case and must not be generalised.**

> **`SA10` §1 and §8.2 read as a contradiction and are not one:** §1 states the `COMPANY` case, §8.2 states
> the general rule. **A Pre-Test row asserting "tenant + company mandatory" would be over-constraining —
> and the recorded lesson is that a blanket rule hides over-constraint in *both* directions.**

---

## 7. SaaS closure gates and platform invariants

| | |
|---|---|
| Closure gates mandated | **`8`** |
| Gates that exist | **`3`** — `G01`, `G02`, `G03` |
| **Gates that do not** | **`5`** |
| `G01` | **`HOLD / EVIDENCE REQUIRED`** |
| `G03` | four rows at **`N/A — JUSTIFICATION REQUIRED`** |
| **`G02`** | **ten rows read verified, while its own closing block reads `HOLD / CORRECTION REQUIRED — PENDING FRESH TARGETED INDEPENDENT RE-AUDIT` and `READY FOR PMO VERIFICATION = NO`** |

> **`G02` is recorded by `SA10-F-04` as *"a status-fidelity hazard for any consumer"* — a gate whose row
> detail and whose own closing status disagree.** **A consumer reading only the rows would take it as
> verified.** This is the same shape as `PT03-F-01` and `PT06-F-01`: **the detail is right and the summary
> is what travels.** **`PT-15` must check `G02` by its closing block, not its rows.**

**Platform invariants carried:** `SI-01`…`SI-10` · `MTI-29` (a background financial process runs one tenant
at a time; platform totals equal the sum of per-tenant results) · `TRG-02` · `ND-13` (a platform
principal's acts name the target tenant as **object** and **never read tenant business data**) ·
`ND-14` (a reason classification binds to a **platform-owned** class, never a tenant label).

---

## 8. Test design carried to `PT-12` — all `PTE-3`, with their order constraint

**`SA17` §2a dependency order, verbatim and unmodified:**

1. **`MTI-50` retention** — *"`CF-I-03` is unbuildable without a historised grant store; **not partially: at all**."*
2. **`CF3-C-01`…`C-04` instrument controls** — synthetic injection, discriminating population, coverage
   assertion, negative control — **before any positive test**.
3. **`CF3-B-02`** — a grant issued *after* the act must **deny**.
4. **`CF3-B-07`** — an actor holding grants in **two tenants**.
5. The **five formerly-unscoped path classes** (`G1`).
6. **`RT-E15-08`/`-06`** — element-15 and attempt-identity synthetic injection, **before any scenario's
   retry dimension is scheduled**.

> **Step 2 is the one that makes the rest meaningful.** A negative-access suite without a
> **synthetic-injection control** and a **discriminating population** returns clean on a broken extractor —
> the failure mode `SA17` §2b prohibition 2 names explicitly. **`0` positive tests may be scheduled before
> the instrument controls fire.**

| Test family | Class | Blocked on |
|---|---|---|
| `0 of 8` isolation proofs | **`PTE-3`** | element 10 built |
| `52` rejection cells + `S-01`…`S-08` | **`PTE-3`** | implementation |
| `CF-I-03` / `CF-I-03R` | **`PTE-3`** | **`MTI-50` first** |
| `13` enforcement surfaces | **`PTE-3`** | implementation |
| `MTI-29` / `TRG-02` platform-total equality | **`PTE-3`** | implementation |
| Cross-context register (`0 of 3`) | **`PTE-3`** | the register is empty |

---

## 9. Checkpoint

> ## `CP-PT-08 — SAAS BOUNDARIES TESTABLE, NOT TESTED`
>
> **`11` denominators, `11` zeros — `0 of 58` invariants, `0 of 8` isolation proofs, `0 of 60` negative
> cases, `0 of 13` enforcement surfaces, `0 of 3` register entries, `0 of 10` compliant handoffs ·
> **`0` executed cross-tenant runtime proof is claimed, and `EC-04` leaves this checkpoint at `0/3`
> exactly as it entered** ·
> **`PT08-F-01` — a Critical isolation defect whose *"nil measured reachability"* comes from the reference
> estate being single-company; severity is ranked on the target architecture, not on a deployment
> accident** ·
> **`PT08-F-02` — `2` lock-defeat paths, not `1`; the second is not covered by the control at all and
> leaves **no record of any kind**; a remediation aimed at the bypass token would close one and not the
> other — carried with the caveat that **no lock has ever been exercised anywhere in this estate**, so the
> whole matrix is source capability observed nowhere** ·
> `8` SaaS gates mandated, `3` exist, `5` do not; **`G02` is a status-fidelity hazard — rows read verified,
> its own closing block reads `HOLD / CORRECTION REQUIRED`** ·
> `SCOPE-AWARE EVERYWHERE` honoured: **`0` blanket tenant+company assertions made.**
>
> **`0` vetoes discharged · `0` tolerance-zero boundaries reclassified · `0` runtime proof fabricated.**

Next checkpoint: `PT-09 — Exception / Reversal / Recovery / Idempotency Matrix`.

No Evidence = No Progress. Never Skip Gate. A specification is not a control. Truth over Pass.
Boss remains the sole Final Approver.
