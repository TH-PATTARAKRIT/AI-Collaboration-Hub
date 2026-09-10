# 23 — OPTIONAL FUNCTION INVENTORY

# `8 DECLARED · 1 COMPLETE · 12.5 %`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Authority: **SMEs Core / Architecture specification act**, under `§13` of the ruling prompt
Boss: **SOLE FINAL APPROVER**

> **`§13`, verbatim: *"If evidence proves there are genuinely ZERO optional functions in an applicable
> area: publish the authority proving the empty set. **'None were declared' is NOT proof of zero.**"***
>
> **No empty set is claimed anywhere in this file.** The inventory is derived, its bound is declared,
> and where the evidence is thin the item is marked, not dropped.

---

## 1. WHAT MAKES A FUNCTION "OPTIONAL" HERE — the criterion, declared first

**A function is optional when a business inside the approved scope may operate without it, and its
absence changes which boundaries fire.** Three sources of optionality exist in this corpus, and each is
evidenced rather than assumed:

| Source | Mechanism | Evidence |
|---|---|---|
| **Business-nature routing** | `ND-01` **Supply Nature** is *"a resolved, immutable per-line fact"* deciding **make / buy / dropship**; *"one customer order may mix **stocked, manufactured and service** lines"* | a trading business never routes *make*; a service business never routes *stocked* |
| **Conditional applicability** | `XMC-H-15` / `XMC-H-16` — `N/A` today, **configuration-defeasible**, no independent check | `SA06-F-05`; `20_` §4 |
| **Absent object** | a capability the corpus routes to but whose object does not exist | `XMC-H-14`: *"the **Quality object itself is absent** — `0` blobs, two shapes, firing positive controls"* |

**Rejected as a source:** *"the reference estate ships it as a separate module."* **No module-install
evidence exists on the frozen tree**, and the one corpus reference to an optional module
(`SA_CORR3_06` L280 — *"a real database constraint exists, but only with an optional module installed"*)
is about the **reference estate**, not about SMEsPlus scope. **Recorded so a later reader does not
mistake it for a scope statement.**

---

## 2. DERIVATION AND ITS DECLARED BOUND

```
POPULATION : functions inside the approved Pre-Test scope that a conforming business may not use
UNIT       : optional function
PATTERN    : the 3 optionality sources above, applied across the 22 canonical scenarios X-01..X-22
             and the 17 declared boundary classes BC-01..BC-17
PATH SET   : STATE03_MIGRATION_FACTORY/**  at c91d5840  -- 779 files
AUTHORITY  : ND-01, 32A_, SA06-F-05, SA_CORR3_08, PT01 scenario register, BOSS-CORR1-01
```

> **Completeness bound, declared.** **No authored optional-function register exists in the corpus.**
> This inventory is derived from scenario and boundary evidence and is a **FLOOR of `8`**.
> **It is not proven exhaustive, and `§13` forbids treating the absence of a declaration as proof of
> zero.** Proving exhaustiveness requires a producing-side scope register that does not exist.
> **Recorded as `CORR2-OPT-01` — MODERATE.**

**One candidate was considered and excluded on evidence:** **lot / serial traceability.** The only
supporting text (*"Delivered quantity, date, **lot or serial**"*) is in `HX-02`, which is **off-baseline**
(`07_` §1). **`0` on-baseline evidence** was found in this path set. **It is excluded as unproven, not as
absent** — the distinction `§13` requires.

---

## 3. THE INVENTORY

