# SA_CORR5_04 — `G5` CROSS-TENANT METERING AND BACKGROUND-PROCESS BOUNDARY INTEGRATION

## CP-SA-C5-40 — G5 EXECUTION BOUNDARY INTEGRATED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR5-ZERO-SME-CARRYFORWARD-001]`
Branch: `architecture/phase-sa-corr5-zero-sme-carryforward-closure-2026-09-09-001`
Workstream: **D** · Closes: **`G5`** — *"a Boss-approved cross-tenant metering pipeline and four
financial background processes are unintegrated with the execution-boundary invariant family"*
(`SA_CORR4_01` §9; `C4-01-F-03`, `-F-04`; `SA_CORR4_06` §4.5).
Boss: **SOLE FINAL APPROVER**

---

## 1. Population — re-measured, and larger than CORR4's

CORR4 measured `SAAS_CELL/22`–`/28`. **Two artefacts entered mainline after CORR4's frame** (`C5-B-05`):

| File | Date | Status | Contribution |
|---|---|---|---|
| `22` usage-based capacity and transparent billing | 2026-09-09 | `BOSS APPROVED DIRECTION` | the pipeline: Resource Governor → Capacity Meter → Entitlement Engine → Usage Statement; `UCE-01`…`-10` |
| `23` customer usage visibility | 2026-09-09 | same | tenant-facing dashboard obligations |
| `24` wallet protection and advance notification | 2026-09-09 | same | wallet states; principles 1–8 |
| `25` 30-day advance depletion notice | 2026-09-09 | same | forecast-based trigger |
| `26` prepaid before usage; notice is not credit | 2026-09-09 | same | pre-execution entitlement/capacity check; control flow |
| `27` low base subscription with prepaid usage | 2026-09-09 | same | deduction order; open items incl. *tax/accounting treatment of prepaid balances* |
| **`29` tenant resource governance & capacity work package** | **2026-09-09, `f151bb3f`** | **`BOSS AUTHORIZED FOR ARCHITECTURE DESIGN`** | **`TRG-01`…`TRG-18`** — *`TRG-01` tenant execution context mandatory for metered operations · `TRG-02` cross-tenant usage attribution prohibited · `TRG-07` historical usage evidence immutable/auditable after period closure · `TRG-10` heavy workloads may require pre-authorisation · `TRG-12` Tenant ≠ Cell ≠ Server ≠ Database Host*; WP-01…WP-08 deliverables named |
| `30` Standard → Enterprise mobility | 2026-09-09, `27717bde` | direction | out of scope here (no execution path) |

Cross-references to the execution-boundary family, re-measured over all eight (case-sensitive):
`MTI-29` **0** · `MTI-30` **0** · `CF-I-02` **0** · `MTI-31` **0**; positive control `tenant` fires in
`23`, `28`, `29` (case-sensitive) and additionally in `22` case-insensitively (`Tenant`). **`G5` reproduces — and `29` already states two of the invariants this file
needs (`TRG-01`, `TRG-02`) in the commercial family's own vocabulary, uncited by the execution-boundary
family.** Same shape as `C4-02-F-01`: both halves exist, neither cites the other.

> **`C5-04-F-01`.** The integration is therefore **bidirectional**: `MTI-29`/`MTI-30`/`CF-I-02` bind
> the pipeline; `TRG-01`/`TRG-02`/`TRG-07` bind the invariant family's reading of metering. This file
> is the join; it originates no new prohibition.

---

## 2. The rule that decides every row

`MTI-29` R2: *"A run that must cover several companies is an enumerated set of single-context
executions, each with its own identity and its own result."* Applied to tenants: **a platform service
that processes many tenants over time is not thereby in a shared execution context. It is a scheduler
of N single-tenant executions plus, separately, a platform-context aggregation over their results.**
The master prompt's warning is honoured by construction: shared context is never assumed from the fact
that one service touches many tenants.

Three contexts appear, and every step below names which it is in:

