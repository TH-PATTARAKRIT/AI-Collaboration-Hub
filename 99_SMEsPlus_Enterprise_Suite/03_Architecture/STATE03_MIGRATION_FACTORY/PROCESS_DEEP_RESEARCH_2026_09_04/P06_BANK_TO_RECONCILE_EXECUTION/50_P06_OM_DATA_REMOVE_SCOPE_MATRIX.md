# P06_OM_DATA_REMOVE_SCOPE_MATRIX.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S06)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Governing constraint:** *"Do not solve by simply adding `company_id`."* — and the CORR1 reframe already in force: **a null company is not itself the defect; the defect is the absence of any scope declaration**, where one field is made to express ownership, availability and selection at once.

---

## 1. Scope determination for the operation

| Scope question | Determination | Basis |
|---|---|---|
| What scope **owns the function**? | **PLATFORM** — it is a maintenance tool on a core settings model, shipped by a third party, with no company or tenant dimension of its own | `_inherit = 'res.config.settings'`; module `depends: ['base']` |
| What scope **owns the target data**? | **COMPANY** — every table it deletes holds company-owned legal and accounting truth | Scope Register `37_` rows 3–7, 13 |
| What scope **executes**? | **whatever session invokes it** — no scope is asserted or checked | `45_` AUTH-F-01 |
| What scope may **access**? | declared `base.group_system` at model level; **not enforced on this path** | `45_` AUTH-F-02/03 |
| What scope may **mutate**? | **undetermined and unchecked** | — |
| What scope **audits**? | **none — the audit trail is itself a deletion target** (`mail.message`, `mail.followers`, `mail.activity`) | `44_` §3 |

**SCOPE-F-11 — A PLATFORM-scoped function performs unfiltered destruction of COMPANY-scoped financial truth.**
This is the exact shape CORR1 exists to name: **the operation's own scope and its targets' scope are different, and nothing reconciles them at the boundary.** Under the correction's rule — *missing required scope = DENY* — an operation that cannot state which company's data it is about has no basis to proceed at all.

---

## 2. Can it target one company, several, or all?

| Target | Answer | Evidence |
|---|---|---|
| **One company** | **NO — it cannot be constrained to one.** `delete from <table>` has no predicate | `44_` OMD-F-04 |
| **All companies in the database** | **YES — that is the only mode it has** | same |
| **One tenant** | not applicable — no tenant concept exists in the reference | — |
| **Several tenants** | **see §4** |
| **Platform reference data** | partially — `remove_account_chart` deletes `account.account`, `account.journal`, `res.partner.bank` | `44_` §4 |

**SCOPE-F-12 — The operation has no company-restricted mode.** A multi-company database has one blast radius: all of it.

---

## 3. The paradox that makes this a scope finding rather than a bug

**SCOPE-F-13 — The same method applies company scoping to its side effects and none to its main effect.**

Within `remove_account`:
- the **sequence reset** carries `('company_id', '=', self.env.company.id)`;
- in `remove_account_chart`, `ir_default` and `account_journal` updates carry `company_id=%d`;
- in MIGR18, the Thai WHT-certificate cleanup carries `('company_id','=',self.env.company.id)`;
- **the table deletes carry nothing.**

So the operation **deletes every company's journal entries and then resets only the current company's sequences.** The two halves disagree about what they are operating on.

**Consequence, stated plainly:** in a two-company database, running `remove_account` from Company A destroys Company B's accounting records **and leaves Company B's sequences untouched**, so B's next document continues from its old number while its history is gone. The result is not a clean reset of anything — it is an inconsistent state in both companies.

**This is why "add `company_id` to the WHERE clause" is the wrong remedy** and why the directive forbids it. The defect is not a missing predicate. It is an operation whose **business semantics were never defined**: nobody decided whose data it removes, so half of it guesses one way and half the other.

---

## 4. Cross-tenant assessment — bounded honestly

**SCOPE-F-14 — Whether this is a cross-tenant defect depends entirely on the tenancy model, which the reference does not implement.**

- If SMEsPlus tenants map to **separate databases**, the operation is bounded to one tenant by construction, and the finding is cross-**company**, not cross-tenant.
- If tenants map to **companies within one database** — which CORR1 explicitly discourages (*"unrelated independent companies are separate tenants by default"*) — then the operation is **cross-tenant destructive**, satisfying severity criterion **C3**.

**The reference implementation has no tenant concept, so this cannot be resolved from source.** **HOLD — SCOPE EVIDENCE REQUIRED**, and it is a **target-architecture** question rather than a reference one.

**The severity assignment in `46_` deliberately does not rely on C3 for `B-50`.** It qualifies on C1, C2, C4 and C6 without it. **If the tenancy model turns out to place tenants in one database, C3 is added and the finding gets worse — it cannot get better.**

---

## 5. The four problems, classified separately as directed

| Class | Present? | Statement |
|---|---|---|
| **Authorization problem** | **YES** | No server-side check on the dispatch chain (`45_`). |
| **Scope resolution problem** | **YES** | The operation never determines whose data it targets; its own scope (PLATFORM) and its targets' scope (COMPANY) are never reconciled. |
| **Ownership problem** | **YES** | It deletes records it does not own and cannot prove it may act on. Under CORR1, *ownership cannot be proven = DENY*. |
| **Destructive business-semantics problem** | **YES, and this is the root** | There is no defined business event for "erase the financial history of a company". No accounting standard, no statutory basis, no reversal path, no audit record. **The operation implements a business act that does not exist.** |

**SCOPE-F-15 — The four are independent, and fixing any three still leaves a defect.**
Add authorisation and an unauthorised user is stopped — an administrator still destroys history irrecoverably. Add company scoping and the blast radius shrinks — the act is still unlogged and irreversible. Add logging and it is recorded — it is still not reversible. **Only defining the business act settles it, and the correct definition may be that no such act exists.**

---

## 6. Requirements for the target

| ID | Requirement |
|---|---|
| `SCM-R-01` | An operation may not act on data whose scope it has not resolved. Missing scope = DENY, per CORR1. |
| `SCM-R-02` | A destructive operation must declare **one** scope for the whole act. Deleting at one scope and compensating at another is a defect even when both are individually correct. |
| `SCM-R-03` | Bulk erasure of financial history must not be expressible as an operation. Where records must be removed, the act must be a scoped, authorised, logged, reversible **business event** with an owner. |
| `SCM-R-04` | The audit trail must not be a deletion target of any operation. |
| `SCM-R-05` | Tenancy must be declared before any multi-company destructive semantics can be assessed. Until then, C3 exposure is unbounded. |
