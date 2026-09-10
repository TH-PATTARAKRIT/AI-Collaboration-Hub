# 22 — CONFIGURATION REACHABILITY POPULATION

# `12 DECLARED · 5 SEMANTICALLY COMPLETE · 41.7 %`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Authority: **SMEs Core / Architecture specification act**, under `§12` of the ruling prompt
Boss: **SOLE FINAL APPROVER**

> **The defect this file corrects:** `09_` measured Configuration Reachability as
> **`NOT MEASURABLE — no declared population`**. `§8` of the ruling: *"An undeclared population is NOT a
> valid deferral."* **The population is declared here. The runtime measurement remains downstream.**
>
> **What this file does NOT do:** it does not create configuration evidence, does not verify any path,
> and does not move any runtime result. **Declaring a population is a governance act, not coverage.**

---

## 1. WHAT IS BEING MEASURED, AND AT WHICH PHASE

| | Population — *what must be configuration-reachable* | Measurement — *whether it can be reached* |
|---|---|---|
| Class | **`S` / `D`** — specification | **`C` / `I`** — needs a built, configurable system |
| Exists at Pre-Test? | **MUST** | **CANNOT** |
| Measured here | **YES — §3** | **NO — deferred, §5** |

**Current-phase measure:** *does each configuration-sensitive feature carry a complete semantic
contract* — scope, enable condition, disable condition, owner, path, dependent semantics, expected
behaviour, and a named future verification gate?

---

## 2. DERIVATION AND ITS DECLARED BOUND

```
POPULATION : configuration-sensitive features inside the approved Pre-Test scope
UNIT       : configuration item (a setting whose value changes a business or accounting outcome)
PATTERN    : corpus sweep for configuration-bearing decisions and for explicit
             configuration-dependency / configuration-protection statements
PATH SET   : STATE03_MIGRATION_FACTORY/**  at c91d5840  -- 779 files
             (declared wider than 09_'s NEW_SESSION_2026_09_10/**, which was too narrow -- see 26_ SS2)
AUTHORITY  : BD-ACC-01/-02/-03A/-03B, CC-D-01, 32A_, B4, SA06-F-05, TC-10, L3, ND-01, SC-54
ANCHOR     : each item is tied to at least one of the 22 canonical scenarios X-01..X-22
```

> **Completeness bound, declared rather than claimed.** This inventory is **derived by a pattern sweep**,
> not read from an authored configuration register — **no such register exists in the corpus.**
> `§13`'s rule applies here too: *"None were declared is NOT proof of zero."* **This population is a
> FLOOR of `12`. It is not proven exhaustive**, and proving exhaustiveness requires a producing-side
> configuration design that does not exist (`SA_CORR4_00` §5: `FINAL_SOLUTION` holds `30` paths, **`0`
> outside `INVENTORY`**). **Recorded as `CORR2-CFG-01` — MODERATE.**

---

## 3. THE POPULATION