| ID | Function | Reason optional | Enable condition | Configuration | Runtime path | Business owner | Disabled behaviour | Accounting effect | Inventory effect | Tenant / company effect | Evidence | Future gate | **Complete?** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **`OPT-01`** | **Manufacturing** (RM → WIP → FG) | Supply Nature may never route *make* | a product routes *make*; a manufacturing order exists | `CFG-12` routing; `CFG-08` overhead driver | `BC-02` → `BC-04` → `BC-05` | SMEs Core | `BC-02`, `BC-04` never fire; no WIP | WIP and absorption postings; **variance** | RM issue, FG receipt | company | `X-16`, `X-17` **GATED**; `SA_CORR3_08` `XMC-H-02`/`-04` | Build/Test | **NO** — `POH-D-02` **withheld**; veto limb `2` outstanding; **fixed-overhead elements have no injection path**; *"**no variance mechanism exists** — one of nine recognised"* |
| **`OPT-02`** | **Quality management** (incl. quality hold) | a business may not inspect | an inspection step is configured on a receipt or production route | `CFG-05` valuation mapping | `BC-14`; `XMC-H-15` | SMEs Core | `BC-14` never fires; stock is available on receipt | **`XMC-H-15` conditional** — none if hold is cost-neutral | hold / release blocks availability | company | `XMC-H-14`: **the Quality object is absent, `0` blobs**; `20_` §4 | FD Exit, then Build/Test | **NO** — **the object does not exist**, so no runtime path can be specified |
| **`OPT-03`** | **Dropship / MTO** | Supply Nature may never route *dropship* | a sales line routes *buy-to-order* | `CFG-12`; `CFG-09` approval gate | `BC-03` | SMEs Core | `BC-03` never fires; all supply from stock or make | via `BC-07` | no stock movement on the dropship leg | company | `SA_CORR3_08` `XMC-H-03`; `X-18` | FD Exit, then Build/Test | **NO** — the enabled path is a **control breach**: it *"bypasses the demand-approval gate every human-raised purchase must pass"*, and `CFG-09`'s mechanism is **absent** |
| **`OPT-04`** | **Service / Project performance** | a business may sell no services | a product of KIND `Service` exists | `CFG-01` KIND; `CFG-02`/`-03` Category | `BC-15` | SMEs Core | `BC-15` never fires | revenue / cost on assertion | **none** — a Service admits no movement | company | `XMC-H-17`; `32A_` `KCR-01`/`-05`, `ND-09-B` | FD Exit, then Build/Test | **NO** — *"for a service there is **no physical fact, only an assertion**, with no event record"*; the project derivation *"writes **three costed rows from one duration**, with two report surfaces reading different row sets"* |
| **`OPT-05`** | **Internal warehouse transfer** | a single-location business never transfers | a second internal location exists | **`CFG-05`** valuation-account mapping | `XMC-H-16` | Inventory | no internal movement; `XMC-H-16` never arises | **none if neutral; an ungoverned posting if not** | stock changes location, not quantity | **COMPANY.** Cross-company is `X-15`, **not this** | `SA06-F-05`; `SA_CORR3_08` §2.6; `20_` §4 (all `8` attributes) | Build/Test — `X-14` | **YES** — the only entry whose `13` attributes are all determinable from evidence |
| **`OPT-06`** | **Multi-company / multi-tenant operation** | a single-company business needs none | a second company or tenant exists | `CFG-06` tax boundary; `CFG-07` numbering | `X-15` | Architecture | one company; isolation questions do not arise | **cross-company statutory posting FORBIDDEN** (`BD-ACC-02`) | cross-company stock path **never traced** (`GAP-FS-07`) | **this is the tenant/company dimension itself** | `X-15`: *"this scenario **is** element `10`; **`0 of 8` isolation proofs**; **two** lock-defeat paths, the second leaving no record"* | Build/Test — `I` dimension | **NO** — `0 of 8` isolation proofs; **element `10` absent** |
| **`OPT-07`** | **Migration replay** | a greenfield deployment never replays | a migration batch is re-run | element `14` batch identity; element `15` idempotency | `BC-16` | Migration | cutover loads once; no replay | **undecidable** — see `25_` | **undecidable** — zero **iff** idempotent | company | `XMC-H-18`: **`14` and `15` `NOT SUPPLIABLE`**; `MF-03` **NOT DECIDABLE** (`25_`); `CORR1-F-03` | Build/Test — `X-22` | **NO** — both governing elements are **`ABSENT`**; *"a re-run can **duplicate an opening balance**"* |
| **`OPT-08`** | **Consumable handling** | a business may stock no consumables | a product of KIND `Consumable` exists | `CFG-01`; `CFG-02`/`-03` | `BC-05` | SMEs Core | no consumable lines | immediate expense at **receipt** — *or at issue* | **none if expensed at receipt** | company | `32A_` §3 Consumable row + its declared basis | FD Exit, then Build/Test | **NO** — `32A_` states its own dependency: *"**If Boss or Functional Design later determines that a Consumable is expensed at ISSUE rather than at RECEIPT**, it carries a pool until issue and **this row changes to all `PROCEED`**"* — **the expensing point is undetermined** |

