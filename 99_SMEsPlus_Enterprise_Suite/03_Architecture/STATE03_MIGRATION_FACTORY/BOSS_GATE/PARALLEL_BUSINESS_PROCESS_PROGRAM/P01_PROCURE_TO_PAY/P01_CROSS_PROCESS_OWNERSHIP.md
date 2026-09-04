# P01 — CROSS-PROCESS OWNERSHIP REGISTER

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.**

Rule enforced: a consumer process may read, reference, derive from or report an event.
It may **not** recreate the same economic effect.

---

## 1. PARALLEL PROGRAM STATUS

**P01 is the first process session of the Parallel Business Process Accounting Deep Research
programme.** A branch enumeration of the repository at session start found no peer process
branch (`P02`…`P0n`) for any other process. Every cross-process row below therefore has a
peer status of **NOT YET EXECUTED**, not "awaiting publication".

Enumeration method: `git for-each-ref refs/remotes/origin` over the full remote branch list,
filtered for process identifiers. False-negative mode: a peer session executing in another
workspace without having pushed would not appear.

---

## 2. OWNERSHIP MATRIX

| Business fact | P01 role | Other process | Their role | Conflict risk |
|---|---|---|---|---|
| Inventory quantity increase on receipt | **Owner** | Inventory | Consumer / reporter | Low |
| Inventory **value** increase on receipt | **Owner**, but only for storable + continuous items | Inventory | Owner of subsequent value movements | **Boundary must be drawn at the receipt layer** |
| Unit cost established at receipt | **Owner** | Inventory / COGS | Consumer | The COGS track is on standing HOLD; P01 must not assume a cost method |
| Cost of goods sold | Not P01 | Inventory / COGS / P02 | Owner | P01 must not post any consumption effect |
| Landed cost absorption | Candidate shared | Inventory | Candidate owner | **UNRESOLVED** — assigned to an expert, see `P01_AAS03_EXPERT_CHALLENGE.md` |
| Vendor payable | **Owner** | Account (core ledger) | Consumer / reporter | Low |
| Payment and settlement | **Owner** for vendor-side | Account (core ledger) | Owner of the reconciliation engine and of FX difference | **P01 must not re-derive FX**; FX arises in the ledger at settlement (`EV-P01-21`) |
| FX rate selection and missing-rate policy | Consumer | Account Wave A | **Owner** — a standing Boss ruling exists on the Account track | P01 must inherit, not decide |
| Purchase tax (input tax) | Candidate owner | Account / Localization | Candidate owner | **UNRESOLVED** |
| Withholding tax | **UNRESOLVED — bill or payment** | Account / Localization | Candidate owner | **UNRESOLVED**, and the Account track holds this as a statutory question |
| Asset recognition | **Trigger**, at bill posting | Asset | **Owner** of the asset lifecycle | P01 owns the *trigger*, Asset owns the *asset*. The boundary is the bill line. |
| Depreciation | Not P01 | Asset | Owner | P01 must not post any depreciation effect |
| Period close | Consumer | Account (core ledger) | Owner | P01 must not define lock semantics |
| Cross-company document generation | **P01 is a trigger surface** (`EV-P01-27`) | SaaS / Platform Architecture | Owner of the tenant and company boundary | **Tolerance-zero. See §4.** |
| Subcontract purchase | Candidate consumer | Manufacturing | Candidate owner | **CLASS C — NOT YET SEARCHED** |
| Intercompany purchase | Trigger surface | Account / SaaS | Owner | See §4 |

---

## 3. INHERITED CONSTRAINTS FROM PEER TRACKS

P01 does not re-open any of these. It records them as binding inputs.

| Source track | Constraint on P01 |
|---|---|
| COGS Deep Research | Terminal **HOLD**. The reference system's continuous-valuation pattern was found unstable across versions. P01 must not assume any particular cost method survives. **This session independently reproduced that instability in a second area — the receipt-to-bill clearing bridge (`EV-P01-24`,`EV-P01-25`).** |
| Account Wave A | System-derived accounting date; silent single-rate FX fallback; no event identity. **P01 independently reproduced the system-derived accounting date in the receipt path (`EV-P01-06`).** |
| Account Wave A / GB-08 | Boss ruling on FX rate ownership and missing-rate policy. P01 inherits it. |
| Inventory MTI ruling set | Multi-tenant invariants. P01's cross-company trigger surface (§4) must be tested against them. |
| Negative Claim Standard | Applied throughout this package. |
| 8-Criteria Universal Exit Constitution | Governs this session's exit. See `P01_PMO_REVIEW.md`. |

---

## 4. TOLERANCE-ZERO: CROSS-COMPANY EFFECT TRIGGERED FROM P01

This is the most serious ownership finding in the session and it is stated in full.