| ID | Function | Scope | Tenant | Company | Enable condition | Disable condition | Owner | Config path | Dependent semantics | Expected behaviour | Future runtime verification | Evidence | **Phase status** |
|---|---|---|:-:|:-:|---|---|---|---|---|---|---|---|---|
| **`CFG-01`** | **Product KIND** — admissibility | product | — | — | product created with a KIND | — | SMEs Core | product type; `6` values (Goods, Consumable, Service, Raw Material, WIP, Finished Goods) | governs which of {movement, closing position, cost object, cost pool, ordered layers} is admitted | **KIND is evaluated first and never overridden by CATEGORY** | Build/Test — `X-18` | `32A_` §1, §2 | **COMPLETE** |
| **`CFG-02`** | **Recognition mode** `Periodic \| Perpetual` | **Product Category** | — | — | Category assigned to a product | — | SMEs Core | `BD-ACC-03A`, **Product Category only** | `Perpetual` requires a **physical movement event**; `Periodic` a **closing stock position** | refusal codes `KCR-01`/`-02` where KIND cannot supply | Build/Test — `X-18`, `X-03` | `BD-ACC-03A`; `32A_` §3 | **COMPLETE** |
| **`CFG-03`** | **Costing method** `Standard \| Average \| FIFO` | **Product Category** | — | — | Category assigned | — | SMEs Core | `BD-ACC-03B`, **Product Category only** | `Standard` → cost object · `Average` → cost pool · `FIFO` → **ordered layers** | `KCR-03`/`-04`/`-05` where KIND cannot supply | Build/Test — `X-18` | `BD-ACC-03B`; `32A_` §3 | **COMPLETE** |
| **`CFG-04`** | **Over-receipt tolerance** `refuse \| accept-and-event` | **COMPANY** | — | **Y** | receipt quantity exceeds ordered | tolerance `0` | Boss election **`B4`** | company-scoped control default | governs `BC-17` goods receipt and `HX-05` three-way match | **ruled `refuse (0)`**; a tolerated over-receipt is **its own evented fact with a reason class** | Build/Test — `X-05` | `B4`; `CHC-13`; `SA_CORR3_08` `HX-05` | **COMPLETE** |
| **`CFG-05`** | **Valuation-account mapping by location / stock state** | **COMPANY** | — | **Y** | a location or stock state mapped to a distinct valuation account | all internal locations share one valuation account | Inventory | **NOT SPECIFIED** — the invariant is *"asserted, not configured"* | **one setting governs `XMC-H-15`, `XMC-H-16` and the `N/A` status of both** | internal→internal creates **no accounting consequence** | Build/Test — `X-14` | `SA06-F-05`; `SA_CORR3_08` §2.6; `20_` §4 | **INCOMPLETE** — path unspecified; **no independent check exists** |
| **`CFG-06`** | **Statutory tax grouping / security boundary** | **COMPANY** | — | **Y** | company configured with a tax regime | — | Tax / statutory | `BD-ACC-02` — replicated **per Company** | **substitution rule base** governs which rule applies | **cross-company statutory posting, offsetting, settlement, aggregation and filing authority are FORBIDDEN** | Build/Test — `X-15`, `BC-11` | `BD-ACC-02`; `SA_CORR3_08` `XMC-H-11` | **INCOMPLETE** — rule base is **`EVIDENCE-INSUFFICIENT`**, *"a black box in this evidence set"* |
| **`CFG-07`** | **Document numbering** | **COMPANY** | — | **Y** | sequence defined | — | Architecture | prefix / suffix / padding / increment, **per company, with date-range scoping** | document identity and audit reference | deterministic, gap-controlled numbering | Build/Test — `X-19` | `TC-10` `EVIDENCE_CONFIRMED` | **COMPLETE** |
| **`CFG-08`** | **Variable overhead allocation driver** | per element | — | — | a variable overhead element defined | element is fixed, not variable | SMEs Core | *"deliberately per-element and configurable — **correctly open, not a gap**"* | fixed driver is **normal-capacity machine hour**, *"from statute, not analysis preference"* | variable driver elected per element | Build/Test — `X-16` | `L3`; `POH-D-01` ruled | **INCOMPLETE** — **`POH-D-02` withheld**; *"a dated normal-capacity register per machine is a required object that **does not exist**"* |
| **`CFG-09`** | **Demand-approval gate** | **COMPANY** | — | **Y** | purchase demand raised by a human | — | Purchase | **NOT SPECIFIED** | every human-raised purchase must pass it | **`BC-03` bypasses it** — *"a document enters a module **below that module's own control floor**"* | Build/Test — `X-12`, `BC-03` | `SA_CORR3_08` `XMC-H-03`; `X-12` *"approval mechanism absent"* | **INCOMPLETE** — mechanism absent; bypass is a **control breach** |
| **`CFG-10`** | **Period lock / accounting-date guard** | **COMPANY** | — | **Y** | a period closed | — | Accounting | **NOT SPECIFIED — no object behind it** | governs `BC-12` Close → subledgers | accounting date **must not pass a lock** | Build/Test — `X-19` | `SA_CORR3_08` `XMC-H-12`; `X-19` | **INCOMPLETE** — **no accounting-period object exists**; date *"silently movable past a lock"*; the producing side is *"waiting for a lock source with no object behind it"* |
| **`CFG-11`** | **Reservation policy** | **COMPANY** | — | **Y** | stock reserved against demand | no reservation | Inventory | **NOT SPECIFIED** | governs `BC-01` and release on cancellation (`BC-13`) | a reservation is released only by a recorded act | Build/Test — `X-12`, `X-10` | `X-12`: *"an adjustment can **silently reduce a reservation**"* | **INCOMPLETE** — policy unspecified; **silent reduction is possible** |
| **`CFG-12`** | **Replenishment / Supply Nature routing** | product + company | — | **Y** | a deficit arises | — | SMEs Core | routing engine | decides **make / buy / dropship** → `BC-02`, `BC-03`, `BC-04` | Supply Nature is *"a **resolved, immutable per-line fact**, with its resolution inputs retained"* | Build/Test — `X-18` | `ND-01`; `SA_CORR3_08` `XMC-H-02` | **INCOMPLETE** — *"the Supply Nature rule deciding **make** is itself **undetermined**"*; `ND-01` **rejects** routing by product configuration and document type, and no replacement rule is specified |

---

## 4. EXPRESSLY NON-CONFIGURABLE — declared, because a negative needs an authority

**`§24`'s discipline applied in reverse: an item excluded from a configuration population needs a reason
with an authority, or the exclusion is unsupported.**

