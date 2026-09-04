# ACCOUNT WAVE A — `GB-08` DOWNSTREAM DEPENDENCY MAP

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GB08-001` · Layer 1 clean-room
Date `2026-09-04`

> What is downstream of the `GB-08` ruling, how hard each dependency is, and what specifically breaks if
> the ruling is deferred or made wrongly. Evidence citations resolve to
> `ACCOUNT_WAVE_A_GB08_EVIDENCE_TRACE.md`.

---

## 1. The dependency shape has changed

The parent package mapped `GB-08` as a **version-choice** dependency: *"which reference build's rate
behaviour do we inherit."* This session's evidence collapses that: the four distinct reference variants
implement **one** resolution semantic, and the v18 divergence (`Δ1`) does not change the rate selected
(`GB08-F1`).

**What is downstream is therefore not a version choice.** It is three things:

| | The real dependency | Evidence |
|---|---|---|
| `R1` | **May a branch own an exchange rate?** Today the schema says yes, the UI says yes, the record rule says yes, and the resolver says no — silently | `GB08-F7` |
| `R2` | **What happens when no applicable rate exists?** Today: fall forward to a *future* rate, then to par `1.0`, silently, in every variant | `GB08-F4`, `GB08-F5` |
| `R3` | **Is an unowned, database-wide rate row legal?** Today: yes, creatable by any accounting manager, readable by every tenant | `GB08-F8` |

Everything below hangs off `R1`, `R2`, `R3`.

---

## 2. Wave B — Accounts Receivable

| Wave B element | Depends on | Hardness | What breaks without the ruling |
|---|---|---|---|
| Foreign-currency **customer invoice** recognition | `R2`, then `R1` | **HARD** | The functional amount is the resolver's output. Under the current semantic an invoice dated before the rate table's first row is recognised at a **future** rate, and one with no rate at all at **par** — both silently. Wave B cannot specify recognition on top of that |
| **Payment** at a different rate; **realised FX** on settlement | `R2`, `R1` | **HARD** | Realised FX is the difference between two conversions. If either leg can be a fallback value, the "gain" is an artefact of the fallback, not of the market |
| **Credit notes** and reversals in foreign currency | `R1`, `R2` | **HARD** | A reversal must reproduce the original resolution or it will not net to zero. `GB08-F6` (ownership beats recency) means the original resolution is **not** reconstructible from the date alone — it depends on which rows existed at posting time |
| **Aged AR** in presentation currency | `R2`, `R3`, and `Δ3` | **HARD** | Aged-AR views are grouped monetary aggregations. On v19 they route through `sum_currency`, which converts at **today**, outside the record rule, with a par fallback (`GB08-F9`). `account.move.line` has **no opt-out override** (`GB08-F11`) |
| **AR reconciliation** across currencies | `R1`, `R2` | **HARD** | Two amounts must be comparable; fallback-valued amounts are not |
| **Domestic-only AR** | — | **NONE** | Unaffected |

> **Wave B cannot define AR revenue measurement in foreign currency without `R1` and `R2`.** This
> remains the single largest Wave A → Wave B carry-forward, and it is `D2` in the Wave B readiness
> package. **The dependency is confirmed; its content is corrected.**

---

## 3. Accounting semantics affected

| Semantic | Affected by | Consequence today |
|---|---|---|
| **Initial recognition** | `R2` | An amount may be recognised at a future rate or at par with no error and no trace |
| **Unrealised revaluation** (period-end) | `R2`, `R1` | Revaluation uses the same resolver; a fallback in the revaluation moves P&L |
| **Realised FX** | `R2` | A realised gain computed from a fallback-valued leg is not a market outcome |
| **Comparatives and restatement** | `R2`, `GB08-F6` | Re-deriving a prior period does **not** reproduce the original figures, because resolution depends on the rows present at posting time and there is **no journal entry recording why** |
| **Consolidation** | `R1` | Root-scoped resolution is what makes group consolidation coherent. If `R1` permits branch ownership, consolidation needs an explicit translation policy that does not exist today |
| **Presentation-currency reporting** | `Δ3`, `R3` | Grouped multi-currency totals convert at **today**, not at transaction dates. The figure is not a ledger total |
| **Statutory reporting (Thai)** | `R2` | TAS 21 is the governing standard **by name**. The specific paragraph obligations are **not verified in this session and are held** under the programme's statutory-claim rule. The *mechanical* fact stands regardless: par substitution is not a spot rate |

---

## 4. SaaS / tenant / company semantics affected

| Boundary | Affected by | Status |
|---|---|---|
| **Tenant isolation of rate data** | `R3` | **BREACHED BY DESIGN TODAY.** `company_id` nullable + global record rule admitting `company_id = False` + `group_account_manager` `1,1,1,1` = one tenant's manager can create a row every tenant reads (`GB08-F8`) |
| **Allowed-company scoping on aggregates** | `Δ3` | `Δ3` ignores the user's allowed-company set entirely and hardcodes `env.company.root_id` (`GB08-F9`) |
| **Branch as a tenant sub-boundary** | `R1` | Currently a **half-boundary**: writable and visible, never authoritative (`GB08-F7`) |
| **Single-tenant reading is unsafe** | all | Every one of these is invisible in a one-company database and material in a many-company one |

---

## 5. Migration semantics affected

| Migration concern | Status |
|---|---|
| **Does the `Δ1` change alter DDL?** | **No.** Identical columns, identical constraint. And per `GB08-F1` it does not alter behaviour either |
| **Is there any migration artefact for `Δ1` / `Δ2`?** | **No.** A pure behavioural change in a point release produces none |
| **Would a DDL-shaped migration gate detect any of this?** | **No.** There is nothing for it to inspect. This is `J-15` |
| **Does `Δ3` change DDL?** | **No.** It is a new query against an unchanged table |
| **Does any option produce a migration artefact?** | **Only `S3`** — reassigning `company_id IS NULL` rows is a data migration with a reviewable artefact |
| **Which option carries the largest silent-revaluation risk?** | **`S2`.** Any existing branch-scoped row is inert today (`GB08-F7`); `S2` makes it live, retrospectively, with **no DDL change and no artefact** |
| **Can a build be identified from its path?** | **No** — `GB08-F10`. `CLAUDE AI/MIGRATION/ODOO18/enterprise` is a **v19** tree |

---

## 6. Reporting semantics affected

| Surface | Path | Behaviour today |
|---|---|---|
| List / relational views | `web/static/src/model/relational_model/utils.js:546–553` | Emits `<field>:sum_currency` for **every** monetary field — opt-out by field definition, not opt-in |
| Pivot | `views/pivot/pivot_model.js:1086–1090` | same |
| Graph | `views/graph/graph_model.js:333–339` | same |
| **Display suppression** | `utils.js:592–601`, `pivot_model.js:988–997` | The `sum_currency` value is **discarded** when a group spans a single currency |

> **Reachability is broad; visible consequence is narrower.** The rule-bypassing query **executes** on
> essentially every grouped monetary read; the wrong figure **surfaces** only on groups spanning two or
> more currencies. **`GB08-F11` adds the sharper point:** three models opt out server-side —
> `budget.line`, `analytic.account`, `stock.quant` — and **`account.move.line` does not.**

---

## 7. Blocking relations — what `GB-08` blocks and what blocks `GB-08`

```
                    MCU-21  (source of truth for rate data)
                      |
                      v
   T0-04  ------>   GB-08   <------  GB-03   (null-company row / tenant axis)
 (tenant model)       |                        - precondition of S3 and of D
                      |
        +-------------+-------------+
        |             |             |
        v             v             v
   D2 (Wave B AR)  MCU-20/BW-31   J-15
   FX invoice      (delta-3       (migration
   FX payment       defects)       with no
   realised FX                     artefact)
   aged AR
