# P11 — C5 · BLOCKER POPULATION RECONCILED

`[SMEPLUS-26-09-05-ACC-P11-CORE-RECON-CORR1-001]` · CP-P11C05 · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**
> **No blocker may be closed because its wording improved.**

---

## 1. Denominator

`POPULATION` `P11-B-nn` ids in `P11_FINAL_BLOCKER_REGISTER.md` · `UNIT` one distinct id ·
`PATH SET` that file at `43195fd`. **Controls run. Executed: `18`.** The prompt's figure reproduces.

## 2. Register

`PD` = peer dependency · `BD` = Boss-decision dependency.

| id | Blocker | Sev | Evidence state | PD | BD | CORR1 changes it? | Exact closure condition |
|---|---|---|---|---|---|---|---|
| `B-01` | `P01`–`P10` published nothing | — | **SUPERSEDED** | — | — | **YES — DISCHARGED** | **All ten published.** Replaced by `B-13`/`B-19` |
| `B-02` | No accounting-event identity (`UAE-29`) | **root** | **UPGRADED to `A`** | `P08` | **YES** | **YES — evidence upgraded, blocker open** | Boss design decision. No research closes it |
| `B-03` | `0 of 17` double-counting classes guarded | high | **CORROBORATED** | `P08` | YES | **YES** — `P08`: 22 attacks, **none stopped outright** | A guard per class, or a Boss-accepted residual |
| `B-04` | No declared programme output path | med | unchanged | all | YES | no | A Boss/PMO declaration |
| `B-05` | `BC-02` binds one producer pair only | high | unchanged | all | YES | no | Generalised contract adopted (`D-8`) |
| `B-06` | `DC-09` double cost absorption | high | unchanged | `P03`,`P04` | YES | no | `BLK-07` ruled **and** a relief mechanism designed |
| `B-07` | `DC-07` candidate double tax recognition | med | unchanged | `P07` | — | no | Source evidence on unmatch behaviour |
| `B-08` | Objects with no determinable scope | med | **REDUCED to 2** | `P07`,`P10` | partial | **YES** — `P10` supplies budget-adjacent scope; tax config resolved earlier | Scope determinations for budget + migration batch |
| `B-09` | `AASR` baseline predates its parent's closure | med | unchanged | — | — | no | `AASR` re-derived against the closed parent |
| `B-10` | `22`-scenario cross-proof `0 of 22` | high | unchanged | Inventory + all | — | **partially** — producer matrices now exist | A joint cross-proof; not producible by P11 alone |
| `B-11` | Analytic is not a subledger of record | high | **CORROBORATED and widened** | `P09` | YES | **YES** — `P09`: two of eight trace steps have **no carrier at all** | A design decision on the analytic substrate |
| `B-12` | `P05`/`P10` producer contracts not established | high | **RE-OPENED** | — | — | **YES — discharged, then RE-OPENED by challenge `C-05`** | ~~DISCHARGED~~ **Publication is not contract establishment.** `B-10` — carried **unchanged** in this same table — holds **0 of 10 handoffs contract-compliant**, and `D-8` says nine producers are under no contract. Restated: *`P05`/`P10` have published; contract compliance remains 0 of 10*. Prior text: **Both published.** `P05` supplies 15 positions; `P10` six primitives + `R-01`..`R-07` |
| `B-13` | Event-to-GL not reconciled against peer matrices | **high** | **NOW ACTIONABLE** | all ten | — | **YES** | Reconciliation performed. **First time possible.** See C8 |
| `B-14` | Tenancy exception undeclared (`SR-01`) | med | unchanged | — | **YES** | no | `D-11` |
| `B-15` | Hierarchy-spans-tenant unruled (`SR-02`) | high | unchanged | — | **YES** | no | `D-12` + an enforced `MTI-04`-class invariant |
| `B-16` | `T0-13` silent mutation, any scope | **T0** | **STRENGTHENED** | `P10` | YES | **YES** — reaches `P10` recognition entries | Refuse, **or** an attributable trace; trace mandatory where nothing is refused |
| `B-17` | `X2-F06` CRITICAL unrepaired | **CRITICAL** | **RE-OPENED** | `P08` | — | **YES — closed, then RE-OPENED by challenge `C-02`** | ~~DISCHARGED~~ **RE-OPENED:** the `S3` "substrate property" behind 5 of the 7 `DERIVED VIEW` verdicts is a `P08` **source-line (18.0)** statement, and `P08` `52_…_V2` forbids the crossing: *"**No deployed database matches the source line.** Any peer combining the two as one fact must re-read it as two facts with two scopes."* The re-run's **logic and direction stand**; its `S3` input must be re-scoped. Prior text: **DISCHARGED.** Ten rows re-run against the stated rule with `X2-F07`/`F08`/`F09` applied to the row data: **0 unqualified, 2 qualified, 7 derived views, 1 unknown.** `P11_SUBLEDGER_RERUN_B17.md` |
| `B-18` | Five unmarked repairs (`P11-G-03`) | med | **CLOSED** | — | — | **YES — CLOSED BY WORK** | **DISCHARGED.** Four converted to marked form carrying their superseded values (the fifth already stated its prior figures); erasure audit **re-run over the whole set**, controls first (pos 19 / neg 0): **20 strikethroughs, 0 erased** |