| ID | Item | Ruled non-configurable by | Why it matters |
|---|---|---|---|
| **`NC-01`** | **`KCR-EVT-01` / `KCR-EVT-02` emission** | `32A_` §4.2 / `M-1`…`M-6` (`SC-BD-07`): *"every firing emits an event; **the event's emission is not configurable**, only the outcome is"* | *"A configuration that could suppress `KCR-EVT-01` would turn a refusal into a **silent skip**"* — the exact defect `M-6` prevents |
| **`NC-02`** | **Foreign-currency remeasurement** | `BR-09`: *"this design does **not** treat remeasurement as optional or configuration-dependent, **unlike the reference system's unevidenced status** (`ADV-08`)"* | a deliberate divergence from the reference estate, recorded as such |
| **`NC-03`** | **Supply Nature routing basis** | `ND-01` §2.2: the reference estate *"routes by **product configuration** and document type; **`ND-01` rejects both**"* | the routing basis is **not** a configuration surface — but `CFG-12` records that **no replacement rule is specified**, so the rejection currently leaves a hole |
| **`NC-04`** | **Tamper-evidence on regulated document classes** | `AO-02`: *"a **default property** of regulated document classes, **not an administrator-remembered opt-in**"*, correcting the reference estate's opt-in mechanism | grounded in official Thai sources (`RG-03`, `RG-04`), not in the vendor mechanism |

**`4` exclusions, each with a named authority. `0` unsupported exclusions.**

---

## 5. DOWNSTREAM CONTRACT — `§8`'s requirement for a valid deferral

**A deferral is valid only with a named population, exact future gate, evidence contract, owner, trigger
and success criterion. All six, for the whole population:**

| | |
|---|---|
| **Named population** | `CFG-01`…`CFG-12` (§3), floor declared at §2 |
| **Exact future gate** | **Build / Test** for `CFG-01`…`CFG-04`, `CFG-07`; **Functional Design Exit then Build / Test** for `CFG-05`, `CFG-06`, `CFG-08`…`CFG-12`, whose paths must first be *specified* |
| **Evidence contract** | for each item: the configuration is **found, reached, selected, activated, persisted and applied** under the intended tenant/company context, and the dependent semantic behaves as the *Expected behaviour* column states |
| **Owner** | as the Owner column |
| **Trigger** | the first Build/Test cycle in which the owning scenario (`X-nn`) is exercised |
| **Success criterion** | the expected behaviour observed **and** the negative case observed — a configuration change that should alter behaviour does alter it, and one that should not, does not |

> **`CORR2-CFG-02` — MATERIAL.** `CFG-05`'s success criterion **cannot be met by observation alone**:
> `SA06-F-05` records that transfer neutrality is *"protected only by configuration; **no independent
> check exists**"*, and `R4-F-18` confirms it. **A downstream verification contract that requires an
> independent check must first cause one to exist.** Carried at `27_` (`ZT-04`) and `29_`.

---

## 6. COVERAGE — CURRENT PHASE ONLY

| Measure | Denominator | Named | Numerator | **Coverage** | Floor | Phase status |
|---|---:|:-:|---:|---:|---:|---|
| Configuration items with a **complete semantic contract** | `12` | ✔ | `5` | **`41.7 %`** | `96 %` | **`HOLD AT CURRENT PHASE`** |
| Configuration items with a **named future gate and evidence contract** | `12` | ✔ | `12` | **`100 %`** | `96 %` | **MEETS** — §5 |
| Non-configurable exclusions with a named authority | `4` | ✔ | `4` | **`100 %`** | `100 %` | **MEETS** |
| **Configuration reachability, measured** | `12` | ✔ | **`0`** | **`0 %`** | `96 %` | **`DEFERRED WITH VALID DOWNSTREAM CONTRACT`** |

```
COMPLETE   5   CFG-01, CFG-02, CFG-03, CFG-04, CFG-07
INCOMPLETE 7   CFG-05, CFG-06, CFG-08, CFG-09, CFG-10, CFG-11, CFG-12
CHECK      5 + 7 = 12   OK
```

**The `7` incomplete share one shape:** in every case the *setting* is known to matter and the *path or
the rule behind it* is not specified — `CFG-05` no path, `CFG-06` a black box, `CFG-08` a missing
register object, `CFG-09` an absent mechanism, `CFG-10` **no object at all**, `CFG-11` an unspecified
policy, `CFG-12` a rejected basis with no replacement. **These are not configuration gaps; they are
missing business semantics that happen to surface as configuration**, and `28_` carries all `7`.

---

## 7. STATUS MOVEMENT — stated exactly

| Before (`09_`) | **After** |
|---|---|
| **`UNMEASURABLE — INVALID POPULATION`** | **`HOLD AT CURRENT PHASE` — `41.7 %`, floor `96 %`** |

> **This is a governance improvement and a coverage failure, and they are different things.**
> The dimension can now be measured; it does not pass. **`0 %` of the improvement is a coverage gain.**

---

## 8. CHECKPOINT

> **Configuration Reachability Population **DECLARED** — `12` items, `13` attributes each, each anchored
> to a canonical scenario · completeness declared as a **FLOOR, not proven exhaustive** (`CORR2-CFG-01`) ·
> `5` complete · `7` incomplete, all `7` carried to `28_` as business semantics ·
> `4` non-configurable exclusions with named authorities, **`0` unsupported** ·
> downstream contract complete on all `6` required elements · **`CORR2-CFG-02`: one success criterion
> requires an independent check that does not exist** ·
> **`41.7 %` — HOLD. `0` runtime `PASS` invented.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the SOLE FINAL APPROVER.**