| Context | Who | Reads | Writes |
|---|---|---|---|
| **`T(i)`** — one tenant's execution | the service, running the i-th single-context execution | that tenant's metered evidence | that tenant's usage ledger, forecast, notice |
| **`P`** — platform context | the service, aggregating **results** | the N results, never tenant content | platform totals, cell headroom, the platform's own financial facts |
| **`CELL`** — infrastructure measurement | the Resource Governor | machine metrics | cell headroom state (`29` WP-06) — **not a tenant fact and never attributed to a tenant without `T(i)` metering** (`TRG-12`, `TRG-13`) |

---

## 3. The pipeline, step by step

| Step | Actor | Context | Idempotency identity (`E15-A1` form) | Isolation / aggregation rule |
|---|---|---|---|---|
| **Resource Governor** — governs placement, fair scheduling, protected mode | platform service principal (class 11) | `CELL` for headroom; **`T(i)`** for any per-tenant throttle or protected-mode state | (tenant, `PLATFORM` company `N/A`, domain=Governor, occurrence = decision instance) | a throttle is a per-tenant decision recorded in `T(i)`; **cell headroom is never divided among tenants by inference** (`TRG-03`, `TRG-13`) |
| **Capacity Meter** — measures consumption | same | **`T(i)` only** — one tenant per measurement window per execution | (tenant, `N/A`, domain=Meter, occurrence = (dimension, window)) | **`TRG-01`**: every metered operation carries its tenant execution context, resolved at the act it meters (propagated `CTX`, `SA_CORR5_02` class 11) — **never attributed after the fact from infrastructure counters** (`TRG-02`) |
| **Commercial Entitlement Engine** — envelope, thresholds, pre-authorisation | same | **`T(i)`** | (tenant, `N/A`, domain=Entitlement, occurrence = (envelope version, window)) | reads the tenant's subscription (`FR-SM-005`'s result) and the tenant's meter; the pre-execution check of `26` runs **inside the requesting act's context**, synchronously, and its decision is an event |
| **Usage Statement / Billing** — statement, wallet deduction, notice | billing service principal (class 13) | **`T(i)`** for the tenant's statement, ledger and notice; **`P`** for the platform's own revenue fact | (tenant, `N/A`, domain=Billing, occurrence = (charge class, period)) — a statement re-run for the same period is the **same** occurrence | **wallet deduction is a platform financial fact** (`SA_CORR5_02` class 13); the customer-visible copy is evidence, not the customer's accounting |
| **Platform aggregation** — Boss Cost-to-Serve dashboard, cell scale-out triggers | platform principal / service | **`P`** | (platform tenant, SMEsPlus company, domain=CostToServe, occurrence = (period)) | **input is the set of `T(i)` results**; no read of any tenant's records; **`TRG-02`** — a platform total that cannot be decomposed into its `T(i)` results is not evidence |

---

## 4. The four financial background processes, eleven attributes each

Existing work consumed: `MTI-29`/`-30` R2, `CF-I-02`, `MTI-31`, `MTI-32` (input snapshot), `MTI-38`,
`MTI-50`, `XMC-C-A6`/`A7`/`A8`/`A14`, `CF-I-03` `T4`, `CF-I-03R`, `SAAS_CELL/24`–`/27`, `/29`.

