# P06_SCOPE_REGISTER.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION (CP-C10)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Relationship to `19_P06_SCOPE_OWNERSHIP_MATRIX.md`:** that file determined scope for 30 objects. This one reconciles those determinations against seven peer scope matrices and records what is agreed, disputed, and net-new.

---

## 1. Peer scope matrices read

`P11_SCOPE_OWNERSHIP_MATRIX.md` · `p02:20_P02_SCOPE_OWNERSHIP_MATRIX.md` · `p05:22_P05_SCOPE_OWNERSHIP_MATRIX.md` · `p07:20_P07_SCOPE_OWNERSHIP_MATRIX.md` · `p09:19_P09_SCOPE_OWNERSHIP_MATRIX.md` · `p10:10b_P10_SCOPE_OWNERSHIP_MATRIX.md` · `p03:18_P03_SCOPE_OWNERSHIP_MATRIX.md` · `p04:20_P04_SCOPE_OWNERSHIP_MATRIX.md`.

---

## 2. Agreed determinations

| Object | P06 | Peers | Status |
|---|---|---|---|
| Journal | COMPANY | P11 COMPANY · P05 COMPANY | **AGREED, 3 processes** |
| Payment / receipt | COMPANY | P05 COMPANY · P02 COMPANY | **AGREED** |
| Reconciliation / matching record | COMPANY, mutate never | P11 COMPANY mutate **never** · P02 COMPANY | **AGREED, 3 processes** |
| Journal entry | COMPANY | universal | **AGREED** |
| Lock date / period close | COMPANY, inherited | P11 COMPANY · P02 COMPANY | **AGREED on scope** |
| Payment method line | COMPANY (journal's company) | P05 same | **AGREED** |
| Bank statement / statement line | COMPANY | no peer row | **UNOPPOSED** |

---

## 3. Disputed and unsettled

**SCR-F-01 — Currency rate: three processes, three positions, no settlement.**

| Process | Position |
|---|---|
| **P06** | **TENANT** — shared reference the customer maintains; unrelated customers must not share one |
| **P11** | **split**: `PLATFORM` for the rate *observation*, `COMPANY` for the rate *selection*. `SC-05` records that *"one table keyed to the company-group root"* collapses the two |
| **P02** | **HOLD — SCOPE EVIDENCE REQUIRED** (`P02-SC-01`), with the same observation/application split named |
| Reference impl. | global, with a company-scoped reporting overlay |

**P06 revises its position.** P11's and P02's split is better than P06's single answer: the *observation* (a rate existed on a date) and the *selection* (this transaction used that rate) are different objects at different scopes. **P06 withdraws "TENANT" as a single determination and adopts the split**, adding that the *tenant* is the correct custodian of the observation table when the platform does not supply it.
**Recorded as a P06 position change on peer evidence.** P11's `T0-07` remains `UNRESOLVED`, tolerance-zero, and P06 does not close it.

**SCR-F-02 — Lock date: scope agreed, enforceability disputed.**
All three processes scope it COMPANY. But **P11 `SC-04`** records *"Fiscal year | `COMPANY` | root companies only; child companies refused … **this is a scope violation**"*, and **P04 `P04-B-43`** establishes the hard lock cascades from every parent, with elevated privilege, including archived companies, irreversibly.
**P06's contribution:** the cascade is real and its members may be **legally distinct** — `vat` and `company_registry` are not root-delegated (B27-F-04). **So a scope agreed as COMPANY is enforced across a boundary that is not COMPANY.** `P06-B-45`.

---

## 4. Net-new to the programme

**SCR-F-03 — Three P06 objects have no counterpart row in any peer scope matrix.**
Verified: PATTERN `bank account|payment provider|payment acquirer|payment token` over all seven peer matrices → **zero rows**.

| Object | P06 determination | Consequence |
|---|---|---|
| **Physical bank account** (`res.partner.bank`) | **COMPANY**, and the reference makes ownership optional and derived | Under P11's Delta 02 rule — *"REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY"* — `A4b` is a **DENY case as published**. P06 is the only process to have found it. |
| **Payment provider** | **HOLD** — TENANT contract vs COMPANY settlement | net-new |
| **Payment token** | COMPANY-owned, **availability wider than ownership** | net-new; severity MEDIUM after adversarial test |

**These three rows will land in `P11_SCOPE_OWNERSHIP_MATRIX.md` as additions, not reconciliations.**

---

## 5. The CORR1 reframe, tested against P06's own findings

The correction's key reframe, as it now stands in project memory:
> *"a null company is not itself a defect — the defect is the absence of any scope declaration, where one nullable field is made to express ownership, availability and selection at once."*

**SCR-F-04 — P06's `A4b` is a textbook instance, and the reframe sharpens it.**
`res.partner.bank.company_id` is a **single nullable derived field** made to express:
- **ownership** — whose bank account is this;
- **availability** — which companies may use it (`check_company_domain_parent_of` admits `False` into every company);
- **selection** — which account a journal may bind (`account_journal.py:469` skips its own check when the value is `False`).

**One nullable field, three jobs, no scope declaration.** That is the defect stated correctly — sharper than P06's original phrasing ("an unowned bank account is admitted everywhere"), which named the symptom.

**SCR-F-05 — And the same reframe explains `A4c` and `P06-B-47` as one defect, not three.**
The payment token's owner is reached through two hops (`token → provider → company`). The bank account's owner is reached through one hop and may be null. In both cases **ownership is derived rather than asserted**, so it cannot be independently verified at the point of use.
**`P06-B-47` is therefore the general form, and `A4b`, `A4c` are its two instances.** This consolidation is a product of the corrected model; it was not visible before.

---

## 6. P06 scope positions, final

| # | Object | Ownership | Financial effect owner | Status |
|---|---|---|---|---|
| 1 | Currency rate observation | PLATFORM, TENANT-custodied where absent | — | **revised on peer evidence** |
| 2 | Currency rate selection | COMPANY | the transacting company | **adopted from P11/P02** |
| 3 | Physical bank account | COMPANY | the account-holding company | **net-new; DENY case** |
| 4 | Bank journal | COMPANY | same | agreed |
| 5 | Bank statement / line | COMPANY | same | unopposed |
| 6 | Bank event identity | COMPANY | — | escalated to `P11-B-02` |
| 7 | Payment | COMPANY | same | agreed |
| 8 | Payment method (definition) | PLATFORM | — | unopposed |
| 9 | Payment method line | COMPANY | same | agreed |
| 10 | Payment provider | **HOLD** | COMPANY at settlement | **net-new, HOLD** |
| 11 | Payment token | COMPANY | — | **net-new; availability > ownership** |
| 12 | Payment transaction | COMPANY | same | unopposed |
| 13 | Reconciliation record | COMPANY, mutate never | yes — it emits | agreed |
| 14 | Reconcile model / tolerance | COMPANY | **yes — it decides whether an invoice closes** | unopposed |
| 15 | Suspense account | COMPANY | same | unopposed |
| 16 | Inter-bank transfer account | COMPANY | same | unopposed |
| 17 | Company hierarchy (`parent_id`/`root_id`) | **TENANT grouping** | **none — it is not a financial boundary** | **P06's closure of `B-27`** |
| 18 | Lock dates | COMPANY, inherited strictest-wins | yes | agreed on scope, disputed on enforcement |
| 19 | Intercompany settlement carrier | **TENANT** — owns neither effect, proves both | two COMPANY effects | **net-new, does not exist** |
| 20 | Audit-trail guarantee | COMPANY, must be one-way | — | revised at prior round (R-07) |

---

## 7. Open scope items

| ID | Item | Status |
|---|---|---|
| `SCOPE-F-06` | Payment provider: TENANT contract vs COMPANY settlement | **HOLD — DESIGN DECISION REQUIRED** |
| `SCOPE-F-08` | Bank aggregator credential scope | **HOLD — SCOPE EVIDENCE REQUIRED** |
| `SCOPE-R-02` | Declare the COMPANY boundary once and enforce it everywhere | **HOLD — DESIGN DECISION REQUIRED** (evidence satisfied, decision outstanding) |
| `T0-07` (P11) | Currency-rate scope collapse | **UNRESOLVED at P11, tolerance-zero.** P06 defers |
| `S-27` | Thai WHT rule set: PLATFORM reference vs COMPANY application | **HOLD — STATUTORY.** P05 reached the same split and calls the current shape a defect (`SC-01`) |