## 3. Changed by CORR1

| Movement | Count | Ids |
|---|---|---|
| **DISCHARGED — evidence superseded** | **2** | `B-01`, `B-12` |
| **CLOSED — WORK COMPLETED AND VERIFIED** | **1** | `B-18` only. **`B-17` was closed and then RE-OPENED by the challenge (`C-02`)** — its input crossed a scope its source forbids |
| **Evidence materially strengthened, blocker OPEN** | **5** | `B-02`, `B-03`, `B-11`, `B-13`, `B-16` |
| Reduced in scope, open | 1 | `B-08` |
| Unchanged | 10 | the rest |
| **Newly opened by CORR1** | **2** | `B-19`, `B-20` — below |

### `P11-B-19` / `P11-B-20` — new

| id | Blocker | Status |
|---|---|---|
| **`B-20`** | **`P01` contradicts the generation P11's event-to-GL matrix assumes.** The deployed v19 databases have **no goods-received clearing account and no valuation-layer table**; the bridge is a **v18** mechanism and *"two of three readable live databases cannot run it."* `P01` states Core Accounting *"should not reconcile against a mechanism until the target generation is established"* | **`HOLD — BOSS DECISION REQUIRED`** · routed to `D-1`. **P11 does not resolve it** |
| **`B-19`** | **Peer publication order silently selected P11's reconciliation depth** (`P11-F-12`). Nine deltas were written against the three-to-four peers that happened to publish first, while `P08` — holding the root-set declaration, the class-`A` event-identity absence, and the strongest form of the balance-invariant finding — was never consumed | **`HOLD — DESIGN RESOLUTION REQUIRED`** · closure: adopt `P11-G-04` and re-run intake ranked by relevance to open items |