Approving a purchase order, or posting a vendor bill, whose partner resolves to another
company in the same database, causes a document to be **created in that other company**,
executed as that company's designated user, with the company context switched.
`EV-P01-27`, `EV-P01-28`.

The mechanism has four properties, each verified:

1. The company is resolved by an **elevated-privilege search across every company in the
   database**, ignoring the acting user's allowed companies. `EV-P01-26`.
2. The match is an **ancestor match on the contact hierarchy**, so a *child contact* of another
   company's partner resolves to that company — not only the company's own partner record.
   `EV-P01-26`.
3. The search takes the **first match**; if two companies' partners are both ancestors of the
   contact, one is chosen silently. `EV-P01-26`.
4. The "create as" user **defaults to the superuser**, and a company setting can make the
   generated document **post automatically** rather than stay in draft. `EV-P01-29`,
   `EV-P01-30`.

No guard restricting the two companies to a common tenant, economic group, or the acting
user's allowed companies was found — **class B, scope: the three files cited only.** An
independent check was assigned to the Database Design expert.

### 4.1 Assessment under the corrected SCOPE-AWARE model

`SMEPLUS-26-09-04-ACC-REV2-CORR1` supersedes any blanket "Tenant and Company context are
mandatory for every operation" reading. The correct test is **scope-aware**, and this finding
is stated under that test, not under the superseded one.

**Scope classification of the mechanism:**

| Question | Answer |
|---|---|
| What scope OWNS the generated document? | **COMPANY** — it is a legal/accounting record of the target company |
| What scope EXECUTES the operation? | **COMPANY (source)** — the acting user is operating in the source company |
| What scope may MUTATE the target company's records? | **COMPANY (target)** |
| Does it create a financial effect? | **Yes**, where the target company's setting posts it automatically |
| Which company owns that financial effect? | **The target company** |

So the operation is COMPANY-scoped, and its execution context is a *different* company from
the one that owns the resulting financial effect. That is not automatically wrong — a genuine
intercompany transaction is exactly that. The defect is in **how the ownership is
established**:

- The corrected constitution states **`REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY`**.
- Here ownership of the target-company financial effect is not proven. It is **inferred from
  an ancestor match in the shared contacts hierarchy**, resolved with elevated privilege that
  ignores the acting user's allowed companies, taking the first match when several exist.
  `EV-P01-26`.
- `OWNERSHIP ≠ AVAILABILITY` and `MULTI-TENANT MEMBERSHIP ≠ MULTI-TENANT EXECUTION CONTEXT`:
  this mechanism derives an **execution context** in the target company from a **reference-data
  relationship** (a contact's parent), which is precisely the substitution those two rules
  forbid.

**Restated finding:** the mechanism is not condemned for being cross-company. It is condemned
because a COMPANY-scoped financial effect is raised in a company whose ownership of that
effect was never proven — only inferred from reference data that a different scope controls.
Under the corrected rule the correct behaviour where ownership cannot be proven is **DENY**;
the observed behaviour is **proceed, as superuser, and optionally post**.

**Tenant question, stated separately and honestly:** whether the two companies belong to the
same tenant is **not tested anywhere in the code read**. That is a class **B** negative
(scope: the three cited files). Under the corrected model, unrelated independent companies are
separate tenants by default, so an untested company pair is also an untested *tenant* pair —
which makes this a candidate **TENANT-boundary** crossing, not merely a company one. This is
the item that carries the tolerance-zero weight, and it remains **UNRESOLVED — SCOPE EVIDENCE
REQUIRED** pending the Database Design expert's independent check.

**Relationship to prior evidence:** the Account Wave A track recorded a hard company lock
being defeated through a contacts-role partner merge. This is the **same primitive**
(partner-hierarchy resolution granting cross-company reach) appearing independently in a
second process. Two independent instances make this a systemic architectural property of the
reference model, not a local defect.

**Disposition:** `TOLERANCE-ZERO — HOLD.` Under exit criterion EC-04 a conditional outcome may
not bypass a tolerance-zero risk. This item alone prevents P01 from being presented as
unconditionally ready.

---

## 5. HANDOFF OBLIGATIONS TO PEER PROCESSES

When each peer process session runs, it must accept or contest these P01 positions:

| ID | Position P01 asserts | Peer that must respond |
|---|---|---|
| `HO-01` | The vendor bill is the sole owner of the payable event | P02 (Order-to-Cash) — must not create a vendor payable |
| `HO-02` | Receipt owns the *first* valuation layer; Inventory owns everything after | Inventory |
| `HO-03` | P01 owns only the asset *trigger*; the asset lifecycle is Asset's | Asset |
| `HO-04` | P01 does not decide FX rate policy | Account |
| `HO-05` | The received-not-billed obligation has two competing representations and needs one owner | Account + Inventory |
| `HO-06` | The cross-company trigger surface is a platform decision, not a process decision | SaaS / Platform Architecture |