| Attribute | **BP-1 Wallet deduction** (base rental · measured usage · add-on · optional; `27` deduction order) | **BP-2 Forecast, threshold and 30-day notice** (`24`, `25`) | **BP-3 Pre-execution entitlement / capacity check** (`26` control flow; `29` WP-04) | **BP-4 Period counter reset with evidence preservation** (`24` principle 2; `TRG-08`, `-09`) |
|---|---|---|---|---|
| Scheduler / system actor | billing service principal, versioned; scheduled by the platform scheduler under a platform grant scoped to the four charge classes | same, scoped to *forecast/notify* | **not a scheduler** — invoked synchronously by the requesting act; executor = entitlement service; **authority = the requesting act's propagated `AUTH`** | billing service, scoped to *period close* |
| Tenant selection | **enumeration from the subscription register** — the set of active tenants at period start; each becomes one `T(i)`; the enumeration itself is a `P`-context event carrying the list | same, per forecast cadence | the tenant of the requesting act (propagated) | enumeration at period boundary |
| Company selection | `N/A` with reason: charges attach to the tenant (customer), not to a company inside it | `N/A`, same reason | `N/A` — capacity is tenant-level (`TRG-12`); **a company-scoped business act that triggers the check keeps its own company context; the check reads tenant capacity and writes nothing to the company** | `N/A` |
| One-at-a-time execution context | **one `T(i)` per execution**; `MTI-31`: run identity scoped to `T(i)`, no two concurrent deductions for one tenant | one `T(i)` per forecast | inside the act | one `T(i)` per reset |
| Isolation boundary | reads only `T(i)`'s meter and ledger; writes only `T(i)`'s ledger; **the platform revenue fact is written in `P` from the `T(i)` result, not from tenant data** | reads only `T(i)`'s ledger and burn; writes only `T(i)`'s notice | reads `T(i)` capacity; **returns allow / reserve / deny to the act**; writes a reservation in `T(i)` | writes `T(i)`'s counter epoch; **never touches `T(i)`'s evidence** |
| Idempotency identity | (tenant, `N/A`, Billing, occurrence = (charge class, period, source usage statement version)) → **a re-run deducts nothing twice** (`XMC-C-A6`); the deduction is an event; its reversal (credit) is a new event (`A8`) | (tenant, `N/A`, Forecast, occurrence = (forecast basis snapshot identity)) — `MTI-32`: the input snapshot travels with the result; a re-run over the same snapshot is the same forecast | (tenant, `N/A`, Entitlement, occurrence = the requesting act's **attempt identity** (`XMC-C-A14`)) — a retried request gets the **same** decision, and one reservation | (tenant, `N/A`, Billing, occurrence = (period)) |
| Retry behaviour | at-least-once scheduling with idempotent effect; a failed `T(i)` is retried **alone** — never the whole batch (`MTI-29`: each execution has its own result) | same | the act's retry re-presents the same attempt identity → same decision; **a reservation released by timeout is a new event, not an edit** (`29` WP-04 *Release Unused Reserve*) | same |
| Error containment | a failure in `T(i)` is recorded as `T(i)`'s non-execution (`MTI-30` pattern) and does not stop `T(j)`; the `P` aggregation **publishes population / processed / failed** beside its total (`CF-I-03` §3.11's rule) | same | **fail closed**: an unreachable entitlement service denies chargeable execution (`26` rule 3 *financially covered before execution*); non-chargeable execution is unaffected | a failed reset leaves the epoch unchanged and evented |
| Audit trail | every deduction an immutable `MTI-38`-shape event in `P` with the tenant as object **and** mirrored into `T(i)`'s customer-visible evidence (`23` drill-down; `TRG-07`) | every forecast and notice an event with its snapshot reference | every allow/reserve/deny an event under the act's `CTX`/`AUTH`; **denials are events, never silent** (`EP-P` rule) | the reset is an event carrying the closed period's final counters as before-values |
| Cross-tenant aggregation restriction | **prohibited inside any `T(i)`**; platform totals in `P` from results only (`TRG-02`) | prohibited; **no tenant's forecast uses another's burn** | prohibited; **cell headroom is a `CELL` fact and a tenant is never denied *because of another tenant's usage* without a `P`-context protected-mode decision that is itself evented** (`29` WP-05/06) | prohibited |
| Handoff to Accounting / Inventory | **To the platform's own Accounting** (SMEsPlus as a company): an ordinary `BD-ACC-01` emitting handoff — owning domain Billing, occurrence = deduction event, tenant = platform tenant, company = SMEsPlus operating company; **`HF-CTX-01`…`-11` apply**. **Tax/accounting treatment of prepaid balances: `HOLD / EVIDENCE REQUIRED`** (`27` open item; Thai statutory) — the *handoff shape* is specified, the *recognition policy* is not. **No handoff to the customer tenant's Accounting or Inventory** | none (a notice is not a financial fact) | **to the requesting act only**: the decision is a precondition carried as evidence (`HF-CTX-08`), not a business fact | none |

---

## 5. Reconciliation with the invariant family — clause by clause

