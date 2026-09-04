# 05 — CANDIDATE CHART OF ACCOUNTS REDESIGN

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01`

---

## 1. Canonical identity

> ### `D-20` — Classification identity is permanent. Replacement is **succession**, never rewrite. `PROVISIONAL`

`BS-07` is `VERIFIED BUSINESS SEMANTIC` and the reference gets the identity model **right**: the
account is a record, the code is a per-company mutable label. `ST-01` records this as independently
corroborating the standing Boss-approved principle.

**But `VF-14` destroys it.** Merge retargets posted items, deletes accounts **past the ORM's own
guards**, and writes **no record of any kind** — invisible, irreversible, untracked (`AE-20`,
`COR-08`). `15 §1` records the result plainly: account identity is *"destroyed by merge"*.

| Candidate rule | Statement | Status |
|---|---|---|
| `CA-01` | Classification identity is independent of code, name and storage identifier | `PROVISIONAL` |
| `CA-02` | A classification is **never deleted** once a fact references it | `PROVISIONAL` |
| `CA-03` | Replacement is a **succession relation**: predecessor retained, successor named, both queryable. Reports over a past period resolve through the succession | `PROVISIONAL` |
| `CA-04` | Retirement (`AE-19`) refuses new facts and is reversible; it is **not** deletion | `PROVISIONAL` |
| `CA-05` | Every retargeting of a posted fact is itself an accounting event with actor, reason and record | `PROVISIONAL` — the direct answer to `VF-14` |

---

## 2. Standard template versus tenant configuration

> ### `D-16` — Template-derived and tenant-created configuration stay distinguishable for the tenant's life. `PROVISIONAL`

`16 §4` states the gap without ambiguity: *"no distinction exists — once provisioned, template
accounts and tenant accounts are indistinguishable."* And:

> **Boss question 16 has no reference answer.** The reference model **cannot** answer which chart
> concepts belong to the standard SaaS template versus tenant configuration, because it retains no
> record of which accounts came from the template. **SMEsPlus must introduce it; there is nothing to
> adapt.**

`DESIGN CHOICE` throughout this section — declared as such because there is no evidence to adapt.

| Concern | Candidate | Status |
|---|---|---|
| Template membership | Every provisioned classification records **which template, which version** it derives from | `PROVISIONAL` |
| Tenant additions | Distinguishable permanently; never silently absorbed into the template | `PROVISIONAL` |
| Tenant customisation of a standard classification | **Bounded** — labels and presentation yes; identity, type and control status no | `PROVISIONAL` |
| Template upgrade | Applies to template-derived members only; tenant additions and bounded customisations survive | `PROVISIONAL` |
| Template rollback | **`UNKNOWN`** — `GAP-S01`, none identified in the reference | `UNKNOWN` |
| Divergence report | A tenant can be asked "how does your chart differ from the standard?" and answered | `PROVISIONAL` |

---

## 3. Account type, group and control status

| Aspect | Reference | Candidate | Status |
|---|---|---|---|
| Type drives reporting behaviour | yes, and **retroactively** (`EV-016`) | type change is a **versioned, dated** event; past reports unaffected | `PROVISIONAL` `D-21` |
| Temporary vs permanent | derived from type | keep the derivation | `PROVISIONAL` |
| Carry-forward | a type property evaluated at report time — **not an event** | keep the concept; **add the auditability** | `PROVISIONAL` |
| Reconcilable | an account property; receivable/payable forced | keep | `PROVISIONAL` |
| **Control account status** | an attribute like any other | **governed, never importable** | `EVIDENCE-DEPENDENT` `D-32` |

> ### `D-32` — Control-account status is a governed attribute, not an importable field. `EVIDENCE-DEPENDENT`
>
> `BW-33`: a control-account attribute is **silently flipped by imported data**. And `T0-09`: **16
> declared company-consistency guards on the company model — on the destination accounts of
> automatically generated ledger facts — **do not execute at write**; they are present in the view layer only (`G-C7`). Population floor **30 declarations across 4 files**, one named, so `T0-09` is **not bounded** (`VF-20`).
>
> **Blocked pending `T0-09`.** The design rule is clear; what is not established is how many other
> declared guards are inert. `CR-07` applies: *prove the executor of every declared control.*

---

## 4. Off-balance and account lifecycle

| Element | Position | Status |
|---|---|---|
| Off-balance semantics | Not established in Wave A evidence at design depth | `UNKNOWN` — **class `C`, not searched.** Not to be reported as absent |
| Lifecycle states | `draft → active → retired → succeeded` | `PROVISIONAL` |
| Deletion | **removed from the model** once any fact references the classification | `PROVISIONAL` `CA-02` |
| Archival | Retirement + succession covers it; no separate destructive path | `PROVISIONAL` |

---

## 5. Multi-company and the code grid

| Finding | Candidate | Status |
|---|---|---|
| Accounts are many-to-many with companies, codes per company (`EV-001`) | keep — it allows one shared classification with per-company presentation (`ST-01`) | `PROVISIONAL` |
| Codes are keyed to the **group root** (`VF-15`) | **re-key to tenant** | `EVIDENCE-DEPENDENT` — blocked on `GB-01` |
| The code grid encodes `account × 10000 + company`, aliasing silently past 10,000 (`SB-02`, `COR-18`) | **`D-13` — no identity encoded by arithmetic over other identities** | `PROVISIONAL` `CR-02` |

**`SB-02` is worth stating precisely because of how it fails**: the ceiling is reached by *cumulative
creation*, not by live count, and past it the grid **reads or writes another company's code without
raising**. A silent cross-company write is a tolerance-zero class of failure reached by ordinary
growth.
