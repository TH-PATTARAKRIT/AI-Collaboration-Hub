# 12 — CANDIDATE SAAS BOUNDARY REDESIGN

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01`
**No tenant-isolation claim is made in this file. §5 explains why one cannot yet be made.**

---

## 1. The governing mismatch

`VF-15`: **the reference has no tenant concept.** Its outermost boundary is the **company group** — a
root company and its descendants. Account codes, currency rates and fiscal years are keyed to the
group **root**.

`16 §1` frames it correctly and this design keeps the framing:

> *This is not a defect in the reference system, which was not built for that deployment. It is a
> **boundary mismatch** that SMEsPlus must close deliberately.*

> ### `D-33` — Tenant is a first-class identity above company. `EVIDENCE-DEPENDENT`
>
> Blocked on `GB-01`, a **Boss decision**, into which `GB-03`'s open half now also reduces — so `GB-01`
> carries more weight after the parent's last round, not less.

---

## 2. The four boundary failures and their candidate closures

| # | Failure | Candidate rule | Status |
|---|---|---|---|
| `SB-01` | The numbering/date-alignment control store has **no company dimension at all** — one write disables it for **every tenant in the database**, invisibly | **`D-12` / `CR-01`** — every control-affecting configuration value carries a tenant dimension; **no configuration may have database-wide effect** | `PROVISIONAL` |
| `SB-02` | `account × 10000 + company`; past 10,000 the grid **reads or writes another company's code**, silently, and the ceiling is reached by cumulative creation | **`D-13` / `CR-02`** — no identity encoded by arithmetic over other identities | `PROVISIONAL` |
| `SB-03` | Tamper-evidence keyed on **storage row identifiers**; a split, merge, restore or migration invalidates it — *precisely when assurance matters most* | **`D-14` / `CR-03`** — key on business identity | `EVIDENCE-DEPENDENT` — `T0-08` |
| `SB-04` | Deletion evidence written to the **application log** — outside the tenant, in shared infrastructure, not part of the tenant's records | **`D-15` / `CR-04`** — all control evidence inside the tenant's own data | `PROVISIONAL` |

**`SB-01` is the highest-severity item in Wave A's boundary set** and it is also the simplest to state:
a control with no tenant dimension is a shared global. In a multi-tenant database that is not a
configuration bug, it is a cross-tenant control failure reachable by one ordinary write.

---

## 3. Standard template versus tenant — the invented concept

Covered in `05 §2`. Restated here because it is a **boundary** concern:

| `CR-05` / `D-16` | Template-derived and tenant-created configuration remain distinguishable for the life of the tenant |
|---|---|
| Reference support | **none found in the primary tree** — the parent establishes the reference *cannot answer* Boss question 16 (class `A` in that scope) |
| Consequence | Boss question 16 is **unanswerable in the reference** |
| Classification | `DESIGN CHOICE` — declared, because there is nothing to adapt |

---

## 4. Company boundary invariants — carried forward unchanged

| # | Invariant | Basis | Status |
|---|---|---|---|
| `CB-01` | Liquidity accounts are never shared across companies | `BS-10`, `EV-019` — the reference refuses it and the reason is sound | `PROVISIONAL` |
| `CB-02` | Bank-reconciliation completeness gates period locking | `EV-019` — generalise into the close checklist | `PROVISIONAL` |
| `CB-03` | Parent-to-subsidiary irreversible lock cascade is a **policy choice** | `CL-05` | `UNKNOWN` — **Boss** |
| `CB-04` | A journal, an entry and an item each belong to exactly one company | `EV-006` | `PROVISIONAL` |
| `CB-05` | No posted fact is rewritten across a company boundary | `GB-02` | `EVIDENCE-DEPENDENT` — **widened twice** |

---

## 5. Why no isolation claim is made

> ### `D-34` — Cross-boundary exposure must be characterised before any isolation claim. `EVIDENCE-DEPENDENT`

| Fact | Value |
|---|---|
| Exposure sites bounded (`GB-04` / `MCU-16`) | **192**, in three populations |
| Elevation sites | **3 of 93 assessed** |
| Root-vs-company scoping sites | **4 of 37 assessed** |
| Raw-SQL sites | **2 of 62 assessed** |
| **Total** | **9 of 192 (4.7%)** — `93+37+62 = 192`; `3+4+2 = 9` |

> **Corrected after `RB-16`.** The first draft reported *elevation 0 of 93* and *raw-SQL 0 of 62*
> alongside *9 assessed*, which does not reconcile: `0+0+4 = 4`, not 9. It had merged the closure
> round's **round-scoped** metrics with the convergence round's **cumulative** counts. The
> per-population split above is the reconciling form. **This is the arithmetic this package's own
> denominator rule exists to prevent, committed by this package.**
| Company-consistency enforcement | **9 of 22** models · **36 of 139** relational fields |
| Declared guards on the company model proven **inert** | **16** (`T0-09`, `VF-20`) |
| And | the 192 bound was computed over a path set now known to **exclude 962 manifested modules** (`GB-07`, `MCU-18`) |

**4.7% of a bound that is itself known to be under-scoped.** `CR-06` marks tenant isolation a
`Tolerance = 0` candidate; a tolerance-zero property cannot be asserted from a 4.7% traversal.

> **This package therefore makes no tenant-isolation claim of any kind, positive or negative.** The
> design rules `CR-01`…`CR-05` are stated as *requirements*; whether the resulting system meets them
> is untestable until `GB-04` is traversed over the corrected path set.

---

## 6. Migration and historical continuity

| Concern | Finding | Candidate | Status |
|---|---|---|---|
| Opening position | an ordinary posted entry balanced to current-year earnings (`EV-017`, `AE-14`) | keep the mechanism, **add provenance** | `PROVISIONAL` `D-29` |
| Migrated balance → origin | **no lineage** (`15 §4`) | required | `PROVISIONAL` |
| Opening measurement | `BW-30` — **opening and onboarding valued at a 2010 rate** | `FXD-03` refusal applies to opening postings too | `PROVISIONAL` |
| Migrated rate rows | constraints are **not re-run at upgrade**; the feed maintains such a row without re-checking its company (`MCC-C-R1`) | revalidate at import | `EVIDENCE-DEPENDENT` `D-35` / `MCU-19` |
| Tamper-evidence across migration | **cannot survive it** (`SB-03`) | `D-14` | `EVIDENCE-DEPENDENT` |
| Historical continuity of meaning | no temporal validity anywhere (`VF-03`) | `D-21` | `PROVISIONAL` |