| Invariant | Applied to the pipeline and BP-1…4 | Result |
|---|---|---|
| `MTI-29` R2 single-context execution, explicit operation-type context | every `T(i)` resolves one tenant and one **platform operation class** (*meter · entitle · deduct · forecast · notify · reset*) | **honoured** — the class set is originated here as the pipeline's operation classes and is subject to `CF-D-02`'s enumeration rule |
| `MTI-30` R2 deferred authority revalidated at release | each scheduled `T(i)` carries the billing service's platform grant and the tenant's subscription state; a suspended/terminated tenant → non-execution recorded (`FDS_TENANT` `BR-TEN-002`/`-003`) | **honoured** |
| `CF-I-02` operation-type context on every background execution | as `MTI-29` row | **honoured** |
| `MTI-31` run identity, mutual exclusion | per `T(i)` | **honoured** |
| `MTI-32` input snapshot | forecast and statement carry their snapshot | **honoured** |
| `MTI-38` event completeness | all four processes | **honoured** via `SA_CORR5_03` `AUD-C` |
| `CF-I-03` `T4` (deferred release revalidation as an input) | every `T(i)` release is a `T4` input | **honoured** |
| `TRG-01`, `-02`, `-07`, `-10` | as above | **honoured, and now cited from the invariant side** |
| `BD-ACC-01` on the platform's own books | BP-1 handoff | **honoured at shape; recognition policy `HOLD`** |
| Boss `00`/`01` — membership ≠ execution context | no step runs in more than one tenant; `P` reads results only | **honoured** |

**10 of 10 honoured at specification level; 0 exceptions created; 0 cross-tenant paths.**

## 6. Runtime-only obligations

`RT-G5-01` a re-run statement for a closed period deducts nothing · `RT-G5-02` a failed `T(i)` does not
stop `T(i+1)` and is reported in population/processed/failed · `RT-G5-03` a tenant's forecast is
unchanged when another tenant's burn changes (discriminating population) · `RT-G5-04` a pre-execution
check retried with the same attempt identity yields the same decision and one reservation ·
`RT-G5-05` platform total equals the sum of `T(i)` results to the unit (`TRG-02`) · `RT-G5-06` a
suspended tenant's scheduled deduction does not execute and the non-execution is recorded ·
`RT-G5-07` **synthetic injection**: one metered act with no tenant context → refused and counted.

## 7. What this file does not do

Define metering units, envelopes, thresholds, rates, reserve algorithms or grace rules — all **open by
Boss's own text** (`22` open items, `24`, `26`, `27`, `29` §7) and **not Phase SA gaps**: they are
commercial and Cost-to-Serve inputs gated by `29` §4's Pre-Pricing Evidence Gate · decide the
tax/accounting treatment of prepaid balances · build anything.

## 8. Residual

1. **The operation-class set for the pipeline is originated here** and falls under `CF-D-02`'s unruled
   enumeration closure. It is stated so the classes exist to bind controls to; it does not pre-empt the
   ruling.
2. **BP-3's synchronous placement** (inside the act) is a design position; an asynchronous
   reservation-first model is coherent. It was chosen because `26` rule 3 requires cover **before
   execution**, which an asynchronous check cannot guarantee.
3. **`29`'s WP deliverables (`TENANT_USAGE_LEDGER_CONTRACT.md` etc.) do not yet exist on any branch** —
   their names occur in exactly **1** of 3,620 paths, file `29` itself, which lists them. When authored they must cite this file and
   `MTI-29`; that is a **future-artefact obligation**, not a Phase SA gap.

## 9. Checkpoint

> ## `CP-SA-C5-40 — G5 EXECUTION BOUNDARY INTEGRATED`
> **8 Boss artefacts consumed (2 new to the frame) · 5 pipeline steps and 4 background processes ×
> 11 attributes · 10 of 10 invariants honoured · 0 cross-tenant paths · 7 runtime obligations ·
> 1 finding (`C5-04-F-01`) · prepaid-balance recognition policy `HOLD / EVIDENCE REQUIRED`.**

**Next autonomous action:** `CP-SA-C5-50` (`SA_CORR5_05`).

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
