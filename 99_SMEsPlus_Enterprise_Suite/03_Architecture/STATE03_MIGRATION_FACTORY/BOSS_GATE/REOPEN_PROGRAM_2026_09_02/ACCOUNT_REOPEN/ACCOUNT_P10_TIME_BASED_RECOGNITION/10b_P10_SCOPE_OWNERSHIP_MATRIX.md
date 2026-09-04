# P10 — SCOPE OWNERSHIP MATRIX

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1
Issued under `SMEPLUS-26-09-04-ACC-REV2-CORR1` (Scope-Aware Constitution Correction).

Canonical model applied: **PLATFORM** (no tenant, no company context) · **TENANT** (security/customer boundary) · **COMPANY** (legal/accounting boundary). `MISSING REQUIRED SCOPE = DENY`. `OWNERSHIP != AVAILABILITY`. `EXECUTES != OWNS`.

This matrix deliberately does **not** assume tenant-and-company for every object. Three objects below are PLATFORM candidates and one is TENANT-owned; assigning them COMPANY scope would be over-constrained and wrong.

---

## 1. Object-by-Object Determination

| Object | OWNS | EXECUTES | ACCESS | MUTATE | REFERENCE | Financial effect? | Company owning that effect |
|--------|------|----------|--------|--------|-----------|-------------------|-----------------------------|
| Day-count convention **definition** (30/360, actual, full-month) | **PLATFORM** | PLATFORM | any | PLATFORM only | any | no | n/a |
| Period-grid **algorithm** (how a window is cut) | **PLATFORM** | PLATFORM | any | PLATFORM only | any | no | n/a |
| Recognition **event schema** (what an event is) | **PLATFORM** | PLATFORM | any | PLATFORM only | any | no | n/a |
| Allocation-convention **standard for the tenant** | **TENANT** | TENANT | tenant | tenant admin | tenant | no, directly | n/a |
| Service/benefit **window** (contract fact) | **TENANT** | TENANT | tenant | the owning document's process | company | no, directly | n/a |
| Fiscal calendar / period grid **instance** | **COMPANY** | COMPANY | company | company | company | no, directly | the company |
| Allocation convention **binding value** | **COMPANY** | COMPANY | company | company | company | yes, indirectly | the company |
| Deferral / accrual **control accounts and journals** | **COMPANY** | COMPANY | company | company | company | yes | the company |
| **Recognition base** (amount + currency + measurement date/rate) | **COMPANY** | COMPANY | company | the source document's process | company | yes | the company |
| **Recognition event** | **COMPANY** | COMPANY | company | P10 kernel only | company | yes | the company |
| **Posting act** | **COMPANY** | COMPANY | company | ledger only | company | yes | the company |
| Recognition **report** | **COMPANY** data, viewed at TENANT | must be COMPANY when it generates | company | n/a | company | yes, when it generates | must be asserted, not derived |

## 2. The Two Scope Defects

### `P10-S-01` — allocation policy resolved at the executing scope

The allocation convention is a **COMPANY-scope binding value**. The reference behaviour reads it from the **active** company while reading the accounts and journal from the **document's** company (`E-P10-004`, `E-P10-003`).

Reachable in three ways, one of which does not even require a multi-company user session: the automatic posting routine runs under the scheduler's own company and posts documents belonging to any company (`E-P10-038`).

| | |
|---|---|
| Original assumption | "multi-company inconvenience" |
| Correct scope analysis | A COMPANY-scoped financial effect is parameterised from outside its owning scope |
| Under the corrected constitution | The required scope for the policy read is the document's company. It is not supplied. The correct behaviour is **DENY**; the observed behaviour is silent substitution |
| Updated classification | **Scope violation, EXECUTES ≠ OWNS. Tolerance-zero candidate under `EC-04` (company isolation)** |
| Architecture impact | The kernel must resolve every policy from the company owning the financial effect, and must deny when that company cannot be proven |
| Cross-process impact | `P04` A2R (posting context), `P11` (scope reconciliation) |
| Evidence still required | Runtime reproduction on a two-company tenant with differing settings |

### `P10-S-02` — a scopeless object performing a company-scoped act

The grouped generation runs on a **report object that carries no company at all** (`E-P10-053`), over a line population that may span several companies (`E-P10-023`), and creates one entry whose company is **back-filled from the journal**, falling back to the active company (`E-P10-054`). The lock-date check and the rounding precision consult only the active company (`E-P10-019`).

| | |
|---|---|
| Original assumption | "a multi-company report bug" |
| Correct scope analysis | A PLATFORM-scoped object is executing a COMPANY-scoped act with the owning company derived rather than asserted |
| Under the corrected constitution | Required ownership cannot be proven → **DENY**. The observed behaviour derives it |
| Updated classification | **Scope violation, ownership derived not asserted. Tolerance-zero candidate under `EC-04`** |
| Conditional | Whether the cross-company entry posts or is refused depends on whether the chart of accounts is shared across the companies (`E-P10-055`). Shared → posts silently. Not shared → refused loudly. **The safer outcome is an accident of configuration, not a control** |
| Architecture impact | Generation must never be initiated from an object that does not carry the owning company |
| Evidence still required | Runtime reproduction under both chart configurations |

## 3. Scope Behaviour That Is Correct, and Should Be Copied

The accrual wizard carries a stored company, executes explicitly in that company's context, and **refuses outright** when the selection spans companies (`E-P10-026`). It is the only P10 mechanism that implements `MISSING REQUIRED SCOPE = DENY`.

This is recorded as the positive pattern: the requirement in `09_P10_EVENT_TO_GL_MATRIX.md` `R-05` is not an invention — it is the reference product's own best behaviour, generalised.

## 4. What Is Deliberately Not COMPANY-Scoped

Recording these explicitly, because the superseded "tenant and company everywhere" reading would have got all four wrong:

1. **Day-count convention definitions** are PLATFORM reference data. A company does not own the definition of 30/360; it owns the *choice* of it.
2. **The period-grid algorithm** is PLATFORM. The company owns its fiscal calendar, not the arithmetic that cuts a window against it.
3. **The recognition event schema** is PLATFORM. The instances are COMPANY.
4. **The service window** is a TENANT fact. The same contract billed by two companies of one tenant has one window. Forcing it to COMPANY scope would duplicate a customer fact per legal entity and would make inter-company recharge incoherent.

## 5. Scope Questions P10 Cannot Resolve Alone

| # | Question | Why research cannot settle it | Routed to |
|---|----------|-------------------------------|-----------|
| `P10-SQ-01` | May a tenant *bind* an allocation convention across its companies, or only default it? | Normative — it is a governance choice about how much autonomy a legal entity retains | Boss, via `P10-D-04` |
| `P10-SQ-02` | Are two unrelated companies under one operator separate tenants for recognition purposes? | The corrected constitution says unrelated independent companies are separate tenants by default; whether these particular companies are unrelated is a business fact | `P11` |
| `P10-SQ-03` | Is a shared chart of accounts permitted in SMEsPlus? | Architectural. It decides whether `P10-S-02` fails loudly or silently | Boss / `P04` |

Status of all three: `HOLD — SCOPE EVIDENCE REQUIRED`, with unaffected work continuing per `REV2-CORR1` §8.