```

| Relation | Direction | Note |
|---|---|---|
| `MCU-21` → `GB-08` | `MCU-21` is the **parent** | It selects the source of truth; `GB-08` is one of its children |
| `GB-03` → `GB-08` | **Precondition** for `S3` and `D` | The null axis must be ruled on before a tenant-standard or clean-room semantic can be specified |
| `T0-04` → `GB-08` | **Precondition** for `S3` | "Tenant" is undefined in the programme; `S3` cannot be specified without it |
| `GB-08` → `D2` | **Blocking** | Wave B AR foreign-currency scope |
| `GB-08` → `MCU-20`/`BW-31` | **Dispositions**, not blocks | These are verified defects to be fixed under any option |
| `GB-08` → `J-15` | **Explains** | The migration control cannot see behavioural change |

> **`GB-08` is not the root of its own dependency tree.** `MCU-21` is above it, and `GB-03` and `T0-04`
> gate two of its four semantic options. A ruling on `GB-08` alone unblocks `D2` **only** if the chosen
> semantic is `S1` or `S4`; `S2` and `S3` carry preconditions that are themselves open.

---

## 8. Wave A Final Gate impact

| Gate dimension | Effect of `GB-08` remaining undecided |
|---|---|
| **Gate recommendation** | Stays **`RECOMMEND HOLD`**. `GB-08` is one of eight open blockers and the only one that must be settled before any downstream conclusion is safe |
| **`CONDITIONAL PASS`** | Remains unavailable — tolerance-zero boundaries remain unresolved, and `GB08-F7`/`GB08-F8` are tolerance-zero in kind |
| **`FAIL`** | Still not recommended. The semantic model has not been substantively disproved; this session **corrects** six parent claims and **disproves none of the model** |
| **`% Board` / `% STATE` / `% STEP`** | Still **not calculable**. `GB08-F3` shows the previously published denominator itself overlaps |
| **Wave B readiness** | Stays **`NOT READY — EXACT DEPENDENCIES`**. `D2` is unchanged in status and corrected in content |