> ### `18 → 20` registered · **1 discharged (`B-01`) · 1 CLOSED (`B-18`) · 18 open · 0 closed by improved wording.**
>
> **CORRECTED `2026-09-05` by the AAS-03 CORR1 challenge.** `B-17` was closed mid-round and is
> **RE-OPENED** (`C-02`); `B-12` was discharged and is **RE-OPENED** (`C-05`). **The round's net blocker
> movement is one closure, and it is the smallest of the three P11 claimed an hour earlier.**
>
> `B-17`'s re-run **stands in logic and direction** — three subledgers of record still become zero —
> **but one of its inputs is scoped wrongly and the closure does not hold on it.**
>
> **`B-01` is discharged by evidence arriving, not by argument** — the precise distinction this
> register exists to preserve. **No blocker moved because its wording improved.**
>
> **`B-12` is NOT discharged** (`X-C1-C-05`): its condition was **contract establishment**, and what
> arrived was **publication**. `B-10` still records **0 of 10 peers compliant** with the 16-element
> handoff contract, so the condition is not merely unproven — it is contradicted by P11's own register.
>
> ~~and the CRITICAL (`B-17`) is deliberately untouched~~ — **CORRECTED. That sentence was true when
> written and was left standing after it stopped being true.** `B-17` was re-run, closed, and re-opened
> inside this same round; the register carried both statements at once for roughly an hour. Recorded
> as `P11-E-32`, and it is the `P11-E-01` class — **a headline outliving the table beneath it** —
> occurring in the register whose purpose is to prevent exactly that.


---

## `S8` RE-RUN ADDENDUM — `2026-09-05` · `CP-P11C13`

**Source:** `P11_S8_SUPERSESSION_RERUN_CORR1.md`. **6 of 10 peers carried a later artefact P11 had not
consumed.** Four new blockers, none of them P11's own reasoning — all four are peer facts P11 was
holding a superseded version of.

| id | Blocker | Status |
|---|---|---|
| **`B-21`** | **`om_data_remove` is INSTALLED on a real Odoo 19 database in this programme's estate** — unfiltered `DELETE FROM` across bank statements, payments, journal entries, journal items, reconciliations **and the audit trail**, committing per table and swallowing errors; **17 copies**, three rebranded *SMEsPlus Remove Data*, one locally extended for this project's Thai WHT certificates. `P06` classifies **`DESTRUCTIVE PATH VERIFIED`** / **`NO SERVER-SIDE AUTHORIZATION VERIFIED`** / **`REACHABLE — DEPLOYMENT VERIFIED`**, answering the question `P08-T0-08` left `D UNKNOWN`. A first-party remediation module states the path **has already been run** | **`CRITICAL` · OPEN** · new tolerance-zero **`T0-14`**. Deployment is a v19 database **not confirmed to be the SMEsPlus target** — bounded by `D-1`, not elided |
| **`B-22`** | **P11 carried a withdrawn figure.** `P11_PEER_INTAKE_DELTA_01.md` stated the cost-centre attribution route *"nets to zero"*. `P09` `S23` re-measured: the net is **`+3,595,851.11`, a sign-inverted CREDIT**; `TH-F-02` is a **277 M swing** across **169,954** records on **one of four** v19 builds | **HIGH · CORRECTED AT SOURCE** · the figure is repaired; the blocker records that P11 published it |
| **`B-23`** | **No `P09` mechanism claim may be treated as describing a running system.** One deployment runs v16, three run v19, the source is v18. Measurements unaffected. **Compounds `B-20`** — two peers independently say P11's event-to-GL matrix is written against an undeclared generation | **`CRITICAL` · OPEN** · routed to `D-1` |
| **`B-24`** | **Two peer vetoes bind P11's own method:** `P06 AASP-VETO-04` — no aggregating negatives across processes until each peer declares its addons-path population (P06 searched **791**; the full v18 distribution is **1752**); `P09 AAS+-VETO-04` — no P09 mechanism claim relied on until version-matched. **`P06` raises its veto against its own contribution to P11's registers** | **HIGH · OPEN** · accepted without dispute; honoured by construction in `CP-P11C13`; must survive into CORR2 where the aggregate registers live |

> ### `20 → 24` registered · **1 discharged (`B-01`) · 1 CLOSED (`B-18`) · 22 open.**
>
> **`B-21` is the second `CRITICAL` in the package and outranks `B-17` on impact.** Ranked by
> **reachability** the order differs — `P06` states both axes and instructs that they **not be
> collapsed**; P11 carries both rather than choosing.
>
> **None of the four was discovered by reasoning.** All four were sitting at SHAs P11 had already
> consumed, behind a one-line command.