---

## 4. TALLY

```
OPTIONAL FUNCTIONS DECLARED         8      (a FLOOR, not proven exhaustive -- SS2)
COMPLETE (all 13 attributes)        1      OPT-05
INCOMPLETE                          7      OPT-01, -02, -03, -04, -06, -07, -08
CHECK  1 + 7                        8      OK
CANDIDATES EXCLUDED ON EVIDENCE     1      lot / serial -- 0 on-baseline evidence, excluded as
                                           UNPROVEN, not as absent
EMPTY SETS CLAIMED                  0
```

**The `7` incomplete fail on the same axis, and it is not optionality.** In each case the function's
**enabled behaviour is not fully specified**: a withheld statutory election (`OPT-01`), an absent object
(`OPT-02`), an absent control (`OPT-03`), a missing event record (`OPT-04`), absent isolation proofs
(`OPT-06`), two absent elements (`OPT-07`), an undetermined expensing point (`OPT-08`).

> **`CORR2-OPT-02` — MATERIAL. Optionality is not the problem; the enabled path is.**
> Every one of the `7` would still be incomplete if the function were **mandatory**. **Declaring the
> inventory did not reveal seven optional-function gaps — it re-surfaced seven business-semantic gaps
> under a dimension that had not previously been measured.** All `7` are carried to `28_`, and
> `OPT-01`, `-02`, `-04`, `-06`, `-07` map onto existing FD blockers rather than adding new ones.

---

## 5. DOWNSTREAM CONTRACT — `§8`'s six elements

| | |
|---|---|
| **Named population** | `OPT-01`…`OPT-08`, floor declared |
| **Exact future gate** | **Build / Test** for `OPT-01`, `OPT-05`, `OPT-06`, `OPT-07`; **Functional Design Exit, then Build / Test** for `OPT-02`, `OPT-03`, `OPT-04`, `OPT-08`, whose enabled behaviour must first be specified |
| **Evidence contract** | with the function **enabled**, its boundaries fire and produce the stated accounting and inventory effects; with it **disabled**, they do not fire and **no partial artefact is left behind** |
| **Owner** | as the Business owner column |
| **Trigger** | first Build/Test cycle exercising the owning scenario |
| **Success criterion** | **both directions observed** — enabled produces the effect, disabled produces **nothing**. **The disabled case is the one that is normally skipped and is required here.** |

---

## 6. COVERAGE — CURRENT PHASE ONLY

| Measure | Denominator | Named | Numerator | **Coverage** | Floor | Phase status |
|---|---:|:-:|---:|---:|---:|---|
| Optional functions with a **complete declared contract** | `8` | ✔ | `1` | **`12.5 %`** | `96 %` | **`HOLD AT CURRENT PHASE`** |
| Optional functions with a **named future gate and evidence contract** | `8` | ✔ | `8` | **`100 %`** | `96 %` | **MEETS** — §5 |
| **Optional function reachability, measured** | `8` | ✔ | **`0`** | **`0 %`** | `96 %` | **`DEFERRED WITH VALID DOWNSTREAM CONTRACT`** |
| Empty-set claims made without authority | `0` | — | `0` | — | — | **MEETS** |

---

## 7. STATUS MOVEMENT

| Before (`09_`) | **After** |
|---|---|
| **`UNMEASURABLE — NO DECLARED INVENTORY`** | **`HOLD AT CURRENT PHASE` — `12.5 %`, floor `96 %`** |

> **The dimension is now measurable and fails badly.** That is a truer position than *"unmeasurable"*,
> and it is worse than the package looked before the inventory existed. **`§13` was worth executing
> precisely because it made the number appear.**

---

## 8. CHECKPOINT

> **Optional Function Inventory **DECLARED** — `8` functions, `13` attributes each · optionality
> criterion declared **before** the inventory, with `3` evidenced sources and `1` rejected source ·
> completeness declared a **FLOOR** (`CORR2-OPT-01`) · **`0` empty sets claimed** ·
> `1` candidate excluded as **UNPROVEN, not absent** · `1` complete, `7` incomplete ·
> **`CORR2-OPT-02`: all `7` would fail if the function were mandatory — the gap is the enabled path,
> not the optionality** · **`12.5 %` — HOLD.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the SOLE FINAL APPROVER.**
